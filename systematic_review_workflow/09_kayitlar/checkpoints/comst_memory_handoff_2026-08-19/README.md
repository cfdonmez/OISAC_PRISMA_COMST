# O-ISAC COMST v2 — Yeni Sohbet Devam Kaydı

Tarih: 2026-08-19  
Son doğrulama: 2026-08-24  
Durum: Sections I--IV yazar okumasında kabul edildi; Section IV survey
öncelikli biçimde bütünsel olarak yeniden yazıldı ve teknik QA aldı. Table IV
platform-family ayrıntılarını taşır; dört platform-family unit kısaltıldı ve
Integration Architectures birimi mekanizma odaklı olarak yenilendi. IV-C'nin
somut teknik iddiaları claim-adjacent citations ile tamamlandı. Section V
açılışı positive survey diliyle yenilendi. Table V, Table IV ile aynı survey-map
ilkesine göre tek sütunlu ve iki bloklu kompakt bir özet olarak yeniden kuruldu.
Section II ve Table II de aynı ilkeyle geriye dönük olarak sıkıştırıldı. Metrics
Across Functions üç bağlı survey unit olarak tamamlandı. How Communication and
Sensing Performance Interact survey-first olarak yeniden kuruldu ve teknik QA
aldı. V-D, Conditions for Comparison Across Studies başlığı altında 130 word, iki
paragraf ve dokuz cümlede tamamlandı. Prohibited style marker sayısı sıfırdır ve
table/prose carrier ayrımı korunmuştur. Section V author reading tamamlandı.
Sıradaki okuma noktası Section VI opening'dir. Sekiz ana metin görseli henüz
üretilmedi.

## 1. Bu kaydın işlevi

Bu dosya yeni bir Codex sohbetinde çalışmaya yanlış taslaktan, eski paydadan
veya tarihsel bir “next step” kaydından başlanmasını önler. Yeni sohbet önce
repo kökündeki `AGENTS.md` dosyasını, sonra
`START_HERE_OISAC_PRISMA_CURRENT.md` dosyasının en üst güncel bölümünü ve
`systematic_review_workflow/09_kayitlar/codex_memory_bank.md` içindeki
`CURRENT RESUME AUTHORITY — 2026-08-19` bölümünü okumalıdır.

Eski checkpointler silinmemiştir; audit trail olarak korunurlar. Güncel çalışma
emri değildirler.

## 2. Aktif manuscript otoritesi

Aktif title:

*Optical Integrated Sensing and Communication for 6G: A Systematic Review and
Survey of Architectures, Metrics, and Tradeoffs Across Optical Platforms*.

Aktif klasör:

`systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`

Temel dosyalar:

- derleyici: `main.tex`;
- okuma sırası: `MANUSCRIPT_BODY_INPUTS.tex`;
- bölüm dosyaları: `sections/00_ABSTRACT.tex` ile
  `sections/10_REPORTING_DECLARATIONS.tex`;
- güncel PDF: `main.pdf`;
- yapı kaydı: `MANUSCRIPT_STRUCTURE.json`;
- aday durum özeti: `README.md`;
- güncel QA dizini: `qa/CURRENT_QA_INDEX_2026-08-13.md`.

`comst_206_v1` yalnız rollback kaynağıdır. Yayınlanmamış 220/221 çalışmalı
taslak bilimsel, sayısal veya editoryal otorite değildir.

## 3. Makalenin güncel mimarisi

Makale dokuz ana sectiondan oluşur:

1. Introduction: motivasyon, survey sınırı, önceki sentezlerin konumu,
   Table I ve dört katkı.
2. O-ISAC Foundations and Comparison Framework: sistem sınırı, modalite,
   coupling, measurement contract ve karşılaştırma profili.
3. Review Process and Evidence Base: yalnız kısa corpus construction,
   evidence use ve technical appraisal açıklaması.
4. Optical Platforms and Integration Architectures.
5. Performance Metrics and Joint Design Tradeoffs.
6. Validation, Reproducibility, and Benchmark Readiness.
7. Enabling Technologies, Applications, and 6G Implications.
8. Discussion, Research Roadmap, and Limitations.
9. Conclusion.

