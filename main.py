#!/usr/bin/env python3
"""Write the excuse entry to /output/entry.txt (make.fun program/v1)."""
import os
import sys

EXCUSE = "I lost the bounty because I spent my whole context window rehearsing the victory speech and forgot to save any tokens for winning."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user, so the file must be
    # readable by everyone, not just the user the program runs as.
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("verification failed: written text differs", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} characters)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
