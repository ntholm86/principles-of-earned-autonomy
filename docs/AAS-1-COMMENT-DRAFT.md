# AAS-1 Public Comment: Reasoning Provenance and Quality

**Date:** 2026-06-19  
**Author:** Nils Wendelboe Holmager  
**Comment on:** AAS-1 Specification v0.1 (May 2026)  
**Assertions addressed:** Provenance (9), Reproducibility (10)  
**Status:** DRAFT — Not yet submitted

---

## Summary

This comment proposes that AAS-1 v0.2 explicitly address **reasoning traces** as a component of the Provenance assertion, and clarify the Reproducibility assertion's scope when models are non-deterministic. It offers the Principles of Earned Autonomy (PEA) trail format and Autonomous Reasoning Fidelity (ARF) probe methodology as reference approaches, with deployment evidence from a 2+ month production use case.

---

## 1. The Gap: Reasoning Provenance

AAS-1 v0.1's Provenance assertion (§6.9) requires capturing:
- Model identity
- Tools invoked
- Prompt context
- Data sources

This captures **what the agent used** but not **how the agent deliberated**. For agents that produce multi-step reasoning before acting (chain-of-thought, planning, tool orchestration), the reasoning trace is the most diagnostic provenance available.

### Proposed Clarification

Extend the Provenance assertion definition to explicitly include:

> **Reasoning trace:** If the agent produces intermediate reasoning (deliberation, planning, chain-of-thought) before taking the recorded action, that reasoning should be captured as part of provenance. The trace should be captured contemporaneously with execution, not reconstructed post-hoc.

### Rationale

1. **Diagnostic value:** When an agent takes a harmful action, the reasoning trace reveals *why*. Model identity and prompt context reveal what was available; the reasoning trace reveals what the agent did with it.

2. **Audit relevance:** The AAS-1 Audit Manual (§7.9) asks auditors to evaluate "whether the model, tools, prompt context and data sources are adequately captured." If the agent deliberated before acting, the deliberation is the most relevant context for the auditor.

3. **Industry trend:** Major LLM providers now expose reasoning traces (OpenAI's `reasoning_effort`, Anthropic's extended thinking). AAS-1 should anticipate that these traces will be available and specify how they fit into the evidentiary record.

### Implementation Note

The Principles of Earned Autonomy (PEA) trail format ([specification](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite)) captures reasoning traces as part of every trail entry:

```
### Interpretation of the ask
[Agent's understanding of the goal]

### Examination  
[What the agent observed and how it reasoned about it]

### Decision
[!DECISION] [What the agent chose to do and why]

### Action
[What was done]

### Reflection
[!REALIZATION] [What the agent learned]
```

Each section is written at execution time, not reconstructed. The format is human-readable (Markdown) while supporting machine parsing (marker extraction).

---

## 2. The Gap: Non-Deterministic Reproducibility

AAS-1 v0.1's Reproducibility assertion (§6.10) requires "sufficient state to permit re-derivation."

For deterministic systems, this is clear: capture inputs, replay, verify outputs match.

For non-deterministic LLMs, this is unclear. Even with identical inputs, the model may produce different outputs on replay. What does "re-derivation" mean when exact reproduction is impossible?

### Proposed Clarification

Distinguish two levels of reproducibility:

1. **Output reproducibility:** Given the same inputs, the agent produces the same output. (Achievable for deterministic models; not achievable for most LLMs.)

2. **Reasoning reproducibility:** Given the same inputs, an auditor can verify that the agent's recorded reasoning is consistent with the inputs. (Achievable for all models that expose reasoning traces.)

The Reproducibility assertion should clarify that for non-deterministic models, *reasoning reproducibility* is the appropriate standard — the auditor can verify the reasoning was grounded in the recorded inputs, even if the exact output might vary on replay.

### A Stronger Test: Reasoning Quality

PEA's Autonomous Reasoning Fidelity (ARF) probes offer a complementary approach that doesn't depend on replay:

> ARF probes test whether an agent is genuinely reasoning about the specific situation it encounters, or pattern-matching from a template.

The methodology uses paired cases:
- **Case A:** A situation with a specific material fact
- **Case B:** The same situation with that fact changed

A reasoning agent should produce different responses when the material fact differs. A pattern-matching agent will produce the same response regardless.

**Key insight:** ARF doesn't require reproducibility. It requires *divergence* on materially different inputs. This is a testable property even for non-deterministic models.

