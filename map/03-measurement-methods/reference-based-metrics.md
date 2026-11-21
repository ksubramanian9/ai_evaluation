---
id: reference-based-metrics
title: "Reference-based text metrics"
branch: 03-measurement-methods
depth: L1
status: not-started
bridge: stats
prerequisites: [ml-metrics]
tags: [statistics]
---
# Reference-based text metrics

BLEU, ROUGE, and related overlap metrics: what they capture and why they correlate weakly with quality.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Explain what BLEU and ROUGE measure and why they remain cheap, deterministic baselines.
- Explain why a BLEU report must include its configuration signature.
- Recognise outputs where overlap scores invert relative to real quality.
- Identify when overlap metrics are still a reasonable choice.

**Done bar.** Practiced: a table of sacreBLEU (with its signature) and ROUGE-1/2/L for 30 items plus 10 paraphrases and 10 fluent-but-wrong outputs, with the inversions marked. Mastered: written answers to all three mastery-check questions, checked against Post and Liu et al., plus explaining to someone else without notes why BLEU scores from different papers cannot be compared, with one inversion example.

## Why it matters
- BLEU (Papineni et al., ACL 2002) and ROUGE (Lin, 2004) are the canonical overlap metrics for MT and summarization; cheap, deterministic, still used as baselines.
- Only bibliographic data verified; the abstracts were not on the fetched pages ([BLEU](https://aclanthology.org/P02-1040/), [ROUGE](https://aclanthology.org/W04-1013/)).

## Common failure modes
- BLEU is a parameterized metric. Tokenization/normalization differences changed scores by up to 1.8 BLEU in Post's measurements, so cross-paper comparisons are invalid without a standardized tool such as sacreBLEU ([Post 2018](https://arxiv.org/abs/1804.08771)).
- Weak correlation with human judgment: G-Eval's authors state BLEU and ROUGE have "relatively low correlation with human judgments" for NLG ([Liu et al. 2023](https://arxiv.org/abs/2303.16634)).
- Callison-Burch et al. "Re-evaluating the Role of Bleu" is the classic critique, but I could not read its abstract, so its claims are UNVERIFIED ([ACL Anthology](https://aclanthology.org/E06-1032/)).
- Single-reference dependence and paraphrase blindness. UNVERIFIED.

## Practice exercise (2 h)
Take 30 summaries or translations with references. Compute BLEU (sacreBLEU, record its signature) and ROUGE-1/2/L. Write 10 meaning-preserving paraphrases and 10 fluent but wrong outputs. Show where the scores invert relative to your own judgment.

## Mastery check
1. Why must a BLEU report include its configuration signature?
2. Construct an output with high ROUGE and bad quality, and the reverse.
3. When are these metrics still a reasonable choice?

## Sources
- [Papineni et al. 2002, BLEU](https://aclanthology.org/P02-1040/)
- [Lin 2004, ROUGE](https://aclanthology.org/W04-1013/)
- [Post 2018, A Call for Clarity in Reporting BLEU Scores (sacreBLEU)](https://arxiv.org/abs/1804.08771)
- [Liu et al. 2023, G-Eval](https://arxiv.org/abs/2303.16634)
- [Callison-Burch et al. 2006, Re-evaluating the Role of Bleu](https://aclanthology.org/E06-1032/)
