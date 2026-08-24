# O-ISAC PRISMA / COMST Durable Memory Bank

> Güncel operasyon için aşağıdaki en yeni tarihli `CURRENT RESUME AUTHORITY`
> bölümü kullanılır. Daha eski bloklar yalnız tarihli audit trail’dir.

## CURRENT RESUME AUTHORITY — FINAL SUBMISSION CLOSEOUT, 2026-08-24

- Kullanıcı bütün manuscripti submission öncesi son kez baştan sona denetleme
  ve sekiz şekli tamamlama yetkisi verdi.
- İlk zorunlu gate GitHub güvenlik kaydıdır. Çalışma klasöründeki `.git` dizini
  boş bulunduğu için uzak geçmişten yalnız metadata geri bağlandı. Mevcut
  dosyalar klondan kopyalanmadı veya üzerine yazılmadı.
- Korunan uzak taban `agent/full-corpus-survey-ready` dalındaki
  `9b29b221213786c9893134a36638c3d9a0739f49` commit'idir. Yeni çalışma dalı
  `codex/final-submission-20260824` olarak açıldı.
- Pre-edit `main.pdf` 23 sayfa, 203,407 byte ve 241 bibliography entry içerir.
  SHA-256 değeri
  `A258E699084D190186298EA95D279E459A75D5F9B9881EC2EF9DC03F505C5E35`'tir.
- Son prose standardı Sections IV ve V'te onaylanan anlatıdır. Her paragraf tek
  ana işi taşır ve construct, evidence, condition ile engineering meaning
  hattında ilerler. Float ayrıntısı prose içinde yeniden listelenmez.
- Reader-facing prose, caption ve table note içinde yazar kaynaklı iki nokta,
  noktalı virgül, `neither ... nor`, tekrar eden `not`, savunmacı denylist
  ritmi ve kolayca yeniden kurulabilen alfabetik tireli compound kullanılmaz.
- Kısaltma ilk gerçek occurrence'ta bir kez açılır. O-ISAC Abstract'ta açıldıktan
  sonra yeniden açılmaz. Bir paragrafta üçten fazla yeni abbreviation tanıtımı
  review trigger'dır. Table ve figure içindeki zorunlu kısa biçimler caption
  veya note içinde açılır.
- OSF predecessor, eski denominator, yapılmamış kontrol veya güncellenecek iş
  gibi audit-history ifadeleri reader-facing manuscriptte yer almaz. Bilimsel
  çıkarımı değiştiren gerçek sınır uygun carrier'da bir kez ve etkisiyle verilir.
- Figures 1--8 yalnız kanonik veri ve düzenlenebilir vektör kaynaklarla üretilir.
  Üretken görsel sistemi kullanılmaz. Figure prose tekrarını azaltır ve renk
  olmadan da okunabilir olur.
- Operasyon sırası baseline push, tam audit, bütünsel prose revision, teknik ve
  görsel QA, figure production, figure-inclusive final QA ve final push'tur.
- Bağımsız checkpoint
  `checkpoints/final_submission_baseline_2026-08-24/README.md` dosyasıdır.

Bu blok, aşağıdaki 2026-08-19 authority'yi operasyonel olarak geçersiz kılar.

## CURRENT RESUME AUTHORITY — 2026-08-19

Son güncelleme: 2026-08-24.

> Bu bölüm tek güncel memory otoritesidir. Aşağıdaki eski “current”, “next”,
> “pending table”, “no compile”, 220/221-study veya V4–V9 package blokları
> tarihli audit trail’dir. Tam bağımsız devam kaydı:
> `checkpoints/comst_memory_handoff_2026-08-19/README.md`.

### 1. Güncel durum

- Active title: *Optical Integrated Sensing and Communication for 6G: A
  Systematic Review and Survey of Architectures, Metrics, and Tradeoffs Across
  Optical Platforms*.
- Aktif manuscript:
  `07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- Aktif driver `main.tex`; kesin okuma sırası `MANUSCRIPT_BODY_INPUTS.tex`.
- `main.pdf`: 23 sayfa, 203,337 byte, 8 canlı tablo, 0 canlı figure, 243 bibliography
  entry ve 206/206 included-study citation.
- PDF SHA-256:
  `4467D5816FA20A1A0D0E64B11A9EC0997EC786D168F04AE83582056DB4D3CBC8`.
- Section V source SHA-256:
  `D733C6CC379DC648CF058211F0A99146890BB8DFE772865829611F6D33FC12AF`.
- ST-01: 206 unique study, 227 eligible report ve 227 report citation.
- Aktif supplement:
  `OISAC_COMST_SUPPLEMENT_FINAL_V10_2026-08-17.zip`; 42 entry; SHA-256
  `4f140851568a667ac0b9dde0b57c104742b0f747f2abb28335cffe37fe61617d`.
- Sekiz main-text figure specification-only durumunda; henüz üretilmedi.
- Abstract final edit için sona bırakıldı.
- Sections I–IV author reading/revision gördü ve kabul edildi. Section IV
  survey-first biçimde bütünsel olarak yeniden yazıldı; evidence, citation,
  build ve rendered-page QA PASS aldı. Table IV ayrıntı taşıyıcısı olarak
  güçlendirildi; fiber, VLC/LiFi, free space optical ve hybrid/residual prose
  blokları mekanizma, örüntü ve mühendislik anlamına indirildi. Integration
  Architectures da coupling location, recurring mechanism, engineering
  consequence ve evidence form etrafında yeniden kuruldu. IV-C'nin somut
  platform ve shared-constraint iddiaları dört dar citation cluster ile
  kaynaklandı. Section V açılışı 159 word, üç paragraf ve on cümledir. Opening,
  V-A lead, Table V ve immediate interpretation yazar kaynaklı semicolon, colon
  ve negative-marker cadence içermez. 4,779 denominator, 85/60/50 overlapping
  study coverage ve 118/4,661 analytical split korunmuştur. Table V artık
  Table IV gibi tek sütunlu kompakt bir survey haritasıdır. Beş metric domain
  satırı ile iki analytical-role satırını taşır; ayrıntılı semantic contract
  V-B ve S-Evidence'da kalır, tradeoff dağılımı planlanan Fig. 6'ya aittir.
  Tablo PDF page 8'de V-A ile V-B arasında doğru okuma sırasında yer alır.
  Metrics Across Functions üç bağlantılı survey unit olarak tamamlanmıştır.
  Communication Metrics 326 word ve dört paragraf, Sensing Metrics 275 word ve
  dört paragraf, Joint and Implementation Metrics 249 word ve üç paragraf
  içerir. Akış metric meaning ve evidence conditions'dan matched joint evidence,
  optimization ve platform burden'a ilerler. Tüm retained study anchor'lar claim
  adjacent kalmıştır. Revised unit'ler author colon, semicolon veya defensive
  negative marker içermez. How Communication and Sensing Performance Interact
  2,262 prose word, 30 paragraph ve 149 sentence ile shared design choice,
  observed response, source condition ve engineering meaning akışında yeniden
  kurulmuştur. İki paragraflık giriş shared resource'ları evidence scope'tan önce
  açıklar. Önceki 176 citation key ve 180 citation use korunmuştur. Governed
  ledger ve detailed family profile planlanan Fig. 6 ile supplement'lere aittir.
  Conditions for Comparison Across Studies, V-D'yi 130 word, iki paragraf ve dokuz
  cümlede kapatır. Prohibited style marker sayısı sıfırdır ve table/prose carrier
  ayrımı korunmuştur. Güncel Section V TeXcount text 3,562 word'dür. Section V
  author reading tamamlanmıştır. Section VI survey-first biçimde yeniden
  kurulmuş, teknik QA'dan geçmiş ve author reread onayını beklemektedir.
  Section II/Table II aynı survey-first ilkeyle geriye
  dönük olarak sıkıştırılmıştır. Section II 711 prose word, 12 paragraf ve 46
  cümledir. Table II dört comparison component ve üç analytical use taşıyan
  yedi satırlı iki-panel survey map'tir. Exact fields/codes S-Data Dictionary,
  record-level provenance ve rationale S-Evidence'da kalır. Sections VII–IX,
  Section VI author reread sonrasında izliyor.

### 2. Yeni sohbet ilk okuma sırası

1. `prisma2020Review/AGENTS.md`.
2. `START_HERE_OISAC_PRISMA_CURRENT.md` içindeki 2026-08-19 current block.
3. `PROJECT_CONTEXT_OISAC_PRISMA.md` içindeki en üst current block.
4. Bu memory bölümü ve
   `checkpoints/comst_memory_handoff_2026-08-19/README.md`.
5. Active manuscript `README.md`, `MANUSCRIPT_STRUCTURE.json` ve
   `qa/CURRENT_QA_INDEX_2026-08-13.md`.
6. Kullanıcının okuduğu section ile iki komşu sectionın geçişleri.

Eski checkpointlerin tamamını yeniden okumak veya Phase A–F’yi yeniden
çalıştırmak gerekli değildir.

### 3. Kullanıcı tarafından onaylanan survey yazım ilkeleri

- Scientific story survey içeriğidir. PRISMA yalnız güven/izlenebilirlik sağlar;
  okuyucuya öğretilmez ve audit history anlatının önüne geçmez.
- Okuyucu mekanizmayı, koşulu ve evidence sınırını kolay anlamalı; ilgilendiği
  özgün çalışmaya citation üzerinden ulaşabilmelidir.
- Metin kısalabilir; COMST kelime medyanına ulaşmak için dolgu yapılmaz.
- Ton akademik ve doğal olmalıdır; robotik, meta-writing ağırlıklı veya günlük
  konuşma dili kullanılmaz.
- Reader-facing prose, caption ve table note içinde yazar kaynaklı iki nokta ve
  noktalı virgül kullanılmaz. Düşünce doğal bir bağlaçla bağlanır veya açık iki
  cümleye ayrılır. `neither ... nor`, art arda `not` ve savunmacı denylist
  kalıpları anlatı dili olarak kullanılmaz.
- Sınırlar dürüstçe verilir fakat anlatı sürekli eksiklik/olumsuzluk diliyle
  kurulmaz. Pozitif, koşullu ve merak uyandırıcı formulation tercih edilir.
- Scientific honesty, bütün doğru olumsuzlukları ana prose'a yığmak değildir.
  Bir sınır yalnız çıkarımı maddi olarak değiştiriyorsa, yanlış anlamayı
  önlüyorsa veya reporting/reproducibility için gerekiyorsa reader-facing
  metne girer; doğru carrier'da bir kez ve etkisiyle birlikte verilir.
- QA denylistleri manuscript cümlesine dönüştürülmez. Prose önce construct'u,
  kanıtı, katkıyı ve geçerli olduğu koşulu kurar; formal nonperformance ve
  caveat ayrıntıları gerektiğinde Limitations, figure/table note, checklist
  veya supplementte taşınır.
- Omission okuyucuyu maddi olarak yanıltacaksa bilgi saklanmaz. Buna karşılık,
  bilimsel sonucu değiştirmeyen her “yapılmadı/kapsam dışı/değildir” kaydını
  öne çıkarmak da şeffaflık sayılmaz; gereksiz self-devaluation'dan kaçınılır.
- Aynı acronym, scope veya section işi tekrar açılmaz. O-ISAC Abstract’ta
  açıldıktan sonra Introduction’da yeniden açılmaz; diğer acronym’ler de yalnız
  ilk gerçek manuscript occurrence’ta açılır.
- Gereksiz tire ve çizgi kullanılmaz; resmi/teknik yazım istisnadır.
- Contribution bullets noun-led scientific deliverable’dır; tekrar eden
  `We ... We ... We ...` dizisi kullanılmaz.
- Tables inventory/exact mapping; figures relationship/flow/distribution/
  mechanism taşır. Prose floatı satır satır tekrar etmez.
- Reader-facing table bir audit matrisi değil, birkaç saniyede okunabilen survey
  haritasıdır. Her tablo tek soruyu yanıtlar, az sayıda sütun ve kısa hücrelerle
  ana dağılımı veya eşlemeyi gösterir. Semantik açıklama prose'a, satır düzeyi
  ayrıntı supplemente, ilişki ve dağılım ise ilgili figure'a bırakılır. Table IV
  ve tek sütunlu kompakt Tables II, IV, V ve VI bu kuralın güncel örnekleridir.
- Kullanıcı micro-management yapmaz. `Anlamadım`, `Yoruldum` veya
  `Katılmıyorum` işareti yeterlidir; teşhis, kaynak kontrolü, revision, compile
  ve QA Codex’in işidir.
- 76 COMST paper style/architecture/visual-function benchmark’ıdır; O-ISAC
  scientific evidence authority değildir ve source wording kopyalanmaz.

### 4. Section ownership ve author-reading noktası

1. **Introduction:** motivation, scope, Table I prior-synthesis positioning ve
   contributions. Yaklaşık 531 non-table prose word. Reader-facing ST-RS1
   note/annex yok; four contributions noun-led.
2. **Foundations and Comparison Framework:** system boundary, modality,
   coupling, measurement contract ve analytical use. Section II 711 prose
   word, 12 paragraph ve 46 sentence içerir. Table II dört comparison component
   ve üç analytical use taşıyan kompakt survey map'tir; exact fields, codes ve
   record detail supplementlere aittir. Figs. 1–2 inline specs hazır.
3. **Review Process and Evidence Base:** kısa corpus construction, evidence
   use, appraisal/inference boundary. Governing QA count 635 prose word.
   Table III canlı; Figs. 3–4 specs hazır.
   Section II--III geçişi comparison conditions üzerinden evidence base'e
   bağlanır. Corpus Construction açılışı direct author actions ve ayrı
   search/eligibility/denominator hareketleriyle COMST paragraph contract'a
   uyar. Selection prose'u 227 report, 21 companion report ve 206 study
   denominator meaningini taşır; ara akış envanteri Fig. 3 spec'ine bırakılır.
   Evidence Extraction provenance→claim-use hattını, Technical Appraisal ise
   TQAF interpretation→structured narrative synthesis hattını kurar. Closing,
   native task/unit/conditions/validation meaningini korurken recurring
   mechanisms ve design relationships'i ortak analytical level olarak kurar.
   Section III
   TQAF'ı deterministic, review-specific ve synthesis-support odaklı pozitif bir
   evidence profile olarak tanımlar. Nonvalidation, RoB/GRADE ve scientific-worth
   sınırı yalnız Section VIII ve reporting supplements'ta taşınır. Table II
   Section III'ten önce, Table III kendi lead-in'inden sonra ve subsection C'den
   önce render edilir; sentence interruption yoktur. PRISMA yalnız reporting
   frame; AI workflow prose’dan çıkarıldı.
4. **Optical Platforms and Integration Architectures:** platform physics ve
   integration mechanisms. Güncel metin 1,880 TeXcount text word, 25 prose
   paragraph ve 113 sentence içerir; pre-revision 2,880 word durumundan 1,000
   word ve %34.7 kısalmıştır. Table IV exclusive family counts, task inventory,
   constraints ve transfer conditions taşır. Family prose yalnız physical
   mechanism, recurring pattern ve engineering interpretation taşır. Fiber,
   VLC/LiFi, free space optical ve hybrid/residual blokları toplam 564 word ve
   sekiz paragraftır. IV-B 678 word ve on paragrafta coupling location,
   recurring mechanism, engineering consequence ve evidence form taşır.
   Section IV'te 71 unique included-study key ve 56 citation command vardır.
   Fig. 5 yedi overlapping integration location, locked counts ve üç mixed case
   taşıyıcısıdır; aktive edilince prose'daki numerical coupling inventory
   kaldırılır. III→IV ve IV→V transitions PASS; Section IV author tarafından
   onaylanmıştır.
5. **Performance Metrics and Joint Design Tradeoffs:** metric meaning,
   admissibility ve tradeoff synthesis. Açılış 159 word, üç paragraf ve on
   cümledir. 4,779 metric record source contextli extraction unit olarak
   tanımlanır; 85/60/50 study coverage ve 118/4,661 analytical split korunur.
   Table V beş metric-domain ve iki analytical-role satırı taşıyan tek sütunlu
   survey haritasıdır; PDF page 8'de V-A ile V-B arasında yer alır. Metrics
   Across Functions ve How Communication and Sensing Performance Interact tamamlanmıştır. V-C
   shared design choice, observed response, source condition ve engineering
   meaning akışını kullanır. Conditions for Comparison Across Studies V-D'yi 130
   word, iki paragraf ve dokuz cümlede tamamlar. Prohibited style marker sayısı
   sıfırdır ve table/prose carrier ayrımı korunmuştur. Section V author reading
   tamamlanmıştır.
6. **Validation Evidence, Reconstructability, and Benchmark Readiness:** dört
   reader question validation settings and methods, both-domain field evidence,
   artifact access and reconstructability, and benchmark readiness sırasını
   izler. Table VI yalnız observed access states taşır. Planned Fig. 7 exclusive
   maximum setting ve multilabel method distributions'a aittir. S7'deki 6/12
   bulgusu study-level both-domain outcomes ile sınırlıdır. Timing ve ayrı
   function locator alanları 12/12 unresolved kalır. Section VI 1,300
   style-audit word, 16.049 mean sentence length ve sıfır author colon,
   semicolon, `neither` veya avoidable alphabetic hyphen içerir. Technical QA
   PASS, author approval pending durumundadır.
7. **Technologies, Applications, 6G:** mechanism-to-requirement mapping.
8. **Discussion, Roadmap, Limitations:** higher-order interpretation.
9. **Conclusion:** kısa takeaway; yeni evidence yok.

I scope’u; II comparison vocabulary’yi; III method/denominatorsı; IV–VII
technical synthesis’i; VIII interpretation/roadmap’i; IX closure’ı sahiplenir.
Bir bölüm diğerinin tanımını veya bulgu kataloğunu yeniden kurmaz.

Mandatory AI disclosure yalnız `sections/10_REPORTING_DECLARATIONS.tex`
içindedir. Sections I–IX içine review-conduct AI anlatısı geri taşınmaz.

### 5. Kilitli paydalar

- Window: 1 January 2020–22 June 2026.
- 1,733 identified → 1,259 screened → 330 reports sought → 272 assessed →
  227 eligible reports → 206 unique studies.
- 39 full-text exclusions; 6 contextual reports; 21 companion reports; 19
  multi-report studies.
- Governed rows: 8,306 = 3,041 evidence + 4,861 metric + 404 tradeoff.
- Primary synthesis: 8,203 = 3,020 evidence + 4,779 metric + 404 governed
  tradeoff.
- Use: 3,206 qualitative + 4,997 quantitative + 31 context only + 72
  quarantined exact claims.
- Substantive tradeoff: 402 / 168 studies / 218 quantitative / 184 qualitative /
  371 conditional. Governed 404 retains two absence sentinels.
- TQAF: 125 strong / 75 adequate / 6 low; not conventional RoB/GRADE/ranking.
- 115 evidence bodies; 4,931 memberships.
- Modalities: 69 photonics assisted THz / 56 fiber / 38 VLC-LiFi / 31 FSO /
  9 hybrid / 3 other.
- Maximum field/deployment tier 12; strict paired-function subset 6.
- 6G relevance: 138 direct / 64 inferential / 1 weak / 3 not applicable.

`record`, `report`, `study`, `claim row`, `metric row`, `tradeoff row`,
`evidence body` ve `citation` birbirinin yerine kullanılmaz. OSF 221-study
snapshot, final 206’ya direct attrition değildir.

### 6. Citation ve bibliography policy

- 206/206 included study claim-matched main-text context içinde cite edilir.
- Main bibliography 243 = 206 included + 29 context/method + 8 exact
  report-specific companion.
- ST-01: 206 study rows; 227-report bibliography = 206 primary + 21 companion.
- Citation cluster tek proposition’a bağlı ve en fazla 7 included study’dir.
- `\nocite`, manual `[n]`, mega-train, citation-only footnote ve irrelevant
  stuffing yasaktır.
- Companion report yalnız report-specific result kullanıldığında main text’te
  cite edilir; prevalence `study_id` ile deduplicate edilir.
- Table I’de 24 direct prior-synthesis citation vardır. 38-source contextual
  register internal audit’tir; ST-RS1 reader-facing annex değildir ve 206-study
  denominator’a girmez.

### 7. Table ve figure state

Tables I–VIII canlı/layout-verified. Pending figure map:

1. Section II — native evidence objects.
2. Section II — four-axis comparison framework.
3. Section III — PRISMA record/report/study flow.
4. Section III — eight TQAF dimensions + separate overall row.
5. Section IV — seven overlapping integration locations.
6. Section V — three-panel 402-row substantive tradeoff profile.
7. Section VI — exclusive maximum tier + multilabel validation methods.
8. Section VII — technology/observable/application/6G chain.

Production: locked data’dan recompute; editable vector; final text ≥8 pt;
direct labels; colorblind/grayscale safe; alt text. Decorative art,
copied/redrawn source figure, pie/donut, radar, 3D, dual axis, rainbow,
heterogeneous Pareto frontier, platform leaderboard ve multi-label-as-partition
yasaktır. Asset QA geçmeden figure ref/caption aktive edilmez.

Placement authority: `02_VISUAL_AND_TABLE_PLACEMENT_CONTRACT.md`. Older global
visual contract yalnız grammar/accessibility için; old status/section numbering
geçersiz. Figs. 3–4 için active Section III inline specs kazanır.

### 8. Supplement/package state

- `supplements/st01/`: 206 studies + 227 reports + complete bibliography.
- `supplements/evidence/`: exclusions; 3,020 evidence; 4,779 metric; 404
  governed/402 substantive tradeoff; 206 TQAF; 115 bodies; 4,931 memberships.
- `supplements/reporting/`: executed search, protocol/amendments, 446-field
  dictionary, conduct/reporting/TQAF/body rules.
- `supplements/s7/`: 206 join + 12 maximum tier + strict six.
- `supplements/related_synthesis/`: internal only, not upload annex.

Exact alias→path map: `supplements/README.md`. V10 is peer-review electronic
supplement, not public DOI-bearing release.

### 9. Authority order

1. Locked Phase C counts/exclusions and Phase B report-to-study mapping.
2. Hash-locked Phase D survey-ready workbook.
3. Frozen Phase E crosswalk/TQAF audit.
4. Final Phase F S1–S7 outputs.
5. Active v2 manuscript/materialized supplements as derived carriers.
6. Current dated QA/checkpoint/memory.
7. COMST corpus only for style/architecture.
8. v1, 220/221, old ZIP/QA/checkpoints and public staging only as history.

Derived carrier upstream locked evidence ile çelişirse carrier regenerate
edilir; locked denominator prose’a uydurulmaz.

### 10. Kuralların yerleri

- Repo workflow: `prisma2020Review/AGENTS.md`.
- Current handoff: `START_HERE_OISAC_PRISMA_CURRENT.md`.
- Context: `PROJECT_CONTEXT_OISAC_PRISMA.md`.
- Decision/progress: `09_kayitlar/decision_log.md`, `progress_tracker.md`.
- Scope/anchors: `comst_206_v2_9section/00_SCOPE_AND_SOURCE_MANIFEST.md`.
- Section ownership: `01_SECTION_LEVEL_EDITING_DECISIONS.md`.
- Visual/table placement: `02_VISUAL_AND_TABLE_PLACEMENT_CONTRACT.md`.
- Supplement contract: `03_SUPPLEMENTARY_EVIDENCE_CONTRACT.md`.
- Author review: `AUTHOR_REVIEW_GUIDE_TR.md` ve
  `SECTION_BY_SECTION_REVIEW_GUIDE_TR_2026-08-14.md`.
- Front matter: `FRONT_MATTER_ACTIVE_2026-08-14.md` ve declarations file.
- QA routing: `qa/CURRENT_QA_INDEX_2026-08-13.md`.
- Section V-C governing current-text report:
  `qa/SECTION5_TRADEOFF_MECHANISMS_SURVEY_FIRST_QA_2026-08-24.*`. Table V and
  Metrics Across Functions baseline:
  `qa/SECTION5_TABLE5_SURVEY_MAP_QA_2026-08-21.*`; approved opening baseline:
  `qa/SECTION5_OPENING_SURVEY_FIRST_QA_2026-08-21.*`.
- Section V-D governing current-text report:
  `qa/SECTION5_CROSS_STUDY_COMPARISON_QA_2026-08-24.md/json`.
- Section VI governing current-text report:
  `qa/SECTION6_VALIDATION_RECONSTRUCTABILITY_SURVEY_FIRST_QA_2026-08-24.md/json`.
- Section IV current text/PDF:
  `qa/SECTION4_SURVEY_FIRST_QA_2026-08-20.*`.
- Approved Section III text/PDF:
  `qa/SECTION3_AUTHOR_REREAD_PREP_QA_2026-08-19.*`; compression baseline:
  `qa/FINAL_SECTION3_SURVEY_FIRST_QA_2026-08-17.*`.
- Citation: `qa/FINAL_CITATION_COMPLETION_QA_2026-08-16.*`,
  regenerated `FINAL_MAIN_CITATION_COVERAGE_206.*` and
  `CITATION_PLACEMENT_CROSSWALK_206.*` (206/206, 0 missing, 415 uses,
  197 citation commands, maximum cluster 7). Crosswalk CSV SHA-256 is
  `63C6343A57A18267CC9253BC09647D80130C97D2842694B12B9F6A3F5A14C5B9`,
  and XLSX SHA-256 is
  `49EABFFABB9DC5B01FB3FECB467330714FE079E48E67686800023F56C6E3428B`.
- Companion provenance: `qa/FINAL_COMPANION_DELIVERABLE_QA.*`.
- PRISMA closure: `qa/PRISMA_2020_FINAL_LOCAL_REAUDIT_2026-08-14.*`.
- Eligibility/reviewer locks:
  `checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/` and
  `...gate_step2_2026-07-19/`.
- Detailed method rules:
  `supplements/reporting/S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md`.
- COMST writing evidence: `comst_76_fulltext_almanac_2026-08-09/` and
  `style_profile/`.
- Visual grammar: `visual_blueprint_2026-08-10/reports/GLOBAL_VISUAL_STYLE_AND_PRODUCTION_CONTRACT.md`.
- Python/vector/accessibility:
  `visual_blueprint_2026-08-10/agent_architecture/PRODUCTION_ACCESSIBILITY_PYTHON_CONTRACT.md`.
- Detailed figure blueprint:
  `visual_blueprint_2026-08-10/agent_figures/OISAC_FIGURE_GRAPH_BLUEPRINT.md`.

### 11. Exact next operation

1. User revised Section VI'yı baştan sona yeniden okur ve author approval verir
   veya anlaşılmayan kısmı işaretler.
2. Codex yalnız `anlamadım/yoruldum/katılmıyorum` işaretlerini alır ve whole-section
   contextte düzeltir.
3. Her düzeltmede Section VI carrier'ları, citations ve V→VI/VI→VII transitions
   birlikte denetlenir.
4. Aynı model VI–IX için sürdürülür.
5. Abstract en son finalize edilir.
6. Approved prose ile Figures 1–8 reconcile edilip üretilir.
7. Figure-inclusive compile/render/accessibility/layout QA yapılır.
8. Portal/public-release actions author-owned kalır.

### 12. Regression yasakları

- Phase C–F veya 206/227 denominatorı yeniden açma.
- 221→206 attrition hikâyesi yazma.
- Section III’te PRISMA öğretme veya audit/AI workflow prose’unu geri getirme.
- Mandatory AI disclosure’u declarations’tan silme.
- ST-RS1 annex’i geri getirme.
- Acronym’leri her sectionda yeniden açma.
- Citation dump, missing-value inference, pooled effect, universal frontier,
  platform rank veya TQAF-as-RoB/GRADE üretme.
- Raw public modality/mechanism labels ile figure üretme.
- Historical `FINAL_VISUAL_CONTRACT_QA`, V1, V4–V9 ZIP veya old “next” kaydını
  current truth sayma.

> The 2026-08-17 block below is a dated snapshot and is superseded
> operationally by the 2026-08-19 resume authority above.

## Current authority — 2026-08-17 Section III survey-first compression

- Active authority: `07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- Table I is self-contained with 24 direct prior-synthesis citations. The
  reader-facing ST-RS1 note and annex were removed.
