---
id: model-upgrade-and-migration
title: "Model upgrade and migration"
branch: 06-production
depth: L2
status: not-started
bridge: testing
prerequisites: [regression-testing]
tags: [nondeterminism, statistics, cost]
---
# Model upgrade and migration

Evaluating provider model changes and deprecations before switching.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** quality shifts over time, including silent provider-side changes, is owned by [drift-detection](drift-detection.md); this node covers planned model switches driven by deprecation or upgrade.

## Learning objectives
You can:
- Compare an old and new model on golden cases with repeats, using per-slice pass rates with paired bootstrap CIs to decide "not worse" under nondeterminism.
- Test the non-quality surface of a migration: parameters, token limits, latency, cost, formatting, and whether the judge model is also deprecated.
- Audit which keys and services still call a deprecated model, and plan testing well before the retirement date.
- Write a go/no-go memo with a rollback plan via shadow then canary, including how to handle a replacement that is better overall but worse on one slice.

**Done bar.** Practiced: a go/no-go memo for ~100 golden cases (old vs new, 3 repeats) with per-slice paired bootstrap CIs, latency, cost, discordant-case review and a shadow-then-canary rollback plan. Mastered: written answers to all three mastery questions checked against the Anthropic and OpenAI deprecation pages, and one real or capstone model switch evaluated this way with the decision and outcome recorded.

## Why it matters
- Anthropic: models move Active -> Legacy -> Deprecated -> Retired; at least 60 days' notice before retirement of public models; retired requests fail; test replacements well before retirement ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)). Example: `claude-sonnet-4-5-20250929` deprecated 2026-09-30, retires 2026-11-30, replacement `claude-sonnet-5-5` (same page). (volatile; as of 2026-11-20)
- OpenAI: notice of at least 6 months for GA models (about 2 weeks for previews); advises running representative requests against the replacement and comparing outputs, latency, cost ([OpenAI deprecations](https://developers.openai.com/api/docs/deprecations)). Example: `gpt-5` family shutdown 2026-12-11 (same page). (as of release; volatile)
- API parameters can be removed too: Anthropic removed `temperature`, `top_p`, `top_k` in API version `2026-10-21` (returns 400) ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)). (as of release; volatile)
- Behaviour shifts across versions can be large (Chen et al.: [arXiv 2307.09009](https://arxiv.org/abs/2307.09009)).
- Partner platforms (Bedrock, Google-managed) follow their own schedules ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)).

## Common failure modes
- Unpinned aliases silently change (UNVERIFIED for specific providers; the Claude Code alias note on the deprecations page implies aliases resolve to current models).
- Not auditing which keys/services still use a deprecated model: Anthropic suggests a Console Usage export by key and model ([page](https://platform.claude.com/docs/en/about-claude/model-deprecations)).
- Prompts tuned to the old model regress; parameter/API changes break calls; judge model also deprecated (design).
- Migration evaluated only on aggregate score; slice regressions hidden (design).

## Practice exercise (4 h)
(design)
- Take a prompt app with ~100 golden cases. Run old vs new model (or two versions) with 3 repeats each; compare per-slice pass rates with paired bootstrap CIs, plus latency and cost; examine the discordant cases; produce a go/no-go memo and a rollback plan using shadow then canary.

## Mastery check
1. How do you decide a new model is "not worse" statistically given nondeterminism?
2. List non-quality things to test (parameters, token limits, latency, cost, formatting).
3. What is your process when the replacement is worse on one slice but better overall?

## Sources
- [Anthropic model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [OpenAI deprecations](https://developers.openai.com/api/docs/deprecations)
- [Chen et al.](https://arxiv.org/abs/2307.09009)
