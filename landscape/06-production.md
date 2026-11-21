# Landscape: 06-production

Volatile items for this branch. One entry per line, format:

- <item> (type: tool|benchmark|model|standard|regulation|docs) as-of: YYYY-MM-DD | <source URL, or `URL not recorded`>

## Entries

Migrated from research/06-production.md (not individually re-verified; entries flagged UNVERIFIED there remain so).

- OTel GenAI semantic conventions: moved to `open-telemetry/semantic-conventions-genai`, Development status; content capture env var `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT` (type: standard) as-of: 2026-11-20 | https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md
- Anthropic deprecation table: Sonnet 4.5 retires 2026-11-30; Haiku 4.5 not sooner than 2026-10-15; `temperature/top_p/top_k` removed in API version 2026-10-21 (type: docs) as-of: 2026-11-20 | https://platform.claude.com/docs/en/about-claude/model-deprecations
- OpenAI deprecations: `gpt-5` family shutdown 2026-12-11; whisper-1 2027-02-26 (type: docs) as-of: 2026-11-20 | https://developers.openai.com/api/docs/deprecations
- Langfuse online LLM-as-judge (sampling rules, ~$0.01-0.10 per eval) (type: tool) as-of: 2026-11-20 | https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge
- Evidently drift defaults vary by version (type: tool) as-of: 2026-11-20 | https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests (link 404 as of 2026-11-21)
- Presidio (PII detection; moved to presidio.dataprivacystack.org) (type: tool) as-of: 2026-11-20 | https://presidio.dataprivacystack.org/
- Llama Guard (guardrail model) (type: model) as-of: 2026-11-20 | https://arxiv.org/abs/2312.06674
- NeMo Guardrails (guardrail toolkit) (type: tool) as-of: 2026-11-20 | https://arxiv.org/abs/2310.10501
- Constitutional Classifiers (guardrail classifiers) (type: model) as-of: 2026-11-20 | https://arxiv.org/abs/2501.18837
- AWS SageMaker shadow tests (type: tool) as-of: 2026-11-20 | https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html
- EDPB Guidelines 01/2025 on Pseudonymisation: adopted for public consultation 16 Jan 2025, consultation closed 14 Mar 2025; final version UNVERIFIED. (type: regulation) as-of: 2026-11-21 | https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-012025-pseudonymisation_en
- EDPB Opinion 28/2024 on AI models (anonymity, legitimate interest), adopted 17 Dec 2024. (type: regulation) as-of: 2026-11-21 | https://edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf
- OpenAI API data controls: abuse-monitoring logs kept up to 30 days by default; API data not used for training by default since 2023-03-01; Zero Data Retention needs prior approval. (type: docs) as-of: 2026-11-21 | https://developers.openai.com/api/docs/guides/your-data
- Microsoft Presidio docs moved to presidio.dataprivacystack.org. (type: tool) as-of: 2026-11-21 | https://presidio.dataprivacystack.org/
