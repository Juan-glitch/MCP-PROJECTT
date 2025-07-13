"""Build a nested dictionary describing the project structure.

The module walks through files and folders starting from a chosen root. As it
visits each entry it asks the filtering and enrichment helpers whether the item
should be included and which extra details to attach. The result is a plain
Python dictionary that mirrors the layout of the project. It is akin to drawing
a map of your house, room by room.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from . import enrich
from .classify import classify_file
from .filters import should_ignore


class ProjectTree:
    """Represent a directory tree and collect metadata.

    Args:
        root_path: Path where the walk should start. Defaults to the current
            working directory.
    """

    def __init__(self, root_path: str = ".") -> None:
        # Keep the starting location for later use
        self.root_path = Path(root_path)

    def build_tree(self) -> Dict:
        """Generate the entire directory tree starting from ``root_path``.

        Returns:
            Dictionary with nested entries representing directories and files.
        """
        return self._build(self.root_path)

    def _build(self, current: Path) -> Dict:
        """Recursive helper used by :meth:`build_tree`.

        Args:
            current: Path being processed.

        Returns:
            Dictionary representation of ``current`` and its children.
        """
        node = {
            "type": "dir" if current.is_dir() else "file",
            "name": current.name,
        }

        if current.is_dir():
            node["children"] = []
            for child in sorted(current.iterdir(), key=lambda p: p.name.lower()):
                if should_ignore(child):
                    continue
                child_node = self._build(child)
                node["children"].append(child_node)
        else:
            # For files we can note the classification right away
            node["classification"] = classify_file(current)

        # Add metadata such as size and dates
        node = enrich.enrich_node(node, current)
        return node

    def display(self) -> None:
        """Print the tree in a human friendly way."""
        self._print_node(self.build_tree())

    def _print_node(self, node: Dict, prefix: str = "") -> None:
        """Recursive helper used by :meth:`display`.

        Args:
            node: Dictionary representing the current entry.
            prefix: String of spaces used to indent child nodes.
        """
        print(prefix + node["name"])
        for child in node.get("children", []):
            self._print_node(child, prefix + "    ")


if __name__ == "__main__":
    ProjectTree().display()