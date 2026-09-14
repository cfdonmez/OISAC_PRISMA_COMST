# PRISMA 2020 Madde–Artefakt–Manuscript Uyum Matrisi

Oluşturma: 2026-08-05  
Son güncelleme: 2026-08-07 — OSF `7f6wb` retrospektif kayıt soy hattı Madde 24a/24c ve A12'ye işlendi  
Kapsam: O-ISAC systematic review, 206 çalışma / 227 uygun rapor  
Durum: Çalışma matrisi; nihai gönderim checklist'i değildir

## Koruma ve kullanım kuralı

- Kaynak `PRISMA_2020_kontrol_listesi_TR.md` değiştirilmemiştir.
- Bu matris, eldeki kanıt artefaktı ile aktif manuscript'e gerçekten aktarılmış raporu birbirinden ayırır.
- `HAZIR`, ilgili kanıtın veya yazım paketinin var olduğunu gösterir; nihai PRISMA kutusunun işaretlenebileceği anlamına gelmez.
- Nihai kutu ancak metin aktif manuscript'e aktarıldıktan, ek/şekil/atıf bağlantıları çözüldükten ve sayfa/bölüm referansı yazıldıktan sonra kapatılır.
- Aktif manuscript bu denetimde değiştirilmemiş ve LaTeX derlemesi yapılmamıştır.

## Durum sözlüğü

| Durum | Anlam |
|---|---|
| `HAZIR` | Kanonik kanıt ve manuscript-ready içerik mevcut. |
| `KISMİ` | Esas kanıt mevcut; açıklama, ek dosya, şekil, atıf veya erişim bağlantısı eksik. |
| `AÇIK` | Gereken değerlendirme/beyan henüz yok veya kullanıcı kararı gerekiyor. |
| `UYGULANMAZ—GEREKÇELİ` | Review tasarımı nedeniyle uygulanmıyor; açık gerekçe manuscript'e yazılmalı. |
| `AKTARILMADI` | Phase-G metni korunan aktif manuscript'e henüz entegre edilmedi. |

## Kanonik yol kısaltmaları

- `C`: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_flow_PHASE_C_FINAL_2026-07-30/`
- `D`: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_survey_ready_2026-08-04/`
- `E`: `systematic_review_workflow/05_kalite_kanit/`
- `F`: `systematic_review_workflow/06_sentez/outputs/phase_f_s1_s7_2026-08-04/`
- `G`: `systematic_review_workflow/07_raporlama/outputs/phase_g_writing_package_2026-08-04/`
- `P`: `systematic_review_workflow/01_protokol/`

## Özet durum

| Artefakt durumu | Madde sayısı |
|---|---:|
| `HAZIR` | 16 |
| `KISMİ` | 20 |
| `UYGULANMAZ—GEREKÇELİ` | 4 |
| `AÇIK` | 2 |
| **Toplam** | **42** |

Aktif manuscript entegrasyonu bu matrisin tüm satırlarında `AKTARILMADI` durumundadır. Bu nedenle nihai PRISMA checklist'inde henüz hiçbir satır otomatik olarak kapatılmamalıdır.

## 42 maddelik uyum matrisi

