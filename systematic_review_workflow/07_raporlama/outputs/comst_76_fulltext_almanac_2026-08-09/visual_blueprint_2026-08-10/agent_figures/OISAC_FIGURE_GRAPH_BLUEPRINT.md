# O-ISAC Survey Figure and Graph Blueprint

**Durum:** Tasarım şartnamesi; hiçbir şekil, grafik, fotoğraf, bitmap, SVG veya PDF üretilmedi. Koordine edilen tablo çalışmasında Table I dokuz bölümlü v2 adayının Introduction/Section I dosyasına eklendi ve yerleşim incelemesi bekliyor.

**Dokuz bölümlü aday notu (13 Ağustos 2026):** Aşağıdaki kalıcı blueprint kimlikleri, panel içerikleri, veri otoriteleri ve erişilebilirlik kuralları korunur. Eski 13 bölümlü dosya adları, Section numaraları ve insertion-line tahminleri artık tarihsel kayıttır; görünür Fig. 1--8 sırası ve güncel yerleşimler `comst_206_v2_9section/02_VISUAL_AND_TABLE_PLACEMENT_CONTRACT.md` ile her v2 Section dosyasındaki activation-ready üretim yorumlarından yönetilir.

**Kapsam:** 14 aktif TeX dosyası, güncellenmiş 16 taşıyıcılı ana plan, 76 yayımlanmış IEEE *Communications Surveys & Tutorials* (COMST) makalesindeki 1,096 şekil ve 654 tabloya ait yakın-okuma kodları, rol istatistikleri ve O-ISAC sentezinin yetkili sayım dosyaları birlikte değerlendirildi. Bu belge yalnızca **şekil/grafik** katmanını tanımlar; sekiz tablo ayrı tablo şartnamesiyle koordine edilmelidir.

## 1. Son karar: sekiz şekil

Ön plandaki yedi şeklin işlevleri korunur. Section II'nin yeniden yazılan anlatısı, Table I'in kaynak ve reader-task haritası ile Section III'ün ayrıntılı comparison framework'ü arasında ayrı bir öğretici görev ortaya çıkarmıştır: model içinde tanımlanan sonuçların, optik ortama özgü gözlemlerin ve mimari ya da dağıtım nesnelerinin neden tek bir sayısal ölçeğe indirgenemeyeceğini göstermek. Bu nedenle mevcut kimlikleri yeniden adlandırmadan **FIG-OISAC-RS1 — Native Evidence Objects and the Cross-Study Handoff** eklenmiştir. Bu şekil yeni bir taxonomy, survey sıralaması veya Section III çerçevesinin özeti değildir.

`FIG-OISAC-RS1` kalıcı blueprint kimliğidir. Yayın içi Fig. numarası float sırasından LaTeX tarafından üretilecektir; planlanan sırada yeni şekil Fig. 1 olur ve mevcut `FIG-OISAC-01`--`FIG-OISAC-07` kimlikleri değişmeden Fig. 2--8 olarak görünür.

Nihai öneri:

| Sıra | Blueprint ID | İşlev | Sonuç |
|---:|---|---|---|
| 1 | FIG-OISAC-RS1 | Üç paralel native evidence object ve ortak ölçeğe indirgenememe ilkesi | **Yeni eklendi** |
| 2 | FIG-OISAC-01 | Dört eksenli karşılaştırma çerçevesi | Korundu; planlanan görünür etiket Fig. 2 |
| 3 | FIG-OISAC-02 | PRISMA akışı ve report-to-study eşlemesi | Korundu; planlanan görünür etiket Fig. 3 |
| 4 | FIG-OISAC-03 | Dokuz satırlı TQAF kanıt profili | Korundu; planlanan görünür etiket Fig. 4 |
| 5 | FIG-OISAC-04 | Çok etiketli entegrasyon/coupling haritası | Korundu; planlanan görünür etiket Fig. 5 |
| 6 | FIG-OISAC-05 | Trade-off aileleri kanıt haritası | Korundu; planlanan görünür etiket Fig. 6 |
| 7 | FIG-OISAC-06 | Validasyon ayarı ve yöntemleri | Korundu; planlanan görünür etiket Fig. 7 |
| 8 | FIG-OISAC-07 | Teknoloji–observable–uygulama–6G zinciri | Korundu; planlanan görünür etiket Fig. 8 |

Sekiz şekil ve ayrı plandaki sekiz tablo toplam **16 ana görsel** oluşturur. COMST corpusunda makale başına medyan 13 şekil ve 8 tablodur; fakat 16 sayısı bir kota değildir. Burada sayı değil, her görselin ayrı bir okuyucu sorusunu çözmesi esas alındı. COMST corpusunda sistem mimarisi şekilleri 67/76 (%88.2), taxonomy map 55/76 (%72.4), survey roadmap 45/76 (%59.2), protocol/workflow 32/76 (%42.1), application map 32/76 (%42.1), trade-off plot 16/76 (%21.1) ve bibliometric/evidence distribution grafikleri 4/76 (%5.3) makalede görüldü. Bu oranlar hedef veya kabul eşiği değildir; yalnızca seçilen görsel işlevlerin yayımlanmış survey pratiğinde karşılığı olduğunu gösterir.

Ek şekil önerilmemesinin nedenleri:

- Giriş için ayrı “paper organization” şeması Introduction son paragrafını ve Section II/III'teki iki farklı kavramsal görevi tekrarlar.
- Modality prevalans çubuğu, altı aileyi veren planlı modality tablosunu tekrarlar ve aileleri yanlışlıkla performans sırası gibi gösterebilir.
- Metric-family sıklık grafiği, extraction granularity ile bilimsel önem arasında sahte bir eşitlik kurar; metric-contract tablosu daha doğru taşıyıcıdır.
- Uygulama sıklık grafiği, planlı application–requirement tablosunu tekrarlar; FIG-OISAC-07 yalnızca katmanlar arası ilişkiyi taşır.
- Roadmap için ok/merdiven biçimli dekoratif bir şekil yerine izlenebilir başarı ölçütleri içeren tablo daha işlevseldir.
- Evrensel Pareto eğrisi, platformlar arası scatter, normalize edilmiş radar chart veya “best modality” grafiği kanıt tarafından desteklenmez.
- Fotoğraf kolajı önerilmez: review'e ait tek bir cihaz kurulumu yoktur; kaynak makalelerden fotoğraf çoğaltmak telif, ölçek ve temsil sorunları doğurur.

## 2. Ortak üretim sözleşmesi

### 2.1 Her şeklin tek görevi

Her şekil yayıma girmeden önce aşağıdaki üç cümle eksiksiz yazılabilmelidir:

1. **Reader question:** Okuyucu bu şekle hangi tek sorunun yanıtını almak için bakıyor?
2. **Core message:** Şekil kapatıldıktan sonra hatırlanması gereken tek cümle nedir?
3. **Inference boundary:** Şekil hangi yorumu özellikle desteklemiyor?

Bu üçü birbirinden ayrılmıyorsa şekil ya bölünmeli ya da tabloya dönüştürülmelidir.

### 2.2 Metin–şekil ilişkisi

COMST yakın okumasında şekillerin %39.5'i metinde görselden önce anılmış, %30.9'u görselin bulunduğu noktada, %22.5'i sonradan anılmıştır. Metnin şekli açıkça hazırladığı durumlar yalnızca %37.7; şekli sonradan yorumladığı durumlar %41.9'dur. Bunlar kalite hedefi değildir. O-ISAC için daha sıkı bir kural kullanılmalıdır:

- Görselden **önce**, şeklin okuyucu sorusunu ve neden gerekli olduğunu bildiren 1–2 cümle.
- Görselden **sonra**, sayıları tekrar etmeyen; örüntüyü, mekanizmayı ve sınırı açıklayan 2–4 cümle.
- “As shown in Fig. X” tek başına lead-in sayılmaz.
- Caption, metindeki yorum paragrafının yerine geçmez.

### 2.3 Boyut ve teknik teslim

- Basit, az etiketli tek-panel grafik ancak okunaklı kalıyorsa `\columnwidth` (yaklaşık 3.45 in) olabilir.
- Bu plandaki sekiz şeklin tamamı yoğun bağlam taşıdığı için varsayılan tercih `figure*`, yaklaşık 7.0–7.16 in genişliktir.
- Final boyutta en küçük yazı 8 pt, tercih edilen gövde 8.5–9 pt; panel harfleri 9–10 pt bold.
- Çizgi kalınlığı final boyutta en az 0.8 pt; kritik sınırlar 1.0–1.2 pt.
- Grafikler ve şemalar vektör olarak `.pdf` ve `.svg`; veri kaynağı `.csv`; üretim kodu `.py` veya `.tex`; kısa bir provenance/README ile saklanmalıdır.
- PNG yalnızca QA önizlemesi içindir; dergiye ana kaynak olarak raster grafik verilmemelidir.
- Python grafikleri sabit kategori sırası, sabit renk sözlüğü ve deterministik çıktı kullanmalıdır; rastgele jitter kullanılmamalıdır.

### 2.4 Renk, grayscale ve erişilebilirlik

- Renk, tek başına kategori taşımaz; doğrudan etiket, panel başlığı, çizgi biçimi veya desenle yedeklenir.
- Kırmızı–yeşil karşıtlığı kullanılmaz. Veri grafiklerinde önerilen çekirdek palet: güçlü/ana akış için mavi `#0072B2`; yeterli/ikincil için orta gri `#A7A9AC`; düşük/sınır için vermilion `#D55E00`; bağlamsal dal için sarı-turuncu `#E69F00`; nötr çizgiler `#4D4D4D`.
- Kavramsal şemalarda en fazla dört semantik renk; düğüm boyutu yalnızca hiyerarşi varsa değişir, prevalans temsil etmek için değiştirilmez.
- Tüm paneller grayscale önizlemede test edilir. Aynı ton değerine düşen kategoriler desen veya doğrudan etiketle ayrılır.
- Caption veya alt metin, şeklin ana mesajını ve kritik sayıları metinsel olarak taşımalıdır.

### 2.5 Belirsizlik ve denominator politikası

- Corpus dağılımları, elde tutulan 206 çalışmanın betimsel tam sayımıdır; rastgele örneklem değildir. Bu nedenle standart hata veya confidence interval eklenmez.
- Yüzde her zaman görünür denominator ile birlikte verilir: `n/206`, `claims/402` veya aile içi `conditional/claims`.
- Multi-label sayımlar toplanmaz. Bu, hem şekil üzerinde hem caption'da yazılır.
- Claim count, experiment count, effect size veya evidence strength değildir.
- Kavramsal şemalara ampirik görünüm kazandırmak için uydurma ok kalınlığı, düğüm alanı veya flow width eklenmez.

