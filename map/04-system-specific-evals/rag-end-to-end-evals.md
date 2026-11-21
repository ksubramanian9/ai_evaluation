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

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Supplemented 2026-11-21: [research/supplements/2026-11-21-rag-end-to-end-evals.md](../../research/supplements/2026-11-21-rag-end-to-end-evals.md). The survey, CRAG, RGB and RAGChecker were read in full text; RAGAS and ARES at abstract only. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Attribute RAG failures to retrieval miss, ranking, unfaithful generation, irrelevant generation or data gap in an attribution table.
- Use gold-context injection to bound generator error separately from retrieval error.
- Explain why hallucination rate should be reported separately from accuracy.
- Critique a RAG eval where component metrics and end-to-end results disagree, and design the tests that would locate the cause.

**Done bar.** Practiced: a confusion-style attribution table over the shared 50-question set, plus one gold-context injection run with the bounded generator error written down. Mastered: written answers to all three mastery questions checked against CRAG, RAGChecker and the RAG evaluation survey, plus a critique of a real RAG system's eval that traces a component/end-to-end disagreement to its cause and states the trade-off of the fix you propose.

## Why it matters
- The survey separates retrieval targets (relevance, ranking accuracy) from generation targets (relevance, faithfulness to documents, correctness) but warns that "the entire system's performance cannot be fully understood by evaluating each component in isolation" ([Yu et al., sec. 2-3](https://arxiv.org/abs/2405.07437)).
- It names attribution as open: with strong LLMs it "becomes challenging to distinguish the impact of retrieval components", and it calls for work linking retrieval metrics to final outputs ([Yu et al., sec. 4](https://arxiv.org/abs/2405.07437)).
- RAGChecker attributes errors at claim level: claim recall says whether retrieved chunks contained the answer; hallucination, noise sensitivity and context utilization say what the generator did with them ([RAGChecker](https://arxiv.org/abs/2408.08067)).
- Component judges exist too: RAGAS scores context relevance, faithfulness and answer quality without references ([RAGAS, abstract](https://arxiv.org/abs/2309.15217)); ARES trains per-component judges and corrects them with a few hundred human labels ([ARES, abstract](https://arxiv.org/abs/2311.09476)).
- CRAG (2024): GPT-4 Turbo alone reached 33.5% accuracy and the best straightforward RAG 43.6%, yet no straightforward RAG passed 20% truthfulness because retrieval noise induced hallucinations ([CRAG](https://arxiv.org/abs/2406.04744)).

## Common failure modes
- Good retrieval, bad answers: RAGChecker found that "as retriever claim recall increases, all generators become more sensitive to such noise", and larger top-k or chunk size raised both recall and noise sensitivity ([RAGChecker](https://arxiv.org/abs/2408.08067)).
- Generator ignores or is misled by context: in RGB, ChatGPT's accuracy fell from 96% to 76% as the noise ratio rose to 0.8, and it scored 9% with counterfactual documents against 89% without (2023) ([RGB](https://arxiv.org/abs/2309.01431)).
- No answer in the context: RGB's negative-rejection testbed (only non-answering documents) showed ChatGPT declining in only 24.67% of English cases by exact match (45% when judged by ChatGPT) (2023) ([RGB](https://arxiv.org/abs/2309.01431)).
- Collapsing hallucination into accuracy: CRAG scores perfect 1, acceptable 0.5, missing 0, incorrect -1, preferring "missing answers to incorrect ones"; truthfulness equals accuracy minus hallucination ([CRAG](https://arxiv.org/abs/2406.04744)).
- Static benchmarks miss time-varying facts; CRAG reports lower accuracy on dynamic facts and tail entities ([CRAG](https://arxiv.org/abs/2406.04744)).
- Gold-context injection is a proposed design here, modelled on RGB's controlled positive/negative documents; no source names it as a standard procedure.

## Practice exercise (3 h)
On the same 50-question set as the retrieval and generation exercises, label each failure as retrieval miss / ranking / generation unfaithful / generation irrelevant / data gap. Compute claim recall and faithfulness per question in the RAGChecker style. Produce a confusion-style attribution table and one oracle run (inject gold context) to bound generator error. Score answers CRAG-style so abstentions and hallucinations are separate.

## Mastery check
1. Given recall@5=0.9 and answer accuracy=0.6, list candidate causes and tests.
2. What does gold-context injection tell you, and what does it not?
3. Why report hallucination rate separately from accuracy?

## Sources
- [Yu et al., Evaluation of Retrieval-Augmented Generation: A Survey, arXiv 2405.07437](https://arxiv.org/abs/2405.07437)
- [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation, arXiv 2408.08067](https://arxiv.org/abs/2408.08067)
- [CRAG, arXiv 2406.04744](https://arxiv.org/abs/2406.04744)
- [RGB, arXiv 2309.01431](https://arxiv.org/abs/2309.01431)
- [RAGAS, arXiv 2309.15217](https://arxiv.org/abs/2309.15217)
- [ARES, arXiv 2311.09476](https://arxiv.org/abs/2311.09476)
