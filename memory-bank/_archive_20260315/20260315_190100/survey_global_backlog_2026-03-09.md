# Survey Global Backlog (updated 2026-03-15)

Owner: AI + User  
Scope: Whole-manuscript next steps after Section III freeze lock, Section V re-entry, and Section VI recovery merge.

## Status snapshot
- 2026-03-15 current-flow handoff:
  - core section omurgasi artik buyuk olcude tamam
  - Section IV package de aktif hale geldi
  - ana aciklar artik yeni section yazimi degil; figure polish / placement, bundle hygiene, ve sonra abstract + Section IX skeleton
- Repo usability karari (2026-03-14):
  - authoring / analysis / review katmanlari korunuyor
  - ancak bunlarin uzerine `manuscript/current_bundle/` altinda tek merkezli okuma/paketleme kati eklendi
  - bundan sonraki manuskript-level hizli kontrol, figure package kontrolu, ve yeni konusma handoff'lari icin once bu klasor kullanilsin
- Whole manuscript integration and release-gate QA tamamlandi at `review_package/*bundle*.md` level; current review-package bundles now integrate the canonical Section I-VIII sources.
- Review-package QA verdict is `CONDITIONAL PASS`; acik release kalemleri artik Section VI placement degil, kalan figure polishleri, bundle hygiene, ve gerekirse Section IX source kararidir.
- Whole-manuscript figure inventory cikartildi:
  - `.agent/workflows/whole_manuscript_figure_inventory_20260314.md`
  - mevcut durum Section I gercek assetler + Section IV/V/VI planned/spec katmani + Section III/Section V numbering collision riskini acikca belgeliyor
- Whole-manuscript section figure strategy cikartildi:
  - `.agent/workflows/whole_manuscript_section_figure_strategy_20260314.md`
  - Section II icin `2 fig + 2 table` explanatory/governance paketi, Section IV/V/VI icin zorunlu visual core, Section VII/VIII icin optional visual stance netlestirildi
- Whole-manuscript figure numbering policy artik freeze edildi:
  - `.agent/workflows/whole_manuscript_figure_numbering_policy_20260315.md`
  - Section I `Fig. 1-3` korunuyor; Section II ve sonrasinda section-prefixed numbering kullaniliyor
  - Section III / Section V collision kapandi; Section V artik `Fig. V-1 / Fig. V-2`
- Section II `Fig. II-1 / Fig. II-2` artik canonical metne insert edildi ve bundle katmanina propagate edildi; bu kalem "spec-only" durumdan cikti, kalan is yalnizca figure-level polish/cleanup.
- Section II `Table II-1 / Table II-2` de canonical metne insert edildi; Section II icin yapisal paket hedefi (`2 fig + 2 table`) saglandi.
- Section VI: authoritative recovery merge, core hardening, integration pass, ve figure insertion tamamlandi; bundan sonraki isler polish/revision seviyesindedir.
- Section V: publication-prose/architecture re-entry pass completed; `Fig. V-1 / Fig. V-2` gercek veri-temelli figure assetleri uretildi, canonical metne insert edildi, ve legacy `221 -> 220` denominator drift kapatildi.
- Section V figure prompt package yazildi:
  - `.agent/workflows/section_05_figure_prompts_20260315.md`
  - tablolar canonical source icinde hazir; denominator reconciliation da artik kapanmis durumda
- Section IV: section-internal prose polish ustune canonical artifact-package pass de uygulandi; `Table IV-D`, `Fig. IV-1`, ve `Fig. IV-2` artik aktif. Kalan is opsiyonel visual polish, caption refinement, ve upstream raw-analysis cleanup.
- Section VIII: editorial closeout ve QA refresh tamamlandi; section-level freeze-ready / monitor-only durumda.
- Section VIII: editorial closeout tamam, ancak artik `Fig. VIII-1` mandatory kabul edildigi icin closeout tamamlanmadan once figure package da eklenecek.
- Section III: repo-validated and conditionally freeze-ready; only archival upstream raw-export recovery remains open.
- Section VII: survey-alignment, reporting-policy lock, ve manuscript-level terminology/handoff consistency tamamlandi; yeni aktif lokal audit odağı Section VII closeout / integration taramasidir.

## Priority order (global)
1. Final figure package polish and remaining placement
   - whole-manuscript numbering policy freeze tamamlandi
   - Section II `Fig. II-1 / Fig. II-2` specs yazildi:
     - `.agent/workflows/section_02_figure_specs_20260314.md`
   - Section II user-side AI generation prompt'lari da yazildi:
     - `.agent/workflows/section_02_figure_ai_prompts_20260314.md`
   - Section II figure/table paketi artik metne baglandi; kalan is `fig_ii_1` visual polish ve `fig_ii_2` teknik cleanup
  - Section IV package artik aktif; kalan is polish / caption / cleanup
2. Section VII closeout / integration taramasi
3. Bundle hygiene and optional raw-source canonical cleanup
4. Abstract + Section IX skeleton drafting after figure/release-gate closeout
5. Section III archival upstream evidence recovery (valuable but non-blocking)

## Open tasks by section

