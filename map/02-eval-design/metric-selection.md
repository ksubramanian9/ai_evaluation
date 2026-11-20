---
id: metric-selection
title: "Metric selection"
branch: 02-eval-design
depth: L2
status: not-started
bridge: stats
prerequisites: [quality-dimensions-taxonomy, ml-metrics]
tags: []
---
# Metric selection

Choosing metrics that match the dimension and decision being made.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

## Why it matters
Metric choice can manufacture conclusions: apparent "emergent abilities" can arise from nonlinear/discontinuous metrics and vanish with continuous ones [Schaeffer et al.](https://arxiv.org/abs/2304.15004). Anthropic maps task to grader: exact match (classification), embedding cosine similarity (consistency), ROUGE-L (summarization), LLM Likert/binary graders (tone, PHI detection); recommends a different model as grader than generator [CLAUDE-EVAL]. OpenAI warns against relying only on generic academic metrics and notes judge position/verbosity bias [OAI-BP]. Judge agreement: GPT-4 >80% with humans on MT-bench, with position, verbosity, self-enhancement bias [Zheng et al.](https://arxiv.org/abs/2306.05685). For agents: pass@k vs pass^k (75% per-trial -> ~42% pass^3) [ANTH-AGENT].
## Common failure modes
Metric/construct mismatch (ROUGE for faithfulness; UNVERIFIED as cited claim); discontinuous metrics hiding progress [Schaeffer](https://arxiv.org/abs/2304.15004); judge biases [Zheng](https://arxiv.org/abs/2306.05685); using pass@k when consistency matters [ANTH-AGENT]; imbalanced classes with accuracy (see baselines node).
## Practice exercise
Take 100 summaries (any public summarization set). Score with ROUGE-L, embedding cosine, and an LLM judge using a 3-point rubric; hand-label 30; compute rank correlation of each metric with your labels. Report which metric you would use for which decision.
## Mastery check
(1) Pick metrics for 3 tasks (extraction, RAG answer, agent task) and justify. (2) Show how swapping exact-match for per-token accuracy changes a scaling curve. (3) Compute pass@3 vs pass^3 for p=0.8.
## Sources
[CLAUDE-EVAL]; [OAI-BP]; https://arxiv.org/abs/2304.15004; https://arxiv.org/abs/2306.05685; [ANTH-AGENT]; [HELM]. Prereq `ml-metrics` is in another branch (not checked).
