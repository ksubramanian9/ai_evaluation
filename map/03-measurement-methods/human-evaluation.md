---
id: human-evaluation
title: "Human evaluation"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: none
prerequisites: [rubric-design, annotation-guidelines]
tags: [human-labels, cost]
---
# Human evaluation

Designing and running human rating studies, including cost and quality control.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Human judgment is the reference that automatic metrics and LLM judges are validated against.
- OpenAI's guide says human labels are the ground truth for calibrating judges and that expert review is costly but needed for calibration ([OpenAI eval best practices, as-of 2026-11-20](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- Anthropic's docs list expert rubrics as a qualitative method but also recommend volume over quality: more automatically graded questions beat fewer hand-graded ones ([Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).

## Common failure modes
- Untrained crowd raters could not tell GPT-3 text from human text (chance level). Quick training raised accuracy only to about 55%, not significantly in all domains, and raters gave conflicting reasons ([Clark et al. 2021](https://arxiv.org/abs/2107.00061)).
- Inconsistent design across NLG papers; van der Lee et al. review practice and propose best practices ([van der Lee et al. 2019](https://aclanthology.org/W19-8643/)).
- Underpowered rating studies: typical human-rating designs are likely underpowered to detect small model differences ([Card et al. 2020](https://arxiv.org/abs/2010.06595)).
- Criteria drift: people define criteria while grading outputs, so rubrics change as raters see outputs ([Shankar et al. 2024](https://arxiv.org/abs/2404.12272)).

## Practice exercise (2-3 h)
Write a 3-criterion rubric with anchors. Have two raters (you on two different days is acceptable) score 40 outputs. Time it, compute cost per item, note rubric edits needed after the first 10 items, and revise.

## Mastery check
1. Name design choices that decide validity (rater qualification, rubric anchors, randomized order); map them to van der Lee (list itself UNVERIFIED).
2. When is human eval worth its cost against an LLM judge?
3. How many items do you need to detect a 5-point difference? (Card et al. power analysis.)

## Sources
- [van der Lee et al. 2019, Best practices for the human evaluation of generated text](https://aclanthology.org/W19-8643/)
- [Clark et al. 2021, All That's 'Human' Is Not Gold](https://arxiv.org/abs/2107.00061)
- [Card et al. 2020, With Little Power Comes Great Responsibility](https://arxiv.org/abs/2010.06595)
- [Shankar et al. 2024, Who Validates the Validators?](https://arxiv.org/abs/2404.12272)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
