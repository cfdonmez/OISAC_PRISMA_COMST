# Survey Global Backlog (updated 2026-03-12)

Owner: AI + User  
Scope: Whole-manuscript next steps after Section III freeze lock, Section V re-entry, and Section VI recovery merge.

## Status snapshot
- Section VI: authoritative recovery merge, core hardening, and integration pass tamamlandi; `Fig. VI-1 / Fig. VI-2` asset uretimi ve dokumana yerlestirme kullanici tarafinda kaldi.
- Section V: publication-prose/architecture re-entry pass completed; `Fig. 4 / Fig. 5` specification + asset production remain open.
- Section IV: section-internal camera-ready polish applied; only cross-manuscript terminology/caption consistency remains.
- Section VIII: near-freeze; only editorial standardization + QA refresh if text changes.
- Section III: repo-validated and conditionally freeze-ready; only archival upstream raw-export recovery remains open.
- Section VII: evidence packs exist, but improvement notes still list consistency and strict-gating risks.

## Priority order (global)
1. Section VIII editorial standardization (closeout gate)
2. Section IV / VII cross-section consistency hardening (cross-section gate)
3. Section V figure specification + asset production
4. Full manuscript integration and final QA (release gate)
5. Section III archival upstream evidence recovery (valuable but non-blocking)

## Open tasks by section

### Section VI (stabilized; user-owned figure placement pending)
- `drafts/draft6_FD.md` recovery source'u `drafts/section_06_draft.md` yoluna geri tasindi.
- Pre-merge archive kaydi:
  - `drafts/_archive_20260205/section_06_draft_pre_recovery_merge_20260312_101453.md`
- `drafts/section_06_draft_reconstructed_20260310.md` yalnizca archival fallback olarak tutuluyor.
- `drafts/section_06_draft.md` core hardening, publication-flow polish, ve whole-manuscript integration pass ile stabilize edildi.
- `Fig. VI-1 / Fig. VI-2` gercek asset uretimi ve dokumana yerlestirme kullanici tarafinda yapilacak.
- Section VI icin AI tarafinda aktif bir pipeline-hygiene gorevi tutulmuyor.

Primary references:
- `drafts/draft6_FD.md`
- `drafts/section_06_draft.md`
- `drafts/section_06_draft_reconstructed_20260310.md`
- `drafts/section_06_recovery_note_20260310.md`
- `.agent/workflows/section_06_improvement_notes.md`
- `.agent/workflows/section_06_action_plan.md`
- `memory-bank/section6_recovery_notes.md`

### Section V (figure/cross-reference gate)
- Freeze a short specification for `Fig. 4` and `Fig. 5`.
- Produce real figure assets from canonical `analysis/V_ev_v2/*.csv` sources.
- Keep `Table VII` as the head-to-head comparative artifact; leave frontier semantics in text + `Fig. 5`.
- Recheck numbering/cross-references against Section I / IV / VIII during integration.

Primary references:
- `memory-bank/section5_camera_ready_notes.md`
- `drafts/section_05_template.md`
- `drafts/section_05_correction_notes.md`
- `.agent/workflows/section_05_draft_playbook.md`

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
- Section VI canonical working path preserved and quality-hardened after recovery merge.
- PRISMA statements and logs fully aligned.
- No plane-mix or metric-alias wording regressions.
- Final manuscript QA pass complete.
