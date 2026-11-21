# AI Evaluation Map: Context

Glossary for this repo. Terms only; no implementation detail.

**Map**: The curriculum as a whole: seven branches of nodes, with prerequisite links between them.

**Branch**: One of seven themed groups of nodes (foundations, eval design, measurement methods, system-specific evals, testing in engineering, production, operating practice). Numbered 01 to 07 in suggested study order.

**Node**: One durable concept to learn, with why it matters, failure modes, a practice exercise, a mastery check and sources. Every node has a depth, a status and a bridge.

**Depth**: The target depth for this learner, not the node's difficulty. L1 awareness: can explain it and recognise when it applies. L2 working: can apply it to a real system. L3 expert: can design, critique and adapt it, and make the trade-offs. A prerequisite may have a higher depth than the node that needs it; the prerequisite only sets study order.

**Status**: Where the learner is with a node: not-started, learning, practiced, mastered. The Markdown frontmatter is the only source of truth. A node moves to practiced when its practice exercise is done and its result written down, and to mastered when its done bar is met.

**Learning objectives**: What the learner can do once a node reaches its target depth, written as observable abilities.

**Done bar**: A node's concrete evidence for moving status to practiced and to mastered.

**Owner node**: The one node responsible for a concept that several nodes touch. Other nodes point to it instead of repeating it.

**Bridge**: The gap a node helps close for this learner: stats (ML/statistics), testing (test engineering), or none.

**Prerequisite**: A node that should be understood before another. Prerequisites form an acyclic graph and may cross branches.

**Candidate**: A topic that might become a node but is not part of the map yet.

**Landscape entry**: A volatile fact (tool, benchmark, model, standard) kept outside the nodes, each with an as-of date. Stale when its as-of date is older than the staleness threshold.

**Research notes**: Sourced findings per branch from which a node was written.

**Capstone**: The end-to-end project (RAG app, then tool-using agent) that exercises the map.

**Site**: The generated, read-only web presentation of all of the above.
