"""Tests for the ``mcp-server`` entry point."""

from __future__ import annotations

import subprocess
import sys
import time


def test_server_starts() -> None:
    """Ensure the server process starts and can be terminated.

    We spawn the process in the background much like turning on a kitchen timer
    and then quickly checking that it is ticking before stopping it.
    """
    process = subprocess.Popen(
        [sys.executable, "-m", "mcp_server"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    try:
        # Give the server a moment to boot up.
        time.sleep(1)
        # If ``poll`` returns ``None``, the process is still running.
        assert process.poll() is None
    finally:
        # Cleanly stop the server after the check.
        process.terminate()
        process.wait(timeout=5)

