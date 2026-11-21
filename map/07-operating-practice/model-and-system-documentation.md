---
id: model-and-system-documentation
title: "Model and system documentation"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [eval-reporting-and-communication]
tags: [fairness, statistics]
---
# Model and system documentation

Model cards, system cards, and eval documentation practices.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Write a system card that covers intended and out-of-scope use, components and versions, eval datasets with provenance, metrics with CIs, disaggregated slices, known failures, red-team findings and a monitoring plan.
- Write an eval section with enough detail for a third party to reproduce it (test-set provenance, prompt template, sampling settings, judge model and version).
- Compare model cards, datasheets, system cards and Annex IV technical files by audience, scope and update trigger.
- Check a card against Annex IV 2(g) and NIST MEASURE 2.1 and list the missing fields.

**Done bar.** Practiced: a system card for the capstone app with all listed sections, plus a gap list from checking it against Annex IV 2(g) and MEASURE 2.1. Mastered: written answers to all three mastery questions checked against Mitchell et al., Gebru et al. and NIST AI 100-1, and the card versioned alongside one real or capstone system change with what was updated recorded.

## Why it matters
- Model Cards (Mitchell et al., FAT* 2019, arXiv v1 5 Oct 2018, v2 14 Jan 2019): short documents accompanying models that report benchmarked evaluation, intended use contexts, evaluation procedures; call for results disaggregated by cultural, demographic or phenotypic groups and intersections ([arXiv 1810.03993](https://arxiv.org/abs/1810.03993)).
- Datasheets for Datasets (Gebru et al.): documentation of motivation, composition, collection process, recommended uses; v1 Mar 2018, CACM Dec 2021 (v8 1 Dec 2021) ([arXiv 1803.09010](https://arxiv.org/abs/1803.09010)).
- Hugging Face model cards: README.md plus YAML metadata; should describe intended uses/limitations, training info, datasets and evaluation results; structured eval results via `model-index`, with a newer simpler format ([HF docs](https://huggingface.co/docs/hub/model-cards)). As-of 2026-11-20, volatile.
- System cards (frontier providers): Anthropic says they "document the capabilities, safety evaluations, and responsible deployment decisions for Claude models"; one per model release, latest Nov 2026 ([Anthropic system cards](https://www.anthropic.com/system-cards)). OpenAI's GPT-4 report arXiv page ([arXiv 2303.08774](https://arxiv.org/abs/2303.08774)) did not confirm a system card; OpenAI system-card page blocked (403): UNVERIFIED.
- Regulatory pull: EU Annex IV technical documentation (test logs, metrics, group accuracy) and GPAI Code of Practice Model Documentation Form (see regulatory-compliance); NIST MEASURE 2.1 requires test sets, metrics and tools to be documented, and MS-2.3-003 asks to share pre-deployment results with release-approval actors ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf); [AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)).
- Benchmark documentation quality: BetterBench scored 24 benchmarks against 46 best practices; found wide quality variation, most did not report statistical significance, many hard to replicate ([arXiv 2411.12990](https://arxiv.org/abs/2411.12990)). Construct-validity review of 445 LLM benchmarks (Bean et al., NeurIPS 2025 D&B) offers a checklist ([arXiv 2511.04703](https://arxiv.org/abs/2511.04703); numbers from search summary, 53.4% reported construct validity evidence; verify in paper).

## Common failure modes
- Aggregate-only numbers (hides subgroup failure; the Model Cards motivation).
- Eval section without test-set provenance, prompt template, sampling settings, judge model/version, so results are not reproducible (derived from MEASURE 2.1 requirement; also BetterBench replicability finding).
- Card written once and not versioned with the model/prompt/system change.
- Card documents the model but not the system (retrieval, tools, guardrails), where the actual risk sits (inference; AI 600-1 stresses value chain and component integration risk).

## Practice exercise (3 h)
Write a system card for your capstone app with: intended/out-of-scope use, components and versions, eval datasets (provenance, size, date), metrics with CIs, disaggregated slices, known failures, red-team findings, monitoring plan. Then check it against Annex IV 2(g) and MEASURE 2.1 and list missing fields.

## Mastery check
1. What must be in an eval section for a third party to reproduce it?
2. Why disaggregate, and how many slices before noise dominates (link to CI node)?
3. Compare model card, datasheet, system card, Annex IV file: audience, scope, update trigger.

## Sources
- [Mitchell et al., Model Cards, arXiv 1810.03993](https://arxiv.org/abs/1810.03993)
- [Gebru et al., Datasheets for Datasets, arXiv 1803.09010](https://arxiv.org/abs/1803.09010)
- [Hugging Face model cards](https://huggingface.co/docs/hub/model-cards)
- [Anthropic system cards](https://www.anthropic.com/system-cards)
- [OpenAI, GPT-4 technical report, arXiv 2303.08774](https://arxiv.org/abs/2303.08774)
- [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf); [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [BetterBench, arXiv 2411.12990](https://arxiv.org/abs/2411.12990)
- [Construct validity review, arXiv 2511.04703](https://arxiv.org/abs/2511.04703)
- [Commission, GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)