- The 38-source contextual-synthesis register remains internal positioning
  audit material only and is outside the 206-study denominator.
- Four contribution bullets are noun-led scientific deliverables; none begins
  with `We`.
- Section III contains 527 prose words excluding Table III and internal figure
  specifications; method detail is carried by the named supplements.
- No AI review-conduct narrative remains in Sections I--IX; the required
  disclosure remains in the acknowledgment.
- Active build: nine sections, 27 pages, eight live tables, 243 bibliography
  entries, and 206/206 included studies cited. ST-01 resolves 227 reports.
- Current supplement: `OISAC_COMST_SUPPLEMENT_FINAL_V10_2026-08-17.zip`;
  SHA-256
  `4f140851568a667ac0b9dde0b57c104742b0f747f2abb28335cffe37fe61617d`.
- Governing QA:
  `qa/FINAL_SECTION3_SURVEY_FIRST_QA_2026-08-17.md/json`; checkpoint:
  `09_kayitlar/checkpoints/comst_section3_survey_first_2026-08-17/README.md`.
- Figures 1--8 remain the only missing manuscript content assets.

## Previous current authority — 2026-08-16

- Active authority: `07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- The survey now has nine active main sections in a compiled 31-page PDF.
- Main manuscript: eight live tables, 206/206 included studies cited in matched
  contexts, and 243 bibliography entries.
- ST-01: 42-page standalone supplement with 206/206 included studies and 227
  resolvable report citations (206 primary plus 21 companion reports).
- Figures 1--8 are the sole missing manuscript content assets. Produce them
  from the frozen specifications, then repeat the figure-inclusive compile,
  cross-reference, full rendered-page, and final layout QA.
- Supplemental package V6 was generated after final QA as
  `OISAC_COMST_SUPPLEMENT_FINAL_V6_2026-08-16.zip`; record SHA-256
  `b0c5d7d636fedaa21b85de1087ba441521a15d7c98e535213e84d48d4a63f65b`.
- The unpublished 220/221-study manuscript is historical and does not govern
  v2. The OSF 221-study record is a superseded predecessor snapshot with
  different procedures and denominators; 221 to 206 is not direct attrition.
- Locked scientific authority remains 227 eligible reports mapped to 206
  included studies. Do not reopen Phase C--F counts for figure production.
- Governing QA:
  `qa/FINAL_CITATION_COMPLETION_QA_2026-08-16.md/json` under the active
  manuscript; checkpoint:
  `09_kayitlar/checkpoints/comst_citation_complete_2026-08-16/README.md`.
- All earlier current-state, pending-table, no-driver, no-compile, and next-step
  statements are dated history and are superseded operationally by this block.

# Previous Current State â€” OSF Registration-Lineage Correction (2026-08-07)

- Same-review OSF registration verified: `7f6wb`, registered 12 February 2026, DOI `10.17605/OSF.IO/7F6WB`.
- Classification: retrospective registration, not prospective preregistration. The record itself says search/screening were complete and synthesis/manuscript drafting had begun with 221 included studies.
- The OSF 221-study state is a legacy predecessor snapshot with different dates, source set, reviewer plan, appraisal/bias plan and denominators. Do not narrate 221 â†’ 206 as direct study attrition.
- Canonical amendment: `systematic_review_workflow/01_protokol/04_protocol_registration_lineage_correction_2026-08-07.md`.
- Checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_registration_lineage_correction_2026-08-07/`.
- PRISMA Item 24a and Abstracts A12 wording are ready. Item 24c moved to ready; current 42-row artefact distribution = 16 ready / 20 partial / 4 justified N/A / 2 open; manuscript integration remains 0/42.
- Historical article author order, affiliations, corresponding author/email, Fatih DÃ¶nmez ORCID and the CC BY 4.0 data/docs + MIT code intent were recovered. Public creator scope, exact rights holder(s)/year and final legal license approval remain author decisions.
- The protected active manuscript was not edited, no LaTeX compilation was run, and no locked Phase Aâ€“F scientific state changed.

# Previous Current State â€” PRISMA 2020 Compliance Closure Gate (2026-08-05)

- 2026-08-06 author decision: no financial or non-financial support was received. Item 25 and Abstracts A11 are package-ready; exact English statement is frozen in the gap-closure draft bank. No active-manuscript integration occurred.
- Item 25 checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_item25_support_declaration_2026-08-06/`.
- 2026-08-06 author decision: the review authors have no competing interests. Item 26 is package-ready; exact English statement is â€œThe authors declare no competing interests.â€ No active-manuscript integration occurred.
- Item 26 checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_item26_competing_interests_declaration_2026-08-06/`.
- 2026-08-06 Item 9 boundary: authors of included studies were not contacted. Weekly meetings were internal review-team discussions used for verbal methodological verification; participants were not authors of included studies. Do not describe these meetings as study-author verification.
- Item 9 checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_item9_author_contact_boundary_2026-08-06/`.
- The Phase-G writing package remains scientifically ready for reviewed integration but is not submission-ready.
- A dated working matrix separates PRISMA artefact readiness, gap-closure drafting and actual manuscript integration for all 42 rows: `systematic_review_workflow/07_raporlama/03_prisma_2020_madde_artefakt_manuscript_uyum_matrisi_2026-08-05.md`.
- Matrix distribution after Items 25â€“26 closure: 15 ready, 21 partial, 4 justified non-applicable and 2 open; active-manuscript integration is 0/42.
- The English closure bank is `systematic_review_workflow/07_raporlama/04_prisma_2020_gap_closure_drafts_EN_2026-08-05.md`; it contains 29 item-specific sections and retains all user/citation/repository placeholders.
- Item 19's underlying study-level result dataset is present in the canonical Phase-D workbook (`04_METRIC_RESULTS`, 4,861 rows), but it still needs a publication-facing supplement and manuscript pointer.
- TQAF must be described as an eight-dimension review-specific technical evidence/reporting appraisal, not conventional risk of bias. Certainty is review-specific, uses all eight dimensions for non-S7 bodies, and is not GRADE.
- Formal reporting-bias assessment was not performed; Items 14/21 must report this limitation and must not imply that bias was absent.
- Author-owned open decisions: verified external-review citations, public repository/DOI, release/tag, license, public scope and request conditions. Funding/support, competing interests and author-contact outcome are closed.
- The original checklist and protected active manuscript were not modified, and no LaTeX compilation was run.
- Checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_compliance_working_gate_2026-08-05/`.
- Next action: freeze supplement and public-availability details, then verify external-review citations before controlled manuscript integration.

> The 2026-08-04 state below remains the locked scientific baseline; its immediate integration step is superseded by the PRISMA closure gate above.

## Previous Current State â€” Phase Aâ€“F Complete; Phase G Current (2026-08-04)

