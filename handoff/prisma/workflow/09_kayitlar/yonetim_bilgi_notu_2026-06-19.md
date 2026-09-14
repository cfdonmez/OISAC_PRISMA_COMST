# Yonetim Bilgi Notu - Step 2 Pilot Aramalar

Tarih: 2026-06-19

Bu not, O-ISAC PRISMA workflow icinde 2026-06-18/19 pilot arama islerinin yonetim ozetidir. Pilot arama kayitlari final PRISMA flow count degildir; screening, deduplication, included studies ve final search count alanlari TBD olarak kalir. Search freeze etiketi `planned search freeze date: June 30, 2026` olarak korunmustur.

## Mevcut Asama

- Step 1: Completed / locked.
- Step 2: Search strategy finalization and pilot testing asamasinda, in progress.
- Step 3: Final search execution not started; planned after June 30, 2026.
- Step 4-8: Deduplication, screening, data extraction, TQAF assessment ve synthesis not started.
- PRISMA flow counts: TBD; pilot sayilari buraya aktarilmadi.

## Yapilan Isler

- Kaynak seti netlestirildi: core primary sources Scopus ve IEEE Xplore; supplementary platform sources ScienceDirect, SpringerLink, Wiley Online Library ve Taylor & Francis Online. Web of Science ve ACM Digital Library formal current source set disinda birakildi.
- Legacy `included_studies_canonical.csv` dosyasinin seed study set veya validation set olarak kullanilmayacagi kayda gecirildi.
- IEEE Xplore pilotlari islendi ve canonical raw export klasorune ayrildi.
- IEEE candidate pilot package: IEEE-PILOT-S1A, IEEE-PILOT-S1B-R2 ve IEEE-PILOT-S1F-R2.
- IEEE rejected/replaced pilotlar korundu: IEEE-PILOT-S1B, IEEE-PILOT-S1B-R1, IEEE-PILOT-S1C-R1, IEEE-PILOT-S1D-R1, IEEE-PILOT-S1E-R1 ve IEEE-PILOT-S1F-R1.
- Scopus pilotlari islendi: SCO-PILOT-S1A, SCO-PILOT-S1B ve SCO-PILOT-S1F candidate olarak kaydedildi.
- Scopus count mismatch durumlari QA warning olarak kaydedildi: SCO-PILOT-S1B reported/export 35 vs 60; SCO-PILOT-S1F reported/export 103 vs 104.
- ScienceDirect supplementary pilot CSV paketi islendi; SD-PILOT-P1, P2A, P2B, P2C, P2D, P2E, P3 ve P4 pilot satirlari `search_log.csv` dosyasina eklendi.
- ScienceDirect audit diagnostics kaydedildi: 350 all rows ve 172 unique records. Bu sayilar final PRISMA count degildir.
- Raw export ve audit dosyalari tarihli klasor yapisina yerlestirildi.
- QA raporu guncellendi ve pilot/final ayrimi tekrar kontrol edildi.

## Olusturulan / Guncellenen Ana Dosyalar

- `PROJECT_CONTEXT_OISAC_PRISMA.md`
- `AGENTS.md`
- `README.md`
- `systematic_review_workflow/02_arama/01_arama_plani.md`
- `systematic_review_workflow/02_arama/search_log.csv`
- `systematic_review_workflow/02_arama/ieee_pilot_summary_2026-06-18.md`
- `systematic_review_workflow/02_arama/scopus_pilot_summary_2026-06-19.md`
- `systematic_review_workflow/02_arama/combined_ieee_scopus_pilot_summary_2026-06-19.md`
- `systematic_review_workflow/02_arama/sciencedirect_pilot_summary_2026-06-19.md`
- `systematic_review_workflow/02_arama/pilot_search_QA_report_2026-06-19.md`
- `systematic_review_workflow/09_kayitlar/decision_log.md`
- `systematic_review_workflow/09_kayitlar/progress_tracker.md`
- `systematic_review_workflow/09_kayitlar/codex_memory_bank.md`

## Handoff Paketleri

- `handoff_to_chatgpt/OISAC_PRISMA_STEP2A_IEEE_PILOT_HANDOFF.zip`
- `handoff_to_chatgpt/OISAC_PRISMA_STEP2B_IEEE_SCOPUS_PILOT_HANDOFF.zip`
- `handoff_to_chatgpt/OISAC_PRISMA_STEP2B_CLEANUP_HANDOFF.zip`
- `handoff_to_chatgpt/OISAC_PRISMA_STEP2C_SCIENCEDIRECT_PILOT_HANDOFF.zip`

Son aktif aktarim paketi: `handoff_to_chatgpt/OISAC_PRISMA_STEP2C_SCIENCEDIRECT_PILOT_HANDOFF.zip`.

## Acik TODO / Riskler

- Scopus exact query strings henuz kesin degil: SCO-PILOT-S1A, SCO-PILOT-S1B ve SCO-PILOT-S1F icin Scopus history veya kullanici teyidi gerekiyor.
- Scopus mismatch kontrolleri final search oncesi cozulecek: SCO-PILOT-S1B 35 vs 60; SCO-PILOT-S1F 103 vs 104.
- ScienceDirect exact UI query strings pending: SD-PILOT-P1, SD-PILOT-P3 ve SD-PILOT-P4.
- SD-PILOT-P3 ve SD-PILOT-P4 final supplementary rescue/sensitivity query olarak tutulacak mi, yoksa dusurulecek mi karar verilmedi.
- SpringerLink, Wiley Online Library ve Taylor & Francis Online supplementary pilots not started.
- Candidate pilot package uzerinden inspection/dedup stratejisi henuz final search count uretmeyecek sekilde planlanmali.

## QA Durumu

- PASS: CSV dosyalari okunabilir durumda.
- PASS: Pilot/final ayrimi raporlarda acik.
- PASS: PRISMA flow count dosyasina pilot sayilari yazilmadi; degerler TBD kaldi.
- PASS: Legacy included studies CSV formal seed/validation set olarak kullanilmiyor.
- WARNING: Scopus count mismatch durumlari final search oncesi dogrulanmali.
- WARNING: Bazi Scopus ve ScienceDirect exact query stringleri placeholder ile duruyor; query string uydurulmadi.

