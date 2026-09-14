# 76 COMST Makalesiyle Tam-Metin Almanakı ve 206-Çalışmalı O-ISAC Survey Denetimi

> **Kapsam:** 76 yayımlanmış IEEE *Communications Surveys & Tutorials* makalesi; 3.994 başlık-sınırlı anlatı birimi; 1.096 şekil ve 654 tablo. `COMST_031`, COMST değil *IEEE Wireless Communications* olduğu için dışarıdadır.

> **Yorum sınırı:** Bu almanak yayınlanmış pratikleri betimler. Kelime, başlık veya görsel sayılarını taklit etmenin kabulü sağladığını iddia etmez. O-ISAC içeriğinin bilimsel otoritesi 206-study evidence base'dir; eski 220/221 taslak değildir.

## 1. Yönetici Özeti

O-ISAC adayının bilimsel omurgası COMST'e uygundur: fiziksel rejim → coupling mimarisi → metric meaning → trade-off → validation → application/6G → discussion. Sorun omurganın kendisi değil, sunum katmanıdır.

- Taslak **14,843** anlatı kelimesiyle korpusun yaklaşık **%1.3** yüzdeliğindedir; yerel medyan **22,851** kelimedir.
- **13** üst seviye bölüm korpusun yaklaşık **%98.7** yüzdeliğindedir; medyan **8**'dir. İncelik değil, sık reader reset riski vardır.
- Ortalama cümle **17.7** kelime; COMST medyanı **25.0**, güçlü-anlatı alt kümesi **25.1**'dir. Taslak her cümleyi uzatmak yerine yalnız gerçek neden/koşul ilişkilerini birleştirmelidir.
- Taslakta prose içinde görünür olan primary-study atıfları **76/206 (%36.9)** düzeyindedir. Çözüm citation stuffing değil; tematik evidence tabloları ve tüm 206'yı izlenebilir kılan supplementtir.
- Şu anda şekil/tablo yoktur. Kayıtlı plan **6 işlevsel şekil + 8 işlevsel tablo** önerir; bunlar dekorasyon değil, tekrar azaltma ve kanıt görünürlüğü araçlarıdır.
- En belirgin dil sapmaları: yüksek kısa-cümle oranı, çok yoğun noktalı virgül, aşırı `therefore`, ve sınır/olumsuzluk dilinin tekrar etmesidir. List-heavy prose ise korpustan düşüktür; bu olumlu özellik korunmalıdır.

Bu nedenle öneri **metni 23 bin kelimeye doldurmak değildir**. Önce 11 merge/7 trim kararını uygulamak, sonra 14 görsel kanıt taşıyıcısını ve eksik study attribution'ı eklemek gerekir. Net kelime artışı yalnız yeni tutorial açıklama, karşılaştırma yorumu ve evidence linkage'tan gelmelidir.

## 2. Veri ve İstatistik Tasarımı

- Her makale Abstract'tan son substantive synthesis/conclusion'a kadar okundu. References, biographies, acknowledgments, salt acronym blocks ve extraction-only image adları prose birimi sayılmadı.
- Üç disjoint coding grubu 76/76 makaleyi kapsadı. Anahtar, sıra, kelime ve görsel toplamları uzlaştırıldı.
- Grup sözlükleri canonical değerlere çevrildi; ham değerler `*_raw` alanlarında tutuldu.
- Tek numeric engine 3.994 birimi tekrar ölçtü. 76 abstract→body boşluğu front matter, altı boşluk yalnız container heading idi; substantive internal gap ve overlap yoktur.
- Aynı satırdaki 1.290 inline heading-prose bloğu geri alındı. Denklem sayacı yalnız açık display container'larını sayar; parantez içindeki citation/equation-label benzeri sayıları denklem kabul etmez.
- Unit-level sürekli ölçülerde makale-kümeli bootstrap; paper prevalence'da Wilson %95 aralığı kullanıldı. Unit/visual kategori oranları raw descriptive proportions'dır; bağımsız birimler gibi dar CI üretilmedi.
- Güçlü-anlatı alt kümesi 16 makaleden oluşur ve close reading ölçütleriyle önceden gerekçelendirilmiştir. Sayısal profili O-ISAC'a yaklaştırmak için otomatik seçim yapılmadı.

## 3. Bütün-Makale İskeleti

### 3.1 Uzunluk, başlık ve kaynak görünürlüğü

| Ölçü | O-ISAC | COMST p10 | Q1 | Medyan | Q3 | p90 | O-ISAC yüzdeliği | Okuma |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `total_narrative_words` | 14843.000 | 17133.500 | 20081.500 | 22851.500 | 25426.500 | 32401.000 | 1.3% | Very lean for the local COMST corpus; add missing evidence carriers and interpretation, not filler. |
| `top_level_sections` | 13.000 | 6.000 | 7.000 | 8.000 | 9.000 | 10.500 | 98.7% | Heading density is high; the registered merge decisions should reduce reader resets. |
| `lower_level_headings` | 57.000 | 21.500 | 27.000 | 38.500 | 53.500 | 69.000 | 76.3% | Heading density is high; the registered merge decisions should reduce reader resets. |
| `reference_list_size` | 86.000 | 167.000 | 193.500 | 238.500 | 312.750 | 391.000 | 0.0% | Current prose exposes only cited keys; thematic tables/supplement must improve 206-study traceability without citation stuffing. |
| `citation_group_density_per_100_words` | 0.559 | 1.285 | 1.699 | 2.049 | 2.602 | 2.929 | 0.0% | Study-level evidence visibility is low; repair it through representative citations and evidence tables. |
| `mean_sentence_words` | 17.712 | 21.355 | 22.769 | 24.965 | 26.947 | 28.704 | 0.0% | Cadence is unusually clipped; merge only genuinely connected clauses and keep sentence-level conditions visible. |
| `mean_paragraph_words` | 78.121 | 83.009 | 95.422 | 110.881 | 127.372 | 146.959 | 6.6% | Descriptive position only; this metric is not an acceptance target. |
| `short_sentence_ratio_12` | 0.192 | 0.058 | 0.074 | 0.100 | 0.129 | 0.164 | 94.7% | Short-sentence share is high; inspect local staccato rather than lengthening every sentence. |
| `long_sentence_ratio_35` | 0.007 | 0.075 | 0.091 | 0.128 | 0.186 | 0.232 | 0.0% | Descriptive position only; this metric is not an acceptance target. |
| `transitions_per_100_words` | 0.714 | 0.653 | 0.778 | 0.940 | 1.087 | 1.203 | 15.8% | Descriptive position only; this metric is not an acceptance target. |
| `semicolons_per_100_words` | 0.499 | 0.015 | 0.033 | 0.053 | 0.090 | 0.130 | 100.0% | Semicolon use is unusually dense and should be reduced during the prose pass. |
| `nominalizations_per_100_words` | 7.842 | 4.317 | 4.971 | 5.694 | 6.441 | 7.491 | 92.1% | Descriptive position only; this metric is not an acceptance target. |
| `negative_boundaries_per_100_words` | 1.469 | 0.114 | 0.133 | 0.188 | 0.270 | 0.377 | 100.0% | Boundary/negation language is unusually frequent; retain scientific limits but vary positive bounded formulations. |
| `list_heavy_sentence_ratio` | 0.116 | 0.141 | 0.169 | 0.204 | 0.246 | 0.270 | 2.6% | Descriptive position only; this metric is not an acceptance target. |

### 3.2 COMST'te tekrarlanan anlatı mimarisi

76 makalede tek bir zorunlu outline yoktur. Bununla birlikte güçlü örnekler aynı reader-job zincirini farklı konu adlarıyla tekrarlar:

1. somut sistem veya mühendislik ihtiyacı;
2. okuyucunun anlaması gereken fiziksel/teknik mekanizma;
3. mevcut literatürün çözemediği belirli karşılaştırma veya tasarım sorunu;
4. bu sorunu taşıyan taxonomy/framework;
5. aynı eksenlerle yinelenen technical families;
6. her aile sonunda yerel synthesis veya lessons learned;
7. validation/implementation/application ile gerçeklik testi;
8. kanıta bağlı challenges/roadmap ve kısa conclusion.

O-ISAC bu zinciri büyük ölçüde kurmuştur. Düzeltme, her başlığın yeni bir **reader job** başlatmasını sağlamak ve aynı taxonomy'yi prose içinde yeniden saymamaktır.

### 3.3 Rol atlası

Aşağıdaki prevalence değerleri 76 makale paydasındadır. Roller close-reading yorumudur; reliability sonucu nedeniyle kesin journal kuralları olarak okunmamalıdır.

| Rol | Birim | Makale | Prevalans | Medyan konum | Medyan birim/makale | Medyan kelime/makale | Yaygın geçiş |
|---|---:|---:|---:|---:|---:|---:|---|
| `abstract` | 76 | 76 | 100.0% | 0.0% | 1.0 | 216.5 | START → abstract → introduction_motivation |
| `introduction_motivation` | 97 | 76 | 100.0% | 2.4% | 1.0 | 1055.5 | abstract → introduction_motivation → related_surveys_gap |
| `related_surveys_gap` | 53 | 48 | 63.2% | 5.8% | 1.0 | 751.5 | introduction_motivation → related_surveys_gap → scope_contributions_organization |
| `scope_contributions_organization` | 92 | 50 | 65.8% | 7.7% | 2.0 | 508.5 | related_surveys_gap → scope_contributions_organization → background_foundations |
| `background_foundations` | 162 | 58 | 76.3% | 17.1% | 2.0 | 774.0 | background_foundations → background_foundations → background_foundations |
| `methods_review_protocol` | 13 | 6 | 7.9% | 21.4% | 1.0 | 546.0 | methods_review_protocol → methods_review_protocol → methods_review_protocol |
| `system_model_architecture` | 89 | 36 | 47.4% | 31.6% | 2.0 | 969.5 | other_substantive → system_model_architecture → other_substantive |
| `taxonomy_framework` | 66 | 32 | 42.1% | 35.5% | 1.0 | 595.5 | taxonomy_framework → taxonomy_framework → taxonomy_framework |
| `integration_design` | 98 | 29 | 38.2% | 37.5% | 2.0 | 1280.0 | integration_design → integration_design → integration_design |
| `standardization_implementation` | 103 | 39 | 51.3% | 43.0% | 2.0 | 700.0 | other_substantive → standardization_implementation → other_substantive |
| `other_substantive` | 760 | 43 | 56.6% | 46.1% | 16.0 | 4622.0 | other_substantive → other_substantive → other_substantive |
| `technical_family_synthesis` | 921 | 70 | 92.1% | 49.1% | 10.0 | 6631.0 | technical_family_synthesis → technical_family_synthesis → technical_family_synthesis |
| `tradeoff_optimization` | 148 | 39 | 51.3% | 52.2% | 3.0 | 1580.0 | tradeoff_optimization → tradeoff_optimization → tradeoff_optimization |
| `metrics_performance_comparison` | 109 | 36 | 47.4% | 54.7% | 2.0 | 507.5 | metrics_performance_comparison → metrics_performance_comparison → metrics_performance_comparison |
| `validation_experiment_reproducibility` | 73 | 31 | 40.8% | 58.1% | 2.0 | 616.0 | validation_experiment_reproducibility → validation_experiment_reproducibility → validation_experiment_reproducibility |
| `technology_enabler` | 109 | 31 | 40.8% | 58.7% | 3.0 | 1357.0 | technology_enabler → technology_enabler → technology_enabler |
| `lessons_learned_discussion` | 220 | 61 | 80.3% | 60.9% | 3.0 | 939.0 | technical_family_synthesis → lessons_learned_discussion → technical_family_synthesis |
| `application_use_case` | 264 | 47 | 61.8% | 62.8% | 4.0 | 1448.0 | application_use_case → application_use_case → application_use_case |
| `challenges_open_issues` | 168 | 41 | 53.9% | 68.9% | 3.0 | 1124.0 | challenges_open_issues → challenges_open_issues → challenges_open_issues |
| `limitations` | 4 | 3 | 3.9% | 69.8% | 1.0 | 802.0 | future_directions_roadmap → limitations → future_directions_roadmap |
| `future_directions_roadmap` | 293 | 68 | 89.5% | 89.5% | 4.0 | 1343.5 | future_directions_roadmap → future_directions_roadmap → future_directions_roadmap |
| `conclusion` | 76 | 76 | 100.0% | 100.0% | 1.0 | 214.0 | future_directions_roadmap → conclusion → lessons_learned_discussion |

