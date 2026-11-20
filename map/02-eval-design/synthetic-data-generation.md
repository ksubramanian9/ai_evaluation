---
id: synthetic-data-generation
title: "Synthetic test data generation"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [golden-datasets]
tags: []
---
# Synthetic test data generation

Generating test cases with models, and the diversity and realism risks that come with it.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

_Source key (reused): [CLAUDE-EVAL] https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; [OAI-BP] https://developers.openai.com/api/docs/guides/evaluation-best-practices ; [ANTH-AGENT] https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; [HELM] https://arxiv.org/abs/2211.09110_

## Why it matters
Model-written evals can be cheap and good: 154 datasets, crowdworkers agreed with 90-100% of labels, and they surfaced inverse scaling and sycophancy [Perez et al.](https://arxiv.org/abs/2212.09251). Self-Instruct pipeline: generate, filter invalid/near-duplicate, finetune [Wang et al.](https://arxiv.org/abs/2212.10560). RAG test-set generation as a RAG-eval use [RAGAs](https://arxiv.org/abs/2309.15217) (testset generator itself UNVERIFIED). OpenAI lists synthetic examples among dataset sources [OAI-BP].
## Common failure modes
Need to check factuality, fidelity, bias [Liu et al. 2024](https://arxiv.org/abs/2404.07503); loss of distribution tails when training on model output (model collapse) [Shumailov et al.](https://arxiv.org/abs/2305.17493) (relevance to eval sets is my inference); near-duplicates (why Self-Instruct filters) [Wang](https://arxiv.org/abs/2212.10560); not matching production traffic [OAI-BP]; generator = judge self-preference (judge self-enhancement bias [Zheng](https://arxiv.org/abs/2306.05685)).
## Practice exercise
Generate 100 test cases with an LLM from 10 seed real cases; dedupe (embedding similarity threshold), human-review 30 for validity, compare slice distribution vs real traffic; report validity rate and diversity.
## Mastery check
(1) What fraction of synthetic items were invalid and why? (2) How do you show synthetic cases are realistic? (3) Risks if the same model generates and answers?
## Sources
https://arxiv.org/abs/2212.09251; https://arxiv.org/abs/2212.10560; https://arxiv.org/abs/2404.07503; https://arxiv.org/abs/2305.17493; [OAI-BP].
