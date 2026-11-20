---
id: data-splits-and-leakage
title: "Data splits and leakage"
branch: 01-foundations
depth: L2
status: not-started
bridge: stats
prerequisites: []
tags: []
---
# Data splits and leakage

Train/validation/test discipline and the common ways leakage invalidates results.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._
## Why it matters
- Leakage is information unavailable at prediction time being used to build the model. It gives optimistic estimates and worse real-world performance ([sklearn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)).
- Scale: a survey found leakage errors in 17 fields affecting 329 papers, with an 8-type taxonomy. In one civil-war-prediction case, the claimed ML advantage over logistic regression vanished once leakage was fixed ([Kapoor & Narayanan](https://arxiv.org/abs/2207.07048)).
- Tuning on the test set leaks knowledge into the model, so the metric no longer measures generalization ([sklearn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)).
- LLM relevance: benchmark contamination is the same failure through pretraining data. UNVERIFIED here; the source belongs with the contamination node in [eval design](../02-eval-design/contamination-and-leakage.md).

## Common failure modes
- Fitting preprocessing or feature selection before splitting. sklearn's example (200 samples, 10,000 random features) gives 0.76 test accuracy on random labels when features are selected on all the data, and 0.5 when split first.
- Group leakage: several samples per subject across train and test. Fix with `GroupKFold`.
- Temporal leakage: shuffling time-ordered data inflates scores. Use `TimeSeriesSplit`.
- Repeated peeking at the test set during tuning.

## Practice exercise (1-2 h)
Reproduce the sklearn random-data experiment (random X, random y). Leak via `SelectKBest` before the split, then fix it with a `Pipeline`. Then build a dataset with repeated "patients" and compare `KFold` against `GroupKFold`. Write one line per leak type naming its category in the Kapoor taxonomy (read the paper's table).

## Mastery check
1. Why is 0.76 accuracy on random labels proof of a bug?
2. For chat transcripts from 500 users, how do you split, and why?
3. Name three leakage types that "split before preprocessing" does not catch.

## Sources
- scikit-learn, common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
- scikit-learn, cross-validation: https://scikit-learn.org/stable/modules/cross_validation.html
- Kapoor & Narayanan, "Leakage and the Reproducibility Crisis in ML-based Science": https://arxiv.org/abs/2207.07048
