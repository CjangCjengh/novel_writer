"""
Locale Generator - Uses LLM to automatically create new language support.
Generates a complete locale file by translating the English base (en.py)
into the target language, then writes it to locales/ and registers it.
"""
import os
import re
import json
import textwrap

from llm_client import get_client
from locales import SUPPORTED_LANGUAGES, load_locale


# Max retries for each batch translation
MAX_GENERATION_RETRIES = 3

# Path to the locales directory
LOCALES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "locales")


def _build_dict_literal(d: dict, indent: int = 4) -> str:
    """
    Convert a dict to a pretty-printed Python dict literal string.
    Handles nested dicts and lists of dicts properly.
    """
    lines = ["{"]
    prefix = " " * indent

    for key, value in d.items():
        if isinstance(value, dict):
            nested = _build_dict_literal(value, indent + 4)
            lines.append(f'{prefix}"{key}": {nested},')
        elif isinstance(value, list):
            # Lists of strings (e.g. genre keywords)
            items_repr = json.dumps(value, ensure_ascii=False)
            lines.append(f'{prefix}"{key}": {items_repr},')
        elif isinstance(value, str):
            # Escape backslashes and triple-quote strings with newlines
            escaped = value.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
            if "\n" in escaped or len(escaped) > 100:
                lines.append(f'{prefix}"{key}": """{escaped}""",')
            else:
                escaped = escaped.replace('"', '\\"')
                lines.append(f'{prefix}"{key}": "{escaped}",')
        else:
            lines.append(f'{prefix}"{key}": {repr(value)},')

    lines.append(" " * (indent - 4) + "}")
    return "\n".join(lines)


