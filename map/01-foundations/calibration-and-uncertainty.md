---
id: calibration-and-uncertainty
title: "Calibration and uncertainty"
branch: 01-foundations
depth: L2
status: not-started
bridge: stats
prerequisites: [ml-metrics]
tags: [nondeterminism, statistics]
---
# Calibration and uncertainty

Whether confidence matches correctness; uncertainty estimation basics.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._
## Why it matters
- Modern neural networks are poorly calibrated, unlike those of a decade earlier. Depth, width, weight decay and batch norm all affect it, and temperature scaling (a one-parameter Platt variant) is a surprisingly effective fix ([Guo et al. 2017](https://arxiv.org/abs/1706.04599)).
- For LLMs, larger models are well calibrated on multiple-choice and true/false questions with the right format, and P(True) self-evaluation works encouragingly. P(IK) generalizes partially but is poorly calibrated on new tasks ([Kadavath et al. 2022](https://arxiv.org/abs/2207.05221)).
- Reliability diagrams plot the fraction of positives against mean predicted probability per bin ([sklearn calibration](https://scikit-learn.org/stable/modules/calibration.html)).

## Common failure modes
- Using Brier score or log loss as a pure calibration measure. sklearn warns they mix calibration, resolution and irreducible uncertainty, so a lower Brier can come from a more discriminative but worse-calibrated model.
- Isotonic calibration on small data overfits (sklearn: better than sigmoid above roughly 1000 samples). The calibrator must be fit on data independent of training.
- Isotonic calibration introduces ties and can change AUC; sigmoid is strictly monotonic.
- Calibration measured in-distribution and assumed to hold on new tasks (Kadavath on P(IK)).
- ECE: the sklearn page does not cover it. Compute it from `calibration_curve` bins and note bin-count sensitivity (UNVERIFIED, no source on ECE bias fetched).
- Verbalized or token-probability confidence from black-box LLM APIs: UNVERIFIED, not researched.

## Practice exercise (2-3 h)
Train a random forest and a logistic regression on a binary dataset. Plot reliability diagrams (`CalibrationDisplay`), compute Brier score and a hand-coded ECE with 10 and 20 bins, then calibrate with sigmoid and isotonic via `CalibratedClassifierCV` on held-out data. Show AUC and ECE before and after. Optional: have an LLM answer 200 multiple-choice questions, extract option log-probs (or P(True)) and plot calibration.

## Mastery check
1. Define calibration, and give a model with perfect ranking but bad calibration.
2. Why can't you read calibration from the Brier score alone?
3. When do you choose sigmoid over isotonic?
4. Why might an LLM's calibration on multiple choice not transfer to open-ended generation?

## Sources
- [Guo et al., "On Calibration of Modern Neural Networks" (ICML 2017)](https://arxiv.org/abs/1706.04599)
- [Kadavath et al., "Language Models (Mostly) Know What They Know"](https://arxiv.org/abs/2207.05221)
- [scikit-learn, probability calibration](https://scikit-learn.org/stable/modules/calibration.html)
