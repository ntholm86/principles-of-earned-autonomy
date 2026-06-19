# AAS-1 Public Comment: Reasoning Traces in Provenance and Reproducibility

**Date:** 2026-06-19  
**Author:** Nils Wendelboe Holmager  
**Comment on:** AAS-1 Specification v0.1 (May 2026)  
**Assertions addressed:** Provenance (9), Reproducibility (10)  
**Status:** DRAFT - Not yet submitted

---

## Summary

This comment proposes two clarifications to AAS-1 v0.2:

1. **Provenance** should explicitly include reasoning traces - the intermediate deliberation an agent produces before taking action.
2. **Reproducibility** should clarify its scope for non-deterministic models, where exact output reproduction is impossible but reasoning consistency is verifiable.

These proposals emerge from 2+ months of implementation experience building agent audit trails. The recurring finding: when diagnosing agent failures, the reasoning trace was diagnostic; the action record alone was not.

---

## 1. Provenance Should Include Reasoning Traces

### The Gap

AAS-1 v0.1's Provenance assertion (§6.9) requires capturing:
- Model identity
- Tools invoked
- Prompt context
- Data sources

This captures **what the agent used** but not **how the agent deliberated**. For agents that produce multi-step reasoning before acting (chain-of-thought, planning, tool orchestration), the reasoning trace is the most diagnostic provenance available.

### Proposed Change

**Current:** "Model, tools, prompt context and data sources captured."

**Proposed:** "Model, tools, prompt context, data sources, and reasoning traces (where produced) captured. Reasoning traces should be captured contemporaneously with execution."

### Rationale

1. **Diagnostic value.** When an agent takes a harmful action, the reasoning trace reveals *why*. Model identity and prompt context reveal what was available; the reasoning trace reveals what the agent did with it.

2. **Audit relevance.** The AAS-1 Audit Manual (§7.9) asks auditors to evaluate "whether the model, tools, prompt context and data sources are adequately captured." If the agent deliberated before acting, the deliberation is the most relevant context.

3. **Industry trend.** Major LLM providers now expose reasoning traces (OpenAI's `reasoning_effort`, Anthropic's extended thinking). AAS-1 should specify how these traces fit into the evidentiary record.

### Evidence from Implementation

Over 123 trail entries across 2+ months, I found that five incident classes were diagnosed primarily from the reasoning trace, not the action record:

- **Migration defects** - The action showed "file changed." The reasoning showed the agent misunderstood the migration scope.
- **Over-strong specifications** - The action showed "spec written." The reasoning showed the agent didn't consider implementation constraints.
- **Encoding failures** - The action showed "corrupted output." The reasoning showed the agent chose the wrong encoding path.
- **Premature convergence** - The action showed "declared done." The reasoning showed the agent pattern-matched instead of examining.
- **Narrow focus** - The action showed "15 documentation fixes." The reasoning showed the agent was stuck in a local optimum.

In each case, an auditor seeing only the Class A action record would miss what actually went wrong.

This implementation experience comes from work on a governance framework called Principles of Earned Autonomy (PEA). The trail format I developed there captures reasoning traces as a structured part of every entry — interpretation of the ask, examination, decision rationale, action, and reflection. It's one approach that works; I offer it as a reference implementation if useful. A full mapping of how this trail format relates to AAS-1's assertions is published at [AAS-1-MAPPING.md](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/docs/AAS-1-MAPPING.md), and the deployment evidence is documented at [DEPLOYMENT-CASE-STUDY.md](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/docs/DEPLOYMENT-CASE-STUDY.md).

---

## 2. Reproducibility for Non-Deterministic Models

### The Gap

AAS-1 v0.1's Reproducibility assertion (§6.10) requires "sufficient state to permit re-derivation."

For deterministic systems, this is clear: capture inputs, replay, verify outputs match.

For non-deterministic LLMs, this is unclear. Even with identical inputs, the model may produce different outputs on replay. What does "re-derivation" mean when exact reproduction is impossible?

### Proposed Change

**Current:** "Sufficient state to permit re-derivation."

**Proposed:** "Sufficient state to permit re-derivation. For non-deterministic models, this means an auditor can verify that the recorded reasoning is consistent with the recorded inputs; exact output reproducibility is not required."

### Rationale

Two levels of reproducibility exist:

1. **Output reproducibility:** Given the same inputs, the agent produces the same output. (Achievable for deterministic models; not achievable for most LLMs.)

2. **Reasoning reproducibility:** Given the same inputs, an auditor can verify that the agent's recorded reasoning is consistent with the inputs. (Achievable for all models that expose reasoning traces.)

For non-deterministic models, *reasoning reproducibility* is the appropriate standard. The auditor can verify the reasoning was grounded in the recorded inputs, even if the exact output might vary on replay.

### A Potential Thirteenth Assertion: Reasoning Quality

For cases where reproducibility isn't achievable, there's a deeper question: did the agent actually reason about *this* situation, or did it apply a template?

I'd like to propose this as worth considering for AAS-1's assertion catalogue: **Reasoning Quality** — the agent's response demonstrates situated reasoning rather than template application.

One methodology for testing this (Autonomous Reasoning Fidelity probes, which I've been developing as part of PEA) uses paired cases with a single material fact changed. A reasoning agent diverges when the material fact differs; a pattern-matching agent produces the same response regardless. This is testable even for non-deterministic models because it measures *divergence*, not *reproduction*.

I'm uncertain whether this fits AAS-1's per-record model — it's a property that emerges from probe pairs, not something visible in a single Class A record. But the underlying question ("did the agent reason or pattern-match?") seems relevant to audit. If the working group sees a path to formalizing this, the [ARF specification](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/probes/ARF-SPEC.md) is published under CC0.

---

## 3. Proposed Audit Manual Guidance

If reasoning traces become part of Provenance, the Audit Manual (§7.9) should add evaluation guidance:

- Is the trace captured at execution time (not reconstructed post-hoc)?
- Is the trace consistent with the recorded inputs?
- Does the trace explain the action taken?

These questions parallel the existing Provenance procedures but apply them to the reasoning layer.

---

## References

- [AAS-1 Specification v0.1](https://aas-1.org/AAS-1_Specification_v0_1.pdf)
- [AAS-1 Audit Manual v0.1](https://aas-1.org/AAS-1_Audit_Manual_v0_1.pdf)

### Supporting Materials (from this comment's author)

These are offered as evidence and reference implementations, not as requests for adoption:

- [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy) — The governance framework that led to these proposals
- [AAS-1 Assertion Mapping](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/docs/AAS-1-MAPPING.md) — Field-by-field mapping of PEA's trail format to AAS-1's twelve assertions
- [Deployment Case Study](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/docs/DEPLOYMENT-CASE-STUDY.md) — 123+ trail entries, five incident classes, cross-model validation evidence
- [ARF Specification](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/probes/ARF-SPEC.md) — Autonomous Reasoning Fidelity probe methodology (CC0)
