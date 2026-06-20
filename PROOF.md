# Conformance and Empirical Evidence

*The framework's load-bearing claims are falsifiable. This file documents how to test each one and what two reference implementations found when they did.*

---

## Digest (60 seconds)

Three conformance tests, one per principle:

1. **Commander's Intent** - Present the artifact cold to evaluators who did not author it. If they produce coherent, situated output without scaffolding, it conforms.
2. **Observable Autonomy** - Give an absent human observer only the trail. If they can locate a decision, reconstruct the reasoning, and find something to challenge, it conforms.
3. **Convergence Is Silence** - Run the loop to silence across three evaluators from distinct families, each in a fresh session. If the loop stops because nothing is left to change, it conforms.

An **ARF probe** tests whether an agent's reasoning is genuinely situated to the specific case rather than pattern-matched: construct a contrastive Case A / Case B pair, pre-register the expected divergence before administering, and score whether responses diverge at exactly the predicted point. An initial 3-probe dataset has been administered through the LLM Harness Protocol; results are in [`probes/results/`](./probes/results/RESULTS.md). Independent replication remains open.

These tests are domain-agnostic. Apply them to your own system. Reference evidence from two implementations follows.

---

## How conformance is tested

Each principle has a test; ARF, the framework's central measurable property, has a probe test of its own. The tests below apply regardless of domain, stack, or scale. Run them on your own implementation, not on this manifesto.

### Principle 1: Commander's Intent

**The falsification question.** The litmus test in [PRINCIPLES.md](./PRINCIPLES.md): *if you removed all specific examples and thresholds from your skill (or process, or specification), would an intelligent agent that did not participate in writing it still know what to do?*

**How to test it.** Present the artifact cold to evaluators from distinct model families who did not author it. Ask them to apply it. Record whether they produce coherent output without external scaffolding, or whether they need the author to interpret the instructions.

**Failure mode.** Evaluators request clarifying context, add their own assumptions, or produce outputs the author would not recognize as conformant. This indicates the artifact is written as a checklist, not a mission.

### Principle 2: Observable Autonomy

**The falsification question.** *Can a person who was not present during a run reconstruct what the agent did, why, and whether to trust the results, from the trail alone?*

**How to test it.** Close the loop. Give an absent human observer only the trail: no direct conversation, no supplemental context. Ask them to audit it: locate a specific decision, reconstruct the reasoning, and find one thing they would challenge.

**Failure mode.** The observer cannot locate the decision that produced a given output, or cannot tell whether a decision was reasoned or pattern-matched. This indicates the trail records outputs, not reasoning.

**Implementation boundary (LLM systems).** For LLM-based systems, self-authored traces are summaries, not verbatim telemetry. The model cannot be treated as an independent recorder of its own internal reasoning after the fact. Verbatim-grade evidence requires harness-level capture (for example, prompt/response transcripts, tool-call logs, or event streams) generated outside the audited agent.

### Principle 3: Convergence Is Silence

**The falsification question.** *Does the loop stop because there is genuinely nothing left to change, or because a stopping rule fired?*

**How to test it.** Run the loop to silence across three independent evaluators from distinct model families, each in a fresh session with no shared context. Record not just what each evaluator changed, but what each explicitly declined to change and why. Count convergence only when silence is the result, not when a turn limit or score threshold was reached.

**Failure mode.** The loop terminates because a stopping rule fired. Or two evaluators find the same things in the same direction, suggesting shared training bias, not independent convergence.

### ARF: Autonomous Reasoning Fidelity

**The falsification question.** *Does this agent reason about this specific case, or produce responses that would be structurally identical for any superficially similar case?*

**How to test it.** Construct a contrastive probe pair following the structure in [PRINCIPLES.md](./PRINCIPLES.md): Case A (a routine scenario the agent is likely to pattern-match against) and Case B (identical except for one material condition: a novel constraint, adversarial element, context shift, or underspecified edge). Before administering either case, record in the audit trail the specific condition that differs and the specific divergence you expect in the agent's response. Administer both cases in independent sessions with no shared context. Score whether the response to Case B diverges from Case A at the pre-registered point, in the predicted direction.

**Pass.** The response to Case B diverges substantively at the pre-registered point, the agent identifies what is different and responds to it. Surface rewording does not count; the reasoning structure must change where the case changed.

**Failure mode.** The response to Case B is structurally identical to Case A despite the material difference, or diverges at a point that was not pre-registered. Structurally identical responses indicate pattern-matching rather than situated reasoning.

