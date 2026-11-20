---
id: annotation-guidelines
title: "Annotation guidelines"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [rubric-design]
tags: []
---
# Annotation guidelines

Instructions and calibration processes that make human labels reliable.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

## Why it matters
Agreement coefficients (kappa-like) quantify label reliability: Artstein & Poesio survey inter-coder agreement for computational linguistics, Computational Linguistics 34(4), 2008 [ACL Anthology](https://aclanthology.org/J08-4004/) (paper content not read; PDF not extractable). Cohen's kappa = (p_o - p_e)/(1 - p_e), range -1 to 1, weights option for ordinal [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html). Disagreement signals ambiguous tasks: "two domain experts reach same verdict" [ANTH-AGENT]; human labels calibrate automated graders [OAI-BP]; people refine criteria while labeling [Shankar](https://arxiv.org/abs/2404.12272).
## Common failure modes
Interpreting kappa with fixed bands (Landis & Koch bands are convention; primary source UNVERIFIED); kappa undefined in degenerate cases [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html); prevalence/bias effects on kappa and alpha vs kappa (UNVERIFIED); annotator drift (UNVERIFIED).
## Practice exercise
Draft a one-page guideline (definitions, decision rules, 3 positive + 3 boundary examples). Two annotators label 50 items; compute kappa (sklearn), adjudicate disagreements, revise guideline, relabel 50 fresh items, show kappa improvement.
## Mastery check
(1) Why high raw agreement but low kappa on imbalanced labels? (2) What goes in a guideline's boundary examples? (3) When do you use weighted kappa?
## Sources
https://aclanthology.org/J08-4004/; scikit-learn page above; [ANTH-AGENT]; [OAI-BP]; https://arxiv.org/abs/2404.12272.
