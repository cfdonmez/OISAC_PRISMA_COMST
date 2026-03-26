# Survey Global Backlog (updated 2026-03-10)

Owner: AI + User  
Scope: Whole-manuscript next steps after Section III freeze lock and Section VI recovery discovery.

## Status snapshot
- Section VI: recovery/merge required after accidental overwrite; user-saved `drafts/draft6_FD.md` is now the authoritative recovery source.
- Section IV: section-internal camera-ready polish applied; only cross-manuscript terminology/caption consistency remains.
- Section VIII: near-freeze; only editorial standardization + QA refresh if text changes.
- Section III: repo-validated and conditionally freeze-ready; only archival upstream raw-export recovery remains open.
- Section VII: evidence packs exist, but improvement notes still list consistency and strict-gating risks.

## Priority order (global)
1. Section VI recovery and canonical merge
2. Section VIII editorial standardization (closeout gate)
3. Section IV / VI / VII cross-section consistency hardening (cross-section gate)
4. Full manuscript integration and final QA (release gate)
5. Section III archival upstream evidence recovery (valuable but non-blocking)

## Open tasks by section

### Section VI (recovery + consistency gate)
- `drafts/draft6_FD.md` is the authoritative recovery source for the richer user-preserved Section VI draft.
- Merge recovered material back into `drafts/section_06_draft.md` without dropping later valid fixes.
- Preserve artifact maps, evidence tables, notation scaffolding, and VI-A..VI-F drafting material during merge.
- Keep `drafts/section_06_draft_reconstructed_20260310.md` only as archival fallback until merge is verified.
- After merge, re-apply quality gates:
  - freeze strict-vs-raw prevalence policy
  - filter invalid OPA/RIS metric rows
  - rerun readiness after Section 6F
  - quarantine or re-anchor weak evidence for ML/PIC/programmable/photonic_generation

Primary references:
- `drafts/draft6_FD.md`
- `drafts/section_06_draft.md`
- `drafts/section_06_draft_reconstructed_20260310.md`
- `drafts/section_06_recovery_note_20260310.md`
- `.agent/workflows/section_06_improvement_notes.md`
- `.agent/workflows/section_06_action_plan.md`
- `memory-bank/section6_recovery_notes.md`

### Section III (conditionally freeze-ready)
- Canonical late-stage lock now holds:
  - `222` full-text assessed
  - `2` full-text excluded
  - `220` included
- Validator passes:
  - `screening/validate_section3_freeze.py`
- Remaining non-blocking archival need:
  - recover freeze-time WoS / merged raw-search bundle to fully row-back `980 / 280 / 700`
- Tracking notes:
  - `.agent/workflows/section3_freeze_closure_note_20260310.md`
  - `.agent/workflows/section3_external_input_need_20260310.md`

Primary references:
- `screening/section3_evidence_reconstruction.md`
- `.agent/workflows/section3_completion_task_list_20260310.md`
- `memory-bank/activeContext.md`

### Section IV (post-polish integration check)
- Preserve polished publication prose while checking cross-manuscript terminology consistency.
- Recheck Fig. IV-1 / Fig. IV-2 / Table IV-* references in final manuscript layout.
- Ensure taxonomy labels and corpus counts stay aligned with Section V-VII.

Primary references:
- `memory-bank/section4_camera_ready_notes.md`
- `.agent/workflows/section_04_improvement_notes.md`

### Section VIII (closeout)
- Editorial-only heading/subheading standardization in `VIII-A..VIII-E`.
- Refresh `analysis/VIII_cr_mrg_v1/section_08_final_QA.md` only if text changes.
- Optional low-priority cleanup: legacy encoding artefacts.

Primary references:
- `.agent/workflows/section_08_improvement_notes.md`
- `analysis/s08_ref_swp_note.md`

### Section VII (consistency hardening)
- Resolve/quarantine scope mismatch rows.
- Freeze strict reporting policy and run final plane-separation wording pass.

Primary references:
- `.agent/workflows/section_07_improvement_notes.md`

## Release gate (whole manuscript)
- Section-level numbers and labels consistent across I-IX.
- Section VI canonical working path declared after recovery merge.
- PRISMA statements and logs fully aligned.
- No plane-mix or metric-alias wording regressions.
- Final manuscript QA pass complete.