### Section VI (section-level complete; figures inserted)
- `drafts/draft6_FD.md` recovery source'u `drafts/section_06_draft.md` yoluna geri tasindi.
- Pre-merge archive kaydi:
  - `drafts/_archive_20260205/section_06_draft_pre_recovery_merge_20260312_101453.md`
- `drafts/section_06_draft_reconstructed_20260310.md` yalnizca archival fallback olarak tutuluyor.
- `drafts/section_06_draft.md` core hardening, publication-flow polish, ve whole-manuscript integration pass ile stabilize edildi.
- `Fig. VI-1 / Fig. VI-2` assetleri canonical `drafts/` altina alinip dokumana yerlestirildi:
  - `drafts/fig_vi_1.jpg`
  - `drafts/fig_vi_2.jpg`
- Section VI icin AI tarafinda aktif bir pipeline-hygiene gorevi tutulmuyor.
- Section VI aktif section drafting sirasindan cikarildi; yalnizca final manuscript QA veya ileride figure polish baglaminda tekrar acilabilir.

Primary references:
- `drafts/draft6_FD.md`
- `drafts/section_06_draft.md`
- `drafts/section_06_draft_reconstructed_20260310.md`
- `drafts/section_06_recovery_note_20260310.md`
- `.agent/workflows/section_06_improvement_notes.md`
- `.agent/workflows/section_06_action_plan.md`
- `memory-bank/section6_recovery_notes.md`

### Section V (figure/cross-reference gate mostly closed)
- Figure prompt/spec package mevcut:
  - `.agent/workflows/section_05_figure_prompts_20260315.md`
- Real figure assets already produced from canonical `analysis/V_ev_v2/*.csv` sources:
  - `drafts/fig_v_1.png`
  - `drafts/fig_v_2.png`
- Keep `Table VII` as the head-to-head comparative artifact; leave frontier semantics in text + `Fig. V-2`.
- Legacy paper-level `221 papers` denominator language canonical `220` included-corpus framing ile uzlastirildi.
- Bundan sonra Section V icin acik kalem denominator degil; gerekirse son caption/note polish ve whole-manuscript drift-check.

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
  - final release icin Section IV / VI / II figure-side polishleri ve gerekiyorsa Section IX source karari acik kaldi
- Figure-package gate icin mevcut karar ihtiyaci:
  - numbering policy freeze tamamlandi ve korunmali
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
- Mermaid PRISMA block VSCode preview uyumu icin sade `flowchart TB` yapisina refresh edildi.
- Not:
  - Section V ile onceki dogrudan figure collision kapandi
  - whole-manuscript numbering policy artik freeze edildi
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

### Section IV (artifact package active; polish/cleanup only)
- `Table IV-D` canonical metne eklendi.
- `Fig. IV-1 / Fig. IV-2` canonical filtreli veri hattindan uretildi ve metne baglandi.
- Preserve current publication prose and recheck final caption/reference wording in whole-manuscript layout.
- Ensure taxonomy labels and corpus counts stay aligned with Section V-VII.
- Dikkat:
  - aktif figure'ler guvenli
  - ancak `analysis/IV_ev_v2/cluster_map.csv` ile `section4B/C/D_evidence.csv` dogrudan yeniden kullanilacaksa canonical filter yeniden uygulanmali.

Primary references:
- `memory-bank/section4_camera_ready_notes.md`
- `.agent/workflows/section_04_artifact_package_20260315.md`

### Section VIII (freeze-ready; monitor only)
- Editorial-only standardization pass tamamlandi.
- `analysis/VIII_cr_mrg_v1/section_08_final_QA.md` refresh edildi ve `READY: PASS` korundu.
- Guncel ek karar:
  - `Fig. VIII-1` mandatory
  - local workflow note:
    - `.agent/workflows/section_08_closeout_checklist_20260315.md`
- Bundan sonra yalnizca yeni text degisikligi olursa QA refresh gerekir demek artik yeterli degil; once `Fig. VIII-1` package'i de tamamlanacak.

Primary references:
- `.agent/workflows/section_08_improvement_notes.md`
- `analysis/s08_ref_swp_note.md`

### Section VII (freeze-ready; closeout audit next)
- Strict reporting policy and manuscript-level plane-separation wording pass tamamlandi.
- `Fig. VII-1` artik aktif:
  - `drafts/fig_vii_1.jpg`
- Bundan sonraki aktif yerel is:
  - closeout / integration taramasi
  - `Fig. VII-1` visual/text cleanup
  - ek figure gerekir mi kontrolu
  - Section VI -> VII ve VII -> VIII handoff dili son kez dogrulama

Primary references:
- `.agent/workflows/section_07_improvement_notes.md`

## Release gate (whole manuscript)
- Review-package manuscript bundles refreshed from canonical Section I-VIII sources.
- Section-level numbers and labels consistent across the final section inventory.
- Section VI canonical working path preserved and quality-hardened after recovery merge.
- PRISMA statements and logs fully aligned.
- No plane-mix or metric-alias wording regressions.
- Final figure insertion complete.
- Section V legacy denominator language canonical included-corpus framing ile uzlastirildi.
- Section IX source present or final section inventory explicitly reduced.
- Final manuscript QA pass complete.
