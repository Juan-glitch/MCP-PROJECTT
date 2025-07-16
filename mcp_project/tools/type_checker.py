# --- FastMCP integration header ---
import json
from typing import List, Callable
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("type_checker")

# --- End FastMCP header ---

import ast
import inspect
from typing import get_type_hints

@mcp.tool()
def detect_type_problems(func: Callable) -> List[str]:
    """
    Detect type problems in the signature of a function.

    Args:
        func: The function to analyze.

    Returns:
        List of problems found in the type annotations.
    """
    # Get the function signature (parameters and return type)
    signature = inspect.signature(func)
    # Get the type hints for parameters and return value
    type_hints = get_type_hints(func)
    problems = []

    # Check each parameter in the function signature
    for param in signature.parameters.values():
        # If the parameter has no type annotation
        if param.annotation == inspect.Parameter.empty:
            problems.append(f"Parameter '{param.name}' has no type annotation")
        # If the annotation is not present in type hints
        elif param.annotation not in type_hints:
            problems.append(f"Type annotation '{param.annotation}' for parameter '{param.name}' not found in type hints")

    # Check the return annotation
    if signature.return_annotation == inspect.Signature.empty:
        problems.append("Return value has no type annotation")
    elif signature.return_annotation not in type_hints:
        problems.append(f"Return type annotation '{signature.return_annotation}' not found in type hints")

    # Check for unknown types in type hints
    for name, type_ in type_hints.items():
        if type_ == inspect._empty:
            problems.append(f"Unknown type for '{name}' in type hints")

    # If no problems were found, add a verbose message
    if not problems:
        problems.append("No type problems detected. All parameters and return value are properly annotated.")

    return problems

if __name__ == "__main__":
    # Start FastMCP server using stdio transport
    mcp.run(transport='stdio')