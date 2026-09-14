# 01 — Sentez ve Analiz Planı

Son doğrulama: 2026-08-04  
Durum: Phase F S1–S7 sentezi tamamlandı; sonuçlar yazım paketine aktarılmaya hazırdır.

## 1. Amaç ve sentez yaklaşımı

Bu çalışma, 6G bağlamındaki Optical Integrated Sensing and Communication (O-ISAC) literatürünü fiber, FSO, VLC/LiFi, photonic-THz, hybrid ve diğer optik platformlar arasında karşılaştırmalı olarak haritalayan PRISMA 2020-temelli bir narrative systematic review ve scoping-style PCC sentezidir.

Literatür; sistem mimarisi, sensing görevi, communication görevi, metrik tanımı, ölçüm düzlemi, senaryo ve doğrulama yöntemi bakımından heterojendir. Bu nedenle ortak bir etki büyüklüğü üzerinden meta-analiz yapılmamıştır. Uygulanan yöntem:

- structured narrative synthesis;
- scoping-style taxonomy mapping;
- modality-specific evidence mapping;
- metric-governed comparison;
- communication–sensing trade-off synthesis;
- validation maturity ve benchmark-readiness mapping;
- 6G research-gap/roadmap synthesisidir.

## 2. Kanonik sentez evreni

| Birim | Sayı | Kullanım |
|---|---:|---|
| Dahil edilen rapor | 227 | Rapor ve sürüm lineage katmanı |
| Dahil edilen çalışma | 206 | Çalışma düzeyi ana payda |
| Evidence claim | 3.041 | 3.020 birincil; 21 karantina |
| Metric claim | 4.861 | 4.779 birincil; 31 context-only; 51 karantina |
| Trade-off claim | 404 | 404 birincil |
| Toplam claim | 8.306 | Tam governance evreni |
| Birincil sentez claim'i | 8.203 | 3.020 + 4.779 + 404 |
| Kapsayıcı non-quarantined evren | 8.234 | 8.203 birincil + 31 context-only |
| Karantina | 72 | Birincil sonuçlardan dışlanır |

`8.234` sayısı birincil kanıt sayısı değildir; 31 context-only metric claim'i içerir. Birincil sentez için yalnız `8.203` kullanılır. Çalışma düzeyi ve claim düzeyi paydalar birbirinin yerine kullanılmaz.

Kanonik Phase-D çalışma kitabı SHA-256: `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`.

## 3. Claim-governance kuralları

- `eligible_qualitative`, `eligible_quantitative`, `context_only` ve `quarantined_conflict` ayrı kullanım sınıflarıdır.
- Quantitative-use etiketi, otomatik cross-study comparability veya pooling yetkisi vermez.
- Metrik tanımı, rolü, ölçüm düzlemi, senaryo ve validation context birlikte uyumlu olmalıdır.
- OSNR, SNR ve ESNR açık bir dönüşüm modeli olmadan birleştirilmez.
- Physical resolution, accuracy/RMSE, CRB-bound ve fiber spatial granularity aynı outcome sayılmaz.
- Analytical, simulation, laboratory, prototype ve field sonuçları aynı validation plane'e indirilmez.
- Çelişkili değerler ortalanmaz veya makul görünen bir değerle değiştirilmez; claim düzeyinde karantinaya alınır.
- Context-only claim'ler primary prevalence veya performance conclusion üretmez.

## 4. S1–S7 analiz birimleri

