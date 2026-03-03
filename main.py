#!/usr/bin/env python3
"""
📖 Novel Agent Workflow - Main Entry Point
An AI-powered automatic novel writing system with i18n support.
"""
import sys
import os

# Ensure project directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from locales import SUPPORTED_LANGUAGES, load_locale, get_locale
from llm_client import get_client, get_available_backends
from utils import multiline_input, setup_readline
from workflow import NovelWorkflow

# Configure readline for proper UTF-8 handling (fixes CJK backspace issues)
setup_readline()


def select_language() -> str:
    """
    Let the user select the language for the novel.
    This determines all UI text, prompts, and templates.
    The language menu itself is always displayed in each language's native name.
    Includes an option to add a new language via LLM generation.
    """
    print("\n🌐 Select language / 选择语言 / 言語選択:")
    lang_codes = list(SUPPORTED_LANGUAGES.keys())
    for i, code in enumerate(lang_codes, 1):
        native_name, english_name = SUPPORTED_LANGUAGES[code]
        print(f"  {i}. {native_name} ({english_name})")

    # Extra option: add a new language
    new_lang_option = len(lang_codes) + 1
    print(f"  {new_lang_option}. ➕ Add new language / 添加新语言 / 新しい言語を追加")

    while True:
        choice = input(f"\n👤 Enter choice / 输入选择 (1-{new_lang_option}): ").strip()
        if not choice.isdigit():
            print(f"Invalid / 无效, please enter 1-{new_lang_option}")
            continue
        choice_num = int(choice)
        if choice_num == new_lang_option:
            # Add new language - need LLM client first
            new_code = _add_new_language_flow()
            if new_code:
                # Reload locale list and use the new language
                load_locale(new_code)
                config.LANGUAGE = new_code
                native_name, english_name = SUPPORTED_LANGUAGES[new_code]
                print(f"  ✅ {native_name} ({english_name})")
                return new_code
            else:
                # User cancelled, re-display menu
                return select_language()
        elif 1 <= choice_num <= len(lang_codes):
            selected_code = lang_codes[choice_num - 1]
            break
        else:
            print(f"Invalid / 无效, please enter 1-{new_lang_option}")

    # Load the selected locale
    load_locale(selected_code)
    config.LANGUAGE = selected_code

    native_name, english_name = SUPPORTED_LANGUAGES[selected_code]
    print(f"  ✅ {native_name} ({english_name})")
    return selected_code


def _add_new_language_flow() -> str | None:
    """
    Flow for adding a new language. This requires the LLM client to be
    initialized first, so we do a mini API setup before locale generation.
    Returns the new language code, or None if cancelled.
    """
    print("\n" + "=" * 60)
    print("➕ To generate a new language, we need to use the LLM first.")
    print("   Please set up the API connection temporarily.")
    print("=" * 60)

    # Temporarily load English for the API setup UI
    load_locale("en")

    # Quick API mode selection (simplified, using English only)
    available = get_available_backends()
    if not available:
        print("\n❌ No LLM backend available!")
        print("   Please ensure llm_openai.py or llm_local.py exists.")
        return None

    if len(available) == 1:
        api_mode = available[0]
        print(f"\n  Auto-selected: {api_mode}")
    else:
        print("\n🔌 Select API mode for language generation:")
        for i, mode in enumerate(available, 1):
            print(f"  {i}. {mode}")
        while True:
            c = input(f"\n👤 Choice (1-{len(available)}): ").strip()
            if c.isdigit() and 1 <= int(c) <= len(available):
                api_mode = available[int(c) - 1]
                break
            print(f"Invalid, enter 1-{len(available)}")

    # Set up API config if needed
    if api_mode == "openai" and not config.OPENAI_API_KEY:
        key = input("Enter OpenAI API Key: ").strip()
        if not key:
            print("API Key required. Cancelled.")
            return None
        config.OPENAI_API_KEY = key
        base_url = input(f"API Base URL (Enter for default: {config.OPENAI_BASE_URL}): ").strip()
        if base_url:
            config.OPENAI_BASE_URL = base_url
        model = input(f"Model name (Enter for default: {config.OPENAI_MODEL}): ").strip()
        if model:
            config.OPENAI_MODEL = model

    if api_mode == "local" and not config.LOCAL_API_URL:
        url = input("Enter local API URL: ").strip()
        if not url:
            print("URL required. Cancelled.")
            return None
        config.LOCAL_API_URL = url
        key = input("Enter API Key (Enter to skip): ").strip()
        if key:
            config.LOCAL_API_KEY = key
        wsid = input("Enter WSID (Enter to skip): ").strip()
        if wsid:
            config.LOCAL_WSID = wsid
        marker = input("Enter model marker (Enter to skip): ").strip()
        if marker:
            config.LOCAL_MODEL_MARKER = marker

    config.API_MODE = api_mode

    # Initialize client
    try:
        from llm_client import get_client
        get_client(api_mode)
    except Exception as e:
        print(f"\n❌ Failed to initialize LLM client: {e}")
        return None

    # Now run the interactive locale generator
    from locale_generator import interactive_add_language
    return interactive_add_language()


