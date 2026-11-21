---
id: performance-latency-cost-testing
title: "Performance, latency, and cost testing"
branch: 05-testing-in-engineering
depth: L2
status: not-started
bridge: testing
prerequisites: [software-testing-fundamentals]
tags: [cost]
---
# Performance, latency, and cost testing

Load, latency, and token-cost testing as release criteria.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Measure TTFT, total latency, and input and output tokens under fixed concurrency, and report p50, p95 and p99 rather than the mean.
- Compute cost per 1k requests and predict cost changes when migrating to a model with a different tokenizer.
- Apply a latency or cost change and check quality on the golden set before adopting it.
- Build a CI budget assertion that combines quality, latency and cost into one release criterion.

**Done bar.** Practiced: 200 realistic prompts replayed at concurrency 1, 4 and 16 with TTFT, latency percentiles and cost per 1k requests, one change re-measured with a golden-set quality check, and a p95 and cost-per-request assertion in CI. Mastered: written answers to all three mastery questions checked against the Anthropic latency and token-counting docs and the vLLM docs, plus a latency and cost test applied once to a real or capstone endpoint with the percentiles and release decision recorded.

## Why it matters
- Latency and price are named success criteria in Anthropic's eval guidance ([develop-tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Definitions: TTFT = time to first token; levers are model choice, shorter prompts/outputs, `max_tokens`, streaming; asking for exact word counts is less effective than sentence/paragraph limits; optimize latency only after establishing quality ([Anthropic reduce-latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency), as-of 2026-11-20).
- Load tooling: vLLM `bench serve` reports TTFT, ITL, TPOT, throughput; request-rate Poisson arrival, burstiness, max-concurrency, ramp-up; repeated runs can hit prefix cache and inflate throughput ([vLLM docs](https://docs.vllm.ai/en/latest/benchmarking/cli.html), as-of 2026-11-20).
- Cost: token counting endpoint is free (rate-limited), is an estimate, and newer-tokenizer Claude models yield ~30% more tokens for the same text, so recount per model ([Anthropic token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting), as-of 2026-11-20).
- OWASP LLM10 Unbounded Consumption is the security framing ([OWASP](https://genai.owasp.org/llm-top-10/)).
- Batch-invariant kernels cost speed ([Thinking Machines](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)), a determinism/latency tradeoff.

## Common failure modes
- Reporting mean latency, not p95/p99 (author judgement).
- Benchmarking with unrealistic prompt/output length distributions or a cache-warm server ([vLLM caution](https://docs.vllm.ai/en/latest/benchmarking/cli.html)).
- Cost estimated from old model's token counts after migration ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/token-counting)).
- Cheaper/faster config adopted without quality regression check; the Anthropic cookbook for latency pairs each technique with a quality-threshold check ([reduce-latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)).
- Agent loops: unbounded tool calls/retries blow the cost budget.

## Practice exercise (4 h)
Replay 200 realistic prompts at fixed concurrency (1, 4, 16) against your endpoint (or local vLLM). Record TTFT, total latency, input/output tokens per request; compute p50/p95/p99, cost per 1k requests. Apply one change (shorter prompt or smaller model), re-measure, and check quality on the golden set. Add a budget assertion (p95 < X s, cost/request < Y) to CI.

## Mastery check
1. Why p95 not mean; what does concurrency do to TTFT?
2. Predict cost change on migrating to a model with a different tokenizer; verify by count.
3. Define a release criterion combining quality, latency, cost.

## Sources
- [Anthropic docs: develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Anthropic reduce-latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)
- [vLLM benchmarking CLI](https://docs.vllm.ai/en/latest/benchmarking/cli.html)
- [Anthropic token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [Thinking Machines, Defeating Nondeterminism in LLM Inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
