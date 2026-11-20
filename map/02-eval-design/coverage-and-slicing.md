---
id: coverage-and-slicing
title: "Coverage and slicing"
branch: 02-eval-design
depth: L2
status: not-started
bridge: testing
prerequisites: [golden-datasets, statistical-inference]
tags: [fairness]
---
# Coverage and slicing

Ensuring test sets cover the input space, and reporting results by slice instead of only in aggregate.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

**Shared concept:** confidence intervals, power and paired comparisons are owned by [statistical-inference](../01-foundations/statistical-inference.md) and [confidence-intervals-for-evals](../03-measurement-methods/confidence-intervals-for-evals.md).

## Why it matters
Aggregate accuracy overestimates performance; CheckList uses a capability x test-type matrix, found critical failures in commercial models, and users wrote ~2x tests and found ~3x bugs [CheckList](https://arxiv.org/abs/2005.04118). Model cards report disaggregated results across demographic/cultural/phenotypic and intersectional groups [Mitchell et al.](https://arxiv.org/abs/1810.03993). HELM quantifies coverage (17.9% -> 96.0%) [HELM]. Slice discovery finds underperforming coherent subsets automatically; Domino recovers 36% of 1,235 benchmark slices [Eyuboglu et al.](https://arxiv.org/abs/2203.14960).
## Common failure modes
Aggregate hides subgroup failure [Mitchell](https://arxiv.org/abs/1810.03993); slices too small for stable estimates (UNVERIFIED in sources fetched; connect to Miller's error-bar paper https://arxiv.org/abs/2411.00640); unlabeled slices in high-dim inputs [Eyuboglu](https://arxiv.org/abs/2203.14960); coverage by count not by input-space diversity (UNVERIFIED).
## Practice exercise
Tag your golden set with 3-4 metadata attributes (topic, length, language, difficulty). Report accuracy per slice with bootstrap CIs; identify the worst slice; add targeted cases and a CheckList-style invariance test (e.g., typo/name swap).
## Mastery check
(1) Overall 90% yet one slice at 60%: how large must the slice be to be sure? (2) Draw a capability x test-type matrix for your app. (3) Why report intervals per slice?
## Sources
https://arxiv.org/abs/2005.04118; https://arxiv.org/abs/1810.03993; https://arxiv.org/abs/2203.14960; [HELM]. (Group-DRO and ML Test Score slice tests not verified.)
