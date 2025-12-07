# agents

Last updated: 2025-12-06 18:20 MST by Codex

## Purpose
- Define how humans and agents collaborate in this vault; keep contributions predictable and auditable.

## Timestamping
- Every edited note adds `Last updated: YYYY-MM-DD HH:MM ZZZ by <author>` under the H1, using `Codex` as the author name for our contributions.
- Log meaningful edits under a `## Vault activity log` section in the changed note.

## Structure
- Top-level today: `intake/`, `references/`, `skills/`, `data/sqlite/`, `data/graphs/`.
- Keep filenames in lowercase kebab-case (e.g., `readme.md`, `starter-kit/` assets). Use folder-qualified links when titles could collide.
- Add an `index.md` once a folder holds ~5+ notes to aid navigation, and keep each index linking to all folders and notable files within its directory. Update indexes when adding, moving, or renaming content so navigation stays accurate.

## Navigation and linking
- Prefer Obsidian wikilinks `[[note-name]]` for internal references; use descriptive text for external URLs.
- Tag consistently (e.g., `#intake/new`, `#skill/<name>`). Document new tag patterns in `references/hashtags-guide.md` when added.
- Cross-link related notes; update indexes when moving or creating content.

## Datastores and retrieval
- Treat Markdown notes, SQLite databases, and Neo4j graphs as first-class sources.
- Choose storage intentionally (see `skills/datastore-selection/skill` for a quick decision path):
  - Markdown for narrative, rationale, and guides.
  - SQLite for structured/tabular records that need filters/aggregations.
  - Neo4j for relationship-heavy domains and traversals.
- Keep `references/datastores-catalog.md` current with locations, schemas, and example queries.

## Intake and curation
- New, rough notes land in `intake/` tagged `#intake/new`; add a short summary and activity log entry.
- Normalize formatting, links, and filenames before moving a note to its destination folder.
- After moving, update the relevant `index.md` with a one-line link and verify backlinks.

## Safety
- Do not store secrets. Link to secure systems instead.
- For destructive or expensive actions (e.g., schema changes, bulk imports), seek explicit human confirmation first.

## Skills
- Each skill lives in `skills/<name>/` with `skill.md` (purpose, inputs, steps, outputs) and `checklist.md` (acceptance criteria), tagged `#skill/<name>`.
- Include scripts when they make execution safer or faster; keep usage documented in the skill.

## Vault activity log
- 2025-12-06 18:20 MST — Codex: Standardized Codex attribution for vault updates and clarified timestamp guidance.
- 2025-12-06 17:48 MST — Codex: Added index maintenance expectations across the vault.
- 2025-12-06 17:35 MST — Codex: Added dev setup guidance, starter indexes, tag baseline, tests, and tracked vault config.
- 2025-12-06 17:29 MST — Codex: Deduplicated guidance, created scaffolding folders, and added initial skill stubs.
