# Landscape: 04-system-specific-evals

Volatile items for this branch. One entry per line, format:

- <item> (type: tool|benchmark|model|standard|regulation|docs) as-of: YYYY-MM-DD | <source URL, or `URL not recorded`>

## Entries

Migrated from research/04-system-specific-evals.md (not individually re-verified; entries flagged UNVERIFIED there remain so).

- BFCL leaderboard (Gorilla; V2/V3 added live and multi-turn per blog note; current version not verified). (type: benchmark) as-of: 2026-11-20 | https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html
- SWE-bench, WebArena (arXiv 2307.13854), OSWorld (arXiv 2404.07972), GAIA (arXiv 2311.12983), tau-bench (arXiv 2406.12045), AgentBench (arXiv 2308.03688): paper-time scores listed above are stale; refresh current SOTA. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2310.06770
- RAGAS metrics list (names may change). (type: tool) as-of: 2026-11-20 | https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
- TruLens "RAG triad" docs (names may change). (type: tool) as-of: 2026-11-20 | https://www.trulens.org/getting_started/core_concepts/rag_triad/
- Sentence-Transformers evaluators. (type: tool) as-of: 2026-11-20 | https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html
- OpenAI Structured Outputs (docs moved to developers.openai.com). (type: docs) as-of: 2026-11-20 | https://developers.openai.com/api/docs/guides/structured-outputs
- LiveCodeBench (rolling releases). (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2403.07974
- EvalPlus/HumanEval+. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2305.01210
- CyberSecEval (later versions exist, UNVERIFIED). (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2312.04724
- Long-context: RULER. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2404.06654
- Long-context: HELMET. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2410.02694
- Long-context: NoLiMa. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2502.05167
- Long-context: NIAH repo. (type: tool) as-of: 2026-11-20 | https://github.com/gkamradt/needle-in-a-haystack
- Multimodal: MMMU. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2311.16502
- Multimodal: MathVista. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2310.02255
- Multimodal: Video-MME. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2405.21075
- Multimodal: POPE. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2305.10355
- Chatbot Arena (vote counts, 240K at paper time). (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2306.05685
- MAST dataset. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2503.13657
- MultiAgentBench. (type: benchmark) as-of: 2026-11-20 | https://arxiv.org/abs/2503.01935
- Anthropic thinking controls: manual `budget_tokens` (min 1,024, target not cap) deprecated on 4.6 and rejected on 4.7+; adaptive thinking with `output_config.effort`; default effort differs by model (type: docs) as-of: 2026-11-21 | https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- OpenAI reasoning effort values are model-dependent (none/minimal/low/medium/high/xhigh/max); raw reasoning tokens hidden, billed as output; optional summaries (type: docs) as-of: 2026-11-21 | https://developers.openai.com/api/docs/guides/reasoning
- MathArena (post-release math competitions; v3 Jan 2026: 50+ models, 7 competitions, 162 problems) (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2505.23281
- tau2-bench (dual-control telecom domain with user simulator) (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2506.07982
- SimulatorArena (909 human-LLM conversations for validating user simulators) (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2510.05444
- Sim2Real user-simulation study and User-Sim Index (451 participants on tau-bench; best simulator USI 76.0 vs 92.7 human at paper time) (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2603.11245
- MGSM (250 GSM8K problems hand-translated into 10 languages). (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2210.03057
- Global-MMLU (42 languages; culturally sensitive vs agnostic subsets). (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2412.03304
- INCLUDE (197,243 QA pairs, 44 languages, local exam sources). (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2411.19799
- TyDi QA (11 languages, collected natively without translation). (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2003.05002
- Multilingual jailbreak data (Deng et al., code and data repo). (type: benchmark) as-of: 2026-11-21 | https://github.com/DAMO-NLP-SG/multilingual-safety-for-LLMs
- RAG diagnosis frameworks: RAGChecker (claim-level retriever/generator metrics), RAGAS, ARES. (type: tool) as-of: 2026-11-21 | https://arxiv.org/abs/2408.08067
- RAG benchmarks: CRAG (4,409 QA, truthfulness scoring), RGB (noise, rejection, integration, counterfactual). (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2406.04744
- Who&When failure-attribution dataset (failure logs from 127 LLM multi-agent systems; best agent-level 53.5%, step-level 14.2% at paper time). (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/abs/2505.00212
- MAST paper at arXiv v3 (26 Oct 2025); MAST-Data 1,642 traces from 7 frameworks. MultiAgentBench revised to v2 on 2026-11-18. (type: benchmark) as-of: 2026-11-21 | https://arxiv.org/html/2503.13657