Önemli yapı bulguları:

- Introduction ve conclusion 76/76'da vardır; technical-family synthesis 70/76, future roadmap 68/76, lessons/discussion 61/76'dır.
- Related-survey gap 48/76 ve ayrı scope/contribution birimi 50/76 makalede kodlandı.
- Ayrı review-method role yalnız 6/76 makalede görüldü; ayrı limitations yalnız 3/76'da görüldü.
- `corpus_descriptive_results` bağımsız rolü hiç gözlenmedi. Bu yüzden O-ISAC Section 5 kısa, görsel destekli ve Section 10'dan ayrıştırılmış olmalıdır.

## 4. Dil, Cümle ve Geçiş Almanakı

### 4.1 Cümle ve paragraf reçetesi

Korpus medyanı yaklaşık 25 kelimelik cümle ve 111 kelimelik paragraftır; güçlü alt küme de benzerdir. Bu, her cümlenin uzun olması gerektiği anlamına gelmez. Güçlü prose; mekanizma, koşul ve sonucu aynı cümlede tutarken yeni iddiayı ayrı cümleye bırakır. O-ISAC için güvenli revizyon hedefi, ortalamayı mekanik biçimde 25'e taşımak değil, staccato bölgeleri seçici biçimde **19–21 kelime** çevresine çıkarmaktır.

O-ISAC'ta kısa cümle oranı %19.2, uzun cümle oranı %0.7'dir. COMST medyanları sırasıyla yaklaşık %10.0 ve %12.8'dir. Bu sapma okunabilirliği artıran sadelikten öte, bazı neden/koşul ilişkilerinin parçalandığını gösterir. Buna karşılık list-heavy cümle oranı O-ISAC'ta düşüktür; listeleri yeniden prose'a dökmemek gerekir.

### 4.2 Bağlaç ve gerçek geçiş ilişkisi

| Bağlaç | COMST /1000 kelime | Güçlü alt küme | O-ISAC | O-ISAC/COMST |
|---|---:|---:|---:|---:|
| `however` | 1.587 | 1.670 | 0.067 | 0.04 |
| `first` | 0.766 | 0.844 | 0.539 | 0.70 |
| `therefore` | 0.699 | 0.615 | 2.560 | 3.67 |
| `thus` | 0.642 | 0.646 | 0.404 | 0.63 |
| `moreover` | 0.584 | 0.483 | 0.000 | 0.00 |
| `furthermore` | 0.539 | 0.704 | 0.000 | 0.00 |
| `in addition` | 0.533 | 0.583 | 0.000 | 0.00 |
| `for example` | 0.519 | 0.670 | 0.270 | 0.52 |
| `specifically` | 0.448 | 0.372 | 0.000 | 0.00 |
| `overall` | 0.334 | 0.327 | 0.404 | 1.21 |
| `for instance` | 0.320 | 0.301 | 0.000 | 0.00 |
| `finally` | 0.314 | 0.433 | 0.067 | 0.21 |
| `second` | 0.272 | 0.317 | 0.202 | 0.74 |
| `particularly` | 0.260 | 0.311 | 0.067 | 0.26 |
| `on the other hand` | 0.245 | 0.237 | 0.000 | 0.00 |

O-ISAC toplam transition yoğunluğunda düşük uçtadır; fakat `therefore` oranı korpusun yaklaşık 3.7 katıdır, `however` ise çok seyrektir. Çözüm bağlaç serpiştirmek değildir. Her paragrafın açılışı önceki paragrafla gerçek ilişkisini—continuation, cause, contrast, narrowing veya return—kurmalı; `therefore` yalnız mantıksal sonuç gerçekten çıkarıldığında kalmalıdır.

### 4.3 Soğuk/otomatik dil sinyalleri

- Noktalı virgül yoğunluğu korpus maksimumunun üzerindedir; iki bağımsız iddia veya condition varsa nokta/bağlaçla yeniden kurulmalıdır.
- `does not`, `cannot`, `rather than`, `only when` gibi boundary ifadeleri bilimsel temkin için gereklidir; ancak O-ISAC oranı korpus maksimumunun da üzerindedir. Aynı sınır her bölümde yeniden söylenmemeli, mümkün olduğunda pozitif ve bounded finding biçimine çevrilmelidir.
- Nominalization yoğunluğu üst uçtadır. `assessment of`, `characterization of`, `implementation of` zincirleri somut fiillerle sadeleştirilmelidir.
- Tekrarlanan `we organize/we distinguish/we therefore` kalıpları bölüm işlevini anlatır fakat survey bulgusunu geri plana iter. Prose önce ne öğrenildiğini, sonra bunun nasıl düzenlendiğini söylemelidir.

## 5. Şekil ve Tablo Almanakı

Korpus toplam **1.096 şekil + 654 tablo** içerir. Makale medyanları **13 şekil** ve **8 tablo**dur; bunlar hedef değil, görsellerin COMST anlatısında taşıdığı yükün göstergesidir.

### 5.1 En yaygın işlevler

| Tür | İşlev | Öğe | Makale | Prevalans | Önceden hazırlanan | Sonradan yorumlanan | Inventory offload |
|---|---|---:|---:|---:|---:|---:|---:|
| figure | `system_architecture` | 230 | 67 | 88.2% | 35.7% | 40.0% | 0.0% |
| figure | `performance_plot` | 214 | 57 | 75.0% | 37.9% | 42.1% | 0.0% |
| figure | `taxonomy_map` | 159 | 55 | 72.4% | 37.1% | 40.3% | 34.0% |
| figure | `other` | 111 | 32 | 42.1% | 42.3% | 46.8% | 0.0% |
| table | `method_algorithm_comparison` | 109 | 41 | 53.9% | 53.2% | 17.4% | 100.0% |
| table | `study_inventory` | 107 | 37 | 48.7% | 38.3% | 21.5% | 100.0% |
| table | `other` | 92 | 34 | 44.7% | 40.2% | 9.8% | 0.0% |
| figure | `physical_mechanism` | 88 | 28 | 36.8% | 37.5% | 51.1% | 0.0% |
| figure | `protocol_workflow` | 78 | 32 | 42.1% | 33.3% | 56.4% | 0.0% |
| table | `system_parameter_comparison` | 76 | 36 | 47.4% | 31.6% | 19.7% | 94.7% |
| table | `related_survey_comparison` | 69 | 59 | 77.6% | 42.0% | 18.8% | 69.6% |
| figure | `survey_roadmap` | 49 | 45 | 59.2% | 44.9% | 20.4% | 26.5% |
| figure | `application_map` | 45 | 32 | 42.1% | 48.9% | 22.2% | 42.2% |
| table | `acronym_notation` | 44 | 41 | 53.9% | 36.4% | 4.5% | 34.1% |
| figure | `signal_processing_flow` | 40 | 25 | 32.9% | 27.5% | 35.0% | 0.0% |
| table | `performance_comparison` | 38 | 19 | 25.0% | 39.5% | 23.7% | 100.0% |
| figure | `tradeoff_plot` | 34 | 16 | 21.1% | 29.4% | 58.8% | 0.0% |
| table | `taxonomy_definition` | 29 | 26 | 34.2% | 34.5% | 17.2% | 75.9% |
| table | `application_mapping` | 25 | 19 | 25.0% | 40.0% | 32.0% | 100.0% |
| figure | `timeline_evolution` | 23 | 20 | 26.3% | 47.8% | 26.1% | 0.0% |

### 5.2 Yerleşim ve prose ilişkisi

| Alan | Değer | n/1750 | Oran |
|---|---|---:|---:|
| `placement_within_section` | `middle` | 774/1750 | 44.2% |
| `placement_within_section` | `late` | 493/1750 | 28.2% |
| `placement_within_section` | `early` | 483/1750 | 27.6% |
| `first_mention_relation` | `before_visual` | 717/1750 | 41.0% |
| `first_mention_relation` | `at_visual` | 518/1750 | 29.6% |
| `first_mention_relation` | `after_visual` | 350/1750 | 20.0% |
| `first_mention_relation` | `not_recovered` | 165/1750 | 9.4% |
| `prose_prepares_before` | `yes` | 680/1750 | 38.9% |
| `prose_prepares_before` | `no` | 664/1750 | 37.9% |
| `prose_prepares_before` | `partial` | 315/1750 | 18.0% |
| `prose_prepares_before` | `unclear` | 91/1750 | 5.2% |
| `prose_interprets_after` | `yes` | 574/1750 | 32.8% |
| `prose_interprets_after` | `unclear` | 565/1750 | 32.3% |
| `prose_interprets_after` | `no` | 410/1750 | 23.4% |
| `prose_interprets_after` | `partial` | 201/1750 | 11.5% |
| `inventory_offload` | `no` | 1017/1750 | 58.1% |
| `inventory_offload` | `yes` | 599/1750 | 34.2% |
| `inventory_offload` | `partial` | 118/1750 | 6.7% |
| `inventory_offload` | `unclear` | 16/1750 | 0.9% |

Yerleşim çoğunlukla section middle'dır; ancak asıl kural konum değil işlevdir. Her O-ISAC görseli için metin önce **hangi soruya bakılacağını**, sonra **hangi tasarım sonucunun çıkarıldığını** söylemelidir. Korpus oranları OCR ve caption drift içerdiğinden bunlar kalite eşiği değildir.

### 5.3 O-ISAC için kayıtlı görsel plan

