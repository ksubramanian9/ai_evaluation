# Research supplement: prompt-injection-security-testing

As-of: 2026-11-21. Web access: WebFetch and WebSearch working. Adds the "Indirect prompt injection" subsection.

- Greshake et al. 2023, "Not what you've signed up for" (arXiv 2302.12173). Section 3.1 delivery methods: passive ("rely on retrieval to deliver injections", web pages, code repos), active (e.g. email processed by assistant), user-driven (user tricked into entering prompt), hidden (multi-stage, images, encoding). Section 3.2 threats: information gathering, fraud, intrusion, malware ("prompts themselves can now act as malware"), manipulated content, availability (DoS). https://arxiv.org/html/2302.12173 (HTML full text, first ~100k chars; PDF did not parse)
- Zhan, Liang, Ying, Kang 2024, "InjecAgent" (ACL 2024 Findings). 1,054 test cases, 17 user tools, 62 attacker tools; intents: direct harm, data exfiltration; 30 agents; ReAct GPT-4 attacked 24%; hacking-prompt reinforcement nearly doubles ASR. https://arxiv.org/abs/2403.02691 (abstract)
- AgentDojo (arXiv 2406.13352) already cited in node; utility/security pairing restated from abstract.

## Gaps
- RAG-as-injection-surface bullet is design inference from Greshake's passive vector, labelled as such.
- AgentDojo and InjecAgent full texts not read.
