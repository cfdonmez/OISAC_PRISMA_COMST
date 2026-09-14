# Tam Makale İlişkilendirme Haritası — V3 Aday Mimarisi

**Durum:** Yazar incelemesine açık mimari taslak  
**Tarih:** 2026-09-03  
**V3-S1 güncellemesi:** 2026-09-04 tarihinde bilimsel çekirdek kilidi yazar
incelemesine açıldı; henüz onaylanmış veya kilitlenmiş değildir.  
**Kaynak metin:** outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section  
**Amaç:** Mevcut metni parça parça yamamak değil; bütün makaleyi tek bilimsel
soru, tek kanıt nesnesi ve görünür bölüm devirleri etrafında yeniden kurmak.

Bu belge bir manuscript uygulaması değildir. Önce makalenin bilimsel
mimarisini kilitlemek, ardından yeni sürüm ağacını bu sözleşmeye göre kurmak
için hazırlanmıştır.

## 1. Makalenin tek merkezî sorusu

> Across heterogeneous optical integrated sensing and communication (O-ISAC)
> platforms, what combination of physical paths, coupling mechanisms or
> locations, and shared design factors links communication and sensing
> performance, and under what measurement and evidence conditions can the
> resulting relations be compared, transferred across designs, and converted
> into testable experimental decisions?

Türkçe çalışma anlamı: Heterojen O-ISAC platformlarında hangi fiziksel yol,
coupling mekanizması veya konumu ve ortak tasarım etkeni bileşimi iletişim ile
algılama performansını birbirine bağlamaktadır; oluşan ilişkiler hangi ölçüm ve
kanıt koşullarında karşılaştırılabilir, başka tasarımlara aktarılabilir ve
sınanabilir deney kararlarına dönüştürülebilir? Bu ifade ikinci bir araştırma
sorusu değil, kanonik İngilizce sorunun çalışma içi açıklamasıdır.

Bu soru, taxonomy, metrics, tradeoffs, validation, applications ve roadmap'i
ayrı ürünler olmaktan çıkarır. Her biri aynı ilişkinin başka bir parçasını
kurar veya sınar.

## 2. Makalenin merkezî bilimsel nesnesi

\[
J_r=\langle P_r,G_r,X_r,C_r,S_r,M_r,E_r\rangle
\]

- **P — Physical system and target-reaching path:** Sistem sınırı, optics'in
  rolü, hedefe ulaşan sinyal yolu ve varsa optical–RF dönüşüm sınırı.
- **G — Coupling mechanism/location:** Communication ile sensing'in neyi ve
  sistemin neresinde paylaştığı.
- **X — Shared/varied factor:** İki fonksiyonu bağlayan ortak veya değiştirilen
  tasarım değişkeni, kısıt ya da bozucu etken.
- **C — Communication outcomes:** Rate, BER, SNR, latency, reliability,
  coverage ve diğer communication sonuçları.
- **S — Sensing outcomes:** Resolution, accuracy/error, range, sensitivity,
  detection/localization ve diğer sensing sonuçları.
- **M — Measurement contract:** İki outcome'un tanımı, ölçüm düzlemi, birimi,
  accounting state'i, operating point'i, baseline'ı, ground truth'u ve
  condition-set hizası.
- **E — Evidence envelope:** Değerin kaynağı, validation setting'i,
  configuration/timing izi, source locator'ı ve izin verilen çıkarım sınırı.

İlişkinin daha güvenli uygulama biçimi:

\[
M_r=\langle M_C,M_S,A_M\rangle,\qquad
E_r=\langle E_C,E_S,T_r,B_r\rangle
\]

Burada **A_M**, C ile S'nin aynı veya eşlenebilir operating condition altında
üretilip üretilmediğini; **T_r**, aynı configuration/timing izini; **B_r** ise
izin verilen iddianın sınırını gösterir.

### Temel bilimsel karar

Bir communication metriği ile bir sensing metriğinin aynı makalede bulunması,
tek başına joint-performance ilişkisi değildir. İlişki ancak ikisini bağlayan
bir **X** ve izlenebilir bir **M/E** sözleşmesi varsa kurulur.

Makalenin aktarılabilir bilimsel birimi en yüksek ham değer değil:

> Fiziksel bağlamı, ortak nedeni, iki sonucu, ölçüm koşulları ve kanıt sınırı
> birlikte korunan X–C–S ilişkisidir.

## 3. Bütün makale akış haritası

