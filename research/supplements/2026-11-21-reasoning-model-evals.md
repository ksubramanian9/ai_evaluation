# Research supplement: reasoning-model-evals

As-of: 2026-11-21. Web access: WebFetch and WebSearch working.

- Snell, Lee, Xu, Kumar 2024, "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters". Compute-optimal per-prompt allocation >4x more efficient than best-of-N; FLOPs-matched, smaller model + test-time compute beats a 14x larger model where the small model has non-trivial success; best strategy depends on prompt difficulty. https://arxiv.org/abs/2408.03314 (abstract)
- Gema et al. 2025, "Inverse Scaling in Test-Time Compute" (TMLR Dec 2025). Tasks where longer reasoning lowers accuracy; four task categories; five failure modes (distraction, overfitting to framing, spurious correlations, losing focus on deduction, amplified concerning behaviours); recommends evaluating across diverse reasoning lengths. https://arxiv.org/abs/2507.14417 (abstract)
- Kapoor, Stroebl, Siegel, Nadgir, Narayanan 2024, "AI Agents That Matter". Narrow accuracy focus; joint cost-accuracy optimisation; inadequate holdouts; reproducibility problems. Abstract does not use the word "Pareto". https://arxiv.org/abs/2407.01502 (abstract)
- Turpin, Michael, Perez, Bowman 2023, "Language Models Don't Always Say What They Think" (NeurIPS 2023). Biasing features (answer always "(A)") influence answers without being mentioned in CoT; accuracy drops up to 36% on 13 BBH tasks (GPT-3.5, Claude 1.0). https://arxiv.org/abs/2305.04388 (abstract)
- Chen et al. 2025, "Reasoning Models Don't Always Say What They Think". 6 hint types; reveal rate often below 20%; outcome RL improves faithfulness then plateaus; reward hacking not verbalised; CoT monitoring not sufficient to rule out undesired behaviour. https://arxiv.org/abs/2505.05410 (abstract)
- Lanham et al. 2023, "Measuring Faithfulness in Chain-of-Thought Reasoning". Interventions on CoT (mistakes, paraphrase); reliance varies by task; larger models less faithful on most tasks studied. https://arxiv.org/abs/2307.13702 (abstract)
- Lightman et al. 2023, "Let's Verify Step by Step". Process supervision beats outcome supervision on MATH; 78% on representative MATH subset; PRM800K, 800K step-level labels. https://arxiv.org/abs/2305.20050 (abstract)
- Balunović, Dekoninck, Petrov, Jovanović, Vechev 2025, "MathArena" (NeurIPS 2025 D&B). "Strong signs of contamination in AIME 2024"; evaluating on newly released competitions avoids contamination; v3 (Jan 2026) 50+ models, 7 competitions, 162 problems. No contamination magnitude in abstract. https://arxiv.org/abs/2505.23281 (abstract)
- Anthropic extended thinking docs. `budget_tokens` min 1,024, less than `max_tokens`, "a target rather than a strict cap"; deprecated on 4.6, rejected (400) on 4.7+; adaptive thinking plus `output_config.effort`; at lower effort model may skip thinking; thinking tokens reported in `usage.output_tokens_details.thinking_tokens`; changing budget invalidates cache. https://platform.claude.com/docs/en/build-with-claude/extended-thinking (full page)
- OpenAI reasoning guide. Effort values model-dependent (none, minimal, low, medium, high, xhigh, max); raw reasoning tokens not exposed; billed as output tokens; summaries optional. https://developers.openai.com/api/docs/guides/reasoning (page, read via summariser)

## Gaps
- No paper read on judging reasoning traces with an LLM judge specifically (e.g. ProcessBench); the node's guidance to grade answer and trace separately is marked as design guidance.
- Run-to-run variance in reasoning length is design inference, not sourced.
- MathArena contamination evidence read at abstract level only; magnitude unverified.