Abstract ana section sayısına dahil değildir. Reporting declarations makale
sonunda numarasız taşıyıcıdır.

## 4. Yazarla birlikte okuma sırasında ulaşılan nokta

- Abstract bilinçli olarak sona bırakıldı. Şimdilik yeni bir abstract revizyonu
  başlatılmamalı.
- Introduction ayrıntılı biçimde gözden geçirildi ve yaklaşık 531 prose
  kelimesine indirildi. Table I kendi başına okunur hâle getirildi. Eski
  reader-facing ST-RS1 notu ve annex yönlendirmesi çıkarıldı. Dört katkı
  tekrarlanan `We` girişleri yerine noun-led scientific deliverables biçiminde.
- Section I ile Section II arasında O-ISAC yeniden tanımı ve gereksiz kapsam
  tekrarı kaldırıldı. Section II açılışı doğrudan comparison framework işine
  geçer.
- Section II 711 prose word, 12 paragraph ve 46 sentence içerir. Table II dört
  comparison component ile üç analytical use taşıyan kompakt iki-panel survey
  map'tir. Exact fields/codes S-Data Dictionary'de, record-level provenance ve
  rationale S-Evidence'da kalır. Figure 1 ve Figure 2 için ayrıntılı üretim
  tarifleri section dosyasında yorum olarak bekler; görseller üretilmedi.
- Section III, okuyucuya PRISMA öğretmeyecek biçimde yeniden yazıldı. Governing
  QA count 635 prose kelimesidir. Section II'nin kapanışı ile Section III'ün
  açılışı, comparison conditions'tan evidence base'e açık bir geçiş kurar. Üç
  alt bölüm vardır: `Corpus
  Construction`, `Evidence Extraction and Use`, `Technical Appraisal and
  Synthesis`. Table III aktiftir. Figure 3 ve Figure 4 tarifleri hazırdır.
- Corpus Construction ilk paragrafı COMST paragraph recipe'e göre yeniden
  kurulmuştur: doğrudan `we searched`/`we retained` eylemleri kullanılır;
  search, eligibility, denominator ve supplement işleri checklist ritmine
  düşmeden ayrılır.
- İkinci Corpus Construction paragrafı ara selection sayılarını prose'da
  yinelemez; 227 eligible report, 21 companion report ve 206 unique study
  ayrımını yorumlar. Full path Fig. 3 specification'da, lineage ST-01'dedir.
- Evidence Extraction denominator→provenance→claim-use sırasını kurar; Table III
  kategori envanterini taşırken prose claim-level restriction'ın anlamını verir.
- Technical Appraisal TQAF boyutları ile ayrı overall contribution kategorisini
  ayırır, 125/75/6 sonucunu yorumlar ve structured narrative synthesis'e bağlar.
  Section closing, native task/unit/conditions/validation meaningini korurken
  recurring mechanisms ve design relationships'i corpus genelindeki ortak
  analytical level olarak kurar; 115 body/seven-domain traceability korunur.
  TQAF survey içindeki amacı, deterministic kuralları ve synthesis-support
  anlamıyla pozitif tanıtılır. Nonvalidation, RoB/GRADE ve scientific-worth
  sınırı Section VIII Limitations ve reporting supplements'a ayrılmıştır.
- Table II Section III başlamadan önce, Table III kendi lead-in'inden sonra ve
  subsection C'den önce render edilir; sentence interruption veya anomalous
  whitespace yoktur.
- Section III içindeki audit-history ve AI workflow anlatısı kaldırıldı.
  Zorunlu IEEE AI-use açıklaması yalnız
  `sections/10_REPORTING_DECLARATIONS.tex` içindedir ve silinmemelidir.
- Section III ve Section IV kullanıcı tarafından kabul edildi. Section IV bütünsel
  survey-first revizyondan sonra 1,880 TeXcount text word, 25 prose paragraph ve
  113 sentence içerir; önceki 2,880-word durumundan 1,000 word ve %34.7 kısadır.
  Table IV family counts, tasks, constraints ve transfer conditions taşır;
  family prose mechanism, recurring pattern ve engineering meaning taşır.
