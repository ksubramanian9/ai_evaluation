# Research supplement: standards

As of: 2026-11-21. Web access: working. Note: www.iso.org returned HTTP 403 to automated fetches, but committee.iso.org served the same catalogue records. All reads are catalogue level (title, status, stage, abstract). No standard text was read; all are paywalled.

## ISO/IEC JTC 1/SC 42 catalogue
Read: full catalogue page. URL: https://committee.iso.org/committee/6794475/x/catalogue/
- Published items relevant to evaluation: TS 4213:2022; 5259-1..5 (2024/2025) and TR 5259-6:2026; 5338:2023; TS 6254:2025; TS 8200:2024; TS 12791:2024; 12792:2025; 22989:2022; 23053:2022; 23894:2023; TR 24027:2021; TR 24028:2020; TR 24029-1:2021; 24029-2:2023; TS 25058:2024; 25059:2023; 38507:2022; 42001:2023; 42005:2025; 42006:2025; TR 42106:2026; TS 42119-2:2025.
- Under development, per the catalogue: 24970 "AI system logging" (stage 60.00); TS 42119-3 "Verification and validation analysis of AI systems" (60.00); 42119-7 "Testing and evaluation, Part 7: Red teaming" (20.00); 42119-8 "Prompt-based text-to-text benchmarking of AI models and AI systems" (20.00); DIS 42007 conformity assessment scheme framework (40.60); DIS 4213 (broader performance measurement); FDIS 25059; AWI 25058; FDIS 24029-3; AWI TR 24028.

## Individual catalogue records (committee.iso.org)
| Standard | Status / stage read | Abstract or summary (catalogue) | URL |
|---|---|---|---|
| ISO/IEC 42001:2023 | Published 2023-12-18, 60.60, Ed. 1, no amendment shown | specifies "requirements for establishing, implementing, maintaining, and continually improving" an AIMS | https://committee.iso.org/standard/42001 |
| ISO/IEC 42005:2025 | Published 2025-05-28, 60.60 | "guidance for organisations conducting AI system impact assessments"; complements 42001, 38507, 23894 | https://committee.iso.org/standard/42005 |
| ISO/IEC 42006:2025 | Published 2025-07-07, 60.60 | requirements for bodies that audit and certify AIMS under 42001; builds on ISO/IEC 17021-1 | https://committee.iso.org/standard/42006 |
| ISO/IEC 23894:2023 | Published 2023-02-06, 60.60 | guidance on risk management for organizations that develop, produce, deploy or use AI | https://committee.iso.org/standard/77304.html |
| ISO/IEC TS 25058:2024 | Published 2024-01-24; now 90.92 "to be revised" (2025-07-28); AWI 25058 replacing | "guidance for evaluation of artificial intelligence (AI) systems using an AI system quality model" | https://committee.iso.org/standard/82570.html |
| ISO/IEC 25059:2023 | Published 2023-06-28; 90.92 "to be revised"; FDIS 25059 replacing | quality model for AI systems, a SQuaRE extension; terminology "for specifying, measuring and evaluating AI system quality" | https://committee.iso.org/standard/80655.html |
| ISO/IEC TS 42119-2:2025 | Published 2025-11-03, 60.60 | requirements and guidance on applying the ISO/IEC/IEEE 29119 series to AI systems; "risk-based approach" | https://committee.iso.org/standard/84127.html |
| ISO/IEC TS 4213:2022 | Published 2022-10-13; confirmed 2025; now 90.92; DIS 4213 replacing ("Performance measurement for AI classification, regression, clustering and recommendation tasks") | "methodologies for measuring classification performance of machine learning models, systems and algorithms" | https://committee.iso.org/standard/79799.html |
| ISO/IEC TR 42106:2026 | Published 2026-07-20, 60.60, 21 pp. | overview of frameworks for "graded benchmarking" of AI system quality characteristics by complexity and context of use | https://committee.iso.org/standard/42106 |
| ISO/IEC TR 29119-11:2020 (SC 7, not SC 42) | Published 2020-11-27; 90.60 close of review 2026-03-05, outcome not shown | guidelines on testing AI-based systems; test oracle problem; black-box and neural-network white-box testing | https://committee.iso.org/standard/79016.html |

This resolves the earlier UNVERIFIED item: 29119-11 exists. It sits under SC 7, which is why it was missing from the SC 42 catalogue.

## EU harmonised standards
- Commission AI Act standardisation page (last updated 19 Oct 2026). Read: full page. URL: https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation
  - Standardisation request C(2025)3871 covers ten areas: risk management, data governance and quality, record keeping, transparency, human oversight, accuracy, robustness, cybersecurity, quality management, conformity assessment.
  - CEN-CENELEC JTC 21 develops them, with an "international first" approach (ISO/IEC SC 42 work can be adopted).
  - Applying standards is voluntary. Applying harmonised standards gives a presumption of compliance.
- Commission Implementing Decision (EU) 2026/2274 of 12 Oct 2026, OJ L 14.10.2026. Read: EUR-Lex record. URL: https://eur-lex.europa.eu/eli/dec_impl/2026/2274/oj
  - Annex cites EN 18286:2026 "Artificial intelligence – Quality management system for EU AI Act regulatory purposes".
  - Responds to the request on quality management systems including post-market monitoring; Art. 40 presumption of conformity.
  - The Commission AI policy page lists the item on 19 Oct 2026. Press coverage uses 19 Oct, but the OJ date is 14 Oct 2026.
- jtc21.eu was unreachable (DNS failure). The JTC 21 work programme was not verified directly.

## IEEE
- IEEE 3129-2023: Robustness Testing and Evaluation of AI-based Image Recognition Service. Active; approved 2023-02-15; published 2023-06-02. Covers test specifications and indicators for common corruptions and adversarial attacks. Read: catalogue page. URL: https://standards.ieee.org/ieee/3129/10747
- IEEE 3168-2024: Robustness Evaluation Test Methods for an NLP Service That Uses Machine Learning. Active; approved 2024-03-21; published 2024-08-09. Read: catalogue page. URL: https://standards.ieee.org/ieee/3168/10923

## NIST
- NIST AI 200-2 ipd, TEVV-Athlon framework: initial public draft announced 7 Aug 2026, comments closed 6 Oct 2026. A four-stage method for building customised assessments from TEVV objectives; covers ML, LLM, multimodal and agentic systems. Read: project page. URL: https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems
- NIST AI Standards "Zero Drafts" pilot (page updated 14 Aug 2026). Covers two topics: documentation (an initial public draft "Guidance and Templates for Public-Facing AI Documentation", Jul 2026) and a TEVV framework (outline only). The drafts are proposals to SDOs and "will likely still change". Read: full page. URL: https://www.nist.gov/artificial-intelligence/nists-ai-standards-zero-drafts-pilot-project-accelerate-standardization
- NIST AI hub page: AI RMF still listed; terminology being changed under EO 14434 (Sept 2026). Read: page. URL: https://www.nist.gov/artificial-intelligence

## Gaps
- No standard's normative text was read. Everything here is catalogue scope or abstract level.
- The ISO 42001 explainer (iso.org/insights) could not be re-fetched (iso.org 403). The "certification voluntary" claim stays as previously sourced via search summary.
- The JTC 21 site was unreachable. AI Act Art. 40 text was not fetched; the presumption of conformity is sourced to the Commission page and the Implementing Decision instead.
- The outcome of the 29119-11 systematic review is unknown.
