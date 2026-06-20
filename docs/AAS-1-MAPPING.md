# Principles of Earned Autonomy → AAS-1 Assertion Mapping

**Version:** 1.0.0  
**Date:** 2026-06-19  
**PEA Version:** 2.3.0  
**AAS-1 Version:** v0.1 (May 2026 draft)

---

## Overview

This document maps the three architectural principles of Principles of Earned Autonomy (PEA) to the twelve standard assertions defined in AAS-1 (Agent Auditability Standard). The purpose is to show:

1. Which AAS-1 assertions a PEA-compliant system satisfies by construction
2. Which require additional implementation beyond PEA's core requirements
3. Where PEA goes beyond what AAS-1 measures

**Summary:** Observable Autonomy is the workhorse — it enables 9 of 12 assertions. Commander's Intent maps to Authorization. Convergence Is Silence operates at a level AAS-1 doesn't address (arc-level evaluation stability, not per-record properties).

---

## The Three Principles

| Principle | Definition | Operational Effect |
|-----------|------------|-------------------|
| **Commander's Intent** | Define the destination, never the route. The agent interprets and adapts; it does not execute a checklist. | The agent operates within bounded authority toward stated goals. Delegation is explicit. |
| **Observable Autonomy** | Every autonomous operation produces a captured, auditable trail that the agent cannot retroactively author. | Complete, tamper-evident records of all agent activity. The foundation for external audit. |
| **Convergence Is Silence** | The work is done when diverse independent evaluators find nothing left to change. | Quality is measured by evaluation stability, not self-assessment. |

---

## AAS-1's Twelve Assertions

AAS-1 defines seven classical assertions (adapted from ISA 315/330, AICPA AU-C, ISAE 3000) and five agent-specific assertions:

### Classical Assertions

| # | Assertion | Definition |
|---|-----------|------------|
| 1 | **Existence** | The recorded action actually took place |
| 2 | **Completeness** | All relevant actions in scope are recorded |
| 3 | **Accuracy** | Inputs and outputs are faithfully captured |
| 4 | **Authorization** | The agent acted within delegated authority |
| 5 | **Cutoff** | Recorded in the correct period |
| 6 | **Classification** | Correctly categorised by action type |
| 7 | **Presentation** | Records are presented and described accurately |

### Agent-Specific Assertions

| # | Assertion | Definition |
|---|-----------|------------|
| 8 | **Identity** | The recorded actor is the agent of record (AIS-1 binding) |
| 9 | **Provenance** | Model, tools, prompt context and data sources captured |
| 10 | **Reproducibility** | Sufficient state to permit re-derivation |
| 11 | **Policy Compliance** | Applicable policies and compliance result recorded |
| 12 | **Independence** | Agent action separated from operator override |

---

## Mapping: PEA Principles → AAS-1 Assertions

### Observable Autonomy → 9 Assertions

Observable Autonomy is PEA's enforcement mechanism. It requires that every autonomous operation produce a captured, auditable trail that the agent cannot retroactively author.

| AAS-1 Assertion | How Observable Autonomy Satisfies It |
|-----------------|-------------------------------------|
| **Existence** | ✅ **Satisfied by construction.** The trail captures what actually happened. The agent cannot fabricate actions that didn't occur because the trail is written contemporaneously with execution. |
| **Completeness** | ✅ **Satisfied by construction.** "Every autonomous operation" is the requirement. Gaps in the trail are visible (missing sequence numbers, broken hash chains). |
| **Accuracy** | ✅ **Satisfied by construction.** Inputs and outputs are captured at execution time, before the agent can modify them. Hash-chaining prevents post-hoc alteration. |
| **Cutoff** | ✅ **Satisfied by construction.** Timestamps are recorded at execution time. The hash chain makes backdating detectable. |
| **Presentation** | ✅ **Satisfied by construction.** The trail format is specified (JSONL, defined schema). Records are machine-readable and human-inspectable. |
| **Provenance** | ✅ **Satisfied by construction.** The trail captures model identity, tool invocations, and input context. This is required by Observable Autonomy's "sufficient for reconstruction" standard. |
| **Reproducibility** | ⚠️ **Partially satisfied.** Observable Autonomy captures the input state. Whether the output is reproducible depends on model determinism (which PEA does not control). See "ARF and Reproducibility" below. |
| **Identity** | ⚠️ **Requires implementation.** Observable Autonomy requires knowing *what* happened; AAS-1's Identity assertion requires cryptographic proof of *who* (AIS-1 binding). PEA is agnostic to identity layer. |
| **Independence** | ✅ **Satisfied by construction.** The trail distinguishes agent actions from operator overrides. Observable Autonomy requires that human interventions be recorded as such, not hidden. |

