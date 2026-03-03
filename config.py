"""Novel Agent Workflow - Configuration Module.
All adjustable hyperparameters are centrally managed here.

All user-adjustable parameters (including API keys) should be placed
in user_config.json (excluded from git via .gitignore).
Refer to user_config.example.json for available fields.

Loading order: config.py defaults -> user_config.json
"""
import os

# ==================== Project Path Configuration ====================
# Base output directory (all novels are saved under this directory)
# Can be set to an absolute path, e.g. "/mnt/nas/novels" or "D:/novels"
# Default: "output" (relative to the project directory)
OUTPUT_BASE_DIR = "output"

# Project root (dynamically set at runtime to <OUTPUT_BASE_DIR>/<novel_name>)
PROJECT_ROOT = ""

# Output subdirectories
DIR_META = "meta"
DIR_WORLDBUILDING = "worldbuilding"
DIR_PLOT = "plot"
DIR_CHAPTERS = "chapters"

# ==================== LLM API Configuration ====================
# API mode: "openai" or "local"
API_MODE = "openai"

# --- OpenAI standard format (secrets loaded from secrets.json) ---
OPENAI_API_KEY = ""
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_MODEL = "gpt-4o"

# --- Local API (secrets loaded from secrets.json) ---
LOCAL_API_URL = ""
LOCAL_API_KEY = ""
LOCAL_WSID = ""
LOCAL_MODEL_MARKER = ""

# ==================== Generation Parameters ====================
# Enable streaming output (real-time token display during generation)
STREAM_MODE = True
TEMPERATURE = 0.7
TOP_P = 0.6
TOP_K = 20
REPETITION_PENALTY = 1.05
MAX_OUTPUT_TOKENS = 32768
MAX_INPUT_TOKENS = 32768

# ==================== Writing Parameters ====================
# Target word count range per chapter
CHAPTER_MIN_WORDS = 3000
CHAPTER_MAX_WORDS = 4000

# Enable automatic word count validation after each chapter
# When enabled, chapters that are too short will be expanded,
# and chapters that are too long will be compressed or split.
CHAPTER_WORD_COUNT_CHECK = True

# Max retries for word count validation (expand/compress loop)
MAX_WORD_COUNT_RETRIES = 2

# Split threshold: if word count exceeds MAX * this ratio, split into two chapters
# e.g. 1.5 means if a chapter is 150%+ of MAX, it gets split
CHAPTER_SPLIT_THRESHOLD = 1.5

# Number of recent chapter summaries to include when writing a new chapter
RECENT_CHAPTERS_FOR_CONTEXT = 5

# ==================== Multi-Draft Outline ====================
# Number of outline variants to generate for comparison (feature #1)
OUTLINE_DRAFT_COUNT = 3

# ==================== Parallel Quality Review ====================
# Enable parallel multi-reviewer after each chapter (feature #2)
ENABLE_PARALLEL_REVIEW = True
# Minimum confidence score (0-100) for a review issue to be reported (feature #5)
REVIEW_CONFIDENCE_THRESHOLD = 80
# Max retries when critical review issues are found (rewrite the chapter)
MAX_REVIEW_RETRIES = 2

# ==================== Polish Loop ====================
# Enable self-polishing loop after writing (feature #3)
ENABLE_POLISH_LOOP = True
# Max polish iterations before force-exiting the loop
MAX_POLISH_ITERATIONS = 2
# Minimum quality score (1-10) required to exit polish loop
POLISH_QUALITY_THRESHOLD = 8

# ==================== Mid-Volume Checkpoint ====================
# Enable user confirmation checkpoint at the start of each volume (feature #4)
ENABLE_VOLUME_CHECKPOINT = True

# ==================== Final Summary ====================
# Enable final summary generation after all chapters are complete (feature #6)
ENABLE_FINAL_SUMMARY = True

# ==================== Parallelism Configuration ====================
# Max parallel workers (for worldbuilding and other parallelizable tasks)
MAX_PARALLEL_WORKERS = 3

# ==================== Retry Configuration ====================
MAX_RETRIES = 5
RETRY_DELAY = 2  # seconds

# ==================== Interaction Configuration ====================
# Max planning rounds (to prevent infinite loops)
MAX_PLANNING_ROUNDS = 20

