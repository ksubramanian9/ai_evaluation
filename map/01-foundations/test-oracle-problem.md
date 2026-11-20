---
id: test-oracle-problem
title: "The test oracle problem"
branch: 01-foundations
depth: L2
status: not-started
bridge: testing
prerequisites: [software-testing-fundamentals]
tags: [nondeterminism]
---
# The test oracle problem

How to decide pass/fail when the expected output is not unique or not known.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._
## Why it matters
- The canonical survey defines an oracle as something that distinguishes correct from incorrect behavior of the system under test, and surveys automation via modelling, specifications, contract-driven development and metamorphic testing ([Barr et al., IEEE TSE 2015](https://discovery-pp.ucl.ac.uk/id/eprint/1471263); abstract level only).
- Metamorphic testing has its own survey with open challenges ([Segura et al., IEEE TSE 2016](https://eprints.whiterose.ac.uk/110335/); abstract level only).
- CheckList uses minimum-functionality, invariance and directional-expectation tests so NLP tests need no exact expected output ([Ribeiro et al. 2020](https://arxiv.org/abs/2005.04118)). The test-type names were recalled, not fetched: UNVERIFIED, check the paper.
- An LLM judge is a pseudo-oracle. GPT-4-class judges reached over 80% agreement with human preferences but show position, verbosity and self-enhancement bias ([Zheng et al., NeurIPS 2023 D&B](https://arxiv.org/abs/2306.05685)). Judges need validation against human labels ([Shankar et al.](https://arxiv.org/abs/2404.12272)).

## Common failure modes
- Exact-match oracle on free text, giving false failures.
- Trusting an LLM judge without measuring its agreement and bias.
- Metamorphic relations that are not truly invariant, such as a paraphrase that changes meaning (UNVERIFIED as a sourced claim).
- Self-preference: a judge grading its own model family favorably (Zheng et al.).

## Practice exercise (3 h)
For a summarization or QA task, build three oracle types: (a) reference/exact-match, (b) property checks (length, required entities, valid JSON) plus metamorphic relations (a paraphrased question must keep its answer), and (c) an LLM judge. Run all three on 50 outputs, hand-label the same 50, and report each oracle's agreement and false-pass and false-fail rates. Test judge position bias by swapping pair order.

## Mastery check
1. Give two metamorphic relations for a QA system and one case where a relation is invalid.
2. What evidence would you need before gating CI on an LLM judge?
3. When is a partial oracle (properties) preferable to a reference answer?

## Sources
- Barr et al., "The Oracle Problem in Software Testing: A Survey" (IEEE TSE 2015): https://discovery-pp.ucl.ac.uk/id/eprint/1471263
- Segura et al., metamorphic testing survey (IEEE TSE 2016): https://eprints.whiterose.ac.uk/110335/
- Zheng et al., MT-Bench / LLM-as-a-judge: https://arxiv.org/abs/2306.05685
- Ribeiro et al., CheckList (ACL 2020): https://arxiv.org/abs/2005.04118
