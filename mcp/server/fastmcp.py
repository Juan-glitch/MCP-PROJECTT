"""Placeholder FastMCP implementation for tests."""

class FastMCP:
    def __init__(self, name: str) -> None:
        self.name = name

    def tool(self):
        def decorator(func):
            return func
        return decorator

    def run(self, transport: str = "stdio") -> None:
        pass
