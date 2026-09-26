#!/usr/bin/env python3
"""Build the symlink-free archive used by Claude Desktop."""

from __future__ import annotations

import argparse
import stat
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "SKILL.md"
ARCHIVE_PATH = "humanizer/SKILL.md"


def build_archive(output: Path) -> None:
    source_bytes = SOURCE.read_bytes()
    output.parent.mkdir(parents=True, exist_ok=True)

    skill = ZipInfo(ARCHIVE_PATH)
    skill.compress_type = ZIP_DEFLATED
    skill.create_system = 3
    skill.external_attr = (stat.S_IFREG | 0o644) << 16

    with ZipFile(output, "w") as archive:
        archive.writestr(skill, source_bytes)

    with ZipFile(output) as archive:
        entries = archive.infolist()
        if [entry.filename for entry in entries] != [ARCHIVE_PATH]:
            raise SystemExit(f"Archive must contain only {ARCHIVE_PATH}")

        mode = entries[0].external_attr >> 16
        if not stat.S_ISREG(mode):
            raise SystemExit(f"{ARCHIVE_PATH} must be a regular file")
        if archive.read(ARCHIVE_PATH) != source_bytes:
            raise SystemExit(f"{ARCHIVE_PATH} must match the root SKILL.md")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Path for the generated ZIP file")
    args = parser.parse_args()

    build_archive(args.output)
    print(f"Built Claude Desktop package: {args.output}")


if __name__ == "__main__":
    main()
