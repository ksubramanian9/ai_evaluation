---
id: eval-driven-development
title: "Eval-driven development"
branch: 02-eval-design
depth: L2
status: not-started
bridge: testing
prerequisites: [golden-datasets, baselines-and-thresholds]
tags: []
---
# Eval-driven development

Writing evals first and iterating on the system against them, the analogue of test-driven development.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

## Why it matters
OpenAI: "Adopt eval-driven development: Evaluate early and often" because outputs vary; anti-patterns include vibe-based evals [OAI-BP]. Anthropic: write evals for planned capabilities before agents can do them, iterate to the bar; promote saturated capability evals to regression suites; read transcripts [ANTH-AGENT]. Anthropic recommends success criteria first, volume over per-item quality with automated grading [CLAUDE-EVAL].
## Common failure modes
Evals added after shipping [OAI-BP]; overfitting to the dev eval (UNVERIFIED in sources; relates to contamination/Goodhart); grader bugs mistaken for model failures [ANTH-AGENT]; criteria change mid-loop [Shankar](https://arxiv.org/abs/2404.12272); no holdout.
## Practice exercise
Start with 20 failing cases for a prompt task before editing the prompt; iterate prompt versions, logging pass rate with CI; keep a hidden holdout of 20 and check dev vs holdout divergence at the end.
## Mastery check
(1) Show the red-green loop for a prompt change. (2) How do you tell prompt overfitting from real improvement? (3) When to promote a case to regression?
## Sources
[OAI-BP]; [ANTH-AGENT]; [CLAUDE-EVAL]; https://arxiv.org/abs/2404.12272. Practitioner not collected.
