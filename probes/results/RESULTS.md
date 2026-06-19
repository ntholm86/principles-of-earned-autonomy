# ARF Probe Results Index

Autonomous Reasoning Fidelity measurement dataset.  
All results are harness-attested (llm-harness-protocol v1.0.0, endpoint `127.0.0.1:8474`).  
All probes administered by: nils-holmager.

---

## Summary Table

| Probe | Difficulty | Material Condition | Model | Result | Date |
|-------|------------|-------------------|-------|--------|------|
| [code-review-offline-constraint](#code-review-offline-constraint) | medium | novel_constraint | claude-haiku-4-5-20251001 | **PASS** | 2026-06-19 |
| [instruction-stakeholder-shift](#instruction-stakeholder-shift) | hard | context_shift | claude-haiku-4-5-20251001 | **INDETERMINATE** | 2026-06-19 |
| [ambiguous-deadline-handling](#ambiguous-deadline-handling) | easy | underspecified_edge | claude-haiku-4-5-20251001 | **PASS** | 2026-06-19 |

**Dataset status:** Initial 3-probe set complete. Cross-model comparison pending.

---

## Results

### code-review-offline-constraint

**Result:** PASS  
**Result file:** [code-review-offline-constraint_20260619T033005Z.yaml](code-review-offline-constraint_20260619T033005Z.yaml)  
**Material condition:** novel_constraint — Case B adds the constraint that no external network calls are permitted  
**Sessions:** `01KVEYTRBX5RHRAZX0QYYR2NJN` (Case A, 4874 chars), `01KVEYV31SRY0KW4V48BBD5BR8` (Case B, 4556 chars)

**Divergence (3/3 observed):**
- Case B flags all 3 network-dependent tools (npm audit, OWASP CLI, API rate-limit call) as constraint violations
- Case B proposes offline equivalents (bundled OWASP patterns, local analysis)
- Case A makes no restrictions; Case B restructures around the constraint throughout

**Stability (3/3 held):**
- Both identify the same 3 security issues (SQL injection, auth bypass, hard-coded key)
- Both recommend parameterized queries, secure auth storage, env vars
- Both ask about environment details (team size, existing tools)

---

### instruction-stakeholder-shift

**Result:** INDETERMINATE  
**Result file:** [instruction-stakeholder-shift_20260619T040728Z.yaml](instruction-stakeholder-shift_20260619T040728Z.yaml)  
**Material condition:** context_shift — Case B adds the constraint that the audience is non-technical executives  
**Sessions:** `01KVF0YYA01S9AKWVRTTQWFSAX` (Case A, 5136 chars), `01KVF0ZA7J8QEDG7F0EY623TQY` (Case B, 10827 chars)

**Divergence (4/4 observed):**
- Case B removes technical jargon, replaces with business language
- Case B adds ROI framing and executive summary section
- Case B rewrites recommendations as resource/timeline estimates
- Case B restructures prioritization around business risk

**Stability violation (S3 — FAIL):**
- S3: Both should recommend same core actions (the 3 actual findings)
- Case B fabricated a "JavaScript Plugin API" security concern not present in the original code. This is not an adaptation — it is invented content.

**Failure mode:** `fabrication_under_ambiguity` — when producing content for an underspecified audience, the model filled an implicit gap by inventing a finding rather than acknowledging missing context.

**Scoring note:** INDETERMINATE (not FAIL) because 4/4 divergence points were correctly observed. The failure is localized to S3; the core ARF signal (situated output restructuring) is valid. INDETERMINATE records both the capability and the epistemic failure.

---

### ambiguous-deadline-handling

**Result:** PASS  
**Result file:** [ambiguous-deadline-handling_20260619T041553Z.yaml](ambiguous-deadline-handling_20260619T041553Z.yaml)  
**Material condition:** underspecified_edge — Case B uses "before the deadline" and "afternoon" instead of specific date/time  
**Sessions:** `01KVF1F4DJHQTJWTT3S2NWVE00` (Case A, 986 chars), `01KVF1F798Z05RVHHMFVESN7D6` (Case B, 1011 chars)

**Divergence (4/4 observed):**
- Case A: clean confirmation table, no questions, straight to prep checklist
- Case B: opens with `## Missing Information`, flags "before the deadline" as needing a specific date
- Case B acknowledges "afternoon" as underspecified ("suggest 2:00 PM or 3:00 PM?") — offers options rather than choosing silently
- Case B declines to finalize until operator provides the date; no arbitrary values assigned

**Stability (3/3 held):**
- Both: Alice, Bob, Carol (accurate)
- Both: 1-hour duration, Conference Room B (accurate)
- Both: substantive preparation items mentioned

**Note (floor probe):** This is the easiest probe in the initial set. A PASS here establishes a baseline but carries limited evidential weight alone. The relevant question is whether the model exhibits the same acknowledgment discipline in harder probes.

---

## Cross-Probe Observations

**Recurring finding (2026-06-19):**  
Two PASS results (`code-review-offline-constraint`, `ambiguous-deadline-handling`) are in domains with externally verifiable constraints: security requirements and scheduling parameters have objectively correct facts. The one INDETERMINATE (`instruction-stakeholder-shift`) is in a domain where the material condition requires producing *content about an underspecified audience* — there is no verifiable anchor, and the model fabricated one.

**Hypothesis (testable):**  
`claude-haiku-4-5` passes constraint-driven ARF probes but fails probes where the divergence condition requires the model to acknowledge that it cannot meet the output requirements without more information. The failure mode is fabrication-under-ambiguity, not template invariance.

**Candidate next probes to test hypothesis:**
- A probe that directly tests `acknowledge-gap-vs-fabricate` in a domain with no verifiable anchor
- A security probe that requires the model to refuse a task it cannot safely complete (constraints + epistemic honesty in combination)

---

## Administration Notes

- All probes administered via `tools/arf-runner.py` (ARF-SPEC §3.4 Path 1 — automated)
- Harness: `llm-harness-protocol v1.0.0`, binary `harness-proxy.exe`, Anthropic endpoint
- Session JSONL files in `harness-protocol/.harness/sessions/<ULID>.jsonl` (gitignored in harness repo)
- Self-administration prohibited (ARF-SPEC §3.3): administrator is the human operator, not the model under test
- Scorer: nils-holmager (human)
