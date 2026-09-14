# Phase E — Teknik Kalite ve Kanıt Kesinliği Değerlendirmesi

## 1. Amaç ve kapsam

Bu dizindeki `risk_of_bias.csv`, dosya adı iş akışı uyumluluğu için korunmakla birlikte klinik bir risk-of-bias aracı değildir. O-ISAC literatüründeki mimari, metrik, doğrulama ve karşılaştırılabilirlik farklılıklarını değerlendiren **deterministik bir Technical Quality Assessment Framework (TQAF)** çıktısıdır.

Değerlendirme 206 dahil çalışma kümesinin tamamına uygulanmıştır. Düşük bir TQAF skoru tek başına çalışma dışlama nedeni değildir; skorlar anlatısal sentezde kanıt gücünü sınırlamak, nicel karşılaştırma sınırlarını görünür kılmak ve benchmark hazırlığını değerlendirmek için kullanılır.

Gerçek literatür araması için son tarih **2026-06-22**'dir. Önceki taslaklarda yer alan 2026-06-30 plan tarihi güncel sonuçların kaynağı değildir.

## 2. Kilitli girdiler ve yöntem sürümü

- Kaynak çalışma kitabı: `04_veri_cekme/outputs/phase_d_survey_ready_2026-08-04/OISAC_PHASE_D_SURVEY_READY_2026-08-04.xlsx`
- Kaynak SHA-256: `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`
- Normalizasyon crosswalk SHA-256: `41d6f8f574bdd0d6eba04806b2930ade8fa1d3d56e28b083de3d56bb13e7d122`
- Yöntem sürümü: `phase_e_tqaf_deterministic_v1.0_2026-08-04`
- Son bloklayıcı QA: **PASS (43/43 kontrol)**

Crosswalk dosyası, önceki tam-korpus çıkarım çalışma kitabına ait kaynak kimliğini kendi içinde korur. Bu veri soy zinciri, `PHASE_E_FINAL_WORKBOOK_INVARIANCE_AUDIT_2026-08-04.{json,md}` ile açıkça nihai survey-ready kaynağa bağlanmıştır. Her iki çalışma kitabı `@oai/artifact-tool` ile içe aktarılmış; 206 çalışmada 46 kontrol ailesi ve toplam 9.476 çalışma-bazlı karşılaştırma yürütülmüştür. Predecessor→final ham/fingerprint girdilerinde, nihai kaynaktan yeniden hesaplanan crosswalk alanlarında ve Phase E'nin tükettiği survey-use/cap değerlerinde **0 fark** bulunmuştur. Böylece önceki SHA crosswalk lineage metadata'sı olarak korunurken, Phase E/F ve appendix için otoritatif girdi SHA'sı `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348` olarak kalır.

## 3. Skorlama yapısı

Sekiz bileşen boyut ve bunlardan türetilen bir toplam katkı skoru vardır. Tüm nihai skorlar tam sayı `0–3` ölçeğindedir:

| Skor | Yorum |
|---:|---|
| 0 | Yetersiz bilgi / raporlanmamış |
| 1 | Zayıf veya eksik |
| 2 | Yeterli |
| 3 | Güçlü; ilgili boyut için en yüksek kanıt düzeyi |

| Boyut | Değerlendirilen ana unsur |
|---|---|
| `technical_relevance` | O-ISAC kapsamı, iki işlevin varlığı, gerçek paylaşımlı entegrasyon ve 6G ilgisi |
| `metric_clarity` | İletişim ve algılama metriklerinin tanımı, birimi, ölçüm düzlemi, bağlamı ve çatışma durumu |
| `reporting_completeness` | Mimari, kaynak, dalga biçimi/front-end, senaryo, donanım, DSP, doğrulama ve kaynak konumu |
| `validation_maturity` | Analitik/simülasyon/deney/prototip/saha olgunluğu; skor 3 için her iki işlevde saha/deployment kanıtı |
| `reproducibility` | Parametreler, setup, protokol, veri ve kod/model erişilebilirliği |
| `benchmark_readiness` | Baseline, açık artefakt, karşılaştırma kabul edilebilirliği ve doğrulama/tekrarlanabilirlik |
| `comparison_admissibility` | Her iki işlevde doğrudan, koşullu veya yalnızca betimsel karşılaştırma uygunluğu |
| `limitation_transparency` | Yazar kaynaklı sınırlamalar, boşluklar, varsayımlar, doğrulama sınırları ve trade-off açıklığı |
| `overall_evidence_contribution` | Sekiz bileşenin aritmetik ortalaması ve aşağıdaki güvenlik üst sınırları sonrası toplam katkı |

