---
id: standards
title: "Standards"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [risk-and-governance-frameworks]
tags: []
---
# Standards

ISO/IEC and other AI standards relevant to evaluation (to verify from primary sources).

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- ISO/IEC 42001:2023, Edition 1, published 2023-12, stage 60.60; requirements for establishing, implementing, maintaining and continually improving an AI management system (AIMS); no amendments listed ([ISO via committee.iso.org](https://committee.iso.org/standard/42001)). Certification voluntary ([ISO explainer](https://www.iso.org/insights/iso-42001-explained), via search summary). Annex A control count (38 controls/9 objectives) from a third-party paper only: UNVERIFIED. Standard text paywalled; content NOT verified.
- ISO/IEC 42005:2025 (AI system impact assessment), Edition 1, May 2025 (lifecycle log 2025-05-28), published; designed to be used with 42001, 38507, 23894 ([ISO via committee.iso.org](https://committee.iso.org/standard/42005)).
- Other catalogue entries relevant to evaluation, per the SC 42 catalogue ([ISO/IEC JTC 1/SC 42 catalogue](https://committee.iso.org/committee/6794475/x/catalogue/)): ISO/IEC TS 25058:2024 (guidance for quality evaluation of AI systems); ISO/IEC 25059:2023 (quality model for AI systems); ISO/IEC TS 42119-2:2025 (overview of testing AI systems); ISO/IEC 42006:2025 (requirements for bodies auditing/certifying AIMS); ISO/IEC 5259-1..5:2024/2025 (data quality); ISO/IEC TR 24027:2021 (bias); ISO/IEC TS 12791:2024 (unwanted bias in classification/regression); ISO/IEC TR 24029-1:2021 and 24029-2:2023 (robustness); ISO/IEC TR 24028:2020 (trustworthiness); ISO/IEC 23894:2023 (risk). As of the catalogue read, no 42001 amendment published. ISO/IEC 29119-11 (testing AI-based systems) was not on the page: UNVERIFIED either way.
- Link to EU law: the Commission page notes a first harmonised standard supporting the AI Act published 19 Oct 2026 ([Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)); which standard: UNVERIFIED.

## Common failure modes
- Equating 42001 certification with a tested system: it certifies a management system, not a model's quality (inference from scope statement above; scope text only).
- Citing a standard from titles without reading it (all content here UNVERIFIED).
- Assuming ISO conformance gives EU AI Act presumption of conformity; only harmonised standards cited in the OJ do (general EU law principle; AI Act Art. 40 text not fetched: UNVERIFIED).

## Practice exercise
Build a catalogue table (number, title, year, status, purchasable price, what evidence an eval team could produce for it) from the SC 42 catalogue; pick two (25058, 42119-2) and read the free preview/scope pages; note what you cannot verify without purchase.

## Mastery check
1. Distinguish management-system standards (42001, 42006) from guidance (23894, 25058) and from quality models (25059).
2. Which standard would you consult for impact assessment vs quality evaluation vs testing AI?
3. What can and cannot a 42001 certificate tell a customer about your eval quality?

## Sources
- https://committee.iso.org/standard/42001 ; https://committee.iso.org/standard/42005 ; https://committee.iso.org/committee/6794475/x/catalogue/
- https://www.iso.org/standard/77304.html (23894 catalogue)
- https://www.iso.org/insights/iso-42001-explained
(All catalogue-level; standard contents not verified.)
