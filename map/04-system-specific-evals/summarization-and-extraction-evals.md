---
id: summarization-and-extraction-evals
title: "Summarization and extraction evals"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: none
prerequisites: [reference-based-metrics, llm-as-judge, rag-generation-evals]
tags: [llm-judge, human-labels]
---
# Summarization and extraction evals

Faithfulness, coverage, and field-level accuracy for summarization and structured extraction.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** faithfulness measurement (claim decomposition, groundedness judges) is covered in [rag-generation-evals](rag-generation-evals.md). This node covers what is specific to summarization (coverage, omissions) and to extraction (schema vs value correctness).

## Learning objectives
You can:
- Compute per-field exact and normalized match, list-field precision/recall, and null handling for structured extraction.
- Compare ROUGE with an entailment or claim-check faithfulness score against human labels for summaries.
- Distinguish schema validity from value correctness, and per-field from record-level accuracy.
- Apply a coverage (omission) check alongside faithfulness and handle refusals or truncated outputs in the pipeline.

**Done bar.** Practiced: per-field and list-field metrics for 30 invoices or emails, plus ROUGE, a faithfulness score and human faithfulness and coverage labels for 20 summaries, with the correlations reported. Mastered: written answers to all four mastery questions checked against Maynez et al., FRANK, G-Eval and the Structured Outputs guide, plus a summarization or extraction eval applied once in real work or the capstone with field-level and faithfulness results recorded.

## Why it matters
- Neural summarizers are "highly prone to hallucinate"; ROUGE is weaker than textual-entailment measures at tracking faithfulness (ACL 2020, [Maynez et al., arXiv 2005.00661](https://arxiv.org/abs/2005.00661)).
- SummEval re-evaluated 14 metrics on 23 models with expert and crowd judgments ([arXiv 2007.12626](https://arxiv.org/abs/2007.12626); findings UNVERIFIED).
- FRANK: typology of factual errors, benchmark for factuality metrics, factuality graded not binary (NAACL 2021, [arXiv 2104.13346](https://arxiv.org/abs/2104.13346)).
- G-Eval: CoT + form-filling GPT-4, Spearman 0.514 on summarization, with a flagged preference for LLM text ([arXiv 2303.16634](https://arxiv.org/abs/2303.16634)).
- Extraction: constrained decoding guarantees schema adherence not value correctness (as of release; volatile) ([OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)).
- JSONSchemaBench (10K real schemas) measures efficiency, coverage, quality ([arXiv 2501.10868](https://arxiv.org/abs/2501.10868)).

## Common failure modes
- Unsupported content in every tested model ([Maynez](https://arxiv.org/abs/2005.00661)).
- n-gram metrics missing faithfulness ([Maynez](https://arxiv.org/abs/2005.00661)).
- LLM judges favoring LLM text ([G-Eval](https://arxiv.org/abs/2303.16634)).
- Schema-valid wrong values, refusals and truncation breaking schema ([OpenAI docs](https://developers.openai.com/api/docs/guides/structured-outputs)).
- Coverage (omissions) not captured by faithfulness (UNVERIFIED as stated).

## Practice exercise (4 h)
30 invoices/emails with gold fields: extract JSON with schema, compute per-field exact/normalized match, precision/recall for list fields, and null-handling. For 20 summaries, compute ROUGE, an entailment/claim-check faithfulness score, and human faithfulness+coverage labels; report correlations.

## Mastery check
1. Why does ROUGE fail on faithfulness?
2. Per-field vs record-level accuracy.
3. Faithfulness vs coverage trade-off.
4. Handle refusals/incomplete responses in the pipeline.

## Sources
- [Maynez et al., arXiv 2005.00661](https://arxiv.org/abs/2005.00661)
- [SummEval, arXiv 2007.12626](https://arxiv.org/abs/2007.12626)
- [FRANK, arXiv 2104.13346](https://arxiv.org/abs/2104.13346)
- [G-Eval, arXiv 2303.16634](https://arxiv.org/abs/2303.16634)
- [JSONSchemaBench, arXiv 2501.10868](https://arxiv.org/abs/2501.10868)
- [OpenAI Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs)
