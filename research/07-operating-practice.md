# Research: 07 Operating practice

Researched 2026-11-20. "As-of" dates = 2026-11-20 unless stated. Tag "practitioner" = non-primary. "UNVERIFIED" = not confirmed from a primary source in this session. Paywalled ISO standards: only catalogue pages read; content NOT verified.

Fetch notes: EUR-Lex official text and iso.org/standard pages blocked automated fetch (empty/403). EU AI Act article text was read from the Commission's AI Act Service Desk (ai-act-service-desk.ec.europa.eu), which is a Commission site but not the OJ; verify wording against EUR-Lex before quoting. Several iso.org pages were read via committee.iso.org mirrors.

---

## risk-and-governance-frameworks

**Why it matters**
- NIST AI RMF 1.0 (NIST AI 100-1, January 2023) is "intended to be voluntary, rights-preserving, non-sector-specific, and use-case agnostic" ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Part 1 intro). Four functions: GOVERN, MAP, MEASURE, MANAGE ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Part 2 Core).
- It gives evaluation a place in risk management: after MEASURE, "objective, repeatable, or scalable" TEVV processes "are in place, followed, and documented"; measurement "provides a traceable basis to inform management decisions" when trustworthiness characteristics trade off ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), MEASURE intro). TEVV "allows for both mid-course remediation and post-hoc risk management" ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Sec. 2 on lifecycle).
- Directly eval-relevant subcategories: MEASURE 2.1 (test sets, metrics, tools documented), 2.3 (performance measured "for conditions similar to deployment setting(s)"), 2.4 (production monitoring), 2.13 (effectiveness of the TEVV metrics/processes themselves evaluated), MEASURE 4.1 (measurement approaches informed by domain experts and end users), MANAGE 4.1 (post-deployment monitoring plans) ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Tables 3-4).
- Generative AI Profile (NIST AI 600-1, July 2024) lists 12 GAI risks, including Confabulation, Dangerous/Violent/Hateful Content, Data Privacy, Harmful Bias or Homogenization, Human-AI Configuration, Information Integrity, Information Security, Value Chain and Component Integration ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), Sec. 2). It states that current pre-deployment TEVV "may be inadequate, non-systematically applied, or fail to reflect or mismatched to deployment contexts", that human exams/video-game tests "do not guarantee" validity in those domains, and that benchmark-vs-real-world gaps are likely worsened by prompt sensitivity ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), App. A.1.4).
- Suggested actions to map to evals: MS-2.3-001 (baseline benchmark suites when choosing a model for fine-tuning/RAG), MS-2.3-002 (evaluate capability claims "using empirically validated methods"), MS-2.3-003 (share pre-deployment test results with release-approval actors), MP-2.3-005 (regular adversarial testing), MS-2.7-007 (red-teaming), MS-4.2-xxx (field/structured public feedback) ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), Sec. 3 tables).
- Structured public feedback listed: participatory engagement, field testing, AI red-teaming; follow human-subjects practices such as informed consent and compensation ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), App. A.1.5).
- Status: NIST says it expects a formal review of AI RMF "no later than 2028" ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Update Schedule). Whether any revision or successor was issued before 2026-11-20: UNVERIFIED (not searched).
- Other frameworks: ISO/IEC 23894:2023 AI risk-management guidance, Edition 1, Feb 2023, guidance only (not certifiable) ([ISO catalogue](https://www.iso.org/standard/77304.html), via search summary; direct fetch 403; content not verified). OECD AI Principles (adopted 2019, updated May 2024; five value-based principles incl. "Robustness, security and safety", "Accountability") ([OECD.AI](https://oecd.ai/en/ai-principles)).

**Common failure modes**
- Treating RMF as a checklist/certification: it is voluntary and use-case agnostic; no conformance mark ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)). Document-only compliance with no actual TEVV (inference from MEASURE 2.13 which asks whether the TEVV itself is effective).
- Using GAI Profile actions without a context profile: AI 600-1 itself says its list is "not exhaustive" and use-case profiles are implementations of the Core ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Sec. 6 Profiles; [AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), App. A).
- Relying on lab benchmarks as evidence of deployment risk (explicitly warned against, A.1.4 above).

**Practice exercise (2-3 h)**
Pick a small LLM app (e.g. a RAG helper). Build a one-page crosswalk: list its top 5 risks from AI 600-1 Sec. 2, and for each name one MAP/MEASURE/MANAGE subcategory and one concrete eval or monitor that would produce evidence (test set, metric, threshold, owner). Mark gaps where no eval exists.

**Mastery check**
1. Explain what MEASURE 2.13 asks and why "evaluating the evaluation" matters for LLM judges and benchmarks.
2. Given a risk (confabulation in a support bot), name the GOVERN/MAP/MEASURE/MANAGE artifacts you would expect and which are eval outputs.
3. Why does AI 600-1 say benchmark and exam performance do not establish validity, and what does it propose in addition?