### 2.6 Yasak biçimler

- 3B bar/pie, donut, radar/spider chart, word cloud, decorative gauge, pictogram-count chart.
- İki farklı denominator'ü aynı eksende açıklamasız birleştiren dual-axis grafik.
- Intersections hesaplanmadan Venn veya UpSet.
- Flow miktarları bilinmeden Sankey.
- Modality, validation veya technology kategorilerini “maturity ladder” gibi gösteren piramit.
- Heterojen kaynak değerlerinden ortak Pareto/frontier.
- Bir çalışmanın kaynağından alınmış eğriyi yeniden dijitize etmek; proje yeni performans değeri üretmedi.

## 3. FIG-OISAC-RS1 — Native Evidence Objects and the Cross-Study Handoff

### Kimlik, planlanan etiket ve kesin yer

- **Kalıcı blueprint kimliği:** `FIG-OISAC-RS1`. Mevcut `FIG-OISAC-01`--`FIG-OISAC-07` kimlikleri yeniden adlandırılmaz.
- **Planlanan yayın sırası:** Section II'deki ilk şekil; mevcut float sırasına göre görünür etiket Fig. 1 olacaktır. Numara TeX tarafından üretilmeli, çizime veya prose'a hard-code edilmemelidir.
- **Dosya:** `02_RELATED_SURVEYS_AND_SCOPE.tex`.
- **Section:** `RELATED SURVEYS AND SCOPE`.
- **Kesin yer:** Table I'i izleyen tematik sentezin sonunda; physical-medium/network ile mechanism/application syntheses'ı kapatan son paragraftan sonra ve evidence objects'ın neden tek bir context-free scale'e indirgenemediğini yorumlayarak Section III'e geçen paragraftan önce. Planlanan Section II mimarisinde P4 ile P5 arasındadır.
- **Satır politikası:** Aktif TeX bu görevde değiştirilmediği için geçici satır numarası verilmez. Section II dondurulduğunda semantic sentence anchor ve gerçek satır numarası birlikte kaydedilir.

### Reader question

**Why can results represented by different native evidence objects not be flattened onto one common numerical scale?**

### Tek cümlelik ana mesaj

**Model-defined results, medium-native observations, and architecture/deployment objects are each meaningful in their native frame; relating them across studies requires context-preserving reconciliation, which Section III takes up.**

### Görsel arketipi

Üç eşit, paralel ve sıralanmamış **native-evidence-object vignette** ile bunların altında tek bir nötr bracket/message. Bu şekil prior-survey family map'i, taxonomy, süreç, funnel, gateway, scorecard veya Section III comparison framework'ü değildir.

### Üç paralel vignette

**Panel (A) — Model-defined result**

Merkez nesne: `Model-defined result`. Çevresinde, ok kullanılmadan üç zorunlu native-context etiketi:

- assumptions;
- objective;
- constraints.

Bu panel analytical bound, optimum veya model sonucu gibi bir nesnenin ancak tanımlandığı model çerçevesinde anlamlı olduğunu anlatır. Denklem, sayısal sonuç veya “best” etiketi verilmez.

**Panel (B) — Medium-native observation**

Merkez nesne: `Medium-native observation`. Çevresinde:

- optical path;
- measurement plane;
- operating conditions.

Basit bir source/path/receiver çizgisel motifi kullanılabilir; ancak yön oku süreç veya performans akışı gibi görünmemelidir. Panel, aynı metric label'ının farklı optical path ve measurement plane'lerde aynı observation olmadığını görünür kılar.

**Panel (C) — Architecture/deployment object**

Merkez nesne: `Architecture / deployment object`. Çevresinde:

- shared components;
- scenario;
- validation setting.

Basit component grouping veya deployment-frame motifi kullanılabilir. Katman sayısı maturity, component count ise complexity/coverage skoru değildir.

### Bottom bracket ve Section III handoff

Üç panelin tamamını kapsayan, yön taşımayan tek bracket altında şu ana mesaj bulunur:

`Meaning is native to the evidence frame; do not flatten into a common numerical scale.`

Brackete bağlı olmayan, alt satırdaki nötr footer:

`Context-preserving study-level reconciliation is taken up in Section III.`

Handoff bir ok, terminal node veya comparison outcome değildir. Section III'ün four-axis record'u, exact field dictionary'si ve admissibility outcomes'ı burada yazılmaz veya çizilmez.

### Connector ve hiyerarşi yasağı

- Paneller arasında ok, flow line, convergence, sequence number veya parent-child connector bulunmaz.
- Panel içindeki context etiketleri merkezi nesnenin çevresine yerleştirilir; ilişki gerekirse ince, yönsüz çizgi veya ortak container ile gösterilir.
- Bottom bracket yalnız ortak non-flattening ilkesini gösterir; evidence aggregation veya pooling anlamı taşımaz.
- A--C harfleri yalnız erişilebilir referanstır; temporal sıra, öncelik, kalite veya kapsam kodlamaz.
- Üç panel eşit width, height, border weight ve whitespace kullanır.

### Encoding, renk ve annotation

- Nicel eksen, percentage, source count, family count veya denominator yoktur.
- Tek bir nötr panel sistemi kullanılır; istenirse model blue-gray, medium teal ve architecture muted orange accent ile ayrılır. Renk panel harfi, başlık, border motif ve direct label ile yedeklenir.
- Panel alanı ve central-object boyutu eşittir.
- Üst annotation: `Parallel native evidence objects—not stages or quality levels.`
- Legend kullanılmaz; direct labels tercih edilir.
- İstatistiksel belirsizlik yoktur; bu source-grounded fakat review-controlled bir kavramsal açıklamadır.

### Lead-in blueprint (English)

> Figure~\ref{fig:native_evidence_objects} makes the resulting mismatch concrete through three evidence objects that are each interpretable in their native frame but do not share a context-free numerical scale.

### Şekil sonrası prose görevi

Sonraki prose panel etiketlerini yeniden saymamalıdır. Önce hiçbir evidence form'un diğerinden intrinsically stronger olmadığını belirtmeli; sonra ortak bir sayısal ölçeğe flatten etmenin native meaning'i sildiğini açıklamalı; son olarak Section III'e context-preserving study-level reconciliation ihtiyacını devretmelidir. Section III'ün dört ekseni, field listesi veya outcomes burada preview edilmez.

Önerilen after-prose:

> None of these evidence forms is intrinsically stronger than another; each supports a different kind of reasoning within its native frame. Relating them therefore requires the context-preserving study-level reconciliation developed in Section III, rather than a common numerical scale imposed in advance.

### Caption blueprint (English)

> **Native evidence objects represented across prior O-ISAC syntheses.** A model-defined result retains its assumptions, objective, and constraints; a medium-native observation retains its optical path, measurement plane, and operating conditions; and an architecture or deployment object retains its shared components, scenario, and validation setting. The equal panels are parallel examples rather than stages or quality levels. Because these objects cannot be flattened onto a common numerical scale without losing native meaning, Section III takes up context-preserving study-level reconciliation.

### Alt text ve erişilebilirlik

Önerilen alt text:

> Three equal side-by-side vignettes show a model-defined result with assumptions, objective, and constraints; a medium-native observation with optical path, measurement plane, and operating conditions; and an architecture or deployment object with shared components, scenario, and validation setting. A bracket states that each is meaningful in its native frame and cannot be flattened onto a common numerical scale. The need for context-preserving study-level reconciliation is handed to Section III. The panels are parallel and unranked.

Ek kapılar:

- Final boyutta minimum 8 pt, hedef 8.5--9 pt.
- Reading order A, B, C, bracket, footer olarak alt text/tagging'e yansıtılır; bu erişilebilir sıra kavramsal sequence sayılmaz.
- Grayscale çıktıda panel harfleri, titles ve border motifs ile ayrım korunur.
- Bottom message tek satırda okunamıyorsa kontrollü iki satıra kırılır; `\scriptsize` veya rasterized text kullanılmaz.

### Boyut ve uygulama rotası

- `figure*`, 7.0--7.16 in genişlik, yaklaşık 3.2--3.9 in yükseklik; aspect 1.85--2.2.
- Tercih: sabit koordinatlı editable SVG/TikZ; alternatif Python `matplotlib.patches`.
- Gelecek teslim: source + SVG + PDF + alt-text Markdown + kısa evidence crosswalk.
- Force-directed layout, raster/AI illustration, stock icons veya source-paper artwork kullanılmaz.

### Veri, kaynak ve evidence gate

- Üç object/context bundle, Section II'deki assigned syntheses veya source-audited family-level evidence-unit descriptions tarafından desteklenmelidir; yalnız başlıktan tahmin yapılmaz.
- **Table I tek başına** altı reader-task family'yi ve 24 full-length/independently citable synthesis assignment'ını taşır.
- **ST-RS1 tek başına** 38 source-level row'u ve multi-label scope'u taşır.
- Figure içinde family adı, source adı, citation listesi, 24/38 count veya chronology statüsü bulunmaz.
- Mohsan chronology qualification ve manuscript-stage source-status ayrımları prose/Table I/ST-RS1'de kalır.
- Bottom message Section II inference'ıyla eşleşmeli; Section III yalnız contradiction/duplication boundary açısından kontrol edilmelidir.
- Negatif duplication gate: arrow/sequence yok; six-family mapping yok; comparison outcomes yok; four-axis cards veya exact record fields yok; first/only/universal claim yok.

### Failure modes / do not do

- Altı reader-task family'yi figure içinde yeniden çizmek veya Table I source assignments'ını vignettes'a dağıtmak.
- Panelleri aşama, chronology, funnel, hierarchy, maturity ladder veya quality rank gibi bağlamak.
- Ok, convergence bus, gateway, terminal outcome, checkmark, traffic light, unequal panel area veya weighted connector kullanmak.
- Ortak metric/unit etiketini common scale kanıtı gibi göstermek.
- Present review'ü dördüncü veya üstün evidence object olarak eklemek.
- Section III comparison record'unu, four axes'i, field dictionary'yi veya admissibility states'i minyatürleştirmek.
- “Model evidence is stronger”, “deployment evidence is mature” veya benzeri rank çıkarımı kurmak.
- Reconciliation işlemini first, only veya universally valid olarak tanımlamak.

### Table I ve Section III ile explicit nonduplication contract