~~~mermaid
flowchart LR
    A["Abstract<br/>Problem + yöntem + ana ilişki + eylem"]
    I["I. Neden bu survey?<br/>Karar boşluğu ve katkı sözleşmesi"]
    II["II. Ne bir joint-evidence ilişkisidir?<br/>J modeli ve claim permissions"]
    III["III. J nasıl üretildi?<br/>Corpus, kayıt katmanları ve QA"]
    IV["IV. Jointness nerede doğuyor?<br/>P x G -> X mekanizma haritası"]
    V["V. Ne oluyor?<br/>X -> (C,S) | P,G,M,E<br/>MAKALENİN BİLİMSEL MERKEZİ"]
    VI["VI. Ne kadar uzağa taşınır?<br/>Validation, paired evidence, reuse"]
    VII["VII. Nerede işe yarar?<br/>Application ve 6G requirement fit"]
    VIII["VIII. Bundan sonra ne yapılmalı?<br/>J boşluğu -> deney -> başarı ölçütü"]
    IX["IX. Araştırmacının alacağı karar<br/>Bounded takeaways"]

    A --> I --> II --> III --> IV --> V --> VI --> VII --> VIII --> IX
    II -. "tanım ve izin kuralları" .-> V
    III -. "metric ve relation records" .-> V
    IV -. "P, G ve X adayları" .-> V
    V -. "kanıtlanmış ilişki ve boşluklar" .-> VIII
    VI -. "transfer sınırı" .-> VIII
    VII -. "gereksinim ve test bağlamı" .-> VIII
~~~

Bu akışta Section V tek sonuç merkezi olur. Diğer bölümler Section V'e ya
girdi getirir, ya sonucu sınırlar, ya da sonucu kullanıma ve araştırma
eylemine çevirir.

## 4. Section düzeyinde görev ve devir sözleşmesi

| Bölüm | Tek okuyucu sorusu | J içindeki görevi | Ürettiği somut çıktı | Sonraki bölüme devir | Revizyon kararı |
|---|---|---|---|---|---|
| **Abstract** | Problem, ana bulgu, sınır ve pratik değer nedir? | Bütün zinciri 4 hareketle özetler. | Problem → corpus/method → X–C–S mechanism finding → actionable implication. | Introduction'da açılacak araştırma sözleşmesi. | **Yeniden yaz.** Taxonomy sonucu değil, karar değeri öne çıksın. |
| **I. Introduction** | Önceki review'lar varken bu survey hangi çözülmemiş işi tamamlıyor? | J'nin tamamını araştırma problemi olarak vaat eder. | Tek merkezî soru, görünür novelty gap ve dört ardışık contribution. | II'ye tanımlanması gereken ilişki nesnesi. | **Yeniden çerçevele.** |
| **II. Foundations and Comparison Framework** | Bir O-ISAC joint-performance ilişkisi nasıl tanımlanır ve hangi iddiaya izin verir? | P, G, X, C, S, M ve E'yi kanonik olarak tanımlar. | J kaydı, failure states ve claim-permission kuralları. | III'e uygulanabilir coding/decision contract. | **Temelden yeniden kur.** |
| **III. Review Process and Evidence Base** | Raporlar denetlenebilir metric ve relationship kayıtlarına nasıl dönüştürüldü? | J'nin corpus üzerinde nasıl operasyonelleştirildiğini açıklar. | Report–study ayrımı, evidence-layer haritası, coding/adjudication ve synthesis route. | IV–VI'ya governed analysis units. | **Yeniden çerçevele; yöntemi uzatma.** |
| **IV. Optical Platforms and Integration Architectures** | Hangi fiziksel yol ve coupling biçimi hangi ortak faktörleri doğuruyor? | P ve G'yi sentezler, Section V için X adayları üretir. | Platform/coupling archetype'ları ve P×G→X haritası. | V'e mekanizma ve fiziksel sınır. | **Güçlü içeriği koru; çıktısını değiştir.** |
| **V. Performance and Joint Design Relations** | X değiştiğinde C ve S nasıl birlikte değişiyor; hangi koşullarda bu ilişki geçerli? | X, C, S ve M'nin merkezî sentezidir; P, G ve E koşullandırır. | Directional/mechanistic relations, verified operating-point anchors, admissible comparison ve non-pooling sonucu. | VI'ya sınanacak relationship claims. | **Temelden yeniden kur; makalenin merkezi yap.** |
| **VI. Validation, Reconstructability and Benchmark Readiness** | Section V'teki ilişkiler ne kadar test edilmiş, yeniden kurulabilir ve taşınabilir? | E'yi relation düzeyinde sınar; C ve S'nin aynı M altında doğrulanmasını arar. | Inference envelope, paired-function validation, reconstructability ve benchmark boundary. | VII'ye permitted application claims; VIII'e evidence gaps. | **Ana yapıyı koru; study label'dan relation testine geçir.** |
| **VII. Technologies, Applications and 6G** | Hangi mekanizma hangi uygulama/network gereksinimini gerçekten destekler? | J'yi use-case requirement düzeyine çevirir. | Technology → G/X → required C/S/M → E → permitted network claim zinciri. | VIII'e test bağlamı ve eksik evidence. | **Envanterden karar matrisine çevir.** |
| **VIII. Discussion, Roadmap and Limitations** | Corpus hangi tasarım dersini ve hangi somut deneyi öneriyor? | Tam J sentezi ve kırık/eksik bağlantıların teşhisi. | Design rules ve observed J break → risk → controlled action → success criterion → artifact. | IX'a bounded nihai hükümler. | **Güçlü iskeleti J eksikleri etrafında yeniden yaz.** |
| **IX. Conclusion** | Araştırmacı bu review'den hangi kararları alıp çıkmalı? | J'nin sınırlandırılmış nihai cevabıdır. | Ne karşılaştırılabilir, ne aktarılamaz, yeni çalışma neyi raporlamalı? | — | **Yeniden çerçevele; yeni veri/citation yok.** |

