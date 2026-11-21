# Research supplement: multilingual-evals

As-of: 2026-11-21. All sources fetched in this session via WebFetch; depth of reading is stated per claim.

## Benchmarks: translated vs natively authored

- MGSM: 250 GSM8K grade-school math problems hand-translated into ten typologically diverse languages; chain-of-thought multilingual reasoning emerges with scale, including in underrepresented languages such as Bengali and Swahili. The abstract does not say who translated. https://arxiv.org/abs/2210.03057 (abstract only)
- Global-MMLU: 28% of MMLU questions need culturally sensitive knowledge; 84.9% of geography questions focus on North America or Europe; translation can introduce artefacts that distort meaning, so machine-translating a dataset is not enough; 42 languages; translations checked by compensated professional and community annotators; questions labelled culturally sensitive vs agnostic; model rankings change between the full set and the culturally sensitive subset. https://arxiv.org/abs/2412.03304 (abstract only)
- INCLUDE: 197,243 QA pairs in 44 written languages built "from local exam sources"; motivated by translated benchmarks ignoring regional and cultural knowledge. The abstract does not say whether every item was originally written in the target language. https://arxiv.org/abs/2411.19799 (abstract only)
- TyDi QA: 11 typologically diverse languages, 204K QA pairs, data "collected directly in each language without the use of translation", by question writers who wanted to know the answer, to avoid priming effects. https://arxiv.org/abs/2003.05002 (abstract only)

## Translation artefacts

- Translating test or training sets (human or machine) can introduce subtle artefacts that noticeably affect cross-lingual models; in NLI, translating premise and hypothesis independently can reduce their lexical overlap, and models are very sensitive to this; some earlier cross-lingual results need revisiting; XNLI state of the art improved by 4.3 (translate-test) and 2.8 (zero-shot) points. https://arxiv.org/abs/2004.04721 (abstract only)

## Safety in low-resource languages

- Yong et al. 2023: translating unsafe English prompts (AdvBench) into low-resource languages got GPT-4 to give actionable harmful content 79% of the time, on par with or above state-of-the-art jailbreaks; high- and mid-resource languages had significantly lower attack success; public translation APIs make this available to anyone; calls for multilingual red-teaming. https://arxiv.org/abs/2310.02446 (abstract only)
- Deng et al. 2023 (ICLR 2024): unintentional scenario, unsafe output rises as language resources fall, low-resource languages about three times as likely as high-resource ones to produce harmful content for ChatGPT and GPT-4; intentional scenario (harmful instruction plus multilingual prompt) gives 80.92% unsafe for ChatGPT and 40.71% for GPT-4; proposes Self-Defense multilingual safety fine-tuning data. https://arxiv.org/abs/2310.06474 (abstract only)

## Gaps

- Per-language numbers inside MGSM, Global-MMLU and Yong et al. were not read (abstracts only).
- "Translationese" as a term is not used in the abstracts read; the node says "translation artefacts" and treats translationese as the general concept, not a sourced claim.
- No primary source was read on how to compute per-language confidence intervals; the node links to the existing statistics nodes instead.
- Model results are historical (2022-2024 models) and say nothing about current models.
