# Research supplement: judge-bias-and-calibration

As-of: 2026-11-21. Purpose: full-text verification of node claims (audit rec #14).

## Wang et al. 2023, Large Language Models are not Fair Evaluators
URL: https://arxiv.org/html/2305.17926 (full text)
- Abstract: "Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator." Table 2: 66/80 (82.5%) when Vicuna is Assistant 2; 2.5% win rate as Assistant 1. Node now names the ordering.
- Sections 3.1-3.3: Multiple Evidence Calibration, Balanced Position Calibration (evaluate both orders, average), Human-in-the-Loop Calibration using Balanced Position Diversity Entropy (BPDE) to pick hard cases.
- Section 4 / Table 4: MEC + BPC improve alignment by 9.8% (GPT-4) and 14.3% (ChatGPT) accuracy; HITLC cuts annotation cost by up to 39%.

## Panickssery et al. 2024, LLM Evaluators Recognize and Favor Their Own Generations
URL: https://arxiv.org/html/2404.13076 (full text)
- Models: GPT-3.5 Turbo, GPT-4, Llama-2-7b-chat. GPT-4 73.5% out-of-box self-recognition in the pairwise setting.
- Section 3: "Self-preference strength is linearly correlated with self-recognition" after fine-tuning; "The correlation doesn't by itself prove the causal hypothesis". Section 5.2: evidence toward, not validation of, causality; generation quality not controlled. Node now carries the caveat.

## Wataoka et al. 2024, Self-Preference Bias in LLM-as-a-Judge
URL: https://arxiv.org/html/2410.21819 (v2, full text)
- Section 4.1: metric based on Equal Opportunity (algorithmic fairness). Section 1/7: "GPT-4 exhibited a significant self-preference bias". Section 5: LLMs "assign significantly higher evaluations to texts with lower perplexity than human evaluators", "regardless of whether the texts were self-generated".
- Correction: node said "GPT-4 prefers lower-perplexity text"; the perplexity finding is stated for LLMs generally, relative to human evaluators. Fixed.

## Dubois et al. 2024, Length-Controlled AlpacaEval
URL: https://arxiv.org/html/2404.04475 (full text)
- Section 4.2: Spearman with Chatbot Arena 0.94 to 0.98 (38 models). Verified.
- Section 3: logistic GLM with model-identity, tanh-transformed standardized length difference, and instruction-difficulty terms; LC win rate drops the length term ("What would the preference be if the model's and baseline's output had the same length?").
- Section 4.1, Figure 3: gpt4_1106_preview raw win rate 22.9% to 64.3% across verbosity prompts; 41.9% to 51.6% after LC.

## Thakur et al., Judging the Judges
URL: https://arxiv.org/html/2406.12624 (v6, revised 18 Aug 2025, title "Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges"; full text)
- Abstract: "judges with high agreement can still assign vastly different scores". Section 4.1: judges above 90% agreement "may still differ more than 10 points".
- Section 3 footnote 2: earlier version used Cohen's kappa, replaced by Scott's pi due to "well-documented theoretical issues". Section 6: "We recommend computing both percent agreement and Scott's π". Node changed from "chance-corrected metrics" to name Scott's pi.

## Zheng et al. 2023
URL: https://arxiv.org/html/2306.05685 (full text)
- Section 3.3, Table 2: GPT-4 consistent in 65.0% of swapped-order cases, 30.0% biased to first position; Claude-v1 23.8% consistent. Section 3.4: count a win only if consistent across both orders.

## OpenAI, Evaluation best practices
URL: https://developers.openai.com/api/docs/guides/evaluation-best-practices (full page)
- "Control for response lengths as LLMs bias towards longer responses in general." Names position bias as a challenge without a specific mitigation.

## Gaps
- Mastery question 3 (calibration-set size and pass threshold) has no sourced numeric guidance; it remains a design exercise.
