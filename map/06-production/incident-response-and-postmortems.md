---
id: incident-response-and-postmortems
title: "Incident response and postmortems"
branch: 06-production
depth: L2
status: not-started
bridge: testing
prerequisites: [observability-and-tracing]
tags: []
---
# Incident response and postmortems

Handling AI failures in production and learning from them.

_Researched 2026-11-20; full notes in [research/06-production.md](../../research/06-production.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Google SRE: blameless postmortems assume everyone had good intentions and fix systems; triggers should be defined in advance (user-visible degradation over a threshold, data loss, on-call intervention such as rollback, long resolution, monitoring failure); good postmortems record impact, mitigation, root causes, follow-ups ([SRE book: postmortem culture](https://sre.google/sre-book/postmortem-culture/)).
- Incident roles: incident command, operations (only group changing the system), communication, planning; declare early; keep a live incident document ([SRE book: managing incidents](https://sre.google/sre-book/managing-incidents/)).
- The AI Incident Database collects real-world failures to build "collective memory" so mistakes aren't repeated (1,000+ reports at publication) ([McGregor, arXiv 2011.08512](https://arxiv.org/abs/2011.08512)).

## Common failure modes
- Blame, which hides problems; unreviewed postmortems as formality; stigmatising frequent authors ([SRE postmortem culture](https://sre.google/sre-book/postmortem-culture/)).
- Freelancing, poor communication, narrow technical focus ([SRE incidents](https://sre.google/sre-book/managing-incidents/)).
- AI-specific: no deterministic repro because of non-determinism and provider-side change (Chen et al.: [arXiv 2307.09009](https://arxiv.org/abs/2307.09009)); no stored traces to replay (see observability); action items that do not become regression tests (design).
- Org liability for chatbot output (Moffatt, see runtime-guardrails).

## Practice exercise
(design)
- Pick a public AI incident from the AI Incident Database. Write a blameless postmortem (timeline, impact, contributing factors, detection gap, mitigation) and derive 3 concrete action items, at least one a new eval case and one a monitor/guardrail. Run a tabletop drill with a self-written scenario (e.g. provider silently changes model behaviour).

## Mastery check
1. What makes a postmortem "blameless" in practice, and what are the triggers for one?
2. For an LLM failure that cannot be reproduced, what evidence must you have captured?
3. Show how each action item closes a detect/prevent/mitigate gap.

## Sources
- [SRE book: postmortem culture](https://sre.google/sre-book/postmortem-culture/)
- [SRE book: managing incidents](https://sre.google/sre-book/managing-incidents/)
- [McGregor, AI Incident Database](https://arxiv.org/abs/2011.08512)
