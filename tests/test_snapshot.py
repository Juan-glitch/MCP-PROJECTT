from mcp_project.core.snapshot import diff_trees, save_snapshot, load_snapshot
from pathlib import Path


def test_diff_trees(tmp_path: Path) -> None:
    old = {"name": "root", "type": "dir", "children": [{"name": "a.txt", "type": "file"}]}
    new = {"name": "root", "type": "dir", "children": [
        {"name": "a.txt", "type": "file"},
        {"name": "b.txt", "type": "file"},
    ]}
    diff = diff_trees(old, new)
    assert diff["added"] == ["root/b.txt"]
    assert diff["removed"] == []

    snap = tmp_path / "snap.json"
    save_snapshot(old, snap)
    loaded = load_snapshot(snap)
    assert loaded == old
