"""Small helper to list files and folders.

Imagine taking a stroll through your house and jotting down the name of every
room and object you see. ``ProjectTree`` performs the same walk on your file
system, saving a simple text representation so you know where everything lives.
"""

from __future__ import annotations  # allow type hints to reference classes by name

import os
from pathlib import Path
from typing import List


class ProjectTree:
    """Collect and display folder structures.

    Picture a tour guide leading you through the directories. At each stop the
    guide writes down what they see so we can replay the tour later. That is
    essentially what this class does.
    """

    def __init__(self, root_path: str = ".") -> None:
        """Set up the starting point for the walk."""

        # ``root_path`` tells us where to begin exploring. Using ``Path`` avoids
        # issues with different operating systems, much like using a universal
        # map legend.
        self.root_path: Path = Path(root_path)

    def build_tree(self) -> List[str]:
        """Return a list of lines describing the directory tree."""

        lines: List[str] = []  # each line will hold one item from the walk

        # ``os.walk`` works like exploring every branch of a tree. It provides a
        # folder path plus the subfolders and files inside it.
        for folder, subfolders, files in os.walk(self.root_path):
            # ``relative_to`` computes the path from the starting folder to the
            # current one. The length of that path tells us how deep we are in
            # the hierarchy.
            depth = len(Path(folder).relative_to(self.root_path).parts)
            indent = "    " * depth

            # Add the folder itself to the list. A trailing slash marks it as a
            # directory, similar to how street signs note a cul-de-sac.
            lines.append(f"{indent}{Path(folder).name}/")

            # Add each file in alphabetical order so the output is predictable.
            for file_name in sorted(files):
                lines.append(f"{indent}    {file_name}")

        return lines

    def display(self) -> None:
        """Print each line returned from :meth:`build_tree`."""

        for line in self.build_tree():
            print(line)


def main() -> None:
    """Entry point for ``python -m mcp_project.tree``."""
    ProjectTree().display()


if __name__ == "__main__":
    main()
