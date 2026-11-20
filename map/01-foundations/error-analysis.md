---
id: error-analysis
title: "Error analysis"
branch: 01-foundations
depth: L2
status: not-started
bridge: stats
prerequisites: [ml-metrics, evaluation-mindset]
tags: []
---
# Error analysis

Systematically categorizing failures to decide what to fix, instead of chasing aggregate scores.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._
## Why it matters
- Aggregate accuracy hides capability-specific bugs. CheckList's behavioral tests found critical failures in commercial and state-of-the-art models, and in a user study practitioners wrote about twice as many tests and found almost three times as many bugs ([Ribeiro et al., ACL 2020](https://arxiv.org/abs/2005.04118)).
- Criteria are discovered by reading outputs ("criteria drift"), and LLM judges need validation against human labels ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).
- Ng suggests hand-examining roughly 10% of the dev set and keeping the rest unseen, because eyeballing overfits ([Ng, Machine Learning Yearning, practitioner](https://home-wordpress.deeplearning.ai/wp-content/uploads/2022/03/andrew-ng-machine-learning-yearning.pdf); chapter details came from search snippets only, UNVERIFIED).
- Practitioner advice: read traces, start with binary good/bad labels, and keep reading until you stop learning new things ([Husain 2024, practitioner](https://hamel.dev/blog/posts/evals/)). That post does not use the terms "open coding" or "axial coding".

## Common failure modes
- Chasing the aggregate score without categorizing failures.
- Fixing criteria before looking at outputs.
- Overfitting to the examples you eyeball.
- Prioritizing a category by frequency alone and ignoring severity (UNVERIFIED, no source fetched).
- Slice-discovery tooling such as Errudite and SliceFinder: UNVERIFIED, not fetched.

## Practice exercise (3 h)
Take 100 failures from a classifier or LLM task. Without predefined labels, write a free-text note per failure and cluster the notes into 5-8 categories. Count them. For the top category write 5 CheckList-style tests (minimum functionality, invariance, directional; verify the names in the paper) and measure the pass rate. Hold out 100 unseen examples to confirm the category is real.

## Mastery check
1. How do you decide which failure category to fix first?
2. How many failures should you read, and how do you know when to stop?
3. How do you keep error analysis from overfitting your eval set?

## Sources
- Ribeiro et al., "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList" (ACL 2020): https://arxiv.org/abs/2005.04118
- Shankar et al., "Who Validates the Validators?": https://arxiv.org/abs/2404.12272
- Practitioner: Ng, Machine Learning Yearning: https://home-wordpress.deeplearning.ai/wp-content/uploads/2022/03/andrew-ng-machine-learning-yearning.pdf
- Practitioner: Husain, "Your AI Product Needs Evals": https://hamel.dev/blog/posts/evals/
