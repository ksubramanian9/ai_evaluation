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
- Holtzman et al., "The Curious Case of Neural Text Degeneration" (ICLR 2020): https://arxiv.org/abs/1904.09751
- Hugging Face Transformers, generation strategies: https://huggingface.co/docs/transformers/generation_strategies
- Anthropic, context windows: https://platform.claude.com/docs/en/build-with-claude/context-windows
- OpenAI cookbook, reproducible outputs with seed (archived): https://developers.openai.com/cookbook/examples/reproducible_outputs_with_the_seed_parameter
- Practitioner: Thinking Machines, "Defeating Nondeterminism in LLM Inference": https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
