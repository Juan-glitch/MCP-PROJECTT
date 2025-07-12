"""Compatibility wrapper for ``ProjectTree``.

This module keeps the old import path working while the real
implementation lives in :mod:`mcp_project.project_tree`.
"""

from __future__ import annotations

from .project_tree import ProjectTree


def main() -> None:
    """Entry point for ``python -m mcp_project.tree``."""
    ProjectTree().display()


if __name__ == "__main__":
    main()
