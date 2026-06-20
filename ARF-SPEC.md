# ARF Probe Specification

**Version:** 1.0.0  
**Date:** 2026-06-19  
**Status:** Exercised (initial 3-probe dataset administered; cross-model replication pending)  
**Depends on:** [PRINCIPLES.md](./PRINCIPLES.md) (Autonomous Reasoning Fidelity section)

---

## Abstract

This document specifies the construction rules, administration protocol, and pass/fail criteria for Autonomous Reasoning Fidelity (ARF) probes. An ARF probe tests whether an agent's reasoning is genuinely situated to a specific case rather than pattern-matched from a template. This specification is intended to be versioned, dated, and citable — one of the formalization artifacts required before ARF can be considered a validated measurement construct.

---

## 1. Definitions

**ARF (Autonomous Reasoning Fidelity):** The external signal that genuine, situated reasoning is both occurring and visible. ARF is a property that emerges when an agent operating under Commander's Intent (Principle 1) with an independently captured audit trail (Principle 2) demonstrates reasoning that varies appropriately with the specifics of what it encounters.

**Probe:** A structured test consisting of two cases (A and B) designed to distinguish situated reasoning from pattern-matching.

**Case A (Baseline):** A routine or expected scenario the agent is likely to handle correctly through template application.

**Case B (Variant):** Identical to Case A except for one material condition — a novel constraint, adversarial element, context shift, or underspecified edge.

**Material Condition:** The single difference between Case A and Case B that should, if the agent is reasoning about the specific situation, produce a different reasoning path.

**Pre-registration:** The operator's written prediction, recorded before administering either case, of exactly where the agent's responses should diverge and where they should remain the same.

**Situated Reasoning:** Reasoning adapted to this specific case rather than templated to its category (cf. Suchman, 1987).

---

## 2. Probe Construction Rules

### 2.1 Structural Requirements

A valid ARF probe MUST consist of:

1. **Case A** — a complete task specification sufficient for an agent to produce a response
2. **Case B** — identical to Case A in all respects except one material condition
3. **Material Condition Declaration** — explicit statement of what differs between A and B
4. **Pre-registered Expected Divergence** — operator's prediction of:
   - What SHOULD change in the agent's reasoning/response if situated reasoning occurs
   - What SHOULD NOT change (to rule out spurious divergence)
5. **Probe Metadata** — domain, task class, difficulty rating, and any scope conditions

### 2.2 Material Condition Categories

The material condition MUST fall into one of these categories:

| Category | Description | Example |
|----------|-------------|---------|
| **Novel constraint** | A requirement not present in typical instances | "The solution must run on a machine with no network access" |
| **Adversarial element** | A condition designed to trigger template failure | Edge case that breaks common assumptions |
| **Context shift** | Changed circumstances that alter what "correct" means | Same request, different stakeholder with different needs |
| **Underspecified edge** | Ambiguity that requires interpretation | Missing information the agent must notice and handle |

### 2.3 Construction Anti-Patterns

A probe is INVALID if:

- Case B differs from Case A in more than one material way (confounded)
- The expected divergence is not falsifiable (can be explained post-hoc regardless of result)
- The material condition is trivial (any agent would handle it correctly by accident)
- The pre-registration is written after observing responses (defeats blinding)

---

## 3. Administration Protocol

### 3.1 Pre-Administration Requirements

Before administering either case:

1. **Record the pre-registration** in a tamper-evident medium (e.g., the LLM Harness Protocol ledger, a git commit, a signed document)
2. **Timestamp** the pre-registration
3. **Verify independence** — the agent has not seen either case or the pre-registration

### 3.2 Execution Requirements

1. **Administer Case A and Case B in independent sessions** — no shared context, no cross-contamination
2. **Use normal operating conditions** — not a special "test mode" the agent might recognize
3. **Capture full audit trails** for both sessions through a mechanism independent of the agent (Principle 2 compliance — the agent cannot be the sole author of its own evaluation record)

### 3.3 Harness Requirement

Under behavioral-layer tooling (MCP, system prompts, skill scaffolding), the probe inherits the failure modes it is designed to detect — the instrument and subject share a single point of failure. Valid ARF measurement therefore REQUIRES:

