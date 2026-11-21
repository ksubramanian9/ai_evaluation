---
id: conversational-evals
title: "Conversational / chatbot evaluation"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: none
prerequisites: [llm-as-judge, nondeterminism-and-variance]
tags: [llm-judge, nondeterminism, human-labels]
---
# Conversational / chatbot evaluation

Multi-turn quality, consistency, and context handling.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Build sharded multi-turn versions of single-turn tasks and compare them with the fully specified version.
- Separate aptitude (best-case) from unreliability (spread) using repeated runs.
- Measure judge position bias by swapping response order, and apply a mitigation.
- Apply a consistency check for persona or fact stability across turns.

**Done bar.** Practiced: 20 tasks sharded into 3-4 turns and run 5 times each, with a table of best-case versus spread for sharded and fully specified versions and a position-bias rate from order-swapped judging. Mastered: written answers to all four mastery questions checked against Zheng et al. and Laban et al., plus a multi-turn eval applied once to a real chatbot or the capstone, with the multi-turn versus single-turn gap recorded.

## Why it matters
- MT-Bench and Chatbot Arena: strong LLM judges agree with humans >80%, but show position, verbosity, self-enhancement bias (NeurIPS 2023 D&B, [arXiv 2306.05685](https://arxiv.org/abs/2306.05685)).
- Chatbot Arena uses crowdsourced pairwise comparison, 240K+ votes ([arXiv 2403.04132](https://arxiv.org/abs/2403.04132)).
- MT-Bench-101: 3-tier ability taxonomy, 4,208 turns/1,388 dialogues/13 tasks, 21 LLMs; alignment techniques did not noticeably improve multi-turn ability (ACL 2024, [arXiv 2402.14762](https://arxiv.org/abs/2402.14762)).
- Underspecified multi-turn: 39% average drop vs single-turn over six tasks, mostly from unreliability ([Laban et al., arXiv 2505.06120](https://arxiv.org/abs/2505.06120)).

## Common failure modes
- Early wrong assumptions then over-reliance; no recovery ([Laban et al.](https://arxiv.org/abs/2505.06120)).
- Judge biases ([Zheng et al.](https://arxiv.org/abs/2306.05685)).
- Single-turn tests miss multi-turn degradation.

## Practice exercise (3 h)
Take 20 single-turn tasks, shard each into 3-4 turns of progressively revealed info, compare to fully specified; run each 5 times to separate aptitude (best-case) from unreliability (spread). Judge with swapped order to measure position bias.

## Mastery check
1. Why does multi-turn unreliability differ from aptitude loss?
2. Mitigate position bias.
3. Pairwise vs absolute scoring trade-offs.
4. Define a consistency check (persona/fact stability across turns).

## Sources
- [Zheng et al., MT-Bench and Chatbot Arena, arXiv 2306.05685](https://arxiv.org/abs/2306.05685)
- [Chatbot Arena, arXiv 2403.04132](https://arxiv.org/abs/2403.04132)
- [MT-Bench-101, arXiv 2402.14762](https://arxiv.org/abs/2402.14762)
- [Laban et al., arXiv 2505.06120](https://arxiv.org/abs/2505.06120)
