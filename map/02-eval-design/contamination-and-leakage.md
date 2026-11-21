---
id: contamination-and-leakage
title: "Contamination and leakage in evals"
branch: 02-eval-design
depth: L2
status: not-started
bridge: stats
prerequisites: [data-splits-and-leakage]
tags: [statistics]
---
# Contamination and leakage in evals

How test data ends up in training data or prompts, and how to detect and avoid it.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Owns:** contamination and leakage detection and avoidance; see also [data-splits-and-leakage](../01-foundations/data-splits-and-leakage.md), [benchmark-limitations](../03-measurement-methods/benchmark-limitations.md).

## Learning objectives
You can:
- Build a paraphrased or perturbed twin of a benchmark subset and compare accuracy on both.
- Run a canonical-order vs shuffled likelihood test on an open-weights model.
- Apply controls that keep a private golden set out of prompts, few-shot examples, judge prompts and tuning.
- Interpret what a gap on a fresh twin proves and does not prove, separating contamination from overfitting.

**Done bar.** Practiced: a 50-item twin set with the original-vs-twin accuracy comparison and, for an open-weights model, the canonical-vs-shuffled likelihood result. Mastered: written answers to all three mastery-check questions, checked against Sainz et al., Oren et al. and Zhang et al., plus leakage controls applied to a real golden set or the capstone with what you checked and found recorded.

## Why it matters
- Contaminated models look better than they are, leading to wrong conclusions; extent hard to measure ([Sainz et al.](https://arxiv.org/abs/2310.18018)).
- Black-box detection: if a benchmark was not seen, example order should not matter; significant likelihood gap for canonical order flags contamination, works down to 1.4B models/1,000 examples ([Oren et al.](https://arxiv.org/abs/2310.17623)).
- Fresh-set check: GSM1k showed up to 8% lower accuracy than GSM8k for some models, r^2=0.36 with likelihood of generating GSM8k, though frontier models showed minimal overfitting ([Zhang et al.](https://arxiv.org/abs/2405.00332)).
- Survey of definitions/mitigation ([Xu et al.](https://arxiv.org/abs/2406.04244)).

## Common failure modes
- Public test sets in web-scale training data ([Sainz](https://arxiv.org/abs/2310.18018)).
- Closed-model data not inspectable (hence black-box tests) ([Oren](https://arxiv.org/abs/2310.17623)).
- Leaking test examples into your own few-shot/judge prompts or tuning (UNVERIFIED, inference).
- Conflating overfitting with contamination ([Zhang](https://arxiv.org/abs/2405.00332)).

## Practice exercise (2-3 h)
Take a public benchmark subset; write a held-out paraphrase/perturbed twin (50 items); compare model accuracy original vs twin; for an open-weights model also run a canonical-order vs shuffled likelihood test per Oren et al.

## Mastery check
1. Why does shuffle-likelihood detect contamination?
2. What do you do for a private golden set to prevent leakage into prompts/tuning?
3. What does a performance gap on a fresh twin prove and not prove?

## Sources
- [Sainz et al., NLP evaluation in trouble](https://arxiv.org/abs/2310.18018)
- [Oren et al., Proving Test Set Contamination in Black Box Language Models](https://arxiv.org/abs/2310.17623)
- [Zhang et al., GSM1k](https://arxiv.org/abs/2405.00332)
- [Xu et al., contamination survey](https://arxiv.org/abs/2406.04244)
- Prereq `data-splits-and-leakage` is in another branch (not checked).
