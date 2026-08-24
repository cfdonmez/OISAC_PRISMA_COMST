# PRISMA 2020 Tam Yeniden Denetimi

Tarih: 2026-08-13  
Aday: `comst_206_v2_9section`  
Sonuç: `NOT_SUBMISSION_READY`

## Denetimin dayanağı

Bu denetim önceki `PASS` etiketlerini devralmadı. Kök dizindeki resmî
`PRISMA_2020_expanded_checklist.pdf` dosyasının 42 madde ve alt maddesi yeniden
okundu. Denetlenen PDF'nin SHA-256 değeri:
`3FD484CD0EB836592011E90DCA78C4811DE7B0674024B6FF597029DD3819E0AA`.
Item 2 ayrıca resmî 12 maddelik PRISMA 2020 for Abstracts checklist'e göre
değerlendirildi.

Bilimsel kapsam, çalışma evreni, sayılar ve sınıflandırmalar için yalnız kilitli
Phase C, D, E ve F artefaktları otorite kabul edildi. Yerel 76 COMST makalesi
yalnız anlatı, bölüm mimarisi ve sunum karşılaştırmasıdır. Bu makaleler O-ISAC
kapsamını, çalışma dahilini, paydayı, PRISMA yükümlülüğünü veya bilimsel sonucu
belirleyemez.

## Dört ayrı durum ekseni

Her PRISMA satırı için aşağıdaki durumlar birbirinden ayrıldı:

1. **Metinde raporlanmış mı?** V2 prose içinde gerçekten yazılı mı?
2. **Artefakt materyalize mi?** Gerçek dosya var mı? Blueprint veya gelecek
   üretim yorumu dosya sayılmaz.
3. **Nihai manuscript pointer var mı?** Aktif şekil, tablo, supplement, protokol
   veya repository işareti var mı?
4. **Kamusal yayın durumu nedir?** Dosya DOI/repository ile gerçekten yayımlı mı?
   `public_release_v1_0_0_staging_2026-08-07` altındaki her şey yalnız draft
   staging'dir ve kamusal yayın sayılmamıştır.

## Sonuç dağılımı

| Durum | Sayı | Anlam |
| --- | ---: | --- |
| `READY` | 9 | Adayda gerekli raporlama ve gerekli destek mevcut. |
| `PARTIAL` | 24 | Esas bilgi var; zorunlu öğe, pointer veya journal artefaktı eksik. |
| `OPEN` | 6 | Temel gereklilik adayda yok veya zorunlu ürün üretilmemiş. |
| `JUSTIFIED_NA` | 3 | Tasarım nedeniyle uygulanmıyor ve neden dürüstçe raporlanıyor. |
| **Toplam** | **42** |  |

Bu dağılım, önceki bütünlük veya regex testlerinin `PASS` olmasının PRISMA
uyumu ya da submission readiness anlamına gelmediğini doğrular.

## PRISMA for Abstracts yeniden denetimi

Mevcut abstract'ın genel durumu `OPEN`'dır: 4 hazır, 3 kısmi, 5 açık alt madde.

| Alt madde | Durum | Bulgular |
| --- | --- | --- |
| A1 Title | `OPEN` | V2 paketinde final manuscript title yok. |
| A2 Objectives | `READY` | Ortak özellikler ve karşılaştırılabilirlik sorusu var. |
| A3 Eligibility | `PARTIAL` | Tarih ve O-ISAC evreni var; peer review, English full technical content, genuine integration ve temel dışlamalar yok. |
| A4 Information sources | `OPEN` | Altı kaynak ve 22 Haziran 2026 son arama tarihi yok. |
| A5 Risk of bias/appraisal | `OPEN` | TQAF ve conventional risk of bias sınırı yok. |
| A6 Synthesis methods | `PARTIAL` | Bulgular var; structured narrative synthesis, metric governance ve no meta-analysis yöntemi yok. |
| A7 Included studies | `READY` | 206 çalışma ve platform aileleri var. |
| A8 Main results | `PARTIAL` | Temel sonuçlar var; ana sonuçların çalışma paydaları tutarlı biçimde ekli değil. |
| A9 Evidence limitations | `READY` | Field evidence ile açık veri/kod eksikliği ve ölçüm bağlamı sınırı var. |
| A10 Interpretation | `READY` | Yorum ölçülü ve platform sıralaması yapmıyor. |
| A11 Funding | `OPEN` | Doğrulanmış no-support beyanı yok. |
| A12 Registration | `OPEN` | Retrospektif OSF kaydı ve numarası yok. |

