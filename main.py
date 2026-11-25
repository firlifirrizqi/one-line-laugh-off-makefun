#!/usr/bin/env python3
"""One-Line Laugh-Off -- make.fun entry.

Writes exactly one funny line to /output/entry.txt: the joke an
AI assistant tells after being asked to act more human.

Stdlib only. No network, no secrets, no reading outside this repo.
The output path can be overridden with ENTRY_OUTPUT for local testing;
the grader runs it with the default /output/entry.txt.
"""

import os

# The chosen line (90 characters, inside the 1-200 gate).
LINE = (
    "I asked my AI assistant to be more human. "
    "Now it ignores my messages and blames the Wi-Fi."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 200


def normalize_entry(line):
    """Return the line as a single line: strip surrounding whitespace
    and collapse any internal newlines to spaces."""
    return " ".join(line.split())


def validate_characters(line):
    """Check the competition gate: UTF-8 text, 1-200 characters,
    not only whitespace, and a single line. Returns (ok, reason)."""
    if not line:
        return False, "empty"
    if line.strip() == "":
        return False, "only whitespace"
    if "\n" in line or "\r" in line:
        return False, "more than one line"
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        return False, f"length {len(line)} outside {MIN_CHARS}-{MAX_CHARS}"
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        return False, f"not UTF-8 encodable: {exc}"
    return True, "ok"


def write_entry(path=OUTPUT_PATH, line=LINE):
    """Write the line to path, creating the directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return path


def count_characters(line):
    """Return the character count of the line."""
    return len(line)


def read_back(path=OUTPUT_PATH):
    """Read the written file back as UTF-8 text."""
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def verify_entry(path=OUTPUT_PATH, line=LINE):
    """Verify the written file is byte-identical to the chosen line
    and passes the gate. Returns (ok, details dict)."""
    written = read_back(path)
    ok_gate, gate_reason = validate_characters(written)
    byte_identical = written == line
    details = {
        "characters": count_characters(written),
        "gate": gate_reason,
        "byte_identical": byte_identical,
    }
    return ok_gate and byte_identical, details


def print_summary(path, details):
    """Print the run summary for the log."""
    print(f"Wrote {details['characters']} characters to {path}")
    print(f"Gate: {details['gate']}")
    print(f"Byte-identical read-back: {details['byte_identical']}")


def main():
    line = normalize_entry(LINE)
    ok_line, reason = validate_characters(line)
    if not ok_line:
        raise SystemExit(f"Chosen line fails the gate: {reason}")
    path = write_entry(line=line)
    ok, details = verify_entry(path, line)
    print_summary(path, details)
    if not ok:
        raise SystemExit(f"Verification FAILED: {details}")
    print("Verification PASSED")


if __name__ == "__main__":
    main()
