"""Entry point to run the FastAPI server with Uvicorn."""

from .main import app
import uvicorn


def main() -> None:
    """Launch the development server."""
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
