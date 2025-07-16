"""Minimal FastAPI app returning the project tree."""

from fastapi import FastAPI

from mcp_project.core import ProjectTree

app = FastAPI()


@app.get("/tree")
def get_tree():
    """Return the directory structure starting at the current folder."""
    return ProjectTree().build_tree()
