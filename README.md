# MCP Project

This repository contains a small example package and a few helper utilities.
Think of it as a sandbox where you can try out ideas without fear of breaking
anything important.

## Development workflow

Active work happens on the `dev` branch. Once changes are ready they are merged
into `main`.

## Quick start

- Install the package in editable mode:

  ```bash
  python -m pip install -e .
  ```

- Show the directory tree of the current folder:

  ```bash
  python -m mcp_project tree
  ```

- Start the development server:

  ```bash
  uvicorn mcp_server.main:app --reload
  ```

- Fetch the project tree in JSON format:

  ```bash
  curl http://localhost:8000/tree
  ```

- Run the tests:

  ```bash
  python -m pytest
  ```

For a tour of the folder layout see `docs/01_project_structure.md`.
For step-by-step validation instructions see `docs/05_validationGuide.md`.

## License

MIT License. See `LICENSE` for details.
