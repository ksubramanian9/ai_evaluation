---
id: eval-harness-design
title: "Eval harness design"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: testing
prerequisites: [programmatic-checks, public-benchmarks]
tags: [nondeterminism]
---
# Eval harness design

Components of an evaluation harness: datasets, runners, graders, result storage, reproducibility.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Biderman et al., drawing on three years of building lm-eval, report that results shift with evaluation setup, comparisons are hard to make fair, and undocumented conventions hurt reproducibility ([Biderman et al. 2024](https://arxiv.org/abs/2405.14782)).
- Inspect (UK AI Security Institute and Meridian Labs) defines an eval as a Task of dataset, solver and scorer ([Inspect docs, as-of 2026-11-20](https://inspect.aisi.org.uk/)).
- lm-evaluation-harness provides YAML task configs, request/result caching, per-sample logging (`--log_samples`) and output paths ([lm-eval README, as-of 2026-11-20](https://github.com/EleutherAI/lm-evaluation-harness)).
- HELM releases raw prompts and completions and a modular toolkit and evaluates all models on the same scenarios/metrics ([Liang et al. 2022](https://arxiv.org/abs/2211.09110)).

## Common failure modes
- Hidden setup differences (prompt format, few-shot, tokenization) change scores ([Biderman et al.](https://arxiv.org/abs/2405.14782)); similar sensitivity appears as 4-5% prompt-style variation on MMLU ([MMLU-Pro](https://arxiv.org/abs/2406.01574)).
- Not storing raw outputs, so graders cannot be rerun; HELM's raw-output release is the counterexample ([HELM](https://arxiv.org/abs/2211.09110)).
- No version pinning of dataset/grader/model. The lm-eval README does not describe a versioning feature (checked), so design it yourself.

## Practice exercise (4-6 h)
Build a mini harness (about 150 lines): JSONL dataset, runner with cache keyed by (model, prompt, params), pluggable graders, results store with config hash and git SHA, and a rerun that reuses cached outputs. Compare with an Inspect task on the same data.

## Mastery check
1. List what must be logged to reproduce a score.
2. How do you re-grade without re-calling the model?
3. What breaks when the prompt template changes but the dataset ID does not?

## Sources
- [Biderman et al. 2024, Lessons from the Trenches on Reproducible Evaluation of Language Models](https://arxiv.org/abs/2405.14782)
- [Inspect (UK AI Security Institute)](https://inspect.aisi.org.uk/)
- [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [Liang et al. 2022, HELM](https://arxiv.org/abs/2211.09110)
- [Wang et al. 2024, MMLU-Pro](https://arxiv.org/abs/2406.01574)
