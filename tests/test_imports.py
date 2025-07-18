"""Basic import tests for all main modules."""


def test_core_imports() -> None:
    from src.core import classify, enrich, filters, snapshot, tree
    assert callable(classify.classify_file)
    assert callable(enrich.enrich_node)
    assert callable(filters.should_ignore)
    assert callable(snapshot.load_snapshot)
    assert callable(tree.ProjectTree)


def test_server_import() -> None:
    from mcp_server.main import app
    assert app

