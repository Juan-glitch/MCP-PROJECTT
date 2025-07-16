"""Simple command-line interface for MCP Project."""

import argparse
from typing import List, Optional

from .core import ProjectTree


def main(argv: Optional[List[str]] = None) -> None:
    """Entry point for the ``mcp-project`` script."""
    parser = argparse.ArgumentParser(description="MCP Project CLI")
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root path to inspect",
    )
    args = parser.parse_args(argv)

    tree = ProjectTree(args.path).build_tree()
    print(tree)


if __name__ == "__main__":
    main()
