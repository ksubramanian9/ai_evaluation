---
id: code-generation-evals
title: "Code generation evals"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: testing
prerequisites: [programmatic-checks, nondeterminism-and-variance, sandboxing-untrusted-code]
tags: [nondeterminism, security, agents]
---
# Code generation evals

Execution-based correctness such as pass@k, test-suite grading, and security of generated code.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** pass@k and pass^k are defined once in [nondeterminism-and-variance](../01-foundations/nondeterminism-and-variance.md#passk-and-passk-owned-here).

**Shared concept:** running untrusted code safely is covered in [sandboxing-untrusted-code](../05-testing-in-engineering/sandboxing-untrusted-code.md).

## Why it matters
- Functional correctness by unit tests, with unbiased pass@k: generate n>=k samples, count c correct, and compute 1 - C(n-c,k)/C(n,k); the naive 1-(1-p)^k estimate is biased; BLEU is unreliable for functional correctness ([Chen et al., Codex, arXiv 2107.03374](https://arxiv.org/pdf/2107.03374), sec. 2.1; read via local pdftotext).
- HumanEval is 164 hand-written problems, avg 7.7 tests; the paper built a gVisor sandbox for untrusted code ([same](https://arxiv.org/pdf/2107.03374), sec. 2.2-2.3).
- Codex solved 28.8% with one sample, 70.2% with 100 ([abstract](https://arxiv.org/abs/2107.03374)).

## Common failure modes
- Weak tests: EvalPlus (~80x more tests) dropped pass@k by 19.3-28.9% and changed rankings across 26 LLMs ([arXiv 2305.01210](https://arxiv.org/abs/2305.01210)).
- Contamination: LiveCodeBench collects post-cutoff problems (400, May 2023-May 2024), notes possible overfitting to HumanEval/MBPP ([arXiv 2403.07974](https://arxiv.org/abs/2403.07974)).
- Insecure code passing tests: ~40% of 1,689 Copilot programs over 89 scenarios were vulnerable ([Pearce et al., arXiv 2108.09293](https://arxiv.org/abs/2108.09293)); CyberSecEval measures propensity to generate insecure code ([arXiv 2312.04724](https://arxiv.org/abs/2312.04724)).
- Repo-level realism: SWE-bench is 2,294 real issues from 12 Python repos; Claude 2 solved 1.96% at release (ICLR 2024, [arXiv 2310.06770](https://arxiv.org/abs/2310.06770)); how solutions are checked is UNVERIFIED from the abstract (tests in paper body, not read).
- Running untrusted code outside a sandbox ([Codex paper](https://arxiv.org/pdf/2107.03374) sec. 2.3).

## Practice exercise (4 h)
Use 20 HumanEval problems ([github.com/openai/human-eval](https://github.com/openai/human-eval), cited in Codex paper). Sample n=10 per problem from any model at temp 0.8, compute pass@1/pass@5 with the Fig. 3 estimator, then add 5 extra edge-case tests per problem and recompute. Run a static analyzer (e.g. Bandit) on outputs for a security pass rate. Execute in Docker.

## Mastery check
1. Derive why 1-(1-p)^k is biased.
2. Why did EvalPlus change rankings?
3. Design a test-suite-adequacy check (mutation testing).
4. What isolation do you need to run model code?

## Sources
- [Chen et al., "Evaluating Large Language Models Trained on Code" (Codex), arXiv 2107.03374](https://arxiv.org/abs/2107.03374)
- [EvalPlus, arXiv 2305.01210](https://arxiv.org/abs/2305.01210)
- [LiveCodeBench, arXiv 2403.07974](https://arxiv.org/abs/2403.07974)
- [SWE-bench, arXiv 2310.06770](https://arxiv.org/abs/2310.06770)
- [Pearce et al., arXiv 2108.09293](https://arxiv.org/abs/2108.09293)
- [CyberSecEval, arXiv 2312.04724](https://arxiv.org/abs/2312.04724)
