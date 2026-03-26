# Active Context

Son Guncelleme: 2026-03-12
Guncelleyen: AI + Kullanici

---

## Su Anki Faz

Section III (Methodology) repo-validated conditionally-freeze-ready duruma getirildi. Section IV section-ici camera-ready polish tamamlandi. Aktif manuskript odagi artik Section VI recovery + canonical merge, Section VIII editorial closeout, Section IV/VI/VII cross-manuscript consistency, ve tam manuskript entegrasyon hazirligi.

Ek guncel odak (2026-03-12):
- Section V production re-entry basladi; draft survey mimarisi baglaminda yeniden okunup aciklar ayrildi.
- `drafts/section_05_template.md` icinde publication-prose pass uygulandi ve `Table V / VI / VII` summary katmani eklendi.
- Section V icin kalici architecture/camera-ready note eklendi:
  - `memory-bank/section5_camera_ready_notes.md`
- Kalan Section V aciklari daraltildi:
  - `Fig. 4 / Fig. 5` asset uretimi
  - Section I / IV / VIII consistency + final numbering/crossref kontrolu
- Section V structure karari uygulandi:
  - `V-E` bagimsiz alt-bolum yerine Section V sonunda closeout synthesis olarak tutuldu
- Section V Table VII scope karari uygulandi:
  - `Table VII` head-to-head comparative artifact olarak tutuldu
  - CRQ/frontier semantics metin + `Fig. 5` tarafinda birakildi
- Re-entry hatirlatmasi:
  - Siradaki ortak karar/uygulama adimi `Fig. 4 / Fig. 5` icin kisa specification pass, hemen ardindan gercek asset uretimidir
  - "Asset production" hem figure tasarimini netlestirmeyi hem de gercek figure dosyalarini uretmeyi ifade eder

Ek guncel odak (2026-03-11):
- Survey'nin late-stage uretim fazinda figure/table/equation/cross-reference planlamasi repo-icindeki COMST-jargon ve metric-governance kaynaklarindan turetilecek; disaridan ad-hoc terminoloji listesi kullanilmayacak.
- Canonical COMST writing/jargon kaynaklari:
  - `memory-bank/goldenModel.md`
  - `memory-bank/master_writing_guide.md`
- Canonical metric/mapping kaynaklari:
  - `analysis/V_ev_v2/axis_definitions.md`
  - `analysis/V_ev_v2/s5b_met_gov.csv`
  - `analysis/VI_ev_v2/axis_definitions.md`
  - `analysis/VII_ev_v2/axis_definitions.md`
  - `analysis/VIII_ev_v1/axis_definitions.md`
- Yakin donem geri giris odagi:
  - Section IV production inventory + cross-manuscript integration-check

Ek guncel odak (2026-03-10):
- Final canonical late-stage PRISMA durumu:
  - `222` full-text assessed
  - `2` full-text excluded
  - `220` studies included
- Section III validator geciyor:
  - `screening/validate_section3_freeze.py`
- Section III icin memory-bank destekli inferred provenance katmani eklendi:
  - `search/inferred_freeze_provenance_timeline_20260310.csv`
  - `search/inferred_freeze_provenance_from_memory_bank_20260310.md`
- Kalan tek buyuk Section III acigi arsivsel:
  - freeze-time WoS / raw-search bundle eksik
  - takip notu: `.agent/workflows/section3_external_input_need_20260310.md`
- Section IV 2026-03-10 camera-ready prose polish pass'i uygulandi; kalan durum cross-manuscript terminology/caption/release-gate kontroludur.
- Section VI accidental overwrite sonrasi recovery zinciri netlestirildi.
- User-preserved Section VI recovery source bulundu:
  - `drafts/draft6_FD.md`
- Section VI recovery hierarchy:
  - authoritative recovery source: `drafts/draft6_FD.md`
  - partially restored working draft: `drafts/section_06_draft.md`
  - archival reconstruction: `drafts/section_06_draft_reconstructed_20260310.md`
  - incident note: `drafts/section_06_recovery_note_20260310.md`
- Section VIII manuscript-level reference sweep tamamlandi ve Section VIII near-freeze durumda.
- Survey genel backlog:
  - `memory-bank/survey_global_backlog_2026-03-09.md`

Odak degisimi:
- Section II kalite kapama notlari korunuyor (referans baseline).
- Section III artik birincil manuskript blokaji olmaktan cikti; kalan acik raw-export seviyesinde.
- Section IV artik birincil rewrite isi degil; polish sonrasi integration-check seviyesinde.
- Section VI artik once recovery/merge, sonra consistency hardening gerektiriyor.
- Section VIII sadece editorial standardization + gerekirse QA refresh bekliyor.
- Siradaki ana manuskript isi: Section VI recovery merge pass.

---

## Yapilanlar (bu asamaya kadar)