- **Table I:** six reader-task families, 24 source assignments, optical reach, typical evidence unit, comparison logic, primary question ve neutral boundary. FIG-OISAC-RS1 bu family'leri, source listelerini veya table columns'ı yeniden taşımaz.
- **FIG-OISAC-RS1:** yalnız üç native evidence-object form'un context-dependence'ını ve non-flattening ilkesini öğretir. Source coverage veya operational comparison rule vermez.
- **FIG-OISAC-01 / T-02 (Section III):** comparison reasoning path, record fields, missing-data rules ve admissible uses. FIG-OISAC-RS1 bunları önceden çizmez; yalnız neden böyle bir çerçeveye ihtiyaç olduğunu kurar.
- Acceptance test: T1 çıkarıldığında source/family positioning kaybolmalı; RS1 çıkarıldığında native-object mismatch görünmez olmalı; Section III carriers çıkarıldığında comparison'ın nasıl yapılacağı bilinmemelidir. Hiçbir iki taşıyıcı aynı soruya tam yanıt vermemelidir.

### COMST analog gerekçesi

- **COMST_063, Fig. 4, “The three types of hybrid communication systems”:** Eşit, yan yana teknik vignettes'ın kendi bileşen ilişkilerini görünür kılması açısından işlevsel analogdur. PLC/WLC categories, channel çizgileri ve exclusive topology semantics aktarılmaz.
- **COMST_053, Fig. 8, “A novel promising 6G network architecture”:** Components ve interfaces'i bir native architecture frame içinde tutması açısından işlevsel analogdur. Kaynağın proposed architecture'ı, layer hierarchy'si, 6G iddiaları veya görsel düzeni aktarılmaz.

Bu örnekler tasarım şablonu değil, işlevsel retorik analogdur. Yeni şekil özgün düzen ve O-ISAC'a ait source-audited evidence-object sözleşmesiyle üretilecektir.

## 4. FIG-OISAC-01 — Four-Axis O-ISAC Comparison Framework

### Kimlik ve yerleşim

- **Dosya:** `03_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex`
- **Section:** `O-ISAC FOUNDATIONS AND THE CROSS-PLATFORM COMPARISON FRAMEWORK`
- **Kesin yer:** Section açılışındaki ikinci paragrafın, “...cross-platform comparison record used throughout the survey.” cümlesinin hemen ardından; `\subsection{Technical System Boundary}` öncesi. Mevcut dosyada yaklaşık satır 16–18 arası.
- **Yerleşim gerekçesi:** Bu şekil bir sonuç grafiği değil, sonraki tüm teknik bölümlerin okuma sözleşmesidir. Okuyucu modality, coupling, metric ve provenance ayrımını alt bölümlere girmeden önce görmelidir.

### Reader question

**Before two reported O-ISAC values can be related, which contextual axes must be fixed, and what comparison outcomes are admissible?**

### Tek cümlelik ana mesaj

**An O-ISAC value becomes comparable only after its physical context, coupling location, measurement plane, and provenance are retained; otherwise it remains a bounded within-study or descriptive observation.**

### Görsel arketipi

İki panelli, merkezi kayıt kartı bulunan **hub-and-gate framework diagram**. Taxonomy tree veya basamak/merdiven kullanılmamalıdır; dört eksen birbirinden bağımsız ama aynı kayıt üzerinde birleşir.

### Panel ve içerik modeli

**Panel (a) — Four axes feeding one comparison record**

Merkezde `Candidate comparison record` kartı bulunur. Dört eşit ağırlıklı blok merkeze bağlanır:

1. **Physical context**
   - modality;
   - optical/RF signal path and conversion boundary;
   - communication task;
   - sensing task, target/disturbance and geometry.
2. **Coupling location**
   - shared hardware;
   - optical carrier;
   - waveform;
   - resource allocation;
   - link/channel;
   - joint design/optimization;
   - shared application.
3. **Measurement contract**
   - metric definition;
   - measurement plane;
   - unit and aggregation;
   - operating point/channel;
   - constraints and baseline.
4. **Provenance**
   - reported/calculated/digitized origin;
   - analytical, simulation, laboratory, prototype or field setting;
   - source locator;
   - configuration continuity.

Merkez kartın alt satırında sabit uyarı: `Missing field = unknown; never inferred from a neighboring study.`

**Panel (b) — Admissibility gate**

Merkez karttan üç eşit boyutlu sonuç kutusuna geçilir:

- `Within-study interpretation` — provenance and conditions clear;
- `Conditional cross-study relation` — decisive fields align and remaining differences are stated;
- `Descriptive only` — semantic or experimental mismatch remains.

Üstü çizili/kapalı dördüncü etiket: `No unconditional cross-platform “yes” category`.

### Değişken, eksen ve kodlama

- Nicel eksen yoktur.
- Ok kalınlıkları eşittir; “daha güçlü entegrasyon” veya “daha yüksek kalite” anlamı taşımaz.
- Dört bağlam bloğu eşit alan kaplar.
- Panel (b)'de üç sonuç kutusu aynı büyüklükte olmalıdır; bu kutular olasılık veya frekans göstermez.
- Measurement-plane mini-chain varsa yalnızca sıra gösterir: `design/input → optical link → electrical → DSP/communication/sensing → joint/system`.

### Etiket, legend ve renk

- Physical context: teal; Coupling: orange; Measurement: purple-blue; Provenance: neutral gray-blue.
- Her renge ayrı simge/başlık eşlik eder; legend gerekmemesi tercih edilir.
- “Signal path” içinde optical-to-RF dönüşüm sınırı kesik dikey çizgiyle gösterilebilir.
- Coupling düğümleri aynı büyüklüktedir; count badge verilmez. Ampirik sayımlar FIG-OISAC-04'ün görevidir.

### Annotation ve belirsizlik

- `Same label ≠ same plane` uyarısı measurement bloğunda.
- `Same unit ≠ same task` uyarısı physical-context bloğunda.
- `Validation setting bounds transfer` uyarısı provenance bloğunda.
- İstatistiksel belirsizlik yoktur; bu review-controlled analytical framework'tür.

### Boyut

- `figure*`, 7.0–7.16 in genişlik, yaklaşık 3.8–4.2 in yükseklik; önerilen aspect 1.75–1.9.
- 2×1 panel veya üstte hub, altta gate; tek sütuna küçültülmemelidir.

### Uygulama rotası

- Tercih: deterministik SVG/TikZ veya Python `matplotlib.patches` + `FancyArrowPatch`; `.svg` ve `.pdf` üretimi.
- Şema node koordinatları kaynak kodda sabitlenmeli; otomatik force-directed layout kullanılmamalıdır.
- İkon gerekiyorsa basit çizgisel, telifsiz veya tamamen özgün olmalı; fotogerçekçi/AI görsel kullanılmamalıdır.

### Veri ve otorite

- Aktif Section 3 tanımları.
- Review Methods'teki extraction/claim-governance alanları.
- Planlı `Cross-Platform Comparison Record` tablosu tam alan sözlüğünün yetkili taşıyıcısıdır; şekil o tabloyu kısaltarak öğretir, yerine geçmez.
- Denominator: uygulanmaz; kavramsal model.

### Önerilen İngilizce lead-in

> Figure X condenses the review's comparison logic into four axes. A reported value is interpreted only after its physical context, coupling location, measurement contract, and provenance are retained; the resulting record then supports within-study interpretation, a conditional cross-study relation, or descriptive use.

### Şekil sonrası paragrafın görevi

Sonraki metin sayıları tekrarlamamalı; şu çıkarımı yapmalıdır: modality, coupling ve measurement plane aynı eksen değildir. `Technical System Boundary` alt bölümü bu yüzden fiziksel sınırı ilk eksen olarak ayrıntılandırır. Ayrıca şeklin “integration score” veya maturity ladder olmadığı açıkça söylenmelidir.

### Caption blueprint (English)

> **Four-axis framework used to interpret O-ISAC evidence across platforms.** Physical context identifies the modality, signal path, tasks, target, and geometry; coupling location records what communication and sensing share; the measurement contract retains the metric definition, plane, unit, conditions, constraints, and baseline; and provenance retains origin, validation setting, configuration, and source locator. These fields feed three admissibility outcomes—within-study interpretation, conditional cross-study relation, or descriptive use. Missing fields are not inferred, and the framework contains no unconditional cross-platform comparison category.

### Evidence gate

- Dört eksen ve üç sonuç metin ile birebir eşleşmeli.
- `reported/calculated/digitized` kökenleri doğru gösterilmeli; proje kendisi digitization yapmış gibi görünmemeli.
- `target`, `constraints`, `validation`, `baseline`, `locator` kaybolmamalı.
- Şekil, planlı schema table ile alan adları bakımından çapraz kontrol edilmeden yayıma girmemeli.

### Failure modes / do not do

- Eksenleri ardışık maturity aşamaları gibi dizmek.
- Modality ailelerini performans sırasına koymak.
- `within-study` kutusunu “low evidence”, `cross-study` kutusunu “high evidence” gibi renklendirmek.
- Missing'i absent olarak göstermek.
- Çok küçük yazıyla tüm extraction schema'yı şekle taşımak; ayrıntı tabloda kalmalıdır.

### COMST işlevsel örnekleri

- **COMST_060, Fig. 6:** “Taxonomy of RIS-assisted localization...” — yakın-okumada `taxonomy_map`; birden fazla analitik boyutu ortak bir görsel referansa dönüştürdüğü için benzer. O-ISAC şekli bunun kategori ağacını değil, karşılaştırma kaydına beslenen bağımsız eksenlerini kullanacaktır.
- **COMST_053, Fig. 8:** “A novel promising 6G network architecture (CSC: Communications, sensing, and computing).” — `system_architecture`; katmanlar ve arayüzler arasındaki ilişkiyi tek bakışta kurduğu için benzer. O-ISAC'ta oklar teknik bağlam akışını gösterir, performans veya olgunluk göstermez.
- **COMST_017, Fig. 4:** “SmartThings architecture.” — `taxonomy_map/system architecture` işlevli yakın okuma; ana bileşenleri ve arayüzleri görünür kılma açısından yapısal bir analogdur.

## 5. FIG-OISAC-02 — PRISMA Flow and Report-to-Study Mapping

### Kimlik ve yerleşim

- **Dosya:** `05_CORPUS_AND_APPRAISAL_RESULTS.tex`
- **Subsection:** `Study Selection and Report-to-Study Mapping`
- **Kesin yer:** Bu alt bölümün dördüncü paragrafının, “...different search state and denominator.” cümlesinin ardından; `\subsection{Governed Evidence Base}` öncesi. Mevcut dosyada yaklaşık satır 35–37 arası.
- **Neden burada:** Tüm seçim ve mapping sayıları önce tanımlanır; şekil bunları tek akışta uzlaştırır. Sonraki alt bölüm sabit 206-study denominator'den başlayabilir.

### Reader question

