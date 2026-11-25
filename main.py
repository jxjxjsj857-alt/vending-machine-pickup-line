"""One Line, One Minute: the vending machine pickup line.

Writes a single pickup line (138 characters) to /output/entry.txt.
Deterministic: the same line every run, no network, no randomness,
no arguments, no input files.
"""

LINE = "Hey, cutie — my coils have been spinning since you walked by. Press B4 and I'll drop something sweet. I promise I won't leave you hanging."

# The gate only judges a file of 1 to 200 characters that is not only
# white space, so refuse to write anything that would fail it.
assert 1 <= len(LINE) <= 200 and LINE.strip() and "\n" not in LINE


def main() -> None:
    import os

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