- Locked corpus: 227 eligible reports mapped to **206 included studies**.
- Phase D complete: 3,041 evidence items, 4,861 metric results and 404 trade-off records, totalling **8,306 governed claims**.
- Survey use: 3,206 qualitative, 4,997 quantitative, 31 context-only and 72 quarantined exact claims.
- Study use: 175 survey-ready and 31 survey-ready with claim restrictions. The 31 are not excluded or simply â€œwaitingâ€; their affected claims already have determinate use restrictions.
- Canonical workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_survey_ready_2026-08-04/OISAC_PHASE_D_SURVEY_READY_2026-08-04.xlsx`; SHA-256 `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`.
- QA PASS: 206 unique studies, 8,306 claims mapped exactly once, 93 conflict-register rows, 72 quarantined claims, 68 non-quarantine guardrails, 0 formula errors.
- Provenance: investigator-supervised, AI-assisted, user-delegated and claim-governed; `independent_human_status = not_documented`.
- Phase E TQAF complete: 206/206 rows; overall 6 low / 75 adequate / 125 strong; 115 evidence bodies; certainty 54 high / 47 moderate / 10 limited / 4 unclear; QA PASS 43/43.
- Phase-E final-workbook invariance audit PASS: 206 studies, 46 check families, 9,476 comparisons, 0 mismatches and 0 failed studies.
- Phase F S1â€“S7 complete: 8,203 primary claims = 3,020 evidence + 4,779 metric + 404 trade-off; internal QA PASS plus independent artifact QA PASS 29/29.
- The 8,234 non-quarantined universe includes 31 context-only metrics and must not be presented as primary evidence. All 72 quarantined claims remain outside primary numeric synthesis.
- Multi-label fallback-only counts: integration 0, enabling technology 19, application 15; unmatched co-occurring tokens remain audit-only.
- Phase-G writing package is complete: English Abstract, Methods, PRISMA Results, claim-governance, TQAF, S1â€“S7, Discussion/Conclusion and a QA-passed appendix with 206 unique study rows, 227-report lineage, locked modality/maturity/status distributions and no local-path leakage.
- Final package-level status is `PASS_FOR_REVIEWED_MANUSCRIPT_INTEGRATION`, not submission-ready.
- Git delivery complete: branch `agent/full-corpus-survey-ready`; scientific package commit `2292bfdb3021a3e1dd495ecaa89953350d494405`; delivery-record head `9b29b221213786c9893134a36638c3d9a0739f49`; draft PR `https://github.com/cfdonmez/OISAC_PRISMA_COMST/pull/1`.
- Current phase is reviewed manuscript integration followed by figure/table refresh and final citation/cross-reference/IEEEtran/rendered-PDF QA.
- Local writing package/checkpoint: `07_raporlama/outputs/phase_g_writing_package_2026-08-04/` and `09_kayitlar/checkpoints/reporting_PHASE_G_WRITING_PACKAGE_2026-08-04/`.
- Permanent checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_SURVEY_READY_2026-08-04/`.

> The first-25 block below is retained only as dated audit history and is superseded operationally.

## Historical state â€” Phase D First-25 Human Lock Complete (2026-08-02)

- Phases A, B and C are complete and locked; the extraction universe is **206 included studies**.
- Phase D pilot lock is complete: 5/5 pilot studies are human-approved and locked, 85/85 checklist items passed and 0 pilot items remain open. The pilot-locked v1.0 schema/codebook is authorized and the post-pilot gate is open.
- Canonical pilot workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_pilot_human_locked_2026-08-02/OISAC_PHASE_D_PILOT_HUMAN_LOCKED_2026-08-02.xlsx`; SHA-256 `69462bd05f66c39172494b5e984ee6c245220720ba18027eb1145a0ab77db672`.
- Batch-20 AI-assisted source extraction covers 20 studies / 21 PDFs and contains 208 evidence, 178 metric, 26 trade-off and 340 completed HC rows. Under the user's explicit delegation, 20/20 received final human adjudication and were locked with source-specific caveats preserved.
- Canonical first-25 workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_25_human_locked_2026-08-02/OISAC_PHASE_D_25_STUDIES_HUMAN_LOCKED_2026-08-02.xlsx`; SHA-256 `794ae6c74f61c5b9310e859559f39dd08cd0c1639fa9f53a29b213bbf64f48ca`.
- Cumulative Phase D status: 25/206 source-extracted and 25/206 user-delegated human-approved/locked. The attribution means final approval of the AI-assisted, source-open adjudication and does not claim that the user personally opened or read every PDF.
- The 21 PDF-specific Gemini audits remain a secondary source-audit provenance trail. The later folder-level Gemini answer was not consistently PDF-grounded and did not control final decisions. No project graph digitization or Phase E TQAF was introduced; synthesis has not started.
- Next safest action: continue Phase D extraction for the remaining 181/206 studies in versioned batches under the pilot-locked schema and caveat-preserving QA model.

> The 2026-07-30 pilot-pending state is superseded by this dated block and remains only as audit history.

## Superseded current state â€” Phase D Pilot P01 Human Verification Pending (2026-07-30)

- Historical state at that date: P01 was populated but not approved or locked, P02â€“P05 had not started and full-corpus extraction was blocked.
- This state was superseded by the completed 5/5 pilot human lock and the Batch-20 extraction recorded above.

## Superseded operational state â€” 2026-07-27

- Canonical operational handoff and complete forward roadmap: `START_HERE_OISAC_PRISMA_CURRENT.md`. Every new agent/chat/computer must read it before acting.
- Title/abstract screening is complete.
- Step 5-C27 final title/abstract checkpoint and new-chat handoff created.
- Active baseline: `systematic_review_workflow/03_secim/title_abstract_screening/batch_B13_final_2026-06-22/title_abstract_screening_form_MASTER_BATCH_B13_APPLIED_2026-06-22.csv`.
- Active baseline SHA-256: `5d8b675c54bbed9860b473b435ed5cbce724bb9882a186f1091e09baa1d59ad2`.
- Total master records: 1259.
- Unique `screening_record_id`: 1259; duplicate IDs: 0.
- Screening status distribution: `calibration_resolved` = 50, `batch_resolved` = 1209, `not_screened` = 0.
- Resolved title/abstract decisions: 1259 / 1259.
- Remaining `not_screened`: 0.
- Final decision distribution: `exclude_title_abstract` = 864, `include_for_full_text` = 321, `contextual_only` = 61, `unclear_need_full_text` = 11, `duplicate_or_related_report_flag` = 2.
- Full-text-needed pool = 332 (`include_for_full_text` + `unclear_need_full_text`).
- Contextual corpus = 61; not primary technical evidence.
- Related-report/version watchlist = 3 records: `SCR-00373`, `SCR-00907`, `SCR-01084`.
- Unclear full-text watchlist = 11 records: `SCR-00373`, `SCR-00462`, `SCR-00508`, `SCR-00623`, `SCR-00669`, `SCR-00689`, `SCR-00730`, `SCR-00931`, `SCR-01044`, `SCR-01141`, `SCR-01183`.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Retrieval disposition: 272 reports retrieved for full-text eligibility. The historical checkpoint has 60 `report_not_retrieved` rows; `SCR-01150` is now superseded as an RPT02 exact duplicate of retrieved `SCR-00886`, leaving 59 unresolved RPT01 records. Retrieval dispositions are not full-text eligibility exclusions.
- PRISMA Pre-Full-Text Eligibility Gate Step 1 was user-approved and locked on 2026-07-19.
- B01 full-text eligibility is finalized: P01-P05 complete; 22/22 reviewed and locked; 19 `include_primary`; 3 `exclude_full_text` (`FTX07` = 2, `FTX04` = 1); contextual and unresolved/Hold = 0.
- Operational eligibility progress through B09-P02 lock: 122/272 retrieved reports reviewed; 95 `include_primary`, 3 `retain_contextual`, 24 `exclude_full_text`; 150 retrieved reports remain. B09-P02 is complete at 5/5 primary. These are operational report-level counts, not formal PRISMA flow or final study-level counts.
- Dedicated final eligibility workbooks exist for B01 and B02. B03/B04 approved decisions are preserved in durable logs, but no dedicated B03/B04 final eligibility workbook/checkpoint was found on 2026-07-25. Formalize those decisions without silent re-adjudication before the global eligibility-final lock.
- Current next safest action: source-open compare the submitted B09-P01 records `SCR-00808`, `SCR-00833`, `SCR-00836`, `SCR-00873`, and `SCR-00882`; obtain explicit user approval before locking P01. B09-P02 is locked and B09-P03/P04 remain pending. Preserve completed earlier decisions.
- 2026-07-08 reviewmdS staging update by direct user request: 17 downloaded files were moved into external `reviewmdS` batch folders for 11 records. FT167 PDF was completed; FT172-FT181 were added. Partial tracker now shows include_for_full_text=164, downloaded_pdf=129, PDF needs_download=35, with SCR-00761 as the only remaining MD-only/PDF-missing row. This remains non-canonical staging and does not replace B13 reconciliation.
- Do not use older B12/B11/B10/B09/B08/B07/B06/B05 masters as active baseline.

## Canonical Forward Roadmap â€” 2026-07-30

1. Phase A â€” retrieved-report full-text eligibility. **Complete.**
2. Phase B â€” eligibility consolidation and report-to-study mapping. **Complete.**
3. Phase C â€” formal PRISMA denominator/reason reconciliation and versioned flow population. **Complete.**
4. Phase D â€” data extraction for the 206 included studies. **Current.**
5. Phase E â€” TQAF technical quality/evidence contribution assessment.
6. Phase F â€” taxonomy, metric-governed comparison, tradeoff, maturity, benchmark and research-gap synthesis.
7. Phase G â€” English manuscript and PRISMA checklist reporting.
8. Phase H â€” final cross-file QA and portable handoff.

## Superseded Canonical Forward Roadmap â€” 2026-07-27

The authoritative detailed roadmap is `START_HERE_OISAC_PRISMA_CURRENT.md`. In order:

1. Complete retrieved-report full-text eligibility for B09 through B13 using the locked FTI/FTX rules and User/Codex source-open review workflow; B06, B07 and B08 are complete.
2. Create and QA canonical B03 and B04 eligibility artifacts from the already approved durable decisions; do not silently re-adjudicate them.
3. Consolidate all 272 retrieved-report eligibility decisions and resolve report-level/study-level related-version mapping.
4. Populate the formal PRISMA 2020 flow only after eligibility consolidation; keep the 60 `report_not_retrieved` separate from full-text exclusions.
5. Run data extraction for eligible primary technical reports.
6. Apply the locked TQAF-style technical quality/evidence contribution assessment.
7. Perform taxonomy, metric-governed comparison, rateâ€“sensing tradeoff, validation-maturity, benchmark-readiness and research-gap synthesis.
8. Draft the English manuscript and complete PRISMA checklist/flow reporting.
9. Run final cross-file QA and create a portable handoff for the next computer/agent.

Immediate submitted part: B09-P01 contains `SCR-00808`, `SCR-00833`, `SCR-00836`, `SCR-00873`, `SCR-00882`. Its standalone prompt is `checkpoints/full_text_prompt_packages_B08_B13_2026-07-27/B09/B09_P01_prompt.txt`; B09-P02 is locked and B09-P03/P04 remain pending.

Formal PRISMA flow, extraction, TQAF, synthesis and final included-study counts remain not started/TBD.

> All dated sections below are chronological audit memory. Historical absolute paths and â€œnextâ€ statements do not override the current state and roadmap above.

# 2026-07-19 PRISMA Pre-Full-Text Eligibility Gate Step 1 Durable Note

- Locked criteria: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/full_text_eligibility_criteria_LOCKED_2026-07-19.md`.
- Locked reason codes: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/full_text_exclusion_reason_codes_LOCKED_2026-07-19.csv`.
- Bilingual reports may qualify only when sufficient English full technical content supports reliable assessment; an English abstract alone is insufficient.
- Date eligibility uses the earliest verifiable publisher online/public availability date and the actual 2026-06-22 cutoff; conflicts require adjudication.
- Retracted/withdrawn reports are excluded from primary technical evidence; correction/erratum reports are linked and not independently counted.
- Full-text exclusion primary-reason hierarchy is locked; `FTX09` is residual only. Low quality is handled through TQAF, not exclusion.
- `RPT01` report not retrieved is not a PRISMA 16b full-text exclusion. Related/duplicate/correction reports use report-level mapping dispositions.
- No eligibility assessment or formal PRISMA flow population occurred. Next gate: reviewer/AI/human adjudication process lock.

# Historical Snapshot (Superseded) â€” 2026-07-04 Pre-Retrieval Durable State Clarification

- Canonical main project folder: `C:\Users\fatih\OneDrive - ASKERÃ„Â° FABRÃ„Â°KA VE TERSANE Ã„Â°Ã…ÂLETME A.Ã…Â (ASFAT)\kisiselAlan\prisma2020Review`.
- External staging workspace only: `C:\Users\fatih\OneDrive - ASKERÃ„Â° FABRÃ„Â°KA VE TERSANE Ã„Â°Ã…ÂLETME A.Ã…Â (ASFAT)\kisiselAlan\reviewmdS`; this folder is for PDF/Markdown staging and is not canonical main-project state.
- B13 applied master is the only active baseline: `systematic_review_workflow/03_secim/title_abstract_screening/batch_B13_final_2026-06-22/title_abstract_screening_form_MASTER_BATCH_B13_APPLIED_2026-06-22.csv`.
- B13 SHA-256 remains `5d8b675c54bbed9860b473b435ed5cbce724bb9882a186f1091e09baa1d59ad2`.
- Final B13 full-text-needed pool is 332 = 321 `include_for_full_text` + 11 `unclear_need_full_text`.
- Final B13 unclear list has 11 records: `SCR-00373`, `SCR-00462`, `SCR-00508`, `SCR-00623`, `SCR-00669`, `SCR-00689`, `SCR-00730`, `SCR-00931`, `SCR-01044`, `SCR-01141`, `SCR-01183`.
- External old `reviewmdS` unclear watchlist has 8 rows and is superseded by final B13 unclear=11.
- Related-report/version watchlist has 3 records: `SCR-00373`, `SCR-00907`, `SCR-01084`.
- Contextual corpus has 61 records and is not primary technical evidence.
- `reviewmdS` current tracker has 164 rows and is partial/non-canonical; it is not final B13 retrieval status.
- `reviewmdS` PDF/Markdown inventory must be reconciled against B13 332 before any retrieval continuation.
- PRISMA flow remains TBD / not populated.
- No eligibility assessment, synthesis, included-study count, or PRISMA count population before B13-vs-`reviewmdS` reconciliation.
- Next safest action: Step 5-C28C - read-only B13-vs-`reviewmdS` retrieval reconciliation audit.

# Current State - after Step 5-C26 / B13 Human Decisions Logged

- Step 5-C26 B13 human decisions completed and logged.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B13_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions: 1259 / 1259.
- Remaining not_screened: 0.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions were provisional only; final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next: final title/abstract screening checkpoint / QA before formal PRISMA flow population.

# Current State - after Step 5-C25 / B13 AI Suggestions Generated

- Step 5-C24 B12 human decisions completed and logged.
- B12-applied master is now the active baseline.
- Step 5-C25 B13 AI suggestions generated for 57 not-screened B13 records.
- B13 contains 2 calibration_resolved records that were not re-screened.
- B13 AI suggestions are provisional only; no final human decisions created.
- Master screening form unchanged.
- PRISMA flow counts remain TBD / not populated.
- Next: user/ChatGPT human review of B13 suggestions.
- After B13 human decisions are logged, title/abstract screening should reach 1259/1259 resolved, but do not populate PRISMA flow at this AI-suggestion step.

# Current State - after Step 5-C24 / B12 Human Decisions Logged

- Step 5-C24 B12 human decisions completed and logged.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B12_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions: 1202 / 1259.
- Remaining `not_screened`: 57.
- PRISMA flow counts remain TBD / not populated.
- B12 contains 100 records: 7 inherited calibration_resolved records preserved unchanged and 93 not_screened records updated from human decisions.
- Next task: Step 5-C25 B13 AI-assisted provisional title/abstract screening suggestions.
- B13 expected status must be read from B12-applied master; do not assume 100 records.

# Current State - after Step 5-C23 / B12 AI Suggestions

- Step 5-C22 B11 human decisions completed and logged.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B11_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions: 1109 / 1259.
- Remaining not_screened: 150.
- PRISMA flow counts remain TBD / not populated.
- Step 5-C23 B12 AI suggestions generated for 93 not-screened B12 records.
- B12 contains 7 calibration_resolved records that were not re-screened.
- B12 AI suggestions are provisional only; no final human decisions created.
- Master screening form unchanged.
- Next: user/ChatGPT human review of B12 suggestions.

# Current State - after Step 5-C22 / B11 Human Decisions Logged

- Step 5-C22 B11 human decisions completed and logged.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B11_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions: 1109 / 1259.
- Remaining not_screened: 150.
- B11 final human decisions: 56 include_for_full_text, 32 exclude_title_abstract, 10 contextual_only, 1 unclear_need_full_text, 1 duplicate_or_related_report_flag.
- B11 related-report flag: SCR-01084, likely related to SCR-01054, to be mapped during full-text/related-report stage.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- B12 readiness note: B12 has 100 records, with 93 not_screened and 7 calibration_resolved records inherited from calibration.
- Next task: Step 5-C23 B12 AI-assisted provisional title/abstract screening suggestions.

# Current State - after Step 5-C21 / B11 AI Suggestions Generated

- Step 5-C20 B10 human decisions completed and logged.
- B10-applied master is the active baseline.
- Step 5-C21 B11 AI suggestions generated for 100 not-screened B11 records.
- B11 AI suggestions are provisional only; no final human decisions created.
- B11 AI suggestion distribution: include_for_full_text=55, exclude_title_abstract=32, contextual_only=10, unclear_need_full_text=2, duplicate_or_related_report_flag=1.
- Master screening form unchanged.
- PRISMA flow counts remain TBD / not populated.
- Current draft tracking remains 1009/1259 resolved and 250 not_screened until B11 human decisions are logged.
- Next: user/ChatGPT human review of B11 suggestions.

# Current State - after Step 5-C20 / B10 human decisions logged

- Step 5-C20 B10 human decisions completed and logged.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B10_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions: 1009 / 1259.
- Remaining not_screened: 250.
- B10 final human decisions: 80 include_for_full_text, 13 contextual_only, 5 exclude_title_abstract, 1 duplicate_or_related_report_flag, 1 unclear_need_full_text.
- B10 related-report flag: SCR-00907, likely related to SCR-00901, to be mapped during full-text/related-report stage.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: Step 5-C21 B11 AI-assisted provisional title/abstract screening suggestions.

# Current State - after Step 5-C19 / B10 AI Suggestions Generated

- Step 5-C18 B09 human decisions completed and logged.
- B09-applied master is the active baseline for B10 AI suggestions.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B09_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions remain 909 / 1259 until B10 human decisions are logged.
- Remaining not_screened remains 350 until B10 human decisions are logged.
- Step 5-C19 B10 AI suggestions generated for 100 not-screened B10 records.
- B10 expected ID span is `SCR-00901` - `SCR-01001` because `SCR-00958` is absent in master; total B10 count remains 100.
- B10 AI suggestions are provisional only; no final human decisions created.
- Master screening form unchanged.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: user/ChatGPT human review of B10 suggestions.

# Current State - after Step 5-C18 / B09 Human Decisions Logged

- Step 5-C18 B09 human decisions completed and logged.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B09_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions: 909 / 1259.
- Remaining not_screened: 350.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: Step 5-C19 B10 AI-assisted provisional title/abstract screening suggestions.

# Current State - after Step 5-C17 / B09 AI Suggestions Generated

- Step 5-C16 B08 human decisions completed and logged.
- B08-applied master is the active baseline for B09 AI suggestions.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B08_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions remain 809 / 1259 until B09 human decisions are logged.
- Remaining not_screened remains 450 until B09 human decisions are logged.
- Step 5-C17 B09 AI suggestions generated for 100 not-screened B09 records.
- B09 AI suggestions are provisional only; no final human decisions created.
- Master screening form unchanged.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: user/ChatGPT human review of B09 suggestions.

# Current State - after Step 5-C16 / before Step 5-C17

- Step 5-C16 B08 human decisions completed and logged.
- Active baseline: `title_abstract_screening_form_MASTER_BATCH_B08_APPLIED_2026-06-22.csv`.
- Total master records: 1259.
- Resolved title/abstract decisions: 809 / 1259.
- Remaining not_screened: 450.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: Step 5-C17 B09 AI-assisted provisional title/abstract screening suggestions.
- 2026-06-29 full-text retrieval update: FT109-FT132 arasindaki 24 yeni include PDF'i ../reviewmdS/01_fulltext/include/B04-B07/ altina tasindi. B08 final kararlari da takip listesine eklendi; B08-applied tracker durumunda include_for_full_text=143, downloaded PDF=81, needs_download=62, unclear watchlist=8 oldu. B09 dahil edilmedi.
- 2026-06-29 ikinci full-text retrieval update: FT133-FT157 araliginda 25 kaydin artifact'leri ../reviewmdS/01_fulltext/include/B02-B08/ altina tasindi; 24 PDF ve 17 ham Markdown eklendi. Current retrieval status: include_for_full_text=143; downloaded PDF=105; PDF needs_download=38; SCR-00761 has raw Markdown only and still needs PDF. B09 dahil edilmedi.
- 2026-06-30 B09 retrieval guncellemesi: B09 final human decisions incelendi; 21 yeni include_for_full_text kaydi ../reviewmdS tracker ana needs_download listesine eklendi. Current retrieval status: include_for_full_text=164; downloaded PDF=105; PDF needs_download=59; SCR-00761 has raw Markdown only; B09 unclear kaydi yok. B10 ve sonrasi dahil edilmedi.
- 2026-06-30 B09 acik erisim PDF guncellemesi: FT158-FT163 araliginda 6 B09 PDF'i ../reviewmdS/01_fulltext/include/B09/ altina tasindi; current retrieval status: include_for_full_text=164, downloaded PDF=111, PDF needs_download=53. Kalan 15 B09 DOI sayfasi indirme icin acildi; B10 ve sonrasi dahil edilmedi.
- 2026-06-30 B09 ek indirme kontrolu: FT164-FT171 araliginda 8 B09 artifact'i ../reviewmdS/01_fulltext/include/B09/ altina tasindi; 7 PDF ve 8 ham Markdown eklendi. Current retrieval status: include_for_full_text=164, downloaded PDF=118, PDF needs_download=46; B09 needs_download=8; SCR-00761 and SCR-00884 have raw Markdown only. B10 ve sonrasi dahil edilmedi.

# Current State - after Step 5-C15 / B08 AI Suggestions Generated

- Step 5-C14B B07 human_notes exact correction completed.
- Step 5-C14C post-B07 correction state alignment completed.
- Active baseline before B08 human logging: `title_abstract_screening_form_MASTER_BATCH_B07_APPLIED_CORRECTED_2026-06-22.csv`.
- Uncorrected B07-applied master is historical/deprecated and must not be used for forward processing.
- B06-applied master is historical and must not be used for B08 forward processing.
- Step 5-C15 B08 AI suggestions generated for 100 not-screened B08 records.
- B08 AI suggestions are provisional only; no final human decisions created.
- Master screening form unchanged.
- Total master records: 1259.
- Resolved title/abstract decisions remain 709 / 1259.
- Remaining not_screened remains 550 until B08 human decisions are logged.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Current full-text retrieval tracker copy remains under `../reviewmdS/PRISMA_full_text_retrieval_tracking_2026-06-27/full_text_retrieval_tracker_CURRENT.csv`.
- Next task: user/ChatGPT human review of B08 suggestions.

# CURRENT STATE - after Step 5-C14C / before Step 5-C15

- Step 5-C14B B07 human_notes exact correction completed successfully.
- Step 5-C14C state alignment completed.
- 2026-06-27 full-text retrieval tracking snapshot is maintained under `../reviewmdS/PRISMA_full_text_retrieval_tracking_2026-06-27/`.
- Current full-text retrieval status after 2026-06-30 B09 extra download check: include_for_full_text=164; downloaded PDF present in reviewmdS=118; PDF needs_download=46; two needs_download records (SCR-00761 and SCR-00884) have raw Markdown only; separate unclear_need_full_text watchlist=8 with 1 PDF already present. B10 and later are not included in this retrieval update.
- Rolling tracker to refresh after each new applied screening batch: `systematic_review_workflow/03_secim/full_text_retrieval_tracking/full_text_retrieval_tracker_CURRENT.csv`.
- Active baseline for all forward processing:
  `systematic_review_workflow/03_secim/title_abstract_screening/batch_B07_final_corrected_2026-06-22/title_abstract_screening_form_MASTER_BATCH_B07_APPLIED_CORRECTED_2026-06-22.csv`
- Do not use the uncorrected B07-applied master for forward processing.
- Do not use the B06-applied master for forward processing.
- Total master records: 1259.
- Resolved title/abstract decisions: 709 / 1259.
- Remaining not_screened: 550.
- Completed/logged: Calibration + B01 + B02 + B03 + B04 + B05 + B06 + B07.
- B07 final decisions: 14 include_for_full_text, 78 exclude_title_abstract, 5 contextual_only, 3 unclear_need_full_text.
- B07 human_notes correction changed only human_notes; decisions, reason codes, flags and PRISMA status did not change.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: Step 5-C15 B08 AI-assisted provisional title/abstract screening suggestions.
- B08 expected status: 100 total records, 100 not_screened, 0 calibration_resolved, 0 batch_resolved.

# Current State - after Step 5-C14b / B07 Human Notes Corrected

- Step 5-C14b B07 human_notes correction completed.
- Decisions/counts were already correct; correction only restored exact human_notes from the ChatGPT/User correction patch.
- Corrected B07-applied master is now the active baseline: title_abstract_screening_form_MASTER_BATCH_B07_APPLIED_CORRECTED_2026-06-22.csv.
- Total master records: 1259.
- Resolved title/abstract decisions: 709 / 1259 draft tracking only.
- Remaining not_screened: 550.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: Step 5-C15 B08 AI-assisted provisional title/abstract screening suggestions using the corrected B07-applied master.

# Current State - after Step 5-C14 / B07 Human Decisions Logged

- Step 5-C13 B07 AI suggestions generated.
- Step 5-C14 B07 human decisions completed and logged.
- B07-applied master is now the active baseline: title_abstract_screening_form_MASTER_BATCH_B07_APPLIED_2026-06-22.csv.
- Total master records: 1259.
- Resolved title/abstract decisions: 709 / 1259 draft tracking only.
- Remaining not_screened: 550.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: Step 5-C15 B08 AI-assisted provisional title/abstract screening suggestions.
- B08 expected status should be checked from the B07-applied master before suggestion generation.

# Current State Ã¢â‚¬â€ after Step 5-C13 / B07 AI Suggestions Generated

- Step 5-C12 B06 human decisions completed and logged.
- Step 5-C12.5 Pre-B07 checkpoint completed.
- Active baseline before B07 human logging: title_abstract_screening_form_MASTER_BATCH_B06_APPLIED_2026-06-22.csv.
- Step 5-C13 B07 AI suggestions generated for 100 not-screened B07 records.
- B07 AI suggestions are provisional only; no final human decisions created.
- Master screening form unchanged.
- Total master records: 1259.
- Resolved title/abstract decisions remain 609 / 1259.
- Remaining not_screened remains 650 until B07 human decisions are logged.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: user/ChatGPT human review of B07 suggestions.

# Current State Ã¢â‚¬â€ after Step 5-C12 / before Step 5-C13

- Step 5-C12 B06 human decisions completed and logged.
- Active baseline: title_abstract_screening_form_MASTER_BATCH_B06_APPLIED_2026-06-22.csv.
- Total master records: 1259.
- Resolved title/abstract decisions: 609 / 1259.
- Remaining not_screened: 650.
- PRISMA flow counts remain TBD / not populated.
- AI suggestions are not final screening decisions.
- Final title/abstract decisions are human/User/ChatGPT decisions.
- Contextual records are not primary technical evidence.
- Next task: Step 5-C13 B07 AI-assisted provisional title/abstract screening suggestions.
- B07 expected status: 100 total records, 100 not_screened, 0 calibration_resolved, 0 batch_resolved.

# Codex Memory Bank - O-ISAC PRISMA Review

Son guncelleme: 2026-07-01

Bu dosya, Codex oturumlari icin hizli calisma hafizasidir. Birincil kaynak `../../PROJECT_CONTEXT_OISAC_PRISMA.md` dosyasidir. Bu dosya ile proje baglami celisirse proje baglami esas alinir.

## 2026-06-22 Step 5-C12 B06 Human Decisions Completed

- Step 5-C11 B06 AI suggestions generated.
- Step 5-C12 B06 human decisions completed and logged.
- B06-applied master is now the active baseline.
- Resolved title/abstract decisions are 609/1259 draft tracking only.
- Remaining not_screened is 650.
- PRISMA flow counts remain TBD / not populated.
- Next: Step 5-C13 B07 AI-assisted provisional title/abstract screening suggestions.

## 2026-06-26 Step 5-C11 B06 Reviewed-85 Human Review Partial Update

- User-provided `B06_reviewed_85_human_decisions_patch_2026-06-25.csv` was applied to `batch_B06_human_review_workbook_2026-06-22.csv` only.
- The patch contained 85 resolved B06 records: 75 newly pending records were updated and the prior 10 high-priority resolved records matched exactly.
- B06 human review workbook status: 85 resolved, 15 pending among 100 B06 not_screened records.
- Cumulative reviewed decision distribution: exclude_title_abstract=80, include_for_full_text=2, contextual_only=2, unclear_need_full_text=1.
- Cumulative reviewed reason code distribution: EX05=45, EX01=21, EX06=6, EX03=3, EX07=2, EX02=1, EX04=1, EX08=1, IN03=1, IN05=1, CTX01=1, CTX05=1, UN01=1.
- Agent-human comparison among 85 resolved records: exact agreement=79, decision disagreement=3, same-decision reason refinement=3.
- Remaining B06 pending records: 15 low-priority include candidates.
- Master screening form unchanged; master-applied resolved so far remains 509/1259 and remaining not_screened remains 750 until B06 decisions are formally logged.
- PRISMA flow counts remain TBD.

## 2026-06-25 Step 5-C11 B06 High-Priority Human Review Partial Update

- User-provided `B06_high_priority_10_human_decisions_patch_2026-06-25.csv` was applied to `batch_B06_human_review_workbook_2026-06-22.csv` only.
- B06 human review workbook status: 10 resolved, 90 pending among 100 B06 not_screened records.
- Reviewed high-priority decision distribution: exclude_title_abstract=6, include_for_full_text=2, contextual_only=1, unclear_need_full_text=1.
- Reviewed high-priority reason code distribution: EX01=2, EX03=2, EX05=2, IN03=1, IN05=1, CTX05=1, UN01=1.
- Agent-human comparison: exact agreement=4, decision disagreement=3, same-decision reason refinement=3.
- Master screening form unchanged; master-applied resolved so far remains 509/1259 and remaining not_screened remains 750 until B06 decisions are formally logged.
- PRISMA flow counts remain TBD.

## 2026-06-22 Step 5-C11 B06 AI Suggestions Generated

- Step 5-C10 B05 human decisions completed and logged.
- B05-applied master is now the active baseline.
- Step 5-C11 B06 AI suggestions generated for 100 not-screened B06 records.
- B06 AI suggestions are provisional only; no final human decisions created.
- Master screening form unchanged.
- PRISMA flow counts remain TBD.
- Next: user/ChatGPT human review of B06 suggestions.

## 2026-06-22 Step 5-C10 B05 Human Decisions Completed

- Step 5-C10 B05 human decisions completed.
- Resolved so far: 50 calibration + 69 B01 + 93 B02 + 100 B03 + 99 B04 + 98 B05 = 509 title/abstract decisions.
- Remaining not_screened: 750.
- B05-applied master copy created: `title_abstract_screening_form_MASTER_BATCH_B05_APPLIED_2026-06-22.csv`.
- Next: Step 5-C11/B06 AI-assisted provisional suggestions.
- PRISMA flow not yet populated.

## 2026-06-25 Step 5-C9 B05 Human Review Completed In Workbook

- User-provided human decisions were recorded for the final 26 medium-priority and 9 low-priority B05 records in `batch_B05_human_review_workbook_2026-06-22.csv`.
- B05 human review workbook status: 98 resolved, 0 pending among 98 B05 not_screened records.
- Final B05 human decision distribution: exclude_title_abstract=79, include_for_full_text=16, contextual_only=2, unclear_need_full_text=1.
- Final B05 reason code distribution: EX05=45, EX01=14, EX07=8, EX03=5, EX06=4, IN05=5, IN04=4, IN02=4, EX04=2, CTX02=2, IN03=2, EX02=1, IN06=1, UN01=1.
- Final B05 agent-human divergences: SCR-00415 unclear_need_full_text/UN01 -> exclude_title_abstract/EX01; SCR-00451 unclear_need_full_text/UN01 -> include_for_full_text/IN02; SCR-00460 reason code IN01 -> IN03 while decision stayed include_for_full_text; SCR-00483 contextual_only/CTX02 -> exclude_title_abstract/EX05.
- Master screening form unchanged in this workbook-only completion step.
- Master-applied resolved so far remains 411/1259; if B05 decisions are formally logged next, human-decided tracking would become 509/1259 with 750 records remaining.
- PRISMA flow not updated.
- Next: Step 5-C10-style B05 human decisions logging/master update should apply only B05 decisions to a new master copy, produce final B05 summary/QA, and leave PRISMA flow untouched until intended.

## 2026-06-25 Step 5-C9 B05 Medium-Priority Human Review Partial Update 2

- User-provided human decisions were recorded for the second 25 medium-priority B05 records in `batch_B05_human_review_workbook_2026-06-22.csv`.
- This subset decision distribution: exclude_title_abstract=25, include_for_full_text=0, contextual_only=0, unclear_need_full_text=0.
- This subset reason code distribution: EX05=11, EX01=5, EX07=4, EX03=2, EX06=2, EX02=1.
- No new agent-human decision or reason-code disagreement was identified in this subset.
- B05 human review workbook status: 63 resolved, 35 pending among 98 B05 not_screened records.
- Pending B05 priority distribution: medium=26, low=9.
- Cumulative B05 human decision distribution so far: exclude_title_abstract=54, include_for_full_text=6, contextual_only=2, unclear_need_full_text=1.
- Master screening form unchanged; master-applied resolved so far remains 411/1259 and remaining not_screened remains 848 until B05 decisions are formally logged.
- PRISMA flow not updated.

## 2026-06-25 Step 5-C9 B05 Medium-Priority Human Review Partial Update 1

- User-provided human decisions were recorded for the first 25 medium-priority B05 records in `batch_B05_human_review_workbook_2026-06-22.csv`.
- This subset decision distribution: exclude_title_abstract=25, include_for_full_text=0, contextual_only=0, unclear_need_full_text=0.
- This subset reason code distribution: EX05=15, EX01=4, EX03=2, EX07=3, EX06=1.
- No new agent-human decision or reason-code disagreement was identified in this subset.
- B05 human review workbook status: 38 resolved, 60 pending among 98 B05 not_screened records.
- Cumulative B05 human decision distribution so far: exclude_title_abstract=29, include_for_full_text=6, contextual_only=2, unclear_need_full_text=1.
- Master screening form unchanged; master-applied resolved so far remains 411/1259 and remaining not_screened remains 848 until B05 decisions are formally logged.
- PRISMA flow not updated.

## 2026-06-25 Step 5-C9 B05 High-Priority Human Review Partial Update

- User-provided human decisions were recorded for the 13 high-priority B05 records in `batch_B05_human_review_workbook_2026-06-22.csv`.
- Reviewed high-priority decision distribution: include_for_full_text=6, exclude_title_abstract=4, contextual_only=2, unclear_need_full_text=1.
- Reviewed high-priority reason code distribution: CTX02=2, EX05=2, EX01=1, EX03=1, IN02=2, IN03=1, IN04=1, IN05=2, UN01=1.
- B05 human review workbook status: 13 resolved, 85 pending among 98 B05 not_screened records.
- Notable agent-human changes: SCR-00415 unclear_need_full_text/UN01 -> exclude_title_abstract/EX01; SCR-00451 unclear_need_full_text/UN01 -> include_for_full_text/IN02; SCR-00460 reason code IN01 -> IN03 while decision stayed include_for_full_text; SCR-00483 contextual_only/CTX02 -> exclude_title_abstract/EX05.
- Master screening form unchanged; master-applied resolved so far remains 411/1259 and remaining not_screened remains 848 until B05 decisions are formally logged.
- PRISMA flow not updated.

## 2026-06-24 Step 5-C9 B05 AI Suggestions Generated

- Step 5-C8 B04 human decisions completed.
- Step 5-C9 B05 AI suggestions generated for 98 not-screened B05 records.
- Next: user/ChatGPT human review of B05 suggestions.
- No PRISMA flow update yet.

## 2026-06-24 Step 5-C7 B04 Medium-Priority Human Review Partial Update 2

- User-provided human decisions were recorded for medium-priority B04 records 26-50 in `batch_B04_human_review_workbook_2026-06-22.csv`.
- This subset decision distribution: exclude_title_abstract=21, contextual_only=4, include_for_full_text=0, unclear_need_full_text=0.
- This subset reason code distribution: EX05=11, EX01=9, EX06=1, CTX01=2, CTX05=2.
- B04 human review workbook status: 70 resolved, 29 pending.
- B04 progress detail: high-priority completed 20/20; medium-priority completed 50/64; low-priority pending 15/15.
- Master screening form unchanged; master-applied resolved so far remains 312/1259 and remaining not_screened remains 947 until B04 decisions are formally logged.
- PRISMA flow not updated.

## 2026-06-24 Step 5-C7 B04 Medium-Priority Human Review Partial Update 1

- User-provided human decisions were recorded for the first 25 medium-priority B04 records in `batch_B04_human_review_workbook_2026-06-22.csv`.
- This subset decision distribution: exclude_title_abstract=24, include_for_full_text=1, contextual_only=0, unclear_need_full_text=0.
- This subset reason code distribution: EX05=11, EX01=9, EX07=1, EX08=1, EX03=1, EX06=1, IN03=1.
- B04 human review workbook status: 45 resolved, 54 pending.
- B04 progress detail: high-priority completed 20/20; medium-priority completed 25/64; low-priority pending 15/15.
- Agent-human refinement in this subset: SCR-00306 reason code EX01 -> EX05 while decision stayed exclude_title_abstract.
- Master screening form unchanged; master-applied resolved so far remains 312/1259 and remaining not_screened remains 947 until B04 decisions are formally logged.
- PRISMA flow not updated.

## 2026-06-24 Step 5-C7 B04 High-Priority Human Review Partial Update

- User-provided human decisions were recorded for the 20 high-priority B04 records in `batch_B04_human_review_workbook_2026-06-22.csv`.
- Reviewed high-priority decision distribution: exclude_title_abstract=17, contextual_only=1, include_for_full_text=1, unclear_need_full_text=1.
- Reviewed high-priority reason code distribution: EX05=11, EX01=2, EX03=2, EX04=2, CTX02=1, IN02=1, UN01=1.
- B04 human review workbook status: 20 resolved, 79 pending.
- Notable agent-human changes: SCR-00351 exclude_title_abstract/EX05 -> contextual_only/CTX02; SCR-00382 unclear_need_full_text/UN01 -> include_for_full_text/IN02; SCR-00381 reason code EX03 -> EX01 while decision stayed exclude_title_abstract.
- Master screening form unchanged; master-applied resolved so far remains 312/1259 and remaining not_screened remains 947 until B04 decisions are formally logged.
- PRISMA flow not updated.

## 2026-06-22 Step 5-C7 B04 AI Suggestions Generated

- Step 5-C6 B03 human decisions completed.
- Step 5-C7 B04 AI suggestions generated for 99 not-screened B04 records.
- B04 observed status: total=100, calibration_resolved=1, batch_resolved=0, not_screened processed=99.
- B04 AI suggestion distribution: exclude_title_abstract=75, include_for_full_text=17, contextual_only=5, unclear_need_full_text=2.
- Human review required: 99; high-risk flagged: 20.
- Resolved so far remains 312/1259 draft tracking only; remaining not_screened remains 947 until B04 human decisions are logged.
- Next: user/ChatGPT human review of B04 suggestions.
- No PRISMA flow update yet.

## 2026-06-22 Step 5-C6 B03 Human Decisions Completed

- Step 5-C6 B03 human decisions completed.
- Resolved so far: 50 calibration + 69 B01 + 93 B02 + 100 B03 = 312 title/abstract decisions.
- Remaining not_screened: 947.
- B03-applied master copy created: `title_abstract_screening_form_MASTER_BATCH_B03_APPLIED_2026-06-22.csv`.
- Next: Step 5-C7/B04 AI-assisted provisional suggestions.
- PRISMA flow not yet populated.

## 2026-06-24 Step 5-C5 Batch B03 Human Review Completed

- User-provided human decisions were recorded for the remaining 33 B03 records in `batch_B03_human_review_workbook_2026-06-22.csv`.
- B03 human review workbook status: 100 resolved, 0 pending.
- Final B03 human decision distribution: exclude_title_abstract=73, include_for_full_text=21, contextual_only=6, unclear_need_full_text=0.
- Final B03 reason code distribution: EX05=46, EX01=15, EX02=2, EX03=4, EX04=1, EX06=1, EX07=3, EX08=1, IN02=2, IN03=3, IN04=6, IN05=8, IN06=2, CTX01=2, CTX02=4.
- Actual agent-human divergences in B03: SCR-00224 contextual_only/CTX02 -> exclude_title_abstract/EX05; SCR-00268 exclude_title_abstract/EX05 -> include_for_full_text/IN05; SCR-00240 reason code EX06 -> EX08 while decision stayed exclude_title_abstract.
- Human-decided title/abstract tracking after B03 would be 312/1259 with 947 remaining once B03 decisions are formally logged to the master in Step 5-C6.
- Master screening form unchanged in this workbook-only completion step; PRISMA flow not updated.
- Next: Step 5-C6 B03 human decisions logging/master update should apply only B03 records to a new master copy, produce final B03 summary/QA, and leave PRISMA flow untouched.

## 2026-06-24 Step 5-C5 Batch B03 Medium-Priority Human Review Partial Update 2

- User-provided human decisions were recorded for medium-priority B03 records 26-50 in `batch_B03_human_review_workbook_2026-06-22.csv`.
- This subset decision distribution: exclude_title_abstract=24, contextual_only=1, include_for_full_text=0, unclear_need_full_text=0.
- Subset reason code distribution: EX05=14, EX01=6, EX03=1, EX04=1, EX06=1, EX07=1, CTX01=1.
- SCR-00266 was retained as contextual_only/CTX01 for fiber-based integrated sensing and communication review/context, not primary evidence.
- B03 human review workbook status after this update: 67 resolved, 33 pending.
- Cumulative B03 human decision distribution: exclude_title_abstract=61, contextual_only=5, include_for_full_text=1, unclear_need_full_text=0.
- No new agent-human decision/code divergence in this subset.
- Master screening form unchanged; PRISMA flow not updated.
- Next: continue B03 human review for the remaining 33 records.

## 2026-06-24 Step 5-C5 Batch B03 Medium-Priority Human Review Partial Update 1

- User-provided human decisions were recorded for the first 25 medium-priority B03 records in `batch_B03_human_review_workbook_2026-06-22.csv`.
- This medium-priority subset was 25/25 exclude_title_abstract.
- Subset reason code distribution: EX05=15, EX01=7, EX03=1, EX07=1, EX08=1.
- B03 human review workbook status after this update: 42 resolved, 58 pending.
- Cumulative B03 human decision distribution: exclude_title_abstract=37, contextual_only=4, include_for_full_text=1, unclear_need_full_text=0.
- New agent-human code change: SCR-00240 EX06 -> EX08.
- Master screening form unchanged; PRISMA flow not updated.
- Next: continue B03 human review for the remaining 58 medium/low-priority records.

## 2026-06-24 Step 5-C5 Batch B03 High-Priority Human Review Partial Update

- User-provided human decisions were recorded for the 17 high-priority B03 records in `batch_B03_human_review_workbook_2026-06-22.csv`.
- B03 human review workbook status: 17 resolved, 83 pending.
- Reviewed high-priority decision distribution: exclude_title_abstract=12, contextual_only=4, include_for_full_text=1, unclear_need_full_text=0.
- Reviewed high-priority reason code distribution: EX05=8, EX02=2, EX03=2, CTX02=4, IN05=1.
- Important agent-human changes: SCR-00224 CTX02/contextual_only -> EX05/exclude_title_abstract; SCR-00268 EX05/exclude_title_abstract -> IN05/include_for_full_text.
- Master screening form unchanged; PRISMA flow not updated.
- Next: continue B03 human review for the remaining 83 medium/low-priority records.

## 2026-06-22 Step 5-C5 Batch B03 AI Suggestions Completed

- Step 5-C4 B02 human decisions completed.
- Step 5-C5 B03 AI suggestions generated for 100 not-screened B03 records.
- B03 AI suggestion distribution: exclude_title_abstract=73, include_for_full_text=20, contextual_only=7, unclear_need_full_text=0.
- Resolved so far remains 212/1259 until B03 human decisions are logged.
- Remaining not_screened remains 1047.
- Next: user/ChatGPT human review of B03 suggestions.
- No PRISMA flow update yet.

## 2026-06-22 Step 5-C4 Batch B02 Human Decisions Completed

- Step 5-C4 B02 human decisions completed.
- Resolved so far: 50 calibration + 69 B01 + 93 B02 = 212 title/abstract decisions.
- Remaining not_screened: 1047.
- B02 human decision distribution: exclude_title_abstract=77, include_for_full_text=15, contextual_only=1.
- B02-applied master copy created: `title_abstract_screening_form_MASTER_BATCH_B02_APPLIED_2026-06-22.csv`.
- Next: Step 5-C5/B03 AI-assisted provisional suggestions.
- PRISMA flow not yet populated.

## 2026-06-24 Step 5-C3 Batch B02 Human Review Completed

- User-provided human decisions were recorded for the final 25 B02 records in `batch_B02_human_review_workbook_2026-06-22.csv`.
- B02 human review workbook status: 93 resolved, 0 pending.
- B02 human decision distribution: exclude_title_abstract=77, include_for_full_text=15, contextual_only=1, unclear_need_full_text=0.
- B02 final reason code distribution: EX05=48, EX01=21, EX03=3, EX04=2, EX06=2, EX07=1, IN01=1, IN02=3, IN03=1, IN04=4, IN05=6, CTX05=1.
- Important agent-human changes captured during B02 review include SCR-00171 UN01->EX03, SCR-00177 CTX02->IN05, SCR-00193 CTX01->CTX05, SCR-00198 EX02->EX05, SCR-00166 EX02->EX05, and SCR-00156 EX05->EX03.
- Human-decided title/abstract tracking after B02 = 212/1259, with 1047 remaining if B02 decisions are formally applied to the master.
- Master screening form unchanged in this workbook-only step; master-applied resolved count remains 119/1259 until B02 decision logging/master update.
- PRISMA flow not updated; next expected step is Step 5-C4 B02 human decisions logging/master update handoff.

## 2026-06-24 Step 5-C3 Batch B02 Partial Human Review Update 3

- User-provided human decisions were recorded for medium-priority B02 records 26-50 in `batch_B02_human_review_workbook_2026-06-22.csv`.
- B02 human review workbook status: 68 resolved, 25 pending.
- Cumulative resolved distribution: 66 exclude_title_abstract, 2 include_for_full_text.
- Cumulative resolved reason code distribution: EX05=43, EX01=17, EX04=2, EX03=3, IN01=1, IN05=1, EX07=1.
- This update resolved all 25 records as exclude_title_abstract, mainly RF/wireless ISAC without optical/photonic platform (EX01), generic photonic/device/material/platform records (EX05), one pure optical sensing/measurement record (EX03), and one proceedings-level record (EX07).
- Master screening form unchanged; PRISMA flow not updated.
- Next: continue user/ChatGPT human review for the remaining 25 B02 records.

## 2026-06-24 Step 5-C3 Batch B02 Partial Human Review Update 2

- User-provided human decisions were recorded for the first 25 medium-priority B02 records in `batch_B02_human_review_workbook_2026-06-22.csv`.
- B02 human review workbook status: 43 resolved, 50 pending.
- Cumulative resolved distribution: 41 exclude_title_abstract, 2 include_for_full_text.
- Cumulative resolved reason code distribution: EX05=27, EX01=10, EX04=2, EX03=2, IN01=1, IN05=1.
- This update retained SCR-00129 as include_for_full_text/IN01 under the conservative explicit mid-infrared integrated sensing and communication rule.
- Master screening form unchanged; PRISMA flow not updated.
- Next: continue user/ChatGPT human review for the remaining 50 B02 records.

## 2026-06-24 Step 5-C3 Batch B02 Partial Human Review Update

- User-provided human decisions were recorded for 18 high-priority B02 records in `batch_B02_human_review_workbook_2026-06-22.csv`.
- B02 human review workbook status: 18 resolved, 75 pending.
- Resolved distribution in this update: 17 exclude_title_abstract, 1 include_for_full_text.
- Reason code distribution in this update: EX05=13, EX04=2, EX01=1, EX03=1, IN05=1.
- Important agent-human change: SCR-00177 changed from contextual_only/CTX02 to include_for_full_text/IN05.
- Master screening form unchanged; PRISMA flow not updated.
- Next: continue user/ChatGPT human review for the remaining 75 B02 records.

## 2026-06-22 Step 5-C3 Batch B02 AI Suggestions Completed

- Step 5-C2D pre-B02 audit completed.
- Step 5-C3 B02 AI suggestions generated for not-screened B02 records only.
- B02 observed counts: total 100, calibration_resolved 7, not_screened processed 93.
- B02 AI suggestion distribution: 14 include_for_full_text, 76 exclude_title_abstract, 2 contextual_only, 1 unclear_need_full_text.
- Next: user/ChatGPT human review of B02 suggestions.
- Master screening form unchanged; no PRISMA flow update yet.

## 2026-06-22 Step 5-C2D Pre-B02 Global Audit Completed

- Whole workflow audit before B02 completed.
- Pre-B02 global-normalized master created.
- B02 baseline: `systematic_review_workflow/03_secim/title_abstract_screening/pre_B02_global_audit_2026-06-22/title_abstract_screening_form_MASTER_PRE_B02_GLOBAL_NORMALIZED_2026-06-22.csv`.
- Resolved so far: 119/1259.
- Remaining: 1140.
- PRISMA flow not updated; counts remain TBD in the formal flow file.
- Next: Step 5-C3 B02 AI-assisted provisional suggestions.

## 2026-06-23 Step 5-C2b Batch B01 Normalization Cleanup Completed

- B01 human decisions completed.
- B01 final decision fields normalized.
- Normalized master copy created under `systematic_review_workflow/03_secim/title_abstract_screening/batch_B01_final_normalized_2026-06-22/`.
- Resolved so far: 119/1259.
- Remaining: 1140.
- PRISMA flow not updated; counts remain TBD in the formal flow file.
- Next: B02 AI-assisted provisional suggestions.

## 2026-06-23 Step 5-C2 Batch B01 Human Decisions Completed

- Step 5-C2 B01 human decisions completed.
- B01 human title/abstract decisions were logged from the authoritative patch file and applied to a new B01-applied master copy.
- Resolved so far: 50 calibration + 69 B01 = 119 title/abstract decisions.
- Remaining not_screened: 1140.
- B01 completed; B02 pending.
- PRISMA flow not updated; counts remain TBD in the formal flow file.
- Next: Step 5-C3/B02 AI-assisted provisional suggestions.

## 2026-06-23 Step 5-C1 Batch B01 Partial Human Review Update

- User-provided human decisions were recorded for the first 20 medium-priority B01 records.
- B01 human review workbook status: 20 resolved, 49 pending.
- Resolved distribution in this update: 18 exclude_title_abstract, 2 include_for_full_text.
- Pattern confirmed: generic photonic component/metasurface/resonator/laser/modulator records -> EX05; RF-only ISAC/JCR -> EX01; direct fiber or photonics-assisted ISAC -> IN04/IN05.
- Master screening forms unchanged; PRISMA flow not updated.
- Next: continue user/ChatGPT human review for remaining 49 B01 records.

## 2026-06-23 Step 5-C1 Batch B01 Partial Human Review Update 2

- User-provided human decisions were recorded for B01 medium-priority records 21-40.
- B01 human review workbook status: 40 resolved, 29 pending.
- Cumulative resolved distribution: 37 exclude_title_abstract, 3 include_for_full_text.
- Cumulative resolved code distribution: EX05=25, EX01=10, EX03=1, EX02=1, IN04=1, IN05=1, IN02=1.
- Master screening forms unchanged; PRISMA flow not updated.
- Next: continue user/ChatGPT human review for remaining 29 B01 records.

## 2026-06-23 Step 5-C1 Batch B01 Human Review Completed

- User-provided human decisions were recorded for all 69 not_screened B01 records.
- B01 human review workbook status: 69 resolved, 0 pending.
- Final B01 human decision distribution: 54 exclude_title_abstract, 14 include_for_full_text, 1 contextual_only, 0 unclear_need_full_text.
- Final B01 reason code distribution: EX05=37, EX01=12, EX02=3, EX03=1, EX07=1, IN02=1, IN03=1, IN04=9, IN05=3, CTX05=1.
- Important agent-human change: SCR-00091 changed from unclear_need_full_text/UN01 to include_for_full_text/IN03.
- Master screening forms unchanged; PRISMA flow not updated.
- Next: decide whether to apply completed B01 human decisions to a master screening copy or proceed to B02 AI suggestions.

## 2026-06-23 Step 5-C1 Batch B01 AI Suggestions Update

- Step 5-B3 calibration finalization completed.
- Step 5-C1 B01 AI suggestions generated for not-screened B01 records only.
- B01 observed counts: total 100, calibration_resolved 31, not_screened processed 69.
- AI suggestion distribution: 13 include_for_full_text, 54 exclude_title_abstract, 1 contextual_only, 1 unclear_need_full_text.
- Next: user/ChatGPT human review of B01 suggestions.
- No PRISMA flow update yet.

## 2026-06-23 Step 5-B3 Calibration Finalization Update

- Step 5 calibration human review completed.
- Calibration decision distribution logged: 16 include_for_full_text, 28 exclude_title_abstract, 5 contextual_only, 1 unclear_need_full_text.
- Screening guide v2 calibrated and reason codes v2 created.
- A 1259-record calibration-applied master copy was created; original master screening form remains unchanged.
- Next: launch Step 5-C full batch screening with TAB-2026-06-22-B01 after user/ChatGPT approval.
- PRISMA flow not yet populated.

## 2026-06-23 Step 5-B2 Calibration Human Review Completed

- User-provided human calibration decisions were recorded for 50/50 calibration records.
- Human calibration distribution: 28 exclude_title_abstract, 16 include_for_full_text, 5 contextual_only, 1 unclear_need_full_text.
- Updates were made only in the calibration human review workbook and related summary/QA files.
- Master screening form unchanged; PRISMA flow counts remain TBD.
- Full title/abstract screening not started.
- Next: approve CTX02 refinement / calibration lessons learned, then decide how to proceed to full title/abstract screening.

## 2026-06-23 Step 5-B2 Partial Human Review Update

- User-provided human calibration decisions were recorded for 16/50 calibration records.
- Human decision distribution for reviewed records: 11 exclude_title_abstract, 4 contextual_only, 1 include_for_full_text.
- Remaining calibration records pending: 34.
- Updates were made only in the calibration human review workbook and attention tracking file.
- Master screening form unchanged; PRISMA flow counts remain TBD.
- Full title/abstract screening not started.

## 2026-06-23 Step 5-A Screening Preparation Update

- Step 4 deduplication approval completed.
- Approved title/abstract screening input: 1259 records.
- Step 5-A screening preparation started/completed.
- Next: Review calibration batch and perform Step 5-B calibration screening.
- Screening decisions not yet made.
- PRISMA flow counts remain TBD.

## 2026-06-23 Step 4-C Deduplication Approval Update

- Step 4-B cluster review completed.
- Step 4-C user-corrected dedup approval decisions applied.
- Approved deduplicated screening input created with 1259 records.
- Metadata/dedup adjudication removals: 2; automatic merge clusters applied: 0.
- Next: ChatGPT/user review of approved deduplicated screening input; then Step 5 title/abstract screening preparation.
- Screening not started.
- PRISMA flow counts stay TBD pending final user/ChatGPT approval.

## 2026-06-23 Step 4-A Deduplication Update

- Step 3 final search execution completed.
- Step 4-A formal deduplication started and draft outputs were created under `systematic_review_workflow/03_secim/deduplication/final_2026-06-22/`.
- Draft Step 4-A metrics: final raw rows=1733, duplicate groups=312, deduplicated screening input records=1261, possible duplicate manual review pairs=37.
- Next: review deduplication report and approve records for title/abstract screening.
- Screening not started.
- PRISMA flow counts stay TBD pending user/ChatGPT review of the deduplication draft.

## 2026-06-23 Step 4-B Duplicate Cluster Review Update

- Step 4-B possible duplicate cluster review preparation completed.
- Possible duplicate pairs=37 were converted into connected duplicate clusters=7.
- Cluster-level manual review file: `systematic_review_workflow/03_secim/deduplication/final_2026-06-22/possible_duplicate_clusters_for_review_2026-06-22.csv`.
- Deduplication approval remains pending; PRISMA flow counts stay TBD.
- Screening not started.

## 2026-06-23 Step 3C Update

- Step 3-A Scopus final raw exports logged on 2026-06-22.
- Step 3-B IEEE Xplore final raw exports logged on 2026-06-22.
- Step 3-C supplementary final raw exports logged on 2026-06-22 for ScienceDirect, SpringerLink, Wiley Online Library and Taylor & Francis Online.
- Supplementary final diagnostics: ScienceDirect 24 raw / 23 unique diagnostic, SpringerLink 75 raw / 72 unique diagnostic, Wiley 29 raw / 27 unique diagnostic, Taylor & Francis 3 raw / 3 unique diagnostic.
- Total supplementary final raw rows parsed=131; unique diagnostic records=125; duplicate groups diagnostic=5. These are not PRISMA flow counts.
- Taylor & Francis remains optional/tight-only, low-yield and query mapping pending.
- Step 4-A draft deduplication is now completed; title/abstract screening, full-text screening, data extraction and synthesis have not started.
- PRISMA flow counts stay TBD.

## 2026-06-22 Step 2D Preparation Update

- Step 2C completed.
- Step 2D preparation started.
- Pilot counts remain audit diagnostics only; PRISMA flow counts stay TBD.

## 2026-06-21 Daily Memory Update

- Ayrintili gunluk not: `daily_memory_2026-06-21.md`.
- Current status: Step 2D - Pilot consolidation preparation started.
- ScienceDirect, SpringerLink, Wiley Online Library and Taylor & Francis Online pilot logging completed.
- Step 2D preparation files are present under `systematic_review_workflow/02_arama/step2d_preparation/`.
- Final search execution, deduplication, title/abstract screening, full-text screening, data extraction and synthesis have not started.
- Pilot counts remain audit diagnostics only; PRISMA flow counts stay TBD.

## Okuma Sirasi

1. `../../PROJECT_CONTEXT_OISAC_PRISMA.md`
2. `codex_memory_bank.md`
3. `progress_tracker.md`
4. `decision_log.md`
5. Uzerinde calisilacak asama dosyasi

## Repo Durumu

- Calisma konusu: Optical Integrated Sensing and Communication (O-ISAC) for 6G.
- Calisma turu: PRISMA-grounded narrative systematic review with a scoping-style PCC component.
- Nihai bilimsel manuscript dili: English.
- Workflow aciklamalari, karar notlari ve ara notlar: Turkish.
- Klasor bir PRISMA workflow kitidir; 2026-06-18 kontrolunde git deposu olarak baslatilmamis gorundu.
- Mevcut PDF, Word ve checklist dosyalarina dokunulmayacak.

## Kilit Metodolojik Kararlar

- Framework: PCC - Population / Concept / Context.
- Search window: January 1, 2020 - June 30, 2026.
- Search freeze label: planned search freeze date: June 30, 2026.
- Core primary databases: Scopus, IEEE Xplore.
- Selected supplementary sources: ScienceDirect, SpringerLink, Wiley Online Library, Taylor & Francis Online.
- Web of Science and ACM Digital Library will not be included because institutional access was not available during the search planning stage.
- Language: English only.
- Primary technical evidence corpus: peer-reviewed journal articles, early-access journal articles, and full-length conference/proceedings papers.
- Contextual corpus: review/survey papers and pre-2020 foundational studies; primary technical evidence sayilmaz.
- No seed study set will be used; legacy `included_studies_canonical.csv` formal PRISMA workflow icinde seed set olarak kullanilmayacak.
- 6G relevance strict keyword-only inclusion criterion degildir; direct / inferred / weak / not applicable olarak kodlanir.
- Meta-analysis planlanmamistir.
- Synthesis approach: structured narrative synthesis, scoping-style taxonomy mapping, evidence tabulation, metric-governed comparison, validation maturity mapping, benchmark readiness assessment, research roadmap synthesis.
- Dusuk methodological/reporting quality tek basina dislama nedeni degildir; TQAF-style technical quality assessment ile nitelendirilir.

## Manuscript-Ready Sabitler

Title:

> Optical Integrated Sensing and Communication for 6G: A PRISMA-Grounded Systematic Review and Metric-Governed Cross-Modality Survey

O-ISAC operational definition:

> In this review, O-ISAC refers to optical or photonic systems in which sensing and communication functions are jointly considered, integrated, co-designed, co-optimized, or evaluated within the same architecture, optical link, waveform/resource framework, hardware platform, channel model, or application scenario.

Main research question:

> How has Optical Integrated Sensing and Communication (O-ISAC) been investigated across fiber, free-space optical, VLC/LiFi, photonic-THz, and hybrid optical platforms, and what do existing peer-reviewed studies reveal about cross-modality taxonomy, sensing and communication metric reporting, metric comparability, comparison admissibility, rate-sensing tradeoffs, enabling technologies, application domains, validation maturity, benchmarking readiness, and remaining research gaps for 6G-oriented O-ISAC systems?

## Historical Stage Snapshot (Superseded â€” do not use as current state)

- Step 1 Topic, rationale, PCC, eligibility criteria, research question: completed / Step 1 final locked.
- Step 2 Search strategy finalization and pilot testing: Step 2D preparation completed enough to support final export logging.
- IEEE pilot: completed for candidate package; pilot counts are not PRISMA flow counts.
- IEEE-PILOT-S1A, IEEE-PILOT-S1B-R2 and IEEE-PILOT-S1F-R2: retained as candidate queries.
- IEEE-PILOT-S1F-R1: valuable but noisy; replaced by IEEE-PILOT-S1F-R2.
- Scopus pilot: completed, QA verification pending.
- SCO-PILOT-S1A, SCO-PILOT-S1B and SCO-PILOT-S1F: retained as candidate queries.
- SCO-PILOT-S1B reported/export mismatch 35 vs 60 and SCO-PILOT-S1F minor mismatch 103 vs 104 require verification before final search.
- ScienceDirect supplementary platform pilot: processed on 2026-06-19; SD-PILOT-P1/P2A/P2B/P2C/P2D/P2E/P3/P4 added to `search_log.csv`.
- ScienceDirect audit diagnostics: 350 all parsed rows and 172 unique records; not PRISMA flow counts.
- SD-PILOT-P3 and SD-PILOT-P4 exact UI query strings pending raw txt recovery or user confirmation.
- SpringerLink supplementary platform pilot: completed and logged on 2026-06-21; SPR-PILOT-P1B and P2A-P2E added to `search_log.csv`; SPR-PILOT-P1A missing/pending.
- SpringerLink audit diagnostics: 159 raw exported rows, 126 unique records and 29 duplicate groups; not PRISMA flow counts.
- SpringerLink keep candidates: SPR-PILOT-P2C, SPR-PILOT-P2D, SPR-PILOT-P2E; SPR-PILOT-P1B/P2A/P2B are noisy/rescue-only.
- Wiley Online Library supplementary platform pilot: completed and logged on 2026-06-21; WLY-PILOT-P1A/P1B and P2A-P2E added to `search_log.csv`.
- Wiley audit diagnostics: 57 raw exported rows, 49 unique records and 7 duplicate groups; not PRISMA flow counts.
- Wiley keep candidates: WLY-PILOT-P2D and WLY-PILOT-P2E; WLY-PILOT-P1B/P2A/P2C are supplementary/rescue candidates; WLY-PILOT-P2B is rescue-only/noisy; WLY-PILOT-P1A likely deprioritized.
- Taylor & Francis Online pilot: completed after cleanup; low-yield/noisy; optional tight exact-phrase source only.
- Step 2D pilot consolidation and final search package draft: preparation started.
- Step 3 Search execution: completed / all final exports collected and logged.
- Step 4 Deduplication: completed / approved deduplicated screening input created.
- Step 5 Screening: in progress / pre-B02 global audit and normalization completed; B02 pending.
- Step 6 Data extraction: form drafted / not started.
- Step 7 TQAF assessment: scale defined / not started.
- Step 8 Synthesis: plan drafted / not started.
- Step 9 Manuscript writing: skeleton drafted / results not started.

## Veri ve Count Durumu

- `02_arama/final_search_execution_log_2026-06-22.csv`: Scopus, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library and Taylor & Francis Online final export rows logged. On-screen counts remain `TBD_or_user_reported`.
- `02_arama/ieee_pilot_summary_2026-06-18.md`: IEEE Step 2A pilot summary ve raw export mapping dosyasi.
- `02_arama/scopus_pilot_summary_2026-06-19.md`: Scopus Step 2B pilot summary.
- `02_arama/combined_ieee_scopus_pilot_summary_2026-06-19.md`: IEEE + Scopus candidate pilot package summary.
- `02_arama/sciencedirect_pilot_summary_2026-06-19.md`: ScienceDirect supplementary platform pilot summary.
- `02_arama/pilot_search_QA_report_2026-06-19.md`: Step 2B pilot QA report.
- `02_arama/springerlink_pilot_summary_2026-06-21.md` and `02_arama/springerlink_pilot_QA_report_2026-06-21.md`: SpringerLink supplementary pilot summary and QA.
- `02_arama/wiley_pilot_summary_2026-06-21.md` and `02_arama/wiley_pilot_QA_report_2026-06-21.md`: Wiley Online Library supplementary pilot summary and QA.
- `02_arama/raw_exports/pilot_2026-06-19/`: canonical IEEE + Scopus pilot raw exports.
- `02_arama/audits/pilot_2026-06-19/`: pilot audit zip and extracted audit files.
- `02_arama/raw_exports/springerlink/pilot_2026-06-21/` and `02_arama/audits/springerlink/pilot_2026-06-21/`: SpringerLink pilot raw/audit files.
- `02_arama/raw_exports/wiley/pilot_2026-06-21/` and `02_arama/audits/wiley/pilot_2026-06-21/`: Wiley pilot raw/audit files.
- `02_arama/known_studies_check.csv`: sensitivity/known studies check henuz doldurulmamis; formal PRISMA seed set olarak kullanilmayacak.
- `03_secim/study_selection_log.csv`: sadece header var; kayit yok.
- `03_secim/prisma_flow_counts.md`: tum sayilar TBD; final raw export/audit diagnostics buraya aktarilmaz.
- `03_secim/title_abstract_screening/batch_B01_final_2026-06-22/`: Step 5-C2 B01 human decisions final outputs, B01-applied master copy, draft-not-populated PRISMA count summary and readiness notes.
- `03_secim/title_abstract_screening/batch_B01_final_normalized_2026-06-22/`: Step 5-C2b normalized B01-applied master copy with standard final title/abstract decision fields populated for 69 B01 records.
- `03_secim/title_abstract_screening/pre_B02_global_audit_2026-06-22/`: Step 5-C2D whole workflow audit outputs and pre-B02 global-normalized master baseline for B02.
- `03_secim/excluded_full_texts.csv`: sadece header var.
- `04_veri_cekme/data_extraction.csv`: sadece header var.
- `05_kalite_kanit/risk_of_bias.csv`: sadece header var.
- `05_kalite_kanit/certainty_grade.csv`: sadece header var.
- `06_sentez/synthesis_matrix.csv`: S1-S7 plan satirlari var; sonuc alanlari TBD.

## Historical Priority List (Superseded â€” do not use as current roadmap)

1. Step 2D pilot query decision matrix'i inspect et ve final search package taslagini rafine et.
2. Scopus exact query string'lerini Scopus history veya kullanici dogrulamasi uzerinden al.
3. SCO-PILOT-S1B reported/export mismatch 35 vs 60 durumunu final search oncesi dogrula.
4. SCO-PILOT-S1F minor mismatch 103 vs 104 durumunu final search oncesi dogrula.
5. SD-PILOT-P3 ve SD-PILOT-P4 exact ScienceDirect UI query stringlerini dogrula.
6. SPR-PILOT-P1A missing/pending query/export durumunu netlestir.
7. IEEE + Scopus + ScienceDirect + SpringerLink + Wiley + Taylor & Francis overlap/dedup pilot analizini daha sonra yap.
8. `database_source_pool.md` icinde secili kaynak setini koru; Web of Science ve ACM Digital Library icin access-unavailable exclusion gerekcesini koru.
9. `search_log.csv` icindeki TBD ve pending search string alanlarini exact query ile guncelle.
10. Arama stratejisi peer review yapilip yapilmayacagina karar ver.
11. Record-management ve duplicate-removal aracini/surecini netlestir.
12. `date_uncertain` kayitlari icin gun/ay belirsizligi karar kuralini netlestir.
13. 6G relevance coding icin direct / inferred / weak / not applicable karar ornekleri hazirla.
14. Search gercekten yurutuldukten sonra actual search date, query, export formatlari ve count alanlarini kaydet.

## Historical Open Questions (Superseded snapshot)

- Hedef dergi var mi?
- Search strategy peer review yapilacak mi?
- Record management icin hangi arac kullanilacak?
- Duplicate removal hangi kural setiyle yapilacak?
- Pilot screening set boyutu 25, 50, 100 veya baska bir sayi mi olacak?
- Reviewer1, reviewer2 ve adjudicator kim olacak?
- Formal seed set kullanmadan sensitivity/known studies check nasil uygulanacak?
- Core ve supplementary kaynaklar icin erisim/export imkanlari hazir mi?
- Secili publisher/platform kaynaklarinda export formatlari ve filtreler yeterli mi?

## Dokunulmayacak veya Uydurulmayacak Alanlar

- Mevcut PDF, Word ve checklist dosyalari degistirilmez.
- Mevcut klasor yapisi bozulmaz.
- Gercek arama yurutulmeden `final search date` yazilmaz.
- Search, screening veya PRISMA count alanlarina uydurma sayi girilmez.
- Dahil edilmis gercek calisma olmadan Results veya final conclusion yazilmaz.
- Review/survey papers ve pre-2020 foundational studies primary technical evidence sayilmaz.
- Dusuk kalite tek basina exclusion gerekcesi yapilmaz.

## Metric Comparability Karar Siniflari

| Category | Decision rule |
|---|---|
| directly comparable | Same metric, same measurement plane, similar scenario, and similar validation condition. |
| conditionally comparable | Same general metric family but different scenario or assumption; comparison is possible only when conditions are explicitly stated. |
| not comparable | Metric name may be similar, but measurement plane, definition, or validation context differs. |
| descriptive only | The study reports a metric, but information is insufficient for numerical or operational comparison. |

## TQAF Skor Olcegi

| Skor | Anlam |
|---|---|
| 0 | not reported / insufficient |
| 1 | weak or incomplete |
| 2 | adequate |
| 3 | strong / benchmark-ready |
| NA | not applicable |

Study-level TQAF alanlari: technical relevance, metric clarity, reporting completeness, validation maturity, reproducibility, benchmark readiness, comparison admissibility, limitation transparency, overall evidence contribution.

## Calisma Disiplini

- Yeni metodolojik kararlar once `../../PROJECT_CONTEXT_OISAC_PRISMA.md` dosyasina islenir.
- Sonra ilgili workflow dosyasi ve `decision_log.md` guncellenir.
- Planlanan islem ile tamamlanmis islem ayrimi korunur.
- Manuscript-ready section, abstract, title, research question, table caption ve akademik taslaklar English yazilir.
- Repo aciklamalari, workflow yonlendirmeleri ve ara notlar Turkish yazilir.

## Son Guncelleme - Step 5-C9 B05

- Step 5-C8 B04 human decisions completed.
- Step 5-C9 B05 AI suggestions generated for 98 not-screened B05 records.
- 2026-06-25 B05 high-priority human review partial update completed: 13 records resolved in the B05 human review workbook.
- 2026-06-25 B05 medium-priority partial update 1 completed: first 25 medium-priority records resolved in the B05 human review workbook.
- 2026-06-25 B05 medium-priority partial update 2 completed: second 25 medium-priority records resolved in the B05 human review workbook.
- 2026-06-25 B05 human review workbook completed: final 26 medium-priority and 9 low-priority records resolved.
- B05 workbook status: 98 resolved, 0 pending among 98 not_screened records.
- Resolved so far: 50 calibration + 69 B01 + 93 B02 + 100 B03 + 99 B04 = 411 title/abstract decisions.
- If B05 human decisions are formally logged next, human-decided tracking becomes 509/1259 and 750 records remain not_screened.
- Next: perform B05 human decisions logging/master update; do not populate PRISMA flow yet unless explicitly requested.
- B05 icin baseline olarak `title_abstract_screening_form_MASTER_BATCH_B04_APPLIED_2026-06-22.csv` kullanilmalidir.
- PRISMA flow not yet populated.

## 2026-07-09 Retrieval Stop Durable Note

- User stopped pursuing the remaining 60 missing PDFs after the documented retrieval phase.
- The 60 records are classified as `report_not_retrieved` / `full_text_not_retrieved`; they are not full-text eligibility exclusions.
- The 272 retrieved reports proceed to future PDF/Markdown readiness QA and later full-text eligibility preparation.
- Formal PRISMA flow remains TBD until a dedicated PRISMA flow step.
- No eligibility assessment, extraction, TQAF assessment, synthesis, or included-study count has started.

## 2026-07-19 Step 2 Reviewer / AI / Human Process LOCK

- User approved and locked the PRISMA Item 8 full-text selection-process model.
- Final authority: one human reviewer (User). Codex/ChatGPT supplies only provisional evidence coding and recommendations; it is not an independent reviewer.
- Every exclusion, contextual, unclear, related/correction, source/date/language/type/retraction problem, low-confidence case, translation/contact consideration and every B01 pilot report requires original-source human review.
- Straightforward include recommendations require explicit human batch approval plus at least 10% and minimum two stratified source-open QA records per batch. Any eligibility decision error expands source-open review to all straightforward includes in that batch.
- Do not claim dual-independent screening. Report the single-human, AI-assisted, non-independent workflow and limitation transparently.
- Record AI tool/model/version, evidence location, human review scope, conflict/adjudication, translation method and any user-approved author contact.
- Locked Step 2 artifacts are under `systematic_review_workflow/09_kayitlar/checkpoints/prisma_pre_full_text_eligibility_gate_step2_2026-07-19/`.
- No eligibility decision was made and B01 pilot has not started. Formal PRISMA flow remains TBD.
- Next gate: canonical full-text eligibility form + B01 pilot plan QA.

## 2026-07-23 B01-P01

- KullanÄ±cÄ± ilk beÅŸ kaynaÄŸÄ± 5/5 aÃ§tÄ±.
- Final ve kilitli `include_primary`: `SCR-00001`, `SCR-00007`, `SCR-00011`.
- `Hold` / aÃ§Ä±k `unclear_adjudication / ADJ01`: `SCR-00087`, `SCR-00094`.
- Ä°ki Hold kaydÄ±nda AI `FTX07` Ã¶nermiÅŸtir; insan nihai dÄ±ÅŸlama onayÄ± olmadÄ±ÄŸÄ± iÃ§in PRISMA 16b exclusion olarak sayÄ±lmayacaktÄ±r.
- Aktif workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_P01_2026-07-23/full_text_eligibility_B01_P01_APPLIED_2026-07-23.xlsx`.

