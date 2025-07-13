import os
from pathlib import Path

# The simple ``ProjectTree`` class lives in the ``core`` module.
from mcp_project.core import ProjectTree


def test_build_tree(tmp_path: Path) -> None:
    # Create a tiny directory structure to inspect
    (tmp_path / "dirA").mkdir()
    (tmp_path / "dirA" / "file.txt").write_text("hi")

    tree = ProjectTree(str(tmp_path))
    lines = tree.build_tree()
    assert any("dirA/" in line for line in lines)
    assert any("file.txt" in line for line in lines)
