# AAS-1 Proposal Drafts

Two proposals formatted to match [`ISSUE_TEMPLATE/proposal.md`](https://github.com/Kadikoy1/aas-1/blob/main/ISSUE_TEMPLATE/proposal.md).

- **PROPOSAL 1** — Edit your existing GitHub issue to this content.
- **PROPOSAL 2** — File as a new issue.

The ARF/Reasoning Quality point (originally the third suggestion) is not ready as a formal proposal; it is preserved as an alternative in Proposal 1.

---

<!-- ============================================================ -->
<!-- PROPOSAL 1 — edit your existing GitHub issue to this content -->
<!-- ============================================================ -->

# [PROPOSAL] Provenance records (§6.9) should capture reasoning traces

## Summary

Add an explicit requirement to §6.9 that where an LLM agent produces a reasoning trace (chain-of-thought, planning steps, or structured pre-action deliberation), that trace is captured as part of the provenance record.

## Section affected

§6.9 Provenance

## Motivation

The current text records what an agent *used* — model identity, tools, prompt context, data sources. For agents that produce reasoning steps before acting, the reasoning trace is the most diagnostic provenance artifact: it reveals what the agent did *with* those inputs.

Across 100+ trail entries building audit systems for LLM agents over two months, I found five incident classes where the reasoning trace was diagnostic and the action record alone would have missed the root cause. The consistent failure pattern: "action: file changed" tells the auditor *what*; "reasoning: misunderstood migration scope" tells them *why*. Details and cross-model validation evidence: [deployment case study](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/docs/DEPLOYMENT-CASE-STUDY.md).

Major providers now expose reasoning (OpenAI's `reasoning` parameter, Anthropic's extended thinking), making capture practical today.

## Proposed change

Add the following to §6.9, after the existing list of required provenance fields:

> Where the agent produces a reasoning trace (chain-of-thought, planning steps, or structured pre-action deliberation), the trace shall be captured as a provenance record field. Where a reasoning trace is not available (the provider does not expose it), this shall be noted; absence of a captured trace is not equivalent to absence of a reasoning process.

## Backwards compatibility

Additive. Existing records that do not include a reasoning trace remain valid. The requirement applies only to agents using provider APIs that expose reasoning traces. Systems deployed before providers made traces available are not retroactively non-compliant.

## Alternatives considered

**Treating reasoning traces as optional metadata rather than a required field.** Rejected: optional fields are systematically omitted under implementation pressure, eliminating their audit value. A required field with an explicit "not available" carve-out achieves both coverage and pragmatism.

**A new numbered assertion for Reasoning Quality** (did the agent reason about *this* situation, or apply a template?). This is a distinct and harder question — it is a property of a pair of records, not a single Class A record, so it does not fit §6.9 directly. One testable methodology is Autonomous Reasoning Fidelity probes using paired cases with a single material fact changed ([ARF spec, CC0](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/ARF-SPEC.md)). Flagged for the working group's consideration as a possible future addition; not part of this proposal.

## Permission to credit

- [ ] You may credit me as a contributor in the AAS-1 v0.2 release notes (name and organisation).
- [ ] Please keep this proposal attributed but not credited in release materials.
- [ ] Please keep this proposal anonymous.

---

<!-- ============================================================ -->
<!-- PROPOSAL 2 — file as a new GitHub issue                      -->
<!-- ============================================================ -->

# [PROPOSAL] Reproducibility (§6.10) — define the standard for non-deterministic models

## Summary

Clarify §6.10 (Reproducibility) to specify that for non-deterministic models the applicable standard is *reasoning reproducibility*, not output-identical reproduction.

## Section affected

§6.10 Reproducibility

## Motivation

"Sufficient state to permit re-derivation" is unambiguous for deterministic systems. For LLMs, exact output reproduction is generally not achievable — the same inputs produce different outputs across calls, even at low temperature settings. Without explicit clarification, §6.10 either excludes LLM agents from AAS-1 compliance or produces nominal compliance: implementations that record state which cannot functionally support re-derivation.

## Proposed change

Add the following clarification to §6.10:

> For non-deterministic models, the re-derivation standard is *reasoning reproducibility*: an auditor can verify that the recorded reasoning is consistent with the recorded inputs, even if the exact output varies on replay. Output-identical reproduction is not required for non-deterministic systems.

## Backwards compatibility

Clarification only. No change to the requirement for deterministic systems. The proposed text narrows an existing ambiguity without relaxing the intent of the original provision.

## Alternatives considered

**Requiring output reproducibility for all systems including LLMs.** Not practically achievable for most LLM deployments. Would produce nominal compliance (recording state that cannot be used for re-derivation) or exclude LLM agents from the standard entirely.

**Deferring to implementation guidance rather than the spec.** The ambiguity is in the normative text; leaving it unaddressed invites inconsistent interpretation across implementations. A one-sentence clarification in the spec is the cleaner fix.

## Permission to credit

- [ ] You may credit me as a contributor in the AAS-1 v0.2 release notes (name and organisation).
- [ ] Please keep this proposal attributed but not credited in release materials.
- [ ] Please keep this proposal anonymous.
