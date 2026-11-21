---
id: classical-ml-validation
title: "Classical ML validation"
branch: 01-foundations
depth: L1
status: not-started
bridge: stats
prerequisites: [data-splits-and-leakage, ml-metrics]
tags: [statistics]
---
# Classical ML validation

Cross-validation, baselines, and drift basics: the foundation LLM evaluation builds on.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._

## Learning objectives
You can:
- Explain why reporting the best tuned CV score overstates performance and how nested CV fixes it.
- Identify which test fits comparing two models on one test set and which fits comparing them across many datasets.
- Recognise which CV splitter fits time-series, grouped and imbalanced data.
- Explain how dataset shift makes deployed models fail silently.

**Done bar.** Practiced: a short write-up showing the dummy baseline, plain-CV and nested-CV scores with the optimistic gap, a McNemar result for two models, and the classifier two-sample test detecting the simulated shift. Mastered: written answers to all three mastery-check questions, checked against the sklearn docs, Cawley & Talbot, Dietterich and Demsar, plus explaining nested CV and the tuned-CV-score failure to someone else without notes.

## Why it matters
- k-fold CV reports the average over folds and avoids wasting data on a fixed validation set, with a separate test set still held out ([sklearn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)).
- Model selection itself overfits. Selection bias can be as large as the performance differences between algorithms, so selection should happen inside the evaluation loop (nested CV) ([Cawley & Talbot 2010](https://www.jmlr.org/papers/v11/cawley10a.html); abstract level only).
- Comparing classifiers: Dietterich compared five approximate tests. McNemar had low type I error and suits single-run algorithms, and 5x2cv is slightly more powerful when 10 runs are affordable ([Dietterich 1998](https://doi.org/10.1162/089976698300017197); read only through a secondary abstract summary). For many datasets, Demsar recommends the Wilcoxon signed-ranks test for two classifiers and Friedman with post-hoc tests for more ([Demsar 2006](https://www.jmlr.org/papers/v7/demsar06a.html)).
- Drift: ML systems fail silently under dataset shift, and two-sample tests on classifier-reduced features did best among the methods tested ([Rabanser et al. 2019](https://arxiv.org/abs/1810.11953)). This is thinly sourced here and may belong in [drift-detection](../06-production/drift-detection.md).
- Baselines: UNVERIFIED, no primary source fetched for "always compare to a trivial baseline". Candidate: sklearn `DummyClassifier` docs.

## Common failure modes
- Unstratified folds with rare classes. In sklearn's example `KFold` produced a fold with no minority samples.
- Using the same integer `random_state` across folds, or comparing non-comparable folds across separate `split` calls (sklearn common pitfalls, randomness section).
- Reporting the best CV score of a tuned grid as the generalization estimate (Cawley & Talbot).
- Treating CV fold scores as independent samples in significance tests: UNVERIFIED; Dietterich 1998 motivates corrected tests, read the full paper.
- Not monitoring input shift after deployment (Rabanser).

## Practice exercise (3 h)
Using one sklearn dataset and 3 models: (1) a dummy baseline, (2) plain CV with tuned hyperparameters reported as final, (3) nested CV. Show the optimistic gap. Compare two models with McNemar on a held-out set (statsmodels `mcnemar`; docs not fetched, UNVERIFIED). Simulate covariate shift by shifting a feature mean and detect it with a classifier two-sample test.

## Mastery check
1. Why does reporting the best tuned CV score overstate performance, and what fixes it?
2. Which test compares two models on one test set, and why? Which for 10 datasets?
3. Which CV splitter for time series, grouped data and imbalanced data?

## Sources
- [scikit-learn, cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [scikit-learn, common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
- [Cawley & Talbot, JMLR 2010](https://www.jmlr.org/papers/v11/cawley10a.html)
- [Dietterich, Neural Computation 1998](https://doi.org/10.1162/089976698300017197)
- [Demsar, JMLR 2006](https://www.jmlr.org/papers/v7/demsar06a.html)
- [Rabanser et al., "Failing Loudly" (NeurIPS 2019)](https://arxiv.org/abs/1810.11953)
