"""Support running the package with ``python -m mcp_project``."""

__all__ = ["main", "ProjectTree"]

from .cli import main
from .core import ProjectTree