Bileşik göstergelerde sabit eşikler kullanılmıştır: `<0.25 → 0`, `0.25–<0.50 → 1`, `0.50–<0.80 → 2`, `≥0.80 → 3`. Toplam katkının ham ortalama eşikleri `<0.75 → 0`, `<1.50 → 1`, `<2.25 → 2`, aksi halde `3` olup güvenlik üst sınırları daha sonra uygulanmıştır. Her çalışma satırındaki `notes` alanı girdi değerlerini, kayıt konumlarını, uygulanan cap'leri ve yöntem sürümünü makinece okunabilir JSON olarak saklar.

## 4. Survey-use güvenlik üst sınırları

Cap'ler çalışma dışlamaz; hangi iddianın hangi sentezde kullanılabileceğini sınırlar. Bir çalışmaya birden çok cap uygulanabilir.

- Herhangi bir karantinaya alınmış iddia bulunan 31 çalışmada toplam katkı skoru en fazla `2` olabilir.
- Karantinaya alınmış metrik/trade-off iddiası bulunan 26 çalışmada karşılaştırma kabul edilebilirliği en fazla `1`, ilgili nicel kalite boyutları en fazla `2` olabilir.
- Maddi kaynak çatışması bulunan 31 çalışmada limitation transparency en fazla `2` olabilir.
- Yazar tarafından raporlanmış sınırlama bulunmayan 9 çalışmada limitation transparency en fazla `1` olabilir.
- Hem metric clarity hem validation maturity `≤1` olan 6 çalışmada toplam katkı en fazla `1` olabilir.
- Toplam katkı `3` olabilmek için technical relevance, metric clarity, reporting completeness ve validation maturity boyutlarının her biri en az `2` olmalıdır.
- Reproducibility `3` için complete/substantial parametre raporlaması ile açık veri veya kod/model; benchmark readiness `3` için external/common baseline, açık artefakt ve doğrudan admissibility birlikte gereklidir.

Phase D'deki 72 karantina kaydı 31 çalışmaya aittir: 21 evidence ve 51 metric kaydı. Bunlar audit izinde korunur ancak kanıt gövdesi iddia toplamlarına katılmaz. Karantina çalışma düzeyinde genel dışlama değildir; etkilenmeyen mimari, yöntem, taksonomi ve uygun kapsamlı bulgular kullanılabilir.

## 5. Çalışma düzeyi sonuçlar

Her boyutun dağılımı 206 çalışmaya tam olarak toplam verir:

| Boyut | Skor 0 | Skor 1 | Skor 2 | Skor 3 |
|---|---:|---:|---:|---:|
| Technical relevance | 0 | 15 | 68 | 123 |
| Metric clarity | 0 | 31 | 7 | 168 |
| Reporting completeness | 0 | 0 | 10 | 196 |
| Validation maturity | 0 | 32 | 168 | 6 |
| Reproducibility | 0 | 4 | 199 | 3 |
| Benchmark readiness | 0 | 48 | 158 | 0 |
| Comparison admissibility | 0 | 192 | 10 | 4 |
| Limitation transparency | 0 | 9 | 44 | 153 |
| Overall evidence contribution | 0 | 6 | 75 | 125 |

Karşılaştırma admissibility dağılımı, korpustaki çok sayıda sonucun tanım/koşul bakımından betimsel kullanılabildiğini fakat doğrudan çapraz-çalışma karşılaştırmasına uygun olmadığını gösterir. Benchmark readiness için skor 3 bulunmaması da ortak baseline ve açık artefakt eksikliğinin sentez düzeyindeki önemli bir sonuç olduğuna işaret eder.

## 6. Kanıt gövdesi kesinliği ve fallback uzlaştırması

