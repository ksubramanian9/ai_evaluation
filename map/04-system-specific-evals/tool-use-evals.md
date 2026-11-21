---
id: tool-use-evals
title: "Tool use and function-calling evals"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: testing
prerequisites: [programmatic-checks, nondeterminism-and-variance]
tags: [agents, nondeterminism]
---
# Tool use and function-calling evals

Correct tool selection, argument validity, and error handling.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** pass@k and pass^k are defined once in [nondeterminism-and-variance](../01-foundations/nondeterminism-and-variance.md#passk-and-passk-owned-here).

## Why it matters
- Tool calls can be checked programmatically.
- BFCL uses AST matching (function name, required params, no hallucinated params, strict types) and executable evaluation, with categories simple/multiple/parallel/parallel-multiple and relevance detection (no call when none fits) ([Gorilla BFCL blog, snapshot Aug 2024; later V2/V3 added live data and multi-turn](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)).
- API-Bank assesses planning, retrieving, calling (73 tools, 314 dialogues, 753 calls) ([arXiv 2304.08244](https://arxiv.org/abs/2304.08244)).
- ToolBench: 16,464 RapidAPI APIs, 49 categories, with ToolEval automatic evaluator ([arXiv 2307.16789](https://arxiv.org/abs/2307.16789)).
- tau-bench evaluates by comparing final database state to goal state and introduces pass^k ([arXiv 2406.12045](https://arxiv.org/abs/2406.12045)).

## Common failure modes
- Rigid typing/implicit conversion errors (5% written as 5 vs 0.05), non-executable calls, omitted REST URLs ([BFCL blog](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)).
- Calling a tool when none is relevant ([BFCL](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html) relevance detection).
- Schema-valid but wrong values: structured-output constraints guarantee schema adherence, not correctness; business rules must be validated by the app ([OpenAI Structured Outputs guide, as of 2026-11-20](https://developers.openai.com/api/docs/guides/structured-outputs); as of release; volatile).
- Inconsistency across trials: pass^8 <25% in tau-bench retail (abstract; [arXiv 2406.12045](https://arxiv.org/abs/2406.12045)).
- Over-strict AST matching penalizes valid alternatives (inference; BFCL notes list-order and strict type rules).

## Practice exercise (4 h)
Define 5 tools (JSON schema). Write 40 prompts including 10 needing no tool and 10 parallel. Grade with a code checker: name match, jsonschema validation, argument equality with normalization, and executable result match against a mock. Report per-category accuracy and 5-trial pass^k.

## Mastery check
1. AST vs execution grading trade-offs.
2. How do you test "should not call"?
3. Why is schema validity insufficient?
4. Compute pass^k from per-task success rates.

## Sources
- [Gorilla BFCL blog](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)
- [API-Bank, arXiv 2304.08244](https://arxiv.org/abs/2304.08244)
- [ToolBench, arXiv 2307.16789](https://arxiv.org/abs/2307.16789)
- [tau-bench, arXiv 2406.12045](https://arxiv.org/abs/2406.12045)
- [OpenAI Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs)
