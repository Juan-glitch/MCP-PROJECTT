# Project Structure

This document gives a quick overview of how the repository is organised.

- `mcp_project/` — package source code
  - `cli.py` — command line interface
  - `core/` — helpers for building and inspecting directory trees
    - `tree.py` — walk directories and collect info
    - `filters.py` — rules to skip files
    - `classify.py` — basic file type detection
    - `enrich.py` — attach metadata like size and dates
    - `snapshot.py` — save and compare tree states
  - `__main__.py` — enables `python -m mcp_project`
- `mcp_server/` — lightweight FastAPI service exposing the tree API
- `tests/` — unit tests covering each helper and the HTTP server
- `docs/` — additional guides (this file lives here)

Use `python -m mcp_project tree` to print a directory tree of the current folder.