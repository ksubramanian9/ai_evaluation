---
id: runtime-guardrails
title: "Runtime guardrails and monitoring"
branch: 06-production
depth: L2
status: not-started
bridge: testing
prerequisites: [safety-and-harm-evals]
tags: [safety]
---
# Runtime guardrails and monitoring

Input/output filters and live monitors, and how to evaluate them.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Llama Guard: an LLM-based classifier for both prompts and responses with a customisable risk taxonomy; reported matching or exceeding moderation baselines on OpenAI Mod and ToxicChat ([arXiv 2312.06674](https://arxiv.org/abs/2312.06674)). [vol]
- NeMo Guardrails: programmable, user-defined, LLM-independent rails (EMNLP 2023 demo) ([arXiv 2310.10501](https://arxiv.org/abs/2310.10501)).
- Constitutional Classifiers: 3,000+ hours of red teaming found no universal jailbreak for an early version; cost was +0.38% absolute refusals on production traffic and 23.7% inference overhead ([arXiv 2501.18837](https://arxiv.org/abs/2501.18837)). Shows guardrails must be evaluated on both attack-success and over-refusal/overhead.
- Liability context: a Canadian tribunal held Air Canada liable for its chatbot's misinformation (Moffatt v. Air Canada, 2024 BCCRT 149) ([decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do), found via search; summary at [ABA](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/), not fetched directly).

## Common failure modes
- Over-refusal (false positives) and latency/compute cost (Constitutional Classifiers numbers above).
- Taxonomy mismatch: a guard trained on one policy used with another; Llama Guard supports adapting taxonomy via prompting ([2312.06674](https://arxiv.org/abs/2312.06674)).
- Benchmark-only evaluation: red teamers vs automated held-out jailbreaks both used in the classifier paper ([2501.18837](https://arxiv.org/abs/2501.18837)).
- Guard evaluated in isolation but not in the full pipeline (streaming, tools): UNVERIFIED.

## Practice exercise
(design)
- Run an open guard model (e.g. Llama Guard) or a moderation API over a small labelled mix: 100 harmful and 300 benign-but-edgy prompts from public safety benchmarks. Report recall, false-positive rate, per-category confusion and latency; sweep the decision threshold and plot a precision-recall curve; pick the threshold for a stated cost ratio.

## Mastery check
1. What two error rates must a guardrail report, and why is the benign set as important as the attack set?
2. How would you monitor a live guardrail for drift (block rate over time, sampled review)?
3. Input vs output rails: what does each catch that the other cannot?

## Sources
- [Llama Guard](https://arxiv.org/abs/2312.06674)
- [NeMo Guardrails](https://arxiv.org/abs/2310.10501)
- [Constitutional Classifiers](https://arxiv.org/abs/2501.18837)
- [Moffatt v. Air Canada decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do)
