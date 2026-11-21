# Content audit: AI Evaluation Map

**Date:** 2026-11-21  
**Scope:** every file in `map/`, `research/`, `landscape/` and `capstone/`, plus `README.md`, `progress.md` and `tools/`.  
**Commit audited:** `d81ae9e`

## Contents

1. [Method](#1-method)
2. [Audit criteria](#2-audit-criteria)
3. [Scorecard](#3-scorecard)
4. [Findings by criterion](#4-findings-by-criterion)
5. [Prioritised recommendations](#5-prioritised-recommendations)
6. [Appendix: raw measurements](#6-appendix-raw-measurements)

---

## 1. Method

The audit combined three kinds of check.

| Kind | What was done |
|---|---|
| **Automated, all 83 nodes** | Parsed frontmatter and headings for every node. Counted words, links, UNVERIFIED markers, practitioner tags, tags, depth and bridge. Analysed the prerequisite graph (roots, leaves, depth inversions, backward-branch edges). Checked research-section coverage, landscape-entry format and `_candidates.md` content. Searched all node text for a list of 60 field topics. |
| **Link check, all sources** | Requested all 240 unique URLs across `map/`, `research/`, `landscape/`, `capstone/` and the README. Used HEAD, falling back to GET, with a 20-second timeout. |
| **Close reading, a sample** | Read 7 nodes in full, covering every branch: `statistical-inference`, `eval-driven-development`, `llm-as-judge`, `rag-retrieval-evals`, `multimodal-evals`, `ci-eval-gates`, `sandboxing-untrusted-code`, plus `eval-maturity-model` and part of `regulatory-compliance`. Also read the "Gaps and uncertainties" section of all 7 research files, and the capstone. |

**Limits.** This audit does **not** re-check individual factual claims against their sources. It checks how claims are sourced and whether the sources resolve, not whether the paraphrases are correct. The topic-coverage check uses keyword matching, so a topic covered under different wording may read as missing. Each coverage gap in §4.A1 was confirmed by hand before inclusion.

---

## 2. Audit criteria

There are 24 criteria in 7 dimensions. Each one says why it matters for a **personal curriculum and decision guide**, which is how the README describes the repo, and how it was measured.

### A. Scope and coverage

| ID | Criterion | Why it matters | How measured |
|---|---|---|---|
| A1 | **Topic coverage.** The map covers the main concepts a practitioner meets when evaluating LLM, RAG and agent systems in 2026. | Gaps become blind spots in practice. | Keyword search for 60 field topics; checked against the research "Gaps" lists. |
| A2 | **Branch balance.** Branches are similar in size and depth, and match the README's 10–15 nodes per branch. | Imbalance skews study time. | Node counts, word counts and depth by branch. |
| A3 | **Clean boundaries.** Overlapping topics have one owner node, and the others point to it. | Duplication drifts; gaps hide between nodes. | "Shared concept" and "owned by" notes; research boundary flags. |
| A4 | **Candidate pipeline.** Each `_candidates.md` holds real candidate topics, ready to promote. | This is how the map grows without bloat. | Content of `_candidates.md`. |

### B. Curriculum design

| ID | Criterion | Why it matters | How measured |
|---|---|---|---|
| B1 | **Prerequisite correctness.** Prerequisites are necessary, sufficient, acyclic and point forward. | The learning path and graph are built from them. | Graph analysis; status of prerequisite problems flagged in research. |
| B2 | **Depth calibration.** L1, L2 and L3 separate nodes meaningfully, and prerequisites are not deeper than the nodes that need them. | Depth guides how much effort a node gets. | Distribution; inversions. |
| B3 | **Useful metadata.** Bridge and tags are applied consistently enough to filter on. | Filtering and cross-cutting views depend on it. | Counts and distribution. |
| B4 | **Learning objectives.** Each node says what you will be able to do when you finish it. | Without them, mastery is undefined. | Search for objective statements. |
| B5 | **Pacing.** There are time estimates and an overall study sequence. | Needed to plan study time. | Time estimates in headings; any schedule. |

### C. Node content quality

| ID | Criterion | Why it matters | How measured |
|---|---|---|---|
| C1 | **Template completeness.** All five required sections are present (Why it matters, Common failure modes, Practice exercise, Mastery check, Sources). | Set as a README rule. | Heading parse. |
| C2 | **Format consistency.** Nodes share one style across branches. | Readability and tooling both need it. | Heading variants, list style, citation style. |
| C3 | **Substance.** Enough depth to act on, proportionate to depth level. | Thin nodes give too little to study. | Word counts versus depth; close reading. |
| C4 | **Actionable exercises.** Data, steps and expected output are specified. | Practice is how the map turns into skill. | Close reading. |
| C5 | **Assessable mastery checks.** Questions test application, and you can tell whether you passed. | Status changes need evidence. | Format; presence of answer keys or rubrics. |

### D. Evidence and sourcing

| ID | Criterion | Why it matters | How measured |
|---|---|---|---|
| D1 | **Claims cited.** Every factual claim links to a source. | Set as a README rule. | Uncited "Why it matters" sections; citation density. |
| D2 | **Source quality mix.** Primary sources first, plus the curated practitioner list the README promises. | Set as a README rule. | Domain mix; practitioner tags; whether the list exists. |
| D3 | **Verification status.** Unverified claims are marked, and they are a minority. | Shows how far each node can be trusted. | UNVERIFIED counts, excluding boilerplate. |
| D4 | **Link health.** Source URLs resolve to the intended page. | Dead links make sources unusable. | Link check. |
| D5 | **Citation usability.** Sources are clickable, both on GitHub and on the site. | Friction lowers how often sources get read. | Bare URLs; name-only Sources sections. |

### E. Currency and volatility

| ID | Criterion | Why it matters | How measured |
|---|---|---|---|
| E1 | **Durable and volatile separated.** Model names, tool flags and regulatory dates live in `landscape/`, not in nodes. | Set as a README rule; nodes should not rot. | Search for model names, tool details and dated status in nodes. |
| E2 | **Landscape format compliance.** Entries follow `<item> (type: …) as-of: … \| <url>`. | Staleness tooling and readers depend on it. | Format parse. |
| E3 | **Right content in landscape.** Entries are actually volatile, not durable papers. | Otherwise the staleness signal is noise. | Close reading. |

### F. Applied practice

| ID | Criterion | Why it matters | How measured |
|---|---|---|---|
| F1 | **Capstone completeness.** The capstone has defined scope, deliverables and acceptance criteria. | It is the integration test for the curriculum. | Close reading. |
| F2 | **Capstone coverage.** The capstone exercises every branch. | Untouched branches stay theoretical. | Step-to-branch mapping. |

### G. Repo hygiene and tooling

| ID | Criterion | Why it matters | How measured |
|---|---|---|---|
| G1 | **README accurate.** Describes the repo as it is now. | It is the entry point. | Compared with the content. |
| G2 | **Validation coverage.** Tooling enforces the README rules. | Rules nobody checks drift. | Read `build_views.py`. |
| G3 | **Generated views current.** `00-overview.md` and `progress.md` match the nodes. | Stale views mislead. | Re-ran the generator and checked for a diff. |

---

## 3. Scorecard

**Scale:** **Strong** = meets the criterion with at most minor nits. **Adequate** = works, with clear improvements available. **Weak** = falls materially short. **Missing** = not addressed.

| ID | Criterion | Rating | Headline evidence |
|---|---|---|---|
| A1 | Topic coverage | **Adequate** | Core lifecycle well covered. About 10 notable topics absent, e.g. multilingual, reasoning models, user simulation, computer-use agents. |
| A2 | Branch balance | **Strong** | 11–14 nodes per branch, all within the 10–15 rule. |
| A3 | Clean boundaries | **Adequate** | Ownership notes exist (pass@k, statistics), but research flagged 8 overlaps and most have no pointer. |
| A4 | Candidate pipeline | **Weak** | 6 of 7 `_candidates.md` hold only a pointer; the real candidates are stranded in research files. |
| B1 | Prerequisite correctness | **Adequate** | Acyclic and validated. 3 problems the research flagged are still open, and there is 1 backward-branch edge. |
| B2 | Depth calibration | **Weak** | 80% of nodes are L2; all of 06-production is L2. 5 depth inversions. |
| B3 | Useful metadata | **Weak** | 60 of 83 nodes untagged; 4 tag values; `cost` on only 3 nodes. |
| B4 | Learning objectives | **Missing** | 0 nodes state objectives. |
| B5 | Pacing | **Weak** | Time estimates on 12 of 83 nodes; no overall schedule. |
| C1 | Template completeness | **Strong** | All 83 nodes have all five sections. |
| C2 | Format consistency | **Weak** | Three distinct house styles, one per research batch (see §4.C2). |
| C3 | Substance | **Adequate** | Median 335 words, good density. Several L2/L3 nodes are thin, around 200 words. |
| C4 | Actionable exercises | **Adequate** | Concrete and well scoped, but rarely state expected results or a time budget. |
| C5 | Assessable mastery checks | **Weak** | Good questions, but answer keys in only 2 nodes, so you can't tell whether you passed. |
| D1 | Claims cited | **Strong** | 82 of 83 "Why it matters" sections carry inline links. Provenance banner on every node. |
| D2 | Source quality mix | **Adequate** | Primary-heavy (316 arXiv links, 121 distinct papers). The README's practitioner list does not exist. |
| D3 | Verification status | **Adequate** | Honest marking, but 87 UNVERIFIED claim lines in 60 nodes (72%). Most papers read at abstract level only. |
| D4 | Link health | **Strong** | 229 of 240 URLs OK. 5 real defects (see §4.D4). |
| D5 | Citation usability | **Weak** | 35 nodes have bare URLs (not clickable on the site). All 12 system-specific nodes list Sources by name only. |
| E1 | Durable/volatile separation | **Weak** | Model names (GPT-4 ×14), tool flags and a dated regulatory timeline are inside nodes. |
| E2 | Landscape format compliance | **Weak** | 0 of 55 entries have `(type: …)`; 28 of 55 have no URL. |
| E3 | Right content in landscape | **Adequate** | Mostly volatile, but several entries are durable papers. |
| F1 | Capstone completeness | **Weak** | 8 one-line steps marked "to be detailed"; 3 open decisions; no deliverables or acceptance criteria. |
| F2 | Capstone coverage | **Adequate** | Touches 02–06; no step for 01 or 07. |
| G1 | README accurate | **Adequate** | Still says "Nodes start as stubs"; promises a practitioner list that doesn't exist. |
| G2 | Validation coverage | **Weak** | Checks status, prerequisites and cycles only. Sections, enums, tags, landscape format and links are unchecked. |
| G3 | Generated views current | **Strong** | Re-running the generator produced no diff. |

**Overall.** The repo is strong where a curriculum is usually weakest: honest sourcing, complete templates and a validated prerequisite graph. It is weakest where learning turns into evidence of mastery: no objectives, no answer keys, an unfinished capstone and depth labels that don't discriminate. It also carries technical debt from being written in batches: three house styles, a candidate pipeline left in research files, and a landscape that doesn't follow its own format.

---

## 4. Findings by criterion

### A. Scope and coverage

**A1 Topic coverage (Adequate).** The design → measure → gate → monitor → feed-back lifecycle is well covered, and core topics are well represented: LLM-as-judge, RAG, agents, CI gates, red teaming, drift and regulation. Each gap below was confirmed by hand and has zero or near-zero mentions across all 83 nodes.

| Gap | Mentions | Why it matters in 2026 | Suggested home |
|---|---|---|---|
| Multilingual and localisation evals | 0 | Quality and safety regress per language; English-only evals hide this. | New node in 04 or 05 |
| Reasoning models and test-time compute | 0 | Scores depend on the thinking budget, cost and latency trade off, and judging reasoning traces is its own problem. | New node in 04, or a section in `llm-basics-for-evaluators` |
| User simulation for multi-turn and agent evals | 0 | It is the standard way to scale conversational and agent evals (as in τ-bench-style setups). | New node in 04 |
| Computer-use, browser and GUI agents | ~2 | A distinct environment, grading and safety problem. | `_candidates.md` in 04 (flagged in research) |
| Indirect prompt injection through tool results and retrieved content | 0 as a named concept | The main security risk for agents and RAG. | Section in `prompt-injection-security-testing` |
| Privacy and PII in eval data and logs | 3 | Golden sets and traces often contain personal data, which carries GDPR and retention duties. | New node in 06 (flagged in research) |
| Eval dataset versioning and maintenance | 0 | Datasets drift, saturate and leak; versioning is what makes results reproducible. | New node in 02 (flagged in research) |
| Item response theory and benchmark item quality | 0 | Item difficulty and discrimination support adaptive and cheaper evals. | `_candidates.md` in 03 |
| Reward and preference model evaluation | 0 | A judge-adjacent skill (research 03 flagged it). | `_candidates.md` in 03 |
| Sycophancy, and hallucination as a named concept | 1 and 2 nodes | Faithfulness is covered in the RAG nodes, but open-domain factuality and sycophancy have no owner. | Section in `quality-dimensions-taxonomy` or `safety-and-harm-evals` |
| Sequential testing and peeking in online experiments | 0 | A common A/B mistake when teams monitor continuously. | Section in `online-experiments` |

**A2 Branch balance (Strong).** Branch sizes are 11, 12, 12, 12, 14, 11 and 11, all inside the 10–15 rule. Word counts are comparable across branches. The only outlier is `regulatory-compliance` at 1,141 words, more than three times the median (see E1).

**A3 Clean boundaries (Adequate).** Good ownership practice exists: pass@k is "owned" by `nondeterminism-and-variance`, and statistics is owned by `statistical-inference` and `confidence-intervals-for-evals`. But the research files flagged these overlaps, and most of them still have no explicit owner or pointer:
- `benchmark-limitations` ↔ `contamination-and-leakage` ↔ `data-splits-and-leakage`
- faithfulness, duplicated in `rag-generation-evals` and `summarization-and-extraction-evals`
- `safety-and-harm-evals` ↔ `red-teaming` ↔ `runtime-guardrails` ↔ `responsible-ai-ethics`
- `robustness-testing` ↔ `metamorphic-and-property-testing`
- `online-metrics-and-user-feedback` ↔ `online-experiments`
- `drift-detection` ↔ `model-upgrade-and-migration`
- `llm-as-judge` ↔ `production-evals-with-judges`

Also, 12 nodes link to other nodes in their prose without declaring them as prerequisites. These are natural "related" links, but there is no field to hold them.

**A4 Candidate pipeline (Weak).** Only `01-foundations/_candidates.md` has a real list (7 items). The other six contain a single line pointing at the research file's "Gaps and uncertainties" section. Those sections hold about 25 concrete candidate topics, such as text-to-SQL evals, voice agents, memory and personalisation, reranker evals, LLM-specific SLOs and judge prompt patterns. As things stand, they don't show on the site's branch pages and are easy to lose.

### B. Curriculum design

**B1 Prerequisite correctness (Adequate).** The graph is acyclic and every prerequisite resolves; `build_views.py` enforces both. There are 5 roots, 37 leaves (45%) and no isolated nodes. Some problems the research flagged were fixed, for example `agent-trajectory-evals` now requires `llm-as-judge`. These are still open:
- `drift-detection` requires `classical-ml-validation`. Research notes say a two-sample-testing foundation (in `statistical-inference`) is the real dependency.
- `eval-maturity-model` (L3) requires only `team-roles-and-process`. It also depends on documentation, tooling and reporting.
- `risk-and-governance-frameworks` requires `safety-and-harm-evals`, but its content is organisational (NIST, ISO). Research suggests `eval-reporting-and-communication` or no prerequisite.
- **Backward-branch edge:** `code-generation-evals` (04) requires `sandboxing-untrusted-code` (05). This is the only edge in the graph that runs against branch order.

**B2 Depth calibration (Weak).** The distribution is L1: 4, L2: 66 (80%), L3: 13. When four in five nodes share a depth, depth tells you little. All 11 nodes in 06-production are L2, including `online-experiments` and `drift-detection`, which are arguably L3 if you need to run them. There are 5 depth inversions, where a prerequisite is deeper than the node that needs it:

| Prerequisite (depth) | Dependent node (depth) |
|---|---|
| `metric-selection` | `multimodal-evals` (L1) |
| `safety-and-harm-evals` (L3) | `runtime-guardrails` (L2) |
| `eval-harness-design` | `eval-tooling-landscape` (L1) |
| `fairness-and-bias-testing` (L3) | `responsible-ai-ethics` (L2) |
| `safety-and-harm-evals` (L3) | `risk-and-governance-frameworks` (L2) |

An inversion is not always wrong; an awareness node can follow an expert one. But each one should be a deliberate choice.

**B3 Useful metadata (Weak).**
- **Tags:** 60 of 83 nodes are untagged. Only 4 values are in use: `nondeterminism` (10), `safety` (8), `fairness` (3), `cost` (3). `cost` is missing from `eval-cost-management`'s neighbours and from `build-vs-buy`, among others.
- **Bridge:** in 07-operating-practice all 11 nodes are `none`, and in 04 nine of 12 are. If bridge marks this learner's gap, it may be accurate. It may also mean bridge was never assessed for those branches.

**B4 Learning objectives (Missing).** No node says what you will be able to do when finished. The mastery check partly stands in for this, but there is no stated bar for moving a node's status to `practiced` or `mastered`.

**B5 Pacing (Weak).** Only the 11 foundations nodes and `sandboxing-untrusted-code` have time estimates, given in the exercise heading, e.g. "(2-3 h)". There is no total effort estimate and no suggested weekly plan. The learning path orders nodes but doesn't give them a time budget.

### C. Node content quality

**C1 Template completeness (Strong).** All 83 nodes contain all five required sections. 12 of them use a variant heading with a time estimate (see C2).

**C2 Format consistency (Weak).** There are three house styles, one per research batch:

| Style | Where | Traits |
|---|---|---|
| **Foundations** | 01 (11 nodes) + `sandboxing-untrusted-code` | Bulleted sections, numbered mastery checks, time estimates, link lists under Sources. |
| **Eval-design** | 02 (12 nodes) | Prose paragraphs; a `_Source key (reused)_` line with bracket keys like `[OAI-BP]`; inline "(1) … (2)" mastery checks; Sources given as keys. |
| **Compact** | 04 (12 nodes) and partly 03, 05, 06, 07 | Dense prose with `[V]` markers; inline mastery checks in 04; Sources listed by name only ("MMMU; MathVista"). |

In total, 24 nodes (all of 02 and 04) use inline mastery checks, and 3 nodes have extra "Verification log" sections. The mixed styles make the site look uneven and make sections hard to parse automatically.

**C3 Substance (Adequate).** The median node is 335 words, which is dense and specific. The thinnest nodes are `multimodal-evals` (202), `multi-agent-evals` (211), `long-context-evals` (226), `conversational-evals` (236), `rubric-design` (244) and `annotation-guidelines` (251). `rubric-design` matters most: it is a prerequisite of `llm-as-judge`. `sandboxing-untrusted-code` openly says it is "thinly sourced", with only one paper read.

**C4 Actionable exercises (Adequate).** The exercises are a real strength: concrete sizes (50 outputs, 500 questions), named tools and a comparison to make. Weaknesses:
- Most don't say what result to expect or what a good outcome looks like.
- Most have no time budget.
- Data sources are sometimes left open ("a small task"). Pointing them at the capstone dataset would give continuity.

**C5 Assessable mastery checks (Weak).** The questions are good and application-focused, for example "Show what changes when the judge shares a model family with the generator". But only 2 nodes have anything like an answer key or rubric, so you can't tell whether you answered well enough to change a node's status.

### D. Evidence and sourcing

**D1 Claims cited (Strong).** 82 of 83 "Why it matters" sections cite inline. The exception is `eval-driven-development`, which cites with bracket keys, not links. Every node has a provenance banner saying how deeply its sources were read. Inferences are labelled as such ("author judgement", "inference", "design inference"). This is unusually rigorous.

**D2 Source quality mix (Adequate).**
- **Primary-heavy:** arXiv provides 316 links across 121 distinct papers. Next come platform.claude.com (46), NIST (23), OpenAI docs (18) and ACL Anthology (14).
- **Concentration:** HELM is cited in 16 nodes and Shankar et al. in 13. That's fine for foundational work, but it shows a reliance on a few surveys.
- **Missing practitioner list:** the README promises "a short list of trusted practitioner sources", and no such list exists. Practitioner sources are tagged in 18 nodes, but there is no curated list to check them against.

**D3 Verification status (Adequate).** Excluding the boilerplate banner, there are 87 UNVERIFIED claim lines across 60 nodes (72%), and 103 more in the research files. The heaviest are `regulatory-compliance` and `standards` (6 each) and `inter-rater-agreement` (5).

The research files list specific fetches still to do: Cohen 1960, Fleiss 1971, Krippendorff, Landis & Koch, Bradley-Terry, the Efron bootstrap, EUR-Lex article text and the CheckList definitions. Several canonical statistics sources are among them.

The banner says "most paper claims were read at abstract level". For nodes you'll rely on, such as `inter-rater-agreement`, `confidence-intervals-for-evals` and `llm-as-judge`, full-text reading is the outstanding work.

**D4 Link health (Strong).** 229 of 240 unique URLs returned 200.

Real defects:

| URL | Problem | Fix |
|---|---|---|
| `https://arxiv.org/abs/2211.09110_` | Malformed: the closing `_` of the italic source-key line in 02 nodes becomes part of the URL. | Put the URL in `<…>` or a Markdown link. |
| `docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests` | 404 | Find the current Evidently docs page. |
| `web.engr.oregonstate.edu/~tgd/publications/dietterich-approximate-statistical-tests-nc1998.pdf` | Unreachable | Use the DOI (10.1162/089976698300017197). |
| `anthropic.com/engineering/demystifying-evals-for-ai-agents` and `…/multi-agent-research-system` | Redirect to `/research/…` | Update to the new URLs. |
| `github.com/gkamradt/LLMTest_NeedleInAHaystack` | Repo renamed | Update to `gkamradt/needle-in-a-haystack`. |

Not confirmed broken, because the sites block automated requests: iso.org (2), dl.acm.org, genai.owasp.org, discovery-pp.ucl.ac.uk and americanbar.org (403); docs.vllm.ai (429); rubydoc.info (202). Check these by hand.

**D5 Citation usability (Weak).**
- 35 nodes contain bare URLs, such as Sources lists in the form `- Miller: https://…`. GitHub auto-links these, but the site generator doesn't, so on the site they are plain text.
- All 12 nodes in 04-system-specific-evals list Sources by **name only** ("BEIR; Järvelin & Kekäläinen 2002"). The URLs appear only inline in the body.
- The 02 nodes rely on bracket keys defined in an italic line.

### E. Currency and volatility

**E1 Durable/volatile separation (Weak).** The README rule is "Durable concepts go in nodes. Volatile items go in `landscape/`." It is broken in three ways:
- **Model names and release-time scores in nodes:** GPT-4 ×14, GPT-4o, GPT-3.5, "Claude 4.7 and later", Llama2, "Claude 2 solved…". These are mostly cited as historical results, which is acceptable if labelled as such, as `multimodal-evals` does with "[V]". They aren't always labelled.
- **Tool configuration in nodes:** `ci-eval-gates` lists promptfoo flags and environment variables. It does label them "tool docs, as-of", but they belong in landscape.
- **Regulatory status in a node:** `regulatory-compliance` contains a dated EU AI Act timeline, the omnibus amendments and Colorado's statute status, labelled "status as-of 2026-11-20". This is exactly the kind of fact that goes stale, and it is the main reason the node is three times the median length. Keep the durable obligations (e.g. Art. 72 post-market monitoring) in the node and move dates and status to `landscape/07-operating-practice.md`.

**E2 Landscape format compliance (Weak).** The specified format is `<item> (type: tool|benchmark|model|standard) as-of: YYYY-MM-DD | <source URL>`.
- **0 of 55** entries include `(type: …)`.
- **28 of 55** have no URL: all 9 in 04, all 9 in 07, 4 in 05, 3 in 03, 2 in 02 and 1 in 06.
- `landscape/01-foundations.md` is empty, though foundations nodes mention volatile things such as API sampling parameters and `system_fingerprint`.
- All entries share one as-of date (2026-11-20) and were "migrated, not individually re-verified".

**E3 Right content in landscape (Adequate).** Several entries are durable papers, not volatile items, for example "CheckList tool. arXiv 2005.04118" and "Ragas framework (arXiv 2309.15217)". A paper doesn't go stale; the tool's current state does. Entries should point at the volatile thing (the repo, the leaderboard, the docs page), not the paper.

### F. Applied practice

**F1 Capstone completeness (Weak).** The capstone is 21 lines: 8 steps, each one line with linked nodes, under the heading "Steps (to be detailed)". Three decisions are still open: document set, model or provider, and hosting. Nothing is defined for:
- deliverables per step (dataset file, eval report, CI workflow, dashboard)
- acceptance criteria (for example, judge κ ≥ 0.6 against your labels, CI gate fires on a seeded regression)
- how capstone evidence moves node status to `practiced`.

**F2 Capstone coverage (Adequate).** The steps exercise branches 02, 03, 04, 05 and 06. There is no step for 07: reporting, a model or system card, or a cost budget. Foundations statistics (CIs, paired comparison) is only implied in step 4. Adding a final "Write the eval report and system card" step would close the loop.

### G. Repo hygiene and tooling

**G1 README accurate (Adequate).**
- It still says "Nodes start as stubs", though all 83 nodes are filled.
- It promises a practitioner-source list that doesn't exist.
- Its landscape format is not what the landscape files use.
- It doesn't mention `CONTEXT.md` or the site's Pages workflow beyond the build command.

**G2 Validation coverage (Weak).** `build_views.py` validates status values, that prerequisites resolve, and that there are no cycles. These README rules are not enforced:
- the five required sections
- `depth` and `bridge` enum values
- a controlled tag vocabulary
- `id` matching the filename
- landscape line format, including type and URL
- links (internal anchors and external URLs)

No CI job runs validation on pull requests. The Pages workflow builds only on push to `main`.

**G3 Generated views current (Strong).** Re-running `build_views.py` produced no change to `00-overview.md` or `progress.md`.

---

## 5. Prioritised recommendations

Effort: **S** < 1 h, **M** 1–4 h, **L** > 4 h. Priority reflects value to *learning with* the map, not just tidiness.

### P1: Do first (high value, mostly low effort)

| # | Recommendation | Criteria | Effort |
|---|---|---|---|
| 1 | **Add learning objectives and a "done" bar to every node.** Two or three "You can…" statements, and a line saying what evidence moves status to `practiced` and to `mastered`, e.g. "exercise completed and mastery answers checked against the sources". | B4, C5 | M (template) + L (fill) |
| 2 | **Finish the capstone spec.** Close the 3 open decisions. Give each step a deliverable and an acceptance criterion. Add a step 9 for the eval report, system card and cost (branch 07). | F1, F2 | M |
| 3 | **Move the real candidates out of research files into `_candidates.md`.** About 25 topics, plus the coverage gaps in §4.A1. | A4, A1 | S |
| 4 | **Fix the 5 real link defects** listed in §4.D4. | D4 | S |
| 5 | **Make citations clickable.** Autolink bare URLs in `build_site.py` (one regex). Turn the 04 name-only Sources into linked lists, and replace the 02 bracket keys with links. | D5, D1 | S (generator) + M (content) |
| 6 | **Fix the 3 open prerequisite problems and the backward edge.** Re-point `drift-detection`, enrich `eval-maturity-model`, re-point `risk-and-governance-frameworks`, and decide whether `sandboxing-untrusted-code` moves to 03 or 04. | B1 | S |

### P2: Next (structural quality)

| # | Recommendation | Criteria | Effort |
|---|---|---|---|
| 7 | **Normalise all nodes to one house style**, probably the foundations style: bullets, numbered mastery checks, `(N h)` in the exercise heading, a linked Sources list. One mechanical pass per branch. | C2, B5 | L |
| 8 | **Recalibrate depth.** Define L1, L2 and L3 by observable behaviour (explain / apply / design-and-critique), re-rate all nodes, and review the 5 inversions. Aim for roughly 20 / 55 / 25 %. | B2 | M |
| 9 | **Define a tag vocabulary and apply it.** For example: `nondeterminism`, `safety`, `fairness`, `cost`, `security`, `privacy`, `agents`, `rag`, `statistics`, `human-labels`. Tag every node. | B3 | M |
| 10 | **Clean up the landscape.** Add `(type: …)` and a URL to every entry. Move volatile content out of `regulatory-compliance`, `ci-eval-gates` and the model-name mentions. Replace paper entries with the volatile artifact (repo, leaderboard, docs). Seed `01-foundations` with entries such as API sampling parameters. | E1, E2, E3 | M |
| 11 | **Resolve the boundary overlaps** in §4.A3. Pick an owner for each and add a "Shared concept: owned by …" line to the others. Consider a `related:` frontmatter field for the 12 nodes that link outside their prerequisites. | A3 | M |
| 12 | **Extend validation.** Check required sections, enums, tag vocabulary, id = filename and landscape format in `build_views.py`. Add a weekly link-check job. Run validation in CI on pull requests. | G2 | M |

### P3: Later (depth and breadth)

| # | Recommendation | Criteria | Effort |
|---|---|---|---|
| 13 | **Write new nodes for the highest-value gaps:** reasoning models and test-time compute, user simulation, multilingual evals, privacy and PII in eval data, eval dataset versioning. Add indirect prompt injection and sequential testing as sections in existing nodes. | A1 | L |
| 14 | **Do the full-text verification pass** on the nodes you rely on most: `inter-rater-agreement`, `confidence-intervals-for-evals`, `llm-as-judge`, `judge-bias-and-calibration`, `statistical-inference`. Fetch the canonical sources in §4.D3 and reduce the UNVERIFIED count. | D3 | L |
| 15 | **Thicken the thin nodes,** starting with `rubric-design` and `annotation-guidelines` (on the critical path to `llm-as-judge`), then `sandboxing-untrusted-code`. | C3 | M |
| 16 | **Create the practitioner-source list** the README promises, e.g. `docs/practitioner-sources.md` with the inclusion bar, and check the 18 practitioner-tagged nodes against it. | D2 | S |
| 17 | **Add a study plan:** a week-by-week schedule derived from learning-path stages and time estimates, shown on the site. | B5 | S once #7 is done |
| 18 | **Update the README** to match current reality: stubs → filled, the landscape format, `CONTEXT.md`, the site and the practitioner list. | G1 | S |

---

## 6. Appendix: raw measurements

**Nodes:** 83. Per branch: 01: 11, 02: 12, 03: 12, 04: 12, 05: 14, 06: 11, 07: 11.

**Word counts:** median 335. Min: `multimodal-evals` 202. Max: `regulatory-compliance` 1,141, `risk-and-governance-frameworks` 669, `llm-basics-for-evaluators` 567.

**Depth:** L1 4, L2 66, L3 13. By branch:

| Branch | L1 | L2 | L3 |
|---|---|---|---|
| 01 | 2 | 9 | 0 |
| 02 | 0 | 11 | 1 |
| 03 | 0 | 10 | 2 |
| 04 | 1 | 7 | 4 |
| 05 | 0 | 9 | 5 |
| 06 | 0 | 11 | 0 |
| 07 | 1 | 9 | 1 |

**Bridge:** none 37, testing 26, stats 20. In 07, all 11 are `none`; in 05, 12 of 14 are `testing`.

**Tags:** 23 of 83 nodes tagged. `nondeterminism` 10, `safety` 8, `fairness` 3, `cost` 3.

**Prerequisite graph:**
- Prerequisites per node: 0 → 5 nodes, 1 → 45, 2 → 29, 3 → 4.
- 5 roots, 37 leaves, 0 isolated nodes, 0 cycles.
- 1 backward-branch edge, 5 depth inversions.

**Template and format:**
- All 5 sections in 83 of 83 nodes.
- Mastery check: numbered in 59 nodes (55 with 3 questions, 4 with 4); inline "(1)…" in 24 (all of 02 and 04).
- Time estimates: 12 nodes.
- Learning objectives: 0 nodes. Answer keys: 2 nodes.

**Sourcing:**
- Distinct arXiv papers: 121. Top domains: arxiv.org 316, platform.claude.com 46, nvlpubs.nist.gov 23, developers.openai.com 18, aclanthology.org 14.
- Most-cited: HELM (2211.09110) in 16 nodes; Shankar et al. (2404.12272) in 13; MT-Bench (2306.05685) in 10; Miller (2411.00640) in 9.
- Practitioner-tagged: 18 nodes.
- UNVERIFIED (excluding the banner): 87 lines in 60 nodes. Research files: 103.
- Nodes with bare URLs: 35. Sources sections with no URL: 12 (all of 04).

**Links:** 240 unique. 229 OK, 11 non-200 (5 real defects, 6 bot-blocked or rate-limited). 7 redirects.

**Landscape:** 55 entries. 0 with `(type:)`. 28 without a URL. `01-foundations` is empty.

**Candidates:** 7 real items (01 only). The other 6 files are pointer-only.

---

## 7. Follow-up status (updated 2026-11-21)

| # | Recommendation | Status |
|---|---|---|
| 1 | Learning objectives and done bar | **Done.** Every node has a `## Learning objectives` section matched to its depth and a **Done bar** for practiced and mastered. The validator now requires the section. |
| 2 | Capstone spec | **Done.** 13 steps, each with a deliverable, an acceptance criterion and the nodes it exercises. Decisions: this repo as the document set, Claude Sonnet 5.5 as generator and Opus 5.5 as judge, local runs with a GitHub Actions gate. Every node is either exercised or listed as theory-only. |
| 3 | Candidates out of research files | **Done.** |
| 4 | Link defects | **Done.** The Evidently page is still dead and marked as such. |
| 5 | Clickable citations | **Done.** The site generator now also autolinks plain URLs. |
| 6 | Prerequisite fixes and backward edge | **Done.** `drift-detection` now requires `statistical-inference`. `eval-maturity-model` also requires documentation and tooling. `risk-and-governance-frameworks` now requires `responsible-ai-ethics`. `sandboxing-untrusted-code` moved to 03, which removes the backward edge. |
| 7 | One house style | **Done.** |
| 8 | Recalibrate depth | **Done.** Depth is redefined as the learner's target depth (see `CONTEXT.md`); the mix is now L1 16, L2 49, L3 18. Under this definition a prerequisite may have a higher depth than its dependent node, so the B2 "inversions" are no longer defects. |
| 9 | Tag vocabulary | **Done.** Tags are now 0-3 per node, so `multimodal-evals` stays untagged by design. |
| 10 | Landscape clean-up and volatile content out of nodes | **Done** for the landscape format and `regulatory-compliance`: dated status moved to the landscape file, and the verification log to the research notes. Model names cited as historical results stay in nodes. |
| 11 | Overlap owners | **Done.** Owns and Shared concept lines cover the 7 overlap clusters. |
| 12 | Extended validation and CI | **Done.** |
| 13 | New nodes for coverage gaps | **Done.** Five new nodes: `reasoning-model-evals`, `user-simulation-evals`, `multilingual-evals`, `privacy-and-pii-in-eval-data`, `eval-dataset-versioning`. Two new sections: indirect injection in `prompt-injection-security-testing` and sequential testing in `online-experiments`. The map now has 88 nodes, all mapped in the capstone. |
| 14 | Full-text verification pass | **Done** for the five highest-traffic nodes: `statistical-inference`, `confidence-intervals-for-evals`, `llm-as-judge`, `judge-bias-and-calibration`, `inter-rater-agreement`. Notes are in `research/supplements/`. Paywalled classics (Cohen 1960/1968, Fleiss 1971, Landis & Koch 1977) are cited through secondary full-text sources and labelled as such. |
| 15 | Thicken thin nodes | **Done** for all seven: `sandboxing-untrusted-code`, `inter-rater-agreement`, `reference-based-metrics`, `multi-agent-evals`, `rag-end-to-end-evals`, `build-vs-buy`, `standards`. |
| 16 | Practitioner list | **Done.** See `docs/practitioner-sources.md`. |
| 17 | Study plan | **Done.** `study-plan.md` is generated by `tools/build_views.py`; set the pace with `--hours-per-week`. |
| 18 | README | **Done.** |
