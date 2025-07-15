"""Simple HTTP server exposing the project tree API.

This module provides a lightweight FastAPI server that reuses the
``ProjectTree`` helper from :mod:`mcp_project`. The goal is to
make it easy to start experimenting with MCP (Minimal Code
Processor) ideas. It exposes a single endpoint ``/tree`` that
returns the directory structure of the repository in JSON form.

The implementation intentionally sticks to the basics so new
developers can follow along without trouble.
"""

from fastapi import FastAPI
from mcp_project.core import ProjectTree

# ---------------------------------------------------------------------------
# Create the FastAPI application. Think of this as preparing a kitchen where
# every endpoint is a separate recipe. FastAPI handles the heavy lifting of
# HTTP communication for us.
# ---------------------------------------------------------------------------
app = FastAPI()


@app.get("/tree")
def read_tree() -> dict:
    """Return the directory tree of the current project.

    It simply instantiates :class:`ProjectTree` and converts the
    resulting nested dictionary into a JSON response.
    """
    return ProjectTree().build_tree()


if __name__ == "__main__":
    # -------------------------------------------------------------------
    # When executed directly, run a development server using uvicorn.
    # Uvicorn is a lightweight ASGI server well suited for FastAPI apps.
    # -------------------------------------------------------------------
    import uvicorn

    # 0.0.0.0 makes the server reachable from outside the container.
    uvicorn.run("mcp_server.main:app", host="0.0.0.0", port=8000, reload=True)
