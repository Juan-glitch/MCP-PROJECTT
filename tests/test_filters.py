from pathlib import Path
from mcp_project.core.enrich import enrich_node


def test_enrich_node(tmp_path: Path) -> None:
    file_path = tmp_path / "file.txt"
    file_path.write_text("data")
    node = {"type": "file", "name": "file.txt"}
    enriched = enrich_node(node, file_path)
    assert "size" in enriched and enriched["size"] > 0
    assert enriched.get("classification") == "code" or enriched.get("classification") == "other"
