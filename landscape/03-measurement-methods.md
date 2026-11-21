# Landscape: 03-measurement-methods

Volatile items for this branch. One entry per line, format:

- <item> (type: tool|benchmark|model|standard|regulation|docs) as-of: YYYY-MM-DD | <source URL, or `URL not recorded`>

## Entries

Migrated from research/03-measurement-methods.md (not individually re-verified; entries flagged UNVERIFIED there remain so).

- Inspect AI (UK AISI and Meridian Labs). (type: tool) as-of: 2026-11-20 | https://inspect.aisi.org.uk/
- EleutherAI lm-evaluation-harness (v0.4.x referenced in README). (type: tool) as-of: 2026-11-20 | https://github.com/EleutherAI/lm-evaluation-harness
- Provider eval docs moved to platform.claude.com and developers.openai.com (301 redirects seen); URLs are volatile. (type: docs) as-of: 2026-11-20 | URL not recorded
- Chatbot Arena leaderboard and the Leaderboard Illusion critique (2025). (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2504.20879
- Benchmarks: MMLU (arXiv 2009.03300), MMLU-Pro (arXiv 2406.01574), MMLU-Redux (arXiv 2406.04127), GSM8k/GSM1k (arXiv 2405.00332), SWE-bench (arXiv 2310.06770), HumanEval (arXiv 2107.03374), IFEval (arXiv 2311.07911), SuperGPQA (arXiv 2502.14739), HELM (arXiv 2211.09110). Scores quoted are at paper dates (2020-2025), not current. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2406.01574
- Judges: GPT-4 and Prometheus 13B (2023); judge model choice is volatile. (type: model) as-of: 2026-11-20 | https://arxiv.org/abs/2310.08491
- BetterBench living repository of benchmark assessments. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2411.12990
- Sandbox runtimes for eval code execution: Docker (namespaces/cgroups, --network none, --read-only, --pids-limit), gVisor (runsc), Firecracker microVMs. (type: tool) as-of: 2026-11-21 | https://gvisor.dev/docs/architecture_guide/security/
- Inspect AI sandbox providers: built-in docker and local (no isolation); external k8s, daytona, modal, proxmox, vagrant, openshell. (type: tool) as-of: 2026-11-21 | https://inspect.aisi.org.uk/sandboxing.html
- SWE-bench Docker harness (3-layer images, cache levels, optional Modal cloud execution; 120GB disk, 16GB RAM recommended). (type: tool) as-of: 2026-11-21 | https://github.com/SWE-bench/SWE-bench/blob/main/docs/guides/docker_setup.md
- Text overlap metrics in use: sacreBLEU, ROUGE, chrF, BERTScore. (type: tool) as-of: 2026-11-21 | https://arxiv.org/abs/1904.09675
- scikit-learn cohen_kappa_score supports weights None/'linear'/'quadratic' (docs 1.9.1). (type: docs) as-of: 2026-11-21 | https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html
- krippendorff (fast-krippendorff) Python package 0.9.0, `krippendorff.alpha(reliability_data=...)`. (type: tool) as-of: 2026-11-21 | https://pypi.org/project/krippendorff/
