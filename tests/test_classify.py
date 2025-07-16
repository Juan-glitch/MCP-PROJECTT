from pathlib import Path
from mcp_project.core.classify import classify_file


def test_classify_basic() -> None:
    assert classify_file(Path("main.py")) == "code"
    assert classify_file(Path("README.md")) == "doc"
    assert classify_file(Path("program.o")) == "binary"
    assert classify_file(Path("pyproject.toml")) == "meta"