# Lazy mode: after outline is confirmed, skip all user interactions and run fully automatically
LAZY_MODE = False

# ==================== Quote Style Configuration ====================
# Dialogue quote style for the novel
# "auto" = choose based on language, or set explicitly:
#   "curly"       = \u201c\u201d (Chinese default, also common in Vietnamese)
#   "corner"      = \u300c\u300d (CJK corner brackets)
#   "guillemet"   = \u00ab\u00bb (French/Russian style)
#   "dash"        = \u2014 em-dash for dialogue (Vietnamese/French option)
#   "straight"    = \"\" (English default)
QUOTE_STYLE = "auto"

# Inner thoughts / internal monologue quote style
# "auto" = choose based on language, or set explicitly:
#   "corner_double" = 『』 (CJK double corner brackets, common for thoughts in CJK)
#   "corner"        = 「」 (CJK single corner brackets)
#   "paren"         = （）(fullwidth parentheses, common for thoughts in Chinese novels)
#   "curly_single"  = '' (single curly quotes)
#   "italic"        = *italic* marker (for languages that use italics for thoughts)
#   "dash"          = —— em-dash for inner thoughts
#   "none"          = no special markers (describe thoughts narratively)
#   "same"          = same as dialogue quote style
INNER_QUOTE_STYLE = "auto"

# ==================== Language Configuration ====================
# Language code for the novel (set at runtime via language selection menu)
# See locales/__init__.py SUPPORTED_LANGUAGES for available codes
LANGUAGE = "en"

# ==================== External Config File ====================
# All user-adjustable settings (hyperparameters + API keys), excluded from git
USER_CONFIG_FILE = "user_config.json"

# Per-novel config file name (placed inside each novel's project directory)
# Overrides both config.py defaults and user_config.json for this novel only
NOVEL_CONFIG_FILE = "novel_config.json"


