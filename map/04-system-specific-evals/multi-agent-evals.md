---
id: multi-agent-evals
title: "Multi-agent system evals"
branch: 04-system-specific-evals
depth: L1
status: not-started
bridge: none
prerequisites: [agent-trajectory-evals]
tags: [agents]
---
# Multi-agent system evals

Evaluating coordination, handoffs, and emergent failures.

_Researched 2026-11-20; full notes in [research/04-system-specific-evals.md](../../research/04-system-specific-evals.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims. Supplemented 2026-11-21: [research/supplements/2026-11-21-multi-agent-evals.md](../../research/supplements/2026-11-21-multi-agent-evals.md). MAST read in full text; MultiAgentBench and Who&When at abstract level._

## Learning objectives
You can:
- Explain the three MAST failure categories (system design, inter-agent misalignment, task verification) with an example failure mode from each.
- Recognise multi-agent failures such as step repetition, duplicated subagent work, over-spawning and premature termination in a trace.
- Explain why attributing a failure to a specific agent and step is hard, and what evidence would justify a multi-agent system over a single-agent baseline.

**Done bar.** Practiced: traces from a 2-3 agent pipeline on 15 tasks annotated with MAST failure modes, with a cost and success comparison against a single-agent baseline. Mastered: written answers to all three mastery questions checked against MAST, Who&When and the Anthropic post, and an explanation, without notes, of the MAST categories and one multi-agent failure mode to someone else.

## Why it matters
- MAST (2025) groups 14 failure modes into 3 categories. It was derived by grounded theory from 150 traces and applied to 1,642 traces from 7 frameworks (MetaGPT, ChatDev, HyperAgent, AppWorld, AG2, Magentic-One, OpenManus). Three annotators reached Cohen's kappa 0.88 on 15 traces ([MAST, arXiv 2503.13657](https://arxiv.org/html/2503.13657)).
- MAST's authors argue that multi-agent failure "is not merely a function of challenges in the underlying model". In their ChatDev case study, better role specifications gave +9.4% success and an objective-verification step gave +15.6%, gains they call modest ([MAST](https://arxiv.org/html/2503.13657)).
- A few-shot LLM annotator agreed with human MAST labels at kappa 0.77, at about $1.8 per trace, so automated failure tagging is feasible but imperfect ([MAST](https://arxiv.org/html/2503.13657)).
- Attribution is hard. On the Who&When dataset (failure logs from 127 systems), the best method found the responsible agent 53.5% of the time and the decisive step only 14.2% (2025, abstract only) ([Who&When, arXiv 2505.00212](https://arxiv.org/abs/2505.00212)).
- MultiAgentBench scores task completion and collaboration or competition quality with milestone KPIs across star, chain, tree and graph topologies; graph performed best in its research scenario (abstract only) ([arXiv 2503.01935](https://arxiv.org/abs/2503.01935)).
- Anthropic (provider) reports that multi-agent systems use about 15x the tokens of chat, judged the end state with an LLM rubric judge, started from about 20 real queries, and found that small lead-agent changes "can unpredictably change how subagents behave" ([Anthropic](https://www.anthropic.com/research/multi-agent-research-system)).

## Common failure modes
These are MAST's names, with prevalence in its dataset ([MAST](https://arxiv.org/html/2503.13657)):
- System design: Disobey task specification (11.8%), Disobey role specification (1.5%), Step repetition (15.7%), Loss of conversation history (2.8%), Unaware of termination conditions (12.4%).
- Inter-agent misalignment: Conversation reset (2.2%), Fail to ask for clarification (6.8%), Task derailment (7.4%), Information withholding (0.85%), Ignored other agent's input (1.9%), Reasoning-action mismatch (13.2%).
- Task verification: Premature termination (6.2%), No or incomplete verification (8.2%), Incorrect verification (9.1%).
- Verification failures also appear in successful runs, so failure counts are not success proxies ([MAST, App. J](https://arxiv.org/html/2503.13657)).
- Over-spawning (50 subagents for a simple query) and duplicated subagent work ([Anthropic](https://www.anthropic.com/research/multi-agent-research-system)).
- Topology-dependent performance ([MultiAgentBench](https://arxiv.org/abs/2503.01935)).

## Practice exercise (4 h)
Run a 2-3 agent pipeline (planner, worker, verifier) on 15 tasks and log the traces. Annotate each failure with a MAST failure mode, using the definitions in the paper. Note where you could not tell which agent or step caused it. Compare cost (tokens) and success against a single-agent baseline.

## Mastery check
1. Single vs multi-agent: what evidence justifies the extra complexity and token cost?
2. Which MAST category is hardest to detect automatically, and why does Who&When suggest step-level attribution is harder than agent-level?
3. Design a handoff test that would catch information withholding or ignored input.

## Sources
- [MAST 2025, Why Do Multi-Agent LLM Systems Fail?, arXiv 2503.13657](https://arxiv.org/html/2503.13657) (full text)
- [Zhang et al. 2025, Which Agent Causes Task Failures and When?, arXiv 2505.00212](https://arxiv.org/abs/2505.00212) (abstract)
- [Zhu et al. 2025, MultiAgentBench, arXiv 2503.01935](https://arxiv.org/abs/2503.01935) (abstract)
- [Anthropic, multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) (provider)