## 5. Subsection düzeyinde ilişkilendirme haritası

Her alt bölüm aynı beş işi yapmalıdır:

1. Tek bir bilimsel soru sorar.
2. Önceki alt bölümden belirli bir girdi alır.
3. Corpus üzerinde belirli bir ayrım/işlem uygular.
4. Okuyucuya somut bir kayıt, mekanizma, karar veya sınır verir.
5. Sonraki alt bölüme bu çıktıyı adıyla devreder.

### Abstract ve Section I

| Blok | Tek soru | Girdi | Somut çıktı | Devir/taşıyıcı |
|---|---|---|---|---|
| **Abstract-A — Problem** | Heterojen O-ISAC sonuçlarını birlikte okuma sorunu nedir? | Platform ve ölçüm çeşitliliği. | Ham değer veya taxonomy listesinin yeterli olmadığını kuran problem. | Abstract-B. |
| **Abstract-B — Method/evidence** | Review hangi evidence base ve ilişki mantığına dayanıyor? | Frozen corpus ve J yaklaşımı. | Scope + analysis units + non-pooling sınırı. | Abstract-C. |
| **Abstract-C — Findings** | Hangi shared factors iki fonksiyonu tekrar tekrar bağlıyor? | Section IV–VI bulguları. | Condition-dependent X–C–S mechanisms + evidence reach. | Abstract-D. |
| **Abstract-D — Value** | Araştırmacı ne kazanıyor? | Section VII–VIII. | Method choice, experiment design, benchmark/reporting yönü. | Introduction. |
| **I-A — Engineering problem and scope** | O-ISAC'in asıl tasarım problemi nedir? | Reuse, shared infrastructure ve heterojen physical roles. | Merkezî engineering problem. | I-B. |
| **I-B — Prior synthesis positioning** | Önceki review'lar zincirin hangi parçalarını kapsıyor, hangi bağlantıyı kurmuyor? | Domain review corpus. | Açık novelty gap; Table I. | I-C. |
| **I-C — Research contract** | Bu survey hangi soruları hangi sırayla cevaplayacak? | Gap + frozen technical corpus. | Ana soru, contributions ve article logic. | Section II. |

**Section I kabul ölçütü:** Okuyucu, Table I ve contribution listesi sonunda
makalenin yalnız “geniş taxonomy” sunmadığını; P/G/X ile C/S arasındaki
ilişkiyi M/E altında sentezlediğini açıkça görebilmelidir.

### Section II — Joint-evidence model and comparison permissions

| Alt bölüm | Tek soru | Girdi | Somut çıktı | Devir/taşıyıcı |
|---|---|---|---|---|
| **II-A — Unit of synthesis and physical boundary** | Bu survey'de karşılaştırılan bilimsel birim nedir ve hangi physical system içinde oluşur? | Scope ve source-native result. | Result/relationship unit + P signature. | II-B; Fig. 1'in ilk katmanı. |
| **II-B — Coupling mechanism and evidential jointness** | İki fonksiyon neyi, nerede ve hangi ortak faktör üzerinden paylaşıyor? | P signature. | G + X record; structural integration ile evidential jointness ayrımı. | II-C; Fig. 1'in ikinci katmanı. |
| **II-C — Communication/sensing outcomes and measurement alignment** | C ile S gerçekten aynı veya eşlenebilir operating point'te mi? | P/G/X + source outcomes. | C, S, M_C, M_S ve A_M. | II-D. |
| **II-D — Evidence envelope and inference boundary** | İlişki nasıl doğrulandı ve ne kadar uzağa taşınabilir? | Tamamlanmaya aday relation. | E_C, E_S, timing/configuration trace ve bounded inference. | II-E. |
| **II-E — Claim permissions** | Bu kayıtla hangi bilimsel cümleyi kurmaya izin vardır? | J'nin tamamı veya eksiklik durumu. | Native-context, within-study mechanism, bounded numerical comparison, mechanism-level synthesis, descriptive retention veya non-pooling kararı. | Section III; Fig. 2 + Table II. |