def _load_json_config(filename: str, *, silent: bool = False):
    """
    Load a JSON config file and override matching module-level variables.
    Keys starting with '_' are treated as comments and skipped.

    Args:
        filename: JSON file name (relative to this module's directory).
        silent: If True, do not print warning when file is missing.
    Returns:
        List of keys that were successfully loaded.
    """
    import json
    filepath = os.path.join(os.path.dirname(__file__) or ".", filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            ext = json.load(f)
        g = globals()
        loaded_keys = []
        for key, value in ext.items():
            if key.startswith("_"):
                continue
            if key in g:
                g[key] = value
                loaded_keys.append(key)
        return loaded_keys
    return None


def load_external_configs():
    """
    Load user_config.json to override default values.
    All settings (hyperparameters + API keys) live in one file.
    """
    from locales import get_locale
    ui = get_locale().UI

    loaded_keys = _load_json_config(USER_CONFIG_FILE)
    if loaded_keys is not None:
        print(ui["config_loaded"].format(file=USER_CONFIG_FILE, keys=", ".join(loaded_keys)))
    else:
        print(ui["config_not_found"].format(file=USER_CONFIG_FILE))
        print(ui["config_hint"].format(file=USER_CONFIG_FILE))


def setup_project_dirs(novel_name: str):
    """Initialize the project directory structure for the given novel name."""
    global PROJECT_ROOT
    from locales import get_locale
    base_dir = OUTPUT_BASE_DIR
    if not os.path.isabs(base_dir):
        base_dir = os.path.join(os.path.dirname(__file__) or ".", base_dir)
    PROJECT_ROOT = os.path.join(base_dir, novel_name)
    for d in [DIR_META, DIR_WORLDBUILDING, DIR_PLOT, DIR_CHAPTERS]:
        os.makedirs(os.path.join(PROJECT_ROOT, d), exist_ok=True)
    ui = get_locale().UI
    print(ui["project_initialized"].format(path=PROJECT_ROOT))

    # Auto-generate novel_config.json from example template if not present
    _ensure_novel_config()

    # Load per-novel config (overrides global user_config.json)
    load_novel_config()

    return PROJECT_ROOT


def _ensure_novel_config():
    """Copy novel_config.example.json into the project directory if novel_config.json does not exist."""
    import shutil
    novel_config_path = os.path.join(PROJECT_ROOT, NOVEL_CONFIG_FILE)
    if os.path.exists(novel_config_path):
        return

    example_path = os.path.join(os.path.dirname(__file__) or ".", "novel_config.example.json")
    if not os.path.exists(example_path):
        return

    try:
        shutil.copy2(example_path, novel_config_path)
        from locales import get_locale
        ui = get_locale().UI
        msg = ui.get("novel_config_auto_created",
                      "[Config] Auto-created {file} from template (edit to customize)")
        print(msg.format(file=NOVEL_CONFIG_FILE))
    except Exception as e:
        print(f"  ⚠️ Failed to create {NOVEL_CONFIG_FILE}: {e}")


def rename_project_dir(new_name: str) -> bool:
    """Rename the project directory to *new_name* and update PROJECT_ROOT.

    Returns True on success, False on failure.
    The function sanitises the name to avoid file-system issues and skips
    the rename when the directory already has the desired name.
    """
    global PROJECT_ROOT
    import re
    from locales import get_locale
    ui = get_locale().UI

    # Sanitise: strip leading/trailing whitespace, replace path-unsafe chars
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', new_name).strip()
    if not safe_name:
        return False

    parent = os.path.dirname(PROJECT_ROOT)
    new_path = os.path.join(parent, safe_name)

    # Already the same name
    if os.path.normpath(new_path) == os.path.normpath(PROJECT_ROOT):
        return True

    # Target already exists
    if os.path.exists(new_path):
        print(ui.get("rename_dir_exists",
                      "  ⚠️ Directory already exists: {path}").format(path=new_path))
        return False

    try:
        os.rename(PROJECT_ROOT, new_path)
        PROJECT_ROOT = new_path
        print(ui.get("rename_dir_done",
                      "  ✅ Project directory renamed to: {path}").format(path=new_path))
        return True
    except Exception as e:
        print(ui.get("rename_dir_failed",
                      "  ❌ Failed to rename directory: {error}").format(error=e))
        return False


def load_novel_config():
    """
    Load per-novel novel_config.json from the project directory.
    This provides a second override layer: config.py -> user_config.json -> novel_config.json.
    Only non-API settings are allowed to be overridden at project level.
    """
    from locales import get_locale
    ui = get_locale().UI

    novel_config_path = os.path.join(PROJECT_ROOT, NOVEL_CONFIG_FILE)
    if not os.path.exists(novel_config_path):
        return

    import json
    try:
        with open(novel_config_path, "r", encoding="utf-8") as f:
            ext = json.load(f)
    except Exception as e:
        print(f"  ⚠️ Failed to load {NOVEL_CONFIG_FILE}: {e}")
        return

    # API-related keys that should NOT be overridden at project level
    api_keys = {
        "API_MODE", "OPENAI_API_KEY", "OPENAI_BASE_URL", "OPENAI_MODEL",
        "LOCAL_API_URL", "LOCAL_API_KEY", "LOCAL_WSID", "LOCAL_MODEL_MARKER",
        "OUTPUT_BASE_DIR", "USER_CONFIG_FILE", "NOVEL_CONFIG_FILE",
    }

    g = globals()
    loaded_keys = []
    skipped_keys = []
    for key, value in ext.items():
        if key.startswith("_"):
            continue
        if key in api_keys:
            skipped_keys.append(key)
            continue
        if key in g:
            g[key] = value
            loaded_keys.append(key)

    if loaded_keys:
        novel_cfg_loaded = ui.get("novel_config_loaded",
            "[Config] Loaded {file}: {keys}")
        print(novel_cfg_loaded.format(file=NOVEL_CONFIG_FILE, keys=", ".join(loaded_keys)))
    if skipped_keys:
        novel_cfg_skipped = ui.get("novel_config_skipped",
            "  ⚠️ Skipped API/path keys in {file} (use global config): {keys}")
        print(novel_cfg_skipped.format(file=NOVEL_CONFIG_FILE, keys=", ".join(skipped_keys)))


def get_path(*parts):
    """Get an absolute file path within the project directory."""
    return os.path.join(PROJECT_ROOT, *parts)


# Load external configs on module import
load_external_configs()
