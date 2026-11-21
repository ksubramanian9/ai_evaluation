---
id: flaky-test-management
title: "Flaky test management"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [determinism-control-and-mocking, confidence-intervals-for-evals]
tags: [nondeterminism, statistics]
---
# Flaky test management

Handling tests whose outcomes vary run to run.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Compute per-test pass rates with Wilson confidence intervals over repeated suite runs and classify tests as stable-pass, stable-fail or flaky.
- Attribute a flaky test to model variance, infrastructure or test design, and distinguish a flaky test from an unreliable model using data.
- Convert a single-shot assertion into a statistical assertion with a chosen N and pass-rate threshold.
- Apply a quarantine policy with an owner and exit criteria.

**Done bar.** Practiced: 20 runs of your suite with per-test pass rate and Wilson CI, a stable/flaky classification, and a cause and fix written down for each flaky test. Mastered: written answers to all three mastery questions checked against Luo et al. and Atil et al., plus a quarantine or statistical-assertion policy applied once to a real or capstone suite with the before and after flake counts recorded.

## Why it matters
- Luo et al. (FSE 2014) inspected 201 commits fixing flaky tests in 51 Apache projects; ten root-cause categories, top three: async wait, concurrency, test-order dependency; 74% of order-dependent flakes fixed via static-field changes ([FSE 2014 via search summary](https://huang.isis.vanderbilt.edu/cs8395/paper/flakytest.pdf); DOI 10.1145/2635868.2635920; ACM page returned 403, details from search snippet, re-verify in PDF).
- LLM-based tests add a new source: model output variance (up to 15% accuracy variation across runs, [Atil](https://arxiv.org/abs/2408.04667)) and batch-dependent numerics ([Thinking Machines](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)).
- Google's flaky-test blog post body did not load; only comments did, so no Google statistics are cited (UNVERIFIED).

## Common failure modes
- Treating LLM variance as "flakiness to retry away": retries hide real 10-30% failure-rate behavior; need pass-rate over N samples with CI instead of single pass/fail (author judgement).
- Quarantine without owner/expiry, so tests rot.
- Auto-rerun until green, masking regressions.
- Flake from external deps (network, rate limits, provider outage) conflated with model variance; Luo's categories include network, time, randomness ([summary](https://huang.isis.vanderbilt.edu/cs8395/paper/flakytest.pdf)).

## Practice exercise (3 h)
Run your suite 20x; per test compute pass rate and Wilson CI. Classify tests: stable-pass, stable-fail, flaky (CI straddles gate). For each flaky one, attribute cause (model variance, infra, test design) and fix: tighten assertion, mock the dependency, or convert to statistical test (N samples, assert pass rate >= p).

## Mastery check
1. Distinguish a flaky test from an unreliable model; how do you tell from data?
2. Design a quarantine policy with exit criteria.
3. Convert a single-shot assertion to a statistical assertion; choose N.

## Sources
- [Luo et al. 2014 (FSE)](https://huang.isis.vanderbilt.edu/cs8395/paper/flakytest.pdf)
- [Atil et al., arXiv 2408.04667](https://arxiv.org/abs/2408.04667)
- [Thinking Machines, Defeating Nondeterminism in LLM Inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