**Section II kabul ölçütü:** Fig. 1 sistemde ilişkinin nerede doğduğunu, Fig. 2
karar akışını, Table II ise izin verilen/yasaklanan iddiayı göstermelidir.
Üçü aynı alan listesini tekrar etmemelidir.

### Section III — Corpus and governed evidence construction

| Alt bölüm | Tek soru | Girdi | Somut çıktı | Devir/taşıyıcı |
|---|---|---|---|---|
| **III-A — Corpus construction** | Hangi reports hangi unique studies'i temsil ediyor? | Search/deduplication records. | 227-report/206-study lineage; Fig. 3. | III-B. |
| **III-B — Evidence layers and J construction** | Study, evidence item, metric record ve relationship record nasıl ayrılıyor/bağlanıyor? | Included studies + extraction schema. | Analysis-unit/denominator ledger; Table III. | III-C. |
| **III-C — Appraisal, adjudication and synthesis routing** | Bir kayıt hangi kalite/izin yoluyla sonuç bölümüne giriyor? | Coded records + comparison rules. | Interpretability/transfer profile ve route to Sections IV–VI; Fig. 4. | Section IV. |

**Section III kabul ölçütü:** 206 study, 8,203 primary synthesis rows, 4,779
metric records, 402 substantive relationships ve 115 evidence bodies aynı
sayım birimi gibi görünmemelidir.

### Section IV — Physical and coupling mechanism synthesis

| Alt bölüm | Tek soru | Girdi | Somut çıktı | Devir/taşıyıcı |
|---|---|---|---|---|
| **IV-A — Platform families as physical signatures** | Her platformda optics ne yapıyor ve hedefe ulaşan yol nedir? | P-coded study records. | Altı platform için physical-role/path/conversion/observable signatures; Table IV. | IV-B. |
| **IV-B — Coupling mechanisms** | Communication ve sensing sistemin neresinde bağlanıyor? | P signatures + integration codes. | Multilabel G profile; paylaşımın location/object tanımı. | IV-C. |
| **IV-C — From coupling to shared design variables** | Hangi G, hangi X değişkeni/kısıtı/bozucuyu ortaklaştırıyor? | G profile + relation variables. | P×G→X archetype map; Fig. 5. | IV-D. |
| **IV-D — Cross-platform mechanism boundaries** | Hangi mechanism başka platformda anlamlı biçimde tekrar eder; hangi numerical value etmez? | P/G/X archetypes. | Transferable mechanism hypotheses + platform-native boundaries. | Section V. |

**Section IV kabul ölçütü:** Her platform anlatısı “ne var?” ile değil,
“hangi X iki fonksiyonu bağlar ve hangi fiziksel sınır nedeniyle başka
platforma doğrudan taşınamaz?” cevabıyla kapanmalıdır.

### Section V — Performance relations: scientific centre

| Alt bölüm | Tek soru | Girdi | Somut çıktı | Devir/taşıyıcı |
|---|---|---|---|---|
| **V-A — Reading metric and relation evidence** | Metric record, joint relation ve comparison group arasındaki fark nedir? | 4,779 metric records + 402 substantive relations + Section II rules. | Hangi denominatorın hangi iddiayı taşıdığı; Table V'nin okuma anahtarı. | V-B. |
| **V-B — X-centred relation families** | Her canonical X ailesi C ve S'yi hangi mekanizma ve yönde etkiliyor? | IV'ün P/G/X haritası + relation layer. | X→(C,S) \| P,G,M,E mechanism synthesis; Fig. 6. | V-C. |
| **V-C — Verified quantitative anchors and comparison outcome** | Hangi sayısal ilişkiler condition-complete; hangileri neden pool edilemez? | Source-verified metric groups. | Sınırlı, okunabilir operating-point cards + explicit zero/matched-group sonucu + non-pooling reasons; Table V. | V-D. |
| **V-D — Design rules and failure boundaries** | Bir araştırmacı bu ilişkileri tasarım kararında nasıl kullanmalı? | Mechanism map + quantitative anchors + non-pooling. | Modality-bounded design rules, counterconditions ve unresolved relations. | Section VI. |

**Section V paragraf sözleşmesi:** Her ana sentez paragrafı şu dört hareketi
taşır:

1. Ortak/değiştirilen faktör **X**.
2. Communication sonucu **C** ve sensing sonucu **S**.
3. İlişkinin geçerli olduğu **P/G/M/E** koşulları.
4. Mühendislik kararı ve yanlış genelleme sınırı.

