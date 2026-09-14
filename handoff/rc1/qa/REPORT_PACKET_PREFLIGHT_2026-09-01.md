# Full Revision Report Packet Preflight

Tarih: 2026-09-01  
Sonuç: `PREFLIGHT_OK`  
Kapsam: Evidence manifest ve source-PDF pointer bütünlüğü

Bu sonuç bir G3 veya başka bir karar kapısı `PASS` beyanı değildir. Bilimsel
uygunluk, reviewer doğrulaması, adjudication veya manuscript kullanım kararı
üretilmemiştir.

## Girdiler

- Verification register:
  `C:\OISAC\worktrees\comst-full-20260901\governance\plan_snapshot\01_verification\full_118_verification_register.csv`
  - SHA-256:
    `77A91B8A34F5CA964D519F4E2759C8554759276D8BB683F4BDD14B5959A49B0B`
- Exact-set otoritesi:
  `C:\OISAC\worktrees\comst-full-20260901\evidence\inputs\ST-19_PRIMARY_METRIC_RESULTS_4779.csv`
  - SHA-256:
    `DAC20625EF18C97BAC289F6AA05C2E2A75172E14CC76745780DDEDF9B689C539`
- Source-PDF kökü:
  `C:\OISAC\reviewmdS\01_fulltext\include`
- PDF page-count kontrolü: `pypdf` ile read-only açılış.
- PDF digest kontrolü: SHA-256.

## Preflight kontrolleri

| Kontrol | Beklenen | Gözlenen | Eksik | Duplikasyon / fazlalık | Sonuç |
|---|---:|---:|---:|---:|---|
| Register metric satırı | 118 | 118 | 0 | 0 metric-ID duplikasyonu | ok |
| ST-19 `yes_with_conditions` exact-ID seti | 118 | 118 | 0 | 0 extra | ok |
| Source report | 16 | 16 | 0 | 0 report-ID duplikasyonu | ok |
| Study cluster | 15 | 15 | 0 | 0 | ok |
| Manifest `metric_row_count` toplamı | 118 | 118 | 0 | 0 | ok |
| Report-ID başına kanonik PDF eşleşmesi | 1 | 16/16 tekil eşleşme | 0 | 0 çoklu eşleşme | ok |
| PDF read-only açılışı ve pozitif sayfa sayısı | 16 | 16 | 0 | 0 hata | ok |
| PDF pozitif byte boyutu | 16 | 16 | 0 | 0 hata | ok |
| PDF SHA-256 tekilliği | 16 | 16 | 0 | 0 duplicate-hash grubu | ok |
| Manifest / SHA-256 sidecar kapsamı | 16 | 16 | 0 | 0 | ok |

Register ve ST-19 exact set karşılaştırmasında `missing=0`, `extra=0` bulundu.
Register içindeki her metric satırı tam olarak bir report ve bir study cluster'a
bağlanmaktadır. Manifestte 14 study cluster bir Phase-G source report ile,
`STC-TUNABLE-LASER-THZ-FMCW-2025-2026` ise `SCR-00083` ve `SCR-00553` olmak
üzere iki companion source report ile temsil edilmektedir.

## Report-study ve satır hacmi

| Report | Study cluster | Metric row | PDF page | PDF bytes | Phase-G relation |
|---|---|---:|---:|---:|---|
| SCR-00007 | STC-SINGLETON-SCR-00007 | 1 | 15 | 6,043,294 | only report in source set |
| SCR-00008 | STC-SINGLETON-SCR-00008 | 21 | 8 | 1,611,665 | only report in source set |
| SCR-00036 | STC-SINGLETON-SCR-00036 | 7 | 9 | 2,152,732 | only report in source set |
| SCR-00038 | STC-SINGLETON-SCR-00038 | 11 | 3 | 1,233,944 | only report in source set |
| SCR-00052 | STC-SINGLETON-SCR-00052 | 3 | 2 | 1,458,472 | only report in source set |
| SCR-00056 | STC-SINGLETON-SCR-00056 | 5 | 8 | 4,915,205 | only report in source set |
| SCR-00057 | STC-SINGLETON-SCR-00057 | 4 | 4 | 701,706 | only report in source set |
| SCR-00072 | STC-ENDOGENOUS-TS-FRFT-DAS-2025 | 6 | 14 | 5,474,548 | only report in source set |
| SCR-00083 | STC-TUNABLE-LASER-THZ-FMCW-2025-2026 | 7 | 16 | 7,107,143 | companion with SCR-00553 |
| SCR-00086 | STC-SINGLETON-SCR-00086 | 7 | 3 | 1,673,043 | only report in source set |
| SCR-00196 | STC-SINGLETON-SCR-00196 | 26 | 11 | 1,987,934 | only report in source set |
| SCR-00220 | STC-FRDM-POLARIZATION-SENSING-2025-2026 | 5 | 10 | 5,411,740 | only report in source set |
| SCR-00233 | STC-SINGLETON-SCR-00233 | 2 | 9 | 2,923,103 | only report in source set |
| SCR-00238 | STC-SINGLETON-SCR-00238 | 3 | 10 | 11,710,435 | only report in source set |
| SCR-00553 | STC-TUNABLE-LASER-THZ-FMCW-2025-2026 | 1 | 2 | 296,030 | companion with SCR-00083 |
| SCR-00941 | STC-SINGLETON-SCR-00941 | 9 | 16 | 9,011,645 | only report in source set |

## Sınır ve koruma

- PDF'ler worktree'ye kopyalanmadı; manifest yalnız absolute local pointer tutar.
- Reviewer alanı, reviewer kararı veya adjudication kaydı oluşturulmadı.
- Bilimsel karşılaştırılabilirlik ya da ana metin seçimi kararı oluşturulmadı.
- G0--G10 kapılarından hiçbiri bu preflight ile değiştirilmedi veya `PASS`
  sayılmadı.
- `preflight_result=ok` yalnız path, bytes, page count, SHA-256 ve set
  bütünlüğünü ifade eder.