**How did 1,733 identified records become 227 eligible reports and 206 unique studies, while contextual records and bibliographic aliases remained visible?**

### Tek cümlelik ana mesaj

**The review's denominator changes from records to unique reports and finally to studies; 21 reports are consolidated through report-to-study mapping rather than excluded.**

### Görsel arketipi

PRISMA 2020 düzenine bağlı **selection flow diagram**, altına eklenen açık bir `reports → studies` mapping bridge ve ayrı contextual branch.

### Panel ve içerik modeli

**Panel (a) — Identification, screening, retrieval, eligibility**

Ana dikey akış:

1. Records identified: **1,733**
   - Scopus 1,273;
   - IEEE Xplore 329;
   - ScienceDirect 24;
   - SpringerLink 75;
   - Wiley 29;
   - Taylor & Francis 3.
2. Removed before screening:
   - duplicates 472;
   - other metadata/platform dispositions 2;
   - automation removals 0.
3. Records screened: **1,259**.
4. Not advanced: **927**, internally separated as:
   - title/abstract exclusions 864;
   - contextual-only 61;
   - duplicate/related-version flags 2.
5. Historical retrieval queue: **332 source records**.
6. Post-screening alias consolidation: **2 aliases**.
7. Unique reports sought: **330**.
8. Reports not retrieved: **58**.
9. Full-text reports assessed: **272**.
10. Full-text outcomes:
    - excluded 39;
    - contextual 6;
    - eligible primary reports **227**.

Full-text exclusion side box, six satırla 39'u uzlaştırır: 4 non-optical/RF-only; 2 communication-only; 12 sensing-only; 5 no genuine integration; 4 abstract/poster/editorial/opinion/other non-full-paper; 12 insufficient English full technical content.

**Panel (b) — Context and study mapping**

- Contextual branch: `61 screening-stage + 6 full-text = 67 contextual records`.
- Mapping bridge: `227 eligible reports → report clustering/companion linkage → 206 unique studies`.
- Bridge annotation: `21-report reduction; not an exclusion count`.
- Historical callout: `Legacy OSF 221-study snapshot = separate search state, not a node in this attrition chain.`

### Değişken, eksen ve kodlama

- Nicel eksen yoktur; kutu sayıları gerçek flow count'tur.
- Ana akış solid blue; exclusion side boxes gray; contextual branch orange; report-to-study bridge teal.
- Ok kalınlığı miktarı temsil etmez; Sankey görünümü verilmez.
- Records, reports ve studies kutularının şekli veya başlık bandı farklı olmalıdır. Öneri: record kutuları düz köşe; report kutuları hafif yuvarlak; study kutusu çift çerçeve. Renk olmadan da unit transition anlaşılmalıdır.

### Annotation ve belirsizlik

- `332 → 330` farkı alias consolidation ile açıkça gösterilmelidir; 330 ve 58 sayıları 332 ve 60 ile karıştırılmamalıdır.
- `61 + 6 = 67` contextual toplamı ana primary stream'e geri bağlanmamalıdır.
- `227 → 206` mapping bir exclusion oku taşımamalıdır.
- İstatistiksel belirsizlik yoktur; locked flow counts'tur.

### Boyut

- `figure*`, 7.16 in × yaklaşık 5.0–5.5 in; aspect 1.3–1.45.
- İki sütunlu yatay panel düzeni veya solda ana flow, sağda contextual/mapping; tek sütuna zorlanmamalıdır.

### Uygulama rotası

- PRISMA 2020 node mantığı korunarak TikZ, Graphviz veya özgün SVG.
- Kaynak count CSV'sinden otomatik label üretimi önerilir; sayılar çizim koduna dağınık biçimde hard-code edilmemelidir.
- Gelecek üretim paketinde `fig_prisma_source_counts.csv`, çizim scripti ve reconciliation testleri bulunmalıdır.

### Veri ve otorite

- Yetkili kaynak: `09_kayitlar/checkpoints/prisma_flow_PHASE_C_FINAL_2026-07-30/PRISMA_FLOW_COUNTS_FINAL_2026-07-30.csv`.
- QA: aynı checkpoint'teki `PHASE_C_PRISMA_QA_2026-07-30.json` ve Item 16a/16b validation.
- Report-to-study mapping: Phase C final report ve locked 227-report/206-study mapping.
- Denominatorler unit-specific: 1,733 records; 1,259 screened records; 330 unique reports sought; 272 assessed reports; 227 eligible reports; 206 studies.

### Önerilen İngilizce lead-in

> Figure X reconciles the review flow while preserving the change in counting unit from records to reports and studies. The formal retrieval layer uses 330 unique reports after two post-screening aliases were consolidated, and the final report-to-study step links companion reports rather than applying another eligibility exclusion.

### Şekil sonrası paragrafın görevi

Ana çıkarım iki cümlede yapılmalıdır: 67 contextual records terminology/history için ayrı tutulur; 227 eligible reports'in 206 çalışmaya inmesi tekrar yayınların/companion reports'in kümelenmesidir. Ardından Governed Evidence Base alt bölümü 206'yı sabit denominator olarak kullanır.

### Caption blueprint (English)

> **PRISMA 2020 flow with contextual-record handling and report-to-study mapping.** Six sources yielded 1,733 records. After 472 duplicates and two other pre-screening dispositions were removed, 1,259 records were screened. The retrieval queue contained 332 source records; consolidation of two bibliographic aliases yielded 330 unique reports sought, of which 58 were not retrieved and 272 were assessed in full text. Full-text assessment produced 227 eligible primary reports, 39 exclusions, and six contextual reports. Together with 61 screening-stage contextual records, the contextual corpus contains 67 records. Mapping related and companion reports reduced 227 eligible reports to 206 unique studies; the difference of 21 is not an additional exclusion count. The retrospective 221-study OSF snapshot used a different review state and is not part of this attrition chain.

### Evidence gate

- `1273+329+24+75+29+3=1733`.
- `1733−472−2=1259`.
- `1259−927=332`; `332−2 aliases=330`.
- `330−58=272`.
- `272−39−6=227`.
- `61+6=67 contextual`.
- `227−21=206 studies`.
- Exclusion reasons sum to 39.
- “No record removed autonomously by automation” note remains accurate.

### Failure modes / do not do

- 221'i eski bir included count olarak akışa bağlamak.
- 332/60 historical source-queue sayıları ile 330/58 formal unique-report sayımlarını aynı kutuda kullanmak.
- Contextual kayıtları exclusions içine gömmek.
- 21'i full-text exclusion gibi göstermek.
- PRISMA'yı survey'in bilimsel katkısı gibi görsel olarak büyütmek; şekil audit işlevlidir.

### COMST işlevsel örnekleri

- **COMST_060, Fig. 1:** “The overall outline of the article.” — yakın-okumada `survey_roadmap`, Review Method içinde hazırlanmış bir akışı tek görsel referansa dönüştürür. O-ISAC şeklinin içerik otoritesi değildir; yalnızca okunaklı sequence işlevi analogdur.
- **COMST_032, Fig. 4:** “General overview of WLAN sensing procedure for both sub-7GHz sensing and DMG sensing.” — `protocol_workflow`; dallanan bir sürecin aşamalarını ve alternatif yollarını açıkça ayırdığı için yapısal analogdur.
- **COMST_038:** metninde PRISMA tabanlı survey methodology açıkça kullanılmıştır, fakat yakın-okuma setinde buna karşılık gelen yüksek güvenli bir selection-flow şekli yoktur. Bu nedenle biçim COMST'tan kopyalanmamalı; PRISMA 2020 reporting logic yetkili şablon olmalıdır.

## 6. FIG-OISAC-03 — TQAF Evidence Profile Across 206 Studies

### Kimlik ve yerleşim

- **Dosya:** `05_CORPUS_AND_APPRAISAL_RESULTS.tex`
- **Subsection:** `Study-Level Technical Appraisal`
- **Kesin yer:** “Clear reporting thus did not usually supply a reusable benchmark or a direct numerical comparison.” cümlesinden sonra; “Validation warrants a second view...” paragrafından önce. Mevcut dosyada yaklaşık satır 77–79 arası.
- **Neden burada:** İlk üç paragraf overall ve sekiz dimension dağılımını tanımlar. Şekil bu sayı yükünü tek profile indirger; sonraki paragraf validation farkını açar.

### Reader question

**Where is the 206-study evidence base strong enough for source-level interpretation, and where does it fail to support portable benchmarking or direct comparison?**

### Tek cümlelik ana mesaj

**Most studies are technically interpretable and well reported, but benchmark readiness and comparison admissibility remain predominantly adequate or low under the review-specific TQAF rules.**

### Görsel arketipi

Dokuz satırlı **horizontal 100% stacked profile**. Her satır 206 çalışmayı strong/adequate/low olarak tam uzlaştırır; satırlar kavramsal gruplar içinde sabit sıradadır.

### Veri modeli

| Group | Dimension | Strong | Adequate | Low | Total |
|---|---|---:|---:|---:|---:|
| Summary | Overall evidence contribution | 125 | 75 | 6 | 206 |
| Interpretability | Technical relevance | 123 | 68 | 15 | 206 |
| Interpretability | Metric clarity | 168 | 7 | 31 | 206 |
| Interpretability | Reporting completeness | 196 | 10 | 0 | 206 |
| Interpretability | Limitation transparency | 153 | 44 | 9 | 206 |
| Portability | Validation maturity | 6 | 168 | 32 | 206 |
| Portability | Reproducibility | 3 | 199 | 4 | 206 |
| Portability | Benchmark readiness | 0 | 158 | 48 | 206 |
| Portability | Comparison admissibility | 4 | 10 | 192 | 206 |

### Değişken, eksen ve kodlama

- Y axis: dokuz dimension; sıralama yukarıdaki gibidir. Strong oranına göre sort edilmez.
- X axis: `0–100% of studies`; ayrıca segment içinde `n` etiketleri.
- Stack order soldan sağa `strong → adequate → low`; legend aynı sırada.
- Overall satırı üstte, diğerlerinden ince ayırıcı çizgiyle ayrılır.
- Interpretability ve Portability grupları sol margin bandı veya brace ile ayrılır; grup etiketleri renk değil metinle taşınır.
- Segment `n<8` ise sayı segment içine sığmıyorsa dış callout; segment tamamen yoksa `0` küçük açık işaretle gösterilir.

### Etiket, legend ve renk

- Strong: mavi `#0072B2`; Adequate: gri `#A7A9AC`; Low: vermilion `#D55E00`.
- Yüzdeler axis üzerinden okunur; segmentlerde sayı `n` doğrudan yazılır. Her satırın sağında küçük `n=206` tekrarına gerek yok; üst başlıkta “each row n=206”.
- Legend başlığı `Review-specific TQAF category`; “quality” kelimesi tek başına kullanılmamalıdır.
- Grayscale için strong düz dolgu, adequate noktalı veya orta gri, low diagonal hatch.