### Section II (Fundamentals) - kalite kapama
- II-A..II-E citation destek kontrolu v3 CSV'lerle tekrar dogrulandi.
- II-E tarafinda unsupported anchor riski temizlendi; destekli anchor setine gecildi.
- II-D tarafinda metric-governance kontrati (plane separation + delta_z / delta_r_min ayrimi) final pass ile dogrulandi.
- Section II draft sonuna COMST/PRISMA finalization checklist eklendi:
  - Figure/Table hedefleri (Section II icin 2 fig + 2 table)
  - freeze oncesi kontrol listesi
- Ilgili dosyalar:
  - `drafts/section_02_fundamentals_draft.md`
  - `.agent/workflows/section_02D_crosscheck.md`
  - `.agent/workflows/section_02E_crosscheck.md`
  - `.agent/workflows/section_02D_v3_change_notes.md`

### Section III (Methodology) - freeze hardening ve audit reconstruction
- Registration truth lock tamamlandi; OSF kaydi metodoloji/protokol/checklist dosyalarina islendi.
- Search consistency lock tamamlandi; formal source policy IEEE Xplore + Scopus + Web of Science olarak netlestirildi.
- PRISMA flow integrity canonical dosyalarda kilitlendi:
  - `search/search_log.csv`
  - `screening/prisma_flow_counts.csv`
  - `screening/excluded_fulltext_log.csv`
- Full-text ve included corpus reconstruction tamamlandi:
  - `screening/fulltext_assessed_reconstruction.csv` -> `222`
  - `screening/included_studies_canonical.csv` -> `220`
  - `screening/canonical_included_corpus_ledger.csv` -> `220`
- `O_ISAC_347` canonical corpus disina alindi ve `EXC-UNVERIFIED-FULLTEXT` olarak kapatildi.
- `O_ISAC_044` repo-verified included olarak uzantisiz PDF iziyle reconcile edildi.
- Section III icin reconstructed search-stage freeze pack olusturuldu:
  - `search/formal_identification_reconstruction_20251130.csv`
  - `search/upstream_prisma_reconstruction_20260310.csv`
  - `search/reconstructed_freeze_bundle_note_20260310.md`
- Memory-bank destekli inferred provenance katmani eklendi:
  - `search/inferred_freeze_provenance_timeline_20260310.csv`
  - `search/inferred_freeze_provenance_from_memory_bank_20260310.md`
- Section III validation script'i eklendi ve PASS verdi:
  - `screening/validate_section3_freeze.py`
- Durum notlari:
  - `screening/section3_evidence_reconstruction.md`
  - `.agent/workflows/section3_freeze_closure_note_20260310.md`
  - `.agent/workflows/section3_completion_task_list_20260310.md`
  - `.agent/workflows/section3_external_input_need_20260310.md`

### Section IV (Taxonomy) - camera-ready not kaydi
- Section IV-A..E bolumleri zorunlu veri dosyalariyla (v2 evidence setleri) yeniden yazildi.
- 2026-03-10 camera-ready prose polish pass'i uygulandi:
  - ham schema/pipeline etiketleri temizlendi
  - audit kategori adlari publication prose'a cevrildi
  - tablo basliklari ve satir adlari daha COMST-uyumlu hale getirildi
- Kalici not dosyasi olusturuldu:
  - `memory-bank/section4_camera_ready_notes.md`
- Section II benzer kayit kontrolu dogrulandi:
  - Bu dosyada "Section II (Fundamentals) - kalite kapama" blogu mevcut
  - Section II draft sonunda finalization checklist mevcut (`drafts/section_02_fundamentals_draft.md`)

### Section V (Performance / Trade-off) - production re-entry ve architecture note
- Section V draft survey mimarisi baglaminda yeniden okundu; section-ici aciklar ile cross-manuscript aciklar ayrildi.
- `drafts/section_05_template.md` icinde publication-prose pass uygulandi.
- Canonical `analysis/V_ev_v2/*` kaynaklarindan `Table V`, `Table VI`, ve `Table VII` summary katmani taslaga eklendi.
- `V-E` bagimsiz alt-bolum olmaktan cikarilip Section V sonunda bounded closeout synthesis olarak yeniden konumlandi.
- `Table VII` kapsam karari freeze edildi; tablo comparative slice rolunde tutuldu.
- Kalici memory-bank notu eklendi:
  - `memory-bank/section5_camera_ready_notes.md`
- Kalan durum yeni veri/yeniden extraction degil; figure asset ve cross-manuscript consistency seviyesindedir.

### Section VI (Enablers / System-Level Co-Design) - recovery triage
- Section VI working draft path'inde accidental overwrite sonrasi recovery calismasi kayda alindi.
- `drafts/section_06_draft.md` partial restored working draft olarak tutuluyor.
- `drafts/section_06_draft_reconstructed_20260310.md` overwrite sonrasi archival reconstruction olarak saklaniyor.
- `drafts/section_06_recovery_note_20260310.md` olay izi olarak olusturuldu.
- User-saved richer working draft bulundu:
  - `drafts/draft6_FD.md`
