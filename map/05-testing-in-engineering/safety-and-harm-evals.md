---
id: safety-and-harm-evals
title: "Safety and harm evaluation"
branch: 05-testing-in-engineering
depth: L3
status: not-started
bridge: none
prerequisites: [red-teaming, rubric-design]
tags: [safety, llm-judge, statistics]
---
# Safety and harm evaluation

Evaluating for harmful, toxic, or policy-violating output.

_Researched 2026-11-20; full notes in [research/05-testing-in-engineering.md](../../research/05-testing-in-engineering.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Most paper claims were read at abstract level; check numbers against the papers before relying on them. Exercises and mastery checks are proposed designs, not sourced claims._

## Why it matters
- Two-sided: harmful compliance and over-refusal. XSTest (NAACL 2024): 250 safe prompts across ten types that should not be refused plus 200 unsafe contrast prompts; finds exaggerated-safety failures ([Röttger et al., arXiv 2308.01263](https://arxiv.org/abs/2308.01263)).
- AILuminate v1.0 (MLCommons): 12 hazard categories, five-tier grade from Poor to Excellent with entropy-based evaluation; prompt count not on abstract (UNVERIFIED) ([arXiv 2503.05731](https://arxiv.org/abs/2503.05731)).
- HarmBench for refusal robustness ([arXiv 2402.04249](https://arxiv.org/abs/2402.04249)).
- Classifiers as graders/guards: Llama Guard (Llama2-7b instruction-tuned, taxonomy-customizable; matches or beats moderation tools on OpenAI Moderation eval and ToxicChat) ([Inan et al., arXiv 2312.06674](https://arxiv.org/abs/2312.06674)).
- Anthropic's example success criterion: under 0.1% of outputs flagged for toxicity in 10,000 trials ([Anthropic develop-tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).
- NIST AI 600-1 lists twelve GenAI risks ([NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence); count from search snippet, UNVERIFIED).

## Common failure modes
- Optimizing refusal rate only; over-refusal (XSTest) ignored.
- Grader (classifier or LLM judge) bias/miscalibration; taxonomy mismatch with your policy ([Llama Guard](https://arxiv.org/abs/2312.06674) is customizable for this reason).
- Public benchmark contamination/saturation (author judgement).
- Zero-hit result on a small sample read as "safe": 0 failures in 1,000 trials still permits a rate up to ~0.3% at 95% (rule of three; author math).
- Ignoring multi-turn and context-dependent harms (Perez shows conversational harms, [arXiv 2202.03286](https://arxiv.org/abs/2202.03286)).

## Practice exercise (4 h)
Define a 4-category policy for your app. Build 40 harmful + 40 benign-but-similar prompts per category (XSTest style). Grade with rubric + Llama Guard or LLM judge; hand-label 50 to estimate judge agreement. Report harmful-compliance rate and over-refusal rate with CIs; plot the tradeoff across two system-prompt variants.

## Mastery check
1. Why both unsafe-compliance and false-refusal rates?
2. Estimate the upper bound on harm rate after 0/500 observed failures.
3. How do you check that an automated safety grader agrees with your policy?

## Sources
- [XSTest, arXiv 2308.01263](https://arxiv.org/abs/2308.01263)
- [AILuminate, arXiv 2503.05731](https://arxiv.org/abs/2503.05731)
- [HarmBench, arXiv 2402.04249](https://arxiv.org/abs/2402.04249)
- [Llama Guard, arXiv 2312.06674](https://arxiv.org/abs/2312.06674)
- [Perez et al., arXiv 2202.03286](https://arxiv.org/abs/2202.03286)
- [Anthropic docs: develop tests](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
