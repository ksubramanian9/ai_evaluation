# Landscape: 05-testing-in-engineering

Volatile items for this branch. One entry per line, format:

- <item> (type: tool|benchmark|model|standard|regulation|docs) as-of: YYYY-MM-DD | <source URL, or `URL not recorded`>

## Entries

Migrated from research/05-testing-in-engineering.md (not individually re-verified; entries flagged UNVERIFIED there remain so).

- promptfoo CI/CD integration (Node >= 22.22.0 required, Node 24 recommended; JUnit/JSON/HTML output) (type: tool) as-of: 2026-11-20 | https://www.promptfoo.dev/docs/integrations/ci-cd/
- garak (NVIDIA) LLM vulnerability scanner (type: tool) as-of: 2026-11-20 | https://github.com/NVIDIA/garak
- PyRIT 1.2.0 (Microsoft AI Red Team) (type: tool) as-of: 2026-11-20 | https://microsoft.github.io/PyRIT/1.2.0/
- MLflow Prompt Registry (type: tool) as-of: 2026-11-20 | https://mlflow.org/docs/latest/genai/prompt-registry/
- Langfuse Prompt Management (type: tool) as-of: 2026-11-20 | https://langfuse.com/docs/prompt-management/get-started
- vLLM `vllm bench serve` metrics and options (type: tool) as-of: 2026-11-20 | https://docs.vllm.ai/en/latest/benchmarking/cli.html
- VCR.py record modes (type: tool) as-of: 2026-11-20 | https://vcrpy.readthedocs.io/en/latest/usage.html
- Fairlearn metrics (MetricFrame, demographic_parity_difference, equalized_odds_difference) (type: tool) as-of: 2026-11-20 | https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html
- Benchmarks: HarmBench (arXiv 2402.04249), XSTest (arXiv 2308.01263), BBQ (arXiv 2110.08193), AILuminate v1.0 (arXiv 2503.05731), AgentDojo (97 tasks / 629 security cases; arXiv 2406.13352), PromptBench/PromptRobust (arXiv 2306.04528), HELM (arXiv 2211.09110) (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2402.04249
- Standards: OWASP Top 10 for LLM Apps 2025 (type: standard) as-of: 2026-11-20 | https://genai.owasp.org/llm-top-10/
- Standards: NIST AI 100-2 E2025 (2025-03) (type: standard) as-of: 2026-11-20 | https://csrc.nist.gov/pubs/ai/100/2/e2025/final
- Standards: NIST AI 600-1 (2024-07-26) (type: standard) as-of: 2026-11-20 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Provider specifics: Anthropic API version 2026-10-21 removes `temperature`/`top_p`/`top_k` (400 error); model lifecycle/retirement dates (claude-sonnet-4-5-20250929 retires 2026-11-30); new tokenizer ~30% more tokens on Claude 4.7+; OpenAI `seed` + `system_fingerprint` "mostly" deterministic [verified 2026-11-20] (type: docs) as-of: 2026-11-20 | https://platform.claude.com/docs/en/api/migration-2026-10-21
- Determinism research: Thinking Machines batch-invariant kernels (Qwen3-235B-A22B experiment, 80 unique/1000) (type: docs) as-of: 2026-11-20 | https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
