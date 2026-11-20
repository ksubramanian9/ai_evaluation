---
id: quality-dimensions-taxonomy
title: "Quality dimensions taxonomy"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [task-definition-and-success-criteria]
tags: []
---
# Quality dimensions taxonomy

Correctness, faithfulness, helpfulness, safety, tone, and latency as separate dimensions to measure.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

## Why it matters
HELM maps use cases (scenarios) and desiderata (metrics) and measures seven metric categories: accuracy, calibration, robustness, fairness, bias, toxicity, efficiency; 30 models x 42 scenarios, coverage of core scenarios raised from 17.9% to 96.0% [HELM]. Anthropic lists example dimensions: task fidelity, consistency, relevance/coherence, tone/style, privacy, context utilization, latency, price [CLAUDE-EVAL]. RAG-specific separation: faithfulness, answer relevance, context relevance [RAGAs](https://arxiv.org/abs/2309.15217). Healthcare example of behavioral dimensions: accuracy, instruction following, communication [HealthBench](https://arxiv.org/abs/2505.08775).
## Common failure modes
Single aggregate score hiding trade-offs (HELM's motivation: broad multi-metric measurement, not accuracy alone) [HELM]; conflating retrieval quality with generation faithfulness in RAG [RAGAs](https://arxiv.org/abs/2309.15217); applying an irrelevant dimension (citation accuracy matters in medical, less in casual chat) [CLAUDE-EVAL].
## Practice exercise
For one app, build a dimension x scenario matrix (rows: dimensions from HELM/Anthropic lists; columns: 3-5 scenarios). Mark each cell: measured / not measured / not relevant, with justification. Compute your own "coverage %" like HELM.
## Mastery check
(1) Name two dimensions that trade off and show a pair of outputs illustrating it. (2) For RAG, which dimension fails if retrieval is poor but the answer is fluent? (3) Which dimensions need no model/human judge?
## Sources
[HELM]; [CLAUDE-EVAL]; https://arxiv.org/abs/2309.15217; https://arxiv.org/abs/2505.08775. NIST AI RMF 1.0 released 2023-01-26, GenAI Profile NIST-AI-600-1 released 2024-07-26 per https://www.nist.gov/itl/ai-risk-management-framework (the page does not list trustworthiness characteristics; the list itself is UNVERIFIED here; page notes RMF is being revised, as-of 2026-11-20).
