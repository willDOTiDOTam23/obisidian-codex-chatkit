# dev-setup

Last updated: 2025-12-06 17:44 MST by Codex

## Purpose
- Document the recommended local environment for this vault.

## Python environment
- Created `.venv/` with `python -m venv .venv`.
- Activate: `source .venv/bin/activate` (POSIX) or `.venv\\Scripts\\activate` (Windows).
- Install packages: `pip install -r requirements.txt` (installs `qrcode[pil]`; Pandoc remains a system dependency).

## Tools
- Pandoc: required for `markdown-to-docx`; install via system package manager (e.g., `brew install pandoc`).

## Node/TypeScript environment
- Requires Node.js >= 18.
- Install deps: `npm install` (installs `@openai/codex-sdk`, TypeScript, ts-node).
- Type-check/build: `npm run typecheck` or `npm run build`.
- Demo the Codex SDK: set `CODEX_API_KEY` and run `npm run codex:demo`.

## Tests
- Run with: `python -m unittest discover tests`.
- Tests skip gracefully if Pandoc or `qrcode` are not installed.

## Vault activity log
- 2025-12-06 17:44 MST — Codex: Added Node/TypeScript setup for Codex SDK.
- 2025-12-06 17:35 MST — Codex: Added dev setup and testing instructions.