### B01-P01 final

- KullanÄ±cÄ± `SCR-00087` ve `SCR-00094` iÃ§in nihai `exclude_full_text / FTX07` onayÄ± verdi.
- Final B01-P01: `include_primary` = `SCR-00001`, `SCR-00007`, `SCR-00011`; `FTX07` = `SCR-00087`, `SCR-00094`.
- BeÅŸ kayÄ±t QA PASS ve kilitli; aktif workbook `full_text_eligibility_B01_P01_FINAL_2026-07-23.xlsx`.

## 2026-07-23 B01-P02 Final

- P02 5/5 insan kaynak incelemesiyle tamamlandÄ±; tÃ¼m kararlar QA PASS ve kilitli.
- `include_primary`: `SCR-00009`, `SCR-00038`, `SCR-00052`, `SCR-00083`.
- `exclude_full_text / FTX04`: `SCR-00060`.
- P01 + P02 kÃ¼mÃ¼latif B01: 10/22 reviewed/locked; 7 include; 3 exclude (`FTX07` = 2, `FTX04` = 1); 12 remaining.
- Aktif workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_P02_2026-07-23/full_text_eligibility_B01_P02_FINAL_2026-07-23.xlsx`.
- Formal PRISMA flow hÃ¢lÃ¢ TBD/not populated; extraction, TQAF ve synthesis baÅŸlamadÄ±.
- SÄ±radaki operasyon B01-P03.

## 2026-07-23 B02 Full-Text Eligibility Final

- B02 15/15 kaynak-aÃ§Ä±k insan/Codex incelemesi tamamlandÄ±; QA PASS ve unresolved/Hold = 0.
- `include_primary`: `SCR-00110`, `SCR-00123`, `SCR-00151`, `SCR-00160`, `SCR-00177`, `SCR-00185`, `SCR-00189`, `SCR-00196`.
- `retain_contextual`: `SCR-00108`.
- `exclude_full_text`: `SCR-00129 / FTX03`; `SCR-00163 / FTX04`; `SCR-00146`, `SCR-00147`, `SCR-00187`, `SCR-00200 / FTX07`.
- `SCR-00160` iÃ§in kullanÄ±cÄ± onaylÄ± karar: `include_primary`. Ortak fotonik mimaride SFCW sensing bileÅŸeni ve 2-Gbit/s ASK iletiÅŸim birlikte Ã¼retilmektedir; hedef-sensing deneyinin geleceÄŸe bÄ±rakÄ±lmasÄ± validation-maturity sÄ±nÄ±rlamasÄ±dÄ±r.
- Aktif B02 workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B02_2026-07-23/full_text_eligibility_B02_FINAL_2026-07-23.xlsx`.
- Formal PRISMA flow hÃ¢lÃ¢ TBD/not populated; extraction, TQAF ve synthesis baÅŸlamadÄ±.
- SÄ±radaki operasyon B03 full-text eligibility kaynak incelemesidir.

