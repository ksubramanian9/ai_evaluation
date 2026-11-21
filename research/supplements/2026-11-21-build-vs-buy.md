# Research supplement: build-vs-buy

As of: 2026-11-21. Web access: working (WebFetch, WebSearch).

Headline: no vendor-neutral standards-body guidance or peer-reviewed decision framework for build vs buy of ML or eval tooling was found. Searches covered general web, arXiv and AWS/ThoughtWorks. What exists: one systematic literature review (academic, MLOps tools in general, not eval tooling specifically), one interview study, cloud-vendor guidance that favours managed services, and practitioner/vendor blog posts (Comet, Neptune and others are vendors of the tools they discuss, so they are not neutral).

## Micallef, Rajenthiram, Gerostathopoulos, "A Systematic Review of MLOps Tools: Tool Adoption, Lifecycle Coverage, and Critical Insights" (CAIN '26; arXiv 2604.16371)
Read: full HTML summary-level read of main findings. URL: https://arxiv.org/html/2604.16371v1
- Method: SLR of 41 primary studies covering 31 MLOps tools. The search was limited to the first 10 Google Scholar pages, plus snowballing.
- "No single tool covers the entire lifecycle"; multi-tool pipelines are the norm, so interoperability matters as much as individual tool strength.
- Open-source tools give control but need extra engineering, e.g. for enterprise-grade security. Managed cloud platforms shift that work to the provider but bring lock-in and subscription cost.
- Building from open-source components demands significant integration and maintenance effort and suits larger, more mature teams.
- Selection criteria noted: team skills (e.g. Kubernetes for Kubeflow), community vitality, ease of integration, flexibility across storage and frameworks.
- Gap noted by the authors: little literature measures integration effort, and papers underreport tool limitations.

## Shankar et al., "Operationalizing Machine Learning: An Interview Study" (arXiv 2209.09125, 2022)
Read: abstract only. URL: https://arxiv.org/abs/2209.09125
- Semi-structured interviews with 18 ML engineers. Velocity, Validation and Versioning are the three variables governing production ML success; the paper discusses implications for tool design.
- The claim that engineers "glue" open-source tools and build "homegrown" infrastructure came from a search summary of the full text. NOT verified by me, so it is not used in the node.

## AWS Well-Architected Machine Learning Lens, MLCOST01-BP02 (cloud-vendor guidance)
Read: full page. URL: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost01-bp02.md
- "Use managed services to reduce total cost of ownership (TCO)". Lists as anti-patterns "Building and maintaining custom ML infrastructure" and "Developing proprietary AI services when managed services would suffice". Risk if not established: High.
- Says TCO should include "infrastructure, operational personnel, maintenance, scaling, and upgrades".
- Caveat: this is a cloud vendor recommending its own managed services. Its TCO advice is generic, and it gives no criteria for when building is right.

## ThoughtWorks (practitioner)
- "Guide to Evaluating MLOps Platforms" landing page. Read: page only, PDF not read. URL: https://thoughtworks.com/insights/whitepapers/guide-to-evaluating-mlops-platforms. The page poses build-vs-buy and selection-criteria questions but gives no criteria on the page. Undated (PDF filename suggests 2021).
- Technology Radar, Langfuse blip. Read: full page. URL: https://www.thoughtworks.com/en-us/radar/platforms/langfuse. Apr 2024 Assess ("self-host the open-source version or use it as a paid cloud service"); Oct 2024 Trial; Apr 2026 Trial (the body text says "remains in Assess", an inconsistency on the page), noting the v3 architecture is "more scalable but also more complex to self-host". Useful as evidence that self-hosting cost changes over a tool's life.

## Carried from the node (not re-read this session)
- Anthropic batch processing: data retention / ZDR constraints. Read 2026-11-20 by the earlier pass.
- EU AI Act Annex IV and Art. 72. Read 2026-11-20 by the earlier pass.
- hamel.dev evals post (practitioner). Read 2026-11-20 by the earlier pass.

## Not used
- Sculley et al. 2015, "Hidden Technical Debt in Machine Learning Systems" (NeurIPS). Only the abstract was readable (PDF text extraction failed), so the glue-code argument is NOT verified and not cited.
- Vendor blogs from the search (Comet, Neptune, Paperspace, V7, builtin.com): not fetched. They are vendor-authored and not neutral.

## Gaps
- No eval-specific (as opposed to MLOps-general) build-vs-buy study was found.
- No quantitative evidence on in-house harness maintenance cost was found.
- The ThoughtWorks guide PDF was not read.
