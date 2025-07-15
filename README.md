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

- The library `httpx` must be installed with a version **below** `0.27`:

  ```bash
  python -m pip install "httpx<0.27"
  ```

- Show the directory tree of the current folder:

  ```bash
  python -m mcp_project tree
  ```

- Run the tests:

  ```bash
  python -m pytest
  ```

- Launch the example API server:

  ```bash
  mcp-server
  ```

For a tour of the folder layout see `docs/01_project_structure.md`.
For step-by-step validation instructions see `docs/05_validationGuide.md`.

## Node tooling

This repository doesn't require Node or `npm`. Earlier versions shipped with
`package.json` and `package-lock.json` for experiments, but those files have
been removed to keep the focus on the Python examples.

## License

MIT License. See `LICENSE` for details.
