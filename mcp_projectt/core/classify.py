# --- FastMCP integration header ---
import json
from typing import Dict
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("classify")
# --- End FastMCP header ---

"""Classify files into broad categories based on their extension."""

# Groups of extensions mapped to a logical type
CODE_EXT = {".py", ".cpp", ".h", ".c", ".java", ".ts", ".kt"}
DOC_EXT = {".md", ".rst"}
BINARY_EXT = {".o", ".ko", ".exe", ".dll"}
META_FILES = {"pyproject.toml", "setup.py", ".gitignore", "README", "LICENSE"}


@mcp.tool()
def classify_file(path: Path) -> str:
    """Guess the type of file ``path`` refers to."""
    # Convert the name to lower case for reliable comparison
    name = path.name.lower()
    ext = path.suffix.lower()

    if name.startswith("test_") or name.endswith("_test.py"):
        return "test"
    if ext in CODE_EXT:
        return "code"
    if ext in DOC_EXT or name in {"readme", "license"}:
        return "doc"
    if ext in BINARY_EXT:
        return "binary"
    if name in META_FILES:
        return "meta"
    return "other"


if __name__ == "__main__":
    # Run FastMCP when executed directly
    mcp.run(transport="stdio")