`certainty_grade.csv`, S1–S7 survey bölümleri için 115 benzersiz kanıt gövdesi içerir:

| Bölüm | Kanıt gövdesi |
|---|---:|
| S1 | 6 |
| S2 | 8 |
| S3 | 47 |
| S4 | 10 |
| S5 | 3 |
| S6 | 31 |
| S7 | 10 |
| **Toplam** | **115** |

Kesinlik dağılımı `high=54`, `moderate=47`, `limited=10`, `unclear=4` şeklindedir. S3 ve S6'daki `other_*` gövdeleri genel bir atık kategorisi değildir; yalnızca çalışma–alan/eksen düzeyinde tanınmış bir kategori yoksa kullanılan fallback'tir. Nihai fallback üyelikleri S3 communication `2`, S3 sensing `2`, S6 technology `19` ve S6 application `15` çalışmadır.

Özellikle S3 communication uzlaştırmasında eski token-agnostic kuralın ürettiği 8 aday incelenmiştir. Uygun communication metric token'ı bulunmayan 6 çalışma fallback'ten çıkarılmış, yalnızca uygun fakat tanınmamış token taşıyan 2 çalışma dahil edilmiştir. Tanınmış fakat karantinaya alınmış metric token'ları üyelik oluşturmaz. Bu kararların 7.951 satırlık kayıt izi `phase_e_tqaf_body_normalization_audit_2026-08-04.csv` içindedir. Dört mixed/unclassified fallback gövdesi survey sonucu üretmek için substantive kabul edilmez ve `unclear` olarak tutulur.

## 7. Legacy boşlukların yönetimi

On iki çalışmadaki 92 metric satırında hem comparability hem admissibility alanı önceki çıkarımdan boş gelmiştir. Bu satırlar sessizce olumlu/olumsuz puanlanmamış, tamamı açıkça:

`insufficient_information_due_legacy_extraction`

etiketine eşlenmiştir. Satır düzeyi kayıt `phase_e_tqaf_resolved_legacy_metric_rows_2026-08-04.csv` içinde korunur.

## 8. Provenans sınırı

Bu Phase E değerlendirmesi, kilitli Phase D verileri üzerinde **AI-assisted, user-delegated ve deterministik** bir iş akışında üretilmiştir. Bu checkpoint bağımsız bir insanın tüm PDF'leri yeniden doğruladığını belgelemez. Doğru durum:

`independent_human_status = not_documented`

Bu nedenle dosya veya üst veri adlarında geçen `HUMAN_ADJUDICATED`, bağımsız çift-insan doğrulamasının kanıtı olarak kullanılamaz. Makalede yöntem açıklaması gerçek süreçle uyumlu olmalıdır.

## 9. Kanonik çıktılar

- `risk_of_bias.csv`: 206 study-level TQAF satırı.
- `certainty_grade.csv`: 115 evidence-body kesinlik satırı.
- `phase_e_tqaf_dimension_audit_2026-08-04.csv`: 1.854 boyut audit satırı.
- `phase_e_tqaf_body_normalization_audit_2026-08-04.csv`: 7.951 üyelik/normalizasyon audit satırı.
- `phase_e_tqaf_resolved_legacy_metric_rows_2026-08-04.csv`: 92 açık legacy çözüm satırı.
- `synthesis_matrix_PHASE_E_2026-08-04.csv`: S1–S7 teknik kalite sentez girdisi.
- `phase_e_tqaf_QA_2026-08-04.json`: 43/43 bloklayıcı kontrol sonucu.
- `phase_e_tqaf_summary_2026-08-04.md`: makine çıktısı kısa özet.
- `phase_e_tqaf_normalization_crosswalk_2026-08-04.{json,md}`: normalizasyon sözleşmesi ve 206 çalışma eşlemesi.
- `PHASE_E_FINAL_WORKBOOK_INVARIANCE_AUDIT_2026-08-04.{json,md}`: eski crosswalk kaynağı ile nihai Phase D kitabı arasında 206 çalışma ve 9.476 karşılaştırmalık release köprüsü.

Kalıcı yeniden üretim paketi `09_kayitlar/checkpoints/quality_assessment_PHASE_E_FINAL_2026-08-04/` altında tutulur.
