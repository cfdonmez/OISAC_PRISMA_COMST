# VIII-G Preflight Plan (Capstone Alignment Lock)

## Scope Lock

- Section VIII intent check: `Open Challenges and Research Roadmap` (PASS).
- Axis-2 domain list check: A-E domains are explicitly listed; `VIII-G` is not listed as a new Axis-2 domain.
- Declared interpretation: **VIII-G is a CAPSTONE cross-section alignment and evidence-consistency check**, not a new challenge domain.

## VIII-G Intent Interpretation (from `section8G_cross_section_report.md`)

- Alignment audit: compare strict Section VIII challenge evidence with upstream Section V/VI/VII linkage signals.
- Coverage continuity check: use `strict_evidence_count`, `linked_any_upstream_count`, and `strict_without_upstream_count`.
- Operational interpretation: VIII-G is an artefact-derived traceability layer that closes Section VIII without extending the Axis-2 domain inventory.

## Cross-Section Alignment Audit

| domain | strict_evidence_count | linked_any_upstream_count | strict_without_upstream_count | status |
|---|---:|---:|---:|---|
| standardization_interoperability | 55 | 55 | 0 | aligned |
| hardware_scalability_efficiency | 25 | 25 | 0 | aligned |
| channel_modeling_evaluation | 54 | 54 | 0 | aligned |
| security_privacy_reliability | 18 | 18 | 0 | aligned |
| deployment_convergence_roadmap | 0 | 0 | 0 | zero/isolated evidence row |

## Preflight Observations

- Four challenge domains show exact strict/upstream count alignment in the current evidence pack.
- `deployment_convergence_roadmap` remains a zero-row in both strict and upstream counts; this should be preserved as a coverage-state observation, not a low-importance claim.
- `strict_without_upstream_count = 0` for all five rows, so VIII-G can be framed as a continuity audit rather than a gap-discovery subsection.

## Example Audit

| challenge_domain | discrepancy_group | paper_ids | audit_note |
|---|---|---|---|
| standardization_interoperability | strict_without_upstream | empty | no example payload available |
| hardware_scalability_efficiency | strict_without_upstream | empty | no example payload available |
| channel_modeling_evaluation | strict_without_upstream | empty | no example payload available |
| security_privacy_reliability | strict_without_upstream | empty | no example payload available |
| deployment_convergence_roadmap | strict_without_upstream | empty | no example payload available |

- Example-audit interpretation: `s8g_xsec_ex.csv` contains row stubs for discrepancy grouping, but no paper-level payload is currently populated.

## section8G Assets Existence Check

| file | role | exists |
|---|---|---|
| `analysis/VIII_ev_v1/s8g_xsec_align.csv` | row-level alignment table | PASS |
| `analysis/VIII_ev_v1/s8g_xsec_ex.csv` | cross-section examples | PASS |
| `analysis/VIII_ev_v1/section8G_cross_section_report.md` | narrative alignment report | PASS |

## Citation and Evidence Plan

- Cite-key shortlist: none (`artefact-only mode`).
- Planned citation mode: **artefact-only mode**.
- Planned literature cite-key usage: none unless a later integration step explicitly requires it.
- Support basis for non-trivial claims: `section8G_cross_section_report.md`, `s8g_xsec_align.csv`, `axis_definitions.md`, and `mapping_rules.md`.

## Case Shortlist for Writing

- G1 = aligned domains block
  Focus: `standardization_interoperability`, `hardware_scalability_efficiency`, `channel_modeling_evaluation`, and `security_privacy_reliability` as perfectly aligned rows with `strict_without_upstream_count = 0`.
- G2 = zero/isolated domain block
  Focus: `deployment_convergence_roadmap` as a zero/isolated evidence row, framed as an evidence-state observation only.
- G3 = example-availability block
  Focus: all five rows in `s8g_xsec_ex.csv` currently have empty `paper_ids`; no example payload available.
- G4 = methodological caution block
  Focus: VIII-G should remain an artefact-derived traceability audit, not a new challenge domain and not a causal dependency claim.
