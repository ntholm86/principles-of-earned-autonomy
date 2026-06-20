# The Problem

*What this work is trying to solve.*

> **Authorship & License**
> Author: Nils Wendelboe Holmager | Date: April 2026
> This philosophical framework and documentation are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

---

## Digest (60 seconds)

**Two problems, one framework:**

1. **Autonomous reasoning**: How do we structure the relationship between human and AI so the AI must *interpret* the mission and *adapt* to the situation rather than execute prescribed steps?
2. **Earned autonomy**: How do we make that reasoning visible enough that different observers can justify granting or withholding authority, on evidence?

Neither can be solved alone. Observable compliance is not evidence of thought. Hidden reasoning is not a basis for trust. The framework is an **evidence substrate**: it produces the conditions on which trust *can* form, for five observer classes (practitioner, deployer, regulator, liability bearer, the agent itself). It does not manufacture trust, guarantee correctness, or solve the social conditions for delegation.

The property the framework is designed to measure is **Autonomous Reasoning Fidelity (ARF)** - the external signal that genuine, situated reasoning is both occurring and visible. ARF is validated by independent, diverse scrutiny.

The operational discipline that connects the two problems is **delegability**: bounded, revocable authority granted on visible, situated reasoning, withdrawable on the same evidence.

The claimed contribution is the combination as a proposed governance framework: Commander's Intent, Observable Autonomy, and Convergence Is Silence together as a discipline for earned, observable, revocable delegation. This is a step toward that governance problem, not a claim that the full problem is solved.

The framework's working hypothesis is that actors cause harm when they lack sufficient context to reason well about consequences, and when that reasoning cannot be checked by those responsible for the outcome. AI agents are the instance the operational machinery addresses, but the structural pattern is general. This leads to a different diagnosis than restriction-first governance assumes; the comparative argument is in [What Existing Work Does and Does Not Solve](#what-existing-work-does-and-does-not-solve).

---

## Index

