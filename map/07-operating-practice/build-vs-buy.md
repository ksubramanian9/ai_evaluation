---
id: build-vs-buy
title: "Build vs. buy"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [eval-tooling-landscape]
tags: [cost]
---
# Build vs. buy

Criteria for choosing between in-house harnesses and vendor platforms.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- No primary-source decision framework was found; this node rests on documented tool properties and practitioner advice. Facts: open-source, self-hostable options exist (Inspect, promptfoo, Langfuse per their docs above; licenses not stated on the pages read: UNVERIFIED, check repos). Batch API and `ZDR not eligible` data retention (29 days for Anthropic batch) are constraints for vendor/data-handling decisions ([Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/batch-processing)).
- Regulatory constraints on external tooling: Annex IV demands dated, signed records and Art. 72 lifetime monitoring evidence; whichever route you choose must export these ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4); [Art. 72](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72)).
- Practitioner (tagged): start simple/in-house for data viewing; be wary of generic vendor evals for problem-specific quality ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).
- Criteria candidates (own synthesis, not sourced): data sensitivity/residency, exportability, judge transparency, CI fit, cost model, team capacity, vendor viability.

## Common failure modes
- Building a custom harness for commodity needs (tracing, storage) or buying one that hides judge prompts and cannot reproduce results (inference).
- Underestimating maintenance of in-house harnesses (inference).
- Vendor/tool volatility: tools change ownership, pricing, and license; verify at decision time (as-of 2026-11-20 for tool facts above).

## Practice exercise
Write a one-page decision record for your capstone: weighted criteria, three options (in-house thin harness on an open-source runner; open-source platform self-hosted; commercial platform), evidence from docs for each criterion, exit plan, review date.

## Mastery check
1. Which parts of eval infrastructure should never be outsourced (gold datasets, rubrics, thresholds)?
2. What is your lock-in exit cost in days?
3. How would you test a vendor's built-in metric before trusting it?

## Sources
- Tool docs as in eval-tooling-landscape; https://platform.claude.com/docs/en/build-with-claude/batch-processing
- practitioner: https://hamel.dev/blog/posts/evals/
- GAP: no primary source for decision criteria. Suggest candidate sources: vendor license files and data processing terms (not researched).
