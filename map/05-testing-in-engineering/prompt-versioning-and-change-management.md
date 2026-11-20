---
id: prompt-versioning-and-change-management
title: "Prompt versioning and change management"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [regression-testing]
tags: []
---
# Prompt versioning and change management

Treating prompts and configs as versioned artifacts with review and rollback.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Model and prompt versions drift independently; provider lifecycle (Active/Legacy/Deprecated/Retired) forces change ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)); behavior of a named service changed within 3 months ([Chen 2023](https://arxiv.org/abs/2307.09009)). Registry patterns: MLflow prompt versions are immutable, with mutable aliases (e.g., production) enabling rollback by reassigning the alias, integrated with tracing/evaluation ([MLflow prompt registry](https://mlflow.org/docs/latest/genai/prompt-registry/), as-of 2026-11-20). Langfuse: a new prompt under an existing name creates a new version; `production` label selects the live version; SDK-side caching decouples prompts from the critical path ([Langfuse docs](https://langfuse.com/docs/prompt-management/get-started), as-of 2026-11-20).

## Common failure modes
- Cache serving a stale prompt after promotion ([Langfuse](https://langfuse.com/docs/prompt-management/get-started)).
- Prompt versioned but model ID/params/tool schemas/retrieval config not versioned together (author judgement; "config as artifact" per node stub).
- Moving alias without eval run; no link between a version and its eval results.
- Pinning an alias that points to an auto-updating model; Anthropic distinguishes dated IDs vs. undated IDs (deprecation page retires both `claude-sonnet-4-5-20250929` and the undated alias, [source](https://platform.claude.com/docs/en/about-claude/model-deprecations)).

## Practice exercise
Store prompts as files + a manifest {prompt hash, model ID, params, eval run ID}. Script: `promote` requires eval pass; `rollback` repoints alias. Or stand up MLflow/Langfuse locally and do the same. Simulate a bad release and roll back; time it.

## Mastery check
1. What must be in the "release unit" beyond the prompt text?
2. Walk through rollback and what could make it not take effect immediately.
3. How would you attribute a quality drop between prompt change vs. silent model change?

## Sources
[MLflow](https://mlflow.org/docs/latest/genai/prompt-registry/); [Langfuse](https://langfuse.com/docs/prompt-management/get-started); [Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations); [Chen 2023](https://arxiv.org/abs/2307.09009).
