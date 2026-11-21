# Research supplement: privacy-and-pii-in-eval-data

As-of: 2026-11-21. All sources fetched in this session. This is not legal advice; it records what the texts say.

## GDPR (official text, EUR-Lex)

Source: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng (read in three chunks covering recitals to ~Article 35; read via WebFetch summaries with quoted phrases, so wording below is as returned by the tool).

- Recital 26: data protection principles apply to information about an identified or identifiable natural person; pseudonymised personal data are information about an identifiable person; "The principles of data protection should therefore not apply to anonymous information."
- Art. 4(1): personal data "means any information relating to an identified or identifiable natural person".
- Art. 4(5): pseudonymisation means data "can no longer be attributed to a specific data subject without the use of additional information", which is kept separately under technical and organisational measures.
- Art. 5(1)(b) purpose limitation: "collected for specified, explicit and legitimate purposes" and not further processed incompatibly.
- Art. 5(1)(c) minimisation: "adequate, relevant and limited to what is necessary".
- Art. 5(1)(e) storage limitation: kept identifiable "for no longer than is necessary".
- Art. 6(4): compatibility test for processing for a purpose other than collection; factor (e) "the existence of appropriate safeguards, which may include encryption or pseudonymisation".
- Art. 25(1): data protection by design, measures "such as pseudonymisation"; Art. 25(2) by default only necessary data processed for each specific purpose.
- Art. 28(1): "the controller shall use only processors providing sufficient guarantees"; Art. 28(3) processing by a processor "shall be governed by a contract or other legal act".
- Art. 35(1): DPIA required where processing "is likely to result in a high risk to the rights and freedoms of natural persons".

## EDPB

- Guidelines 01/2025 on Pseudonymisation, "Adopted on 16 January 2025", "version for public consultation" (consultation 17 Jan to 14 Mar 2025). Executive summary read in full text (PDF extracted locally): pseudonymised data that could be attributed using additional information is personal data, even if the additional information is held by someone else; erasing the additional information makes it anonymous only if anonymity conditions are met; pseudonymisation can reduce risk, support reliance on legitimate interests, help establish compatibility under Art. 6(4); "pseudonymisation alone will normally not be a sufficient measure"; introduces the "pseudonymisation domain". https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-012025-pseudonymisation_en and PDF https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf (executive summary read)
- Opinion 28/2024 on AI models, adopted 17 December 2024. Executive summary read: anonymity claims assessed case by case; AI models trained with personal data "cannot, in all cases, be considered anonymous"; anonymous only if both the likelihood of direct (incl. probabilistic) extraction and of obtaining personal data from queries are insignificant, taking into account all means reasonably likely to be used. https://edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf (executive summary read)

## Tools and vendors

- Presidio (docs moved to presidio.dataprivacystack.org): analyzer detects PII with NER, regex, rules and checksums, multiple languages; anonymizer de-identifies; disclaimer "there is no guarantee that Presidio will find all sensitive information", use additional protections. https://presidio.dataprivacystack.org/ (home page read)
- OpenAI API data controls (volatile, landscape only): abuse monitoring logs retained up to 30 days by default; API data not used for training by default since 1 March 2023; Zero Data Retention subject to prior approval; some endpoints not ZDR-eligible. https://developers.openai.com/api/docs/guides/your-data (page read)

## Synthetic data and memorisation

- Stadler, Oprisanu, Troncoso: synthetic data either fails to prevent inference attacks or fails to retain utility; no better privacy-utility trade-off than traditional anonymisation; what signals are kept is "hard to predict". https://arxiv.org/abs/2011.07018 (abstract only)
- Carlini et al.: extraction attack on GPT-2 recovered hundreds of verbatim sequences including names, phone numbers and emails; possible even when a sequence appeared in only one training document; larger models more vulnerable. https://arxiv.org/abs/2012.07805 (abstract only)

## Gaps

- Anthropic, Google and other judge-vendor retention terms were not fetched; only OpenAI's page is recorded.
- EDPB Guidelines 01/2025 final (post-consultation) status UNVERIFIED.
- Non-EU regimes (e.g. CCPA, HIPAA) not researched; node is GDPR-framed and says so.
- Whether sending eval data to an LLM API is a processor relationship in a given deployment is fact-specific; the node states the Art. 28 requirement only.