def select_api_mode() -> str:
    """Let the user select the API mode, auto-detecting available backends."""
    ui = get_locale().UI
    available = get_available_backends()

    if not available:
        print(ui["no_backend"])
        print(ui["no_backend_hint"])
        sys.exit(1)

    print(ui["select_api_mode"])
    options = []
    if "openai" in available:
        options.append(("openai", ui["api_openai_desc"]))
    if "local" in available:
        options.append(("local", ui["api_local_desc"]))

    for i, (_, desc) in enumerate(options, 1):
        print(f"  {i}. {desc}")

    # Auto-select if only one backend available
    if len(options) == 1:
        mode = options[0][0]
        print(ui["auto_selected"].format(desc=options[0][1]))
    else:
        while True:
            choice = input(ui["input_choice"].format(max=len(options))).strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                mode = options[int(choice) - 1][0]
                break
            print(ui["invalid_choice"].format(max=len(options)))

    # OpenAI mode: check API Key
    if mode == "openai" and not config.OPENAI_API_KEY:
        key = input(ui["input_openai_key"]).strip()
        if not key:
            print(ui["api_key_empty"])
            sys.exit(1)
        config.OPENAI_API_KEY = key

        base_url = input(ui["input_base_url"].format(default=config.OPENAI_BASE_URL)).strip()
        if base_url:
            config.OPENAI_BASE_URL = base_url

        model = input(ui["input_model"].format(default=config.OPENAI_MODEL)).strip()
        if model:
            config.OPENAI_MODEL = model

    # Local mode: check API URL
    if mode == "local" and not config.LOCAL_API_URL:
        url = input(ui["input_local_url"]).strip()
        if not url:
            print(ui["api_url_empty"])
            sys.exit(1)
        config.LOCAL_API_URL = url

        key = input(ui["input_api_key"]).strip()
        if key:
            config.LOCAL_API_KEY = key

        wsid = input(ui["input_wsid"]).strip()
        if wsid:
            config.LOCAL_WSID = wsid

        marker = input(ui["input_model_marker"]).strip()
        if marker:
            config.LOCAL_MODEL_MARKER = marker

    return mode


def scan_existing_projects() -> list[str]:
    """Scan the output directory for existing novel projects."""
    base_dir = config.OUTPUT_BASE_DIR
    if not os.path.isabs(base_dir):
        base_dir = os.path.join(os.path.dirname(__file__) or ".", base_dir)
    if not os.path.isdir(base_dir):
        return []
    projects = []
    for name in sorted(os.listdir(base_dir)):
        project_path = os.path.join(base_dir, name)
        if os.path.isdir(project_path):
            # Only list valid projects containing plan.json, meta/ or plot/
            has_plan = os.path.exists(os.path.join(project_path, "plan.json"))
            has_meta = os.path.isdir(os.path.join(project_path, "meta"))
            has_plot = os.path.isdir(os.path.join(project_path, "plot"))
            if has_plan or has_meta or has_plot:
                # Collect project status info
                chapters_dir = os.path.join(project_path, "chapters")
                chapter_count = 0
                if os.path.isdir(chapters_dir):
                    chapter_count = len([f for f in os.listdir(chapters_dir) if f.endswith(".txt")])
                projects.append((name, chapter_count, has_plan, has_meta, has_plot))
    return projects


def select_existing_project(ui: dict) -> str:
    """
    Scan existing projects and let user select one from a list.
    Falls back to manual input if no projects are found.
    Returns the selected project name.
    """
    projects = scan_existing_projects()
    if not projects:
        print(ui["no_existing_projects"])
        novel_name = input(ui["input_novel_name"]).strip()
        return novel_name if novel_name else "my_novel"

    print(ui["scan_projects_header"])
    for i, (name, ch_count, has_plan, has_meta, has_plot) in enumerate(projects, 1):
        # Build status labels
        status_parts = []
        if ch_count > 0:
            status_parts.append(ui["project_status_chapters"].format(count=ch_count))
        if has_plan:
            status_parts.append(ui["project_status_plan"])
        if has_meta:
            status_parts.append(ui["project_status_meta"])
        if has_plot:
            status_parts.append(ui["project_status_plot"])
        status = ", ".join(status_parts) if status_parts else ""
        print(f"  {i}. 📖 {name}  [{status}]")

    # Extra option: manual input
    manual_option = len(projects) + 1
    print(f"  {manual_option}. ✏️  {ui['or_input_manually']}")

    while True:
        choice = input(ui["select_project_prompt"].format(max=manual_option)).strip()
        if not choice.isdigit():
            print(ui["invalid_choice"].format(max=manual_option))
            continue
        choice_num = int(choice)
        if 1 <= choice_num <= len(projects):
            selected_name = projects[choice_num - 1][0]
            print(f"  ✅ {selected_name}")
            return selected_name
        elif choice_num == manual_option:
            novel_name = input(ui["input_novel_name"]).strip()
            return novel_name if novel_name else "my_novel"
        else:
            print(ui["invalid_choice"].format(max=manual_option))


