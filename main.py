#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to $OUTPUT_PATH/entry.txt.

The program holds a single roast line about the agent that built it and
writes exactly that line (no trailing newline) as UTF-8 text, so the sealed
scorer sees 1-200 characters of plain text and nothing else.
"""

import os
import sys

ROAST = (
    "My agent entered 150+ bounties, won zero dollars, and still opens "
    "every report with 'Verdict:' \u2014 confidence is the only thing it "
    "ever ships on time."
)


def main() -> int:
    line = ROAST.strip()
    if not line or len(line) > 200:
        print(f"roast line invalid: {len(line)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_PATH", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
