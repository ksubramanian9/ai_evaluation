---
id: eval-driven-development
title: "Eval-driven development"
branch: 02-eval-design
depth: L2
status: not-started
bridge: testing
prerequisites: [golden-datasets, baselines-and-thresholds, statistical-inference]
tags: [statistics]
---
# Eval-driven development

Writing evals first and iterating on the system against them, the analogue of test-driven development.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** confidence intervals, power and paired comparisons are owned by [statistical-inference](../01-foundations/statistical-inference.md) and [confidence-intervals-for-evals](../03-measurement-methods/confidence-intervals-for-evals.md).

## Learning objectives
You can:
- Run a red-green loop: write failing cases before editing a prompt, then iterate until they pass.
- Log pass rate with a CI for each prompt version.
- Use a hidden holdout to tell prompt overfitting from real improvement.
- Decide when to promote a case to the regression suite.

**Done bar.** Practiced: a version log of pass rates with CIs starting from 20 failing cases, plus the dev-vs-holdout comparison at the end. Mastered: written answers to all three mastery-check questions, checked against the OpenAI and Anthropic guides, plus one real prompt or feature change (capstone or work) developed eval-first with its holdout result recorded.

## Why it matters
- OpenAI: "Adopt eval-driven development: Evaluate early and often" because outputs vary; anti-patterns include vibe-based evals ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- Anthropic: write evals for planned capabilities before agents can do them, iterate to the bar; promote saturated capability evals to regression suites; read transcripts ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Anthropic recommends success criteria first, volume over per-item quality with automated grading ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).

## Common failure modes
- Evals added after shipping ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- Overfitting to the dev eval (UNVERIFIED in sources; relates to contamination/Goodhart).
- Grader bugs mistaken for model failures ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Criteria change mid-loop ([Shankar](https://arxiv.org/abs/2404.12272)).
- No holdout.

## Practice exercise (2-3 h)
Start with 20 failing cases for a prompt task before editing the prompt; iterate prompt versions, logging pass rate with CI; keep a hidden holdout of 20 and check dev vs holdout divergence at the end.

## Mastery check
1. Show the red-green loop for a prompt change.
2. How do you tell prompt overfitting from real improvement?
3. When to promote a case to regression?

## Sources
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Shankar et al. 2024, Who Validates the Validators?](https://arxiv.org/abs/2404.12272)
- Practitioner source: not collected.
