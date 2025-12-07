#!/usr/bin/env python3
"""
Convert a Markdown file to DOCX using the Pandoc CLI.

Usage:
    python convert.py input.md [output.docx]
"""
import argparse
import subprocess
from pathlib import Path
import sys


def run() -> int:
    parser = argparse.ArgumentParser(description="Convert Markdown to DOCX via Pandoc.")
    parser.add_argument("input_md", type=Path, help="Path to the Markdown file.")
    parser.add_argument(
        "output_docx",
        type=Path,
        nargs="?",
        help="Optional output DOCX path (defaults to input stem).",
    )
    args = parser.parse_args()

    input_md: Path = args.input_md
    output_docx: Path = args.output_docx or input_md.with_suffix(".docx")

    if not input_md.is_file():
        parser.error(f"Input does not exist or is not a file: {input_md}")

    output_docx.parent.mkdir(parents=True, exist_ok=True)

    cmd = ["pandoc", str(input_md), "-o", str(output_docx)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        return result.returncode

    print(f"Wrote {output_docx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
