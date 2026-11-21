---
id: eval-tooling-landscape
title: "Eval tooling landscape"
branch: 07-operating-practice
depth: L1
status: not-started
bridge: none
prerequisites: [eval-harness-design]
tags: [agents, llm-judge]
---
# Eval tooling landscape

Categories of evaluation and observability tooling (specific tools live in landscape files).

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Categories (derived from docs read): (1) eval frameworks/harnesses with datasets, solvers, scorers, logs, agents, sandboxing, e.g. Inspect, developed by UK AI Security Institute and Meridian Labs ([Inspect](https://inspect.aisi.org.uk/)); (2) declarative eval + red-team CLIs, e.g. promptfoo (evals, red teaming, CI/CD) ([promptfoo](https://www.promptfoo.dev/docs/intro/)); (3) observability + evals + datasets + prompt management platforms, e.g. Langfuse (open source, tracing based on OpenTelemetry, LLM-as-judge, annotation queues, datasets) ([Langfuse](https://langfuse.com/docs)); (4) instrumentation standards: OpenTelemetry GenAI semantic conventions, now in a separate repo `semantic-conventions-genai` (Apache-2.0; spans, metrics, events; stability level not stated in README) ([OTel repo](https://github.com/open-telemetry/semantic-conventions-genai)); (5) cloud/provider-native eval features (not researched); (6) benchmark/leaderboard hubs (HF model-index) ([HF docs](https://huggingface.co/docs/hub/model-cards)).
- Practitioner advice: start with existing tools such as spreadsheets and custom data viewers before specialized products; avoid generic frameworks in place of problem-specific evals ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).

## Common failure modes
- Selecting a tool before defining the eval questions; letting tool metrics (built-in "faithfulness" etc.) define quality without validation (practitioner; Shankar for validation).
- Lock-in via proprietary trace/dataset formats (inference).
- Relying on experimental semantic conventions that may change (stability UNVERIFIED).
- Treating tool availability as maturity.

## Practice exercise (4 h)
Implement the same 20-item eval in two tools (e.g. Inspect and promptfoo). Record: setup time, how datasets and scorers are defined, log format/exportability, CI integration, judge configuration, cost visibility, and what a migration would require.

## Mastery check
1. Classify any tool you meet into the five categories and list what it does not do.
2. What would you need to export to leave a platform?
3. Which tool features replace human review, and which only organize it?

## Sources
- [Inspect](https://inspect.aisi.org.uk/)
- [promptfoo](https://www.promptfoo.dev/docs/intro/)
- [Langfuse](https://langfuse.com/docs)
- [OpenTelemetry GenAI semantic conventions repo](https://github.com/open-telemetry/semantic-conventions-genai)
- [Hugging Face model cards](https://huggingface.co/docs/hub/model-cards)
- practitioner: [Hamel Husain, evals](https://hamel.dev/blog/posts/evals/)
