---
id: reasoning-model-evals
title: "Reasoning and test-time-compute model evals"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: none
prerequisites: [nondeterminism-and-variance, llm-as-judge, performance-latency-cost-testing, contamination-and-leakage]
tags: [cost, nondeterminism, llm-judge]
---
# Reasoning and test-time-compute model evals

Evaluating models whose accuracy depends on how much they think: budget and effort sweeps, cost-latency-accuracy curves, judging reasoning traces, and contamination of reasoning benchmarks.

_Researched 2026-11-21. Supplemented 2026-11-21: [research/supplements/2026-11-21-reasoning-model-evals.md](../../research/supplements/2026-11-21-reasoning-model-evals.md). Paper claims were read at abstract level unless the supplement says otherwise; vendor parameter names were read from the current docs page and are volatile (see [landscape/04-system-specific-evals.md](../../landscape/04-system-specific-evals.md)). Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** run-to-run variance is owned by [nondeterminism-and-variance](../01-foundations/nondeterminism-and-variance.md), cost and latency measurement by [performance-latency-cost-testing](../05-testing-in-engineering/performance-latency-cost-testing.md), and contamination by [contamination-and-leakage](../02-eval-design/contamination-and-leakage.md); this node covers how those apply when test-time compute is a setting.

## Learning objectives
You can:
- Report a reasoning model's score as a curve over thinking budget or effort level, with cost and latency per point, instead of a single number.
- Pick an operating point from a cost-latency-accuracy curve for a stated product constraint.
- Grade final answers separately from reasoning traces, and explain why a plausible trace is not evidence of how the answer was reached.
- Choose a reasoning benchmark that resists contamination (post-release problems) and say why an older one may be inflated.

**Done bar.** Practiced: a sweep of one reasoning model over at least three budget or effort settings on 50 problems, 3 runs each, with a table and plot of accuracy, mean tokens, cost and p50/p95 latency per setting, and a chosen operating point with its justification. Mastered: written answers to all four mastery questions checked against Snell et al., Gema et al., Turpin et al., Chen et al. 2025 and MathArena, plus a critique of a real reasoning-model comparison (vendor post, paper or internal report) that names any missing budget, cost or contamination control.

