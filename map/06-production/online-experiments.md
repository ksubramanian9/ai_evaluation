---
id: online-experiments
title: "A/B tests and online experiments"
branch: 06-production
depth: L2
status: not-started
bridge: stats
prerequisites: [statistical-inference, online-metrics-and-user-feedback]
tags: [statistics, nondeterminism]
---
# A/B tests and online experiments

Experiment design and analysis for AI features, including non-determinism and novelty effects.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** online metric definitions and signal biases are owned by [online-metrics-and-user-feedback](online-metrics-and-user-feedback.md); this node covers causal analysis of those metrics through controlled experiments.

## Learning objectives
You can:
- Explain why daily peeking at p<0.05 inflates false positives, and apply a fix (fixed horizon or always-valid p-values/CIs).
- Run a chi-square sample ratio mismatch check and decide what to do with a result when SRM fires.
- Apply CUPED with a pre-period metric and measure the variance reduction it gives.
- Design an experiment for an LLM feature that accounts for per-request nondeterminism (user-level randomisation), interference between variants and novelty effects.

**Done bar.** Practiced: a simulation write-up showing false-positive rate over 2,000 A/A runs for fixed-horizon vs daily peeking, measured CUPED variance reduction, and an SRM check that flags a 52/48 split. Mastered: written answers to all three mastery questions checked against Kohavi et al., Johari et al. and the CUPED page, and one real or capstone A/B test designed and analysed with SRM check and interval recorded.

## Why it matters
- Controlled experiments are the standard design for establishing causal effect on user-observable behaviour; the Kohavi guide covers surprising results, ingredients, and technical/organisational limits ([Kohavi et al. 2009](https://link.springer.com/article/10.1007/s10618-008-0114-1)).
- Peeking breaks standard p-values; always-valid p-values/CIs stay valid under continuous monitoring and were deployed on a commercial platform ([Johari et al.](https://arxiv.org/abs/1512.04922)).
- CUPED uses pre-experiment data to reduce metric variance and raise sensitivity; its benefit depends on the pre/post correlation ([CUPED page](https://exp-platform.com/cuped/); correlation caveat via [search summary of Lin & Crespo 2024](https://arxiv.org/html/2410.09027v1), not read directly).
- Review of statistical challenges in online experimentation ([arXiv 2212.11366](https://arxiv.org/abs/2212.11366)).

## Common failure modes
- Peeking/early stopping (Johari above).
- Sample ratio mismatch: observed split differs from intended; Microsoft research calls it one of the most useful data-quality indicators, and the book's index lists SRM p.219 and novelty effect pp.33, 49, 174 ([search results incl. book index](https://assets.cambridge.org/97811087/24265/index/9781108724265_index.pdf)); definitions of novelty effect from the book text UNVERIFIED.
- LLM-specific: nondeterministic outputs add per-request variance; user-level randomisation and variance reduction needed (design/inference; no primary source found on LLM-specific A/B).
- Interference/shared state across variants (also cited for canaries in [SRE workbook](https://sre.google/workbook/canarying-releases/)).

## Practice exercise (3 h)
(design)
- Simulate an A/B test with a binary success metric (base 40%, +2pt effect) with 1) fixed-horizon test, 2) daily peeking at p<0.05, measure false-positive rate over 2,000 A/A runs. Then apply CUPED with a correlated pre-period metric and measure variance reduction and a chi-square SRM check with a deliberately buggy 52/48 split.

## Mastery check
1. Why is daily peeking at p<0.05 invalid, and what are two fixes?
2. SRM p-value is 0.0001 - what do you do with the result?
3. How would you detect a novelty effect for a new assistant UI?

## Sources
- [Kohavi et al. 2009](https://link.springer.com/article/10.1007/s10618-008-0114-1)
- [Johari et al. always-valid](https://arxiv.org/abs/1512.04922)
- [Deng et al. CUPED (WSDM 2013)](https://exp-platform.com/cuped/)
- [Statistical challenges review](https://arxiv.org/abs/2212.11366)
- Book: Kohavi, Tang, Xu, Trustworthy Online Controlled Experiments, CUP 2020 ([index/excerpt](https://assets.cambridge.org/97811087/24265/index/9781108724265_index.pdf))