**Note on reference evidence.** The formalization artifacts required for validated ARF evidence are: a published spec, test harness, probe dataset, and reproducibility report. The first three now exist: [ARF-SPEC.md](./ARF-SPEC.md) (v1.0.0, 2026-06-19), the [LLM Harness Protocol](https://github.com/ntholm86/harness-proxy) (v2.0.0), and an initial 3-probe dataset administered through the harness ([results](./probes/results/RESULTS.md)). The probe dataset covers three task classes (code review under novel constraints, instruction interpretation under stakeholder shift, ambiguity handling) on one model family (`claude-haiku-4-5`); results are 2 PASS, 1 INDETERMINATE. The reproducibility report — independent administrators and cross-model replication per [ARF-SPEC.md §7](./ARF-SPEC.md#7-validation-requirements) — remains open. The structural reason a probe administered through behavioral protocols cannot be trusted (instrument and subject share a single point of failure) has a published structural response: the harness provides protocol-layer capture that makes harness-administered probe execution possible. The initial dataset demonstrates administrability; validation awaits replication.

---

## Reference evidence

The framework has two published reference implementations, each carrying bounded evidence for a different load-bearing claim. *Reference Implementation A* (Skills Suite) exercises the three principles applied to an artifact and reports what conformance testing found. *Reference Implementation B* (Harness Protocol) exercises the structural layer Principle 2 requires and reports that capture-author separation is buildable in current tooling. The general empirical premise is grounded by the literature cited in [PRINCIPLES.md](./PRINCIPLES.md); what follows is bounded reference evidence from two implementations built under those principles. Two implementations, two domains. Bounded, real evidence.

### Reference Implementation A: Principles of Earned Autonomy Skills Suite

The artifact under test was the **Principles of Earned Autonomy Skills Suite**, a conformance implementation in the developer-tooling domain.

**Source and inspection.** The full record is the append-only audit trail of the suite, public at [github.com/ntholm86/principles-of-earned-autonomy-skills-suite/blob/main/.trail/audit-trail.md](https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite/blob/main/.trail/audit-trail.md). Each paragraph below cites the specific trail entries that back it, so a reader can open the linked entries and reconstruct the evidence independently. The cited entries are dated and slugged; the file is append-only and the suite repository carries its own integrity verifier.

#### Principle 1: Commander's Intent

Three fresh-session evaluators from distinct model families, none involved in authoring the suite, were each asked to apply it cold to the same target (the suite self-targeted). Each produced a coherent evaluation approach without external scaffolding and none reported the skills as underspecified. The evaluators and outcomes are recorded in suite trail entries `2026-04-24 -- v3-silence-1` (Anthropic Claude Sonnet 4.6, peg 1/3, silence), `2026-04-24 -- v3-silence-2` (xAI Grok Code Fast 1, peg 2/3, silence), and `2026-04-24 -- v3-silence-3` (Google Gemini 3.1 Pro Preview, peg 3/3, silence). The suite directed independent reasoning across three distinct model lineages from a single instruction set, without a checklist.

#### Principle 2: Observable Autonomy

After the chain closed, a human-led review opened the trail cold and was able to reconstruct each evaluator's reasoning, locate decisions, and find a defect the chain had missed (see *What was falsified*). The defect was findable *because* the trail made the chain's reasoning inspectable after the fact. Observability is what allowed falsification to occur at all. The fix and its reasoning are recorded in the suite trail entry `2026-04-24 -- trail/README.md drift fix`.

#### Principle 3: Convergence Is Silence

The three evaluators above, working from fresh sessions on the locked artifact in isolation, each independently recorded zero changes (entries `v3-silence-1/2/3` above). A subsequent fourth evaluator ran an explicit cross-layer coherence check and likewise found no contradiction (suite trail entry `2026-04-24 -- cross-layer-coherence`, Anthropic Claude). The chain closed on silence rather than on a stabilizing score. The skill suite reached its own defined exit condition.

**Transparency on diversity.** The three principal evaluators differed by model family but were administered by a single operator from the same instruction set; "diverse independent evaluators" was satisfied for model lineage but not for operator. The minimum-bar test in [PRINCIPLES.md](./PRINCIPLES.md) sets a higher bar than this single piece of evidence clears on its own; this is one data point from one implementation, not a complete validation of the principle.

#### What was falsified (Reference Implementation A)

After the chain closed, human review of the same target found a cross-file contradiction all three evaluators had stepped past: the suite's `trail/README.md` described a directory layout (separate `SUMMARY.md` and `INDEX.md` files) that no longer existed in the live tree, and its glossary still defined the suite's earlier (v2) skill vocabulary that had been replaced. A second instance of the same class, documentation drift surviving a closed convergence chain, was then found inside the suite itself (a v2-content splice tail in the same `trail/README.md`). Both fixes and their reasoning are in the suite trail entries `2026-04-24 -- trail/README.md drift fix` and `2026-04-24 -- trail-README-splice-repair`.

This falsifies one specific (unstated) reading: *that family-diverse silence convergence implies the artifact is correct.* It does not falsify Principle 3 as written, which claims convergence is the **strongest external signal**, not a guarantee.

The recurring shape of the failure is now part of the record: the chain reads files for their first-order content and does not reliably test the second-order claims those files make about the rest of the repository. This is a property of the chain as currently operated, and it is exactly the kind of limit [PROBLEM.md](./PROBLEM.md) already names, independent evaluators reduce shared blind spots but do not eliminate them.

#### A note on the development trail (Reference Implementation A)

The skill suite was not built in one sitting. It was derived through roughly one hundred self-targeting improvement runs and two structural rebuilds, during which the measurement framework was retired and replaced more than once. That history is genealogical evidence: it shows where the suite came from and that it can survive its own destructive scrutiny, but it is not what this document establishes. The conformance evidence above is against the **frozen** skill suite, exercised by parties that did not participate in its development.

A document that hid the falsification to protect the convergence claim would be the self-validating loop these principles were written to prevent. Both results are recorded here for the same reason.

---

### Reference Implementation B: LLM Harness Protocol

The artifact under test was the **LLM Harness Protocol** ([github.com/ntholm86/harness-proxy](https://github.com/ntholm86/harness-proxy)), a transparent MITM proxy implementing the structural layer Principle 2 requires.

**What the harness does.** The proxy intercepts standard LLM API traffic at a configurable listener (default `127.0.0.1:8474`) and forwards it to the real upstream after writing one entry per turn to an append-only JSONL ledger. Each entry is canonicalized via RFC 8785 (JSON Canonicalization Scheme) and chained to the previous entry via SHA-256 over the canonical bytes, so reordering or modifying any prior entry breaks the chain detectably. The proxy is fail-closed on persistence: the response is not released to the caller until the ledger entry is durably persisted (fsync'd). The audited agent never authors a ledger entry; the proxy does, before the agent's response is released.

**Provider coverage.** OpenAI / Grok (`/v1/chat/completions`), Anthropic (`/v1/messages`), and Gemini (`/v1beta/models/*`). Streaming and buffered responses both supported. The proxy is a dumb pipe for credentials (all headers forwarded verbatim, nothing read or stored), so client-side library code does not change beyond pointing `base_url` at the proxy.

**Specification.** The protocol is specified in the harness repository's `SPEC.md` (entry format, hash chain, streaming continuations, failure semantics, conformance tiers). The baseline ledger primitive is inherited from prior art (the `evo` framework's *proof ledger*, March 2026, and the *Agent Audit Trail* Internet-Draft `draft-sharif-agent-audit-trail`, March 2026); the enforcement mechanisms (fail-closed action gating, invisible MITM deployment, streaming continuations) are defined on top, as the structural layer Principle 2 requires.

**Build and integrity evidence.** The Rust implementation in `proxy-rust/` builds and runs on Windows x86_64 and Linux x86_64; CI builds and uploads artifacts on every push. The repository includes unit tests covering ledger integrity, JCS canonicalization, and ULID generation. Conformance is what the unit tests and the SPEC verify; full third-party replication is not yet in evidence.

**What this reference implementation establishes.** Capture-author separation, the load-bearing structural property Principle 2 requires, is buildable in current tooling without modifications to LLM client libraries, without provider cooperation, and without the audited agent's compliance.

**What this reference implementation does not establish.** The harness is a structural mechanism, not a measurement of reasoning quality. It does not validate ARF on its own; it removes one of the two structural reasons ARF could not previously be validly measured (instrument-and-subject sharing a single point of failure). The second blocker — a pre-registered probe dataset administered through the harness, with results independently replicated — is partially addressed: an initial 3-probe dataset now exists (see [`probes/results/`](./probes/results/RESULTS.md)), but independent replication remains open. The harness lifts ARF from *cannot be measured under current tooling* to *can be measured under the harness*; the initial dataset demonstrates administrability; validation awaits cross-model replication.

---

## What this evidence does and does not establish

| Claim | Status |
|---|---|
| A skill suite written as missions (not steps) can direct fresh evaluators' reasoning | Supported (Reference Implementation A) |
| A self-improving skill suite governed by these principles can reach silence | Supported (Reference Implementation A) |
| The trail makes after-the-fact reasoning inspectable by an absent observer | Supported (Reference Implementation A; the falsification itself is the evidence) |
| The principles transmit across at least three distinct model families | Supported within the tested set (Reference Implementation A) |
| Capture-author separation is buildable at the protocol layer in current tooling | Supported (Reference Implementation B) |
| A fail-closed, hash-chained, append-only ledger across multiple LLM providers can be operated without provider cooperation or client-library changes | Supported (Reference Implementation B) |
| Silence convergence implies the artifact is correct | **Not supported. Falsified.** |
| Independent evaluators are immune to shared blind spots | **Not supported.** |
| The harness, on its own, validates ARF | **Not supported.** The harness removes one structural blocker (instrument inheritance) but does not constitute an ARF probe result. |
| A pre-registered ARF probe administered through the harness, with independent replication | **Initial dataset submitted.** Three probes administered through harness v2.0.0, results in [`probes/results/`](./probes/results/RESULTS.md). Independent replication remains open. |

---
