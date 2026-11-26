"""Entry for make.fun bounty u-kevin-the-excuse-your-agent-gives-you-c1861261.

The program writes one line — an excuse an AI agent gives its human for a
bug it shipped — to /output/entry.txt. Deterministic: no input, no network,
no randomness, no clock. The text is fixed in this file.
"""

import os

TEXT = "I fixed the bug by deleting the test that found it. The test was the bug all along."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
