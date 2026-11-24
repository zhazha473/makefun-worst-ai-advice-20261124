"""Worst AI Advice: The 48-Hour Tight Line Open.

One line of the worst advice an AI assistant could give, written
deterministically to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13, standard library only, no network access.
"""

import os

ENTRY = (
    "Delete your backups to save disk space \u2014 old copies just slow you "
    "down. Trust me, you'll only ever need the latest version. Probably."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
