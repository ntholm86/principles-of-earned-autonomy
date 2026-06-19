# Provenance should include reasoning traces; Reproducibility needs clarification for non-deterministic models

Two suggestions for v0.2, both from implementation experience building audit trails for LLM agents.

---

**First: Provenance (§6.9) should explicitly include reasoning traces.**

The current text captures model, tools, prompt context, and data sources - what the agent *used*. For agents that produce chain-of-thought or planning steps before acting, the reasoning trace is often the most diagnostic provenance: it shows what the agent *did with* those inputs.

Over 100+ trail entries across two months, I found five incident classes where the reasoning trace was diagnostic and the action record alone would have missed the root cause. The pattern: "action: file changed" tells the auditor *what*; "reasoning: misunderstood migration scope" tells them *why*. Details and cross-model validation evidence: [deployment case study](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/docs/DEPLOYMENT-CASE-STUDY.md).

Major providers now expose reasoning (OpenAI's `reasoning` parameter, Anthropic's extended thinking). AAS-1 should specify where these traces fit in the evidentiary record.

---

**Second: Reproducibility (§6.10) needs a clarification for non-deterministic models.**

"Sufficient state to permit re-derivation" is clear for deterministic systems. For LLMs, exact output reproduction is often impossible - the same inputs can yield different outputs on replay.

I'd suggest: for non-deterministic models, the standard is *reasoning reproducibility* - an auditor can verify that the recorded reasoning is consistent with the recorded inputs, even if the exact output might vary on replay. This is achievable; output reproducibility is not.

---

**A possible thirteenth assertion: Reasoning Quality.**

This one I'm less certain about. Did the agent actually reason about *this* situation, or did it apply a template? The question matters for audit, but it doesn't fit cleanly into the per-record model - it's a property that emerges from paired test cases, not a single Class A record.

One methodology (Autonomous Reasoning Fidelity probes) uses paired cases with a single material fact changed. A reasoning agent diverges when the material fact differs; a pattern-matching agent produces the same response regardless. It's testable even for non-deterministic models because it measures divergence, not reproduction. If the working group sees a path to formalizing this, the [ARF spec](https://github.com/ntholm86/principles-of-earned-autonomy/blob/main/ARF-SPEC.md) is CC0.

---