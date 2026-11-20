# Research: 03-measurement-methods

As-of: 2026-11-20. Only claims read on the cited page are stated as fact. Items from my background knowledge that I did not verify are marked UNVERIFIED. All sources are primary (papers, official docs) unless tagged practitioner (none used).

## programmatic-checks

**Why it matters.** Deterministic graders are cheap and reproducible. Anthropic's eval docs list exact match (after normalizing whitespace/case), cosine similarity and ROUGE-L as code-based graders, and say to design questions so they allow automated grading (multiple choice, string match, code-graded, LLM-graded) [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests). HumanEval grades by functional correctness of generated programs against tests, not text similarity [Chen et al. 2021](https://arxiv.org/abs/2107.03374). IFEval uses 25 "verifiable instruction" types (about 500 prompts) so instruction following can be checked without humans or an LLM judge, citing the cost and bias of those alternatives [Zhou et al. 2023](https://arxiv.org/abs/2311.07911).

**Failure modes.**
- Schema-valid is not correct. OpenAI Structured Outputs guarantee schema adherence (JSON mode only guarantees valid JSON), but the docs say your code must validate business rules the schema does not express, and refusals/incomplete outputs still need handling [OpenAI docs, as-of 2026-11-20](https://developers.openai.com/api/docs/guides/structured-outputs).
- Exact match is brittle to formatting and paraphrase (design inference from the normalization caveat in the Anthropic docs, not a sourced finding).
- Code execution needs sandboxing and tests that discriminate (weak tests pass wrong code). UNVERIFIED as a specific cited claim.
- Repeated sampling changes the score: Codex solved 28.8% of HumanEval at 1 sample and 70.2% with 100 samples per problem [Chen et al.](https://arxiv.org/abs/2107.03374).

**Practice exercise.** Take about 50 prompts with JSON output. Write three graders: JSON parse, JSON-schema validation, business-rule check. Compare pass rates and hand-inspect 10 schema-valid outputs for wrong values. Then run 20 HumanEval-style problems with a test runner in a subprocess with a timeout.

**Mastery check.**
1. Why does 100% schema validity not imply 100% correctness?
2. Give a task where exact match under-counts and one where it over-counts.
3. What would an IFEval-style verifier for "mention AI at least 3 times" look like?
4. How does the number of samples change a functional-correctness score?

**Sources.** [Anthropic eval docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests); [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs); [Codex/HumanEval](https://arxiv.org/abs/2107.03374); [IFEval](https://arxiv.org/abs/2311.07911).

## reference-based-metrics

**Why it matters.** BLEU (Papineni et al., ACL 2002) and ROUGE (Lin, 2004) are the canonical overlap metrics for MT and summarization; cheap, deterministic, still used as baselines. Only bibliographic data verified; the abstracts were not on the fetched pages [BLEU](https://aclanthology.org/P02-1040/), [ROUGE](https://aclanthology.org/W04-1013/).

**Failure modes.**
- BLEU is a parameterized metric. Tokenization/normalization differences changed scores by up to 1.8 BLEU in Post's measurements, so cross-paper comparisons are invalid without a standardized tool such as sacreBLEU [Post 2018](https://arxiv.org/abs/1804.08771).
- Weak correlation with human judgment: G-Eval's authors state BLEU and ROUGE have "relatively low correlation with human judgments" for NLG [Liu et al. 2023](https://arxiv.org/abs/2303.16634). Callison-Burch et al. "Re-evaluating the Role of Bleu" is the classic critique, but I could not read its abstract, so its claims are UNVERIFIED [ACL Anthology](https://aclanthology.org/E06-1032/).
- Single-reference dependence and paraphrase blindness. UNVERIFIED.

**Practice exercise.** Take 30 summaries or translations with references. Compute BLEU (sacreBLEU, record its signature) and ROUGE-1/2/L. Write 10 meaning-preserving paraphrases and 10 fluent but wrong outputs. Show where the scores invert relative to your own judgment.

**Mastery check.**
1. Why must a BLEU report include its configuration signature?
2. Construct an output with high ROUGE and bad quality, and the reverse.
3. When are these metrics still a reasonable choice?

**Sources.** [BLEU](https://aclanthology.org/P02-1040/); [ROUGE](https://aclanthology.org/W04-1013/); [sacreBLEU/Post](https://arxiv.org/abs/1804.08771); [G-Eval](https://arxiv.org/abs/2303.16634).

## embedding-similarity-metrics

**Why it matters.** BERTScore matches candidate and reference tokens using contextual BERT embeddings rather than exact n-grams. It was tested on 363 MT and captioning systems and reported better correlation with human judgments than existing metrics [Zhang et al. 2020](https://arxiv.org/abs/1904.09675). Sentence-BERT makes sentence-level embedding comparison cheap: finding the most similar pair among 10,000 sentences takes about 50 million BERT pair inferences (about 65 hours) in the pair-input setup [Reimers & Gurevych 2019](https://arxiv.org/abs/1908.10084). Anthropic's docs use cosine similarity of sentence embeddings as a consistency grader [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests).

**Failure modes.**
- Geometry: contextual embeddings are anisotropic (not isotropic in any layer of ELMo/BERT/GPT-2), which makes raw cosine values hard to interpret [Ethayarajh 2019](https://arxiv.org/abs/1909.00512).
- Cosine captures topical/semantic closeness and can miss negation, entity or number swaps. UNVERIFIED (no source read on this).
- Scores depend on the embedding model/layer and are not comparable across models. UNVERIFIED.

**Practice exercise.** Embed 40 sentence pairs (20 paraphrases, 10 negations, 10 entity/number swaps) with a Sentence-BERT model. Plot cosine by class and find the separating threshold. Compute BERTScore on the same pairs. Report which classes fail.

**Mastery check.**
1. What does a cosine of 0.85 mean for a given embedding model?
2. Why might negation pairs score high?
3. How would you calibrate a threshold against human labels?

**Sources.** [BERTScore](https://arxiv.org/abs/1904.09675); [SBERT](https://arxiv.org/abs/1908.10084); [Ethayarajh](https://arxiv.org/abs/1909.00512).

## human-evaluation

**Why it matters.** Human judgment is the reference that automatic metrics and LLM judges are validated against. OpenAI's guide says human labels are the ground truth for calibrating judges and that expert review is costly but needed for calibration [OpenAI eval best practices, as-of 2026-11-20](https://developers.openai.com/api/docs/guides/evaluation-best-practices). Anthropic's docs list expert rubrics as a qualitative method but also recommend volume over quality: more automatically graded questions beat fewer hand-graded ones [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests).

**Failure modes.**
- Untrained crowd raters could not tell GPT-3 text from human text (chance level). Quick training raised accuracy only to about 55%, not significantly in all domains, and raters gave conflicting reasons [Clark et al. 2021](https://arxiv.org/abs/2107.00061).
- Inconsistent design across NLG papers; van der Lee et al. review practice and propose best practices [van der Lee et al. 2019](https://aclanthology.org/W19-8643/).
- Underpowered rating studies: typical human-rating designs are likely underpowered to detect small model differences [Card et al. 2020](https://arxiv.org/abs/2010.06595).
- Criteria drift: people define criteria while grading outputs, so rubrics change as raters see outputs [Shankar et al. 2024](https://arxiv.org/abs/2404.12272).

**Practice exercise.** Write a 3-criterion rubric with anchors. Have two raters (you on two different days is acceptable) score 40 outputs. Time it, compute cost per item, note rubric edits needed after the first 10 items, and revise.

**Mastery check.**
1. Name design choices that decide validity (rater qualification, rubric anchors, randomized order); map them to van der Lee (list itself UNVERIFIED).
2. When is human eval worth its cost against an LLM judge?
3. How many items do you need to detect a 5-point difference? (Card et al. power analysis.)

**Sources.** [van der Lee et al.](https://aclanthology.org/W19-8643/); [Clark et al.](https://arxiv.org/abs/2107.00061); [Card et al.](https://arxiv.org/abs/2010.06595); [Shankar et al.](https://arxiv.org/abs/2404.12272); [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## inter-rater-agreement

**Why it matters.** Agreement quantifies whether labels are reliable enough to serve as ground truth. Artstein & Poesio's survey is the CL reference on inter-coder agreement coefficients; the fetched page had no abstract, so its content claims are UNVERIFIED [Artstein & Poesio 2008](https://aclanthology.org/J08-4004/). Thakur et al. argue percent agreement alone is insufficient for judging LLM judges: "judges with high percent agreement can still assign vastly different scores" [Thakur et al. 2024](https://arxiv.org/abs/2406.12624).

**Failure modes.**
- Reporting raw percent agreement, which ignores chance agreement. UNVERIFIED here (Artstein & Poesio cover it).
- Kappa prevalence/skew paradox and arbitrary Landis-Koch bands. UNVERIFIED; Cohen 1960 and Landis & Koch 1977 were not read.
- Using nominal kappa for ordinal scales when weighted kappa or Krippendorff's alpha fits. UNVERIFIED.

**Practice exercise.** Use the two-rater data from human-evaluation. Compute percent agreement, Cohen's kappa, weighted kappa (sklearn) and Krippendorff's alpha (`krippendorff` package). Build a skewed 95/5 label set and show high agreement with low kappa. Bootstrap a CI on kappa.

**Mastery check.**
1. Why can 90% agreement coexist with kappa near 0?
2. When do you use Fleiss' kappa vs Krippendorff's alpha?
3. What agreement level makes labels usable as ground truth for a judge, and why is there no universal cutoff?

**Sources.** [Artstein & Poesio](https://aclanthology.org/J08-4004/); [Thakur et al.](https://arxiv.org/abs/2406.12624). Originals (Cohen 1960, Fleiss 1971, Krippendorff) still to locate; see Gaps.

## llm-as-judge

**Why it matters.** Strong LLM judges can approximate human preference at scale. Zheng et al. report GPT-4-class judges reaching over 80% agreement with controlled and crowdsourced human preferences, comparable to human-human agreement [Zheng et al. 2023](https://arxiv.org/abs/2306.05685). G-Eval uses chain-of-thought and a form-filling paradigm and reports Spearman 0.514 with humans on summarization with GPT-4 [Liu et al. 2023](https://arxiv.org/abs/2303.16634). Prometheus (open 13B judge using a user rubric and reference) reports Pearson 0.897 with humans on 45 custom rubrics (GPT-4 0.882, ChatGPT 0.392) [Kim et al. 2023](https://arxiv.org/abs/2310.08491). Vendor guidance: use a different model from the generator, constrain output format ("Output only 'yes' or 'no'"), and use binary or Likert formats with clear criteria [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests). OpenAI: start with a strong judge, add reasoning before scoring, prefer pairwise or pass/fail over open-ended scores, validate against human annotations [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

**Failure modes.**
- Position, verbosity and self-enhancement bias, plus limited reasoning ability [Zheng et al.](https://arxiv.org/abs/2306.05685).
- Possible bias toward LLM-generated text (preliminary) [G-Eval](https://arxiv.org/abs/2303.16634).
- Proprietary judges have uncontrolled versioning and cost [Prometheus](https://arxiv.org/abs/2310.08491).
- Judges inherit LLM flaws, so they must be validated against human grades; criteria are subjective and iterative [Shankar et al.](https://arxiv.org/abs/2404.12272).

**Practice exercise.** Take 50 outputs from a small task with your own pass/fail labels. Write a judge prompt with a rubric, a reasoning step and a strict output format. Run it with two judge models. Report agreement with your labels (kappa) and the confusion matrix. Iterate the rubric once.

**Mastery check.**
1. Why validate a judge against human labels before using it for regression gating?
2. Compare binary, Likert and pairwise judging formats.
3. Show what changes when the judge shares a model family with the generator.

**Sources.** [MT-Bench paper](https://arxiv.org/abs/2306.05685); [G-Eval](https://arxiv.org/abs/2303.16634); [Prometheus](https://arxiv.org/abs/2310.08491); [Shankar et al.](https://arxiv.org/abs/2404.12272); [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests); [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## judge-bias-and-calibration

**Why it matters.** Each bias can shift rankings. Reordering responses changed outcomes; Vicuna-13B beat ChatGPT on 66 of 80 queries under one ordering with ChatGPT as evaluator. Proposed calibration: multiple evidence, balanced position (aggregate across orders), human-in-the-loop for hard cases [Wang et al. 2023](https://arxiv.org/abs/2305.17926).

**Failure modes.**
- Self-preference: evaluators score their own outputs higher; strength correlates linearly with self-recognition ability [Panickssery et al. 2024](https://arxiv.org/abs/2404.13076). Alternative account: GPT-4 prefers lower-perplexity (more familiar) text whether or not self-generated [Wataoka et al. 2024](https://arxiv.org/abs/2410.21819).
- Length bias: AlpacaEval favored longer outputs. A regression-based length control raised Spearman correlation with Chatbot Arena from 0.94 to 0.98 [Dubois et al. 2024](https://arxiv.org/abs/2404.04475).
- High percent agreement can hide very different scores, so use chance-corrected metrics [Thakur et al.](https://arxiv.org/abs/2406.12624).
- Verbosity and position bias are named in [Zheng et al.](https://arxiv.org/abs/2306.05685); OpenAI advises controlling for response length [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

**Practice exercise.** Build 30 pairs. Run the judge in both orders and report the flip rate. Pad one answer in each pair with filler and measure win-rate change. Add a self-vs-other condition if you have two model families. Apply balanced-position aggregation and report what changes.

**Mastery check.**
1. Quantify position bias from swapped-order runs.
2. How does length control work (counterfactual GLM)?
3. Design a calibration set: size, label source, metric, pass threshold for the judge.

**Sources.** [Wang et al.](https://arxiv.org/abs/2305.17926); [Panickssery et al.](https://arxiv.org/abs/2404.13076); [Wataoka et al.](https://arxiv.org/abs/2410.21819); [Dubois et al.](https://arxiv.org/abs/2404.04475); [Thakur et al.](https://arxiv.org/abs/2406.12624); [Zheng et al.](https://arxiv.org/abs/2306.05685).

## pairwise-comparison-and-ranking

**Why it matters.** Pairwise preference is easier for judges (OpenAI: "LLMs are better at discriminating between options"; pairwise or pass/fail is more reliable than open-ended scores) [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices). Chatbot Arena collects crowdsourced pairwise votes (over 240K at paper time) and ranks models with statistical methods; the abstract does not name Bradley-Terry, so confirm in the full paper [Chiang et al. 2024](https://arxiv.org/abs/2403.04132). MT-Bench uses judge-based pairwise comparison [Zheng et al.](https://arxiv.org/abs/2306.05685).

**Failure modes.**
- Leaderboard distortion from undisclosed private testing and selective disclosure (27 private Meta variants cited) and unequal sampling favoring proprietary models [Singh et al. 2025](https://arxiv.org/abs/2504.20879).
- Length and style confounds [Dubois et al.](https://arxiv.org/abs/2404.04475).
- Position bias in judge-based pairs [Wang et al.](https://arxiv.org/abs/2305.17926).
- Intransitivity and non-Bradley-Terry structure; original Bradley-Terry (1952) and Elo derivations. UNVERIFIED (not read).

**Practice exercise.** Generate pairwise outcomes among 4 prompt variants on 40 inputs using a judge in both orders. Fit Bradley-Terry by logistic regression and compare with online Elo. Bootstrap CIs on ratings and report which ranks are statistically indistinguishable.

**Mastery check.**
1. Derive win probability from the rating difference.
2. Why does Elo depend on game order but a Bradley-Terry fit does not?
3. How many comparisons separate two models with a 55% win rate?

**Sources.** [Chatbot Arena](https://arxiv.org/abs/2403.04132); [Leaderboard Illusion](https://arxiv.org/abs/2504.20879); [MT-Bench paper](https://arxiv.org/abs/2306.05685); [OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## confidence-intervals-for-evals

**Why it matters.** Miller argues evals are experiments: questions are samples from a super-population; he supplies formulas for analysis, two-model comparison and planning [Miller 2024](https://arxiv.org/abs/2411.00640). Card et al. find underpowered experiments common in NLP; e.g. MT test sets of 2,000 sentences have about 75% power to detect a 1 BLEU difference [Card et al. 2020](https://arxiv.org/abs/2010.06595). Dror et al. give a protocol for choosing significance tests and report testing is often overlooked or misapplied in ACL/TACL 2017 papers [Dror et al. 2018](https://aclanthology.org/P18-1128/). BetterBench found most of 24 assessed benchmarks do not report statistical significance [Reuel et al. 2024](https://arxiv.org/abs/2411.12990).

**Failure modes.**
- CLT-based intervals on small benchmarks usually dramatically underestimate uncertainty with fewer than a few hundred items [Bowyer et al. 2025](https://arxiv.org/abs/2503.01747).
- Ignoring paired structure when comparing two models on the same questions (Miller covers two-model comparison; detail UNVERIFIED beyond the abstract).
- Ignoring run-to-run sampling variance and clustered questions. UNVERIFIED beyond the abstract.
- Multiple comparisons and selective reporting; related evidence: [Singh et al.](https://arxiv.org/abs/2504.20879).

**Practice exercise.** Take per-item 0/1 results of two prompts on 200 items. Compute Wald, Wilson and bootstrap CIs, and a paired bootstrap on the difference. Subsample to 30 items and see which interval breaks down. Run a power calculation for a 3-point difference.

**Mastery check.**
1. When do Wilson, bootstrap or Bayesian intervals beat the Wald CLT interval?
2. Why is a paired test more powerful for comparing two models?
3. How many items detect a 2-point accuracy gain at 80% power?

**Sources.** [Miller](https://arxiv.org/abs/2411.00640); [Bowyer et al.](https://arxiv.org/abs/2503.01747); [Card et al.](https://arxiv.org/abs/2010.06595); [Dror et al.](https://aclanthology.org/P18-1128/); [BetterBench](https://arxiv.org/abs/2411.12990).

## eval-harness-design

**Why it matters.** Biderman et al., drawing on three years of building lm-eval, report that results shift with evaluation setup, comparisons are hard to make fair, and undocumented conventions hurt reproducibility [Biderman et al. 2024](https://arxiv.org/abs/2405.14782). Inspect (UK AI Security Institute and Meridian Labs) defines an eval as a Task of dataset, solver and scorer [Inspect docs, as-of 2026-11-20](https://inspect.aisi.org.uk/). lm-evaluation-harness provides YAML task configs, request/result caching, per-sample logging (`--log_samples`) and output paths [lm-eval README, as-of 2026-11-20](https://github.com/EleutherAI/lm-evaluation-harness). HELM releases raw prompts and completions and a modular toolkit and evaluates all models on the same scenarios/metrics [Liang et al. 2022](https://arxiv.org/abs/2211.09110).

**Failure modes.**
- Hidden setup differences (prompt format, few-shot, tokenization) change scores [Biderman et al.](https://arxiv.org/abs/2405.14782); similar sensitivity appears as 4-5% prompt-style variation on MMLU [MMLU-Pro](https://arxiv.org/abs/2406.01574).
- Not storing raw outputs, so graders cannot be rerun; HELM's raw-output release is the counterexample [HELM](https://arxiv.org/abs/2211.09110).
- No version pinning of dataset/grader/model. The lm-eval README does not describe a versioning feature (checked), so design it yourself.

**Practice exercise.** Build a mini harness (about 150 lines): JSONL dataset, runner with cache keyed by (model, prompt, params), pluggable graders, results store with config hash and git SHA, and a rerun that reuses cached outputs. Compare with an Inspect task on the same data.

**Mastery check.**
1. List what must be logged to reproduce a score.
2. How do you re-grade without re-calling the model?
3. What breaks when the prompt template changes but the dataset ID does not?

**Sources.** [Biderman et al.](https://arxiv.org/abs/2405.14782); [Inspect](https://inspect.aisi.org.uk/); [lm-eval](https://github.com/EleutherAI/lm-evaluation-harness); [HELM](https://arxiv.org/abs/2211.09110).

## public-benchmarks

**Why it matters.** Benchmarks give shared, comparable measurement. MMLU: 57 tasks, most 2020 models near chance [Hendrycks et al. 2021](https://arxiv.org/abs/2009.03300). HELM: 42 scenarios and 7 metrics (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) across 30 models [Liang et al.](https://arxiv.org/abs/2211.09110). SWE-bench: 2,294 real GitHub issue tasks over 12 Python repos; best model at publication resolved 1.96% [Jimenez et al. 2023](https://arxiv.org/abs/2310.06770). HumanEval, IFEval and MT-Bench are covered above. Successors: MMLU-Pro (10 options, 16-33% accuracy drop) [Wang et al. 2024](https://arxiv.org/abs/2406.01574); SuperGPQA (285 disciplines; top score 61.82% at paper time) [SuperGPQA](https://arxiv.org/abs/2502.14739).

**Failure modes.**
- Label noise: MMLU-Redux estimates 6.49% of MMLU questions contain errors (57% in the Virology sample) [Gema et al. 2024](https://arxiv.org/abs/2406.04127).
- Prompt sensitivity (MMLU-Pro above).
- Reading a score without its setup (prompt, shots, grader); see eval-harness-design.
- Aggregate hides uneven per-task performance [Hendrycks et al.](https://arxiv.org/abs/2009.03300).

**Practice exercise.** Run a small open model on 100-item slices of two benchmarks via lm-eval or Inspect. Vary prompt format and number of shots. Report scores with CIs and a per-subject breakdown. Read 20 items for label errors.

**Mastery check.**
1. State what construct a benchmark measures and what it does not.
2. How would you decide whether a 1-point leaderboard gap is real?
3. Why prefer your own task eval to a public score for product decisions?

**Sources.** [MMLU](https://arxiv.org/abs/2009.03300); [HELM](https://arxiv.org/abs/2211.09110); [SWE-bench](https://arxiv.org/abs/2310.06770); [MMLU-Redux](https://arxiv.org/abs/2406.04127); [MMLU-Pro](https://arxiv.org/abs/2406.01574).

## benchmark-limitations

**Why it matters.** Raji et al. argue that treating a few influential benchmarks as proxies for "general" ability is a construct-validity problem [Raji et al. 2021](https://arxiv.org/abs/2111.15366). BetterBench scored 24 benchmarks against 46 lifecycle best practices and found wide quality variation and little significance reporting [Reuel et al.](https://arxiv.org/abs/2411.12990).

**Failure modes.**
- Contamination: benchmark content in training data yields unreliable scores [Xu et al. survey](https://arxiv.org/abs/2406.04244).
- Memorization/overfitting: on fresh GSM1k, accuracy dropped up to 8% vs GSM8k for some models, correlated with likelihood of reproducing GSM8k examples; frontier models showed little overfitting [Zhang et al. 2024](https://arxiv.org/abs/2405.00332).
- Label errors and saturation: [Gema et al.](https://arxiv.org/abs/2406.04127); successors added difficulty [MMLU-Pro](https://arxiv.org/abs/2406.01574).
- Leaderboard gaming: selective disclosure, private testing, unequal data access [Singh et al.](https://arxiv.org/abs/2504.20879).
- Score vs real-world gap (construct validity) [Raji et al.](https://arxiv.org/abs/2111.15366).

**Practice exercise.** Pick one benchmark. Audit it: read 50 items for errors, check for public answer keys, and compare a small model's perplexity on items vs paraphrased versions. Score it on a subset of BetterBench criteria and write a one-page verdict.

**Mastery check.**
1. Differentiate contamination, overfitting and saturation, with a test for each.
2. What does GSM1k show and not show?
3. Score a benchmark against 5 BetterBench-style criteria.

**Sources.** [Raji et al.](https://arxiv.org/abs/2111.15366); [BetterBench](https://arxiv.org/abs/2411.12990); [Xu et al.](https://arxiv.org/abs/2406.04244); [GSM1k](https://arxiv.org/abs/2405.00332); [MMLU-Redux](https://arxiv.org/abs/2406.04127); [Leaderboard Illusion](https://arxiv.org/abs/2504.20879).

## Gaps and uncertainties

- Abstracts for BLEU, ROUGE, Callison-Burch and Artstein & Poesio were missing from fetched pages; only titles/authors verified. Fetch the PDFs before filling those nodes.
- Not located: Cohen 1960, Fleiss 1971, Krippendorff (alpha), Landis & Koch 1977, Bradley-Terry 1952, Elo, Efron bootstrap (all UNVERIFIED), and the formal pass@k definition (read the Codex paper body).
- Many claims come from abstracts only. Bowyer's methods, Miller's recommendations and Chatbot Arena's Bradley-Terry use need full-text reads.
- Prerequisites referenced but outside this branch (confirm they exist): `ml-metrics`, `statistical-inference`, `nondeterminism-and-variance`, `rubric-design`, `annotation-guidelines`, `test-oracle-problem`, `metric-selection`, `contamination-and-leakage`. Suggest adding `confidence-intervals-for-evals` as a prerequisite of `judge-bias-and-calibration` (flip-rate and agreement need uncertainty), and `public-benchmarks` knowledge to `eval-harness-design`.
- Boundary: `benchmark-limitations` overlaps `contamination-and-leakage`; keep detection methods there and measurement validity here.
- Candidates for `_candidates.md`: pass@k estimation and code-execution sandboxing; LLM-judge prompt patterns (rubric, CoT, reference-guided); reward/preference model evaluation; reference-free MT/summary quality estimators such as COMET/BLEURT (UNVERIFIED, not researched); retrieval metrics (nDCG, recall@k; may belong to a RAG branch); calibration metrics (ECE); power analysis and sample-size planning; style-controlled arena ranking; agent/trajectory grading; human-eval platform and cost management; metric meta-evaluation (Kendall tau against humans).

## Landscape items

(as-of 2026-11-20 unless stated)
- Inspect AI (UK AISI and Meridian Labs): https://inspect.aisi.org.uk/
- EleutherAI lm-evaluation-harness (v0.4.x referenced in README): https://github.com/EleutherAI/lm-evaluation-harness
- Provider eval docs moved to platform.claude.com and developers.openai.com (301 redirects seen); URLs are volatile.
- Chatbot Arena leaderboard and the Leaderboard Illusion critique (2025): https://arxiv.org/abs/2504.20879
- Benchmarks: MMLU, MMLU-Pro, MMLU-Redux, GSM8k/GSM1k, SWE-bench, HumanEval, IFEval, SuperGPQA, HELM. Scores quoted are at paper dates (2020-2025), not current.
- Judges: GPT-4 and Prometheus 13B (2023); judge model choice is volatile.
- BetterBench living repository of benchmark assessments: https://arxiv.org/abs/2411.12990
