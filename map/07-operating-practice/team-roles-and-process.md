---
id: team-roles-and-process
title: "Team roles and process"
branch: 07-operating-practice
depth: L2
status: not-started
bridge: none
prerequisites: [eval-driven-development]
tags: [human-labels, llm-judge]
---
# Team roles and process

Who owns evals, how domain experts and engineers collaborate, and review cadence.

_Researched 2026-11-20; full notes in [research/07-operating-practice.md](../../research/07-operating-practice.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Build a RACI for the eval lifecycle (dataset curation, rubric, judge calibration, release gate, incident review, periodic re-audit) with a named owner for eval quality.
- Run an iterative rubric session with a domain expert grading blind, record disagreements, revise the rubric and report agreement.
- Apply a review cadence for refreshing test sets, recalibrating judges and re-reviewing thresholds, with stated triggers for an unscheduled review.

**Done bar.** Practiced: a written RACI for the eval lifecycle plus a 30-example blind rubric session with disagreements, a revised rubric and an agreement figure. Mastered: written answers to all three mastery questions checked against NIST AI 100-1 (GOVERN 2.1, MEASURE 4.1) and Shankar et al., and the RACI and cadence adopted on a capstone or real team with one review cycle recorded.

## Why it matters
- NIST GOVERN 2.1: "Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear"; GOVERN 2.3: executive leadership takes responsibility for risk decisions; GOVERN 4.1: safety-first, critical-thinking culture; MEASURE 4.1: measurement approaches "informed through consultation with domain experts and other end users" ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Tables 1-3). AI 100-1 says subject matter experts help evaluate TEVV findings and align TEVV parameters to requirements (Sec. 2 / AI actors). TEVV actors are integrated across the lifecycle ([AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), Sec. 2).
- Shankar et al. ("Who Validates the Validators?", Apr 2024): human-in-loop; "criteria drift": users need criteria to grade outputs, but grading outputs helps define criteria, so criteria cannot be fully fixed up front ([arXiv 2404.12272](https://arxiv.org/abs/2404.12272)). Implication: domain-expert grading must be iterative, with engineers building tooling.
- Provider guidance: Anthropic docs favor task-specific evals mirroring the real distribution, including edge cases where even humans disagree; automation where possible; volume over hand-graded quality; LLM graders ideally a different model from the generator ([Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), as-of 2026-11-20).
- Practitioner (tagged): Hamel Husain describes unit tests, human+model eval, A/B tests; reviewers must keep reading data; look at data with low-friction viewers ([hamel.dev, practitioner](https://hamel.dev/blog/posts/evals/)).
- EU Act: Annex IV test reports must be "dated and signed by accountable people" ([Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)), implying named owners.

## Common failure modes
- No named owner for eval quality; evals owned by whoever last touched the prompt (inference from GOVERN 2.1).
- Domain experts used only at the end, or asked to write fixed rubrics before seeing outputs (criteria drift).
- Eval author = system author with no independent review (inference; UNVERIFIED as a documented primary-source claim).
- Whack-a-mole prompt fixing without regression evals (practitioner: Husain).
- Judge never validated against human labels (Shankar; Husain).

## Practice exercise (3 h)
Write a RACI for your eval lifecycle (dataset curation, rubric, judge calibration, release gate, incident review, periodic re-audit). Then run a 30-example rubric session with one other person grading blind, record disagreements, revise rubric, report agreement.

## Mastery check
1. Who has authority to block a release on eval results, and where is it written?
2. Describe criteria drift and how your process handles it.
3. What cadence for refreshing test sets, recalibrating judges, and re-reviewing thresholds, and what triggers an unscheduled review?

## Sources
- [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)
- [Shankar et al., Who Validates the Validators, arXiv 2404.12272](https://arxiv.org/abs/2404.12272)
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [EU AI Act Annex IV](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-4)
- practitioner: [Hamel Husain, evals](https://hamel.dev/blog/posts/evals/)
