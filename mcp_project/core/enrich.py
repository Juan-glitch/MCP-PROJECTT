# --- FastMCP integration header ---
import json
from typing import Dict
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("enrich")
# --- End FastMCP header ---

from .classify import classify_file


@mcp.tool()
def enrich_node(node: Dict, full_path: Path) -> Dict:
    """Attach metadata to a directory tree node."""
    stats = full_path.stat()

    node["size"] = stats.st_size
    node["modified"] = stats.st_mtime
    node["permissions"] = stats.st_mode

    if node.get("type") == "file":
        node["classification"] = classify_file(full_path)

    return node


if __name__ == "__main__":
    # Run FastMCP when executed directly
    mcp.run(transport="stdio")
