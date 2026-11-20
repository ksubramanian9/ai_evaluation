---
id: multimodal-evals
title: "Multimodal evals (extension)"
branch: 04-system-specific-evals
depth: L1
status: not-started
bridge: none
prerequisites: [metric-selection]
tags: []
---
# Multimodal evals (extension)

Extension node: vision, speech, and mixed-modality evaluation.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
MMMU: ~11.5K college-level questions, 6 disciplines/30 subjects/183 subfields, GPT-4V ~56% at release (CVPR 2024, [arXiv 2311.16502](https://arxiv.org/abs/2311.16502)). MathVista: 6,141 examples, GPT-4V 49.9%, 10.4 points below human ([arXiv 2310.02255](https://arxiv.org/abs/2310.02255)). Video-MME: 900 videos/254 h/2,700 QA ([arXiv 2405.21075](https://arxiv.org/abs/2405.21075)). POPE: polling-based object-hallucination test; existing methods skewed by instructions and generation style (EMNLP 2023, [arXiv 2305.10355](https://arxiv.org/abs/2305.10355)). Scores are release-time [V].

## Common failure modes
Object hallucination, frequent/co-occurring objects favored (POPE); evaluation sensitive to prompt style; speech evaluation not covered here (UNVERIFIED; no speech source read, e.g. WER).

## Practice exercise
Build 50 yes/no POPE-style probes ("Is there a X in the image?") on 25 images with present and absent objects; compute accuracy, precision, recall, yes-rate for one VLM.

## Mastery check
(1) Why a yes-rate metric? (2) Why are knowledge benchmarks like MMMU poor hallucination tests? (3) Design a test for text-in-image reading.

## Sources
MMMU; MathVista; Video-MME; POPE.
