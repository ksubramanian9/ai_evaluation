---
id: public-benchmarks
title: "Public benchmarks"
branch: 03-measurement-methods
depth: L1
status: not-started
bridge: none
prerequisites: [metric-selection]
tags: [statistics]
---
# Public benchmarks

What standard benchmarks measure and how to read their results.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Explain what a standard benchmark (such as MMLU, HELM or SWE-bench) measures and what it does not.
- Recognise the setup details (prompt format, shots, grader) needed to read a score.
- Recognise label noise and prompt sensitivity as reasons a small leaderboard gap may not be real.
- Explain why your own task eval beats a public score for product decisions.

**Done bar.** Practiced: scores with CIs and a per-subject breakdown for two 100-item benchmark slices under varied prompt formats and shot counts, plus notes on label errors found in 20 read items. Mastered: written answers to all three mastery-check questions, checked against Hendrycks et al., Liang et al., Jimenez et al., Gema et al. and Wang et al., plus explaining to someone else without notes what one benchmark measures and why label noise or prompt sensitivity limits it.

## Why it matters
- Benchmarks give shared, comparable measurement.
- MMLU: 57 tasks, most 2020 models near chance ([Hendrycks et al. 2021](https://arxiv.org/abs/2009.03300)).
- HELM: 42 scenarios and 7 metrics (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) across 30 models ([Liang et al.](https://arxiv.org/abs/2211.09110)).
- SWE-bench: 2,294 real GitHub issue tasks over 12 Python repos; best model at publication resolved 1.96% ([Jimenez et al. 2023](https://arxiv.org/abs/2310.06770)).
- HumanEval, IFEval and MT-Bench are covered above.
- Successors: MMLU-Pro (10 options, 16-33% accuracy drop) ([Wang et al. 2024](https://arxiv.org/abs/2406.01574)); SuperGPQA (285 disciplines; top score 61.82% at paper time) ([SuperGPQA](https://arxiv.org/abs/2502.14739)).

## Common failure modes
- Label noise: MMLU-Redux estimates 6.49% of MMLU questions contain errors (57% in the Virology sample) ([Gema et al. 2024](https://arxiv.org/abs/2406.04127)).
- Prompt sensitivity (MMLU-Pro above).
- Reading a score without its setup (prompt, shots, grader); see eval-harness-design.
- Aggregate hides uneven per-task performance ([Hendrycks et al.](https://arxiv.org/abs/2009.03300)).

## Practice exercise (2-3 h)
Run a small open model on 100-item slices of two benchmarks via lm-eval or Inspect. Vary prompt format and number of shots. Report scores with CIs and a per-subject breakdown. Read 20 items for label errors.

## Mastery check
1. State what construct a benchmark measures and what it does not.
2. How would you decide whether a 1-point leaderboard gap is real?
3. Why prefer your own task eval to a public score for product decisions?

## Sources
- [Hendrycks et al. 2021, MMLU](https://arxiv.org/abs/2009.03300)
- [Liang et al. 2022, HELM](https://arxiv.org/abs/2211.09110)
- [Jimenez et al. 2023, SWE-bench](https://arxiv.org/abs/2310.06770)
- [Gema et al. 2024, MMLU-Redux](https://arxiv.org/abs/2406.04127)
- [Wang et al. 2024, MMLU-Pro](https://arxiv.org/abs/2406.01574)
- [SuperGPQA](https://arxiv.org/abs/2502.14739)
