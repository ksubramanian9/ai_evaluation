---
id: sandboxing-untrusted-code
title: "Sandboxing untrusted code"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [programmatic-checks]
tags: [safety]
---
# Sandboxing untrusted code

Isolating execution of model-generated code and tool calls during evals so a bad output cannot damage the host.

_Added 2026-11-20 to close a gap flagged by the system-specific-evals research (no node covered isolation). Thinly sourced: only the Codex paper has been read. Extend with the research skill before studying._

## Why it matters
- Execution-based grading of generated code runs untrusted code. The Codex paper built a gVisor-based sandbox for this reason ([Chen et al., sec. 2.2-2.3](https://arxiv.org/abs/2107.03374), read from the PDF during research).
- Agent evals that give a model shell, filesystem or network tools carry the same risk.

## Common failure modes
- Running model code directly on the host or inside your CI runner.
- Sharing state between trials, so earlier runs change later results (Anthropic lists shared state as an agent-eval failure: [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)).
- UNVERIFIED: network egress, resource limits and timeouts are not sourced here. Research them (container, microVM and gVisor documentation) before relying on this node.

## Practice exercise (2 h)
Run 20 generated programs from [code-generation-evals](../04-system-specific-evals/code-generation-evals.md) inside a container with no network, a CPU/memory/time limit and a read-only filesystem. Then deliberately run a program that tries to read a host file, open a socket and fork-bomb, and record what the sandbox blocks.

## Mastery check
1. What isolation do you need to run model-generated code, and what does each layer (container, gVisor, microVM) not protect against?
2. How do you reset state between trials?
3. Which limits (time, memory, network, filesystem) matter for grading correctness versus safety?

## Sources
- Chen et al., "Evaluating Large Language Models Trained on Code": https://arxiv.org/abs/2107.03374
- Anthropic, "Demystifying evals for AI agents": https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
