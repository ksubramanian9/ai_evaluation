---
id: quality-dimensions-taxonomy
title: "Quality dimensions taxonomy"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [task-definition-and-success-criteria]
tags: [fairness, privacy, cost]
---
# Quality dimensions taxonomy

Correctness, faithfulness, helpfulness, safety, tone, and latency as separate dimensions to measure.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Build a dimension x scenario matrix for an app and compute its coverage percentage.
- Select the relevant dimensions and justify the ones marked not relevant.
- Separate retrieval quality from generation faithfulness when evaluating RAG.
- Identify dimensions that trade off and dimensions that need no model or human judge.

**Done bar.** Practiced: a filled dimension x scenario matrix with a justification per cell and your HELM-style coverage %. Mastered: written answers to all three mastery-check questions, checked against HELM, Anthropic and RAGAs, plus the matrix applied to a real system or the capstone with the gaps it exposed recorded.

## Why it matters
- HELM maps use cases (scenarios) and desiderata (metrics) and measures seven metric categories: accuracy, calibration, robustness, fairness, bias, toxicity, efficiency; 30 models x 42 scenarios, coverage of core scenarios raised from 17.9% to 96.0% ([HELM](https://arxiv.org/abs/2211.09110)).
- Anthropic lists example dimensions: task fidelity, consistency, relevance/coherence, tone/style, privacy, context utilization, latency, price ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- RAG-specific separation: faithfulness, answer relevance, context relevance ([RAGAs](https://arxiv.org/abs/2309.15217)).
- Healthcare example of behavioral dimensions: accuracy, instruction following, communication ([HealthBench](https://arxiv.org/abs/2505.08775)).

## Common failure modes
- Single aggregate score hiding trade-offs (HELM's motivation: broad multi-metric measurement, not accuracy alone) ([HELM](https://arxiv.org/abs/2211.09110)).
- Conflating retrieval quality with generation faithfulness in RAG ([RAGAs](https://arxiv.org/abs/2309.15217)).
- Applying an irrelevant dimension (citation accuracy matters in medical, less in casual chat) ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).

## Practice exercise (2 h)
For one app, build a dimension x scenario matrix (rows: dimensions from HELM/Anthropic lists; columns: 3-5 scenarios). Mark each cell: measured / not measured / not relevant, with justification. Compute your own "coverage %" like HELM.

## Mastery check
1. Name two dimensions that trade off and show a pair of outputs illustrating it.
2. For RAG, which dimension fails if retrieval is poor but the answer is fluent?
3. Which dimensions need no model/human judge?

## Sources
- [HELM](https://arxiv.org/abs/2211.09110)
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [RAGAs, Es et al.](https://arxiv.org/abs/2309.15217)
- [HealthBench, Arora et al.](https://arxiv.org/abs/2505.08775)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): RMF 1.0 released 2023-01-26, GenAI Profile NIST-AI-600-1 released 2024-07-26 (the page does not list trustworthiness characteristics; the list itself is UNVERIFIED here; page notes RMF is being revised, as-of 2026-11-20)
