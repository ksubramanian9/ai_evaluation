---
id: ml-metrics
title: "Core ML metrics"
branch: 01-foundations
depth: L2
status: not-started
bridge: stats
prerequisites: []
tags: []
---
# Core ML metrics

Accuracy, precision/recall/F1, AUC, regression error, and ranking metrics; when each misleads.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._
## Why it matters
- The metric encodes the cost model. scikit-learn documents matching scoring rules: squared error for the mean, absolute error for the median, pinball loss for quantiles ([sklearn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)).
- On imbalanced data accuracy can beat chance purely because of the imbalance, while balanced accuracy falls to 1/n_classes in that case (same page).
- ROC plots can be deceptive under class imbalance. PR plots reflect precision and are more informative about expected future performance ([Saito & Rehmsmeier 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118432)).

## Common failure modes
- Reporting accuracy on imbalanced data.
- Reading a high ROC-AUC as high precision at deployment prevalence. Saito & Rehmsmeier's re-analysis of a published tool comparison showed strong ROC but very low precision.
- F1 undefined or zero when there are no positives: sklearn defaults to 0 and exposes `zero_division`.
- Optimizing a metric that does not match the decision (for example R^2 when the median matters).
- Ranking metrics (NDCG and similar) are UNVERIFIED here: the sklearn page was truncated before that section.

## Practice exercise (2 h)
Use sklearn on a dataset with about 2% positives (`fetch_openml` credit-card fraud, or `make_classification(weights=[0.98])`). Train logistic regression and compute accuracy, balanced accuracy, ROC-AUC, average precision, and F1 at the default and a tuned threshold. Plot ROC and PR curves. Show that a constant-negative classifier gets 98% accuracy, and explain which metric moves least with prevalence.

## Mastery check
1. Given a prevalence and a confusion matrix, compute precision, recall and F-beta by hand. Justify the beta for a recall-critical task.
2. When does ROC-AUC mislead, and what do you report instead?
3. Which metric fits a ranked-list task where only the top 5 matter? (Verify NDCG/MRR definitions in the sklearn docs.)

## Sources
- scikit-learn, model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- Saito & Rehmsmeier, PLOS ONE 2015: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118432
