# Research: 06-production (as of 2026-11-20)

Conventions: every claim carries a URL. "UNVERIFIED" = could not confirm from the source itself. "(practitioner)" = non-primary. "[vol]" = volatile, candidate for landscape/.
Several exercises/mastery items are my own design (not sourced claims); they are marked "(design)".

---

## observability-and-tracing

**Why it matters**
- OpenTelemetry has GenAI semantic conventions that standardise spans for model calls, retrieval, tool execution and agents. Well-known `gen_ai.operation.name` values include `chat`, `embeddings`, `retrieval`, `execute_tool`, `invoke_agent`, `plan`, `search_memory` ([OTel GenAI spans](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)). A shared schema lets eval tooling and backends consume traces from any instrumented stack. [vol]
- The conventions moved out of the core semconv site into a separate repo ([OTel moved notice](https://opentelemetry.io/docs/specs/semconv/gen-ai/)); spans and most attributes are marked Development (unstable) ([spans spec](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)). [vol, as-of 2026-11-20]
- Traces are the raw material for later nodes (sampling, judges, dataset mining, incident debugging). Sculley et al. note ML systems carry ongoing maintenance cost from data dependencies and external-world change ([Hidden Technical Debt, NIPS 2015](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)); traces are how you see them.

**Failure modes**
- Capturing content by default leaks PII: the spec marks message/system-instruction/tool-definition attributes as Opt-In and warns they are "likely to contain sensitive information including user/PII data"; content capture defaults to `NO_CONTENT`, controlled by `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT` (`NO_CONTENT|SPAN_ONLY|EVENT_ONLY|SPAN_AND_EVENT`) ([spans spec](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)). The opposite failure: leaving it off means traces cannot be evaluated or turned into test cases.
- Attribute churn: unstable conventions can change between versions; pin instrumentation versions (inference from Development status; the status itself is cited above).
- Traces missing the retrieval and tool steps, so RAG/agent failures cannot be localised (design).
- Sampling decisions that drop error traces (see traffic-sampling-and-logging).

**Practice exercise** (design)
- Build a small RAG or tool-calling script. Instrument it with the OTel SDK (or an OTel-GenAI instrumentation library), emitting `chat`, `retrieval` and `execute_tool` spans, and export to a local backend (Jaeger or an OTel Collector file exporter).
- Run 20 queries, then write a script that reads the exported spans and finds the slowest and the most token-expensive request, plus the span where a deliberately injected bad retrieval occurred.
- Toggle the content-capture env var and compare what the trace contains.

**Mastery check**
1. Which GenAI attributes are Opt-In and why? What is the default capture mode?
2. Given a trace of a wrong RAG answer, which spans do you inspect to decide retrieval vs generation failure?
3. How do you keep traces useful for eval while meeting privacy constraints? (Cross-ref traffic-sampling-and-logging.)

**Primary sources**
- [OTel GenAI spans spec (repo)](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)
- [OTel GenAI moved notice](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [Sculley et al. 2015](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)

---

## traffic-sampling-and-logging

**Why it matters**
- Head sampling decides early (e.g. consistent probability by trace ID); simple and cheap but cannot keep "every error trace". Tail sampling decides on the whole trace (errors, latency, attributes) but is stateful and harder to operate; the docs say it is "almost always necessary" for larger systems and suggest combining both for very high volume ([OTel sampling](https://opentelemetry.io/docs/concepts/sampling/)).
- Eval cost: online LLM judging costs about $0.01-0.10 per assessment (Langfuse estimate) so you must sample ([Langfuse docs](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge), practitioner/vendor, [vol]).
- Privacy: GDPR Art. 5 requires data "limited to what is necessary" (minimisation) and kept identifiable "no longer than is necessary" (storage limitation) ([GDPR Art. 5 text](https://gdpr-info.eu/art-5-gdpr/), unofficial reproduction of the regulation; official text at EUR-Lex not fetched).

**Failure modes**
- Uniform random sampling under-represents rare failures; error/low-feedback/long-conversation traces need stratified or tail-style rules ([OTel sampling](https://opentelemetry.io/docs/concepts/sampling/)).
- Log content retention beyond need violates storage limitation (above).
- Automated PII scrubbing is incomplete: Presidio itself states "there is no guarantee that Presidio will find all sensitive information" ([Presidio docs](https://presidio.dataprivacystack.org/)).
- Sampling bias into datasets: sampling only thumbs-down or only flagged traces biases evals (design; see online-metrics).

**Practice exercise** (design)
- Take 5k synthetic or public chat logs (e.g. a public chat dataset). Implement (a) 2% uniform sample, (b) stratified sample keeping all errors/long/low-confidence plus 1% of the rest with inverse-probability weights.
- Estimate a known metric (e.g. refusal rate) from each; compare bias/variance over 200 repeats.
- Add a Presidio pass and manually inspect 50 samples for misses.

**Mastery check**
1. When can head sampling not satisfy "keep all failures"? What does tail sampling cost?
2. How do you get an unbiased metric estimate from a non-uniform sample?
3. State a retention policy for prompts and justify it against minimisation/storage limitation.

**Primary sources**
- [OTel sampling concepts](https://opentelemetry.io/docs/concepts/sampling/)
- [GDPR Art. 5](https://gdpr-info.eu/art-5-gdpr/)
- [Presidio](https://presidio.dataprivacystack.org/)
- (practitioner/vendor) [Langfuse online evaluators](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)

---

## online-metrics-and-user-feedback

**Why it matters**
- Implicit feedback like clicks is biased by position: raw clicks train suboptimal rankers, and propensity-weighted counterfactual estimation corrects this ([Joachims, Swaminathan, Schnabel](https://arxiv.org/abs/1608.04468)). Earlier work by Joachims et al. reported that clicks are biased by presentation and that relative preferences are more reliable than absolute click values ([Joachims et al. 2005 PDF](https://www.cs.cornell.edu/people/tj/publications/joachims_etal_05a.pdf)) - UNVERIFIED in detail: PDF text was not machine-readable in my fetch; the claim is from the paper's known thesis, confirm before citing.
- Offline metrics may not match online outcomes; Kohavi et al. present controlled experiments as the way to establish causal impact on user-observable behaviour ([Kohavi et al. 2009](https://link.springer.com/article/10.1007/s10618-008-0114-1), abstract via search).

**Failure modes**
- Position/presentation bias (above). For chat UIs, analogous selection bias applies: thumbs come from a self-selected few (UNVERIFIED for LLM chat; no primary source found).
- Metric gaming and proxy mismatch (cross-ref metric-selection).
- Feedback conflated with quality: users may click or thumb based on tone/length, which mirrors judge verbosity bias ([Zheng et al. 2023](https://arxiv.org/abs/2306.05685)).
- Hidden feedback loops: system outputs shape the data later used to train/evaluate it ([Sculley et al.](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html), abstract lists "hidden feedback loops").

**Practice exercise** (design)
- Use a public click or preference dataset (e.g. a public search click log or pairwise preference data). Compute naive CTR per position, then an inverse-propensity-weighted estimate with propensities estimated from a randomised slice (or simulate clicks with a known position-bias model and recover true relevance).
- For an LLM app: define 3 implicit signals (regenerate rate, edit distance, abandonment), compute them on a logged sample, and correlate each with a small human-labelled quality set.

**Mastery check**
1. Why can't you read CTR as relevance? How does propensity weighting fix it, and what does it assume?
2. Name two biases in thumbs-up/down feedback and one design change reducing each.
3. Which implicit signal would you trust for a coding assistant and why? Defend with a correlation to labelled data.

**Primary sources**
- [Joachims et al., unbiased LTR (arXiv 1608.04468)](https://arxiv.org/abs/1608.04468)
- [Kohavi et al. 2009](https://link.springer.com/article/10.1007/s10618-008-0114-1)
- [Sculley et al. 2015](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)

---

## production-evals-with-judges

**Why it matters**
- Strong LLM judges reach over 80% agreement with humans, the same as human-human agreement, on MT-Bench and Chatbot Arena, which makes scalable scoring of live traffic possible ([Zheng et al. 2023](https://arxiv.org/abs/2306.05685)).
- Platforms run judges on a sampled subset of live traces via rules with filters and sampling rates ([Langfuse](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge), vendor, [vol]).
- Anthropic's eval guidance recommends a different model for grading than the generator and lists LLM-based binary and Likert grading ([Anthropic: develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), [vol]).

**Failure modes**
- Position, verbosity and self-enhancement biases, plus limited reasoning ([Zheng et al.](https://arxiv.org/abs/2306.05685)).
- Judge not validated: LLM evaluators inherit LLM flaws; criteria drift as users see outputs, and some criteria only emerge from observed outputs ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).
- Cost blowup from judging all traffic (Langfuse cost estimate above); evaluators see only the matched observation, not children, so a judge can lack needed context ([Langfuse](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)).
- Judge model changes silently shift scores (design; judge is itself subject to provider deprecation, see model-upgrade).

**Practice exercise** (design)
- Take ~200 logged Q&A pairs (public dataset). Human-label 60. Write a binary judge prompt, measure agreement (Cohen's kappa) with the labels, then run it on the rest at a 10% sample rate; report score with a bootstrap CI.
- Test swap-order and a verbose rewrite to measure position/verbosity bias.

**Mastery check**
1. What do you report to claim a production judge is trustworthy (agreement, kappa, CI, bias probes)?
2. How would you detect that the judge, not the app, caused a score change?
3. Choose a sampling rate for 1M requests/day with a $200/day budget at $0.05/judgement; what does that imply for detectable effect size?

**Primary sources**
- [Zheng et al. MT-Bench](https://arxiv.org/abs/2306.05685)
- [Shankar et al. EvalGen](https://arxiv.org/abs/2404.12272)
- [Anthropic develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- (practitioner/vendor) [Langfuse](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)

---

## online-experiments

**Why it matters**
- Controlled experiments are the standard design for establishing causal effect on user-observable behaviour; the Kohavi guide covers surprising results, ingredients, and technical/organisational limits ([Kohavi et al. 2009](https://link.springer.com/article/10.1007/s10618-008-0114-1)).
- Peeking breaks standard p-values; always-valid p-values/CIs stay valid under continuous monitoring and were deployed on a commercial platform ([Johari et al.](https://arxiv.org/abs/1512.04922)).
- CUPED uses pre-experiment data to reduce metric variance and raise sensitivity; its benefit depends on the pre/post correlation ([CUPED page](https://exp-platform.com/cuped/); correlation caveat via [search summary of Lin & Crespo 2024](https://arxiv.org/html/2410.09027v1), not read directly).
- Review of statistical challenges in online experimentation ([arXiv 2212.11366](https://arxiv.org/abs/2212.11366)).

**Failure modes**
- Peeking/early stopping (Johari above).
- Sample ratio mismatch: observed split differs from intended; Microsoft research calls it one of the most useful data-quality indicators, and the book's index lists SRM p.219 and novelty effect pp.33, 49, 174 ([search results incl. book index](https://assets.cambridge.org/97811087/24265/index/9781108724265_index.pdf)); definitions of novelty effect from the book text UNVERIFIED.
- LLM-specific: nondeterministic outputs add per-request variance; user-level randomisation and variance reduction needed (design/inference; no primary source found on LLM-specific A/B).
- Interference/shared state across variants (also cited for canaries in [SRE workbook](https://sre.google/workbook/canarying-releases/)).

**Practice exercise** (design)
- Simulate an A/B test with a binary success metric (base 40%, +2pt effect) with 1) fixed-horizon test, 2) daily peeking at p<0.05, measure false-positive rate over 2,000 A/A runs. Then apply CUPED with a correlated pre-period metric and measure variance reduction and a chi-square SRM check with a deliberately buggy 52/48 split.

**Mastery check**
1. Why is daily peeking at p<0.05 invalid, and what are two fixes?
2. SRM p-value is 0.0001 - what do you do with the result?
3. How would you detect a novelty effect for a new assistant UI?

**Primary sources**
- [Kohavi et al. 2009](https://link.springer.com/article/10.1007/s10618-008-0114-1)
- [Johari et al. always-valid](https://arxiv.org/abs/1512.04922)
- [Deng et al. CUPED (WSDM 2013)](https://exp-platform.com/cuped/)
- [Statistical challenges review](https://arxiv.org/abs/2212.11366)
- Book: Kohavi, Tang, Xu, Trustworthy Online Controlled Experiments, CUP 2020 ([index/excerpt](https://assets.cambridge.org/97811087/24265/index/9781108724265_index.pdf))

---

## shadow-and-canary-releases

**Why it matters**
- Canarying is "a partial and time-limited deployment of a change in a service and its evaluation"; canary vs control is effectively A/B testing; exposure of a defect is proportional to canary traffic ([SRE Workbook: canarying](https://sre.google/workbook/canarying-releases/)).
- Shadow testing mirrors a copy of live requests to the new variant while only the production variant's response is returned; responses are discarded or logged for offline comparison ([AWS SageMaker shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html), [vol] vendor docs). It validates operational metrics before promotion.

**Failure modes** (from the SRE Workbook)
- Imperfect isolation between canary and control; miscalibrated thresholds; metric interval longer than canary duration; synthetic load missing state; before/after comparison confounded by time; run one canary at a time; use absolute SLOs as well as relative comparison ([workbook](https://sre.google/workbook/canarying-releases/)).
- LLM-specific: shadow outputs are not seen by users so quality needs a judge or reference (design); stateful agents with side effects cannot be shadowed safely without stubbing tools (design/inference, UNVERIFIED by source).
- Shadow support has constraints (e.g. some endpoint types incompatible) ([AWS](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html)).

**Practice exercise** (design)
- Build a router that sends 5% of requests to a candidate prompt/model (canary) and mirrors 100% of a replayed log to it (shadow). Compare latency, cost, format-validity rate, and judge score; write an automatic rollback rule (e.g. abort if error rate > baseline + threshold) and test it with an injected regression.

**Mastery check**
1. Shadow vs canary: what does each reveal and not reveal?
2. Pick 3 canary metrics for a RAG chatbot and thresholds; justify.
3. Why could hourly metrics invalidate a 30-minute canary?

**Primary sources**
- [Google SRE Workbook: Canarying releases](https://sre.google/workbook/canarying-releases/)
- [AWS SageMaker shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html)

---

## drift-detection

**Why it matters**
- Hosted-model behaviour changes: GPT-4 prime/composite accuracy fell from 84% (March 2023) to 51% (June 2023), and the authors recommend continuous monitoring ([Chen, Zaharia, Zou](https://arxiv.org/abs/2307.09009)).
- For input drift, a two-sample test on pre-trained-classifier-reduced representations performed best across the shifts tested in "Failing Loudly" ([Rabanser et al.](https://arxiv.org/abs/1810.11953)). Domain-discriminating methods help characterise shifts and judge harm.
- Concept drift is where the input-target relation changes over time; Gama et al. survey adaptation strategies and evaluation ([ACM CSUR 2014 via search](https://eprints.bournemouth.ac.uk/22491/); taxonomy of drift types - sudden/gradual/recurring - not verified, page blocked).

**Failure modes**
- Detecting statistical shift that is harmless (alert fatigue); Rabanser et al. frame assessing harm as separate from detection ([abstract](https://arxiv.org/abs/1810.11953)).
- Per-column tests with default thresholds: Evidently docs differ across versions on defaults (Wasserstein/K-S/PSI, threshold 0.1, drift_share 50%) - check your version ([Evidently docs](https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests) (link 404 as of 2026-11-21), practitioner/OSS, [vol]).
- Provider-side silent model changes need output/quality drift checks, not only input checks (Chen et al.).
- Applying tabular-drift tests to text without embeddings: UNVERIFIED (no primary source found on embedding-drift validity).

**Practice exercise** (design)
- Take a text classification dataset with a natural time split (e.g. news by year). Embed, then run (a) per-dimension KS with Bonferroni, (b) classifier two-sample test (domain classifier AUC), (c) MMD. Inject synthetic drift of increasing magnitude and plot detection power vs false-positive rate. Replay a fixed prompt set against a model weekly and track an output metric (design).

**Mastery check**
1. Covariate vs label vs concept shift; which can you detect without labels?
2. Why does the dimensionality-reduction step matter for two-sample tests?
3. Design the monitoring for a hosted LLM whose provider may change behaviour silently.

**Primary sources**
- [Rabanser et al. Failing Loudly](https://arxiv.org/abs/1810.11953)
- [Chen et al. How is ChatGPT's behavior changing](https://arxiv.org/abs/2307.09009)
- [Gama et al. survey](https://eprints.bournemouth.ac.uk/22491/)
- (practitioner/OSS) [Evidently drift options](https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests) (link 404 as of 2026-11-21)

---

## runtime-guardrails

**Why it matters**
- Llama Guard: an LLM-based classifier for both prompts and responses with a customisable risk taxonomy; reported matching or exceeding moderation baselines on OpenAI Mod and ToxicChat ([arXiv 2312.06674](https://arxiv.org/abs/2312.06674)). [vol]
- NeMo Guardrails: programmable, user-defined, LLM-independent rails (EMNLP 2023 demo) ([arXiv 2310.10501](https://arxiv.org/abs/2310.10501)).
- Constitutional Classifiers: 3,000+ hours of red teaming found no universal jailbreak for an early version; cost was +0.38% absolute refusals on production traffic and 23.7% inference overhead ([arXiv 2501.18837](https://arxiv.org/abs/2501.18837)). Shows guardrails must be evaluated on both attack-success and over-refusal/overhead.
- Liability context: a Canadian tribunal held Air Canada liable for its chatbot's misinformation (Moffatt v. Air Canada, 2024 BCCRT 149) ([decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do), found via search; summary at [ABA](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/), not fetched directly).

**Failure modes**
- Over-refusal (false positives) and latency/compute cost (Constitutional Classifiers numbers above).
- Taxonomy mismatch: a guard trained on one policy used with another; Llama Guard supports adapting taxonomy via prompting ([2312.06674](https://arxiv.org/abs/2312.06674)).
- Benchmark-only evaluation: red teamers vs automated held-out jailbreaks both used in the classifier paper ([2501.18837](https://arxiv.org/abs/2501.18837)).
- Guard evaluated in isolation but not in the full pipeline (streaming, tools): UNVERIFIED.

**Practice exercise** (design)
- Run an open guard model (e.g. Llama Guard) or a moderation API over a small labelled mix: 100 harmful and 300 benign-but-edgy prompts from public safety benchmarks. Report recall, false-positive rate, per-category confusion and latency; sweep the decision threshold and plot a precision-recall curve; pick the threshold for a stated cost ratio.

**Mastery check**
1. What two error rates must a guardrail report, and why is the benign set as important as the attack set?
2. How would you monitor a live guardrail for drift (block rate over time, sampled review)?
3. Input vs output rails: what does each catch that the other cannot?

**Primary sources**
- [Llama Guard](https://arxiv.org/abs/2312.06674)
- [NeMo Guardrails](https://arxiv.org/abs/2310.10501)
- [Constitutional Classifiers](https://arxiv.org/abs/2501.18837)
- [Moffatt v. Air Canada decision](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do)

---

## feedback-loop-to-datasets

**Why it matters**
- Interviews with 18 ML engineers identify Velocity, Validation and Versioning as the variables governing production success and describe continual monitoring of production performance drops as part of the loop ([Shankar et al. 2022](https://arxiv.org/abs/2209.09125)).
- Evaluation criteria evolve as you look at outputs ("criteria drift"), so datasets must be refreshed from observed failures ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).
- Anthropic's guidance: mirror the real task distribution and include edge cases; more automatically graded questions beat fewer hand-graded ([Anthropic develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), [vol]). That page's explicit guidance on production data was not seen (only first 100k chars read).

**Failure modes**
- Hidden feedback loops and entanglement ([Sculley et al.](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)).
- Test-set contamination by training on or tuning against mined failures (design; cross-ref golden-datasets).
- Unrepresentative mining (only thumbs-down) skews dataset; privacy of logged data (see traffic-sampling-and-logging).
- Labels from an unvalidated judge become the ground truth (Shankar 2024).

**Practice exercise** (design)
- From logged traces with a failure flag, mine 50 failures, cluster by error type, write a minimal test case per cluster (input, expected property, scorer), anonymise, add to a versioned dataset with provenance fields, split into dev (for tuning) and a frozen holdout, and confirm the fix flips the case and does not regress the older set.

**Mastery check**
1. How do you keep a mined-failure set from inflating scores after you fix those failures?
2. What metadata should each promoted case carry (source trace id, date, label author, privacy status)?
3. How does criteria drift change when you re-label?

**Primary sources**
- [Shankar et al. 2022 Operationalizing ML](https://arxiv.org/abs/2209.09125)
- [Shankar et al. 2024 Who validates the validators](https://arxiv.org/abs/2404.12272)
- [Sculley et al.](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)

---

## incident-response-and-postmortems

**Why it matters**
- Google SRE: blameless postmortems assume everyone had good intentions and fix systems; triggers should be defined in advance (user-visible degradation over a threshold, data loss, on-call intervention such as rollback, long resolution, monitoring failure); good postmortems record impact, mitigation, root causes, follow-ups ([SRE book: postmortem culture](https://sre.google/sre-book/postmortem-culture/)).
- Incident roles: incident command, operations (only group changing the system), communication, planning; declare early; keep a live incident document ([SRE book: managing incidents](https://sre.google/sre-book/managing-incidents/)).
- The AI Incident Database collects real-world failures to build "collective memory" so mistakes aren't repeated (1,000+ reports at publication) ([McGregor, arXiv 2011.08512](https://arxiv.org/abs/2011.08512)).

**Failure modes**
- Blame, which hides problems; unreviewed postmortems as formality; stigmatising frequent authors ([SRE postmortem culture](https://sre.google/sre-book/postmortem-culture/)).
- Freelancing, poor communication, narrow technical focus ([SRE incidents](https://sre.google/sre-book/managing-incidents/)).
- AI-specific: no deterministic repro because of non-determinism and provider-side change (Chen et al.: [arXiv 2307.09009](https://arxiv.org/abs/2307.09009)); no stored traces to replay (see observability); action items that do not become regression tests (design).
- Org liability for chatbot output (Moffatt, see runtime-guardrails).

**Practice exercise** (design)
- Pick a public AI incident from the AI Incident Database. Write a blameless postmortem (timeline, impact, contributing factors, detection gap, mitigation) and derive 3 concrete action items, at least one a new eval case and one a monitor/guardrail. Run a tabletop drill with a self-written scenario (e.g. provider silently changes model behaviour).

**Mastery check**
1. What makes a postmortem "blameless" in practice, and what are the triggers for one?
2. For an LLM failure that cannot be reproduced, what evidence must you have captured?
3. Show how each action item closes a detect/prevent/mitigate gap.

**Primary sources**
- [SRE book: postmortem culture](https://sre.google/sre-book/postmortem-culture/)
- [SRE book: managing incidents](https://sre.google/sre-book/managing-incidents/)
- [McGregor, AI Incident Database](https://arxiv.org/abs/2011.08512)

---

## model-upgrade-and-migration

**Why it matters**
- Anthropic: models move Active -> Legacy -> Deprecated -> Retired; at least 60 days' notice before retirement of public models; retired requests fail; test replacements well before retirement ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)). Example: `claude-sonnet-4-5-20250929` deprecated 2026-09-30, retires 2026-11-30, replacement `claude-sonnet-5-5` (same page). [vol, as-of 2026-11-20]
- OpenAI: notice of at least 6 months for GA models (about 2 weeks for previews); advises running representative requests against the replacement and comparing outputs, latency, cost ([OpenAI deprecations](https://developers.openai.com/api/docs/deprecations)). Example: `gpt-5` family shutdown 2026-12-11 (same page). [vol]
- API parameters can be removed too: Anthropic removed `temperature`, `top_p`, `top_k` in API version `2026-10-21` (returns 400) ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)). [vol]
- Behaviour shifts across versions can be large (Chen et al.: [arXiv 2307.09009](https://arxiv.org/abs/2307.09009)).
- Partner platforms (Bedrock, Google-managed) follow their own schedules ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)).

**Failure modes**
- Unpinned aliases silently change (UNVERIFIED for specific providers; the Claude Code alias note on the deprecations page implies aliases resolve to current models).
- Not auditing which keys/services still use a deprecated model: Anthropic suggests a Console Usage export by key and model ([page](https://platform.claude.com/docs/en/about-claude/model-deprecations)).
- Prompts tuned to the old model regress; parameter/API changes break calls; judge model also deprecated (design).
- Migration evaluated only on aggregate score; slice regressions hidden (design).

**Practice exercise** (design)
- Take a prompt app with ~100 golden cases. Run old vs new model (or two versions) with 3 repeats each; compare per-slice pass rates with paired bootstrap CIs, plus latency and cost; examine the discordant cases; produce a go/no-go memo and a rollback plan using shadow then canary.

**Mastery check**
1. How do you decide a new model is "not worse" statistically given nondeterminism?
2. List non-quality things to test (parameters, token limits, latency, cost, formatting).
3. What is your process when the replacement is worse on one slice but better overall?

**Primary sources**
- [Anthropic model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [OpenAI deprecations](https://developers.openai.com/api/docs/deprecations)
- [Chen et al.](https://arxiv.org/abs/2307.09009)

---

## Gaps and uncertainties

- Prerequisites: `drift-detection` requires `classical-ml-validation` (not really about drift; a stats/ML monitoring foundation like two-sample tests is closer); `online-experiments` prerequisite `statistical-inference` fine but should also link `variance` / sequential testing if exist; `feedback-loop-to-datasets` needs `golden-datasets` (ok); `shadow-and-canary-releases` requires `ci-eval-gates` but canarying is more about runtime SLO comparison than CI gates; `incident-response-and-postmortems` depends only on observability but also on `runtime-guardrails` and `drift-detection` as detection sources. `model-upgrade-and-migration` should also reference `regression-testing` plus `production-evals-with-judges`.
- Boundary overlaps: online-metrics vs online-experiments (metric definitions vs causal analysis); drift-detection vs model-upgrade (provider-side drift); runtime-guardrails vs safety-and-harm-evals.
- Weak sourcing: LLM-specific A/B testing, LLM chat thumbs bias, embedding-drift validity, shadowing agents with side effects, and guard-in-pipeline evaluation had no primary source found. Joachims 2005 and Gama drift taxonomy not read directly.
- Candidates for `map/06-production/_candidates.md`: cost and latency monitoring (token budgets, SLOs); LLM-specific SLIs/SLOs and error budgets; privacy/PII redaction and data retention; sequential testing/bandits for prompt selection; replay/regression testing from traces; prompt/version management and feature flags; red-teaming in production/abuse monitoring; human review queues and annotation ops; RAG/agent-specific monitoring (retrieval quality, tool-error rates); regulatory post-market monitoring (UNVERIFIED, not researched).

## Landscape items (as-of 2026-11-20)

- OTel GenAI semantic conventions: moved to `open-telemetry/semantic-conventions-genai`, Development status; content capture env var `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT` - https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md
- Anthropic deprecation table: Sonnet 4.5 retires 2026-11-30; Haiku 4.5 not sooner than 2026-10-15; `temperature/top_p/top_k` removed in API version 2026-10-21 - https://platform.claude.com/docs/en/about-claude/model-deprecations
- OpenAI deprecations: `gpt-5` family shutdown 2026-12-11; whisper-1 2027-02-26 - https://developers.openai.com/api/docs/deprecations
- Langfuse online LLM-as-judge (sampling rules, ~$0.01-0.10 per eval) - https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge
- Evidently drift defaults vary by version - https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests (link 404 as of 2026-11-21)
- Presidio (PII detection; moved to presidio.dataprivacystack.org) - https://presidio.dataprivacystack.org/
- Llama Guard, NeMo Guardrails, Constitutional Classifiers (guardrail models/toolkits) - links in runtime-guardrails
- AWS SageMaker shadow tests - https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html
