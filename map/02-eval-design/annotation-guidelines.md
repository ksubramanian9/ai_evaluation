---
id: annotation-guidelines
title: "Annotation guidelines"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [rubric-design]
tags: [human-labels]
---
# Annotation guidelines

Instructions and calibration processes that make human labels reliable.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Write an annotation guideline with definitions, decision rules and boundary examples.
- Compute Cohen's kappa for two annotators, using weighted kappa for ordinal labels.
- Adjudicate disagreements and revise the guideline to raise agreement.
- Explain why raw agreement can be high while kappa is low on imbalanced labels.

**Done bar.** Practiced: the one-page guideline, kappa on the first 50 items, adjudication notes, the revised guideline, and kappa on 50 fresh items showing the change. Mastered: written answers to all three mastery-check questions, checked against the sklearn kappa docs and the other sources, plus a guideline used for a real labeling task or the capstone with its kappa recorded.

## Why it matters
- Agreement coefficients (kappa-like) quantify label reliability: Artstein & Poesio survey inter-coder agreement for computational linguistics, Computational Linguistics 34(4), 2008 ([ACL Anthology](https://aclanthology.org/J08-4004/)); paper content not read, PDF not extractable.
- Cohen's kappa = (p_o - p_e)/(1 - p_e), range -1 to 1, weights option for ordinal ([scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)).
- Disagreement signals ambiguous tasks: "two domain experts reach same verdict" ([Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Human labels calibrate automated graders ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- People refine criteria while labeling ([Shankar](https://arxiv.org/abs/2404.12272)).

## Common failure modes
- Interpreting kappa with fixed bands (Landis & Koch bands are convention; primary source UNVERIFIED).
- Kappa undefined in degenerate cases ([scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)).
- Prevalence/bias effects on kappa and alpha vs kappa (UNVERIFIED).
- Annotator drift (UNVERIFIED).

## Practice exercise (3 h)
Draft a one-page guideline (definitions, decision rules, 3 positive + 3 boundary examples). Two annotators label 50 items; compute kappa (sklearn), adjudicate disagreements, revise guideline, relabel 50 fresh items, show kappa improvement.

## Mastery check
1. Why high raw agreement but low kappa on imbalanced labels?
2. What goes in a guideline's boundary examples?
3. When do you use weighted kappa?

## Sources
- [Artstein & Poesio, Inter-Coder Agreement for Computational Linguistics (2008)](https://aclanthology.org/J08-4004/)
- [scikit-learn, cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)
- [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Shankar et al. 2024, Who Validates the Validators?](https://arxiv.org/abs/2404.12272)
