# Validation Guide

This short guide explains how to check that the project works as intended.
It covers installation, running the command line interface and executing the
unit tests.

## 1. Install the package

The project uses a standard Python package layout. To make the code available
for import and to run the CLI you can install it in *editable* mode. Think of
this as placing a bookmark in the source directory so Python can find it.

```bash
python -m pip install -e .
```

This command reads `pyproject.toml`, builds the package and registers it with
your interpreter. Any edits you make to the source files will be picked up
immediately without reinstalling.

## 2. Try the command line interface

With the package installed you can invoke the CLI using `python -m mcp_project`.
The default command prints a friendly greeting. Pass `tree` to see the
structure of the current directory as JSON.

```bash
# Display a greeting
python -m mcp_project

# Show the directory tree
python -m mcp_project tree
```

The tree output is a nested dictionary where every folder becomes a node with
`children`. Files also include a simple classification such as `code`, `doc` or
`other`.

## 3. Run the tests

Automated tests confirm that each helper behaves correctly. Execute them with:

```bash
pytest -q
```

All tests should pass. They cover file classification, metadata enrichment,
filtering rules and snapshot comparisons.

