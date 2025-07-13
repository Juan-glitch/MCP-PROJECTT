# Project Structure

This document gives a quick overview of the folder layout. Think of it as a map so you know where each piece of the project lives.

- `mcp_project/` – package source code (think of this as the "engine room")
  - `cli.py` – command line interface
  - `core/` – basic utilities such as the simple tree explorer
  - `tools/` – extra helpers like an advanced tree generator
  - `__main__.py` – lets you run the package with ``python -m mcp_project``
- `tests/` – unit tests (these check that the parts still work)
- `docs/` – further documentation

Use `python -m mcp_project tree` to print a directory tree of the current folder.
