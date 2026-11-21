# Research supplement: eval-dataset-versioning

As-of: 2026-11-21. All sources fetched in this session via WebFetch.

## Documentation

- Gebru et al., Datasheets for Datasets: no standard way to document datasets; by analogy with electronics datasheets, each dataset should document motivation, composition, collection process, recommended uses; aims to improve creator-consumer communication, transparency and accountability. v1 Mar 2018, v8 Dec 2021 (CACM). https://arxiv.org/abs/1803.09010 (abstract only)
- Pushkarna, Zaldivar, Kjartansson, Data Cards (FAccT 2022): structured summaries of essential facts across a dataset's lifecycle, including upstream sources, collection and annotation methods, training and evaluation methods, intended use; documentation as a user-centric product; lessons from over 20 Data Cards. https://arxiv.org/abs/2204.01075 (abstract only)

## Label errors and corrections

- Northcutt, Athalye, Mueller (NeurIPS 2021 D&B): at least 3.3% test label errors on average across 10 datasets; at least 6% of ImageNet validation; 51% of algorithm-flagged candidates confirmed by humans; ResNet-18 beats ResNet-50 on ImageNet if mislabeled test examples rise by just 6%; VGG-11 beats VGG-19 on CIFAR-10 at 5%. https://arxiv.org/abs/2103.14749 (abstract only)
- Gema et al., Are We Done with MMLU?: 57% of analysed Virology questions contain errors; estimated 6.49% of MMLU questions have errors; MMLU-Redux, 5,700 re-annotated questions across 57 subjects; significant discrepancies with originally reported performance. https://arxiv.org/abs/2406.04127 (abstract only)

## Saturation, refresh and holdout reuse

- Kiela et al., Dynabench: models "quickly achieve outstanding performance on benchmark tasks" yet fail simple challenge examples; proposes dynamic dataset creation. https://arxiv.org/abs/2104.14337 (abstract only)
- Recht et al. 2019: new CIFAR-10 and ImageNet test sets following original processes; accuracy drops 3-15% (CIFAR-10) and 11-14% (ImageNet); gains on original test sets carried over; drops attributed not to adaptivity but to slightly harder images. https://arxiv.org/abs/1902.10811 (abstract only)
- Dwork et al. 2015: adaptively reusing a holdout set "can easily lead to overfitting to the holdout set itself"; proposes a reusable holdout mechanism. https://arxiv.org/abs/1506.02629 (abstract only)

## Tooling (volatile, landscape)

- Hugging Face Datasets: `load_dataset(..., revision=...)` takes a tag name, branch name or commit hash to load a specific dataset version (docs v5.2.0). https://huggingface.co/docs/datasets/en/loading (page read)

## Gaps

- No primary source read on changelog conventions for eval sets specifically (semantic versioning of datasets is a proposed practice in the node, not a sourced claim).
- Recht et al. is classical vision; transfer to LLM eval sets is an inference, labelled as such.
