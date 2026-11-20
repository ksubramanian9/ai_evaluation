---
id: benchmark-limitations
title: "Benchmark limitations and saturation"
branch: 03-measurement-methods
depth: L3
status: not-started
bridge: none
prerequisites: [public-benchmarks, contamination-and-leakage]
tags: []
---
# Benchmark limitations and saturation

Saturation, contamination, and the gap between benchmark score and real-world performance.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Raji et al. argue that treating a few influential benchmarks as proxies for "general" ability is a construct-validity problem [Raji et al. 2021](https://arxiv.org/abs/2111.15366). BetterBench scored 24 benchmarks against 46 lifecycle best practices and found wide quality variation and little significance reporting [Reuel et al.](https://arxiv.org/abs/2411.12990).

## Common failure modes
- Contamination: benchmark content in training data yields unreliable scores [Xu et al. survey](https://arxiv.org/abs/2406.04244).
- Memorization/overfitting: on fresh GSM1k, accuracy dropped up to 8% vs GSM8k for some models, correlated with likelihood of reproducing GSM8k examples; frontier models showed little overfitting [Zhang et al. 2024](https://arxiv.org/abs/2405.00332).
- Label errors and saturation: [Gema et al.](https://arxiv.org/abs/2406.04127); successors added difficulty [MMLU-Pro](https://arxiv.org/abs/2406.01574).
- Leaderboard gaming: selective disclosure, private testing, unequal data access [Singh et al.](https://arxiv.org/abs/2504.20879).
- Score vs real-world gap (construct validity) [Raji et al.](https://arxiv.org/abs/2111.15366).

## Practice exercise
Pick one benchmark. Audit it: read 50 items for errors, check for public answer keys, and compare a small model's perplexity on items vs paraphrased versions. Score it on a subset of BetterBench criteria and write a one-page verdict.

## Mastery check
1. Differentiate contamination, overfitting and saturation, with a test for each.
2. What does GSM1k show and not show?
3. Score a benchmark against 5 BetterBench-style criteria.

## Sources
[Raji et al.](https://arxiv.org/abs/2111.15366); [BetterBench](https://arxiv.org/abs/2411.12990); [Xu et al.](https://arxiv.org/abs/2406.04244); [GSM1k](https://arxiv.org/abs/2405.00332); [MMLU-Redux](https://arxiv.org/abs/2406.04127); [Leaderboard Illusion](https://arxiv.org/abs/2504.20879).