| Madde | Artefakt | Kapanış türü | Kanıt ve kalan iş | Aktif manuscript |
|---|---|---|---|---|
| 1 | `HAZIR` | Mevcut metin | Kanonik başlık systematic review türünü açıkça belirtiyor; aktif `.tex` dosyasındaki placeholder başlık değiştirilmeden korunuyor. | `AKTARILMADI` |
| 2 | `KISMİ` | Metin | `G/09_ABSTRACT_206_EN.tex` amaç, yöntem özeti, corpus ve ana sonuçları içeriyor. Başlıca uygunluk ölçütleri, altı kaynağın adı/son arama tarihi, TQAF yöntemi ve kayıt durumu tamamlanmalı. Funding beyanı 2026-08-06 tarihinde kapatıldı. Aşağıdaki PRISMA Abstracts alt matrisi paket düzeyinde 8 hazır ve 4 kısmi alt kalem gösteriyor. | `AKTARILMADI` |
| 3 | `HAZIR` | Mevcut metin | `P/01_protokol_sablonu.md` ve Phase-G Discussion; bilgi boşluğu ve review gerekçesi hazır. | `AKTARILMADI` |
| 4 | `HAZIR` | Mevcut metin | PCC tabanlı ana soru ile RQ1–RQ7 protokol ve proje bağlamında açık. | `AKTARILMADI` |
| 5 | `HAZIR` | Mevcut metin | `G/01_METHODS_PRISMA_206_EN.tex`; dahil/dışlama, rapor özellikleri ve S1–S7 sentez grupları tanımlı. Gerçek cutoff 22 Haziran 2026. | `AKTARILMADI` |
| 6 | `HAZIR` | Mevcut metin | Altı bilgi kaynağı/platform ve 22 Haziran 2026 son arama tarihi Methods'ta mevcut. | `AKTARILMADI` |
| 7 | `KISMİ` | Dürüstlük açıklaması + ek tablo | Kaynak bazlı strateji kayıtları var. İki düşük getirili Taylor & Francis export'unun tam sorgu eşlemesi audit trail'den yeniden kurulamıyor; sorgu uydurulmadan açıkça belirtilmeli. | `AKTARILMADI` |
| 8 | `KISMİ` | Yöntem metni | Gerçek süreç investigator-supervised, AI-assisted, user-delegated ve claim-governed. Aşama bazlı değerlendirici sayısı, bağımsızlık yokluğu, uyuşmazlık çözümü ve araç/sürüm kaydı açık yazılmalı. | `AKTARILMADI` |
| 9 | `KISMİ` | Yöntem metni; author-contact sonucu doğrulandı | Study/report/claim düzeyinde extraction, provenance, QA ve çoklu rapor lineage hazır. Bağımsız çift insan extraction yapılmadığı açık yazılmalı. Kullanıcı 2026-08-06 tarihinde dahil çalışma yazarlarıyla temas kurulmadığını; haftalık toplantıların survey ekibi içinde sözlü yöntem tartışması/doğrulaması olduğunu teyit etti. | `AKTARILMADI` |
| 10a | `HAZIR` | Mevcut metin | Metrik, koşul, validation, trade-off ve claim-use seçim kuralları `G/01_METHODS...` ve `G/03_CLAIM_GOVERNANCE_EN.tex` içinde tanımlı. | `AKTARILMADI` |
| 10b | `HAZIR` | Mevcut metin | Bibliyografik, mimari, modality, sensing/communication, validation, application, availability ve missingness değişkenleri tanımlı. | `AKTARILMADI` |
| 11 | `KISMİ` | Terminoloji ve yöntem düzeltmesi | 206 study-level, sekiz boyutlu TQAF kaydı var. TQAF'ın doğrulanmış klasik risk-of-bias aracı değil, review-specific teknik kanıt/raporlama appraisal'ı olduğu; sürümü ve insan/AI süreci açık yazılmalı. | `AKTARILMADI` |
| 12 | `KISMİ` | Gerekçeli yöntem metni | Kaynak metrikleri, birimler, measurement plane ve koşullar korunuyor. Ortak effect measure, standardize dönüşüm ve pooling kullanılmadığı açıkça belirtilmeli. | `AKTARILMADI` |
| 13a | `HAZIR` | Mevcut metin | S1–S7 üyeliği, primary/context/quarantine ve karşılaştırılabilirlik kapıları açık. | `AKTARILMADI` |
| 13b | `HAZIR` | Mevcut metin | Eksik değerler uydurulmadı; graph digitization ve yeni performans değeri üretimi yapılmadı; çelişkili değerler ortalanmadı. | `AKTARILMADI` |
| 13c | `KISMİ` | Sunum yöntemi metni | 206-study appendix ve sentez tabloları mevcut. Study/report denominator, multi-label sayımlar ve neden forest/funnel plot üretilmediği Methods'ta açıklaştırılmalı. | `AKTARILMADI` |
| 13d | `HAZIR` | Mevcut metin | Heterojen engineering corpus nedeniyle meta-analysis yapılmaması ve structured descriptive/taxonomy/metric-governed narrative synthesis gerekçesi hazır. | `AKTARILMADI` |
| 13e | `KISMİ` | Heterojenlik yöntemi metni | Modality, architecture, metric, plane, scenario ve validation strata kullanıldı. Bunlar açıkça descriptive heterogeneity investigation olarak çerçevelenmeli; I²/meta-regression uygulanmadığı belirtilmeli. | `AKTARILMADI` |
| 13f | `UYGULANMAZ—GEREKÇELİ` | N/A cümlesi | Pooled veya model-dependent ana sonuç olmadığı için review-level sensitivity analysis uygulanmadı. QA/invariance kontrolleri sensitivity analysis diye sunulmamalı. | `AKTARILMADI` |
| 14 | `AÇIK` | Sınırlılık/gerekçe metni | Formal missing-results/publication/selective-outcome bias aracı uygulanmadı. TQAF reporting completeness bunun eşdeğeri değildir. Uygulanamama nedeni ve kalan belirsizlik açık raporlanmalı. | `AKTARILMADI` |
| 15 | `KISMİ` | Algoritma düzeltmesi | `E/certainty_grade.csv` içinde 115 evidence body var. Methods'taki “core dimensions” ifadesi gerçek kodla uyumsuz; kararlar sekiz TQAF boyutunun tamamına dayanıyor. Exact eşikler ve “not GRADE” sınırı eklenmeli. | `AKTARILMADI` |
| 16a | `KISMİ` | Şekil entegrasyonu | `C` içinde kilitli PRISMA akışı ve sayılar tamam: 1,733 identified; 1,259 screened; 330 sought; 58 not retrieved; 272 assessed; 227 included reports; 206 studies. Phase-G'de şekil marker'ı gerçek şekille değiştirilmemiş. | `AKTARILMADI` |
| 16b | `KISMİ` | Ek tablo + pointer | `C/FULL_TEXT_EXCLUSIONS_39_PRISMA16B_FINAL_2026-07-30.csv` 39/39 citation, tek ana neden ve evidence note içeriyor. Makalede bireysel listeye supplement pointer gerekli. | `AKTARILMADI` |
| 17 | `KISMİ` | Atıf çözümü + ek tablo | `G/11_INCLUDED_STUDIES_206.tex` 206 study row ve 227-report lineage içeriyor; 206 kaydın bibliography/citation key çözümü henüz tamam değil. | `AKTARILMADI` |
| 18 | `UYGULANMAZ—GEREKÇELİ` | Alternatif appraisal + açık sınır | Conventional study-level risk-of-bias assessment yapılmadı. `E/risk_of_bias.csv` içindeki 206 satır review-specific TQAF sonuçlarıdır; publication-facing ad “study-level TQAF” olmalı ve RoB sonucu gibi sunulmamalı. Gerekçe manuscript'te yazılmalı ve TQAF ayrı supplement'te gösterilmelidir. | `AKTARILMADI` |
| 19 | `KISMİ` | Supplement export + pointer | `D/OISAC_PHASE_D_SURVEY_READY_2026-08-04.xlsx`, `04_METRIC_RESULTS` sayfasında 4,861 metric-result row ve study/report ID, metric, değer/birim, plane, koşul, validation, uncertainty ve source locator alanları doğrulandı. Yayına dönük study-level supplement/pointer eksik. | `AKTARILMADI` |
| 20a | `KISMİ` | Birleşik sentez tablosu | `E/synthesis_matrix_PHASE_E_2026-08-04.csv`, `E/certainty_grade.csv` ve `F` contributor/characteristic verisini içeriyor. Her S1–S7 body için contributor + characteristics + TQAF + certainty tek yayımlanabilir tabloda birleştirilmeli. | `AKTARILMADI` |
| 20b | `UYGULANMAZ—GEREKÇELİ` | N/A cümlesi | Effect-size meta-analysis veya model-based statistical synthesis yapılmadı; pooled estimate, CI ve statistical heterogeneity ölçüsü uygulanmaz. Descriptive counts/proportions ayrıca raporlanıyor. | `AKTARILMADI` |
| 20c | `KISMİ` | Sonuç çerçeveleme metni | Heterojenlik modality, architecture, metric/role, measurement plane, scenario ve validation tier boyunca descriptively haritalandı; causal moderator testi yapılmadığı açık yazılmalı. | `AKTARILMADI` |
| 20d | `UYGULANMAZ—GEREKÇELİ` | N/A cümlesi | Pooled model veya evrensel performans sıralaması bulunmadığı için pooled-result sensitivity analysis uygulanmaz. | `AKTARILMADI` |
| 21 | `AÇIK` | Sonuç sınırlılığı metni | Formal missing-results/reporting-bias assessment sonucu yok. Corpus'un harmonized prespecified outcome set ve çoğu çalışma için erişilebilir protocol/analysis plan içermediği; bias'ın dışlanamayacağı açık yazılmalı. | `AKTARILMADI` |
| 22 | `KISMİ` | Body-level supplement + pointer | `E/certainty_grade.csv` 115 body içeriyor: 54 high, 47 moderate, 10 limited, 4 unclear. Makalede aggregate sonuç var; her body'nin rating/contributor kaydı ek dosyada gösterilmeli. | `AKTARILMADI` |
| 23a | `KISMİ` | Doğrulanmış dış atıf | Phase-G Discussion corpus içi yorumları içeriyor. Önceki O-ISAC reviews ve broader ISAC literature ile doğrulanmış citation'lı karşılaştırma eksik; atıf uydurulmamalı. | `AKTARILMADI` |
| 23b | `HAZIR` | Mevcut metin | Metric comparability, validation, reproducibility, benchmark readiness ve claim restrictions sınırlılıkları tartışılmış. | `AKTARILMADI` |
| 23c | `HAZIR` | Mevcut metin | AI-assisted provenance, routine independent duplicate human review yokluğu ve olası etkisi açık. | `AKTARILMADI` |
| 23d | `KISMİ` | Policy/standards cümlesi | Practice ve future-research roadmap güçlü. Standards bodies, funders ve 6G programme coordinators için açık politika/standart etkisi eklenmeli. | `AKTARILMADI` |
| 24a | `HAZIR` | Doğrulanmış retrospektif kayıt metni | Review 12 Şubat 2026'da OSF `7f6wb` üzerinde retrospektif olarak kaydedildi (DOI `10.17605/OSF.IO/7F6WB`). Kayıt sırasında search/screening tamamlanmış ve synthesis/manuscript drafting başlamıştı; prospective preregistration iddiası kurulmayacak. | `AKTARILMADI` |
| 24b | `KISMİ` | Public erişim bağlantısı | Internal versioned protocol, decision log ve amendment var. Okuyucuya açık supplement/repository URL veya DOI henüz yok. | `AKTARILMADI` |
| 24c | `HAZIR` | Dated registration-lineage amendment | `P/04_protocol_registration_lineage_correction_2026-08-07.md`, OSF'deki 221-study predecessor snapshot ile 206-study final execution arasındaki kaynak, cutoff, denominator, reviewer, appraisal ve bias/sensitivity sapmalarını; nedenleri ve raporlama etkileriyle açıkça belgeler. | `AKTARILMADI` |
| 25 | `HAZIR` | Kullanıcı/yazar beyanı alındı | Kullanıcı 2026-08-06 tarihinde review için finansal veya finansal olmayan destek alınmadığını doğruladı. Hazır metin: “This review received no specific financial or non-financial support. No funder or sponsor had any role in the design, conduct, analysis, interpretation, manuscript preparation, or decision to submit.” | `AKTARILMADI` |
| 26 | `HAZIR` | Kullanıcı/yazar beyanı alındı | Kullanıcı 2026-08-06 tarihinde review yazarları için çıkar çatışması bulunmadığını doğruladı. Hazır metin: “The authors declare no competing interests.” | `AKTARILMADI` |
| 27 | `KISMİ` | Repository kararı + erişim metni | Protocol, logs, ledgers, extraction, TQAF, synthesis ve QA/code artefaktları mevcut; fakat persistent public URL/DOI, release/tag, license, açık kapsam ve restricted-material koşulları belirlenmedi. Publisher PDF'leri yeniden dağıtılmamalı. | `AKTARILMADI` |

