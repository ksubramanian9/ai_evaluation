---
id: rag-generation-evals
title: "RAG generation evaluation"
branch: 04-system-specific-evals
depth: L3
status: not-started
bridge: none
prerequisites: [llm-as-judge]
tags: [rag, llm-judge, human-labels]
---
# RAG generation evaluation

Faithfulness/groundedness and answer relevance given retrieved context.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** this node owns faithfulness/groundedness measurement. [summarization-and-extraction-evals](summarization-and-extraction-evals.md) reuses it.

## Learning objectives
You can:
- Distinguish faithfulness from answer relevance with an example each way, and explain why a faithful answer can still be wrong.
- Build a claim-decomposition faithfulness judge and measure its agreement with hand labels using Cohen's kappa.
- Explain how prediction-powered inference uses a small set of human labels to correct judge error.
- Design negative-rejection and counterfactual-context test cases and choose between reference-free metrics given their trade-offs.

**Done bar.** Practiced: 30 (question, context, answer) triples with 10 ungrounded and 10 irrelevant-context cases, a claim-decomposition judge, hand labels, Cohen's kappa, and a comparison with a RAGAS faithfulness run. Mastered: written answers to all four mastery questions checked against RAGAS, ARES, FActScore and RGB, plus a faithfulness eval you designed or reviewed for a real system that makes an explicit trade-off (for example judge cost versus human-label correction) and names a flaw this node covers.

## Why it matters
- Faithfulness/groundedness and answer relevance can be scored without gold answers: RAGAS is a "reference-free" framework covering retrieval relevance, faithfulness to context, and generation quality ([arXiv 2309.15217](https://arxiv.org/abs/2309.15217)).
- ARES trains lightweight judges on synthetic data to score context relevance, answer faithfulness, answer relevance, and uses prediction-powered inference with a few hundred human annotations to correct judge error (NAACL 2024, [arXiv 2311.09476](https://arxiv.org/abs/2311.09476)).
- FActScore splits text into atomic facts and measures the share supported by a knowledge source; ChatGPT scored ~58% on biographies; automated estimator error <2% (EMNLP 2023, [arXiv 2305.14251](https://arxiv.org/abs/2305.14251)).
- The "RAG triad" (context relevance, groundedness via claim decomposition, answer relevance) is a practitioner framing ([TruLens docs](https://www.trulens.org/getting_started/core_concepts/rag_triad/), practitioner/library).

## Common failure modes
- Model answers from parametric memory, correct but ungrounded (UNVERIFIED as a named failure; inferable from groundedness definition above).
- Models fail to reject when context lacks the answer, and are misled by counterfactual or noisy documents ([RGB, arXiv 2309.01431](https://arxiv.org/abs/2309.01431): noise robustness, negative rejection, information integration, counterfactual robustness; models struggled with the latter three).
- Judge error uncorrected: ARES motivates PPI for this reason (above).
- Metric tool lists change names/definitions: RAGAS currently lists Context Precision, Context Recall, Faithfulness, Response Relevancy, Noise Sensitivity (as of release; volatile) ([docs, as of 2026-11-20](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)).

## Practice exercise (4 h)
Build 30 (question, context, answer) triples, 10 deliberately ungrounded, 10 with irrelevant context. Implement a claim-decomposition faithfulness judge (FActScore-style) with any LLM, hand-label, report agreement (Cohen's kappa) and compare to a RAGAS faithfulness run.

## Mastery check
1. Distinguish faithfulness from answer relevance with one example each way.
2. Why can a faithful answer be wrong?
3. How does PPI use human labels?
4. Design a negative-rejection test case.

## Sources
- [RAGAS, arXiv 2309.15217](https://arxiv.org/abs/2309.15217)
- [ARES, arXiv 2311.09476](https://arxiv.org/abs/2311.09476)
- [FActScore, arXiv 2305.14251](https://arxiv.org/abs/2305.14251)
- [RGB, arXiv 2309.01431](https://arxiv.org/abs/2309.01431)
- practitioner: [TruLens RAG triad](https://www.trulens.org/getting_started/core_concepts/rag_triad/)
- [RAGAS docs, available metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
