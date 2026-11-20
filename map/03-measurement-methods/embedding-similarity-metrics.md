---
id: embedding-similarity-metrics
title: "Embedding-based similarity"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: stats
prerequisites: [reference-based-metrics]
tags: []
---
# Embedding-based similarity

Semantic similarity scoring and its blind spots.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
BERTScore matches candidate and reference tokens using contextual BERT embeddings rather than exact n-grams. It was tested on 363 MT and captioning systems and reported better correlation with human judgments than existing metrics [Zhang et al. 2020](https://arxiv.org/abs/1904.09675). Sentence-BERT makes sentence-level embedding comparison cheap: finding the most similar pair among 10,000 sentences takes about 50 million BERT pair inferences (about 65 hours) in the pair-input setup [Reimers & Gurevych 2019](https://arxiv.org/abs/1908.10084). Anthropic's docs use cosine similarity of sentence embeddings as a consistency grader [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests).

## Common failure modes
- Geometry: contextual embeddings are anisotropic (not isotropic in any layer of ELMo/BERT/GPT-2), which makes raw cosine values hard to interpret [Ethayarajh 2019](https://arxiv.org/abs/1909.00512).
- Cosine captures topical/semantic closeness and can miss negation, entity or number swaps. UNVERIFIED (no source read on this).
- Scores depend on the embedding model/layer and are not comparable across models. UNVERIFIED.

## Practice exercise
Embed 40 sentence pairs (20 paraphrases, 10 negations, 10 entity/number swaps) with a Sentence-BERT model. Plot cosine by class and find the separating threshold. Compute BERTScore on the same pairs. Report which classes fail.

## Mastery check
1. What does a cosine of 0.85 mean for a given embedding model?
2. Why might negation pairs score high?
3. How would you calibrate a threshold against human labels?

## Sources
[BERTScore](https://arxiv.org/abs/1904.09675); [SBERT](https://arxiv.org/abs/1908.10084); [Ethayarajh](https://arxiv.org/abs/1909.00512).