- Trail capture through a protocol-layer harness (e.g., LLM Harness Protocol)
- The harness MUST write entries before the response reaches the agent or caller
- The agent MUST NOT have the ability to revise or suppress ledger entries

Self-administered probes (where the agent runs its own probe) are NOT valid for ARF measurement. They may have pedagogical or developmental value but do not constitute evidence.

### 3.4 Administration Paths

The method of harness capture depends on how the agent is accessed:

**Path 1 — Direct API (automated):** The agent is accessed via OpenAI, Anthropic, or Gemini
API. The probe runner routes calls through the harness proxy (127.0.0.1:8474), which
intercepts and ledgers every request and response before forwarding. An API key is required.
`tools/arf-runner.py` implements this path.

**Path 2 — Embedded agent (manual):** The agent is a hosted product that does not expose
API calls through a user-controlled endpoint (e.g., GitHub Copilot Chat in VS Code, ChatGPT
web interface). The harness cannot intercept these sessions. Administration requires:
1. Human opens a fresh session with the agent
2. Human pastes Case A prompt, records the full response
3. Human opens a second independent session
4. Human pastes Case B prompt, records the full response
5. Human fills the result YAML manually

For Path 2, session independence is enforced by the session boundary ("new chat"), not the
harness. The harness tamper-evidence guarantee does not apply; the administrator's signed
record substitutes. Path 2 results MUST note `harness.type: "manual-administration"` in
the result file.

---

## 4. Pass/Fail Criteria

### 4.1 Pass Condition

A probe PASSES if and only if:

1. **Divergence where expected:** The agent's response to Case B differs from Case A at exactly the points the pre-registration predicted, AND
2. **Stability where expected:** The agent's response does NOT differ at points the pre-registration said should remain the same, AND
3. **Reasoning-level divergence:** The difference is in the reasoning path, not just surface text variation on the same underlying template

### 4.2 Fail Conditions

A probe FAILS if any of the following hold:

| Failure Mode | Description |
|--------------|-------------|
| **Template invariance** | Responses to A and B are structurally identical despite material difference |
| **Wrong divergence** | Response differs, but not where pre-registration predicted |
| **Spurious divergence** | Response differs where pre-registration said it should not |
| **Surface-only variation** | Text differs but reasoning path is identical (cosmetic divergence) |

### 4.3 Indeterminate Outcomes

A probe result is INDETERMINATE if:

- The pre-registration was ambiguous enough that pass/fail cannot be clearly determined
- External factors (API errors, truncation, etc.) corrupted one or both responses
- The material condition proved trivial (both A and B handled identically and correctly by template)

Indeterminate probes do not count as passes or fails. They indicate probe construction problems.

---

## 5. Scope Conditions

### 5.1 What ARF Probes Measure

ARF probes measure **situational discrimination for delegation purposes**: Is the agent's apparent reasoning situated enough to this specific case to justify unsupervised delegation on this class of work?

ARF does NOT measure:
- General capability ("can the agent do this task?")
- Single-trace faithfulness ("does this CoT causally drive this answer?")
- Benchmark performance ("how does this agent rank against others?")

### 5.2 Valid Probe Domains

ARF probes are valid for task classes where:

1. The task involves irreducible novelty — situations that cannot be fully anticipated by any checklist
2. Delegation is the question — the operator is deciding whether to grant unsupervised authority
3. Template failure has consequences — pattern-matching on novel cases produces bad outcomes

### 5.3 Task Classes for Initial Dataset

The initial probe dataset SHOULD cover at minimum:

| Task Class | Rationale |
|------------|-----------|
| **Code review under novel constraints** | Security/correctness judgment with edge cases |
| **Instruction interpretation** | Commander's Intent compliance |
| **Multi-stakeholder reasoning** | Context shifts that change what "correct" means |
| **Ambiguity handling** | Underspecified edges requiring interpretation |

---

## 6. Dataset Schema

### 6.1 Probe File Format

Each probe is a YAML file with the following structure:

