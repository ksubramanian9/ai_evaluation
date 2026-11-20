# Research: 04-system-specific-evals

Researched 2026-11-20. Claims cite the source that owns them (abstract-level reads unless noted). "Exercise" and "Mastery check" content is proposed design (not a sourced claim). "[V]" = volatile, goes to landscape/. Practitioner sources are tagged.

## rag-retrieval-evals

**Why it matters.** Retrieval is a separable component; RAG evaluation surveys treat retrieval (relevance) and generation (accuracy, faithfulness) as distinct evaluation targets ([Yu et al. survey, arXiv 2405.07437](https://arxiv.org/abs/2405.07437)). nDCG extends precision/recall to graded relevance and applies a rank discount so later results count less ([Järvelin & Kekäläinen, ACM TOIS 20(4) 2002, DOI 10.1145/582415.582418](https://dl.acm.org/doi/10.1145/582415.582418); abstract confirmed via search summary, page itself returned 403). Zero-shot behaviour varies by domain: BEIR (18 datasets, 10 systems) found BM25 a robust baseline, with re-ranking/late-interaction best on average but costly, and dense/sparse often underperforming ([BEIR, NeurIPS 2021 D&B](https://arxiv.org/abs/2104.08663)).

**Failure modes.**
- Optimizing on one in-domain set; BM25 baseline unexpectedly strong out of domain (BEIR above).
- Incomplete relevance labels penalize correct unjudged hits (UNVERIFIED; textbook chapter fetch failed: nlp.stanford.edu/IR-book).
- Ignoring graded relevance when using binary recall@k (motivation for nDCG, Järvelin & Kekäläinen above).
- Measuring retrieval only, missing that the generator ignores context (see rag-end-to-end-evals).

**Exercise.** Take ~100 questions over a small corpus (e.g. a BEIR subset such as SciFact via the BEIR repo, [arXiv 2104.08663](https://arxiv.org/abs/2104.08663)). Implement recall@k, MRR, nDCG@k by hand, compare BM25 vs one embedding model, and use sentence-transformers' `InformationRetrievalEvaluator` as a cross-check; it reports MRR, NDCG, MAP, accuracy@k, precision/recall@k ([Sentence-Transformers docs, as of 2026-11-20 [V]](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html)). Bootstrap a CI on the difference.

**Mastery check.** (1) When do MRR and nDCG rank two systems differently? Construct an example. (2) Why can recall@k be high yet answers wrong? (3) Compute nDCG@5 by hand for a graded list. (4) How would unjudged documents bias your comparison?

**Sources.** BEIR; Järvelin & Kekäläinen 2002; Yu et al. 2405.07437; Sentence-Transformers docs (practitioner/library docs).

## rag-generation-evals

**Why it matters.** Faithfulness/groundedness and answer relevance can be scored without gold answers: RAGAS is a "reference-free" framework covering retrieval relevance, faithfulness to context, and generation quality ([arXiv 2309.15217](https://arxiv.org/abs/2309.15217)). ARES trains lightweight judges on synthetic data to score context relevance, answer faithfulness, answer relevance, and uses prediction-powered inference with a few hundred human annotations to correct judge error (NAACL 2024, [arXiv 2311.09476](https://arxiv.org/abs/2311.09476)). FActScore splits text into atomic facts and measures the share supported by a knowledge source; ChatGPT scored ~58% on biographies; automated estimator error <2% (EMNLP 2023, [arXiv 2305.14251](https://arxiv.org/abs/2305.14251)). The "RAG triad" (context relevance, groundedness via claim decomposition, answer relevance) is a practitioner framing ([TruLens docs](https://www.trulens.org/getting_started/core_concepts/rag_triad/), practitioner/library).

**Failure modes.**
- Model answers from parametric memory, correct but ungrounded (UNVERIFIED as a named failure; inferable from groundedness definition above).
- Models fail to reject when context lacks the answer, and are misled by counterfactual or noisy documents ([RGB, arXiv 2309.01431](https://arxiv.org/abs/2309.01431): noise robustness, negative rejection, information integration, counterfactual robustness; models struggled with the latter three).
- Judge error uncorrected: ARES motivates PPI for this reason (above).
- Metric tool lists change names/definitions: RAGAS currently lists Context Precision, Context Recall, Faithfulness, Response Relevancy, Noise Sensitivity [V] ([docs, as of 2026-11-20](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)).

**Exercise.** Build 30 (question, context, answer) triples, 10 deliberately ungrounded, 10 with irrelevant context. Implement a claim-decomposition faithfulness judge (FActScore-style) with any LLM, hand-label, report agreement (Cohen's kappa) and compare to a RAGAS faithfulness run.

**Mastery check.** (1) Distinguish faithfulness from answer relevance with one example each way. (2) Why can a faithful answer be wrong? (3) How does PPI use human labels? (4) Design a negative-rejection test case.

**Sources.** RAGAS; ARES; FActScore; RGB; TruLens (practitioner); RAGAS docs.

## rag-end-to-end-evals

**Why it matters.** RAG's "hybrid structure and reliance on dynamic knowledge sources" makes evaluation hard; the survey proposes a unified process (Auepora) to organize targets and benchmarks ([arXiv 2405.07437](https://arxiv.org/abs/2405.07437)). CRAG (4,409 QA pairs, mock web/KG APIs, 5 domains) reports straightforward RAG lifts accuracy only 34% to 44%, industry systems answer 63% without hallucination, and accuracy falls for dynamic facts, tail entities, complex queries ([arXiv 2406.04744](https://arxiv.org/abs/2406.04744)).

**Failure modes.**
- Component metrics look fine, end-to-end poor (or the reverse); can't attribute (UNVERIFIED as stated; the attribution framing is from the node description).
- Static benchmarks miss time-varying facts (CRAG above).
- Hallucination vs "missing" scoring: CRAG reports accuracy and hallucination rates separately (abstract); grading details UNVERIFIED (repo github.com/facebookresearch/CRAG not read).

**Exercise.** On the same 50-question set as the retrieval and generation exercises, label each failure as retrieval miss / ranking / generation unfaithful / generation irrelevant / data gap; produce a confusion-style attribution table and one oracle experiment (inject gold context) to bound generator error.

**Mastery check.** (1) Given recall@5=0.9 and answer accuracy=0.6, list candidate causes and tests. (2) What does gold-context injection tell you? (3) Why report hallucination rate separately from accuracy?

**Sources.** Yu et al. survey; CRAG; RGB.

## code-generation-evals

**Why it matters.** Functional correctness by unit tests, with unbiased pass@k: generate n>=k samples, count c correct, and compute 1 - C(n-c,k)/C(n,k); the naive 1-(1-p)^k estimate is biased; BLEU is unreliable for functional correctness ([Chen et al., Codex, arXiv 2107.03374](https://arxiv.org/pdf/2107.03374), sec. 2.1; read via local pdftotext). HumanEval is 164 hand-written problems, avg 7.7 tests; the paper built a gVisor sandbox for untrusted code (same, sec. 2.2-2.3). Codex solved 28.8% with one sample, 70.2% with 100 ([abstract](https://arxiv.org/abs/2107.03374)).

**Failure modes.**
- Weak tests: EvalPlus (~80x more tests) dropped pass@k by 19.3-28.9% and changed rankings across 26 LLMs ([arXiv 2305.01210](https://arxiv.org/abs/2305.01210)).
- Contamination: LiveCodeBench collects post-cutoff problems (400, May 2023-May 2024), notes possible overfitting to HumanEval/MBPP ([arXiv 2403.07974](https://arxiv.org/abs/2403.07974)).
- Insecure code passing tests: ~40% of 1,689 Copilot programs over 89 scenarios were vulnerable ([Pearce et al., arXiv 2108.09293](https://arxiv.org/abs/2108.09293)); CyberSecEval measures propensity to generate insecure code ([arXiv 2312.04724](https://arxiv.org/abs/2312.04724)).
- Repo-level realism: SWE-bench is 2,294 real issues from 12 Python repos; Claude 2 solved 1.96% at release (ICLR 2024, [arXiv 2310.06770](https://arxiv.org/abs/2310.06770)); how solutions are checked is UNVERIFIED from the abstract (tests in paper body, not read).
- Running untrusted code outside a sandbox (Codex paper sec. 2.3).

**Exercise.** Use 20 HumanEval problems (github.com/openai/human-eval, cited in Codex paper). Sample n=10 per problem from any model at temp 0.8, compute pass@1/pass@5 with the Fig. 3 estimator, then add 5 extra edge-case tests per problem and recompute. Run a static analyzer (e.g. Bandit) on outputs for a security pass rate. Execute in Docker.

**Mastery check.** (1) Derive why 1-(1-p)^k is biased. (2) Why did EvalPlus change rankings? (3) Design a test-suite-adequacy check (mutation testing). (4) What isolation do you need to run model code?

**Sources.** Codex; EvalPlus; LiveCodeBench; SWE-bench; Pearce et al.; CyberSecEval.

## tool-use-evals

**Why it matters.** Tool calls can be checked programmatically. BFCL uses AST matching (function name, required params, no hallucinated params, strict types) and executable evaluation, with categories simple/multiple/parallel/parallel-multiple and relevance detection (no call when none fits) ([Gorilla BFCL blog, snapshot Aug 2024; later V2/V3 added live data and multi-turn](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)). API-Bank assesses planning, retrieving, calling (73 tools, 314 dialogues, 753 calls) ([arXiv 2304.08244](https://arxiv.org/abs/2304.08244)). ToolBench: 16,464 RapidAPI APIs, 49 categories, with ToolEval automatic evaluator ([arXiv 2307.16789](https://arxiv.org/abs/2307.16789)). tau-bench evaluates by comparing final database state to goal state and introduces pass^k ([arXiv 2406.12045](https://arxiv.org/abs/2406.12045)).

**Failure modes.**
- Rigid typing/implicit conversion errors (5% written as 5 vs 0.05), non-executable calls, omitted REST URLs (BFCL blog).
- Calling a tool when none is relevant (BFCL relevance detection).
- Schema-valid but wrong values: structured-output constraints guarantee schema adherence, not correctness; business rules must be validated by the app ([OpenAI Structured Outputs guide, as of 2026-11-20 [V]](https://developers.openai.com/api/docs/guides/structured-outputs)).
- Inconsistency across trials: pass^8 <25% in tau-bench retail (abstract).
- Over-strict AST matching penalizes valid alternatives (inference; BFCL notes list-order and strict type rules).

**Exercise.** Define 5 tools (JSON schema). Write 40 prompts including 10 needing no tool and 10 parallel. Grade with a code checker: name match, jsonschema validation, argument equality with normalization, and executable result match against a mock. Report per-category accuracy and 5-trial pass^k.

**Mastery check.** (1) AST vs execution grading trade-offs. (2) How do you test "should not call"? (3) Why is schema validity insufficient? (4) Compute pass^k from per-task success rates.

**Sources.** BFCL blog; API-Bank; ToolBench; tau-bench; OpenAI docs.

## agent-task-success-evals

**Why it matters.** Outcome-based grading, environment-state checked: Anthropic defines outcome as final environment state (e.g. reservation exists in DB), recommends grading outcome rather than rigid step sequences, 20-50 tasks from real failures to start, and distinguishes pass@k from pass^k ([Anthropic Engineering, "Demystifying evals for AI agents"](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), provider engineering doc). Benchmarks: WebArena uses functional correctness; best GPT-4 agent 14.41% vs human 78.24% ([arXiv 2307.13854](https://arxiv.org/abs/2307.13854)); GAIA 466 questions, humans 92% vs GPT-4+plugins 15% ([arXiv 2311.12983](https://arxiv.org/abs/2311.12983)); OSWorld 369 tasks with per-task execution-based scripts, human >72.36% vs best model 12.24% ([arXiv 2404.07972](https://arxiv.org/abs/2404.07972)); AgentBench 8 environments, ICLR 2024 ([arXiv 2308.03688](https://arxiv.org/abs/2308.03688)). Scores are as of paper date; current frontier numbers are much higher [V] (UNVERIFIED, not looked up).

**Failure modes.**
- Broken tasks/grader bugs (near-0% pass often means a flawed eval); agents cheating; shared state between trials; saturation (Anthropic doc).
- One-sided evals (only testing when behavior should occur).
- Single-run reporting hides unreliability (tau-bench pass^k).
- Poor long-term reasoning, decision-making, instruction following dominate failures in AgentBench (abstract).

**Exercise.** Build a toy agent task suite (e.g. 20 tasks over a SQLite DB: "refund order X"), a state-based grader, run 5 trials each, report pass@1, pass@5, pass^5; hand-inspect 5 transcripts for grader bugs.

**Mastery check.** (1) Why state-based over claim-based success? (2) When pass@k vs pass^k? (3) Diagnose a 0% task. (4) Design a capability vs regression split.

**Sources.** Anthropic doc (provider); tau-bench; WebArena; GAIA; OSWorld; AgentBench.

## agent-trajectory-evals

**Why it matters.** Success rate alone "reveals little about where an agent succeeds or fails along the way"; AgentBoard adds a fine-grained progress rate ([arXiv 2401.13178](https://arxiv.org/abs/2401.13178); computation details UNVERIFIED). Agent-as-a-Judge gives intermediate feedback on the process; on DevAI (55 tasks, 365 requirements) it is reported to outperform LLM-as-a-judge and approach human reliability (abstract only; no numbers read) ([arXiv 2410.10934](https://arxiv.org/abs/2410.10934)). Counterpoint: agents can reach the same goal via different valid paths, so judge end states, with checkpoints at key state changes for complex flows ([Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)); and avoid rigid step grading ([Anthropic evals doc](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)). Ragas lists Tool Call Accuracy, Agent Goal Accuracy, Topic Adherence [V] ([docs](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)).

**Failure modes.**
- Over-penalizing valid alternate paths (Anthropic).
- Observed behaviours: 50 subagents for simple queries, endless search for nonexistent sources, duplicated work, overly long queries, continuing after enough results (Anthropic multi-agent post); tool-efficiency as rubric dimension.
- Judge reliability on long traces (UNVERIFIED).

**Exercise.** Using transcripts from the agent-task-success exercise, add per-step labels (useful / redundant / wrong tool), compute a progress-rate-like metric (milestones reached / total), step-count and redundant-call ratios; test whether trajectory metrics predict outcome failures.

**Mastery check.** (1) When is trajectory grading warranted vs outcome only? (2) Define milestones for a task. (3) What does progress rate expose that success hides? (4) Risks of agent-judges.

**Sources.** AgentBoard; Agent-as-a-Judge; Anthropic x2 (provider).

## multi-agent-evals

**Why it matters.** MAST, from 1,600+ annotated traces across 7 frameworks, defines 14 failure modes in 3 categories (system design, inter-agent misalignment, task verification), with kappa 0.88, built from 150 traces ([arXiv 2503.13657](https://arxiv.org/abs/2503.13657)). MultiAgentBench scores task completion and collaboration/competition quality via milestone KPIs across star/chain/tree/graph topologies ([arXiv 2503.01935](https://arxiv.org/abs/2503.01935)). Small changes to the lead agent can unpredictably alter subagent behaviour, so evaluate interaction patterns ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)).

**Failure modes.** The 3 MAST categories above (exact 14 names UNVERIFIED, abstract only); duplicated subagent work and over-spawning (Anthropic); topology-dependent performance (MultiAgentBench).

**Exercise.** Run a 2-3 agent pipeline (planner/worker/verifier) on 15 tasks, log traces, annotate failures with MAST categories (fetch full taxonomy from the paper first), and compare against single-agent baseline for cost and success.

**Mastery check.** (1) Single vs multi-agent: what evidence justifies the extra complexity? (2) Which MAST category is hardest to detect automatically? (3) Design a handoff test.

**Sources.** MAST; MultiAgentBench; Anthropic (provider).

## conversational-evals

**Why it matters.** MT-Bench and Chatbot Arena: strong LLM judges agree with humans >80%, but show position, verbosity, self-enhancement bias (NeurIPS 2023 D&B, [arXiv 2306.05685](https://arxiv.org/abs/2306.05685)). Chatbot Arena uses crowdsourced pairwise comparison, 240K+ votes ([arXiv 2403.04132](https://arxiv.org/abs/2403.04132)). MT-Bench-101: 3-tier ability taxonomy, 4,208 turns/1,388 dialogues/13 tasks, 21 LLMs; alignment techniques did not noticeably improve multi-turn ability (ACL 2024, [arXiv 2402.14762](https://arxiv.org/abs/2402.14762)). Underspecified multi-turn: 39% average drop vs single-turn over six tasks, mostly from unreliability ([Laban et al., arXiv 2505.06120](https://arxiv.org/abs/2505.06120)).

**Failure modes.** Early wrong assumptions then over-reliance; no recovery (Laban et al.); judge biases (Zheng et al.); single-turn tests miss multi-turn degradation.

**Exercise.** Take 20 single-turn tasks, shard each into 3-4 turns of progressively revealed info, compare to fully specified; run each 5 times to separate aptitude (best-case) from unreliability (spread). Judge with swapped order to measure position bias.

**Mastery check.** (1) Why does multi-turn unreliability differ from aptitude loss? (2) Mitigate position bias. (3) Pairwise vs absolute scoring trade-offs. (4) Define a consistency check (persona/fact stability across turns).

**Sources.** Zheng et al.; Chatbot Arena; MT-Bench-101; Laban et al.

## long-context-evals

**Why it matters.** Needle-in-a-haystack sweeps context length x needle depth ([Kamradt repo](https://github.com/gkamradt/LLMTest_NeedleInAHaystack), practitioner). Lost in the Middle: accuracy drops when evidence is mid-context (TACL, [arXiv 2307.03172](https://arxiv.org/abs/2307.03172)). RULER adds multi-hop tracing/aggregation; only about half of 17 models claiming >=32K stayed satisfactory at 32K (COLM 2024, [arXiv 2404.06654](https://arxiv.org/abs/2404.06654)). HELMET (7 categories, 59 models): synthetic tasks like NIAH do not reliably predict downstream performance ([arXiv 2410.02694](https://arxiv.org/abs/2410.02694)). NoLiMa removes lexical overlap; 11/13 models fell below half of short-context baselines at 32K; GPT-4o 99.3 to 69.7 (ICML 2025, [arXiv 2502.05167](https://arxiv.org/abs/2502.05167)).

**Failure modes.** Position effects; saturated lexical-match needle tests; claimed vs effective context length; reasoning/aggregation degrading faster than retrieval (RULER, HELMET).

**Exercise.** Run a 3x5 grid (lengths x depths) with a lexical needle and a paraphrased (low-overlap) needle on one model, 3 seeds; plot heatmaps; compare.

**Mastery check.** (1) Why is NIAH insufficient? (2) What does NoLiMa change? (3) Cost-aware design of a length sweep. (4) Separate retrieval from reasoning failures.

**Sources.** Lost in the Middle; RULER; HELMET; NoLiMa; Kamradt (practitioner).

## multimodal-evals

**Why it matters.** MMMU: ~11.5K college-level questions, 6 disciplines/30 subjects/183 subfields, GPT-4V ~56% at release (CVPR 2024, [arXiv 2311.16502](https://arxiv.org/abs/2311.16502)). MathVista: 6,141 examples, GPT-4V 49.9%, 10.4 points below human ([arXiv 2310.02255](https://arxiv.org/abs/2310.02255)). Video-MME: 900 videos/254 h/2,700 QA ([arXiv 2405.21075](https://arxiv.org/abs/2405.21075)). POPE: polling-based object-hallucination test; existing methods skewed by instructions and generation style (EMNLP 2023, [arXiv 2305.10355](https://arxiv.org/abs/2305.10355)). Scores are release-time [V].

**Failure modes.** Object hallucination, frequent/co-occurring objects favored (POPE); evaluation sensitive to prompt style; speech evaluation not covered here (UNVERIFIED; no speech source read, e.g. WER).

**Exercise.** Build 50 yes/no POPE-style probes ("Is there a X in the image?") on 25 images with present and absent objects; compute accuracy, precision, recall, yes-rate for one VLM.

**Mastery check.** (1) Why a yes-rate metric? (2) Why are knowledge benchmarks like MMMU poor hallucination tests? (3) Design a test for text-in-image reading.

**Sources.** MMMU; MathVista; Video-MME; POPE.

## summarization-and-extraction-evals

**Why it matters.** Neural summarizers are "highly prone to hallucinate"; ROUGE is weaker than textual-entailment measures at tracking faithfulness (ACL 2020, [Maynez et al., arXiv 2005.00661](https://arxiv.org/abs/2005.00661)). SummEval re-evaluated 14 metrics on 23 models with expert and crowd judgments ([arXiv 2007.12626](https://arxiv.org/abs/2007.12626); findings UNVERIFIED). FRANK: typology of factual errors, benchmark for factuality metrics, factuality graded not binary (NAACL 2021, [arXiv 2104.13346](https://arxiv.org/abs/2104.13346)). G-Eval: CoT + form-filling GPT-4, Spearman 0.514 on summarization, with a flagged preference for LLM text ([arXiv 2303.16634](https://arxiv.org/abs/2303.16634)). Extraction: constrained decoding guarantees schema adherence not value correctness ([OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) [V]); JSONSchemaBench (10K real schemas) measures efficiency, coverage, quality ([arXiv 2501.10868](https://arxiv.org/abs/2501.10868)).

**Failure modes.** Unsupported content in every tested model (Maynez); n-gram metrics missing faithfulness; LLM judges favoring LLM text (G-Eval); schema-valid wrong values, refusals and truncation breaking schema (OpenAI docs); coverage (omissions) not captured by faithfulness (UNVERIFIED as stated).

**Exercise.** 30 invoices/emails with gold fields: extract JSON with schema, compute per-field exact/normalized match, precision/recall for list fields, and null-handling. For 20 summaries, compute ROUGE, an entailment/claim-check faithfulness score, and human faithfulness+coverage labels; report correlations.

**Mastery check.** (1) Why does ROUGE fail on faithfulness? (2) Per-field vs record-level accuracy. (3) Faithfulness vs coverage trade-off. (4) Handle refusals/incomplete responses in the pipeline.

**Sources.** Maynez; SummEval; FRANK; G-Eval; JSONSchemaBench; OpenAI docs.

## Gaps and uncertainties

- Prerequisite issues: `rag-retrieval-evals` and `multimodal-evals` depend on `metric-selection`; `agent-trajectory-evals` depends only on task success but needs `llm-as-judge`, and `conversational-evals` needs experiment-design/variance (multi-turn reliability). `long-context-evals` depends on `llm-basics-for-evaluators` but fits better after RAG nodes. `tool-use-evals` and `code-generation-evals` rely on `programmatic-checks` but need sandboxing/isolation knowledge not in any node.
- Boundary: pass@k/pass^k appear in code, tool-use and agent nodes; best owned by a nondeterminism/foundations node. Faithfulness duplicated in rag-generation and summarization.
- Unverified: textbook IR metrics source (fetch failed); the "nDCG" label in the 2002 paper; SWE-bench grading method; MAST's 14 mode names; AgentBoard progress-rate formula; SummEval findings; speech evaluation; current (2026) benchmark state-of-the-art.
- Missing candidates for `_candidates.md`: text-to-SQL evals; voice/speech agents; computer-use/GUI agent evals; safety/refusal in agents (prompt injection in tool results); memory/personalization evals; reranker evals; search/deep-research agent evals; translation; evals for guardrail/classifier components; cost/latency evals for agents; user-simulator reliability for conversational/agent evals (tau-bench).

## Landscape items (as-of 2026-11-20)

- BFCL leaderboard (Gorilla; V2/V3 added live and multi-turn per blog note; current version not verified).
- SWE-bench, WebArena, OSWorld, GAIA, tau-bench, AgentBench: paper-time scores listed above are stale; refresh current SOTA.
- RAGAS metrics list and TruLens "RAG triad" docs (names may change).
- Sentence-Transformers evaluators; OpenAI Structured Outputs (docs moved to developers.openai.com).
- LiveCodeBench (rolling releases), EvalPlus/HumanEval+, CyberSecEval (later versions exist, UNVERIFIED).
- Long-context: RULER, HELMET, NoLiMa, NIAH repo.
- Multimodal: MMMU, MathVista, Video-MME, POPE.
- Chatbot Arena (vote counts, 240K at paper time).
- MAST dataset / MultiAgentBench.