### Annotation ve belirsizlik

- Sağ üst callout: `TQAF is review-specific and nonvalidated; categories describe evidentiary support, not study worth.`
- Interpretability–portability ayrımında ince bir açıklama: `clear source reporting does not guarantee transfer across studies`.
- Confidence interval yoktur; tüm 206 retained studies için deterministic classification'dır.
- Causal annotation yoktur; open artifact veya validation'ın score'a neden olduğu test edilmedi.

### Boyut

- `figure*`, 7.16 in × 4.2–4.7 in; aspect yaklaşık 1.55–1.7.
- Tek sütun kullanılmamalıdır; uzun dimension etiketleri ve doğrudan n değerleri küçülür.

### Uygulama rotası

- Python `matplotlib` horizontal `barh`, sabit kategori sırası ve kaynak CSV.
- Gelecekteki source CSV kolonları: `group,display_order,dimension,strong_n,adequate_n,low_n,denominator`.
- Script her satır toplamını 206'ya karşı assert etmeli ve overall toplam QA üretmelidir.
- Çıktı `.pdf` + `.svg`; font embedding kontrol edilmelidir.

### Veri ve otorite

- `09_kayitlar/checkpoints/quality_assessment_PHASE_E_FINAL_2026-08-04/phase_e_tqaf_summary_2026-08-04.md`.
- Aynı checkpoint'teki dimension audit ve QA JSON; 206 one-study rows, 43/43 QA pass.
- Denominator: her satır 206 unique studies.
- Score mapping: strong=3, adequate=2, low=1. Bu dağılımlarda score 0 yoktur.

### Önerilen İngilizce lead-in

> Figure X places the eight TQAF dimensions beside the overall evidence-contribution category. Each row reconciles all 206 studies and separates dimensions that support source-level interpretation from those that govern transfer, reconstruction, and direct comparison.

### Şekil sonrası paragrafın görevi

Metin grafiği okumalı, barları tekrar etmemelidir: reporting completeness ve metric clarity'nin genel olarak güçlü olması; benchmark readiness ve comparison admissibility'nin buna rağmen güçlü olmaması. Bu çelişki değil, farklı contract'ların sonucudur. Sonraki “Validation warrants a second view” paragrafı maximum setting ile paired-function validation score ayrımına geçer.

### Caption blueprint (English)

> **Review-specific TQAF profile for all 206 included studies.** Each horizontal bar shows the proportion and count classified as strong (score 3), adequate (score 2), or low (score 1) for one deterministic dimension or for overall evidence contribution. Technical relevance, metric clarity, reporting completeness, and limitation transparency primarily describe whether a study can be interpreted on its own terms. Validation maturity, reproducibility, benchmark readiness, and comparison admissibility impose additional conditions on transfer and reuse. The categories are not eligibility decisions, risk-of-bias grades, or a ranking of scientific worth, and no causal relation among dimensions is inferred.

### Evidence gate

- Her satır strong+adequate+low=206.
- Exact counts yukarıdaki tabloyla ve Phase-E summary ile eşleşir.
- `benchmark strong=0`, `reporting low=0` açıkça ama dramatize edilmeden gösterilir.
- Overall ile sekiz dimension karıştırılmaz; overall ayrı summary row'dur.
- Validation bar, FIG-OISAC-06'daki maximum-tier distribution olarak etiketlenmemelidir; ikisi farklı kuraldır.

### Failure modes / do not do

- Satırları strong oranına göre leaderboard gibi sıralamak.
- Radar chart kullanmak; ordinal score'ları geometrik alana dönüştürmek.
- Mean TQAF score üretmek; mevcut sınıflandırmanın dışına yeni nicel ölçek eklemek.
- Low'u “bad study” veya strong'u “high-quality paper” diye etiketlemek.
- Validation maturity 6/168/32 ile maximum validation tier 32/18/78/66/12'yi birleştirmek.

### COMST işlevsel örnekleri

- **COMST_069, Figs. 4–8:** örneğin Fig. 4 “Percentage of RA papers for PLC in terms of voltage levels.” — `bibliometric_distribution`; survey corpusundaki kategori dağılımlarını doğrudan göstermek açısından analogdur. O-ISAC tek bir denominator ve direct counts kullanacak, çalışma değerini sıralamayacaktır.
- **COMST_060, Fig. 8:** “State of the art literature breakdown...” — `bibliometric_distribution`, section ortasında yer alır ve metin sonradan örüntüyü yorumlar. O-ISAC profile da numeric inventory'yi offload eder, fakat mutually exclusive TQAF categories'yi korur.
- **COMST_024, Fig. 7:** “Adopted sensors.” — yakın-okumada surveyed-evidence distribution; teknik envanteri prose'dan görsele taşıması bakımından işlevsel analogdur.

## 7. FIG-OISAC-04 — Multi-Label Integration and Resource-Coupling Map

### Kimlik ve yerleşim

- **Dosya:** `07_INTEGRATION_ARCHITECTURES.tex`
- **Section:** `INTEGRATION ARCHITECTURES AND RESOURCE COUPLING`
- **Kesin yer:** Section'ın iki açılış paragrafı ve 118/117/113/... sayımlarından sonra; `\subsection{Shared Hardware, Carrier, and Link}` öncesi. Mevcut dosyada yaklaşık satır 15–16.

### Reader question

**At which locations can communication and sensing be coupled, and why do the seven mechanism labels overlap rather than form an exclusive hierarchy?**

### Tek cümlelik ana mesaj

**O-ISAC integration can occur at several locations in the same system—hardware, carrier, waveform, resources, link, design rule, and application—so category counts describe overlapping mechanisms, not maturity levels.**

### Görsel arketipi

Generic communication–sensing signal path üzerine bindirilmiş **annotated coupling topology**; eşit boyutlu count badges ve üç örnek mechanism chain. Bar chart, Venn ve ladder kullanılmaz.

### Panel ve içerik modeli

**Ana panel — Where coupling occurs**

Yatay sistem yolu:

`source/front end → carrier/modulation → waveform/frame → resource controller → propagation link/channel & target → receiver/DSP → service/application`

İki ince lane aynı yol boyunca ilerler: `communication function` ve `sensing function`. Paylaşım noktaları bu lane'leri bağlayan node/brace olarak işaretlenir:

- Shared hardware — **117/206**;
- Shared optical carrier — **49/206**;
- Shared waveform — **113/206**;
- Shared resource allocation — **118/206**;
- Shared link/channel — **87/206**;
- Joint design/optimization — **72/206**, birden fazla değişkeni çevreleyen bracket;
- Shared application scenario — **46/206**, service layer bağlantısı;
- Mixed boundary cases — **3/206**, ana yol dışında küçük audit callout.

Alt bantta üç kısa case chain, count değil mekanizma örneği olarak:

1. `Embedded pilots → waveform + resources` (SCR-00007);
2. `Deployed fiber path → hardware/link coupling` (SCR-00957 veya source audit ile doğrulanmış örnek);
3. `Multi-segment service → application/boundary coupling` (SCR-00277 veya final citation audit ile doğrulanmış örnek).

Bu üç örnek son üretimde aktif citation map ile yeniden doğrulanmalıdır.

### Değişken, eksen ve kodlama

- Nicel axis yoktur; counts uniform badges olarak verilir.
- Node alanı ve badge alanı count ile ölçeklenmez.
- Soldan sağa sıra physical location sırasıdır, prevalence sırası değildir.
- Communication ve sensing lane'leri farklı line style ile ayrılır: communication solid, sensing dashed; renk ayrıca destekleyebilir.
- Joint design brace tek bir fiziksel component değildir; seçilen değişkenler/constraints arasında üstten uzanır.

### Etiket, legend ve renk

- Hardware/components: mavi-gri; signal/carrier/waveform: teal; resource/design: orange; link/application: purple.
- Her paylaşım düğümünde tam etiket ve `n=...`; legend yalnızca lane/line style için.
- Üst banner: `Multi-label study coding; counts must not be summed.`
- Alt annotation: `Location of coupling ≠ strength or maturity of integration.`

### Annotation ve belirsizlik

- `other=0` ve `unclear=0` ana düğüm olarak çizilmez; küçük QA notu olarak caption'a alınabilir.
- Count percentages istenirse badge altında küçük puntoda verilebilir: 57.3, 56.8, 54.9, 42.2, 35.0, 23.8, 22.3, 1.5%. Count ana göstergedir.
- Multi-label intersections hesaplanmadığı için overlap alanları veya chord widths üretilmez.
- Confidence interval yoktur.

### Boyut

- `figure*`, 7.16 in × 3.8–4.3 in; aspect 1.7–1.9.

### Uygulama rotası

- SVG/TikZ veya Python `matplotlib.patches`; düz coordinate system.
- Ana data file `s2_integration_mechanisms.csv`; label generator count ve percent'i otomatik almalıdır.
- Case callout'ları citation key ile kaynak kodda saklanmalı; elle yazılmış study title kullanılmamalıdır.

### Veri ve otorite

- `09_kayitlar/checkpoints/synthesis_PHASE_F_FINAL_2026-08-04/s2_integration_mechanisms.csv`.
- Denominator: 206 unique studies; tüm mechanism kategorileri multi-label.
- Aktif Section 7 ve Phase-F QA/normalization audit.

### Önerilen İngilizce lead-in

> Figure X locates the seven recurring integration mechanisms along a generic O-ISAC signal and service path. The badges report overlapping study coverage, while the layout is ordered by coupling location rather than by prevalence or maturity.

### Şekil sonrası paragrafın görevi

İlk çıkarım: en sık görülen üç etiket (resource, hardware, waveform) aynı çalışmada bir causal chain oluşturabilir; toplanamaz. İkinci çıkarım: application-level coupling gerçek bir category'dir fakat shared waveform ile eşdeğer değildir. Sonra Shared Hardware alt bölümüne fiziksel reuse noktasından geçilir.

### Caption blueprint (English)

> **Locations of communication–sensing coupling in the 206-study O-ISAC corpus.** Shared resource allocation (118 studies), hardware (117), waveform (113), link or channel (87), joint design or optimization (72), optical carrier (49), and application scenario (46) are shown at their typical locations along a generic system path; three mixed boundary cases are retained separately. Coding is multi-label, so a study may occupy several locations and the counts must not be summed. Node order and size do not indicate prevalence, integration strength, or maturity.

### Evidence gate

