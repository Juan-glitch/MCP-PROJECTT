
from pathlib import Path
from mcp_project.core import ProjectTree


def test_build_tree(tmp_path: Path) -> None:
    """ProjectTree should detect a nested file."""
    dir_a = tmp_path / "dirA"
    dir_a.mkdir()
    file_path = dir_a / "file.txt"
    file_path.write_text("hi")

    tree = ProjectTree(str(tmp_path)).build_tree()

    names = [child["name"] for child in tree["children"]]
    assert "dirA" in names
    sub_names = [child["name"] for child in tree["children"][names.index("dirA")]["children"]]
    assert "file.txt" in sub_names
