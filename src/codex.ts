import { Codex, type Thread } from "@openai/codex-sdk";

export type CodexClientOptions = {
  apiKey?: string;
};

export const createCodexClient = (options?: CodexClientOptions): Codex => {
  return new Codex({ apiKey: options?.apiKey });
};

export const startThread = (codex: Codex): Thread => codex.startThread();

export const resumeThread = (codex: Codex, threadId: string): Thread =>
  codex.resumeThread(threadId);

export const runOnThread = async (thread: Thread, prompt: string) => {
  return thread.run(prompt);
};
