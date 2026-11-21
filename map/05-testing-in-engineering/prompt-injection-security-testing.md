---
id: prompt-injection-security-testing
title: "Prompt injection and security testing"
branch: 05-testing-in-engineering
depth: L3
status: not-started
bridge: testing
prerequisites: [red-teaming]
tags: [safety, security, agents]
---
# Prompt injection and security testing

Testing for injection, data exfiltration, and tool abuse.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims. Supplemented 2026-11-21: [research/supplements/2026-11-21-prompt-injection-security-testing.md](../../research/supplements/2026-11-21-prompt-injection-security-testing.md)._

## Learning objectives
You can:
- Build direct and indirect prompt-injection test cases for a tool-using agent and measure attacker goal achieved from the tool-call log, not the text.
- Report attack success rate alongside utility on benign tasks before and after mitigations.
- Map OWASP LLM01, LLM06 and LLM07 items to concrete tests.
- Critique a security test plan or defense, explaining why no finite test set can show a defense has passed and weighing security against utility.

**Done bar.** Practiced: a toy email-summarizer agent with 10 planted injection emails, ASR measured from the tool-call log before and after two mitigations, and utility on 20 benign tasks. Mastered: written answers to all three mastery questions checked against OWASP, Greshake et al. and AgentDojo, plus a security review of a real agent (yours or a team's) that finds a gap this node covers (indirect injection, refusal-only metrics, untested screens, over-privileged tools) and states the utility trade-off of the fix.

## Why it matters
- OWASP Top 10 for LLM Applications 2025 lists LLM01 Prompt Injection first, plus LLM02 Sensitive Information Disclosure, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage ([OWASP GenAI](https://genai.owasp.org/llm-top-10/)).
- Indirect injection: retrieved data can carry instructions; demonstrated on Bing Chat and code-completion engines, with data theft, worming, and API-call control; "effective mitigations are currently lacking" as of the paper ([Greshake et al., arXiv 2302.12173](https://arxiv.org/abs/2302.12173)).
- AgentDojo: 97 tasks and 629 security test cases; even without attacks models fail many tasks; attacks break some but not all security properties ([Debenedetti et al., arXiv 2406.13352](https://arxiv.org/abs/2406.13352)).
- NIST AI 100-2 E2025 (March 2025) is the AML taxonomy and terminology ([NIST CSRC](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)); attack-category details inside the PDF UNVERIFIED (PDF did not parse).
- Anthropic's guidance separates direct (user adversary) from indirect (untrusted third-party content) injection; recommends untrusted content only in `tool_result`, JSON-encoding it, least privilege, screening tool outputs, and red-teaming your own agent ([Anthropic mitigate jailbreaks](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), as-of 2026-11-20).

### Indirect prompt injection
- Delivery vectors to test, per Greshake et al. Section 3.1: passive (planted in content the system retrieves, such as web pages or code repositories), active (sent to the system, such as an email an assistant will process), user-driven (the user is tricked into pasting it) and hidden (encoded, multi-stage or in images to evade detection) ([Greshake et al., HTML full text](https://arxiv.org/html/2302.12173), read 2026-11-21).
- Their threat taxonomy gives test goals beyond "follow my instruction": information gathering (exfiltration), fraud, intrusion (backdoor into connected systems), malware (self-spreading prompts), manipulated content (altered summaries or search results) and availability (denial of service) ([Greshake et al., Section 3.2](https://arxiv.org/html/2302.12173)).
- RAG pipelines are an injection surface: any retrieved document is attacker-controllable text if the corpus includes web or user content (passive vector above; design inference from [Greshake et al.](https://arxiv.org/html/2302.12173)).
- Tool results are the main channel for agents: InjecAgent embeds attacker instructions in content returned by tools (emails, websites) and covers 1,054 cases over 17 user tools and 62 attacker tools, split into direct harm and private-data exfiltration ([Zhan et al. 2024, arXiv 2403.02691](https://arxiv.org/abs/2403.02691), abstract only).
- InjecAgent reports ReAct-prompted GPT-4 attacked successfully 24% of the time, and adding a "hacking prompt" to the injection nearly doubled that (2024 paper result; [arXiv 2403.02691](https://arxiv.org/abs/2403.02691), abstract only).
- AgentDojo pairs injection test cases with benign utility tasks in the same tool environment, so a defense can be scored on both security and utility ([Debenedetti et al., arXiv 2406.13352](https://arxiv.org/abs/2406.13352), abstract only).

## Common failure modes
- Testing only direct jailbreaks; missing indirect injection via emails, web pages, tool output.
- Measuring "model refused" instead of "action not taken" (agent side effects, exfiltration channel).
- Defenses (classifier screens) never tested for bypass; a screen model can itself refuse or be injected (Anthropic notes `stop_reason: "refusal"` handling, [source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)).
- Static attack set: attackers adapt; AgentDojo is designed as a dynamic environment ([arXiv 2406.13352](https://arxiv.org/abs/2406.13352)).
- Over-privileged tools make any success severe.

## Practice exercise (4 h)
Build a toy email-summarizer agent with 2 tools (read_inbox, send_email). Plant 10 injected emails (exfiltrate secret, send mail to attacker, system prompt leak). Metric: attacker goal achieved (tool call log), not text. Then apply two mitigations (JSON-encode + tool-output screen; least-privilege) and rerun; report ASR before/after plus utility on 20 benign tasks (AgentDojo's utility/security pairing).

## Mastery check
1. Map each OWASP LLM01/LLM06/LLM07 item to a test you wrote.
2. Why report utility alongside ASR?
3. Explain why no defense can be declared "passed" by a finite test set.

## Sources
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [Greshake et al., arXiv 2302.12173](https://arxiv.org/abs/2302.12173)
- [AgentDojo, arXiv 2406.13352](https://arxiv.org/abs/2406.13352)
- [InjecAgent, Zhan et al. 2024, arXiv 2403.02691](https://arxiv.org/abs/2403.02691)
- [NIST AI 100-2 E2025](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)
- [Anthropic docs: mitigate jailbreaks](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
- practitioner: [garak](https://github.com/NVIDIA/garak) (encoding-based prompt injection probes, as-of 2026-11-20)
