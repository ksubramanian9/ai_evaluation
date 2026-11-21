---
id: validity-and-reliability
title: "Validity and reliability"
branch: 02-eval-design
depth: L3
status: not-started
bridge: stats
prerequisites: [metric-selection, statistical-inference]
tags: [statistics]
---
# Validity and reliability

Whether an eval measures what it claims (construct validity) and gives stable results.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** confidence intervals, power and paired comparisons are owned by [statistical-inference](../01-foundations/statistical-inference.md) and [confidence-intervals-for-evals](../03-measurement-methods/confidence-intervals-for-evals.md).

## Learning objectives
You can:
- Compute run-to-run and paraphrase variance, SE or bootstrap CIs, and a paired difference between two prompt versions.
- State the minimum detectable effect for an eval's n.
- Distinguish construct validity from reliability and list threats to validity for an eval.
- Critique a benchmark using Bean et al.'s recommendations and weigh which threats matter most.

**Done bar.** Practiced: a write-up with CIs from 5 runs x 3 prompt paraphrases, the paired difference, the minimum detectable effect for your n, and the construct with 3 threats to validity. Mastered: written answers to all three mastery-check questions, checked against Bean et al., Bowman & Dahl, Raji et al., Jacobs & Wallach and Miller, plus a critique of a benchmark you use that applies one Bean et al. recommendation and states the trade-off of fixing it.

## Why it matters
- 445 LLM benchmarks reviewed by 29 experts show recurring patterns weakening construct validity; eight recommendations ([Bean et al., NeurIPS 2025 D&B](https://arxiv.org/abs/2511.04703)).
- Benchmarks should be reliable, unbiased, with headroom ([Bowman & Dahl](https://arxiv.org/abs/2104.02145)).
- General benchmarks framed as measures of "general" progress have construct validity problems ([Raji et al.](https://arxiv.org/abs/2111.15366)).
- Measurement-modeling vocabulary: construct validity/reliability ([Jacobs & Wallach](https://arxiv.org/abs/1912.05511)).
- Stability: "evaluations are experiments"; formulas for analysis, model comparison, power planning ([Miller](https://arxiv.org/abs/2411.00640); abstract only).

## Common failure modes
- Construct mismatch ([Bean](https://arxiv.org/abs/2511.04703)).
- Sampling noise treated as signal ([Miller](https://arxiv.org/abs/2411.00640)).
- Judge bias ([Zheng](https://arxiv.org/abs/2306.05685)).
- Metric artifacts ([Schaeffer](https://arxiv.org/abs/2304.15004)).
- Contamination ([Sainz](https://arxiv.org/abs/2310.18018)).

## Practice exercise (3 h)
Run your eval 5x at temperature>0 and with 3 prompt paraphrases; compute SE/bootstrap CI and paired difference between two prompt versions; state minimum detectable effect for your n. Separately, list the construct and 3 threats to validity.

## Mastery check
1. Distinguish construct validity from reliability with an example from your eval.
2. Is a 2-point gain on 200 items real?
3. Apply one Bean et al. recommendation to a benchmark you use (read the paper).

## Sources
- [Bean et al., Measuring what Matters (NeurIPS 2025 D&B)](https://arxiv.org/abs/2511.04703)
- [Bowman & Dahl, What Will it Take to Fix Benchmarking in NLU?](https://arxiv.org/abs/2104.02145)
- [Raji et al., AI and the Everything in the Whole Wide World Benchmark](https://arxiv.org/abs/2111.15366)
- [Jacobs & Wallach, measurement and fairness](https://arxiv.org/abs/1912.05511)
- [Miller, Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640)
