---
id: llm-unit-tests
title: "Unit tests for LLM components"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [software-testing-fundamentals, programmatic-checks]
tags: [llm-judge, nondeterminism]
---
# Unit tests for LLM components

Narrow, fast assertions on prompts and components.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Held-out accuracy "often overestimates" model performance; CheckList borrows behavioral testing from software engineering, with a capability x test-type matrix and a test generator; practitioners using it wrote 2x the tests and found ~3x the bugs of those without ([Ribeiro et al., ACL 2020](https://arxiv.org/abs/2005.04118)).
- Anthropic's guidance: success criteria should be specific, measurable, achievable, relevant; evals should mirror the real task distribution incl. edge cases; automate grading; "more questions with slightly lower signal automated grading" beats fewer hand-graded ([Anthropic docs: develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), as-of 2026-11-20).
- The CheckList test names MFT/INV/DIR are NOT confirmed from the abstract page; UNVERIFIED (read paper body before writing them into the node).

## Common failure modes
- Exact-match graders on free text give false failures; the docs show exact match only for constrained labels (sentiment), with cosine similarity, ROUGE-L, and LLM grading for fuzzier tasks ([Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Using the same model to generate and grade; docs advise a different grader model ([Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Happy-path-only cases: docs list irrelevant/nonexistent input, overlong input, harmful input, ambiguous cases as edge cases ([same](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Single-run assertions on a nondeterministic component (see determinism and flaky nodes).

## Practice exercise (3 h)
Pick one prompt (e.g., ticket-classifier). Write 30 pytest cases: 15 exact-label, 5 edge (empty, 10k chars, sarcasm, mixed), 5 format checks (JSON schema), 5 LLM-graded. Record each with a mock/VCR cassette so the suite runs offline in <5s. Seed a deliberate prompt bug; confirm which tests catch it.

## Mastery check
1. Which assertions in your suite are deterministic checks vs. LLM-graded, and why that split?
2. Show a test that passes on a wrong answer (false pass) and fix it.
3. Explain why a 95% pass rate on 20 cases is weak evidence (link to CI node).

## Sources
- [CheckList, Ribeiro et al., arXiv 2005.04118](https://arxiv.org/abs/2005.04118)
- [Anthropic docs: develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
