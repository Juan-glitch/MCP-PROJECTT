# MCP-PROJECTT

Minimal Python project skeleton with devcontainer support.

## Usage

Run the CLI:

```bash
python -m mcp_project
```

## Development workflow

Active work happens on the `dev` branch. Changes are merged into `main` when they are ready for release.

## Directory layout

- `mcp_project/` – source code for the package.
- `requirements.txt` – project dependencies.
- `pyproject.toml` – build configuration.
- `tests/` – unit tests.

### Show the project tree

Display the folder structure using:

```bash
python -m mcp_project.tree
# or
python -m mcp_project tree
```

### Use ``ProjectTree`` in your code

You can also build the listing programmatically:

```python
from mcp_project import ProjectTree

tree = ProjectTree(".")
for line in tree.build_tree():
    print(line)
```

### Run tests

Execute the test suite with:

```bash
python -m pytest
```
