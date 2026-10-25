#!/usr/bin/env python3
"""AC-C 1.x: a small C-compatible compiler driver."""
import argparse
import os
import shutil
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="acc",
        description="AC-C 1.x — C compiler driver powered by Clang",
        epilog="Example: python3 acc.py hello.c -o hello")
    parser.add_argument("--version", action="version", version="AC-C 1.0")
    parser.add_argument("--clang", help="Path to Clang executable")
    args, rest = parser.parse_known_args()
    if not rest:
        parser.print_help()
        return 0
    compiler = args.clang or shutil.which("clang")
    if not compiler:
        print("AC-C error: clang not found", file=sys.stderr)
        return 1
    command = [compiler, *rest]
    print("AC-C 1.x | compiling with Clang", flush=True)
    try:
        return subprocess.run(command, check=False).returncode
    except OSError as exc:
        print(f"AC-C error: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