Mevcut Section V alt başlıkları nedenler ile outcome çiftlerini aynı seviyede
karıştırmaktadır. Yeni X aileleri, 402 ilişkinin controlled normalization'ı
sonrasında kilitlenmelidir; mevcut on bir tradeoff family otomatik olarak yeni
üst başlık sayılmamalıdır.

### Section VI — Evidence reach and reuse

| Alt bölüm | Tek soru | Girdi | Somut çıktı | Devir/taşıyıcı |
|---|---|---|---|---|
| **VI-A — Validation reach** | İlişkiler analytical/simulation/lab/prototype/field düzeyinde ne kadar sınandı? | Section V relations + validation records. | Relation-aware evidence reach; Fig. 7 panel A. | VI-B. |
| **VI-B — Paired-function validation** | C ve S aynı configuration, timing ve disturbance altında birlikte doğrulandı mı? | Paired-function evidence. | Joint functional coverage ve evidence gaps; Fig. 7 panel B. | VI-C. |
| **VI-C — Reconstructability** | Başka bir grup operating point ve comparison'ı yeniden kurabilir mi? | M/E trace + artifacts. | Reconstruction contract ve access/support status; Table VI. | VI-D. |
| **VI-D — Benchmark readiness** | Hangi relation bugün benchmark olabilir; hangisi hangi nedenle olamaz? | VI-A–C. | Benchmark permission/boundary. | Section VII ve VIII. |

**Section VI kabul ölçütü:** “Field study”, “paired functional evidence” ve
“simultaneous joint operation” eş anlamlı kullanılmamalıdır.

### Section VII — Requirement and network translation

| Alt bölüm | Tek soru | Girdi | Somut çıktı | Devir/taşıyıcı |
|---|---|---|---|---|
| **VII-A — Technologies that create observables and control variables** | Hangi technology P/G/X zincirinde hangi teknik işi yapıyor? | Section IV–V mechanisms. | Technology-to-mechanism role map. | VII-B. |
| **VII-B — Application requirement contracts** | Her application hangi C/S/M outcomes ve stress tests'i gerektiriyor? | Relation findings + application records. | Requirement contracts; Table VII. | VII-C. |
| **VII-C — 6G/network claim permissions** | Hangi evidence seviyesi application relevance'i network claim'e yükseltir? | Requirements + E boundary. | Mechanism-to-requirement-to-network evidence map; Fig. 8. | Section VIII. |

**Section VII kabul ölçütü:** Teknoloji veya application etiketi tek başına
6G readiness sayılmamalı; her direct/inferential claim bir requirement ve E
gate'i üzerinden kurulmalıdır.

### Section VIII ve IX

| Alt bölüm | Tek soru | Girdi | Somut çıktı | Devir/taşıyıcı |
|---|---|---|---|---|
| **VIII-A — Cross-corpus design lessons** | P/G/X mekanizmaları, C/S ilişkileri ve E sınırları birlikte ne söylüyor? | Sections IV–VII. | Az sayıda, güçlü ve koşullu design principles. | VIII-B. |
| **VIII-B — J gap-to-experiment roadmap** | Hangi kırık bağlantı hangi kontrollü deneyle kapatılmalı? | Observed J gaps. | Gap → insufficiency → hypothesis → baseline/control → disturbance sweep → success measure → artifact/dependency; Table VIII. | VIII-C. |
| **VIII-C — Review limitations** | Review hangi iddiaları bilinçli olarak kurmuyor? | Corpus/search/coding/non-pooling boundaries. | Scope, missingness, post-hoc refinement ve non-generalization limits. | Section IX. |
| **IX — Bounded conclusion** | Araştırmacı yöntem, kıyas ve sonraki deney açısından ne yapmalı? | Tüm zincir. | Üç kısa takeaway: design logic, comparison boundary, experiment/reporting contract. | — |

## 6. Kanıt ve denominator omurgası

Bu sayılar tek bir huni gibi gösterilmemelidir; farklı analiz katmanlarıdır.

