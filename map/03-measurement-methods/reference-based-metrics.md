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

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Supplemented 2026-11-21: [research/supplements/2026-11-21-reference-based-metrics.md](../../research/supplements/2026-11-21-reference-based-metrics.md). BLEU, ROUGE, Callison-Burch et al. were read in full; chrF at abstract and conclusions; BERTScore at abstract only. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Explain what BLEU (clipped n-gram precision plus brevity penalty) and ROUGE (n-gram or subsequence recall) measure.
- Explain why a BLEU report must include its configuration signature and number of references.
- Recognise outputs where overlap scores invert relative to real quality.
- Identify when overlap metrics are still a reasonable choice.

**Done bar.** Practiced: a table of sacreBLEU (with its signature) and ROUGE-1/2/L for 30 items plus 10 paraphrases and 10 fluent-but-wrong outputs, with the inversions marked. Mastered: written answers to all three mastery-check questions, checked against Papineni et al., Lin, Callison-Burch et al. and Post, plus explaining to someone else without notes why BLEU scores from different papers cannot be compared, with one inversion example.

## Why it matters
- BLEU clips each candidate n-gram count at its maximum count in any single reference, takes the geometric mean of 1- to 4-gram precisions, and multiplies by a brevity penalty computed over the whole corpus ([Papineni et al. 2002](https://aclanthology.org/P02-1040/)).
- BLEU was designed as a corpus-level metric: its authors say it "only needs to match human judgment when averaged over a test corpus" and that sentence scores "will often vary from human judgments" ([Papineni et al.](https://aclanthology.org/P02-1040/)).
- Its original validation was system-level: correlation 0.99 with monolingual and 0.96 with bilingual judges over 5 systems (2002) ([Papineni et al.](https://aclanthology.org/P02-1040/)).
- ROUGE-N is n-gram recall against reference summaries; ROUGE-L uses longest common subsequence, and ROUGE-S/SU skip-bigrams ([Lin 2004](https://aclanthology.org/W04-1013/)).
- ROUGE correlated well with system-level human coverage scores on single-document summaries, but high correlation "was hard to achieve" for multi-document summaries (DUC 2001-2003) ([Lin 2004](https://aclanthology.org/W04-1013/)).
- Variants: chrF scores character n-gram F-score and is tokenisation-independent ([Popović 2015](https://aclanthology.org/W15-3049/)); BERTScore matches tokens by contextual embeddings instead of exact strings (abstract only) ([Zhang et al.](https://arxiv.org/abs/1904.09675)).

## Common failure modes
- Configuration drift: tokenization and normalization changed scores by up to 1.8 BLEU in Post's measurements, so cross-paper comparisons need a standard tool such as sacreBLEU ([Post 2018](https://arxiv.org/abs/1804.08771)).
- Reference count: more references raise BLEU; a human translator scored 0.3468 against four references and 0.2571 against two ([Papineni et al.](https://aclanthology.org/P02-1040/)).
- Paraphrase blindness: synonyms count only if a reference contains them, and content words weigh the same as function words ([Callison-Burch et al. 2006](https://aclanthology.org/E06-1032/)).
- Too many equal scores: one example hypothesis has at least 40,320 reorderings with a similar BLEU score, so a higher BLEU is "neither necessary nor sufficient" for better quality ([Callison-Burch et al.](https://aclanthology.org/E06-1032/)).
- Comparing different system types: in NIST 2005 the human-ranked 1st entry was 6th by BLEU, and BLEU "vastly" underestimated rule-based Systran against statistical systems ([Callison-Burch et al.](https://aclanthology.org/E06-1032/)).
- Weak correlation for open-ended NLG: G-Eval's authors report BLEU and ROUGE have "relatively low correlation with human judgments" ([Liu et al. 2023](https://arxiv.org/abs/2303.16634)).

**Still reasonable when** you track incremental changes to one system or compare systems with similar strategies, at corpus level, with a fixed configuration ([Callison-Burch et al.](https://aclanthology.org/E06-1032/)).

## Practice exercise (2 h)
Take 30 summaries or translations with references. Compute BLEU (sacreBLEU, record its signature) and ROUGE-1/2/L. Write 10 meaning-preserving paraphrases and 10 fluent but wrong outputs. Show where the scores invert relative to your own judgment, and note whether the inversions shrink at corpus level.

## Mastery check
1. Why must a BLEU report include its configuration signature and reference count?
2. Construct an output with high ROUGE and bad quality, and the reverse.
3. When are these metrics still a reasonable choice?

## Sources
- [Papineni et al. 2002, BLEU](https://aclanthology.org/P02-1040/)
- [Lin 2004, ROUGE](https://aclanthology.org/W04-1013/)
- [Callison-Burch, Osborne, Koehn 2006, Re-evaluating the Role of Bleu in Machine Translation Research](https://aclanthology.org/E06-1032/)
- [Post 2018, A Call for Clarity in Reporting BLEU Scores (sacreBLEU)](https://arxiv.org/abs/1804.08771)
- [Popović 2015, chrF](https://aclanthology.org/W15-3049/)
- [Zhang et al., BERTScore, arXiv 1904.09675](https://arxiv.org/abs/1904.09675)
- [Liu et al. 2023, G-Eval](https://arxiv.org/abs/2303.16634)
