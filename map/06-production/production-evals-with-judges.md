---
id: production-evals-with-judges
title: "Production evals with judges"
branch: 06-production
depth: L3
status: not-started
bridge: none
prerequisites: [llm-as-judge, traffic-sampling-and-logging]
tags: [llm-judge, cost, statistics]
---
# Production evals with judges

Scoring live traffic with automated graders at acceptable cost.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** judge design and validation is owned by [llm-as-judge](../03-measurement-methods/llm-as-judge.md), with bias and calibration in [judge-bias-and-calibration](../03-measurement-methods/judge-bias-and-calibration.md); this node covers sampling, cost and operating judges on live traffic.

## Learning objectives
You can:
- Validate a production judge against human labels (Cohen's kappa) and probe it for position and verbosity bias.
- Run a judge on a sampled fraction of live traffic and report the score with a bootstrap CI.
- Choose a sampling rate under a cost budget and work out what it implies for detectable effect size.
- Design a judging setup that can tell a judge-caused score change (judge model change, missing context, criteria drift) from an app-caused one, and critique a setup that cannot.

**Done bar.** Practiced: a judge report on ~200 logged Q&A pairs with kappa against 60 human labels, a 10%-sample score with bootstrap CI, and swap-order and verbose-rewrite bias measurements. Mastered: written answers to all three mastery questions checked against Zheng et al. and Shankar et al., plus a production judging design (or critique of an existing one) that makes an explicit trade-off between sampling rate, cost and detectable effect size, and names how judge drift is caught.

## Why it matters
- Strong LLM judges reach over 80% agreement with humans, the same as human-human agreement, on MT-Bench and Chatbot Arena, which makes scalable scoring of live traffic possible ([Zheng et al. 2023](https://arxiv.org/abs/2306.05685)).
- Platforms run judges on a sampled subset of live traces via rules with filters and sampling rates ([Langfuse](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge), vendor; as of release; volatile).
- Anthropic's eval guidance recommends a different model for grading than the generator and lists LLM-based binary and Likert grading ([Anthropic: develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests); as of release; volatile).

## Common failure modes
- Position, verbosity and self-enhancement biases, plus limited reasoning ([Zheng et al.](https://arxiv.org/abs/2306.05685)).
- Judge not validated: LLM evaluators inherit LLM flaws; criteria drift as users see outputs, and some criteria only emerge from observed outputs ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).
- Cost blowup from judging all traffic (Langfuse cost estimate above); evaluators see only the matched observation, not children, so a judge can lack needed context ([Langfuse](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)).
- Judge model changes silently shift scores (design; judge is itself subject to provider deprecation, see model-upgrade).

## Practice exercise (4 h)
(design)
- Take ~200 logged Q&A pairs (public dataset). Human-label 60. Write a binary judge prompt, measure agreement (Cohen's kappa) with the labels, then run it on the rest at a 10% sample rate; report score with a bootstrap CI.
- Test swap-order and a verbose rewrite to measure position/verbosity bias.

## Mastery check
1. What do you report to claim a production judge is trustworthy (agreement, kappa, CI, bias probes)?
2. How would you detect that the judge, not the app, caused a score change?
3. Choose a sampling rate for 1M requests/day with a $200/day budget at $0.05/judgement; what does that imply for detectable effect size?

## Sources
- [Zheng et al. MT-Bench](https://arxiv.org/abs/2306.05685)
- [Shankar et al. EvalGen](https://arxiv.org/abs/2404.12272)
- [Anthropic develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- (practitioner/vendor) [Langfuse](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)
