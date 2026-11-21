---
id: rubric-design
title: "Rubric design"
branch: 02-eval-design
depth: L3
status: not-started
bridge: none
prerequisites: [quality-dimensions-taxonomy]
tags: [llm-judge, human-labels]
---
# Rubric design

Writing scoring criteria that are unambiguous enough for humans and judge models to apply consistently.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Write a rubric with observable anchors in both a 1-5 and a binary form.
- Measure inter-rater kappa for each rubric version and refine ambiguous levels.
- Validate an LLM judge applying the rubric against human labels.
- Choose between binary, Likert and pairwise formats for a dimension, and critique rubrics with vague anchors.

**Done bar.** Practiced: both rubric versions with anchor examples, Cohen's kappa for each on 40 outputs, and the refined levels. Mastered: written answers to all three mastery-check questions, checked against Prometheus, HealthBench, Anthropic, OpenAI and Shankar et al., plus a critique of a real rubric that names a flaw this node covers (vague anchors, drift, unvalidated judge) and states the trade-off of the format you choose instead.

## Why it matters
- Rubrics make graders (human or LLM) consistent: Prometheus conditions on a user-supplied rubric and reference, 0.897 Pearson with humans on 45 custom rubrics (GPT-4 0.882) ([Kim et al.](https://arxiv.org/abs/2310.08491)).
- HealthBench uses conversation-specific rubrics, 48,562 criteria written by 262 physicians over 5,000 conversations ([Arora et al.](https://arxiv.org/abs/2505.08775)).
- Anthropic's LLM-graded examples use Likert 1-5 or binary classification ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- OpenAI suggests pairwise or pass/fail for reliability ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).

## Common failure modes
- Rubrics drift as graders see outputs ([Shankar](https://arxiv.org/abs/2404.12272)).
- Position/verbosity bias in judge application ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- Vague anchors (UNVERIFIED in primary source).
- Judge not validated against humans ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).

## Practice exercise (2-3 h)
Write a 1-5 rubric with anchor examples and a binary variant for one dimension; have 2 raters (or you + LLM judge) label 40 outputs; compare Cohen's kappa for both versions; refine ambiguous levels.

## Mastery check
1. Why might binary beat 1-5?
2. Rewrite a vague level descriptor with observable evidence.
3. How do you validate an LLM judge on a rubric?

## Sources
- [Kim et al., Prometheus](https://arxiv.org/abs/2310.08491)
- [Arora et al., HealthBench](https://arxiv.org/abs/2505.08775)
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Shankar et al. 2024, Who Validates the Validators?](https://arxiv.org/abs/2404.12272)
