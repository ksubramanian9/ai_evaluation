---
id: statistical-inference
title: "Statistical inference for evaluation"
branch: 01-foundations
depth: L2
status: not-started
bridge: stats
prerequisites: [ml-metrics]
tags: [nondeterminism]
---
# Statistical inference for evaluation

Confidence intervals, significance tests, effect sizes, and power for comparing systems.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._
## Why it matters
- Miller's recommendations: CLT standard errors; clustered standard errors when questions are grouped (up to a 3x adjustment in his example); variance reduction by resampling answers and using next-token probabilities; paired-difference inference when comparing models; and power analysis, which for his illustrative parameters suggests new evals need roughly 1,000+ questions ([Miller 2024](https://arxiv.org/abs/2411.00640)).
- Significance testing in NLP is often skipped or misused. Dror et al. give a protocol for choosing a test ([Dror et al., ACL 2018](https://aclanthology.org/P18-1128/)).
- Power is neglected in NLP. Card et al. give power-analysis practice and notebooks ([Card et al., EMNLP 2020](https://aclanthology.org/2020.emnlp-main.745); details from the abstract only; arXiv 2010.06595).
- Tools: `scipy.stats.bootstrap` defaults to BCa with 9999 resamples and has a `paired` option ([SciPy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)). `statsmodels` `TTestIndPower.solve_power` solves for any one of effect size, nobs, alpha or power ([statsmodels docs](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html)). The effect-size definition was not on the fetched page: UNVERIFIED.

## Common failure modes
- Ignoring clustering (several questions per passage), so CIs are too narrow.
- Unpaired comparison, which throws away free variance reduction.
- Underpowered evals that declare "no difference".
- Misusing or skipping significance tests.
- Multiple comparisons across many metrics or prompts: UNVERIFIED, no source fetched.
- Lowering temperature to cut variance can add bias (Miller, section 3.3).

## Practice exercise (2-3 h)
Take two models' per-question 0/1 results on about 500 questions. Compute: a naive SE and CI; a bootstrap CI with `scipy.stats.bootstrap`; a paired-difference CI with `paired=True`; McNemar on the discordant pairs; and the N needed to detect a 2-point difference. For proportions, a two-sample proportion power function fits better than the t-test; verify in the statsmodels docs.

## Mastery check
1. Why is a paired CI narrower than two independent CIs?
2. An eval has 200 items and model A beats B by 3 points. What can you conclude, and what N would you need?
3. When do clustered SEs matter, and how do you compute them?
4. What does a bootstrap assume that can fail?

## Sources
- Miller: https://arxiv.org/abs/2411.00640
- Dror et al., ACL 2018: https://aclanthology.org/P18-1128/
- Card et al., EMNLP 2020: https://aclanthology.org/2020.emnlp-main.745
- Dietterich 1998 and Demsar 2006 (see [classical-ml-validation](classical-ml-validation.md))
- SciPy bootstrap: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html
- statsmodels power: https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html
