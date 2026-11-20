---
id: rubric-design
title: "Rubric design"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [quality-dimensions-taxonomy]
tags: []
---
# Rubric design

Writing scoring criteria that are unambiguous enough for humans and judge models to apply consistently.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

## Why it matters
Rubrics make graders (human or LLM) consistent: Prometheus conditions on a user-supplied rubric and reference, 0.897 Pearson with humans on 45 custom rubrics (GPT-4 0.882) [Kim et al.](https://arxiv.org/abs/2310.08491); HealthBench uses conversation-specific rubrics, 48,562 criteria written by 262 physicians over 5,000 conversations [Arora et al.](https://arxiv.org/abs/2505.08775). Anthropic's LLM-graded examples use Likert 1-5 or binary classification [CLAUDE-EVAL]; OpenAI suggests pairwise or pass/fail for reliability [OAI-BP].
## Common failure modes
Rubrics drift as graders see outputs [Shankar](https://arxiv.org/abs/2404.12272); position/verbosity bias in judge application [OAI-BP]; vague anchors (UNVERIFIED in primary source); judge not validated against humans [OAI-BP].
## Practice exercise
Write a 1-5 rubric with anchor examples and a binary variant for one dimension; have 2 raters (or you + LLM judge) label 40 outputs; compare Cohen's kappa for both versions; refine ambiguous levels.
## Mastery check
(1) Why might binary beat 1-5? (2) Rewrite a vague level descriptor with observable evidence. (3) How do you validate an LLM judge on a rubric?
## Sources
https://arxiv.org/abs/2310.08491; https://arxiv.org/abs/2505.08775; [CLAUDE-EVAL]; [OAI-BP]; https://arxiv.org/abs/2404.12272.
