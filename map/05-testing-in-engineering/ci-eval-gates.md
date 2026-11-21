---
id: ci-eval-gates
title: "CI/CD eval gates"
branch: 05-testing-in-engineering
depth: L3
status: not-started
bridge: testing
prerequisites: [regression-testing, eval-harness-design]
tags: [statistics, cost]
---
# CI/CD eval gates

Running evals in the pipeline and blocking releases on thresholds.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Build a CI workflow that runs an eval suite on prompt changes, publishes a report and fails on a threshold.
- Justify a gate threshold from measured baseline variance instead of an arbitrary number.
- Design a tiered gate that decides which checks block merge, which warn and which run nightly, trading cost and time against coverage.
- Critique a gate for flakiness, stale caches and data leakage in logs, and prevent a flaky gate from being bypassed.

**Done bar.** Practiced: a GitHub Actions workflow running a 50-case suite (cached deterministic checks plus 10 live LLM-graded cases) that publishes JUnit output and fails below baseline minus 2 SE, with fast PR and nightly tiers. Mastered: written answers to all three mastery questions checked against the promptfoo CI/CD docs and the ML Test Score, plus a review of a real gate (yours or a team's) that finds a flaw this node covers and states the cost-versus-coverage trade-off of the fix.

## Why it matters
- The ML Test Score rubric (28 tests/monitoring items from production systems, IEEE Big Data 2017) is the foundational "is this ML system production-ready" checklist ([Breck et al.](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)).
- Tooling example: promptfoo runs evals on PRs touching `prompts/**` or the config, supports `--fail-on-error`, custom pass-rate gates (docs example 95%), caching via `actions/cache`, JUnit XML output, and scheduled red-team runs ([promptfoo CI/CD docs](https://www.promptfoo.dev/docs/integrations/ci-cd/), tool docs, as-of 2026-11-20).

## Common failure modes
- Gating on a noisy metric: flaky gate trains people to rerun/ignore (see flaky node).
- Cost/time blowup: running full eval on every commit; mitigations include caching and path filters ([promptfoo](https://www.promptfoo.dev/docs/integrations/ci-cd/)).
- Rate limits in CI; docs suggest caching and `-j 1` ([promptfoo](https://www.promptfoo.dev/docs/integrations/ci-cd/)).
- Cache key not covering all inputs, giving stale passes ([promptfoo troubleshooting](https://www.promptfoo.dev/docs/integrations/ci-cd/)).
- Leaking data in CI logs/artifacts; promptfoo offers `PROMPTFOO_STRIP_RESPONSE_OUTPUT` and `PROMPTFOO_STRIP_TEST_VARS` ([same](https://www.promptfoo.dev/docs/integrations/ci-cd/)).
- Threshold chosen arbitrarily rather than from baseline variance (author judgement).

## Practice exercise (4 h)
GitHub Actions workflow: on PR changing prompts, run a 50-case suite (cached/cassette for deterministic checks, live for 10 LLM-graded cases), publish JUnit report, fail if pass rate < baseline minus 2 SE. Two tiers: fast PR gate, nightly full suite plus red-team.

## Mastery check
1. Justify your threshold from measured baseline variance.
2. Which checks block merge vs. warn vs. run nightly, and why?
3. How do you stop a failing-but-flaky gate being bypassed?

## Sources
- [promptfoo CI/CD docs](https://www.promptfoo.dev/docs/integrations/ci-cd/)
- [Breck et al., The ML Test Score](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)