## Madde 2 alt denetimi — PRISMA for Abstracts

| Alt kalem | Paket durumu | Kanıt / kalan iş | Aktif manuscript |
|---|---|---|---|
| A1 — Title | `HAZIR` | Kanonik başlık review türünü tanımlıyor; aktif manuscript başlığı placeholder. | `AKTARILMADI` |
| A2 — Objectives | `HAZIR` | Amaç ve yaklaşım `G/09_ABSTRACT_206_EN.tex` içinde. | `AKTARILMADI` |
| A3 — Eligibility criteria | `KISMİ` | Tarih aralığı var; başlıca inclusion/exclusion ölçütleri abstract'a eklenmeli. | `AKTARILMADI` |
| A4 — Information sources | `KISMİ` | Cutoff var; altı kaynak/platform adı ve last-search ifadesi eklenmeli. | `AKTARILMADI` |
| A5 — Appraisal method | `KISMİ` | Aggregate appraisal sonucu var; sekiz-boyutlu review-specific TQAF yöntemi ve conventional RoB olmadığı eklenmeli. | `AKTARILMADI` |
| A6 — Synthesis methods | `HAZIR` | Metric-governed narrative synthesis tanımlı. | `AKTARILMADI` |
| A7 — Included studies | `HAZIR` | 227 eligible reports / 206 studies ve temel özellikler veriliyor. | `AKTARILMADI` |
| A8 — Main results | `HAZIR` | Claim, modality, trade-off, validation ve appraisal sonuçları var; pooled estimate uygulanmaz. | `AKTARILMADI` |
| A9 — Limitations of evidence | `HAZIR` | Field evidence, open artifacts ve benchmark-readiness sınırlılıkları var. | `AKTARILMADI` |
| A10 — Interpretation | `HAZIR` | Genel yorum ve temel implications var. | `AKTARILMADI` |
| A11 — Funding | `HAZIR` | Kullanıcının 2026-08-06 tarihli “destek alınmadı” beyanı İngilizce funding statement'a dönüştürüldü. | `AKTARILMADI` |
| A12 — Registration | `HAZIR` | Kısa metin hazır: “Retrospectively registered on the Open Science Framework (7f6wb; DOI: 10.17605/OSF.IO/7F6WB) on 12 February 2026.” | `AKTARILMADI` |

