---
id: llm-basics-for-evaluators
title: "LLM basics for evaluators"
branch: 01-foundations
depth: L1
status: not-started
bridge: none
prerequisites: []
tags: [nondeterminism]
---
# LLM basics for evaluators

Tokens, context windows, sampling parameters, and system vs. model behavior as they affect what can be measured.

_Researched 2026-11-20 from the sources below; full notes in [research/01-foundations.md](../../research/01-foundations.md). Items marked UNVERIFIED were not confirmed from a fetched primary page. Check numeric claims against the papers before relying on them._

## Learning objectives
You can:
- Explain what counts toward the context window in an agentic request with tools and thinking.
- Explain how greedy, temperature and top-p decoding differ and why decoding settings change eval results.
- Recognise why temperature 0 does not give reproducible output, and what the API-version note means for repeatable evals.
- Identify the fields an eval run must log (model version, sampling params, system prompt, fingerprint) to be reproducible.

**Done bar.** Practiced: a log comparing unique-output counts and lengths for greedy, sampling and beam search, plus the token count at which the padded retrieval question failed. Mastered: written answers to all three mastery-check questions, checked against Holtzman et al., the Hugging Face and Anthropic docs and the verification log, plus explaining to someone else without notes why "temperature 0" is not a reproducibility guarantee.

## Why it matters
- Decoding strategy alone can change output quality a lot for the same model. Greedy decoding gets repetitive on long outputs, and sampling trades determinism for diversity ([Holtzman et al. 2020](https://arxiv.org/abs/1904.09751); [HF generation strategies](https://huggingface.co/docs/transformers/generation_strategies)).
- The context window is everything the model can reference, including its own output: system prompt, tool definitions, tool results and thinking tokens all count. Accuracy and recall degrade as token count grows ("context rot") ([Anthropic context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)).
- "Deterministic" settings are not deterministic; see [nondeterminism-and-variance](nondeterminism-and-variance.md). Anthropic's SDK reference says temperature 0.0 results "will not be fully deterministic" (cited from a [mirror of the API docs](https://rubydoc.info/github/anthropics/anthropic-sdk-ruby/main/Anthropic%2FModels%2FBeta%2FMessageCreateParams:temperature); the official reference page was too large to fetch, so treat as secondary).
- The thing under test is model + prompt + sampling config + serving stack. OpenAI exposes `system_fingerprint` to signal backend configuration changes and calls determinism best-effort ([archived cookbook](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter); [Azure restatement](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output)). UNVERIFIED against current OpenAI docs: the current page returned 404.

## Common failure modes
- Context overflow or silent truncation, or counting only the user message tokens (per Anthropic, input over the window returns a 400 error).
- Assuming temperature 0 means reproducible.
- Evaluating a model name without recording version, sampling params, system prompt and fingerprint.
- Burying key facts deep in long contexts and blaming the model's "knowledge" for the resulting failure.
- Putting volatile facts (context sizes, parameter support) in this node. They belong in `landscape/`.

## Practice exercise (2 h)
With a small open model through Hugging Face `generate`, run one prompt with greedy, sampling (temperature 0.7, top_p 0.9) and beam search, 20 samples each. Compare unique-output counts and length. Then pad the prompt with irrelevant text until a retrieval question fails, and log the token count at failure with the tokenizer.

## Mastery check
1. What counts toward the context window in an agentic request with tools and thinking?
2. Explain greedy vs top-p vs temperature, and which settings you would fix in an eval and why.
3. List the fields you must log for an eval run to be reproducible.

## Sources
- [Holtzman et al., "The Curious Case of Neural Text Degeneration" (ICLR 2020)](https://arxiv.org/abs/1904.09751)
- [Hugging Face Transformers, generation strategies](https://huggingface.co/docs/transformers/generation_strategies)
- [Anthropic, context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [OpenAI cookbook, reproducible outputs with seed (archived)](https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter)
- practitioner: [Thinking Machines, "Defeating Nondeterminism in LLM Inference"](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)

## Verification log (2026-11-20)
Confirmed on Anthropic's official [API migration page](https://platform.claude.com/docs/en/api/migration-2026-10-21): in API version `2026-10-21`, "a request that sends `temperature`, `top_p`, or `top_k` returns a 400 error, even at the parameter's default value", with no model exception. Without them, requests use defaults (temperature 1.0). Models that already accepted only defaults, such as Claude 4.7 and later, sample as before. The page says no other setting replaces temperature. Requests that need a non-default value must stay on version `2023-06-01`. Practical consequence: on this version you cannot lower temperature to make evals repeatable, so use recorded responses, mocks, multiple samples and statistics instead.

This supersedes the mirror-based citation for temperature behavior above; the "not fully deterministic" claim itself still rests only on the SDK mirror.
