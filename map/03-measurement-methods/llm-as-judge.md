---
id: llm-as-judge
title: "LLM-as-judge"
branch: 03-measurement-methods
depth: L3
status: not-started
bridge: none
prerequisites: [rubric-design, human-evaluation]
tags: [llm-judge, human-labels]
---
# LLM-as-judge

Using a model to grade outputs: prompt design, scoring formats, and when it is appropriate.

_Researched 2026-11-20; full notes in [research/03-measurement-methods.md](../../research/03-measurement-methods.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Verified in full text on 2026-11-21: Zheng et al., Liu et al., Kim et al. and Shankar et al. (arXiv HTML; Kim and Shankar first ~100k characters, covering all cited sections), the Anthropic develop-tests page and the OpenAI evaluation best-practices page. Supplemented 2026-11-21: [research/supplements/2026-11-21-llm-as-judge.md](../../research/supplements/2026-11-21-llm-as-judge.md). Exercises and mastery checks are proposed designs, not sourced claims._

**Owns:** judge design and validation; see also [judge-bias-and-calibration](judge-bias-and-calibration.md), [production-evals-with-judges](../06-production/production-evals-with-judges.md).

## Learning objectives
You can:
- Write a judge prompt with a rubric, a reasoning step and a strict output format.
- Validate a judge against human labels with kappa and a confusion matrix, and iterate the rubric.
- Compare binary, Likert and pairwise judging formats and choose one for a task.
- Critique a judge setup (unvalidated, same model family as the generator, uncontrolled versioning) and decide whether it is fit for regression gating.

**Done bar.** Practiced: the judge prompt, kappa and confusion matrices for two judge models on 50 labeled outputs, and one rubric iteration with its effect on agreement. Mastered: written answers to all three mastery-check questions, checked against Zheng et al., Liu et al., Kim et al., Shankar et al. and the Anthropic and OpenAI guides, plus a design or critique of a real judge that decides whether it can gate releases and states the trade-off between cost, bias and agreement.

## Why it matters
- Strong LLM judges can approximate human preference at scale.
- Zheng et al. report GPT-4 judges reaching over 80% agreement with controlled and crowdsourced human preferences, the same level as human-human agreement; on MT-bench without ties, GPT-4 agreed with humans 85% versus 81% human-human (section 4.2, Table 5) ([Zheng et al. 2023](https://arxiv.org/abs/2306.05685)).
- G-Eval has the LLM generate chain-of-thought evaluation steps, scores in a form-filling paradigm, and takes a probability-weighted sum of score tokens (section 2); it reports Spearman 0.514 with humans on SummEval with GPT-4 (Table 1) ([Liu et al. 2023](https://arxiv.org/abs/2303.16634)).
- Prometheus (open 13B judge trained on the 100K-response Feedback Collection; inputs are instruction, response, custom score rubric and a score-5 reference answer) reports Pearson 0.897 with humans on 45 custom rubrics (GPT-4 0.882, ChatGPT 0.392; section 5.1, Figure 4) ([Kim et al. 2023](https://arxiv.org/abs/2310.08491)).
- Vendor guidance: have detailed, clear rubrics; be empirical or specific (e.g. output only 'correct' or 'incorrect', or a 1-5 scale); encourage reasoning before the score; and it is "generally best practice to evaluate with a different model from the one used to generate the evaluated output" (Tips for LLM-based grading and code examples, [Anthropic docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- OpenAI: "use the most capable model to grade if you can", add reasoning before scoring, "use pairwise comparison or pass/fail for more reliability", and validate agreement against human labels before optimizing for cost ([OpenAI guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).

## Common failure modes
- Position, verbosity and self-enhancement bias, plus limited math and reasoning grading (default prompt failed 14 of 20 math judgments; reference-guided grading cut this to 15%) (sections 3.3-3.4, [Zheng et al.](https://arxiv.org/abs/2306.05685)).
- Possible bias toward LLM-generated text, which the authors call "a preliminary study" (section 4, [G-Eval](https://arxiv.org/abs/2303.16634)).
- Proprietary judges are closed-source, have uncontrolled versioning and prohibitive costs (section 1, [Prometheus](https://arxiv.org/abs/2310.08491)).
- LLM evaluators "inherit all the problems of the LLMs they evaluate, requiring further human validation"; criteria drift: "users need criteria to grade outputs, but grading outputs helps users define criteria" (qualitative study with 9 practitioners, section 6) ([Shankar et al.](https://arxiv.org/abs/2404.12272)).

## Practice exercise (2-3 h)
Take 50 outputs from a small task with your own pass/fail labels. Write a judge prompt with a rubric, a reasoning step and a strict output format. Run it with two judge models. Report agreement with your labels (kappa) and the confusion matrix. Iterate the rubric once.

## Mastery check
1. Why validate a judge against human labels before using it for regression gating?
2. Compare binary, Likert and pairwise judging formats.
3. Show what changes when the judge shares a model family with the generator.

## Sources
- [Zheng et al. 2023, MT-Bench paper](https://arxiv.org/abs/2306.05685)
- [Liu et al. 2023, G-Eval](https://arxiv.org/abs/2303.16634)
- [Kim et al. 2023, Prometheus](https://arxiv.org/abs/2310.08491)
- [Shankar et al. 2024, Who Validates the Validators?](https://arxiv.org/abs/2404.12272)
- [Anthropic, develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [OpenAI, evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
