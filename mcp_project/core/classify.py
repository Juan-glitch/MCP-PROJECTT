"""Classify files into broad categories based on their extension.

This module performs a quick check on the file name to guess what the file is
for. Think of it as looking at a book's cover: a glance usually tells you
whether it is a novel or a manual. The approach is simple but good enough for a
first version of the project tree.
"""

from pathlib import Path

# Groups of extensions mapped to a logical type
CODE_EXT = {".py", ".cpp", ".h", ".c", ".java", ".ts", ".kt"}
DOC_EXT = {".md", ".rst"}
BINARY_EXT = {".o", ".ko", ".exe", ".dll"}
META_FILES = {"pyproject.toml", "setup.py", ".gitignore", "README", "LICENSE"}


def classify_file(path: Path) -> str:
    """Guess what type of file ``path`` refers to.

    Args:
        path: Path to the file we want to classify.

    Returns:
        The label ``"code"``, ``"doc"``, ``"test"``, ``"binary"``, ``"meta"`` or
        ``"other"`` depending on the extension.
    """

    # Standardize the name to lower case for reliable comparison
    name = path.name.lower()
    ext = path.suffix.lower()

    # Tests are just code that checks other code. A common convention is to
    # start filenames with ``test_`` or end them with ``_test``.
    if name.startswith("test_") or name.endswith("_test.py"):
        return "test"

    if ext in CODE_EXT:
        return "code"
    if ext in DOC_EXT or name in {"readme", "license"}:
        return "doc"
    if ext in BINARY_EXT:
        return "binary"
    if name in META_FILES:
        return "meta"

    # Anything we do not recognize falls into the generic bucket.
    return "other"
