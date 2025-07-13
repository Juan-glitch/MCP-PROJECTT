"""MCP Project example package.

This file exposes the most useful functions so importing ``mcp_project`` feels
similar to opening a toolbox and seeing all the common tools ready to use.
"""

__all__ = ["main", "ProjectTree"]

from .cli import main
from .core import ProjectTree