## Why it matters
- Test-time compute changes the score: Snell et al. report that allocating inference compute per prompt by difficulty was over 4x more efficient than best-of-N, and that in a FLOPs-matched comparison a smaller model with extra test-time compute outperformed a 14x larger model on problems where the small model had non-trivial success (2024, [arXiv 2408.03314](https://arxiv.org/abs/2408.03314)).
- More thinking is not monotonically better: Gema et al. build tasks where longer reasoning lowers accuracy (distractors, spurious features, constraint tracking) and recommend evaluating models across diverse reasoning lengths (2025, [arXiv 2507.14417](https://arxiv.org/abs/2507.14417)).
- The setting is an API parameter: Anthropic's manual mode takes a `budget_tokens` value that is "a target rather than a strict cap", and its adaptive mode lets the model decide whether and how much to think, possibly skipping thinking at lower effort ([Anthropic extended thinking docs](https://platform.claude.com/docs/en/build-with-claude/extended-thinking), as-of 2026-11-21).
- OpenAI exposes a model-dependent reasoning effort setting; reasoning tokens are hidden but billed as output tokens and reported in usage ([OpenAI reasoning guide](https://developers.openai.com/api/docs/guides/reasoning), as-of 2026-11-21).
- Accuracy alone misleads: Kapoor et al. argue agent benchmarks focus narrowly on accuracy, call for jointly optimising cost and accuracy, and report widespread reproducibility problems (2024, [arXiv 2407.01502](https://arxiv.org/abs/2407.01502)).
- Stated reasoning can be unfaithful: biasing features (for example always making the answer "(A)") changed answers while CoT explanations did not mention them, dropping accuracy by up to 36% on 13 BIG-Bench Hard tasks (2023, [Turpin et al., arXiv 2305.04388](https://arxiv.org/abs/2305.04388)).
- Reasoning models also under-report: across 6 prompt hints, the rate at which CoTs revealed using a hint was often below 20%, and CoT monitoring is "not sufficient to rule out" undesired behaviour (2025, [Chen et al., arXiv 2505.05410](https://arxiv.org/abs/2505.05410)).
- Faithfulness varies by task and model; Lanham et al. test it by intervening on the CoT (inserting mistakes, paraphrasing) and found larger models gave less faithful reasoning on most tasks studied (2023, [arXiv 2307.13702](https://arxiv.org/abs/2307.13702)).
- Step-level grading of traces is possible and useful for training verifiers: process supervision beat outcome supervision on MATH, with 800K step labels released as PRM800K (2023, [Lightman et al., arXiv 2305.20050](https://arxiv.org/abs/2305.20050)).
- Reasoning benchmarks get contaminated: MathArena reports "strong signs of contamination in AIME 2024" and evaluates on competitions held after model release to avoid it (2025, [Balunović et al., arXiv 2505.23281](https://arxiv.org/abs/2505.23281)).

## Common failure modes
- Comparing two models at different, unreported budget or effort settings (default settings differ by model per the [Anthropic](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) and [OpenAI](https://developers.openai.com/api/docs/guides/reasoning) docs).
- Reporting accuracy without tokens, cost or latency, so a gain bought with 10x compute looks free ([Kapoor et al.](https://arxiv.org/abs/2407.01502)).
- Sweeping only upward and assuming more budget never hurts ([Gema et al.](https://arxiv.org/abs/2507.14417)).
- Treating a visible trace or summary as the model's actual reasoning, or as an audit log; raw reasoning may be hidden or summarised ([OpenAI reasoning guide](https://developers.openai.com/api/docs/guides/reasoning)) and stated reasoning can omit what drove the answer ([Turpin et al.](https://arxiv.org/abs/2305.04388), [Chen et al.](https://arxiv.org/abs/2505.05410)).
- Letting a judge reward a long, confident trace when the final answer is wrong; grade the answer with a programmatic check first and the trace separately (design guidance; no primary source).
- Using an older public competition set for a frontier reasoning model without a contamination check ([MathArena](https://arxiv.org/abs/2505.23281)).
- Single-run scores: reasoning length and therefore accuracy vary between runs, so report spread over repeated runs (design guidance; see [nondeterminism-and-variance](../01-foundations/nondeterminism-and-variance.md)).

## Practice exercise (3-4 h)
Pick 50 problems with verifiable answers, half from a competition released after your model's training cutoff and half from an older public set. Run one reasoning model at three or more budget or effort settings, 3 runs each, recording accuracy, thinking tokens from the usage field, cost, and p50/p95 latency. Plot accuracy against cost and against latency, mark the Pareto points, and pick an operating point for a stated constraint (for example p95 under 20 s). Compare old-set and new-set accuracy as a rough contamination signal. Finally, have a judge rate 20 traces for soundness without seeing the answer key, and report how often a "sound" trace ended in a wrong answer and the reverse.

## Mastery check
1. Why must a reasoning-model score be reported with its budget or effort setting, and what else must go beside it?
2. Give two reasons a higher thinking budget can lower accuracy, and how your sweep would detect it.
3. A trace looks correct but the answer is wrong, or the reverse. What does each case tell you, and why can a trace not be read as the model's true reasoning?
4. How would you tell whether a reasoning benchmark score is inflated by contamination?

## Sources
- [Snell et al. 2024, Scaling LLM Test-Time Compute Optimally, arXiv 2408.03314](https://arxiv.org/abs/2408.03314)
- [Gema et al. 2025, Inverse Scaling in Test-Time Compute, arXiv 2507.14417](https://arxiv.org/abs/2507.14417)
- [Kapoor et al. 2024, AI Agents That Matter, arXiv 2407.01502](https://arxiv.org/abs/2407.01502)
- [Turpin et al. 2023, Language Models Don't Always Say What They Think, arXiv 2305.04388](https://arxiv.org/abs/2305.04388)
- [Chen et al. 2025, Reasoning Models Don't Always Say What They Think, arXiv 2505.05410](https://arxiv.org/abs/2505.05410)
- [Lanham et al. 2023, Measuring Faithfulness in Chain-of-Thought Reasoning, arXiv 2307.13702](https://arxiv.org/abs/2307.13702)
- [Lightman et al. 2023, Let's Verify Step by Step, arXiv 2305.20050](https://arxiv.org/abs/2305.20050)
- [Balunović et al. 2025, MathArena, arXiv 2505.23281](https://arxiv.org/abs/2505.23281)
- [Anthropic docs: extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
- [OpenAI docs: reasoning models](https://developers.openai.com/api/docs/guides/reasoning)