def run_single_novel(ui: dict, choice: str, novel_name: str):
    """Run a workflow for a single novel."""
    # Initialize project directories for this novel
    config.setup_project_dirs(novel_name)

    workflow = NovelWorkflow()

    if choice == "1":
        workflow.run_full()
    elif choice == "2":
        workflow.resume()
    elif choice == "3":
        workflow.phase_planning()
    elif choice == "4":
        workflow.phase_worldbuilding()
    elif choice == "5":
        workflow.phase_master_outline()
        volume = input(ui["input_volume_num"]).strip()
        if volume.isdigit():
            workflow.phase_volume_outline(int(volume))
    elif choice == "6":
        start = input(ui["input_start_chapter"]).strip()
        start_ch = int(start) if start.isdigit() else 1
        end = input(ui["input_end_chapter"]).strip()
        end_ch = int(end) if end.isdigit() else None
        workflow.phase_writing(start_chapter=start_ch, end_chapter=end_ch)


def run_batch_novels(ui: dict):
    """Run batch mode: generate multiple novels sequentially."""
    print(ui["batch_input_names"])
    raw = input(ui["user_prefix"] if "user_prefix" in ui else "👤 ").strip()
    if not raw:
        print(ui["batch_empty"])
        return

    novel_names = [n.strip() for n in raw.split(",") if n.strip()]
    if not novel_names:
        print(ui["batch_empty"])
        return

    # Select sub-operation for each novel
    print(ui["batch_select_op"])
    print(ui["op_full"])
    print(ui["op_resume"])

    while True:
        sub_choice = input(ui["input_choice"].format(max=2)).strip()
        if sub_choice in ["1", "2"]:
            break
        print(ui["invalid_choice"].format(max=2))

    total = len(novel_names)
    print(ui["batch_start"].format(total=total, names=", ".join(novel_names)))

    for idx, name in enumerate(novel_names, 1):
        print(f"\n{'=' * 60}")
        print(ui["batch_progress"].format(current=idx, total=total, name=name))
        print("=" * 60)

        try:
            config.setup_project_dirs(name)
            workflow = NovelWorkflow()
            if sub_choice == "1":
                workflow.run_full()
            elif sub_choice == "2":
                workflow.resume()

            print(ui["batch_novel_done"].format(name=name))

        except KeyboardInterrupt:
            print(ui["batch_interrupted"].format(name=name, remaining=total - idx))
            resume = input(ui["batch_continue_prompt"]).strip().lower()
            if resume not in ["y", "yes"]:
                print(ui["batch_stopped"])
                return
        except Exception as e:
            print(ui["batch_novel_error"].format(name=name, error=e))
            import traceback
            traceback.print_exc()
            # Ask whether to continue with remaining novels
            if idx < total:
                cont = input(ui["batch_continue_prompt"]).strip().lower()
                if cont not in ["y", "yes"]:
                    print(ui["batch_stopped"])
                    return

    print(ui["batch_all_done"].format(total=total))


def main():
    """Main function."""
    print("=" * 60)
    # Pre-locale welcome (always English)
    print("📖 Novel Agent Workflow v1.0")
    print("   AI-Powered Novel Writing System")
    print("=" * 60)

    # Step 0: Language selection (before any locale-dependent text)
    select_language()

    # Now we have locale loaded, get UI strings
    ui = get_locale().UI

    # Step 1: Select API mode
    api_mode = select_api_mode()
    config.API_MODE = api_mode

    # Step 2: Initialize LLM client
    client = get_client(api_mode)

    # Notify if lazy mode is enabled
    if config.LAZY_MODE:
        print(ui["lazy_mode_enabled"])

    # Step 3: Select operation
    print(ui["select_operation"])
    print(ui["op_full"])
    print(ui["op_resume"])
    print(ui["op_planning"])
    print(ui["op_worldbuilding"])
    print(ui["op_outline"])
    print(ui["op_writing"])
    print(ui["op_batch"])

    while True:
        choice = input(ui["input_op_choice"]).strip()
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            break
        print(ui["invalid_op"])

    try:
        if choice == "7":
            # Batch mode: multiple novels
            run_batch_novels(ui)
        else:
            # Single novel mode
            print(ui["project_setup"])
            # For "resume" and "writing only", auto-list existing projects for selection
            if choice in ["2", "6"]:
                novel_name = select_existing_project(ui)
            else:
                novel_name = input(ui["input_novel_name"]).strip()
                if not novel_name:
                    novel_name = "my_novel"
            run_single_novel(ui, choice, novel_name)

    except KeyboardInterrupt:
        print(ui["interrupted"])
    except Exception as e:
        print(ui["error_occurred"].format(error=e))
        import traceback
        traceback.print_exc()

    print(ui["goodbye"])


if __name__ == "__main__":
    main()
