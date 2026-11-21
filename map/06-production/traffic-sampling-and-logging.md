---
id: traffic-sampling-and-logging
title: "Traffic sampling and logging"
branch: 06-production
depth: L2
status: not-started
bridge: none
prerequisites: [observability-and-tracing]
tags: [privacy, statistics, cost]
---
# Traffic sampling and logging

Which production traffic to log and sample, including privacy constraints.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Choose between head and tail sampling (or a combination) given a requirement such as "keep every failure", and state what tail sampling costs to operate.
- Implement stratified sampling that keeps rare failures and compute unbiased metric estimates with inverse-probability weights.
- Apply a PII scrubbing pass and measure its misses by manual inspection rather than assuming it is complete.
- Write a prompt-retention policy justified against data minimisation and storage limitation.

**Done bar.** Practiced: a comparison of uniform vs stratified-with-weights samples on 5k logs, showing bias/variance of a known metric over 200 repeats, plus a count of Presidio misses in 50 inspected samples. Mastered: written answers to all three mastery questions checked against the OTel sampling page, GDPR Art. 5 and Presidio docs, and a sampling rule and retention policy applied to a capstone or real system with the resulting volumes recorded.

## Why it matters
- Head sampling decides early (e.g. consistent probability by trace ID); simple and cheap but cannot keep "every error trace". Tail sampling decides on the whole trace (errors, latency, attributes) but is stateful and harder to operate; the docs say it is "almost always necessary" for larger systems and suggest combining both for very high volume ([OTel sampling](https://opentelemetry.io/docs/concepts/sampling/)).
- Eval cost: online LLM judging costs about $0.01-0.10 per assessment (Langfuse estimate) so you must sample ([Langfuse docs](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge), practitioner/vendor; as of release; volatile).
- Privacy: GDPR Art. 5 requires data "limited to what is necessary" (minimisation) and kept identifiable "no longer than is necessary" (storage limitation) ([GDPR Art. 5 text](https://gdpr-info.eu/art-5-gdpr/), unofficial reproduction of the regulation; official text at EUR-Lex not fetched).

## Common failure modes
- Uniform random sampling under-represents rare failures; error/low-feedback/long-conversation traces need stratified or tail-style rules ([OTel sampling](https://opentelemetry.io/docs/concepts/sampling/)).
- Log content retention beyond need violates storage limitation (above).
- Automated PII scrubbing is incomplete: Presidio itself states "there is no guarantee that Presidio will find all sensitive information" ([Presidio docs](https://presidio.dataprivacystack.org/)).
- Sampling bias into datasets: sampling only thumbs-down or only flagged traces biases evals (design; see online-metrics).

## Practice exercise (4 h)
(design)
- Take 5k synthetic or public chat logs (e.g. a public chat dataset). Implement (a) 2% uniform sample, (b) stratified sample keeping all errors/long/low-confidence plus 1% of the rest with inverse-probability weights.
- Estimate a known metric (e.g. refusal rate) from each; compare bias/variance over 200 repeats.
- Add a Presidio pass and manually inspect 50 samples for misses.

## Mastery check
1. When can head sampling not satisfy "keep all failures"? What does tail sampling cost?
2. How do you get an unbiased metric estimate from a non-uniform sample?
3. State a retention policy for prompts and justify it against minimisation/storage limitation.

## Sources
- [OTel sampling concepts](https://opentelemetry.io/docs/concepts/sampling/)
- [GDPR Art. 5](https://gdpr-info.eu/art-5-gdpr/)
- [Presidio](https://presidio.dataprivacystack.org/)
- (practitioner/vendor) [Langfuse online evaluators](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)