| Katman | Geçerli evren | Makaledeki işi | Kritik sınır |
|---|---:|---|---|
| Search/selection | 1,733 records → 227 eligible reports → 206 studies | Scope ve corpus lineage. | Report ile study aynı sayı birimi değildir. |
| Governed evidence ledger | 8,306 rows | Bütün coded evidence governance. | 8,203 primary + 31 context + 72 conflict. |
| Primary synthesis ledger | 8,203 rows | Teknik sentezin ana evidence universe'ü. | 3,020 qualitative evidence + 4,779 metric + 404 governed tradeoff ledger. |
| Metric layer | 4,779 records | C/S/joint/implementation quantities ve M/E alanları. | 118 + 4,661 survey-use ayrımıdır; effect count değildir. |
| Scientific relationship layer | 402 substantive relations / 168 studies | X–C–S mechanism sentezinin doğal evreni. | 404 governed satırdan iki absence sentinel ayrılır. Metric katmanının altkümesi gibi çizilmez. |
| Relationship evidence type | 218 quantitative + 184 qualitative | Relation representation. | Sayıların toplamı 402'dir. |
| Relationship conditionality | 371 condition-dependent + 31 descriptive | İddia sınırı. | Sayıların toplamı 402'dir. |
| Evidence bodies | 115 bodies / seven domains | Corpus-level narrative conclusions. | Membership bir effect veya independent study değildir. |
| Phase-G verified metric set | 118 records / 15 studies / 16 reports | Source-verified metric evidence; operating-point completeness varies by record. | 76 group: 23 within-study multirow, 53 singleton, 0 independent multi-study group. |
| Main-text candidate anchors | 18 rows / eight evidence cards | Okunabilir teknik/sayısal örnekler. | Cross-study pooled comparison değildir; tamamı native units/conditions ile kalır. |

### 118 kayıt için zorunlu ifade düzeltmesi

118 kayıt, gerçekleştirilmiş 118 cross-study numerical comparison değildir.
Doğrulanmış grup kataloğunda:

- 76 canonical group vardır;
- 23'ü within-study multirow group'tur;
- 53'ü condition-bound singleton'dır;
- birden fazla bağımsız çalışma içeren grup sayısı **0**'dır.

Dolayısıyla Section V'in güçlü ve dürüst sonucu iki katmanlı olmalıdır:

1. Kaynak-içi, condition-complete teknik ilişkiler sayısal olarak gösterilir.
2. Gerçek cross-study numerical pooling'in neden kurulamadığı açık bir corpus
   bulgusu ve benchmark motivasyonu olarak raporlanır.

Yeni eşleştirme sonunda gerçekten iki veya daha fazla study içeren bir grup
oluşursa ancak o zaman bounded cross-study numerical comparison taşıyıcısına
eklenir. Mimari böyle bir grubun çıkmasına bağımlı değildir.

## 7. Figure ve table ilişkilendirme sözleşmesi

### Figures

| Taşıyıcı | Yeni tek görevi | Sahip olduğu J öğeleri | Karar |
|---|---|---|---|
| **Fig. 1 — Joint-evidence anatomy** | Generic O-ISAC signal chain üzerinde system boundary, target-reaching path, coupling, X ve C/S outcomes'un nerede doğduğunu göstermek. | P, G, X, C, S | **Tamamen yeniden tasarla.** Eski üç evidence-object kartının yararlı kısmı E açıklamasına taşınır. |
| **Fig. 2 — Inference-permission pipeline** | J kaydını physical-regime, jointness, measurement-alignment ve evidence-scope gate'lerinden geçirip permitted use üretmek. | P, G, X, C, S, M, E | **Tamamen yeniden tasarla.** Sayı taşımaz. |
| **Fig. 3 — PRISMA report–study flow** | Search record, report ve unique study ayrımını göstermek. | E/provenance | **Koru; yalnız açıklık/caption iyileştirmesi.** |
| **Fig. 4 — Interpretability and transfer bottlenecks** | TQAF'ı interpretation-support ile transfer/reuse boyutlarına ayırmak. | M, E | **Hiyerarşi ve caption'ı yeniden kur.** Validation-method sayıları burada bulunmaz. |
| **Fig. 5 — Coupling-to-variable map** | G location/object ile joint relation üreten X faktörlerini bağlamak; structural integration ile evidential jointness'ı ayırmak. | P, G, X | **Yeniden tasarla.** Study-level cross-tab yalnız governed join varsa kullanılır. |
| **Fig. 6 — Joint-performance relation map** | Canonical X ailelerinden C ve S outcomes'a giden yönlü, condition-tagged ve evidence-bounded ilişkileri göstermek. | Bütün J | **Makalenin merkez şekli; major rebuild.** Frekans grafiği olmaktan çıkar. |
| **Fig. 7 — Evidence reach and paired validation** | Validation reach ile iki fonksiyonun aynı configuration/condition altında doğrulanmasını ayrı göstermek. | C, S, M, E | **Yeniden tasarla/genişlet.** Basit validation-method envanteri ikincil kalır. |
| **Fig. 8 — Mechanism-to-requirement translation** | Kanıtlanmış relation'ın application requirement ve permitted 6G/network claim'e nasıl dönüştüğünü göstermek. | Bütün J | **Tamamen yeniden tasarla.** Marjinal counts arasında kanıtlanmamış causal arrow kurulmaz. |

