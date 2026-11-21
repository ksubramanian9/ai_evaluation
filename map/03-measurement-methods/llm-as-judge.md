---
id: llm-as-judge
title: "LLM-as-judge"
branch: 03-measurement-methods
depth: L3
status: not-started
bridge: none
prerequisites: [rubric-design, human-evaluation]
tags: [llm-judge, human-labels]
---
# LLM-as-judge

Using a model to grade outputs: prompt design, scoring formats, and when it is appropriate.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

**Owns:** judge design and validation; see also [judge-bias-and-calibration](judge-bias-and-calibration.md), [production-evals-with-judges](../06-production/production-evals-with-judges.md).

## Learning objectives
You can:
- Write a judge prompt with a rubric, a reasoning step and a strict output format.
- Validate a judge against human labels with kappa and a confusion matrix, and iterate the rubric.
- Compare binary, Likert and pairwise judging formats and choose one for a task.
- Critique a judge setup (unvalidated, same model family as the generator, uncontrolled versioning) and decide whether it is fit for regression gating.

**Done bar.** Practiced: the judge prompt, kappa and confusion matrices for two judge models on 50 labeled outputs, and one rubric iteration with its effect on agreement. Mastered: written answers to all three mastery-check questions, checked against Zheng et al., Liu et al., Kim et al., Shankar et al. and the Anthropic and OpenAI guides, plus a design or critique of a real judge that decides whether it can gate releases and states the trade-off between cost, bias and agreement.

## Why it matters
- Strong LLM judges can approximate human preference at scale.
- Zheng et al. report GPT-4-class judges reaching over 80% agreement with controlled and crowdsourced human preferences, comparable to human-human agreement ([Zheng et al. 2023](https://arxiv.org/abs/2306.05685)).
- G-Eval uses chain-of-thought and a form-filling paradigm and reports Spearman 0.514 with humans on summarization with GPT-4 ([Liu et al. 2023](https://arxiv.org/abs/2303.16634)).
- Prometheus (open 13B judge using a user rubric and reference) reports Pearson 0.897 with humans on 45 custom rubrics (GPT-4 0.882, ChatGPT 0.392) ([Kim et al. 2023](https://arxiv.org/abs/2310.08491)).
- Vendor guidance: use a different model from the generator, constrain output format ("Output only 'yes' or 'no'"), and use binary or Likert formats with clear criteria ([Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- OpenAI: start with a strong judge, add reasoning before scoring, prefer pairwise or pass/fail over open-ended scores, validate against human annotations ([OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).

## Common failure modes
- Position, verbosity and self-enhancement bias, plus limited reasoning ability ([Zheng et al.](https://arxiv.org/abs/2306.05685)).
- Possible bias toward LLM-generated text (preliminary) ([G-Eval](https://arxiv.org/abs/2303.16634)).
- Proprietary judges have uncontrolled versioning and cost ([Prometheus](https://arxiv.org/abs/2310.08491)).
- Judges inherit LLM flaws, so they must be validated against human grades; criteria are subjective and iterative ([Shankar et al.](https://arxiv.org/abs/2404.12272)).

## Practice exercise (2-3 h)
Take 50 outputs from a small task with your own pass/fail labels. Write a judge prompt with a rubric, a reasoning step and a strict output format. Run it with two judge models. Report agreement with your labels (kappa) and the confusion matrix. Iterate the rubric once.

## Mastery check
1. Why validate a judge against human labels before using it for regression gating?
2. Compare binary, Likert and pairwise judging formats.
3. Show what changes when the judge shares a model family with the generator.

## Sources
- [Zheng et al. 2023, MT-Bench paper](https://arxiv.org/abs/2306.05685)
- [Liu et al. 2023, G-Eval](https://arxiv.org/abs/2303.16634)
- [Kim et al. 2023, Prometheus](https://arxiv.org/abs/2310.08491)
- [Shankar et al. 2024, Who Validates the Validators?](https://arxiv.org/abs/2404.12272)
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
