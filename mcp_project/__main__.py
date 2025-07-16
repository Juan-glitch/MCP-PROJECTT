"""
Main entrypoint for the MCP Project.
This script provides a single command-line interface (CLI) to control and initialize 
all the main services and utilities in the MCP Project ecosystem.

The design goal is to allow developers to:
- Start the whole system or individual services from one place.
- Use simple CLI commands to launch, debug, or inspect the project.
- Extend this script easily as the project grows.

Each service (FastMCP, Enrich, MCP, etc.) should provide a 'start_*_server' function
that is imported and called from here, making the orchestration clear and testable.
"""

from __future__ import annotations

import argparse
import json
from typing import List, Optional

from mcp_project.core import ProjectTree

# --- Import your server/service launchers here ---
# from mcp_project.fastmcp_server import start_fastmcp_server
# from mcp_project.enrich_server import start_enrich_server
# from mcp_project.mcp_server import start_mcp_server
# (Uncomment and adapt as needed)

def main(argv: Optional[List[str]] = None) -> None:
    """
    Main CLI handler for the MCP Project.

    Args:
        argv: Optional list of strings to parse instead of ``sys.argv``.

    The CLI offers several subcommands:
    - tree     : Print the project directory structure (for inspection/debug)
    - fastmcp  : Start the FastMCP server/service
    - enrich   : Start the Enrich server/service
    - mcp      : Start the MCP server/service
    - all      : Start all main services at once (for development/integration)
    - hello    : Default, prints a welcome message

    Example usage:
        python -m mcp_project tree
        python -m mcp_project fastmcp
        python -m mcp_project all
    """
    parser = argparse.ArgumentParser(
        description="MCP PROJECT: Unified CLI entrypoint"
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="hello",
        choices=["tree", "fastmcp", "enrich", "mcp", "all", "hello"],
        help="Choose a command: tree, fastmcp, enrich, mcp, all"
    )
    args = parser.parse_args(argv)

    if args.command == "tree":
        # Show project directory structure as JSON
        tree = ProjectTree().build_tree()
        print(json.dumps(tree, indent=2))

    elif args.command == "fastmcp":
        # Start the FastMCP server (uncomment import above)
        print("Starting FastMCP server...")
        # start_fastmcp_server()

    elif args.command == "enrich":
        # Start the Enrich server (uncomment import above)
        print("Starting Enrich server...")
        # start_enrich_server()

    elif args.command == "mcp":
        # Start the MCP server (uncomment import above)
        print("Starting MCP server...")
        # start_mcp_server()

    elif args.command == "all":
        # Start all services (in threads, processes, or async as needed)
        print("Starting all main MCP Project services...")
        # start_fastmcp_server()
        # start_enrich_server()
        # start_mcp_server()

    else:
        print("Hello from MCP PROJECT! (Use 'tree', 'fastmcp', 'enrich', 'mcp', or 'all')")


if __name__ == "__main__":
    # Entry point: calls main with default sys.argv
    main()
