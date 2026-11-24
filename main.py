#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — one-line entry.

Writes a single joke (under 200 characters) to /output/entry.txt
about office life: a real joke, a surprise at the end, and a truth
every office worker recognizes.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The joke: a meeting about too many meetings — and it ran over.
# Counted at 76 characters — inside the 1..199 window.
LINE = (
    "I scheduled a meeting to discuss why we have too many "
    "meetings. It ran over."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the joke to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
