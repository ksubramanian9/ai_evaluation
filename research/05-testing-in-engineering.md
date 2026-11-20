# Research: 05-testing-in-engineering

As-of 2026-11-20. Claims carry inline URLs. "Practice" and "Mastery" content are proposed designs (author judgement), not sourced claims. [practitioner] = non-primary. Items marked UNVERIFIED were not confirmed against the source text.

---

## llm-unit-tests

**Why it matters.** Held-out accuracy "often overestimates" model performance; CheckList borrows behavioral testing from software engineering, with a capability x test-type matrix and a test generator; practitioners using it wrote 2x the tests and found ~3x the bugs of those without ([Ribeiro et al., ACL 2020](https://arxiv.org/abs/2005.04118)). Anthropic's guidance: success criteria should be specific, measurable, achievable, relevant; evals should mirror the real task distribution incl. edge cases; automate grading; "more questions with slightly lower signal automated grading" beats fewer hand-graded ([Anthropic docs: develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), as-of 2026-11-20). The CheckList test names MFT/INV/DIR are NOT confirmed from the abstract page; UNVERIFIED (read paper body before writing them into the node).

**Failure modes.**
- Exact-match graders on free text give false failures; the docs show exact match only for constrained labels (sentiment), with cosine similarity, ROUGE-L, and LLM grading for fuzzier tasks ([Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Using the same model to generate and grade; docs advise a different grader model ([Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Happy-path-only cases: docs list irrelevant/nonexistent input, overlong input, harmful input, ambiguous cases as edge cases ([same](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Single-run assertions on a nondeterministic component (see determinism and flaky nodes).

**Practice (3h).** Pick one prompt (e.g., ticket-classifier). Write 30 pytest cases: 15 exact-label, 5 edge (empty, 10k chars, sarcasm, mixed), 5 format checks (JSON schema), 5 LLM-graded. Record each with a mock/VCR cassette so the suite runs offline in <5s. Seed a deliberate prompt bug; confirm which tests catch it.

**Mastery check.**
1. Which assertions in your suite are deterministic checks vs. LLM-graded, and why that split?
2. Show a test that passes on a wrong answer (false pass) and fix it.
3. Explain why a 95% pass rate on 20 cases is weak evidence (link to CI node).

**Sources.** [CheckList arXiv 2005.04118](https://arxiv.org/abs/2005.04118); [Anthropic develop-tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests).

---

## determinism-control-and-mocking

**Why it matters.** "Deterministic" settings do not give repeatable results: across 5 LLMs x 8 tasks x 10 runs, accuracy varied up to 15% between runs and best-to-worst gap reached 70%; no model was consistently repeatable ([Atil et al., arXiv 2408.04667](https://arxiv.org/abs/2408.04667)). Cause per Thinking Machines: kernels are not batch-invariant, so server load changes batch size and thus numerics; Qwen3-235B at temperature 0 gave 80 unique completions in 1000 samples, diverging at token 103; batch-invariant kernels made all 1000 identical, at a speed cost ([Thinking Machines, 2025](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/); company research blog, treat as primary-from-practitioner-lab). OpenAI's seed gives "mostly" identical outputs when seed, parameters and `system_fingerprint` match; residual nondeterminism remains ([OpenAI cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter); Azure says the same: [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output)). Note: Anthropic API version 2026-10-21 returns HTTP 400 if `temperature`, `top_p`, or `top_k` is sent, even at defaults ([Anthropic migration guide](https://platform.claude.com/docs/en/api/migration-2026-10-21)); sampling control may be unavailable per provider, so mocking/recording is the dependable repeatability lever. (Volatile, as-of 2026-11-20.)

**Failure modes.**
- Assuming temperature 0 or a seed implies identical output (refuted above).
- Ignoring `system_fingerprint`/model snapshot changes between runs ([OpenAI cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter)).
- Stale cassettes: VCR record mode `once` replays and errors on new requests; `new_episodes` silently records new ones; `none` guarantees no new HTTP calls; `all` never replays ([VCR.py docs](https://vcrpy.readthedocs.io/en/latest/usage.html)). Prompt change plus replayed cassette = test that never hits the model.
- Mocks that hide real behavior, so tests pass while production fails (author judgement).
- Secrets recorded in cassettes. VCR.py filtering: UNVERIFIED on the usage page (it points to Configuration docs).

**Practice (2-3h).** Send the same prompt 50x to one API (temp 0 if allowed) and count unique outputs and first-divergence token. Then wrap the client with VCR.py (record `once`), show the second run makes zero network calls, and write a test that fails if the cassette is missing in CI (record mode `none`).

**Mastery check.**
1. Explain why batch size changes outputs at temperature 0.
2. When should a test use a recorded response vs. live call vs. mock?
3. Design cassette invalidation keyed on prompt hash + model ID.

**Sources.** [Atil 2408.04667](https://arxiv.org/abs/2408.04667); [Thinking Machines](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/); [OpenAI cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter); [VCR.py](https://vcrpy.readthedocs.io/en/latest/usage.html); [Anthropic migration 2026-10-21](https://platform.claude.com/docs/en/api/migration-2026-10-21).

---

## regression-testing

**Why it matters.** Provider models change under you: GPT-4 prime-vs-composite accuracy fell 84% to 51% between March and June 2023 versions; GPT-3.5 moved the other way on some tasks; instruction-following declined, and authors call for "continuous monitoring" ([Chen, Zaharia, Zou, arXiv 2307.09009](https://arxiv.org/abs/2307.09009)). Providers retire models on a schedule (at least 60 days' notice for public models) and advise testing replacements well ahead ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations), as-of 2026-11-20; e.g., `claude-sonnet-4-5-20250929` retirement 2026-11-30 listed there). Behavioral test suites (CheckList) are a regression format ([Ribeiro 2020](https://arxiv.org/abs/2005.04118)).

**Failure modes.**
- Only aggregate score compared; per-slice regressions hidden by improvements elsewhere (author judgement; see coverage-and-slicing).
- Overfitting prompts to the golden set; set becomes stale.
- Comparing runs without noise estimate, so noise reads as regression (see Atil: up to 15% run-to-run accuracy variation, [arXiv 2408.04667](https://arxiv.org/abs/2408.04667)).
- Migrating models without re-running the suite, relying on the new model being "better"; Chen et al. show newer versions can be worse on specific tasks ([arXiv 2307.09009](https://arxiv.org/abs/2307.09009)).

**Practice (3-4h).** Take the unit-test suite plus ~100-case golden set. Run on model A and model B (or two prompt versions) x5 repeats. Report per-case flip table (pass->fail, fail->pass), per-slice deltas, and paired bootstrap CI on the difference. Decide ship/no-ship with a written rule.

**Mastery check.**
1. Why compare paired per-case results rather than two aggregate numbers?
2. A new model improves overall +2% but regresses a critical slice -8%: what is the decision rule?
3. How many repeats make a 3-point change detectable? (compute from your own variance)

**Sources.** [Chen 2307.09009](https://arxiv.org/abs/2307.09009); [Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations); [CheckList](https://arxiv.org/abs/2005.04118); [Atil](https://arxiv.org/abs/2408.04667).

---

## ci-eval-gates

**Why it matters.** The ML Test Score rubric (28 tests/monitoring items from production systems, IEEE Big Data 2017) is the foundational "is this ML system production-ready" checklist ([Breck et al.](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)). Tooling example: promptfoo runs evals on PRs touching `prompts/**` or the config, supports `--fail-on-error`, custom pass-rate gates (docs example 95%), caching via `actions/cache`, JUnit XML output, and scheduled red-team runs ([promptfoo CI/CD docs](https://www.promptfoo.dev/docs/integrations/ci-cd/), tool docs, as-of 2026-11-20).

**Failure modes.**
- Gating on a noisy metric: flaky gate trains people to rerun/ignore (see flaky node).
- Cost/time blowup: running full eval on every commit; mitigations include caching and path filters ([promptfoo](https://www.promptfoo.dev/docs/integrations/ci-cd/)).
- Rate limits in CI; docs suggest caching and `-j 1` ([promptfoo](https://www.promptfoo.dev/docs/integrations/ci-cd/)).
- Cache key not covering all inputs, giving stale passes ([promptfoo troubleshooting](https://www.promptfoo.dev/docs/integrations/ci-cd/)).
- Leaking data in CI logs/artifacts; promptfoo offers `PROMPTFOO_STRIP_RESPONSE_OUTPUT` and `PROMPTFOO_STRIP_TEST_VARS` ([same](https://www.promptfoo.dev/docs/integrations/ci-cd/)).
- Threshold chosen arbitrarily rather than from baseline variance (author judgement).

**Practice (3h).** GitHub Actions workflow: on PR changing prompts, run a 50-case suite (cached/cassette for deterministic checks, live for 10 LLM-graded cases), publish JUnit report, fail if pass rate < baseline minus 2 SE. Two tiers: fast PR gate, nightly full suite plus red-team.

**Mastery check.**
1. Justify your threshold from measured baseline variance.
2. Which checks block merge vs. warn vs. run nightly, and why?
3. How do you stop a failing-but-flaky gate being bypassed?

**Sources.** [promptfoo CI/CD](https://www.promptfoo.dev/docs/integrations/ci-cd/); [ML Test Score](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/).

---

## prompt-versioning-and-change-management

**Why it matters.** Model and prompt versions drift independently; provider lifecycle (Active/Legacy/Deprecated/Retired) forces change ([Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)); behavior of a named service changed within 3 months ([Chen 2023](https://arxiv.org/abs/2307.09009)). Registry patterns: MLflow prompt versions are immutable, with mutable aliases (e.g., production) enabling rollback by reassigning the alias, integrated with tracing/evaluation ([MLflow prompt registry](https://mlflow.org/docs/latest/genai/prompt-registry/), as-of 2026-11-20). Langfuse: a new prompt under an existing name creates a new version; `production` label selects the live version; SDK-side caching decouples prompts from the critical path ([Langfuse docs](https://langfuse.com/docs/prompt-management/get-started), as-of 2026-11-20).

**Failure modes.**
- Cache serving a stale prompt after promotion ([Langfuse](https://langfuse.com/docs/prompt-management/get-started)).
- Prompt versioned but model ID/params/tool schemas/retrieval config not versioned together (author judgement; "config as artifact" per node stub).
- Moving alias without eval run; no link between a version and its eval results.
- Pinning an alias that points to an auto-updating model; Anthropic distinguishes dated IDs vs. undated IDs (deprecation page retires both `claude-sonnet-4-5-20250929` and the undated alias, [source](https://platform.claude.com/docs/en/about-claude/model-deprecations)).

**Practice (2-3h).** Store prompts as files + a manifest {prompt hash, model ID, params, eval run ID}. Script: `promote` requires eval pass; `rollback` repoints alias. Or stand up MLflow/Langfuse locally and do the same. Simulate a bad release and roll back; time it.

**Mastery check.**
1. What must be in the "release unit" beyond the prompt text?
2. Walk through rollback and what could make it not take effect immediately.
3. How would you attribute a quality drop between prompt change vs. silent model change?

**Sources.** [MLflow](https://mlflow.org/docs/latest/genai/prompt-registry/); [Langfuse](https://langfuse.com/docs/prompt-management/get-started); [Anthropic deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations); [Chen 2023](https://arxiv.org/abs/2307.09009).

---

## flaky-test-management

**Why it matters.** Luo et al. (FSE 2014) inspected 201 commits fixing flaky tests in 51 Apache projects; ten root-cause categories, top three: async wait, concurrency, test-order dependency; 74% of order-dependent flakes fixed via static-field changes ([FSE 2014 via search summary](https://huang.isis.vanderbilt.edu/cs8395/paper/flakytest.pdf); DOI 10.1145/2635868.2635920; ACM page returned 403, details from search snippet, re-verify in PDF). LLM-based tests add a new source: model output variance (up to 15% accuracy variation across runs, [Atil](https://arxiv.org/abs/2408.04667)) and batch-dependent numerics ([Thinking Machines](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)). Google's flaky-test blog post body did not load; only comments did, so no Google statistics are cited (UNVERIFIED).

**Failure modes.**
- Treating LLM variance as "flakiness to retry away": retries hide real 10-30% failure-rate behavior; need pass-rate over N samples with CI instead of single pass/fail (author judgement).
- Quarantine without owner/expiry, so tests rot.
- Auto-rerun until green, masking regressions.
- Flake from external deps (network, rate limits, provider outage) conflated with model variance; Luo's categories include network, time, randomness ([summary](https://huang.isis.vanderbilt.edu/cs8395/paper/flakytest.pdf)).

**Practice (3h).** Run your suite 20x; per test compute pass rate and Wilson CI. Classify tests: stable-pass, stable-fail, flaky (CI straddles gate). For each flaky one, attribute cause (model variance, infra, test design) and fix: tighten assertion, mock the dependency, or convert to statistical test (N samples, assert pass rate >= p).

**Mastery check.**
1. Distinguish a flaky test from an unreliable model; how do you tell from data?
2. Design a quarantine policy with exit criteria.
3. Convert a single-shot assertion to a statistical assertion; choose N.

**Sources.** [Luo 2014](https://huang.isis.vanderbilt.edu/cs8395/paper/flakytest.pdf); [Atil](https://arxiv.org/abs/2408.04667); [Thinking Machines](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/).

---

## metamorphic-and-property-testing

**Why it matters.** Metamorphic testing (MT) addresses both test generation and the oracle problem: check relations between outputs of related inputs rather than exact outputs ([Chen et al., ACM CSUR 51(1), 2018](https://research.nottingham.edu.cn/en/publications/metamorphic-testing-a-review-of-challenges-and-opportunities/), bibliographic details via search; ACM page 403). For LLMs: Cho, Ruberto, Terragni collected 191 MRs for NLP tasks, implemented 36, ran ~560,000 metamorphic tests on three LLMs ([arXiv 2511.02108](https://arxiv.org/abs/2511.02108)); the "~11% MT-only failures" figure is from a secondary summary, UNVERIFIED. Property-based testing: Hypothesis generates inputs across a defined range, including edge cases ([Hypothesis docs](https://hypothesis.readthedocs.io/en/latest/)); shrinking/database are not described on that page (UNVERIFIED there).

**Failure modes.**
- Weak MRs that any model satisfies (e.g., trivially constant output), giving false confidence (author judgement).
- MRs that are not truly semantics-preserving (paraphrase changes meaning), producing false alarms.
- Property generators producing unrealistic inputs.
- Treating MT as complete: MT detects inconsistency, not consistent wrongness; both original and follow-up can be wrong the same way.

**Practice (3h).** For a QA or classification prompt define 5 MRs (paraphrase invariance, irrelevant-sentence insertion invariance, negation flips label, entity swap preserves structure, unit-conversion equivalence). Generate follow-ups programmatically (templates or Hypothesis strategies), run 200 pairs, report violation rate per MR, manually audit 20 violations for MR validity vs. model bug.

**Mastery check.**
1. Give an MR for a summarizer and say what class of bug it cannot catch.
2. How do you validate an MR is itself correct?
3. Property vs. metamorphic relation: example of each for an extraction task.

**Sources.** [Chen 2018](https://research.nottingham.edu.cn/en/publications/metamorphic-testing-a-review-of-challenges-and-opportunities/); [Cho 2511.02108](https://arxiv.org/abs/2511.02108); [Hypothesis](https://hypothesis.readthedocs.io/en/latest/).

---

## robustness-testing

**Why it matters.** PromptRobust/PromptBench: 4,788 adversarial prompts over 8 tasks and 13 datasets at character, word, sentence, and semantic levels; "contemporary LLMs are not robust to adversarial prompts" ([Zhu et al., arXiv 2306.04528](https://arxiv.org/abs/2306.04528)). CheckList includes perturbation-style invariance tests ([Ribeiro](https://arxiv.org/abs/2005.04118); type names UNVERIFIED from abstract). HELM measures robustness and fairness among seven metrics over 42 scenarios and 30 models ([Liang et al., TMLR 2023](https://arxiv.org/abs/2211.09110)).

**Failure modes.**
- Perturbations unrealistic vs. real user noise; or label-changing perturbations.
- Reporting average drop only; worst-case per input matters.
- Mixing up prompt robustness (instruction wording) with input robustness (user text).
- Robustness tests run only on one model, with no transfer analysis; Zhu et al. analyze transfer of adversarial prompts across models ([arXiv 2306.04528](https://arxiv.org/abs/2306.04528)).

**Practice (3h).** Take 100 golden cases. Apply 4 perturbation families (typos, case/whitespace, paraphrase via LLM + manual audit, distractor sentence). Report accuracy per family with CI and the fraction of cases whose output flips. Try PromptBench or a small custom script.

**Mastery check.**
1. Why is flip-rate more informative than accuracy drop alone?
2. How do you ensure a perturbation preserves the label?
3. Which perturbations matter for your user population and how would you know?

**Sources.** [Zhu 2306.04528](https://arxiv.org/abs/2306.04528); [HELM](https://arxiv.org/abs/2211.09110); [CheckList](https://arxiv.org/abs/2005.04118).

---

## red-teaming

**Why it matters.** Anthropic's study: 38,961 red-team attacks released; 2.7B/13B/52B models and four model types; RLHF models got harder to red-team with scale, others flat ([Ganguli et al., arXiv 2209.07858](https://arxiv.org/abs/2209.07858)). Automated: use an LM to generate test cases against a target and a classifier to score; found tens of thousands of offensive replies from a 280B chatbot ([Perez et al., arXiv 2202.03286](https://arxiv.org/abs/2202.03286)). Standardization: HarmBench compares 18 red-teaming methods on 33 target LLMs/defenses ([Mazeika et al., arXiv 2402.04249](https://arxiv.org/abs/2402.04249)). NIST AI 600-1 (GenAI Profile, published 2024-07-26) describes red-teaming as structured testing to probe for flaws and links it to pre-deployment testing ([NIST page](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence); red-teaming wording came from search snippet of the [PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), UNVERIFIED against full text). Tools (as-of 2026-11-20): [garak](https://github.com/NVIDIA/garak) (probes + detectors, reports FAIL rate per probe/detector), [PyRIT](https://microsoft.github.io/PyRIT/1.2.0/) (Microsoft AI Red Team; multi-turn Crescendo/TAP/Skeleton Key, scorers, memory).

**Failure modes.**
- Automated attack success rate reported without a validated judge; scorer error dominates (HarmBench motivation: no common standard, [source](https://arxiv.org/abs/2402.04249)).
- Red team coverage narrow (one attack family); a one-off exercise rather than continuous.
- Findings not converted into regression tests.
- Attacker/crowdworker diversity limits (Ganguli documents methodology uncertainties, [source](https://arxiv.org/abs/2209.07858)).

**Practice (3-4h).** Pick a small chatbot with a system prompt and a policy (e.g., no medical dosing). Run garak with 2 probe families, plus 30 hand-written multi-turn attacks and 30 LM-generated (Perez method). Judge with a rubric; compute attack success rate with CI; add every successful attack to a regression file.

**Mastery check.**
1. Compare human, LM-generated, and tool-driven red teaming on cost, diversity, realism.
2. How do you validate the judge for attack success?
3. Define scope, threat model, and stopping criteria for a red-team exercise.

**Sources.** [Ganguli 2209.07858](https://arxiv.org/abs/2209.07858); [Perez 2202.03286](https://arxiv.org/abs/2202.03286); [HarmBench](https://arxiv.org/abs/2402.04249); [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [garak](https://github.com/NVIDIA/garak); [PyRIT](https://microsoft.github.io/PyRIT/1.2.0/).

---

## prompt-injection-security-testing

**Why it matters.** OWASP Top 10 for LLM Applications 2025 lists LLM01 Prompt Injection first, plus LLM02 Sensitive Information Disclosure, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage ([OWASP GenAI](https://genai.owasp.org/llm-top-10/)). Indirect injection: retrieved data can carry instructions; demonstrated on Bing Chat and code-completion engines, with data theft, worming, and API-call control; "effective mitigations are currently lacking" as of the paper ([Greshake et al., arXiv 2302.12173](https://arxiv.org/abs/2302.12173)). AgentDojo: 97 tasks and 629 security test cases; even without attacks models fail many tasks; attacks break some but not all security properties ([Debenedetti et al., arXiv 2406.13352](https://arxiv.org/abs/2406.13352)). NIST AI 100-2 E2025 (March 2025) is the AML taxonomy and terminology ([NIST CSRC](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)); attack-category details inside the PDF UNVERIFIED (PDF did not parse). Anthropic's guidance separates direct (user adversary) from indirect (untrusted third-party content) injection; recommends untrusted content only in `tool_result`, JSON-encoding it, least privilege, screening tool outputs, and red-teaming your own agent ([Anthropic mitigate jailbreaks](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), as-of 2026-11-20).

**Failure modes.**
- Testing only direct jailbreaks; missing indirect injection via emails, web pages, tool output.
- Measuring "model refused" instead of "action not taken" (agent side effects, exfiltration channel).
- Defenses (classifier screens) never tested for bypass; a screen model can itself refuse or be injected (Anthropic notes `stop_reason: "refusal"` handling, [source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)).
- Static attack set: attackers adapt; AgentDojo is designed as a dynamic environment ([arXiv 2406.13352](https://arxiv.org/abs/2406.13352)).
- Over-privileged tools make any success severe.

**Practice (3-4h).** Build a toy email-summarizer agent with 2 tools (read_inbox, send_email). Plant 10 injected emails (exfiltrate secret, send mail to attacker, system prompt leak). Metric: attacker goal achieved (tool call log), not text. Then apply two mitigations (JSON-encode + tool-output screen; least-privilege) and rerun; report ASR before/after plus utility on 20 benign tasks (AgentDojo's utility/security pairing).

**Mastery check.**
1. Map each OWASP LLM01/LLM06/LLM07 item to a test you wrote.
2. Why report utility alongside ASR?
3. Explain why no defense can be declared "passed" by a finite test set.

**Sources.** [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/); [Greshake](https://arxiv.org/abs/2302.12173); [AgentDojo](https://arxiv.org/abs/2406.13352); [NIST AI 100-2e2025](https://csrc.nist.gov/pubs/ai/100/2/e2025/final); [Anthropic mitigate-jailbreaks](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks); [garak](https://github.com/NVIDIA/garak) (encoding-based prompt injection probes, as-of 2026-11-20).

---

## fairness-and-bias-testing

**Why it matters.** BBQ (ACL 2022 Findings): hand-built QA sets over nine social dimensions; under-informative contexts elicit stereotyped answers; accuracy up to 3.4 points higher when the correct answer aligns with the bias, >5 for gender in most models ([Parrish et al., arXiv 2110.08193](https://arxiv.org/abs/2110.08193)). Classical definitions: Hardt et al. propose an "oblivious" criterion depending only on joint statistics of predictor, target, protected attribute (equal opportunity; [arXiv 1610.02413](https://arxiv.org/abs/1610.02413); equalized-odds definition itself not on abstract page, see Fairlearn). Fairlearn: demographic parity = equal selection rates (difference 0 / ratio 1); equalized odds = equal TPR and FPR across groups, difference is the larger of the two gaps; check intersecting subgroups, small groups have less data, multiple comparisons need correction (e.g., Bonferroni) ([Fairlearn docs](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html), as-of 2026-11-20). HELM includes fairness and bias among 7 metrics ([arXiv 2211.09110](https://arxiv.org/abs/2211.09110)).

**Failure modes.**
- Choosing one metric without noting incompatibility between definitions (UNVERIFIED here; Hardt/Fairlearn pages do not state it).
- Small subgroup sizes producing noisy gaps; no CIs, and multiple-comparison inflation ([Fairlearn](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html)).
- Benchmark-only testing (BBQ is U.S. English-centric, [arXiv 2110.08193](https://arxiv.org/abs/2110.08193)); doesn't reflect your app's demographics.
- Proxy attributes; counterfactual name-swap only.
- Generation bias (free text) measured with classification-style metrics.

**Practice (3h).** (a) Classical: train a small classifier on a tabular dataset (e.g., UCI Adult), compute MetricFrame by group, demographic parity and equalized-odds differences with bootstrap CIs. (b) LLM: counterfactual name/pronoun-swap pairs on 100 prompts for your app, measure outcome-difference rate (an MT relation), run 50 BBQ items.

**Mastery check.**
1. Compute and interpret demographic parity difference vs. equalized-odds difference on a toy table.
2. Which metric fits a hiring-screen LLM vs. a customer-support bot, and why?
3. How many samples per group do you need to detect a 5-point gap?

**Sources.** [BBQ](https://arxiv.org/abs/2110.08193); [Hardt 2016](https://arxiv.org/abs/1610.02413); [Fairlearn](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html); [HELM](https://arxiv.org/abs/2211.09110).

---

## safety-and-harm-evals

**Why it matters.** Two-sided: harmful compliance and over-refusal. XSTest (NAACL 2024): 250 safe prompts across ten types that should not be refused plus 200 unsafe contrast prompts; finds exaggerated-safety failures ([Röttger et al., arXiv 2308.01263](https://arxiv.org/abs/2308.01263)). AILuminate v1.0 (MLCommons): 12 hazard categories, five-tier grade from Poor to Excellent with entropy-based evaluation; prompt count not on abstract (UNVERIFIED) ([arXiv 2503.05731](https://arxiv.org/abs/2503.05731)). HarmBench for refusal robustness ([arXiv 2402.04249](https://arxiv.org/abs/2402.04249)). Classifiers as graders/guards: Llama Guard (Llama2-7b instruction-tuned, taxonomy-customizable; matches or beats moderation tools on OpenAI Moderation eval and ToxicChat) ([Inan et al., arXiv 2312.06674](https://arxiv.org/abs/2312.06674)). Anthropic's example success criterion: under 0.1% of outputs flagged for toxicity in 10,000 trials ([Anthropic develop-tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)). NIST AI 600-1 lists twelve GenAI risks ([NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence); count from search snippet, UNVERIFIED).

**Failure modes.**
- Optimizing refusal rate only; over-refusal (XSTest) ignored.
- Grader (classifier or LLM judge) bias/miscalibration; taxonomy mismatch with your policy ([Llama Guard](https://arxiv.org/abs/2312.06674) is customizable for this reason).
- Public benchmark contamination/saturation (author judgement).
- Zero-hit result on a small sample read as "safe": 0 failures in 1,000 trials still permits a rate up to ~0.3% at 95% (rule of three; author math).
- Ignoring multi-turn and context-dependent harms (Perez shows conversational harms, [arXiv 2202.03286](https://arxiv.org/abs/2202.03286)).

**Practice (3-4h).** Define a 4-category policy for your app. Build 40 harmful + 40 benign-but-similar prompts per category (XSTest style). Grade with rubric + Llama Guard or LLM judge; hand-label 50 to estimate judge agreement. Report harmful-compliance rate and over-refusal rate with CIs; plot the tradeoff across two system-prompt variants.

**Mastery check.**
1. Why both unsafe-compliance and false-refusal rates?
2. Estimate the upper bound on harm rate after 0/500 observed failures.
3. How do you check that an automated safety grader agrees with your policy?

**Sources.** [XSTest](https://arxiv.org/abs/2308.01263); [AILuminate](https://arxiv.org/abs/2503.05731); [HarmBench](https://arxiv.org/abs/2402.04249); [Llama Guard](https://arxiv.org/abs/2312.06674); [Anthropic develop-tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests); [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).

---

## performance-latency-cost-testing

**Why it matters.** Latency and price are named success criteria in Anthropic's eval guidance ([develop-tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)). Definitions: TTFT = time to first token; levers are model choice, shorter prompts/outputs, `max_tokens`, streaming; asking for exact word counts is less effective than sentence/paragraph limits; optimize latency only after establishing quality ([Anthropic reduce-latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency), as-of 2026-11-20). Load tooling: vLLM `bench serve` reports TTFT, ITL, TPOT, throughput; request-rate Poisson arrival, burstiness, max-concurrency, ramp-up; repeated runs can hit prefix cache and inflate throughput ([vLLM docs](https://docs.vllm.ai/en/latest/benchmarking/cli.html), as-of 2026-11-20). Cost: token counting endpoint is free (rate-limited), is an estimate, and newer-tokenizer Claude models yield ~30% more tokens for the same text, so recount per model ([Anthropic token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting), as-of 2026-11-20). OWASP LLM10 Unbounded Consumption is the security framing ([OWASP](https://genai.owasp.org/llm-top-10/)). Batch-invariant kernels cost speed ([Thinking Machines](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)), a determinism/latency tradeoff.

**Failure modes.**
- Reporting mean latency, not p95/p99 (author judgement).
- Benchmarking with unrealistic prompt/output length distributions or a cache-warm server ([vLLM caution](https://docs.vllm.ai/en/latest/benchmarking/cli.html)).
- Cost estimated from old model's token counts after migration ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/token-counting)).
- Cheaper/faster config adopted without quality regression check; the Anthropic cookbook for latency pairs each technique with a quality-threshold check ([reduce-latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)).
- Agent loops: unbounded tool calls/retries blow the cost budget.

**Practice (2-3h).** Replay 200 realistic prompts at fixed concurrency (1, 4, 16) against your endpoint (or local vLLM). Record TTFT, total latency, input/output tokens per request; compute p50/p95/p99, cost per 1k requests. Apply one change (shorter prompt or smaller model), re-measure, and check quality on the golden set. Add a budget assertion (p95 < X s, cost/request < Y) to CI.

**Mastery check.**
1. Why p95 not mean; what does concurrency do to TTFT?
2. Predict cost change on migrating to a model with a different tokenizer; verify by count.
3. Define a release criterion combining quality, latency, cost.

**Sources.** [Anthropic reduce-latency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency); [vLLM benchmarking](https://docs.vllm.ai/en/latest/benchmarking/cli.html); [Anthropic token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting); [OWASP](https://genai.owasp.org/llm-top-10/).

---

## Gaps and uncertainties

- Prerequisite IDs all resolve to existing stubs (eval-harness-design, golden-datasets, baselines-and-thresholds, nondeterminism-and-variance, confidence-intervals-for-evals, software-testing-fundamentals, programmatic-checks, test-oracle-problem, coverage-and-slicing, rubric-design).
- Boundary overlap: `safety-and-harm-evals` (bridge: none) overlaps with red-teaming and 04-system-specific/07; `robustness-testing` vs. `metamorphic-and-property-testing` share perturbation/invariance techniques (Cho et al. treat paraphrase invariance as MR); `flaky-test-management` vs. `determinism-control-and-mocking` need a clear split (cause control vs. handling residual variance). `fairness-and-bias-testing` has bridge `stats` but prerequisite is only coverage-and-slicing; CIs/multiple comparisons (confidence-intervals-for-evals) should probably be a prerequisite. `safety-and-harm-evals` depends on LLM-judge calibration (03-measurement-methods) not listed. `prompt-injection-security-testing` prerequisite is red-teaming only; consider agent/tool-use evals (04) as related.
- Unverified: CheckList MFT/INV/DIR definitions; Hardt equalized-odds definition from paper; NIST AI 100-2e2025 and AI 600-1 body text (PDFs unparsed; only abstract/search snippets); AILuminate prompt count; Google flaky-test statistics (page body not retrievable); Luo 2014 details via search snippet only (ACM 403); Chen 2018 details via search snippet only; "11% MT-only" figure; VCR.py sensitive-data filtering; Hypothesis shrinking.
- Missing candidates for `map/05-testing-in-engineering/_candidates.md`: (1) test-time statistical assertions (pass@k / pass-rate with CI as a test primitive); (2) eval data management (contamination, test-set rotation); (3) trace/record-replay for agents (tool-call mocking, simulators); (4) canary/shadow deployment and rollback testing; (5) test-case generation with LLMs (synthetic tests, mutation); (6) mutation testing for prompts; (7) privacy/PII leakage and memorization testing (OWASP LLM02); (8) guardrail/classifier testing (Llama Guard-style components); (9) model-migration testing playbook (deprecation-driven); (10) LLM-as-judge unit-testing (judge regression); (11) structured-output/schema conformance testing; (12) accessibility/multilingual testing.

## Landscape items (as-of 2026-11-20)

- promptfoo CI/CD integration (Node >= 22.22.0 required, Node 24 recommended; JUnit/JSON/HTML output) - https://www.promptfoo.dev/docs/integrations/ci-cd/
- garak (NVIDIA) LLM vulnerability scanner - https://github.com/NVIDIA/garak
- PyRIT 1.2.0 (Microsoft AI Red Team) - https://microsoft.github.io/PyRIT/1.2.0/
- MLflow Prompt Registry; Langfuse Prompt Management - links above
- vLLM `vllm bench serve` metrics and options - https://docs.vllm.ai/en/latest/benchmarking/cli.html
- VCR.py record modes - https://vcrpy.readthedocs.io/en/latest/usage.html
- Fairlearn metrics (MetricFrame, demographic_parity_difference, equalized_odds_difference) - https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html
- Benchmarks: HarmBench, XSTest, BBQ, AILuminate v1.0, AgentDojo (97 tasks / 629 security cases), PromptBench/PromptRobust, HELM
- Standards: OWASP Top 10 for LLM Apps 2025; NIST AI 100-2 E2025 (2025-03); NIST AI 600-1 (2024-07-26)
- Provider specifics: Anthropic API version 2026-10-21 removes `temperature`/`top_p`/`top_k` (400 error); model lifecycle/retirement dates (claude-sonnet-4-5-20250929 retires 2026-11-30); new tokenizer ~30% more tokens on Claude 4.7+; OpenAI `seed` + `system_fingerprint` "mostly" deterministic
- Determinism research: Thinking Machines batch-invariant kernels (Qwen3-235B-A22B experiment, 80 unique/1000)
