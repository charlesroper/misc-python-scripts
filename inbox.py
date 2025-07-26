#!/usr/bin/env python3
"""
This script allows you to quickly append timestamped notes to a designated
Obsidian scratch/inbox file.

- Prompts the user for multi-line input, ending with a blank line or Ctrl-D
  (EOF).

- Each entry is timestamped and formatted as a top-level bullet with sub-bullets
  for each line.

- The target file path is configurable at the top of the script.

- Useful for capturing quick notes or ideas directly into your Obsidian vault
  from the command line.
"""

from pathlib import Path
from datetime import datetime
import sys

# CONFIG: Define your vault-relative path here
scratch_path: Path = (
    Path.home() / "GDrive" / "Obsidian" / "Core" / "00 Top" / "001 Scratch.md"
)


def main() -> None:
    # Timestamp
    now: str = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Prompt the user (emoji retained)
    print("📝 Add a note to your Obsidian Inbox (end with a blank line):")

    lines: list[str] = []
    try:
        while True:
            line: str = input("> ")
            if not line.strip():
                break
            lines.append(line)
    except KeyboardInterrupt:
        # Friendly, emoji-aware exit
        print("\n📝 Cancelling! ❌")
        sys.exit(0)

    if lines:
        # Ensure file exists before writing
        scratch_path.parent.mkdir(parents=True, exist_ok=True)
        scratch_path.touch(exist_ok=True)

        with open(scratch_path, "a", encoding="utf-8") as f:
            # Write the timestamp as a top-level bullet
            f.write(f"\n{now}")
            # Write each line as an indented sub-bullet
            for entry_line in lines:
                f.write(f"\n\t- {entry_line}")
            # Ensure an extra line break at the end
            f.write("\n")
        print("✅ Entry added.")
    else:
        print("⚠️ No input received. Nothing added.")


if __name__ == "__main__":
    main()