## 2026-07-23 B03-P01 Full-Text Eligibility

- KullanÄ±cÄ± ve Codex beÅŸ kaynaÄŸÄ± baÄŸÄ±msÄ±z olarak aÃ§Ä±p inceledi; 5/5 deÄŸerlendirme uyumluydu.
- `include_primary`: `SCR-00210`, `SCR-00218`, `SCR-00220`.
- `retain_contextual`: `SCR-00222`.
- `exclude_full_text / FTX04`: `SCR-00223`.
- B03-P01 daÄŸÄ±lÄ±mÄ±: 3 primary, 1 contextual, 1 exclusion; Hold/unresolved = 0.
- Formal PRISMA flow deÄŸiÅŸtirilmedi; sÄ±radaki operasyon B03-P02â€™dir.

## 2026-07-23 B03-P02 Full-Text Eligibility

- B03-P02 5/5 kaynak-aÃ§Ä±k kullanÄ±cÄ±/Codex incelemesiyle tamamlandÄ±; tÃ¼m kararlar uyumluydu.
- `include_primary`: `SCR-00233`, `SCR-00238`, `SCR-00256`, `SCR-00268`, `SCR-00273`.
- `SCR-00273`: ayrÄ± fiziksel test konfigÃ¼rasyonlarÄ±na raÄŸmen ortak optical-camera model, application scenario ve exposure-time joint optimization FTI05 iÃ§in yeterlidir.
- B03 kÃ¼mÃ¼latif P01+P02: 10/16 reviewed; 8 primary, 1 contextual, 1 `FTX04`; 6 remaining.
- Formal PRISMA flow deÄŸiÅŸtirilmedi; sÄ±radaki operasyon B03-P03â€™tÃ¼r.

