# 02 — PRISMA Teslim Kontrolü

Son doğrulama: 2026-08-04  
Durum: workflow verisi ve sentez tamam; manuscript integration ve final editorial QA açık.

## Tamamlanan PRISMA bileşenleri

| PRISMA 2020 alanı | Durum | Kanıt |
|---|---|---|
| Item 3 rationale | complete | Cross-modality, metric comparability ve benchmark gap gerekçesi |
| Item 4 objectives | complete | PCC + RQ1–RQ7 |
| Item 5 eligibility | complete/locked | FTI/FTX/CTX/RPT kuralları ve actual cutoff |
| Item 6 information sources | complete | Altı kaynak/platform; executed 2026-06-22 |
| Item 7 search strategies | complete in search log | Exact source-specific queries/exports retained |
| Item 8 selection process | complete with amendment | Actual AI-assisted/user-delegated provenance disclosed |
| Item 9 data collection | complete | Study/report/claim-level extraction, 206 studies |
| Item 10 data items | complete | Evidence, metrics, trade-offs, conditions, provenance, governance |
| Item 11 risk/appraisal | complete | Deterministic nine-dimension TQAF; 206/206 |
| Item 13 synthesis | complete | S1–S7 narrative/metric-governed synthesis; no meta-analysis |
| Item 16a flow | complete | 1.733 → 1.259 → 330 → 272 → 227 reports → 206 studies |
| Item 16b exclusions | complete | 39 full-text exclusions with single primary reason |
| Item 20 synthesis results | complete in Phase F | 8.203 primary claims; S1–S7 tables |
| Item 22 certainty | complete | 115 evidence bodies; 54 high, 47 moderate, 10 limited, 4 unclear |
| Item 24c amendments | complete | Search cutoff and actual reviewer-process amendment documented |
| Item 24a registration | complete statement | No external registration; internal protocol/versioning disclosed |

## Sayısal uzlaşma kontrolü

- [x] `1.733 - 472 - 2 = 1.259` screened.
- [x] `1.259 - 927 = 332` historical retrieval source records.
- [x] `332 - 2 aliases = 330` unique reports sought.
- [x] `330 - 58 = 272` full texts assessed.
- [x] `272 - 39 - 6 = 227` included reports.
- [x] `227 reports → 206 studies` after related-report mapping.
- [x] Contextual corpus = 61 title/abstract + 6 full-text = 67.
- [x] `3.041 + 4.861 + 404 = 8.306` governed claims.
- [x] Primary synthesis = `3.020 + 4.779 + 404 = 8.203`.
- [x] Inclusive non-quarantined = `8.203 + 31 context-only = 8.234`.
- [x] `8.234 + 72 quarantine = 8.306`.
- [x] Study status = 175 survey-ready + 31 restricted = 206.

## Bilimsel ve provenance kontrolü

- [x] Record/report/study birimleri ayrı yazıldı.
- [x] Contextual corpus primary technical evidence sayılmadı.
- [x] Quantitative eligibility, automatic comparability olarak sunulmadı.
- [x] Quarantined values averaging/imputation yapılmadan dışarıda tutuldu.
- [x] 31 context-only metric primary S3 sayımlarından çıkarıldı.
- [x] Exclusive S1/S5/S7 dağılımları 206'ya uzlaşıyor.
- [x] Multi-label S2/S6 toplamlarının 206'yı aşabileceği açıklandı.
- [x] Fallback `other` yalnız hiçbir tanınmış kategori yoksa atanıyor.
- [x] TQAF exclusion kuralı olarak kullanılmadı.
- [x] `independent_human_status = not_documented` açıkça kaydedildi.
- [x] Dual-independent review veya inter-rater reliability uydurulmadı.
- [x] Actual cutoff 2026-06-22; eski planned 2026-06-30 tarihi kullanılmadı.

## Yayın öncesi açık görevler

- [ ] Dated full-corpus TeX patch'i aktif manuscript'e scoped diff ile entegre et.
- [ ] Section IV–VIII'deki bütün 220/221-tabanlı tabloları/şekilleri Phase-F çıktılarından yeniden üret.
- [ ] 206-study included-studies appendix'i report-lineage alanıyla üret.
- [ ] Locked Phase-C PRISMA figure'ı manuscript'e yerleştir.
- [x] Abstract ve Discussion/Roadmap/Conclusion için 206-study İngilizce taslakları oluştur.
- [ ] Bu taslakları aktif manuscript'e entegre edip final editorial freeze uygula.
- [ ] Data availability, funding, competing interests ve author-contribution ifadelerini yazarla tamamla.
- [ ] Bibliography/citation-key ve cross-reference QA çalıştır.
- [ ] IEEEtran compile, float/layout ve final PDF visual QA çalıştır.
- [ ] Son bağımsız insan kontrolünü gerçek kapsamıyla belgele; yapılmadıysa yapılmış gibi yazma.

## Yasaklar

- Global `220/221 → 206` sayı değiştirme yapılmaz.
- `O_ISAC_*` citation key'leri sayısal replace ile değiştirilmez.
- 8.234 kapsayıcı evren, 8.203 primary evidence gibi sunulmaz.
- Claim-level quarantine, study exclusion veya “78 çalışma insan bekliyor” şeklinde yorumlanmaz.
- Historical `human_locked` dosya adları independent human verification kanıtı sayılmaz.
