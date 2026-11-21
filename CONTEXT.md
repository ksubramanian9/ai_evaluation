# AI Evaluation Map: Context

Glossary for this repo. Terms only; no implementation detail.

**Map**: The curriculum as a whole: seven branches of nodes, with prerequisite links between them.

**Branch**: One of seven themed groups of nodes (foundations, eval design, measurement methods, system-specific evals, testing in engineering, production, operating practice). Numbered 01 to 07 in suggested study order.

**Node**: One durable concept to learn, with why it matters, failure modes, a practice exercise, a mastery check and sources. Every node has a depth, a status and a bridge.

**Depth**: How far to take a node. L1 awareness, L2 working knowledge, L3 expert.

**Status**: Where the learner is with a node: not-started, learning, practiced, mastered. The Markdown frontmatter is the only source of truth.

**Bridge**: The gap a node helps close for this learner: stats (ML/statistics), testing (test engineering), or none.

**Prerequisite**: A node that should be understood before another. Prerequisites form an acyclic graph and may cross branches.

**Candidate**: A topic that might become a node but is not part of the map yet.

**Landscape entry**: A volatile fact (tool, benchmark, model, standard) kept outside the nodes, each with an as-of date. Stale when its as-of date is older than the staleness threshold.

**Research notes**: Sourced findings per branch from which a node was written.

**Capstone**: The end-to-end project (RAG app, then tool-using agent) that exercises the map.

**Site**: The generated, read-only web presentation of all of the above.