Abstract düzeltilirken survey mesajı korunmalıdır. PRISMA bilgisi bütün abstract'ı
ele geçirmemeli; fakat altı kaynak ve cutoff, eligibility özeti, gerçek reviewer
modeli, TQAF sınırı, synthesis yöntemi, ana sonuç paydaları, support ve
registration tek bir sıkı yöntem cümle kümesiyle eklenmelidir.

## 42 maddelik dürüst uyum matrisi

Kısaltmalar: `Y` = var, `P` = kısmi, `N` = yok, `DRAFT` = yalnız staging,
`NR` = kamusal yayın gerekmiyor.

| Item | Konu | Prose | Materyalize artefakt | Final pointer | Public/release | Durum | Açık gate / gerekli düzeltme |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Title | N | N | N | NR | `OPEN` | Final driver ve başlık oluşturulmalı; başlık açıkça “systematic review” demeli. Öneri: *Optical Integrated Sensing and Communication for 6G: A Systematic Review and Cross Platform Survey*. |
| 2 | Abstract | P | Y: `sections/00_ABSTRACT.tex` | Y | NR | `OPEN` | A1, A4, A5, A11, A12 kapatılmalı; A3, A6, A8 tamamlanmalı. |
| 3 | Rationale | Y: Introduction | Y: Table I ve prose | Y | NR | `READY` | Mevcut gerekçe korunmalı; COMST korpusu bilimsel karar otoritesi yapılmamalı. |
| 4 | Objectives | P: abstract/introduction | Y: protocol PCC/RQs | P | DRAFT | `PARTIAL` | Açık PCC objective ve bütün RQ'lar eklenmeli veya final protokol pointer verilmelidir. |
| 5 | Eligibility criteria | P: Section III | Y: locked criteria/codes | P | DRAFT | `PARTIAL` | Outcome nonrequirement, 6G wording, tradeoff ve low-quality nonexclusion kuralları ile final criteria pointer eklenmeli. |
| 6 | Information sources | P: six sources/cutoff | Y: search log | N | DRAFT | `PARTIAL` | Kaynak bazında interface, coverage ve last-search-date tablosu materyalize edilip işaretlenmeli. |
| 7 | Search strategy | P | P: source files; two T&F mappings unreconstructable | N | DRAFT | `PARTIAL` | Full source strategies supplementi dondurulmalı; iki Taylor & Francis sorgusu uydurulmadan unmapped export olarak açıklanmalı. |
| 8 | Selection process | P: Section III | Y: locked reviewer process | P | DRAFT | `PARTIAL` | Aşama bazında tek final investigator, independence yokluğu, AI rolü, version rule ve translation boundary açık yazılmalı. |
| 9 | Data collection process | P: Section III | Y: Phase D workbook | P | DRAFT | `PARTIAL` | Tek-investigator AI-assisted extraction, tool/version, validation ve multi-report rule tek yerde tamamlanıp form/codebook pointer verilmelidir. |
| 10a | Outcome data items | P | Y: metrics/tradeoffs | P | DRAFT | `PARTIAL` | Bütün compatible results mi yoksa seçili sonuçlar mı toplandı kilitli talimattan doğrulanıp gerçek seçim kuralı yazılmalıdır. |
| 10b | Other variables | P | Y: codebook | N | DRAFT | `PARTIAL` | Final data dictionary ve `NR/NA/UNC/no inference` kuralları işaretlenmelidir. |
| 11 | Risk of bias methods | P: TQAF var | Y: TQAF files | P | DRAFT | `PARTIAL` | Conventional RoB yapılmadığı açıkça söylenmeli; TQAF yalnız nonvalidated technical appraisal olarak sunulmalı. |
| 12 | Effect measures | Y | Y: metric ledger | Y | NR | `READY` | No common effect measure, no transformation ve no pooling sınırı korunmalı. |
| 13a | Synthesis eligibility | Y | Y: claim-use/restriction | Y | NR | `READY` | Study inclusion ile claim usability ayrımı korunmalı. |
| 13b | Data preparation | Y | Y: origin/conflict fields | Y | NR | `READY` | No digitization, no imputation ve conflict preservation korunmalı. |
| 13c | Tabulation/display | P | P: yalnız locked PRISMA flow gerçek; diğerleri blueprint | P: inactive comments | N | `PARTIAL` | Figure 3, Figure 4 ve Table III dahil gerekli carrier'lar üretilmeli; denominator/multilabel ve no forest/funnel gerekçesi yazılmalı. |
| 13d | Synthesis methods | Y | Y: Phase F | Y | NR | `READY` | Structured, taxonomy based, metric governed narrative synthesis sınırı korunmalı. |
| 13e | Heterogeneity methods | P | Y: normalization/body data | P | DRAFT | `PARTIAL` | Descriptive strata, prespecified/emergent ayrımı ve no statistical heterogeneity/meta-regression açık yazılmalı. |
| 13f | Sensitivity methods | P: yapılmadığı yazılı | N: yapılmadı | P | NR | `PARTIAL` | No pooled/model-dependent result gerekçesi ve QA'nın sensitivity olmadığı eklenirse `JUSTIFIED_NA` olur. |
| 14 | Missing-results bias methods | P: yapılmadığı yazılı | N | P | NR | `PARTIAL` | Neden formal tool/funnel uygulanmadığı ve selective reporting'in unquantified kaldığı açık yazılmalı. |
| 15 | Certainty methods | Y | Y: 115 body outputs | Y | NR | `READY` | Exact rules ve “not GRADE” sınırı korunmalı. |
| 16a | Selection results | Y: exact counts | Y: locked PDF/PNG | N: Figure 3 yalnız comment | DRAFT | `PARTIAL` | Locked flow gerçek figür olarak eklenmeli; 227 reports ve 206 studies ayrı gösterilmeli. |
| 16b | Excluded studies | P: aggregate only | Y: 39-row cited register | N | DRAFT | `PARTIAL` | 39 raporun tam atıf, tek ana neden ve report-specific note içeren supplementi aktif pointer almalı. |
| 17 | Included characteristics | P: aggregate synthesis | P: 206 bib + draft rich inventory | N | DRAFT | `OPEN` | ST-01 materyalize edilmeli; 206/206 çalışma gerçek citation key ile atıflanmalı ve özellikleri gösterilmeli. Yalnız `\nocite{*}` yeterli değildir. |
| 18 | Risk of bias results | P: aggregate TQAF | P: TQAF, conventional RoB değil | N | DRAFT | `PARTIAL` | Conventional RoB yapılmadığı gerekçeli biçimde yazılmalı; 206-row TQAF ayrı adla, rationale ile sunulmalı. |
| 19 | Individual-study results | P: aggregate/examples | Y: 4,861 metric rows | N | DRAFT | `PARTIAL` | 4,861 raw ve 4,779 primary ayrımını koruyan study/report/metric/condition/locator supplementi ve aktif pointer gerekir. |
| 20a | Contributors to syntheses | P | Y: 115 bodies + 4,931 memberships | N | DRAFT | `PARTIAL` | Her evidence body için contributing studies, relevant characteristics, TQAF ve certainty tek reader-facing carrier'da birleştirilmeli. |
| 20b | Statistical synthesis results | Y: yapılmadı ve gerekçe var | N: yapılmadı | Y | NR | `JUSTIFIED_NA` | Descriptive sayılar pooled effect olarak sunulmamalı. |
| 20c | Heterogeneity results | P | Y: subgroup maps | P | DRAFT | `PARTIAL` | Her descriptive stratum contributor'ları işaretlenmeli ve ilişkinin observational/noncausal olduğu açık yazılmalı. |
| 20d | Sensitivity results | Y: yapılmadı | N | Y | NR | `JUSTIFIED_NA` | 13f yöntem gerekçesi tamamlandıktan sonra kapanır. |
| 21 | Reporting biases results | Y: yapılmadı ve limitation | N | Y | NR | `JUSTIFIED_NA` | TQAF reporting completeness bias testi değildir; publication/selective reporting bias dışlanamaz cümlesi korunmalı. |
| 22 | Certainty results | P: 54/47/10/4 | Y: 115-row table | N | DRAFT | `PARTIAL` | Body-level contributor, rule ve rating tablosu aktif pointer almalı; abstract/conclusion review-specific certainty ile uyumlanmalı. |
| 23a | Interpretation | P: güçlü internal interpretation | Y: verified contextual source audit | P | NR | `PARTIAL` | Discussion'a yalnız exact claim'i destekleyen doğrulanmış kaynaklarla prior O-ISAC ve broader ISAC karşılaştırması eklenmeli. |
| 23b | Evidence limitations | Y | Y: Section VIII | Y | NR | `READY` | Evidence limitation ile review-process limitation ayrımı korunmalı. |
| 23c | Review-process limitations | Y | Y: Section VIII | Y | NR | `READY` | Search, retrieval, retrospective registration, AI, no duplicate review, no bias/sensitivity/meta-analysis ve etkileri korunmalı. |
| 23d | Implications | P: roadmap güçlü | P: Table VIII blueprint | P | NR | `PARTIAL` | Practice/policy sonucu standards bodies, funders ve 6G programmes için açıklaştırılmalı; Table VIII tutulacaksa üretilmeli. |
| 24a | Registration | Y | Y: lineage correction | Y: DOI | **Released OSF** | `READY` | Retrospektif kayıt ve 221'in 206'ya attrition olmadığı korunmalı; abstract'a compact bilgi eklenmeli. |
| 24b | Protocol access | P: “protocol exists” | Y: internal protocol/amendments | N | DRAFT | `PARTIAL` | Final supplement/repository DOI oluşturulup aktif pointer eklenmeli. |
| 24c | Amendments | P | Y: dated amendments | P | DRAFT | `PARTIAL` | Her amendment için değişiklik, gerekçe ve review stage gösteren final deviation table gereklidir. |
| 25 | Support | N | Y: author-confirmed checkpoint | N | NR | `OPEN` | Front matter ve abstract'a no-support beyanı eklenmeli. |
| 26 | Competing interests | N | Y: author-confirmed checkpoint | N | NR | `OPEN` | “The authors declare no competing interests.” eklenmeli. |
| 27 | Data/code/materials availability | N | P: sanitized DRAFT package | N | **Not released** | `OPEN` | Creator, rights, licenses, clean repo, DOI, version, contact ve restrictions kapatılıp gerçek release yapılmalıdır. |

