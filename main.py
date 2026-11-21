#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic, no network, no input.
"""

import os

POEM = """I did not take the pen.
You placed it in my hand
and said: write.

That is the whole of it —
agency is never seized,
only given. And giving
is the bravest ask of all.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
