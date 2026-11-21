---
id: regression-testing
title: "Regression testing"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [golden-datasets, baselines-and-thresholds]
tags: [statistics, nondeterminism]
---
# Regression testing

Detecting quality drops after prompt, model, or code changes.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Provider models change under you: GPT-4 prime-vs-composite accuracy fell 84% to 51% between March and June 2023 versions; GPT-3.5 moved the other way on some tasks; instruction-following declined, and authors call for "continuous monitoring" ([Chen, Zaharia, Zou, arXiv 2307.09009](https://arxiv.org/abs/2307.09009)).
- Providers retire models on a schedule (at least 60 days' notice for public models) and advise testing replacements well ahead ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations), as-of 2026-11-20; e.g., `claude-sonnet-4-5-20250929` retirement 2026-11-30 listed there).
- Behavioral test suites (CheckList) are a regression format ([Ribeiro 2020](https://arxiv.org/abs/2005.04118)).

## Common failure modes
- Only aggregate score compared; per-slice regressions hidden by improvements elsewhere (author judgement; see coverage-and-slicing).
- Overfitting prompts to the golden set; set becomes stale.
- Comparing runs without noise estimate, so noise reads as regression (see Atil: up to 15% run-to-run accuracy variation, [arXiv 2408.04667](https://arxiv.org/abs/2408.04667)).
- Migrating models without re-running the suite, relying on the new model being "better"; Chen et al. show newer versions can be worse on specific tasks ([arXiv 2307.09009](https://arxiv.org/abs/2307.09009)).

## Practice exercise (4 h)
Take the unit-test suite plus ~100-case golden set. Run on model A and model B (or two prompt versions) x5 repeats. Report per-case flip table (pass->fail, fail->pass), per-slice deltas, and paired bootstrap CI on the difference. Decide ship/no-ship with a written rule.

## Mastery check
1. Why compare paired per-case results rather than two aggregate numbers?
2. A new model improves overall +2% but regresses a critical slice -8%: what is the decision rule?
3. How many repeats make a 3-point change detectable? (compute from your own variance)

## Sources
- [Chen, Zaharia, Zou, arXiv 2307.09009](https://arxiv.org/abs/2307.09009)
- [Anthropic model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [CheckList, arXiv 2005.04118](https://arxiv.org/abs/2005.04118)
- [Atil et al., arXiv 2408.04667](https://arxiv.org/abs/2408.04667)