**Primary sources**
- https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf (read in full text)
- https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf (read in full text)
- https://oecd.ai/en/ai-principles
- https://www.iso.org/standard/77304.html (catalogue; not verified in content)

---

## regulatory-compliance

**Why it matters** (status as-of 2026-11-20)
- EU AI Act = Regulation (EU) 2024/1689 (EUR-Lex CELEX 32024R1689; official text not fetched: [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)).
- Timeline per Commission page (last updated 19 Oct 2026): in force 1 Aug 2024; prohibitions + AI literacy from 2 Feb 2025; GPAI obligations and governance from 2 Aug 2025; general application 2 Aug 2026 with AI Office enforcement powers over GPAI; high-risk Annex III moved to 2 Dec 2027; Annex I (products) to 2 Aug 2028; new prohibition 9 (non-consensual sexual content/CSAM generation) from Dec 2026 ([Commission AI Act policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)).
- CHANGED: the "AI Omnibus" amended the Act. Per the Commission it was proposed 19 Nov 2025, politically agreed 7 May 2026, in force 27 July 2026 ([Commission page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)). Service Desk Article 113 shows para (a), (c) amended and (d) new, and Art 5(1)(ba),(bb),(1a),(1b) applying from 2 Dec 2026 ([Art. 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113)). The regulation number of the omnibus (reported by search results as 2026/1744, OJ publication 24 July 2026) is UNVERIFIED from primary sources (only law-firm summaries; EUR-Lex blocked).
- Transparency (Art. 50) timing: Commission page says "August 2026"; whether the omnibus altered any Art. 50 date is UNVERIFIED (one secondary source says not delayed). Re-check before relying.
- Testing/documentation obligations that matter for evals (Service Desk text; verify vs OJ):
  - Art. 9(6)-(8): high-risk systems "shall be tested for the purpose of identifying the most appropriate and targeted risk management measures"; testing "at any time throughout the development process" and before placing on market, "against prior defined metrics and probabilistic thresholds" ([Art. 9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9)).
  - Annex IV 2(g): technical documentation includes validation/testing procedures and data, metrics for accuracy, robustness, compliance incl. "potentially discriminatory impacts", and dated, signed test logs and reports; point 3: accuracy "for specific persons or groups of persons"; point 4: appropriateness of performance metrics ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)).
  - Art. 72: providers must "actively and systematically collect, document and analyse" performance data over the lifetime; the monitoring plan is part of the Annex IV documentation; Commission template due by 2 Sept 2027 ([Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72)).
  - Art. 55(1): GPAI with systemic risk must perform model evaluation "in accordance with standardised protocols and tools reflecting the state of the art", including documented adversarial testing, and report serious incidents to the AI Office ([Art. 55](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-55)). Art. 51(2): presumption of systemic risk above 10^25 training FLOP ([Art. 51](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-51)).
  - Art. 15 (accuracy/robustness/cybersecurity), Art. 53 (GPAI documentation), Art. 4 (AI literacy), Art. 50: text not fetched (429/time). UNVERIFIED.
  - Penalties Art. 99: up to EUR 35M / 7% (prohibited practices), EUR 15M / 3% (other operator obligations), EUR 7.5M / 1% (misleading information), higher of the two for undertakings ([Art. 99](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99)).
