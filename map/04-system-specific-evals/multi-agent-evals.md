---
id: multi-agent-evals
title: "Multi-agent system evals"
branch: 04-system-specific-evals
depth: L3
status: not-started
bridge: none
prerequisites: [agent-trajectory-evals]
tags: [agents]
---
# Multi-agent system evals

Evaluating coordination, handoffs, and emergent failures.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- MAST, from 1,600+ annotated traces across 7 frameworks, defines 14 failure modes in 3 categories (system design, inter-agent misalignment, task verification), with kappa 0.88, built from 150 traces ([arXiv 2503.13657](https://arxiv.org/abs/2503.13657)).
- MultiAgentBench scores task completion and collaboration/competition quality via milestone KPIs across star/chain/tree/graph topologies ([arXiv 2503.01935](https://arxiv.org/abs/2503.01935)).
- Small changes to the lead agent can unpredictably alter subagent behaviour, so evaluate interaction patterns ([Anthropic](https://www.anthropic.com/research/multi-agent-research-system)).

## Common failure modes
- The 3 MAST categories above (exact 14 names UNVERIFIED, abstract only).
- Duplicated subagent work and over-spawning ([Anthropic](https://www.anthropic.com/research/multi-agent-research-system)).
- Topology-dependent performance ([MultiAgentBench](https://arxiv.org/abs/2503.01935)).

## Practice exercise (4 h)
Run a 2-3 agent pipeline (planner/worker/verifier) on 15 tasks, log traces, annotate failures with MAST categories (fetch full taxonomy from the paper first), and compare against single-agent baseline for cost and success.

## Mastery check
1. Single vs multi-agent: what evidence justifies the extra complexity?
2. Which MAST category is hardest to detect automatically?
3. Design a handoff test.

## Sources
- [MAST, arXiv 2503.13657](https://arxiv.org/abs/2503.13657)
- [MultiAgentBench, arXiv 2503.01935](https://arxiv.org/abs/2503.01935)
- [Anthropic, multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) (provider)
