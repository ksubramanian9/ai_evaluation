---
id: online-metrics-and-user-feedback
title: "Online metrics and user feedback"
branch: 06-production
depth: L2
status: not-started
bridge: none
prerequisites: [metric-selection]
tags: []
---
# Online metrics and user feedback

Implicit and explicit signals such as thumbs, edits, and abandonment, and their biases.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Implicit feedback like clicks is biased by position: raw clicks train suboptimal rankers, and propensity-weighted counterfactual estimation corrects this ([Joachims, Swaminathan, Schnabel](https://arxiv.org/abs/1608.04468)). Earlier work by Joachims et al. reported that clicks are biased by presentation and that relative preferences are more reliable than absolute click values ([Joachims et al. 2005 PDF](https://www.cs.cornell.edu/people/tj/publications/joachims_etal_05a.pdf)) - UNVERIFIED in detail: PDF text was not machine-readable in my fetch; the claim is from the paper's known thesis, confirm before citing.
- Offline metrics may not match online outcomes; Kohavi et al. present controlled experiments as the way to establish causal impact on user-observable behaviour ([Kohavi et al. 2009](https://link.springer.com/article/10.1007/s10618-008-0114-1), abstract via search).

## Common failure modes
- Position/presentation bias (above). For chat UIs, analogous selection bias applies: thumbs come from a self-selected few (UNVERIFIED for LLM chat; no primary source found).
- Metric gaming and proxy mismatch (cross-ref metric-selection).
- Feedback conflated with quality: users may click or thumb based on tone/length, which mirrors judge verbosity bias ([Zheng et al. 2023](https://arxiv.org/abs/2306.05685)).
- Hidden feedback loops: system outputs shape the data later used to train/evaluate it ([Sculley et al.](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html), abstract lists "hidden feedback loops").

## Practice exercise
(design)
- Use a public click or preference dataset (e.g. a public search click log or pairwise preference data). Compute naive CTR per position, then an inverse-propensity-weighted estimate with propensities estimated from a randomised slice (or simulate clicks with a known position-bias model and recover true relevance).
- For an LLM app: define 3 implicit signals (regenerate rate, edit distance, abandonment), compute them on a logged sample, and correlate each with a small human-labelled quality set.

## Mastery check
1. Why can't you read CTR as relevance? How does propensity weighting fix it, and what does it assume?
2. Name two biases in thumbs-up/down feedback and one design change reducing each.
3. Which implicit signal would you trust for a coding assistant and why? Defend with a correlation to labelled data.

## Sources
- [Joachims et al., unbiased LTR (arXiv 1608.04468)](https://arxiv.org/abs/1608.04468)
- [Kohavi et al. 2009](https://link.springer.com/article/10.1007/s10618-008-0114-1)
- [Sculley et al. 2015](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)
