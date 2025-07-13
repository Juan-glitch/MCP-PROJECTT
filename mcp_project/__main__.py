"""Entry point for ``python -m mcp_project``.

This file lets you run the package directly from the command line using the
``-m`` option. It simply calls :func:`mcp_project.cli.main`.
"""

from .cli import main

if __name__ == "__main__":
    # Only execute ``main`` when this file is run as a script.
    main()
