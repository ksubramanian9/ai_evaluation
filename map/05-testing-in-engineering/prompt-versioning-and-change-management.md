---
id: prompt-versioning-and-change-management
title: "Prompt versioning and change management"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [regression-testing]
tags: [nondeterminism]
---
# Prompt versioning and change management

Treating prompts and configs as versioned artifacts with review and rollback.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Build a release manifest that versions the prompt together with model ID, parameters and eval run ID.
- Apply promote and rollback steps that require an eval pass and repoint an alias.
- Explain what can stop a rollback taking effect immediately, such as cached prompts or undated model aliases.
- Attribute a quality drop to a prompt change versus a silent model change.

**Done bar.** Practiced: prompts stored as files with a manifest, a promote script gated on an eval pass and a rollback script, plus a simulated bad release rolled back with the time recorded. Mastered: written answers to all three mastery questions checked against the MLflow, Langfuse and Anthropic deprecation docs, plus versioning applied once to a real or capstone prompt with a promotion or rollback recorded.

## Why it matters
- Model and prompt versions drift independently; provider lifecycle (Active/Legacy/Deprecated/Retired) forces change ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)).
- Behavior of a named service changed within 3 months ([Chen 2023](https://arxiv.org/abs/2307.09009)).
- Registry patterns: MLflow prompt versions are immutable, with mutable aliases (e.g., production) enabling rollback by reassigning the alias, integrated with tracing/evaluation ([MLflow prompt registry](https://mlflow.org/docs/latest/genai/prompt-registry/), as-of 2026-11-20).
- Langfuse: a new prompt under an existing name creates a new version; `production` label selects the live version; SDK-side caching decouples prompts from the critical path ([Langfuse docs](https://langfuse.com/docs/prompt-management/get-started), as-of 2026-11-20).

## Common failure modes
- Cache serving a stale prompt after promotion ([Langfuse](https://langfuse.com/docs/prompt-management/get-started)).
- Prompt versioned but model ID/params/tool schemas/retrieval config not versioned together (author judgement; "config as artifact" per node stub).
- Moving alias without eval run; no link between a version and its eval results.
- Pinning an alias that points to an auto-updating model; Anthropic distinguishes dated IDs vs. undated IDs (deprecation page retires both `claude-sonnet-4-5-20250929` and the undated alias, [source](https://platform.claude.com/docs/en/about-claude/model-deprecations)).

## Practice exercise (3 h)
Store prompts as files + a manifest {prompt hash, model ID, params, eval run ID}. Script: `promote` requires eval pass; `rollback` repoints alias. Or stand up MLflow/Langfuse locally and do the same. Simulate a bad release and roll back; time it.

## Mastery check
1. What must be in the "release unit" beyond the prompt text?
2. Walk through rollback and what could make it not take effect immediately.
3. How would you attribute a quality drop between prompt change vs. silent model change?

## Sources
- [MLflow prompt registry](https://mlflow.org/docs/latest/genai/prompt-registry/)
- [Langfuse prompt management](https://langfuse.com/docs/prompt-management/get-started)
- [Anthropic model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [Chen, Zaharia, Zou 2023, arXiv 2307.09009](https://arxiv.org/abs/2307.09009)
