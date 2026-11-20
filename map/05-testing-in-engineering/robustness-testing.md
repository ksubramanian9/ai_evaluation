---
id: robustness-testing
title: "Robustness testing"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [coverage-and-slicing]
tags: []
---
# Robustness testing

Behavior under paraphrase, typos, adversarial and out-of-distribution inputs.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
PromptRobust/PromptBench: 4,788 adversarial prompts over 8 tasks and 13 datasets at character, word, sentence, and semantic levels; "contemporary LLMs are not robust to adversarial prompts" ([Zhu et al., arXiv 2306.04528](https://arxiv.org/abs/2306.04528)). CheckList includes perturbation-style invariance tests ([Ribeiro](https://arxiv.org/abs/2005.04118); type names UNVERIFIED from abstract). HELM measures robustness and fairness among seven metrics over 42 scenarios and 30 models ([Liang et al., TMLR 2023](https://arxiv.org/abs/2211.09110)).

## Common failure modes
- Perturbations unrealistic vs. real user noise; or label-changing perturbations.
- Reporting average drop only; worst-case per input matters.
- Mixing up prompt robustness (instruction wording) with input robustness (user text).
- Robustness tests run only on one model, with no transfer analysis; Zhu et al. analyze transfer of adversarial prompts across models ([arXiv 2306.04528](https://arxiv.org/abs/2306.04528)).

## Practice exercise
Take 100 golden cases. Apply 4 perturbation families (typos, case/whitespace, paraphrase via LLM + manual audit, distractor sentence). Report accuracy per family with CI and the fraction of cases whose output flips. Try PromptBench or a small custom script.

## Mastery check
1. Why is flip-rate more informative than accuracy drop alone?
2. How do you ensure a perturbation preserves the label?
3. Which perturbations matter for your user population and how would you know?

## Sources
[Zhu 2306.04528](https://arxiv.org/abs/2306.04528); [HELM](https://arxiv.org/abs/2211.09110); [CheckList](https://arxiv.org/abs/2005.04118).