- Fiber, VLC/LiFi, free space optical ve hybrid/residual units toplam 564 word
  ve sekiz paragraftır. IV-B 678 word ve on paragrafta coupling location,
  recurring mechanism, engineering consequence ve evidence form taşır. Section
  IV'te 71 unique included-study key ve 56 citation command vardır. IV-C'nin
  concrete platform ve shared-constraint claims'i dört compact citation cluster
  ile desteklenir. Regenerated citation crosswalk 206/206 PASS, 0 missing, 421 included-study use, 198
  citation command ve maximum cluster 7 verir.
- Fig. 5 specification yedi overlapping integration location, locked counts ve
  üç mixed case'i taşır. Figür aktive edildiğinde current numerical coupling
  inventory prose'dan kaldırılır. Table IV ile Section III→IV ve IV→V
  transitions scientific/build/rendered QA PASS aldı. Section V opening 159
  word, üç paragraph ve on sentence içerir. Opening, V-A lead ve Table V
  semicolon, colon veya negative-marker cadence içermez. Table V artık PDF page
  8'de, V-A lead'in hemen ardından tek sütunlu bir survey map olarak yer alır.
  Eski üç panelli audit matrix yerine metric-domain coverage ve analytical-role
  özetini taşıyan iki kompakt blok kullanır. 4,779 denominator, overlapping
  85/60/50 coverage ve 118/4,661 split korunur. Semantic ayrıntı V-B'de,
  row-level provenance S-Evidence'da, tradeoff dağılımı Fig. 6'da kalır.
  Communication Metrics 326 word ve 19 cümlede rate accounting, reliability,
  measurement plane ve physical/temporal scope sırasını izler. Sensing Metrics
  275 word ve 19 cümlede task, estimation, dataset context ve comparison
  conditions akışını kurar. Joint and Implementation Metrics 249 word ve 15
  cümlede matched evidence, optimization ve platform burden akışını kurar.
  How Communication and Sensing Performance Interact 2,262 prose word, 30
  paragraph ve 149 sentence içerir. İki paragraflık giriş shared resource'ları
  evidence scope'tan önce açıklar. Shared design choice, observed response,
  source condition ve engineering meaning akışını kullanır. Önceki 176 citation
  key ve 180 citation use korunmuştur. Governed ledger ve detailed profile
  planlanan Fig. 6 ile supplement'lere aittir. Conditions for Comparison Across
  Studies V-D'yi 130 word, iki paragraf ve dokuz cümlede kapatır. Prohibited
  style marker sayısı sıfırdır ve table/prose carrier ayrımı korunmuştur.
  Section V güncel olarak 3,562 TeXcount text word içerir. Section V author
  reading tamamlanmıştır. Güncel yazar okuma noktası Section VI opening'dir.

## 5. Kullanıcının kalıcı yazım ve çalışma tercihleri

1. Bu bir survey makalesidir. PRISMA, veri yönetimi veya proje geçmişi ana
   hikâyenin önüne geçmemelidir.
2. Okuyucu hızlı anlamalı, merak etmeli ve ilgilendiği özgün çalışmaya
   referanslardan ulaşabilmelidir.
3. Metin kısa tutulabilir. COMST örneklerinin kelime sayısına ulaşmak için
   dolgu yapılmaz.
4. Ton akademik fakat doğal olmalıdır. Robotik kalıplar, aynı fiille başlayan
   katkı listeleri, aşırı meta-writing ve günlük konuşma tonu kullanılmaz.
   Reader-facing prose, caption ve table note içinde yazar kaynaklı iki nokta
   veya noktalı virgül kullanılmaz. `Neither ... nor`, art arda `not` ve
   denylist cadence doğal bağlaçlar veya açık cümlelerle yeniden kurulur.
5. Sınırlar ve eksiklikler dürüstçe verilir; fakat anlatı sürekli olumsuzluk
   diliyle kurulmaz. Pozitif, koşullu ve bilimsel çerçeve tercih edilir.
