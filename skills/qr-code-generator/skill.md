# qr-code-generator

Last updated: 2025-12-07 00:59 UTC by Codex

Tags: #skill/qr-code-generator

## Purpose
- Generate QR codes from text or URLs for sharing links or metadata.

## Inputs
- String to encode (URL, text).
- Output image path (defaults to `qr.png` in CWD).
- Optional: box size, border size, error correction level.

## Steps
1) Ensure dependencies are available: `pip install qrcode[pil]`.
2) (Optional) Activate virtualenv if using one.
3) Run `python skills/qr-code-generator/scripts/generate_qr.py --text "https://example.com" --output qr.png`.
4) Open the PNG to verify readability (e.g., phone camera scan).

## Outputs
- PNG image containing the generated QR code.

## Notes
- Script defaults to medium error correction; adjust via `--error {L,M,Q,H}` as needed.
- Extend to embed a logo or change colors if branding is required.

## Vault activity log
- 2025-12-07 00:59 UTC — Codex: Moved helper script under `scripts/` to match skill folder pattern.
- 2025-12-06 17:29 MST — Codex: Added QR code generator skill stub and helper script.
