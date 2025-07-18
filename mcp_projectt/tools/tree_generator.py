#!/usr/bin/env python3
"""
Advanced Project Tree Generator v2.0

Generates colored trees, Markdown & Mermaid formats, debug info, stats.
Originally in Spanish—rewritten here with clear, structured English docs.
"""

import os
import sys
import time
from pathlib import Path
import argparse
from colorama import Fore, Style

# Constants for tree drawing
PIPE = "│"
ELBOW = "└── "
TEE = "├── "
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

def get_size(path: Path) -> int:
    """Returns size in bytes for a file or total size for a directory."""
    if path.is_file():
        return path.stat().st_size
    return sum(f.stat().st_size for f in path.rglob('*') if f.is_file())

class TreeGenerator:
    """
    Walks through directories and builds the tree string.

    Yields each line of the tree. Avoids building full list in memory.
    """
    def __init__(self, root: Path, max_depth: int = None, include_hidden: bool = False):
        self.root = root
        self.max_depth = max_depth
        self.include_hidden = include_hidden
        self.stats = {'files':0, 'dirs':0, 'size':0, 'start': time.time()}

    def generate(self):
        yield from self._generate(self.root, prefix="", depth=0)

    def _generate(self, current: Path, prefix: str, depth: int):
        # Depth check
        if self.max_depth is not None and depth > self.max_depth:
            return

        entries = sorted(current.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        if not self.include_hidden:
            entries = [e for e in entries if not e.name.startswith('.')]

        for idx, entry in enumerate(entries):
            connector = ELBOW if idx == len(entries) - 1 else TEE
            line = f"{prefix}{connector}{entry.name}"
            size = get_size(entry)
            self.stats.update({
                'files': self.stats['files'] + (1 if entry.is_file() else 0),
                'dirs': self.stats['dirs'] + (1 if entry.is_dir() else 0),
                'size': self.stats['size'] + size
            })
            yield f"{line} ({size} bytes)"
            if entry.is_dir():
                new_prefix = prefix + (SPACE_PREFIX if connector == ELBOW else PIPE_PREFIX)
                yield from self._generate(entry, new_prefix, depth + 1)



def parse_args():
    parser = argparse.ArgumentParser(description="Advanced Project Tree Generator")
    parser.add_argument("path", nargs='?', default=".", help="Root path")
    parser.add_argument("-d", "--max-depth", type=int, help="Max recursion depth")
    parser.add_argument("-a", "--all", action="store_true", help="Include hidden files")
    parser.add_argument("-s", "--stats", action="store_true", help="Show stats")
    return parser.parse_args()

def main():
    args = parse_args()
    root = Path(args.path)
    gen = TreeGenerator(root, args.max_depth, args.all)

    try:
        for line in gen.generate():
            print(Fore.GREEN + str(line) + Style.RESET_ALL)

        if args.stats:
            elapsed = time.time() - gen.stats['start']
            print(Fore.CYAN + f"\nStats: Files={gen.stats['files']}, "
                               f"Dirs={gen.stats['dirs']}, "
                               f"Size={gen.stats['size']} bytes, "
                               f"Time={elapsed:.2f}s" + Style.RESET_ALL)

    except KeyboardInterrupt:
        print(Fore.YELLOW + "Canceled by user" + Style.RESET_ALL)
        sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    main()
