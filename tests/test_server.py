"""Tiny check for the HTTP API."""

from fastapi.testclient import TestClient
from mcp_server.main import app


def test_tree_endpoint_returns_data() -> None:
    """Ensure ``/tree`` responds with a directory structure."""

    # Start a lightweight HTTP client pointing at our FastAPI app. This is like
    # having a tiny browser that lives inside the tests.
    client = TestClient(app)

    # Request the project tree and decode the JSON body.
    response = client.get("/tree")
    data = response.json()

    # We expect a successful status code and a root entry classified as a
    # directory. The presence of ``children`` confirms the structure was built.
    assert response.status_code == 200
    assert data.get("type") == "dir"
    assert "children" in data

