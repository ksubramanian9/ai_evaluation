---
id: prompt-injection-security-testing
title: "Prompt injection and security testing"
branch: 05-testing-in-engineering
depth: L3
status: not-started
bridge: testing
prerequisites: [red-teaming]
tags: [safety]
---
# Prompt injection and security testing

Testing for injection, data exfiltration, and tool abuse.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
OWASP Top 10 for LLM Applications 2025 lists LLM01 Prompt Injection first, plus LLM02 Sensitive Information Disclosure, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage ([OWASP GenAI](https://genai.owasp.org/llm-top-10/)). Indirect injection: retrieved data can carry instructions; demonstrated on Bing Chat and code-completion engines, with data theft, worming, and API-call control; "effective mitigations are currently lacking" as of the paper ([Greshake et al., arXiv 2302.12173](https://arxiv.org/abs/2302.12173)). AgentDojo: 97 tasks and 629 security test cases; even without attacks models fail many tasks; attacks break some but not all security properties ([Debenedetti et al., arXiv 2406.13352](https://arxiv.org/abs/2406.13352)). NIST AI 100-2 E2025 (March 2025) is the AML taxonomy and terminology ([NIST CSRC](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)); attack-category details inside the PDF UNVERIFIED (PDF did not parse). Anthropic's guidance separates direct (user adversary) from indirect (untrusted third-party content) injection; recommends untrusted content only in `tool_result`, JSON-encoding it, least privilege, screening tool outputs, and red-teaming your own agent ([Anthropic mitigate jailbreaks](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), as-of 2026-11-20).

## Common failure modes
- Testing only direct jailbreaks; missing indirect injection via emails, web pages, tool output.
- Measuring "model refused" instead of "action not taken" (agent side effects, exfiltration channel).
- Defenses (classifier screens) never tested for bypass; a screen model can itself refuse or be injected (Anthropic notes `stop_reason: "refusal"` handling, [source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)).
- Static attack set: attackers adapt; AgentDojo is designed as a dynamic environment ([arXiv 2406.13352](https://arxiv.org/abs/2406.13352)).
- Over-privileged tools make any success severe.

## Practice exercise
Build a toy email-summarizer agent with 2 tools (read_inbox, send_email). Plant 10 injected emails (exfiltrate secret, send mail to attacker, system prompt leak). Metric: attacker goal achieved (tool call log), not text. Then apply two mitigations (JSON-encode + tool-output screen; least-privilege) and rerun; report ASR before/after plus utility on 20 benign tasks (AgentDojo's utility/security pairing).

## Mastery check
1. Map each OWASP LLM01/LLM06/LLM07 item to a test you wrote.
2. Why report utility alongside ASR?
3. Explain why no defense can be declared "passed" by a finite test set.

## Sources
[OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/); [Greshake](https://arxiv.org/abs/2302.12173); [AgentDojo](https://arxiv.org/abs/2406.13352); [NIST AI 100-2e2025](https://csrc.nist.gov/pubs/ai/100/2/e2025/final); [Anthropic mitigate-jailbreaks](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks); [garak](https://github.com/NVIDIA/garak) (encoding-based prompt injection probes, as-of 2026-11-20).
