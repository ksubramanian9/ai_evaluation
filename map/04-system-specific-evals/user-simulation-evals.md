---
id: user-simulation-evals
title: "User simulation for multi-turn and agent evals"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: none
prerequisites: [conversational-evals, agent-task-success-evals, llm-as-judge]
tags: [agents, llm-judge, human-labels]
---
# User simulation for multi-turn and agent evals

Using an LLM to play the user in multi-turn and agent evals, and validating that simulator against real users before trusting its scores.

_Researched 2026-11-21. Supplemented 2026-11-21: [research/supplements/2026-11-21-user-simulation-evals.md](../../research/supplements/2026-11-21-user-simulation-evals.md). tau-bench and tau2-bench were read at abstract level; the Sim2Real and SimulatorArena numbers were read from the papers' HTML full text (partially). Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** multi-turn quality metrics are owned by [conversational-evals](conversational-evals.md) and outcome grading by [agent-task-success-evals](agent-task-success-evals.md); this node covers the simulated user that drives those conversations.

## Learning objectives
You can:
- Build an LLM user simulator from a task goal, a persona and an information-release policy, and use it to drive an agent eval.
- Validate a simulator against real transcripts on message realism, outcome agreement and agreement of agent rankings.
- Diagnose simulator-induced bias (over-cooperation, verbosity, giving away all information at once) and how it inflates agent scores.
- Design a persona set that covers the user behaviours your product actually sees.

**Done bar.** Practiced: a simulator with at least 5 personas driving 20 tasks against one agent, plus a comparison with at least 10 real or hand-played transcripts that reports message length, turns, agent success rate and a ranking check across two agent variants. Mastered: written answers to all four mastery questions checked against Yao et al., Zhou et al. (Sim2Real) and Dou et al. (SimulatorArena), plus a review of one real simulator-based eval that states whether its simulator was validated and what its scores would likely look like with real users.

## Why it matters
- tau-bench drives tool-agent conversations with an LLM playing the user, grades success by comparing final database state with an annotated goal state, and introduces pass^k for reliability; gpt-4o-class agents succeeded on under 50% of tasks with pass^8 under 25% in retail (2024, [Yao et al., arXiv 2406.12045](https://arxiv.org/abs/2406.12045)).
- tau2-bench extends this to dual control, where the user also acts through tools on shared state; its simulator is constrained by the tools and observable state available to it to improve fidelity, and agents drop sharply when they must guide users (2025, [Barres et al., arXiv 2506.07982](https://arxiv.org/abs/2506.07982)).
- Simulators make agents look better than they are: replacing tau-bench's simulator with 451 real participants over 165 tasks, Zhou et al. found LLM simulators "excessively cooperative, stylistically uniform" and lacking realistic frustration, an "easy mode" in which top simulators gave agent success up to 77.8% against a 63.6% human baseline (2026, [arXiv 2603.11245](https://arxiv.org/abs/2603.11245), HTML read).
- In the same study the best of 31 simulators scored 76.0 on their User-Sim Index against 92.7 for human-human agreement, and a more capable general model was not necessarily a more faithful simulator ([Zhou et al.](https://arxiv.org/abs/2603.11245)).
- Simulator validity can be measured: SimulatorArena uses 909 annotated human-LLM conversations and scores simulators on how closely messages match human behaviour and how well their assistant ratings match human ratings; profile-conditioned simulators reached Spearman rho of about 0.7 (2025, [Dou et al., arXiv 2510.05444](https://arxiv.org/abs/2510.05444)).
- Personas matter: in SimulatorArena, simulators conditioned on user profiles (background, message style) aligned better with humans than vanilla prompting ([Dou et al.](https://arxiv.org/abs/2510.05444)).

## Common failure modes
- Unvalidated simulator: scores are reported as if they were user outcomes without any comparison to real users ([Zhou et al.](https://arxiv.org/abs/2603.11245)).
- Over-cooperative simulator that reveals all task information at once; Zhou et al. recommend discouraging this ([arXiv 2603.11245](https://arxiv.org/abs/2603.11245), HTML read).
- Assistant-style users: zero-shot CoT simulators wrote 89.5 and 123.9 words per message against 15.5 and 32.6 for humans, and were "overly verbose and polite" ([Dou et al., HTML Table 2](https://arxiv.org/html/2510.05444v2)).
- Simulated feedback is uniformly more positive than real users' ratings, so simulator ratings overstate satisfaction ([Zhou et al.](https://arxiv.org/abs/2603.11245)).
- One persona for all tasks, so the eval misses confused, terse, adversarial or frustrated users (design guidance, consistent with the profile results in [Dou et al.](https://arxiv.org/abs/2510.05444)).
- Tuning the simulator on the same human transcripts used to validate it; Zhou et al. recommend separate human conversations for each ([arXiv 2603.11245](https://arxiv.org/abs/2603.11245)).
- Simulator and agent from the same model family, which may share blind spots (design hypothesis, by analogy with judge self-preference in [llm-as-judge](../03-measurement-methods/llm-as-judge.md); UNVERIFIED for simulators).
- Simulator nondeterminism ignored: the simulated user varies between runs, so report pass^k or spread over repeated runs ([Yao et al.](https://arxiv.org/abs/2406.12045)).

## Practice exercise (4 h)
Pick a toy support agent with 2-3 tools and 20 tasks with a goal state. Write a simulator prompt with the task goal, a persona and a rule to reveal information only when asked. Create 5 personas (cooperative, terse, confused, frustrated, changes their mind). Run each task-persona pair 3 times and record success and pass^3. Then collect 10 real transcripts (colleagues or yourself playing the user from the same task cards) and compare against the simulated runs: mean words per user message, turns, success rate, and whether the two agent variants rank the same way. Write one paragraph on how the simulator inflates or deflates scores and one change you would make to it.

## Mastery check
1. What three things would you measure to decide whether a user simulator is a valid stand-in for real users?
2. Why do LLM simulators tend to inflate agent success, and how would you detect it in your own eval?
3. How do you choose a persona set, and how would you show it covers your real traffic?
4. Your simulator agrees with humans on agent rankings but not on absolute success rate. What can you still claim from simulated runs?

## Sources
- [Yao et al. 2024, tau-bench, arXiv 2406.12045](https://arxiv.org/abs/2406.12045)
- [Barres et al. 2025, tau2-bench, arXiv 2506.07982](https://arxiv.org/abs/2506.07982)
- [Zhou et al. 2026, Mind the Sim2Real Gap in User Simulation for Agentic Tasks, arXiv 2603.11245](https://arxiv.org/abs/2603.11245)
- [Dou et al. 2025, SimulatorArena, arXiv 2510.05444](https://arxiv.org/abs/2510.05444)
