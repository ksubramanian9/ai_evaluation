# Research supplement: inter-rater-agreement

As-of: 2026-11-21. Purpose: full-text verification and thickening of the node (audit recs #14, #15). Web access worked (WebFetch, WebSearch); PDFs were extracted locally with pdftotext.

## Artstein & Poesio 2008, Inter-Coder Agreement for Computational Linguistics
URL: https://aclanthology.org/J08-4004/ (PDF https://aclanthology.org/J08-4004.pdf). Depth: full text (sections 1-5 read via pdftotext; Greek letters lost in extraction, recovered from context).
- 2.3: percent agreement is "biased in favor of dimensions with a small number of categories" (quoting Scott 1955) and does not correct for skew. Example (from Di Eugenio & Glass 2004): 95% statement / 5% info-request gives chance agreement 0.9025 + 0.0025 = 90.5%, so "a seemingly high observed agreement of 90% is actually worse than expected by chance." Verifies the old UNVERIFIED percent-agreement failure mode.
- 2.4: S, pi and kappa all use (Ao - Ae)/(1 - Ae); they differ only in Ae. 2.4.2: Scott's pi uses the pooled distribution of both coders. 2.4.3: Cohen's kappa uses each coder's own distribution ("individual annotator bias"); kappa >= pi.
- 2.5 and footnote 5: Fleiss (1971) generalized Scott's pi to many coders but called it kappa; Davies & Fleiss (1982) generalized Cohen's kappa. Correction to common usage: "Fleiss' kappa" is a multi-pi.
- 2.6: pi and kappa treat all disagreements equally. 2.6.1: alpha "applies to multiple coders, and it allows for different magnitudes of disagreement"; with nominal data "it is nearly identical to multi-pi"; alpha and pi "approach each other as either the number of items or the number of coders approaches infinity"; any distance metric with d(k,k)=0 works, but "different distance metrics yield different values of alpha for the same annotation data." 2.6.2: weighted kappa, Cohen (1968).
- 3 (Bias and Prevalence): bias problem = kappa and pi diverge when coder marginals diverge; prevalence problem = "exceeding difficulty in getting high agreement values when most of the items fall under one category."
- 3.1: pi-style coefficients measure chance agreement "among arbitrary coders", kappa-style "among the coders who produced the reliability data"; for reliability, single-distribution coefficients (pi, alpha) are "most appropriate"; kappa speaks to trustworthiness (validity). For fixed Ao, larger marginal differences give lower Ae and higher kappa. Difference between kappa and pi shrinks as agreement rises and as coders increase (Observations 1-2); with 18 subjects, values "never differed beyond the third decimal point." Recommend testing with more than two coders.
- 3.2: prevalence "paradox" (cites Cicchetti & Feinstein 1990; Feinstein & Cicchetti 1990); justified because "the test for reliability in such cases is the ability to agree on the rare categories."
- 4.1.1: summary of Krippendorff (2004a, ch. 11): three or more coders, clearly specified selection criteria, independent work from a fixed written scheme; minimum number of units via Bloch & Kraemer (1989) formula (Krippendorff 2004a p. 239); each category should occur "often enough to yield at least five chance agreements"; sample should contain all values.
- 4.1.2: significance against chance is "trivial" (quoting Cohen 1960 p. 44); use confidence intervals. Cohen (1960) implies kappa is approximately normal for large samples; Krippendorff (2004a) says alpha's distribution is unknown, so bootstrap.
- 4.1.3 and Figure 1: Landis & Koch (1977) bands at 0.2 steps labelled Poor (<0), Slight, Fair, Moderate, Substantial, Perfect (this is A&P's reproduction; the original wording was not read). Krippendorff 1980: K > .8 good, .67-.8 "tentative conclusions"; later Krippendorff: "Even a cutoff point of alpha = .800 ... is a pretty low standard" (2004a p. 242). Neuendorf 2002: .90 acceptable to all, .80 most situations.
- 4.1.4: Reidsma & Carletta (2008): agreement coefficients are poor predictors of machine-learning success.
- 5.2: recommend K/alpha (abstract away from coder bias); increasing the number of annotators "is the best strategy"; alpha "indispensable" when labels are not equally distinct; weights affect the value. 5.3: "if a threshold needs to be set, 0.8 is a good value", but "we doubt that a single cutoff point is appropriate for all purposes"; report methodology, significance, and a confusion matrix.

## Krippendorff, Computing Krippendorff's Alpha-Reliability (2011.1.25, literature updated 2013.9.13)
URL: https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf. Depth: full text (10 pages).
- alpha = 1 - Do/De; applies to "any number of observers", "any metric or level of measurement (nominal, ordinal, interval, ratio, and more)", "incomplete or missing data", "large and small sample sizes alike, not requiring a minimum".
- Worked example (section D, 4 observers, 12 units, 7 missing values): alpha nominal 0.743, ordinal 0.815, interval 0.849. Used in the node.
- Does not itself state the .800/.667 thresholds (those come via A&P quoting Krippendorff 1980/2004a).

## Hayes & Krippendorff 2007, Answering the Call for a Standard Reliability Measure for Coding Data
URL: https://www.asc.upenn.edu/sites/default/files/2021-03/Answering%20the%20Call%20for%20a%20Standard%20Reliability%20Measure%20for%20Coding%20Data.pdf (manuscript as submitted, Communication Methods and Measures 1(1):77-89). Depth: full text.
- Five criteria for a reliability index; percent agreement "flawed in nearly all important respects"; Cohen's kappa critiqued for treating coders as non-interchangeable and letting systematic disagreement inflate it; Fleiss's K generalizes Scott's pi, nominal only; Cronbach's alpha measures consistency, not agreement.
- alpha's distribution is bootstrapped; KALPHA macro reports CI and q, the probability alpha falls below alpha_min (example CI .7078-.8078; q = 0.9473 for alpha_min .80). Little gained beyond about 10,000 bootstrap samples.
- Not used in the node: the claim that two-observer ordinal alpha equals Spearman's rho. It is the authors' own claim and was not cross-checked.

## Thakur et al., Judging the Judges (arXiv 2406.12624v6, 18 Aug 2025)
URL: https://arxiv.org/html/2406.12624. Depth: full text (first 100k of ~104k characters; the cited sections are covered).
- CORRECTION: the node quoted "judges with high percent agreement can still assign vastly different scores". The v6 abstract reads "judges with high agreement can still assign vastly different scores." The Introduction says "high percent agreement can still give scores that differ 10-20 points". Section 4.1: "even judges that have more than 90% may still differ more than 10 points in their assigned score." The node now uses the section 4.1 claim.
- Section 3 and Appendix B: they use Scott's pi, not Cohen's kappa (an earlier version used kappa); kappa's chance term "adjusts for the observed average differences between raters, which is in fact part of what we intend to measure."
- Section 3: three human annotators on 1,200 TriviaQA samples; average Scott's pi 96.2 (x100), percent agreement 98.52%.
- Conclusion: report both percent agreement and Scott's pi, with qualitative analysis.

## Abstract-level / bibliographic only
- Landis & Koch 1977, Biometrics 33:159-174, doi 10.2307/2529310. Abstract via Europe PMC (PMID 843571). The abstract does not mention the benchmark bands; the bands come only from A&P Figure 1.
- Feinstein & Cicchetti 1990, J Clin Epidemiol 43:543-549, doi 10.1016/0895-4356(90)90158-l (Europe PMC abstract): a high p0 "can be drastically lowered by a substantial imbalance in the table's marginal totals"; second paradox: kappa is higher with asymmetrical imbalance.
- Byrt, Bishop & Carlin 1993, J Clin Epidemiol 46:423-429, doi 10.1016/0895-4356(93)90018-v (Europe PMC abstract): kappa is affected by bias and prevalence; they define bias and prevalence indices and recommend reporting them with kappa. PABAK is attributed to this paper by secondary sources only (not used).
- Cohen 1960 (doi 10.1177/001316446002000104), Cohen 1968 (doi 10.1037/h0026256), Fleiss 1971 (doi 10.1037/h0031619): metadata via Semantic Scholar API; closed access, abstracts elided. Not read.
- scikit-learn cohen_kappa_score docs (1.9.1): weights None/'linear'/'quadratic'. krippendorff PyPI 0.9.0 (uploaded 2026-10-07), `krippendorff.alpha(reliability_data=...)`. Recorded in the landscape file.

## Gaps
- Cohen 1960, Cohen 1968 and Fleiss 1971 were not read in the original; their content is taken from Artstein & Poesio.
- Landis & Koch's exact band labels and their own caveats (e.g. whether they call the bands arbitrary) are UNVERIFIED in the original.
- Krippendorff 2004a (book) and Krippendorff 2004b (HCR, repository.upenn.edu/asc_papers/242 returned 403) were not read directly; thresholds come via A&P quotes.
- The Bloch & Kraemer minimum-sample formula was not obtained, so the node gives no concrete item count.
- No source was found that gives a sample-size rule specific to validating an LLM judge.