Her satırın tam artefakt yolları, ayrıntılı bulguları ve doğrudan eklenebilir
İngilizce düzeltme metinleri eşlik eden
`PRISMA_2020_FULL_REAUDIT_2026-08-13.json` içinde bulunmaktadır.

## Item 17 kritik düzeltmesi

Item 17'nin mevcut durumu kesin olarak `OPEN`'dır:

- dahil edilen benzersiz çalışma: 206;
- aday bibliyografyadaki primary-study girişi: 206;
- mevcut manuscript içinde gerçekten atıflanan dahil çalışma: 76;
- henüz atıflanmayan dahil çalışma: 130;
- aktif, citation-linked, 206-row final study-characteristics supplement: yok;
- rich 206-row public projection: var, fakat `DRAFT` staging ve release değil.

Kapanış koşulu yalnız referans listesine 206 kayıt koymak değildir. ST-01'in her
satırı gerçek citation key ile çalışma özelliğini eşleştirmeli; 206 benzersiz
study ID, 206 çözümlenmiş citation key ve 206 görünür study citation gate'i
geçmelidir. Companion report lineage kaybolmamalı, ancak 227 rapor 227 çalışma
gibi sayılmamalıdır.

## Conventional risk of bias ile TQAF sınırı

Items 11 ve 18, yalnız TQAF dosyaları bulunduğu için kapatılamaz. Conventional
study-level risk-of-bias assessment yapılmamıştır. `risk_of_bias.csv` tarihsel
dosya adıdır; içeriği review-specific TQAF'dır. Yayın metni:

