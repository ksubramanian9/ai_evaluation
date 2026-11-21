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

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Verified in full text on 2026-11-21: Wang et al., Panickssery et al., Wataoka et al., Dubois et al., Thakur et al. (v6) and Zheng et al. (arXiv HTML), and the OpenAI evaluation best-practices page. Supplemented 2026-11-21: [research/supplements/2026-11-21-judge-bias-and-calibration.md](../../research/supplements/2026-11-21-judge-bias-and-calibration.md). Exercises and mastery checks are proposed designs, not sourced claims._

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
- Reordering responses changed outcomes; with ChatGPT as evaluator, Vicuna-13B beat ChatGPT on 66 of 80 queries when placed second, but won only 2.5% when placed first (Table 2). Proposed calibration: multiple evidence, balanced position (aggregate across orders), and human-in-the-loop for cases flagged by a balanced position diversity entropy score (sections 3.1-3.3); MEC plus BPC raised alignment with humans by 9.8% (GPT-4) and 14.3% (ChatGPT) accuracy (section 4) ([Wang et al. 2023](https://arxiv.org/abs/2305.17926)).

## Common failure modes
- Self-preference: evaluators (GPT-3.5, GPT-4, Llama-2-7b-chat) score their own outputs higher; after fine-tuning, self-preference strength correlates linearly with self-recognition ability, which the authors treat as evidence for, not proof of, a causal link (sections 3, 5.2) ([Panickssery et al. 2024](https://arxiv.org/abs/2404.13076)). Alternative account: GPT-4 shows significant self-preference bias under a fairness-based metric (section 4.1), and LLMs rate lower-perplexity text higher than human evaluators do, whether or not it is self-generated (section 5) ([Wataoka et al. 2024](https://arxiv.org/abs/2410.21819)).
- Length bias: AlpacaEval favored longer outputs; prompting gpt4_1106_preview to be concise or verbose moved its win rate from 22.9% to 64.3%, versus 41.9% to 51.6% after length control (section 4.1). The length control is a GLM on model identity, length difference and instruction difficulty, evaluated at zero length difference (section 3); it raised Spearman correlation with Chatbot Arena from 0.94 to 0.98 (section 4.2) ([Dubois et al. 2024](https://arxiv.org/abs/2404.04475)).
- High percent agreement can hide very different scores (judges above 90% agreement can still differ by more than 10 points, section 4.1), so report percent agreement together with Scott's pi; the current version replaced Cohen's kappa with Scott's pi (section 3 footnote 2, section 6) ([Thakur et al.](https://arxiv.org/abs/2406.12624)).
- Verbosity and position bias are named in Zheng et al.: GPT-4 was consistent under swapped order in 65.0% of cases, Claude-v1 in 23.8% (section 3.3, Table 2); they propose counting a win only if it holds in both orders (section 3.4) ([Zheng et al.](https://arxiv.org/abs/2306.05685)). OpenAI advises: "Control for response lengths as LLMs bias towards longer responses in general" ([OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).

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
