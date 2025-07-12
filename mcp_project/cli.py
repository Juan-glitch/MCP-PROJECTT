"""Simple command line interface."""

from __future__ import annotations

import argparse
from typing import List, Optional

from .tree import ProjectTree


def main(argv: Optional[List[str]] = None) -> None:
    """Run the CLI with optional arguments."""
    parser = argparse.ArgumentParser(description="MCP PROJECT CLI")
    parser.add_argument(
        "command",
        nargs="?",
        default="hello",
        help="Choose 'tree' to show directories or leave empty for greeting",
    )
    args = parser.parse_args(argv)

    if args.command == "tree":
        ProjectTree().display()
    else:
        print("Hello from MCP PROJECT")

if __name__ == "__main__":
    main()
