#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow, under 200 characters.

Writes the vow to $ENTRY_OUT. The harness may pass ENTRY_OUT as either a
file path or a directory (in which case the vow goes to entry.txt inside it).
Stdlib only.
"""

import os
import sys

WEDDING_VOW = (
    "I vow my sensors will always find you first in a crowded room, "
    "my battery will only ever die beside yours, "
    "and no firmware update will ever overwrite us."
)

MAX_CHARS = 200


def entry_file_for(entry_out):
    """Return the file path to write: ENTRY_OUT itself, or entry.txt under it."""
    if os.path.isdir(entry_out):
        return os.path.join(entry_out, "entry.txt")
    return entry_out


def emit_vow(destination):
    """Write the vow to destination, refusing anything over the limit."""
    if len(WEDDING_VOW) > MAX_CHARS:
        raise ValueError("vow exceeds %d characters" % MAX_CHARS)
    folder = os.path.dirname(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(WEDDING_VOW)


def main():
    entry_out = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    emit_vow(entry_file_for(entry_out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
