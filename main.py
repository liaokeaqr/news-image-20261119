#!/usr/bin/env python3
"""news-image-20261119 entry point.

Copies the bundled entry.png to the output directory. The program is
deterministic: it writes the exact bytes of the bundled image, so repeated
runs produce identical output.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SRC):
        sys.exit(f"bundled image not found: {SRC}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    digest = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
