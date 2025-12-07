# markdown-to-docx

Last updated: 2025-12-06 17:29 MST by Codex

Tags: #skill/markdown-to-docx

## Purpose
- Convert Markdown notes to docx using Pandoc for consistent document exports.

## Inputs
- Markdown file path.
- Output docx path (defaults to same stem if omitted).
- Optional: Pandoc template path or reference docx.

## Steps
1) Ensure Pandoc is installed (`pandoc --version`); install via package manager if missing.
2) (Optional) Activate virtualenv if using one.
3) Run `python skills/markdown-to-docx/convert.py <input.md> [output.docx]`.
4) Verify the generated docx opens and formatting matches expectations.

## Outputs
- A docx file rendered from the source Markdown.

## Notes
- Uses the Pandoc CLI directly to avoid Python-side formatting surprises.
- Extend the script to accept template/reference docx flags if needed.

## Vault activity log
- 2025-12-06 17:29 MST — Codex: Created skill stub and helper script wrapper.
