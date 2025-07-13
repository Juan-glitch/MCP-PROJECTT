"""Decide quickly whether a path should be ignored while building the tree.

As the directory walker explores files it consults this module to skip entries
like ``.git`` or ``__pycache__``. It is similar to using earplugs when walking
past a noisy street: we avoid paying attention to things that do not matter for
the tree representation.
"""

from pathlib import Path

# Names of directories we do not want to explore. Feel free to extend this set.
IGNORED_DIRS = {".git", "__pycache__", ".venv", "venv"}


def should_ignore(path: Path) -> bool:
    """Return ``True`` when ``path`` should not appear in the tree.

    Args:
        path: File or directory to check.

    Returns:
        ``True`` if the name matches one of the ignored patterns.
    """
    # ``Path.name`` gives the final component (file or folder name). It is like
    # reading the label on a drawer.
    name = path.name

    # Simple membership test: if the name is in the ``IGNORED_DIRS`` set we do
    # not want it. No complex rules here; we aim for clarity.
    return name in IGNORED_DIRS