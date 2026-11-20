---
id: llm-as-judge
title: "LLM-as-judge"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: none
prerequisites: [rubric-design, human-evaluation]
tags: []
---
# LLM-as-judge

Using a model to grade outputs: prompt design, scoring formats, and when it is appropriate.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Strong LLM judges can approximate human preference at scale. Zheng et al. report GPT-4-class judges reaching over 80% agreement with controlled and crowdsourced human preferences, comparable to human-human agreement [Zheng et al. 2023](https://arxiv.org/abs/2306.05685). G-Eval uses chain-of-thought and a form-filling paradigm and reports Spearman 0.514 with humans on summarization with GPT-4 [Liu et al. 2023](https://arxiv.org/abs/2303.16634). Prometheus (open 13B judge using a user rubric and reference) reports Pearson 0.897 with humans on 45 custom rubrics (GPT-4 0.882, ChatGPT 0.392) [Kim et al. 2023](https://arxiv.org/abs/2310.08491). Vendor guidance: use a different model from the generator, constrain output format ("Output only 'yes' or 'no'"), and use binary or Likert formats with clear criteria [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests). OpenAI: start with a strong judge, add reasoning before scoring, prefer pairwise or pass/fail over open-ended scores, validate against human annotations [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## Common failure modes
- Position, verbosity and self-enhancement bias, plus limited reasoning ability [Zheng et al.](https://arxiv.org/abs/2306.05685).
- Possible bias toward LLM-generated text (preliminary) [G-Eval](https://arxiv.org/abs/2303.16634).
- Proprietary judges have uncontrolled versioning and cost [Prometheus](https://arxiv.org/abs/2310.08491).
- Judges inherit LLM flaws, so they must be validated against human grades; criteria are subjective and iterative [Shankar et al.](https://arxiv.org/abs/2404.12272).

## Practice exercise
Take 50 outputs from a small task with your own pass/fail labels. Write a judge prompt with a rubric, a reasoning step and a strict output format. Run it with two judge models. Report agreement with your labels (kappa) and the confusion matrix. Iterate the rubric once.

## Mastery check
1. Why validate a judge against human labels before using it for regression gating?
2. Compare binary, Likert and pairwise judging formats.
3. Show what changes when the judge shares a model family with the generator.

## Sources
[MT-Bench paper](https://arxiv.org/abs/2306.05685); [G-Eval](https://arxiv.org/abs/2303.16634); [Prometheus](https://arxiv.org/abs/2310.08491); [Shankar et al.](https://arxiv.org/abs/2404.12272); [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests); [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).
