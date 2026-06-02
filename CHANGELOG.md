# Changelog

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
