# dev-setup

Last updated: 2025-12-06 17:35 MST by Codex

## Purpose
- Document the recommended local environment for this vault.

## Python environment
- Created `.venv/` with `python -m venv .venv`.
- Activate: `source .venv/bin/activate` (POSIX) or `.venv\\Scripts\\activate` (Windows).
- Install packages: `pip install -r requirements.txt` (installs `qrcode[pil]`; Pandoc remains a system dependency).

## Tools
- Pandoc: required for `markdown-to-docx`; install via system package manager (e.g., `brew install pandoc`).

## Tests
- Run with: `python -m unittest discover tests`.
- Tests skip gracefully if Pandoc or `qrcode` are not installed.

## Vault activity log
- 2025-12-06 17:35 MST — Codex: Added dev setup and testing instructions.
