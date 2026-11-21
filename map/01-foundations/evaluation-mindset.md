---
id: evaluation-mindset
title: "Evaluation mindset for probabilistic systems"
branch: 01-foundations
depth: L1
status: not-started
bridge: none
prerequisites: []
tags: [nondeterminism, statistics]
---
# Evaluation mindset for probabilistic systems

Why evaluating AI differs from verifying deterministic software: no single right output, distributions instead of points.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._

## Learning objectives
You can:
- Explain why an eval score is an estimate with error, not a fact.
- Recognise when a benchmark's name implies a construct it does not measure.
- Identify configuration choices (seeds, prompts, decoding, hardware and software) that move a score without changing the model.
- Explain why success criteria get revised after reading outputs.

**Done bar.** Practiced: a table of per-run accuracy over 5 sampled runs with the spread and a standard-error-based 95% CI, plus the paragraph on which 2-point differences you would trust. Mastered: written answers to all three mastery-check questions, checked against Miller, Raji et al., Hochlehnert et al. and Shankar et al., plus explaining to someone else without notes why "model A scored 71.2, model B 70.5" is not a finding.

## Why it matters
- LLM evals are experiments: the questions are a sample from a larger population, so a score is an estimate with error, not a fact ([Miller 2024](https://arxiv.org/abs/2411.00640)).
- Headline benchmarks are proxies. A high score is read as progress on broad goals the benchmark may not measure (construct validity) ([Raji et al. 2021](https://arxiv.org/abs/2111.15366)).
- Reported gains on reasoning benchmarks are sensitive to decoding parameters, seeds, prompt format and hardware/software, and unreported variance makes comparisons unclear ([Hochlehnert et al. 2025](https://arxiv.org/abs/2504.07086)).
- Criteria for "good" are partly defined by looking at outputs ("criteria drift"), so eval design is iterative ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).

## Common failure modes
- Treating a single-run score as truth, with no error bars.
- Treating a benchmark as a general capability measure.
- Comparing systems whose seeds, prompts or decoding differ without saying so.
- Fixing criteria up front and never revising them after reading outputs.

## Practice exercise (2-3 h)
Take a 100-question multiple-choice set (a subset of an open benchmark) and a model API. Run it 5 times with sampling on. Report per-run accuracy, the spread across runs, and a standard-error-based 95% CI from one run. Write a paragraph on which 2-point differences you would trust.

## Mastery check
1. Why is "model A scored 71.2, model B 70.5" not a finding? What would you need?
2. Give an example of a benchmark whose name implies a construct it does not measure.
3. List four configuration choices that can move a reported score without changing the model.

## Sources
- [Miller, "Adding Error Bars to Evals"](https://arxiv.org/abs/2411.00640)
- [Raji et al., "AI and the Everything in the Whole Wide World Benchmark" (NeurIPS 2021 D&B)](https://arxiv.org/abs/2111.15366)
- [Hochlehnert et al., "A Sober Look at Progress in Language Model Reasoning" (COLM 2025)](https://arxiv.org/abs/2504.07086)
- [Shankar et al., "Who Validates the Validators?"](https://arxiv.org/abs/2404.12272)
