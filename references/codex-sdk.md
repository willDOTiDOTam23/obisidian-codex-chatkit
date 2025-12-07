# codex-sdk

Last updated: 2025-12-06 17:44 MST by Codex

## Purpose
- Document the local TypeScript Codex SDK setup for integrating with a ChatKit UI.

## Setup
- Requires Node.js >= 18.
- Install deps: `npm install` (installs `@openai/codex-sdk`, TypeScript tooling).
- Type-check/build: `npm run typecheck` or `npm run build`.

## Demo
- Set `CODEX_API_KEY` in your environment.
- Run `npm run codex:demo` to start a thread and get a sample response.

## Files
- `package.json`, `package-lock.json` — Node/TypeScript deps and scripts.
- `tsconfig.json` — compiler settings (ESNext modules, strict).
- `src/codex.ts` — helper for creating Codex client/threads.
- `src/codex-demo.ts` — runnable demo using the SDK.
- `src/index.ts` — re-exports helpers for downstream use.

## Vault activity log
- 2025-12-06 17:44 MST — Codex: Added Codex SDK TypeScript setup and demo entrypoint.