def _extract_python_dict(text: str) -> dict | None:
    """
    Extract a Python dict from LLM response text.
    Tries JSON parse first, then eval with safety restrictions.
    """
    # Try JSON parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try extracting from code blocks
    patterns = [
        r'```python\s*(.*?)\s*```',
        r'```json\s*(.*?)\s*```',
        r'```\s*(.*?)\s*```',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            content = match.group(1).strip()
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                pass

    # Last resort: try to find a JSON-like object in the text
    # Find the outermost { ... }
    brace_start = text.find("{")
    brace_end = text.rfind("}")
    if brace_start != -1 and brace_end > brace_start:
        candidate = text[brace_start:brace_end + 1]
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            pass

    return None


def _translate_batch(client, lang_name: str, lang_code: str,
                     section_name: str, source_dict: dict,
                     extra_instructions: str = "") -> dict:
    """
    Use LLM to translate one section (UI / PROMPTS / TEMPLATES) into the target language.

    Args:
        client: LLM client instance.
        lang_name: Human-readable language name (e.g. "French", "Français").
        lang_code: Language code (e.g. "fr").
        section_name: Which section we're translating ("UI", "PROMPTS", "TEMPLATES").
        source_dict: The English source dictionary to translate.
        extra_instructions: Additional context/instructions for the LLM.

    Returns:
        Translated dictionary.

    Raises:
        RuntimeError: If translation fails after max retries.
    """
    system_prompt = f"""You are a professional software localization expert specializing in {lang_name}.
Your task is to translate Python dictionary values from English into {lang_name}.

CRITICAL RULES:
1. Translate ONLY the values, NEVER change the keys.
2. Keep all {{placeholder}} format tokens exactly as they are (e.g. {{error}}, {{num}}, {{max}}).
3. Keep all emoji characters as they are.
4. Keep all special markers like \\n, \\t as they are.
5. For technical terms (LLM, API, OpenAI, JSON, Markdown, etc.), keep them as-is.
6. For strings that contain code-like content (file paths, commands), keep the code parts as-is.
7. The tone and style should feel natural in {lang_name}, not like a robotic translation.
8. If the language has special characteristics (honorifics, formality levels, etc.), use an appropriate register for a creative writing tool.
9. Output MUST be valid JSON. Use standard JSON escaping for special characters.
10. Translate ALL entries - do not skip any."""

    # Build source as JSON for clean round-tripping
    source_json = json.dumps(source_dict, ensure_ascii=False, indent=2)

    user_prompt = f"""Please translate the following {section_name} dictionary values from English into {lang_name} (language code: {lang_code}).

{extra_instructions}

Source dictionary (English):
```json
{source_json}
```

Output the translated dictionary as valid JSON. Include ALL keys from the source. Translate only the string values.
Output ONLY the JSON object, nothing else."""

    for attempt in range(MAX_GENERATION_RETRIES):
        response = client.chat(system_prompt, [{"role": "user", "content": user_prompt}])
        if not response:
            print(f"  ⚠️ Attempt {attempt + 1} returned empty response, retrying...")
            continue

        result = _extract_python_dict(response)
        if result:
            # Validate: check that we have a reasonable number of keys
            coverage = len(result) / max(len(source_dict), 1)
            if coverage >= 0.7:
                # Fill in any missing keys from source
                for key in source_dict:
                    if key not in result:
                        result[key] = source_dict[key]
                return result
            else:
                print(f"  ⚠️ Attempt {attempt + 1}: only {len(result)}/{len(source_dict)} keys translated, retrying...")
        else:
            print(f"  ⚠️ Attempt {attempt + 1}: failed to parse response as dict, retrying...")

    raise RuntimeError(
        f"Failed to translate {section_name} section after {MAX_GENERATION_RETRIES} attempts"
    )


def _generate_locale_code(lang_code: str, lang_name: str, native_name: str,
                          ui_dict: dict, prompts_dict: dict, templates_dict: dict) -> str:
    """
    Generate the complete Python source code for a locale file.
    """
    # Build a well-formatted Python file
    lines = []
    lines.append(f'"""')
    lines.append(f'{native_name} ({lang_name}) locale - Auto-generated by locale_generator.py')
    lines.append(f'"""')
    lines.append(f'from locales.en import PROMPTS as _BASE_PROMPTS, TEMPLATES as _BASE_TEMPLATES')
    lines.append(f'')

    # UI section
    lines.append(f'# {"=" * 60}')
    lines.append(f'# UI: User interface strings')
    lines.append(f'# {"=" * 60}')
    lines.append(f'UI = {_build_dict_literal(ui_dict)}')
    lines.append(f'')

    # PROMPTS section - inherit from base and override
    lines.append(f'# {"=" * 60}')
    lines.append(f'# PROMPTS: LLM prompt templates')
    lines.append(f'# {"=" * 60}')
    lines.append(f'PROMPTS = dict(_BASE_PROMPTS)')
    lines.append(f'PROMPTS.update({_build_dict_literal(prompts_dict)})')
    lines.append(f'')

    # TEMPLATES section - inherit from base and override
    lines.append(f'# {"=" * 60}')
    lines.append(f'# TEMPLATES: Markdown templates')
    lines.append(f'# {"=" * 60}')
    lines.append(f'TEMPLATES = dict(_BASE_TEMPLATES)')
    lines.append(f'TEMPLATES.update({_build_dict_literal(templates_dict)})')
    lines.append(f'')

    return "\n".join(lines)


def generate_new_locale(lang_name: str, native_name: str, lang_code: str) -> str:
    """
    Generate a new locale file for the specified language using LLM translation.

    This is the main entry point. It:
    1. Loads the English base locale
    2. Translates UI, PROMPTS, and TEMPLATES in batches
    3. Writes the generated .py file to locales/
    4. Registers the new language in SUPPORTED_LANGUAGES

    Args:
        lang_name: English name of the language (e.g. "French").
        native_name: Name in the target language (e.g. "Français").
        lang_code: Short code for the language (e.g. "fr").

    Returns:
        Path to the generated locale file.
    """
    client = get_client()

    # Load English base
    en = load_locale("en")
    en_ui = en.UI
    en_prompts = en.PROMPTS
    en_templates = en.TEMPLATES

    print(f"\n🌐 Generating {native_name} ({lang_name}) locale...")
    print(f"   Language code: {lang_code}")
    print(f"   Total entries: UI={len(en_ui)}, PROMPTS={len(en_prompts)}, TEMPLATES={len(en_templates)}")

    # Batch 1: UI strings
    print(f"\n   📋 [1/3] Translating UI strings ({len(en_ui)} entries)...")
    ui_dict = _translate_batch(
        client, lang_name, lang_code, "UI", en_ui,
        extra_instructions="These are user interface strings for a novel writing tool. Keep them concise and natural."
    )
    print(f"   ✅ UI: {len(ui_dict)} entries translated")

    # Batch 2: PROMPTS (these are longer and more complex)
    print(f"\n   📋 [2/3] Translating PROMPTS ({len(en_prompts)} entries)...")
    prompts_dict = _translate_batch(
        client, lang_name, lang_code, "PROMPTS", en_prompts,
        extra_instructions=textwrap.dedent("""
        These are prompt templates sent to an AI model. Important notes:
        - The prompts must guide the AI to respond IN THE TARGET LANGUAGE.
        - Keep all {placeholder} tokens exactly as they are.
        - Keep all JSON template structures (with {{ and }}) exactly as they are.
        - 'genre_fantasy_keywords' and 'genre_scifi_keywords' should contain genre keywords
          that are common in the target language's literary tradition.
        - System prompts should maintain a professional but friendly tone.
        """).strip()
    )
    print(f"   ✅ PROMPTS: {len(prompts_dict)} entries translated")

    # Batch 3: TEMPLATES (Markdown templates)
    print(f"\n   📋 [3/3] Translating TEMPLATES ({len(en_templates)} entries)...")
    templates_dict = _translate_batch(
        client, lang_name, lang_code, "TEMPLATES", en_templates,
        extra_instructions=textwrap.dedent("""
        These are Markdown templates for generated project files. Important notes:
        - Keep all Markdown formatting (headers, tables, checkboxes, code blocks).
        - Keep all {placeholder} tokens exactly as they are.
        - Keep the directory structure code block in ASCII (just translate the comments).
        - Translate table headers and content descriptions.
        """).strip()
    )
    print(f"   ✅ TEMPLATES: {len(templates_dict)} entries translated")

    # Generate source code
    print(f"\n   📝 Generating locale file...")
    source_code = _generate_locale_code(
        lang_code, lang_name, native_name,
        ui_dict, prompts_dict, templates_dict
    )

    # Write to file
    file_path = os.path.join(LOCALES_DIR, f"{lang_code}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(source_code)
    print(f"   ✅ Written: {file_path}")

    # Register in SUPPORTED_LANGUAGES
    SUPPORTED_LANGUAGES[lang_code] = (native_name, lang_name)
    print(f"   ✅ Registered: {lang_code} → {native_name} ({lang_name})")

    # Verify by loading
    try:
        mod = load_locale(lang_code)
        assert hasattr(mod, "UI") and hasattr(mod, "PROMPTS") and hasattr(mod, "TEMPLATES")
        print(f"   ✅ Verification passed: UI={len(mod.UI)}, PROMPTS={len(mod.PROMPTS)}, TEMPLATES={len(mod.TEMPLATES)}")
    except Exception as e:
        print(f"   ⚠️ Verification warning: {e}")
        print(f"   The file was written but may need manual review.")

    print(f"\n🎉 {native_name} ({lang_name}) locale generated successfully!")
    return file_path


def interactive_add_language() -> str | None:
    """
    Interactive flow for adding a new language via the terminal.
    Asks the user for language details, then generates the locale file.

    Returns:
        The language code of the newly created locale, or None if cancelled.
    """
    print("\n" + "=" * 60)
    print("🌐 Add New Language Support")
    print("=" * 60)

    print("\nCurrently supported languages:")
    for code, (native, english) in SUPPORTED_LANGUAGES.items():
        print(f"  {code:8s} → {native} ({english})")

    print("\nPlease provide the following information for the new language:")

    # Get language name in English
    lang_name = input("\n  English name (e.g. 'French', 'Arabic'): ").strip()
    if not lang_name:
        print("  Cancelled.")
        return None

    # Get native name
    native_name = input(f"  Native name (e.g. 'Français', 'العربية'): ").strip()
    if not native_name:
        native_name = lang_name

    # Get language code
    suggested_code = lang_name[:2].lower()
    lang_code = input(f"  Language code (e.g. 'fr', 'ar') [default: {suggested_code}]: ").strip()
    if not lang_code:
        lang_code = suggested_code

    # Sanitize code
    lang_code = re.sub(r'[^a-z0-9_]', '_', lang_code.lower())

    # Check if already exists
    if lang_code in SUPPORTED_LANGUAGES:
        existing = SUPPORTED_LANGUAGES[lang_code]
        print(f"\n  ⚠️ Language code '{lang_code}' already exists: {existing[0]} ({existing[1]})")
        overwrite = input("  Overwrite? (y/n): ").strip().lower()
        if overwrite != "y":
            print("  Cancelled.")
            return None

    # Check if file already exists
    file_path = os.path.join(LOCALES_DIR, f"{lang_code}.py")
    if os.path.exists(file_path):
        print(f"\n  ⚠️ File locales/{lang_code}.py already exists.")
        overwrite = input("  Overwrite? (y/n): ").strip().lower()
        if overwrite != "y":
            print("  Cancelled.")
            return None

    # Confirm
    print(f"\n  Summary:")
    print(f"    English name : {lang_name}")
    print(f"    Native name  : {native_name}")
    print(f"    Language code : {lang_code}")
    print(f"    File path    : locales/{lang_code}.py")

    confirm = input(f"\n  Proceed with generation? (y/n): ").strip().lower()
    if confirm != "y":
        print("  Cancelled.")
        return None

    # Generate!
    try:
        generate_new_locale(lang_name, native_name, lang_code)
        return lang_code
    except Exception as e:
        print(f"\n  ❌ Generation failed: {e}")
        import traceback
        traceback.print_exc()
        return None