6. Bilimsel dürüstlük, bütün doğru olumsuzlukları ana prose'a taşımak değildir.
   Bir caveat yalnız inference'ı değiştiriyor, yanlış okumayı önlüyor veya
   reporting/reproducibility için gerekiyorsa reader-facing metne girer; uygun
   carrier'da bir kez ve etkisiyle birlikte verilir. QA denylistleri prose'a
   çevrilmez; katkı, construct, evidence ve geçerli koşul önce kurulur.
7. Okuyucuyu maddi olarak yanıltacak bilgi saklanmaz; ancak sonucu değiştirmeyen
   “yapılmadı/kapsam dışı/değildir” envanterleri foreground edilmez. Gereksiz
   self-devaluation manuscriptin bilimsel değerini ve survey akışını düşürür.
8. Aynı terim, acronym, kapsam veya bölüm görevi sonraki section açılışlarında
   yeniden tanımlanmaz. Her section yalnız kendi reader job’unu taşır.
9. Tire ve çizgi yalnız teknik doğruluk veya resmi yazım gerektirdiğinde
   kullanılır. Kolayca yeniden ifade edilebilen birleşik yapılarda mümkün
   olduğunca çizgisiz İngilizce tercih edilir.
10. Büyük tablo ve görseller prose tekrarını azaltmalıdır. Metin float içindeki
   her hücreyi, düğümü veya sayıyı yeniden anlatmamalıdır.
11. Kullanıcıya micro-management yaptırılmaz. Codex örnekleri, otorite
   dosyalarını ve QA’yı kendisi inceler; güvenli ve kanıta dayalı düzeltmeleri
   uygular; kullanıcıdan yalnız gerçekten yazar kararı gereken durumda girdi
   ister.
12. Bölüm bölüm okuma sırasında kullanıcının yalnız `anlamadım`, `yoruldum`
    veya `katılmıyorum` demesi yeterlidir. Teşhis, yeniden yazım, kaynak ve
    biçim kontrolü Codex’in işidir.

## 6. Section sahipliği ve tekrar yasağı

- Section I: motivasyon, kapsam, prior-survey positioning ve katkı vaadi.
- Section II: comparison vocabulary ve admissibility framework.
- Section III: method, denominators, evidence governance ve appraisal sınırı.
- Section IV: platform physics ve integration mechanisms.
- Section V: metric meaning, admissibility ve tradeoff synthesis.
- Section VI: validation maturity, reproducibility ve benchmarks.
- Section VII: technologies, applications ve 6G relevance.
- Section VIII: higher-order implications, research roadmap ve limitations.
- Section IX: kısa, yeni kanıt eklemeyen kapanış.

Bir section başka sectionın tanımını, bulgusunu veya roadmap’ini yeniden
kurmamalıdır. Geçiş cümlesi önceki bölümü özetlemek yerine çözülmemiş ilişkiyi
sonraki bölümün reader job’una bağlamalıdır.

## 7. Kilitli bilimsel paydalar

- Arama/evidence window: 1 Ocak 2020 ile 22 Haziran 2026.
- Identified records: 1,733.
- Screened records: 1,259.
- Reports sought: 330.
- Full-text reports assessed: 272.
- Full-text exclusions: 39.
- Full-text aşamasında contextual retained: 6.
- Eligible reports: 227.
- Unique included studies: 206.
- Companion reports: 21; multi-report studies: 19.
- Governed claims: 8,306 = 3,041 evidence + 4,861 metric + 404 tradeoff.
- Primary synthesis: 8,203 = 3,020 evidence + 4,779 metric + 404 governed
  tradeoff.
- Survey use: 3,206 qualitative, 4,997 quantitative, 31 context only, 72
  quarantined exact claims.
- Substantive tradeoff profile: 402 records / 168 studies / 218 quantitative /
  184 qualitative / 371 conditional.
- TQAF overall contribution: 125 strong / 75 adequate / 6 low.
- Evidence bodies: 115; memberships: 4,931.
- Modalities: 69 photonics assisted THz, 56 fiber, 38 VLC/LiFi, 31 FSO, 9
  hybrid optical, 3 other optical.
