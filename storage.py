"""
Storage management module - Manages all file I/O for the novel project.
Mirrors the auto_novel directory structure:
  meta/          - Metadata (progress, style guide, hooks tracker)
  worldbuilding/ - World settings
  plot/          - Plot management (outlines, volume outlines, chapter summaries)
  chapters/      - Chapter text output
"""
import os
import config
from locales import get_locale


def _ensure_dir(filepath: str):
    """Ensure the parent directory of a file path exists."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)


def read_file(relative_path: str) -> str | None:
    """Read a file within the project directory."""
    path = config.get_path(relative_path)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None


def write_file(relative_path: str, content: str):
    """Write a file within the project directory."""
    path = config.get_path(relative_path)
    _ensure_dir(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    ui = get_locale().UI
    print(ui["file_written"].format(path=relative_path))


def append_file(relative_path: str, content: str):
    """Append content to a file within the project directory."""
    path = config.get_path(relative_path)
    _ensure_dir(path)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


def file_exists(relative_path: str) -> bool:
    """Check if a file exists within the project directory."""
    return os.path.exists(config.get_path(relative_path))


def list_chapter_files() -> list[str]:
    """List all written chapter files, sorted by number."""
    chapters_dir = config.get_path(config.DIR_CHAPTERS)
    if not os.path.exists(chapters_dir):
        return []
    files = [f for f in os.listdir(chapters_dir) if f.startswith("chapter_") and f.endswith(".txt")]
    files.sort()
    return files


def get_completed_chapter_count() -> int:
    """Get the count of completed chapters."""
    return len(list_chapter_files())


# ==================== Template Initializers ====================

def init_readme(novel_info: dict):
    """Initialize README.md using locale template."""
    tpl = get_locale().TEMPLATES["readme"]
    content = tpl.format(
        title=novel_info.get("title", "Untitled"),
        genre=novel_info.get("genre", "TBD"),
        target_words=novel_info.get("target_words", "TBD"),
        min_words=config.CHAPTER_MIN_WORDS,
        max_words=config.CHAPTER_MAX_WORDS,
        total_chapters=novel_info.get("total_chapters", "TBD"),
        volumes=novel_info.get("volumes", "TBD"),
        pov=novel_info.get("pov", "TBD"),
        tags=novel_info.get("tags", "TBD"),
        one_line_summary=novel_info.get("one_line_summary", ""),
    )
    write_file("README.md", content)


def init_progress(novel_info: dict):
    """Initialize the progress tracking file using locale template."""
    content = get_locale().TEMPLATES["progress"]
    write_file(f"{config.DIR_META}/progress.md", content)


def init_hooks_tracker():
    """Initialize the foreshadowing/hooks tracker file using locale template."""
    content = get_locale().TEMPLATES["hooks_tracker"]
    write_file(f"{config.DIR_META}/hooks_tracker.md", content)


def init_chapter_briefs():
    """Initialize the chapter summary file using locale template."""
    content = get_locale().TEMPLATES["chapter_briefs"]
    write_file(f"{config.DIR_PLOT}/chapter_briefs.md", content)
