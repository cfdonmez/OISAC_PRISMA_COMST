# O-ISAC COMST Full Revision — G0 Prehuman Checkpoint

Date: `2026-09-01`

Status: `G0_PASS__G1_BLOCKED_PENDING_ALL_AUTHOR_LOCK`

Worktree: `C:\OISAC\worktrees\comst-full-20260901`

Branch: `rev/comst-full-20260901`

Frozen baseline commit: `13e3727241cb1d7726abb3ddb1833505c73c157f`

## Checkpoint purpose

This checkpoint records the safe start of the full-revision path. It freezes
the independent 27-page manuscript baseline, the Phase A--F authority hashes,
the exact 118-row conditional-comparison candidate set, the 15-study/16-report
source packet, and blank double-human verification infrastructure.

It is not a scientific verification lock, a completed full revision, or a
submission-ready manuscript.

## Completed at G0

- The full-revision tree is an independent root history created from the frozen
  Overleaf package; it has no balanced-revision ancestry or carryover.
- The frozen source ZIP hash is
  `FD69AD68C68B6408FF1B0CE5E584156F6B773FA78F199ADEDF0C9440B648AC88`.
- The baseline manuscript rebuilt cleanly to 27 pages. Its PDF SHA-256 is
  `4526521C1D260639EE7F046D11227C796D791FC2A766ADF184BE1264857998D2`.
- The canonical and rebuilt PDFs have the same `pdftotext -layout` logical
  content SHA-256:
  `921A79139A4271CE7210E86086EBBBC295DACED8C58B3D849705986A2FA1623A`.
- Final build-log checks found 0 undefined citations, 0 undefined references,
  0 LaTeX warnings, 0 overfull boxes, and 0 fatal errors. All 27 rendered pages
  passed visual inspection.
- The baseline hash manifest rechecked 11/11 files with 0 errors. The Phase
  A--F authority manifest rechecked 22/22 files with 0 errors.
- The candidate set is exactly 118 unique metric rows, representing 15 study
  clusters and 16 source reports. The report manifest sums to 118 rows; all
  16 source PDF paths, byte sizes, and SHA-256 values rechecked with 0 errors.
- Reviewer V1 and V2 issue forms each contain 118 unique rows and 81 columns:
  39 frozen context columns plus 42 human-entry columns. The forms match the
  register set and order exactly.
- All 4,956 human-entry cells in each form are blank. Both issue forms are
  byte-identical with SHA-256
  `FA5F6CA9BA628EB6BAD1E946C7B6829354DCC33AD106324BBCB9A3049BECD81D`.
- Canonical prefill audit compared 4,130 cells with 0 mismatches; register
  prefill audit compared 354 cells with 0 mismatches.
- The deterministic 12-row pilot candidate contains 4 communication, 4
  sensing, and 4 joint rows. It is a candidate only and has not been approved
  or reviewed.

## Key immutable artefacts

| Artefact | SHA-256 |
|---|---|
| `evidence/verification/PHASE_G_VERIFICATION_CODEBOOK_DRAFT.md` | `95DEAA678AFBBA80E648C555A7447BFF1C20F1040A5758CC0C4540F5046A6AAB` |
| `evidence/verification/PILOT_12_CANDIDATE_MANIFEST.csv` | `4592B376329BF0DFC687F3AB8BF17D5664072A2C78A1D04FFBD464CD8C489383` |
| `evidence/verification/STUDY_REPORT_MANIFEST_15_16.csv` | `E36425059801DD5DB84A21673B8DB3AD9FDC2F6100A418730CF21C489476C576` |
| `evidence/verification/REPORT_PDF_HASHES.sha256` | `E7EF49B2E347597F1F9230181F5F37D0329A25EEE6C1B5E6CE006F60872A1B98` |
| `outputs/pdf/OISAC_COMST_FULL_REVISION_G0_BASELINE_2026-09-01.pdf` | `4526521C1D260639EE7F046D11227C796D791FC2A766ADF184BE1264857998D2` |

## Human-review separation

The two people assigned to the balanced-revision Excel will review only the
frozen balanced workbook. That workbook is not modified, merged, copied, or
treated as Phase G human verification in this full-revision tree.

Full revision requires separately assigned V1 and V2 humans plus a separate
adjudicator. The blank V1/V2 CSV forms are preparation artefacts and have not
been issued.

## Closed scientific gates

- Amendment-001 remains `PROPOSED_NOT_LOCKED`.
- G1 remains `BLOCKED_PENDING_EXPLICIT_ALL_AUTHOR_LOCK`.
- G2 is `NOT_RUN_NOT_PASS`.
- No source value has been human verified in Phase G.
- No Phase G numeric claim, new operating point, ranking, pooling result, or
  manuscript wording has been added.
- The canonical Phase A--F files and the frozen balanced workbook remain
  unchanged.

## Required decision before G1 can pass

All authors must explicitly lock the 118/15/16 scope, name two different human
reviewers and a separate adjudicator, approve the codebook and 12-row pilot
criteria, accept overlay-only correction and default non-pooling, approve the
numeric-claim gate, and confirm the balanced-tree carryover prohibition.

After that lock, the next executable step is the independent 12-row V1/V2
pilot followed by adjudication and the G2 agreement test. Full 118-row review
cannot begin before the pilot passes.
