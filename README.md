# AI Evaluation and Testing: Meta-Learning Map

A personal curriculum, taxonomy, and decision guide for evaluating and testing AI systems. Core scope is LLM/GenAI applications (prompts, RAG, agents). Classical ML evaluation is a foundations branch. Vision, speech, and multimodal are extension nodes only.

Evaluation (statistical quality measurement) and testing (pass/fail engineering checks) are treated as one lifecycle: design, measure, gate, monitor, feed back.

## Layout

| Path | Purpose |
|---|---|
| `map/01…07-*/` | One Markdown file per node, seven branches |
| `map/*/_candidates.md` | Topics that might become nodes; not part of the map yet |
| `map/00-overview.md` | Generated Mermaid diagrams and tables |
| `landscape/` | Volatile items (tools, benchmarks, model names), each with `as-of:` date |
| `capstone/` | End-to-end project: RAG app, then tool-using agent |
| `progress.md` | Generated status table |
| `tools/build_views.py` | Validates nodes, regenerates overview and progress, flags stale landscape entries |

## Node frontmatter

```yaml
id: slug            # matches filename
title: "..."
branch: 01-foundations
depth: L1           # L1 awareness, L2 working, L3 expert
status: not-started # not-started | learning | practiced | mastered
bridge: stats       # stats = ML/statistics gap, testing = test-engineering gap, none
prerequisites: [other-node-id]
tags: [nondeterminism] # cross-cutting: nondeterminism, fairness, safety, cost
```

Nodes start as stubs. When you study one, fill in: why it matters, failure modes, practice exercise, mastery check, primary sources (tag practitioner sources as such).

## Rules

- Durable concepts go in nodes. Volatile items go in `landscape/` with `as-of: YYYY-MM-DD`.
- Every factual claim links to a source: primary sources first, plus a short list of trusted practitioner sources.
- Keep each branch to about 10–15 nodes; overflow goes in `_candidates.md`.

## Commands

```
python tools/build_views.py              # regenerate views, validate, list stale landscape entries
python tools/build_views.py --stale-days 60
```
