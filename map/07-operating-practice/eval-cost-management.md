---
id: eval-cost-management
title: "Eval cost management"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [llm-as-judge, confidence-intervals-for-evals]
tags: [cost]
---
# Eval cost management

Controlling judge, human, and compute cost with sampling and tiering.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Provider batch discounts: Anthropic Message Batches API cuts cost 50%, most batches finish in under 1 hour, and the page lists large-scale evaluations as a use case; 29-day retention, not ZDR-eligible ([Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/batch-processing)). OpenAI Batch API: 50% discount, 24-hour window, lists running evaluations ([OpenAI docs](https://developers.openai.com/api/docs/guides/batch)). As-of 2026-11-20, volatile.
- Prompt caching (Anthropic): 5-minute cache write 1.25x, 1-hour write 2x, read 0.1x of base input (0.05x for Opus 5.5/Sonnet 5.5; 0.025x for some models); multipliers stack with batch discount; minimum cacheable prompt 512-4096 tokens by model ([Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)). As-of 2026-11-20, volatile. Useful when a long rubric or few-shot judge prompt is repeated.
- FrugalGPT (Chen, Zaharia, Zou, 2023): prompt adaptation, LLM approximation, LLM cascade; reports matching GPT-4 at up to 98% lower cost ([arXiv 2305.05176](https://arxiv.org/abs/2305.05176)). Applies to tiered judges (cheap judge first, escalate uncertain cases). Result is for specific 2023 models/datasets; generality to judging UNVERIFIED.
- Anthropic docs: "volume over quality" (more automated-graded questions beat fewer hand-graded) ([Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Statistical sample sizing from Miller (power analysis) bounds how many items you need ([arXiv 2411.00640](https://arxiv.org/abs/2411.00640)).

## Common failure modes
- Cheaper judge adopted without re-validating agreement with humans (Shankar et al., [arXiv 2404.12272](https://arxiv.org/abs/2404.12272)).
- Cutting sample size below the power needed, then reading noise as signal (Miller).
- Running full suite on every commit instead of tiering (smoke -> nightly -> release); not caching deterministic outputs; ignoring batch/caching for offline runs.
- Counting only API cost, not human grading time or engineer time (inference).
- Not logging cost per eval run, so spend is invisible.

## Practice exercise
Instrument an eval run to record tokens and cost per item and per judge call. Compare: sync full run, batch full run, cached-prefix run, and cascade (cheap judge, escalate low-confidence to strong judge) on 300 items. Report cost, wall time, and agreement with a 50-item human gold set.

## Mastery check
1. Design a three-tier eval schedule (per-commit, nightly, release) with item counts justified by power analysis.
2. When does caching save money for judging and when not (minimum token, TTL)?
3. How do you prove a cheaper judge is acceptable?

## Sources
- https://platform.claude.com/docs/en/build-with-claude/batch-processing ; .../prompt-caching ; https://developers.openai.com/api/docs/guides/batch
- https://arxiv.org/abs/2305.05176 ; https://arxiv.org/abs/2411.00640
