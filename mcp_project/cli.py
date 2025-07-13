"""Simple command line interface for MCP Project."""

from __future__ import annotations

import argparse
import json
from typing import List, Optional

from mcp_project.core import ProjectTree


def main(argv: Optional[List[str]] = None) -> None:
    """Parse arguments and print the project tree if requested.

    Args:
        argv: Optional list of strings to parse instead of ``sys.argv``.
    """
    parser = argparse.ArgumentParser(description="MCP PROJECT CLI")
    parser.add_argument(
        "command",
        nargs="?",
        default="hello",
        help="Use 'tree' to view the directory structure",
    )
    args = parser.parse_args(argv)

    if args.command == "tree":
        tree = ProjectTree().build_tree()
        print(json.dumps(tree, indent=2))
    else:
        print("Hello from MCP PROJECT")


if __name__ == "__main__":
    main()