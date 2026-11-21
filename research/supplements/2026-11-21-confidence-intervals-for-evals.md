# Research supplement: confidence-intervals-for-evals

As-of: 2026-11-21. Purpose: full-text verification of node claims (audit rec #14). See also 2026-11-21-statistical-inference.md for the Miller, Dror and Card details shared with that node.

## Miller 2024
URL: https://arxiv.org/html/2411.00640 (full text)
- Section 2: questions "drawn at random from a (hypothetical, infinite, unseen) super-population of questions". Verified.
- Section 4.2: paired differences are a "free" variance reduction; 1/3 relative reduction at correlation 0.5. Resolves the node's "UNVERIFIED beyond the abstract" item on pairing.
- Section 3.1 (resampling) and section 2.2 / Table 4 (clustered SEs, 3.05x on DROP). Resolves the node's UNVERIFIED item on run-to-run variance and clustering.

## Bowyer et al. 2025, Position: Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints
URL: https://arxiv.org/html/2503.01747 (v3, read first ~100k of ~148k characters: abstract through section 5 and Table 1; appendices beyond that not read)
- Abstract: CLT-based methods "usually dramatically underestimating uncertainty (i.e. producing error bars that are too small)". Verified.
- It is a position paper (ICML); evidence is mainly simulation with N = 3, 10, 30, 100 (section 3). At N = 100, nominal 95% CLT intervals cover about 92.5% (section 3.1). No hard threshold N* (section 4).
- Recommendations: Wilson or Beta-Bernoulli Bayesian for a single model (3.1); Bayesian for differences and odds ratios (3.3), paired Bayes for paired data (3.4), Bayesian for clustered questions (3.2). Bootstrap intervals also under-cover at small N (3.1, 3.5, section 5). Clopper-Pearson judged overly conservative. Added briefly to the node because mastery question 1 depends on it.

## Card et al. 2020
URL: https://arxiv.org/pdf/2010.06595 (full text)
- Section 4: 2,000-sentence MT test sets, about 75% power for 1 BLEU. Verified.
- Section 1/3: MRPC and SST-2 "now too small to be able to properly measure future progress against top performing models". Added.

## Dror et al. 2018
URL: https://aclanthology.org/P18-1128.pdf (full text)
- Section 4, Table 2: 63 of 180 experimental ACL 2017 long papers ran a significance test; 6 of 42 naming it used the wrong test. Section 4: 3 of 110 multi-dataset ACL papers corrected for multiplicity (Bonferroni); TACL 4 of 19. Numbers added.

## Reuel et al. 2024, BetterBench
URL: https://arxiv.org/html/2411.12990 (read first ~100k of ~213k characters, covering sections 1-7; appendices partly unread)
- 24 benchmarks (16 foundation-model, 8 non-foundation-model). Abstract: "most benchmarks do not report statistical significance of their results". Section 7: "14 out of 24 benchmarks did not perform multiple evaluations of the same model or report statistical significance" (this count combines two criteria). Verified; node now quotes section 7.

## Singh et al. 2025, The Leaderboard Illusion
URL: https://arxiv.org/html/2504.20879 (read first ~100k of ~224k characters: abstract through section 3)
- Section 3.2: private testing plus retraction "enables a best-of-N strategy"; selecting the best variant "introduces an upward bias". The paper does not use the term "multiple comparisons"; node says so. Note: several authors are affiliated with Cohere, a provider on the Arena.

## Gaps
- Bowyer appendices (prior sensitivity, App. I) and BetterBench appendices not read.
- No primary statistics text fetched on Wilson vs Wald coverage beyond Bowyer's simulations.
- Mastery question 3 (items to detect a 2-point gain) has a computable answer via Miller section 5's formula but is not stated as a sourced number in the node.
