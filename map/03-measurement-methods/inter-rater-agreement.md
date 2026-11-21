---
id: inter-rater-agreement
title: "Inter-rater agreement"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: stats
prerequisites: [human-evaluation, statistical-inference]
tags: [human-labels, statistics]
---
# Inter-rater agreement

Cohen's/Fleiss' kappa, Krippendorff's alpha, and what agreement levels imply.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Compute percent agreement, Cohen's kappa, weighted kappa and Krippendorff's alpha.
- Bootstrap a CI on kappa.
- Show how skewed labels produce high agreement with low kappa.
- Choose an agreement coefficient for the number of raters and the scale type.

**Done bar.** Practiced: a table of the four coefficients on the two-rater data, the skewed 95/5 demonstration, and a bootstrap CI on kappa. Mastered: written answers to all three mastery-check questions, checked against Artstein & Poesio and Thakur et al., plus agreement reported for a real labeling or judge-validation task with the chosen coefficient and its CI recorded.

## Why it matters
- Agreement quantifies whether labels are reliable enough to serve as ground truth.
- Artstein & Poesio's survey is the CL reference on inter-coder agreement coefficients; the fetched page had no abstract, so its content claims are UNVERIFIED ([Artstein & Poesio 2008](https://aclanthology.org/J08-4004/)).
- Thakur et al. argue percent agreement alone is insufficient for judging LLM judges: "judges with high percent agreement can still assign vastly different scores" ([Thakur et al. 2024](https://arxiv.org/abs/2406.12624)).

## Common failure modes
- Reporting raw percent agreement, which ignores chance agreement. UNVERIFIED here (Artstein & Poesio cover it).
- Kappa prevalence/skew paradox and arbitrary Landis-Koch bands. UNVERIFIED; Cohen 1960 and Landis & Koch 1977 were not read.
- Using nominal kappa for ordinal scales when weighted kappa or Krippendorff's alpha fits. UNVERIFIED.

## Practice exercise (2 h)
Use the two-rater data from human-evaluation. Compute percent agreement, Cohen's kappa, weighted kappa (sklearn) and Krippendorff's alpha (`krippendorff` package). Build a skewed 95/5 label set and show high agreement with low kappa. Bootstrap a CI on kappa.

## Mastery check
1. Why can 90% agreement coexist with kappa near 0?
2. When do you use Fleiss' kappa vs Krippendorff's alpha?
3. What agreement level makes labels usable as ground truth for a judge, and why is there no universal cutoff?

## Sources
- [Artstein & Poesio 2008, Inter-Coder Agreement for Computational Linguistics](https://aclanthology.org/J08-4004/)
- [Thakur et al. 2024, Judging the Judges](https://arxiv.org/abs/2406.12624)
- Originals (Cohen 1960, Fleiss 1971, Krippendorff) still to locate; see Gaps (URL not recorded).
