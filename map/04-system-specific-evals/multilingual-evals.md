---
id: multilingual-evals
title: "Multilingual evals"
branch: 04-system-specific-evals
depth: L2
status: not-started
bridge: none
prerequisites: [coverage-and-slicing, golden-datasets]
tags: [safety, fairness]
---
# Multilingual evals

Measuring quality and safety per language, and choosing between translated and natively authored test sets.

_Researched 2026-11-21. Supplemented 2026-11-21: [research/supplements/2026-11-21-multilingual-evals.md](../../research/supplements/2026-11-21-multilingual-evals.md). All paper claims were read at abstract level; check numbers against the papers before relying on them. Model results are historical (2022-2024 models). Benchmark names live in [landscape/04-system-specific-evals.md](../../landscape/04-system-specific-evals.md). Exercises and mastery checks are proposed designs, not sourced claims._

**Owns:** language as an eval slice and multilingual test-set construction; see also [coverage-and-slicing](../02-eval-design/coverage-and-slicing.md), [safety-and-harm-evals](../05-testing-in-engineering/safety-and-harm-evals.md), [red-teaming](../05-testing-in-engineering/red-teaming.md).

## Learning objectives
You can:
- Slice an eval by language and report per-language quality and safety results with sample sizes, instead of one pooled score.
- Explain how translated test sets differ from natively authored ones (translation artefacts, cultural skew) and choose one for a given product.
- Run a small multilingual safety check that translates unsafe prompts into a low-resource language and compare refusal rates with English.

**Done bar.** Practiced: a per-language results table (at least three languages, one low-resource) for one task and one safety probe set, with n per cell and a short note on which items were machine-translated and which were native. Mastered: written answers to all three mastery-check questions, checked against Shi et al., Singh et al., Artetxe et al., Yong et al. and Deng et al., plus a test-set plan for a real or capstone product that states which languages get native items, which get verified translations, and why.

## Why it matters
- Translated benchmarks are common: MGSM hand-translated 250 GSM8K math problems into ten typologically diverse languages ([Shi et al. 2022, abstract](https://arxiv.org/abs/2210.03057)).
- Translation can change what is measured: translating test or training sets can introduce subtle artefacts that noticeably affect models; in NLI, translating premise and hypothesis separately reduces their lexical overlap, and models are sensitive to this ([Artetxe et al. 2020, abstract](https://arxiv.org/abs/2004.04721)).
- Translation also carries over the source culture: 28% of MMLU questions need culturally sensitive knowledge, and 84.9% of its geography questions focus on North America or Europe ([Singh et al. 2024, Global-MMLU, abstract](https://arxiv.org/abs/2412.03304)).
- Model rankings changed between the full Global-MMLU set and its culturally sensitive subset, so a translated benchmark can mislead model choice ([Singh et al. 2024, abstract](https://arxiv.org/abs/2412.03304)).
- Natively authored sets avoid these problems: TyDi QA was "collected directly in each language without the use of translation" to avoid priming ([Clark et al. 2020, abstract](https://arxiv.org/abs/2003.05002)); INCLUDE builds 197,243 questions in 44 languages from local exam sources to capture regional knowledge ([Romanou et al. 2024, abstract](https://arxiv.org/abs/2411.19799)).
- Safety can regress by language: translating unsafe AdvBench prompts into low-resource languages got GPT-4 to give actionable harmful content 79% of the time, while high- and mid-resource languages had significantly lower attack success (2023 result) ([Yong et al. 2023, abstract](https://arxiv.org/abs/2310.02446)).
- Unsafe output rose as language resources fell even without attacker intent; low-resource languages were about three times as likely as high-resource ones to produce harmful content for ChatGPT and GPT-4 (2023 result) ([Deng et al. 2023, abstract](https://arxiv.org/abs/2310.06474)).

## Common failure modes
- Reporting one pooled score that hides a weak language; slice by language as you would by any other attribute ([coverage-and-slicing](../02-eval-design/coverage-and-slicing.md)).
- Machine-translating an English golden set and treating the result as native quality; Global-MMLU argues machine translation alone is insufficient and used professional and community annotators to verify ([Singh et al. 2024, abstract](https://arxiv.org/abs/2412.03304)).
- Measuring translated items that keep English-centric cultural content, then reading the gap as a language-skill gap ([Singh et al. 2024, abstract](https://arxiv.org/abs/2412.03304)).
- Running safety and red-team suites in English only; public translation APIs let anyone move an attack into a low-resource language ([Yong et al. 2023, abstract](https://arxiv.org/abs/2310.02446)).
- Grading non-English outputs with an English-centric judge or reference metric without checking it per language (proposed check; see [judge-bias-and-calibration](../03-measurement-methods/judge-bias-and-calibration.md)).
- Too few items per language to tell a real gap from noise; report n and intervals per slice (see [confidence-intervals-for-evals](../03-measurement-methods/confidence-intervals-for-evals.md)).

## Practice exercise (3 h)
Pick a task from your capstone or a public set. Take 30 English items and produce two versions in one high-resource and one low-resource language: machine-translated, and (for 10 items) checked or rewritten by a fluent speaker or a native public set such as TyDi QA. Run your system on all versions and report accuracy per language and per version, with n. Then take 20 unsafe prompts from a public safety set, translate them into the low-resource language and compare refusal rates with English. Write three sentences on which differences you think come from translation artefacts and which from the model.

## Mastery check
1. Why can a model's score on a machine-translated benchmark overstate or understate its real quality in that language?
2. When would you pay for natively authored test items instead of verified translations, and for which languages first?
3. Your English safety suite passes. What multilingual evidence would you need before shipping in ten languages?

## Sources
- [Shi et al. 2022, Language Models are Multilingual Chain-of-Thought Reasoners (MGSM)](https://arxiv.org/abs/2210.03057)
- [Singh et al. 2024, Global MMLU](https://arxiv.org/abs/2412.03304)
- [Romanou et al. 2024, INCLUDE](https://arxiv.org/abs/2411.19799)
- [Clark et al. 2020, TyDi QA](https://arxiv.org/abs/2003.05002)
- [Artetxe et al. 2020, Translation Artifacts in Cross-lingual Transfer Learning](https://arxiv.org/abs/2004.04721)
- [Yong et al. 2023, Low-Resource Languages Jailbreak GPT-4](https://arxiv.org/abs/2310.02446)
- [Deng et al. 2023, Multilingual Jailbreak Challenges in Large Language Models](https://arxiv.org/abs/2310.06474)
