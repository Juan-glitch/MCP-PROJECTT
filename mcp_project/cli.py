"""Tiny interface for the command line.

Imagine this module as the front door to the package. When you type
``python -m mcp_project`` in your terminal, control comes here. The interface
only recognizes one command for now: ``tree``. If you omit it we politely say
hello.
"""

from __future__ import annotations  # allows forward references in type hints

import argparse
from typing import List, Optional

from mcp_project.core.tree import ProjectTree



def main(argv: Optional[List[str]] = None) -> None:
    """Parse arguments and run the chosen action."""

    # Set up a parser to interpret what the user types. Think of it as a recipe
    # that tells Python which ingredients (arguments) we expect.
    parser = argparse.ArgumentParser(description="MCP PROJECT CLI")

    # ``command`` is optional. If the user provides "tree" we display the
    # directory structure. Leaving it out just prints a friendly greeting.
    parser.add_argument(
        "command",
        nargs="?",
        default="hello",
        help="Choose 'tree' to show directories or leave empty for greeting",
    )

    # ``parse_args`` reads the actual words from the command line. When running
    # tests we can supply ``argv`` manually.
    args = parser.parse_args(argv)

    # Decide what to do based on the command
    if args.command == "tree":
        # Display the project tree starting at the current directory
        ProjectTree().display()
    else:
        # Simple welcome message for any other command
        print("Hello from MCP PROJECT")

if __name__ == "__main__":
    # When a Python file is executed directly (not imported), ``__name__`` is
    # set to ``"__main__"``. This little check lets us run the ``main`` function
    # only in that case. It's a common pattern you will see in many scripts.
    main()