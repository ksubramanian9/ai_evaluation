---
id: golden-datasets
title: "Golden datasets"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [task-definition-and-success-criteria]
tags: []
---
# Golden datasets

Building and maintaining curated reference sets of inputs and expected behavior.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

## Why it matters
Start small: "20-50 simple tasks drawn from real failures"; good task = two domain experts reach the same verdict; use reference solutions; balance should/shouldn't-happen cases [ANTH-AGENT]. Datasets should come from production data, expert references, synthetic data, historical logs, covering typical/edge/adversarial cases [OAI-BP]. Anthropic: mirror real task distribution, include edge cases (irrelevant/overly long input, ambiguity) [CLAUDE-EVAL]. Benchmarks need reliability, annotation quality, headroom [Bowman & Dahl](https://arxiv.org/abs/2104.02145) (abstract cites dataset design, annotation reliability, size, social bias as needed repairs).
## Common failure modes
Datasets that don't reproduce production traffic [OAI-BP]; one-sided sets that reward overdoing a behavior [ANTH-AGENT]; broken tasks (near-zero scores likely mean broken task/grader) [ANTH-AGENT]; saturation (eval stops discriminating once all solvable tasks pass; graduate to regression suite) [ANTH-AGENT]; unreliable/biased labels [Bowman & Dahl](https://arxiv.org/abs/2104.02145). Adversarial human-in-loop collection (Dynabench) is one remedy for saturation/fragility [Kiela et al.](https://arxiv.org/abs/2104.14337).
## Practice exercise
Mine 30 real/realistic failures for an app (or use a public QA set), write input + expected behavior + grader, include 10 negative cases, have a second person (or you a day later) independently label; report agreement and fix ambiguous items. Version the file with a changelog.
## Mastery check
(1) What makes a task "two experts agree"? (2) How would you detect a broken item? (3) When does a golden set become a regression suite and what replaces it?
## Sources
[ANTH-AGENT]; [OAI-BP]; [CLAUDE-EVAL]; https://arxiv.org/abs/2104.02145; https://arxiv.org/abs/2104.14337.
