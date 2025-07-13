from pathlib import Path
from mcp_project.core import ProjectTree

def test_build_tree(tmp_path: Path) -> None:
    """
    Creates a temporary directory structure with a file and
    verifies that ProjectTree correctly detects it.
    """
    # Create a temporary directory and file inside the test environment
    dir_a = tmp_path / "dirA"
    dir_a.mkdir()
    (dir_a / "file.txt").write_text("hi")

    # Create a ProjectTree instance pointing to the temporary directory
    tree = ProjectTree(str(tmp_path))

    # Get the output as a list of lines
    lines = tree.build_tree()

    # Check that the directory and file appear in the output
    assert any("dirA/" in line for line in lines)
    assert any("file.txt" in line for line in lines)

# Note: You do not need to run this manually.
# Pytest will automatically find and run this test when you run `pytest` in the terminal.
