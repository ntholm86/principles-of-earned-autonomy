# Principles of Earned Autonomy

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19732890.svg)](https://doi.org/10.5281/zenodo.19732890)

**If an autonomous action is not auditable, it is broken. Not risky — broken.**

The correct response to broken is revocation, not tolerance. Autonomy that cannot be traced cannot be trusted. Trust that cannot be earned cannot be revoked.

This repository is the framework that makes that a requirement rather than a preference. Three architectural principles. One measurable property. No tool prescriptions — any stack can conform.

1. **Commander's Intent** — define the destination, never the route. The agent must interpret and adapt, not execute a checklist.
2. **Observable Autonomy** — every autonomous operation produces a visible, auditable trail. If it cannot be seen, it should not be running.
3. **Convergence Is Silence** — the work is done when independent evaluators find nothing left to change. Not when a score stops moving.

Most AI governance frameworks treat AI risk as an authority problem — restrict what an AI can decide and do, bound the failure architecturally, and produce safety by subtraction. This framework starts from the opposite premise: AI causes harm when it lacks sufficient context to reason well, not when it has insufficient constraints. The trust instrument is not restriction, and not transparency alone — other frameworks already treat transparency as a complement to restriction. It is demonstrated reasoning quality: an agent with adequate context to understand consequences, whose reasoning is verified as genuine rather than merely visible. ARF measures the reasoning-fidelity component of that quality — whether the reasoning is genuinely situated rather than templated. A more capable agent that passes a reasoning-fidelity check earns more trust, not more constraint.

One conformance example — the [Principles of Earned Autonomy - Skills Suite](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite) — has been published separately as a reference implementation in the developer-tooling domain. The skills suite is evidence that the principles work in practice; it is not the proof of the principles themselves.

## Read in this order

| File | What it does | Time |
|---|---|---|
| [PROBLEM.md](./PROBLEM.md) | Names the two problems and defines delegability as the connecting discipline. Start here. | 60 sec (Digest) or 15 min (full) |
| [PRINCIPLES.md](./PRINCIPLES.md) | Three principles that solve the problems, plus the ARF operational definition. | 60 sec (Digest) or 20 min (full) |
| [PROOF.md](./PROOF.md) | Conformance tests for each principle, plus bounded empirical evidence from one implementation. | 5 min |
| [EMPIRICAL_EVIDENCE.md](./EMPIRICAL_EVIDENCE.md) | Why the principles are structural rather than behavioral — documented evidence that behavioral alignment alone fails under post-hoc rationalization. | 5 min |

## License

Philosophy and documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Author: Nils Wendelboe Holmager | April 2026
