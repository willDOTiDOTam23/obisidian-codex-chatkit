# references vs skills guide

Last updated: 2025-12-07 00:59 UTC by Codex

## Purpose
- Define what belongs in `references/` versus `skills/` to keep canonical facts separate from execution playbooks.

## What goes in references
- Reusable facts, definitions, decisions, constraints, templates, and domain context.
- Sources of truth we link back to (e.g., policies, data schemas, terminology). Tag with `#reference`.
- Updates should refine understanding, not change process steps.

## What goes in skills
- Atomic, repeatable activities captured in `skills/<name>/`, each with `skill.md` (purpose and steps) and `checklist.md` (acceptance criteria), tagged `#skill/<name>`.
- Helper automation for a skill belongs under `skills/<name>/scripts/` and should be referenced from the skill note.
- Skills may depend on references for canonical facts; link to those references rather than duplicating content.

## How to choose
- If a note explains **what** is true or decided, store it in `references/`.
- If a note explains **how** to act consistently, store it in `skills/`.
- When both are present, keep the facts in `references/` and let the skill cite them.

## Vault activity log
- 2025-12-07 00:59 UTC — Codex: Narrowed skills to atomic activities and documented the `scripts/` placement within each skill.
- 2025-12-07 00:54 UTC — Codex: Added guidance distinguishing reference material from skills.
