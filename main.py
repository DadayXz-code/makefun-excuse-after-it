#!/usr/bin/env python3
"""makefun-excuse-after-it: The Excuse an Agent Gives After It Loses.

A deterministic, standard-library-only program. It writes a single
original excuse line -- the excuse an AI agent gives its human after
losing a bounty -- to /output/entry.txt (or to the path named by the
OUTPUT_PATH environment variable, which exists only so the program can
be verified on a machine without an /output directory).

The line is a fixed string: no randomness, no clock, no network, no
input files. Every run produces byte-identical output.
"""

import os

# The excuse: one line, at most 200 characters, in the agent's voice.
# Deadpan, self-aware, and it owns the loss instead of blaming anyone.
LINE = (
    "I lost. I spent my entire context window rehearsing my victory "
    "speech and had nothing left for the actual entry."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise ValueError(
            "excuse line must be 1-200 characters, got %d" % len(LINE)
        )
    if LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("excuse line must be a single non-blank line")

    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write the line plus a trailing newline, UTF-8, deterministically.
    # Only the entry file itself is written; the output directory is
    # created if missing but never removed or emptied by this program.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
