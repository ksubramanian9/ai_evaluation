---
id: task-definition-and-success-criteria
title: "Task definition and success criteria"
branch: 02-eval-design
depth: L2
status: not-started
bridge: none
prerequisites: [evaluation-mindset]
tags: [statistics]
---
# Task definition and success criteria

Turning a vague quality goal into an explicit, testable definition of success.

_Researched 2026-11-20; full notes in [research/02-eval-design.md](../../research/02-eval-design.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Anthropic's docs say to define success criteria before building evals; good criteria are specific, measurable, achievable, relevant, and most use cases need multidimensional criteria (example: F1 >= 0.85, 99.5% non-toxic, 95% of responses < 200ms) ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- OpenAI's workflow starts with "Define eval objective" ([OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- Measurement-theory framing: unobservable constructs must be inferred via a measurement model whose assumptions can diverge from the intended concept ([Jacobs & Wallach](https://arxiv.org/abs/1912.05511)).
- Evaluation should be grounded in real human needs/context (socio-technical gap) ([Liao & Xiao](https://arxiv.org/abs/2306.03100)).

## Common failure modes
- "Good performance" without an operational definition ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Criteria that exist only after seeing outputs ("criteria drift": users need criteria to grade, but grading helps define criteria) ([Shankar et al.](https://arxiv.org/abs/2404.12272)).
- Target unrealistic for current model capability ([Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- Mismatch between construct and operationalization ([Jacobs & Wallach](https://arxiv.org/abs/1912.05511)).

## Practice exercise (2-3 h)
Pick an app (e.g., support-ticket summarizer). Write 4-6 criteria, each rewritten to pass the specific/measurable/achievable/relevant test; attach a measurement method and threshold to each. Grade 20 outputs, then revise criteria and log what changed (observe criteria drift yourself).

## Mastery check
1. Rewrite "the bot should be helpful" as 3 testable criteria with measurement methods.
2. Explain criteria drift and how an iterative process handles it.
3. Which criteria are construct-level vs directly observable, and what assumption links them?

## Sources
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Jacobs & Wallach, measurement and fairness](https://arxiv.org/abs/1912.05511)
- [Liao & Xiao, socio-technical gap](https://arxiv.org/abs/2306.03100)
- [Shankar et al. 2024, Who Validates the Validators?](https://arxiv.org/abs/2404.12272)
