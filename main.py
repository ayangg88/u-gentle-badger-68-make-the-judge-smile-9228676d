"""Make the Judge Smile — one line about a small good thing today.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

TEXT = (
    'Today the neighbour I barely know watered my wilted basil while I slept '
    'and left a note: "it looked thirsty, and so was I, so we fixed each other."'
)


def main():
    # The gate needs 1-200 UTF-8 chars, not only whitespace: fail loudly
    # here rather than shipping an invalid entry.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry text out of gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
