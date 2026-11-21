---
id: feedback-loop-to-datasets
title: "Feedback loop into datasets"
branch: 06-production
depth: L2
status: not-started
bridge: none
prerequisites: [traffic-sampling-and-logging, golden-datasets]
tags: [human-labels, privacy]
---
# Feedback loop into datasets

Turning production failures into new test cases.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Mine failures from logged traces, cluster them by error type and write a minimal test case per cluster (input, expected property, scorer).
- Add promoted cases to a versioned dataset with provenance metadata (source trace id, date, label author, privacy status) and anonymise them.
- Split mined cases into a dev set for tuning and a frozen holdout so fixed failures do not inflate scores.
- Apply a check that labels come from a validated source, not an unvalidated judge, and re-label when criteria drift.

**Done bar.** Practiced: a versioned dataset of test cases from 50 mined failures, with provenance fields, a dev/holdout split, and a record showing the fix flips the case without regressing the older set. Mastered: written answers to all three mastery questions checked against Shankar et al. 2022/2024 and Sculley et al., and the loop run once on capstone or real-work traces with the promoted cases and holdout result recorded.

## Why it matters
- Interviews with 18 ML engineers identify Velocity, Validation and Versioning as the variables governing production success and describe continual monitoring of production performance drops as part of the loop ([Shankar et al. 2022](https://arxiv.org/abs/2209.09125)).
- Evaluation criteria evolve as you look at outputs ("criteria drift"), so datasets must be refreshed from observed failures ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).
- Anthropic's guidance: mirror the real task distribution and include edge cases; more automatically graded questions beat fewer hand-graded ([Anthropic develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests); as of release; volatile). That page's explicit guidance on production data was not seen (only first 100k chars read).

## Common failure modes
- Hidden feedback loops and entanglement ([Sculley et al.](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)).
- Test-set contamination by training on or tuning against mined failures (design; cross-ref golden-datasets).
- Unrepresentative mining (only thumbs-down) skews dataset; privacy of logged data (see traffic-sampling-and-logging).
- Labels from an unvalidated judge become the ground truth (Shankar 2024).

## Practice exercise (3 h)
(design)
- From logged traces with a failure flag, mine 50 failures, cluster by error type, write a minimal test case per cluster (input, expected property, scorer), anonymise, add to a versioned dataset with provenance fields, split into dev (for tuning) and a frozen holdout, and confirm the fix flips the case and does not regress the older set.

## Mastery check
1. How do you keep a mined-failure set from inflating scores after you fix those failures?
2. What metadata should each promoted case carry (source trace id, date, label author, privacy status)?
3. How does criteria drift change when you re-label?

## Sources
- [Shankar et al. 2022 Operationalizing ML](https://arxiv.org/abs/2209.09125)
- [Shankar et al. 2024 Who validates the validators](https://arxiv.org/abs/2404.12272)
- [Sculley et al.](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)
