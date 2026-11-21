---
id: metric-selection
title: "Metric selection"
branch: 02-eval-design
depth: L2
status: not-started
bridge: stats
prerequisites: [quality-dimensions-taxonomy, ml-metrics]
tags: [statistics, llm-judge]
---
# Metric selection

Choosing metrics that match the dimension and decision being made.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Choose metrics for an extraction task, a RAG answer and an agent task, and justify each.
- Measure each candidate metric's rank correlation with human labels.
- Show how a discontinuous metric can hide or manufacture progress.
- Compute pass@k and pass^k and pick the one that matches the requirement.

**Done bar.** Practiced: ROUGE-L, embedding-cosine and LLM-judge scores on 100 summaries, rank correlations against 30 hand labels, and a note on which metric you would use for which decision. Mastered: written answers to all three mastery-check questions, checked against Schaeffer et al., Anthropic, OpenAI and Zheng et al., plus a metric choice for a real system or the capstone with its agreement with human labels recorded.

## Why it matters
- Metric choice can manufacture conclusions: apparent "emergent abilities" can arise from nonlinear/discontinuous metrics and vanish with continuous ones ([Schaeffer et al.](https://arxiv.org/abs/2304.15004)).
- Anthropic maps task to grader: exact match (classification), embedding cosine similarity (consistency), ROUGE-L (summarization), LLM Likert/binary graders (tone, PHI detection); recommends a different model as grader than generator ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- OpenAI warns against relying only on generic academic metrics and notes judge position/verbosity bias ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- Judge agreement: GPT-4 >80% with humans on MT-bench, with position, verbosity, self-enhancement bias ([Zheng et al.](https://arxiv.org/abs/2306.05685)).
- For agents: pass@k vs pass^k (75% per-trial -> ~42% pass^3) ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).

## Common failure modes
- Metric/construct mismatch (ROUGE for faithfulness; UNVERIFIED as cited claim).
- Discontinuous metrics hiding progress ([Schaeffer](https://arxiv.org/abs/2304.15004)).
- Judge biases ([Zheng](https://arxiv.org/abs/2306.05685)).
- Using pass@k when consistency matters ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Imbalanced classes with accuracy (see baselines node).

## Practice exercise (2-3 h)
Take 100 summaries (any public summarization set). Score with ROUGE-L, embedding cosine, and an LLM judge using a 3-point rubric; hand-label 30; compute rank correlation of each metric with your labels. Report which metric you would use for which decision.

## Mastery check
1. Pick metrics for 3 tasks (extraction, RAG answer, agent task) and justify.
2. Show how swapping exact-match for per-token accuracy changes a scaling curve.
3. Compute pass@3 vs pass^3 for p=0.8.

## Sources
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Schaeffer et al., Are Emergent Abilities a Mirage?](https://arxiv.org/abs/2304.15004)
- [Zheng et al., MT-Bench / LLM-as-a-judge](https://arxiv.org/abs/2306.05685)
- [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
- [HELM](https://arxiv.org/abs/2211.09110)
- Prereq `ml-metrics` is in another branch (not checked).
