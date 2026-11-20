---
id: rag-retrieval-evals
title: "RAG retrieval evaluation"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: stats
prerequisites: [metric-selection]
tags: []
---
# RAG retrieval evaluation

Recall@k, MRR, nDCG, and context relevance for the retrieval step.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Retrieval is a separable component; RAG evaluation surveys treat retrieval (relevance) and generation (accuracy, faithfulness) as distinct evaluation targets ([Yu et al. survey, arXiv 2405.07437](https://arxiv.org/abs/2405.07437)). nDCG extends precision/recall to graded relevance and applies a rank discount so later results count less ([Järvelin & Kekäläinen, ACM TOIS 20(4) 2002, DOI 10.1145/582415.582418](https://dl.acm.org/doi/10.1145/582415.582418); abstract confirmed via search summary, page itself returned 403). Zero-shot behaviour varies by domain: BEIR (18 datasets, 10 systems) found BM25 a robust baseline, with re-ranking/late-interaction best on average but costly, and dense/sparse often underperforming ([BEIR, NeurIPS 2021 D&B](https://arxiv.org/abs/2104.08663)).

## Common failure modes
- Optimizing on one in-domain set; BM25 baseline unexpectedly strong out of domain (BEIR above).
- Incomplete relevance labels penalize correct unjudged hits (UNVERIFIED; textbook chapter fetch failed: nlp.stanford.edu/IR-book).
- Ignoring graded relevance when using binary recall@k (motivation for nDCG, Järvelin & Kekäläinen above).
- Measuring retrieval only, missing that the generator ignores context (see rag-end-to-end-evals).

## Practice exercise
Take ~100 questions over a small corpus (e.g. a BEIR subset such as SciFact via the BEIR repo, [arXiv 2104.08663](https://arxiv.org/abs/2104.08663)). Implement recall@k, MRR, nDCG@k by hand, compare BM25 vs one embedding model, and use sentence-transformers' `InformationRetrievalEvaluator` as a cross-check; it reports MRR, NDCG, MAP, accuracy@k, precision/recall@k ([Sentence-Transformers docs, as of 2026-11-20 [V]](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html)). Bootstrap a CI on the difference.

## Mastery check
(1) When do MRR and nDCG rank two systems differently? Construct an example. (2) Why can recall@k be high yet answers wrong? (3) Compute nDCG@5 by hand for a graded list. (4) How would unjudged documents bias your comparison?

## Sources
BEIR; Järvelin & Kekäläinen 2002; Yu et al. 2405.07437; Sentence-Transformers docs (practitioner/library docs).
