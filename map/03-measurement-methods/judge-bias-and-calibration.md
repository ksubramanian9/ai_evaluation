---
id: judge-bias-and-calibration
title: "Judge bias and calibration"
branch: 03-measurement-methods
depth: L3
status: not-started
bridge: stats
prerequisites: [llm-as-judge, inter-rater-agreement, confidence-intervals-for-evals]
tags: [llm-judge, nondeterminism]
---
# Judge bias and calibration

Position, verbosity, and self-preference bias; validating a judge against human labels.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** judge design and validation is owned by [llm-as-judge](llm-as-judge.md); this node covers judge bias and calibration (position, length and self-preference bias, and validating a judge against human labels).

## Learning objectives
You can:
- Quantify position bias from swapped-order runs as a flip rate.
- Measure length bias by padding answers, and explain how regression-based length control works.
- Apply balanced-position aggregation and report what it changes.
- Design a judge calibration set (size, label source, metric, pass threshold), trading labeling cost against confidence in the judge.

**Done bar.** Practiced: a write-up on 30 pairs with the swapped-order flip rate, the win-rate change from padding, an optional self-vs-other result, and rankings before and after balanced-position aggregation. Mastered: written answers to all three mastery-check questions, checked against Wang et al., Panickssery et al., Wataoka et al., Dubois et al., Thakur et al. and Zheng et al., plus a calibration-set design or a critique of a real judge setup that finds an uncontrolled bias and states the trade-off of the mitigation.

## Why it matters
- Each bias can shift rankings.
- Reordering responses changed outcomes; Vicuna-13B beat ChatGPT on 66 of 80 queries under one ordering with ChatGPT as evaluator. Proposed calibration: multiple evidence, balanced position (aggregate across orders), human-in-the-loop for hard cases ([Wang et al. 2023](https://arxiv.org/abs/2305.17926)).

## Common failure modes
- Self-preference: evaluators score their own outputs higher; strength correlates linearly with self-recognition ability ([Panickssery et al. 2024](https://arxiv.org/abs/2404.13076)). Alternative account: GPT-4 prefers lower-perplexity (more familiar) text whether or not self-generated ([Wataoka et al. 2024](https://arxiv.org/abs/2410.21819)).
- Length bias: AlpacaEval favored longer outputs. A regression-based length control raised Spearman correlation with Chatbot Arena from 0.94 to 0.98 ([Dubois et al. 2024](https://arxiv.org/abs/2404.04475)).
- High percent agreement can hide very different scores, so use chance-corrected metrics ([Thakur et al.](https://arxiv.org/abs/2406.12624)).
- Verbosity and position bias are named in [Zheng et al.](https://arxiv.org/abs/2306.05685); OpenAI advises controlling for response length ([OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).

## Practice exercise (3 h)
Build 30 pairs. Run the judge in both orders and report the flip rate. Pad one answer in each pair with filler and measure win-rate change. Add a self-vs-other condition if you have two model families. Apply balanced-position aggregation and report what changes.

## Mastery check
1. Quantify position bias from swapped-order runs.
2. How does length control work (counterfactual GLM)?
3. Design a calibration set: size, label source, metric, pass threshold for the judge.

## Sources
- [Wang et al. 2023, Large Language Models are not Fair Evaluators](https://arxiv.org/abs/2305.17926)
- [Panickssery et al. 2024, LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076)
- [Wataoka et al. 2024, Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819)
- [Dubois et al. 2024, Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475)
- [Thakur et al. 2024, Judging the Judges](https://arxiv.org/abs/2406.12624)
- [Zheng et al. 2023, MT-Bench paper](https://arxiv.org/abs/2306.05685)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
