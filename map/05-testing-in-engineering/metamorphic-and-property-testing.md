---
id: metamorphic-and-property-testing
title: "Metamorphic and property-based testing"
branch: 05-testing-in-engineering
depth: L3
status: not-started
bridge: testing
prerequisites: [test-oracle-problem]
tags: []
---
# Metamorphic and property-based testing

Testing invariants and relations between outputs when no exact oracle exists.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Metamorphic testing (MT) addresses both test generation and the oracle problem: check relations between outputs of related inputs rather than exact outputs ([Chen et al., ACM CSUR 51(1), 2018](https://research.nottingham.edu.cn/en/publications/metamorphic-testing-a-review-of-challenges-and-opportunities/), bibliographic details via search; ACM page 403). For LLMs: Cho, Ruberto, Terragni collected 191 MRs for NLP tasks, implemented 36, ran ~560,000 metamorphic tests on three LLMs ([arXiv 2511.02108](https://arxiv.org/abs/2511.02108)); the "~11% MT-only failures" figure is from a secondary summary, UNVERIFIED. Property-based testing: Hypothesis generates inputs across a defined range, including edge cases ([Hypothesis docs](https://hypothesis.readthedocs.io/en/latest/)); shrinking/database are not described on that page (UNVERIFIED there).

## Common failure modes
- Weak MRs that any model satisfies (e.g., trivially constant output), giving false confidence (author judgement).
- MRs that are not truly semantics-preserving (paraphrase changes meaning), producing false alarms.
- Property generators producing unrealistic inputs.
- Treating MT as complete: MT detects inconsistency, not consistent wrongness; both original and follow-up can be wrong the same way.

## Practice exercise
For a QA or classification prompt define 5 MRs (paraphrase invariance, irrelevant-sentence insertion invariance, negation flips label, entity swap preserves structure, unit-conversion equivalence). Generate follow-ups programmatically (templates or Hypothesis strategies), run 200 pairs, report violation rate per MR, manually audit 20 violations for MR validity vs. model bug.

## Mastery check
1. Give an MR for a summarizer and say what class of bug it cannot catch.
2. How do you validate an MR is itself correct?
3. Property vs. metamorphic relation: example of each for an extraction task.

## Sources
[Chen 2018](https://research.nottingham.edu.cn/en/publications/metamorphic-testing-a-review-of-challenges-and-opportunities/); [Cho 2511.02108](https://arxiv.org/abs/2511.02108); [Hypothesis](https://hypothesis.readthedocs.io/en/latest/).
