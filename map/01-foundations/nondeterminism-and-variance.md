---
id: nondeterminism-and-variance
title: "Non-determinism and variance"
branch: 01-foundations
depth: L2
status: not-started
bridge: stats
prerequisites: [llm-basics-for-evaluators, statistical-inference]
tags: [nondeterminism]
---
# Non-determinism and variance

Run-to-run variance in LLM outputs and how to budget samples to see through it.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._
## Why it matters
- Across 5 LLMs, 8 tasks and 10 runs, accuracy varied by up to 15% across natural runs and the best-to-worst gap reached 70%. No model was consistently repeatable even at "deterministic" settings. The authors propose TARr@N and TARa@N metrics ([Atil et al. 2024](https://arxiv.org/abs/2408.04667)).
- In ChatGPT code generation, the share of tasks with zero equal outputs across requests was 75.76% (CodeContests), 51.00% (APPS) and 47.56% (HumanEval). Temperature 0 reduces but does not remove nondeterminism ([Ouyang et al.](https://arxiv.org/abs/2308.02828)).
- Cause (practitioner source, one experiment): varying batch size with non-batch-invariant kernels. 1,000 temperature-0 completions of one prompt gave 80 unique outputs, versus 1 with batch-invariant kernels ([Thinking Machines, practitioner](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)).
- Budgeting: resampling each question K times cuts conditional variance by 1/K with diminishing returns, and next-token probabilities help when no chain of thought is needed ([Miller 2024](https://arxiv.org/abs/2411.00640)).
- Seed and decoding sensitivity in reasoning benchmarks ([Hochlehnert et al. 2025](https://arxiv.org/abs/2504.07086)).

## Common failure modes
- Assuming temperature 0 or a fixed seed gives reproducibility.
- Single-run comparisons of near-equal systems.
- Rerunning only failures until they pass, which is flaky-test behavior (UNVERIFIED, no source).
- Backend changes between runs (see the fingerprint note in [llm-basics-for-evaluators](llm-basics-for-evaluators.md)).

## Practice exercise (2-3 h)
Pick 50 questions with checkable answers. Run each 10 times at temperature 0 and at 0.7. Compute per-run accuracy, between-run SD, the fraction of questions with unstable answers, and Atil-style exact-match agreement across runs. Use the between-question vs within-question variance decomposition to choose K for a target CI width.

## Mastery check
1. Decompose eval variance into question sampling and generation sampling. Which does K-resampling reduce?
2. How many repeats do you need to detect a 2-point change? (Needs a power calculation; see [statistical-inference](statistical-inference.md).)
3. Why can the same request give different outputs at temperature 0 on a hosted API?

## Sources
- Atil et al., "Non-Determinism of 'Deterministic' LLM Settings": https://arxiv.org/abs/2408.04667
- Ouyang et al., ChatGPT code generation non-determinism: https://arxiv.org/abs/2308.02828
- Miller, "Adding Error Bars to Evals": https://arxiv.org/abs/2411.00640
- Hochlehnert et al.: https://arxiv.org/abs/2504.07086
- Practitioner: Thinking Machines: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

## pass@k and pass^k (owned here)
- pass@k asks whether at least one of k samples succeeds. The unbiased estimator draws n >= k samples, counts c correct, and computes 1 - C(n-c, k)/C(n, k). The naive 1 - (1-p)^k estimate is biased ([Chen et al., Codex, sec. 2.1](https://arxiv.org/abs/2107.03374), read from the PDF during research).
- pass^k asks whether all k trials succeed, which measures reliability. tau-bench introduced it and reported pass^8 below 25% in its retail domain ([tau-bench abstract](https://arxiv.org/abs/2406.12045)). Anthropic's example: 75% per-trial success gives about 42% at pass^3, which is 0.75^3 ([Anthropic, "Demystifying evals for AI agents"](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)).
- Use pass@k when one good attempt is enough (a developer picks the best of several suggestions). Use pass^k when every run must work (an agent acting unattended).
- Mastery check: explain why 1 - (1-p)^k is biased when p is estimated from the same n samples, and compute pass^k from per-task success rates.
- Used by: [code-generation-evals](../04-system-specific-evals/code-generation-evals.md), [tool-use-evals](../04-system-specific-evals/tool-use-evals.md), [agent-task-success-evals](../04-system-specific-evals/agent-task-success-evals.md).
