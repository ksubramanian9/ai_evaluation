---
id: inter-rater-agreement
title: "Inter-rater agreement"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: stats
prerequisites: [human-evaluation, statistical-inference]
tags: [human-labels, statistics]
---
# Inter-rater agreement

Cohen's/Fleiss' kappa, Krippendorff's alpha, and what agreement levels imply.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Verified in full text 2026-11-21: Artstein & Poesio, Krippendorff 2011, Hayes & Krippendorff, Thakur et al. Cohen, Fleiss and Landis & Koch are paywalled and are described via Artstein & Poesio; items marked "abstract only" were not read further. Supplemented 2026-11-21: [research/supplements/2026-11-21-inter-rater-agreement.md](../../research/supplements/2026-11-21-inter-rater-agreement.md). Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Compute percent agreement, Cohen's kappa, weighted kappa and Krippendorff's alpha.
- Bootstrap a CI on kappa or alpha.
- Show how skewed labels produce high agreement with low kappa.
- Choose a coefficient for the number of raters, the scale type and the purpose (labeling reliability vs validating an LLM judge).

**Done bar.** Practiced: the coefficient table on the two-rater data, the skewed 95/5 demonstration, a bootstrap CI, and judge-vs-human agreement next to a human-human baseline. Mastered: written answers to all three mastery-check questions, checked against Artstein & Poesio, Krippendorff and Thakur et al., plus agreement reported for a real labeling or judge-validation task with coefficient, CI and confusion matrix.

## Why it matters
- Chance-corrected coefficients compute (Ao - Ae) / (1 - Ae); Scott's pi takes chance from the pooled label distribution, Cohen's kappa from each coder's own; Fleiss 1971 generalized pi, not kappa, to many coders (sections 2.4-2.5, [Artstein & Poesio 2008](https://aclanthology.org/J08-4004/)).
- Krippendorff's alpha (1 - observed/expected disagreement) handles any number of coders, missing data and nominal to ratio metrics ([Krippendorff 2011](https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf)); for nominal data it nearly equals multi-pi (section 2.6.1, [Artstein & Poesio](https://aclanthology.org/J08-4004/)).
- Kappa vs alpha: pi and alpha measure reproducibility of the procedure, kappa agreement of these particular coders; use the former for reliability, and the gap shrinks as coders are added (sections 3.1, 5.2, [Artstein & Poesio](https://aclanthology.org/J08-4004/)).
- Ordinal labels need weights: one dataset gives alpha 0.743 nominal, 0.815 ordinal, 0.849 interval ([Krippendorff 2011](https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf)); weighted kappa (Cohen 1968) is the kappa-family option (section 2.6.2, [Artstein & Poesio](https://aclanthology.org/J08-4004/)).
- Raters and items: Krippendorff requires three or more independent coders, a sample sized by the Bloch & Kraemer formula, and every category frequent enough for five chance agreements (section 4.1.1, [Artstein & Poesio](https://aclanthology.org/J08-4004/)).
- Alpha's sampling distribution is unknown, so its CI is bootstrapped ([Hayes & Krippendorff 2007](https://www.asc.upenn.edu/sites/default/files/2021-03/Answering%20the%20Call%20for%20a%20Standard%20Reliability%20Measure%20for%20Coding%20Data.pdf)).
- Judge validation: Thakur et al. prefer Scott's pi because kappa's chance term absorbs judge-human differences, "which is in fact part of what we intend to measure" (Appendix B); three humans reached pi 96.2 on 1,200 TriviaQA items (section 3) ([Thakur et al. 2024](https://arxiv.org/abs/2406.12624)).

## Common failure modes
- Raw percent agreement: with 95/5 labels chance agreement is 90.5%, so 90% observed is worse than chance (section 2.3, [Artstein & Poesio](https://aclanthology.org/J08-4004/)).
- Prevalence paradox: skew gives low kappa despite high agreement, reflecting weak agreement on the rare class (section 3.2, [Artstein & Poesio](https://aclanthology.org/J08-4004/); abstract only, [Feinstein & Cicchetti 1990](https://doi.org/10.1016/0895-4356(90)90158-l)); report bias and prevalence indices alongside kappa (abstract only, [Byrt et al. 1993](https://doi.org/10.1016/0895-4356(93)90018-v)).
- Bias paradox: at fixed observed agreement, kappa rises as coder marginals diverge (section 3.1, [Artstein & Poesio](https://aclanthology.org/J08-4004/)).
- Treating Landis & Koch bands (0.2 steps, "slight" to "perfect") as standards; Krippendorff wants alpha of at least 0.8, and no single cutoff suits every purpose (sections 4.1.3, 5.3, [Artstein & Poesio](https://aclanthology.org/J08-4004/)).
- Judging a judge by percent agreement: judges above 90% can still differ from humans by over 10 points in score (section 4.1, [Thakur et al.](https://arxiv.org/abs/2406.12624)).

## Practice exercise (2-3 h)
Use the two-rater data from human-evaluation. Compute percent agreement, Cohen's kappa, weighted kappa (sklearn) and Krippendorff's alpha (`krippendorff` package) at nominal and ordinal levels. Build a skewed 95/5 label set and show high agreement with low kappa. Bootstrap a CI on alpha. Add an LLM judge as a rater; compare its agreement with the human-human value and show the confusion matrix.

## Mastery check
1. Why can 90% agreement coexist with kappa near 0?
2. When do you use Cohen's kappa, Fleiss' kappa or Krippendorff's alpha, and which suits validating an LLM judge?
3. What agreement level makes labels usable as ground truth for a judge, and why is there no universal cutoff?

## Sources
- [Artstein & Poesio 2008, Inter-Coder Agreement for Computational Linguistics](https://aclanthology.org/J08-4004/)
- [Krippendorff 2011 (rev. 2013), Computing Krippendorff's Alpha-Reliability](https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf)
- [Hayes & Krippendorff 2007, Answering the Call for a Standard Reliability Measure](https://www.asc.upenn.edu/sites/default/files/2021-03/Answering%20the%20Call%20for%20a%20Standard%20Reliability%20Measure%20for%20Coding%20Data.pdf)
- [Thakur et al. 2024, Judging the Judges](https://arxiv.org/abs/2406.12624)
- [Feinstein & Cicchetti 1990, High agreement but low kappa (abstract only)](https://doi.org/10.1016/0895-4356(90)90158-l)
- [Byrt, Bishop & Carlin 1993, Bias, prevalence and kappa (abstract only)](https://doi.org/10.1016/0895-4356(93)90018-v)
- Paywalled, not read: [Cohen 1960](https://doi.org/10.1177/001316446002000104), [Cohen 1968](https://doi.org/10.1037/h0026256), [Fleiss 1971](https://doi.org/10.1037/h0031619), [Landis & Koch 1977 (abstract only)](https://doi.org/10.2307/2529310).
