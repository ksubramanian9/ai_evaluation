---
id: rag-end-to-end-evals
title: "RAG end-to-end evaluation"
branch: 04-system-specific-evals
depth: L3
status: not-started
bridge: none
prerequisites: [rag-retrieval-evals, rag-generation-evals]
tags: [rag]
---
# RAG end-to-end evaluation

Attributing failures to retrieval vs. generation and evaluating the whole pipeline.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Attribute RAG failures to retrieval miss, ranking, unfaithful generation, irrelevant generation or data gap in an attribution table.
- Use gold-context injection to bound generator error separately from retrieval error.
- Explain why hallucination rate should be reported separately from accuracy.
- Critique a RAG eval where component metrics and end-to-end results disagree, and design the tests that would locate the cause.

**Done bar.** Practiced: a confusion-style attribution table over the shared 50-question set, plus one gold-context injection run with the bounded generator error written down. Mastered: written answers to all three mastery questions checked against CRAG and the RAG evaluation survey, plus a critique of a real RAG system's eval that traces a component/end-to-end disagreement to its cause and states the trade-off of the fix you propose.

## Why it matters
- RAG's "hybrid structure and reliance on dynamic knowledge sources" makes evaluation hard; the survey proposes a unified process (Auepora) to organize targets and benchmarks ([arXiv 2405.07437](https://arxiv.org/abs/2405.07437)).
- CRAG (4,409 QA pairs, mock web/KG APIs, 5 domains) reports straightforward RAG lifts accuracy only 34% to 44%, industry systems answer 63% without hallucination, and accuracy falls for dynamic facts, tail entities, complex queries ([arXiv 2406.04744](https://arxiv.org/abs/2406.04744)).

## Common failure modes
- Component metrics look fine, end-to-end poor (or the reverse); can't attribute (UNVERIFIED as stated; the attribution framing is from the node description).
- Static benchmarks miss time-varying facts ([CRAG](https://arxiv.org/abs/2406.04744) above).
- Hallucination vs "missing" scoring: CRAG reports accuracy and hallucination rates separately (abstract); grading details UNVERIFIED (repo [github.com/facebookresearch/CRAG](https://github.com/facebookresearch/CRAG) not read).

## Practice exercise (3 h)
On the same 50-question set as the retrieval and generation exercises, label each failure as retrieval miss / ranking / generation unfaithful / generation irrelevant / data gap; produce a confusion-style attribution table and one oracle experiment (inject gold context) to bound generator error.

## Mastery check
1. Given recall@5=0.9 and answer accuracy=0.6, list candidate causes and tests.
2. What does gold-context injection tell you?
3. Why report hallucination rate separately from accuracy?

## Sources
- [Yu et al., RAG evaluation survey, arXiv 2405.07437](https://arxiv.org/abs/2405.07437)
- [CRAG, arXiv 2406.04744](https://arxiv.org/abs/2406.04744)
- [RGB, arXiv 2309.01431](https://arxiv.org/abs/2309.01431)
