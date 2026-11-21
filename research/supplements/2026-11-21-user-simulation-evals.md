# Research supplement: user-simulation-evals

As-of: 2026-11-21. Web access: WebFetch and WebSearch working.

- Yao, Shinn, Razavi, Narasimhan 2024, "tau-bench". LM plays the user; agent has domain API tools and policy; success = final database state vs annotated goal state; pass^k for reliability; gpt-4o-class agents <50% success, pass^8 <25% in retail. https://arxiv.org/abs/2406.12045 (abstract)
- Barres, Dong, Ray, Si, Narasimhan 2025, "tau2-Bench: Evaluating Conversational Agents in a Dual-Control Environment". Telecom domain as Dec-POMDP where user also acts via tools; simulator constrained by tools and observable state for fidelity; significant drops moving from no-user to dual-control. https://arxiv.org/abs/2506.07982 (abstract)
- Zhou et al. 2026, "Mind the Sim2Real Gap in User Simulation for Agentic Tasks" (COLM 2026). 451 participants, 165 tasks, 31 simulators; simulators "excessively cooperative, stylistically uniform"; "easy mode"; more capable model not necessarily more faithful; uniformly more positive feedback. From HTML (first 100k chars): best USI 76.0 (DeepSeek-V3.1) vs 92.7 human-human; human baseline agent success 63.6% vs top simulators up to 77.8%; recommendations: validate against real humans, report behaviour/outcomes/ratings separately, discourage revealing all info at once, separate human data for improving vs evaluating simulators, small human study per domain to confirm rankings. https://arxiv.org/abs/2603.11245 and https://arxiv.org/html/2603.11245v2 (abstract + partial full text)
- Dou et al. 2025, "SimulatorArena" (EMNLP 2025). 909 annotated human-LLM conversations, math tutoring and document creation; message-level realism and rating-level alignment; profile-conditioned simulators reach Spearman rho ~0.7. From HTML: vanilla simulators "overly verbose and polite"; zero-shot-CoT user messages 89.5 / 123.9 words vs human 15.5 / 32.6 (Table 2); evaluation via Likert style similarity, LLM Turing test with order swap, Spearman on z-normalised ratings, Macro F1 for outcomes. https://arxiv.org/abs/2510.05444 and https://arxiv.org/html/2510.05444v2 (abstract + partial full text)
- Search results also listed further 2026 simulator-fidelity papers (arXiv 2605.02624, 2606.20708, 2601.17087, 2610.31512); NOT read, not cited.

## Gaps
- Same-family simulator/agent bias is a hypothesis (marked UNVERIFIED in node).
- Persona-coverage guidance is design guidance beyond SimulatorArena's profile result.
- tau-bench's simulator prompt details not read.