## 2026-07-23 B03-P03 Full-Text Eligibility

- B03-P03 5/5 kaynak-aÃ§Ä±k kullanÄ±cÄ±/Codex incelemesiyle tamamlandÄ±; deÄŸerlendirmeler uyumluydu.
- `include_primary`: `SCR-00274`, `SCR-00277`, `SCR-00278`, `SCR-00294`.
- `exclude_full_text / FTX04`: `SCR-00281`; communication rolÃ¼ mimaride bulunsa da raporda genuine joint communicationâ€“sensing evaluation yoktur.
- B03 kÃ¼mÃ¼latif P01â€“P03: 15/16 reviewed; 12 primary, 1 contextual, 2 exclusions (`FTX04` = 2); 1 remaining.
- Formal PRISMA flow deÄŸiÅŸtirilmedi; sÄ±radaki operasyon B03-P04â€™tÃ¼r.

## 2026-07-23 B03-P04 ve B03 Final

- `SCR-00298`: `exclude_full_text / FTX07`; teknik gÃ¶vde Ã‡ince, English iÃ§erik yalnÄ±z abstract/captions/extended summary dÃ¼zeyindedir.
- B03 final 16/16 reviewed and locked.
- `include_primary` = 12: `SCR-00210`, `SCR-00218`, `SCR-00220`, `SCR-00233`, `SCR-00238`, `SCR-00256`, `SCR-00268`, `SCR-00273`, `SCR-00274`, `SCR-00277`, `SCR-00278`, `SCR-00294`.
- `retain_contextual` = 1: `SCR-00222`.
- `exclude_full_text` = 3: `SCR-00223 / FTX04`, `SCR-00281 / FTX04`, `SCR-00298 / FTX07`.
- Hold/unresolved = 0. Formal PRISMA flow TBD/not populated.
- SÄ±radaki operasyon B04 full-text eligibility kaynak incelemesidir.

