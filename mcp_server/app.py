"""A tiny FastAPI application used for testing the server entry point."""

# Import the FastAPI class. Think of this as the blueprint for our web server.
from fastapi import FastAPI

# Create the application instance. It's like opening the doors of a new shop
# where clients will come in to interact.
app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a basic health message.

    This is comparable to a receptionist saying "hello" to confirm the shop
    is open for business.
    """
    return {"status": "ok"}