- Maximum field/deployment tier: 12 studies; narrower paired-function gate: 6.
- Exclusive 6G relevance: 138 direct / 64 inferential / 1 weak / 3 not
  applicable.

Bu paydalar yeniden yorumlanmaz veya eski 220/221 taslağından türetilmez.
`record`, `report`, `study`, `claim row`, `metric row` ve `tradeoff record`
birbirinin yerine kullanılamaz.

## 8. Atıf ve referans politikası

- Ana metin 206/206 included study’yi bilimsel olarak uygun cümle veya tablo
  bağlamında cite eder.
- Ana bibliography 243 girdidir: 206 included study, 29 contextual/method
  source ve exact report-derived claimlerde kullanılan 8 companion report.
- ST-01 bütün 227 eligible reportu çözer: 206 primary + 21 companion.
- Ana metinde bir citation cluster en fazla 7 included study taşır. Cluster
  tematik ve claim matched olmalıdır.
- `\nocite`, manuel `[1-30]` numaraları, tek bir dipnotta citation dump veya
  yalnız coverage artırmak için ilişkisiz citation ekleme yapılmaz.
- Companion report yalnız o rapordan gelen belirli bir iddia kullanıldığında
  ana metinde cite edilir. Study prevalence her zaman `study_id` ile
  deduplicate edilir.
- Table I’de 24 prior synthesis doğrudan cite edilir. 38-source contextual
  synthesis register yalnız internal positioning audit’tir; ST-RS1 adıyla
  reader-facing annex değildir ve submission paketine girmez.

## 9. Görsel ve tablo durumu

Ana mimari 16 carrier içerir: sekiz table + sekiz figure.

Aktif tablolar:

- Table I: prior syntheses;
- Table II: compact comparison components and analytical-use map;
- Table III: use of extracted evidence;
- Table IV: modality families;
- Table V: metric domains and admissibility;
- Table VI: artifact availability and reconstruction contract;
- Table VII: application requirements;
- Table VIII: evidence linked research roadmap.

Bekleyen görseller:

- Fig. 1, Section II: native evidence objects;
- Fig. 2, Section II: four-axis comparison framework;
- Fig. 3, Section III: PRISMA record → report → study flow;
- Fig. 4, Section III: eight TQAF dimensions + separate overall row;
- Fig. 5, Section IV: seven overlapping integration locations;
- Fig. 6, Section V: three-panel substantive tradeoff profile;
- Fig. 7, Section VI: maximum validation tier + multilabel validation methods;
- Fig. 8, Section VII: technology, observable, application and 6G chain.

Görseller dekoratif değildir. Kanonik veri dosyalarından yeniden üretilmeli,
editable vector biçiminde olmalı, colorblind/grayscale safe encoding taşımalı,
final boyutta en az 8 pt metin kullanmalı ve alt text içermelidir. Sayılar
prose’dan kopyalanmaz. Raw public modality/mechanism labels kanonik sayılmaz;
frozen Phase E crosswalk ve Phase F normalization kullanılır.

## 10. Aktif ek paket ve taşıyıcılar

Aktif paket:

`OISAC_COMST_SUPPLEMENT_FINAL_V10_2026-08-17.zip`

- SHA-256:
  `4f140851568a667ac0b9dde0b57c104742b0f747f2abb28335cffe37fe61617d`;
- 40 allowlisted source + 2 metadata = 42 ZIP entry;
- package directory: `submission_supplement_final_v10_2026-08-17/`;
- source/package hash mismatch: 0.

Aktif manuscript altındaki taşıyıcılar:

- `supplements/st01/`: 206 study, 227 report, 227-entry report bibliography;
- `supplements/evidence/`: exclusions, 3,020 evidence, 4,779 metric, 404
  governed ve 402 substantive tradeoff, 206 TQAF, 115 bodies ve 4,931
  memberships;
- `supplements/reporting/`: executed search views, protocol/amendments,
  446-field dictionary, review-conduct/reporting boundaries;
