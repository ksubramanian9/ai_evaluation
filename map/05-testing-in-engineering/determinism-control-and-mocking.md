---
id: determinism-control-and-mocking
title: "Determinism control and mocking"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [nondeterminism-and-variance]
tags: [nondeterminism]
---
# Determinism control and mocking

Seeds, temperature, recorded responses, and mocks to make tests repeatable.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
"Deterministic" settings do not give repeatable results: across 5 LLMs x 8 tasks x 10 runs, accuracy varied up to 15% between runs and best-to-worst gap reached 70%; no model was consistently repeatable ([Atil et al., arXiv 2408.04667](https://arxiv.org/abs/2408.04667)). Cause per Thinking Machines: kernels are not batch-invariant, so server load changes batch size and thus numerics; Qwen3-235B at temperature 0 gave 80 unique completions in 1000 samples, diverging at token 103; batch-invariant kernels made all 1000 identical, at a speed cost ([Thinking Machines, 2025](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/); company research blog, treat as primary-from-practitioner-lab). OpenAI's seed gives "mostly" identical outputs when seed, parameters and `system_fingerprint` match; residual nondeterminism remains ([OpenAI cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter); Azure says the same: [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output)). Note: Anthropic API version 2026-10-21 returns HTTP 400 if `temperature`, `top_p`, or `top_k` is sent, even at defaults ([Anthropic migration guide](https://platform.claude.com/docs/en/api/migration-2026-10-21)); sampling control may be unavailable per provider, so mocking/recording is the dependable repeatability lever. (Volatile, as-of 2026-11-20.)

## Common failure modes
- Assuming temperature 0 or a seed implies identical output (refuted above).
- Ignoring `system_fingerprint`/model snapshot changes between runs ([OpenAI cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter)).
- Stale cassettes: VCR record mode `once` replays and errors on new requests; `new_episodes` silently records new ones; `none` guarantees no new HTTP calls; `all` never replays ([VCR.py docs](https://vcrpy.readthedocs.io/en/latest/usage.html)). Prompt change plus replayed cassette = test that never hits the model.
- Mocks that hide real behavior, so tests pass while production fails (author judgement).
- Secrets recorded in cassettes. VCR.py filtering: UNVERIFIED on the usage page (it points to Configuration docs).

## Practice exercise
Send the same prompt 50x to one API (temp 0 if allowed) and count unique outputs and first-divergence token. Then wrap the client with VCR.py (record `once`), show the second run makes zero network calls, and write a test that fails if the cassette is missing in CI (record mode `none`).

## Mastery check
1. Explain why batch size changes outputs at temperature 0.
2. When should a test use a recorded response vs. live call vs. mock?
3. Design cassette invalidation keyed on prompt hash + model ID.

## Sources
[Atil 2408.04667](https://arxiv.org/abs/2408.04667); [Thinking Machines](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/); [OpenAI cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter); [VCR.py](https://vcrpy.readthedocs.io/en/latest/usage.html); [Anthropic migration 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21).