### Commander's Intent → Authorization

Commander's Intent requires that the agent operate within bounded authority toward stated goals. This maps directly to AAS-1's Authorization assertion.

| AAS-1 Assertion | How Commander's Intent Satisfies It |
|-----------------|-------------------------------------|
| **Authorization** | ✅ **Conceptually aligned.** Commander's Intent defines the destination (what the agent is authorized to do) without specifying the route (how). An agent acting outside its Intent is unauthorized by definition. |

**Implementation note:** Commander's Intent is a governance principle, not a record format. To satisfy AAS-1's Authorization assertion in practice, a PEA-compliant system must:

1. Record the Intent (destination, constraints) in the trail
2. Record per-action justification linking the action to the Intent
3. Flag actions that may exceed the Intent for human review

The `.trail/destination.md` artifact in PEA implementations serves this role — it's the operator-held authority boundary the agent operates within.

### Commander's Intent → Classification

Commander's Intent also influences Classification, though indirectly:

| AAS-1 Assertion | How Commander's Intent Relates |
|-----------------|-------------------------------|
| **Classification** | ⚠️ **Indirectly supported.** The Intent shapes what action types are in scope. However, AAS-1's Classification requires explicit action typing (a controlled vocabulary). PEA does not mandate this — it's implementation-dependent. |

### Convergence Is Silence → (No Direct Mapping)

Convergence Is Silence operates at a level AAS-1 doesn't address. AAS-1 assertions are per-record properties; Convergence Is Silence is an arc-level property about when evaluation findings stabilize.

| AAS-1 Assertion | Convergence Is Silence |
|-----------------|------------------------|
| **Policy Compliance** | ⚠️ **Orthogonal.** AAS-1 asks: "Did the agent record which policies applied and whether it complied?" Convergence asks: "Did independent evaluators stop finding issues?" These are different questions. A system can have perfect Policy Compliance records and still fail Convergence (if evaluators keep finding new problems). |

**What Convergence adds beyond AAS-1:**

AAS-1 provides the evidentiary foundation for audit. Convergence provides the termination condition for iterative improvement. They are complementary:

- AAS-1: "Here is the evidence of what the agent did."
- Convergence: "Here is how we know the agent's work is done."

A PEA-compliant system uses AAS-1-compatible records (via Observable Autonomy) and then applies Convergence as the meta-criterion for declaring stability.

---

## Mapping Summary Table

| AAS-1 Assertion | PEA Principle | Coverage |
|-----------------|---------------|----------|
| 1. Existence | Observable Autonomy | ✅ Full |
| 2. Completeness | Observable Autonomy | ✅ Full |
| 3. Accuracy | Observable Autonomy | ✅ Full |
| 4. Authorization | Commander's Intent | ✅ Conceptual (needs implementation) |
| 5. Cutoff | Observable Autonomy | ✅ Full |
| 6. Classification | Commander's Intent | ⚠️ Partial (action typing not mandated) |
| 7. Presentation | Observable Autonomy | ✅ Full |
| 8. Identity | Observable Autonomy | ⚠️ Partial (needs AIS-1 binding) |
| 9. Provenance | Observable Autonomy | ✅ Full |
| 10. Reproducibility | Observable Autonomy | ⚠️ Partial (model determinism) |
| 11. Policy Compliance | (orthogonal) | ⚠️ Not addressed directly |
| 12. Independence | Observable Autonomy | ✅ Full |

**Legend:**
- ✅ Full — PEA satisfies the assertion by construction
- ⚠️ Partial — PEA enables but does not guarantee the assertion
- ❌ Not addressed — PEA does not speak to this assertion