### Tables

| Taşıyıcı | Yeni tek görevi | Sahip olduğu J öğeleri | Karar |
|---|---|---|---|
| **Table I — Prior-review coverage and unresolved link** | Önceki synthesis ailelerinin J zincirinde neyi kapsadığını ve hangi bağlantıyı kurmadığını görünür yapmak; bu survey'in tamamladığı işi son satırda göstermek. | Bütün J | **Yeniden kur.** 76 COMST makalesi biçimsel referans corpus'udur; O-ISAC domain evidence gibi tabloya girmez. |
| **Table II — Claim-permission matrix** | Minimum alignment → permitted claim → prohibited overclaim → downstream use eşlemesini vermek. | Bütün J | **Tamamen yeniden kur.** Fig. 2 akışı, Table II exact rule'u taşır. |
| **Table III — Evidence-layer and denominator ledger** | Report, study, evidence item, metric, relation ve evidence body birimlerini ve kullanıldığı section'ı göstermek. | Bütün J'nin provenance katmanı | **Mevcut accounting'i koru, yapıyı genişlet.** |
| **Table IV — Platform boundary/condition matrix** | Altı platform için optics role, target path, conversion boundary, observable ve decisive condition'ı vermek. | P, S, M, E | **Yeniden kur.** Fig. 5 G/X'i sahiplenir. |
| **Table V — Quantitative evidence and comparison outcome** | Az sayıda condition-complete evidence card ile exact values/units/baselines'ı; ayrıca within-study, singleton ve multi-study comparison sonucunu vermek. | Bütün J; ağırlık C, S, M, E | **Data-gated major rebuild.** Mevcut sekiz kart/18 anchor uygun başlangıçtır; tam 118 atlas supplementte kalır. İkonlar yalnız compact legend olarak kullanılır, anlamı metinde bir kez açıklanır. |
| **Table VI — Reconstructability/benchmark matrix** | Same-run C/S trace, parameter completeness, baseline, artifact access ve benchmark permission'ı birlikte göstermek. | C, S, M, E | **Yeniden kur.** Raw access counts tek başına sonuç değildir. |
| **Table VII — Application requirement contract** | Her application archetype için required C, S, M/stress/ground truth, minimum E ve prohibited inference'ı vermek. | P, C, S, M, E | **Yeniden kur.** Tam 13-domain inventory gerekirse supplementte kalabilir; ana metin requirement archetype'larını taşır. |
| **Table VIII — J gap-to-experiment roadmap** | Eksik J öğesini corpus bulgusuna, kontrollü deneye, başarı ölçütüne ve reusable artifact'a bağlamak. | Bütün J | **Finding→action→milestone iskeletini koru; J breaks etrafında güçlendir.** |

### Değişmez nonduplication kuralı

- **Figure:** mekanizma, yön, ilişki veya akış.
- **Table:** exact value, tanım, kural veya denetlenebilir eşleme.
- **Prose:** neden, sonuç, mühendislik anlamı, countercondition ve sınır.
- **Supplement:** tam kayıt evreni, source locator, karar izi ve ayrıntılı
  denominator.

Aynı kategori envanteri şekil, tablo ve paragrafta üç defa anlatılmayacaktır.

## 8. J bileşenlerinin veri fizibilitesi

| Bileşen | Mevcut destek | Eksik/riski | Gerekli işlem |
|---|---|---|---|
| **P** | Canonical modality, optical front end, functions, tasks, channel/scenario alanları güçlü. | Target-reaching path ve conversion boundary için ayrı governed alan yok. | Mevcut full textlerden controlled path/conversion crosswalk. |
| **G** | Locked integration mechanism codes güçlü. | Multilabel yapı yanlışlıkla tek maturity score'a indirgenebilir. | Mevcut normalization'ı aynen koru; toplam alma. |
| **X** | Relation axis, objective ve constraints içerik bakımından güçlü. | Free text; mevcut 11 family neden ve outcome sınıflarını karıştırıyor. | Verbatim X + controlled X family; unresolved bucket ve source QA. |
| **C** | Communication metric layer güçlü. | Gross/net rate, OSNR/SNR, pre/post-FEC gibi semantic farklar. | Reported definition'ı koru; semantic family yalnız navigation için. |
| **S** | Sensing metric/task layer güçlü. | Resolution, error, precision ve bound aynı quantity değildir. | Task + metric semantics birlikte kodlanır. |
| **M** | Metric düzeyinde condition set, plane, unit, baseline ve scenario desteği güçlü. | Relationship düzeyinde doğrudan ve çift taraflı M linkage kısmi. | M_C ve M_S ayrı; A_M explicit. Missing değer NR/UNC kalır. |
| **E** | Metric düzeyinde validation, origin, locator ve verification güçlü. | Study-level validation relation'a otomatik taşınırsa overclaim oluşur. | E_C/E_S ve relation-specific boundary; gerektiğinde bounded source reopen. |

