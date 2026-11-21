---
id: eval-maturity-model
title: "Eval maturity model"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [team-roles-and-process, model-and-system-documentation, eval-tooling-landscape]
tags: [human-labels, llm-judge]
---
# Eval maturity model

Stages of organizational evaluation capability and how to progress.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Build a 4-5 level maturity rubric across dimensions (datasets, metric validity, judge calibration, CI gates, monitoring, ownership, documentation, reporting with uncertainty), each level anchored to a verifiable artifact.
- Apply the rubric to score a real system and name the next-level step with the highest risk reduction.
- Explain why the rubric is a synthesis rather than an established model, and adjust required levels per risk tier rather than treating them as universal.

**Done bar.** Practiced: a written maturity rubric with each level tied to an artifact and a cited source, plus a scored capstone and its chosen next step. Mastered: written answers to all three mastery questions checked against Google Cloud MLOps levels and NIST AI 100-1, and the rubric applied to a second (real-work) system with the score and next step recorded.

## Why it matters
- No authoritative, widely adopted "LLM eval maturity model" was found in primary sources (UNVERIFIED that none exists; limited search). Treat this node as a synthesized model, labeled as such.
- Adjacent primary-ish anchors for staging: Google Cloud MLOps levels 0 (manual, notebooks, no CI/CD, rare monitoring), 1 (pipeline automation, automated data/model validation, triggers incl. drift), 2 (CI/CD around pipelines, automated tests, staged rollouts) ([Google Cloud architecture doc](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning); undated on page). Practitioner staging: unit-test evals, human+model eval, A/B testing ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).
- Regulatory/standards evidence for what a "mature" org shows: documented TEVV and metric effectiveness review (MEASURE 2.1, 2.13), monitoring plans (MANAGE 4.1), roles (GOVERN 2.1) ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)); management-system continual improvement (ISO/IEC 42001 scope, [ISO](https://committee.iso.org/standard/42001)).
- Benchmark/eval quality evidence: BetterBench 46 practices; construct-validity checklist ([arXiv 2411.12990](https://arxiv.org/abs/2411.12990); [arXiv 2511.04703](https://arxiv.org/abs/2511.04703)). These can serve as top-level criteria.

## Common failure modes
- Skipping levels (LLM judge dashboards without any human-labelled gold set).
- Maturity measured by tool count rather than decision quality.
- Treating maturity levels as universal rather than per risk tier (inference).
- Stuck at "vibe checks" (practitioner: Husain).

## Practice exercise (3 h)
Draft a 4-5 level rubric along dimensions (datasets, metrics validity, judge calibration, automation/CI gates, monitoring, ownership, documentation, reporting with uncertainty). Anchor each level to a verifiable artifact and a cited source above. Score your capstone and name the next-level step with highest risk reduction.

## Mastery check
1. For one dimension, define observable evidence that separates level 2 from level 3.
2. How would you validate that the maturity rubric itself predicts better release decisions?
3. Which levels are mandatory for a high-risk EU use case versus a prototype?

## Sources
- [Google Cloud, MLOps continuous delivery and automation pipelines](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)
- [ISO/IEC 42001](https://committee.iso.org/standard/42001)
- [BetterBench, arXiv 2411.12990](https://arxiv.org/abs/2411.12990)
- [Construct validity review, arXiv 2511.04703](https://arxiv.org/abs/2511.04703)
- practitioner: [Hamel Husain, evals](https://hamel.dev/blog/posts/evals/)
