# Research supplement: multi-agent-evals

As of: 2026-11-21. Web access: working (WebFetch, WebSearch).

## MAST: "Why Do Multi-Agent LLM Systems Fail?" (arXiv 2503.13657)
Read: full text of the HTML version (arXiv v3, stamped 26 Oct 2025), main body and appendices H-N; the tail of Appendix N (worked examples) only skimmed. URL: https://arxiv.org/html/2503.13657

- Taxonomy: 14 failure modes in 3 categories. Names verbatim, with prevalence across MAST-Data as reported in the paper's taxonomy figure:
  - FC1 System Design Issues: FM-1.1 Disobey task specification (11.8%); FM-1.2 Disobey role specification (1.5%); FM-1.3 Step repetition (15.7%); FM-1.4 Loss of conversation history (2.80%); FM-1.5 Unaware of termination conditions (12.4%).
  - FC2 Inter-Agent Misalignment: FM-2.1 Conversation reset (2.20%); FM-2.2 Fail to ask for clarification (6.80%); FM-2.3 Task derailment (7.40%); FM-2.4 Information withholding (0.85%); FM-2.5 Ignored other agent's input (1.90%); FM-2.6 Reasoning-action mismatch (13.2%).
  - FC3 Task Verification: FM-3.1 Premature termination (6.20%); FM-3.2 No or incomplete verification (8.20%); FM-3.3 Incorrect verification (9.10%).
- Definitions read for FM-1.3 ("Unnecessary reiteration of previously completed steps"), FM-2.6 ("Discrepancy between the logical reasoning process and the actual actions taken"), FM-3.2 ("(partial) omission of proper checking or confirmation of task outcomes"), FM-3.3 ("Failure to adequately validate or cross-check crucial information or decisions").
- Data: MAST-Data has 1,642 annotated traces (abstract says "1600+") from 7 frameworks: MetaGPT, ChatDev, HyperAgent, AppWorld, AG2, Magentic-One, OpenManus. Manus is mentioned but excluded because traces were unavailable.
- Method: grounded theory on 150 traces from five frameworks, examined by six experts. Inter-annotator agreement: three annotators labelled 15 traces in iterative rounds of five, reaching an average Cohen's kappa of 0.88.
  - CORRECTION to the node: it said kappa 0.88 was "built from 150 traces". The 150 traces built the taxonomy; the kappa came from 15 traces.
- LLM annotator: few-shot o1 judge, kappa 0.77 with human experts (94% accuracy); kappa 0.79 on two unseen systems/benchmarks. Average cost about $1.8 per trace, ranging from about $0.37 (AppWorld) to about $4.14 (OpenManus), driven by trace length (Appendix K).
- Interventions (ChatDev, GPT-4o): better role specifications +9.4% success; a high-level objective verification step +15.6% on ProgramDev. The authors say the gains are modest, one topology change was not significant (p = 0.4), and results depend on the base LLM.
- Conclusion: "MAS failure is not merely a function of challenges in the underlying model"; the authors conjecture that better base models alone will not address the full MAST.
- Appendix J: some failure modes (e.g. unaware of termination conditions) occur mainly in failed runs; verification failures also occur in successful runs, so failure counts do not map one-to-one onto outcomes.

## MultiAgentBench (arXiv 2503.01935)
Read: abstract page only. URL: https://arxiv.org/abs/2503.01935
- Evaluates LLM multi-agent systems across interactive scenarios, measuring task completion and collaboration/competition quality with milestone-based KPIs. Tests coordination topologies (star, chain, tree, graph) and strategies (group discussion, cognitive planning).
- Abstract findings: gpt-4o-mini has the highest average task score; graph structure performs best in the research scenario; cognitive planning raises milestone achievement by 3%. Revised v2 on 18 Nov 2026.

## Who&When, automated failure attribution (arXiv 2505.00212)
Read: abstract page only. URL: https://arxiv.org/abs/2505.00212
- Defines automated failure attribution: identifying which agent and which step caused a multi-agent failure. Who&When dataset: failure logs from 127 multi-agent systems annotated with responsible agent and decisive error step.
- Best method: 53.5% accuracy for the responsible agent and 14.2% for the failure step; some methods are below random; o1 and DeepSeek R1 fall short of practical usefulness.

## Anthropic, "How we built our multi-agent research system" (13 Jun 2025, provider)
Read: full post. URL: https://www.anthropic.com/research/multi-agent-research-system
- The evaluation used an LLM judge with a rubric, started from about 20 queries representing real usage, judged the end state rather than the process, and kept manual testing.
- Token usage alone explains 80% of performance variance on their eval. Multi-agent systems use about 15x more tokens than chat (single agents about 4x).
- Multi-agent outperformed single-agent Claude Opus 4 by 90.2% on their internal research eval (provider-reported, internal eval).
- Failure examples: spawning 50 subagents for simple queries; subagents duplicating work. "small changes to the lead agent can unpredictably change how subagents behave."

## Gaps
- MultiAgentBench and Who&When were read at abstract level only. Their metric definitions and annotation protocol were not checked.
- The MAST annotation guidelines and the release status of its LLM-annotator code were not found in the portion read. Check the paper's project link before reusing them.
- Whether MAST category prevalences generalise beyond the 7 frameworks studied is not established. The paper reports framework-dependent distributions.
