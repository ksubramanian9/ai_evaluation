---
id: fairness-and-bias-testing
title: "Fairness and bias testing"
branch: 05-testing-in-engineering
depth: L3
status: not-started
bridge: stats
prerequisites: [coverage-and-slicing]
tags: [fairness]
---
# Fairness and bias testing

Measuring disparities across groups and slices.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
BBQ (ACL 2022 Findings): hand-built QA sets over nine social dimensions; under-informative contexts elicit stereotyped answers; accuracy up to 3.4 points higher when the correct answer aligns with the bias, >5 for gender in most models ([Parrish et al., arXiv 2110.08193](https://arxiv.org/abs/2110.08193)). Classical definitions: Hardt et al. propose an "oblivious" criterion depending only on joint statistics of predictor, target, protected attribute (equal opportunity; [arXiv 1610.02413](https://arxiv.org/abs/1610.02413); equalized-odds definition itself not on abstract page, see Fairlearn). Fairlearn: demographic parity = equal selection rates (difference 0 / ratio 1); equalized odds = equal TPR and FPR across groups, difference is the larger of the two gaps; check intersecting subgroups, small groups have less data, multiple comparisons need correction (e.g., Bonferroni) ([Fairlearn docs](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html), as-of 2026-11-20). HELM includes fairness and bias among 7 metrics ([arXiv 2211.09110](https://arxiv.org/abs/2211.09110)).

## Common failure modes
- Choosing one metric without noting incompatibility between definitions (UNVERIFIED here; Hardt/Fairlearn pages do not state it).
- Small subgroup sizes producing noisy gaps; no CIs, and multiple-comparison inflation ([Fairlearn](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html)).
- Benchmark-only testing (BBQ is U.S. English-centric, [arXiv 2110.08193](https://arxiv.org/abs/2110.08193)); doesn't reflect your app's demographics.
- Proxy attributes; counterfactual name-swap only.
- Generation bias (free text) measured with classification-style metrics.

## Practice exercise
(a) Classical: train a small classifier on a tabular dataset (e.g., UCI Adult), compute MetricFrame by group, demographic parity and equalized-odds differences with bootstrap CIs. (b) LLM: counterfactual name/pronoun-swap pairs on 100 prompts for your app, measure outcome-difference rate (an MT relation), run 50 BBQ items.

## Mastery check
1. Compute and interpret demographic parity difference vs. equalized-odds difference on a toy table.
2. Which metric fits a hiring-screen LLM vs. a customer-support bot, and why?
3. How many samples per group do you need to detect a 5-point gap?

## Sources
[BBQ](https://arxiv.org/abs/2110.08193); [Hardt 2016](https://arxiv.org/abs/1610.02413); [Fairlearn](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html); [HELM](https://arxiv.org/abs/2211.09110).
