# Survey Global Backlog (updated 2026-03-14)

Owner: AI + User  
Scope: Whole-manuscript next steps after Section III freeze lock, Section V re-entry, and Section VI recovery merge.

## Status snapshot
- Repo usability karari (2026-03-14):
  - authoring / analysis / review katmanlari korunuyor
  - ancak bunlarin uzerine `manuscript/current_bundle/` altinda tek merkezli okuma/paketleme kati eklendi
  - bundan sonraki manuskript-level hizli kontrol, figure package kontrolu, ve yeni konusma handoff'lari icin once bu klasor kullanilsin
- Whole manuscript integration and release-gate QA tamamlandi at `review_package/*bundle*.md` level; current review-package bundles now integrate the canonical Section I-VIII sources.
- Review-package QA verdict is `CONDITIONAL PASS`; acik release kalemleri Section V legacy `221 papers` denominator dili, final figure asset/placement, ve gerekirse Section IX source kararidir.
- Whole-manuscript figure inventory cikartildi:
  - `.agent/workflows/whole_manuscript_figure_inventory_20260314.md`
  - mevcut durum Section I gercek assetler + Section IV/V/VI planned/spec katmani + Section III/Section V numbering collision riskini acikca belgeliyor
- Whole-manuscript section figure strategy cikartildi:
  - `.agent/workflows/whole_manuscript_section_figure_strategy_20260314.md`
  - Section II icin `2 fig + 2 table` explanatory/governance paketi, Section IV/V/VI icin zorunlu visual core, Section VII/VIII icin optional visual stance netlestirildi
- Section II `Fig. II-1 / Fig. II-2` artik canonical metne insert edildi ve bundle katmanina propagate edildi; bu kalem "spec-only" durumdan cikti, kalan is yalnizca figure-level polish/cleanup.
- Section II `Table II-1 / Table II-2` de canonical metne insert edildi; Section II icin yapisal paket hedefi (`2 fig + 2 table`) saglandi.
- Section VI: authoritative recovery merge, core hardening, and integration pass tamamlandi; `Fig. VI-1 / Fig. VI-2` asset uretimi ve dokumana yerlestirme kullanici tarafinda kaldi.
- Section V: publication-prose/architecture re-entry pass completed; `Fig. 4 / Fig. 5` specification + asset production remain open.
- Section IV: section-internal camera-ready polish applied; manuscript-level consistency contract checked, kalan is yalnizca final integration/cross-reference kontrolu.
- Section VIII: editorial closeout ve QA refresh tamamlandi; section-level freeze-ready / monitor-only durumda.
- Section III: repo-validated and conditionally freeze-ready; only archival upstream raw-export recovery remains open.
- Section VII: survey-alignment, reporting-policy lock, ve manuscript-level terminology/handoff consistency tamamlandi; section-level freeze-ready / monitor-only durumda.

## Priority order (global)
1. Final figure package and placement
   - first freeze whole-manuscript numbering policy and resolve Section III / Section V collision
   - Section II `Fig. II-1 / Fig. II-2` specs yazildi:
     - `.agent/workflows/section_02_figure_specs_20260314.md`
   - Section II user-side AI generation prompt'lari da yazildi:
     - `.agent/workflows/section_02_figure_ai_prompts_20260314.md`
   - Section II figure/table paketi artik metne baglandi; kalan is `fig_ii_1` visual polish ve `fig_ii_2` teknik cleanup
2. Section V legacy denominator reconciliation + QA refresh
3. Abstract + Section IX skeleton drafting after figure/release-gate closeout
4. Section III archival upstream evidence recovery (valuable but non-blocking)

## Open tasks by section

### Section VI (section-level complete; monitor only)
- `drafts/draft6_FD.md` recovery source'u `drafts/section_06_draft.md` yoluna geri tasindi.
- Pre-merge archive kaydi:
  - `drafts/_archive_20260205/section_06_draft_pre_recovery_merge_20260312_101453.md`
- `drafts/section_06_draft_reconstructed_20260310.md` yalnizca archival fallback olarak tutuluyor.
- `drafts/section_06_draft.md` core hardening, publication-flow polish, ve whole-manuscript integration pass ile stabilize edildi.
- `Fig. VI-1 / Fig. VI-2` gercek asset uretimi ve dokumana yerlestirme kullanici tarafinda yapilacak.
- Section VI icin AI tarafinda aktif bir pipeline-hygiene gorevi tutulmuyor.
- Section VI aktif section drafting sirasindan cikarildi; yalnizca final manuscript QA ve kullanici figure placement baglaminda tekrar acilabilir.

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
- Reconcile legacy paper-level `221 papers` denominator language against the canonical `220` included-corpus framing before final release QA closeout.

