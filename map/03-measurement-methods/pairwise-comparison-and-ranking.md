---
id: pairwise-comparison-and-ranking
title: "Pairwise comparison and ranking"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: stats
prerequisites: [llm-as-judge, statistical-inference]
tags: []
---
# Pairwise comparison and ranking

Head-to-head preference comparison and rating systems such as Elo / Bradley-Terry.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
Pairwise preference is easier for judges (OpenAI: "LLMs are better at discriminating between options"; pairwise or pass/fail is more reliable than open-ended scores) [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices). Chatbot Arena collects crowdsourced pairwise votes (over 240K at paper time) and ranks models with statistical methods; the abstract does not name Bradley-Terry, so confirm in the full paper [Chiang et al. 2024](https://arxiv.org/abs/2403.04132). MT-Bench uses judge-based pairwise comparison [Zheng et al.](https://arxiv.org/abs/2306.05685).

## Common failure modes
- Leaderboard distortion from undisclosed private testing and selective disclosure (27 private Meta variants cited) and unequal sampling favoring proprietary models [Singh et al. 2025](https://arxiv.org/abs/2504.20879).
- Length and style confounds [Dubois et al.](https://arxiv.org/abs/2404.04475).
- Position bias in judge-based pairs [Wang et al.](https://arxiv.org/abs/2305.17926).
- Intransitivity and non-Bradley-Terry structure; original Bradley-Terry (1952) and Elo derivations. UNVERIFIED (not read).

## Practice exercise
Generate pairwise outcomes among 4 prompt variants on 40 inputs using a judge in both orders. Fit Bradley-Terry by logistic regression and compare with online Elo. Bootstrap CIs on ratings and report which ranks are statistically indistinguishable.

## Mastery check
1. Derive win probability from the rating difference.
2. Why does Elo depend on game order but a Bradley-Terry fit does not?
3. How many comparisons separate two models with a 55% win rate?

## Sources
[Chatbot Arena](https://arxiv.org/abs/2403.04132); [Leaderboard Illusion](https://arxiv.org/abs/2504.20879); [MT-Bench paper](https://arxiv.org/abs/2306.05685); [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).
