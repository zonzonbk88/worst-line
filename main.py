"""Entry for make.fun bounty "The Worst Line an AI Could Say".

Writes one pickup line -- the worst an AI could plausibly say -- to
/output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1-140 characters, one line,
not only whitespace. No trailing newline is written.
"""

LINE = "I analysed all 4,096 of your photos and I am 97.3% sure you will say yes."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
