---
id: regulatory-compliance
title: "Regulatory compliance"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [risk-and-governance-frameworks]
tags: [safety]
---
# Regulatory compliance

EU AI Act and other regulation as they affect testing and documentation obligations.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
(status as-of 2026-11-20)
- EU AI Act = Regulation (EU) 2024/1689 (EUR-Lex CELEX 32024R1689; official text not fetched: [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)).
- Timeline per Commission page (last updated 19 Oct 2026): in force 1 Aug 2024; prohibitions + AI literacy from 2 Feb 2025; GPAI obligations and governance from 2 Aug 2025; general application 2 Aug 2026 with AI Office enforcement powers over GPAI; high-risk Annex III moved to 2 Dec 2027; Annex I (products) to 2 Aug 2028; new prohibition 9 (non-consensual sexual content/CSAM generation) from Dec 2026 ([Commission AI Act policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)).
- CHANGED: the "AI Omnibus" amended the Act. Per the Commission it was proposed 19 Nov 2025, politically agreed 7 May 2026, in force 27 July 2026 ([Commission page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)). Service Desk Article 113 shows para (a), (c) amended and (d) new, and Art 5(1)(ba),(bb),(1a),(1b) applying from 2 Dec 2026 ([Art. 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113)). The regulation number of the omnibus (reported by search results as 2026/1744, OJ publication 24 July 2026) is UNVERIFIED from primary sources (only law-firm summaries; EUR-Lex blocked).
- Transparency (Art. 50) timing: Commission page says "August 2026"; whether the omnibus altered any Art. 50 date is UNVERIFIED (one secondary source says not delayed). Re-check before relying.
- Testing/documentation obligations that matter for evals (Service Desk text; verify vs OJ):
  - Art. 9(6)-(8): high-risk systems "shall be tested for the purpose of identifying the most appropriate and targeted risk management measures"; testing "at any time throughout the development process" and before placing on market, "against prior defined metrics and probabilistic thresholds" ([Art. 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9)).
  - Annex IV 2(g): technical documentation includes validation/testing procedures and data, metrics for accuracy, robustness, compliance incl. "potentially discriminatory impacts", and dated, signed test logs and reports; point 3: accuracy "for specific persons or groups of persons"; point 4: appropriateness of performance metrics ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)).
  - Art. 72: providers must "actively and systematically collect, document and analyse" performance data over the lifetime; the monitoring plan is part of the Annex IV documentation; Commission template due by 2 Sept 2027 ([Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72)).
  - Art. 55(1): GPAI with systemic risk must perform model evaluation "in accordance with standardised protocols and tools reflecting the state of the art", including documented adversarial testing, and report serious incidents to the AI Office ([Art. 55](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-55)). Art. 51(2): presumption of systemic risk above 10^25 training FLOP ([Art. 51](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-51)).
  - Art. 15 (accuracy/robustness/cybersecurity), Art. 53 (GPAI documentation), Art. 4 (AI literacy), Art. 50: text not fetched (429/time). UNVERIFIED.
  - Penalties Art. 99: up to EUR 35M / 7% (prohibited practices), EUR 15M / 3% (other operator obligations), EUR 7.5M / 1% (misleading information), higher of the two for undertakings ([Art. 99](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99)).
- GPAI guidance: Commission guidelines on scope of GPAI obligations published 18 July 2025, page updated 20 Apr 2026 ([Commission](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act)); voluntary GPAI Code of Practice published 10 July 2025 with Transparency, Copyright, Safety & Security chapters and a Model Documentation Form; signatories incl. Anthropic, Google, OpenAI, Microsoft, Mistral; xAI signed only Safety & Security (page updated 7 Oct 2026) ([Commission](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)). Commission page also reports a first harmonised standard published 19 Oct 2026 (title not verified) ([Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)).
- US state example: Colorado SB 24-205 was repealed and re-enacted by SB 26-189 ("Automated Decision-Making Technology"), signed 14 May 2026, with developer documentation requirements from 1 Jan 2027 ([Colorado General Assembly](https://leg.colorado.gov/bills/sb26-189)). Earlier delay to 30 June 2026 and a court-ordered enforcement pause are from secondary sources only (UNVERIFIED).

## Common failure modes
- Using pre-omnibus dates (2 Aug 2026 for high-risk) in plans.
- Assuming a model provider's compliance covers the deployer's duties; role (provider vs deployer vs downstream modifier) decides obligations (GPAI scope guidelines above; detail UNVERIFIED).
- Treating internal eval logs as compliance evidence without dated sign-off, pre-defined thresholds and group-level metrics (Art. 9(8), Annex IV above).
- Assuming a high-risk classification absent from a generic LLM app; classification depends on Annex III use case ([Annex III page](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3), not read in detail).

## Practice exercise (3 h)
Take your capstone app. (1) Decide role and risk class using the Commission page and Annex III. (2) Build a table mapping each applicable obligation (Art. 9, Annex IV 2(g), Art. 72) to an eval artifact you already produce, with missing items flagged. (3) Record the date you checked status.

## Mastery check
1. State current application dates for prohibitions, GPAI, Annex III and Annex I high-risk, and what changed in 2026.
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

## Verification log (2026-11-20)
Checked against official pages by a follow-up pass. The EUR-Lex Official Journal text could not be read (empty response), so article wording remains unverified.
- **Confirmed from the Commission's official pages** ([news](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), [policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [transparency quick facts](https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems)): the omnibus enters into force on 27 July 2026; Annex III high-risk rules apply from 2 December 2027; Annex I product rules from 2 August 2028; a new prohibition (nudification / non-consensual sexual content and CSAM generation) applies from "December 2026".
- **Art. 50:** the general transparency application date stays 2 August 2026. A grace period until December 2026 applies to the Art. 50(2) marking obligation for generative AI systems placed on the market before 2 August 2026.
- **Still unverified:** the regulation number 2026/1744 (the Commission news page links the text as `OJ:L_202601744`, which is consistent but not a statement of the number); the Official Journal publication date (secondary law-firm sources say 24 July 2026); the exact day "2 December 2026" for the new prohibition (the Commission policy page says only "December 2026").
- **Colorado SB 26-189** ([official bill page](https://leg.colorado.gov/bills/sb26-189)): the bill history shows "Governor Signed" on 05/14/2026. The staff summary says it repeals and reenacts the 2024 act, is enforced by the attorney general under the Consumer Protection Act, creates no new private right of action, and requires a 60-day cure notice before actions begun before 1 January 2030. Developer documentation applies from 1 January 2027. The statute's own effective-date and repeal clauses were not read, and the earlier delay and court-ordered pause remain secondary-source claims.
