"""
Locale management module.
Loads language-specific UI strings, prompts, and templates based on user selection.
Supports both pre-defined languages and dynamically generated ones.
"""
import importlib
import os
import re
from types import ModuleType

# Language code -> (display name in that language, English name)
SUPPORTED_LANGUAGES = {
    "en":      ("English",      "English"),
    "zh_cn":   ("简体中文",      "Simplified Chinese"),
    "zh_tw":   ("繁體中文",      "Traditional Chinese"),
    "ja":      ("日本語",        "Japanese"),
    "ko":      ("한국어",        "Korean"),
    "vi":      ("Tiếng Việt",   "Vietnamese"),
    "th":      ("ภาษาไทย",      "Thai"),
    "zh_cl":   ("文言文",        "Classical Chinese"),
    "ja_cl":   ("古典日本語",     "Classical Japanese"),
    "la":      ("Latina",       "Latin"),
    "sa":      ("संस्कृतम्",     "Sanskrit"),
}

# Currently loaded locale module
_current_locale: ModuleType | None = None
_current_lang: str = "en"


def _discover_locale_files():
    """
    Scan the locales/ directory for .py files not yet in SUPPORTED_LANGUAGES.
    Auto-registers them with a best-effort name extracted from the module docstring.
    This allows dynamically generated locale files to be picked up without code changes.
    """
    locales_dir = os.path.dirname(os.path.abspath(__file__))
    for filename in sorted(os.listdir(locales_dir)):
        if not filename.endswith(".py") or filename.startswith("_"):
            continue
        code = filename[:-3]  # strip .py
        if code in SUPPORTED_LANGUAGES:
            continue
        # Try to extract language info from the module
        try:
            mod = importlib.import_module(f"locales.{code}")
            # Check it has the required structure
            if not (hasattr(mod, "UI") and hasattr(mod, "PROMPTS") and hasattr(mod, "TEMPLATES")):
                continue
            # Try to extract names from docstring
            doc = (mod.__doc__ or "").strip()
            # Pattern: "NativeName (EnglishName) locale"
            match = re.match(r'^(.+?)\s*\((.+?)\)\s*locale', doc, re.IGNORECASE)
            if match:
                native_name = match.group(1).strip()
                english_name = match.group(2).strip()
            else:
                # Fallback: use code as both names
                native_name = code
                english_name = code
            SUPPORTED_LANGUAGES[code] = (native_name, english_name)
        except Exception:
            pass  # Skip files that can't be imported


# Auto-discover any new locale files on import
_discover_locale_files()


def load_locale(lang_code: str) -> ModuleType:
    """
    Load and cache the locale module for the given language code.

    Args:
        lang_code: One of the keys in SUPPORTED_LANGUAGES (e.g. 'en', 'zh_cn').

    Returns:
        The loaded locale module.

    Raises:
        ValueError: If the language code is not supported.
        ImportError: If the locale file cannot be found.
    """
    global _current_locale, _current_lang

    if lang_code not in SUPPORTED_LANGUAGES:
        raise ValueError(
            f"Unsupported language: '{lang_code}'. "
            f"Available: {list(SUPPORTED_LANGUAGES.keys())}"
        )

    module = importlib.import_module(f"locales.{lang_code}")
    _current_locale = module
    _current_lang = lang_code
    return module


def get_locale() -> ModuleType:
    """Get the currently loaded locale module. Defaults to English if none loaded."""
    global _current_locale
    if _current_locale is None:
        load_locale("en")
    return _current_locale


def get_lang() -> str:
    """Get the current language code."""
    return _current_lang


def t(path: str, **kwargs) -> str:
    """
    Shortcut to access a locale string by dot-separated path and format it.

    Example:
        t("UI.welcome_title")  -> "📖 Novel Agent Workflow v1.0"
        t("UI.chapter_writing", chapter_num=5)  -> "📖 Writing Chapter 5..."

    Args:
        path: Dot-separated path to the string (e.g. "UI.welcome_title").
        **kwargs: Format arguments to apply to the string.

    Returns:
        The formatted locale string.
    """
    locale = get_locale()
    parts = path.split(".")
    obj = locale
    for part in parts:
        if isinstance(obj, dict):
            obj = obj[part]
        else:
            obj = getattr(obj, part)

    if kwargs and isinstance(obj, str):
        return obj.format(**kwargs)
    return obj
