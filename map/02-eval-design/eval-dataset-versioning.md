---
id: eval-dataset-versioning
title: "Eval dataset versioning and maintenance"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [golden-datasets, contamination-and-leakage]
tags: [human-labels]
---
# Eval dataset versioning and maintenance

Versioning eval sets, tying every result to a dataset version, and handling corrections, saturation and refresh.

_Researched 2026-11-21. Supplemented 2026-11-21: [research/supplements/2026-11-21-eval-dataset-versioning.md](../../research/supplements/2026-11-21-eval-dataset-versioning.md). All paper claims were read at abstract level; check numbers against the papers before relying on them. Tool specifics live in [landscape/02-eval-design.md](../../landscape/02-eval-design.md). Exercises and mastery checks are proposed designs, not sourced claims._

**Owns:** eval-set versions, changelogs and refresh; see also [golden-datasets](golden-datasets.md) (building the set), [contamination-and-leakage](contamination-and-leakage.md), [model-and-system-documentation](../07-operating-practice/model-and-system-documentation.md) (datasheets as system documentation).

## Learning objectives
You can:
- Put an eval set under version control with a changelog, and record the dataset version with every result so trend lines compare like with like.
- Apply a label correction and show its effect on past scores and model rankings by rescoring old runs on both versions.
- Decide when a set is saturated or overexposed and plan a refresh with a fresh holdout.
- Write a datasheet or data card for an eval set.

**Done bar.** Practiced: an eval set with two tagged versions, a changelog entry per change, a results table keyed by (system version, dataset version), and a rescoring of at least two past runs on the corrected version. Mastered: written answers to all three mastery-check questions, checked against Northcutt et al., Gema et al., Dwork et al., Recht et al. and Gebru et al., plus a datasheet and refresh policy for a real or capstone eval set.

## Why it matters
- Test labels are often wrong: at least 3.3% of test labels were erroneous on average across 10 popular datasets, and at least 6% of ImageNet validation ([Northcutt et al. 2021, abstract](https://arxiv.org/abs/2103.14749)).
- Corrections can flip rankings: ResNet-18 beats ResNet-50 on ImageNet if the share of mislabeled test examples rises by only 6% ([Northcutt et al. 2021, abstract](https://arxiv.org/abs/2103.14749)). So a score is meaningless without the label version it was computed on.
- LLM benchmarks have the same problem: an estimated 6.49% of MMLU questions contain errors (57% of analysed Virology items), and re-annotated MMLU-Redux showed significant discrepancies with reported performance ([Gema et al. 2024, abstract](https://arxiv.org/abs/2406.04127)).
- Benchmarks saturate: models "quickly achieve outstanding performance on benchmark tasks" while still failing simple challenge examples, which motivates dynamic dataset creation ([Kiela et al. 2021, Dynabench, abstract](https://arxiv.org/abs/2104.14337)); see also saturation in [golden-datasets](golden-datasets.md).
- Reusing one holdout for many decisions overfits to it: adaptive reuse "can easily lead to overfitting to the holdout set itself" ([Dwork et al. 2015, abstract](https://arxiv.org/abs/1506.02629)).
- Refreshing a test set with the original process can still move scores: new CIFAR-10 and ImageNet test sets dropped accuracy by 3-15% and 11-14%, which the authors attribute to slightly harder images rather than adaptive overfitting; gains on the old set carried over (2019 vision result) ([Recht et al. 2019, abstract](https://arxiv.org/abs/1902.10811)). A refreshed set therefore starts a new trend line.
- Datasheets document a dataset's motivation, composition, collection process and recommended uses ([Gebru et al., abstract](https://arxiv.org/abs/1803.09010)); Data Cards add lifecycle facts such as annotation methods, evaluation methods and intended use ([Pushkarna et al. 2022, abstract](https://arxiv.org/abs/2204.01075)).
- Dataset hubs support pinning: e.g. Hugging Face `load_dataset` takes a `revision` (tag, branch or commit) ([Hugging Face Datasets docs](https://huggingface.co/docs/datasets/en/loading)).

## Common failure modes
- Editing the set in place and plotting one trend line across versions, so a label fix looks like a model regression or improvement ([Northcutt et al.](https://arxiv.org/abs/2103.14749)).
- Results that record the model and prompt version but not the dataset version or hash (proposed check; pair with [prompt-versioning-and-change-management](../05-testing-in-engineering/prompt-versioning-and-change-management.md)).
- Tuning prompts against the same set you report on until it stops being a holdout ([Dwork et al.](https://arxiv.org/abs/1506.02629)).
- Keeping a saturated set as the headline metric after it stops discriminating ([Kiela et al.](https://arxiv.org/abs/2104.14337)).
- Fixing errors silently instead of logging which items changed and why, so nobody can rescore history (proposed practice).
- Publishing or sharing the set (or its answers) where it can enter training data; see [contamination-and-leakage](contamination-and-leakage.md).
- No datasheet, so later users do not know the set's sources, label process or intended use ([Gebru et al.](https://arxiv.org/abs/1803.09010)).

## Practice exercise (3 h)
Take your golden set (or 100 items of a public set). Put it in git or a dataset hub and tag v1. Rescore two past system versions on v1. Audit 30 items, fix the wrong or ambiguous ones, write a changelog entry per item (id, old label, new label, reason) and tag v1.1. Rescore both systems on v1.1 and show the score and ranking change. Split off 20% as a sealed holdout you will only score at release time. Write a one-page datasheet (motivation, composition, collection, labelling, intended use, known issues, refresh rule).

## Mastery check
1. A dashboard shows a 4-point jump after a dataset fix. How do you tell how much is the model and how much is the labels?
2. When should a set be retired, refreshed, or moved to a regression suite, and how do you keep the trend line honest across the change?
3. How do you keep a holdout meaningful when the team runs evals daily?

## Sources
- [Northcutt, Athalye, Mueller 2021, Pervasive Label Errors in Test Sets Destabilize ML Benchmarks](https://arxiv.org/abs/2103.14749)
- [Gema et al. 2024, Are We Done with MMLU?](https://arxiv.org/abs/2406.04127)
- [Kiela et al. 2021, Dynabench](https://arxiv.org/abs/2104.14337)
- [Dwork et al. 2015, Generalization in Adaptive Data Analysis and Holdout Reuse](https://arxiv.org/abs/1506.02629)
- [Recht et al. 2019, Do ImageNet Classifiers Generalize to ImageNet?](https://arxiv.org/abs/1902.10811)
- [Gebru et al., Datasheets for Datasets](https://arxiv.org/abs/1803.09010)
- [Pushkarna, Zaldivar, Kjartansson 2022, Data Cards](https://arxiv.org/abs/2204.01075)
- [Hugging Face Datasets, Load](https://huggingface.co/docs/datasets/en/loading)
