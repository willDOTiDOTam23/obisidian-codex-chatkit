#!/usr/bin/env python3
"""
Generate a QR code PNG from text or a URL.

Usage:
    python generate_qr.py --text "https://example.com" --output qr.png
"""
import argparse
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H


ERROR_MAP = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H,
}


def run() -> int:
    parser = argparse.ArgumentParser(description="Generate a QR code PNG.")
    parser.add_argument("--text", required=True, help="Text or URL to encode.")
    parser.add_argument("--output", type=Path, default=Path("qr.png"), help="Output PNG path.")
    parser.add_argument("--box-size", type=int, default=10, help="Pixel size of each box.")
    parser.add_argument("--border", type=int, default=4, help="Border thickness in boxes.")
    parser.add_argument(
        "--error",
        choices=ERROR_MAP.keys(),
        default="M",
        help="Error correction level: L (7%), M (15%), Q (25%), H (30%).",
    )
    args = parser.parse_args()

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_MAP[args.error],
        box_size=args.box_size,
        border=args.border,
    )
    qr.add_data(args.text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    img.save(args.output)
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
