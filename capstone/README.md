# Capstone

Build and evaluate one system end to end; every step links to map nodes.

- **Stage 1: RAG question-answering app** over a chosen document set.
- **Stage 2: tool-using agent**, extending stage 1.

## Steps (to be detailed)

| Step | Activity | Nodes |
|---|---|---|
| 1 | Define task and success criteria | task-definition-and-success-criteria |
| 2 | Build golden dataset | golden-datasets, synthetic-data-generation |
| 3 | Retrieval evals | rag-retrieval-evals |
| 4 | Generation evals with a validated judge | rag-generation-evals, llm-as-judge, judge-bias-and-calibration |
| 5 | Regression suite and CI gate | regression-testing, ci-eval-gates |
| 6 | Red teaming and robustness | red-teaming, robustness-testing |
| 7 | Tracing and production monitoring | observability-and-tracing, drift-detection |
| 8 | Extend to agent: trajectory and tool-use evals | agent-trajectory-evals, tool-use-evals |

Open decisions: document set, model/provider, hosting.