Primary references:
- `memory-bank/section5_camera_ready_notes.md`
- `drafts/section_05_template.md`
- `drafts/section_05_correction_notes.md`
- `.agent/workflows/section_05_draft_playbook.md`

### Whole manuscript (integration complete; release gate still open)
- `review_package/01_manuscript_bundle.md` ve `review_package/COMST_review_bundle_01_manuscript.md` canonical Section I-VIII kaynaklarindan yeniden uretildi.
- Figure inventory note:
  - `.agent/workflows/whole_manuscript_figure_inventory_20260314.md`
- Section-level figure strategy note:
  - `.agent/workflows/whole_manuscript_section_figure_strategy_20260314.md`
- Release-gate QA notu:
  - `review_package/05_release_gate_QA.md`
- QA sonucu `CONDITIONAL PASS`:
  - bundle seviyesi stale/incomplete durum temizlendi
  - Section VII / VIII guncel kaynaklari integrated
  - final release icin figure insertion, Section V denominator uzlasimi, ve gerekiyorsa Section IX source karari acik kaldi
- Figure-package gate icin mevcut karar ihtiyaci:
  - whole-manuscript numbering policy freeze
  - Section III `Fig. 5` ile Section V `Fig. 4 / Fig. 5` arasindaki collision'in cozulmesi
  - Section II spec'leri kullanilarak `Fig. II-1 / Fig. II-2` user-side AI visual generation
  - Section IV / V / VI final figure package kapsam kararinin kullaniciyla birlikte netlestirilmesi

### Abstract / Section IX (deliberately deferred)
- Bu iki bolumun final prose'u simdilik bilerek ertelendi.
- Sebep:
  - final sayilar, figure paketi, ve release-gate duzeltmeleri sabitlenmeden erken yazim hizli stale olabilir
- Plan:
  - figure paketi ve kalan release-gate tutarliliklari tamamlandiktan sonra
  - abstract + Section IX icin once skeleton draft, sonra final polishing

### Section III (conditionally freeze-ready)
- Canonical late-stage lock now holds:
  - `222` full-text assessed
  - `2` full-text excluded
  - `220` included
- Local methodology numbering cleanup uygulandi:
  - eligibility table `Table III-1`
  - PRISMA flow anchor `Fig. III-1`
- Repo-ici dosya yolu dili publication-facing prose'a cevrildi; metodoloji artik internal path gosterimi icermiyor.
- Not:
  - Section V ile onceki dogrudan `Fig. 5` collision kapandi
  - ancak whole-manuscript numbering policy halen global olarak freeze bekliyor
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
- Preserve polished publication prose during final manuscript integration.
- Recheck Fig. IV-1 / Fig. IV-2 / Table IV-* references in final manuscript layout.
- Ensure taxonomy labels and corpus counts stay aligned with Section V-VII.

Primary references:
- `memory-bank/section4_camera_ready_notes.md`
- `.agent/workflows/section_04_improvement_notes.md`

### Section VIII (freeze-ready; monitor only)
- Editorial-only standardization pass tamamlandi.
- `analysis/VIII_cr_mrg_v1/section_08_final_QA.md` refresh edildi ve `READY: PASS` korundu.
- Bundan sonra yalnizca yeni text degisikligi olursa QA refresh gerekir.

Primary references:
- `.agent/workflows/section_08_improvement_notes.md`
- `analysis/s08_ref_swp_note.md`

### Section VII (freeze-ready; monitor only)
- Strict reporting policy and manuscript-level plane-separation wording pass tamamlandi.
- Bundan sonra yalnizca yeni text degisikligi veya final manuscript entegrasyonu sirasinda tekrar QA gerekir.

Primary references:
- `.agent/workflows/section_07_improvement_notes.md`

## Release gate (whole manuscript)
- Review-package manuscript bundles refreshed from canonical Section I-VIII sources.
- Section-level numbers and labels consistent across the final section inventory.
- Section VI canonical working path preserved and quality-hardened after recovery merge.
- PRISMA statements and logs fully aligned.
- No plane-mix or metric-alias wording regressions.
- Final figure insertion complete.
- Section V legacy denominator language reconciled with the canonical included-corpus framing.
- Section IX source present or final section inventory explicitly reduced.
- Final manuscript QA pass complete.
