---
id: programmatic-checks
title: "Programmatic checks"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: testing
prerequisites: [test-oracle-problem]
tags: [security]
---
# Programmatic checks

Exact match, regex, schema validation, and code execution as cheap deterministic graders.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Deterministic graders are cheap and reproducible.
- Anthropic's eval docs list exact match (after normalizing whitespace/case), cosine similarity and ROUGE-L as code-based graders, and say to design questions so they allow automated grading (multiple choice, string match, code-graded, LLM-graded) ([Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- HumanEval grades by functional correctness of generated programs against tests, not text similarity ([Chen et al. 2021](https://arxiv.org/abs/2107.03374)).
- IFEval uses 25 "verifiable instruction" types (about 500 prompts) so instruction following can be checked without humans or an LLM judge, citing the cost and bias of those alternatives ([Zhou et al. 2023](https://arxiv.org/abs/2311.07911)).

## Common failure modes
- Schema-valid is not correct. OpenAI Structured Outputs guarantee schema adherence (JSON mode only guarantees valid JSON), but the docs say your code must validate business rules the schema does not express, and refusals/incomplete outputs still need handling ([OpenAI docs, as-of 2026-11-20](https://developers.openai.com/api/docs/guides/structured-outputs)).
- Exact match is brittle to formatting and paraphrase (design inference from the normalization caveat in the Anthropic docs, not a sourced finding).
- Code execution needs sandboxing and tests that discriminate (weak tests pass wrong code). UNVERIFIED as a specific cited claim.
- Repeated sampling changes the score: Codex solved 28.8% of HumanEval at 1 sample and 70.2% with 100 samples per problem ([Chen et al.](https://arxiv.org/abs/2107.03374)).

## Practice exercise (2-3 h)
Take about 50 prompts with JSON output. Write three graders: JSON parse, JSON-schema validation, business-rule check. Compare pass rates and hand-inspect 10 schema-valid outputs for wrong values. Then run 20 HumanEval-style problems with a test runner in a subprocess with a timeout.

## Mastery check
1. Why does 100% schema validity not imply 100% correctness?
2. Give a task where exact match under-counts and one where it over-counts.
3. What would an IFEval-style verifier for "mention AI at least 3 times" look like?
4. How does the number of samples change a functional-correctness score?

## Sources
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [OpenAI, Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Chen et al. 2021, Codex/HumanEval](https://arxiv.org/abs/2107.03374)
- [Zhou et al. 2023, IFEval](https://arxiv.org/abs/2311.07911)
