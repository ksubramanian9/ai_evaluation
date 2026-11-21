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
| `study-plan.md` | Generated week-by-week study plan (exercise hours + reading allowance by depth; skips mastered nodes) |
| `tools/build_site.py` | Builds the browsable website into `site/` (gitignored); assets in `tools/site/` |
| `tools/build_views.py` | Validates nodes, regenerates overview and progress, flags stale landscape entries |
| `research/` | Sourced notes the nodes were written from |
| `docs/practitioner-sources.md` | Curated list of practitioner sources cited by nodes |
| `docs/audits/` | Content audits of the map |
| `CONTEXT.md` | Domain glossary and project context |

## Node frontmatter

```yaml
id: slug            # matches filename
title: "..."
branch: 01-foundations
depth: L1           # target depth for you: L1 explain, L2 apply, L3 design and critique (not difficulty)
status: not-started # not-started | learning | practiced | mastered
bridge: stats       # stats = ML/statistics gap, testing = test-engineering gap, none
prerequisites: [other-node-id]
tags: [nondeterminism] # cross-cutting, from the vocabulary below
```

Tags come from a controlled vocabulary (0-3 per node; leave a node untagged when no tag fits, as with `multimodal-evals`): `nondeterminism`, `statistics`, `human-labels`, `llm-judge`, `rag`, `agents`, `safety`, `security`, `fairness`, `privacy`, `cost`. The validator rejects anything else.

Nodes are filled from sourced research (`research/`); fill remaining gaps as you study a node and update its `status`. Every node body uses the same layout:

```
# Title
One-line description
_Provenance banner_
**Shared concept:** / **Owns:** line (optional; names the owner node)
## Learning objectives    (2-4 abilities matched to depth, then a **Done bar.** for practiced and mastered)
## Why it matters          (bullets, each claim with an inline link)
## Common failure modes    (bullets)
## Practice exercise (N h) (prose or numbered steps, realistic estimate)
## Mastery check           (numbered questions)
## Sources                 (clickable links; prefix "practitioner:" for practitioner sources)
```

`build_views.py` fails on a mismatched id, bad depth/bridge/tag, or a missing required heading.

## Landscape format

One entry per line in `landscape/<branch>.md`:

```
- <item> (type: tool|benchmark|model|standard|regulation|docs) as-of: YYYY-MM-DD | <url>
```

Use `URL not recorded` when no URL is known. Entries missing a type or URL produce `WARN:` lines (non-fatal); entries older than `--stale-days` produce `STALE:` lines.

## Rules

- Durable concepts go in nodes. Volatile items go in `landscape/` with `as-of: YYYY-MM-DD`.
- Every factual claim links to a source: primary sources first, plus a short list of trusted practitioner sources (see [docs/practitioner-sources.md](docs/practitioner-sources.md)); practitioner sources are tagged as such and never stand alone as evidence.
- Keep each branch to about 10–15 nodes; overflow goes in `_candidates.md`.

## Commands

```
pip install -r requirements.txt
python tools/build_site.py               # build site/, open site/index.html (works from file://)
python tools/build_views.py              # regenerate views, validate, list stale landscape entries
python tools/build_views.py --stale-days 60
python tools/build_views.py --hours-per-week 8   # regenerate study-plan.md at a different weekly budget (default 6)
```

CI (`.github/workflows/validate.yml`) runs both builds on every push and pull request; `pages.yml` publishes the site from `main`.
