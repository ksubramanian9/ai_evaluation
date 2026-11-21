---
id: statistical-inference
title: "Statistical inference for evaluation"
branch: 01-foundations
depth: L2
status: not-started
bridge: stats
prerequisites: [ml-metrics]
tags: [nondeterminism, statistics]
---
# Statistical inference for evaluation

Confidence intervals, significance tests, effect sizes, and power for comparing systems.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Verified in full text on 2026-11-21: Miller (arXiv HTML), Dror et al. (ACL Anthology PDF), Card et al. (arXiv PDF), and the SciPy and statsmodels docs pages cited. Items marked UNVERIFIED were not confirmed from a fetched primary page. Supplemented 2026-11-21: [research/supplements/2026-11-21-statistical-inference.md](../../research/supplements/2026-11-21-statistical-inference.md)._

## Learning objectives
You can:
- Compute naive, bootstrap and paired-difference CIs for per-question eval results.
- Run McNemar on discordant pairs and a power calculation for a target difference.
- Recognise when clustered standard errors are needed and compute them.
- Judge whether a reported gap on a given number of items supports a conclusion.

**Done bar.** Practiced: a notebook on two models' per-question results (about 500 questions) showing the naive CI, bootstrap CI, paired-difference CI, McNemar result and the N needed to detect a 2-point difference. Mastered: written answers to all four mastery-check questions, checked against Miller, Dror et al., Card et al. and the SciPy and statsmodels docs, plus one real comparison (capstone or work) reported with a paired CI and the conclusion recorded.

## Why it matters
- Miller's recommendations: CLT standard errors (section 2.1); clustered standard errors when questions are grouped (section 2.2; clustered SEs over 3x the naive SE on DROP in Table 4); variance reduction by resampling answers and using next-token probabilities (sections 3.1-3.2); paired-difference inference when comparing models (section 4.2); and power analysis (section 5), where delta = 3 points, alpha = 0.05 and 80% power give n of about 969, so he concludes new evals should have at least 1,000 questions ([Miller 2024](https://arxiv.org/abs/2411.00640)).
- Significance testing in NLP is often skipped or misused: of 180 experimental ACL 2017 long papers, only 63 ran a significance test, 21 of those did not name it, and 6 of the 42 that did used the wrong test (section 4, Table 2). Dror et al. give a decision tree for choosing a test (section 3, Figure 1) ([Dror et al., ACL 2018](https://aclanthology.org/P18-1128/)).
- Power is neglected in NLP. Card et al. give a simulation-based power-analysis procedure (section 2, Figure 2) and release notebooks ([github.com/dallascard/NLP-power-analysis](https://github.com/dallascard/NLP-power-analysis)); they note "underpowered" is often taken to mean below 80% power ([Card et al., EMNLP 2020](https://aclanthology.org/2020.emnlp-main.745); read in full via [arXiv 2010.06595](https://arxiv.org/abs/2010.06595)).
- Tools: `scipy.stats.bootstrap` defaults to BCa with 9999 resamples and has a `paired` option ([SciPy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)). `statsmodels` `TTestIndPower.solve_power` solves for any one of effect size, nobs, alpha or power ([statsmodels docs](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html)). Its `effect_size` is the "standardized effect size, difference between the two means divided by the standard deviation" ([solve_power docs](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.solve_power.html)). For two proportions, `proportion_effectsize` gives 2*(arcsin(sqrt(p1)) - arcsin(sqrt(p2))) "for use in power function" ([statsmodels docs](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_effectsize.html)), and `NormalIndPower` is the z-test power class for two independent samples ([statsmodels docs](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.NormalIndPower.html)); the docs do not explicitly pair the two.

## Common failure modes
- Ignoring clustering (several questions per passage), so CIs are too narrow.
- Unpaired comparison, which throws away free variance reduction.
- Underpowered evals that declare "no difference".
- Misusing or skipping significance tests.
- Multiple comparisons across many metrics, datasets or prompts: in ACL 2017, only 3 of 110 papers that used multiple datasets corrected for multiplicity (all with Bonferroni); in TACL, 4 of 19 (section 4, [Dror et al. 2018](https://aclanthology.org/P18-1128/)).
- Lowering temperature to cut variance can "reduce conditional variance by injecting bias into the estimator" (section 3.3, [Miller 2024](https://arxiv.org/abs/2411.00640)).

## Practice exercise (2-3 h)
Take two models' per-question 0/1 results on about 500 questions. Compute: a naive SE and CI; a bootstrap CI with `scipy.stats.bootstrap`; a paired-difference CI with `paired=True`; McNemar on the discordant pairs; and the N needed to detect a 2-point difference. For proportions, use `proportion_effectsize` with a normal-approximation power class such as `NormalIndPower` rather than the t-test class (note: this ignores pairing, so it is conservative for a paired design).

## Mastery check
1. Why is a paired CI narrower than two independent CIs?
2. An eval has 200 items and model A beats B by 3 points. What can you conclude, and what N would you need?
3. When do clustered SEs matter, and how do you compute them?
4. What does a bootstrap assume that can fail?

## Sources
- [Miller](https://arxiv.org/abs/2411.00640)
- [Dror et al., ACL 2018](https://aclanthology.org/P18-1128/)
- [Card et al., EMNLP 2020](https://aclanthology.org/2020.emnlp-main.745) ([arXiv 2010.06595](https://arxiv.org/abs/2010.06595); [notebooks](https://github.com/dallascard/NLP-power-analysis))
- [Dietterich, Neural Computation 1998](https://doi.org/10.1162/089976698300017197) and [Demsar, JMLR 2006](https://www.jmlr.org/papers/v7/demsar06a.html) (see [classical-ml-validation](classical-ml-validation.md))
- [SciPy bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)
- [statsmodels power](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html), [solve_power](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.solve_power.html), [proportion_effectsize](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_effectsize.html), [NormalIndPower](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.NormalIndPower.html)
