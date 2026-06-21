# Deployment Case Study: Principles of Earned Autonomy Skills Suite

**Version:** 1.0.0  
**Date:** 2026-06-19  
**Deployment Period:** April 2026 – present (ongoing)  
**Subject:** [Principles of Earned Autonomy - Skills Suite](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite)

---

## Executive Summary

The Principles of Earned Autonomy (PEA) framework has been deployed in production since April 2026 via the Skills Suite — a set of five skills (Intent, Improve, Probe, Trail, Retrospect) that operationalize the three PEA principles. This document provides deployment evidence in an incident-narrative format for institutional review.

**Key metrics:**
- **Trail entries:** 123+ (as of 2026-05-23)
- **Markers recorded:** 162 ([!REALIZATION] and [!REVERSAL])
- **Reversal rate:** 7.4% (12 reversals / 150 realizations)
- **Model families validated:** 3 (Anthropic/Claude, Google/Gemini, OpenAI/GPT)
- **Version:** v3.x (major redesign from v2)
- **License:** MIT (skills code), CC BY-SA 4.0 (documentation)

**Deployment targets:**
1. Self-targeting (skills improving themselves) — fully public, trail published
2. External targets (evo, vectorium, leifoglenedk) — trails in respective repos
3. Enterprise deployment — confidential, employer-owned work product

---

## Deployment Setup

### Architecture

The skills-suite implements PEA's three principles as operational mechanisms:

| Principle | Implementation | Artifact |
|-----------|---------------|----------|
| Commander's Intent | Intent skill (step 1 of Improve) + Destination skill | `.acm/destination.md` |
| Observable Autonomy | Trail skill (append-only evidence per run) | `.acm/audit-trail.md` |
| Convergence Is Silence | 3/3 cross-model validation protocol | Chain count in trail entries |

### The Memory Model

The deployment discovered that AI agents' lack of persistent memory is not a bug but an architectural fact. The response is a structured memory layer that survives session resets, context window limits, and model swaps:

- `destination.md` — operator-held destination (stable, operator-written)
- `audit-trail.md` — append-only decision record
- `retrospect.md` — current orientation (synthesized from trail arc)
- `sessions/` — verbatim session transcripts (when captured)

When the model changes (Claude → Gemini → GPT), the next model picks up the same memory layer. The substrate survives the model change.

### Operational Flow

Each Improve run:
1. Reads `destination.md`, `retrospect.md`, `learning.md`, then `audit-trail.md`
2. Examines the target via lenses (Purpose, Inconsistency, Overburden, Waste)
3. Decides: one incremental change, argument for redesign, or silence
4. Acts and verifies
5. Reflects (falsifiable model-claim, named blind spot, imagined-reader pushback)
6. Records entry to `audit-trail.md`

---

## Incident Narratives

### Incident 1: Splice-Append Defects (v3 Migration)

**When:** 2026-04-23 to 2026-04-24  
**Impact:** Three separate occurrences of duplicated content in live files  
**Detection:** Fresh-session evaluators during convergence chain

**What happened:**

The v2→v3 migration moved content to `archive/v2/` but used append-style writes rather than replace-style writes in some files. This left duplicate content in:
1. `PRINCIPLES.md` — caught by GPT-5.4
2. `CHANGELOG.md` — caught by Claude Sonnet 4.6
3. `trail/README.md` — caught by Claude Sonnet 4.6

**How PEA principles applied:**

- **Observable Autonomy:** Each occurrence was recorded in the trail with full context
- **Convergence Is Silence:** The convergence chain correctly prevented ratification — each defect was found before the chain advanced
- **Trail as diagnosis:** The trail entries made the pattern visible across runs

**Resolution:**

Each splice was repaired by the evaluator that found it. After the third occurrence:

> **[!REALIZATION]** "This is the third occurrence of the same splice-append defect class in this repo... The pattern suggests the v2-to-v3 migration used append-style writes rather than replace-style writes. The convergence chain correctly prevented any from being ratified."

**Lesson learned:**

Large structural changes (migrations, renames) create a predictable "echo tail" of inconsistencies. The loop catches them, but expects 3-5 cleanup runs after any major structural change.

---

### Incident 2: Enforcement Over-Reaches

**When:** 2026-05-23  
**Impact:** Two spec constraints stated too strongly, blocking adoption  
**Detection:** Reality exposed them as unimplementable during session

