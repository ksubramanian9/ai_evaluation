---
id: software-testing-fundamentals
title: "Software testing fundamentals"
branch: 01-foundations
depth: L2
status: not-started
bridge: testing
prerequisites: []
tags: [nondeterminism]
---
# Software testing fundamentals

Test pyramid, oracles, coverage, regression, and test design techniques that carry over to AI systems.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._
## Why it matters
- The test pyramid (credited to Mike Cohn) says many small fast unit tests, fewer coarse tests, very few end-to-end tests. The inverted "ice-cream cone" is slow and flaky, and tests should check observable behavior, not implementation ([Vocke on martinfowler.com, practitioner](https://martinfowler.com/articles/practical-test-pyramid.html)).
- Google's ML Test Score is a rubric of 28 tests for ML production readiness ([Breck et al. 2017](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)). One reproduction says the score is the minimum across four sections; that is secondary, so confirm in the paper.
- Behavioral testing for NLP carries over test-design ideas (see [error-analysis](error-analysis.md)).
- UNVERIFIED: formal definitions of oracle, regression testing and coverage. The ISTQB glossary fetch returned empty. Use the [ISTQB glossary](https://glossary.istqb.org) or SWEBOK (SWEBOK URL not recorded).

## Common failure modes
- Inverted pyramid: end-to-end-heavy suites.
- Duplicate coverage at several layers (Vocke).
- Treating coverage as a goal (UNVERIFIED as a sourced claim).
- Applying deterministic pass/fail to probabilistic outputs, producing flaky gates (UNVERIFIED as a sourced claim; see [nondeterminism-and-variance](nondeterminism-and-variance.md)).

## Practice exercise (2 h)
Take a small LLM function, such as a classifier-prompt wrapper. Write unit tests for parsing and prompt building (deterministic, no model), contract tests with a mocked model, and a few live-model tests run N times with a pass-rate threshold. Draw the resulting pyramid and note cost and latency per layer.

## Mastery check
1. Which layers of an LLM app can be tested deterministically, and which cannot?
2. Why do end-to-end tests become flaky, and how does LLM nondeterminism make it worse?
3. Give a regression test design for a prompt change.

## Sources
- [Breck et al., "The ML Test Score"](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)
- [ISTQB glossary (to fetch)](https://glossary.istqb.org)
- practitioner: [Vocke, "The Practical Test Pyramid"](https://martinfowler.com/articles/practical-test-pyramid.html)
