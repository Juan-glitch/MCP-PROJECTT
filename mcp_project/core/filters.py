"""Decide quickly whether a path should be ignored while building the tree."""

from pathlib import Path

# Names of directories we do not want to explore
IGNORED_DIRS = {".git", "__pycache__", ".venv", "venv"}


def should_ignore(path: Path) -> bool:
    """Return ``True`` when ``path`` should not appear in the tree."""
    name = path.name
    return name in IGNORED_DIRS
