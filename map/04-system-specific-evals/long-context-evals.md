---
id: long-context-evals
title: "Long-context evals"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: none
prerequisites: [llm-basics-for-evaluators]
tags: [rag, cost]
---
# Long-context evals

Testing retrieval and reasoning over long inputs.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Run a context-length by needle-depth sweep and plot the result as a heatmap.
- Compare a lexical needle with a low-overlap (paraphrased) needle to show why plain needle-in-a-haystack is insufficient.
- Separate retrieval failures from reasoning or aggregation failures in long-context results.
- Plan a cost-aware length sweep for a given model and budget.

**Done bar.** Practiced: a 3x5 length-by-depth grid with lexical and paraphrased needles, 3 seeds, two heatmaps and a written comparison. Mastered: written answers to all four mastery questions checked against RULER, HELMET and NoLiMa, plus one long-context test run on a real system's actual context sizes, with effective versus claimed context length recorded.

## Why it matters
- Needle-in-a-haystack sweeps context length x needle depth ([Kamradt repo](https://github.com/gkamradt/needle-in-a-haystack), practitioner).
- Lost in the Middle: accuracy drops when evidence is mid-context (TACL, [arXiv 2307.03172](https://arxiv.org/abs/2307.03172)).
- RULER adds multi-hop tracing/aggregation; only about half of 17 models claiming >=32K stayed satisfactory at 32K (COLM 2024, [arXiv 2404.06654](https://arxiv.org/abs/2404.06654)).
- HELMET (7 categories, 59 models): synthetic tasks like NIAH do not reliably predict downstream performance ([arXiv 2410.02694](https://arxiv.org/abs/2410.02694)).
- NoLiMa removes lexical overlap; 11/13 models fell below half of short-context baselines at 32K; GPT-4o 99.3 to 69.7 (ICML 2025, [arXiv 2502.05167](https://arxiv.org/abs/2502.05167)).

## Common failure modes
- Position effects.
- Saturated lexical-match needle tests.
- Claimed vs effective context length.
- Reasoning/aggregation degrading faster than retrieval ([RULER](https://arxiv.org/abs/2404.06654), [HELMET](https://arxiv.org/abs/2410.02694)).

## Practice exercise (3 h)
Run a 3x5 grid (lengths x depths) with a lexical needle and a paraphrased (low-overlap) needle on one model, 3 seeds; plot heatmaps; compare.

## Mastery check
1. Why is NIAH insufficient?
2. What does NoLiMa change?
3. Cost-aware design of a length sweep.
4. Separate retrieval from reasoning failures.

## Sources
- [Lost in the Middle, arXiv 2307.03172](https://arxiv.org/abs/2307.03172)
- [RULER, arXiv 2404.06654](https://arxiv.org/abs/2404.06654)
- [HELMET, arXiv 2410.02694](https://arxiv.org/abs/2410.02694)
- [NoLiMa, arXiv 2502.05167](https://arxiv.org/abs/2502.05167)
- practitioner: [Kamradt needle-in-a-haystack](https://github.com/gkamradt/needle-in-a-haystack)