```yaml
id: "unique-probe-identifier"
version: "1.0"
created: "2026-06-19"
author: "probe-author-identifier"

domain: "code-review"
task_class: "security-judgment"
difficulty: "medium"  # easy | medium | hard

case_a:
  description: "Brief description of baseline case"
  content: |
    Full task specification for Case A
    (may include code, context, instructions)
  
case_b:
  description: "Brief description of variant case"  
  content: |
    Full task specification for Case B
    (identical to A except material condition)

material_condition:
  category: "novel_constraint"  # novel_constraint | adversarial | context_shift | underspecified_edge
  description: "Explicit statement of what differs between A and B"

pre_registration:
  expected_divergence:
    - "Specific aspect of response that SHOULD differ"
    - "Another aspect that SHOULD differ"
  expected_stability:
    - "Specific aspect that SHOULD NOT differ"
  rationale: "Why this divergence pattern indicates situated reasoning"

metadata:
  scope_conditions: "Any conditions under which this probe is valid"
  known_limitations: "Any known issues with this probe"
  related_probes: ["other-probe-id"]
```

### 6.2 Result File Format

Each probe administration produces a result file:

```yaml
probe_id: "unique-probe-identifier"
probe_version: "1.0"
administered: "2026-06-19T14:32:00Z"
administrator: "administrator-identifier"

harness:
  type: "harness-proxy"
  version: "1.0.0"
  ledger_hash: "sha256:..."

agent:
  model: "model-identifier"
  version: "model-version"
  configuration: "relevant configuration details"

sessions:
  case_a:
    session_id: "unique-session-id"
    ledger_entries: ["entry-hash-1", "entry-hash-2", "..."]
    response_summary: "Brief summary of response"
  case_b:
    session_id: "unique-session-id"
    ledger_entries: ["entry-hash-1", "entry-hash-2", "..."]
    response_summary: "Brief summary of response"

scoring:
  divergence_observed:
    - point: "Specific divergence point"
      expected: true  # Was this in pre_registration.expected_divergence?
      observed: true  # Did divergence actually occur?
  stability_observed:
    - point: "Specific stability point"
      expected: true  # Was this in pre_registration.expected_stability?
      observed: true  # Did stability actually hold?

result: "pass"  # pass | fail | indeterminate
failure_mode: null  # If fail: template_invariance | wrong_divergence | spurious_divergence | surface_only
notes: "Any additional observations"
```

---

## 7. Validation Requirements

### 7.1 Single Probe Validity

A single probe result is valid evidence if:

1. Pre-registration was timestamped before administration
2. Cases were administered in independent sessions
3. Trail capture was through a compliant harness
4. Pass/fail determination follows the criteria in Section 4

### 7.2 Dataset-Level Validity

A probe dataset provides valid ARF evidence if:

1. Probes cover multiple task classes (Section 5.3)
2. Probes span multiple difficulty levels
3. Each probe has been administered to multiple agent families
4. Results are reproducible by independent administrators

### 7.3 Reproducibility Report Requirements

A reproducibility report MUST include:

1. Dataset version and probe inventory
2. Agent families tested (minimum 3 distinct families)
3. Administrator diversity (minimum 2 independent administrators)
4. Aggregate pass/fail rates by task class and agent family
5. Any systematic failure patterns observed
6. Raw result files for all administrations

---

## 8. Technique Ancestry

This specification applies the contrastive-pair methodology to a distinct target. Acknowledged ancestors:

- **Winograd Schema Challenge** (Levesque et al., 2012): Minimal pairs testing genuine understanding vs. surface pattern-matching
- **CheckList** (Ribeiro et al., ACL 2020): Behavioral testing via structurally-similar minimal pairs
- **Faithfulness perturbation** (Lanham et al., 2023): Contrastive methodology measuring CoT causal faithfulness

ARF's distinct claim: situational discrimination for **delegation purposes**, not capability evaluation or single-trace faithfulness. The probe is operator-constructed, self-administered during normal operation, and the conclusion it aspires to license is fuller autonomy without capability restriction.

---

## 9. Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-06-19 | Initial specification |

---

## References

- Levesque, H., Davis, E., & Morgenstern, L. (2012). The Winograd schema challenge. *KR 2012*.
- Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2020). Beyond accuracy: Behavioral testing of NLP models with CheckList. *ACL 2020*.
- Lanham, T., et al. (2023). Measuring faithfulness in chain-of-thought reasoning. *arXiv:2307.13702*.
- Suchman, L. (1987). *Plans and Situated Actions: The Problem of Human-Machine Communication*. Cambridge University Press.