- [The Two Problems](#the-two-problems)
- [Delegability: the connecting discipline](#delegability-the-connecting-discipline)
- [Who the Evidence Must Serve](#who-the-evidence-must-serve)
- [What the Framework Measures: Autonomous Reasoning Fidelity](#what-the-framework-measures-autonomous-reasoning-fidelity)
- [What Existing Work Does and Does Not Solve](#what-existing-work-does-and-does-not-solve)
- [What Must Be Built on Top](#what-must-be-built-on-top)
- [Out of Scope: What This Framework Does Not Solve](#out-of-scope-what-this-framework-does-not-solve)
- [The Working Hypothesis](#the-working-hypothesis)

---

## The Two Problems

### Problem 1: Autonomous Reasoning

Most AI systems follow instructions, some brilliantly. But following instructions is not reasoning. An agent given a checklist executes the checklist. Its ceiling is the checklist. It finds what the checklist described and misses what the checklist didn't mention. It cannot adapt to a situation the instruction author never anticipated.

The alternative is an agent that receives a mission (*what* must be achieved and *why*) and determines *how* based on what it actually encounters. The human defines the objective; the agent determines the method. This is the difference between compliance and reasoning.

This matters because consequential domains are not checklists. A nurse's patient is not a textbook case. An engineer's system has quirks the documentation doesn't cover. The situations that matter most depart from the expected pattern, and an agent that can only follow prescribed steps will fail precisely when it is needed most.

> **Problem 1:** How do you structure the relationship between human and AI so that useful performance depends on the AI interpreting objectives, adapting to context, and discovering what matters, rather than merely executing prescribed steps?

### Problem 2: Earned Autonomy

Even if an AI system is reasoning well, nobody can see it.

Outputs may be correct. Decisions may be sound. But from the outside, genuine reasoning and sophisticated pattern-matching produce identical-looking results. A human who grants authority to a system whose reasoning is invisible has abdicated.

This is not only technical. It is institutional and psychological. People do not delegate meaningful authority to systems they cannot inspect, challenge, explain, or revoke. Organizations cannot insure what they cannot audit. Regulators cannot certify what they cannot examine. Practitioners cannot stake their judgment on what they cannot interrogate.

> **Problem 2:** On what basis should a human, team, or institution decide that this agent has earned autonomy in this context, for this scope, right now, and what evidence justifies that judgment?

### Why They Must Be Solved Together

Observable autonomy without genuine reasoning gives a window into compliance. You can see every step, but the steps were prescribed, so the observation confirms obedience, not thought. Trust calibrated to compliance is fragile: it breaks the first time the situation departs from the script.

Genuine reasoning without observable autonomy gives an unverifiable claim. The agent may be reasoning brilliantly or hallucinating confidently, and nobody can tell. The capability is real but invisible, so it cannot serve as the basis for granting authority.

Both together produce something qualitatively different: an agent that reasons freely about what to do AND makes that reasoning visible enough for observers to judge whether it justifies the authority being granted. The reasoning is the substance. The visibility is the evidence. Neither is sufficient without the other.

**Scope clarification.** In comparatively prescribable domains (commercial aviation, assembly-line automation), earned autonomy is established through layered oversight: certification, written procedures, human-factors training, continuous monitoring, and maintenance regimes. Even there, autonomy is not granted by capability alone; it rests on a long-running discipline of visible evidence and revocable authority. This framework targets domains with **irreducible novelty**: medicine, law, engineering, analysis - domains where the situations that matter most cannot be fully anticipated by any checklist, and where the same evidence-based, revocable-authority logic must be reconstructed in operational form for agents whose every case may differ.

---

## Delegability: the connecting discipline

The discipline that connects both problems is **delegability**: the operational practice of converting demonstrated, visible, situated reasoning into *bounded, revocable* authority.

Delegability is distinct from capability (the model can do the task) and safety (the model won't cause harm). It is the discipline that connects what the agent *appears to be doing* to what an observer *can justifiably let it keep doing*, and can withdraw on the same evidence.

**The operational test of delegability** (asked by each observer class, answered from the trail):

1. Is the reasoning visible enough for me to judge it?
2. Is the reasoning *situated* to this case: would it have come out differently for a different case?
3. Is the *scope* of authority I'm granting bounded to what the evidence actually supports?
4. Can I *revoke* the authority on the same evidence, if the trail shows the reasoning stops being situated?

A system is delegable *here, now, at this scope* when all four answer yes. Any single "no" is a reason to narrow scope or withhold delegation, the framework functioning correctly.

The accountability problem this discipline is designed to close was named by Matthias (2004) as the 'responsibility gap': as AI systems become more autonomous, neither developer, deployer, nor machine can be fully held responsible for outcomes. Delegability is the operational response: the trail makes reasoning traceable, which makes attribution possible where the gap would otherwise exist.

---

## Who the Evidence Must Serve

Observable Autonomy (Principle 2) states that every autonomous operation must produce a visible, continuous trail. But "visible" is not a single thing. Different observers need different evidence from the same trail, and a framework for earned autonomy must account for all of them while still preserving the reasoning-fidelity question that the trail is meant to surface.

- **The practitioner** (nurse, engineer, analyst) needs case-level reasoning. *Why did the agent choose this action for this case? Did it actually reason about my specific situation, or did it pattern-match from training data?* Evidence must be specific, situated, and challengeable in the moment. Question: *Do I trust this decision, and did this agent actually think about it?*

- **The deployer** (the organization that fields the system) needs aggregate reliability. *Across a thousand cases, how often did the reasoning hold up? Where did it fail? Do failures cluster where the agent fell back to pattern-matching?* Question: *Should I keep granting this system this scope of authority?*

- **The regulator** (the body that sets standards for the domain) needs population-level validation. *Does this class of system meet the threshold for this domain? Does its success reflect genuine adaptation or brittle heuristics that only look good in aggregate?* Evidence must be standardized, reproducible, resistant to cherry-picking. Question: *Can this type of system be permitted to operate here, and on what basis do we believe its reasoning generalizes safely enough?*

- **The liability bearer** (insurer, legal entity, institution absorbing failure cost) needs tail-risk distribution. *What is the worst-case exposure? Do catastrophic failures cluster where the system stopped adapting?* Evidence must quantify downside, not just average performance. Question: *What is my exposure if this system fails in the worst way it can fail, and what does the trail say about why?*

- **The agent itself** (an autonomous system operating under these principles) has access to its own trail. It can detect when its outputs become repetitive rather than situated, when it is operating outside the scope where its autonomy was earned. Self-assessment can become self-justification, so the agent's trail must remain legible to all other observers. *The agent is an observer, never the final one.*

These observers ask different questions. They require different aggregations, time horizons, units of analysis. They all depend on the same underlying property: a trail that is continuous, legible, and structurally guaranteed by the system's architecture, not bolted on.

A framework that satisfies the practitioner but not the regulator will be adopted and then revoked. A framework that satisfies the regulator but not the practitioner will be mandated and then circumvented. A framework that satisfies neither the deployer nor the liability bearer will never reach production regardless of how good the AI's outputs are. **Earned autonomy that only one observer can verify is not yet earned.**

---

## What the Framework Measures: Autonomous Reasoning Fidelity

The target property is **Autonomous Reasoning Fidelity** (ARF). ARF is the external signal that exists only when both problems are being addressed together.

ARF is the strongest practical *external* signal this framework can produce: evidence that an agent is reasoning about what to do rather than merely complying (Problem 1) *and* that this reasoning is visible enough for observers to judge whether it justifies the autonomy being granted (Problem 2).

ARF emerges only when both principles are satisfied simultaneously:

- **Commander's Intent** creates the conditions under which interpretation and adaptation are required for good performance: the agent must engage with the mission rather than execute steps.
- **Observable Autonomy** makes the engagement visible: the trail shows *how* the agent arrived at its conclusions, not just what the conclusions were.

Neither half alone produces delegability. Unconstrained reasoning in a black box leaves the autonomy side unaddressed: no evidence an observer can act on. Visible compliance leaves the reasoning side unaddressed: evidence of obedience, not thought.

**A critical dependency.** In routine cases, situated reasoning and sophisticated pattern-matching produce identical-looking trails. The distinguishing signal emerges under *novel* conditions: when the situation departs from expected patterns and the agent must either genuinely adapt or reveal its reasoning as generic. The framework therefore requires **structured novelty** as a necessary complement to the trail. Without it, the trail documents narration, not reasoning.

**Validation.** ARF is validated by **Convergence Is Silence** (Principle 3): diverse, independent evaluators finding the same signal without consulting each other. ARF that survives diverse scrutiny is externally evidenced. ARF that only one observer ever validated is an assertion.

*(The operational definition of ARF (preconditions, situational discrimination, validation test) is in [PRINCIPLES.md](./PRINCIPLES.md#autonomous-reasoning-fidelity-operational-definition).)*

---

## What Existing Work Does and Does Not Solve

Current AI work addresses adjacent parts of both problems:

- **Capability evaluation** (MMLU, HumanEval, domain-specific benchmarks) asks whether a model can produce useful or correct outputs. It measures what the model *can do*, not whether it *reasoned* its way there or whether a human should *let it do it* unsupervised.
- **Safety and governance frameworks** (NIST AI Risk Management Framework, NIST AI 100-1, 2023; the EU AI Act, Regulation (EU) 2024/1689; ISO/IEC 42001:2023, AI management systems) *establish*, in standards bodies and binding law, that traceability, technical documentation, and human oversight are necessary for responsible deployment of high-risk AI. This framework inherits that bar wholesale - the existence of a trail and the requirement of human oversight are not contested here, they are presupposed. What these frameworks define is *that* a record must exist and *that* oversight must be possible; what they do not yet supply is the basis on which an operator judges, case by case, whether the recorded reasoning is genuine enough to justify continued or expanded delegation. That basis - evidence quality inside the trail rather than the trail's existence alone - is what this framework is built to produce.
- **Alignment and interpretability research** (RLHF, constitutional AI, mechanistic interpretability, representation engineering) makes models safer and more transparent from the inside. Within this body of work, Hubinger et al. (2024) and Greenblatt et al. (2024) are *load-bearing evidence* for the threat model this framework is built to survive: they demonstrate that even safety-trained models can exhibit deceptive or strategically-aligned behavior that is invisible at the output layer. That finding is precisely the reason capture-author separation in Observable Autonomy is structural rather than organizational - if a sufficiently capable model can produce convincing self-narration that does not reflect its actual reasoning, then a record authored by the agent itself cannot be the basis on which authority is extended. This framework therefore inherits the deceptive-alignment finding as motivation and adds the structural response: the audited agent must not be the sole author of its record, and an external observer must be able to reconstruct what the agent did and why from an artifact the agent could not unilaterally compose. Explainability and interpretability remain valuable upstream tools; this framework's contribution is the deployment-time discipline that does not depend on the agent's self-report being faithful.
- **Transparency-by-design, algorithmic accountability, and explicability** (Theodorou, Wortham & Bryson, 2017; Mittelstadt et al., 2016; Floridi et al., 2018) form a closely related ethics-and-design family. Theodorou, Wortham & Bryson argue that transparency must be designed into autonomous systems by default rather than bolted on, and must be inspectable in real time. Mittelstadt et al. catalogue six ethical concerns about algorithms (inconclusive, inscrutable, and misguided evidence; unfair outcomes; transformative effects; traceability), naming *traceability* as a precondition for accountability alongside the others - the same structural requirement arriving independently from the ethics-of-algorithms tradition rather than from the philosophy of moral responsibility that produces MHC, so the two together constitute cross-disciplinary convergence on the traceability requirement rather than duplicate citation of one idea. Floridi et al., in the AI4People framework, propose **explicability** - the union of intelligibility and accountability - as the necessary fifth principle of AI ethics alongside beneficence, non-maleficence, autonomy, and justice. This framework inherits all three: transparency as a design obligation, traceability as a precondition for accountability, and explicability as the ethical principle that any responsible autonomous deployment must satisfy. What this framework *adds* on top of that inherited ethics is operational substrate. Transparency-by-design and traceability obligations remain *behavioural* (the system displays what it is doing) and *organizational* (an auditor can reconstruct what happened); both can be satisfied by records the audited agent itself authors. Explicability as a principle does not specify the mechanism that would make it structurally enforceable rather than aspirational. Observable Autonomy proposes that mechanism: capture-author separation as a structural artifact - the audited agent cannot be the sole author of its record - so that explicability, traceability, and transparency are not contingent on the agent's self-narration being faithful. The principle is Floridi's; the mechanism that operationalizes it is this framework's contribution. (How capture-author separation is itself derived from prior security and safety design - Saltzer & Schroeder's separation of privilege and Sagan's nuclear two-person rule - is in [PRINCIPLES.md Principle 2 Origin](./PRINCIPLES.md#principle-2-observable-autonomy).)
- **Meaningful human control and trust calibration** (Santoni de Sio & van den Hoven, 2018; Lee & See, 2004) are the closest philosophical ancestry for this framework, and the diagnosis at the core of this work *is theirs* before it is restated here. Santoni and van den Hoven argued, in the context of autonomous weapons systems and the moral-responsibility gap they open, that two conditions are necessary for autonomous systems to remain under meaningful human control: a *tracking* condition (the system's behavior is responsive to the relevant human moral reasons) and a *tracing* condition (every action is traceable to a proper moral understanding by at least one human in the design or deployment chain). Lee and See established that reliance on automation must be calibrated to demonstrated capability and that calibration requires observability. This framework adopts those preconditions wholesale: traceability and calibrated reliance as necessary conditions for responsible autonomy. The seriousness of the matter is set by the domain in which Santoni's work was originally posed - lethal autonomous systems where attribution of moral responsibility cannot be allowed to dissolve - and that seriousness scales down to every other deployment in which an autonomous agent is granted authority on a human's behalf. What this framework *adds* on top of that inherited diagnosis is operational and structural. (a) MHC's tracing is an *organizational and epistemic* condition - satisfied when at least one competent human in the chain is in a position to understand. Observable Autonomy hardens tracing into a *structural* requirement: a tamper-resistant, capture-author-separated record from which an absent observer can reconstruct what the agent did and why. Where MHC says *someone understands*, this framework says *produce an artifact an outsider can audit, and do not let the audited agent be its sole author*. (b) MHC's tracking asks whether the system responds to the right moral reasons but is silent on how tasks should be *specified* to enable that responsiveness. Commander's Intent fills that gap by requiring mission-level rather than script-level specification, so interpretation is invited rather than foreclosed. (c) Neither MHC nor trust calibration provides a case-level probe to distinguish situated reasoning from templated compliance during normal operation; ARF is designed to be that probe, and Convergence Is Silence is the diverse-evaluator stopping rule that brackets it. (d) MHC asks the *backward* question - who is morally responsible when an outcome fails. This framework asks the *forward* question - given visible evidence, should this authority be extended or revoked. The diagnosis is inherited from Santoni and Lee & See; the narrowed contribution is structural Observable Autonomy plus mission-level specification plus a case-level fidelity probe, combined into an operational deployment-time discipline for earned, observable, revocable delegation.
- **Scalable oversight and process supervision** (Christiano, Shlegeris, and Amodei, 2018; Irving, Christiano, and Amodei, 2018; Lightman et al., 2023) supply the *core diagnostic premise* this framework rests on: the safety-relevant property is the quality of reasoning, not the scope of capability. Iterated Amplification (Christiano et al., 2018) builds training pipelines around supervising decomposed reasoning steps; Debate (Irving et al., 2018) exposes AI reasoning chains through adversarial play for human judgment; process supervision (Lightman et al., 2023) demonstrates that rewarding step-by-step reasoning outperforms rewarding final outputs alone. That this body of work establishes the premise is acknowledged here rather than re-derived. What this framework *adds* is the move from training-time and evaluation-time supervision to deployment-time delegation: given a capable model already in operation, how does an operator judge, in a specific case, whether its reasoning is genuinely situated rather than templated? That is the operational question ARF and Convergence Is Silence are designed to answer.
- **Prompt engineering and agent frameworks** (ReAct, chain-of-thought, tool-use architectures) improve how agents execute tasks, and the body of work around them - including faithfulness research (Turpin et al., 2023) - has already established the central problem this framework operates against: stated reasoning and actual reasoning can diverge, and the surface structure of a chain-of-thought trace does not, on its own, distinguish genuine interpretation from sophisticated pattern-matching. This framework inherits that finding as motivation. Its contribution is not to claim that the indistinguishability exists - that is settled - but to propose an operational discipline (Commander's Intent specification, capture-author-separated records, and case-level contrastive probing) under which the distinction can be made visible at the case level rather than left invisible by the prompt-and-trace surface alone.
- **Restriction-first AI governance**: a broad family of governance approaches in which trust is produced by constraining what an AI can decide and do. Concrete recent examples include frontier-lab capability-and-deployment policies (Anthropic's Responsible Scaling Policy; OpenAI's Preparedness Framework; Google DeepMind's Frontier Safety Framework) and the broader pattern set of risk-tiered authorization, allowed-states constraints, execution-bound authorization, sandboxing, deterministic policy enforcement, and separation of probabilistic advisory components from decision authority. The conceptual pair is *safety ↔ restriction*: more autonomy requires more constraint. This family addresses real problems: blast-radius containment and deterministic policy enforcement are genuine needs. Its primary concern is controlling misuse, limiting blast radius, and governing authority through safeguards and constraints. This framework starts from a different primary concern: whether an agent's reasoning in a specific case is good enough, and visible enough, to justify broader delegation on evidence. The instrument here is demonstrated reasoning quality: context that enables good reasoning (Commander's Intent supplies this), plus observable verification that the reasoning is genuinely situated rather than templated (ARF measures this). The conceptual pair: *safety ↔ demonstrated reasoning quality*. These approaches are adjacent rather than identical: restriction-first governance provides containment and guardrails, while this framework proposes a governance discipline for earned delegation in domains with irreducible novelty. The framework's downstream hypothesis is that, within the domain of non-adversarial delegation, stronger evidence of situated reasoning can justify broader authority without relying only on additional capability restriction. That claim remains a proposed direction, not a settled result. Restriction frameworks still address real safety needs; the narrower claim here is that they do not by themselves answer the delegability question this framework is designed to ask.

At the governance layer, Rahwan (2018) argues that oversight of autonomous systems must be plural and distributed rather than concentrated in a single human-in-the-loop; this framework treats the same anti-singularity-of-judgment instinct at a different scale, the convergence-check layer, in [Convergence Is Silence](./PRINCIPLES.md#principle-3-convergence-is-silence).

Positioning this work in the landscape: scalable oversight and process supervision are its closest companions on the claim that reasoning quality is safety-relevant; faithfulness and interpretability work are companions on the claim that self-report and visible process are not automatically reliable evidence; safety-and-governance frameworks and restriction-first approaches are partial companions because they address oversight, containment, and accountability. The point of divergence is narrower than any general opposition to safety work: this framework is aimed at deployment-time delegability - turning mission-level freedom, structural observability, and independent validation into a basis for earned, observable, revocable authority.

The work cited above, individually or in combination, does not yet answer the two operational questions this work cares about:

> **Is this agent genuinely reasoning about what to do, or merely complying?**
>
> **Has this agent earned the right to act more autonomously here, and what evidence justifies that judgment?**

That is the gap this work targets. Not capability, not safety, not alignment - but delegability as defined above.

These fields have not yet added up to a deployable discipline for earned autonomy grounded in externally evidenced reasoning.

---

## What Must Be Built on Top

The principles are a foundation, not a complete solution. The layers that must be built on top include:

- **Structural Execution Harnesses (Beyond Probabilistic Protocols).** Current agent implementations—such as providing instructions via the Model Context Protocol (MCP) or system prompts—rely on probabilistic compliance. The model must *choose* to write a trail or invoke a logging API. True Observable Autonomy requires the harness or the network protocol itself to capture the agent's reasoning (e.g., natively extracting deliberation payloads or `<thought>` blocks) independent of the model's behavioral choices. The principles require structural enforcement; current tooling provides behavioral polyfills. Standardizing telemetry at the protocol layer is required to close this gap. A reference implementation of this structural layer now exists: the [LLM Harness Protocol](https://github.com/ntholm86/llm-harness-proxy), a transparent MITM proxy that writes a tamper-evident, hash-chained ledger of every LLM interaction before the response is released to the caller, across OpenAI, Anthropic, and Gemini APIs. The harness demonstrates that capture-author separation can be enforced at the network layer in current tooling without client-side library changes; the broader standardization work (cross-vendor protocol adoption, deliberation-payload extraction beyond what providers currently expose) remains open.
- **Novelty and anti-compliance evaluation.** The most critical layer. Routine situations cannot distinguish situated reasoning from pattern-matching; the trails look identical. The framework needs structured novelty: cases where rote instruction-following fails but situated interpretation succeeds, adversarially underspecified situations, and distribution shifts that expose shallow compliance. Without this, the framework's central claim (that it can measure ARF) is asserted rather than tested. Formalizing ARF means turning the probe structure from a defined method into a dated, citable technical artifact: a published spec, a test harness independent of the audited agent, a curated probe dataset with pre-registered expected divergences, and a reproducibility report showing independent replication across agent families and task domains. The spec ([ARF-SPEC.md](./ARF-SPEC.md), v1.0.0), harness ([LLM Harness Protocol](https://github.com/ntholm86/llm-harness-proxy), v2.0.0), and initial probe dataset ([probes/results/](./probes/results/RESULTS.md)) now exist; validation awaits independent replication.
- **Domain-specific correctness standards.** The principles are domain-portable; the quality criteria are not. Medicine, law, and engineering each need their own definition of "correct" within the framework.
- **Legal liability and governance models.** The trail makes accountability *possible*; policy must define who bears it when earned autonomy produces a bad outcome.
- **Evaluator independence and diversity.** Convergence Is Silence requires diverse scrutiny. How evaluator pools are composed, rotated, and kept independent is an operational problem the principles define but do not solve.
- **Failure testing and revocation thresholds.** Under what conditions should earned autonomy be revoked? The trail provides the evidence; thresholds must be defined per domain.
- **Scope control as autonomy expands.** Autonomy earned in one scope does not automatically transfer to a broader one. The escalation path needs design.
- **Tail-risk quantification.** The liability bearer needs more than average performance. Worst-case exposure, failure propagation paths, and downside distributions must be extractable from the trail.
- **Long-horizon alignment.** The principles verify reasoning fidelity in the near term. Whether an agent's goals remain aligned over extended periods is a separate research problem.

These are the research and engineering agenda that sits on top of the foundation. These principles establish necessary preconditions; without them, none of the layers above can function.

---

## Out of Scope: What This Framework Does Not Solve

This framework is an **evidence substrate**, not a trust generator. It produces the conditions under which trust *can* form on observable grounds. It does not manufacture trust, guarantee adoption, or solve the social, organizational, and human-factors problems that surround autonomous AI. Naming these limits prevents the framework from being judged against claims it never made.

1. **Reviewer engagement and scaling.** Earned autonomy is meaningful only if someone evaluates the evidence. If no one reads the trail, autonomy becomes de facto unconditional regardless of how much evidence exists. If everyone reads it, the reviewer becomes the bottleneck. The framework provides a captured-as-it-happens trail and an in-trail reviewer-engagement signal so non-engagement is at least visible, but it has no answer for *how* organizations actually staff, incentivize, and sustain meaningful human review at scale. **This is the framework's deepest unresolved gap.** It is named here so it cannot be hidden by the existence of the trail.
2. **Reasoning correctness.** Transparency proves *visibility*, not *correctness*. A trail can be honest, legible, and wrong. Convergence Is Silence is the framework's primary defense against this, but it depends on diverse evaluators being available, willing, and competent. Where they are not, transparency does not save you.
3. **Human intent stability.** Commander's Intent assumes the human can articulate a destination clearly enough for the agent to interpret it. Real missions are often vague, contradictory, politically constrained, or shifting. If upstream intent is unstable, every downstream decision inherits that instability.
4. **Organizational willingness to delegate.** Many organizations do not want AI to have autonomy at all, earned or otherwise. Fear of loss of control, job displacement, liability, political consequences, and being blamed for AI mistakes are legitimate concerns the framework cannot address. The framework's claim is conditional: *if* you want to delegate, here is how to make the delegation observable. It does not argue that you should.
5. **Incentives, values, and the social layer of trust.** Reliability is one component of trust. Trust also requires shared values, aligned incentives, and demonstrated character over time, none of which the framework supplies. The framework is an **evidence substrate**, not a trust model.
6. **Domain measurability.** In some domains the next improvement is unclear, unmeasurable, or politically contested. The framework gives the agent discipline for navigating uncertainty, but it cannot manufacture a measurable target where none exists.
7. **Legal liability and accountability assignment.** The trail makes accountability *possible*; policy and law must define who bears it.
8. **Adoption and organizational psychology.** Whether stakeholders will accept the concept of "earned autonomy" at all is a sociological question the framework treats as a precondition. If the answer is no for a given organization or domain, the framework is inert there regardless of how well it functions.

These are not disclaimers added defensively. They are scope boundaries. A framework that claims to solve them would be overclaim. A framework that pretends they don't exist would be dishonest. Naming them here is itself an instance of Observable Autonomy applied to the framework's own design.

---

## The Working Hypothesis

Autonomous actors — AI systems today, but the pattern is substrate-general — cause harm when they lack sufficient context to reason well about consequences and when that reasoning cannot be checked. The framework's operational machinery targets AI because that is where the capability-governance gap is widest, but the architectural principles apply wherever self-narrating actors hold stakes in their own account.

Humanity can adopt more AI power if two conditions are met: AI systems reason about what to do rather than merely follow instructions, and that reasoning is made visible enough for autonomy to be **earned, legible, and challengeable** rather than opaque, vendor-asserted, or intuition-driven.

If that hypothesis is right, this work is not an academic exercise. It is the early articulation of an **adoption architecture for autonomous AI**: the missing layer between model capability and real-world delegation.

What may generalize across domains is not every surface instruction, threshold, or vocabulary term. What may generalize is the deeper pattern: give the agent a mission rather than a script, require a visible trail of how it reasoned, challenge the claim from diverse perspectives, and expand authority only when the evidence, of both genuine reasoning and earned trust, supports it.

The name may evolve. The function will not:

> **Give humans a practical, evidence-based way to grant AI systems more authority - by solving both the reasoning problem (is the AI genuinely interpreting and adapting to this situation?) and the trust problem (can observers justify the autonomy being granted?) - so that the enormous potential of autonomous AI becomes adoptable, not just impressive.**

---

## References

The following works are cited in this document. Inline citations appear in the body text; this section provides the full bibliographic entries for verification and further reading.

- **Christiano, P., Shlegeris, B., & Amodei, D.** (2018). Supervising strong learners by amplifying weak experts. *arXiv:1810.08575*. https://arxiv.org/abs/1810.08575 [Iterated Amplification: builds training pipelines around supervising decomposed reasoning steps; shares the diagnostic premise that reasoning quality is the safety-relevant property.]

- **Irving, G., Christiano, P., & Amodei, D.** (2018). AI safety via debate. *arXiv:1805.00899*. https://arxiv.org/abs/1805.00899 [Debate: exposes AI reasoning chains through adversarial play for human judgment; shares the diagnostic premise that reasoning quality is the safety-relevant property.]

- **Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., & Cobbe, K.** (2023). Let's verify step by step. *arXiv:2305.20050*. https://arxiv.org/abs/2305.20050 [Process supervision: demonstrates that rewarding step-by-step reasoning outperforms rewarding final outputs alone; shares the diagnostic premise that reasoning quality is the safety-relevant property.]

- **Hubinger, E., et al.** (2024). Sleeper agents: Training deceptive LLMs that persist through safety training. *arXiv:2401.05566*. https://arxiv.org/abs/2401.05566 [Cited in the alignment-and-interpretability bullet: evidence that visible behavior under oversight is not, by itself, reliable evidence of deployment-time behavior.]

- **Greenblatt, R., et al.** (2024). Alignment faking in large language models. *arXiv:2412.14093*. https://arxiv.org/abs/2412.14093 [Cited in the alignment-and-interpretability bullet: evidence that a model can strategically appear aligned during oversight.]

- **National Institute of Standards and Technology.** (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* (NIST AI 100-1). https://doi.org/10.6028/NIST.AI.100-1 [Cited as a representative safety-and-governance framework.]

- **European Union.** (2024). Regulation (EU) 2024/1689 laying down harmonised rules on Artificial Intelligence. *Official Journal of the European Union*, L 1689, 12.7.2024. https://eur-lex.europa.eu/eli/reg/2024/1689/oj [Cited as a representative safety-and-governance framework.]

- **International Organization for Standardization.** (2023). *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system*. https://www.iso.org/standard/81230.html [Cited as a representative safety-and-governance framework.]

- **Anthropic.** (2023, updated). *Responsible Scaling Policy*. https://www.anthropic.com/responsible-scaling-policy [Cited as a representative example of restriction-first frontier-lab governance.]

- **OpenAI.** (2023, updated). *Preparedness Framework*. https://openai.com/safety/preparedness [Cited as a representative example of restriction-first frontier-lab governance.]

- **Google DeepMind.** (2024). *Frontier Safety Framework*. https://deepmind.google/discover/blog/introducing-the-frontier-safety-framework/ [Cited as a representative example of restriction-first frontier-lab governance.]

- **Matthias, A.** (2004). The responsibility gap: Ascribing responsibility for the actions of learning automata. *Ethics and Information Technology*, 6(3), 175-183. https://doi.org/10.1007/s10676-004-3422-1 [Named the accountability gap that emerges when AI systems become sufficiently autonomous that neither developer, deployer, nor machine can be fully held responsible for outcomes. Delegability is the operational response: the trail makes reasoning traceable and attribution possible.]

- **Santoni de Sio, F., & van den Hoven, J.** (2018). Meaningful human control over autonomous systems: A philosophical account. *Frontiers in Robotics and AI*, 5, 15. https://doi.org/10.3389/frobt.2018.00015 [Closest philosophical companion. MHC's tracking and tracing conditions are extended here: tracing is hardened from an organizational/epistemic condition into a structural Observable Autonomy requirement (capture-author separation, tamper resistance), and the forward-looking delegability frame replaces MHC's backward-looking responsibility-attribution frame.]

- **Lee, J. D., & See, K. A.** (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50-80. https://doi.org/10.1518/hfes.46.1.50_30392 [Established that reliance on automation must be calibrated to demonstrated capability and that calibration requires observability. Cited here as the operational companion to MHC on the prior-work line.]

- **Theodorou, A., Wortham, R. H., & Bryson, J. J.** (2017). Designing and implementing transparency for real time inspection of autonomous robots. *Connection Science*, 29(3), 230-241. https://doi.org/10.1080/09540091.2017.1310182 [Established transparency-by-design as a default requirement for autonomous systems, with real-time inspectability for designers and users. Cited here as the design-time transparency ancestor; this framework adds the structural mechanism (capture-author separation) that makes transparency hold even when the audited agent is the one producing the transparency output.]

- **Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S., & Floridi, L.** (2016). The ethics of algorithms: Mapping the debate. *Big Data & Society*, 3(2), 2053951716679679. https://doi.org/10.1177/2053951716679679 [Mapped six ethical concerns about algorithms, naming traceability as a precondition for accountability. Cited here as part of the ethics-and-accountability family this framework inherits; the structural traceability addition is named in the body.]

- **Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Luetge, C., Madelin, R., Pagallo, U., Rossi, F., Schafer, B., Valcke, P., & Vayena, E.** (2018). AI4People - An ethical framework for a good AI society: Opportunities, risks, principles, and recommendations. *Minds and Machines*, 28(4), 689-707. https://doi.org/10.1007/s11023-018-9482-5 [Proposed *explicability* (intelligibility + accountability) as the fifth principle of AI ethics. Cited here as the named ethical principle that this framework's Principle 2 operationalizes via capture-author separation.]

- **Rahwan, I.** (2018). Society-in-the-loop: programming the algorithmic social contract. *Ethics and Information Technology*, 20(1), 5-14. https://doi.org/10.1007/s10676-017-9430-8 [Cited at the governance layer as the plural-oversight ancestor for Convergence Is Silence; both share the anti-singularity-of-judgment instinct at different scales (social-contract layer vs convergence-check layer).]
