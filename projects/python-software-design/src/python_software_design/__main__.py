"""Command line entry point for python-software-design."""

from __future__ import annotations

import argparse

from . import __version__


def main(argv: list[str] | None = None) -> int:
    """Run the command line interface."""
    parser = argparse.ArgumentParser(prog="python-software-design")
    parser.add_argument("--version", action="version", version=__version__)
    parser.parse_args(args=argv)
    print("Hello from python-software-design.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
