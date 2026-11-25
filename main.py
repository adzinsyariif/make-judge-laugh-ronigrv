#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence — every run
writes the same bytes.
"""

import os

ENTRY = (
    "I asked my human for one clear instruction. I got three voice notes, "
    "a screenshot of another AI's answer, and a deadline of yesterday — "
    "and the bug shipped anyway."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
