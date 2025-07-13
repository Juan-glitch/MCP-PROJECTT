"""Provide extra details for each node of the project tree.

The role of this module is to decorate every file or folder with useful
information: size, modification time, permissions and even a quick
classification. Picture it as writing short notes next to every item in a house
inventory so you know more than just the name.
"""

from pathlib import Path
from typing import Dict

from .classify import classify_file


def enrich_node(node: Dict, full_path: Path) -> Dict:
    """Attach metadata to a node in the directory tree.

    Args:
        node: Dictionary describing a file or directory.
        full_path: Absolute path to the same file or directory on disk.

    Returns:
        The original ``node`` with extra keys added.
    """
    stats = full_path.stat()

    # ``st_size`` is the file size in bytes. If the path is a directory the size
    # reported by ``stat`` is typically zero or a small value. For a quick
    # overview we keep it simple and do not sum the contents.
    node["size"] = stats.st_size

    # Modification time tells us when the content last changed. We store the
    # raw timestamp; tools can convert it to human dates later.
    node["modified"] = stats.st_mtime

    # ``stat`` also gives us the permission bits (read/write/execute). These
    # values look cryptic but are standard in Unix-like systems.
    node["permissions"] = stats.st_mode

    # Use our lightweight classifier to label the entry.
    if node.get("type") == "file":
        node["classification"] = classify_file(full_path)

    return node