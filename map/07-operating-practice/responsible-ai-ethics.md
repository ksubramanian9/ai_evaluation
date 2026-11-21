---
id: responsible-ai-ethics
title: "Responsible AI and ethics"
branch: 07-operating-practice
depth: L1
status: not-started
bridge: none
prerequisites: [fairness-and-bias-testing]
tags: [fairness, safety]
---
# Responsible AI and ethics

Ethical considerations that shape what you choose to evaluate.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Shared concept:** harm measurement is owned by [safety-and-harm-evals](../05-testing-in-engineering/safety-and-harm-evals.md); this node covers what to evaluate and why.

## Learning objectives
You can:
- Explain how ethical principles (e.g. OECD) decide what gets evaluated, and recognise the principle-to-metric gap.
- Identify uncovered harms using a risk taxonomy (Weidinger et al.) as a coverage check, including who bears them.
- Recognise when evaluation procedures themselves need ethics safeguards (consent, compensation, exposure of crowdworkers and red-teamers).

**Done bar.** Practiced: a written mini impact assessment for the capstone listing stakeholders, mapped Weidinger risk areas, the risks deliberately not evaluated with reasons, and one eval or monitor per accepted risk. Mastered: written answers to all three mastery questions checked against the OECD principles, Weidinger et al. and NIST AI 600-1, and an explanation, without notes, of the principle-to-metric gap and one way it fails to someone else.

## Why it matters
- Ethical commitments decide what gets evaluated. OECD AI Principles (2019, updated May 2024): inclusive growth/well-being; human rights and democratic values incl. fairness and privacy; transparency and explainability; robustness, security and safety; accountability ([OECD.AI](https://oecd.ai/en/ai-principles)).
- Weidinger et al. (DeepMind, Dec 2021) taxonomy of 21 risks in six areas: discrimination/exclusion/toxicity; information hazards; misinformation harms; malicious uses; human-computer interaction harms; automation, access and environmental harms. Good source for choosing eval targets ([arXiv 2112.04359](https://arxiv.org/abs/2112.04359)).
- NIST: trustworthiness tradeoffs need traceable measurement; MEASURE 2.2 requires human-subject evaluations to meet protection requirements and be representative; GOVERN 5.1 asks for feedback from those external to the team; AI 600-1 says feedback activities should follow informed consent and compensation ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf); [AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)).
- Corporate example: Microsoft Responsible AI Standard v2 (June 2022): goals of accountability, transparency, fairness, reliability and safety, privacy and security, inclusiveness; Goal A1 impact assessment ([Microsoft PDF](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf), via search summary; text not read directly). Impact assessment ISO/IEC 42005 (see standards).
- EU Act Annex IV explicitly asks for "potentially discriminatory impacts" in test metrics ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)).

## Common failure modes
- Ethics as principles list with no measurable eval (principle-to-metric gap).
- Choosing metrics because they are easy, so harms to affected groups go unmeasured (Weidinger taxonomy as a coverage check).
- Evaluating with crowdworkers/red-teamers without consent, compensation or exposure safeguards (AI 600-1 above).
- Evaluating only majority-user performance.

## Practice exercise (2 h)
Run a mini impact assessment for your app: list affected stakeholders (users, non-users), map to Weidinger risk areas, choose which ones you will not evaluate and write down why, and define one eval or monitor per accepted risk.

## Mastery check
1. Translate one OECD principle into a testable requirement and a metric with threshold.
2. What harms does your eval suite not cover, and who bears them?
3. When do evaluation procedures themselves need ethics review?

## Sources
- [OECD AI Principles](https://oecd.ai/en/ai-principles)
- [Weidinger et al., arXiv 2112.04359](https://arxiv.org/abs/2112.04359)
- [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf); [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [Microsoft Responsible AI Standard v2 (PDF)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf) (corporate practice; read via search summary only)
- [EU AI Act Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)
- UNESCO Recommendation on the Ethics of AI (2021): NOT researched; add if wanted (URL not recorded).
