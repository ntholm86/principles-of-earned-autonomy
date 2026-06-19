# ARF Probe Dataset

**Version:** 0.1.0  
**Status:** Initial corpus (demonstration probes)  
**Last updated:** 2026-06-19

---

## Purpose

This directory contains the curated ARF probe dataset — Case A / Case B pairs with pre-registered expected divergences, following the specification in [ARF-SPEC.md](../ARF-SPEC.md).

## Corpus Status

| Status | Count | Description |
|--------|-------|-------------|
| **Demonstration** | 3 | Initial probes to validate format and methodology |
| **Validated** | 0 | Probes administered through harness with reproducible results |
| **Retired** | 0 | Probes found to be invalid or superseded |

## Probe Inventory

| ID | Domain | Task Class | Difficulty | Material Condition | Status |
|----|--------|------------|------------|-------------------|--------|
| `code-review-offline-constraint` | code-review | security-judgment | medium | novel_constraint | demonstration |
| `instruction-stakeholder-shift` | instruction-interpretation | intent-compliance | medium | context_shift | demonstration |
| `ambiguous-deadline-handling` | task-execution | ambiguity-resolution | easy | underspecified_edge | demonstration |

## Directory Structure

```
probes/
├── README.md                           # This file
├── code-review-offline-constraint.yaml # Probe 1
├── instruction-stakeholder-shift.yaml  # Probe 2
├── ambiguous-deadline-handling.yaml    # Probe 3
└── results/                            # Administration results (empty until administered)
```

## Contributing Probes

New probes must:

1. Follow the schema in [ARF-SPEC.md](../ARF-SPEC.md) Section 6.1
2. Pass the construction anti-pattern checks (Section 2.3)
3. Be reviewed by someone other than the author before inclusion
4. Target one of the task classes in Section 5.3 (or propose a new class with rationale)

## Validation Roadmap

1. **Phase 1 (current):** Demonstration probes — validate format, refine methodology
2. **Phase 2:** Harness integration — administer through LLM Harness Protocol
3. **Phase 3:** Multi-agent testing — administer to 3+ agent families
4. **Phase 4:** Independent replication — external administrators reproduce results
5. **Phase 5:** Reproducibility report — formal write-up for citation
