# Landscape: 06-production

Volatile items for this branch. One entry per line, format:

- <item> (type: tool|benchmark|model|standard) as-of: YYYY-MM-DD | <source URL>

## Entries

Migrated from research/06-production.md (not individually re-verified; entries flagged UNVERIFIED there remain so).

- OTel GenAI semantic conventions: moved to `open-telemetry/semantic-conventions-genai`, Development status; content capture env var `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT` - https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md as-of: 2026-11-20
- Anthropic deprecation table: Sonnet 4.5 retires 2026-11-30; Haiku 4.5 not sooner than 2026-10-15; `temperature/top_p/top_k` removed in API version 2026-10-21 - https://platform.claude.com/docs/en/about-claude/model-deprecations as-of: 2026-11-20
- OpenAI deprecations: `gpt-5` family shutdown 2026-12-11; whisper-1 2027-02-26 - https://developers.openai.com/api/docs/deprecations as-of: 2026-11-20
- Langfuse online LLM-as-judge (sampling rules, ~$0.01-0.10 per eval) - https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge as-of: 2026-11-20
- Evidently drift defaults vary by version - https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests as-of: 2026-11-20
- Presidio (PII detection; moved to presidio.dataprivacystack.org) - https://presidio.dataprivacystack.org/ as-of: 2026-11-20
- Llama Guard, NeMo Guardrails, Constitutional Classifiers (guardrail models/toolkits) - links in runtime-guardrails as-of: 2026-11-20
- AWS SageMaker shadow tests - https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html as-of: 2026-11-20