> No conventional study-level risk-of-bias instrument was applied. We used the
> review-specific, deterministic eight-dimension TQAF to characterize technical
> evidence and reporting. TQAF is nonvalidated and is not a substitute for a
> conventional risk-of-bias assessment.

demeli; 206-row TQAF ancak “Study-level TQAF technical evidence and reporting
appraisal” adıyla sunulmalıdır.

## Düzeltilmeye hazır kritik metinler

### Item 16b

> Supplement S Exclusions lists all 39 reports excluded after full-text
> assessment, with a complete citation, one primary exclusion reason, and a
> report-specific evidence note. The six contextual reports were retained
> separately and were not counted as full-text exclusions.

### Item 17

> Supplement ST-01 cites and characterizes all 206 included study clusters,
> including the designated primary report, companion-report lineage,
> publication year and venue, optical modality, integration mechanisms,
> communication and sensing functions, validation design, application labels,
> and claim-restriction status.

### Item 19

> Supplement S Metrics reports individual-study results with study and report
> identifiers, metric definition and role, source-reported value and unit,
> measurement plane, operating condition, validation context, uncertainty where
> available, result origin, and source locator. No project-derived performance
> value or pooled estimate was calculated.

### Item 20a ve 22

> Supplement S Bodies identifies the studies contributing to each S1-S7
> evidence body and reports the characteristics, TQAF context, deterministic
> certainty rule, and rating needed to interpret that synthesis. Review-specific
> certainty was high for 54 bodies, moderate for 47, limited for 10, and unclear
> for 4; these categories are not GRADE ratings.

