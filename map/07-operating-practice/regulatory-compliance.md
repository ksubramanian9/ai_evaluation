---
id: regulatory-compliance
title: "Regulatory compliance"
branch: 07-operating-practice
depth: L1
status: not-started
bridge: none
prerequisites: [risk-and-governance-frameworks]
tags: [safety]
---
# Regulatory compliance

EU AI Act and other regulation as they affect testing and documentation obligations.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Explain the durable testing and documentation obligations that affect evals: testing against prior defined metrics and thresholds (Art. 9), Annex IV test documentation with group-level metrics and dated, signed logs, lifetime monitoring (Art. 72), and evaluation duties for GPAI with systemic risk (Art. 55).
- Recognise that obligations depend on role (provider, deployer, downstream modifier) and risk class, and that jurisdictions diverge.
- Explain why application dates must be checked against current primary pages and the landscape entry, with an as-of date, rather than taken from a node.

**Done bar.** Practiced: a written role and risk-class decision for the capstone plus a table mapping each applicable obligation (Art. 9, Annex IV 2(g), Art. 72) to an existing eval artifact, with gaps flagged and the date status was checked. Mastered: written answers to all four mastery questions checked against the Service Desk article pages and the Commission page (with current dates looked up and as-of recorded), and an explanation, without notes, of the provider-vs-deployer failure mode to someone else.

## Why it matters
- The EU AI Act is Regulation (EU) 2024/1689 (official text not fetched: [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)). It has been amended since adoption, so application dates move: current dates, the 2026 "AI Omnibus" amendment, Art. 50 timing, GPAI guidance and US state laws are tracked in [landscape/07-operating-practice.md](../../landscape/07-operating-practice.md), with the checks behind them in the [research notes](../../research/07-operating-practice.md#regulatory-compliance-verification-log-2026-11-20).
- Testing/documentation obligations that matter for evals (Service Desk text; verify vs OJ):
  - Art. 9(6)-(8): high-risk systems "shall be tested for the purpose of identifying the most appropriate and targeted risk management measures"; testing "at any time throughout the development process" and before placing on market, "against prior defined metrics and probabilistic thresholds" ([Art. 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9)).
  - Annex IV 2(g): technical documentation includes validation/testing procedures and data, metrics for accuracy, robustness, compliance incl. "potentially discriminatory impacts", and dated, signed test logs and reports; point 3: accuracy "for specific persons or groups of persons"; point 4: appropriateness of performance metrics ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)).
  - Art. 72: providers must "actively and systematically collect, document and analyse" performance data over the lifetime; the monitoring plan is part of the Annex IV documentation; Commission template due by 2 Sept 2027 ([Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72)).
  - Art. 55(1): GPAI with systemic risk must perform model evaluation "in accordance with standardised protocols and tools reflecting the state of the art", including documented adversarial testing, and report serious incidents to the AI Office ([Art. 55](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-55)). Art. 51(2): presumption of systemic risk above 10^25 training FLOP ([Art. 51](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-51)).
  - Art. 15 (accuracy/robustness/cybersecurity), Art. 53 (GPAI documentation), Art. 4 (AI literacy), Art. 50: text not fetched (429/time). UNVERIFIED.
  - Penalties Art. 99: up to EUR 35M / 7% (prohibited practices), EUR 15M / 3% (other operator obligations), EUR 7.5M / 1% (misleading information), higher of the two for undertakings ([Art. 99](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99)).
- Obligations depend on your role (provider, deployer, downstream modifier) and on risk class: GPAI duties attach to model providers, high-risk duties to the Annex III use case ([GPAI scope guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act); detail UNVERIFIED).
- Jurisdictions diverge: US states legislate separately, e.g. Colorado's automated decision-making law, which has already been repealed and re-enacted once ([Colorado SB 26-189](https://leg.colorado.gov/bills/sb26-189)).

## Common failure modes
- Using outdated application dates in plans (the 2026 omnibus moved Annex III high-risk from August 2026 to December 2027); re-check the landscape entry and the Commission page before relying on any date.
- Assuming a model provider's compliance covers the deployer's duties; role (provider vs deployer vs downstream modifier) decides obligations (GPAI scope guidelines above; detail UNVERIFIED).
- Treating internal eval logs as compliance evidence without dated sign-off, pre-defined thresholds and group-level metrics (Art. 9(8), Annex IV above).
- Assuming a high-risk classification absent from a generic LLM app; classification depends on Annex III use case ([Annex III page](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3), not read in detail).

## Practice exercise (3 h)
Take your capstone app. (1) Decide role and risk class using the Commission page and Annex III. (2) Build a table mapping each applicable obligation (Art. 9, Annex IV 2(g), Art. 72) to an eval artifact you already produce, with missing items flagged. (3) Record the date you checked status.

## Mastery check
1. Find the current application dates for prohibitions, GPAI, Annex III and Annex I high-risk from the primary pages, record your as-of date, and explain why a node should not hard-code them.
2. What must a high-risk test report contain under Annex IV, and why do "prior defined metrics and thresholds" matter for how you write eval acceptance criteria?
3. When does a model fall under Art. 55 evaluation duties, and what does adversarial testing there require?
4. Why can a company be compliant under the EU Act yet affected differently by US state law (Colorado example)?

## Sources
- [Commission, AI Act policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) (as-of page update 2026-10-19)
- EU AI Act articles via Service Desk: [Art. 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9), [Art. 51](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-51), [Art. 55](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-55), [Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72), [Art. 99](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99), [Art. 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113), [Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)
- [EUR-Lex, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) (official text; not fetched)
- [Commission, GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)
- [Commission, GPAI scope guidelines](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act)
- [Colorado SB 26-189](https://leg.colorado.gov/bills/sb26-189)
