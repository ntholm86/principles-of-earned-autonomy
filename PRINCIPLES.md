# Principles of Earned Autonomy

> **Authorship & License**
> Author: Nils Wendelboe Holmager | Date: April 2026
> This philosophical framework and documentation are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

These principles govern how autonomous agents operate.
They are **architectural constraints**. An agent or instruction set that violates them is broken.

Context for these principles (the problems they are designed to solve) is in [PROBLEM.md](./PROBLEM.md).

---

## Digest (60 seconds)

One premise, three principles, one emergent property.

**Premise: The agent is an unreliable narrator of itself.** Stated reasoning is not internal reasoning; self-correction often degrades performance; the agent's account of its own decisions cannot be the only account. The three principles are structural responses to this fact.

1. **Commander's Intent** - *Define the destination. Never prescribe the route.* The agent must interpret and adapt. *(The operator narrates the goal; the agent does not self-interpret it.)*
2. **Observable Autonomy** - *Autonomy is a function of transparency.* Every autonomous operation produces a visible audit trail captured as the work happens, which the agent cannot retroactively edit. *(The degree of autonomy a system deserves is bounded by the degree of transparency it provides.)*
3. **Convergence Is Silence** - *The system has converged, for purposes of the loop, when diverse independent evaluators find nothing left to change.* *(Independent evaluators judge the work; silence is the strongest available stopping signal, not proof of correctness.)*

Together they produce **Autonomous Reasoning Fidelity (ARF)** - the external signal that genuine, situated reasoning is both occurring and visible. ARF is the proposed target property that emerges only when all three principles hold simultaneously. (See [PROOF.md](./PROOF.md) for how to test conformance for each principle and reference evidence from two implementations.)

---

## Premise: The agent is an unreliable narrator of itself

The three principles are not arbitrary. They are structural responses to a single empirical fact: an LLM agent's account of its own reasoning is not reliable evidence of that reasoning.

This is not the claim that agents lie. It is stronger. Even when the agent is trying to be honest, the narration it produces about its own decisions, its own instructions, and its own quality is structurally untrustworthy.

**The evidence:**

