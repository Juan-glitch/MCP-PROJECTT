"""Convenient imports for the MCP Project package.

When this package is imported it exposes :func:`mcp_project.main` and
:class:`mcp_project.core.ProjectTree` to make quick scripts easier to write.
"""

__all__ = ["main", "ProjectTree"]

from .cli import main
from .core import ProjectTree