## Kapanış sırası

1. Dürüstlük ve yöntem metinlerini onayla: 7–9 ve 11–15. Madde 9 author-contact sınırı, Madde 24a/24c registration lineage ve Madde 25–26 beyanları tamamlandı.
2. Yayına dönük supplement'leri üret/isimlendir: 16b–20a ve 22.
3. Doğrulanmış dış atıfları seç: 23a.
4. Public repository/DOI, release ve lisans kararını ver: 24b ve 27.
5. Onaylanan İngilizce parçaları aktif manuscript'e kontrollü biçimde entegre et.
6. PRISMA akış şekli, bibliography, cross-reference ve sayfa/bölüm referanslarını tamamla.
7. Ancak bundan sonra kaynak checklist kopyasında 42 satırı kapat ve Phase-H final QA'ya geç.

## Kritik yorum sınırları

- 227 uygun rapor, 206 dahil çalışma demektir; bu iki denominator birbirinin yerine kullanılmaz.
- TQAF, conventional clinical risk-of-bias veya GRADE değildir; Madde 18 bu nedenle gerekçeli uygulanmaz olarak tutulur ve TQAF ayrı bir teknik appraisal olarak raporlanır.
- User-delegated kararlar, routine independent duplicate human review olarak raporlanmaz.
- Formal reporting-bias assessment yapılmadığı için “bias yoktur” sonucu çıkarılmaz.
- Meta-analysis yapılmadığı için 13f, 20b ve 20d gerekçeli uygulanmazdır; QA/invariance testleri sensitivity analysis değildir.
- Excel'deki `04_METRIC_RESULTS` sayfası Item 19'un altta yatan çalışma düzeyi veri artefaktını karşılar; publication-facing supplement ve manuscript pointer olmadan Item 19 nihai olarak kapanmaz.

## 2026-08-07 public-release staging update

- Items 16b, 17, 19, 20a and 22 now have sanitized publication-facing workbook/CSV artifacts in `07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/`.
- Item 19's public projection contains all 4,861 metric rows plus 3,041 evidence-index rows, 2,559 condition sets, 404 trade-off rows and their claim-use gates; local paths, actor identifiers and long source-derived prose are excluded.
- Item 18 remains `UYGULANMAZ—GEREKÇELİ` for conventional risk of bias; the 206-row TQAF is released separately and must not be called RoB or GRADE.
- Item 21 now has public limitation text, but no formal missing-results-bias assessment exists and manuscript integration remains pending.
- Items 24b and 27 remain open until creator metadata, licenses, a safe package-only GitHub release and Zenodo DOI are finalized.
- Item 24a now reports OSF `7f6wb` as a retrospective registration, not a prospective preregistration. Item 24c is supported by the dated registration-lineage correction amendment.
- The artifact-status totals were recomputed after this correction: 16 `HAZIR`, 20 `KISMİ`, 4 justified non-applicable and 2 open. Active-manuscript integration remains `AKTARILMADI` for all items.