**What happened:**

Two enforcement rules were written at maximum strength:

1. **Forward-only fidelity contract** — required harness-captured transcripts for all entries
2. **Harness-boundary mandate** — required verbatim harness extraction

Both had to be softened when no available harness could satisfy them.

**How PEA principles applied:**

- **Observable Autonomy:** The softening was published as explicit policy with a named era boundary, not quietly weakened
- **Trail as evidence:** Both over-reaches and their corrections are recorded in the same session

**Resolution:**

Established an operational rule:

> "Enforcement softenings must be published as explicit policy with a named era boundary. Do not quietly weaken a spec or verifier constraint. Name the era before which the old rule does not apply, document the reason, and keep the aspiration visible as the highest-trust tier when conditions allow it."

**Lesson learned:**

Specs written ahead of implementation will be over-strong. The healthy resolution: acknowledge the ideal, name the era boundary, keep the aspiration visible.

---

### Incident 3: PowerShell Mojibake

**When:** 2026-04-24  
**Impact:** Trail entry corrupted by encoding failure  
**Detection:** Operator spotted visible damage immediately

**What happened:**

An agent composed a trail entry using a PowerShell here-string. PowerShell consumed every backtick as an escape character:
- `` `t `` became a tab
- `` `a `` became BEL (audible bell)
- All inline-code backticks were stripped

> **[!REALIZATION]** "My first attempt to append this entry corrupted itself... Lesson: never compose markdown trail entries through PowerShell here-strings; the metasyntax overlap is a footgun."

**How PEA principles applied:**

- **Observable Autonomy:** The corruption was detected because the trail is inspectable
- **Trail as diagnosis:** The incident was recorded, enabling the pattern to be avoided

**Resolution:**

- Rewrote using Python script with no escape-character collisions
- Added operational rule: "When writing non-ASCII content to disk in PowerShell, use explicit UTF-8 encoding"
- Enhanced `verify.py` to detect mojibake patterns

**Lesson learned:**

PowerShell 5.1's default encoding (Windows-1252) and escape character handling are incompatible with markdown trail content. Use Python or explicit UTF-8 encoding.

---

### Incident 4: Optimistic Convergence Prediction

**When:** Runs 49, 50, 53 (2026-05-01)  
**Impact:** False predictions that "next run is silence candidate"  
**Detection:** Pattern emerged across multiple false positives

**What happened:**

Three consecutive runs predicted they were the "first silence candidate." Each was wrong — the next run found more defects.

> **[!REALIZATION]** "The loop's intuition about when convergence is near is systematically optimistic. The pattern is not 'the loop is failing' — there are real things to find each run — the pattern is that *the agent consistently mistakes the absence of a known defect class for the absence of all defects*. The next-silence prediction should be retired or at least demoted from a forecast to a guess."

**How PEA principles applied:**

- **Convergence Is Silence:** The protocol worked — each false positive was caught by the next run
- **Trail as evidence:** The pattern was visible because predictions were recorded

**Resolution:**

The "next-silence prediction" was demoted from forecast to guess. The trail now records it as a speculation, not a commitment.

**Lesson learned:**

Agents are systematically overconfident about convergence. The convergence chain (requiring 3 independent evaluators to all find nothing) compensates for this bias.

---

### Incident 5: Greppable Fix Bias

**When:** Runs 47-63 (2026-05-01)  
**Impact:** Loop spent 15 runs on echo cleanup, one structural change came from operator  
**Detection:** Retrospect arc-read

**What happened:**

After the v3.8.0 reflection rewrite (a design-level change), the loop spent the next 8 runs fixing documentation echoes of that change. Each echo was real and the loop caught it correctly. But:

> **[!REALIZATION]** "Without operator intervention, this loop converges quickly to mechanical defects and slowly or never to design-level defects. That is a structural property of *this target's loop*, not a defect — but it is worth knowing."

**How PEA principles applied:**

- **Observable Autonomy:** The pattern was visible in the trail
- **Retrospect:** The arc-read surfaced what individual runs couldn't see

**Resolution:**

Acknowledged as a boundary condition: the loop finds what can be found by reading files; it cannot find behavioral improvements that require user feedback from real use.

**Lesson learned:**

