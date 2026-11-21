---
id: golden-datasets
title: "Golden datasets"
branch: 02-eval-design
depth: L3
status: not-started
bridge: none
prerequisites: [task-definition-and-success-criteria]
tags: [human-labels]
---
# Golden datasets

Building and maintaining curated reference sets of inputs and expected behavior.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Build a golden set from real failures with inputs, expected behavior, graders and negative cases.
- Measure independent-labeler agreement and fix ambiguous items.
- Detect broken items and saturation, and decide when a set graduates to a regression suite.
- Design a golden set's composition (sources, balance, edge cases) and critique one that is one-sided or does not mirror production traffic.

**Done bar.** Practiced: a versioned file of 30 cases (10 negative) with expected behavior and graders, a changelog, and an agreement report listing the items you fixed. Mastered: written answers to all three mastery-check questions, checked against Anthropic, OpenAI and Bowman & Dahl, plus a critique of a real or public golden set that finds a flaw this node covers (one-sided, broken items, saturation, unrepresentative of traffic) and states the trade-off of your fix.

## Why it matters
- Start small: "20-50 simple tasks drawn from real failures"; good task = two domain experts reach the same verdict; use reference solutions; balance should/shouldn't-happen cases ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Datasets should come from production data, expert references, synthetic data, historical logs, covering typical/edge/adversarial cases ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- Anthropic: mirror real task distribution, include edge cases (irrelevant/overly long input, ambiguity) ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Benchmarks need reliability, annotation quality, headroom ([Bowman & Dahl](https://arxiv.org/abs/2104.02145)); the abstract cites dataset design, annotation reliability, size, social bias as needed repairs.

## Common failure modes
- Datasets that don't reproduce production traffic ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- One-sided sets that reward overdoing a behavior ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Broken tasks (near-zero scores likely mean broken task/grader) ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Saturation (eval stops discriminating once all solvable tasks pass; graduate to regression suite) ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Unreliable/biased labels ([Bowman & Dahl](https://arxiv.org/abs/2104.02145)).
- Adversarial human-in-loop collection (Dynabench) is one remedy for saturation/fragility ([Kiela et al.](https://arxiv.org/abs/2104.14337)).

## Practice exercise (3-4 h)
Mine 30 real/realistic failures for an app (or use a public QA set), write input + expected behavior + grader, include 10 negative cases, have a second person (or you a day later) independently label; report agreement and fix ambiguous items. Version the file with a changelog.

## Mastery check
1. What makes a task "two experts agree"?
2. How would you detect a broken item?
3. When does a golden set become a regression suite and what replaces it?

## Sources
- [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Bowman & Dahl, What Will it Take to Fix Benchmarking in NLU?](https://arxiv.org/abs/2104.02145)
- [Kiela et al., Dynabench](https://arxiv.org/abs/2104.14337)