| Sıra | Dosya / bağlam | Tür | Okuyucu işi | Komşu bölümlere etkisi | Evidence gate |
|---:|---|---|---|---|---|
| 3 | `02_RELATED_SURVEYS_AND_SCOPE.tex` — RELATED SURVEYS AND SCOPE | table | Compare prior O-ISAC surveys by reader utility, define the unresolved empirical-comparison gap, and state the review's non-claims. | Önce: It verifies the Introduction's novelty claim using named prior work. Sonra: The table will make the technical axes introduced in Foundations appear as a direct response to a visible gap. | Retain all seven cited reviews, the September 2026 metadata caveat, the 227-report/206-study boundary, and the explicit no-ranking and no-universal-scale claims. |
| 4 | `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` — O-ISAC FOUNDATIONS AND THE CROSS-PLATFORM COMPARISON FRAMEWORK | figure | Introduce the four-axis cross-platform framework: physical context, coupling location, measurement plane, and provenance. | Önce: It turns the Related Surveys gap into an explicit analytical response. Sonra: It prepares the system-boundary and taxonomy units to define individual axes rather than re-explain the whole framework. | The figure must preserve modality/signal path, integration mechanism, measurement plane, condition, validation, and the rule that missing fields are not inferred. |
| 9 | `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` — The Cross-Platform Comparison Record | table | Specify the structured comparison record and the three admissibility outcomes used throughout synthesis. | Önce: It converts the measurement-plane concept into an operational record. Sonra: It gives Review Methods a clear technical object whose selection and governance can be explained next. | The table must include modality, path, tasks, mechanism, metric definition/plane/unit, conditions, target, constraints, validation, baseline, locator, and no unconditional comparison category. |
| 17 | `05_CORPUS_AND_APPRAISAL_RESULTS.tex` — Study Selection and Report-to-Study Mapping | figure | Reconcile identification, screening, retrieval, full-text eligibility, contextual records, and report-to-study mapping. | Önce: It grounds the new results bridge in the actual evidence flow. Sonra: Governed Evidence Base can start from the fixed 206-study corpus without revisiting report attrition. | Reconcile 1,733 identified, 472 duplicates plus 2 other dispositions, 1,259 screened, 927 not advanced, 330 reports sought after aliases, 58 unretrieved, 272 assessed, 227 eligible reports, 67 contextual records, and 206 unique studies. |
| 18 | `05_CORPUS_AND_APPRAISAL_RESULTS.tex` — Governed Evidence Base | table | Describe claim-level dispositions and distinguish coding records, primary synthesis records, study restrictions, and audit events. | Önce: It starts from the 206-study denominator established by the selection flow. Sonra: Study-Level Appraisal can then discuss evidence strength without re-defining claim partitions. | The table must reconcile 3,206 qualitative + 4,997 quantitative + 31 contextual + 72 quarantined = 8,306; 8,203 primary records; 3,020 evidence + 4,779 metric + 404 trade-off rows; 93 audit events distinct from quarantined claims. |
| 21 | `06_OPTICAL_MODALITY_FAMILIES.tex` — OPTICAL MODALITY FAMILIES | table | Introduce six canonical modality families, their non-duplicative counts, and the boundary between canonical counting and multi-label integration. | Önce: It turns the evidence-portability boundary into a physical organization of the corpus. Sonra: Photonics-assisted Terahertz can begin the family close read with the shared comparison axes already visible. | The table must preserve counts 69/56/38/31/9/3 = 206, dominant optical role, canonical-not-exclusive status, and representative citations without implying rank. |
| 29 | `07_INTEGRATION_ARCHITECTURES.tex` — INTEGRATION ARCHITECTURES AND RESOURCE COUPLING | figure | Shift from physical modality to multi-label integration mechanisms and report their overlapping prevalence. | Önce: It receives the modality section's physical boundary and changes the organizing axis deliberately. Sonra: Shared Hardware can start with component-level reuse while the reader retains the whole mechanism map. | Keep 118 resource, 117 hardware, 113 waveform, 87 link/channel, 72 joint design, 49 carrier, 46 application, 3 mixed, none unresolved; mark all as multi-label and non-hierarchical. |
| 35 | `08_METRICS_AND_COMPARISON_LOGIC.tex` — METRICS AND COMPARISON LOGIC | table | Introduce typed metric evidence, report coverage, and frame semantic comparability as the section's central problem. | Önce: It receives the integration section's question about measurable outcomes. Sonra: The comparable-observation rules can be folded into the table preface rather than form another abstract subsection. | Reconcile 4,779 records; sensing 203 studies/1,816 records, communication 194/1,328, joint 158/870, implementation 64/476; keep all coverage multi-label and non-ranking. |
| 42 | `09_COMMUNICATION_SENSING_TRADEOFFS.tex` — COMMUNICATION--SENSING TRADE-OFFS | figure | Define trade-off as an evidenced interdependence, reconcile the governed ledger, and establish conditionality before mechanism families. | Önce: It converts metric admissibility into a causal relationship synthesis. Sonra: Bandwidth and Resource Allocation can begin with the largest family while the reader sees the full map. | Reconcile 404 coded rows, 2 absence sentinels, 402 substantive records from 168 studies, 218 quantitative, 184 qualitative, 371 conditional; prohibit summing study counts or interpreting frequency as strength. |
| 50 | `10_VALIDATION_AND_REPRODUCIBILITY.tex` — Maximum Validation Maturity | figure | Report mutually exclusive maximum validation tiers and interpret the gap between laboratory/prototype and field evidence. | Önce: It turns the section opening's distinctions into a corpus-level result. Sonra: Validation Methods can explain overlapping evidence without reusing the exclusive-tier visual. | Keep 32/18/78/66/12 = 206, 156 at least laboratory, 12 field, all representative citations, and the rule that maximum tier does not measure condition coverage or paired functions. |
| 53 | `10_VALIDATION_AND_REPRODUCIBILITY.tex` — Reported Artifacts and Reconstructability | table | Report data and code/model availability and distinguish discoverability from reconstructability. | Önce: It follows paired-function maturity with the external reuse question. Sonra: Benchmark Readiness can use the table as the artifact component of its conjunctive contract. | Reconcile data 145/41/13/7 = 206, code 197/7/1/1 = 206, reproducibility 4/199/3, preserve unavailable-or-unreported wording, no universal link tests or execution claims, and all five citations. |
| 55 | `11_TECHNOLOGIES_APPLICATIONS_6G.tex` — ENABLING TECHNOLOGIES, APPLICATIONS, AND 6G POSITIONING | figure | Introduce a cross-layer chain from physical technology and observables through spatial control, intelligence, applications, and 6G framing. | Önce: It follows validation by returning to what must be validated across a complete system chain. Sonra: Shared Samples to Physical Observables can start at the source and signal layers of the map. | The figure must separate generation/transport, observables, spatial control, inference, application requirements, and 6G/network evidence; mark all technology and application labels multi-label. |
| 59 | `11_TECHNOLOGIES_APPLICATIONS_6G.tex` — Applications as Operating-Requirement Bundles | table | Interpret overlapping application labels as operating-requirement bundles rather than markets or architectures. | Önce: It turns the preceding technology and inference layers into mission constraints. Sonra: The 6G Label subsection can then distinguish broad use-case relevance from network readiness using the same requirement map. | Retain every application count, multi-label/non-market warning, target and communication-role conditions, and all twelve cited examples; do not sum categories. |
| 64 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` — Research Roadmap | table | Organize five research priorities that convert observed evidence gaps into testable success criteria. | Önce: It receives concrete network gaps from the preceding expanded subsection. Sonra: Limitations can then follow one consolidated research agenda rather than five isolated micro-sections. | Every roadmap row must trace to a result in Metrics, Trade-offs, Validation, or Technologies; preserve modality-specific physics and avoid claims that the review tested proposed interventions. |

## 6. O-ISAC Dosya-Bazlı Denetim

Bu bölümdeki kararlar henüz manuscripte uygulanmadı. Her dosyanın etkisi komşu bölümlerle birlikte değerlendirilmiştir.

### `00_ABSTRACT.tex`

Özetin soru odaklı ve survey-first akışı korunmalı. Bulguların sayısı görsel/tablo entegrasyonundan sonra bir kez daha uzlaştırılmalı; PRISMA ayrıntısı özetin önüne geçmemeli.

- Mevcut profil: 235 kelime, 1 birim, ortalama cümle 23.5 kelime, citation-group density 0.0/100 kelime.
- Eşleşen COMST rolleri: `abstract`.
- Karar dağılımı: retain=1.

### `01_INTRODUCTION.tex`

Giriş bilinçli olarak kısa ve teknik soruya odaklıdır. Ayrı Related Surveys bölümüyle birlikte ön çerçeve COMST aralığına girer; yeni bir katalog paragrafı eklemek yerine mevcut nedensel akış korunmalıdır.

- Mevcut profil: 679 kelime, 1 birim, ortalama cümle 18.861 kelime, citation-group density 1.031/100 kelime.
- Eşleşen COMST rolleri: `introduction_motivation`.
- Karar dağılımı: retain=1.

### `02_RELATED_SURVEYS_AND_SCOPE.tex`

Önceki survey'leri tek tek anlatmak yerine karşılaştırma eksenlerini tabloya taşımalıdır. Metin yalnız tablonun gösterdiği gerçek boşluğu ve bu çalışmanın sınırını yorumlamalıdır.

- Mevcut profil: 727 kelime, 1 birim, ortalama cümle 18.641 kelime, citation-group density 0.825/100 kelime.
- Eşleşen COMST rolleri: `related_surveys_gap`.
- Karar dağılımı: add_table=1.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| RELATED SURVEYS AND SCOPE | `add_table` | A related-survey matrix can externalize scope, analytical depth, modality coverage, evidence unit, and comparison logic without repeating the prose. | Önce: It verifies the Introduction's novelty claim using named prior work. Sonra: The table will make the technical axes introduced in Foundations appear as a direct response to a visible gap. |

### `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex`

Teknik çerçeve gerekli, fakat aynı dört ekseni farklı alt başlıklarda yeniden kurmamalıdır. Bir ana çerçeve şekli ve karşılaştırma-kaydı tablosu tekrarın yükünü taşıyabilir.

- Mevcut profil: 1182 kelime, 6 birim, ortalama cümle 17.13 kelime, citation-group density 0.761/100 kelime.
- Eşleşen COMST rolleri: `background_foundations, taxonomy_framework`.
- Karar dağılımı: add_figure=1; add_table=1; merge=1; retain=2; trim=1.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| O-ISAC FOUNDATIONS AND THE CROSS-PLATFORM COMPARISON FRAMEWORK | `add_figure` | A single framework diagram can carry the recurring relations and reduce later verbal restatement while giving the reader a persistent reference. | Önce: It turns the Related Surveys gap into an explicit analytical response. Sonra: It prepares the system-boundary and taxonomy units to define individual axes rather than re-explain the whole framework. |
| Technical System Boundary | `merge` | Folding this paragraph into the parent opening preserves the boundary while reducing a one-paragraph subsection break. | Önce: The Foundations opening becomes a complete problem-and-boundary statement. Sonra: Modality and Signal-Path Boundaries can begin directly with the six-family classification rule. |
| Modality and Signal-Path Boundaries | `trim` | This early unit should fix classification and transfer boundaries; detailed family behavior belongs in the later evidence-led modality section. | Önce: The merged technical boundary will flow into a concise, rule-based taxonomy. Sonra: The integration ladder will receive a clean set of physical categories without premature family mini-surveys. |
| The Cross-Platform Comparison Record | `add_table` | A schema table can make the comparison contract reproducible and later tables can point to the same field definitions. | Önce: It converts the measurement-plane concept into an operational record. Sonra: It gives Review Methods a clear technical object whose selection and governance can be explained next. |

### `04_REVIEW_METHODS_AND_EVIDENCE_GOVERNANCE.tex`

Ayrı üst seviye yöntem bölümü yerel COMST korpusunda seyrektir. İzlenebilirlik, tarih, seçim sınırı, AI-insan rolü ve çıkarım kısıtları ana metinde kalmalı; ayrıntılı lineage ve puanlama mekaniği ek dosyaya taşınmalıdır.

- Mevcut profil: 1568 kelime, 6 birim, ortalama cümle 17.231 kelime, citation-group density 0.064/100 kelime.
- Eşleşen COMST rolleri: `methods_review_protocol, scope_contributions_organization`.
- Karar dağılımı: move_to_supplement=1; rewrite_transition=1; trim=4.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| REVIEW METHODS AND EVIDENCE GOVERNANCE | `rewrite_transition` | A two-sentence bridge should state that the method preserves study identity and claim conditions, without adding more governance detail. | Önce: It will close the framework section by explaining why evidence assembly must follow the comparison contract. Sonra: Review Design can begin with executed design choices rather than carrying the entire cross-section transition. |
| Review Design, Scope, and Protocol Lineage | `trim` | The main text needs the retrospective-registration limitation and non-attrition warning, while detailed predecessor-state lineage is better kept in the protocol record. | Önce: The new methods bridge will lead into a concise transparency statement instead of a historical detour. Sonra: Search Strategy will become the first detailed executed method the reader encounters. |
| Search Strategy and Eligibility | `trim` | Condensing execution detail while retaining reproducible source/date/rule information will keep the main text readable and PRISMA-S compliant. | Önce: It follows the shortened protocol lineage with the actual evidence boundary. Sonra: Selection and Counting Units can then explain how eligible reports became unique studies. |
| Selection, Counting Units, and Reviewer Process | `trim` | The main text should retain roles, provenance, and independence limitations; invariant/checklist mechanics can live with the audit materials. | Önce: It converts eligibility rules into a non-inflated study denominator. Sonra: Extraction can begin from a clear study-report relationship without repeating workflow controls. |
| Extraction and Claim-Level Governance | `trim` | Keeping the claim contract and conflict rule while removing repeated examples will protect rigor without interrupting the survey's technical flow. | Önce: It receives a well-defined report-to-study map from Selection. Sonra: Technical Appraisal can focus on evidence strength rather than re-explaining claim semantics. |
| Technical Appraisal, Certainty, and Synthesis | `move_to_supplement` | A short main-text summary can state purpose, eight dimensions, evidence-body aggregation, and narrative synthesis while the reproducible algorithm moves to a supplement. | Önce: Extraction will end with a concise statement of how evidence strength is controlled. Sonra: Corpus Results can begin sooner and refer to the supplement when reporting score distributions. |

### `05_CORPUS_AND_APPRAISAL_RESULTS.tex`

Korpusta bağımsız 'corpus results' rolü görülmediği için bu bölüm journal-atipiktir. PRISMA akışı ve claim disposition tablosu ile kısa tutulmalı; validation/artifact ayrıntısı Section 10'a bırakılmalıdır.

- Mevcut profil: 1012 kelime, 5 birim, ortalama cümle 16.323 kelime, citation-group density 0.0/100 kelime.
- Eşleşen COMST rolleri: `methods_review_protocol, corpus_descriptive_results, background_foundations`.
- Karar dağılımı: add_figure=1; add_table=1; retain=1; rewrite_transition=1; trim=1.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| CORPUS AND APPRAISAL RESULTS | `rewrite_transition` | A brief results bridge should distinguish corpus composition from evidence portability and announce that repeated validation details are deferred to Section 10. | Önce: It will signal the shift from executed method to empirical review outputs. Sonra: Study Selection can present the flow as the first result rather than an unannounced continuation of methods. |
| Study Selection and Report-to-Study Mapping | `add_figure` | A flow diagram will make denominator transitions and contextual branches auditable while shortening the screening narrative. | Önce: It grounds the new results bridge in the actual evidence flow. Sonra: Governed Evidence Base can start from the fixed 206-study corpus without revisiting report attrition. |
| Governed Evidence Base | `add_table` | A disposition table can show the unit, category, count, inclusion in primary synthesis, and reconciliation formula. | Önce: It starts from the 206-study denominator established by the selection flow. Sonra: Study-Level Appraisal can then discuss evidence strength without re-defining claim partitions. |
| Study-Level Technical Appraisal | `trim` | Keeping overall/dimension/appraisal results here and assigning validation, artifacts, and benchmark readiness exclusively to Section 10 removes the Sec05↔Sec10 duplication. | Önce: Governed claim counts will feed directly into study-level evidence-strength results. Sonra: Evidence-Body Certainty can aggregate the appraisal without an intervening preview of the later validation section. |

### `06_OPTICAL_MODALITY_FAMILIES.tex`

Survey'in fiziksel omurgalarından biridir. Modalite matrisi sayıları ve çalışma görünürlüğünü taşırken prose her ailenin mekanizmasını, kısıtını ve transfer sınırını açıklamalıdır.

- Mevcut profil: 1486 kelime, 8 birim, ortalama cümle 18.575 kelime, citation-group density 0.404/100 kelime.
- Eşleşen COMST rolleri: `technical_family_synthesis, background_foundations`.
- Karar dağılımı: add_table=1; merge=2; retain=5.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| OPTICAL MODALITY FAMILIES | `add_table` | A modality matrix will increase study visibility and let the six prose subsections focus on mechanisms rather than repeat definitions. | Önce: It turns the evidence-portability boundary into a physical organization of the corpus. Sonra: Photonics-assisted Terahertz can begin the family close read with the shared comparison axes already visible. |
| Other Optical Systems | `merge` | Combining the residual cases with the cross-family boundary will retain them while reducing structural fragmentation. | Önce: Hybrid Systems will flow into a compact residual-and-boundary close. Sonra: The merged close can transition directly to mechanism-based Integration Architectures. |
| Cross-Family Interpretation Boundary | `merge` | A single unheaded closing synthesis can retain the boundary and residual evidence while improving pace. | Önce: It will give the merged residual paragraph an explicit field-level implication. Sonra: Integration Architectures will receive a direct physical-family-to-coupling transition. |

### `07_INTEGRATION_ARCHITECTURES.tex`

Modaliteden coupling mekanizmasına geçiş açıkça işaretlenmelidir. Çok etiketli mimari haritası kategorileri toplamaya veya hiyerarşik sıralamaya dönüştürmeden örtüşmeleri göstermelidir.

- Mevcut profil: 999 kelime, 6 birim, ortalama cümle 17.839 kelime, citation-group density 1.101/100 kelime.
- Eşleşen COMST rolleri: `integration_design, tradeoff_optimization, background_foundations`.
- Karar dağılımı: add_citations=1; add_figure=1; merge=1; retain=3.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| INTEGRATION ARCHITECTURES AND RESOURCE COUPLING | `add_figure` | An architecture map should show coupling locations and overlaps rather than a misleading exclusive bar chart. | Önce: It receives the modality section's physical boundary and changes the organizing axis deliberately. Sonra: Shared Hardware can start with component-level reuse while the reader retains the whole mechanism map. |
| Resource Allocation and Joint Design | `add_citations` | A few additional anchors from fiber, FSO, VLC/LiFi, and photonic-THz would demonstrate transfer boundaries without creating a catalogue. | Önce: It follows waveform sharing by exposing the rules that allocate shared resources. Sonra: Application-Level Coupling can then present the broad boundary after stronger evidence for explicit joint design. |
| What the Integration Counts Mean | `merge` | Removing the heading and retaining the paragraph as the section close will improve flow without losing content. | Önce: It will turn Application-Level Coupling directly into a field-level synthesis. Sonra: Metrics and Comparison Logic will receive an uninterrupted causal question about whether outcomes are defined well enough. |

### `08_METRICS_AND_COMPARISON_LOGIC.tex`

Bu bölüm survey'in özgün karşılaştırma disiplinidir. Ölçüm düzlemi ve admissibility kuralları tek contract tablosunda sabitlenmeli; kısa mikro-alt başlıklar birleştirilmelidir.

- Mevcut profil: 1617 kelime, 7 birim, ortalama cümle 17.021 kelime, citation-group density 0.989/100 kelime.
- Eşleşen COMST rolleri: `metrics_performance_comparison, taxonomy_framework`.
- Karar dağılımı: add_table=1; merge=2; retain=4.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| METRICS AND COMPARISON LOGIC | `add_table` | A metric-contract table will let later prose explain boundary cases while improving study-level evidence visibility. | Önce: It receives the integration section's question about measurable outcomes. Sonra: The comparable-observation rules can be folded into the table preface rather than form another abstract subsection. |
| From Reported Quantity to Comparable Observation | `merge` | Folding the irreducible rules into the section opening and proposed metric table will remove a repeated abstract framework layer. | Önce: The metric-section introduction will become an actionable contract rather than a second general definition. Sonra: Communication Metrics can begin directly with information accounting and reliability distinctions. |
| Applying Measurement Planes | `merge` | The unique multisegment example should be folded into Joint Metrics or the metric table, while the repeated plane definitions remain in Section 3. | Önce: Joint and Implementation Metrics will retain the practical chain example without a new conceptual reset. Sonra: The admissibility subsection can follow directly as the empirical outcome of the comparison contract. |

### `09_COMMUNICATION_SENSING_TRADEOFFS.tex`

Frekansları performans üstünlüğü gibi göstermeden 402 substantive kaydı koşullu mekanizma aileleri olarak sentezlemelidir. Universal rate-resolution/Pareto iddiası kurulmayacaktır.

- Mevcut profil: 1293 kelime, 7 birim, ortalama cümle 17.24 kelime, citation-group density 0.541/100 kelime.
- Eşleşen COMST rolleri: `tradeoff_optimization, background_foundations`.
- Karar dağılımı: add_citations=1; add_figure=1; retain=4; trim=1.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| COMMUNICATION--SENSING TRADE-OFFS | `add_figure` | A mechanism-family figure can show record/study coverage and conditional share without visualizing incompatible effect magnitudes. | Önce: It converts metric admissibility into a causal relationship synthesis. Sonra: Bandwidth and Resource Allocation can begin with the largest family while the reader sees the full map. |
| Waveform, Hardware, and Complexity | `add_citations` | Adding a small set of source-verified prototype examples will show that complexity migrates differently across hardware and DSP chains. | Önce: It extends performance coupling to feasibility and implementation burden. Sonra: The long-tail close can then reserve only genuinely non-recurring relationships. |
| Long-Tail Relationships and the Frontier Boundary | `trim` | Keep the rare-category evidence and one concise frontier boundary, then move promptly to validation. | Önce: Waveform/complexity will feed a shorter residual-family synthesis instead of another framework restatement. Sonra: Validation can begin from the question of whether observed couplings survive realistic evidence settings. |

### `10_VALIDATION_AND_REPRODUCIBILITY.tex`

Section 5'teki genel appraisal ile yinelenmemelidir. Maksimum validation tier, paired-function evidence, artifact availability ve benchmark readiness burada tek otorite olmalıdır.

- Mevcut profil: 1116 kelime, 6 birim, ortalama cümle 16.657 kelime, citation-group density 0.538/100 kelime.
- Eşleşen COMST rolleri: `validation_experiment_reproducibility, methods_review_protocol`.
- Karar dağılımı: add_figure=1; add_table=1; retain=4.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| Maximum Validation Maturity | `add_figure` | A simple tier distribution will make 206-study reconciliation and the operational evidence gap visible; captions can state that tiers are not quality ranks. | Önce: It turns the section opening's distinctions into a corpus-level result. Sonra: Validation Methods can explain overlapping evidence without reusing the exclusive-tier visual. |
| Reported Artifacts and Reconstructability | `add_table` | A data-versus-code availability table can show counts, percentages, meaning, and audit limits while retaining reconstruction guidance in prose. | Önce: It follows paired-function maturity with the external reuse question. Sonra: Benchmark Readiness can use the table as the artifact component of its conjunctive contract. |

### `11_TECHNOLOGIES_APPLICATIONS_6G.tex`

Teknolojileri ve uygulamaları kataloglamak yerine source/signal/spatial/inference/application zinciriyle bağlamalıdır. Uygulama matrisi pazar sıralaması değil operating-requirement map olmalıdır.

- Mevcut profil: 1486 kelime, 6 birim, ortalama cümle 18.346 kelime, citation-group density 0.875/100 kelime.
- Eşleşen COMST rolleri: `application_use_case, technology_enabler`.
- Karar dağılımı: add_figure=1; add_table=1; retain=4.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| ENABLING TECHNOLOGIES, APPLICATIONS, AND 6G POSITIONING | `add_figure` | A cross-layer map can show where technologies act and how application requirements feed constraints back without implying a linear maturity pipeline. | Önce: It follows validation by returning to what must be validated across a complete system chain. Sonra: Shared Samples to Physical Observables can start at the source and signal layers of the map. |
| Applications as Operating-Requirement Bundles | `add_table` | An application-to-requirement matrix can map target, communication role, geometry, update/latency, safety, and representative evidence without ranking markets. | Önce: It turns the preceding technology and inference layers into mission constraints. Sonra: The 6G Label subsection can then distinguish broad use-case relevance from network readiness using the same requirement map. |

### `12_DISCUSSION_ROADMAP_LIMITATIONS.tex`

Beş kısa roadmap mikro-bölümü tek kanıt→eylem→test→başarı ölçütü tablosunda birleşmelidir. Discussion yalnız Results'ın tekrarı değil, alan düzeyindeki sonuç ve sınırların yorumudur.

- Mevcut profil: 1203 kelime, 10 birim, ortalama cümle 18.508 kelime, citation-group density 0.083/100 kelime.
- Eşleşen COMST rolleri: `methods_review_protocol, lessons_learned_discussion, metrics_performance_comparison, validation_experiment_reproducibility, technology_enabler, limitations`.
- Karar dağılımı: add_citations=1; add_table=1; expand=1; merge=5; retain=1; rewrite_transition=1.

| Birim | Karar | Gerekçe | Önceki/sonraki etki |
|---|---|---|---|
| DISCUSSION, RESEARCH ROADMAP, AND LIMITATIONS | `rewrite_transition` | A short bridge should state that the section separates what the evidence supports, what experiment is next, and what the review itself cannot establish. | Önce: It will turn the 6G label boundary into a discussion question. Sonra: Cross-Cutting Interpretation can begin with the answer rather than also carrying section navigation. |
| Cross-Cutting Interpretation | `add_citations` | A small set of representative anchors and internal section references can show which evidence supports each field-level inference without turning Discussion into a catalogue. | Önce: It receives the new discussion bridge and states the survey's answer. Sonra: From 6G Framing can specialize the end-to-end evidence gap rather than repeat the whole synthesis. |
| From 6G Framing to Network Evidence | `expand` | A concise expansion should distinguish access/fronthaul/transport roles and cite the strongest available network-scale examples and missing interfaces. | Önce: It narrows Cross-Cutting Interpretation to the 6G claim boundary. Sonra: The Research Roadmap can then formulate tests for the named orchestration, mobility, energy, security, and recovery gaps. |
| Research Roadmap | `add_table` | A single roadmap table can integrate evidence gap, action, modality-specific test, success criterion, and dependency while reducing heading fragmentation. | Önce: It receives concrete network gaps from the preceding expanded subsection. Sonra: Limitations can then follow one consolidated research agenda rather than five isolated micro-sections. |
| Make the measurement contract routine | `merge` | Convert it into the measurement-contract row of the roadmap table, referencing rather than restating the full framework. | Önce: It becomes the first actionable response to the network and cross-platform evidence gaps. Sonra: The benchmark row can build on a stable measurement contract. |
| Build modality-aware benchmarks | `merge` | Place it in the roadmap table with explicit dependencies and modality columns instead of expanding prose. | Önce: It follows the measurement-contract action as its experimental implementation. Sonra: The realistic-disturbance row can define how those benchmarks are stress-tested. |
| Test joint operation under realistic disturbance | `merge` | A roadmap-table row can expose the dependency chain and retain modality-specific disturbance examples compactly. | Önce: It turns benchmark definitions into an operational stress test. Sonra: The artifact row can specify what must be released to reproduce that test. |
| Release the artifacts that define the experiment | `merge` | Place the required package and external rerun criterion in the roadmap table, linking back to artifact results rather than re-explaining them. | Önce: It supplies the reproducibility layer for the realistic-disturbance test. Sonra: The intelligence/scale/security row can add system-specific evaluation extensions to the same reusable package. |
| Evaluate intelligence, scale, and security as system properties | `merge` | A final roadmap-table row can separate evaluation dimensions and link them to technology, application, and network evidence. | Önce: It extends the reusable experiment package to adaptive and network-scale systems. Sonra: Limitations can then distinguish proposed future tests from what this review actually established. |

### `13_CONCLUSION.tex`

Kısa sonuç bölümü korunabilir. Yeni sayı veya iddia eklememeli; survey'in neyi açıklığa kavuşturduğunu ve ortak değerlendirme ilkelerinin neden gerekli olduğunu kapatmalıdır.

- Mevcut profil: 240 kelime, 1 birim, ortalama cümle 20.0 kelime, citation-group density 0.0/100 kelime.
- Eşleşen COMST rolleri: `conclusion`.
- Karar dağılımı: retain=1.

## 7. Güvenirlik ve Hangi İstatistiğe Ne Kadar Güvenileceği

Altı önceden seçilmiş makalede 243 section ve 137 visual bağımsız yeniden kodlandı. Exact key/count gate PASS; eksik kod yoktur. Mevcut durum: **COMPLETE**.

| Birim | Alan | Agreement | Kappa | Kullanım kararı |
|---|---|---:|---:|---|
| section | `normalized_primary_role` | 58.0% | 0.5310034248519366 | Orta kararlılık; geniş pattern için kullanılabilir. |
| section | `opening_relation` | 34.2% | 0.1727659574468085 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| section | `closing_relation` | 39.1% | 0.22349130951095755 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| section | `paragraph_contract` | 32.1% | 0.14841874986725567 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| section | `sentence_architecture` | 20.2% | 0.062242644864832615 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| section | `dominant_organization` | 53.5% | 0.22104337465603816 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| section | `tone` | 35.0% | 0.11701393680143513 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| section | `tutorial_depth` | 43.6% | 0.15721120984278883 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| section | `comparison_explicitness` | 27.6% | -0.00455677173861983 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| section | `visual_dependency` | 64.6% | 0.442630820931349 | Orta kararlılık; geniş pattern için kullanılabilir. |
| section | `move_sequence_exact` | 0.4% | NA | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| visual | `visual_function` | 49.6% | 0.4600753941055517 | Orta kararlılık; geniş pattern için kullanılabilir. |
| visual | `placement_within_section` | 78.1% | 0.663059517953763 | Görece kararlı; yine de betimleyici. |
| visual | `prose_prepares_before` | 56.2% | 0.2899714952060119 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| visual | `prose_interprets_after` | 42.3% | 0.19734500148323939 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| visual | `data_density` | 61.3% | 0.3144179019922576 | Düşük kararlılık; hard journal normu olarak kullanılmaz. |
| visual | `inventory_offload` | 83.9% | 0.6766788242866337 | Görece kararlı; yine de betimleyici. |

Bu sonuç, objective counts ile interpretive coding'i ayırmamızı gerektirir. Kelime, cümle, citation, görsel sayısı ve yerleşim gibi otomatik ölçüler güçlüdür. `sentence_architecture`, `tone`, exact move sequence ve comparison-explicitness gibi alanlar yalnız açıklayıcı örnek ve close-reading desteğiyle kullanılacaktır; yüzdeye bakılarak manuscript yeniden tasarlanmayacaktır.

Adjudication durumu: **COMPLETE**.
- Hakemlenen uyuşmazlık: 1994
- Primary confirmed: 135
- Secondary adopted: 1774
- Third value: 85

## 8. Uygulama Sırası

1. Author review ile 71 decision row'u onayla veya değiştir.
2. Section 5↔10 tekrarını kaldır; methods ayrıntısını supplement'e ayır; kısa roadmap ve metric-plane başlıklarını birleştir.
3. Önce sekiz tabloyu üret: related surveys, comparison record, claim disposition, modality, metric contract, artifact, application requirements ve roadmap.
4. Sonra altı şekli üret: framework, PRISMA/report-to-study flow, integration map, trade-off map, validation tiers ve technology→application chain.
5. Tablo/görsellerle prose tekrarını azalt; her görsel için question-before / implication-after kontrolü yap.
6. 206-study traceability tablosu/supplementini bağla; main prose'a yalnız temsilî ve claim-matched citations ekle.
7. Dil geçişini uygula: staccato cümleleri seçici birleştir, `therefore` ve noktalı virgül tekrarını azalt, sınırları pozitif bounded findings ile çeşitlendir.
8. Abstract, Introduction ve Conclusion'ı yeni görsel/kanıt katmanından sonra yeniden uzlaştır.
9. En son evidence-number, citation-key, PRISMA, visual-caption ve manuscript-integrity QA çalıştır. LaTeX derleme bu almanak aşamasının parçası değildir.

## 9. Tam 71-Birim Karar Kaydı

| # | Dosya | Başlık | Rol | Kelime | Karar | Gerekçe | Evidence gate | Durum |
|---:|---|---|---|---:|---|---|---|---|
| 1 | `00_ABSTRACT.tex` | Abstract | `abstract` | 235 | `retain` | It already performs the compact survey-first reader job without foregrounding PRISMA or governance machinery. | Keep the 206-study window, 402 substantive trade-off records, three integration patterns, conditional-comparison boundary, and field/artifact scarcity synchronized with frozen results. | `not_implemented` / `pending_author_review` |
| 2 | `01_INTRODUCTION.tex` | INTRODUCTION | `introduction_motivation` | 679 | `retain` | The section reaches the survey gap quickly and keeps PRISMA details out of the opening argument. | Preserve the inclusive O-ISAC boundary, the four contributions, the 1 January 2020–22 June 2026 window, and citations supporting each modality example and IMT-2030 framing. | `not_implemented` / `pending_author_review` |
| 3 | `02_RELATED_SURVEYS_AND_SCOPE.tex` | RELATED SURVEYS AND SCOPE | `related_surveys_gap` | 727 | `add_table` | A related-survey matrix can externalize scope, analytical depth, modality coverage, evidence unit, and comparison logic without repeating the prose. | Retain all seven cited reviews, the September 2026 metadata caveat, the 227-report/206-study boundary, and the explicit no-ranking and no-universal-scale claims. | `not_implemented` / `pending_author_review` |
| 4 | `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` | O-ISAC FOUNDATIONS AND THE CROSS-PLATFORM COMPARISON FRAMEWORK | `background_foundations` | 122 | `add_figure` | A single framework diagram can carry the recurring relations and reduce later verbal restatement while giving the reader a persistent reference. | The figure must preserve modality/signal path, integration mechanism, measurement plane, condition, validation, and the rule that missing fields are not inferred. | `not_implemented` / `pending_author_review` |
| 5 | `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` | Technical System Boundary | `background_foundations` | 96 | `merge` | Folding this paragraph into the parent opening preserves the boundary while reducing a one-paragraph subsection break. | Do not lose the statements that shared waveform is only one integration form and that a photonic front end does not make RF propagation optical. | `not_implemented` / `pending_author_review` |
| 6 | `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` | Modality and Signal-Path Boundaries | `taxonomy_framework` | 292 | `trim` | This early unit should fix classification and transfer boundaries; detailed family behavior belongs in the later evidence-led modality section. | Keep all six families, the VLC/LiFi non-synonym caveat, the photonic-THz RF-path distinction, hybrid interface accounting, and the five anchor citations. | `not_implemented` / `pending_author_review` |
| 7 | `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` | An Explanatory Ladder of Integration | `taxonomy_framework` | 203 | `retain` | The prose supplies the non-ordinal interpretation and boundary cases that a diagram alone cannot convey. | Preserve the non-maturity and non-eligibility warnings, overlapping attributes, concurrency separation, and the three representative citations. | `not_implemented` / `pending_author_review` |
| 8 | `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` | Measurement Planes Before Performance Values | `taxonomy_framework` | 210 | `retain` | A stable early definition prevents later metric sections from normalizing physically different quantities by name or unit. | Retain all named plane distinctions and the rule that analytical, simulation, laboratory, dataset, and field evidence have different validity conditions. | `not_implemented` / `pending_author_review` |
| 9 | `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` | The Cross-Platform Comparison Record | `taxonomy_framework` | 259 | `add_table` | A schema table can make the comparison contract reproducible and later tables can point to the same field definitions. | The table must include modality, path, tasks, mechanism, metric definition/plane/unit, conditions, target, constraints, validation, baseline, locator, and no unconditional comparison category. | `not_implemented` / `pending_author_review` |
| 10 | `04_REVIEW_METHODS_AND_EVIDENCE_GOVERNANCE.tex` | REVIEW METHODS AND EVIDENCE GOVERNANCE | `methods_review_protocol` | 0 | `rewrite_transition` | A two-sentence bridge should state that the method preserves study identity and claim conditions, without adding more governance detail. | Do not introduce new counts or methods in the bridge; retain the distinction between transparent review conduct and technical contribution. | `not_implemented` / `pending_author_review` |
| 11 | `04_REVIEW_METHODS_AND_EVIDENCE_GOVERNANCE.tex` | Review Design, Scope, and Protocol Lineage | `scope_contributions_organization` | 231 | `trim` | The main text needs the retrospective-registration limitation and non-attrition warning, while detailed predecessor-state lineage is better kept in the protocol record. | Keep PRISMA 2020 and PRISMA-S citations, OSF date and DOI, retrospective status, material re-baselining, the 206 active denominator, and the warning that 221-to-206 is not attrition. | `not_implemented` / `pending_author_review` |
| 12 | `04_REVIEW_METHODS_AND_EVIDENCE_GOVERNANCE.tex` | Search Strategy and Eligibility | `methods_review_protocol` | 319 | `trim` | Condensing execution detail while retaining reproducible source/date/rule information will keep the main text readable and PRISMA-S compliant. | Preserve all six sources, 1 January 2020–22 June 2026, earliest verifiable availability rule, eligible report types, joint-consideration rule, exclusions, and contextual-corpus exclusion from 206. | `not_implemented` / `pending_author_review` |
| 13 | `04_REVIEW_METHODS_AND_EVIDENCE_GOVERNANCE.tex` | Selection, Counting Units, and Reviewer Process | `methods_review_protocol` | 193 | `trim` | The main text should retain roles, provenance, and independence limitations; invariant/checklist mechanics can live with the audit materials. | Keep the distinct counting units, companion clustering and primary extraction report, investigator-supervised AI-assisted status, no routine duplicate human review, no third reviewer, and no inter-rater statistic. | `not_implemented` / `pending_author_review` |
| 14 | `04_REVIEW_METHODS_AND_EVIDENCE_GOVERNANCE.tex` | Extraction and Claim-Level Governance | `methods_review_protocol` | 367 | `trim` | Keeping the claim contract and conflict rule while removing repeated examples will protect rigor without interrupting the survey's technical flow. | Retain exact source locators, reported/calculated/digitized origin, the statement that this review did not digitize or create values, four usability categories, semantic comparison conditions, and quarantined-conflict handling. | `not_implemented` / `pending_author_review` |
| 15 | `04_REVIEW_METHODS_AND_EVIDENCE_GOVERNANCE.tex` | Technical Appraisal, Certainty, and Synthesis | `methods_review_protocol` | 458 | `move_to_supplement` | A short main-text summary can state purpose, eight dimensions, evidence-body aggregation, and narrative synthesis while the reproducible algorithm moves to a supplement. | Main text must retain that TQAF is review-specific, not eligibility or GRADE, the seven synthesis domains, 115 evidence bodies, no pooling/meta-analysis, no formal bias/sensitivity analysis; the supplement must preserve every threshold and cap. | `not_implemented` / `pending_author_review` |
| 16 | `05_CORPUS_AND_APPRAISAL_RESULTS.tex` | CORPUS AND APPRAISAL RESULTS | `methods_review_protocol` | 0 | `rewrite_transition` | A brief results bridge should distinguish corpus composition from evidence portability and announce that repeated validation details are deferred to Section 10. | The bridge must not duplicate counts; it should preserve selection, appraisal, and portability as distinct reader jobs. | `not_implemented` / `pending_author_review` |
| 17 | `05_CORPUS_AND_APPRAISAL_RESULTS.tex` | Study Selection and Report-to-Study Mapping | `methods_review_protocol` | 269 | `add_figure` | A flow diagram will make denominator transitions and contextual branches auditable while shortening the screening narrative. | Reconcile 1,733 identified, 472 duplicates plus 2 other dispositions, 1,259 screened, 927 not advanced, 330 reports sought after aliases, 58 unretrieved, 272 assessed, 227 eligible reports, 67 contextual records, and 206 unique studies. | `not_implemented` / `pending_author_review` |
| 18 | `05_CORPUS_AND_APPRAISAL_RESULTS.tex` | Governed Evidence Base | `corpus_descriptive_results` | 163 | `add_table` | A disposition table can show the unit, category, count, inclusion in primary synthesis, and reconciliation formula. | The table must reconcile 3,206 qualitative + 4,997 quantitative + 31 contextual + 72 quarantined = 8,306; 8,203 primary records; 3,020 evidence + 4,779 metric + 404 trade-off rows; 93 audit events distinct from quarantined claims. | `not_implemented` / `pending_author_review` |
| 19 | `05_CORPUS_AND_APPRAISAL_RESULTS.tex` | Study-Level Technical Appraisal | `methods_review_protocol` | 432 | `trim` | Keeping overall/dimension/appraisal results here and assigning validation, artifacts, and benchmark readiness exclusively to Section 10 removes the Sec05↔Sec10 duplication. | Retain 125/75/6 overall contribution, all eight dimension distributions, 4/10/192 comparison admissibility, score-cap effects, and the statement that TQAF does not revisit eligibility; cross-reference rather than repeat Section 10 distributions. | `not_implemented` / `pending_author_review` |
| 20 | `05_CORPUS_AND_APPRAISAL_RESULTS.tex` | Evidence-Body Certainty and Interpretive Boundary | `background_foundations` | 148 | `retain` | This unit provides the necessary bridge from appraisal results to the modality and mechanism synthesis. | Preserve 115 bodies and the 6/8/47/10/3/31/10 domain split, 54 high, 47 moderate, 10 limited, 4 unclear non-substantive exclusions, and the non-GRADE warning. | `not_implemented` / `pending_author_review` |
| 21 | `06_OPTICAL_MODALITY_FAMILIES.tex` | OPTICAL MODALITY FAMILIES | `technical_family_synthesis` | 147 | `add_table` | A modality matrix will increase study visibility and let the six prose subsections focus on mechanisms rather than repeat definitions. | The table must preserve counts 69/56/38/31/9/3 = 206, dominant optical role, canonical-not-exclusive status, and representative citations without implying rank. | `not_implemented` / `pending_author_review` |
| 22 | `06_OPTICAL_MODALITY_FAMILIES.tex` | Photonics-Assisted Terahertz Systems | `technical_family_synthesis` | 278 | `retain` | The current prose synthesizes mechanism and condition rather than listing papers, which is the correct survey-first balance. | Keep the optical-front-end versus radiated-RF distinction, coherence/conversion constraints, laboratory-versus-outdoor boundary, and all five representative citations. | `not_implemented` / `pending_author_review` |
| 23 | `06_OPTICAL_MODALITY_FAMILIES.tex` | Fiber O-ISAC | `technical_family_synthesis` | 255 | `retain` | The section consistently makes the fiber route, sensing observable, and traffic interaction the subjects of synthesis. | Preserve the two integration regimes, launch-power/dynamic-range and phase-reference limits, deployment-setting distinction, and five anchor citations. | `not_implemented` / `pending_author_review` |
| 24 | `06_OPTICAL_MODALITY_FAMILIES.tex` | VLC/LiFi Systems | `technical_family_synthesis` | 269 | `retain` | The section keeps task and receiver physics attached, preventing a universal visible-light sensing score. | Keep the non-synonym caveat, IM/DD constraints, camera-versus-photodiode distinction, matched-task comparison rule, and five representative citations. | `not_implemented` / `pending_author_review` |
| 25 | `06_OPTICAL_MODALITY_FAMILIES.tex` | Free-Space Optical Systems | `technical_family_synthesis` | 239 | `retain` | The current length is sufficient to teach the mechanism, examples, and transfer boundary without becoming a paper catalogue. | Preserve direct/reflected timing and power budgets, calibration distinctions, controlled-versus-outdoor boundary, and five representative citations. | `not_implemented` / `pending_author_review` |
| 26 | `06_OPTICAL_MODALITY_FAMILIES.tex` | Hybrid Optical Systems | `technical_family_synthesis` | 161 | `retain` | Its concise interface-led synthesis gives the hybrid category a distinct analytical purpose. | Keep the nine-study count, conversion-point and segment-specific power distinctions, and all five cited hybrid examples. | `not_implemented` / `pending_author_review` |
| 27 | `06_OPTICAL_MODALITY_FAMILIES.tex` | Other Optical Systems | `technical_family_synthesis` | 57 | `merge` | Combining the residual cases with the cross-family boundary will retain them while reducing structural fragmentation. | Do not drop the three distinct cases or citations, and do not create a pooled residual performance category. | `not_implemented` / `pending_author_review` |
| 28 | `06_OPTICAL_MODALITY_FAMILIES.tex` | Cross-Family Interpretation Boundary | `background_foundations` | 80 | `merge` | A single unheaded closing synthesis can retain the boundary and residual evidence while improving pace. | Preserve that counts do not rank modalities and that task, signal path, active constraint, and validation must align for numerical transfer. | `not_implemented` / `pending_author_review` |
| 29 | `07_INTEGRATION_ARCHITECTURES.tex` | INTEGRATION ARCHITECTURES AND RESOURCE COUPLING | `integration_design` | 137 | `add_figure` | An architecture map should show coupling locations and overlaps rather than a misleading exclusive bar chart. | Keep 118 resource, 117 hardware, 113 waveform, 87 link/channel, 72 joint design, 49 carrier, 46 application, 3 mixed, none unresolved; mark all as multi-label and non-hierarchical. | `not_implemented` / `pending_author_review` |
| 30 | `07_INTEGRATION_ARCHITECTURES.tex` | Shared Hardware, Carrier, and Link | `integration_design` | 233 | `retain` | The prose remains mechanism-led and conditional rather than enumerating all studies. | Preserve hardware-versus-carrier distinction, transferred constraints, and four representative citations across three physical regimes. | `not_implemented` / `pending_author_review` |
| 31 | `07_INTEGRATION_ARCHITECTURES.tex` | Shared Waveforms | `integration_design` | 191 | `retain` | The section performs the correct conceptual work and ends with the evidence question that Metrics later answers. | Retain pilot, embedded waveform, and visible-light examples; keep concurrency and matched-condition validation separate from the waveform-sharing label. | `not_implemented` / `pending_author_review` |
| 32 | `07_INTEGRATION_ARCHITECTURES.tex` | Resource Allocation and Joint Design | `tradeoff_optimization` | 217 | `add_citations` | A few additional anchors from fiber, FSO, VLC/LiFi, and photonic-THz would demonstrate transfer boundaries without creating a catalogue. | Keep resource-specific mechanisms, the distinction among weighted models, sweeps, and feasible points, no global-optimum inference, and add only source-verified representative citations. | `not_implemented` / `pending_author_review` |
| 33 | `07_INTEGRATION_ARCHITECTURES.tex` | Application-Level Coupling and Boundary Cases | `background_foundations` | 138 | `retain` | The broad edge is necessary for explaining the review's inclusive eligibility without weakening technical labels. | Preserve the shared-application non-waveform rule, three mixed cases and citations, segment attribution, and no quality penalty. | `not_implemented` / `pending_author_review` |
| 34 | `07_INTEGRATION_ARCHITECTURES.tex` | What the Integration Counts Mean | `integration_design` | 83 | `merge` | Removing the heading and retaining the paragraph as the section close will improve flow without losing content. | Keep the descriptive-not-hierarchical rule and the coherence, interference, synchronization, dynamic-range, and failure-coupling implications. | `not_implemented` / `pending_author_review` |
| 35 | `08_METRICS_AND_COMPARISON_LOGIC.tex` | METRICS AND COMPARISON LOGIC | `metrics_performance_comparison` | 228 | `add_table` | A metric-contract table will let later prose explain boundary cases while improving study-level evidence visibility. | Reconcile 4,779 records; sensing 203 studies/1,816 records, communication 194/1,328, joint 158/870, implementation 64/476; keep all coverage multi-label and non-ranking. | `not_implemented` / `pending_author_review` |
| 36 | `08_METRICS_AND_COMPARISON_LOGIC.tex` | From Reported Quantity to Comparable Observation | `metrics_performance_comparison` | 185 | `merge` | Folding the irreducible rules into the section opening and proposed metric table will remove a repeated abstract framework layer. | Preserve task/definition/plane/condition/validation/provenance, matched operating-point requirement, stated-versus-tabulated origin, and the no-digitization/no-derived-value statement. | `not_implemented` / `pending_author_review` |
| 37 | `08_METRICS_AND_COMPARISON_LOGIC.tex` | Communication Metrics | `metrics_performance_comparison` | 335 | `retain` | The prose supplies the conditional interpretation and cross-plane distinctions that a table cannot fully explain. | Keep gross/net/aggregate distinctions, pre/post-FEC and event differences, optical/electrical/digital SNR separation, geometry/latency boundaries, and all five citations. | `not_implemented` / `pending_author_review` |
| 38 | `08_METRICS_AND_COMPARISON_LOGIC.tex` | Sensing Metrics | `metrics_performance_comparison` | 289 | `retain` | The section preserves task semantics and avoids a universal accuracy scale. | Retain resolution-versus-error/bound distinctions, distribution summaries, dataset/threshold/ground-truth conditions, and all five representative citations. | `not_implemented` / `pending_author_review` |
| 39 | `08_METRICS_AND_COMPARISON_LOGIC.tex` | Joint and Implementation Metrics | `metrics_performance_comparison` | 205 | `retain` | This unit bridges metric semantics to the practical joint outcomes synthesized in Trade-offs and Validation. | Keep the pilot-deviation proxy boundary, weighted-objective non-universality, implementation constraints, and five source citations. | `not_implemented` / `pending_author_review` |
| 40 | `08_METRICS_AND_COMPARISON_LOGIC.tex` | Applying Measurement Planes | `taxonomy_framework` | 146 | `merge` | The unique multisegment example should be folded into Joint Metrics or the metric table, while the repeated plane definitions remain in Section 3. | Do not lose the fast-swept photonic-THz citation, multisegment chain rule, or the prohibition on crossing planes by unit matching. | `not_implemented` / `pending_author_review` |
| 41 | `08_METRICS_AND_COMPARISON_LOGIC.tex` | When Is Cross-Study Numerical Comparison Admissible? | `metrics_performance_comparison` | 229 | `retain` | This empirical endpoint justifies the narrative comparison strategy and prevents a fabricated cross-platform leaderboard. | Keep 118 conditional and 4,661 no among 4,779 records, approximately 2.5/97.5 percent, no unconditional category, no pooling/ranking, and explicit held-constant/different conditions. | `not_implemented` / `pending_author_review` |
| 42 | `09_COMMUNICATION_SENSING_TRADEOFFS.tex` | COMMUNICATION--SENSING TRADE-OFFS | `tradeoff_optimization` | 235 | `add_figure` | A mechanism-family figure can show record/study coverage and conditional share without visualizing incompatible effect magnitudes. | Reconcile 404 coded rows, 2 absence sentinels, 402 substantive records from 168 studies, 218 quantitative, 184 qualitative, 371 conditional; prohibit summing study counts or interpreting frequency as strength. | `not_implemented` / `pending_author_review` |
| 43 | `09_COMMUNICATION_SENSING_TRADEOFFS.tex` | Bandwidth, Spectrum, and Resource Allocation | `tradeoff_optimization` | 145 | `retain` | The concise mechanism-led section gives the largest family enough evidence without turning into a ledger dump. | Keep 95 records/71 studies, 50 quantitative/45 qualitative, 90 conditional, all three citations, and the prohibition on one generic overhead variable. | `not_implemented` / `pending_author_review` |
| 44 | `09_COMMUNICATION_SENSING_TRADEOFFS.tex` | Power, Energy, and Dynamic Range | `tradeoff_optimization` | 168 | `retain` | The section states a transferable mechanism while preserving non-transferable numerical exchange rates. | Keep 90 records/64 studies, 50 quantitative/40 qualitative, 81 conditional, the separate-function prototype caveat, and both source citations. | `not_implemented` / `pending_author_review` |
| 45 | `09_COMMUNICATION_SENSING_TRADEOFFS.tex` | Communication Reliability and Sensing Quality | `tradeoff_optimization` | 137 | `retain` | It moves from resource controls to their coupled communication and sensing outcomes. | Keep 59 records/48 studies, 37 quantitative/22 qualitative, 55 conditional, both citations, and the remove-avoidable-coupling-before-accepting-loss inference. | `not_implemented` / `pending_author_review` |
| 46 | `09_COMMUNICATION_SENSING_TRADEOFFS.tex` | Rate, Resolution, Accuracy, and Range | `tradeoff_optimization` | 248 | `retain` | Preserving the three branches prevents the headline ISAC trope from erasing task and mechanism differences. | Keep all three family counts and conditional shares, six citations, metric/geometry distinctions, and no cross-platform frontier inference. | `not_implemented` / `pending_author_review` |
| 47 | `09_COMMUNICATION_SENSING_TRADEOFFS.tex` | Waveform, Hardware, and Complexity | `tradeoff_optimization` | 125 | `add_citations` | Adding a small set of source-verified prototype examples will show that complexity migrates differently across hardware and DSP chains. | Keep 21 records/20 studies, 6 quantitative/15 qualitative, all conditional, separate burden dimensions, and add citations without inventing cost comparisons. | `not_implemented` / `pending_author_review` |
| 48 | `09_COMMUNICATION_SENSING_TRADEOFFS.tex` | Long-Tail Relationships and the Frontier Boundary | `background_foundations` | 235 | `trim` | Keep the rare-category evidence and one concise frontier boundary, then move promptly to validation. | Preserve 19/15 other records/studies, 9/7 partial relationships, one security and one synergy record, their conditional shares, and the 402-record non-effect boundary. | `not_implemented` / `pending_author_review` |
| 49 | `10_VALIDATION_AND_REPRODUCIBILITY.tex` | VALIDATION AND REPRODUCIBILITY | `validation_experiment_reproducibility` | 86 | `retain` | This section is the proper home for detailed validation and reproducibility synthesis. | Keep strongest-setting versus method versus paired-function distinctions and define reconstruction as configuration plus evaluation contract. | `not_implemented` / `pending_author_review` |
| 50 | `10_VALIDATION_AND_REPRODUCIBILITY.tex` | Maximum Validation Maturity | `validation_experiment_reproducibility` | 198 | `add_figure` | A simple tier distribution will make 206-study reconciliation and the operational evidence gap visible; captions can state that tiers are not quality ranks. | Keep 32/18/78/66/12 = 206, 156 at least laboratory, 12 field, all representative citations, and the rule that maximum tier does not measure condition coverage or paired functions. | `not_implemented` / `pending_author_review` |
| 51 | `10_VALIDATION_AND_REPRODUCIBILITY.tex` | Validation Methods and Operating Realism | `methods_review_protocol` | 224 | `retain` | The unit is needed to prevent a maximum-tier chart from being read as the entire validation history. | Keep 131 analytical, 14 numerical, 104 simulation, 13 dataset, 148 laboratory, 83 prototype, 12 field, 33 mixed, none unclear; preserve modality-specific realism fields and no automatic rigor hierarchy. | `not_implemented` / `pending_author_review` |
| 52 | `10_VALIDATION_AND_REPRODUCIBILITY.tex` | Maximum Tier Versus Paired-Function Evidence | `validation_experiment_reproducibility` | 148 | `retain` | Paired-function validation is a scientifically distinct result and directly supports the central end-to-end evidence gap. | Keep TQAF validation 32/168/6, all 12 at maximum field tier, only 6 satisfying paired-function field evidence, the fiber example citation, and no component-to-system maturity transfer. | `not_implemented` / `pending_author_review` |
| 53 | `10_VALIDATION_AND_REPRODUCIBILITY.tex` | Reported Artifacts and Reconstructability | `validation_experiment_reproducibility` | 235 | `add_table` | A data-versus-code availability table can show counts, percentages, meaning, and audit limits while retaining reconstruction guidance in prose. | Reconcile data 145/41/13/7 = 206, code 197/7/1/1 = 206, reproducibility 4/199/3, preserve unavailable-or-unreported wording, no universal link tests or execution claims, and all five citations. | `not_implemented` / `pending_author_review` |
| 54 | `10_VALIDATION_AND_REPRODUCIBILITY.tex` | Benchmark Readiness and the Validation Contract | `validation_experiment_reproducibility` | 225 | `retain` | This is the validation section's necessary synthesis and should remain the premise, not a duplicate, of the later roadmap. | Keep benchmark readiness 0 strong/48 low/158 adequate, every conjunctive requirement, modality-aware packages, concurrent/offline distinction, and no causal interpretation of artifacts, tier, or performance. | `not_implemented` / `pending_author_review` |
| 55 | `11_TECHNOLOGIES_APPLICATIONS_6G.tex` | ENABLING TECHNOLOGIES, APPLICATIONS, AND 6G POSITIONING | `application_use_case` | 76 | `add_figure` | A cross-layer map can show where technologies act and how application requirements feed constraints back without implying a linear maturity pipeline. | The figure must separate generation/transport, observables, spatial control, inference, application requirements, and 6G/network evidence; mark all technology and application labels multi-label. | `not_implemented` / `pending_author_review` |
| 56 | `11_TECHNOLOGIES_APPLICATIONS_6G.tex` | From Shared Samples to Physical Observables | `technology_enabler` | 327 | `retain` | The section explains stacked technology interfaces and active constraints rather than reciting frequencies. | Keep 68 photonic generation, 66 chirped, 64 coherent, 56 OFDM counts as overlapping; preserve RF-path boundary, interface budgets, and four source citations. | `not_implemented` / `pending_author_review` |
| 57 | `11_TECHNOLOGIES_APPLICATIONS_6G.tex` | Spatial Control, Coverage, and Multiplicity | `technology_enabler` | 223 | `retain` | This is a concise spatial synthesis with appropriate evidence and transfer limits. | Keep 13 beamforming, 11 OPA, 7 MIMO, 2 RIS/ORIS as overlapping; preserve independent-dimension/calibration conditions and all six citations. | `not_implemented` / `pending_author_review` |
| 58 | `11_TECHNOLOGIES_APPLICATIONS_6G.tex` | Integration, Distributed Infrastructure, and Intelligence | `technology_enabler` | 304 | `retain` | The section earns its length by distinguishing mechanism layers and refusing a shared accuracy scale. | Keep 20 photonic integration, 22 DAS, 20 ML/AI, 2 digital twin, 19 other as overlapping; preserve task-specific baseline and shift conditions plus seven citations. | `not_implemented` / `pending_author_review` |
| 59 | `11_TECHNOLOGIES_APPLICATIONS_6G.tex` | Applications as Operating-Requirement Bundles | `application_use_case` | 329 | `add_table` | An application-to-requirement matrix can map target, communication role, geometry, update/latency, safety, and representative evidence without ranking markets. | Retain every application count, multi-label/non-market warning, target and communication-role conditions, and all twelve cited examples; do not sum categories. | `not_implemented` / `pending_author_review` |
| 60 | `11_TECHNOLOGIES_APPLICATIONS_6G.tex` | What the 6G Label Does---and Does Not---Establish | `technology_enabler` | 227 | `retain` | The unit limits a potentially promotional label and establishes the premise for the network-evidence discussion. | Keep 138 direct, 64 inferential, 1 weak, 3 not applicable = 206, all six citations, and explicit non-claims about standard compliance, conformance, adoption, interoperability, and readiness. | `not_implemented` / `pending_author_review` |
| 61 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | DISCUSSION, RESEARCH ROADMAP, AND LIMITATIONS | `methods_review_protocol` | 0 | `rewrite_transition` | A short bridge should state that the section separates what the evidence supports, what experiment is next, and what the review itself cannot establish. | Do not repeat corpus counts or methods; preserve the three distinct reader jobs of interpretation, roadmap, and limitations. | `not_implemented` / `pending_author_review` |
| 62 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | Cross-Cutting Interpretation | `lessons_learned_discussion` | 324 | `add_citations` | A small set of representative anchors and internal section references can show which evidence supports each field-level inference without turning Discussion into a catalogue. | Keep shared-engineering-problem framing, non-hierarchical integration, measurement/condition boundary, no universal frontier, complete-chain maturity gap; add only source-verified anchors and result-section references. | `not_implemented` / `pending_author_review` |
| 63 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | From 6G Framing to Network Evidence | `lessons_learned_discussion` | 113 | `expand` | A concise expansion should distinguish access/fronthaul/transport roles and cite the strongest available network-scale examples and missing interfaces. | Retain ITU-R IMT-2030 framing, no standard/conformance inference, and add only studies with explicit end-to-end network roles; do not infer readiness from component feasibility. | `not_implemented` / `pending_author_review` |
| 64 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | Research Roadmap | `methods_review_protocol` | 0 | `add_table` | A single roadmap table can integrate evidence gap, action, modality-specific test, success criterion, and dependency while reducing heading fragmentation. | Every roadmap row must trace to a result in Metrics, Trade-offs, Validation, or Technologies; preserve modality-specific physics and avoid claims that the review tested proposed interventions. | `not_implemented` / `pending_author_review` |
| 65 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | Make the measurement contract routine | `metrics_performance_comparison` | 96 | `merge` | Convert it into the measurement-contract row of the roadmap table, referencing rather than restating the full framework. | Keep task, plane, unit, target/channel, condition, baseline, validation, all named distinction examples, and independently reconstructable-record success criterion. | `not_implemented` / `pending_author_review` |
| 66 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | Build modality-aware benchmarks | `validation_experiment_reproducibility` | 86 | `merge` | Place it in the roadmap table with explicit dependencies and modality columns instead of expanding prose. | Preserve fiber, FSO, VLC/LiFi, and photonic-THz scenario fields, common task/calibration, independent multi-group test, and no identical-absolute-value requirement. | `not_implemented` / `pending_author_review` |
| 67 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | Test joint operation under realistic disturbance | `lessons_learned_discussion` | 110 | `merge` | A roadmap-table row can expose the dependency chain and retain modality-specific disturbance examples compactly. | Keep both functions at every operating point, listed resource types, meaningful single-function baselines, modality-specific disturbances, and repeatable limiting-mechanism criterion. | `not_implemented` / `pending_author_review` |
| 68 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | Release the artifacts that define the experiment | `validation_experiment_reproducibility` | 87 | `merge` | Place the required package and external rerun criterion in the roadmap table, linking back to artifact results rather than re-explaining them. | Keep raw/minimally processed data, generation/receiver/estimator code, hardware settings, calibration, machine-readable metrics, persistent/versioned releases, and independent rerun under a new condition. | `not_implemented` / `pending_author_review` |
| 69 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | Evaluate intelligence, scale, and security as system properties | `technology_enabler` | 86 | `merge` | A final roadmap-table row can separate evaluation dimensions and link them to technology, application, and network evidence. | Keep train/calibration shift, adversarial interference, safe fallback, control overhead, latency, compute/energy, multi-user effects, wrong-decision consequence, and explainable degradation as the success criterion. | `not_implemented` / `pending_author_review` |
| 70 | `12_DISCUSSION_ROADMAP_LIMITATIONS.tex` | Limitations of This Review | `limitations` | 301 | `retain` | These limitations are necessary to prevent the systematic-review apparatus and 206-study corpus from implying stronger inference than executed. | Keep six-source English window, 58 unretrieved, two incomplete export mappings, retrospective OSF, no routine independent duplicate review, nonvalidated TQAF, no GRADE/bias/sensitivity/meta-analysis/causal moderators, judgment dependence, 92 unresolved-condition rows, artifact-audit limits, and no worldwide prevalence inference. | `not_implemented` / `pending_author_review` |
| 71 | `13_CONCLUSION.tex` | CONCLUSION | `conclusion` | 240 | `retain` | The three-paragraph problem–finding–action structure gives closure without returning to PRISMA or governance detail. | Do not add new evidence or ranking claims; retain family-of-systems framing, no universal frontier, sparse paired field/reusable benchmark evidence, modality-aware measurement contracts, joint disturbance tests, and reusable artifacts. | `not_implemented` / `pending_author_review` |

## 10. Reproducibility ve Dosya Otoritesi

- Canonical close-read masters: `data/comst_*_close_read_master.csv`.
- Common-engine numeric masters: `data/comst_*_harmonized_master.csv`.
- Corpus statistics: `data/paper_*`, `data/role_*`, `data/visual_*`, `data/transition_comparison_final.csv`.
- O-ISAC comparison and decisions: `data/oisac_vs_comst_paper_metrics.csv`, `data/oisac_unit_role_benchmarks.csv`, `data/oisac_decision_crosswalk_final.csv`, `data/oisac_visual_plan.csv`.
- Reliability: `data/reliability_statistics.csv`, contingency, missingness, disagreements and adjudication outputs.
- The active manuscript remained unchanged during almanac construction.
