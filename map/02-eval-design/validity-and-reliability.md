---
id: validity-and-reliability
title: "Validity and reliability"
branch: 02-eval-design
depth: L3
status: not-started
bridge: stats
prerequisites: [metric-selection, statistical-inference]
tags: []
---
# Validity and reliability

Whether an eval measures what it claims (construct validity) and gives stable results.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

**Shared concept:** confidence intervals, power and paired comparisons are owned by [statistical-inference](../01-foundations/statistical-inference.md) and [confidence-intervals-for-evals](../03-measurement-methods/confidence-intervals-for-evals.md).

## Why it matters
445 LLM benchmarks reviewed by 29 experts show recurring patterns weakening construct validity; eight recommendations [Bean et al., NeurIPS 2025 D&B](https://arxiv.org/abs/2511.04703). Benchmarks should be reliable, unbiased, with headroom [Bowman & Dahl](https://arxiv.org/abs/2104.02145). General benchmarks framed as measures of "general" progress have construct validity problems [Raji et al.](https://arxiv.org/abs/2111.15366). Measurement-modeling vocabulary: construct validity/reliability [Jacobs & Wallach](https://arxiv.org/abs/1912.05511). Stability: "evaluations are experiments"; formulas for analysis, model comparison, power planning [Miller](https://arxiv.org/abs/2411.00640) (abstract only).
## Common failure modes
Construct mismatch [Bean](https://arxiv.org/abs/2511.04703); sampling noise treated as signal [Miller](https://arxiv.org/abs/2411.00640); judge bias [Zheng](https://arxiv.org/abs/2306.05685); metric artifacts [Schaeffer](https://arxiv.org/abs/2304.15004); contamination [Sainz](https://arxiv.org/abs/2310.18018).
## Practice exercise
Run your eval 5x at temperature>0 and with 3 prompt paraphrases; compute SE/bootstrap CI and paired difference between two prompt versions; state minimum detectable effect for your n. Separately, list the construct and 3 threats to validity.
## Mastery check
(1) Distinguish construct validity from reliability with an example from your eval. (2) Is a 2-point gain on 200 items real? (3) Apply one Bean et al. recommendation to a benchmark you use (read the paper).
## Sources
https://arxiv.org/abs/2511.04703; https://arxiv.org/abs/2104.02145; https://arxiv.org/abs/2111.15366; https://arxiv.org/abs/1912.05511; https://arxiv.org/abs/2411.00640.