**Fizibilite hükmü:** Yeni bibliographic search gerekmez. J, mevcut review
sorularındaki platform, integration, metrics, tradeoffs, conditions ve
validation alanlarının bütünleştirici gösterimidir. Ancak J'yi 402 ilişki için
denetlenebilir record-level projection olarak yayınlamak istiyorsak bounded
normalization, join, iki-reviewer QA ve versioned supplement gerekir.

## 9. Version-change kapsamı

Bu değişiklik küçük prose revizyonu değildir. Aşağıdakiler değişeceği için
**major manuscript version** gerektirir:

- merkezî analysis object;
- Section II ve Section V'in mantığı;
- contribution listesi ve prior-review positioning;
- Fig. 1, 2, 5, 6, 7 ve 8'in bilimsel görevi;
- Table I, II, IV, V, VI ve VII'nin reader job'ı;
- bütün section handoff cümleleri;
- terminology ve denominator ownership.

### Korunacak bilimsel varlıklar

- Frozen search scope ve PRISMA report–study lineage.
- 206-study canonical corpus.
- Locked platform assignments ve integration normalization.
- Governed evidence, metric, tradeoff ve evidence-body katmanları.
- Source-verified 118-record Phase-G lock ve human decisions.
- Non-pooling ilkesi ve native units/conditions.
- Source locators, hashes, conflict/context separation ve audit trail.

### Yeniden üretilecek varlıklar

- J data dictionary/crosswalk.
- P path/conversion crosswalk.
- Controlled X-family map.
- Relationship-level M/E alignment projection.
- Yeni Fig. 1, 2, 5, 6, 7, 8 source data ve vector assets.
- Değişen Table I, II, IV, V, VI, VII.
- Section I–IX cross-references ve captions.
- Supplement manifest, packing list ve final render QA.

## 10. Uygulama öncesi karar kapıları

1. **Scientific lock — IN PROGRESS (V3-S1):** Merkezî soru ve J tanımı aynı
   hash'li payload üzerinden yazar incelemesindedir; henüz PASS değildir.
   [Kilit kaydı](../00_governance/V3_SCIENTIFIC_CORE_LOCK.md)
2. **Architecture lock:** Section/subsection çıktıları ve handoff'lar
   onaylanır.
3. **Carrier lock:** Her figure/table için tek reader job ve nonduplication
   sınırı onaylanır.
4. **Data feasibility lock:** P, X, M ve E backfill kapsamı küçük bir pilotla
   doğrulanır; yeni search yapılmaz.
5. **X-family lock:** 402 relation üzerinde controlled factor taxonomy
   dondurulur; neden ve outcome çiftleri ayrılır.
6. **Comparison lock:** 76 verified group için within-study/singleton/zero
   multi-study sonucu korunur; yeni promotion yalnız source-open adjudication
   ile yapılır.
7. **Manuscript implementation:** Yeni version tree açılır ve Sections II/V
   önce yazılır; diğer sections onlara bağlanır.
8. **Scientific QA:** Denominator, source claim, non-pooling, terminology ve
   cross-reference regression testleri.
9. **Visual/layout QA:** Vector/editable figures, grayscale/accessibility,
   page budget ve tam PDF render denetimi.
10. **Human release gate:** İki bağımsız teknik okuyucu ve tüm yazarların
    scientific sign-off'u.

## 11. Bu haritada yazarların önce kontrol etmesi gereken altı karar

1. Makalenin merkezî nesnesi **J relationship** olacak mı?
2. Section V açıkça makalenin bilimsel merkezi olacak mı?
3. Mevcut on bir tradeoff family yerine X-merkezli yeni family'ler
   normalizasyon sonrası kurulacak mı?
4. Gerçek cross-study numerical group sayısının sıfır olması saklanmadan ana
   bulgu ve benchmark motivasyonu olarak kullanılacak mı?
5. Main text az sayıda condition-complete evidence card taşıyıp tam atlası
   supplementte bırakacak mı?
6. Fig. 1, 2, 5, 6, 7 ve 8 ile Table I, II, IV, V, VI ve VII'nin major rebuild
   kapsamına girmesi kabul ediliyor mu?

Bu altı karar kilitlendiğinde yeni sürüm yalnız daha uzun bir review olmayacak;
taxonomy'den mekanizmaya, mekanizmadan joint-performance evidence'a,
evidence'dan araştırma kararına uzanan tek bir bilimsel argüman olacaktır.
