# G0 Input Freeze QA — 2026-09-01

Final status: `PASS`

Scope: `G0_GOVERNANCE_AND_BASELINE_ONLY`

Next gate: `G1_BLOCKED_PENDING_EXPLICIT_ALL_AUTHOR_AMENDMENT_LOCK`

## Karar özeti

Frozen source paketi ve canonical manuscript artefact'ları gerçek dosya
hash'leriyle yeniden doğrulandı. Frozen paket bağımsız tam-revizyon ağacında
derlendi; yeniden üretilen PDF 27 sayfadır, metinsel layout içeriği canonical
PDF ile aynıdır ve 27/27 sayfa render incelemesi temizdir. Binary PDF hash'inin
canonical PDF'den farklı olması, deterministic olmayan PDF metadata/build
katmanına bağlı bir yeniden derleme farkıdır; logical text hash, sayfa sayısı,
log ve render kapıları eşleştiği için G0'ı bozmaz.

Bu PASS yalnız G0 içindir. Amendment-001 `PROPOSED_NOT_LOCKED` kaldığından
verification, analysis veya manuscript'e yeni sayısal iddia aktarımı
başlatılamaz.

## 1. İzolasyon ve baseline kimliği

| Kontrol | Sonuç | Kanıt |
|---|---|---|
| Ayrı fiziksel çalışma ağacı | PASS | `C:\OISAC\worktrees\comst-full-20260901` |
| Baseline Git kimliği | PASS | Root commit `13e3727241cb1d7726abb3ddb1833505c73c157f`; parent yok |
| Baseline tag/branch | PASS | `comst-full-base-20260901`; `baseline/comst-core-20260825-27p` |
| Frozen source authority | PASS | ZIP hash aşağıdaki tabloda |
| Balanced carryover | PASS at G0 ancestry | Baseline root commit'tir; balanced branch merge/carryover bundan sonra da yasaktır |
| Canonical kaynaklara yazma | PASS | Yalnız pointer/hash kullanıldı; canonical dosyalar değiştirilmedi |

## 2. BASELINE_MANIFEST kontrolü

Plan snapshot'ındaki `00_governance/BASELINE_MANIFEST.tsv` içinde tanımlı 10
artefact'ın tamamı canonical path'te bulundu; bytes ve SHA-256 değerleri yeniden
hesaplanarak manifest ile eşleştirildi.

- Expected entries: `10`
- Present entries: `10`
- Byte matches: `10/10`
- SHA-256 matches: `10/10`
- Missing or mismatched entries: `0`
- Result: `PASS`

Gerçek hash satırları `governance/BASE_MANUSCRIPT_HASH_MANIFEST.sha256` içinde,
Phase A--F otoriteleri ise `governance/PHASE_A_F_HASH_MANIFEST.sha256` içinde
dondurulmuştur.

## 3. Source ve PDF kimlikleri

| Artefact | SHA-256 | Bytes | Pages | Sonuç |
|---|---|---:|---:|---|
| Frozen source ZIP | `FD69AD68C68B6408FF1B0CE5E584156F6B773FA78F199ADEDF0C9440B648AC88` | 470,379 | NA | PASS |
| Canonical manuscript PDF | `6A195C6856E5BD784DEF0A5149B1DF025771E5E50D7B2C02A7D229108B450DC2` | 598,488 | 27 | PASS |
| G0 rebuilt manuscript PDF | `4526521C1D260639EE7F046D11227C796D791FC2A766ADF184BE1264857998D2` | 598,152 | 27 | PASS |

Canonical PDF pointer:
`C:\OISAC\prisma2020Review\systematic_review_workflow\07_raporlama\outputs\comst_prose_revision_2026-08-08\manuscript\comst_206_v2_9section\main.pdf`

G0 rebuilt PDF:
`C:\OISAC\worktrees\comst-full-20260901\outputs\pdf\OISAC_COMST_FULL_REVISION_G0_BASELINE_2026-09-01.pdf`

## 4. Logical-content eşitliği

Her iki PDF için `pdftotext -layout` çıktısının SHA-256 değeri:

`921A79139A4271CE7210E86086EBBBC295DACED8C58B3D849705986A2FA1623A`

- Canonical/rebuilt logical-layout hash equal: `YES`
- Page count equal: `27 = 27`
- Binary PDF hash equal: `NO`, beklenen yeniden-derleme farkı
- Logical-content result: `PASS`

## 5. Build-log QA

Final build log taraması:

| Sınıf | Sayı | Gate |
|---|---:|---|
| Undefined citations | 0 | PASS |
| Undefined references | 0 | PASS |
| LaTeX warnings | 0 | PASS |
| Overfull boxes | 0 | PASS |
| Fatal errors | 0 | PASS |
| Underfull boxes | 11 | NONBLOCKING |

Underfull kayıtları içerik kaybı, clipping, overfull veya fatal üretmediğinden
G0 baseline için nonblocking olarak kaydedildi.

## 6. Render QA

- Rendered pages: `27/27`
- Missing pages: `0`
- Visible clipping: `0`
- Visible overlap: `0`
- Unreadable figure/table labels: `0`
- Visual result: `PASS`

## 7. Phase A--F freeze

Phase A--F için eligibility, mapping, PRISMA, extraction, TQAF ve S1--S7
otoritelerini temsil eden canonical dosyaların gerçek SHA-256 değerleri
`governance/PHASE_A_F_HASH_MANIFEST.sha256` içinde kaydedildi. Bu dosyalar
read-only authority'dir; tam revizyon yalnız ayrı Phase G overlay üretir.

Result: `PASS`

## 8. G0/G1 kararı

G0 ölçütleri karşılandı:

- [x] Frozen source ZIP hash kayıtlı ve doğrulandı.
- [x] Canonical 27-page PDF hash/bytes kayıtlı ve doğrulandı.
- [x] Ayrı ağaçtan temiz baseline build 27 sayfa üretildi.
- [x] Canonical/rebuilt logical-layout hash eşleşti.
- [x] Build log blocking hata içermiyor.
- [x] 27/27 sayfa görsel olarak temiz.
- [x] BASELINE_MANIFEST 10/10 eşleşti.
- [x] Phase A--F gerçek hash'leri kaydedildi.
- [x] Balanced merge/carryover yasağı charter ve amendment içine yazıldı.

G0: `PASS`

G1: `BLOCKED`

Blocker: Amendment-001 için bütün yazarların açık lock kararı, reviewer rolleri,
adjudicator, pilot ölçütleri ve numeric-claim gate henüz kaydedilmemiştir.