- Count list exactly matches S2 CSV.
- `resource=118`, `hardware=117`, `waveform=113` labels swapped olmamalıdır.
- Tüm kategoriler multi-label; total üretilmez.
- `mixed=3`, `other=0`, `unclear=0` doğru audit edilir.
- Case examples final citation/source audit olmadan caption'a alınmaz.

### Failure modes / do not do

- Exclusive bar, pie veya donut ile toplam %100 vermek.
- Venn/UpSet üretmek; intersection data yoktur.
- “deeper coupling”i daha iyi veya daha olgun göstermek.
- Joint design'i system path üzerinde fiziksel cihaz gibi çizmek.
- Application-level coupling'i shared waveform'a yükseltmek.

### COMST işlevsel örnekleri

- **COMST_044, Fig. 9:** “Diagram of Resource Allocation in Different Domains.” — yakın-okumada `physical_mechanism`; time/frequency/code/space gibi resource domains'i tek mekanizma haritasında ilişkilendirdiği için güçlü analogdur.
- **COMST_060, Figs. 6–7:** RIS-assisted localization taxonomy — `taxonomy_map`; eşzamanlı birden fazla sınıflandırma boyutunu görünür kılar. O-ISAC şekli exclusive branch yerine coupling location kullanır.
- **COMST_014, Fig. 5:** “Taxonomy of VLP systems.” — `taxonomy_map`, integration-design bağlamında kategori ilişkilerini prose'dan offload etmesi bakımından analogdur.

## 8. FIG-OISAC-05 — Condition-Aware Trade-Off Evidence Map

### Kimlik ve yerleşim

- **Dosya:** `09_COMMUNICATION_SENSING_TRADEOFFS.tex`
- **Section:** `COMMUNICATION--SENSING TRADE-OFFS`
- **Kesin yer:** Üçüncü açılış paragrafının, “The families below synthesize recurring causal mechanisms while retaining that boundary.” cümlesinden sonra; `\subsection{Bandwidth, Spectrum, and Resource Allocation}` öncesi. Mevcut dosyada yaklaşık satır 26–28.

### Reader question

**Which trade-off mechanisms dominate the governed evidence, how much of each family is quantitative versus qualitative, and how often is interpretation conditional?**

### Tek cümlelik ana mesaj

**Trade-off evidence concentrates in resource and power mechanisms and is overwhelmingly condition-dependent; family frequency maps where coupling is studied, not how strong an effect is.**

### Görsel arketipi

Ortak y-sırasını paylaşan üç panelli **aligned evidence-profile plot**:

- (a) stacked horizontal claim bars: quantitative + qualitative;
- (b) unique-study lollipop/dot counts;
- (c) conditional-share dots.

Bu bir Pareto/frontier grafiği değildir ve hiçbir kaynak performans değerini yeniden çizmez.

### Nihai veri modeli

Phase-F raw ledger iki `reported_status=absent` sentinel içerdiği için görsel **402 substantive rows** üzerinden üretilmelidir. Locked `tradeoff_family()` düzeltmesinde sentinel'lerin biri `bandwidth_spectrum_or_resource_allocation`, diğeri `qualitative_or_partial_general` ailesindedir. Bu nedenle ilk satır 95'ten 94 record'a, 71'den 70 study'ye, 90'dan 89 conditional record'a ve 45'ten 44 qualitative record'a; ikinci satır 11'den 10 record'a, 9'dan 8 study'ye, 8'den 7 conditional record'a ve 9'dan 8 qualitative record'a düşer. İki sentinel de final comparison-admissibility alanında conditionally comparable görünse de bilimsel substantive profile'a alınmaz. Diğer aile satırları değişmez.

| Order | Family | Quant. | Qual. | Claims | Unique studies | Conditional | Conditional % |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Bandwidth/spectrum/resource allocation | 50 | 44 | 94 | 70 | 89 | 94.7 |
| 2 | Power/energy/dynamic range | 50 | 40 | 90 | 64 | 81 | 90.0 |
| 3 | Communication reliability vs sensing quality | 37 | 22 | 59 | 48 | 55 | 93.2 |
| 4 | Rate–resolution | 26 | 20 | 46 | 39 | 41 | 89.1 |
| 5 | Rate–accuracy/localization | 22 | 18 | 40 | 33 | 39 | 97.5 |
| 6 | Rate–range/coverage | 10 | 11 | 21 | 16 | 18 | 85.7 |
| 7 | Waveform/hardware/complexity | 6 | 15 | 21 | 20 | 21 | 100.0 |
| 8 | Other joint trade-off | 14 | 5 | 19 | 15 | 18 | 94.7 |
| 9 | Qualitative/partial general | 2 | 8 | 10 | 8 | 7 | 70.0 |
| 10 | Security/resilience | 1 | 0 | 1 | 1 | 1 | 100.0 |
| 11 | Synergy/non-antagonistic coupling | 0 | 1 | 1 | 1 | 1 | 100.0 |
|  | **Total/union where defined** | **218** | **184** | **402** | **168 unique studies overall; family counts not additive** | **371** | **92.3 overall** |

### Değişken, eksen ve kodlama

- Ortak y axis yukarıdaki manuscript narrative order'dır; tie olan iki 21-record family metindeki sıraya göre dizilir.
- Panel (a) x axis `substantive records`, 0–100. Quantitative solid blue; qualitative orange outline/hatch. Bar sonunda total `n`.
- Panel (b) x axis `unique studies in family`, 0–75; dark neutral dot + thin stem. Study counts toplanmaz.
- Panel (c) x axis `conditional records within family (%)`, 0–100; overall 92.3% dikey dashed reference. Her dot yanında `conditional/claims`, ör. `89/94`.
- n=1 family dots hollow ve `n=1` etiketiyle gösterilir; %100 görsel olarak büyük kanıt izlenimi vermemelidir.

### Etiket, legend ve renk

- Quantitative: mavi `#0072B2`; qualitative: orange `#E69F00`; study dot: koyu gri; conditional dot: purple/blue `#6A51A3`.
- Panel başlıklarında denominator açıkça yazılır.
- Family label kısaltmaları caption/alt text içinde tam açılır.
- Üst banner: `Claims are coded relationships—not independent effects.`

### Annotation ve belirsizlik

- Panel (a) toplam annotation: `218 quantitative + 184 qualitative = 402 substantive`.
- Panel (b): `168 studies in the union; family study counts overlap.`
- Panel (c): `371/402 conditional`; n=1 tail open markers.
- Confidence interval yoktur. Özellikle küçük family yüzdeleri inferential estimate gibi yorumlanmamalıdır.
- Frequency/strength ayrımı caption'da açık olmalıdır.

### Boyut

- `figure*`, 7.16 in × 5.0–5.5 in; aspect 1.3–1.45.
- Üç panelin x-axis scale'leri farklıdır ve ayrı başlık taşır; dual-axis kullanılmaz.

### Uygulama rotası

- Python `matplotlib` + `GridSpec`, ortak y-coordinate.
- Raw `s4_tradeoff_families.csv` doğrudan çizilmemeli; bandwidth/resource ve qualitative/partial satırlarından birer qualitative, conditional absence sentinel çıkaran açık bir preprocessing/QA adımı olmalıdır.
- Script assertions: 11 rows; quant=218; qual=184; claims=402; conditional=371; overall studies=168 separately supplied.
- `.csv` derived source, `.py`, `.svg`, `.pdf` birlikte saklanmalıdır.

### Veri ve otorite

- Raw authority: `09_kayitlar/checkpoints/synthesis_PHASE_F_FINAL_2026-08-04/s4_tradeoff_families.csv`.
- Sentinel correction authority: active Section 9 ve `manuscript/comst_206_v1/qa/TRADEOFF_DENOMINATOR_RECONCILIATION.md`.
- Denominator lineage: **404 governed ledger rows / 169 governed studies / 373 conditionally comparable ledger rows**. Excluding the two qualitative, conditional `reported_status=absent` audit sentinels yields **402 substantive records / 168 substantive studies / 371 conditional substantive records**. The 169-to-168 study change is therefore part of the sentinel exclusion, not an unexplained deduplication.

### Önerilen İngilizce lead-in

> Figure X separates three properties of the trade-off ledger: the quantitative and qualitative record volume in each mechanism family, the overlapping number of contributing studies, and the share of records that remain condition-dependent. The plot uses the 402 substantive records after the two absence-status audit rows are removed.

### Şekil sonrası paragrafın görevi

Metin şu iki pattern'i yorumlamalıdır: resource ve power aileleri en çok kodlanan mekanizmalardır; fakat hemen tüm ailelerde conditionality yüksektir. Bu, ortak effect size veya frontier kurmaya değil, alt bölümlerde causal mechanism okumaya yönlendirir. n=1 security/synergy tail için genel sonuç çıkarılmamalıdır.

### Caption blueprint (English)

> **Condition-aware map of 402 substantive communication–sensing trade-off records from 168 studies.** Panel (a) separates 218 quantitative and 184 qualitative records across 11 mechanism families; panel (b) reports the overlapping number of studies contributing to each family; and panel (c) reports the within-family share carrying a comparison gate, source guardrail, or other condition-dependent admissibility decision. Overall, 371 of 402 records (92.3%) are conditional. Two absence-status rows retained in the 404-row governed ledger are excluded from this scientific profile. Family study counts must not be summed, record frequency is not effect strength, and the records do not sample a common design space or universal Pareto frontier.

### Evidence gate

- Derived table exactly reconciles 402, 218, 184, 371 and 168.
- Governed-to-substantive lineage exactly reconciles `404 / 169 / 373` to `402 / 168 / 371`; neither denominator state may be silently substituted for the other.
- Bandwidth/resource row uses 94 claims/70 studies/89 conditional/50 quantitative/44 qualitative, not raw 95/71/90/50/45.
- Qualitative/partial row uses 10 claims/8 studies/7 conditional/2 quantitative/8 qualitative, not raw 11/9/8/2/9.
- Panel (b) does not sum study counts.
- Conditional percentages use family claim denominator, not 402.
- Security/synergy n=1 is visibly marked.
- No performance value, common unit, effect size, curve digitization or frontier is produced.

### Failure modes / do not do

- Raw 404 rowsu substantive diye çizmek.
- Unique-study barsı toplayıp yanlış total üretmek.
- Conditional %'yi confidence/quality score gibi göstermek.
- 11 family için radar veya pie chart kullanmak.
- Source BER/range/rate valuesini aynı scatter'a taşımak.
- Frequency sırasını “importance” veya “severity” diye adlandırmak.

### COMST işlevsel örnekleri