| Kod | Sentez alanı | Birim | Ana kural |
|---|---|---|---|
| S1 | Optical modality taxonomy | 206 benzersiz çalışma | Phase-E frozen crosswalk; mutually exclusive |
| S2 | Architecture/integration mechanisms | 206 çalışma, multi-label | Toplamlar 206'yı aşabilir; fallback yalnız tanınan kategori yoksa kullanılır |
| S3 | Metric reporting map | 4.779 primary metric claim | Context-only ve karantina dışarıda; claim ve unique-study sayıları ayrı |
| S4 | Communication–sensing trade-offs | 404 trade-off claim | 168 çalışma; aynı çalışma birden çok family'ye katkı verebilir |
| S5 | Validation/reproducibility/benchmark readiness | 206 çalışma | Phase-E frozen crosswalk + TQAF |
| S6 | Enabling technologies/applications | 206 çalışma, multi-label | Nonexclusive toplamlar; unmatched token audit'te korunur |
| S7 | Gaps and 6G relevance | 206 çalışma | 6G sınıfı mutually exclusive; gap sonuçları TQAF ile üçgenlenir |

## 5. Exclusive crosswalk sonuçları

### S1 — Optical modality

| Sınıf | Çalışma | % |
|---|---:|---:|
| photonic_THz | 69 | 33,5 |
| fiber | 56 | 27,2 |
| VLC_LiFi | 38 | 18,4 |
| FSO | 31 | 15,0 |
| hybrid_optical | 9 | 4,4 |
| other_optical | 3 | 1,5 |

### S5 — Validation maturity

| Seviye | Çalışma | % |
|---|---:|---:|
| 2 — simulation/numerical | 32 | 15,5 |
| 3 — enhanced simulation/dataset | 18 | 8,7 |
| 4 — laboratory experiment/proof of concept | 78 | 37,9 |
| 5 — controlled prototype | 66 | 32,0 |
| 6 — field trial/deployment | 12 | 5,8 |

Open data: 13 open, 41 on request, 145 unavailable/NR, 7 NA.  
Open code/model: 1 partial, 7 on request, 197 unavailable/NR, 1 NA.

### S7 — 6G relevance

| Sınıf | Çalışma | % |
|---|---:|---:|
| direct | 138 | 67,0 |
| inferred | 64 | 31,1 |
| weak | 1 | 0,5 |
| not_applicable | 3 | 1,5 |

Her exclusive dağılım 206'ya tam uzlaşır.

## 6. TQAF kullanım kuralı

Phase E, 206 çalışma için dokuz study-level boyutu 0–3 ölçeğinde deterministik olarak puanlar: technical relevance, metric clarity, reporting completeness, validation maturity, reproducibility, benchmark readiness, comparison admissibility, limitation transparency ve overall evidence contribution.

Overall contribution dağılımı: 6 düşük, 75 yeterli, 125 güçlü. Quarantined claim içeren 31 çalışma overall ≤2 ile sınırlandırılmıştır. Quarantined metric claim içeren 26 çalışma comparison admissibility ≤1 ile sınırlandırılmıştır. TQAF bir exclusion aracı değildir; iddia gücünü ve yazım dilini kalibre eder.

115 S1–S7 evidence body için certainty özeti: 54 high, 47 moderate, 10 limited ve 4 unclear. `mixed/unclassified` fallback gövdeleri substantive conclusion üretmez ve `unclear` tutulur.

## 7. Yazım ilkeleri

- S1/S5/S7 yüzdelerinde payda 206'dır.
- Multi-label S2/S6 toplamları prevalence toplamı olarak yorumlanmaz; kategori bazında `n/206` raporlanır.
- S3 ve S4'te claim sayısı ile unique-study sayısı birlikte verilir.
- Bir sonuç yalnız koşulluysa koşul cümlede görünür olmalıdır.
- TQAF certainty, study quality ve claim admissibility birbirinin yerine kullanılmaz.
- Dört geniş fallback evidence body yalnız audit/coverage amaçlıdır; survey sonucu gibi sunulmaz.
- Mevcut 220/221 tabanlı şekil ve tablolar sayısal find-and-replace ile düzeltilmez; 206-study kaynaktan yeniden üretilir.

## 8. Provenance sınırı

Uygulanan süreç `investigator-supervised, AI-assisted, user-delegated and claim-governed` olarak raporlanır. `independent_human_status = not_documented`. Bağımsız çift insan taraması, bağımsız full-corpus PDF doğrulaması veya inter-rater reliability iddiası yapılmaz.