Autonomous loops are good at greppable inconsistencies, poor at design-level improvements. Operator intervention remains necessary for structural redesign.

---

## Cross-Model Validation Evidence

The deployment validated PEA's Convergence Is Silence principle across three model families:

| Run | Model Family | Finding | Trail Entry |
|-----|--------------|---------|-------------|
| v3-silence-1 | Anthropic/Claude | Silence | 2026-04-24 |
| v3-silence-2 | Google/Gemini | Silence | 2026-04-24 |
| v3-silence-3 | OpenAI/GPT | Silence | 2026-04-24 |

After achieving 3/3 convergence, a cross-layer coherence evaluation confirmed the skills were consistent with the upstream principles.

**Key validation moment:**

When Gemini (run 56) was introduced to the v3.8.0 reflection format for the first time:

> **[!REALIZATION]** "The new v3.8.0 reflection format successfully crosses model families. Gemini natively adopted the tripartite structure (claim, blind spot, pushback) without falling back into checklist-style summaries."

This confirmed the reflection mechanism isn't Anthropic-specific — it transfers to other model families.

---

## Enterprise Deployment

In addition to the self-targeting deployment, the skills-suite was used in a real enterprise delivery context:

> "I used this skillset in a real enterprise delivery context on a confidential production system with high architectural and delivery complexity: multi-tenant cloud services, domain-driven boundaries across multiple microservices, cross-platform requirements, and fully automated CI/CD. A scope estimated internally as a large T-shirt-size effort was completed in 3 days. The full trail exists but is employer-owned professional work product covered by intellectual property and confidentiality obligations, so it cannot be published here."
>
> — POSITION.md, Section "What the runs are showing"

This deployment provides additional evidence that the framework operates on real production systems, not just self-referential exercises. The constraint is legal (employer IP/confidentiality), not technical.

---

## Operational Rules Established

The deployment produced explicit operational rules, recorded in `.acm/retrospect.md`:

1. **Every spec change must be paired with enforcement in the same session.** Prevents "spec written, enforcement deferred" failures.

2. **Mark `[!REVERSAL]` when the iteration backs out of a planned step.** Calibrates the reversal/realization ratio as a health metric.

3. **When writing non-ASCII content to disk in PowerShell, use explicit UTF-8 encoding.** Prevents mojibake from PS5 default encoding.

4. **Enforcement softenings must be published as explicit policy with a named era boundary.** Maintains honesty when specs are ahead of implementation.

5. **When running Retrospect, regenerate derived artifacts before forming arc-claims.** Prevents stale-data reasoning errors.

---

## Metrics Summary

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Trail entries | 123+ | Active deployment with substantial history |
| Reversal rate | 7.4% | Honest — reversals are recorded, not hidden |
| Model families | 3 | Cross-model validation achieved |
| Incident classes | 5+ | Real incidents encountered and resolved |
| Enterprise deployment | 1 | Production use beyond self-targeting |

---

## Conclusion

The Skills Suite deployment demonstrates that PEA's three principles are operationally viable:

1. **Commander's Intent** — Agents interpret destination, not checklists. The Destination skill surfaces latent operator intent.

2. **Observable Autonomy** — Every run produces a trail entry. Incidents are diagnosed from the trail. Patterns emerge across runs.

3. **Convergence Is Silence** — The 3/3 cross-model protocol catches defects that single-model evaluation misses. Optimistic convergence predictions are compensated by requiring independent validation.

The deployment also established boundaries:

- **The loop is good at greppable defects, poor at design-level improvements.** Operator intervention remains necessary for structural redesign.
- **Specs written ahead of implementation will be over-strong.** Era boundaries and explicit softening policies handle this gracefully.
- **The memory model solves cross-session continuity.** Model changes don't break the work.

The full trail is published at the [skills-suite repository](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite). The enterprise deployment provides additional production evidence under confidentiality constraints.

---

## References

- [Skills Suite Repository](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite)
- [POSITION.md](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite/blob/main/POSITION.md) — Stance document with falsification criteria
- [PEA Manifesto](https://github.com/ntholm86/principles-of-earned-autonomy)
- [AAS-1 Mapping](./AAS-1-MAPPING.md) — How PEA principles map to audit assertions
- [LLM Harness Protocol](https://github.com/ntholm86/llm-harness-proxy) — Structural enforcement layer
