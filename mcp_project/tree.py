"""Utilities to inspect project directories."""

from __future__ import annotations

import os
from pathlib import Path
from typing import List


class ProjectTree:
    """Collect and display folder structures.

    The class walks through the file system starting from ``root_path`` and
    stores a simple text representation. Think of it like drawing a map of all
    the files and folders so you can quickly see what is inside.
    """

    def __init__(self, root_path: str = ".") -> None:
        # ``root_path`` is where the search begins. By default it uses the
        # current directory. ``Path`` helps us work with filesystem paths in a
        # platform-independent way.
        self.root_path: Path = Path(root_path)

    def build_tree(self) -> List[str]:
        """Return a list of lines describing the directory tree."""
        lines: List[str] = []
        # ``os.walk`` goes through every folder and file starting at
        # ``root_path``. It's like exploring every branch of a tree to list
        # everything inside.
        for folder, subfolders, files in os.walk(self.root_path):
            # ``relative_to`` computes the path from ``root_path`` to the
            # current ``folder``. The number of parts tells us the depth so we
            # can indent accordingly.
            depth = len(Path(folder).relative_to(self.root_path).parts)
            indent = "    " * depth
            lines.append(f"{indent}{Path(folder).name}/")
            for file_name in sorted(files):
                lines.append(f"{indent}    {file_name}")
        return lines

    def display(self) -> None:
        """Print the tree line by line."""
        for line in self.build_tree():
            print(line)


def main() -> None:
    """Entry point for ``python -m mcp_project.tree``."""
    ProjectTree().display()


if __name__ == "__main__":
    main()