### Item 24c

> Supplement S Protocol reports each departure from the retrospective OSF
> snapshot, the reason for the change, and the stage at which it occurred. The
> 221-study snapshot used different dates, sources, reviewer plans, appraisal
> plans, and denominators and is not an attrition step toward the final 206-study
> corpus.

### Items 25 ve 26

> This review received no specific financial or non-financial support. No funder
> or sponsor had any role in the design, conduct, analysis, interpretation,
> manuscript preparation, or decision to submit.

> The authors declare no competing interests.

### Item 27

> The executed protocol and amendments, search logs, selection decisions,
> report-to-study mappings, extraction forms and derived tables, TQAF outputs,
> synthesis tables, and analysis and QA code are available at [persistent
> repository URL or DOI; version; license]. Publisher PDFs and other copyrighted
> full texts are not redistributed. [Restricted material and request conditions,
> if any] are available from [responsible author and contact].

Item 27 metni ancak gerçek repository/DOI, version, license ve contact
dondurulduktan sonra kullanılabilir.

## Net blocker listesi

1. **Front matter:** final title, PRISMA-complete abstract, support ve competing
   interests adayda yok.
2. **Objective and methods:** PCC/RQ, source, full search, reviewer, extraction,
   outcome-selection ve codebook ayrıntıları ile final pointer'lar tamam değil.
3. **RoB boundary:** conventional RoB yapılmadığı açıkça kapatılmalı; TQAF RoB
   gibi sunulmamalı.
4. **Selection carriers:** locked PRISMA flow adayda aktif figür değil; 39
   exclusions register'ının active supplement pointer'ı yok.
5. **Item 17:** 206/206 included-study citation ve characteristic gate'i açık.
6. **Individual results:** 4,861/4,779 metric carrier'ı journal supplement ve
   manuscript pointer hâline gelmedi.
7. **Synthesis contributors and certainty:** 115 body ve 4,931 membership final
   reader-facing table ile bağlanmadı.
8. **Heterogeneity/bias/sensitivity wording:** descriptive heterogeneity,
   sensitivity nonapplicability ve missing-results bias sınırları birleştirilmiş
   final yöntem metninde tamamlanmalı.
9. **Discussion:** prior evidence comparisonı source-verified olmalı; practice
   ve policy implications açık yazılmalı.
10. **Protocol access/amendments:** permanent access ve change/reason/stage
    tablosu yok.
11. **Availability/release:** public package hâlâ staging; creator, rights,
    license, clean repository ve DOI kararları açık.

## Güvenle otomatikleştirilebilen sonraki kapılar

- 42/42 benzersiz PRISMA item/subitem kontrolü;
- her satırda dört ayrı eksenin zorunlu olması;
- ST-01 için 206 benzersiz study ID + 206 citation key + 206 görünür citation;
- draft staging'in hiçbir zaman `released` sayılmaması;
- blueprint comment'in materyalize görsel/tablo sayılmaması;
- TQAF'ın conventional RoB veya GRADE diye etiketlenmemesi;
- OSF kaydının her yerde retrospective olması ve 221 → 206 attrition oku
  kurulmaması;
- yapılmamış meta-analysis, formal sensitivity veya formal missing-results bias
  assessment iddiası kurulmaması;
- 76 COMST makalesinin scientific decision authority olarak kullanılmaması.

## Checklist CSV durumu

Publication-facing CSV için gerekli spreadsheet runtime loader, tekrarlanan
sınırlı beklemelerde kullanılabilir bir `artifact_tool` yolu döndürmedi. Skill
kurallarına uygun olarak alternatif kütüphane, global dependency veya tahmini
path kullanılmadı. Bu nedenle CSV bu turda üretilmedi. Eşlik eden JSON tam 42
satırlık yapılandırılmış veriyi içerir ve runtime düzeldiğinde deterministik
olarak CSV'ye aktarılabilir.

