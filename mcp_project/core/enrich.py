# --- FastMCP integration header ---
import json
from typing import Dict
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Inicializa el servidor FastMCP
mcp = FastMCP("enrich")

# --- Fin cabecera FastMCP ---

from .classify import classify_file

@mcp.tool()
def enrich_node(node: Dict, full_path: Path) -> Dict:
    """Attach metadata to a node in the directory tree.

    Args:
        node: Dictionary describing a file or directory.
        full_path: Absolute path to the same file or directory on disk.

    Returns:
        The original ``node`` with extra keys added.
    """
    stats = full_path.stat()

    node["size"] = stats.st_size
    node["modified"] = stats.st_mtime
    node["permissions"] = stats.st_mode

    if node.get("type") == "file":
        node["classification"] = classify_file(full_path)

    return node

if __name__ == "__main__":
    # Inicializa y ejecuta el servidor FastMCP
    mcp.run(transport='stdio')