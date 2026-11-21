---
id: drift-detection
title: "Drift detection"
branch: 06-production
depth: L2
status: not-started
bridge: stats
prerequisites: [statistical-inference, traffic-sampling-and-logging]
tags: [statistics]
---
# Drift detection

Detecting shifts in inputs, outputs, and quality over time.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Owns:** quality shifts over time, including silent provider-side model changes; see also [model-upgrade-and-migration](model-upgrade-and-migration.md), [runtime-guardrails](runtime-guardrails.md).

## Learning objectives
You can:
- Distinguish covariate, label and concept shift, and state which can be detected without labels.
- Run per-dimension KS with Bonferroni, a domain-classifier two-sample test and MMD on embedded text, and compare their detection power against false-positive rate.
- Build an output/quality drift check (a fixed prompt set replayed against a hosted model on a schedule) to catch provider-side changes that input checks miss.
- Separate detecting a statistical shift from judging whether it is harmful, and set thresholds that avoid alert fatigue.

**Done bar.** Practiced: a plot of detection power vs false-positive rate for KS, classifier and MMD tests under injected drift of increasing magnitude, plus a weekly replay log of one output metric. Mastered: written answers to all three mastery questions checked against Rabanser et al. and Chen et al., and a drift monitor (input and output/quality) running on a capstone or real system with at least one alert or quiet period recorded and interpreted.

## Why it matters
- Hosted-model behaviour changes: GPT-4 prime/composite accuracy fell from 84% (March 2023) to 51% (June 2023), and the authors recommend continuous monitoring ([Chen, Zaharia, Zou](https://arxiv.org/abs/2307.09009)).
- For input drift, a two-sample test on pre-trained-classifier-reduced representations performed best across the shifts tested in "Failing Loudly" ([Rabanser et al.](https://arxiv.org/abs/1810.11953)). Domain-discriminating methods help characterise shifts and judge harm.
- Concept drift is where the input-target relation changes over time; Gama et al. survey adaptation strategies and evaluation ([ACM CSUR 2014 via search](https://eprints.bournemouth.ac.uk/22491/); taxonomy of drift types - sudden/gradual/recurring - not verified, page blocked).

## Common failure modes
- Detecting statistical shift that is harmless (alert fatigue); Rabanser et al. frame assessing harm as separate from detection ([abstract](https://arxiv.org/abs/1810.11953)).
- Per-column tests with default thresholds: Evidently docs differ across versions on defaults (Wasserstein/K-S/PSI, threshold 0.1, drift_share 50%) - check your version ([Evidently docs](https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests) (link 404 as of 2026-11-21), practitioner/OSS; as of release; volatile).
- Provider-side silent model changes need output/quality drift checks, not only input checks (Chen et al.).
- Applying tabular-drift tests to text without embeddings: UNVERIFIED (no primary source found on embedding-drift validity).

## Practice exercise (4 h)
(design)
- Take a text classification dataset with a natural time split (e.g. news by year). Embed, then run (a) per-dimension KS with Bonferroni, (b) classifier two-sample test (domain classifier AUC), (c) MMD. Inject synthetic drift of increasing magnitude and plot detection power vs false-positive rate. Replay a fixed prompt set against a model weekly and track an output metric (design).

## Mastery check
1. Covariate vs label vs concept shift; which can you detect without labels?
2. Why does the dimensionality-reduction step matter for two-sample tests?
3. Design the monitoring for a hosted LLM whose provider may change behaviour silently.

## Sources
- [Rabanser et al. Failing Loudly](https://arxiv.org/abs/1810.11953)
- [Chen et al. How is ChatGPT's behavior changing](https://arxiv.org/abs/2307.09009)
- [Gama et al. survey](https://eprints.bournemouth.ac.uk/22491/)
- (practitioner/OSS) [Evidently drift options](https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests) (link 404 as of 2026-11-21)