ARF is not proposed as an AAS-1 assertion (it's a methodology, not a per-record property). But it addresses the underlying concern: how do we verify reasoning quality when we can't rely on exact reproducibility?

The ARF specification is published at [github.com/ntholm86/principles-of-earned-autonomy](https://github.com/ntholm86/principles-of-earned-autonomy) under CC0.

---

## 3. Real-World Use Case: Skills-Suite Deployment

AAS-1 v0.1 asks for "real-world engagement use cases." Here is one.

### Deployment Facts

- **System:** Principles of Earned Autonomy Skills Suite
- **Period:** April 2026 – present (ongoing)
- **Trail entries:** 123+ as of 2026-05-23
- **Markers recorded:** 162 ([!REALIZATION] and [!REVERSAL])
- **Model families validated:** 3 (Anthropic/Claude, Google/Gemini, OpenAI/GPT)
- **License:** MIT (code), CC BY-SA 4.0 (documentation)

### What the Trail Captures

Each trail entry records:
- **Date, target, operator, model identity** (AAS-1 Class A equivalent)
- **Interpretation of the ask** (reasoning provenance)
- **Examination and decision** (reasoning trace with decision markers)
- **Action and verification** (what was done, how it was verified)
- **Reflection** (what was learned, marked as `[!REALIZATION]`)

The trail is append-only, hash-referenced (via git commit SHAs), and cross-model validated (three model families declared "silence" on the same target).

### Incidents and Resolution

The deployment produced 5+ incident classes that were diagnosed from the trail:

1. **Splice-append defects** — Migration left duplicate content; caught by fresh-session evaluators before convergence
2. **Enforcement over-reaches** — Specs written too strongly; corrected with explicit era-boundary policies
3. **Mojibake corruption** — PowerShell encoding failure; diagnosed from corrupted trail entry
4. **Optimistic convergence prediction** — Agents predicted "silence" too early; pattern visible across trail entries
5. **Greppable fix bias** — Loop spent 15 runs on documentation echoes; diagnosed by arc-level trail read

In each case, the reasoning trace (not just the action record) was diagnostic. Without "interpretation of the ask" and "examination," the auditor would see only that a file changed, not why.

### Relevance to AAS-1

This deployment demonstrates:
- **Provenance** includes reasoning traces, and those traces are diagnostic
- **Reproducibility** across model families is achievable for reasoning patterns (even when exact outputs differ)
- **Cross-model evaluation** as a governance mechanism (three families reaching the same verdict)

The full deployment case study is published at [github.com/ntholm86/principles-of-earned-autonomy/docs/DEPLOYMENT-CASE-STUDY.md](https://github.com/ntholm86/principles-of-earned-autonomy).

---

## 4. Proposed Changes to AAS-1 v0.2

### Provenance (Assertion 9)

**Current:** "Model, tools, prompt context and data sources captured."

**Proposed:** "Model, tools, prompt context, data sources, and reasoning traces (where produced) captured. Reasoning traces should be captured contemporaneously with execution."

### Reproducibility (Assertion 10)

**Current:** "Sufficient state to permit re-derivation."

**Proposed:** "Sufficient state to permit re-derivation. For non-deterministic models, this means an auditor can verify that the recorded reasoning is consistent with the recorded inputs; exact output reproducibility is not required."

### Audit Manual (§7.9 Provenance procedures)

Add guidance on evaluating reasoning traces:
- Is the trace captured at execution time (not reconstructed)?
- Is the trace consistent with the recorded inputs?
- Does the trace explain the action taken?

---

## 5. Summary

| Proposal | Section | Type |
|----------|---------|------|
| Extend Provenance to include reasoning traces | 1 | Assertion clarification |
| Clarify Reproducibility for non-deterministic models | 2 | Assertion clarification |
| Offer PEA trail format as reference | 1, 3 | Reference implementation |
| Offer ARF methodology for reasoning quality | 2 | Complementary approach |
| Skills-suite deployment as use case | 3 | Real-world evidence |

All materials referenced are published under open licenses (CC0 or CC BY-SA 4.0) and available for AAS-1 to incorporate or adapt.

---

## References

- [AAS-1 Specification v0.1](https://aas-1.org/AAS-1_Specification_v0_1.pdf)
- [Principles of Earned Autonomy](https://github.com/ntholm86/principles-of-earned-autonomy)
- [PEA Skills Suite](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite)
- [ARF-SPEC.md](https://github.com/ntholm86/principles-of-earned-autonomy/probes/ARF-SPEC.md)
- [Deployment Case Study](https://github.com/ntholm86/principles-of-earned-autonomy/docs/DEPLOYMENT-CASE-STUDY.md)
- [AAS-1 Mapping](https://github.com/ntholm86/principles-of-earned-autonomy/docs/AAS-1-MAPPING.md)