- GPAI guidance: Commission guidelines on scope of GPAI obligations published 18 July 2025, page updated 20 Apr 2026 ([Commission](https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act)); voluntary GPAI Code of Practice published 10 July 2025 with Transparency, Copyright, Safety & Security chapters and a Model Documentation Form; signatories incl. Anthropic, Google, OpenAI, Microsoft, Mistral; xAI signed only Safety & Security (page updated 7 Oct 2026) ([Commission](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)). Commission page also reports a first harmonised standard published 19 Oct 2026 (title not verified) ([Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)).
- US state example: Colorado SB 24-205 was repealed and re-enacted by SB 26-189 ("Automated Decision-Making Technology"), signed 14 May 2026, with developer documentation requirements from 1 Jan 2027 ([Colorado General Assembly](https://leg.colorado.gov/bills/sb26-189)). Earlier delay to 30 June 2026 and a court-ordered enforcement pause are from secondary sources only (UNVERIFIED).

**Common failure modes**
- Using pre-omnibus dates (2 Aug 2026 for high-risk) in plans.
- Assuming a model provider's compliance covers the deployer's duties; role (provider vs deployer vs downstream modifier) decides obligations (GPAI scope guidelines above; detail UNVERIFIED).
- Treating internal eval logs as compliance evidence without dated sign-off, pre-defined thresholds and group-level metrics (Art. 9(8), Annex IV above).
- Assuming a high-risk classification absent from a generic LLM app; classification depends on Annex III use case (Annex III page: https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3, not read in detail).

**Practice exercise (2-3 h)**
Take your capstone app. (1) Decide role and risk class using the Commission page and Annex III. (2) Build a table mapping each applicable obligation (Art. 9, Annex IV 2(g), Art. 72) to an eval artifact you already produce, with missing items flagged. (3) Record the date you checked status.

**Mastery check**
1. State current application dates for prohibitions, GPAI, Annex III and Annex I high-risk, and what changed in 2026.
2. What must a high-risk test report contain under Annex IV, and why do "prior defined metrics and thresholds" matter for how you write eval acceptance criteria?
3. When does a model fall under Art. 55 evaluation duties, and what does adversarial testing there require?
4. Why can a company be compliant under the EU Act yet affected differently by US state law (Colorado example)?

**Primary sources**
- https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (as-of page update 2026-10-19)
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9, /article-51, /article-55, /article-72, /article-99, /article-113, /annex-4
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 (official text; not fetched)
- https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
- https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act
- https://leg.colorado.gov/bills/sb26-189

---

## standards

**Why it matters**
- ISO/IEC 42001:2023, Edition 1, published 2023-12, stage 60.60; requirements for establishing, implementing, maintaining and continually improving an AI management system (AIMS); no amendments listed ([ISO via committee.iso.org](https://committee.iso.org/standard/42001)). Certification voluntary ([ISO explainer](https://www.iso.org/insights/iso-42001-explained), via search summary). Annex A control count (38 controls/9 objectives) from a third-party paper only: UNVERIFIED. Standard text paywalled; content NOT verified.
- ISO/IEC 42005:2025 (AI system impact assessment), Edition 1, May 2025 (lifecycle log 2025-05-28), published; designed to be used with 42001, 38507, 23894 ([ISO via committee.iso.org](https://committee.iso.org/standard/42005)).
- Other catalogue entries relevant to evaluation, per the SC 42 catalogue ([ISO/IEC JTC 1/SC 42 catalogue](https://committee.iso.org/committee/6794475/x/catalogue/)): ISO/IEC TS 25058:2024 (guidance for quality evaluation of AI systems); ISO/IEC 25059:2023 (quality model for AI systems); ISO/IEC TS 42119-2:2025 (overview of testing AI systems); ISO/IEC 42006:2025 (requirements for bodies auditing/certifying AIMS); ISO/IEC 5259-1..5:2024/2025 (data quality); ISO/IEC TR 24027:2021 (bias); ISO/IEC TS 12791:2024 (unwanted bias in classification/regression); ISO/IEC TR 24029-1:2021 and 24029-2:2023 (robustness); ISO/IEC TR 24028:2020 (trustworthiness); ISO/IEC 23894:2023 (risk). As of the catalogue read, no 42001 amendment published. ISO/IEC 29119-11 (testing AI-based systems) was not on the page: UNVERIFIED either way.
- Link to EU law: the Commission page notes a first harmonised standard supporting the AI Act published 19 Oct 2026 ([Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)); which standard: UNVERIFIED.

**Common failure modes**
- Equating 42001 certification with a tested system: it certifies a management system, not a model's quality (inference from scope statement above; scope text only).
- Citing a standard from titles without reading it (all content here UNVERIFIED).
- Assuming ISO conformance gives EU AI Act presumption of conformity; only harmonised standards cited in the OJ do (general EU law principle; AI Act Art. 40 text not fetched: UNVERIFIED).

**Practice exercise (2 h)**
Build a catalogue table (number, title, year, status, purchasable price, what evidence an eval team could produce for it) from the SC 42 catalogue; pick two (25058, 42119-2) and read the free preview/scope pages; note what you cannot verify without purchase.

**Mastery check**
1. Distinguish management-system standards (42001, 42006) from guidance (23894, 25058) and from quality models (25059).
2. Which standard would you consult for impact assessment vs quality evaluation vs testing AI?
3. What can and cannot a 42001 certificate tell a customer about your eval quality?

**Primary sources**
- https://committee.iso.org/standard/42001 ; https://committee.iso.org/standard/42005 ; https://committee.iso.org/committee/6794475/x/catalogue/
- https://www.iso.org/standard/77304.html (23894 catalogue)
- https://www.iso.org/insights/iso-42001-explained
(All catalogue-level; standard contents not verified.)

---

## model-and-system-documentation

**Why it matters**
- Model Cards (Mitchell et al., FAT* 2019, arXiv v1 5 Oct 2018, v2 14 Jan 2019): short documents accompanying models that report benchmarked evaluation, intended use contexts, evaluation procedures; call for results disaggregated by cultural, demographic or phenotypic groups and intersections ([arXiv 1810.03993](https://arxiv.org/abs/1810.03993)).
- Datasheets for Datasets (Gebru et al.): documentation of motivation, composition, collection process, recommended uses; v1 Mar 2018, CACM Dec 2021 (v8 1 Dec 2021) ([arXiv 1803.09010](https://arxiv.org/abs/1803.09010)).
- Hugging Face model cards: README.md plus YAML metadata; should describe intended uses/limitations, training info, datasets and evaluation results; structured eval results via `model-index`, with a newer simpler format ([HF docs](https://huggingface.co/docs/hub/model-cards)). As-of 2026-11-20, volatile.
- System cards (frontier providers): Anthropic says they "document the capabilities, safety evaluations, and responsible deployment decisions for Claude models"; one per model release, latest Nov 2026 ([Anthropic system cards](https://www.anthropic.com/system-cards)). OpenAI's GPT-4 report arXiv page ([arXiv 2303.08774](https://arxiv.org/abs/2303.08774)) did not confirm a system card; OpenAI system-card page blocked (403): UNVERIFIED.
- Regulatory pull: EU Annex IV technical documentation (test logs, metrics, group accuracy) and GPAI Code of Practice Model Documentation Form (see regulatory-compliance); NIST MEASURE 2.1 requires test sets, metrics and tools to be documented, and MS-2.3-003 asks to share pre-deployment results with release-approval actors ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf); [AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)).
- Benchmark documentation quality: BetterBench scored 24 benchmarks against 46 best practices; found wide quality variation, most did not report statistical significance, many hard to replicate ([arXiv 2411.12990](https://arxiv.org/abs/2411.12990)). Construct-validity review of 445 LLM benchmarks (Bean et al., NeurIPS 2025 D&B) offers a checklist ([arXiv 2511.04703](https://arxiv.org/abs/2511.04703); numbers from search summary, 53.4% reported construct validity evidence; verify in paper).

**Common failure modes**
- Aggregate-only numbers (hides subgroup failure; the Model Cards motivation).
- Eval section without test-set provenance, prompt template, sampling settings, judge model/version, so results are not reproducible (derived from MEASURE 2.1 requirement; also BetterBench replicability finding).
- Card written once and not versioned with the model/prompt/system change.
- Card documents the model but not the system (retrieval, tools, guardrails), where the actual risk sits (inference; AI 600-1 stresses value chain and component integration risk).

**Practice exercise (3 h)**
Write a system card for your capstone app with: intended/out-of-scope use, components and versions, eval datasets (provenance, size, date), metrics with CIs, disaggregated slices, known failures, red-team findings, monitoring plan. Then check it against Annex IV 2(g) and MEASURE 2.1 and list missing fields.

**Mastery check**
1. What must be in an eval section for a third party to reproduce it?
2. Why disaggregate, and how many slices before noise dominates (link to CI node)?
3. Compare model card, datasheet, system card, Annex IV file: audience, scope, update trigger.

**Primary sources**
- https://arxiv.org/abs/1810.03993 ; https://arxiv.org/abs/1803.09010
- https://huggingface.co/docs/hub/model-cards
- https://www.anthropic.com/system-cards
- https://arxiv.org/abs/2411.12990 ; https://arxiv.org/abs/2511.04703
- https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai

---

## responsible-ai-ethics

**Why it matters**
- Ethical commitments decide what gets evaluated. OECD AI Principles (2019, updated May 2024): inclusive growth/well-being; human rights and democratic values incl. fairness and privacy; transparency and explainability; robustness, security and safety; accountability ([OECD.AI](https://oecd.ai/en/ai-principles)).
- Weidinger et al. (DeepMind, Dec 2021) taxonomy of 21 risks in six areas: discrimination/exclusion/toxicity; information hazards; misinformation harms; malicious uses; human-computer interaction harms; automation, access and environmental harms. Good source for choosing eval targets ([arXiv 2112.04359](https://arxiv.org/abs/2112.04359)).
- NIST: trustworthiness tradeoffs need traceable measurement; MEASURE 2.2 requires human-subject evaluations to meet protection requirements and be representative; GOVERN 5.1 asks for feedback from those external to the team; AI 600-1 says feedback activities should follow informed consent and compensation ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf); [AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)).
- Corporate example: Microsoft Responsible AI Standard v2 (June 2022): goals of accountability, transparency, fairness, reliability and safety, privacy and security, inclusiveness; Goal A1 impact assessment ([Microsoft PDF](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf), via search summary; text not read directly). Impact assessment ISO/IEC 42005 (see standards).
- EU Act Annex IV explicitly asks for "potentially discriminatory impacts" in test metrics ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)).

**Common failure modes**
- Ethics as principles list with no measurable eval (principle-to-metric gap).
- Choosing metrics because they are easy, so harms to affected groups go unmeasured (Weidinger taxonomy as a coverage check).
- Evaluating with crowdworkers/red-teamers without consent, compensation or exposure safeguards (AI 600-1 above).
- Evaluating only majority-user performance.

**Practice exercise (2-3 h)**
Run a mini impact assessment for your app: list affected stakeholders (users, non-users), map to Weidinger risk areas, choose which ones you will not evaluate and write down why, and define one eval or monitor per accepted risk.

**Mastery check**
1. Translate one OECD principle into a testable requirement and a metric with threshold.
2. What harms does your eval suite not cover, and who bears them?
3. When do evaluation procedures themselves need ethics review?

**Primary sources**
- https://oecd.ai/en/ai-principles ; https://arxiv.org/abs/2112.04359
- NIST AI 100-1 / 600-1 (above)
- Microsoft RAI Standard v2 PDF (corporate practice; read via search summary only)
- UNESCO Recommendation on the Ethics of AI (2021): NOT researched; add if wanted.

---

## team-roles-and-process

**Why it matters**
- NIST GOVERN 2.1: "Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear"; GOVERN 2.3: executive leadership takes responsibility for risk decisions; GOVERN 4.1: safety-first, critical-thinking culture; MEASURE 4.1: measurement approaches "informed through consultation with domain experts and other end users" ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Tables 1-3). AI 100-1 says subject matter experts help evaluate TEVV findings and align TEVV parameters to requirements (Sec. 2 / AI actors). TEVV actors are integrated across the lifecycle ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Sec. 2).
- Shankar et al. ("Who Validates the Validators?", Apr 2024): human-in-loop; "criteria drift": users need criteria to grade outputs, but grading outputs helps define criteria, so criteria cannot be fully fixed up front ([arXiv 2404.12272](https://arxiv.org/abs/2404.12272)). Implication: domain-expert grading must be iterative, with engineers building tooling.
- Provider guidance: Anthropic docs favor task-specific evals mirroring the real distribution, including edge cases where even humans disagree; automation where possible; volume over hand-graded quality; LLM graders ideally a different model from the generator ([Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), as-of 2026-11-20).
- Practitioner (tagged): Hamel Husain describes unit tests, human+model eval, A/B tests; reviewers must keep reading data; look at data with low-friction viewers ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).
- EU Act: Annex IV test reports must be "dated and signed by accountable people" ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)), implying named owners.

**Common failure modes**
- No named owner for eval quality; evals owned by whoever last touched the prompt (inference from GOVERN 2.1).
- Domain experts used only at the end, or asked to write fixed rubrics before seeing outputs (criteria drift).
- Eval author = system author with no independent review (inference; UNVERIFIED as a documented primary-source claim).
- Whack-a-mole prompt fixing without regression evals (practitioner: Husain).
- Judge never validated against human labels (Shankar; Husain).

**Practice exercise (2 h)**
Write a RACI for your eval lifecycle (dataset curation, rubric, judge calibration, release gate, incident review, periodic re-audit). Then run a 30-example rubric session with one other person grading blind, record disagreements, revise rubric, report agreement.

**Mastery check**
1. Who has authority to block a release on eval results, and where is it written?
2. Describe criteria drift and how your process handles it.
3. What cadence for refreshing test sets, recalibrating judges, and re-reviewing thresholds, and what triggers an unscheduled review?

**Primary sources**
- https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf ; https://arxiv.org/abs/2404.12272 ; https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- practitioner: https://hamel.dev/blog/posts/evals/

---

## eval-maturity-model

**Why it matters**
- No authoritative, widely adopted "LLM eval maturity model" was found in primary sources (UNVERIFIED that none exists; limited search). Treat this node as a synthesized model, labeled as such.
- Adjacent primary-ish anchors for staging: Google Cloud MLOps levels 0 (manual, notebooks, no CI/CD, rare monitoring), 1 (pipeline automation, automated data/model validation, triggers incl. drift), 2 (CI/CD around pipelines, automated tests, staged rollouts) ([Google Cloud architecture doc](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning); undated on page). Practitioner staging: unit-test evals, human+model eval, A/B testing ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).
- Regulatory/standards evidence for what a "mature" org shows: documented TEVV and metric effectiveness review (MEASURE 2.1, 2.13), monitoring plans (MANAGE 4.1), roles (GOVERN 2.1) ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)); management-system continual improvement (ISO/IEC 42001 scope, [ISO](https://committee.iso.org/standard/42001)).
- Benchmark/eval quality evidence: BetterBench 46 practices; construct-validity checklist ([arXiv 2411.12990](https://arxiv.org/abs/2411.12990); [arXiv 2511.04703](https://arxiv.org/abs/2511.04703)). These can serve as top-level criteria.

**Common failure modes**
- Skipping levels (LLM judge dashboards without any human-labelled gold set).
- Maturity measured by tool count rather than decision quality.
- Treating maturity levels as universal rather than per risk tier (inference).
- Stuck at "vibe checks" (practitioner: Husain).

**Practice exercise (3 h)**
Draft a 4-5 level rubric along dimensions (datasets, metrics validity, judge calibration, automation/CI gates, monitoring, ownership, documentation, reporting with uncertainty). Anchor each level to a verifiable artifact and a cited source above. Score your capstone and name the next-level step with highest risk reduction.

**Mastery check**
1. For one dimension, define observable evidence that separates level 2 from level 3.
2. How would you validate that the maturity rubric itself predicts better release decisions?
3. Which levels are mandatory for a high-risk EU use case versus a prototype?

**Primary sources**
- https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf ; https://arxiv.org/abs/2411.12990
- practitioner: https://hamel.dev/blog/posts/evals/

---

## eval-reporting-and-communication

**Why it matters**
- Miller, "Adding Error Bars to Evals" (arXiv 2411.00640, 1 Nov 2024): evals are experiments; gives formulas for error bars, clustered standard errors, paired differences, power analysis, with reporting recommendations ([arXiv](https://arxiv.org/abs/2411.00640)).
- BetterBench: most benchmarks do not report statistical significance ([arXiv 2411.12990](https://arxiv.org/abs/2411.12990)).
- NIST AI 600-1 on limits: lab/benchmark results may not extrapolate; share pre-deployment results with release authorities (MS-2.3-003) ([AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)). Construct validity paper supplies a reporting checklist ([arXiv 2511.04703](https://arxiv.org/abs/2511.04703)).
- Compliance reports need dated, signed test logs with pre-defined thresholds (Art. 9(8), Annex IV above).
- Cost/latency belong in the report alongside quality (inference).

**Common failure modes**
- Point estimates without intervals; ranking models on differences within noise (Miller).
- Unpaired comparisons when same questions were used (Miller).
- Ignoring clustering (questions sharing a passage) so intervals are too narrow (Miller).
- Single aggregate hiding slice regressions (Model Cards disaggregation).
- Reporting a benchmark score as capability without construct validity (Bean et al.).
- Reporting only pass rate, not what was *not* tested (limits section).

**Practice exercise (2-3 h)**
Take two prompt versions on a 200-item eval. Compute paired difference with 95% CI (bootstrap and analytic), a power calculation for the item count needed to detect a 3-point gap, and write a one-page decision memo: recommendation, effect size with interval, slices, cost, known gaps, residual risk.

**Mastery check**
1. A stakeholder says "v2 is 2 points better." What do you need before agreeing?
2. When do paired analysis and clustered SEs change the conclusion?
3. Write the "limits of this evaluation" paragraph for your memo.

**Primary sources**
- https://arxiv.org/abs/2411.00640 ; https://arxiv.org/abs/2411.12990 ; https://arxiv.org/abs/2511.04703
- https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

---

## eval-cost-management

**Why it matters**
- Provider batch discounts: Anthropic Message Batches API cuts cost 50%, most batches finish in under 1 hour, and the page lists large-scale evaluations as a use case; 29-day retention, not ZDR-eligible ([Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/batch-processing)). OpenAI Batch API: 50% discount, 24-hour window, lists running evaluations ([OpenAI docs](https://developers.openai.com/api/docs/guides/batch)). As-of 2026-11-20, volatile.
- Prompt caching (Anthropic): 5-minute cache write 1.25x, 1-hour write 2x, read 0.1x of base input (0.05x for Opus 5.5/Sonnet 5.5; 0.025x for some models); multipliers stack with batch discount; minimum cacheable prompt 512-4096 tokens by model ([Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)). As-of 2026-11-20, volatile. Useful when a long rubric or few-shot judge prompt is repeated.
- FrugalGPT (Chen, Zaharia, Zou, 2023): prompt adaptation, LLM approximation, LLM cascade; reports matching GPT-4 at up to 98% lower cost ([arXiv 2305.05176](https://arxiv.org/abs/2305.05176)). Applies to tiered judges (cheap judge first, escalate uncertain cases). Result is for specific 2023 models/datasets; generality to judging UNVERIFIED.
- Anthropic docs: "volume over quality" (more automated-graded questions beat fewer hand-graded) ([Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Statistical sample sizing from Miller (power analysis) bounds how many items you need ([arXiv 2411.00640](https://arxiv.org/abs/2411.00640)).

**Common failure modes**
- Cheaper judge adopted without re-validating agreement with humans (Shankar et al., [arXiv 2404.12272](https://arxiv.org/abs/2404.12272)).
- Cutting sample size below the power needed, then reading noise as signal (Miller).
- Running full suite on every commit instead of tiering (smoke -> nightly -> release); not caching deterministic outputs; ignoring batch/caching for offline runs.
- Counting only API cost, not human grading time or engineer time (inference).
- Not logging cost per eval run, so spend is invisible.

**Practice exercise (2-3 h)**
Instrument an eval run to record tokens and cost per item and per judge call. Compare: sync full run, batch full run, cached-prefix run, and cascade (cheap judge, escalate low-confidence to strong judge) on 300 items. Report cost, wall time, and agreement with a 50-item human gold set.

**Mastery check**
1. Design a three-tier eval schedule (per-commit, nightly, release) with item counts justified by power analysis.
2. When does caching save money for judging and when not (minimum token, TTL)?
3. How do you prove a cheaper judge is acceptable?

**Primary sources**
- https://platform.claude.com/docs/en/build-with-claude/batch-processing ; .../prompt-caching ; https://developers.openai.com/api/docs/guides/batch
- https://arxiv.org/abs/2305.05176 ; https://arxiv.org/abs/2411.00640

---

## eval-tooling-landscape

**Why it matters**
- Categories (derived from docs read): (1) eval frameworks/harnesses with datasets, solvers, scorers, logs, agents, sandboxing, e.g. Inspect, developed by UK AI Security Institute and Meridian Labs ([Inspect](https://inspect.aisi.org.uk/)); (2) declarative eval + red-team CLIs, e.g. promptfoo (evals, red teaming, CI/CD) ([promptfoo](https://www.promptfoo.dev/docs/intro/)); (3) observability + evals + datasets + prompt management platforms, e.g. Langfuse (open source, tracing based on OpenTelemetry, LLM-as-judge, annotation queues, datasets) ([Langfuse](https://langfuse.com/docs)); (4) instrumentation standards: OpenTelemetry GenAI semantic conventions, now in a separate repo `semantic-conventions-genai` (Apache-2.0; spans, metrics, events; stability level not stated in README) ([OTel repo](https://github.com/open-telemetry/semantic-conventions-genai)); (5) cloud/provider-native eval features (not researched); (6) benchmark/leaderboard hubs (HF model-index) ([HF docs](https://huggingface.co/docs/hub/model-cards)).
- Practitioner advice: start with existing tools such as spreadsheets and custom data viewers before specialized products; avoid generic frameworks in place of problem-specific evals ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).

**Common failure modes**
- Selecting a tool before defining the eval questions; letting tool metrics (built-in "faithfulness" etc.) define quality without validation (practitioner; Shankar for validation).
- Lock-in via proprietary trace/dataset formats (inference).
- Relying on experimental semantic conventions that may change (stability UNVERIFIED).
- Treating tool availability as maturity.

**Practice exercise (3 h)**
Implement the same 20-item eval in two tools (e.g. Inspect and promptfoo). Record: setup time, how datasets and scorers are defined, log format/exportability, CI integration, judge configuration, cost visibility, and what a migration would require.

**Mastery check**
1. Classify any tool you meet into the five categories and list what it does not do.
2. What would you need to export to leave a platform?
3. Which tool features replace human review, and which only organize it?

**Primary sources**
- https://inspect.aisi.org.uk/ ; https://www.promptfoo.dev/docs/intro/ ; https://langfuse.com/docs ; https://github.com/open-telemetry/semantic-conventions-genai

---

## build-vs-buy

**Why it matters**
- No primary-source decision framework was found; this node rests on documented tool properties and practitioner advice. Facts: open-source, self-hostable options exist (Inspect, promptfoo, Langfuse per their docs above; licenses not stated on the pages read: UNVERIFIED, check repos). Batch API and `ZDR not eligible` data retention (29 days for Anthropic batch) are constraints for vendor/data-handling decisions ([Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/batch-processing)).
- Regulatory constraints on external tooling: Annex IV demands dated, signed records and Art. 72 lifetime monitoring evidence; whichever route you choose must export these ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4); [Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72)).
- Practitioner (tagged): start simple/in-house for data viewing; be wary of generic vendor evals for problem-specific quality ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).
- Criteria candidates (own synthesis, not sourced): data sensitivity/residency, exportability, judge transparency, CI fit, cost model, team capacity, vendor viability.

**Common failure modes**
- Building a custom harness for commodity needs (tracing, storage) or buying one that hides judge prompts and cannot reproduce results (inference).
- Underestimating maintenance of in-house harnesses (inference).
- Vendor/tool volatility: tools change ownership, pricing, and license; verify at decision time (as-of 2026-11-20 for tool facts above).

**Practice exercise (2 h)**
Write a one-page decision record for your capstone: weighted criteria, three options (in-house thin harness on an open-source runner; open-source platform self-hosted; commercial platform), evidence from docs for each criterion, exit plan, review date.

**Mastery check**
1. Which parts of eval infrastructure should never be outsourced (gold datasets, rubrics, thresholds)?
2. What is your lock-in exit cost in days?
3. How would you test a vendor's built-in metric before trusting it?

**Primary sources**
- Tool docs as in eval-tooling-landscape; https://platform.claude.com/docs/en/build-with-claude/batch-processing
- practitioner: https://hamel.dev/blog/posts/evals/
- GAP: no primary source for decision criteria. Suggest candidate sources: vendor license files and data processing terms (not researched).

---

## Gaps and uncertainties

Prerequisite/boundary problems
- risk-and-governance-frameworks has prerequisite `safety-and-harm-evals`, yet its content (NIST/OECD/ISO) is organisational; arguably prerequisite should be `eval-reporting-and-communication` or none. `regulatory-compliance` and `standards` both depend on it, fine.
- `model-and-system-documentation` has prerequisite `eval-reporting-and-communication`; plausible. But `eval-maturity-model` (L3) prerequisite only `team-roles-and-process`; it also needs documentation and tooling.
- `eval-tooling-landscape` (L1) prerequisite `eval-harness-design`: fine; `build-vs-buy` depends on it.
- Overlap: `responsible-ai-ethics` vs `fairness-and-bias-testing` and `safety-and-harm-evals`; keep it to "what to evaluate and why", not metrics.
- `team-roles-and-process` prerequisite `eval-driven-development` is in another branch; assumed to exist.
- `eval-cost-management` prerequisite `llm-as-judge` is outside branch; also needs `confidence-intervals-for-evals` (power analysis).
- `regulatory-compliance` description says "EU AI Act and other regulation"; US federal posture and other jurisdictions (UK, China, etc.) not researched; only Colorado checked.

Unverified / not researched
- EUR-Lex official text (blocked); omnibus regulation number and OJ date; Art. 4, 15, 40, 50, 53 text; Art. 50 timing after omnibus; Annex III page detail.
- ISO standard contents (paywalled); ISO/IEC 42001 Annex A control counts; 29119-11 status; 42119-2 content; harmonised standard published 19 Oct 2026 (identity unknown).
- Whether NIST revised or superseded AI RMF/AI 600-1 by 2026-11-20; NIST AI RMF Playbook not read.
- UNESCO Recommendation, Microsoft RAI standard (read only via search summary), Google/OpenAI/Meta frontier-safety frameworks not read.
- Colorado earlier delay details and court stay: secondary only.
- OpenAI system card page (403); OTel GenAI stability status.
- Eval maturity: no primary source; build-vs-buy: no primary source.

Candidates for `_candidates.md`
- Frontier safety frameworks / responsible scaling policies (provider commitments tied to evals).
- Incident reporting and disclosure practice (NIST AI 600-1 Incident Disclosure; EU Art. 55 serious incident reporting).
- Third-party / external evaluation and audit (AI safety institutes, auditors, ISO/IEC 42006).
- Eval data governance and contamination policy, privacy of eval logs.
- Human-subjects ethics for annotation and red-teaming.
- Jurisdiction tracker (US states, UK, others).
- Evidence/assurance cases and release-gate decision records.
- Vendor risk / procurement evals for third-party models.

## Landscape items (as-of 2026-11-20)

- EU AI Act application dates after omnibus: prohibitions/AI literacy 2 Feb 2025; GPAI 2 Aug 2025; general 2 Aug 2026; Annex III high-risk 2 Dec 2027; Annex I 2 Aug 2028; Art. 5 new prohibitions 2 Dec 2026 (source: Commission pages above; omnibus in force 27 Jul 2026).
- GPAI Code of Practice signatory list (page updated 2026-10-07); xAI partial signatory.
- Commission GPAI guidelines (18 Jul 2025; updated 2026-04-20); first harmonised AI Act standard published 2026-10-19 (identity unverified).
- Colorado SB 26-189 (signed 2026-05-14; developer documentation from 2027-01-01); replaces SB 24-205.
- ISO/IEC catalogue: 42001:2023, 42005:2025, 42006:2025, 23894:2023, TS 25058:2024, 25059:2023, TS 42119-2:2025, 5259 series, TR 24028 revision in development.
- NIST AI RMF 1.0 (Jan 2023; formal review due by 2028); AI 600-1 (Jul 2024).
- Provider pricing/discounts: Anthropic batch 50% and caching multipliers; OpenAI batch 50%/24 h (pages read 2026-11-20).
- Anthropic system cards list (latest: Fable 5.2 / Mythos 5.2, Nov 2026).
- Tools: Inspect (UK AISI + Meridian Labs), promptfoo (Promptfoo, Inc.), Langfuse, OpenTelemetry GenAI semantic conventions (moved to `semantic-conventions-genai` repo; stability unverified), Hugging Face model-index/eval-results format.

## regulatory-compliance: verification log (2026-11-20)
Checked against official pages by a follow-up pass. The EUR-Lex Official Journal text could not be read (empty response), so article wording remains unverified.
- **Confirmed from the Commission's official pages** ([news](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), [policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [transparency quick facts](https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems)): the omnibus enters into force on 27 July 2026; Annex III high-risk rules apply from 2 December 2027; Annex I product rules from 2 August 2028; a new prohibition (nudification / non-consensual sexual content and CSAM generation) applies from "December 2026".
- **Art. 50:** the general transparency application date stays 2 August 2026. A grace period until December 2026 applies to the Art. 50(2) marking obligation for generative AI systems placed on the market before 2 August 2026.
- **Still unverified:** the regulation number 2026/1744 (the Commission news page links the text as `OJ:L_202601744`, which is consistent but not a statement of the number); the Official Journal publication date (secondary law-firm sources say 24 July 2026); the exact day "2 December 2026" for the new prohibition (the Commission policy page says only "December 2026").
- **Colorado SB 26-189** ([official bill page](https://leg.colorado.gov/bills/sb26-189)): the bill history shows "Governor Signed" on 05/14/2026. The staff summary says it repeals and reenacts the 2024 act, is enforced by the attorney general under the Consumer Protection Act, creates no new private right of action, and requires a 60-day cure notice before actions begun before 1 January 2030. Developer documentation applies from 1 January 2027. The statute's own effective-date and repeal clauses were not read, and the earlier delay and court-ordered pause remain secondary-source claims.

Moved here from the regulatory-compliance node on 2026-11-21 so the node holds durable obligations only.
