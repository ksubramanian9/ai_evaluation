---
id: long-context-evals
title: "Long-context evals"
branch: 04-system-specific-evals
depth: L3
status: not-started
bridge: none
prerequisites: [llm-basics-for-evaluators]
tags: []
---
# Long-context evals

Testing retrieval and reasoning over long inputs.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Needle-in-a-haystack sweeps context length x needle depth ([Kamradt repo](https://github.com/gkamradt/LLMTest_NeedleInAHaystack), practitioner). Lost in the Middle: accuracy drops when evidence is mid-context (TACL, [arXiv 2307.03172](https://arxiv.org/abs/2307.03172)). RULER adds multi-hop tracing/aggregation; only about half of 17 models claiming >=32K stayed satisfactory at 32K (COLM 2024, [arXiv 2404.06654](https://arxiv.org/abs/2404.06654)). HELMET (7 categories, 59 models): synthetic tasks like NIAH do not reliably predict downstream performance ([arXiv 2410.02694](https://arxiv.org/abs/2410.02694)). NoLiMa removes lexical overlap; 11/13 models fell below half of short-context baselines at 32K; GPT-4o 99.3 to 69.7 (ICML 2025, [arXiv 2502.05167](https://arxiv.org/abs/2502.05167)).

## Common failure modes
Position effects; saturated lexical-match needle tests; claimed vs effective context length; reasoning/aggregation degrading faster than retrieval (RULER, HELMET).

## Practice exercise
Run a 3x5 grid (lengths x depths) with a lexical needle and a paraphrased (low-overlap) needle on one model, 3 seeds; plot heatmaps; compare.

## Mastery check
(1) Why is NIAH insufficient? (2) What does NoLiMa change? (3) Cost-aware design of a length sweep. (4) Separate retrieval from reasoning failures.

## Sources
Lost in the Middle; RULER; HELMET; NoLiMa; Kamradt (practitioner).