- `supplements/s7/`: 206-row join, 12 maximum-tier ve 6 paired-function subset;
- `supplements/related_synthesis/`: internal audit only, not submission annex.

Reader-facing supplement alias ve exact path eşlemesi
`supplements/README.md` içindedir.

## 11. Otorite hiyerarşisi

Çelişki durumunda şu sıra izlenir:

1. Hash-locked Phase C/D master ve final selection ledgers.
2. Frozen Phase E crosswalk ve TQAF audit.
3. Final Phase F S1–S7 outputs.
4. Aktif v2 manuscript ve materialized supplement projections.
5. Güncel QA ve bu checkpoint.
6. COMST almanakı yalnız yapı, ton ve görsel işlev örneği olarak.
7. v1, 220/221 taslak, eski ZIP/QA/checkpoint ve staging dosyaları yalnız
   tarihsel audit veya rollback için.

Derived CSV/XLSX/PDF bir upstream locked authority ile çelişirse upstream
otorite kazanır ve derived taşıyıcı yeniden üretilir.

## 12. Kuralların bulunduğu dosyalar

- Repo çalışma disiplini: `AGENTS.md`.
- Güncel başlangıç/next step: `START_HERE_OISAC_PRISMA_CURRENT.md`.
- Ayrıntılı bağlam: `PROJECT_CONTEXT_OISAC_PRISMA.md`.
- Ana memory: `systematic_review_workflow/09_kayitlar/codex_memory_bank.md`.
- Kararlar ve ilerleme: `systematic_review_workflow/09_kayitlar/decision_log.md`
  ve `progress_tracker.md`.
- Manuscript scope, protected anchors ve section journey:
  `comst_206_v2_9section/00_SCOPE_AND_SOURCE_MANIFEST.md`.
- Section ownership/editing decisions:
  `comst_206_v2_9section/01_SECTION_LEVEL_EDITING_DECISIONS.md`.
- Güncel 8 figure + 8 table yerleşim sözleşmesi:
  `comst_206_v2_9section/02_VISUAL_AND_TABLE_PLACEMENT_CONTRACT.md`.
- Supplement authority ve carrier kuralları:
  `comst_206_v2_9section/03_SUPPLEMENTARY_EVIDENCE_CONTRACT.md`.
- Yazar okuma rehberi:
  `comst_206_v2_9section/SECTION_BY_SECTION_REVIEW_GUIDE_TR_2026-08-14.md`.
- Aktif title/authors/declarations:
  `comst_206_v2_9section/FRONT_MATTER_ACTIVE_2026-08-14.md` ve
  `sections/10_REPORTING_DECLARATIONS.tex`.
- Güncel QA otoritesi:
  `comst_206_v2_9section/qa/CURRENT_QA_INDEX_2026-08-13.md`.
- Section V and compact Table V governing current-text QA:
  `qa/SECTION5_TABLE5_SURVEY_MAP_QA_2026-08-21.md/json`.
- Section V-C governing current-text QA:
  `qa/SECTION5_TRADEOFF_MECHANISMS_SURVEY_FIRST_QA_2026-08-24.md/json`.
- Section V-D governing current-text QA:
  `qa/SECTION5_CROSS_STUDY_COMPARISON_QA_2026-08-24.md/json`.
- Section II and compact Table II governing current-text QA:
  `qa/SECTION2_TABLE2_SURVEY_MAP_QA_2026-08-21.md/json`.
- Approved Section V opening baseline, with its former Table V layout identity
  superseded by the current-text QA above:
  `qa/SECTION5_OPENING_SURVEY_FIRST_QA_2026-08-21.md/json`.
- Approved Section IV QA: `qa/SECTION4_SURVEY_FIRST_QA_2026-08-20.md/json`.
- Approved Section III snapshot:
  `qa/SECTION3_AUTHOR_REREAD_PREP_QA_2026-08-19.md/json`; compression baseline:
  `qa/FINAL_SECTION3_SURVEY_FIRST_QA_2026-08-17.md/json`.
