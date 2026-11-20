---
id: agent-task-success-evals
title: "Agent task success"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: none
prerequisites: [task-definition-and-success-criteria, nondeterminism-and-variance]
tags: []
---
# Agent task success

Outcome-based evaluation of whether an agent completed the task.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** pass@k and pass^k are defined once in [nondeterminism-and-variance](../01-foundations/nondeterminism-and-variance.md#passk-and-passk-owned-here).

## Why it matters
Outcome-based grading, environment-state checked: Anthropic defines outcome as final environment state (e.g. reservation exists in DB), recommends grading outcome rather than rigid step sequences, 20-50 tasks from real failures to start, and distinguishes pass@k from pass^k ([Anthropic Engineering, "Demystifying evals for AI agents"](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), provider engineering doc). Benchmarks: WebArena uses functional correctness; best GPT-4 agent 14.41% vs human 78.24% ([arXiv 2307.13854](https://arxiv.org/abs/2307.13854)); GAIA 466 questions, humans 92% vs GPT-4+plugins 15% ([arXiv 2311.12983](https://arxiv.org/abs/2311.12983)); OSWorld 369 tasks with per-task execution-based scripts, human >72.36% vs best model 12.24% ([arXiv 2404.07972](https://arxiv.org/abs/2404.07972)); AgentBench 8 environments, ICLR 2024 ([arXiv 2308.03688](https://arxiv.org/abs/2308.03688)). Scores are as of paper date; current frontier numbers are much higher [V] (UNVERIFIED, not looked up).

## Common failure modes
- Broken tasks/grader bugs (near-0% pass often means a flawed eval); agents cheating; shared state between trials; saturation (Anthropic doc).
- One-sided evals (only testing when behavior should occur).
- Single-run reporting hides unreliability (tau-bench pass^k).
- Poor long-term reasoning, decision-making, instruction following dominate failures in AgentBench (abstract).

## Practice exercise
Build a toy agent task suite (e.g. 20 tasks over a SQLite DB: "refund order X"), a state-based grader, run 5 trials each, report pass@1, pass@5, pass^5; hand-inspect 5 transcripts for grader bugs.

## Mastery check
(1) Why state-based over claim-based success? (2) When pass@k vs pass^k? (3) Diagnose a 0% task. (4) Design a capability vs regression split.

## Sources
Anthropic doc (provider); tau-bench; WebArena; GAIA; OSWorld; AgentBench.
