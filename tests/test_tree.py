import os
from pathlib import Path
from mcp_project.tree import ProjectTree


def test_build_tree(tmp_path: Path) -> None:
    # Create sample directory structure
    (tmp_path / "dirA").mkdir()
    (tmp_path / "dirA" / "file.txt").write_text("hi")

    tree = ProjectTree(str(tmp_path))
    lines = tree.build_tree()
    assert any("dirA/" in line for line in lines)
    assert any("file.txt" in line for line in lines)
