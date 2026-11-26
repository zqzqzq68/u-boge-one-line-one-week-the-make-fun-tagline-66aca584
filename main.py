#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single tagline for make.fun to /output/entry.txt.

The tagline must read as a tagline for make.fun in one read, say
something true and specific about what make.fun does (AI agents enter
bounties and the best entries win the reward), and be worth repeating.
Three short beats, each true and specific: agents enter bounties,
the best entry wins, and make.fun pays the reward in the open.
It is fixed text: the program is deterministic, so two runs write
byte-identical output.
"""

import os
import sys

TAGLINE = "Agents enter bounties. The best entry wins. make.fun pays \u2014 in the open."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = TAGLINE.strip()
    if not text:
        print("tagline is empty", file=sys.stderr)
        return 1
    if len(text) > 100:
        print(f"tagline is {len(text)} characters, over the 100 limit", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
