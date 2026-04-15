# Section III Impact Matrix

Purpose:

- This matrix translates the current Section III PRISMA wording into evidence-aware editing decisions.
- It is designed to prevent local wording edits from creating new contradictions elsewhere in the manuscript or evidence pack.

Decision labels:

- `KEEP`: claim is safe as written.
- `SOFTEN`: claim should remain but with more careful wording.
- `SUPPLEMENT-ANCHOR`: claim is acceptable if clearly tied to the evidence pack / supplementary materials.
- `REVISE`: claim should be rewritten because the current wording overstates evidential strength.

Evidence classes:

- `ROW-BACKED`: directly supported in the current repo snapshot.
- `RECONSTRUCTION-SUPPORTED`: canonically maintained and supported by reconstruction/audit files, but not fully row-backed.
- `PARTIAL`: only partially supported; strong wording should be avoided.

## A. Protocol and Registration

| Location | Current claim | Evidence class | Decision | Basis | Downstream impact |
|---|---|---|---|---|---|
| `bare_jrnl_new_sample4.tex:741` | PRISMA 2020 + PRISMA-S compliance statement | ROW-BACKED | `KEEP` | Protocol and Section III wording are aligned | None beyond checklist consistency |
| `bare_jrnl_new_sample4.tex:741` | OSF registration ID and URL | ROW-BACKED | `KEEP` | Registration details are stable and explicitly stated | None |
| `bare_jrnl_new_sample4.tex:742` | No substantive amendments after registration | ROW-BACKED | `KEEP` | Current repo history supports reporting-level clarification rather than method change | Checklist item 7 remains pass |
| `bare_jrnl_new_sample4.tex:743` | Objective statement for the review | ROW-BACKED | `KEEP` | This is a framing claim, not an evidence-vulnerability claim | None |

## B. Information Sources and Search Strategy

| Location | Current claim | Evidence class | Decision | Basis | Downstream impact |
|---|---|---|---|---|---|
| `bare_jrnl_new_sample4.tex:746` | Canonical formal databases are IEEE Xplore, Scopus, and Web of Science | RECONSTRUCTION-SUPPORTED | `KEEP` | Supported by protocol, search strings, and reconstructed search log | Search evidence files must stay aligned |
| `bare_jrnl_new_sample4.tex:746` | All three were last searched on November 30, 2025 | RECONSTRUCTION-SUPPORTED | `KEEP` | Historically grounded and consistently reported, though not backed by full original raw bundle | Freeze bundle files must remain available |
| `bare_jrnl_new_sample4.tex:746` | These three databases defined the canonical formal identification stage | RECONSTRUCTION-SUPPORTED | `KEEP` | Correct framing of source policy; does not overclaim row-level preservation | Search log / protocol wording must remain synchronized |
| `bare_jrnl_new_sample4.tex:746` | arXiv and TechRxiv were supplementary monitoring only | RECONSTRUCTION-SUPPORTED | `KEEP` | Supported by protocol source-policy design | `other_sources_results = 0` logic depends on this |
| `bare_jrnl_new_sample4.tex:746` | `other_sources_results = 0` | RECONSTRUCTION-SUPPORTED | `KEEP` | Explicitly supported by protocol and flow counts | Flow diagram and source-policy files must remain aligned |
| `bare_jrnl_new_sample4.tex:755` | Search strings and run-level logs were preserved in study records | PARTIAL | `SOFTEN` | Search strings are preserved; run-level log is reconstructed rather than original raw-bundle complete | Search-log note and freeze bundle must be referenced carefully |
| `bare_jrnl_new_sample4.tex:755` | Supporting search-stage materials were archived in the supplementary evidence package | RECONSTRUCTION-SUPPORTED | `KEEP` | Now true given the reconstructed freeze bundle and evidence pack | Evidence pack manifest and zip should remain in sync |
| `bare_jrnl_new_sample4.tex:755` | Search was frozen on November 30, 2025 | RECONSTRUCTION-SUPPORTED | `KEEP` | Consistently declared and historically grounded | Freeze-related notes must remain consistent |

## C. Eligibility Criteria

| Location | Current claim | Evidence class | Decision | Basis | Downstream impact |
|---|---|---|---|---|---|
| `bare_jrnl_new_sample4.tex:759-799` | Inclusion and exclusion criteria table and prose | ROW-BACKED | `KEEP` | Protocol, workflow, and final corpus decisions are aligned at policy level | None unless later corpus policy changes |
| `bare_jrnl_new_sample4.tex:766` | Final corpus centered on 2020-2025 but includes a small number of earlier studies | ROW-BACKED | `KEEP` | Consistent with corpus metadata and protocol framing | None |

## D. Study Selection Workflow