## 2026-07-23 B04-P01 Full-Text Eligibility

- B04-P01 5/5 kullanÄ±cÄ±/Codex kaynak-aÃ§Ä±k incelemesiyle tamamlandÄ±; deÄŸerlendirmeler tamamen uyumluydu.
- `include_primary`: `SCR-00312`, `SCR-00344`, `SCR-00346`, `SCR-00356`, `SCR-00361`.
- B04-P01 final: 5 primary include; contextual, exclusion ve Hold/unresolved = 0.
- Formal PRISMA flow deÄŸiÅŸtirilmedi; extraction, TQAF ve synthesis baÅŸlamadÄ±.
- SÄ±radaki operasyon B04-P02â€™dir.

## 2026-07-23 B04-P02 Full-Text Eligibility

- B04-P02 5/5 kullanÄ±cÄ±/Codex kaynak-aÃ§Ä±k incelemesiyle tamamlandÄ±; deÄŸerlendirmeler tamamen uyumluydu.
- `include_primary`: `SCR-00362`, `SCR-00366`, `SCR-00367`, `SCR-00369`, `SCR-00376`.
- B04-P02 final: 5 primary include; contextual, exclusion ve Hold/unresolved = 0.
- B04 kÃ¼mÃ¼latif P01â€“P02: 10/14 reviewed; 10 primary include; 4 remaining.
- Formal PRISMA flow deÄŸiÅŸtirilmedi; extraction, TQAF ve synthesis baÅŸlamadÄ±.
- SÄ±radaki operasyon B04-P03â€™tÃ¼r.

## 2026-07-23 B04-P03 ve Retrieved-B04 Final

- B04-P03 4/4 kullanÄ±cÄ±/Codex kaynak-aÃ§Ä±k incelemesiyle tamamlandÄ±; deÄŸerlendirmeler tamamen uyumluydu.
- `include_primary`: `SCR-00379`, `SCR-00387`, `SCR-00396`.
- `exclude_full_text / FTX06`: `SCR-00388`; Ã¼Ã§ sayfalÄ±k poster paper, eligible full-length conference paper deÄŸildir.
- `SCR-00379`: smoke-induced scattering kaynaklÄ± SNR/BER deÄŸiÅŸimi sensing proxyâ€™sidir; kalibre aerosol konsantrasyonu Ã¶lÃ§Ã¼mÃ¼ deÄŸildir.
- `SCR-00387`: tek yÃ¶nlÃ¼ laboratory proof-of-concept ve transmitter-side digitized ranging reference kullanÄ±r; bu bir validation-maturity notudur.
- Retrieved B04 final 14/14: 13 primary include, 1 `FTX06`, contextual ve Hold/unresolved = 0.
- B04 full-text-needed havuzundaki diÄŸer 5 rapor `report_not_retrieved` olarak ayrÄ± kalÄ±r; eligibility exclusion deÄŸildir.
- Formal PRISMA flow deÄŸiÅŸtirilmedi; extraction, TQAF ve synthesis baÅŸlamadÄ±.
- SÄ±radaki operasyon B05 retrieved-report full-text eligibility incelemesidir.

## 2026-07-23 B01-P03 Full-Text Eligibility Backfill Final

- User explicitly approved `SCR-00008`, `SCR-00012`, `SCR-00013`, `SCR-00036`, and `SCR-00057` as `include_primary`; all five records are human-approved, QA PASS and locked.
- 35/35 FTI criteria are `yes`; AI provisional, human and final decisions agree 5/5; primary exclusion-reason fields are null.
- Normalization: attachment `primary_code: include_primary` was mapped to `human_decision`/`final_decision`; numbered prefixes were removed from IDs.
- Date evidence: `SCR-00036` uses PDF Crossmark VoR MajorVersionDate `2026-01-10`, not acceptance `2026-01-05`; `SCR-00057` uses PDF PRISM coverDisplayDate `2025-06-29`.
- Cumulative B01 after P01-P03: 15/22 reviewed/locked; 12 `include_primary`; 3 `exclude_full_text` (`FTX07` = 2, `FTX04` = 1); 7 retrieved reports remain.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_P03_2026-07-23/full_text_eligibility_B01_P03_FINAL_2026-07-23.xlsx`.
- QA: exact target set 5/5, unexpected workbook value changes 0, formula changes 0, formula errors 0. B13 and formal PRISMA flow unchanged.
- Next resumed-B01 action: B01-P04. Later B02-B04 history remains preserved.

## 2026-07-24 KÄ±sa GÃ¼nlÃ¼k Not

- BugÃ¼nkÃ¼ Ã§alÄ±ÅŸmada B01â€™de aÃ§Ä±k kalan akÄ±ÅŸa geri dÃ¶nÃ¼ldÃ¼; kullanÄ±cÄ±ya FTI01-FTI07 tabanlÄ± kaynak-inceleme yanÄ±t ÅŸablonu verildi ve kullanÄ±cÄ± yanÄ±tlarÄ± Codexâ€™in baÄŸÄ±msÄ±z PDF incelemesiyle karÅŸÄ±laÅŸtÄ±rÄ±ldÄ±.
- `SCR-00008`, `SCR-00012`, `SCR-00013`, `SCR-00036` ve `SCR-00057` iÃ§in karar uyumu 5/5, kriter uyumu 35/35 bulundu; kullanÄ±cÄ± onayÄ± `include_primary` olarak kaydedilip kilitlendi.
- `SCR-00036` ve `SCR-00057` yayÄ±n tarihleri PDF metadata kanÄ±tÄ±yla normalize edildi; insan/final karar alanlarÄ± ayrÄ±ÅŸtÄ±rÄ±ldÄ± ve dÄ±ÅŸlama kodlarÄ± boÅŸ bÄ±rakÄ±ldÄ±.
- Yeni B01-P03 final checkpointâ€™i, karar CSVâ€™si, QA kaydÄ±, kilit raporu ve gÃ¶rsel kontroller oluÅŸturuldu. Workbook diff kontrolÃ¼nde beklenmeyen deÄŸer deÄŸiÅŸikliÄŸi, formÃ¼l deÄŸiÅŸikliÄŸi ve formÃ¼l hatasÄ± bulunmadÄ±.
- B01 gÃ¼ncel durumu 15/22 locked, 12 `include_primary`, 3 `exclude_full_text`, 7 remaining. SÄ±radaki resumed-B01 iÅŸlemi B01-P04â€™tÃ¼r.
- B13 active master ve formal PRISMA flow deÄŸiÅŸtirilmedi; B02-B04 geÃ§miÅŸi korundu.

## 2026-07-25 B01-P04/P05 Full-Text Eligibility and B01 Final

- This entry supersedes earlier B01 progress notes for current-state purposes; P01-P03 workbooks remain historical audit artifacts.
- User and Codex source-open assessments agreed for all seven remaining B01 reports.
- P04 final includes: `SCR-00002`, `SCR-00015`, `SCR-00086`, `SCR-00091`, `SCR-00099`.
- P05 final includes: `SCR-00056`, `SCR-00072`.
- Seven-record QA: 49/49 FTI criteria `yes`; 7/7 human/final decisions `include_primary`; no FTX code; all records QA PASS and locked.
- Retrieved B01 final: 22/22 locked; 19 `include_primary`; 3 exclusions (`SCR-00087 / FTX07`, `SCR-00094 / FTX07`, `SCR-00060 / FTX04`); contextual and unresolved/Hold = 0.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_FINAL_2026-07-25/full_text_eligibility_B01_FINAL_2026-07-25.xlsx`.
- Final workbook SHA-256: `95eb361519260e1ec252f60819cf28080d11b769b438791e5d218f6710260a0e`.
- The B01 final workbook above is the canonical forward source for B01 eligibility decisions; earlier B01-P01/P02/P03 workbooks must not be used as current truth.
- Workbook integrity QA: 151 FTI `yes`, 3 FTI `no`, 0 blank; 154 evidence rows; 852 formulas preserved; no formula errors or unexpected value changes.
- B13 active master and formal PRISMA flow remain unchanged; extraction, TQAF and synthesis have not started.
- Next operation: B05 retrieved-report full-text eligibility source review.

## 2026-07-26 B05-P01 Full-Text Eligibility Final

- User and Codex source-open decisions agreed 5/5.
- `include_primary`: `SCR-00406`, `SCR-00407`, `SCR-00418`, `SCR-00432`.
- `exclude_full_text / FTX07`: `SCR-00409`; FTI02 is `no` because the detailed technical body is Chinese and the English content is only the structured Abstract on pp.12-13.
- QA: 5/5 sources opened, 34 FTI `yes`, 1 FTI `no`, 4 include gates PASS, 1 valid FTX07 exclusion, 2 HRT13 include-QA samples, unresolved/Hold = 0.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B05_P01_2026-07-26/full_text_eligibility_B05_P01_FINAL_2026-07-26.xlsx`.
- Workbook SHA-256: `b540d76d589d5aa649a1675e8a29ed4e1816d9b1d85f819f7f912a747044a1ef`.
- Operational progress: 72/272 reviewed; 56 primary, 2 contextual, 14 excluded; 200 remain.
- B13 active master and formal PRISMA flow unchanged; extraction, TQAF and synthesis not started.
- Next: B05-P02 = `SCR-00436`, `SCR-00440`, `SCR-00451`, `SCR-00456`, `SCR-00460`.

## 2026-07-26 B05-P02 Full-Text Eligibility Final

- Final `include_primary`: `SCR-00436`, `SCR-00440`, `SCR-00451`, `SCR-00456`, `SCR-00460`.
- QA: 5/5 sources opened, 35/35 FTI `yes`, 5 include gates PASS, exclusion/Hold/unresolved = 0, all records QA PASS and locked.
- Initial decision agreement was 4/5. The external source review proposed `SCR-00451 / FTX04`; locked FTI05 permits integration within a common architecture/optical link/hardware/application scenario without requiring a shared sensing probe or waveform. User approved the Codex `include_primary` recommendation.
- `SCR-00451` is recorded as `decision_disagreement / resolved_user_approved` with HRT03. HRT13 samples are `SCR-00436` and `SCR-00440`; HRT08 was resolved for `SCR-00460`.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B05_P02_2026-07-26/full_text_eligibility_B05_P02_FINAL_2026-07-26.xlsx`.
- Workbook SHA-256: `04781c71602cb81e5db022b85ba002c28563e1e60b00872b8d3ce217639405ab`.
- B05 cumulative after P01-P02: 10/14 reviewed; 9 primary, 1 `FTX07`, 4 pending.
- Operational progress: 77/272 reviewed; 61 primary, 2 contextual, 14 excluded; 195 remain.
- B13 active master and formal PRISMA flow unchanged; extraction, TQAF and synthesis not started.
- Next: B05-P03 = `SCR-00473`, `SCR-00488`, `SCR-00492`, `SCR-00496`.

## 2026-07-26 B05-P03 and B05 Full-Text Eligibility Final

- Final `include_primary`: `SCR-00473`, `SCR-00488`, `SCR-00492`, `SCR-00496`.
- QA: 4/4 sources opened, 28/28 FTI `yes`, 4 include gates PASS, exclusion/Hold/unresolved = 0, all records QA PASS and locked.
- Independent Codex and user source-review decisions agreed 4/4. HRT13 samples are `SCR-00473` and `SCR-00492`; HRT06 was resolved for `SCR-00488`; HRT08 was resolved for `SCR-00496`.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B05_P03_2026-07-26/full_text_eligibility_B05_P03_FINAL_2026-07-26.xlsx`.
- Workbook SHA-256: `5ca43de0e9649fd3d5b4d76ec819b8dee9e6bd0b6f14140093a275ee752ca41e`.
- B05 final: 14/14 reviewed; 13 primary, 1 `FTX07`, 0 pending.
- Operational progress: 81/272 reviewed; 65 primary, 2 contextual, 14 excluded; 191 remain.
- B13 active master and formal PRISMA flow unchanged; extraction, TQAF and synthesis not started.
- Next: B06-P01 = `SCR-00502`, `SCR-00506`, `SCR-00508`, `SCR-00523`, `SCR-00527`.

## 2026-07-27 B06 Full-Text Eligibility Final

- All 13 retrieved B06 reports were source-reviewed, human/User approved, QA-checked and locked.
- Final decisions: 9 `include_primary`; 4 `exclude_full_text`; contextual/Hold = 0.
- Included IDs: `SCR-00502`, `SCR-00506`, `SCR-00527`, `SCR-00553`, `SCR-00557`, `SCR-00576`, `SCR-00589`, `SCR-00592`, `SCR-00594`.
- Excluded IDs/reasons: `SCR-00508 / FTX03`; `SCR-00523 / FTX07`; `SCR-00528 / FTX07`; `SCR-00571 / FTX07`.
- `SCR-00527` was included after the local 14-page English full text resolved the external source-set evidence gap; the same m-CAP VLC signal supports both data transmission and RSS trilateration, and the user explicitly approved inclusion.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B06_FINAL_2026-07-27/full_text_eligibility_B06_FINAL_2026-07-27.xlsx`.
- SHA-256: `dd67e541b9672f4dd3442b3814683a5e8ed1620db56c9c5be4ea9b4288fda4c0`.
- QA: 108 canonical fields; 13/13 unique rows, sources opened, row QA PASS and locked; formula-driven QA PASS; formula errors = 0; HRT13 samples = 2.

