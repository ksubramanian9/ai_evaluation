---
id: confidence-intervals-for-evals
title: "Confidence intervals for eval results"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: stats
prerequisites: [statistical-inference, nondeterminism-and-variance]
tags: [nondeterminism]
---
# Confidence intervals for eval results

Reporting uncertainty on eval scores, bootstrapping, and when differences are real.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Miller argues evals are experiments: questions are samples from a super-population; he supplies formulas for analysis, two-model comparison and planning [Miller 2024](https://arxiv.org/abs/2411.00640). Card et al. find underpowered experiments common in NLP; e.g. MT test sets of 2,000 sentences have about 75% power to detect a 1 BLEU difference [Card et al. 2020](https://arxiv.org/abs/2010.06595). Dror et al. give a protocol for choosing significance tests and report testing is often overlooked or misapplied in ACL/TACL 2017 papers [Dror et al. 2018](https://aclanthology.org/P18-1128/). BetterBench found most of 24 assessed benchmarks do not report statistical significance [Reuel et al. 2024](https://arxiv.org/abs/2411.12990).

## Common failure modes
- CLT-based intervals on small benchmarks usually dramatically underestimate uncertainty with fewer than a few hundred items [Bowyer et al. 2025](https://arxiv.org/abs/2503.01747).
- Ignoring paired structure when comparing two models on the same questions (Miller covers two-model comparison; detail UNVERIFIED beyond the abstract).
- Ignoring run-to-run sampling variance and clustered questions. UNVERIFIED beyond the abstract.
- Multiple comparisons and selective reporting; related evidence: [Singh et al.](https://arxiv.org/abs/2504.20879).

## Practice exercise
Take per-item 0/1 results of two prompts on 200 items. Compute Wald, Wilson and bootstrap CIs, and a paired bootstrap on the difference. Subsample to 30 items and see which interval breaks down. Run a power calculation for a 3-point difference.

## Mastery check
1. When do Wilson, bootstrap or Bayesian intervals beat the Wald CLT interval?
2. Why is a paired test more powerful for comparing two models?
3. How many items detect a 2-point accuracy gain at 80% power?

## Sources
[Miller](https://arxiv.org/abs/2411.00640); [Bowyer et al.](https://arxiv.org/abs/2503.01747); [Card et al.](https://arxiv.org/abs/2010.06595); [Dror et al.](https://aclanthology.org/P18-1128/); [BetterBench](https://arxiv.org/abs/2411.12990).
