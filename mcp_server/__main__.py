"""Entry point for launching the API with ``python -m mcp_server`` or ``mcp-server``."""

# ``uvicorn`` is the lightweight web server that will host our FastAPI app.
# You can picture it as the engine of a car: once it starts, the application
# begins responding to requests.
import uvicorn

# Import the FastAPI ``app`` defined in ``app.py``. This is the web application
# we want ``uvicorn`` to run.
from .app import app


def main() -> None:
    """Start the development server.

    The function below boots up ``uvicorn`` so the API becomes reachable. It's
    similar to turning on a lamp: once switched on, it keeps shining until we
    turn it off.
    """
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    # Running the module directly should behave the same as calling ``main``.
    main()
