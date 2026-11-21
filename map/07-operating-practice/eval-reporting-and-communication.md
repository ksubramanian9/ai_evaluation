---
id: eval-reporting-and-communication
title: "Eval reporting and communication"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [confidence-intervals-for-evals]
tags: [statistics]
---
# Eval reporting and communication

Presenting results, uncertainty, and tradeoffs to decision-makers.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Compute a paired difference with a 95% CI (bootstrap and analytic) and apply clustered standard errors when items share a source.
- Run a power calculation for the item count needed to detect a stated gap.
- Write a decision memo that reports effect size with interval, slices, cost, known gaps and residual risk, including a "limits of this evaluation" section.
- Identify reporting failures in someone else's result: point estimates without intervals, unpaired comparisons, aggregate-only numbers, and benchmark scores read as capability.

**Done bar.** Practiced: a one-page decision memo comparing two prompt versions on 200 items, with paired CI (bootstrap and analytic), a power calculation for a 3-point gap, slices, cost, known gaps and residual risk. Mastered: written answers to all three mastery questions checked against Miller and BetterBench, and one real or capstone eval result reported to a decision-maker in this format with the decision recorded.

## Why it matters
- Miller, "Adding Error Bars to Evals" (arXiv 2411.00640, 1 Nov 2024): evals are experiments; gives formulas for error bars, clustered standard errors, paired differences, power analysis, with reporting recommendations ([arXiv](https://arxiv.org/abs/2411.00640)).
- BetterBench: most benchmarks do not report statistical significance ([arXiv 2411.12990](https://arxiv.org/abs/2411.12990)).
- NIST AI 600-1 on limits: lab/benchmark results may not extrapolate; share pre-deployment results with release authorities (MS-2.3-003) ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)). Construct validity paper supplies a reporting checklist ([arXiv 2511.04703](https://arxiv.org/abs/2511.04703)).
- Compliance reports need dated, signed test logs with pre-defined thresholds (Art. 9(8), Annex IV above).
- Cost/latency belong in the report alongside quality (inference).

## Common failure modes
- Point estimates without intervals; ranking models on differences within noise (Miller).
- Unpaired comparisons when same questions were used (Miller).
- Ignoring clustering (questions sharing a passage) so intervals are too narrow (Miller).
- Single aggregate hiding slice regressions (Model Cards disaggregation).
- Reporting a benchmark score as capability without construct validity (Bean et al.).
- Reporting only pass rate, not what was *not* tested (limits section).

## Practice exercise (2 h)
Take two prompt versions on a 200-item eval. Compute paired difference with 95% CI (bootstrap and analytic), a power calculation for the item count needed to detect a 3-point gap, and write a one-page decision memo: recommendation, effect size with interval, slices, cost, known gaps, residual risk.

## Mastery check
1. A stakeholder says "v2 is 2 points better." What do you need before agreeing?
2. When do paired analysis and clustered SEs change the conclusion?
3. Write the "limits of this evaluation" paragraph for your memo.

## Sources
- [Miller, Adding Error Bars to Evals, arXiv 2411.00640](https://arxiv.org/abs/2411.00640)
- [BetterBench, arXiv 2411.12990](https://arxiv.org/abs/2411.12990)
- [Construct validity review, arXiv 2511.04703](https://arxiv.org/abs/2511.04703)
- [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
