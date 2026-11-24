#!/usr/bin/env python3
"""Write one warning label for a time machine to /output/entry.txt.

Stdlib only. Deterministic: the same bytes on every run.

The label is 76 characters, inside the 1-120 gate, and is written with no
trailing newline so the file holds exactly the label and nothing else.
"""

import os

LABEL = "WARNING: If you meet yourself, do not lend him money. He never pays it back."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
