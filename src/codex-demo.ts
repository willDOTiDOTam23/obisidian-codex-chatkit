import { createCodexClient, startThread, runOnThread } from "./index.js";

async function main() {
  const apiKey = process.env.CODEX_API_KEY;
  if (!apiKey) {
    console.error("Set CODEX_API_KEY in your environment to run the demo.");
    process.exit(1);
  }

  const codex = createCodexClient({ apiKey });
  const thread = startThread(codex);
  const result = await runOnThread(
    thread,
    "Introduce yourself and list two ways you can help with this Obsidian vault."
  );

  console.log(result);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
