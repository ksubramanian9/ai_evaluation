---
id: sandboxing-untrusted-code
title: "Sandboxing untrusted code"
branch: 03-measurement-methods
depth: L2
status: not-started
bridge: testing
prerequisites: [programmatic-checks]
tags: [security, safety]
---
# Sandboxing untrusted code

Isolating execution of model-generated code and tool calls during evals so a bad output cannot damage the host.

_Added 2026-11-20 to close a gap flagged by the system-specific-evals research. Supplemented 2026-11-21: [research/supplements/2026-11-21-sandboxing-untrusted-code.md](../../research/supplements/2026-11-21-sandboxing-untrusted-code.md). Tool flags are volatile; check current docs. Exercises and mastery checks are proposed designs, not sourced claims._

## Learning objectives
You can:
- Run model-generated code in a container with no network, CPU, memory, process and time limits, and a read-only filesystem.
- Test isolation by running hostile programs and recording what the sandbox blocks.
- Reset state between trials so earlier runs cannot change later results.
- Choose an isolation layer (container, gVisor, microVM) and state what it does not protect against.

**Done bar.** Practiced: a run log for 20 generated programs inside the sandbox, plus a record of what was blocked when a program tried to read a host file, open a socket and fork-bomb. Mastered: written answers to all three mastery-check questions, checked against Chen et al., the Docker, gVisor and Firecracker docs and Anthropic, plus the sandbox used for a real or capstone code or agent eval with its configuration recorded.

## Why it matters
- The Codex authors sandboxed execution because generated programs "are often incorrect"; the goal was to stop programs modifying, persisting on, or exfiltrating from a host or network ([Chen et al., sec. 2.3](https://arxiv.org/abs/2107.03374)).
- human-eval's guard "is NOT a security sandbox": it disables functions such as `os.fork` and `shutil.rmtree`, and sets memory rlimits only if you pass a limit ([execution.py](https://github.com/openai/human-eval/blob/master/human_eval/execution.py)).
- Established harnesses isolate per task: SWE-bench runs evaluation in Docker with per-task images ([SWE-bench Docker guide](https://github.com/SWE-bench/SWE-bench/blob/main/docs/guides/docker_setup.md)); Inspect gives each sample its own sandbox and cleans up automatically ([Inspect sandboxing](https://inspect.aisi.org.uk/sandboxing.html)).

**Isolation layers and their limits**
- Containers isolate with namespaces, cgroups and capabilities, but share the host kernel; Docker warns defaults "may provide incomplete isolation" combined with kernel vulnerabilities ([Docker security](https://docs.docker.com/engine/security/)).
- gVisor implements syscalls in a user-space kernel so none pass to the host. It does not cover hardware side channels, resource exhaustion (host cgroups) or network policy (container level) ([gVisor security model](https://gvisor.dev/docs/architecture_guide/security/)).
- Firecracker microVMs use KVM as "the first layer of isolation", plus seccomp and a jailer; it treats the guest as malicious but does no network filtering, so egress "should be filtered at the host-level" ([Firecracker design](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md)).

**Controls**
- Network: Docker's `none` driver leaves only loopback ([Docker none network](https://docs.docker.com/engine/network/drivers/none/)). Codex used eBPF firewall rules allowing only experiment-control traffic ([Chen et al.](https://arxiv.org/abs/2107.03374)).
- Resources: containers have no limits by default; set `--memory`, `--memory-swap` and `--cpus` ([Docker resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)), and `--pids-limit` against fork bombs ([docker run](https://docs.docker.com/reference/cli/docker/container/run/)).
- Filesystem and privileges: `--read-only` with a `--tmpfs` scratch mount, `--cap-drop`, `no-new-privileges`, and `--rm` for cleanup ([docker run](https://docs.docker.com/reference/cli/docker/container/run/)).
- Time: wall-clock timeouts, as in human-eval's alarm plus process kill ([execution.py](https://github.com/openai/human-eval/blob/master/human_eval/execution.py)).

## Common failure modes
- Running model code on the host or CI runner; Inspect's `local` sandbox is explicitly "no sandbox" ([Inspect](https://inspect.aisi.org.uk/sandboxing.html)).
- Trusting a non-root user: Inspect warns "Don't count on a non-root container user to contain an adversarial model" ([Inspect](https://inspect.aisi.org.uk/sandboxing.html)).
- A custom Compose file silently drops Inspect's default `network_mode: none` ([Inspect](https://inspect.aisi.org.uk/sandboxing.html)).
- Shared state between trials (leftover files, caches, exhausted resources) causes correlated failures or inflates scores, e.g. Claude reading earlier trials' git history ([Anthropic](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).
- Too-tight limits: OOM kills and timeouts get graded as wrong answers. Separating "infrastructure failure" from "fail" is a proposed practice, not sourced.

## Practice exercise (2 h)
Run 20 generated programs from [code-generation-evals](../04-system-specific-evals/code-generation-evals.md) in a fresh `--rm` container with `--network none`, `--memory`, `--cpus`, `--pids-limit`, `--read-only` plus a tmpfs, and a timeout. Then run a program that reads a host file, opens a socket and fork-bombs, and record what each control blocks. Repeat once with `--runtime=runsc` (gVisor) if available.

## Mastery check
1. What isolation do you need to run model-generated code, and what does each layer (container, gVisor, microVM) not protect against?
2. How do you reset state between trials, and how would you detect leakage?
3. Which limits (time, memory, network, filesystem) matter for grading correctness versus safety?

## Sources
- [Chen et al., "Evaluating Large Language Models Trained on Code", arXiv 2107.03374](https://arxiv.org/abs/2107.03374)
- [OpenAI human-eval, execution.py](https://github.com/openai/human-eval/blob/master/human_eval/execution.py)
- [Docker, Engine security](https://docs.docker.com/engine/security/)
- [Docker, Resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)
- [Docker, docker container run reference](https://docs.docker.com/reference/cli/docker/container/run/)
- [Docker, None network driver](https://docs.docker.com/engine/network/drivers/none/)
- [gVisor, Security model](https://gvisor.dev/docs/architecture_guide/security/)
- [Firecracker, Design](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md)
- [SWE-bench, Docker setup guide](https://github.com/SWE-bench/SWE-bench/blob/main/docs/guides/docker_setup.md)
- [Inspect AI, Sandboxing](https://inspect.aisi.org.uk/sandboxing.html)
- [Anthropic, "Demystifying evals for AI agents"](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
