# Landscape: 05-testing-in-engineering

Volatile items for this branch. One entry per line, format:

- <item> (type: tool|benchmark|model|standard) as-of: YYYY-MM-DD | <source URL>

## Entries

Migrated from research/05-testing-in-engineering.md (not individually re-verified; entries flagged UNVERIFIED there remain so).

- promptfoo CI/CD integration (Node >= 22.22.0 required, Node 24 recommended; JUnit/JSON/HTML output) - https://www.promptfoo.dev/docs/integrations/ci-cd/ as-of: 2026-11-20
- garak (NVIDIA) LLM vulnerability scanner - https://github.com/NVIDIA/garak as-of: 2026-11-20
- PyRIT 1.2.0 (Microsoft AI Red Team) - https://microsoft.github.io/PyRIT/1.2.0/ as-of: 2026-11-20
- MLflow Prompt Registry; Langfuse Prompt Management - links above as-of: 2026-11-20
- vLLM `vllm bench serve` metrics and options - https://docs.vllm.ai/en/latest/benchmarking/cli.html as-of: 2026-11-20
- VCR.py record modes - https://vcrpy.readthedocs.io/en/latest/usage.html as-of: 2026-11-20
- Fairlearn metrics (MetricFrame, demographic_parity_difference, equalized_odds_difference) - https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html as-of: 2026-11-20
- Benchmarks: HarmBench, XSTest, BBQ, AILuminate v1.0, AgentDojo (97 tasks / 629 security cases), PromptBench/PromptRobust, HELM as-of: 2026-11-20
- Standards: OWASP Top 10 for LLM Apps 2025; NIST AI 100-2 E2025 (2025-03); NIST AI 600-1 (2024-07-26) as-of: 2026-11-20
- Provider specifics: Anthropic API version 2026-10-21 removes `temperature`/`top_p`/`top_k` (400 error); model lifecycle/retirement dates (claude-sonnet-4-5-20250929 retires 2026-11-30); new tokenizer ~30% more tokens on Claude 4.7+; OpenAI `seed` + `system_fingerprint` "mostly" deterministic as-of: 2026-11-20 [verified 2026-11-20: https://platform.claude.com/docs/en/api/migration-2026-10-21]
- Determinism research: Thinking Machines batch-invariant kernels (Qwen3-235B-A22B experiment, 80 unique/1000) as-of: 2026-11-20
