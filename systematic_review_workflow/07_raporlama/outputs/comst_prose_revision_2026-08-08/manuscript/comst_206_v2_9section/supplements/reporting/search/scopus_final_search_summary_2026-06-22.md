# Scopus Final Search Summary - 2026-06-22

## Kaynak ve kapsam

- Source: Scopus
- Source role: core source
- Execution date: 2026-06-22
- Actual cutoff: 2026-06-22

Bu dosya Step 3-A Scopus final raw export logging kaydıdır. Deduplication, screening veya included studies listesi oluşturulmamıştır.

## Export dosyaları ve satır sayıları

| Query ID | Canonical export file | Exported row count |
|---|---|---:|
| SCO-FINAL-S1A | `final_exports/scopus/2026-06-22/SCO-FINAL-S1A_export_2026-06-22.csv` | 41 |
| SCO-FINAL-S1B | `final_exports/scopus/2026-06-22/SCO-FINAL-S1B_export_2026-06-22.csv` | 1128 |
| SCO-FINAL-S1F | `final_exports/scopus/2026-06-22/SCO-FINAL-S1F_export_2026-06-22.csv` | 104 |

- Total raw Scopus rows: 1273
- Audit unique diagnostic: 1122
- Duplicate groups diagnostic: 141

Bu değerler PRISMA flow count değildir. `1122` unique değeri formal PRISMA deduplication sonucu değil, yalnızca Scopus içi DOI/title audit dedup diagnostic değeridir.

## Uyarılar

- SCO-FINAL-S1B broad/high-recall uyarısı: 1128 satırlık geniş çekirdek sorgudur; daha sonraki title/abstract screening aşamasında gürültü beklenir.
- Publication date missing warning: CSV exportlarında tam publication date alanı yoktur; 2026 kayıtları 2026-06-22 cutoff tarihine göre daha sonra ayrıca kontrol edilmelidir.
- Document type filter mismatch warning: Exportlarda Article/Conference Paper/Review dışı bazı document type değerleri vardır; eligibility aşamasında filtre/protokol uyumu doğrulanmalıdır.
- Language field missing warning: CSV exportlarında language alanı yoktur; English filtresinin Scopus interface/search log üzerinden doğrulanması gerekir.
- Article in press warning: Article in press kayıtları publication stage/date açısından daha sonra incelenmelidir.

## Kapsam dışı

- Deduplication yapılmadı.
- Screening yapılmadı.
- Included studies listesi oluşturulmadı.
- PRISMA flow count dosyasına sayı yazılmadı; sayılar TBD kalmalıdır.
- Audit CSV dosyaları formal screening kararı değildir.
