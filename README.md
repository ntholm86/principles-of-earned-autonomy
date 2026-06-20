# Principles of Earned Autonomy

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19732890.svg)](https://doi.org/10.5281/zenodo.19732890)

**If an autonomous action is not auditable, it is broken. Not risky, broken.**

The correct response to broken is revocation, not tolerance. Autonomy that cannot be traced cannot be trusted. Trust that cannot be earned cannot be revoked.

This repository is the framework that makes that a requirement rather than a preference.

Restriction-first AI governance treats AI capability as the hazard and bounds it. This framework diagnoses the hazard differently: actors cause harm when they lack sufficient context to reason well about consequences, and when that reasoning cannot be checked by those responsible for the outcome — a structural property established across cognitive science and AI research. AI agents are the first operational instance; the architectural principles are general. The three principles address both conditions directly:

1. **Commander's Intent**: define the destination, never the route. The agent must interpret and adapt rather than execute a checklist.
2. **Observable Autonomy**: every autonomous operation produces a visible, auditable trail. If it cannot be seen, it should not be running.
3. **Convergence Is Silence**: the loop has converged when independent evaluators find nothing left to change. Silence is a stopping signal, not a correctness guarantee.

The claimed contribution here is not the isolated claim that reasoning matters, or that self-report is unreliable. It is the synthesis as a proposed governance framework: combining Commander's Intent, Observable Autonomy, and Convergence Is Silence into a discipline for earned, observable, revocable delegation. This is a step in that direction, not a claim that ARF or this framework solves every downstream AI-safety problem.

Autonomous Reasoning Fidelity (ARF) is the proposed target property the framework is designed to surface: the external signal that genuine, situated reasoning is both occurring and visible. Its probe method is defined here; formal validation remains future work. No tool prescriptions; any stack can conform.

The general empirical premise is grounded by the literature cited in [PRINCIPLES.md](./PRINCIPLES.md): self-narration and weak self-correction are not reliable evidence of reasoning. The framework's principles are architectural responses to that premise.

Two conformance examples have been published separately as reference implementations. The [Principles of Earned Autonomy - Skills Suite](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite) is a reference implementation in the developer-tooling domain, exercising the three principles in a self-improving skill set evaluated by diverse model families. The [LLM Harness Protocol](https://github.com/ntholm86/llm-harness-proxy) is a reference implementation of the structural layer the framework requires: a tamper-evident, hash-chained, fail-closed MITM proxy that captures LLM reasoning and tool calls outside the audited model's authorship, across OpenAI, Anthropic, and Gemini APIs. Together they cover the framework's two implementation surfaces - the principles applied to an artifact (skills suite) and the structural mechanism that makes Principle 2 enforceable independent of the audited agent's compliance (harness). Both provide bounded reference evidence; public evidence travels with the released documents and the reference implementation materials they cite.

## Read in this order

The core argumentative line is: problem -> principles -> bounded reference evidence.

| File | What it does | Time |
|---|---|---|
| [PROBLEM.md](./PROBLEM.md) | Names the two problems and defines delegability as the connecting discipline. Start here. | 60 sec (Digest) or 15 min (full) |
| [PRINCIPLES.md](./PRINCIPLES.md) | Three principles that solve the problems, plus the ARF operational definition. | 60 sec (Digest) or 20 min (full) |
| [PROOF.md](./PROOF.md) | Conformance tests for each principle and for ARF, plus bounded empirical evidence from two reference implementations. | 5 min |

Then, if you want the formative case and external corroboration that motivated the structural constraints, read [EMPIRICAL_EVIDENCE.md](./EMPIRICAL_EVIDENCE.md). It is background material, not part of the core evidentiary line.

## License

Philosophy and documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Author: Nils Wendelboe Holmager | April 2026
