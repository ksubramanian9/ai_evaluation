---
id: agent-trajectory-evals
title: "Agent trajectory evaluation"
branch: 04-system-specific-evals
depth: L3
status: not-started
bridge: none
prerequisites: [agent-task-success-evals, llm-as-judge]
tags: [agents, llm-judge]
---
# Agent trajectory evaluation

Evaluating intermediate steps, planning, tool choice, and efficiency, not only the final result.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Success rate alone "reveals little about where an agent succeeds or fails along the way"; AgentBoard adds a fine-grained progress rate ([arXiv 2401.13178](https://arxiv.org/abs/2401.13178); computation details UNVERIFIED).
- Agent-as-a-Judge gives intermediate feedback on the process; on DevAI (55 tasks, 365 requirements) it is reported to outperform LLM-as-a-judge and approach human reliability (abstract only; no numbers read) ([arXiv 2410.10934](https://arxiv.org/abs/2410.10934)).
- Counterpoint: agents can reach the same goal via different valid paths, so judge end states, with checkpoints at key state changes for complex flows ([Anthropic multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system)).
- Avoid rigid step grading ([Anthropic evals doc](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Ragas lists Tool Call Accuracy, Agent Goal Accuracy, Topic Adherence (as of release; volatile) ([docs](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)).

## Common failure modes
- Over-penalizing valid alternate paths ([Anthropic](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Observed behaviours: 50 subagents for simple queries, endless search for nonexistent sources, duplicated work, overly long queries, continuing after enough results ([Anthropic multi-agent post](https://www.anthropic.com/research/multi-agent-research-system)); tool-efficiency as rubric dimension.
- Judge reliability on long traces (UNVERIFIED).

## Practice exercise (3 h)
Using transcripts from the agent-task-success exercise, add per-step labels (useful / redundant / wrong tool), compute a progress-rate-like metric (milestones reached / total), step-count and redundant-call ratios; test whether trajectory metrics predict outcome failures.

## Mastery check
1. When is trajectory grading warranted vs outcome only?
2. Define milestones for a task.
3. What does progress rate expose that success hides?
4. Risks of agent-judges.

## Sources
- [AgentBoard, arXiv 2401.13178](https://arxiv.org/abs/2401.13178)
- [Agent-as-a-Judge, arXiv 2410.10934](https://arxiv.org/abs/2410.10934)
- [Anthropic, multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) (provider)
- [Anthropic, "Demystifying evals for AI agents"](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) (provider)
- [Ragas available metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