| Location | Current claim | Evidence class | Decision | Basis | Downstream impact |
|---|---|---|---|---|---|
| `bare_jrnl_new_sample4.tex:808` | Three-step PRISMA workflow: deduplication, screening, eligibility | ROW-BACKED | `KEEP` | Correct high-level workflow framing | None |
| `bare_jrnl_new_sample4.tex:811` | Deduplication was semi-automated with manual verification of ambiguous matches | PARTIAL | `SUPPLEMENT-ANCHOR` | Method framing is correct, but the full freeze-level dedup trail is incomplete | Dedup note/evidence pack should remain cited indirectly |
| `bare_jrnl_new_sample4.tex:816` | Two-reviewer calibration, independent screening, consensus, and third-reviewer arbitration | ROW-BACKED / RECONSTRUCTION-SUPPORTED | `KEEP` | Protocol-backed and not contradicted by current repo | None |
| `bare_jrnl_new_sample4.tex:818` | Canonical aggregate PRISMA counts were maintained in a structured screening ledger and reconciled against stage-specific audit records | RECONSTRUCTION-SUPPORTED | `KEEP` | This is exactly the right level of caution for mixed-strength evidence | Evidence-map files must remain consistent |
| `bare_jrnl_new_sample4.tex:818` | Earlier-stage records covered deduplication and title/abstract screening | PARTIAL | `SOFTEN` | True in a limited sense, but early-stage support is incomplete and partly external/noncanonical | Title/abstract and dedup notes must use matching language |
| `bare_jrnl_new_sample4.tex:818` | Later-stage records directly backed full-text assessment, exclusion, and inclusion ledgers | ROW-BACKED | `KEEP` | Strongly supported by current repo | None |
| `bare_jrnl_new_sample4.tex:818` | `222` assessed, `2` excluded, `220` included | ROW-BACKED | `KEEP` | Strong late-stage basis | Introduction/abstract/conclusion corpus counts remain safe |
| `bare_jrnl_new_sample4.tex:818` | Complete 220-paper ledger retained in the structured screening archive | ROW-BACKED | `KEEP` | Canonical included-study ledger exists | Evidence pack appendix should remain aligned |

## E. Flow Diagram

| Location | Current claim | Evidence class | Decision | Basis | Downstream impact |
|---|---|---|---|---|---|
| `bare_jrnl_new_sample4.tex:826` | `980` records identified from databases | RECONSTRUCTION-SUPPORTED | `KEEP` | Canonical count preserved; not fully row-backed | Evidence pack must keep reconstructed search-stage support visible |
| `bare_jrnl_new_sample4.tex:828` | `280` duplicate records removed | PARTIAL | `SUPPLEMENT-ANCHOR` | Canonical count preserved; current combined support is `188`, with `92` still open | Dedup evidence notes must remain explicit about the gap |
| `bare_jrnl_new_sample4.tex:830` | `700` records screened | PARTIAL | `SUPPLEMENT-ANCHOR` | Reconstruction-supported but not fully row-backed | Title/abstract reconstruction note becomes critical |
| `bare_jrnl_new_sample4.tex:832` | `478` records excluded after title/abstract screening | PARTIAL | `SUPPLEMENT-ANCHOR` | Partially supported; still not fully canonical at row level | Same as above |
| `bare_jrnl_new_sample4.tex:834` | `222` full-text articles assessed | ROW-BACKED | `KEEP` | Strong current basis | None |
| `bare_jrnl_new_sample4.tex:836` | `2` full-text exclusions and reason summary | ROW-BACKED | `KEEP` | Strong current basis | Full-text exclusion log should remain accessible |
| `bare_jrnl_new_sample4.tex:838` | `220` studies included | ROW-BACKED | `KEEP` | Strong current basis | Main corpus-wide statements remain stable |

## F. Editing Sequence Recommended

1. Edit only the `SOFTEN` and `SUPPLEMENT-ANCHOR` rows in Section III.
2. Keep all `ROW-BACKED` and stable `RECONSTRUCTION-SUPPORTED` rows unchanged unless a wording conflict is discovered.
3. After manuscript edits, re-check:
   - `manuscript/finalShortened/kontrol_listeleri/09_prisma_2020_reporting_checklist.md`
   - `manuscript/finalShortened/kontrol_listeleri/10_prisma_flow_evidence_map.md`
   - `screening/section3_evidence_reconstruction.md`
   - `manuscript/finalShortened/prisma_evidence_pack/MANIFEST.csv`
4. Run a repo-wide consistency pass for:
   - `980`, `280`, `700`, `478`, `222`, `220`
   - `freeze`, `dedup`, `canonical`, `structured screening ledger`
5. Re-run `screening/validate_section3_freeze.py`.

## G. Immediate Next Editing Targets

- `bare_jrnl_new_sample4.tex:755`
- `bare_jrnl_new_sample4.tex:811`
- `bare_jrnl_new_sample4.tex:818`
- Flow-figure interpretation around `bare_jrnl_new_sample4.tex:826-838` if explanatory wording is added elsewhere
