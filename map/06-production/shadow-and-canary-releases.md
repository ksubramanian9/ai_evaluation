---
id: shadow-and-canary-releases
title: "Shadow and canary releases"
branch: 06-production
depth: L2
status: not-started
bridge: testing
prerequisites: [ci-eval-gates]
tags: [statistics, agents]
---
# Shadow and canary releases

Safe rollout patterns for model and prompt changes.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Explain what shadow testing and canarying each reveal and fail to reveal, including why shadow outputs need a judge or reference.
- Build a router that canaries a fraction of traffic to a candidate and mirrors replayed traffic to it in shadow.
- Choose canary metrics and thresholds (latency, cost, format validity, judge score, absolute SLOs) and match the metric interval to the canary duration.
- Write and test an automatic rollback rule against an injected regression.

**Done bar.** Practiced: a working canary/shadow router with a comparison of latency, cost, format-validity rate and judge score, plus a rollback rule shown to fire on an injected regression. Mastered: written answers to all three mastery questions checked against the SRE Workbook and AWS shadow-test docs, and one real or capstone prompt/model change rolled out via shadow or canary with the metrics and go/rollback decision recorded.

## Why it matters
- Canarying is "a partial and time-limited deployment of a change in a service and its evaluation"; canary vs control is effectively A/B testing; exposure of a defect is proportional to canary traffic ([SRE Workbook: canarying](https://sre.google/workbook/canarying-releases/)).
- Shadow testing mirrors a copy of live requests to the new variant while only the production variant's response is returned; responses are discarded or logged for offline comparison ([AWS SageMaker shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html), (as of release; volatile) vendor docs). It validates operational metrics before promotion.

## Common failure modes
- From the SRE Workbook: imperfect isolation between canary and control ([workbook](https://sre.google/workbook/canarying-releases/)).
- From the SRE Workbook: miscalibrated thresholds, and a metric interval longer than the canary duration ([workbook](https://sre.google/workbook/canarying-releases/)).
- From the SRE Workbook: synthetic load missing state, and before/after comparison confounded by time ([workbook](https://sre.google/workbook/canarying-releases/)).
- From the SRE Workbook: run one canary at a time; use absolute SLOs as well as relative comparison ([workbook](https://sre.google/workbook/canarying-releases/)).
- LLM-specific: shadow outputs are not seen by users so quality needs a judge or reference (design); stateful agents with side effects cannot be shadowed safely without stubbing tools (design/inference, UNVERIFIED by source).
- Shadow support has constraints (e.g. some endpoint types incompatible) ([AWS](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html)).

## Practice exercise (4 h)
(design)
- Build a router that sends 5% of requests to a candidate prompt/model (canary) and mirrors 100% of a replayed log to it (shadow). Compare latency, cost, format-validity rate, and judge score; write an automatic rollback rule (e.g. abort if error rate > baseline + threshold) and test it with an injected regression.

## Mastery check
1. Shadow vs canary: what does each reveal and not reveal?
2. Pick 3 canary metrics for a RAG chatbot and thresholds; justify.
3. Why could hourly metrics invalidate a 30-minute canary?

## Sources
- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- [AWS SageMaker shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html)