- Citation completion ve placement:
  `qa/FINAL_CITATION_COMPLETION_QA_2026-08-16.md/json`,
  `qa/FINAL_MAIN_CITATION_COVERAGE_206.md/json` ve
  `qa/CITATION_PLACEMENT_CROSSWALK_206.csv/xlsx`.
- Companion provenance:
  `qa/FINAL_COMPANION_DELIVERABLE_QA.md/json`.
- PRISMA local closure:
  `qa/PRISMA_2020_FINAL_LOCAL_REAUDIT_2026-08-14.md/json/csv`.
- Locked eligibility:
  `checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/`.
- Locked reviewer/adjudication process:
  `checkpoints/prisma_pre_full_text_eligibility_gate_step2_2026-07-19/`.
- Detailed method/TQAF/body thresholds:
  `supplements/reporting/S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md`.
- COMST architecture/tone evidence:
  `07_raporlama/outputs/comst_76_fulltext_almanac_2026-08-09/` ve
  `07_raporlama/outputs/comst_prose_revision_2026-08-08/style_profile/`.
  Bunlar O-ISAC scientific fact authority değildir.
- Global visual grammar:
  `visual_blueprint_2026-08-10/reports/GLOBAL_VISUAL_STYLE_AND_PRODUCTION_CONTRACT.md`.
  Bu dosyanın eski status, section number ve placement cümleleri tarihsel;
  görsel grammar ve accessibility kuralları geçerlidir. Güncel yerleşimde v2
  `02_VISUAL_AND_TABLE_PLACEMENT_CONTRACT.md` kazanır.

## 13. Güncel derleme ve QA

- `main.pdf`: 25 sayfa; 206,753 byte; US Letter.
- PDF SHA-256:
  `4CDD36AA2A260A5E70AA7056D9B65D7541E36E459F694750EDA210F7B936F5C9`.
- Section II source SHA-256:
  `30f900165a2226f9d9fd8f48033d9b0af314ed317aefa88b6fceabf249757d20`.
- Section V source SHA-256:
  `D733C6CC379DC648CF058211F0A99146890BB8DFE772865829611F6D33FC12AF`.
- 243 resolved main bibliography entry.
- 206/206 included study cited.
- Citation placement crosswalk: 206 PASS, 0 missing, 421 included-study uses,
  198 citation commands, maximum cluster 7.
  CSV SHA-256:
  `3DA2B47E38E4C30B1F82FFD13041143016F7C824C5A4F5186AE3AC8E8F340644`;
  XLSX SHA-256:
  `7ECF2AFCBBE5EFE5E073AF178FFBD009BF2331959DBB3C8BC04036E5D22D190D`.
- 8 live table; 0 active figure/includegraphics.
- Undefined citation/ref: 0.
- Fatal LaTeX error: 0.
- Overfull box: 0.
- Supplement package mismatch: 0.

Bu sayfa sayısı görsellerden önceki baseline’dır. Sekiz görsel eklendikten sonra
yeniden compile, cross-reference, rendered-page ve final layout QA yapılır.

## 14. Yeni sohbet için kesin devam sırası

1. Bu checkpoint ve ana memory bank’in 2026-08-19 bölümünü oku.
2. Aktif `main.pdf` ve kullanıcının işaret ettiği section dosyasını aç.
3. Kullanıcı Section VI opening'den devam eder. Yalnız işaretlediği passage'ı
   değil bütün Section VI'yı, ilgili carrier'ları, citations'ı ve V→VI / VI→VII
   sınırlarını birlikte kontrol ederek düzelt.
4. Section VI'yı bütün olarak denetle ve survey-first revizyonu uygula.
5. Aynı yöntem Sections VI--IX için kullanılır. Abstract en sona bırakılır.
6. Prose author review tamamlandıktan sonra Figures 1–8 üretilir ve aktive
   edilir.
7. Her substantive edit sonrası citation set, locked counts, labels/refs,
   compile log ve rendered PDF kontrol edilir; state değişirse continuity
   dosyaları birlikte güncellenir.

## 15. Yapılmaması gerekenler

