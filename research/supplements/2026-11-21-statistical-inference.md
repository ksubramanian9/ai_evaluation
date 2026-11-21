# Research supplement: statistical-inference

As-of: 2026-11-21. Purpose: full-text verification of node claims (audit rec #14).

## Miller 2024, Adding Error Bars to Evals
URL: https://arxiv.org/html/2411.00640 (full text, arXiv HTML)
- Section 2.1: CLT applies to evals with finite-variance scores and many questions; report the SE under each mean. Verified.
- Section 2.2: clustered SEs for grouped questions (DROP, QuAC, RACE, SQuAD, MGSM). Text: adjustment "far from trivial (up to 3X)"; Table 4 ratios 3.05 (DROP), 1.10 (RACE-H), 1.88 (MGSM); caption "can be over 3X larger". Node now says "over 3x on DROP (Table 4)".
- Section 3.1-3.2: resampling K=2 cuts variance by 1/3 (limit 2/3); next-token probabilities cut it by 2/3 in the uniform-difficulty example. Verified.
- Section 3.3 "Don't touch the thermostat!": lowering temperature can "reduce conditional variance by injecting bias into the estimator". Verified.
- Section 4.2: paired differences are a "free" variance reduction; at correlation 0.5, variance falls by 1/3. Verified.
- Section 5: omega^2 = 1/9, delta = 0.03, alpha = 0.05, power 0.80 gives n of about 969; "new evals should contain at least 1,000 questions". Node now states the parameters.
- Miller does not discuss multiple comparisons.

## Dror et al. 2018, Hitchhiker's Guide to Testing Statistical Significance in NLP
URL: https://aclanthology.org/P18-1128.pdf (full text, PDF)
- Section 3, Figure 1: decision tree for choosing a test (parametric if the test-statistic distribution is known; otherwise bootstrap/permutation or sampling-free tests).
- Section 4, Table 2: ACL 2017: 196 long papers, 180 experimental, 63 ran a significance test, 21 of those did not name it, 6 of the 42 naming it used the wrong test. TACL 2017: 33 experimental papers, 15 without significance testing, all named tests valid.
- Section 4: multiple comparisons. ACL 2017: of 110 papers using multiple datasets, only 3 corrected for multiplicity (all Bonferroni). TACL: 4 of 19. This resolves the node's UNVERIFIED multiple-comparisons item.

## Card et al. 2020, With Little Power Comes Great Responsibility
URL: https://arxiv.org/pdf/2010.06595 (full text, PDF v1); notebooks https://github.com/dallascard/NLP-power-analysis (repo checked, contains accuracy.ipynb and BLEU.ipynb)
- Abstract and section 1: power is the probability of rejecting the null given a real effect; underpowered is "often taken to mean less than 80% power" (citing Cohen 1962).
- Section 2, Figure 2: simulation-based power-analysis procedure.
- Section 4: 2,000-sentence MT test sets have about 75% power for a 1 BLEU difference.

## SciPy scipy.stats.bootstrap
URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html (full page)
- Defaults n_resamples=9999, method='BCa'. paired=True resamples one index array used for all samples. Verified.
- No explicit i.i.d. statement; the coverage statement is conditional on samples "taken at random from their respective distributions".

## statsmodels power
URLs (full pages):
- https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.solve_power.html: effect_size is the "standardized effect size, difference between the two means divided by the standard deviation"; solves for one of effect_size, nobs1, alpha, power, ratio. Resolves the UNVERIFIED effect-size item. Correction: ratio is also solvable (node said "any one of effect size, nobs, alpha or power", which is incomplete but not wrong).
- https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_effectsize.html: 2*(arcsin(sqrt(p1)) - arcsin(sqrt(p2))), "for use in power function"; matches R pwr.p2.test.
- https://www.statsmodels.org/stable/generated/statsmodels.stats.power.NormalIndPower.html: z-test power for two independent samples. The docs do not explicitly pair it with proportion_effectsize; the node says so.

## Gaps
- Dietterich 1998 and Demsar 2006 were not re-read here (owned by classical-ml-validation).
- No source fetched on power for paired proportions (McNemar power); the exercise's power calculation via NormalIndPower is a conservative approximation, stated as such in the node.
