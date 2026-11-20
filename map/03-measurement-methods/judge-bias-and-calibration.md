---
id: judge-bias-and-calibration
title: "Judge bias and calibration"
branch: 03-measurement-methods
depth: L3
status: not-started
bridge: stats
prerequisites: [llm-as-judge, inter-rater-agreement, confidence-intervals-for-evals]
tags: [nondeterminism]
---
# Judge bias and calibration

Position, verbosity, and self-preference bias; validating a judge against human labels.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Each bias can shift rankings. Reordering responses changed outcomes; Vicuna-13B beat ChatGPT on 66 of 80 queries under one ordering with ChatGPT as evaluator. Proposed calibration: multiple evidence, balanced position (aggregate across orders), human-in-the-loop for hard cases [Wang et al. 2023](https://arxiv.org/abs/2305.17926).

## Common failure modes
- Self-preference: evaluators score their own outputs higher; strength correlates linearly with self-recognition ability [Panickssery et al. 2024](https://arxiv.org/abs/2404.13076). Alternative account: GPT-4 prefers lower-perplexity (more familiar) text whether or not self-generated [Wataoka et al. 2024](https://arxiv.org/abs/2410.21819).
- Length bias: AlpacaEval favored longer outputs. A regression-based length control raised Spearman correlation with Chatbot Arena from 0.94 to 0.98 [Dubois et al. 2024](https://arxiv.org/abs/2404.04475).
- High percent agreement can hide very different scores, so use chance-corrected metrics [Thakur et al.](https://arxiv.org/abs/2406.12624).
- Verbosity and position bias are named in [Zheng et al.](https://arxiv.org/abs/2306.05685); OpenAI advises controlling for response length [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## Practice exercise
Build 30 pairs. Run the judge in both orders and report the flip rate. Pad one answer in each pair with filler and measure win-rate change. Add a self-vs-other condition if you have two model families. Apply balanced-position aggregation and report what changes.

## Mastery check
1. Quantify position bias from swapped-order runs.
2. How does length control work (counterfactual GLM)?
3. Design a calibration set: size, label source, metric, pass threshold for the judge.

## Sources
[Wang et al.](https://arxiv.org/abs/2305.17926); [Panickssery et al.](https://arxiv.org/abs/2404.13076); [Wataoka et al.](https://arxiv.org/abs/2410.21819); [Dubois et al.](https://arxiv.org/abs/2404.04475); [Thakur et al.](https://arxiv.org/abs/2406.12624); [Zheng et al.](https://arxiv.org/abs/2306.05685).