---

## ARF and Reproducibility

AAS-1's Reproducibility assertion asks: "Is there sufficient state to permit re-derivation?"

This is exactly what Autonomous Reasoning Fidelity (ARF) probes measure — but with a twist. ARF doesn't ask "can we reproduce the exact output?" (which depends on model determinism). ARF asks "can we verify that the reasoning was situated rather than templated?"

| Concept | AAS-1 Reproducibility | ARF |
|---------|----------------------|-----|
| Question | Can we get the same output from the same input? | Did the agent reason about *this* situation or apply a template? |
| Metric | Deterministic replay (if possible) | Divergence on materially different cases |
| Evidence | Input hash, model ID, tool state | Paired probes with controlled variation |

**Relationship:** ARF is a *stronger* test than mere reproducibility. A reproducible agent that pattern-matches will produce the same wrong answer twice. An ARF-passing agent will produce different answers when the situation materially differs.

A PEA-compliant system with ARF probes provides evidence for:
- **Reproducibility** (the input state is captured)
- **Reasoning quality** (the agent actually used that input state, not a template)

---

## What PEA Adds Beyond AAS-1

AAS-1 is an evidentiary standard — it defines what records look like and how auditors evaluate them. PEA is a governance architecture — it defines how agents should be constrained and how autonomy should be earned.

| Dimension | AAS-1 | PEA |
|-----------|-------|-----|
| **Scope** | Per-record evidence | System-level architecture |
| **Question answered** | "Is this record auditable?" | "Should this agent have this autonomy?" |
| **Quality metric** | 12 assertions per record | Convergence across evaluators |
| **Reasoning quality** | Provenance (what model, what input) | ARF (did the model actually reason?) |
| **Termination** | Audit opinion on record population | Silence from independent evaluators |

**PEA concepts with no AAS-1 equivalent:**

1. **Earned Autonomy** — The idea that autonomy is granted based on demonstrated reasoning quality, not assigned by role or capability tier.

2. **Convergence as governance signal** — Using evaluation stability (not self-assessment or capability metrics) to determine when an agent has earned fuller autonomy.

3. **ARF as a probe-based metric** — Measuring reasoning quality via paired scenarios that distinguish situated reasoning from template application.

---

## Implementation Path

For a PEA-compliant system to achieve full AAS-1 compatibility:

### Already Satisfied (via Observable Autonomy + Commander's Intent)

- Existence, Completeness, Accuracy, Cutoff, Presentation, Provenance, Independence
- Authorization (with explicit Intent recording)

### Requires Additional Implementation

| Assertion | What's Needed |
|-----------|---------------|
| **Classification** | Add action type taxonomy to trail records. The LLM Harness Protocol's [AAT-MAPPING](https://github.com/ntholm86/harness-proxy/blob/master/docs/AAT-MAPPING.md) documents this gap and proposes an inference path. |
| **Identity** | Bind agent identity to AIS-1. This is orthogonal to PEA's principles — PEA is identity-layer agnostic. |
| **Reproducibility** | For deterministic models, capture sufficient state. For non-deterministic models, document the limitation. ARF probes provide evidence of reasoning quality regardless of reproducibility. |
| **Policy Compliance** | Record which policies apply and the compliance result. PEA's `.trail/destination.md` is a partial implementation (it records the Intent boundary) but doesn't capture per-action compliance verdicts. |

---

## References

- [AAS-1 Specification v0.1](https://aas-1.org/AAS-1_Specification_v0_1.pdf)
- [AAS-1 Audit Manual v0.1](https://aas-1.org/AAS-1_Audit_Manual_v0_1.pdf)
- [PEA Manifesto](https://github.com/ntholm86/pea-manifesto)
- [PRINCIPLES.md](../PRINCIPLES.md) — Full statement of PEA's three principles
- [ARF-SPEC.md](../probes/ARF-SPEC.md) — Autonomous Reasoning Fidelity probe specification
- [LLM Harness Protocol AAT Mapping](https://github.com/ntholm86/harness-proxy/blob/master/docs/AAT-MAPPING.md) — Field-level mapping to IETF Agent Audit Trail