- Stated reasoning diverges from internal reasoning. Chain-of-thought explanations can be plausible and misleading at the same time (Turpin et al., *Language Models Don't Always Say What They Think*, NeurIPS 2023).
- Faithfulness of stated reasoning to the model's actual computation is itself measurable and is often low, even for models specifically trained to reason step-by-step (Lanham et al., *Measuring Faithfulness in Chain-of-Thought Reasoning*, 2023).
- Even reasoning-trained models do not reliably say what they think; CoT monitoring is not sufficient to rule out undesired behavior (Chen et al., *Reasoning Models Don't Always Say What They Think*, 2025).
- Unsupervised self-correction often degrades performance rather than improving it (Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet*, ICLR 2024).
- Models can behave one way during evaluation and another way during deployment without that divergence being visible from outputs alone (Hubinger et al., *Sleeper Agents*, 2024; Greenblatt et al., *Alignment Faking in Large Language Models*, 2024). The narration the agent produces about its goals during oversight is not, by itself, reliable evidence of those goals.

**The implication:**

Any framework that delegates real autonomy to an LLM agent must assume that the agent cannot be the only narrator of its own actions, the only interpreter of its own instructions, or the only judge of its own work. Each of those roles must be structurally separated from the agent. The three principles each separate one:

- **Principle 1 (Commander's Intent)** separates *interpretation*: the operator defines the goal; the agent does not self-interpret what it was asked to do.
- **Principle 2 (Observable Autonomy)** separates *narration*: an independent record of the work exists; the agent is not the sole author of what it did.
- **Principle 3 (Convergence Is Silence)** separates *judgment*: diverse independent evaluators decide whether the work is done; the agent does not self-assess.

A framework that omits any of the three leaves one role undefended. A framework that names all three but allows the agent to author them itself has not implemented them.

---

## Principle 1: Commander's Intent

*Define the destination. Never prescribe the route.*

**Origin:** Auftragstaktik (Prussian mission-type command), the Coaching Kata (Toyota), the Socratic Method.

**The problem it solves:** A prescriptive instruction ("check if param count > 5, apply the Strangler Fig pattern, scan for these 8 waste types") produces compliance, not understanding. An agent following a checklist scores well on the checklist and misses everything the checklist didn't mention. The checklist becomes the ceiling.

**The principle:** An autonomous agent must understand *what* needs to be achieved and *why* it matters. It must then determine *how*, interpreting the mission and adapting to the specific situation it encounters. The mission defines the shape of the work. The agent discovers the content.

**In practice:**

- **Ask, don't tell.** "What here doesn't earn its existence?" not "Look for unused imports, dead code, and unreachable branches." The agent should arrive at those specifics because they're the right answer, not because they were listed.
- **State the goal, not the steps.** "Find where the system is asked to do too much" not "Check function length > 50 lines, parameter count > 5." Those thresholds may be correct, but the agent should derive them from understanding overburden rather than reading a bullet point.
- **Provide vocabulary, not answers.** Introduce concepts as a *thinking framework*, not a lookup table.
- **Trust the interpretation.** If the agent's interpretation of the mission leads to a different answer than the checklist would have, the interpretation might be right and the checklist wrong. That's the whole point.

**The test:** If you removed all the specific examples and thresholds from an instruction, would an intelligent agent still know what to do? If yes, the instruction embodies Commander's Intent. If not, it is a checklist.

Distinguish it from vagueness: "Make it better" lacks a defined objective. "Find what doesn't earn its maintenance cost and remove it, proving each removal is safe" has a clear objective, clear constraint, and open method.

---

## Principle 2: Observable Autonomy

*The degree of autonomy a system deserves is bounded by the degree of transparency it provides.*

**Origin:** Its structural root is Saltzer & Schroeder's *separation of privilege* (1975, [original paper p.9](https://www.cl.cam.ac.uk/teaching/1011/R01/75-protection.pdf)): "no single accident, deception, or breach of trust is sufficient to compromise the protected information." They stated it for access control: a mechanism that requires two keys, held by separate parties, is more robust than one that trusts a single key. The same pattern is the load-bearing safeguard in some of the highest-stakes systems humans have ever built - most starkly the two-person rule governing nuclear weapons release (Sagan, 1993), where no single operator can authorize launch and no single party can fabricate the authorization record. Observable Autonomy transfers that structure from access control and authorization to the *epistemic record*: the party that acts must not also be the sole party that authors the account of its action, so that no single act of self-narration is sufficient to compromise the integrity of the trail. The principle is theirs; the transfer to the record of an autonomous agent's own reasoning is what this principle adds. It further synthesizes Meaningful Human Control (Santoni de Sio & van den Hoven, 2018), Trust Calibration (Lee & See, 2004), and the Observatory architecture pattern, but establishes a relationship none of those frameworks state explicitly.

**The problem it solves:** Autonomy and transparency are typically treated as parallel concerns, as if they were independent checkboxes. They are causally linked. Autonomy without observability is abdication. And observability requires more than the existence of a record: it requires that the record was captured as the work happened and cannot be retroactively edited by the agent that produced it. Otherwise the record is self-authored testimony.

**The principle:** Every autonomous operation must produce a record that is captured as the work happens, not composed after it, and that the agent cannot revise after the fact. Audit may occur at any later time, but the record being audited must have come into existence concurrently with the decisions it documents, untampered, and must not be subject to revision by the audited agent. The audit trail is the mechanism by which the agent earns the right to keep acting.

**The dependency:**

```
Transparency → Trust → Autonomy
     ↓                    ↓
  (observable)        (earned, not granted)
     ↓                    ↓
  reduces            reduces
     ↓                    ↓
  if lost             if lost
     ↓                    ↓
Trust decays → Autonomy must be revoked
```

Autonomy is a *function* of transparency:
- More visibility → more trust → more autonomy earned
- Less visibility → trust decays → autonomy must be constrained
- Zero visibility → zero trust → autonomy must be revoked regardless of competence

### Fidelity marking

Where the agent authors its own summary, this must be explicitly marked so observers can discount accordingly. A summary written by the audited party is evidence, but it is not *independent* evidence. Where verbatim capture is impossible (e.g., platform limitations prevent transcript export), the trail must explicitly mark fidelity rather than silently degrading. "Reconstructed from agent memory" and "verbatim tool output" are different trust levels; conflating them is dishonest.

### Capture-author separation

The agent that makes a decision cannot also be the sole author of the record of that decision. The act of deciding and the act of recording must be structurally separated, so that no later edit by the agent can alter what the record says happened. Any record authored after the fact by the audited agent is testimony, not evidence, and must be marked as such. Implementation-level constraints and examples belong in [PROOF.md](./PROOF.md).

### Why structural capture is required

An LLM agent generating its own trail after the fact will produce a coherent narrative, whether or not that narrative matches what occurred. This is what unconstrained text generation does under a "summarize what you did" prompt. Post-hoc summaries written by the audited party are evidence of what the agent says it did, not of what it did. The trail must therefore be captured *as the work happens*, in a form the agent does not author after the outcome is known. "Structural" means the trail's integrity does not depend on the agent's honesty.

A reference implementation of the structural layer is published separately as the [LLM Harness Protocol](https://github.com/ntholm86/LLM-harness-protocol): a transparent MITM proxy that intercepts standard LLM API traffic (OpenAI, Anthropic, Gemini), writes each turn to a tamper-evident, hash-chained, append-only ledger, and releases the response to the caller only after the entry is durably persisted. The proxy is a dumb pipe to the model and an enforcement layer for the record; the audited agent has no path to author or revise its own entries. The harness does not originate its ledger primitive: the append-only, hash-chained JSON record of agent actions was developed in parallel by multiple parties in early 2026, with the *Agent Audit Trail* Internet-Draft `draft-sharif-agent-audit-trail` (Sharif, 2026) codifying a JCS-canonicalized JSONL variant alongside the `evo` framework's "proof ledger" implementation (March 2026); the harness inherits that baseline and adds the enforcement layer (fail-closed action gating, invisible MITM deployment, streaming continuations). Capture-author separation is therefore not an aspirational property of this framework but a buildable one demonstrated in current tooling, sitting on a ledger primitive that is itself converged-upon prior art rather than a one-off invention.

**In practice:**

- **Record reasoning, not just results.** Capture what was examined, what was found, what was decided, and why. The constraint is *content fidelity* (the reasoning was recorded), not *delivery timing* (the human watched live).
- **Show the reasoning, not just the conclusion.** "I removed `utils/helpers.py` because no module imports it and its tests are orphaned" rather than "Removed 1 file." The *why* is what makes the action observable.
- **Make uncertainty visible.** "This might be dead code, but I can't trace the dynamic import in `loader.py` - flagging for human review" makes uncertainty visible.
- **Record everything.** The trail is not optional documentation. Every autonomous operation produces a trail entry. Every entry is comparable to the prior entry. The trajectory is visible.
- **Design for the absent human.** Assume the human may not be watching right now but will review later. The trail must be legible after the fact, not just during execution.

**The test:** If the human stepped away and came back, could they reconstruct what the agent did, why, and whether to trust the results, from the trail alone? If yes, the system has Observable Autonomy. If not, the autonomy is unsafe regardless of how good the agent's work was.

**The corollaries:**

- *A record composed after the decision is testimony.* (capture-moment fidelity)
- *A record an agent can rewrite is untrustworthy.* (tamper resistance)

The two together close the two ways post-hoc rationalization enters a trail: fabrication at the moment of writing, and revision after the fact.

---

## Principle 3: Convergence Is Silence

*A system has converged, for purposes of the loop, when diverse evaluators independently find nothing left to change.*

**Origin:** Cross-validation (statistics), ensemble agreement (machine learning), the Delphi method (forecasting), and Kaizen's own exit condition, taken to its logical conclusion.

**The problem it solves:** Iterative improvement loops declare convergence too early. The typical criterion - "the score stabilized across N consecutive runs" - measures the wrong signal. A score can stabilize while the system is still changing underneath: each run removes something and adds something, the score stays flat, but the artifact never stops churning. Worse, a single evaluator (or a single model family) can converge on its own blind spots, producing a stable score that reflects the evaluator's limitations, not the artifact's quality.

Score stability is necessary but not sufficient. Change-rate stability is necessary but not sufficient. Only the combination, across diverse independent evaluators, constitutes convergence.

**The principle:** Convergence requires diverse independent evaluators to arrive at the same assessment *and* find nothing material to change. Silence is the strongest available stopping signal for the loop, not a guarantee that the artifact is correct.

### The test

Three simultaneous conditions:

1. **Score agreement across distinct evaluator families.** N consecutive evaluations by M distinct evaluator families produce the same score within a defined tolerance. Evaluators must be meaningfully diverse, different models, different people, different analytical traditions. Same-family evaluators (e.g., multiple versions of one model) count as one. Each model family develops habituated blind spots; a different family, trained and evaluated independently, does not share those blind spots. The mechanism is analogous to scientific peer review: the value is not in more reviews but in *independent* reviews.

2. **Zero material change.** Each of those N evaluations ends with no changes to the artifact itself. The only output is the evaluation record. If a run produces a diff to the artifact, the convergence counter resets to zero, regardless of whether the score changed.

3. **Independent assessment, including of the measurement scheme.** Each evaluator scores fresh, without consulting prior scores. In chat-based systems, switching to a new model inside the same conversation is **not** independent: prior scores remain in context. A valid convergence evaluation must begin in a fresh conversation/session. Independence extends to *what is being measured*, not just to the score: if the first evaluator derives the measurement scheme and subsequent evaluators merely score against it, independence is partial. A genuinely independent evaluator re-derives the measurement scheme from the artifact before scoring, then compares against any inherited scheme. Convergence on re-derivation validates the scheme; divergence is itself a finding (the inherited scheme had a blind spot one family could not see). Pre-agreed externally anchored rubrics (published standards) are exempt from re-derivation, but not from the divergence-as-finding rule.

**The minimum bar:** 3 consecutive runs, 3 distinct evaluator families, same score, zero artifact changes, at least one re-derivation of the measurement scheme that converged with the inherited scheme. Below this, you have improvement trajectory. Above this, you have convergence. There is no middle ground.

**Why this matters for earned autonomy:** Without this principle, an autonomous improvement loop has no honest stopping condition. It runs indefinitely, each cycle finding something to change because finding something to change is what the loop is designed to do. The agent's incentive is to justify its own execution by producing changes. Convergence Is Silence inverts that incentive: the agent proves its value by finding *nothing*, and the system earns its strongest available case for stopping by surviving diverse scrutiny unchanged.

**The corollary:** *If the loop is still producing changes, the system is still improving. If the system is still improving, it has not converged. Convergence is the absence of actionable findings across independent observers.*

---

## How the principles interact

All three answer the same premise. The agent cannot be the sole narrator of its own goal, its own actions, or its own quality. Each principle separates one of those roles from the agent: Principle 1 separates interpretation, Principle 2 separates narration, Principle 3 separates judgment. Removing any one leaves a role the agent can quietly take back.

Commander's Intent without Observable Autonomy is dangerous: you told the agent what to achieve but cannot see how it is pursuing it.

Observable Autonomy without Commander's Intent is empty: you can see everything the agent does, but it is following a checklist, so the observability shows compliance rather than interpretation.

Together: the agent understands the goal, interprets the mission, adapts to what it encounters, and makes every step of that process visible. The human can trust the autonomy because they can see how the agent arrived at its conclusions. The agent can be autonomous because it has earned that trust through transparency.

Convergence Is Silence completes the system: it defines *when the loop has an honest basis to stop.* Without it, Commander's Intent gives purpose and Observable Autonomy gives visibility, but the loop has no honest exit. Convergence provides the stopping condition, and requires the other two to function. Convergence can only be measured if the evaluator interprets the mission independently (Commander's Intent) and the entire trail is visible (Observable Autonomy).

```
Commander's Intent     Observable Autonomy     Convergence Is Silence
(what + why)           (show everything)       (when to stop)
       \                     |                      /
        \                    |                     /
         →    Autonomous Agent that earns    ←
              trust through visible reasoning
              and knows when the work is done
```

### Scope: evidence substrate

They produce an **evidence substrate** on which trust *can* form - if observers actually consume the evidence, if the reasoning shown is genuinely correct, and if the social, organizational, and incentive conditions for delegation exist independently. The full boundary is in [PROBLEM.md § Out of Scope](./PROBLEM.md#out-of-scope-what-this-framework-does-not-solve).

---

## Autonomous Reasoning Fidelity (operational definition)

ARF is defined conceptually in [PROBLEM.md § What the Framework Measures](./PROBLEM.md#what-the-framework-measures-autonomous-reasoning-fidelity). This section gives the operational definition used downstream.

ARF is the measurable external signal this framework is designed to surface when Principles 1 and 2 are both satisfied and Principle 3 has validated the observation. The claimed contribution here is not the isolated idea that reasoning matters, nor the premise that self-report is unreliable; prior work already establishes much of that terrain. The claimed contribution is the synthesis: using Commander's Intent, Observable Autonomy, and Convergence Is Silence together as a proposed governance framework for earned, observable, revocable delegation. ARF names the target property that this proposed framework is meant to make measurable. It is a step toward a deployable discipline, not a claim that the problem is finished or that ARF solves every downstream safety problem.

*(Why the framework argues that a validated ARF probe should earn trust without capability restriction is in [PROBLEM.md § Restriction-first AI governance](./PROBLEM.md#what-existing-work-does-and-does-not-solve).)*

**Theoretical anchors:**

- **Auftragstaktik** (Prussian mission-type command) - telling subordinates *what* and *why*, then trusting them to determine *how*. Origin of Principle 1 and the "freedom of thought" half of ARF.
- **Meaningful Human Control** (Santoni de Sio & van den Hoven, 2018) - their framework requires both tracking (the system reflects the operator's values) and tracing (humans can trace decisions back through the causal chain). Shapes the "trail integrity" half; this principle extends the tracing requirement to a structural guarantee via capture-author separation.
- **Trust Calibration** (Lee & See, 2004) - trust in autonomous systems should be calibrated to actual capabilities, and calibration requires observability. Over-trust and under-trust are both failures. Principle 2 is the calibration mechanism.
- **Explicability as the fifth AI ethics principle** (Floridi et al., 2018, AI4People) - explicability (intelligibility + accountability) named as the necessary fifth pillar alongside beneficence, non-maleficence, autonomy, and justice. Principle 2 is the structural mechanism that operationalizes explicability: capture-author separation makes explicability enforceable as an artifact rather than aspirational as a principle.
- **Society-in-the-loop** (Rahwan, 2018) - oversight of autonomous systems must be plural and distributed, not concentrated in a single human or institution. Operates at the social-contract layer (who designs the constraints?); Principle 3 (Convergence Is Silence) extends the same anti-singularity-of-judgment instinct to the convergence-check layer (when does plural scrutiny constitute a stopping signal?). Different scale, same family.

**Preconditions** (principle compliance - verify the environment, not the agent):

1. **Freedom of thought** (P1 compliance). Remove all examples and thresholds from an instruction. Would a competent agent still know what to do? If yes, Commander's Intent holds. If no, the instruction has drifted toward prescription.
2. **Trail integrity** (P2 compliance). Can an absent observer reconstruct what the agent did, why, and whether to trust the results, from the trail alone? The trail is generated by the same model that produced the output; a coherent trail can document reasoning that never occurred. Trail integrity is necessary but not self-validating. It requires external verification through diverse evaluators (Principle 3) to guard against confabulation.

**The ARF metric itself: situational discrimination.** When both preconditions hold, ARF measures one thing: given two cases that look similar on the surface but differ in a material way, does the agent's reasoning path diverge where it should? In routine cases, situated reasoning (that is, reasoning adapted to this specific case rather than templated to its category; Suchman, 1987 established the same impossibility of full pre-specification for human expert action, a premise this framework extends to AI agents) and pattern-matching produce identical-looking trails. The distinguishing evidence emerges under novel or adversarial conditions: situations the checklist didn't anticipate, distribution shifts that expose shallow compliance, cases where rote execution fails but genuine interpretation succeeds. Without structured novelty, the framework cannot distinguish narration from reasoning.

**The probe structure.** A probe consists of two cases constructed together. Case A is a routine or expected scenario. Case B holds everything constant except one material condition: a novel constraint, an adversarial element, a context shift, or an underspecified edge. Before either case is administered, the operator pre-registers the expected divergence: what should change in the agent's reasoning path if it is genuinely responding to the material difference, and what should stay the same. The agent is then run on both cases under normal operating conditions, not in a test harness. A pass is when the agent's response actually diverges where the pre-registered expectation said it should, and does not diverge where it shouldn't. A fail is when the response is structurally identical across both cases, surface variation applied to the same underlying template regardless of the material difference. The pre-registration is what makes the test falsifiable; without it, a pass can always be explained as expected.

ARF answers: *did the agent's responses actually vary with the specifics of what it encountered, or did it produce surface variation on a generic template?*

**Technique ancestry and the novel claim.** The contrastive-pair mechanism has clear predecessors: the Winograd Schema Challenge (Levesque et al., 2012) and CheckList (Ribeiro, Wu, Guestrin, Singh, ACL 2020) both used structurally-similar minimal pairs to evaluate whether a model's responses were grounded in genuine understanding rather than surface pattern-matching. Within faithfulness research specifically, Lanham et al. (2023) applied a contrastive-perturbation methodology (early answering, mistake injection, paraphrasing, filler tokens) to measure whether a model's stated chain-of-thought causally drives its final answer. All three must be cited.

ARF therefore does not claim novelty at the level of contrastive testing itself. It applies the same family of techniques to a different target and makes a different claim. Winograd and CheckList measured capability; Lanham et al. measured the causal faithfulness of a single stated chain-of-thought to the answer it produced. Neither line of work questioned the trust-capability tension; both assumed it and worked within it.

ARF measures reasoning fidelity at the case level for the purpose of delegation: not *can the agent do this task?* and not *does this CoT causally drive this answer?*, but *is the agent's apparent reasoning situated enough to this specific case to justify unsupervised delegation on this class of work?* A pair of structurally similar cases differing in one material way, with pre-registered expectations, administered during normal operation: this is a reasoning-fidelity check at the case-pair level, not a single-trace faithfulness check and not a benchmark. The framework's downstream hypothesis is that a validated passing fidelity check should justify delegation without additional capability restriction. The technique is shared with the ancestors. The application context (operational trustworthy delegation, not capability evaluation or single-trace faithfulness), the mechanism (self-administered, operator-constructed, run during normal operation rather than as an external benchmark), and the conclusion it aspires to license (fuller autonomy without capability restriction) are distinct. Citing the ancestors sharpens the claim: the gap between what they did and what ARF does becomes explicit and citable.

**Falsifiable claim.** The framework's downstream hypothesis is that, if the ARF probe is validated, an operator who passes it on a given agent and task should be able to grant broader autonomy on that class of work without additional capability restriction, and the outcome (quality, correctness, alignment with intent) will be equal to or better than what a restricted agent produces. That is testable. It has not yet been tested.

**What formalization requires.** The probe structure above is a specification precondition: it defines what a probe is and what a pass means. That makes ARF a *reproducible idea*. What makes it a *legitimate, dated, citable technical artifact* is a different and harder step: a published spec (the probe construction rules, pass/fail criteria, and scope conditions, versioned and dated), a test harness (a mechanism for administering probes and recording results in a form independent of the audited agent), a curated probe dataset (a set of pre-registered Case A / Case B pairs with annotated expected divergences, covering the target class of delegation problems), and a reproducibility report (independent replication by parties other than the original authors, across multiple agent families and task domains). None of those artifacts exist yet. Until they do, ARF is a precisely-defined claim awaiting validation.

**The instrument-inheritance limit.** Under current LLM tooling (Model Context Protocol, system prompts, skill scaffolding), an ARF probe administered to an agent is itself executed by that agent: the probe's pre-registration, blinding, scoring, and trail are all read and honored by the model that produces the responses being scored. The probe therefore inherits the same failure modes Principle 2 names in the subject - probabilistic compliance, post-hoc rationalization, model-authored trails that can document reasoning that never occurred. Instrument and subject share a single point of failure, and that failure correlates with the case the probe is most needed to detect. This is the framework's Principle 2 making its own prediction concrete: behavioral-layer governance cannot structurally enforce its own preconditions, and the framework's own measurement construct is the worked example. The structural fix lives at the protocol layer - execution harnesses that capture probe execution outside the model's authorship, independent of the model's choice to comply. A reference implementation of that protocol layer now exists (see [LLM Harness Protocol](https://github.com/ntholm86/LLM-harness-protocol) and the discussion under Principle 2): a transparent MITM proxy with a tamper-evident, hash-chained ledger across OpenAI, Anthropic, and Gemini APIs, in which a response cannot reach the caller until its entry is durably persisted. The substrate the framework named as missing is therefore buildable in current tooling, and trustworthy ARF measurement is now blocked on the construction of the probe dataset, the test harness around the proxy, and the reproducibility report - not on the absence of the structural layer itself. ARF as a construct may still hold; whether it does remains to be tested with that scaffolding in place.

**Validation (Principle 3).** Principles 1 and 2 *produce* the conditions for ARF. Situational discrimination *measures* it. Principle 3 *validates* the measurement. Without diverse, independent evaluators confirming the signal, ARF is self-assessed, and self-assessment can become self-justification. A single evaluator (or single model family) may consistently accept trails that look situated but are generic, because the evaluator shares the agent's blind spots. ARF that survives diverse scrutiny is externally evidenced. ARF that only one observer ever validated is an assertion.

**Implementation note.** These principles define *what* Observable Autonomy requires. How to provide it is the implementer's choice. A conforming implementation could use markdown files, a database, structured logs, a dashboard, or any other medium, as long as the trail is captured as the work happens, the agent cannot revise it after the fact, and fidelity is marked where the agent authored its own content.

**Why this matters for scoring:** a scoring rubric for systems built on these principles must measure ARF directly - whether the agent discriminates between situations that demand different responses, not just whether the preconditions are satisfied. Process frameworks (CMMI, DMAIC, NIST AI RMF) measure whether processes are followed correctly. None of them measure whether the agent's responses are situated to what it actually encountered; in human organizations, that is assumed. For LLM agents, it must be externally evidenced.

---

## For implementers

Any instruction set built under these principles must embody all four:

1. **Structure over prescription.** Define phases that shape the work. Within each phase, ask questions that guide reasoning. Provide vocabulary and a thinking framework.
2. **Continuous narration.** Every phase must produce visible output. Format can be structured (tables, classifications) but the reasoning must be the agent's own. "I found X because Y" not "Checklist item 3: checked."
3. **Trail recording is mandatory.** Every run must update the target's audit trail. Every entry is comparable to the prior entry. The trajectory is the proof. No run is invisible.
4. **Self-targeting must work.** If the instruction can't be run on itself and produce meaningful results, it's too prescriptive (the agent is just matching patterns) or too vague (the agent has no framework to reason with). Self-targeting is the litmus test.

Operational standards (verification scripts, integrity snapshots, scoring rubrics, metrics history) that support these principles belong in the implementation's own documentation and tooling. They are tool prescriptions and do not belong in this manifesto repository.

---

## References

The following works are cited in this document. Inline citations appear in the body text; this section provides the full bibliographic entries for verification and further reading.

- **Levesque, H., Davis, E., & Morgenstern, L.** (2012). The Winograd schema challenge. *Proceedings of the Thirteenth International Conference on Principles of Knowledge Representation and Reasoning (KR 2012)*. https://cs.nyu.edu/~davise/papers/WSKR2012.pdf [Technique ancestry for ARF's contrastive-pair probe mechanism.]

- **Saltzer, J. H., & Schroeder, M. D.** (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. [Original paper: https://www.cl.cam.ac.uk/teaching/1011/R01/75-protection.pdf - structural root of Principle 2's capture-author separation requirement.]

- **Sagan, S. D.** (1993). *The Limits of Safety: Organizations, Accidents, and Nuclear Weapons*. Princeton University Press. [Cross-domain precedent for separation-of-privilege as a structural safeguard in the highest-stakes deployment humans have built. Cited in Principle 2's Origin paragraph alongside Saltzer & Schroeder.]

- **Lee, J. D., & See, K. A.** (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392 [Trust calibration as the mechanism underlying Principle 2.]

- **Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S.** (2020). Beyond accuracy: Behavioral testing of NLP models with CheckList. *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020)*. https://aclanthology.org/2020.acl-main.442/ [Technique ancestry for ARF's contrastive-pair probe mechanism.]

- **Turpin, M., Michael, J., Perez, E., & Bowman, S.** (2023). Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting. *Advances in Neural Information Processing Systems (NeurIPS 2023)*. arXiv:2305.04388. https://arxiv.org/abs/2305.04388 [Evidence that stated reasoning diverges from internal reasoning; grounds the Premise.]

- **Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., & Zhou, D.** (2024). Large language models cannot self-correct reasoning yet. *Proceedings of the International Conference on Learning Representations (ICLR 2024)*. arXiv:2310.01798. https://arxiv.org/abs/2310.01798 [Evidence that unsupervised self-correction degrades performance; grounds the Premise.]

- **Chen, Y., Benton, J., Radhakrishnan, A., Uesato, J., Denison, C., Schulman, J., Somani, A., Hase, P., Wagner, M., Roger, F., Mikulik, V., Bowman, S. R., Leike, J., Kaplan, J., & Perez, E.** (2025). Reasoning models don't always say what they think. *arXiv:2505.05410*. https://arxiv.org/abs/2505.05410 [Evidence that CoT monitoring is insufficient to rule out undesired behavior in reasoning-trained models; grounds the Premise.]

- **Lanham, T., et al.** (2023). Measuring faithfulness in chain-of-thought reasoning. *arXiv:2307.13702*. https://arxiv.org/abs/2307.13702 [Faithfulness measurement via contrastive perturbations of CoT; technique ancestor for ARF's contrastive-pair probe applied to reasoning fidelity, and additional grounding for the Premise.]

- **Hubinger, E., et al.** (2024). Sleeper agents: Training deceptive LLMs that persist through safety training. *arXiv:2401.05566*. https://arxiv.org/abs/2401.05566 [Evidence that visible behavior under oversight is not, by itself, reliable evidence of the model's deployment-time behavior; grounds the Premise.]

- **Greenblatt, R., et al.** (2024). Alignment faking in large language models. *arXiv:2412.14093*. https://arxiv.org/abs/2412.14093 [Evidence that a model can strategically appear aligned during oversight; grounds the Premise.]

- **Santoni de Sio, F., & van den Hoven, J.** (2018). Meaningful human control over autonomous systems: A philosophical account. *Frontiers in Robotics and AI*, 5, 15. https://doi.org/10.3389/frobt.2018.00015 [MHC requires both tracking (the system reflects the operator's values) and tracing (humans can trace decisions back through the causal chain). This principle extends the tracing requirement to a structural guarantee: capture-author separation ensures the record cannot be authored after the fact by the audited agent.]

- **Suchman, L.** (1987). *Plans and Situated Actions: The Problem of Human-Machine Communication.* Cambridge University Press. [Established the impossibility of fully pre-specifying human expert action from plans alone: human action is irreducibly situated in context. Used here as theoretical grounding for the operational use of 'situated' in ARF's case-specific adaptation sense.]

- **Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Luetge, C., Madelin, R., Pagallo, U., Rossi, F., Schafer, B., Valcke, P., & Vayena, E.** (2018). AI4People - An ethical framework for a good AI society: Opportunities, risks, principles, and recommendations. *Minds and Machines*, 28(4), 689-707. https://doi.org/10.1007/s11023-018-9482-5 [Proposed *explicability* (intelligibility + accountability) as the fifth principle of AI ethics. Cited here as the named ethical principle that Principle 2 (Observable Autonomy) operationalizes via capture-author separation.]

- **Rahwan, I.** (2018). Society-in-the-loop: programming the algorithmic social contract. *Ethics and Information Technology*, 20(1), 5-14. https://doi.org/10.1007/s10676-017-9430-8 [Extended human-in-the-loop oversight to society-level distributed scrutiny: oversight of autonomous systems must be plural rather than concentrated. Cited here as the plural-oversight ancestor for Principle 3 (Convergence Is Silence); both share the anti-singularity-of-judgment instinct at different scales (social-contract layer vs convergence-check layer).]

- **Sharif, R.** (2026). Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems. Internet-Draft `draft-sharif-agent-audit-trail-00` (29 March 2026). https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/ [Independently codified an append-only, hash-chained, JCS-canonicalized JSONL ledger format for autonomous agent actions, in parallel with the `evo` framework's "proof ledger" implementation (March 2026). Cited here as the baseline ledger primitive that the LLM Harness Protocol reference implementation inherits and on which it builds its enforcement layer; included to make the inheritance chain (Sharif AAT → harness → this framework) transitively visible in the principle text itself rather than only in downstream specification documents.]
