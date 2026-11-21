---
id: build-vs-buy
title: "Build vs. buy"
branch: 07-operating-practice
depth: L1
status: not-started
bridge: none
prerequisites: [eval-tooling-landscape]
tags: [cost]
---
# Build vs. buy

Criteria for choosing between in-house harnesses and vendor platforms.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims. Supplemented 2026-11-21: [research/supplements/2026-11-21-build-vs-buy.md](../../research/supplements/2026-11-21-build-vs-buy.md). No standards-body or peer-reviewed build-vs-buy framework for eval tooling was found; the criteria list below is synthesis._

## Learning objectives
You can:
- Explain the main criteria for build vs buy (data sensitivity and residency, exportability, judge transparency, CI fit, total cost of ownership, team capacity, vendor viability) and recognise that they are a synthesis, not a sourced framework.
- Identify which parts of eval infrastructure should stay in-house (gold datasets, rubrics, thresholds).
- Recognise constraints that rule options out, such as data-retention terms and the need to export dated records for regulatory evidence.

**Done bar.** Practiced: a one-page decision record for the capstone with weighted criteria, three options, doc evidence per criterion, an exit plan and a review date. Mastered: written answers to all three mastery questions checked against the tool docs, the MLOps tool review and the Annex IV/Art. 72 pages, and an explanation, without notes, of the build-vs-buy criteria and the lock-in failure mode to someone else.

## Why it matters
- The evidence base is thin. No vendor-neutral standard or eval-specific study was found (searched 2026-11-21). The closest academic source is a systematic review of general MLOps tools, not eval tools ([Micallef et al. 2026, arXiv 2604.16371](https://arxiv.org/html/2604.16371v1)).
- That review (41 studies, 31 tools) finds that "No single tool covers the entire lifecycle" and that multi-tool pipelines are the norm, so interoperability matters as much as features ([arXiv 2604.16371](https://arxiv.org/html/2604.16371v1)).
- The same review says open-source components give control but need integration and maintenance effort that suits larger, mature teams. Managed platforms shift that effort to the vendor at the price of lock-in and subscriptions ([arXiv 2604.16371](https://arxiv.org/html/2604.16371v1)).
- Selection criteria it reports include team skills, community vitality, ease of integration and flexibility. It also notes that little research measures integration effort ([arXiv 2604.16371](https://arxiv.org/html/2604.16371v1)).
- Cloud-vendor guidance (not neutral) recommends managed services and lists building custom ML infrastructure as an anti-pattern. It frames total cost of ownership as including "operational personnel, maintenance, scaling, and upgrades" ([AWS ML Lens MLCOST01-BP02](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost01-bp02.md)).
- Data handling constrains vendor use. For example, Anthropic batch processing is marked not eligible for zero data retention, with 29-day retention (read 2026-11-20) ([Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/batch-processing)).
- Regulation constrains both routes. Annex IV demands dated, signed records and Art. 72 lifetime monitoring evidence, so whichever tool you choose must export these ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4); [Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72)).
- Practitioner: start simple and in-house for viewing data, and be wary of generic vendor metrics for problem-specific quality ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).
- Criteria candidates (own synthesis, not sourced): data sensitivity and residency, exportability, judge transparency, CI fit, total cost of ownership, team capacity, vendor viability.

## Common failure modes
- Building a custom harness for commodity needs such as tracing and storage, or buying one that hides judge prompts and cannot reproduce results (inference).
- Underestimating integration and maintenance effort; the MLOps review flags this as both common and under-measured ([arXiv 2604.16371](https://arxiv.org/html/2604.16371v1)).
- Assuming self-hosting cost is fixed. ThoughtWorks' Radar noted that Langfuse v3 is "more scalable but also more complex to self-host" (practitioner: [ThoughtWorks Radar](https://www.thoughtworks.com/en-us/radar/platforms/langfuse)).
- Tool volatility: ownership, pricing and licences change, so verify at decision time (see [landscape](../../landscape/07-operating-practice.md)).

## Practice exercise (2 h)
Write a one-page decision record for your capstone. Include weighted criteria and three options: a thin in-house harness on an open-source runner, a self-hosted open-source platform, and a commercial platform. Give doc evidence for each criterion, an exit plan and a review date.

## Mastery check
1. Which parts of eval infrastructure should never be outsourced (gold datasets, rubrics, thresholds)?
2. What is your lock-in exit cost in days?
3. How would you test a vendor's built-in metric before trusting it?

## Sources
- [Micallef, Rajenthiram, Gerostathopoulos 2026, A Systematic Review of MLOps Tools, arXiv 2604.16371](https://arxiv.org/html/2604.16371v1) (CAIN '26)
- [AWS Well-Architected ML Lens, MLCOST01-BP02](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost01-bp02.md) (cloud vendor)
- Tool docs as in [eval-tooling-landscape](eval-tooling-landscape.md)
- [Anthropic, batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- [EU AI Act Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4); [EU AI Act Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72)
- practitioner: [Hamel Husain, evals](https://hamel.dev/blog/posts/evals/)
- practitioner: [ThoughtWorks Technology Radar, Langfuse](https://www.thoughtworks.com/en-us/radar/platforms/langfuse)
- GAP: no standards-body or eval-specific primary source for decision criteria; vendor licence files and data processing terms not researched.
