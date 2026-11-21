---
id: baselines-and-thresholds
title: "Baselines and thresholds"
branch: 02-eval-design
depth: L2
status: not-started
bridge: testing
prerequisites: [metric-selection, statistical-inference]
tags: [statistics]
---
# Baselines and thresholds

Setting what "good enough" means with baselines, human performance, and acceptance thresholds.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** confidence intervals, power and paired comparisons are owned by [statistical-inference](../01-foundations/statistical-inference.md) and [confidence-intervals-for-evals](../03-measurement-methods/confidence-intervals-for-evals.md).

## Learning objectives
You can:
- Compute trivial baselines (majority, stratified, keyword rule) and human-vs-human agreement for a golden set.
- Set an acceptance threshold justified by baselines, CI, n and business cost.
- Implement the threshold as a gate script that fails below it.
- Explain why human agreement caps the achievable score.

**Done bar.** Practiced: a baseline table, the prompt v1 score with its CI, a written threshold justification, and a gate script that exits non-zero below the threshold. Mastered: written answers to all three mastery-check questions, checked against the DummyClassifier docs, Anthropic, Bowman & Dahl and Miller, plus a threshold set for a real system or the capstone with the gate result recorded.

## Why it matters
- Trivial baselines show whether a model learns anything: scikit-learn DummyClassifier (most_frequent, prior, stratified, uniform, constant) is "a simple baseline to compare against" ([scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)).
- Thresholds should be achievable, based on industry benchmarks, prior experiments, research, or expert knowledge; example: <0.1% toxic of 10,000 trials ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Human agreement bounds achievable score (my inference from [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Headroom matters ([Bowman & Dahl](https://arxiv.org/abs/2104.02145)).
- ML Test Score gives 28 production-readiness tests ([Breck et al.](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)); baseline-test details UNVERIFIED.

## Common failure modes
- Accuracy near majority-class rate looks good (follows from DummyClassifier docs; no direct source).
- Unrealistic targets ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Thresholds without uncertainty (see [Miller](https://arxiv.org/abs/2411.00640)).
- Ceilings capped by annotator disagreement.

## Practice exercise (2-3 h)
For a classification golden set: compute majority, stratified, and keyword-rule baselines, and human-vs-human agreement; then compare LLM prompt v1 with CIs; set a threshold justified by baseline + business cost and write it in a gate script (exit non-zero below it).

## Mastery check
1. Choose a threshold for a safety metric and justify with CI and n.
2. What baselines for a RAG QA system?
3. Why is human agreement a ceiling?

## Sources
- [scikit-learn, DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Bowman & Dahl, What Will it Take to Fix Benchmarking in NLU?](https://arxiv.org/abs/2104.02145)
- [Breck et al., The ML Test Score](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)
- [Miller, Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640)
