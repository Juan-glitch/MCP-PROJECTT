"""Store and compare snapshots of the project tree.

The functions here are intentionally minimal: they simply read and write JSON
representations of the directory tree and compute differences between two
snapshots. Imagine taking a quick photo of a room to remember how it looked; a
snapshot works the same way for the file system.
"""

import json
from pathlib import Path
from typing import Dict, List


def save_snapshot(tree: Dict, path: Path) -> None:
    """Save ``tree`` to disk in JSON format.

    Args:
        tree: Dictionary produced by :class:`ProjectTree`.
        path: Destination file for the snapshot.
    """
    path.write_text(json.dumps(tree, indent=2))


def load_snapshot(path: Path) -> Dict:
    """Load a snapshot from ``path``.

    Args:
        path: JSON file previously written with :func:`save_snapshot`.

    Returns:
        The tree dictionary stored in the file.
    """
    return json.loads(path.read_text())


def _flatten(tree: Dict, prefix: str = "") -> List[str]:
    """Return a flat list of file paths from ``tree``.

    This helper walks every child node and collects their names so that we can
    compare two trees easily.

    Args:
        tree: Tree dictionary to process.
        prefix: Path prefix accumulated during recursion.

    Returns:
        List of file paths relative to the root of ``tree``.
    """
    current = prefix + tree["name"]
    paths = [current]
    for child in tree.get("children", []):
        paths.extend(_flatten(child, current + "/"))
    return paths


def diff_trees(tree_old: Dict, tree_new: Dict) -> Dict[str, List[str]]:
    """Return items added or removed between two trees.

    Args:
        tree_old: Snapshot representing the earlier state.
        tree_new: Snapshot representing the later state.

    Returns:
        A dictionary with ``"added"`` and ``"removed"`` lists describing the
        differences.
    """
    old_set = set(_flatten(tree_old))
    new_set = set(_flatten(tree_new))
    return {
        "added": sorted(new_set - old_set),
        "removed": sorted(old_set - new_set),
    }

