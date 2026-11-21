---
id: observability-and-tracing
title: "Observability and tracing"
branch: 06-production
depth: L2
status: not-started
bridge: testing
prerequisites: [eval-harness-design]
tags: [privacy, rag, agents]
---
# Observability and tracing

Capturing traces of prompts, retrievals, tool calls, and outputs for debugging and evaluation.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- OpenTelemetry has GenAI semantic conventions that standardise spans for model calls, retrieval, tool execution and agents. Well-known `gen_ai.operation.name` values include `chat`, `embeddings`, `retrieval`, `execute_tool`, `invoke_agent`, `plan`, `search_memory` ([OTel GenAI spans](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)). A shared schema lets eval tooling and backends consume traces from any instrumented stack. (as of release; volatile)
- The conventions moved out of the core semconv site into a separate repo ([OTel moved notice](https://opentelemetry.io/docs/specs/semconv/gen-ai/)); spans and most attributes are marked Development (unstable) ([spans spec](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)). (volatile; as of 2026-11-20)
- Traces are the raw material for later nodes (sampling, judges, dataset mining, incident debugging). Sculley et al. note ML systems carry ongoing maintenance cost from data dependencies and external-world change ([Hidden Technical Debt, NIPS 2015](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)); traces are how you see them.

## Common failure modes
- Capturing content by default leaks PII: the spec marks message/system-instruction/tool-definition attributes as Opt-In and warns they are "likely to contain sensitive information including user/PII data"; content capture defaults to `NO_CONTENT`, controlled by `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT` (`NO_CONTENT|SPAN_ONLY|EVENT_ONLY|SPAN_AND_EVENT`) ([spans spec](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)). The opposite failure: leaving it off means traces cannot be evaluated or turned into test cases.
- Attribute churn: unstable conventions can change between versions; pin instrumentation versions (inference from Development status; the status itself is cited above).
- Traces missing the retrieval and tool steps, so RAG/agent failures cannot be localised (design).
- Sampling decisions that drop error traces (see traffic-sampling-and-logging).

## Practice exercise (4 h)
(design)
- Build a small RAG or tool-calling script. Instrument it with the OTel SDK (or an OTel-GenAI instrumentation library), emitting `chat`, `retrieval` and `execute_tool` spans, and export to a local backend (Jaeger or an OTel Collector file exporter).
- Run 20 queries, then write a script that reads the exported spans and finds the slowest and the most token-expensive request, plus the span where a deliberately injected bad retrieval occurred.
- Toggle the content-capture env var and compare what the trace contains.

## Mastery check
1. Which GenAI attributes are Opt-In and why? What is the default capture mode?
2. Given a trace of a wrong RAG answer, which spans do you inspect to decide retrieval vs generation failure?
3. How do you keep traces useful for eval while meeting privacy constraints? (Cross-ref traffic-sampling-and-logging.)

## Sources
- [OTel GenAI spans spec (repo)](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)
- [OTel GenAI moved notice](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [Sculley et al. 2015](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)
