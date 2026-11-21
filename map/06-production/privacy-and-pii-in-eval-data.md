---
id: privacy-and-pii-in-eval-data
title: "Privacy and PII in eval data"
branch: 06-production
depth: L2
status: not-started
bridge: none
prerequisites: [traffic-sampling-and-logging, golden-datasets]
tags: [privacy, llm-judge]
---
# Privacy and PII in eval data

Handling personal data in golden sets, traces and logs: redaction, pseudonymisation, retention, purpose limits and third-party judges.

_Researched 2026-11-21. Supplemented 2026-11-21: [research/supplements/2026-11-21-privacy-and-pii-in-eval-data.md](../../research/supplements/2026-11-21-privacy-and-pii-in-eval-data.md). GDPR claims are from the official EUR-Lex text; EDPB claims are from the executive summaries of the documents. Paper claims were read at abstract level. This is the GDPR framing only and is not legal advice; dated regulatory status and vendor retention terms live in [landscape/06-production.md](../../landscape/06-production.md). Exercises and mastery checks are proposed designs, not sourced claims._

**Owns:** privacy handling of eval data (golden sets, traces, judge calls); see also [traffic-sampling-and-logging](traffic-sampling-and-logging.md) (what to log), [feedback-loop-to-datasets](feedback-loop-to-datasets.md), [regulatory-compliance](../07-operating-practice/regulatory-compliance.md).

## Learning objectives
You can:
- Find personal data in an eval set or trace sample, and choose between deletion, redaction, pseudonymisation and synthetic replacement for each field.
- Explain why pseudonymised eval data is still personal data under GDPR, and what that means for retention and access.
- Decide whether production data may be sent to a third-party judge, and list the checks (purpose, processor terms, retention, minimisation) before doing so.
- State the limits of synthetic data as a privacy fix.

**Done bar.** Practiced: a PII inventory of 50 real or realistic traces with a per-field decision (drop, redact, pseudonymise, keep), a detector run (e.g. Presidio) with its misses counted by hand, and a one-page retention and judge-routing rule. Mastered: written answers to all four mastery-check questions, checked against GDPR Arts. 4, 5, 6(4), 25 and 28, EDPB Guidelines 01/2025 and Opinion 28/2024, Stadler et al. and Carlini et al., plus that rule applied to a capstone or real eval pipeline with what changed recorded.

## Why it matters
- Eval data drawn from production is personal data whenever it relates to "an identified or identifiable natural person" ([GDPR Art. 4(1), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)).
- Data must be "collected for specified, explicit and legitimate purposes" and not further processed incompatibly; reusing support chats as a golden set is a new purpose that needs an Art. 6(4) compatibility check, where pseudonymisation and encryption count as safeguards ([GDPR Arts. 5(1)(b), 6(4)(e), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)).
- Minimisation ("limited to what is necessary") and storage limitation (identifiable "for no longer than is necessary") apply to golden sets and trace stores as much as to logs ([GDPR Art. 5(1)(c), (e), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)).
- Pseudonymisation means data can no longer be attributed to a person "without the use of additional information" kept separately ([GDPR Art. 4(5), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)), and Art. 25 names it as a data-protection-by-design measure ([GDPR Art. 25(1)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)).
- Pseudonymised data is still personal data, even when the key is held by someone else; erasing the key makes it anonymous only if the conditions for anonymity are met ([EDPB Guidelines 01/2025, executive summary](https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf)).
- The EDPB says pseudonymisation can reduce risk and help establish compatibility of further processing, but "alone will normally not be a sufficient measure" ([EDPB Guidelines 01/2025, executive summary](https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf)).
- Only anonymous information falls outside data protection rules ([GDPR Recital 26, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)).
- Sending eval data to an external judge or eval vendor usually makes them a processor: the controller "shall use only processors providing sufficient guarantees", under a contract ([GDPR Art. 28(1), (3), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)). Vendor retention defaults differ and change; see the landscape file.
- Automated PII detection is incomplete: Presidio states "there is no guarantee that Presidio will find all sensitive information" and advises additional protections ([Presidio docs](https://presidio.dataprivacystack.org/)).
- Synthetic data is not automatically private: across state-of-the-art generators it either failed to stop inference attacks or lost utility, with a privacy-utility trade-off that is "hard to predict" ([Stadler et al., abstract](https://arxiv.org/abs/2011.07018)).
- Models can memorise and emit rare training text, including names, phone numbers and emails seen in a single document ([Carlini et al. 2020, abstract](https://arxiv.org/abs/2012.07805)); the EDPB treats a model as anonymous only if extraction and query leakage of personal data are insignificant ([EDPB Opinion 28/2024, executive summary](https://edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf)). Inference for eval practice: synthetic eval items generated by a model fine-tuned on production data can leak that data.

## Common failure modes
- Copying raw production traces into a golden set "for now" with no purpose check, owner or retention date ([GDPR Art. 5(1)(b), (e)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)).
- Treating pseudonymised or hashed identifiers as anonymous and dropping access controls ([EDPB Guidelines 01/2025](https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf)).
- Trusting a PII detector without measuring its misses, especially in free text and non-English text ([Presidio docs](https://presidio.dataprivacystack.org/)).
- Redacting so aggressively that the eval no longer tests the behaviour (e.g. an address-extraction task with every address removed); replace with realistic surrogates instead (proposed practice).
- Routing production data to a third-party judge without processor terms or knowing its retention ([GDPR Art. 28](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)).
- Deleting a user's data from the trace store but not from golden sets, judge caches and exported eval reports derived from it (proposed check).
- Assuming synthetic data solves privacy without testing for leakage of real records ([Stadler et al.](https://arxiv.org/abs/2011.07018)).

## Practice exercise (3 h)
Take 50 traces from your capstone (or realistic fabricated ones with seeded PII: names, emails, phone numbers, addresses, account ids). List every field and free-text span that is personal data. Run a PII detector and count by hand what it missed. For each field decide drop, redact, pseudonymise (keyed, key stored separately) or keep, and justify against minimisation. Write a one-page rule: who may read raw traces, how long each store keeps data, which judge models may see unredacted text, and what happens on a deletion request. Rerun one eval on the redacted set and note any score change.

## Mastery check
1. Your golden set uses salted hashes for user ids. Is it anonymous data? What follows for retention and access?
2. What must be true before you send production conversations to an external LLM judge?
3. When does redaction break an eval, and what would you do instead?
4. Why is a synthetic copy of production data not automatically safe to share?

## Sources
- [GDPR, Regulation (EU) 2016/679, official text, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
- [EDPB Guidelines 01/2025 on Pseudonymisation (public consultation version)](https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf)
- [EDPB Opinion 28/2024 on AI models](https://edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf)
- [Microsoft Presidio docs](https://presidio.dataprivacystack.org/)
- [Stadler, Oprisanu, Troncoso, Synthetic Data: Anonymisation Groundhog Day](https://arxiv.org/abs/2011.07018)
- [Carlini et al. 2020, Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805)