- **COMST_059, Fig. 12:** “Two-user Gaussian multiple-access capacity region...” — yakın-okumada `tradeoff_plot`; ortak model ve tanımlı eksenler altında geçerli bir frontier örneğidir. O-ISAC corpusunda böyle ortak bir design space bulunmadığından bizim şekil frontier çizmek yerine evidence-family profile gösterir.
- **COMST_073, Fig. 15:** “Visualising the landscape of available indoor positioning systems, in terms of their cost versus their accuracy...” — `tradeoff_plot`; caption'ın kendisi subjective extrapolation sınırını kabul eder. Bu, platformlar arası oval/scatter yaklaşımının neden O-ISAC'ta kullanılmaması gerektiğine karşı-örnektir.
- **COMST_044, Fig. 9:** resource-allocation domains diagram — trade-off mekanizmalarını fiziksel kontrol değişkenleri üzerinden öğretmesi bakımından kavramsal analogdur.

## 9. FIG-OISAC-06 — Validation Setting Versus Reported Validation Methods

### Kimlik ve yerleşim

- **Dosya:** `10_VALIDATION_AND_REPRODUCIBILITY.tex`
- **Subsection:** `Validation Methods and Operating Realism`
- **Kesin yer:** Bu alt bölümün ilk paragrafının, overlapping method counts ve “The totals exceed 206...” açıklamasından hemen sonra; “These methods answer different validity questions.” paragrafından önce. Mevcut dosyada yaklaşık satır 49–53.
- **Plan değişikliği:** İlk plan şekli `Maximum Validation Maturity` altında tek dağılım olarak yerleştiriyordu. FIG-OISAC-03 artık TQAF validation dimension'ını gösterdiği için tekrar önlemek amacıyla burada iki farklı validation view yan yana getirilir: exclusive maximum setting ve overlapping methods. Böylece 78 maximum-laboratory ile 148 laboratory-method count'un neden çelişmediği görsel olarak açıklanır.

### Reader question

**What is the strongest validation setting reached by each study, and which analytical, simulated, experimental, prototype, or field methods were used along the way?**

### Tek cümlelik ana mesaj

**Most O-ISAC studies reach laboratory or controlled-prototype settings, often through multiple validation methods, but field evidence remains limited and method accumulation is not a quality rank.**

### Görsel arketipi

İki panelli corpus distribution:

- **Panel (a):** one 100% stacked bar veya beş aligned bars — maximum tier, mutually exclusive;
- **Panel (b):** logical-order horizontal lollipop bars — validation methods, multi-label.

### Panel (a) veri modeli — maximum tier

| Order | Maximum tier | Studies | % of 206 |
|---:|---|---:|---:|
| 1 | Simulation or numerical | 32 | 15.5 |
| 2 | Enhanced simulation or dataset-supported | 18 | 8.7 |
| 3 | Laboratory experiment or proof of concept | 78 | 37.9 |
| 4 | Controlled prototype | 66 | 32.0 |
| 5 | Field trial or deployment | 12 | 5.8 |
|  | Total | 206 | 100.0 |

Direct annotation: `156/206 reached at least laboratory/PoC`; `12/206 reached field/deployment`.

### Panel (b) veri modeli — methods

| Logical group | Method | Studies | % of 206 |
|---|---|---:|---:|
| Model/data | Analytical | 131 | 63.6 |
| Model/data | Numerical analysis | 14 | 6.8 |
| Model/data | Simulation | 104 | 50.5 |
| Model/data | Dataset-based | 13 | 6.3 |
| Physical | Laboratory experiment | 148 | 71.8 |
| Physical | Prototype/testbed | 83 | 40.3 |
| Physical | Field experiment | 12 | 5.8 |
| Cross-method | Mixed validation | 33 | 16.0 |
| QA | Unclear | 0 | 0.0 |

### Değişken, eksen ve kodlama

- Panel (a): `percent of 206 studies`, 0–100; beş segment logical progression sırasındadır. Segment labels count+percent.
- Panel (b): x axis `studies reporting method`, 0–160; logical method order, count'a göre sort edilmez.
- Panel (a) heading: `Highest observed setting (mutually exclusive; Σ=206)`.
- Panel (b) heading: `Reported methods (multi-label; do not sum)`.
- Maximum-tier segment alanı count ile orantılı olabilir çünkü kategoriler exclusive ve sum=206. Method bars count ile orantılıdır fakat pie yapılmaz.

### Etiket, legend ve renk

- Panel (a) aynı rengin açık-koyu progression'ı kullanmamalıdır; bu maturity-as-quality çağrışımı yaratabilir. Bunun yerine beş category doğrudan etiketli, nötr ve farklı hatch/ton kombinasyonları.
- Panel (b) model/data group mavi, physical group orange, mixed gray; group brace metinsel.
- Field rengi kırmızı yapılmamalıdır; azlık “failure” değil evidence gap'tir.
- Grayscale için segment pattern ve direct labels zorunlu.

### Annotation ve belirsizlik

- Ortadaki açıklama oku: `Maximum tier answers “how far did the study reach?”; methods answer “what evidence did it use?”`.
- `148 laboratory methods ≠ 78 maximum-laboratory tier` örnek callout; higher-tier studies can also include laboratory work.
- Paired-function rule bu şeklin category'si değildir. Alt metinde `maximum setting does not establish that both functions were validated together` yazılmalıdır.
- Confidence interval yoktur.

### Boyut

- `figure*`, 7.16 in × 3.8–4.3 in; side-by-side veya üst/alt düzen. Uzun label'lar nedeniyle üst/alt düzen daha okunaklı olabilir.

### Uygulama rotası

- Python `matplotlib` + `GridSpec`; iki ayrı source table.
- Assertions: panel (a) sum=206; panel (b) unclear=0; panel (b) sum intentionally >206 and no total bar.
- `.svg` ve `.pdf`; panel titles ve denominator script tarafından üretilmeli.

### Veri ve otorite

- `09_kayitlar/checkpoints/synthesis_PHASE_F_FINAL_2026-08-04/s5_validation_maturity.csv`.
- `.../s5_validation_types.csv`.
- Aktif Section 10 ve Phase-F QA.
- Denominator: 206 unique studies. Panel (a) mutually exclusive; panel (b) multi-label.

### Önerilen İngilizce lead-in

> Figure X places the strongest setting reached by each study beside the validation methods reported across the corpus. The first panel is mutually exclusive, whereas the second is multi-label; this distinction explains why method counts can exceed the number of studies assigned to a given maximum tier.

### Şekil sonrası paragrafın görevi

Metin panel farkını teknik olarak yorumlamalıdır: analysis/simulation controlled sweeps; laboratory real components; prototype subsystem interactions; field at least one operational boundary. Daha fazla yöntem otomatik olarak daha yüksek rigor değildir; configuration transitions traceable olmalıdır. Sonraki realism paragrafına modality-specific disturbance koşullarıyla geçilir.

### Caption blueprint (English)

> **Maximum validation setting and reported validation methods in the 206-study corpus.** Panel (a) assigns each study to its single highest observed setting: simulation or numerical evidence (32), enhanced simulation or dataset-supported validation (18), laboratory experiment or proof of concept (78), controlled prototype (66), or field trial/deployment (12). Panel (b) reports overlapping methods, including analytical treatment (131), simulation (104), laboratory experiment (148), prototype/testbed validation (83), and field experiment (12). Thus, 156 studies reached at least a laboratory/PoC maximum tier, but only 12 reached field/deployment. Maximum tier is not a quality rank, method counts must not be summed, and neither panel establishes that communication and sensing were validated together under matched conditions.

### Evidence gate

- Panel (a) exact sum 32+18+78+66+12=206.
- `at least lab=78+66+12=156`.
- Panel (b) counts and percentages match S5 types CSV.
- `laboratory 148` is method count, `laboratory maximum 78` is exclusive tier; labels must not be swapped.
- TQAF validation score distribution 6/168/32 bu şekle üçüncü bar olarak eklenmez; FIG-OISAC-03'te kalır.
- Field 12, paired-function strongest score 6 ile eş anlamlı gösterilmez.

### Failure modes / do not do

- Pyramid veya staircase ile field'ı “best study” gibi göstermek.
- Panel (b) method counts'ı toplam %100 pie olarak çizmek.
- 156'yı field-ready diye yorumlamak.
- Field evidence'i paired-function field evidence sanmak.
- TQAF validation barını tekrar eklemek.

### COMST işlevsel örnekleri

- **COMST_060, Fig. 8:** “State of the art literature breakdown...” — `bibliometric_distribution`; corpus categories ve research trend'i tek yüksek-density grafikte görünür kılar.
- **COMST_069, Figs. 4–8:** survey evidence'nin farklı classification dimensions üzerindeki yüzde dağılımları; bir kategori haritasını prose'dan ayırma açısından analog. O-ISAC'ta exclusive ve multi-label paneller açık başlıklarla ayrılacaktır.
- **COMST_053, Fig. 10** (yakın-okuma `physical_mechanism`, Testbeds for 6G Channels): validation/testbed katmanlarının neden yalnızca sayı değil setting/contract açıklaması gerektirdiğine kavramsal analogdur.

## 10. FIG-OISAC-07 — Cross-Layer Technology-to-Application Evidence Chain

### Kimlik ve yerleşim

- **Dosya:** `11_TECHNOLOGIES_APPLICATIONS_6G.tex`
- **Section:** `ENABLING TECHNOLOGIES, APPLICATIONS, AND 6G POSITIONING`
- **Kesin yer:** Section açılış paragrafının “...physical observable to spatial control, inference, and operating need.” cümlesinden sonra; `\subsection{From Shared Samples to Physical Observables}` öncesi. Mevcut dosyada yaklaşık satır 11–13.

### Reader question

**How does an optical or photonic mechanism become a useful application claim, and what additional evidence is required before a 6G label can be interpreted as network readiness?**

### Tek cümlelik ana mesaj

**O-ISAC value emerges through a chain from generation and physical observables to spatial control, inference, and application requirements; a 6G label is only framing unless evidence remains continuous across that chain.**

### Görsel arketipi

Altı katmanlı, iki yönlü **cross-layer architecture-and-requirement map**. Sankey değildir; arrow widths count taşımaz. Solid arrows technical progression, dashed reverse arrows application requirements' feedback'ini gösterir.

### Katman ve içerik modeli

1. **Generation and transport**
   - photonic THz generation 68;
   - coherent optics 64;
   - photonic integration 20;
   - fiber DAS/infrastructure reuse 22;
   - source-specific other 19.
2. **Waveform and physical observables**
   - FMCW/chirped processing 66 → delay/Doppler/beat frequency;
   - OFDM/multicarrier 56 → pilots, payload, time–frequency resource;
   - phase/polarization/backscatter;
   - spatial/received-power/image observables.
