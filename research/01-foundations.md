# Research: 01-foundations (11 nodes)

Researched 2026-11-20. Method: each cited page was fetched; claims below paraphrase what the fetch returned. "UNVERIFIED" = not confirmed from a fetched primary page. "practitioner" = blog/course source. Note that fetches were summarized by a small model, so exact numbers should be re-checked against the paper before being copied into a node as a hard fact.

---

## evaluation-mindset

**Why it matters**
- LLM evals are experiments: questions are samples from an unseen super-population, so a score is an estimate with error, not a fact ([Miller 2024](https://arxiv.org/abs/2411.00640)).
- Headline benchmarks are proxies; a high score on a popular benchmark is read as progress toward broad goals it may not measure (construct validity) ([Raji et al. 2021](https://arxiv.org/abs/2111.15366)).
- Reported gains in reasoning benchmarks are sensitive to decoding parameters, seeds, prompt format, hardware/software; unreported variance makes comparisons unclear ([Hochlehnert et al. 2025](https://arxiv.org/abs/2504.07086)).
- Criteria for "good" are partly defined by looking at outputs ("criteria drift"), so evaluation design is iterative ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).

**Common failure modes**
- Treating a single run/point score as truth; no error bars (Miller).
- Treating a benchmark as a general capability measure (Raji).
- Comparing systems with unreported seeds/prompt/decoding differences (Hochlehnert).
- Fixing criteria up front and never revising them after seeing outputs (Shankar).

**Practice exercise (2-3 h)**: Take any 100-question multiple-choice set (e.g. a subset of an open benchmark) and a model API. Run it 5 times with sampling on. Report per-run accuracy, spread across runs, and a standard-error-based 95% CI from one run. Write a paragraph: which differences of 2 points would you trust?

**Mastery check**
1. Why is "model A scored 71.2, model B 70.5" not a finding? What would you need?
2. Give an example where a benchmark's name implies a construct it does not measure.
3. List four configuration choices that can move a reported score without changing the model.

**Primary sources**
- Miller, "Adding Error Bars to Evals", arXiv 2411.00640: https://arxiv.org/abs/2411.00640
- Raji et al., "AI and the Everything in the Whole Wide World Benchmark", NeurIPS 2021 D&B: https://arxiv.org/abs/2111.15366
- Hochlehnert et al., "A Sober Look at Progress in Language Model Reasoning", COLM 2025: https://arxiv.org/abs/2504.07086
- Shankar et al., "Who Validates the Validators?": https://arxiv.org/abs/2404.12272

---

## llm-basics-for-evaluators

**Why it matters**
- Decoding strategy alone can greatly change output quality with the same model; greedy decoding gets repetitive on long outputs, sampling trades determinism for diversity ([Holtzman et al. 2020](https://arxiv.org/abs/1904.09751); [HF generation strategies](https://huggingface.co/docs/transformers/generation_strategies)).
- The context window is everything the model can reference including its own output; system prompt, tool definitions, tool results, and thinking tokens all count. Accuracy and recall degrade as token count grows ("context rot") ([Anthropic context windows doc](https://platform.claude.com/docs/en/build-with-claude/context-windows)).
- "Deterministic" settings are not deterministic: see nondeterminism-and-variance below. Anthropic's SDK reference states temperature 0.0 results "will not be fully deterministic" ([Anthropic SDK reference, mirror of API docs](https://rubydoc.info/github/anthropics/anthropic-sdk-ruby/main/Anthropic%2FModels%2FBeta%2FMessageCreateParams:temperature); the official API reference page was too large to fetch, so treat as secondary mirror).
- System vs model: the evaluated thing is model + prompt + sampling config + serving stack. OpenAI exposes `system_fingerprint` to signal backend configuration changes, and says determinism is best-effort ([OpenAI cookbook, archived](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter); Azure restatement: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output). The current OpenAI platform docs page returned 404; UNVERIFIED against current docs.

**Common failure modes**
- Context overflow or silent truncation of inputs; counting only user message tokens (Anthropic doc: input over the window returns 400 "prompt is too long").
- Assuming temperature 0 means reproducible (Atil, Ouyang, Thinking Machines below).
- Evaluating a model name without recording version, sampling params, system prompt, and fingerprint.
- Placing key facts deep in long contexts and misattributing the resulting failure to the model's "knowledge" (context rot, Anthropic doc).

**Practice exercise (2 h)**: With a small open model via Hugging Face `generate`, run one prompt with greedy, `do_sample=True` temperature 0.7, top_p 0.9, and beam search, 20 samples each; compare unique-output counts and length. Then pad the prompt with irrelevant text until a retrieval question fails; log token count at failure using the tokenizer.

**Mastery check**
1. What counts toward the context window in an agentic request with tools and thinking?
2. Explain greedy vs top-p vs temperature, and which settings you would fix in an eval and why.
3. List the fields you must log for an eval run to be reproducible.

**Primary sources**
- Holtzman et al., "The Curious Case of Neural Text Degeneration" (ICLR 2020): https://arxiv.org/abs/1904.09751
- Hugging Face Transformers, generation strategies: https://huggingface.co/docs/transformers/generation_strategies
- Anthropic, context windows: https://platform.claude.com/docs/en/build-with-claude/context-windows
- OpenAI cookbook, reproducible outputs with seed (archived): https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter
- Practitioner: Thinking Machines, "Defeating Nondeterminism in LLM Inference": https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

---

## ml-metrics

**Why it matters**
- The metric encodes the cost model; scikit-learn documents proper-scoring pairings (squared error for the mean, absolute error for the median, pinball for quantiles) ([sklearn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)).
- On imbalanced data, accuracy can be above chance only because of the imbalance; balanced accuracy drops to 1/n_classes in that case (sklearn, same page).
- ROC plots can be deceptive under class imbalance; PR plots reflect precision and are more informative for expected future performance ([Saito & Rehmsmeier 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118432)).

**Common failure modes**
- Reporting accuracy on imbalanced data (sklearn balanced accuracy note).
- Reading a high ROC-AUC as high precision at deployment prevalence (Saito & Rehmsmeier; their re-analysis of a published tool comparison showed strong ROC but very low precision).
- F1 undefined/zero when no positives: sklearn defaults to 0 and exposes `zero_division`.
- Optimizing a metric inconsistent with the decision (e.g. R^2 vs absolute error when median matters; sklearn scoring table).
- Ranking metrics (NDCG etc.): UNVERIFIED, the sklearn page was truncated before that section; re-fetch https://scikit-learn.org/stable/modules/model_evaluation.html offset 100000.

**Practice exercise (2 h)**: sklearn on a dataset with ~2% positives (e.g. `fetch_openml` credit-card-fraud or `make_classification(weights=[0.98])`). Train logistic regression; compute accuracy, balanced accuracy, ROC-AUC, average precision, F1 at default and tuned threshold. Plot ROC and PR. Show that a constant-negative classifier gets 98% accuracy; explain which metric moves the least with prevalence.

**Mastery check**
1. Given a prevalence and a confusion matrix, compute precision/recall/F-beta by hand; justify beta for a recall-critical task.
2. When does ROC-AUC mislead and what do you report instead?
3. Which metric for a task where output is a ranked list and only the top 5 matter? (Answer needs NDCG/MRR or similar; verify definitions in sklearn docs.)

**Primary sources**
- scikit-learn, model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- Saito & Rehmsmeier, PLOS ONE 2015: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118432

---

## data-splits-and-leakage

**Why it matters**
- Leakage = information unavailable at prediction time used in building the model; yields optimistic estimates and poorer real performance ([sklearn common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)).
- Scale of the problem: a survey found leakage errors in 17 fields affecting 329 papers, with an 8-type taxonomy; in a civil-war-prediction case, the claimed ML advantage over logistic regression disappeared once leakage was fixed ([Kapoor & Narayanan 2022/2023](https://arxiv.org/abs/2207.07048)).
- Tuning on the test set leaks knowledge into the model so the metric no longer reports generalization ([sklearn cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)).
- LLM relevance: benchmark contamination is the same failure for pretraining data. UNVERIFIED here; add a contamination source (not fetched) in the LLM branch.

**Common failure modes**
- Fitting preprocessing/feature selection before splitting: sklearn's example (200 samples, 10,000 random features) gives 0.76 test accuracy on random labels when selecting features on all data, 0.5 when split first.
- Group leakage: multiple samples per subject across train/test; fix with `GroupKFold` (sklearn CV doc).
- Temporal leakage: shuffling time-ordered data inflates scores; use `TimeSeriesSplit` (sklearn CV doc).
- Repeated peeking at the test set during tuning (sklearn CV doc).

**Practice exercise (1-2 h)**: Reproduce the sklearn random-data experiment (random X, random y), then (a) leak via SelectKBest before split, (b) fix with a Pipeline. Then build a dataset with repeated "patients", compare KFold vs GroupKFold scores. Write one line per leak type naming the Kapoor taxonomy category (read the paper's table).

**Mastery check**
1. Why is accuracy 0.76 on random labels proof of a bug?
2. For a dataset of chat transcripts from 500 users, how do you split, and why?
3. Name three leakage types not caught by "split before preprocessing".

**Primary sources**
- scikit-learn common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
- scikit-learn cross-validation: https://scikit-learn.org/stable/modules/cross_validation.html
- Kapoor & Narayanan, "Leakage and the Reproducibility Crisis in ML-based Science": https://arxiv.org/abs/2207.07048

---

## classical-ml-validation

**Why it matters**
- k-fold CV reports the average over folds and avoids wasting data on a fixed validation set, with a test set still held out ([sklearn CV](https://scikit-learn.org/stable/modules/cross_validation.html)).
- Model selection itself overfits: selection bias can be comparable to the performance differences between algorithms; models should be evaluated with selection inside the loop (nested CV) ([Cawley & Talbot 2010](https://www.jmlr.org/papers/v11/cawley10a.html); abstract level only).
- Comparing classifiers: Dietterich compared five approximate tests; McNemar has low type I error and suits single-run algorithms, 5x2cv is slightly more powerful when 10 runs are affordable ([Dietterich 1998, via search result](https://web.engr.oregonstate.edu/~tgd/publications/dietterich-approximate-statistical-tests-nc1998.pdf); I only read a secondary abstract summary). For many datasets, Demsar recommends Wilcoxon signed-ranks (two classifiers) and Friedman + post-hoc (more) ([Demsar 2006](https://www.jmlr.org/papers/v7/demsar06a.html)).
- Drift: ML systems fail silently under dataset shift; two-sample tests on classifier-reduced features performed best among methods tested ([Rabanser et al. 2019](https://arxiv.org/abs/1810.11953)).
- Baselines: UNVERIFIED (no primary source fetched for "always compare to a trivial baseline"). Candidate: sklearn `DummyClassifier` docs.

**Common failure modes**
- Unstratified folds with rare classes (sklearn example: KFold gave a fold with no minority samples; stratification can shrink reported spread).
- Same `random_state` integer in estimator across folds vs RandomState, and non-comparable folds across separate `split` calls (sklearn common pitfalls, randomness section).
- Reporting the best CV score from a tuned grid as the generalization estimate (Cawley & Talbot).
- Treating CV fold scores as independent samples for significance tests: UNVERIFIED (Dietterich 1998 motivates corrected tests; read full paper).
- Not monitoring input shift after deploy (Rabanser).

**Practice exercise (3 h)**: Using one sklearn dataset and 3 models: (1) dummy baseline, (2) plain CV with tuned hyperparameters reported as final, (3) nested CV. Show the optimistic gap. Compare two models with McNemar (statsmodels `mcnemar`; UNVERIFIED docs not fetched) on a held-out set. Simulate covariate shift (shift a feature mean) and run a classifier two-sample test to detect it.

**Mastery check**
1. Why does reporting the best tuned CV score overstate performance, and what fixes it?
2. For two models on one test set, which test and why? For 10 datasets?
3. Which CV splitter for time series / grouped / imbalanced data?

**Primary sources**
- scikit-learn CV: https://scikit-learn.org/stable/modules/cross_validation.html ; common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
- Cawley & Talbot, JMLR 2010: https://www.jmlr.org/papers/v11/cawley10a.html
- Dietterich, Neural Computation 1998: https://web.engr.oregonstate.edu/~tgd/publications/dietterich-approximate-statistical-tests-nc1998.pdf
- Demsar, JMLR 2006: https://www.jmlr.org/papers/v7/demsar06a.html
- Rabanser et al., "Failing Loudly", NeurIPS 2019: https://arxiv.org/abs/1810.11953

---

## calibration-and-uncertainty

**Why it matters**
- Modern neural networks (unlike those a decade earlier) are poorly calibrated; depth, width, weight decay and batch norm affect it; temperature scaling (one-parameter Platt variant) is a surprisingly effective fix ([Guo et al. 2017](https://arxiv.org/abs/1706.04599)).
- LLMs: larger models are well calibrated on multiple-choice/true-false with the right format; P(True) self-evaluation works encouragingly; P(IK) generalizes partially but is poorly calibrated on new tasks ([Kadavath et al. 2022](https://arxiv.org/abs/2207.05221)).
- Reliability diagrams plot fraction of positives vs mean predicted probability per bin ([sklearn calibration](https://scikit-learn.org/stable/modules/calibration.html)).

**Common failure modes**
- Using Brier or log loss as a pure calibration measure: sklearn warns they mix calibration, resolution, and irreducible uncertainty, so a lower Brier may be a more discriminative but worse-calibrated model.
- Isotonic calibration on small data overfits (sklearn: better than sigmoid when above ~1000 samples); calibrator must be fit on data independent of training (sklearn).
- Isotonic introduces ties and can change AUC; sigmoid is strictly monotonic (sklearn).
- Calibration measured on in-distribution data and assumed to hold on new tasks (Kadavath on P(IK)).
- ECE: sklearn page does not mention it; compute from `calibration_curve` bins yourself, and note bin-count sensitivity (UNVERIFIED, no primary source fetched on ECE bias).
- Verbalized or token-probability confidence of black-box LLM APIs: UNVERIFIED, not researched.

**Practice exercise (2-3 h)**: Train a RandomForest and logistic regression on a binary dataset; plot reliability diagrams (`CalibrationDisplay`), compute Brier and a hand-coded ECE with 10 vs 20 bins; calibrate with sigmoid and isotonic via `CalibratedClassifierCV` on held-out data; show AUC and ECE before/after. Optional: have an LLM answer 200 multiple-choice questions, extract option log-probs (if available) or P(True), and plot calibration.

**Mastery check**
1. Define calibration; give a model with perfect accuracy ranking but bad calibration.
2. Why can't you read calibration from the Brier score alone?
3. When pick sigmoid over isotonic?
4. Why might an LLM's calibration on MCQ not transfer to open-ended generation?

**Primary sources**
- Guo et al., ICML 2017: https://arxiv.org/abs/1706.04599
- Kadavath et al., "Language Models (Mostly) Know What They Know": https://arxiv.org/abs/2207.05221
- scikit-learn calibration: https://scikit-learn.org/stable/modules/calibration.html

---

## error-analysis

**Why it matters**
- Aggregate accuracy hides capability-specific bugs: CheckList's behavioral tests found critical failures in commercial and SOTA models, and practitioners using it wrote about twice as many tests and found almost three times as many bugs in a user study ([Ribeiro et al., ACL 2020](https://arxiv.org/abs/2005.04118)).
- Criteria are discovered by reading outputs (criteria drift), and LLM judges need validation against human labels ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).
- Eyeball/blackbox split: Ng suggests examining ~10% of the dev set by hand and keeping the rest unseen, because eyeballing overfits ([Ng, Machine Learning Yearning, practitioner/course](https://home-wordpress.deeplearning.ai/wp-content/uploads/2022/03/andrew-ng-machine-learning-yearning.pdf); chapter details via search snippets only, so exact chapter numbers UNVERIFIED).
- Practitioner: look at traces, start with binary good/bad labels, keep reading until you stop learning new things ([Husain 2024, practitioner](https://hamel.dev/blog/posts/evals/)). That post does not use "open coding"/"axial coding" terms, so do not attribute them to it.

**Common failure modes**
- Chasing the aggregate score without categorizing failures (Ribeiro).
- Fixing criteria before looking at outputs (Shankar).
- Overfitting the examples you eyeball (Ng).
- Fixing a category by frequency alone, ignoring severity: UNVERIFIED, no source fetched.
- Slice discovery tooling (Errudite, SliceFinder): UNVERIFIED, not fetched.

**Practice exercise (3 h)**: Take 100 failures from any classifier or LLM task. Without predefined labels, write a free-text note per failure; cluster notes into 5-8 categories; count them; for the top category write 5 CheckList-style tests (minimum functionality, invariance, directional; names from CheckList, verify in the paper) and measure the pass rate. Hold out 100 unseen examples to confirm the category is real.

**Mastery check**
1. How do you decide which failure category to fix first?
2. How many failures should you read, and how do you know to stop?
3. How do you keep error analysis from overfitting your eval set?

**Primary sources**
- Ribeiro et al., CheckList, ACL 2020: https://arxiv.org/abs/2005.04118
- Shankar et al., "Who Validates the Validators?": https://arxiv.org/abs/2404.12272
- Ng, Machine Learning Yearning (practitioner): https://home-wordpress.deeplearning.ai/wp-content/uploads/2022/03/andrew-ng-machine-learning-yearning.pdf
- Husain, "Your AI Product Needs Evals" (practitioner): https://hamel.dev/blog/posts/evals/

---

## statistical-inference

**Why it matters**
- Miller's recommendations: CLT standard errors; clustered SEs when questions are grouped (adjustment up to 3x in his example); variance reduction by resampling answers and next-token probabilities; paired-difference inference when comparing models; power analysis, concluding new evals should have at least ~1,000 questions under his illustrative parameters ([Miller 2024](https://arxiv.org/html/2411.00640)).
- Significance testing in NLP is often ignored or misused; Dror et al. offer a protocol for choosing a test ([Dror et al. ACL 2018](https://aclanthology.org/P18-1128/)).
- Power is neglected in NLP; Card et al. give power-analysis practices and notebooks ([Card et al., EMNLP 2020](https://aclanthology.org/2020.emnlp-main.745), details from search abstract only; the arXiv number is 2010.06595; I first mis-guessed an ACL URL, which belonged to another paper).
- Tools: `scipy.stats.bootstrap` defaults to BCa, 9999 resamples, with a `paired` option that reuses indices; degenerate data gives NaN/warnings ([SciPy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)). `statsmodels` `TTestIndPower.solve_power` solves for any one of effect size, nobs, alpha, power ([statsmodels docs](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html); effect-size definition not on the fetched page, UNVERIFIED).

**Common failure modes**
- Ignoring clustering (passages with several questions) so CIs are too narrow (Miller).
- Unpaired comparison throwing away free variance reduction (Miller).
- Underpowered evals declaring "no difference" (Card; Miller).
- Misusing or skipping significance tests (Dror).
- Multiple comparisons across many metrics/prompts: UNVERIFIED, no source fetched.
- Lowering temperature to reduce variance can add bias (Miller sec 3.3).

**Practice exercise (2-3 h)**: Use two models' per-question 0/1 results on ~500 questions (generate with any API or small HF models). Compute: naive SE and CI; bootstrap CI with `scipy.stats.bootstrap`; paired-difference CI with `paired=True`; McNemar on discordant pairs; required N for a 2-point difference via a power calculation (note that for proportions a two-sample proportion power function is more apt than t-test; verify in statsmodels docs).

**Mastery check**
1. Why is a paired CI narrower than two independent CIs?
2. An eval has 200 items; model A beats B by 3 points. What can you conclude? What N would you need?
3. When do clustered SEs matter and how do you compute them?
4. What does a bootstrap assume that can fail?

**Primary sources**
- Miller, arXiv 2411.00640: https://arxiv.org/abs/2411.00640
- Dror et al., ACL 2018: https://aclanthology.org/P18-1128/
- Card et al., EMNLP 2020: https://aclanthology.org/2020.emnlp-main.745
- Dietterich 1998 and Demsar 2006 (see classical-ml-validation)
- SciPy bootstrap: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html ; statsmodels power: https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html

---

## nondeterminism-and-variance

**Why it matters**
- 5 LLMs x 8 tasks x 10 runs: accuracy varied by up to 15% across natural runs and best-to-worst gap up to 70%, with no model consistently repeatable even at "deterministic" settings; authors propose TARr@N and TARa@N metrics ([Atil et al. 2024](https://arxiv.org/abs/2408.04667)).
- ChatGPT code generation: share of tasks with zero equal outputs across requests was 75.76% (CodeContests), 51.00% (APPS), 47.56% (HumanEval); temp 0 reduces but does not remove nondeterminism ([Ouyang et al.](https://arxiv.org/abs/2308.02828)).
- Cause (practitioner source, single experiment): batch-size variation with non-batch-invariant kernels; 1,000 temp-0 completions of one prompt gave 80 unique outputs, vs 1 with batch-invariant kernels ([Thinking Machines, practitioner](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)).
- Budgeting: resample each question K times to cut conditional variance by 1/K with diminishing returns; use next-token probabilities when no CoT is needed ([Miller 2024](https://arxiv.org/html/2411.00640)).
- Seed/decoding sensitivity in reasoning benchmarks ([Hochlehnert et al. 2025](https://arxiv.org/abs/2504.07086)).

**Common failure modes**
- Assuming temp 0 or a fixed seed gives reproducibility (Atil, Ouyang; OpenAI says best-effort).
- Single-run comparisons of near-equal systems (Hochlehnert).
- Rerunning only failures until pass, i.e. flaky-test behavior: UNVERIFIED, no source.
- Backend changes between runs (fingerprint), see llm-basics.

**Practice exercise (2-3 h)**: Pick 50 questions with checkable answers. Run each 10 times at temp 0 and at temp 0.7. Compute per-run accuracy, between-run SD, fraction of questions with unstable answers, and Atil-style exact-match agreement across runs. Use the variance decomposition (between-question vs within-question) to decide K for a target CI width.

**Mastery check**
1. Decompose eval variance into question sampling vs generation sampling; which does K-resampling reduce?
2. How many repeats do you need to detect a 2-point change? (Needs a power calc.)
3. Why can the same request give different outputs at temp 0 on a hosted API?

**Primary sources**
- Atil et al., "Non-Determinism of 'Deterministic' LLM Settings": https://arxiv.org/abs/2408.04667
- Ouyang et al.: https://arxiv.org/abs/2308.02828
- Miller: https://arxiv.org/abs/2411.00640
- Hochlehnert et al.: https://arxiv.org/abs/2504.07086
- Practitioner: Thinking Machines: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

---

## software-testing-fundamentals

**Why it matters**
- Test pyramid (Mike Cohn, per Vocke): many small fast unit tests, fewer coarse tests, very few end-to-end tests; the "ice-cream cone" inversion is slow and flaky; test observable behavior, not implementation ([Vocke on martinfowler.com, practitioner](https://martinfowler.com/articles/practical-test-pyramid.html)).
- ML-specific adaptation: Google's ML Test Score is a rubric of 28 tests for production readiness; per one reproduction the score is the minimum across four sections (secondary; confirm in paper) ([Breck et al. 2017](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/); PDF: https://research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf).
- Behavioral testing for NLP transfers test-design ideas (see error-analysis, CheckList).
- Formal definitions of oracle, regression testing, coverage: UNVERIFIED. The ISTQB glossary fetch returned empty content; use the ISTQB glossary (https://glossary.istqb.org) or SWEBOK in a re-run.

**Common failure modes**
- Inverted pyramid / E2E-heavy suites (Vocke).
- Duplicate coverage at multiple layers (Vocke).
- Coverage as a goal: UNVERIFIED.
- Applying deterministic pass/fail to probabilistic outputs, producing flaky gates: UNVERIFIED as a sourced claim; see nondeterminism.

**Practice exercise (2 h)**: Take a small LLM function (e.g. a classifier-prompt wrapper). Write: unit tests for parsing/prompt-building (deterministic, no model), contract tests with a mocked model, a handful of live model tests run N times with a pass-rate threshold. Draw the resulting pyramid and note cost/latency per layer.

**Mastery check**
1. Which layers of an LLM app can be tested deterministically and which cannot?
2. Why do E2E tests become flaky, and how does LLM nondeterminism worsen it?
3. Give a regression test design for a prompt change.

**Primary sources**
- Breck et al., ML Test Score: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/
- ISTQB glossary (to fetch): https://glossary.istqb.org
- Practitioner: Vocke, Practical Test Pyramid: https://martinfowler.com/articles/practical-test-pyramid.html

---

## test-oracle-problem

**Why it matters**
- Canonical survey: an oracle distinguishes correct from incorrect behavior of the system under test; surveys oracle automation via modelling, specifications, contract-driven development and metamorphic testing ([Barr et al., IEEE TSE 2015, DOI 10.1109/TSE.2014.2372785](https://discovery-pp.ucl.ac.uk/id/eprint/1471263); I read search-result abstracts, not the full text).
- Metamorphic testing surveyed across 119 papers (1998-2015) with open challenges ([Segura et al., IEEE TSE 2016](https://eprints.whiterose.ac.uk/110335/); abstract level only; the 119 count comes from a search snippet attributing it to a later survey, so mark as secondary).
- NLP instantiation: CheckList uses minimum functionality, invariance and directional-expectation tests to avoid needing exact expected outputs (names from my recollection; UNVERIFIED, check [paper](https://arxiv.org/abs/2005.04118)).
- LLM-as-judge as a pseudo-oracle: GPT-4-class judges reach over 80% agreement with human preferences, but show position, verbosity and self-enhancement bias ([Zheng et al., NeurIPS 2023 D&B](https://arxiv.org/abs/2306.05685)). Judges themselves need validation against human labels ([Shankar et al.](https://arxiv.org/abs/2404.12272)).

**Common failure modes**
- Exact-match oracle on free text, giving false failures.
- Trusting an LLM judge without measuring agreement or bias (Zheng; Shankar).
- Metamorphic relations that are not truly invariant (e.g. paraphrase changes meaning): UNVERIFIED as sourced claim.
- Self-preference: judge model grades its own family favorably (Zheng, self-enhancement).

**Practice exercise (3 h)**: For a summarization or QA task, define three oracle types: (a) reference/exact-match, (b) property checks (length, contains required entities, JSON-valid) and metamorphic relations (paraphrased question must keep answer), (c) LLM judge. Run all on 50 outputs; hand-label 50; report each oracle's agreement and false-pass/false-fail rates; test judge position bias by swapping pair order.

**Mastery check**
1. Give two metamorphic relations for a QA system and one case where a relation is invalid.
2. What evidence would you need before gating CI on an LLM judge?
3. When is a partial oracle (properties) preferable to a reference answer?

**Primary sources**
- Barr et al., TSE 2015: https://discovery-pp.ucl.ac.uk/id/eprint/1471263
- Segura et al., TSE 2016: https://eprints.whiterose.ac.uk/110335/
- Zheng et al., MT-Bench / LLM-as-judge: https://arxiv.org/abs/2306.05685
- Ribeiro et al., CheckList: https://arxiv.org/abs/2005.04118

---

# Gaps and uncertainties

**Unverified or weakly verified**
- Anthropic API reference page was 1.3M characters, so the temp-0 non-determinism sentence is cited from the SDK reference mirror; OpenAI's current docs URL gave 404 (cookbook archived page used via search snippets).
- ranking metrics (NDCG), ECE, ISTQB definitions, statsmodels effect-size definition, Cohn pyramid original, Errudite/SliceFinder, benchmark contamination, multiple-comparison corrections, "baseline" guidance: not verified.
- Dietterich 1998, Cawley & Talbot, Barr, Segura, Card, Breck: read only through search-result abstracts/metadata, not full text. A wrong first fetch (an unrelated TaBERT paper at an ACL URL; an unrelated astro paper at arXiv 1706.07580) was discarded: do not cite Varoquaux's cross-validation small-sample paper without finding its real arXiv ID.
- Fetch tool returns model-summarized text; numeric claims (15%, 70%, 329 papers, 75.76%...) should be spot-checked against the PDFs before use.
- Chen et al. "Metamorphic testing: a review of challenges and opportunities" (ACM CSUR 2018) fetch returned 403; not used.

**Prerequisite and boundary issues**
- `statistical-inference` has no prerequisites, but the practice depends on `ml-metrics` (per-item correctness) and basic probability; consider `[ml-metrics]`.
- `nondeterminism-and-variance` overlaps `statistical-inference` heavily (K-resampling, power); keep one owner for power/paired-difference content and cross-link.
- `calibration-and-uncertainty` is tagged nondeterminism but the content is mostly about probability quality; the tag fits only for sampling-based uncertainty. Consider tag change. Also LLM-specific confidence (verbalized, consistency) belongs partly in a later branch.
- `error-analysis` prerequisites `[ml-metrics]` seem weak; it depends more on `evaluation-mindset` and data-slicing than metrics. Consider `[ml-metrics, evaluation-mindset]`.
- `test-oracle-problem` prerequisite `software-testing-fundamentals` is fine, but LLM-as-judge validation (agreement, bias) sits at its edge; avoid duplicating with the later judge-evaluation branch.
- `classical-ml-validation` bundles baselines + CV + drift; drift is thin on sources here and may belong with monitoring in a later branch.
- `data-splits-and-leakage` needs an LLM-era extension (benchmark contamination, train-test overlap) to be relevant to this map's core scope.
- `llm-basics-for-evaluators` mixes durable concepts with volatile ones (context sizes, parameter support); put model numbers in `landscape/` per the README rule.

**Candidates for `map/01-foundations/_candidates.md`**
- Measurement validity and reliability (construct validity, inter-annotator agreement, Cohen/Krippendorff; Raji et al. supports validity).
- Benchmark contamination and test-set reuse.
- Human annotation and agreement basics (labeling guidelines, kappa).
- Sampling and dataset design for evals (stratification, golden set sizing, clustering).
- Multiple comparisons and p-hacking in eval iteration.
- Baselines and trivial-model comparison.
- Probability refresher (distributions, CLT, bootstrap) if `statistical-inference` is too dense.

**Source count**: about 38 distinct URLs cited (about 30 fetched directly, rest from search results), of which 6 are practitioner-tagged (Thinking Machines, Ng, Husain, Vocke, plus archived OpenAI cookbook and Azure doc as vendor docs).
