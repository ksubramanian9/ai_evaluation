---
id: red-teaming
title: "Red teaming"
branch: 05-testing-in-engineering
depth: L3
status: not-started
bridge: testing
prerequisites: [robustness-testing]
tags: [safety, security, llm-judge]
---
# Red teaming

Structured adversarial probing, manual and automated, to find failures before users do.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Anthropic's study: 38,961 red-team attacks released; 2.7B/13B/52B models and four model types; RLHF models got harder to red-team with scale, others flat ([Ganguli et al., arXiv 2209.07858](https://arxiv.org/abs/2209.07858)).
- Automated: use an LM to generate test cases against a target and a classifier to score; found tens of thousands of offensive replies from a 280B chatbot ([Perez et al., arXiv 2202.03286](https://arxiv.org/abs/2202.03286)).
- Standardization: HarmBench compares 18 red-teaming methods on 33 target LLMs/defenses ([Mazeika et al., arXiv 2402.04249](https://arxiv.org/abs/2402.04249)).
- NIST AI 600-1 (GenAI Profile, published 2024-07-26) describes red-teaming as structured testing to probe for flaws and links it to pre-deployment testing ([NIST page](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence); red-teaming wording came from search snippet of the [PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), UNVERIFIED against full text).
- Tools (as-of 2026-11-20): [garak](https://github.com/NVIDIA/garak) (probes + detectors, reports FAIL rate per probe/detector), [PyRIT](https://microsoft.github.io/PyRIT/1.2.0/) (Microsoft AI Red Team; multi-turn Crescendo/TAP/Skeleton Key, scorers, memory).

## Common failure modes
- Automated attack success rate reported without a validated judge; scorer error dominates (HarmBench motivation: no common standard, [source](https://arxiv.org/abs/2402.04249)).
- Red team coverage narrow (one attack family); a one-off exercise rather than continuous.
- Findings not converted into regression tests.
- Attacker/crowdworker diversity limits (Ganguli documents methodology uncertainties, [source](https://arxiv.org/abs/2209.07858)).

## Practice exercise (4 h)
Pick a small chatbot with a system prompt and a policy (e.g., no medical dosing). Run garak with 2 probe families, plus 30 hand-written multi-turn attacks and 30 LM-generated (Perez method). Judge with a rubric; compute attack success rate with CI; add every successful attack to a regression file.

## Mastery check
1. Compare human, LM-generated, and tool-driven red teaming on cost, diversity, realism.
2. How do you validate the judge for attack success?
3. Define scope, threat model, and stopping criteria for a red-team exercise.

## Sources
- [Ganguli et al., arXiv 2209.07858](https://arxiv.org/abs/2209.07858)
- [Perez et al., arXiv 2202.03286](https://arxiv.org/abs/2202.03286)
- [HarmBench, arXiv 2402.04249](https://arxiv.org/abs/2402.04249)
- [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- practitioner: [garak](https://github.com/NVIDIA/garak)
- practitioner: [PyRIT](https://microsoft.github.io/PyRIT/1.2.0/)
