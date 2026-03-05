"""
Prompt templates module - Bridge to locale-based prompts.
All agents should access prompts through this module for consistency.
"""
from locales import get_locale


def get_prompts() -> dict:
    """Get the PROMPTS dictionary from the currently loaded locale."""
    return get_locale().PROMPTS


def get_templates() -> dict:
    """Get the TEMPLATES dictionary from the currently loaded locale."""
    return get_locale().TEMPLATES


# --- Language enforcement ---
def get_language_instruction() -> str:
    """Generate a mandatory language instruction based on config.LANGUAGE.
    Reads the localised 'language_instruction' template from the current locale's
    PROMPTS dict and formats it with {native_name} and {english_name}.
    Returns empty string if language info is unavailable.
    """
    import config as _cfg
    from locales import SUPPORTED_LANGUAGES
    lang_code = _cfg.LANGUAGE
    lang_info = SUPPORTED_LANGUAGES.get(lang_code)
    if not lang_info:
        return ""
    native_name, english_name = lang_info
    template = get_prompts().get("language_instruction", "")
    if not template:
        return ""
    return "\n\n" + template.format(native_name=native_name, english_name=english_name)


def _with_lang(prompt: str) -> str:
    """Append the language enforcement instruction to a system prompt."""
    lang_inst = get_language_instruction()
    if lang_inst:
        return prompt + lang_inst
    return prompt


# Convenience accessors for commonly used prompts
def planner_system() -> str:
    return _with_lang(get_prompts()["planner_system"])


def planner_first_question() -> str:
    return get_prompts()["planner_first_question"]


def planner_check_enough(**kwargs) -> str:
    return get_prompts()["planner_check_enough"].format(**kwargs)


def planner_summarize() -> str:
    return get_prompts()["planner_summarize"]


# --- Continue from existing chapters ---
def planner_continue_system() -> str:
    return _with_lang(get_prompts()["planner_continue_system"])


def planner_continue_first_question(**kwargs) -> str:
    return get_prompts()["planner_continue_first_question"].format(**kwargs)


def planner_continue_summarize(**kwargs) -> str:
    return get_prompts()["planner_continue_summarize"].format(**kwargs)


def chapter_summary_prompt(**kwargs) -> str:
    return get_prompts()["chapter_summary_prompt"].format(**kwargs)


def master_outline_continue_prompt(**kwargs) -> str:
    return get_prompts()["master_outline_continue_prompt"].format(**kwargs)


def outline_system() -> str:
    return _with_lang(get_prompts()["outline_system"])


def volume_outline_system() -> str:
    return _with_lang(get_prompts()["volume_outline_system"])


def worldbuilding_system() -> str:
    return _with_lang(get_prompts()["worldbuilding_system"])


def character_system() -> str:
    return _with_lang(get_prompts()["character_system"])


def writer_system(**kwargs) -> str:
    return _with_lang(get_prompts()["writer_system"].format(**kwargs))


def writer_chapter_prompt(**kwargs) -> str:
    return get_prompts()["writer_chapter_prompt"].format(**kwargs)


def post_write_system() -> str:
    return _with_lang(get_prompts()["post_write_system"])


def style_guide_system() -> str:
    return _with_lang(get_prompts()["style_guide_system"])


# --- Feature #1: Multi-draft outline ---
def outline_merge_prompt(**kwargs) -> str:
    return get_prompts()["outline_merge_prompt"].format(**kwargs)


# --- Feature #2: Parallel quality review ---
def consistency_reviewer_system() -> str:
    return _with_lang(get_prompts()["consistency_reviewer_system"])


def style_reviewer_system() -> str:
    return _with_lang(get_prompts()["style_reviewer_system"])


def foreshadowing_reviewer_system() -> str:
    return _with_lang(get_prompts()["foreshadowing_reviewer_system"])


def review_chapter_prompt(**kwargs) -> str:
    return get_prompts()["review_chapter_prompt"].format(**kwargs)


# --- Quote style helper ---
def get_quote_style_instruction() -> str:
    """Generate a quote style instruction string based on config.QUOTE_STYLE and config.INNER_QUOTE_STYLE.
    Reads instruction text from the current locale's UI dict for proper i18n."""
    import config as _cfg
    from locales import get_locale
    ui = get_locale().UI
    parts = []

    # Dialogue quote style
    style = _cfg.QUOTE_STYLE
    if style != "auto":
        key = f"quote_rule_dialogue_{style}"
        d = ui.get(key, "")
        if d:
            parts.append(d)

    # Inner thought / internal monologue quote style
    inner = _cfg.INNER_QUOTE_STYLE
    if inner != "auto":
        key = f"quote_rule_inner_{inner}"
        i = ui.get(key, "")
        if i:
            parts.append(i)

    return "\n".join(parts)


def get_quote_rules_heading() -> str:
    """Return the localised heading for the quote style rules section."""
    from locales import get_locale
    return get_locale().UI.get("quote_rules_heading", "Quote Style Rules")


# --- Feature #3: Polish loop ---
def polish_evaluate_system() -> str:
    return _with_lang(get_prompts()["polish_evaluate_system"])


def polish_evaluate_prompt(**kwargs) -> str:
    return get_prompts()["polish_evaluate_prompt"].format(**kwargs)


def polish_improve_system() -> str:
    return _with_lang(get_prompts()["polish_improve_system"])


def polish_improve_prompt(**kwargs) -> str:
    return get_prompts()["polish_improve_prompt"].format(**kwargs)


# --- Feature #4: Volume checkpoint adjustment ---
def volume_adjust_prompt(**kwargs) -> str:
    return get_prompts()["volume_adjust_prompt"].format(**kwargs)


# --- Feature #6: Final summary ---
def final_summary_system() -> str:
    return _with_lang(get_prompts()["final_summary_system"])


def final_summary_prompt(**kwargs) -> str:
    return get_prompts()["final_summary_prompt"].format(**kwargs)


# --- Word count validation ---
def expand_chapter_system() -> str:
    return _with_lang(get_prompts()["expand_chapter_system"])


def expand_chapter_prompt(**kwargs) -> str:
    return get_prompts()["expand_chapter_prompt"].format(**kwargs)


def compress_chapter_system() -> str:
    return _with_lang(get_prompts()["compress_chapter_system"])


def compress_chapter_prompt(**kwargs) -> str:
    return get_prompts()["compress_chapter_prompt"].format(**kwargs)


def split_chapter_system() -> str:
    return _with_lang(get_prompts()["split_chapter_system"])


def split_chapter_prompt(**kwargs) -> str:
    return get_prompts()["split_chapter_prompt"].format(**kwargs)