## 2026-07-27 B07 Full-Text Eligibility Final

- All 13 retrieved B07 reports were source-reviewed, human/User approved, QA-checked and locked.
- Final decisions: 9 `include_primary`; 1 `retain_contextual`; 3 `exclude_full_text`; Hold = 0.
- Included IDs: `SCR-00602`, `SCR-00607`, `SCR-00619`, `SCR-00626`, `SCR-00631`, `SCR-00647`, `SCR-00665`, `SCR-00679`, `SCR-00680`.
- Contextual ID: `SCR-00656`.
- Excluded IDs/reasons: `SCR-00606 / FTX01`; `SCR-00623 / FTX03`; `SCR-00689 / FTX06`.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B07_FINAL_2026-07-27/full_text_eligibility_B07_FINAL_2026-07-27.xlsx`.
- SHA-256: `52cf6ed54d30bb659f170469f9e7b92fce3c3e8b849bbab6542a4d9a6ed6afe8`.
- QA: 108 canonical fields; 13/13 unique rows, sources opened, row QA PASS and locked; formula-driven QA PASS; formula errors = 0; HRT13 samples = 2.
- Operational cumulative state after B07: 107/272 reviewed; 83 primary, 3 contextual, 21 excluded; 165 retrieved reports remain.

## 2026-07-27 B08â€“B13 Prompt Package Complete

- All remaining retrieved reports were partitioned without overlap or omission: 165 reports in 35 standalone prompts (`B08`=2, `B09`=4, `B10`=13, `B11`=11, `B12`=4, `B13`=1).
- Package folder: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_prompt_packages_B08_B13_2026-07-27/`.
- ZIP: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_prompt_packages_B08_B13_2026-07-27.zip`.
- ZIP SHA-256: `ee2c27220830a0f76c267f4370f815da5002cb1cfd69b1ca68dfb2b322486f71`.
- Independent QA PASS: 165/165 exact canonical IDs/titles/batches/source order; 35/35 prompt files; max five reports per part; all 165 PDF paths exist; required FTI, guardrail, FTX hierarchy and output sections present; no pre-adjudicated decisions; ZIP 39/39 entries hash-match the package.
- B12 non-retrieved appendix IDs `SCR-01148`, `SCR-01150`, `SCR-01157`, `SCR-01163`, `SCR-01164` were not placed in eligibility prompts and remain `RPT01`, not full-text exclusions.
- Next: run `B08/B08_P01_prompt.txt`, return the five-line source-review output, then compare and human-approve before B08 lock.

## 2026-07-27 B08 Full-Text Eligibility Final

- All 10 retrieved B08 reports were source-reviewed, human/User approved, QA-checked and locked.
- Final decisions: 7 `include_primary`; 3 `exclude_full_text`; contextual/Hold = 0.
- Included IDs: `SCR-00719`, `SCR-00722`, `SCR-00730`, `SCR-00731`, `SCR-00761`, `SCR-00763`, `SCR-00784`.
- Excluded IDs/reasons: `SCR-00715 / FTX06`; `SCR-00755 / FTX02`; `SCR-00766 / FTX04`.
- `SCR-00755` was adjudicated from external `Yes` to `FTX02` because the PDF explicitly places optical-cable/DAS integration in a future stage. `SCR-00766` remained excluded, but `FTX05` was corrected to `FTX04` because it is a valid full conference paper and the failure is lack of genuine sensing-communication integration.
- RPT02 mapping fields were documented for `SCR-00722`, `SCR-00731`, `SCR-00763`, and `SCR-00784`; report-level eligibility was unchanged.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B08_FINAL_2026-07-27/full_text_eligibility_B08_FINAL_2026-07-27.xlsx`.
- SHA-256: `ebf3a848b0de49378f49a566a81b5eb8265152c3bedddc20688c36ec6205bf1a`.
- QA: 108 canonical fields; 10/10 unique rows, sources opened, row QA PASS and locked; formula-driven QA PASS; formula errors = 0; HRT13 samples = 2; related mappings = 4.
- Operational cumulative state after B08: 117/272 reviewed; 90 primary, 3 contextual, 24 excluded; 155 retrieved reports remain.
- Next submitted group is B09-P02; B09-P01 remains pending unless separately supplied.

## 2026-07-27 B09-P02 Full-Text Eligibility Lock

- User approval text: `P02 OK`.
- Final report-level decisions: five `include_primary` â€” `SCR-00884`, `SCR-00885`, `SCR-00886`, `SCR-00887`, `SCR-00889`; no contextual, exclusion or Hold.
- `SCR-00886` maps to `SCR-01075` as conference-to-journal extension and to `SCR-01150` as the exact same OFC W4J.2 report under an alternate DOI. Study-level handling is count once.
- `SCR-00889` has a pending predecessor/companion mapping to `SCR-00900`; preserve distinct results and confirm reciprocally when B09-P04 is reviewed.
- `SCR-01150` historical RPT01 status is superseded by a dated `RPT02 / exact_duplicate` adjudication. The 2026-07-09 60-row checkpoint remains immutable; current unresolved RPT01 = 59.
- Canonical part-lock workbook: `checkpoints/full_text_eligibility_B09_P02_LOCK_2026-07-27/full_text_eligibility_B09_P02_LOCK_2026-07-27.xlsx`.
- SHA-256: `58ef65e57260034681b62fd5e50915fa6bd999563b7ebef1c10ce10e80a27244`.
- QA: 108 canonical fields; 5/5 unique rows, sources opened, row QA PASS and locked; formula-driven QA PASS; formula errors = 0; HRT13 samples = 2; mapping rows = 2.
- Operational cumulative state: 122/272 reviewed; 95 primary, 3 contextual, 24 excluded; 150 retrieved reports remain.
- Next submitted part is B09-P01; B09-P03/P04 remain pending.

## 2026-07-30 Phase D Pre-Pilot Baseline

- Phases A, B and C are complete; Phase D is current.
- Final extraction universe: 206 included study clusters, 227 eligible reports and 206 unique primary extraction reports.
- Versioned workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_setup_2026-07-30/OISAC_PHASE_D_EXTRACTION_BASELINE_2026-07-30.xlsx`.
- Workbook SHA-256: `f39e3539b26330ea90cdcefa78fdb760ea176c5bdd7b1a8bb4bc079dcfebfc80`.
- Workbook layers: 206-row study master; 232-row full report/version lineage; blank long-format evidence, metric and tradeoff tables; controlled codebook; 5-study pilot; 17-item human checklist; QA summary/log.
- Eligible report-family distribution: 187 Ã— 1, 17 Ã— 2 and 2 Ã— 3; 19 included multi-report families.
- Source QA PASS: 227/227 eligible PDFs and 206/206 primary PDFs available and valid. `SCR-00730` must be reached from overlay `source_path` because its staging path remains under `unclear/B08`.
- Two Phase B-authorized canonical/primary differences are flagged for Phase D lineage review: `SCR-01113 â†’ SCR-00957` and external `SCR-00027 â†’ SCR-01100`.
- Missing-value discipline: blank = not reviewed; after review use `reported/NR/NA/UNC`. No unsupported inferred values. Calculated/digitized values require method, formula and input lineage.
- TQAF scoring remains Phase E and is absent from the Phase D workbook.
- Pilot set: `SCR-00007`, `SCR-00008`, `SCR-00083` family, `SCR-00941`, `SCR-00196`; 5 studies / 6 eligible PDFs.
- Pilot extraction has not started. Full-corpus gate is intentionally blocked until all five pilots are human-approved and schema/codebook are version-locked.
- Checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_SETUP_2026-07-30/`.
- Next operation: extract pilot 1, `STC-SINGLETON-SCR-00007 / SCR-00007`, from the original PDF and present it for user checklist verification.

## 2026-07-30 Phase D Pilot P01 Extraction (Intermediate)

- P01 `STC-SINGLETON-SCR-00007 / SCR-00007` was AI-assisted extracted from the original 15-page PDF.
- Active workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_pilot_2026-07-30/OISAC_PHASE_D_PILOT_WORKBOOK_2026-07-30.xlsx`.
- Workbook SHA-256: `27eb72384918b108698a248f3feb144ce947456049309548d47b76b4724a3c41`.
- Populated P01 layers: 66 evidence items, 6 metric results, 2 tradeoff records and 17 human-checklist rows with evidence locators.
- P01 workflow state: `pending_verification`; human review `pending`; `not_locked`. No human approval has been claimed.
- Three open human-decision issues: Fig. 1 `AWGN + Fading` versus narrative/Table 1 `AWGN`; whether MAPE under noise-only AWGN supports the conservative `channel_sensing` code; whether spectral efficiency versus pilot overhead is partial proxy evidence rather than a direct sensing-metric tradeoff.
- MAPE is preserved as *mean absolute pilot error*. No graph digitization, calculated value, silent unit conversion or TQAF score was added.
- P02 `SCR-00008`, P03 `SCR-00083` family, P04 `SCR-00941` and P05 `SCR-00196` remain `not_started`; human approvals are 0/5.
- Deterministic pilot QA PASS: 10/10 checks; missing provenance = 0; formula errors = 0; exported workbook reopened successfully.
- Checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_PILOT_P01_2026-07-30/`.
- Full-corpus gate remains blocked. Next operation: user completes P01 `HC01â€“HC17`; approve leads to a versioned human-lock checkpoint and P02, while revise/hold requires correction and repeat QA.

## 2026-07-30 Phase D Five-Pilot Batch Extraction

- P01â€“P05 source extraction is complete for five included studies and six PDFs.
- Active workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_pilot_all_2026-07-30/OISAC_PHASE_D_PILOT_ALL_WORKBOOK_2026-07-30.xlsx`.
- SHA-256: `397fcad05ae5d9761c0d319904803b07694063a7a037e7f280bd219dcf93c2ed`.
- Record totals: 274 evidence, 122 metrics, 17 tradeoffs and 85 human-checklist rows.
- Per-pilot counts: P01 `66/6/2`; P02 `50/32/3`; P03 `59/45/4`; P04 `38/12/5`; P05 `61/27/3`.
- QA PASS: IDs complete/unique; source/page and checklist-locator missingness = 0; formula errors = 0; calculated/digitized values = 0; workbook reopened; 14 renders visually reviewed.
- P03 keeps `SCR-00083` and `SCR-00553` provenance and the companion/frequency-division/joint conditions separate.
- Open human-decision issues = 35. Human responses = 0; approvals = 0/5; every pilot is pending and not locked.
- P03 final pilot QA preserves complete pipe-delimited metric links for all four tradeoff rows, codes them non-quantitative, keeps `P03-Q004` open, preserves `mixed / frequency_division|joint_waveform / laboratory_experiment`, and retains 24 provisional family codes with zero P03 `other` collapse.
- No TQAF scoring and no final comparability/admissibility adjudication occurred.
- Checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_PILOT_ALL_PENDING_HUMAN_2026-07-30/`.
- Next: user reviews `12_ALL_PILOTS_REVIEW` and completes P01â€“P05 `HC01â€“HC17` in `08_HUMAN_CHECKLIST`; full-corpus extraction remains blocked until 5/5 approval and schema/codebook lock.

## 2026-08-07 PRISMA public-release staging memory

- Canonical workbook: `04_veri_cekme/outputs/phase_d_survey_ready_2026-08-04/OISAC_PHASE_D_SURVEY_READY_2026-08-04.xlsx`; SHA-256 `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`.
- Staging root: `07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/`.
- Public workbook SHA-256: `faba81fb212deb1851b44d75b6cfc742ad9c78c9c917dc58f050dc5da16a8f74`.
- Draft ZIP SHA-256 after registration/metadata correction: `8c0e170aaf4e64af7e3f25c9d30742de1e038ef812545b0bdbdf07d6c26c8a72`; label is `NOT_FOR_PUBLICATION`.
- Package QA: `PASS_STRUCTURE_SANITIZATION_BLOCKED_METADATA`; all expected CSV/XLSX row counts and 86 manifest hashes pass, sensitive findings 0.
- Public data: 206 studies, 232 report-lineage rows, 39 exclusions, 3,041 evidence rows, 2,559 condition sets, 4,861 metrics, 404 trade-offs, 8,306 claim decisions, 206 study TQAF rows, 115 evidence bodies, 4,931 body membership rows, 93 conflicts, 7 S1-S7 sections and 446 codebook rows.
- Excluded: publisher PDFs/full text, raw database exports, paths, emails, actor IDs, Gemini/browser artifacts and long source-derived prose.
- Existing public repo is unsafe for automatic Zenodo archiving because it tracks 317 PDFs. Use a dedicated clean artifact repository or another package-only route.
- Historical records resolve the survey-author order as Fatih DÃ¶nmez, Ahmet Altuncu and Mustafa Namdar; affiliations and Fatih DÃ¶nmez's ORCID are verified, while the other two ORCIDs may remain absent.
- Pending user response: whether the public dataset/software creator list should include all three survey authors or only the OSF-listed Fatih DÃ¶nmez; exact rights holder(s) and copyright year; final CC BY 4.0 data/docs and MIT code approval; preferred clean package-only GitHub route.
- No GitHub/Zenodo write, manuscript edit or LaTeX compile occurred.

## 2026-08-13 COMST Nine-Section Manuscript Restructuring Memory â€” Historical Snapshot

- Active reading candidate: `07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- The candidate is a non-destructive restructuring of `comst_206_v1`; v1 remains the rollback source and was not overwritten.
- Structure: one abstract and nine main sections. The survey progression is Introduction; foundations/comparison framework; review method/evidence base; optical platforms/integration architectures; metrics/joint-design tradeoffs; validation/reproducibility/benchmark readiness; technologies/applications/6G; discussion/roadmap/limitations; conclusion.
- Scientific center remains the O-ISAC survey. PRISMA and PRISMA-S support traceability but are not presented as the manuscript's technical contribution.
- Final QA PASS: manuscript integrity, evidence assertions, survey architecture and candidate lineage.
- Final visual-contract QA PASS: 16/16 carriers, 221/221 checks and zero failures. This is a specification gate only; it generated no figure or pending table.
- Visual state: eight figures plus eight tables are contracted. Table I alone is live; seven tables and eight figures remain pending. No figure was generated.
- No LaTeX compile, page rendering or layout inspection was performed.
- Governance state: author review/approval pending; manuscript not submission-ready. Do not call it final, approved or typeset.
- Locked Phase-C/Phase-D/Phase-E/Phase-F evidence authorities, public-release staging and the historical unpublished 220/221-study manuscript were not modified.
- Checkpoint-time deterministic directory digests: v1 `CA0A7B234901779061CB3F7EF996C261BF62655382047420945E0388B4C04F2B`; v2 `BE1BC69DD190BC891323308D183CCB81F08EFBA871A51D7DC8BC0AC367363F37`.
- Checkpoint: `09_kayitlar/checkpoints/comst_manuscript_9section_RESTRUCTURED_2026-08-13/README.md`.
- Next safest action: author review of the complete nine-section candidate. Materialize the remaining carriers and compile only after that review.

## 2026-08-14 COMST Post-fix Full Re-audit Memory â€” Superseded by Current Closeout

- Current candidate remains
  `07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`;
  v1 and the unpublished 220/221-study manuscript remain preserved history.
- Governing principle: 76 COMST papers are style, section-architecture, and
  visual-design exemplars only. They are not scientific evidence authorities.
- The discovered citation gap is closed locally. ST-01 contains 206 unique
  studies with 206 semantic `\cite{}` rows and exact bibliography keys. The
  separate eligible-report carrier has 227 rows: 206 primary and 21 companion.
- The main manuscript bibliography explicitly includes all 206 exact study
  keys without `\nocite{*}`. Narrative prose remains claim-attached and
  selective.
- Local journal-candidate evidence carriers: 39 exclusions; 3,020 primary
  evidence; 4,779 primary metrics; 404 governed/402 substantive tradeoffs; 206
  TQAF studies; 115 evidence bodies; 4,931 memberships. Contextual syntheses
  are 38 and outside the 206 denominator.
- Supplement S7 has a one-to-one 206-row join, 12 maximum-tier studies, and 6
  paired-function studies. Relationship timing and separate function-specific
  locators are explicit `NR`, not inferred.
- Reporting carrier includes executed six-source search records, four protocol
  and amendment files, eight deviations, 446 data-dictionary rows, and honest
  disclosure of two unreconstructed Taylor & Francis query mappings.
- Active abstract = 250 words; canonical name = Technical Quality Assessment
  Framework. It reports retrospective OSF registration, no support, and the
  main evidence boundaries.
- Sentence-level re-audit fixed 11 findings. Post-fix integrated QA passes
  32/32. Post-fix PRISMA: 29 READY, 6 PARTIAL, 0 OPEN, 7 JUSTIFIED_NA.
- Current QA index:
  `comst_206_v2_9section/qa/CURRENT_QA_INDEX_2026-08-13.md`. Old undated
  `FINAL_*` and the pre-fix PRISMA report are superseded snapshots.
- Still not submission ready: Figures 1--8 and Tables II--VIII are not
  generated; no standalone driver, compile, or rendered QA exists; title/front
  matter awaits author approval; CRediT, creator scope, rights/year, licenses,
  clean repository, version, and DOI remain open.
- No GitHub/Zenodo write or public release occurred.
- Checkpoint:
  `09_kayitlar/checkpoints/comst_manuscript_POSTFIX_FULL_REAUDIT_2026-08-13/README.md`.
- Next safest action: visual/table production from frozen authorities, then
  integrated author reading and rendered manuscript QA.