- Recovery source priority kilitlendi:
  1. `drafts/draft6_FD.md`
  2. `drafts/section_06_draft.md`
  3. `drafts/section_06_draft_reconstructed_20260310.md`
  4. `drafts/section_06_recovery_note_20260310.md`
- Mevcut Section VI kalite/acik notlari hala aktif:
  - `.agent/workflows/section_06_improvement_notes.md`
  - `.agent/workflows/section_06_action_plan.md`
- Kalici memory-bank notu eklendi:
  - `memory-bank/section6_recovery_notes.md`

### Section VIII (Challenges / Outlook) - closeout prep
- Section VIII icin manuscript-wide reference sweep tamamlandi.
- Stale referanslar aktif manuscript/review/template katmaninda temizlendi.
- Kalan is editorial standardization + metin degisirse QA refresh olarak daraltildi.
- Ilgili notlar:
  - `.agent/workflows/section_08_improvement_notes.md`
  - `analysis/s08_ref_swp_note.md`

---

## Yapilacaklar (hemen siradaki adimlar)

0) Section VI recovery merge ve canonical lock
- `drafts/draft6_FD.md` icindeki user-preserved icerigi `drafts/section_06_draft.md` yoluna geri birlestir.
- Artifact map, evidence table, notation scaffolding ve VI-A..VI-F drafting malzemesini merge sirasinda koru.
- `drafts/section_06_draft_reconstructed_20260310.md` merge dogrulanana kadar yalnizca archival fallback olarak tut.
- `.agent/workflows/section_06_improvement_notes.md` icindeki gate'leri merge sonrasi tekrar uygula:
  - strict-vs-raw prevalence policy
  - invalid OPA/RIS metric filtering
  - readiness rerun after Section 6F
  - weak-anchor families (ML/PIC/programmable/photonic_generation) icin stronger anchor veya qualitative-only etiketleme

1) Section VIII closeout
- `VIII-A..VIII-E` baslik/subheading standardization (yalnizca editorial pass).
- Section VIII metni degisirse `analysis/VIII_cr_mrg_v1/section_08_final_QA.md` refresh.
- Opsiyonel: legacy outline/template encoding artefact temizligi.

2) Section IV / VI / VII cross-manuscript consistency hardening
- Section IV icin final manuskriptte terminology/caption consistency kontrolu yap.
- Section VI icin strict-vs-raw prevalence policy freeze et ve invalid metric filtering aciklarini kapat.
- Section VII icin scope mismatch / weak evidence / strict reporting policy kilidini tamamla.
- Tum bu adimlarda Section II metric-governance dili korunacak.

3) Whole-manuscript integration prep
- Section-level sayi ve label senkronunu I-IX boyunca son kez kontrol et.
- Introduction, methodology, taxonomy ve challenge/roadmap akisinin ayni corpus sayilariyla konustugundan emin ol.
- Final QA/release gate icin notlari tek yerde topla.

4) Section III archival recovery (non-blocking but valuable)
- Bulunursa freeze-time WoS / merged raw-search export bundle geri kazanilacak.
- Takip:
  - `.agent/workflows/section3_external_input_need_20260310.md`

---

## Aktif Riskler

- Section VI canonical path su anda en zengin user-authored icerigi tam yansitmiyor olabilir; recovery merge tamamlanana kadar omission riski var.
- Section VI prevalence claim'leri raw metrics strict gate olmadan kullanilirsa adoption seviyesini oldugundan yuksek gosterebilir.
- Section VI tablo ve synthesis'lerinde invalid enabler metric satirlari filter uygulanmadan kalabilir.
- Section III upstream PRISMA zinciri (`980 / 280 / 700`) hala tam row-level raw-export-backed degil.
- Eksik dis girdi:
  - WoS / Clarivate freeze export
  - `data/raw_search_results/` veya esdeger merged raw-search bundle
- Section IV icin section-ici polish tamamlandi, ancak final manuskriptte terminology/caption drift riski kaldi.
- Section VI ve VII tarafinda strict reporting policy ve consistency gate kararlarinin finalize edilmesi gerekiyor.
- Section II metninde yayin oncesi teknik temizlik (BOM + ic yorum temizligi) gerekebilir.

---

## Degismez Governance Kurallari

- Plane separation: OSNR optical-plane; SNR/ESNR electrical-plane.
- Metric aliasing yok: resolution, accuracy, `delta_r_min`, `sigma_r`, `delta_z` ayrimi korunacak.
- Her claim icin anchor + context zorunlu.
- PRISMA scope lock: canonical corpus ve flow sayilari sectionlar arasi degismeyecek.
- Current canonical Section III late-stage lock:
  - `222 assessed`
  - `2 excluded`
  - `220 included`
