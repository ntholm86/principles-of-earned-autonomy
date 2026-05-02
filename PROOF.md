# Empirical Evidence

*The framework's load-bearing claims are falsifiable. This file documents how to test each one and what one reference implementation found when it did.*

---

## Digest (60 seconds)

Three conformance tests, one per principle:

1. **Commander's Intent** — Present the artifact cold to evaluators who did not author it. If they produce coherent, situated output without scaffolding, it conforms.
2. **Observable Autonomy** — Give an absent human observer only the trail. If they can locate a decision, reconstruct the reasoning, and find something to challenge, it conforms.
3. **Convergence Is Silence** — Run the loop to silence across three evaluators from distinct families, each in a fresh session. If the loop stops because nothing is left to change, it conforms.

These tests are domain-agnostic. Apply them to your own system. Reference evidence from one implementation follows.

---

## How conformance is tested

Each principle has a test. The tests below apply regardless of domain, stack, or scale. Run them on your own implementation, not on this manifesto.

### Principle 1 — Commander's Intent

**The falsification question.** The litmus test in [PRINCIPLES.md](./PRINCIPLES.md): *if you removed all specific examples and thresholds from your skill (or process, or specification), would an intelligent agent that did not participate in writing it still know what to do?*

**How to test it.** Present the artifact cold to evaluators from distinct model families who did not author it. Ask them to apply it. Record whether they produce coherent output without external scaffolding, or whether they need the author to interpret the instructions.

**Failure mode.** Evaluators request clarifying context, add their own assumptions, or produce outputs the author would not recognize as conformant. This indicates the artifact is written as a checklist, not a mission.

### Principle 2 — Observable Autonomy

**The falsification question.** *Can a person who was not present during a run reconstruct what the agent did, why, and whether to trust the results, from the trail alone?*

**How to test it.** Close the loop. Give an absent human observer only the trail — no direct conversation, no supplemental context. Ask them to audit it: locate a specific decision, reconstruct the reasoning, and find one thing they would challenge.

**Failure mode.** The observer cannot locate the decision that produced a given output, or cannot tell whether a decision was reasoned or pattern-matched. This indicates the trail records outputs, not reasoning.

### Principle 3 — Convergence Is Silence

**The falsification question.** *Does the loop stop because there is genuinely nothing left to change — or because a stopping rule fired?*

**How to test it.** Run the loop to silence across three independent evaluators from distinct model families, each in a fresh session with no shared context. Record not just what each evaluator changed, but what each explicitly declined to change and why. Count convergence only when silence is the result, not when a turn limit or score threshold was reached.

**Failure mode.** The loop terminates because a stopping rule fired. Or two evaluators find the same things in the same direction — suggesting shared training bias, not independent convergence.

---

## Reference evidence

The artifact under test was the **autonomous-agent-skills suite** — six skills that an AI agent runs on a codebase to improve itself and record its reasoning. This manifesto is the rulebook; the skills suite is what was built and tested under that rulebook. One implementation, one domain (developer tooling). Bounded, real evidence.

The full record is in the skills suite's `.trail/log.md`. What follows is one example per principle.

### Principle 1 — Commander's Intent

Three fresh model families (Anthropic, xAI/Grok, Google/Gemini) — none involved in authoring the suite — were each asked to apply it cold to a real target. Each evaluator produced a coherent evaluation approach without external scaffolding. None reported the skills as underspecified. The suite directed independent reasoning across distinct model lineages without a checklist.

### Principle 2 — Observable Autonomy

After a closed convergence chain, a human review opened the trail cold and was able to reconstruct each evaluator's reasoning, locate decisions, and — critically — find a defect the chain had missed (see *What was falsified*). The defect was findable *because* the trail made the chain's reasoning inspectable after the fact. Observability is what allowed falsification to occur at all.

### Principle 3 — Convergence Is Silence

Three evaluator families, evaluating a locked artifact in isolation, each independently recorded zero changes. The chain closed on silence rather than on a stabilizing score. The skill suite reached its own defined exit condition.

---

## What was falsified

After the chain closed, human review of the same target found a cross-file contradiction all three evaluators had stepped past: a file in scope referred to one of the principles by a name that did not match [PRINCIPLES.md](./PRINCIPLES.md). A second instance of the same class — documentation drift surviving a closed convergence chain — was then found inside the skill suite itself.

This falsifies one specific (unstated) reading: *that family-diverse silence convergence implies the artifact is correct.* It does not falsify Principle 3 as written, which claims convergence is the **strongest external signal**, not a guarantee.

The recurring shape of the failure is now part of the record: the chain reads files for their first-order content and does not reliably test the second-order claims those files make about the rest of the repository. This is a property of the chain as currently operated, and it is exactly the kind of limit [PROBLEM.md](./PROBLEM.md) already names — independent evaluators reduce shared blind spots but do not eliminate them.

---

## What this evidence does and does not establish

| Claim | Status |
|---|---|
| A skill suite written as missions (not steps) can direct fresh evaluators' reasoning | Supported |
| A self-improving skill suite governed by these principles can reach silence | Supported |
| The trail makes after-the-fact reasoning inspectable by an absent observer | Supported (the falsification itself is the evidence) |
| The principles transmit across at least three distinct model families | Supported within the tested set |
| Silence convergence implies the artifact is correct | **Not supported. Falsified.** |
| Independent evaluators are immune to shared blind spots | **Not supported.** |

---

## A note on the development trail

The skill suite was not built in one sitting. It was derived through roughly one hundred self-targeting improvement runs and two structural rebuilds, during which the measurement framework was retired and replaced more than once. That history is genealogical evidence — it shows where the suite came from and that it can survive its own destructive scrutiny — but it is not what this document is proving. The proof above is against the **frozen** skill suite, exercised by parties that did not participate in its development.

A document that hid the falsification to protect the convergence claim would be the self-validating loop these principles were written to prevent. Both results are recorded here for the same reason.
