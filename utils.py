"""Utility functions for the novel_writer project."""

import sys
import locale

from locales import get_locale


def setup_readline():
    """Configure GNU readline for proper UTF-8 multi-byte character handling.

    Without these settings, pressing Backspace while editing non-ASCII
    characters (e.g. CJK) may only erase one byte of a multi-byte
    sequence, producing garbled output.
    """
    try:
        import readline
    except ImportError:
        return

    # Allow 8-bit characters in input (required for UTF-8)
    readline.parse_and_bind("set input-meta on")
    # Allow 8-bit characters in output (display them as-is)
    readline.parse_and_bind("set output-meta on")
    # Do NOT strip the 8th bit from input characters
    readline.parse_and_bind("set convert-meta off")

    # Ensure the locale is UTF-8 aware so readline treats multi-byte
    # sequences as single characters when moving/deleting.
    try:
        if not locale.getlocale()[1] or "utf" not in (locale.getlocale()[1] or "").lower():
            locale.setlocale(locale.LC_ALL, "")
    except locale.Error:
        pass

    # Force Python's stdin to UTF-8 if it isn't already
    if hasattr(sys.stdin, "reconfigure"):
        try:
            sys.stdin.reconfigure(encoding="utf-8")
        except Exception:
            pass


def multiline_input(prompt: str = "") -> str:
    """Read multi-line input from the terminal, supporting normal and paste modes.

    Normal mode (default):
        The user can type multiple lines freely. Pressing Enter on an
        empty line (i.e. two consecutive Enters) signals the end of input.
        Single-line input is fully compatible.

    Paste mode:
        Type ``/paste`` as the first line to enter paste mode. In this
        mode blank lines do **not** terminate input; only a standalone
        ``/end`` line ends the session. Ideal for pasting Markdown or
        other content that contains blank lines.

    Args:
        prompt: The prompt string displayed before the first line.

    Returns:
        The concatenated input text with leading/trailing whitespace
        stripped. Lines are joined with ``\\n``.
    """
    ui = get_locale().UI
    hint = ui.get("multiline_hint", "(Enter a blank line to finish)")
    paste_hint = ui.get("multiline_paste_hint",
                        "(Paste mode: type /end on a new line to finish)")
    print(f"{hint}")

    first_line = input(prompt)

    # Empty input, return immediately
    if not first_line.strip():
        return ""

    # Paste mode: first line is /paste
    if first_line.strip().lower() == "/paste":
        print(paste_hint)
        return _read_paste_mode()

    # Normal mode: blank line terminates
    lines: list[str] = [first_line]
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        lines.append(line)

    return "\n".join(lines).strip()


def _read_paste_mode() -> str:
    """Paste mode: keep reading input until a standalone /end line is entered."""
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip().lower() == "/end":
            break
        lines.append(line)

    return "\n".join(lines).strip()