3. **Spatial control and multiplicity**
   - beamforming 13;
   - OPA 11;
   - MIMO 7;
   - RIS/ORIS 2.
4. **Inference and system model**
   - ML/AI 20;
   - digital twin 2;
   - calibration, training distribution, uncertainty, compute/latency as boundary labels.
5. **Application requirement bundles**
   - network/access and mobility: 6G/access 100, optical access 32, vehicular 41;
   - persistent infrastructure/environment: environmental monitoring 55, smart infrastructure 41, industrial 34;
   - positioning/security/human-facing: indoor positioning 25, security 26, healthcare 8;
   - extreme/special environments: aerospace 20, underwater 2, datacenter 4, other 15.
   - Counts remain individual chips; bundles are reader organization and are not summed.
6. **6G/network-evidence gate**
   - direct relevance 138;
   - inferred 64;
   - weak 1;
   - not applicable 3;
   - gate conditions: end-to-end network role, timing/mobility/orchestration, energy/security/recovery, interoperability, paired-function evidence, validated service.
   - Output label: `6G framing ≠ conformance, interoperability, or deployment readiness`.

Reverse dashed arrows from layer 5/6 to earlier layers carry requirement labels: geometry/coverage; update rate/latency; safety/privacy; environment/maintenance; energy/dynamic range; calibration/recovery.

### Değişken, eksen ve kodlama

- Nicel axis yoktur. Counts uniform small badges; node size prevalence ile değişmez.
- Katmanlar soldan sağa teknik chain sırasındadır; chronology veya maturity değildir.
- Solid arrows “technical dependency/observable path”; dashed reverse arrows “requirement feedback”. Legend bunu açıklar.
- Interface boundaries (optical→RF conversion, physical→inference, subsystem→network) dikey kesik çizgilerle işaretlenir.
- 6G relevance categories exclusive ve sum=206; teknoloji ve application labels multi-label.

### Etiket, legend ve renk

- Physical generation: mavi; observable/waveform: teal; spatial: purple; inference: orange; requirements: neutral/gold; evidence gate: dark blue outline.
- Badge area sabit; `n=` prefix tüm ampirik count'larda kullanılır.
- Application bundles kendi subtotal'larını göstermemelidir.
- Her katmanın altında bir boundary phrase: `power/phase`, `plane/definition`, `geometry/calibration`, `shift/cost`, `mission constraints`, `network proof`.

### Annotation ve belirsizlik

- Ana zincir üzerinde üç kırılma callout'u: `conversion/interface`, `calibration/ground truth`, `application/network continuity`.
- Multi-label banner: `Technology and application counts overlap; arrows do not encode co-occurrence or causal effect.`
- Direct/inferred 6G relevance sınıfları source framing'dir; readiness probability değildir.
- Confidence interval yoktur.

### Boyut

- `figure*`, 7.16 in × 4.0–4.6 in; aspect 1.55–1.8.
- Çok sayıda chip nedeniyle final-size 100% preview zorunludur; gerekirse “other” ve düşük-count labels caption'a taşınabilir, fakat authoritative source listede kalmalıdır.

### Uygulama rotası

- Özgün SVG/TikZ veya Python `matplotlib.patches`; automatic Sankey/NetworkX force layout kullanılmaz.
- Data source files S6 technologies, S6 applications ve S7 relevance ayrı okunmalı; count badges script ile üretilmelidir.
- Conceptual requirement bundles ayrı bir versioned mapping CSV'de tutulmalı ve “reviewer synthesis, non-exclusive” olarak işaretlenmelidir.

### Veri ve otorite

- `09_kayitlar/checkpoints/synthesis_PHASE_F_FINAL_2026-08-04/s6_enabling_technologies.csv`.
- `.../s6_application_domains.csv`.
- `.../s7_six_g_relevance.csv`.
- Aktif Section 11 ve cited representative studies.
- Denominator: technology/application counts are multi-label among 206; S7 relevance is mutually exclusive among 206.

### Önerilen İngilizce lead-in

> Figure X organizes the section as a cross-layer evidence chain rather than as a list of technologies and markets. It follows the route from generation and observable formation through spatial control and inference to application requirements, while the reverse arrows show how operating needs constrain every earlier layer.

### Şekil sonrası paragrafın görevi

Metin, tek bir çalışmanın birden çok teknoloji node'una sahip olabileceğini ve application labels'in architecture olmadığını açıklamalıdır. Sonra ilk alt bölüme geçiş: shared samples ve observables chain'in başlangıcıdır. Section sonunda şekle dönülerek 6G gate'in standard compliance/readiness olmadığını hatırlatmak gerekir.

### Caption blueprint (English)

> **Cross-layer organization of O-ISAC enabling technologies, observables, application requirements, and 6G evidence.** Generation and transport mechanisms create or preserve physical observables; waveform and spatial-control technologies determine how those observables are shared; inference converts them into estimates or decisions; and application requirements feed geometry, latency, safety, environment, energy, and calibration constraints back into the system. Technology and application labels are multi-label and their badges report overlapping study coverage, not causal influence or technical rank. The final gate separates direct, inferred, weak, and not-applicable 6G relevance (138/64/1/3 studies) from the additional evidence needed for conformance, interoperability, paired-function operation, and deployment readiness.

### Evidence gate

- Technology counts exactly match S6 technology CSV.
- Application counts exactly match S6 application CSV; bundle subtotals üretilmez.
- 138+64+1+3=206.
- Technology/application arrows co-occurrence veya causal effect gibi kalınlaştırılmaz.
- Photonics-assisted THz path üzerinde radiated segment RF olarak açık boundary alır.
- `direct 6G relevance` readiness veya compliance olarak etiketlenmez.
- Requirement bundles planlı application–requirement table ile tutarlı olmalıdır.

### Failure modes / do not do

- Sankey width ile uydurma study flow üretmek.
- Technology counts'ı exclusive market share olarak göstermek.
- 6G direct count'u deployment readiness olarak sunmak.
- Application labels'i architecture veya modality sınıfı yapmak.
- Çok sayıda telifli icon/fotoğraf kullanmak.
- Okları nedensellik kanıtı gibi yorumlamak.

### COMST işlevsel örnekleri

- **COMST_053, Fig. 6:** “Potential 6G application scenarios.” — `application_map`; teknik kabiliyetleri application space'e bağlama işlevi bakımından analogdur.
- **COMST_053, Fig. 8:** “A novel promising 6G network architecture...” — `system_architecture`; subsystem-to-network chain kurduğu için analogdur.
- **COMST_053, Fig. 9:** “Potential 6G key technologies.” — taxonomy/application map işlevi; teknoloji envanterini offload eder. O-ISAC şekli bunun ötesinde requirement feedback ve evidence gate ekler.
- **COMST_060, Fig. 5:** RIS-assisted localization applications map — `application_map`; use-case labels ile technical mechanism arasında görsel köprü kurar.

## 10. Bölüm-bölüm şekil kararı ve tablo arayüzü

| Manuscript section | Figure decision | Tabloyla iş bölümü |
|---|---|---|
| Introduction | Yeni şekil yok | Related-survey table ve FIG-OISAC-01 tekrarını önler |
| Related Surveys and Scope | Şekil yok | Related-survey matrix scope/gap'i taşır |
| Foundations and Comparison Framework | FIG-OISAC-01 | Comparison-record table exact field dictionary; şekil conceptual logic |
| Review Methods | Ayrı yöntem şekli yok | PRISMA akışı sonuçlarda FIG-OISAC-02; method prose governance'ı açıklar |
| Corpus and Appraisal Results | FIG-OISAC-02 + FIG-OISAC-03 | Claim-disposition table extraction units'i taşır; figures selection + appraisal pattern |
| Optical Modality Families | Ayrı count grafiği yok | Modality table counts, physical roles, representative studies |
| Integration Architectures | FIG-OISAC-04 | Şekil coupling location/overlap; prose mechanisms/examples |
| Metrics and Comparison Logic | Ayrı grafik yok | Metric-contract table definitions/planes; ortak value plot yasak |
| Communication–Sensing Trade-offs | FIG-OISAC-05 | Şekil family profile; study-level inventories gerektiğinde supplement/data |
| Validation and Reproducibility | FIG-OISAC-06 | Artifact table data/code/reconstructability |
| Technologies, Applications, 6G | FIG-OISAC-07 | Application–requirement table exact requirement axes and representative evidence |
| Discussion/Roadmap/Limitations | Ayrı roadmap şekli yok | Roadmap table traceable gap→action→test→success→dependency |
| Conclusion | Yeni görsel yok | Sonuç görsel eklemeden ana mesajı toplar |

## 11. Üretim öncesi ortak QA checklist

Her şekil için “implemented” durumu ancak aşağıdaki maddeler PASS ise verilebilir:

1. Exact reader question ve one-sentence message caption/prose ile uyumlu.
2. Source CSV ve denominator tanımlı.
3. Reconciliation assertions PASS.
4. Figure/table overlap audit yapıldı; aynı okuyucu işi iki görsel yapmıyor.
5. Lead-in şekilden önce; interpretation şekilden sonra.
6. Caption denominator, multi-label/exclusive status ve inference boundary içeriyor.
7. Final IEEE width'te tüm etiketler ≥8 pt ve kesilmemiş.
8. Colorblind ve grayscale test PASS.
9. PDF/SVG text selectable veya fontlar embedded.
10. Figure values manuscript prose ve authoritative synthesis files ile birebir.
11. No digitization, no derived performance value, no unsupported causal arrow.
12. Alt text/accessible text ana mesajı ve kritik sayıları taşıyor.
13. Source code, input CSV, output PDF/SVG ve hash/provenance birlikte arşivlenmiş.
14. Manuscript cross-reference ve caption numbering final LaTeX aşamasında doğrulanmış.

## 12. Son editoryal hüküm

Bu görsel mimari survey'i “daha resimli” yapmak için değil, prose'un taşıyamadığı yedi farklı bilişsel işi dışsallaştırmak için tasarlandı:

- çerçeveyi öğretmek;
- denominator akışını denetlenebilir yapmak;
- appraisal çelişkisini görünür kılmak;
- coupling location'ları ayırmak;
- trade-off evidence'ı frontier üretmeden özetlemek;
- validation'ın exclusive ve multi-label görünümlerini ayırmak;
- teknoloji iddiasını application ve 6G evidence gate'e bağlamak.

Bu yedi işten birini karşılamayan yeni şekil eklenmemelidir. Görsel üretim aşamasında yapılacak ilk iş çizim değil, her şeklin source-data CSV'sini ve reconciliation testini dondurmak olmalıdır.
