# Autonomous Agent Principles

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19732890.svg)](https://doi.org/10.5281/zenodo.19732890)

**If an autonomous action is not auditable, it is broken. Not risky — broken.**

The correct response to broken is revocation, not tolerance. Autonomy that cannot be traced cannot be trusted. Trust that cannot be earned cannot be revoked.

This repository is the framework that makes that a requirement rather than a preference. Three architectural principles. One measurable property. No tool prescriptions — any stack can conform.

1. **Commander's Intent** — define the destination, never the route. The agent must interpret and adapt, not execute a checklist.
2. **Observable Autonomy** — every autonomous operation produces a visible, auditable trail. If it cannot be seen, it should not be running.
3. **Convergence Is Silence** — the work is done when independent evaluators find nothing left to change. Not when a score stops moving.

One conformance example — the [autonomous-agent-skills suite](https://github.com/ntholm86/autonomous-agent-skills) — has been published separately as a reference implementation in the developer-tooling domain. The skills suite is evidence that the principles work in practice; it is not the proof of the principles themselves.

## Read in this order

| File | What it does | Time |
|---|---|---|
| [PROBLEM.md](./PROBLEM.md) | Names the two problems and defines delegability as the connecting discipline. Start here. | 60 sec (Digest) or 15 min (full) |
| [PRINCIPLES.md](./PRINCIPLES.md) | Three principles that solve the problems, plus the ARF operational definition. | 60 sec (Digest) or 20 min (full) |
| [PROOF.md](./PROOF.md) | How to test conformance for each principle — domain-agnostic protocol, plus reference evidence from one implementation. | 5 min |

## License

Philosophy and documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Author: Nils Wendelboe Holmager | April 2026
