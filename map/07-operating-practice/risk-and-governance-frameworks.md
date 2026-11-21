---
id: risk-and-governance-frameworks
title: "Risk and governance frameworks"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [safety-and-harm-evals]
tags: [safety]
---
# Risk and governance frameworks

NIST AI RMF and similar frameworks (details to verify from primary sources).

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- NIST AI RMF 1.0 (NIST AI 100-1, January 2023) is "intended to be voluntary, rights-preserving, non-sector-specific, and use-case agnostic" ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Part 1 intro). Four functions: GOVERN, MAP, MEASURE, MANAGE ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Part 2 Core).
- It gives evaluation a place in risk management: after MEASURE, "objective, repeatable, or scalable" TEVV processes "are in place, followed, and documented"; measurement "provides a traceable basis to inform management decisions" when trustworthiness characteristics trade off ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), MEASURE intro). TEVV "allows for both mid-course remediation and post-hoc risk management" ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Sec. 2 on lifecycle).
- Directly eval-relevant subcategories: MEASURE 2.1 (test sets, metrics, tools documented), 2.3 (performance measured "for conditions similar to deployment setting(s)"), 2.4 (production monitoring), 2.13 (effectiveness of the TEVV metrics/processes themselves evaluated), MEASURE 4.1 (measurement approaches informed by domain experts and end users), MANAGE 4.1 (post-deployment monitoring plans) ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Tables 3-4).
- Generative AI Profile (NIST AI 600-1, July 2024) lists 12 GAI risks, including Confabulation, Dangerous/Violent/Hateful Content, Data Privacy, Harmful Bias or Homogenization, Human-AI Configuration, Information Integrity, Information Security, Value Chain and Component Integration ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), Sec. 2). It states that current pre-deployment TEVV "may be inadequate, non-systematically applied, or fail to reflect or mismatched to deployment contexts", that human exams/video-game tests "do not guarantee" validity in those domains, and that benchmark-vs-real-world gaps are likely worsened by prompt sensitivity ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), App. A.1.4).
- Suggested actions to map to evals: MS-2.3-001 (baseline benchmark suites when choosing a model for fine-tuning/RAG), MS-2.3-002 (evaluate capability claims "using empirically validated methods"), MS-2.3-003 (share pre-deployment test results with release-approval actors), MP-2.3-005 (regular adversarial testing), MS-2.7-007 (red-teaming), MS-4.2-xxx (field/structured public feedback) ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), Sec. 3 tables).
- Structured public feedback listed: participatory engagement, field testing, AI red-teaming; follow human-subjects practices such as informed consent and compensation ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), App. A.1.5).
- Status: NIST says it expects a formal review of AI RMF "no later than 2028" ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Update Schedule). Whether any revision or successor was issued before 2026-11-20: UNVERIFIED (not searched).
- Other frameworks: ISO/IEC 23894:2023 AI risk-management guidance, Edition 1, Feb 2023, guidance only (not certifiable) ([ISO catalogue](https://www.iso.org/standard/77304.html), via search summary; direct fetch 403; content not verified). OECD AI Principles (adopted 2019, updated May 2024; five value-based principles incl. "Robustness, security and safety", "Accountability") ([OECD.AI](https://oecd.ai/en/ai-principles)).

## Common failure modes
- Treating RMF as a checklist/certification: it is voluntary and use-case agnostic; no conformance mark ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)). Document-only compliance with no actual TEVV (inference from MEASURE 2.13 which asks whether the TEVV itself is effective).
- Using GAI Profile actions without a context profile: AI 600-1 itself says its list is "not exhaustive" and use-case profiles are implementations of the Core ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Sec. 6 Profiles; [AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), App. A).
- Relying on lab benchmarks as evidence of deployment risk (explicitly warned against, A.1.4 above).

## Practice exercise (3 h)
Pick a small LLM app (e.g. a RAG helper). Build a one-page crosswalk: list its top 5 risks from AI 600-1 Sec. 2, and for each name one MAP/MEASURE/MANAGE subcategory and one concrete eval or monitor that would produce evidence (test set, metric, threshold, owner). Mark gaps where no eval exists.

## Mastery check
1. Explain what MEASURE 2.13 asks and why "evaluating the evaluation" matters for LLM judges and benchmarks.
2. Given a risk (confabulation in a support bot), name the GOVERN/MAP/MEASURE/MANAGE artifacts you would expect and which are eval outputs.
3. Why does AI 600-1 say benchmark and exam performance do not establish validity, and what does it propose in addition?

## Sources
- [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) (read in full text)
- [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) (read in full text)
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [ISO/IEC 23894 catalogue entry](https://www.iso.org/standard/77304.html) (catalogue; not verified in content)
