---
id: rag-end-to-end-evals
title: "RAG end-to-end evaluation"
branch: 04-system-specific-evals
depth: L3
status: not-started
bridge: none
prerequisites: [rag-retrieval-evals, rag-generation-evals]
tags: []
---
# RAG end-to-end evaluation

Attributing failures to retrieval vs. generation and evaluating the whole pipeline.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
RAG's "hybrid structure and reliance on dynamic knowledge sources" makes evaluation hard; the survey proposes a unified process (Auepora) to organize targets and benchmarks ([arXiv 2405.07437](https://arxiv.org/abs/2405.07437)). CRAG (4,409 QA pairs, mock web/KG APIs, 5 domains) reports straightforward RAG lifts accuracy only 34% to 44%, industry systems answer 63% without hallucination, and accuracy falls for dynamic facts, tail entities, complex queries ([arXiv 2406.04744](https://arxiv.org/abs/2406.04744)).

## Common failure modes
- Component metrics look fine, end-to-end poor (or the reverse); can't attribute (UNVERIFIED as stated; the attribution framing is from the node description).
- Static benchmarks miss time-varying facts (CRAG above).
- Hallucination vs "missing" scoring: CRAG reports accuracy and hallucination rates separately (abstract); grading details UNVERIFIED (repo github.com/facebookresearch/CRAG not read).

## Practice exercise
On the same 50-question set as the retrieval and generation exercises, label each failure as retrieval miss / ranking / generation unfaithful / generation irrelevant / data gap; produce a confusion-style attribution table and one oracle experiment (inject gold context) to bound generator error.

## Mastery check
(1) Given recall@5=0.9 and answer accuracy=0.6, list candidate causes and tests. (2) What does gold-context injection tell you? (3) Why report hallucination rate separately from accuracy?

## Sources
Yu et al. survey; CRAG; RGB.
