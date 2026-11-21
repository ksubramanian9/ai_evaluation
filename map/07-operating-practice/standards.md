---
id: standards
title: "Standards"
branch: 07-operating-practice
depth: L1
status: not-started
bridge: none
prerequisites: [risk-and-governance-frameworks]
tags: [safety]
---
# Standards

The kinds of ISO/IEC, IEEE, European and NIST standards that matter for evaluation, and how to use them.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Exercises and mastery checks are proposed designs, not sourced claims. Supplemented 2026-11-21: [research/supplements/2026-11-21-standards.md](../../research/supplements/2026-11-21-standards.md). Existence, status and scope were checked on official catalogue pages. No standard's normative text was read, since all are paywalled. Current status and dates are in [landscape/07-operating-practice.md](../../landscape/07-operating-practice.md)._

## Learning objectives
You can:
- Distinguish management-system standards (42001, 42006) from risk and impact guidance (23894, 42005), quality models and evaluation guidance (25059, 25058) and test or measurement standards (42119 series, 29119-11, TS 4213, IEEE 3129/3168).
- Identify which kind of standard to consult for impact assessment, quality evaluation, testing and performance measurement of AI systems.
- Explain what a 42001 certificate does and does not tell a customer about eval quality, and recognise that only harmonised standards cited in the Official Journal carry presumption of conformity under the EU AI Act.

**Done bar.** Practiced: a catalogue table of evaluation-relevant standards (number, kind, status, scope sentence, eval evidence you could produce), built from the official catalogue pages and noting what you could not verify without purchase. Mastered: written answers to all three mastery questions checked against the catalogue pages and the Implementing Decision, and an explanation, without notes, of the management-system vs tested-system distinction to someone else.

## Why it matters
- **Management systems** certify an organisation's process, not a model. ISO/IEC 42001 specifies requirements for "establishing, implementing, maintaining, and continually improving" an AI management system ([ISO 42001](https://committee.iso.org/standard/42001)). ISO/IEC 42006 sets requirements for the bodies that audit and certify against it ([ISO 42006](https://committee.iso.org/standard/42006)).
- **Risk and impact guidance**: ISO/IEC 23894 gives AI risk-management guidance ([ISO 23894](https://committee.iso.org/standard/77304.html)). ISO/IEC 42005 gives guidance for AI system impact assessments on individuals, groups and society, and complements 42001, 38507 and 23894 ([ISO 42005](https://committee.iso.org/standard/42005)).
- **Quality models and evaluation guidance**: ISO/IEC 25059 is a SQuaRE quality model giving terminology "for specifying, measuring and evaluating AI system quality" ([ISO 25059](https://committee.iso.org/standard/80655.html)). ISO/IEC TS 25058 guides evaluation of AI systems using that model ([ISO TS 25058](https://committee.iso.org/standard/82570.html)).
- **Testing**: ISO/IEC TS 42119-2 applies the ISO/IEC/IEEE 29119 software-testing series to AI with a "risk-based approach" ([ISO TS 42119-2](https://committee.iso.org/standard/84127.html)). The SC 42 catalogue lists further 42119 parts in development, including red teaming and prompt-based text-to-text benchmarking ([SC 42 catalogue](https://committee.iso.org/committee/6794475/x/catalogue/)). ISO/IEC TR 29119-11 (from SC 7, not SC 42) covers testing AI-based systems, centred on the test oracle problem ([ISO TR 29119-11](https://committee.iso.org/standard/79016.html)).
- **Measurement and benchmarking**: ISO/IEC TS 4213 specifies methods for measuring ML classification performance ([ISO TS 4213](https://committee.iso.org/standard/79799.html)). ISO/IEC TR 42106 surveys graded benchmarking of quality characteristics by context of use ([ISO TR 42106](https://committee.iso.org/standard/42106)). IEEE 3129 and IEEE 3168 define robustness test methods for image-recognition and NLP services ([IEEE 3129](https://standards.ieee.org/ieee/3129/10747); [IEEE 3168](https://standards.ieee.org/ieee/3168/10923)).
- **EU harmonised standards**: CEN-CENELEC JTC 21 is drafting standards against a ten-area request that includes accuracy, robustness and record keeping. Applying them is voluntary, but it gives a presumption of compliance ([Commission](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation)). The first cited standard is a quality-management standard, not an evaluation-method standard ([Implementing Decision (EU) 2026/2274](https://eur-lex.europa.eu/eli/dec_impl/2026/2274/oj)).
- **US**: NIST has a draft TEVV framework ([NIST AI 200-2 ipd](https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems)) and "zero drafts" that it says "will likely still change" ([NIST Zero Drafts](https://www.nist.gov/artificial-intelligence/nists-ai-standards-zero-drafts-pilot-project-accelerate-standardization)).

## Common failure modes
- Equating 42001 certification with a tested system: it certifies a management system, not a model's quality (inference from the scope statement).
- Citing a standard from its title or abstract as if you had read its requirements (all content here is catalogue level).
- Assuming ISO conformance gives EU presumption of conformity. Only standards whose references are published in the Official Journal do ([Implementing Decision 2026/2274](https://eur-lex.europa.eu/eli/dec_impl/2026/2274/oj)). AI Act Art. 40 text was not fetched.
- Citing a superseded edition: several entries (25058, 25059, TS 4213) are marked "to be revised", so check the stage code before citing.

## Practice exercise (3 h)
Build a catalogue table (number, kind, status and stage, scope sentence, what evidence an eval team could produce for it) from the SC 42 catalogue, the 29119-11 page and the IEEE pages. Pick two (25058, 42119-2), read their free preview or scope pages, and note what you cannot verify without purchase.

## Mastery check
1. Distinguish management-system standards (42001, 42006) from risk guidance (23894), quality models (25059) and test standards (42119-2).
2. Which standard would you consult for impact assessment vs quality evaluation vs testing vs classification metrics?
3. What can and cannot a 42001 certificate tell a customer about your eval quality?

## Sources
- [ISO/IEC JTC 1/SC 42 catalogue](https://committee.iso.org/committee/6794475/x/catalogue/)
- [ISO/IEC 42001](https://committee.iso.org/standard/42001); [ISO/IEC 42005](https://committee.iso.org/standard/42005); [ISO/IEC 42006](https://committee.iso.org/standard/42006); [ISO/IEC 23894](https://committee.iso.org/standard/77304.html)
- [ISO/IEC 25059](https://committee.iso.org/standard/80655.html); [ISO/IEC TS 25058](https://committee.iso.org/standard/82570.html); [ISO/IEC TS 42119-2](https://committee.iso.org/standard/84127.html); [ISO/IEC TR 29119-11](https://committee.iso.org/standard/79016.html)
- [ISO/IEC TS 4213](https://committee.iso.org/standard/79799.html); [ISO/IEC TR 42106](https://committee.iso.org/standard/42106)
- [IEEE 3129-2023](https://standards.ieee.org/ieee/3129/10747); [IEEE 3168-2024](https://standards.ieee.org/ieee/3168/10923)
- [Commission, AI Act standardisation](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation); [Implementing Decision (EU) 2026/2274](https://eur-lex.europa.eu/eli/dec_impl/2026/2274/oj)
- [NIST TEVV-Athlon (AI 200-2 ipd)](https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems); [NIST Zero Drafts](https://www.nist.gov/artificial-intelligence/nists-ai-standards-zero-drafts-pilot-project-accelerate-standardization)
- (All catalogue level; standard contents not verified.)
