# Research supplement: online-experiments

As-of: 2026-11-21. Web access: WebFetch and WebSearch working. Adds the "Sequential testing and the peeking problem" subsection.

- Johari, Pekelis, Walsh, "Always Valid Inference: Bringing Sequential Analysis to A/B Testing" (arXiv 1512.04922, 2015, rev. 2019). Standard inference "wholly unreliable if users endogenously choose samples sizes"; always-valid p-values and CIs valid whenever user stops; sequential-test interface; multiple-testing control; deployed on large commercial platform, hundreds of thousands of experiments. Abstract does not state a specific Type I error figure. https://arxiv.org/abs/1512.04922 (abstract)
- Howard, Ramdas, McAuliffe, Sekhon, "Time-uniform, nonparametric, nonasymptotic confidence sequences" (Annals of Statistics 49(2), 2021; arXiv 1810.08240). Confidence sequence = CIs "uniformly valid over an unbounded time horizon"; finite-sample, nonparametric; links Cramér-Chernoff, LIL and SPRT; application to average treatment effect. https://arxiv.org/abs/1810.08240 (abstract)
- Deng, Lu, Chen, "Continuous Monitoring of A/B Tests without Pain: Optional Stopping in Bayesian Testing" (arXiv 1602.05549, 2016; IEEE DSAA). Proves Bayesian testing with continuous monitoring valid under proper stopping rules; identifies improper practices; guidelines. Note: author is Shouyuan Chen (the assignment's "Deng et al." resolved to this paper). https://arxiv.org/abs/1602.05549 (abstract)
- Search also surfaced YEAST (arXiv 2406.16523); not read, not cited.

## Gaps
- Magnitude of false-positive inflation from peeking not taken from a primary source (node's exercise simulates it instead).
- "Choosing a method" bullet is design guidance.