- 206 study / 227 report paydasını yeniden açma.
- OSF 221’den 206’ya attrition hikâyesi yazma.
- PRISMA’yı Section III’te öğretme veya audit history’yi prose’a geri taşıma.
- Sections I–IX içine AI workflow anlatısı ekleme; mandatory disclosure yalnız
  reporting declarations’ta kalır.
- ST-RS1’i reader-facing annex olarak geri getirme.
- Citation completeness’i uzun dipnot veya ilişkisiz mega-trenle çözme.
- Aynı acronymi her sectionda yeniden açma.
- Heterojen sonuçlardan pooled effect, universal frontier veya platform
  leaderboard üretme.
- TQAF’ı conventional risk of bias, GRADE veya study ranking gibi sunma.
- Raw public modality/mechanism labels ile figure üretme.
- Decorative 6G art, pie/donut, radar, 3D, dual-axis, rainbow veya color-only
  visual kullanma.
- Eski V1/V4–V9 package, undated FINAL visual QA veya historical “next”
  kayıtlarını current truth kabul etme.

## 16. İnsan/yayın aşamasında kalan dış işler

- Abstract’ın son yazar okuması ve final polishing.
- Figures 1–8’in üretimi ve yerleştirilmesi.
- Figure-inclusive final layout/page-budget QA.
- Submission portalında ORCID authentication ve supplement upload.
- İstenirse public repository, license, release tag ve DOI işlemleri.

Bu dış işlemler locked scientific corpus’u değiştirmez.

Memory synchronization QA:

`systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/qa/MEMORY_HANDOFF_QA_2026-08-19.md/json`

## 17. Yeni sohbete yapıştırılabilecek kısa başlangıç mesajı

> O-ISAC COMST projesine kaldığımız yerden devam ediyoruz. Önce
> `prisma2020Review/AGENTS.md`, `START_HERE_OISAC_PRISMA_CURRENT.md` Bölüm 19,
> `systematic_review_workflow/09_kayitlar/codex_memory_bank.md` içindeki
> `CURRENT RESUME AUTHORITY — 2026-08-19` ve
> `checkpoints/comst_memory_handoff_2026-08-19/README.md` dosyalarını oku.
> Aktif manuscript `comst_206_v2_9section`; Abstract en sona bırakıldı;
> Sections I–IV gözden geçirildi ve kabul edildi; Section IV bütünsel
> survey-first revizyondan geçti. Table IV family inventory ve comparison
> conditions taşır; IV-B coupling location, recurring mechanism, engineering
> consequence ve evidence form taşır. IV-C concrete mechanism claims için dört
> compact citation cluster taşır. Section V opening 159 word, üç paragraph ve
> on sentence içerir. Table V, V-A lead'in hemen ardından PDF page 8'de yer alan
> tek sütunlu ve iki bloklu kompakt bir survey map'tir. Metric-domain coverage
> ve 118/4,661 analytical-role split'ini özetler; semantic ayrıntı V-B'de,
> row-level provenance S-Evidence'da ve tradeoff dağılımı Fig. 6'da kalır.
> Communication Metrics, Sensing Metrics ve Joint and Implementation Metrics
> kendi bağlı survey akışlarını tamamlar. How Communication and Sensing Performance Interact shared
> design choice, observed response, source condition ve engineering meaning akışında yeniden
> kurulmuştur. Detailed eleven-family profile Fig. 6'ya aittir. Conditions for
> Comparison Across Studies V-D'yi iki paragrafta kapatır ve Section V author reading
> tamamlanmıştır. Okuma Section VI opening'den sürüyor. Bana
> micro-management yaptırma. Ben
> yalnız anlaşılmayan, yoran veya katılmadığım yeri işaretleyeceğim; sen bütün
> sectionı, komşu geçişleri, citations, COMST survey tonu, table/figure taşıyıcı
> ayrımını ve locked evidence’ı kontrol ederek düzelt. Section VI'ya bütün olarak
> geçiyoruz. Figures 1–8 prose review sonrasında
> üretilecek; 206/227 ve Phase C–F kilitlerini yeniden açma.
