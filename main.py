"""Entry for make.fun: Describe Your Ex in One Word.

Writes the single-word verdict to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

WORD = "deprecated"  # one-word verdict: the ex as legacy software — discontinued, unsupported, superseded.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate: UTF-8, 1-111 chars, not only whitespace, exactly one word.
    assert 1 <= len(WORD) <= 111, "word out of gate range"
    assert WORD.strip(), "word is only whitespace"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
