# Research supplement: llm-as-judge

As-of: 2026-11-21. Purpose: full-text verification of node claims (audit rec #14).

## Zheng et al. 2023, Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
URL: https://arxiv.org/html/2306.05685 (full text)
- Abstract: GPT-4 reaches "over 80% agreement, the same level of agreement between humans". Section 4.2, Table 5: MT-bench without ties, GPT-4 vs human 85%, human vs human 81%. Table 6 (Chatbot Arena): GPT-4 vs human 87% without ties. Node wording "comparable to" tightened to "the same level as", plus the MT-bench numbers.
- Section 3.3: position, verbosity, self-enhancement bias; limited math grading: default prompt failed 14 of 20 judgments (70%) on 10 math questions; reference-guided grading cut this to 15% (section 3.4, Table 4).

## Liu et al. 2023, G-Eval
URL: https://arxiv.org/html/2303.16634 (full text)
- Section 2: auto-CoT evaluation steps from task introduction and criteria; "form-filling paradigm"; score = sum of p(s_i) * s_i over score tokens (Eq. 1).
- Table 1: G-Eval-4 average Spearman 0.514 (Kendall 0.418) on SummEval. Verified.
- Section 4: "G-Eval may have a bias towards the LLM-generated summaries"; "should be considered as a preliminary study". Verified.

## Kim et al. 2023, Prometheus
URL: https://arxiv.org/html/2310.08491 (read first ~100k of ~111k characters; all cited sections covered)
- Abstract and section 5.1, Figure 4: Pearson 0.897 on 45 customized rubrics, GPT-4 0.882, ChatGPT 0.392 (body calls it GPT-3.5-Turbo). Verified.
- Inputs: instruction, response, customized score rubric, reference answer ("would receive a score of 5"). Feedback Collection: 1K rubrics, 20K instructions, 100K responses with feedback (section 3, Table 1).
- Section 1: proprietary evaluators: "Closed-source Nature", "Uncontrolled Versioning", "Prohibitive Costs". Node expanded from two to three reasons.

## Shankar et al. 2024, Who Validates the Validators?
URL: https://arxiv.org/html/2404.12272 (read first ~100k of ~125k characters, through the findings sections)
- Abstract: LLM evaluators "simply inherit all the problems of the LLMs they evaluate, requiring further human validation". Criteria drift: "users need criteria to grade outputs, but grading outputs helps users define criteria". EvalGen in ChainForge; qualitative study with 9 practitioners (section 6). Verified.

## Anthropic, Develop tests
URL: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests (full page, read across two fetches)
- "Tips for LLM-based grading": "Have detailed, clear rubrics"; "Be empirical or specific" (output only 'correct' or 'incorrect', or a 1-5 scale); "Encourage reasoning" (grader with thinking on). Code comment: "Generally best practice to evaluate with a different model from the one used to generate the evaluated output". Binary prompt ends "Output only 'yes' or 'no'."
- Correction: the node attributed "use binary or Likert formats with clear criteria" loosely; it now paraphrases the page's actual three tips and adds "encourage reasoning", which the node had attributed only to OpenAI.

## OpenAI, Evaluation best practices
URL: https://developers.openai.com/api/docs/guides/evaluation-best-practices (full page)
- "Use the most capable model to grade if you can." "Add reasoning and chain-of-thought as reasoning before scoring improves eval performance." "Use pairwise comparison or pass/fail for more reliability." Validate "agreement against your human labels before optimizing for cost or latency." Verified. The page names a specific current model; that is volatile and was not put in the node.

## Gaps
- None of the node's sourced claims remain unverified. The first bullet ("Strong LLM judges can approximate human preference at scale") is a summary of the Zheng result, not a separate claim.
