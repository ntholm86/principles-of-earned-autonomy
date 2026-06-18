# Changelog

## v2.0.3 - 2026-06-18

### Changed

- **PRINCIPLES.md Principle 2 Origin paragraph extended with transitional-justice citation.** The architectural response (capture-author separation) is now shown as cross-domain to match the now-cross-domain premise. The Origin paragraph previously cited Saltzer & Schroeder (1975, security/access-control) and Sagan (1993, nuclear authorization). It now adds Hayner (2011, transitional justice): truth commissions prohibit perpetrators from authoring the sole account of their actions, constructing the official record through independent testimony and documentary evidence instead. Three domains — security, nuclear authorization, transitional justice — now demonstrate the same structural pattern: the party that acts must not be the sole author of the record of its actions. Full bibliographic entry for Hayner added to PRINCIPLES.md References.

  Files changed: `PRINCIPLES.md`.

- **Metadata version bumped to 2.0.3.**

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v2.0.2 - 2026-06-18

### Changed

- **PRINCIPLES.md Digest and Premise opener updated to substrate-general framing.** v2.0.1 added a Cross-domain confirmation subsection establishing that unreliable self-narration is a property of any self-narrating actor with stakes, not just LLMs. This release propagates that framing to the two surfaces that still used LLM-specific language:

  1. **Full Premise opener (line 32):** Changed "an LLM agent's account of its own reasoning is not reliable evidence of that reasoning" to "a self-narrating actor with stakes in its own account is not a reliable narrator of its own reasoning. LLM agents are one instance — the instance this framework's operational machinery is built for."
  
  2. **Digest premise description (line 18):** Changed detailed AI-specific evidence ("stated reasoning is not internal reasoning; self-correction often degrades performance...") to the cross-domain framing: "Self-narration under self-interest is structurally unreliable — a property cognitive science established in humans and AI alignment research confirmed in LLMs."
  
  The two-senses-of-domain distinction is preserved: *applicability* is general (any self-narrating actor with stakes); *operational demonstration* is AI-only (the framework's machinery is built for LLM agents). No changes to PROBLEM.md — its AI-focus is correct because it describes the application domain.

  Files changed: `PRINCIPLES.md`.

- **Metadata version bumped to 2.0.2.**

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v2.0.1 - 2026-06-18

### Changed

- **PRINCIPLES.md Premise section extended with a Cross-domain confirmation subsection.** The premise that self-narrating actors with stakes in their own narration produce structurally unreliable accounts was independently established in cognitive science decades before AI made it measurable. New subsection added between "The evidence" (AI-literature citations) and "The implication" (architectural-response reasoning). It names four cognitive-science citations - Festinger (1957) cognitive dissonance, Nisbett & Wilson (1977) confabulation, Kunda (1990) motivated reasoning, Trivers & von Hippel (2011) self-deception - and applies Principle 3 to the cross-tradition convergence itself: two independent academic traditions (cognitive science from the late 1950s onward and AI alignment research from the early 2020s) developed the same finding through disjoint methods on disjoint substrates, which is, by this framework's own stopping condition, the strongest available evidence that unreliable self-narration is a structural property rather than incidental to either domain. LLM agents are framed as one instance in a class that includes humans; the AI literature is the contemporary measurement of a structural property cognitive science had already established. The architectural response (capture-author separation) is connected back to its existing security and authorization lineage (Saltzer & Schroeder, 1975; Sagan, 1993) as the same answer to the same problem shape across domains. Full bibliographic entries for the four new citations added to PRINCIPLES.md References. The existing AI-specific premise wording, the three-role separation, the LLM-specific implication paragraph, and the principle definitions are unchanged - the change strengthens the premise's grounding by extension rather than reopening any core text.

  Files changed: `PRINCIPLES.md`.

- **Metadata version bumped to 2.0.1.** Release surfaces kept in sync.

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v2.0.0 - 2026-06-04

Major version bump: the framework's evidentiary status materially changes from *principle proposed* to *principle demonstrated buildable*. A reference implementation of the structural layer Principle 2 requires has been published separately as the [LLM Harness Protocol](https://github.com/ntholm86/LLM-harness-protocol), a transparent MITM proxy that writes a tamper-evident, hash-chained, append-only ledger of every LLM interaction before the response is released to the caller, across OpenAI, Anthropic, and Gemini APIs. Capture-author separation is therefore no longer an aspirational property of this framework but a buildable one with a working reference. The harness does not, on its own, validate ARF; it removes the structural blocker (instrument-and-subject sharing a single point of failure) that previously prevented trustworthy ARF measurement under MCP-only tooling.

### Changed

- **README.md** acknowledges two reference implementations rather than one: Skills Suite (principles applied to an artifact) and Harness Protocol (structural layer that makes Principle 2 enforceable independent of the audited agent's compliance).
- **PROBLEM.md "Structural Execution Harnesses" bullet** in *What Must Be Built on Top* now notes that a reference implementation of the structural layer exists, while preserving the open standardization agenda (cross-vendor protocol adoption, deliberation-payload extraction).
- **PRINCIPLES.md Principle 2 "Why structural capture is required"** adds a paragraph naming the harness as the reference implementation of capture-author separation at the network layer.
- **PRINCIPLES.md "The instrument-inheritance limit"** revised to reflect that the structural substrate has been built. ARF measurement is now blocked on the probe dataset, the test harness around the proxy, and the reproducibility report, not on the absence of the structural layer itself. Wording is careful not to overstate: ARF as a construct may still hold; whether it does remains to be tested with that scaffolding in place.
- **PROOF.md** restructured to carry two bounded reference implementations: Reference Implementation A (Skills Suite, the prior conformance evidence) and Reference Implementation B (Harness Protocol). New Reference Implementation B section documents what the harness establishes (capture-author separation buildable at the protocol layer across three providers) and what it does not (ARF validation, third-party replication of the probe dataset).
- **PROOF.md claims table** extended with two new supported claims (capture-author separation buildable; multi-provider fail-closed ledger operable without provider cooperation) and one new not-yet-supported claim (pre-registered ARF probe administered through the harness with independent replication). The claim *"harness, on its own, validates ARF"* is explicitly marked not supported.
- **EMPIRICAL_EVIDENCE.md Failure C** now points forward to the harness as the structural response that motivated its construction: the failure motivated the requirement; the harness is the structural mechanism that enforces it.

### Metadata

- Version bumped to 2.0.0. CITATION.cff, .zenodo.json, CHANGELOG.md kept in sync.

---

## v1.9.9 - 2026-06-04

### Changed

- **PROBLEM.md transparency-and-accountability bullet sharpened on three load-points** identified by a publication-rigour-review pass over v1.9.8. (1) Mittelstadt's contribution is now distinguished from MHC's tracing rather than listed alongside it: both identify traceability as a structural requirement, but Mittelstadt arrives from ethics-of-algorithms while Santoni & van den Hoven arrive from philosophy of moral responsibility, so citing both is cross-disciplinary convergence rather than duplicate citation. (2) The Floridi-operationalization claim now carries an explicit pointer to PRINCIPLES.md Principle 2 Origin, where capture-author separation is itself derived from Saltzer & Schroeder's separation of privilege and Sagan's nuclear two-person rule; the chain from Floridi's normative principle to the structural mechanism's own ancestry is now visible in one read. (3) The restriction-first governance bullet now mentions Rahwan (2018) at the governance layer with a forward pointer to Convergence Is Silence in PRINCIPLES.md, closing the gap where Rahwan was anchored as a Principle 3 ancestor without any acknowledgment in the prior-work landscape.

  Files changed: `PROBLEM.md`.

- **Metadata version bumped to 1.9.9.** Release surfaces kept in sync.

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v1.9.8 - 2026-06-04

### Changed

- **PROBLEM.md prior-work section now engages the transparency-by-design, algorithmic accountability, and explicability family.** A new combined bullet positions Theodorou, Wortham & Bryson (2017), Mittelstadt et al. (2016), and Floridi et al. (2018, AI4People) as inherited ancestry on three intertwined fronts: transparency as a design obligation, traceability as a precondition for accountability, and explicability as the necessary fifth principle of AI ethics. The bullet applies the inheritance-acknowledging pattern (state what is inherited, then state what is added on top): this framework inherits all three obligations; Observable Autonomy proposes the structural mechanism (capture-author separation) that makes them operationally enforceable rather than satisfiable by records the audited agent itself authors. Full bibliographic entries for Theodorou/Wortham/Bryson, Mittelstadt, and Floridi added to PROBLEM.md References.

  Files changed: `PROBLEM.md`.

- **PRINCIPLES.md theoretical anchors expanded with Floridi's explicability principle and Rahwan's society-in-the-loop.** Two anchors added to the ARF Theoretical anchors block: (a) explicability as the named AI-ethics principle that Principle 2 operationalizes (Floridi et al., 2018) - capture-author separation makes explicability enforceable as an artifact rather than aspirational as a principle; (b) society-in-the-loop (Rahwan, 2018) as the plural-oversight ancestor for Principle 3 - both share the anti-singularity-of-judgment instinct at different scales (social-contract layer vs convergence-check layer). Full bibliographic entries for Floridi and Rahwan added to PRINCIPLES.md References.

  Files changed: `PRINCIPLES.md`.

- **Metadata version bumped to 1.9.8.** Release surfaces kept in sync after the comparator-coverage edits.

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v1.9.7 - 2026-06-04

### Changed

- **PROBLEM.md prior-work bullets reworked through the inheritance-acknowledging pattern.** Three bullets that previously read as gap-mining against respected prior work now state explicitly what this framework *inherits* before stating what it *adds*:
  - *Safety and governance frameworks*: NIST RMF, the EU AI Act, and ISO/IEC 42001 are now credited with *establishing*, in standards and binding law, that traceability, technical documentation, and human oversight are necessary. This framework inherits that bar wholesale and adds the deployment-time question of evidence quality inside the trail rather than trail existence alone.
  - *Alignment and interpretability research*: Hubinger et al. (2024) and Greenblatt et al. (2024) are now positioned as load-bearing evidence for the threat model this framework is built to survive. Their finding that safety-trained models can exhibit deceptive or strategically-aligned behavior invisible at the output layer is the reason capture-author separation in Observable Autonomy is structural rather than organizational. Inherits the deceptive-alignment finding as motivation; adds the structural response.
  - *Scalable oversight and process supervision*: Christiano et al. (2018), Irving et al. (2018), and Lightman et al. (2023) are now credited with *supplying the core diagnostic premise* (reasoning quality is the safety-relevant property) rather than merely sharing it. Inherits the premise; adds the move from training-time and evaluation-time supervision to deployment-time delegation.
  - *Prompt engineering and agent frameworks*: faithfulness research (Turpin et al., 2023) is now credited with establishing the divergence between stated and actual reasoning. The framework inherits that finding as motivation rather than re-asserting it.

  Files changed: `PROBLEM.md`.

- **PRINCIPLES.md Principle 2 "Origin" paragraph now carries a formal citation for the nuclear two-person rule.** Sagan, S. D. (1993). *The Limits of Safety: Organizations, Accidents, and Nuclear Weapons* (Princeton University Press) is the canonical scholarly source for separation-of-privilege as a structural safeguard in nuclear weapons release. Inline cite added next to the two-person-rule sentence; full bibliographic entry added to References next to Saltzer & Schroeder (1975).

  Files changed: `PRINCIPLES.md`.

- **Metadata version bumped to 1.9.7.** Release surfaces kept in sync after the prior-work reframe and the Sagan citation.

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v1.9.6 - 2026-06-04

### Changed

- **PROBLEM.md MHC bullet reframed from "closest companion / gaps" to "inherited diagnosis / what this work adds on top".** The diagnosis at the core of this framework - that traceability and reason-responsiveness are necessary preconditions for responsible autonomy - is now stated explicitly as Santoni de Sio & van den Hoven's (2018) and Lee & See's (2004), inherited wholesale rather than re-derived. The original autonomous-weapons context of Santoni's work is named to set the seriousness of the matter and to make clear that the framework scales the same logic down to every deployment in which an autonomous agent is granted authority on a human's behalf. The four contributions this work *adds* on top of that inherited diagnosis (structural tracing, mission-level specification, case-level fidelity probe, forward-looking delegability) are retained but now positioned as additions to a load-bearing ancestor rather than as gaps in a competitor. This is the clearer separation between what is borrowed and what is new.

  Files changed: `PROBLEM.md`.

- **PRINCIPLES.md Principle 2 "Origin" paragraph now cites the nuclear two-person rule alongside Saltzer & Schroeder 1975.** Adds a sentence noting that the separation-of-privilege pattern is the load-bearing safeguard in the highest-stakes systems humans have built, with the two-person rule on nuclear weapons release as the starkest instance: no single operator can authorize launch and no single party can fabricate the authorization record. This makes the cross-domain precedent for Observable Autonomy's capture-author separation visible to readers who would otherwise treat the access-control origin as narrowly technical.

  Files changed: `PRINCIPLES.md`.

- **Metadata version bumped to 1.9.6.** Release surfaces kept in sync after the MHC reframe and the Principle 2 origin addition.

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v1.9.5 - 2026-06-04

### Changed

- **PROBLEM.md "What Existing Work Does and Does Not Solve" now explicitly engages Meaningful Human Control and trust-calibration literature.** A new bullet positions Santoni de Sio & van den Hoven (2018) and Lee & See (2004) as the closest philosophical companions, names MHC's *tracking* and *tracing* conditions, and narrows this framework's contribution after them to four moves: (a) extending MHC's organizational tracing into a structural Observable Autonomy requirement via capture-author separation and tamper resistance; (b) Commander's Intent as a mission-vs-script specification discipline absent from MHC; (c) ARF and Convergence Is Silence as a case-level fidelity probe and diverse-evaluator stopping rule that neither MHC nor trust calibration supplies; (d) a forward-looking delegability frame (authority extension and revocation on visible evidence) instead of MHC's backward-looking responsibility-attribution frame. Closes a prior-art omission a hostile reviewer would otherwise treat as uniqueness by omission. Full bibliographic entries for MHC and Lee & See added to PROBLEM.md References.

  Files changed: `PROBLEM.md`.

- **PROBLEM.md scope clarification softened.** The prescribable-domain contrast no longer asserts that aviation and assembly-line autonomy are settled by "static certification" and "exhaustive testing". It now describes those as *comparatively* prescribable domains in which earned autonomy is established through layered oversight (certification, written procedures, human-factors training, continuous monitoring, maintenance), and frames this framework as reconstructing the same evidence-based, revocable-authority logic in operational form for domains of irreducible novelty. Removes avoidable pushback from safety-critical-systems readers.

  Files changed: `PROBLEM.md`.

- **EMPIRICAL_EVIDENCE.md EU AI Act corroboration narrowed.** Removed the "regulators worldwide have independently converged on the same conclusion" claim and the "most comprehensive AI regulatory framework enacted anywhere" superlative. The paragraph now scopes the conclusion to EU-level corroboration of the traceability requirement, names the specific articles already cited above (Articles 11, 12, 14), and adds an explicit boundary sentence stating that stronger worldwide-convergence claims would require additional jurisdictions and are not made here. Preserves the corroborative force without overclaiming.

  Files changed: `EMPIRICAL_EVIDENCE.md`.

- **Metadata version bumped to 1.9.5.** Release surfaces kept in sync after the prior-work, scope, and EU-evidence edits.

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v1.9.4 - 2026-06-04

### Changed

- **PRINCIPLES.md ARF section now names the instrument-inheritance limit explicitly.** A new paragraph in the Autonomous Reasoning Fidelity (operational definition) section states that under current LLM tooling (Model Context Protocol, system prompts, skill scaffolding), an ARF probe administered to an agent is itself executed by that agent, so the probe inherits the same failure modes Principle 2 names in the subject. Instrument and subject share a single point of failure. The paragraph frames this as Principle 2 making its own prediction concrete - the framework's measurement construct is the worked example of why behavioral-layer governance cannot structurally enforce its own preconditions - and names the structural fix as living at the protocol layer (execution harnesses that capture probe execution outside the model's authorship). ARF as a construct may still hold; whether it does cannot be proven under MCP-only tooling. Published ARF measurement requires the structural substrate the framework already names as missing.

  Files changed: `PRINCIPLES.md`.

- **Metadata version bumped to 1.9.4.** Release surfaces kept in sync after the PRINCIPLES.md addition.

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v1.9.3 - 2026-06-03

### Changed

- **PROBLEM.md now includes an explicit prior-art positioning paragraph.** The existing-work section now names the nearest companions, partial companions, and principal point of divergence in one compact paragraph. This makes the manuscript's landscape claim easier for a cold reader to parse without inferring it from multiple bullets.

  Files changed: `PROBLEM.md`.

- **Metadata version bumped to 1.9.3.** Release surfaces were kept in sync after the new positioning paragraph was added.

  Files changed: `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md`.

---

## v1.9.2 - 2026-06-03

### Changed

- **Contribution framing now states the real novelty more directly.** README.md, PROBLEM.md, and PRINCIPLES.md now say explicitly that the claimed contribution is not the isolated claim that reasoning matters or that self-narration is unreliable. The claimed contribution is the synthesis as a proposed governance framework for earned delegation: Commander's Intent, Observable Autonomy, and Convergence Is Silence combined into a discipline of earned, observable, revocable authority. The same pass also makes the humility posture explicit: this is presented as a step toward deployable governance for delegability, not a claim to have solved the full safety or measurement landscape.

  Files changed: `README.md`, `PROBLEM.md`, `PRINCIPLES.md`.

- **Citation and Zenodo metadata aligned to the contribution framing.** CITATION.cff and .zenodo.json now describe the work as a proposed governance synthesis rather than implying a standalone novelty claim for ARF by itself.

  Files changed: `CITATION.cff`, `.zenodo.json`.

- **PROBLEM.md restriction-first comparison softened to match the narrower contribution claim.** The restriction-first paragraph now frames those approaches as adjacent governance families with a different primary concern rather than landing the contrast as a total incompatibility claim. It now says more clearly that the manifesto's narrower claim is about delegability under non-adversarial delegation, and that stronger evidence of situated reasoning is a downstream hypothesis rather than a settled result.

  Files changed: `PROBLEM.md`.

---

## v1.9.1 - 2026-06-03

### Changed

- **PRINCIPLES.md: Meaningful Human Control now carries a full citation and differentiation.** Both inline appearances of "Meaningful Human Control" now cite Santoni de Sio & van den Hoven (2018) rather than the uncited "(autonomous systems ethics)" placeholder. The ARF theoretical-anchors bullet now distinguishes MHC's tracking-and-tracing requirements from this principle's novel contribution: capture-author separation extends the tracing requirement to a structural guarantee rather than an organisational assumption. Full bibliographic entry added to the References section.

  Files changed: `PRINCIPLES.md`.

- **PRINCIPLES.md: "Situated" reasoning now carries a Suchman (1987) parenthetical.** The ARF situational-discrimination paragraph now clarifies that "situated" is used in the operational sense of case-specific adaptation rather than the broader situated-action-theory tradition (Suchman, 1987), and notes that Suchman established the same impossibility of full pre-specification for human expert action that this framework extends to AI agents. Full bibliographic entry added to the References section.

  Files changed: `PRINCIPLES.md`.

- **PROBLEM.md: Matthias (2004) responsibility gap cited in Delegability section.** A sentence added to the end of the Delegability section connects the framework's operational response (delegability via traceable reasoning) to Matthias's named philosophical problem (the responsibility gap: increasing AI autonomy creates accountability gaps that cannot be closed by restriction alone). Full bibliographic entry added to the References section.

  Files changed: `PROBLEM.md`.

- **EMPIRICAL_EVIDENCE.md: AI Index connector claim scoped correctly.** Section 6's connector changed from "is the responsible AI measurement the AI Index identifies as missing" to "is one critical instance of the responsible AI measurement gap the AI Index identifies" to avoid overstating what Takeaway #5 specifically names.

  Files changed: `EMPIRICAL_EVIDENCE.md`.

- **CITATION.cff abstract now carries the operator-independence caveat.** The three-family silence-convergence run is now described as "single-operator-administered" in the abstract, matching the bounded-evidence framing already stated in PROOF.md. Version bumped to 1.9.1.

  Files changed: `CITATION.cff`, `.zenodo.json`.

---

## v1.9.0 - 2026-06-03

### Changed

- **PROOF.md now anchors its reference evidence to the public, append-only audit trail of the implementation it cites.** The "Reference evidence" section explicitly names the artifact under test (the Principles of Earned Autonomy Skills Suite), links to its public audit trail at `https://github.com/ntholm86/principles-of-earned-autonomy-skills-suite/blob/main/.trail/audit-trail.md`, and identifies, by dated entry slug, the specific trail entries that back each principle paragraph and the falsification narrative. The Principle 1, 2, and 3 paragraphs now cite the `2026-04-24` entries `v3-silence-1`, `v3-silence-2`, `v3-silence-3`, `cross-layer-coherence`, and `trail/README.md drift fix` directly. A new transparency paragraph after Principle 3 records that the three evaluators differed by model family but were administered by a single operator, so the minimum-bar test in PRINCIPLES.md is not fully cleared by this single piece of evidence. The falsification wording was tightened to match the actual finding (documentation drift in the suite's `trail/README.md`: stale directory structure and retired v2 skill vocabulary in the glossary), rather than the previous looser "principle name did not match" framing.

  Files changed: `PROOF.md`.

- **Premise of PRINCIPLES.md extended with additional grounding literature.** Added inline citations to Lanham et al. (2023), *Measuring Faithfulness in Chain-of-Thought Reasoning*, as further evidence that stated reasoning can diverge from internal reasoning; and added Hubinger et al. (2024), *Sleeper Agents*, and Greenblatt et al. (2024), *Alignment Faking in Large Language Models*, as evidence that visible behavior under oversight is not, by itself, reliable evidence of deployment-time behavior. The ARF "Technique ancestry" paragraph now cites Lanham et al. (2023) alongside the Winograd Schema Challenge and CheckList, with an explicit differentiation between single-trace faithfulness measurement and ARF's case-pair reasoning-fidelity check. Full bibliographic entries added to the References section.

  Files changed: `PRINCIPLES.md`.

- **PROBLEM.md "What Existing Work Does and Does Not Solve" section now carries inline citations for the comparison.** The Safety-and-governance bullet now cites NIST AI 100-1 (2023), Regulation (EU) 2024/1689 with OJ reference, and ISO/IEC 42001:2023. The Alignment-and-interpretability bullet now cites Hubinger et al. (2024) and Greenblatt et al. (2024). The Restriction-first bullet now names Anthropic's Responsible Scaling Policy, OpenAI's Preparedness Framework, and Google DeepMind's Frontier Safety Framework as concrete recent examples of the family it describes, ahead of the broader pattern set; the canonical reasoning-quality-vs-restriction argument later in the bullet is unchanged. The summary line was softened from "None of these fields, individually or together, yet answer..." to "The work cited above, individually or in combination, does not yet answer..." Full bibliographic entries added.

  Files changed: `PROBLEM.md`.

- **EMPIRICAL_EVIDENCE.md citation fidelity tightened for the external-evidence sections.** Section 5 (EU AI Act) replaces verbatim quoted phrases with explicit paraphrases and cites the OJ reference plus Articles 11, 12, and 14 of Regulation (EU) 2024/1689 directly. Section 6 (Stanford AI Index 2026) replaces the verbatim Takeaway #5 quote with an explicit paraphrase while retaining the source citation; downstream connector phrasing was adjusted to match.

  Files changed: `EMPIRICAL_EVIDENCE.md`.

- **CITATION.cff abstract tightened to match the actual evidence shape.** Replaced "empirical evidence from a three-family silence-convergence test" with "bounded reference evidence from one implementation (a three-family silence-convergence run ... anchored to a public append-only audit trail)" so the abstract matches the bounded-evidence framing now made explicit in PROOF.md, and added Lanham et al. (2023) to the named technique ancestry.

  Files changed: `CITATION.cff`.

- **Version bumped to 1.9.0** across `CITATION.cff` and `.zenodo.json` to reflect the citation-and-evidence-fidelity pass.

  Files changed: `CITATION.cff`, `.zenodo.json`.

---

## v1.8.3 - 2026-06-03

### Changed

- **Private manuscript-history references removed from public documents.** EMPIRICAL_EVIDENCE.md, README.md, and PROOF.md no longer discuss private working artifacts or repository history. The public-facing documents now speak only about the released evidence surfaces and the framework itself.

  Files changed: `EMPIRICAL_EVIDENCE.md`, `README.md`, `PROOF.md`.

---

## v1.8.2 - 2026-06-03

### Changed

- **Evidence-layer separation clarified.** EMPIRICAL_EVIDENCE.md now explicitly states that sections 1-4 document a formative case from the framework's synthesis rather than the manifesto's load-bearing evidence base, and README.md and PROOF.md were aligned to the same distinction.

  Files changed: `EMPIRICAL_EVIDENCE.md`, `PROOF.md`, `README.md`.

---

## v1.8.1 - 2026-06-03

### Changed

- **Publication-calibration pass across EMPIRICAL_EVIDENCE.md, README.md, PRINCIPLES.md, and PROBLEM.md.** The public-evidence language around the internal behavioral-alignment experiment is now calibrated so the section distinguishes between the developmental case itself and the external corroboration that follows. Proof-language was narrowed to observation/report language.

  Files changed: `EMPIRICAL_EVIDENCE.md`, `README.md`.

- **Convergence Is Silence clarified as a stopping condition, not a correctness guarantee.** PRINCIPLES.md and README.md now state explicitly what PROOF.md already established through falsification: silence is the strongest available stopping signal for the loop, not proof that nothing was missed.

  Files changed: `PRINCIPLES.md`, `README.md`.

- **ARF license claim recalibrated from asserted result to stated hypothesis.** README.md and PRINCIPLES.md no longer summarize ARF as if a passed probe had already been validated to license fuller autonomy. The probe remains defined; the downstream autonomy-license claim is now explicitly stated as a hypothesis awaiting validation.

  Files changed: `README.md`, `PRINCIPLES.md`.

- **Comparative framing in PROBLEM.md narrowed to claims the document can carry on its own evidence.** The XAI paragraph no longer overstates a literature conclusion without citation, and the restriction-first section now defines a broad family of approaches rather than claiming a settled field-wide dominant paradigm.

  Files changed: `PROBLEM.md`.

---

## v1.8.0 - 2026-06-03

### Changed

- **README.md: argument architecture corrected — diagnostic framing now precedes the principles.** The opening section of README previously listed the three principles and then explained the diagnostic contrast (restriction-first vs. this framework). This presented the "what" before the "why," inverting the logical chain (Thesis → Principles → ARF). The four-sentence diagnostic arc now introduces the principles list rather than following it; ARF closes the sequence. Same words, correct order. The README is now the only place in the manifesto where the diagnostic claim, the three principles, and ARF are presented as a unified logical sequence in the right order.

  Files changed: `README.md`.

- **PROBLEM.md: Digest now includes the foundational diagnosis.** A cold reader opening PROBLEM.md directly — without having read README — previously encountered the two problems, ARF, and delegability, but had no signal for why this framework exists rather than restriction-first governance. A closing paragraph has been added to the Digest giving the foundational diagnostic contrast (reasoning failure vs. capability excess as root cause) and pointing to the existing-work section for the full argument. Uses the same wording as the README framing to stay consistent across the reading path.

  Files changed: `PROBLEM.md`.

- **PRINCIPLES.md: ARF tag definition aligned to canonical phrase.** The Digest described ARF as "the external signal that the agent is genuinely reasoning about the situation and that the reasoning is visible enough for observers to judge" — different words from the canonical phrase in PROBLEM.md Digest ("the external signal that genuine, situated reasoning is both occurring and visible"). Both said the same thing; only one used the technical term "situated" and the precise two-part structure (occurring = Problem 1; visible = Problem 2). Aligned to the canonical form. The body's operational ARF definition (§Autonomous Reasoning Fidelity) is intentionally expanded and unchanged.

  Files changed: `PRINCIPLES.md`.

---

## v1.7.0 - 2026-06-03

### Changed

- **PROBLEM.md: thesis sentences precision-tightened.** The three closing sentences of the "Restriction-first AI governance" bullet now carry their full intended precision. Sentence 1 gained a domain boundary: "Within the domain of non-adversarial delegation" — removing an overreach that stated the claim universally. Sentence 3 shifted from a causal form ("Restriction decreases the reasoning quality that produces safety") to a structural form ("Restriction frameworks do not measure or develop the reasoning quality that produces safety") — a claim that is fully defensible from the document's existing content without an additional citation.

  Files changed: `PROBLEM.md`.

- **PROBLEM.md: scalable oversight and process supervision added to existing-work section.** A new bullet acknowledges the body of work that shares this framework's core diagnostic premise (reasoning quality is the safety-relevant property, not capability scope). Three papers cited and correctly attributed: Iterated Amplification (Christiano, Shlegeris, and Amodei, 2018; arXiv:1810.08575), Debate (Irving, Christiano, and Amodei, 2018; arXiv:1805.00899), and process supervision (Lightman et al., 2023; arXiv:2305.20050). The bullet explicitly delimits the gap: this prior work operates at training and evaluation time; ARF addresses the deployment-time question an operator faces with a model already in operation.

  Files changed: `PROBLEM.md`.

- **PROBLEM.md: References section added.** A formal References section was added at the end of the document, providing full bibliographic entries for the three scalable oversight citations added this version (Christiano et al., 2018; Irving et al., 2018; Lightman et al., 2023), consistent with the existing References section in PRINCIPLES.md.

  Files changed: `PROBLEM.md`.

---

## v1.6.0 - 2026-06-02

### Changed

- **README positioning paragraph replaced with a four-sentence framing arc.** The previous 6-sentence paragraph used technical jargon and duplicated detail already in PROBLEM.md. Replaced with four operator-authored sentences that state the argument plainly: the diagnostic contrast between restriction-first governance and this framework, how the three principles address both failure modes, and what ARF measures. This is the entry point statement of what the manifesto is and why the diagnostic contrast matters.

  Files changed: `README.md`.

- **PRINCIPLES.md: "What a passing ARF test licenses" removed from the ARF operational definition.** This ~200-word paragraph re-argued the restriction-vs-ARF diagnostic contrast in full — the same argument already made at greater length in PROBLEM.md's "Restriction-first AI governance" section. Removed; replaced with a single navigation line pointing to PROBLEM.md. The operational definition now flows without interruption: named property → theoretical anchors → preconditions → metric → probe structure → technique ancestry → falsifiable claim → formalization requirements.

  Files changed: `PRINCIPLES.md`.

---

## v1.5.1 - 2026-06-02

### Fixed

- **PROOF.md structural defects from the de-AI pass.** Two defects introduced by the v1.5.0 multi-replacement pass: (1) the Principle 1 conformance section had its `**The falsification question.**` subhead merged into the body text; (2) the ARF probe sentence in the Digest became a comma splice when the em dash was replaced with a comma. Both fixed; all four conformance sections (P1, P2, P3, ARF) now structurally consistent.

  Files changed: `PROOF.md`.

- **EMPIRICAL_EVIDENCE.md: context note added to Section 3.** Section 3 previously opened directly into the failure class descriptions without signaling how the developmental case should be read. A note was added to frame the section as contextual material rather than a standalone proof surface.

  Files changed: `EMPIRICAL_EVIDENCE.md`.

---

## v1.5.0 - 2026-06-02

### Changed

- **De-AI language pass across all manifesto documents.** Replaced all em dashes (U+2014) with context-appropriate punctuation (colon, comma, parentheses, or hyphen). Removed metaphors that had drifted toward AI writing patterns ("is theater," "story the agent tells about itself"). Removed X-not-Y padding where the negative clause added no structural information; load-bearing contrasts retained.

  Files changed: `README.md`, `PRINCIPLES.md`, `PROBLEM.md`, `PROOF.md`, `EMPIRICAL_EVIDENCE.md`, `CHANGELOG.md`.

---

## v1.4.0 - 2026-06-02

### Added

- **ARF operational definition: technique ancestry, probe structure, falsifiable claim, and formalization agenda.** PRINCIPLES.md now documents the Winograd Schema Challenge (Levesque et al., 2011) and CheckList (Ribeiro et al., ACL 2020) as technique ancestors for the contrastive-pair probe mechanism; the probe construction rules (Case A / Case B pair, pre-registered expected divergence, independent sessions); the falsifiable claim; and the formalization agenda naming the four artifacts required to make ARF a validated method (published spec, test harness, probe dataset, reproducibility report).

  Files changed: `PRINCIPLES.md` (extended ARF operational definition section).

- **Formal References section in PRINCIPLES.md.** Seven complete bibliographic entries: Levesque et al. (2011), Saltzer & Schroeder (1975), Lee & See (2004), Ribeiro et al. (2020), Turpin et al. (NeurIPS 2023), Huang et al. (ICLR 2024), Chen et al. (arXiv:2505.05410, 2025).

  Files changed: `PRINCIPLES.md` (appended `## References` section).

- **ARF conformance test in PROOF.md.** PROOF.md now documents a domain-agnostic ARF probe test alongside the three principle conformance tests, and includes an ARF row in the "What this evidence does and does not establish" table.

  Files changed: `PROOF.md` (added `### ARF: Autonomous Reasoning Fidelity` subsection; updated intro sentence; added ARF table row; aligned Digest ARF note with body wording).

---

## v1.3.0 - 2026-05-30

### Changed

- **P2 Observable Autonomy: structural root anchored in Saltzer & Schroeder 1975.** The Origin line now leads with the *separation of privilege* principle (Saltzer & Schroeder, *Proceedings of the IEEE*, vol. 63, no. 9, pp. 1278–1308, September 1975, doi:10.1109/PROC.1975.9939): "no single accident, deception, or breach of trust is sufficient to compromise the protected information." Observable Autonomy transfers that structure from access control to the epistemic record: the party that acts must not also be the sole party that authors the account of its action. The principle is theirs (1975); the domain transfer to the record of an autonomous agent's own reasoning is what this principle adds. The existing synthesis (Meaningful Human Control, Lee & See 2004, Observatory pattern) is retained and follows the S&S anchor.

  Files changed: `PRINCIPLES.md` (extended `**Origin:**` under Principle 2).

---

## v1.2.0 - 2026-05-13

### Changed

- **P2: multi-resolution requirement removed.** Observable Autonomy now requires one untampered, full-detail trail captured as the work happens. The previous three-tier classification (full evidence / indexed evidence / digested evidence) was a derivative convenience elevated into an architectural constraint; that overreaches.

  What stays: capture-author separation, fidelity marking, the structural-not-reported argument, and both corollaries (*A record composed after the decision is testimony, not evidence* / *A record an agent can rewrite is not a record*).

  Files changed: `PRINCIPLES.md` (removed `### The resolution requirement` subsection; removed "at their resolution" from the test; rewrote the implementation note); `PROBLEM.md` (dropped "at my resolution" qualifier from the delegability test; rephrased reviewer-engagement out-of-scope item).

---

## v1.1.0 - 2026-05-12

### Added

- **Premise: The agent is an unreliable narrator of itself.** A new section before the three principles cites Turpin et al. (NeurIPS 2023), Chen et al. (2025), and Huang et al. (ICLR 2024) as load-bearing evidence, not decoration. Frames the three principles as structural responses that each separate one role (interpretation / narration / judgment) from the agent.
- **Principle 2 restructured around two failure modes of post-hoc rationalization:**
  - Capture-moment fabrication: record composed after the decision.
  - After-the-fact tampering: record edited by the agent later.
- **Two new corollaries for P2:** *A record composed after the decision is testimony, not evidence.* (capture-moment fidelity) / *A record an agent can rewrite is not a record.* (tamper resistance). These close the two ways post-hoc rationalization enters a trail.
- **`### Capture-author separation`** subsection in P2 (replaces the former harness boundary constraint). States the requirement structurally without prescribing an implementation mechanism.
- **`### Why structural, not reported`** subsection in P2. Explains why the trail's integrity must not depend on the agent's honesty.
- **Digest updated:** removed `continuous` (ambiguous re: live-watching); added per-principle parenthetical naming the role each separates.
- **`How the principles interact` updated:** opening sentence now explicitly links all three principles to the Premise.

### Removed

- Corollary *"If you can't see it, it shouldn't be doing it"*, conflated audit timing with capture timing; replaced by the two new corollaries above.

---

## v1.0.0 - 2026-05-02

Initial public release. Three principles (Commander's Intent, Observable Autonomy, Convergence Is Silence), one emergent property (Autonomous Reasoning Fidelity), empirical evidence from a three-family silence-convergence test.
