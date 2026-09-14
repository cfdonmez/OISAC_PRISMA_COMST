# Full Introduction Audit — Group C (COMST_053–COMST_077)

## Kapsam ve okuma yöntemi

Bu rapor, yerel COMST korpusundaki **COMST_053–COMST_077 aralığının tamamını (25/25 makale)** kapsar. Her dosyada `I. INTRODUCTION` başlığından sonraki ana numaralı bölüme kadar olan metin okunmuştur. İnceleme yalnızca cümle uzunluğu veya bağlaç sayımı yapmaz; her girişin paragraf işlevlerini, düşünsel geçişlerini, related-work/gap kurulumunu, katkı vaadini, organizasyon geçişini, tonunu ve ritmini nitel olarak çıkarır.

Yerel Markdown dosyaları PDF'den dönüştürülmüştür. Bu nedenle bazı çift sütunlu sayfalarda tablo, şekil açıklaması, yazar bilgisi veya dipnot ana metnin arasına girmiştir. Bu parçalar metinsel sıraya göre yeniden birleştirilerek okunmuştur. Özellikle COMST_053'ün organizasyon paragrafının sonu dönüşümde kayıptır; COMST_061'de kısaltma tablosu ilk paragrafın ortasına girmiştir; COMST_075'te related-work tablosu metni ikiye ayırmıştır. Bu sorunlar aşağıda ayrıca belirtilmiştir. Bunlar içerik analizini büyük ölçüde engellememiş, fakat kayıp metin bulunan yerde çıkarım yapılmamıştır.

## Makale bazında anlatı reçeteleri

### COMST_053 — On the Road to 6G: Visions, Requirements, Key Technologies, and Testbeds

- **İşlev dizisi:** Hücresel kuşakların evrimi ve 5G'nin mevcut kapasitesi → 5G'nin karşılayamadığı gereksinimlerin ayrıntılı dökümü → ülkeler, kurumlar, projeler ve white paper'lar üzerinden 6G hareketliliği → mevcut 6G survey alanı → bu survey'in vizyon, KPI, mimari, teknoloji ve testbed katkıları → bölüm yol haritası.
- **Geçiş, ton ve ritim:** Genişten daha da genişe giden ansiklopedik bir ritim vardır. “Although 5G…”, “To address…”, “The above plans…” ve “With the rapid development…” türü geçişler kronoloji ile problem–yanıt bağını kurar. Ton otoriter ve kapsam iddiası yüksek; paragraflar uzun ve isim/kaynak yoğun.
- **Related work ve gap:** Literatür, tek tek teknik sonuçlardan çok kurumsal ve coğrafi hareketlilik olarak sunulur; karşılaştırma tablosu kapsam farklılıklarını taşır. Boşluk, tüm 6G anlayışını tek çatı altında güncellemek ve özellikle testbed/verification platformlarını birlikte incelemek olarak kurulur. Gap, kısa bir eksiklik cümlesinden ziyade kapsama dayalı farklaştırmadır.
- **Katkı ve organizasyon:** Dört maddelik katkı listesi vizyon, mimari/teknoloji, testbed ve açık sorunları eşler. Sonraki paragraf yalnız bir içindekiler listesi vermek yerine “state of the art → knowledge gaps → trade-offs → research avenues” sentez mantığını da açıklar; bu güçlüdür. Ancak kurum ve white-paper envanteri Introduction'ı ağırlaştırır. Markdown dönüşümü organizasyon paragrafının son kısmını kaybetmiştir.

### COMST_054 — Optical Wireless Communication in Atmosphere and Underwater

- **İşlev dizisi:** 6G hedefleri → OWC'nin RF'yi tamamlayan rolü → LiFi, FSO ve underwater OWC'nin ortam-temelli örnekleri → LoS, çevre ve hizalama sınırlamaları → istatistiksel kanal modellemenin neden gerekli olduğu → erken teknik çalışmalar → mevcut review kümeleri → çapraz-ortam modelleme boşluğu → kapsam ve bölüm yolu.
- **Geçiş, ton ve ritim:** “At present”, “In outdoor scenarios”, “however”, “To comprehensively understand” ve “Given the growing importance… However…” ifadeleri alanı kademeli daraltır. Ton teknik ve açıklayıcıdır; bazı cümleler dilbilgisel olarak pürüzlü olsa da problem zinciri izlenebilir.
- **Related work ve gap:** Review'ler VLC/LiFi, uygulama-özel VLC, genel OWC, underwater OWC ve FSO olarak işlevsel kümelere ayrılır. Gap yalnız “yeni survey yok” değildir: farklı ortamların istatistiksel modellerinin hangi fiziksel olguyu, hangi koşulda temsil ettiğini bir araya getiren çapraz-alan karşılaştırmasının eksikliği gösterilir. Bu, güçlü bir karşılaştırma eksenidir.
- **Katkı ve organizasyon:** Katkı vaadi atmosferik, underwater, aerial ve space OWC'yi ortak fiziksel bozulmalar, aktarılabilir mitigation yöntemleri ve performans metrikleri üzerinden bağlamaktır. Organizasyon paragrafı teori → sınırlamalar → deneyler → kanal modelleri → iyileştirme teknikleri → aktif araştırma → gelecek yönleri şeklinde mantıksal bir omurga sunar. “İlk comprehensive survey” iddiası ve aynı “up-to-date/comprehensive” fikrinin tekrarı daha az aktarılabilir kalıplardır.

### COMST_055 — Post-Quantum Blockchain Security for the Internet of Things

- **İşlev dizisi:** IoT kullanım alanları → ölçek büyümesi ve güvenlik açığı → merkezi bulut mimarisinin tek-nokta riskleri → blockchain'in dağıtık güven modeli → kuantum algoritmalarının mevcut zincirlere tehdidi → post-quantum blockchain gereği ve uygulama zorlukları → survey amacı → organizasyon.
- **Geçiş, ton ve ritim:** Giriş kısa bir neden-sonuç merdiveni kurar. “Such extensive acceptance…”, “Although…”, “This is because…”, “Thus…” ve “However…” ifadeleri her paragrafın bir öncekinin sonucundan başlamasını sağlar. Ton sade ve öğreticidir; teknik ayrıntı yalnız gereksinimi kuracak kadar verilir.
- **Related work ve gap:** Related surveys ana Introduction içinde karşılaştırılmaz; bu işlev doğrudan Section II'ye ertelenmiştir. Intro'daki gap, blockchain-IoT güvenliğinin kuantum tehdidi karşısında yeniden ele alınması ve bu entegrasyonun yöntem/zorluklarının sentezlenmesi olarak ima edilir.
- **Katkı ve organizasyon:** Ayrı bir madde listesi yerine amaç paragrafı post-quantum primitives, blockchain-IoT katmanları, PQB kurma yöntemleri ve açık sorunları sıralar. Organizasyon paragrafı kapsamlı fakat uzundur; her bölümün birden fazla işlevini ayrıntılı sayması ritmi düşürür. Güçlü yön, problem zincirinin yalınlığıdır.

### COMST_056 — Precoding for High-Throughput Satellite Communication Systems

- **İşlev dizisi:** Broadband erişim ve kapsama ihtiyacı → GEO/LEO/MEO constellation değişimi → on-board processing ilerlemesi → multi-beam mimarinin kaynak yeniden kullanımı ve girişim bedeli → precoding'in doğal odak haline gelmesi → terrestrial ve satellite precoding survey'lerinin karşılaştırılması → 2010 sonrası güncel sentez ihtiyacı → iki perspektifli taxonomy → organizasyon.
- **Geçiş, ton ve ritim:** “In this context”, “In addition”, “Another significant milestone”, “However” ve “Therefore” bağları yeni konuyu önceki darboğazdan üretir. Ton ölçülü, teknik ve kendinden emindir. Her paragraf tek bir mimari dönüşüm veya karşılaştırma işlevi taşır.
- **Related work ve gap:** Önce genel MIMO/precoding survey'leri, sonra genel SatCom survey'i, ardından eski satellite-precoding survey'i ele alınır. Gap açıkça iki boyutludur: genel survey'ler precoding'e yeterince derin inmez; özel survey ise 2010 sonrasındaki büyük literatür artışını kapsamaz.
- **Katkı ve organizasyon:** Katkı, “daha kapsamlıyız” yerine problem formulation (group/objective/level) ve system design (architecture/implementation/service) şeklindeki iki eksenli sınıflandırmaya bağlanır; ayrıca impairments ve robust precoding'i korur. Organizasyon kısa ve sınıflandırmayla hizalıdır. Bu grup içindeki en aktarılabilir teknik Introduction modellerinden biridir.

### COMST_057 — RIS-Enabled Backscatter Communication

- **İşlev dizisi:** 6G'nin düşük güç ve kitlesel bağlantı gerilimi → BackCom'un enerji avantajı fakat çift-yol zayıflaması → RIS'in uyumluluğu → IoT ölçeği, teknik çözümler ve kullanım senaryoları → pratik sorunların dağınık literatürü → RIS-helper ile RIS-sender ayrımı üzerinden survey boşluğu → katkılar → organizasyon.
- **Geçiş, ton ve ritim:** Problem–çözüm dönüşleri sık kullanılır: “However”, “Thus”, “To tackle this problem”, “On the other hand”, “Nonetheless” ve “In this context”. Ton enerjik ve ileriye dönüktür. Fakat uzun uygulama örnekleri ve yayın-yayın related-work anlatımı ritmi ansiklopedik hale getirir.
- **Related work ve gap:** Mevcut çalışmalar BackCom, RIS-assisted BackCom, AI-enabled BackCom ve RIS-as-sender işlevlerine göre karşılaştırılır. En değerli gap, terminolojik/işlevsel ayrımdır: RIS'in yalnız iletime yardım etmesi ile bizzat backscatter sender olması aynı şey değildir; önceki survey'ler bu ayrımı ve modulation/channel-estimation/optimization zincirini birlikte yeterince ele almaz.
- **Katkı ve organizasyon:** Katkılar principles/classification, modulation/performance, channel estimation, optimization, emerging uses ve practical challenges'a bağlanır. İyi bir içerik sözleşmesi vardır; ancak beş uzun madde Introduction'ı ikinci bir outline'a dönüştürür. Organizasyon paragrafında bölüm numarası hatası olabilecek “Based on Section VII, Section V” ifadesi de kaynak metinde vardır.

### COMST_058 — Quantum AI-Enhanced IoT-Fog Communication

- **İşlev dizisi:** IoT'nin geniş saldırı yüzeyi → 6G veri gizliliği baskısı → survey kapsamının erken ilanı → evolving threat landscape → kritik altyapı ve IoT-fog mimarisi → quantum AI vaatleri → kuantum hesaplamanın uzun temel anlatımı → objectives/scope listesi → organizasyon.
- **Geçiş, ton ve ritim:** “As a result”, “Nonetheless”, “However” ve “Furthermore” ile ilerler; fakat birçok paragraf aynı “acil güvenlik ihtiyacı/Quantum AI vaadi” fikrini yeniden kurar. Ton yüksek iddialı, genel ve yer yer tanıtım metni gibidir. Dilbilgisi ve özne-yüklem sorunları ritmi zayıflatır.
- **Related work ve gap:** Bir karşılaştırma tablosuna atıf yapılır, ancak Introduction içindeki prose gap diğer örneklere göre daha zayıftır. Eksiklik, Quantum AI tabanlı threat mitigation ve post-quantum güvenliğin yeterince derin ele alınmaması olarak ifade edilir; bunun nasıl ölçüldüğü anlatı içinde yeterince belirgin değildir.
- **Katkı ve organizasyon:** Hedefler detection, privacy, IDS, protocol threats, monitoring ve resilience olarak açıkça listelenir. Fakat survey'in özgün sentez ekseni ile genel konu kapsamı birbirine karışır. Uzun quantum-computing primer'ının Introduction içinde yer alması, arka planı ana bölümlere bırakmayan zayıf bir kalıptır.

### COMST_059 — Rate-Splitting Multiple Access

- **İşlev dizisi:** 6G'de interference-management ihtiyacı → OMA–SDMA–NOMA evrimi → RSMA'nın partial decode/partial treat-as-noise ilkesi → oyuncak örnek → mevcut MA ailelerinin avantaj/sınırlamaları → asıl problemin orthogonality değil interference treatment olduğunun sentezi → imperfect-CSIT darboğazı → üç motive edici soru → RSMA yanıtı → survey gap ve katkılar → organizasyon.
- **Geçiş, ton ve ritim:** Uzun olmasına rağmen öğretici bir argüman ritmi vardır. “In contrast”, “To further enhance”, “Comparing…”, “The aforementioned disadvantages…”, “Unfortunately…” ve “On account of…” bağları yalnız metin eklemez, çıkarım yapar. Kısa “Next…” ve soru–yanıt geçişleri yoğun teknik blokları nefeslendirir.
- **Related work ve gap:** Introduction yayın-yayın survey dökümü yapmaz. Gap, RSMA çalışmalarının dar senaryolara dağılması, neden/nasıl/ne zaman yararlı olduğuna ilişkin pedagojik ve bütüncül tutorial eksikliği ve literatürde konsensüs bulunmaması üzerinden kurulur.
- **Katkı ve organizasyon:** Katkılar principles/frameworks, theory milestones, precoder design, PHY architecture, comparative simulations, applications ve standardization olarak gap'e cevap verir. “Why/how/when” üçlüsü güçlü bir yazar-okuyucu sözleşmesidir. Grup içinde düşünsel akışı en güçlü örneklerden biridir; tek zayıflık Introduction'ın bazı background bölümlerini kendi içine alarak çok uzamasıdır.

### COMST_060 — RIS in 6G Radio Localization

- **İşlev dizisi:** RIS'in elektromanyetik yeniden programlanabilirliği → localization için anchor/deployment avantajı → ilgili survey'leri signal, environment, technique ve application eksenlerinde kümeleme → dar kapsam, güncellik ve reproducibility açıkları → yeni survey ihtiyacı → üç research question → search/inclusion yöntemi → özgün katkılar → sonuç bölümlerine geçiş.
- **Geçiş, ton ve ritim:** “This feature makes…”, “Moreover”, “While research…”, “However” ve “To develop the understanding…” ifadeleri teknik özellikten review gereğine gider. Ton sistematik, delile ve yeniden üretilebilirliğe duyarlı; uzun related-work paragrafı dışında kontrollüdür.
- **Related work ve gap:** Önceki survey'ler neye göre sınıflandırıldığını açıkça gösterir; yalnız tek tek kaynak özeti değildir. Gap, RIS-assisted localization'ın bütün spektrumunu, güncel çalışmaları ve yeniden üretilebilir yöntemi aynı çerçevede taşımayan review'lerdir. Üç araştırma sorusu gap'i doğrudan inceleme görevlerine çevirir.
- **Katkı ve organizasyon:** Katkılar araştırma sorularına ve bölümlere eşlenir; review method Introduction içinde görünür kılınır. Bu, systematic-review niteliği olan bir COMST girişinin güçlü örneğidir. Zayıf yönü, kaynak kümelerinin tek paragrafta aşırı yoğunlaşmasıdır.

### COMST_061 — RIS-Assisted Physical Layer Security in RF and Optical Wireless Systems

- **İşlev dizisi:** 5G kapasite sınırı ve 6G gereksinimleri → broadcast ortamında bilgi sızıntısı → cryptography'nin resource/key-management sınırları → PLS'in gerekçesi → klasik PLS yöntemlerinin maliyeti → RIS'in channel-control avantajı → yüksek frekanslı RF ve optical sistemlerde ortak ihtiyaç → ilgili survey'ler → RF ve OWC'yi birlikte ele alan bilgi-teorik güvenlik boşluğu → katkılar → organizasyon.
- **Geçiş, ton ve ritim:** “Although”, “To deal with”, “However”, “To overcome”, “The advancement…”, “To fully implement…” ve “Consequently” zinciri sağlamdır. Her çözüm, önce kendi sınırlaması gösterildikten sonra bir sonraki teknik katmana bağlanır. Ton resmi, teknik ve temkinli; yoğun fakat amaçlıdır.
- **Related work ve gap:** Survey'ler önce genel RIS/6G entegrasyonu, sonra RIS-assisted PLS olarak iki katmanda incelenir. Ortak eksiklik iki cümlede sentezlenir: çoğu RF odaklıdır ve information-theoretic security kısmen ele alınır; optical taraf çoğunlukla kısa geçilir. Gap böylece alan, yöntem ve derinlik boyutlarına sahiptir.
- **Katkı ve organizasyon:** RF-PLS, OWC-PLS, optimization, ML, performance, application/challenge başlıkları gap'in parçalarına karşılık gelir. Katkı listesi uzundur ama teknik işlevlere ayrıldığı için salt içindekiler listesi değildir. O-ISAC için çapraz-modality anlatısına yakın, güçlü bir örnektir.

### COMST_062 — RIS-Empowered Satellite–Aerial–Terrestrial Networks With PD-NOMA

- **İşlev dizisi:** Global seamless connectivity ihtiyacı → SATN'nin katmanlı üstünlükleri → fading, connectivity, interference, power, security ve hardware zorlukları → OMA/SDMA sınırları ve NOMA ihtiyacı → RIS'in enerji/channel-control rolü → NOMA–RIS karşılıklı tamamlayıcılığı → survey literatürü → entegrasyon boşluğu → altı katkı → organizasyon.
- **Geçiş, ton ve ritim:** “However”, “Therefore”, “Furthermore”, “On the other hand”, “Although” ve “Notably” ile bileşenler birbirine bağlanır. Ton teknik ve kapsamlıdır; fakat uzun zorluk/teknoloji listeleri ve “In this survey, we focus on PD-NOMA” cümlesinin art arda tekrarlanması akışı mekanikleştirir.
- **Related work ve gap:** İlgili survey'ler RIS, SATN, NOMA-RIS, NTN ve beamforming odaklarına göre anlatılır. Gap, üçlü NOMA–RIS–SATN birleşiminin foundations, performance, resource allocation, security, complementary technologies ve implementation issues ile birlikte incelenmemesidir.
- **Katkı ve organizasyon:** Katkılar entegrasyon bileşenlerine ayrılmıştır ve case study içerir. Çok sayıda kapsam başlığını Introduction'da sıralamak “kapsam = özgünlük” izlenimi yaratır; bu daha zayıf bir COMST kalıbıdır. Güçlü taraf, NOMA ile RIS'in yalnız avantaj toplamı değil, karşılıklı telafi mekanizması olduğunu açıklamasıdır.

### COMST_063 — Seamless Connectivity: Integrating PLC and Wireless Communications

- **İşlev dizisi:** “Wired-wireless”ın tarihsel kökeni → PLC'nin uygulama ve standardizasyon evrimi → spektrum ve connectivity baskısı → PLC'nin WLC/VLC/optical/DSL ile entegrasyonu → tek teknolojinin coverage/throughput/reliability gereksinimini sürekli karşılayamaması → hybrid sistem motivasyonu → survey kümeleri ve boşluk → katkılar → organizasyon.
- **Geçiş, ton ve ritim:** Tarihsel açılış konuya karakter verir. “Well into the 21st Century”, “To meet these demands”, “In this regard”, “The common denominator…” ve “Indeed” geçişleri geçmişi güncel tasarım sorununa bağlar. Ton akademik ama canlı; ortak mühendislik gerekçesi açıkça formüle edilir.
- **Related work ve gap:** Literatür PLC, WLC ve hybrid communication olmak üzere üç kümeye ayrılır; sayıca bol WLC review'leri ile sınırlı hybrid review'leri karşılaştırılır. Gap; PLC–WLC hybrid türlerinin tarihsel evrimini, teknik tasarımını, industrial/standardization gelişmelerini ve nitel karşılaştırmasını birlikte veren çalışma olmamasıdır.
- **Katkı ve organizasyon:** Katkılar ayrı teknolojilerin strengths/weaknesses'ından üç hybrid tipe, design approaches'a, qualitative comparison'a, lessons learned ve roadmap'e ilerler. Bu sıra, makalenin sentez mantığını gösterir. Uzun katkı listesine rağmen her madde aynı taxonomy'nin sonraki adımıdır; güçlü bir bütünlük vardır.

### COMST_064 — Security and Privacy on 6G Network Edge

- **İşlev dizisi:** 6G trafik/latency ölçeği → edge computing ve caching'in gereği → edge intelligence'ın yükselişi → ML'in yeni saldırı ve privacy yüzeyi → edge'in avantajlarına rağmen kalan tehditler → mevcut countermeasures → üç edge paradigmasını ortak güvenlik bağlamında inceleme → trade-off kapsamı → katkılar → organizasyon.
- **Geçiş, ton ve ritim:** “To meet…”, “Another important paradigm…”, “On the other hand…”, “It can be found…” ve “However…” ile hizmet ihtiyacından güvenlik çelişkisine geçilir. Ton açık ve veri-odaklıdır; sık “And” başlangıçları ile rakamsal gelecek tahminleri dili zaman zaman mekanik kılar.
- **Related work ve gap:** Existing-survey karşılaştırması Introduction içinde yapılmaz; Section II'nin açık görevidir. Intro, edge computing/caching/intelligence'ın korelasyonuna dayanarak birleşik kapsamın gereğini kurar. Gap'in önceki review'lere göre tam farkı bu nedenle bir sonraki bölüme ertelenir.
- **Katkı ve organizasyon:** Katkılar üç paradigmanın ilişkisi, security/privacy threats, O-RAN/FL/blockchain ve 6G için future limitations'ı kapsar. Organizasyon paragrafı yöntemsel olmayan klasik bölüm dökümüdür. Güçlü yön, güvenlik–QoS–enerji trade-off'unu survey kapsamına erken almasıdır.

### COMST_065 — Semantics-Empowered Space–Air–Ground–Sea Integrated Network

- **İşlev dizisi:** 6G ubiquitous-connectivity hedefi → SAGSIN gereği → büyük mesafe, dinamik kanal ve sınırlı cihaz kapasitesi → bit-perfect iletişimin task-oriented uygulamalarda gereksiz/maliyetli oluşu → semantic communications'a paradigma geçişi → üç araştırma sorusu → semantics'in significance/meaning/effectiveness yorumları → PCCAIP çerçevesi → SAGSIN ve semantic survey'lerini ayrı ayrı inceleme → kesişim boşluğu → katkılar → organizasyon.
- **Geçiş, ton ve ritim:** “However”, “On the other hand”, “Moreover”, “Therefore” ve örneklerle kurulan çıkarım zinciri güçlüdür. Üç soru, uzun girişe yön duygusu verir. Ton kavramsal, pedagojik ve iddialıdır; yeni çerçeveyi yalnız isimlendirmekle kalmaz, neden üç bileşene ihtiyaç duyulduğunu açıklar.
- **Related work ve gap:** İki literatür ailesi ayrı alt başlıklarda işlenir. SAGSIN survey'leri traditional/bit-level communication'a; semantic survey'leri ise tek semantic yoruma veya genel terrestrial senaryolara odaklanır. Gap bu iki alanın kesişiminde, dynamic channel/resource/security/task koşullarını ortak paradigma ile ele almaktır.
- **Katkı ve organizasyon:** PCCAIP, significance-protection, meaning-enhancement ve effectiveness-yielding katmanları contributions ve ana bölümlerle bire bir hizalıdır. Bu, özgün taxonomy'nin Introduction omurgası olabileceğini gösteren güçlü bir örnektir. Dezavantajı, Introduction'ın bazı temel/taksonomi içeriğini fazla ayrıntılı taşımasıdır.

### COMST_066 — Spectrum Sharing and Interference Management for 6G LEO Satellite–Terrestrial Integration

- **İşlev dizisi:** Terrestrial coverage ile satellite reach'in tamamlayıcılığı → LITNet entegrasyonu → artan terminal/satellite sayısıyla spectrum scarcity ve interference → ITU/coexistence bağlamı ve sistem kısıtları → ele alınacak interference türleri → önceki survey'ler → tüm mekanizmaları kapsayan sınıflandırma boşluğu → kapsam sınırı → katkılar → şekil tabanlı yapı geçişi.
- **Geçiş, ton ve ritim:** “While…Conversely…Consequently…” açılışı dengeli bir karşıtlık kurar. “Despite…”, “In light of…”, “However, a notable gap remains” ve “Additionally…” anlatıyı alan tanımından gap'e götürür. Ton doğrudan ve teknik; bazı fikirler spectrum scarcity çevresinde tekrarlanır.
- **Related work ve gap:** Kaynaklar database coexistence, resource allocation, LEO connectivity, general SatCom, mitigation, ISI ve MIMO gibi kapsamlarına göre tek tek özetlenir. Gap sonradan üç açık sınıfa sıkıştırılır: IBI, ISI ve LTI'nin oluşum mekanizmalarını ve mitigation'ını aynı LITNet çerçevesinde sistematik sınıflandıran survey yoktur.
- **Katkı ve organizasyon:** Fundamentals → tüm interference scenarios → IBI → ISI → LTI → AI/LLM → research challenges dizisi taxonomy ile tutarlıdır. Organizasyon bir bölüm-paragrafı yerine figüre bırakılmıştır; bu, ayrıntılı katkı listesinden sonra tekrarı azaltır.

### COMST_067 — Terahertz Communications and Sensing for 6G and Beyond

- **İşlev dizisi:** 6G/IMT-2030 bağlamı → ISAC kullanım senaryosuna daralma → “6G neden THz'ye ihtiyaç duyar?” temel sorusu → communications açısından alt-6/mmWave/optical karşılaştırması → sensing avantajları → sensing-aided communication ve communication-aided sensing sinerjisi → THz survey landscape → holistic/6G/sensing boşluğu → kapsamlı katkılar → şekil tabanlı yapı.
- **Geçiş, ton ve ritim:** En güçlü kırılma, teknik ayrıntıdan önce sorulan temel sorudur. “In what follows”, “Prior to stepping into…”, “Based on these considerations”, “On the other hand” ve “Therefore” ifadeleri karşılaştırmayı yönlendirir. Ton tutorial-otoriter; uzun listeler arasında kısa tez cümleleri ritim sağlar.
- **Related work ve gap:** Mevcut survey'ler antenna, propagation, measurement, channel modeling, beamforming ve hardware gibi tek teknik boyutlarda derin; magazine yazıları geniş ama sığ olarak konumlandırılır. Ek iki açık: sensing'in ihmal edilmesi ve 6G'ye özgü demand/scenario bağlamının eksikliği. Bu üçlü gap oldukça nettir.
- **Katkı ve organizasyon:** Katkılar band karşılaştırmasından trials/testbeds'e kadar ondan fazla maddeye yayılır. İçerik zenginliği görünür olsa da liste çok uzundur ve Introduction'ı kataloglaştırır. Güçlü aktarılabilir özellik, communications ve sensing'i iki paralel konu olarak değil, iki yönlü yardım ilişkisiyle bağlamasıdır.

### COMST_068 — Toward 6G Optical Fronthaul

- **İşlev dizisi:** Pandemi sonrası trafik ve connectivity büyümesi → mobil kuşak evrimi → 5G service families → 6G use-case kataloğu → O-RAN dönüşümü → fronthaul'un kritik darboğaz olması → wireless ve optical seçeneklerin karşılaştırılması → survey scope → eski/dağınık review boşluğu → organizasyon.
- **Geçiş, ton ve ritim:** Alan çok geniş açılır ve ancak geç aşamada fronthaul'a daralır. “While 5G…”, “Moreover, this shift…”, “In the dynamic evolution…”, “In contrast…” ve “We have chosen…” geçişleri vardır. Ton tanıtıcı ve yer yer promosyoneldir; uzun 6G uygulama listesi ana soruna gelmeyi geciktirir.
- **Related work ve gap:** İlgili review'ler 5G wireless backhaul veya genel optical communications ekseninde konumlandırılır; güncel 5G/6G fronthaul achievements ve özellikle 6G optical fronthaul'a ayrılmış derinlik eksiktir. Ayrıntılı karşılaştırma Section II'ye bırakılır.
- **Katkı ve organizasyon:** Scope paragrafı evolution, split options, optical technologies, research efforts ve challenges sırasını verir. “Up-to-date” fikri art arda tekrarlanır; özgün sentez ekseninin “güncellik ve genişlik” ötesinde daha keskin kurulması gerekirdi. Optical–wireless karşıtlığının fronthaul gereksinimlerine bağlanması güçlüdür.

### COMST_069 — Resource Allocation for PLC Systems

- **İşlev dizisi:** PLC'nin tarihsel olgunluğu → elektrik altyapısının iletişim için sert kanal olması → impedance, attenuation, EMI, impulsive noise vb. kaynak kısıtları → resource allocation'ın zorunlu hale gelmesi → RA ve PLC survey aileleri → kesişim boşluğu → tek eski RA-for-PLC review ile fark → link/PHY scope sınırı → taxonomy ve chronological synthesis katkıları → organizasyon.
- **Geçiş, ton ve ritim:** “Consequently”, “Ultimately”, “Considering…”, “In order to illustrate…”, “Tables reveal, however…” ve “Although…” geçişleri fiziksel kanaldan literatür boşluğuna kesintisiz gider. Ton olgun, teknik ve ölçülüdür; Introduction'ın her parçası aynı “harsh medium → resource management” tezini besler.
- **Related work ve gap:** Review'ler önce RA-genel ve PLC-genel olarak iki kümeye ayrılır; sonra aralarındaki boşluk gösterilir. Bir istisna çalışma açıkça kabul edilir ve yeni survey'in kapsam, dual-methodology ve PLC-centric taxonomy farkı bunun üzerinden açıklanır. Bu, adil ve ikna edici gap kurulumudur.
- **Katkı ve organizasyon:** Network layer'ın neden kapsam dışı, link/PHY'nin neden kapsam içi olduğu açıklanır. Katkılar physical motivation, taxonomy, optimization formulation, chronological evolution, lessons ve future directions'a gider. Scope sınırının teknik gerekçeyle savunulması güçlü bir COMST kalıbıdır.

### COMST_070 — UAV-Assisted Communications With RF Energy Harvesting

- **İşlev dizisi:** UAV'nin esnek connectivity rolü → pazar/bağlantı büyümesi ve NTN bağlamı → standards/industrial applications → UAV kanalının ayırt edici özellikleri → battery-duration darboğazı → genel energy harvesting → RF-EH'nin erişilebilir çözüm olarak daralması → UAV ve EH survey kümeleri → standardization/SWIPT/industry boşluğu → katkılar → organizasyon.
- **Geçiş, ton ve ritim:** “Furthermore”, “In contrast”, “However”, “These concerns have spurred…”, “In this direction” ve “Apart from…” bağları kullanılır. Battery probleminden RF-EH odağına geçiş güçlüdür; ancak pazar sayıları, kurumlar, application catalog ve related-work özetleri çok uzun olduğu için ritim ağırlaşır.
- **Related work ve gap:** İlk grup UAV communication ve genel EH survey'leri, ikinci grup UAV energy transfer/management çalışmalarından oluşur. Gap, RF-based EH for UAV communications'ın standardization, SWIPT architecture, industrial development, modeling, optimization ve emerging technologies ile ortak işlenmemesidir.
- **Katkı ve organizasyon:** Taxonomy/standards, EH receivers/models, emerging PHY/network/computing technologies, optimization ve future research başlıkları kapsamla hizalıdır. Güçlü taraf, iki literatür ailesini ortak pratik probleme bağlamasıdır; zayıf taraf, Introduction'ın “her şeyi kapsıyoruz” listesine dönüşmesidir.

### COMST_071 — Edge–Cloud Generative AI in Mobile Networks

- **İşlev dizisi:** AIGC'nin teknik ve ekonomik yükselişi → model/uygulama örnekleri → cloud'da model erişimi → mobile kullanıcı için latency ve interactivity açığı → edge–cloud–device katmanları → low-latency/localization/personalization/privacy motivasyonları → resource, fairness ve mobility challenges → generative-AI ve mobile-edge survey aileleri → real-time/privacy-preserving mobile AIGC boşluğu → katkılar → organizasyon.
- **Geçiş, ton ve ritim:** “Based on…”, “Over time…”, “Although…”, “Consequently…” ve “Compared to…” bağlantıları iki alanı bir araya getirir. Ton güncel, açıklayıcı ve yer yer promosyoneldir. Ürün/model örnekleri canlılık verir fakat hızla eskime ve Introduction'ı background kataloğuna dönüştürme riski taşır.
- **Related work ve gap:** Related work önce generative models/content modalities, sonra edge intelligence/federated learning/blockchain olarak iki hat halinde sunulur. Gap bu iki hattın kesişimindedir: collaborative mobile-edge-cloud altyapıda gerçek zamanlı, privacy-preserving AIGC service provisioning.
- **Katkı ve organizasyon:** Definition/lifecycle/metrics, applications/use cases, implementation challenges ve future directions dört maddede verilir. Katkıların service lifecycle'a bağlanması güçlüdür. Zayıf taraf, survey'in farkını anlatmadan önce çok fazla model ve ürün detayı verilmesidir.

### COMST_072 — Vehicle as a Service (VaaS)

- **İşlev dizisi:** Alice adlı ziyaretçi üzerinden somut smart-city yolculuğu → bu deneyimin sensing/communication/computing/storage/intelligence (SCCSI) gereksinimleri → 5G+ altyapısının CAPEX/OPEX darboğazı → “ekonomik alternatif var mı?” sorusu → araçlardaki atıl kaynaklar ve proximity avantajı → VaaS/SCCSI service-network önerisi → C-V2X'ten işlev farkı → prior surveys ve gap → katkılar → organizasyon.
- **Geçiş, ton ve ritim:** Hikâye açılışı alışılmadık derecede insani ve hatırlanabilirdir. “The above story…”, “To fulfill…”, “Although…”, “Thus, a critical question…”, “To answer…” geçişleri senaryoyu araştırma problemine çevirir. Ton vizyoner ama teknik gerekçeli; uzun paragraflara rağmen soru ve italik tez cümleleri ritim verir.
- **Related work ve gap:** Vehicular networking, vehicular edge computing ve vehicular cloud literatürü karşılaştırılır. Gap; araçları yalnız kullanıcı veya geçici compute node değil, planlı ve teşvikli biçimde çok boyutlu SCCSI kaynağı/servis sağlayıcısı olarak ele alan architecture + literature synthesis eksikliğidir.
- **Katkı ve organizasyon:** VaaS kavramı, VANET upgrades, architecture ve beş resource family survey'i aynı tez etrafında birleşir. Somut durumdan kavramsal katkıya geçiş grup içindeki en doğal örneklerden biridir. Risk, uzun açılış hikâyesinin teknik odağı geciktirmesidir; burada hikâyedeki her unsur daha sonra framework'e bağlandığı için bu risk büyük ölçüde yönetilmiştir.

### COMST_073 — Visible Light Positioning Tutorial

- **İşlev dizisi:** Outdoor GNSS başarısı fakat indoor attenuation → RF tabanlı indoor alternatiflerin infrastructure/multipath sorunları → VLP'nin fiziksel ve ekonomik avantajları → sistem bileşenlerinin kısa tanımı → mevcut VLP overview'leri → software/algorithm ağırlığı ve hardware/illumination/end-to-end eksikliği → tutorial ve primer vaadi → organizasyon.
- **Geçiş, ton ve ritim:** “However”, “Moreover”, “Indeed”, “In recent years” ve “Therefore” ile problem hızlı daralır. Ton temiz, tutorial-odaklı ve teknik; gereksiz 6G katalogları yoktur. Paragraflar kısa bir öğretim yolunu izler.
- **Related work ve gap:** Survey'ler localization algorithms, receiver types, standardization, VLC PHY ve illumination/hardware coverage'a göre karşılaştırılır. Gap somuttur: tüm parçalarıyla gerçek VLP sistemi kurmayı öğreten, hardware ve software'i uçtan uca birleştiren tutorial yoktur.
- **Katkı ve organizasyon:** Background/taxonomy, components, positioning methods, tek-PD RSS primer ve roadmap sırası doğrudan okuyucunun öğrenme yoludur. “Primer”ın açık hedefi, katkıyı salt bibliyografik kapsamdan uygulama yeteneğine dönüştürür. Güçlü ve ekonomik bir Introduction örneğidir.

### COMST_074 — WiFi Sensing on the Edge

- **İşlev dizisi:** WiFi sinyallerinin çevreden yansıması ve CSI'ın fiziksel sezgisi → device-free/privacy/through-wall avantajları → CSI capture araçlarının laptop/USRP maliyeti → gerçek edge deployment'ın pratik imkânsızlığı → ESP32'nin çözüm adayı → survey + onboard experimental evaluation katkıları → previous survey gap → organizasyon.
- **Geçiş, ton ve ritim:** “Despite…”, “As a result…”, “In this work…” geçişleri doğrudan pratik darboğaza gider. Ton somut, mühendislik odaklı ve deneysel; genel “future network” söylemi yerine cihaz, maliyet ve computation constraint üzerinden ilerler.
- **Related work ve gap:** Önceki WiFi-sensing survey'lerinin application veya deep-learning odaklı olduğu, embedded edge implementation'ı sistem seviyesinde ele almadığı söylenir. Ancak bu gap cümlesi katkı listesinden sonra gelir; klasik COMST sırasına göre geç kalmıştır.
- **Katkı ve organizasyon:** Taxonomy, signal-processing survey'i, calibration, üç ölçekli use case ve ESP32 ölçümleri birlikte verilir. Survey ile özgün experimental study'nin birleşmesi metne kanıt gücü katar. Güçlü açılış, sensör fiziğini hemen okuyucuya hissettirmesidir.

### COMST_075 — Wireless Access for V2X Communications

- **İşlev dizisi:** Industry 4.0 ve intelligent vehicles → otobüsün arkasındaki yaya örneğiyle onboard sensing'in görüş alanı sınırı → V2X'in cooperative perception gerekçesi → safety-critical + multi-user + heterogeneous requirements üçlü problemi → DSRC ve C-V2X adayları → tutorial amacı ve teknik scope exclusions → organizasyon → thematic related work.
- **Geçiş, ton ve ritim:** “However”, “Unfortunately”, “It is these edge-case scenarios…”, “Before any…”, “Of the vast portfolio…” geçişleri soyut endüstri bağlamını tek bir safety problemine indirger. Ton analitik ama erişilebilir; somut pedestrian senaryosu teknik soruya hizmet eder.
- **Related work ve gap:** Related work organizasyon paragrafından sonra gelir; genel V2X, VANET, vehicular cloud/fog, heterogeneous access, IoV, security ve C-V2X temalarına ayrılır. Survey'in farkı, wireless-access teknik kabiliyeti açısından “hangi aday teknoloji daha uygun?” sorusuna cevap verme ve higher-layer/adoption konularını bilinçli dışarıda tutmadır.
- **Katkı ve organizasyon:** Ayrı contribution listesi yerine purpose/scope paragrafı ve bölüm yolu kullanılır. Bölümler fundamentals → candidate technologies → metric-centered comparison → enabling technologies/future directions olarak soruya cevap verir. Markdown'da related-work tablosu metni böler, fakat ana anlatı kurtarılabilmiştir.

### COMST_076 — Wireless Backhaul in 5G and Beyond

- **İşlev dizisi:** 5G kapasite artışı ve wireless backhaul tanımı → pre-5G relays/self-backhaul'un neden yaygınlaşmadığı → mmWave/mMIMO/beamforming ve densification ile koşulların değişmesi → resource allocation, association, deployment, scheduling, energy ve coverage sorunları → UAV/HAPS/satellite uygulamaları → scope → motivation → mevcut surveys → organizasyon.
- **Geçiş, ton ve ritim:** “While…”, “However, with the introduction…”, “Even though…”, “Finally…” geçişleri tarihsel önce/sonra karşılaştırması kurar. Ton sade ve doğrudan; “we believe” ve “there are no works we know of” gibi ifadeler diğer güçlü örneklere göre daha gündelik ve daha az kanıtlanmış görünür.
- **Related work ve gap:** Surveys, general 5G backhaul, frequency alternatives, small-cell backhaul, UDN, moving networks, HAPS, aerial networks, satellites ve SAGIN olarak özetlenir. Gap “tüm perspektifleri karşılaştıran güncel çalışma yok” şeklindedir; sentez ekseni daha keskin tanımlanmamıştır.
- **Katkı ve organizasyon:** Ayrı katkı maddeleri yoktur; Scope paragrafı içeriği listeler, Difference bölümüyse önceki işleri anlatır. Organizasyon on beş bölümü tek uzun cümlede sayar. Tarihsel “neden daha önce olmadı, şimdi neden mümkün?” karşıtlığı güçlü; contribution/roadmap sunumu daha zayıftır.

### COMST_077 — Terahertz Channel Propagation, Measurement and Modeling

- **İşlev dizisi:** Artan veri talebi ve 6G için THz gerekçesi → THz bandının tanımı ve application families → propagation modeling'in zorunluluğu → THz araştırmasının tarihsel kökeni → electronic–photonic convergence ve source/detector ilerlemesi → arrays/RIS/OAM/NOMA/ML gibi enablers → standardization ve spectrum allocation → THz'nin pratik seçenek olduğu sonucu.
- **Geçiş, ton ve ritim:** “This unprecedented need…”, “Henceforth…”, “Nonetheless…”, “What has happened recently…”, “On the other hand…” ve “In conclusion…” geniş bir tutorial akışı kurar. Ton teknik, tarihsel ve özgüvenlidir; ancak Introduction bir girişten çok mini background bölümü gibi uzar.
- **Related work ve gap:** Introduction içinde survey karşılaştırması veya açık gap kurulumu yoktur. Bunlar sonraki ana bölüm olan `II. MOTIVATION AND CONTRIBUTIONS`'a taşınmıştır. Bu nedenle bu raporda Introduction sınırı içinde olmayan işlevler çıkarılmamıştır.
- **Katkı ve organizasyon:** Introduction katkı listesi ya da organizasyon paragrafıyla bitmez; standart/spektrum fizibilitesiyle kapanır ve motivasyon-katkı bölümüne devreder. Bu, klasik “gap → contribution → roadmap” düzeninin zorunlu olmadığını gösterse de, Introduction'a çok fazla enabling-technology ayrıntısı yükler.

## Grup düzeyinde ortak COMST Introduction reçetesi

Bu 25 metinden çıkan en sağlam reçete tek bir bağlaç veya sabit paragraf sayısı değildir. İyi çalışan girişler, okuyucunun bilgi durumunu adım adım değiştiren aşağıdaki işlev zincirini kurar:

1. **Konuyu bir sistem gerçeğiyle aç.** Açılış ya fiziksel bir mekanizma (WiFi yansıması, VLP'nin indoor avantajı), gözlenebilir bir kullanım sorunu (occluded pedestrian), tarihsel dönüşüm (PLC/WLC) ya da açık bir ağ gereksinimi olmalıdır. Genel “6G çok önemlidir” cümlesi tek başına yeterli değildir.
2. **İlk fırsatın yanında ilk bedeli göster.** Güçlü girişler çözümü erken övmez; neden mevcut yaklaşımın yetmediğini açıklar. Satellite multi-beam girişimi interference doğurur; edge AI yeni privacy yüzeyi açar; BackCom düşük güç sağlar ama double fading yaşar.
3. **Konuyu doğal bir darboğazla daralt.** Aday teknoloji, önceki paragraftaki sınırlamanın sonucu olarak ortaya çıkar. `Problem → mechanism → residual limitation` zinciri, bir teknoloji kataloğundan daha ikna edicidir.
4. **Kapsam sınırını teknik gerekçeyle koy.** Yalnız “bu survey şunları kapsar” denmez; ölçüm seviyesi, layer, modality, işlev veya implementation state gibi nedenlerle nelerin içeride/dışarıda olduğu açıklanır. COMST_069 ve COMST_075 bu işi iyi yapar.
5. **Related work'ü yayın sırasıyla değil, karşılaştırma eksenleriyle grupla.** Güçlü eksenler şunlardır: modality, layer, technical task, application, validation depth, hardware/software, general/specialized ve communication/sensing. Makale makale özet yalnız istisnaları göstermek için kullanılmalıdır.
6. **Gap'i üç parçalı kur.** `(a) Mevcut survey'ler neyi iyi yapıyor? (b) Hangi ortak ilişki/karşılaştırma hâlâ yok? (c) Bu eksiklik okuyucunun hangi teknik kararı vermesini engelliyor?` En ikna edici boşluklar yalnız “güncel survey yok” veya “ilk comprehensive survey” değildir.
7. **Survey vaadini gap'in aynası yap.** Gap cross-modality comparison ise katkı da cross-modality framework olmalıdır; gap measurement ambiguity ise katkı measurement-point/provenance korunumu olmalıdır. Kapsam genişliği tek başına bilimsel katkı değildir.
8. **Katkıları bölüm başlığı olarak değil sentez eylemi olarak yaz.** `classify`, `distinguish`, `trace`, `compare under stated conditions`, `explain why`, `identify where evidence stops` gibi eylemler daha güçlüdür. Uzun noun listeleri veya “overview X, discuss Y, present Z” dizileri daha mekanik görünür.
9. **Organizasyonu kısa tut ve düşünsel rotayı göster.** Güçlü roadmap, “foundations → comparison framework → evidence → trade-offs → limits/roadmap” gibi mantığı bir cümlede açıklar. On beş bölümün tek tek ayrıntılı dökümü Introduction'ın sonundaki ivmeyi söndürür.
10. **Yoğun açıklama ile kısa pivot cümlelerini dönüşümlü kullan.** COMST_059'daki temel sorular, COMST_072'deki “is there an alternative?” ve COMST_053'teki state-of-the-art/gap mantığı, uzun teknik paragraflar arasında yön tabelası görevi görür.

## Geçiş biçimleri: sözcük değil işlev

Korpusta geçiş başarısını yaratan şey “however” sayısı değil, bağlacın yaptığı düşünsel iştir:

- **Fırsattan sınıra:** `However`, `Yet`, `Despite`, `Although` — yeni konu açmak için değil, önceki iddianın bedelini göstermek için.
- **Sınırdan teknik ihtiyaca:** `Consequently`, `Therefore`, `Hence`, `In this context` — çözüm adayını nedensiz sunmamak için.
- **Genel alandan survey odağına:** `Among these`, `In what follows`, `In this survey`, `Specifically` — kapsamı görünür biçimde daraltmak için.
- **Literatürden gap'e:** `Several surveys have addressed X; however, ...` — önceki çalışmayı küçümsemeden eksik ilişkiyi göstermek için.
- **Gap'ten katkıya:** `To address this gap`, `These observations motivate...` — contribution listesini bir önceki kanıtın sonucu yapmak için.
- **Yoğun bloklar arası yön değişimi:** kısa soru, kısa tez veya kısa karşıtlık cümlesi — okuyucunun paragraf işlevini yeniden kavraması için.

Bağlaçların mekanik biçimde her paragrafın başına konması COMST tonu üretmez. Asıl ölçüt, yeni paragrafın öncekinin hangi açık sorusunu devraldığıdır.

## Ton ve ritim reçetesi

- **Güvenli otorite:** Alanı bilen bir ses kullanılır, fakat evrensel üstünlük ve “kusursuz/ilk/tek” türü iddialar ya karşılaştırma tablosuyla sınırlandırılır ya da hiç kullanılmaz.
- **Somut isimler, kontrollü sıfatlar:** `measurement point`, `receiver architecture`, `double fading`, `linearity`, `validation setting` gibi somut teknik kavramlar; `revolutionary`, `unprecedented`, `tremendous` gibi promosyonel sıfatlardan daha değerlidir.
- **Bir paragraf, bir retorik iş:** Aynı paragraf hem alan tarihini, hem üç teknolojiyi, hem survey gap'ini, hem de katkıyı taşımamalıdır.
- **Değişken cümle ritmi:** Teknik açıklamalar orta uzunlukta cümlelerle; yön değişimleri kısa ve belirgin cümlelerle verilir. Arka arkaya aynı kalıptaki “We first… We then… Finally…” cümleleri azaltılır.
- **İnsani ama bilimsel açılış:** COMST_072 ve COMST_075 somut senaryo kullanır; COMST_074 fiziksel sezgi kullanır. Bu örnekler, “insani ses” üretmenin gündelikleşmek değil, okuyucunun problemi görmesini sağlamak olduğunu gösterir.

## Güçlü ve zayıf kalıplar

### En güçlü, aktarılabilir kalıplar

- **COMST_056:** sistem değişimi → interference problemi → özel survey gap'i → iki eksenli taxonomy.
- **COMST_059:** tutorial açıklama → merkezi tasarım ilkesi → üç soru → “why/how/when” contribution sözleşmesi.
- **COMST_060:** research questions + reproducible review method + gap ile bölüm eşlemesi.
- **COMST_061:** RF/optical gibi iki modality'yi ortak security mekanizması üzerinden birleştirme.
- **COMST_063 ve COMST_069:** tarihsel/physical foundation'dan kesişim literatürü boşluğuna geçiş.
- **COMST_065:** iki ayrı literatür ailesini özgün bir framework ile bağlama.
- **COMST_067:** communications ve sensing'i paralel liste değil iki yönlü sinerji olarak kurma.
- **COMST_072 ve COMST_075:** somut insan/safety senaryosunu teknik sisteme ve gap'e dönüştürme.
- **COMST_073 ve COMST_074:** fiziksel veya implementation-level problemle hızlı ve anlaşılır açılış.

### Daha zayıf veya dikkatle kullanılacak kalıplar

- Ülke, kurum, proje, ürün veya market-size envanterini uzun süre sürdürmek (özellikle COMST_053, COMST_068, COMST_070, COMST_071).
- Introduction'ı textbook/background bölümüne dönüştürmek (COMST_058, COMST_059'un bazı alt kısımları, COMST_065, COMST_067, COMST_077).
- Related work'ü her yayını aynı cümle kalıbıyla tek tek özetlemek (COMST_057, COMST_066, COMST_070, COMST_076).
- Gap'i yalnız “güncel”, “comprehensive” veya “first” sıfatına dayandırmak (COMST_054'ün bazı cümleleri, COMST_068, COMST_076).
- Çok uzun contribution listeleriyle Introduction'ı ikinci bir içindekiler tablosuna çevirmek (COMST_062, COMST_067, COMST_070).
- Related-work gap'ini katkılardan sonra söylemek (COMST_074) veya klasik Intro dışında sonraki ana bölüme bırakmak (COMST_077); bu yapılabilir, fakat okuyucunun survey gerekçesini geç öğrenmesine yol açar.
- Organization paragrafında her section'ın tüm alt işlevlerini tek uzun cümleyle saymak (COMST_055, COMST_076).

## Grup C'den çıkan kısa kontrol listesi

Bir Introduction, aşağıdaki sorulara sırayla ve açıkça cevap veriyorsa COMST anlatı mantığına yaklaşır:

1. Okuyucu ilk iki paragrafta gerçek teknik problemi görebiliyor mu?
2. Çözüm adayının avantajı kadar bedeli/sınırı da gösteriliyor mu?
3. Survey'in konusu geniş alandan doğal bir darboğazla mı türetiliyor?
4. Önceki survey'ler adil ve karşılaştırılabilir kümeler halinde mi anlatılıyor?
5. Gap bir “yayın eksikliği” değil, bir **bilgi veya karar eksikliği** olarak mı kuruluyor?
6. Katkılar gap'in aynısı olan sentez görevlerine mi cevap veriyor?
7. Kapsam dışı unsurlar teknik gerekçeyle sınırlandırılıyor mu?
8. Organization paragrafı içindekileri tekrarlamak yerine düşünsel rotayı mı gösteriyor?
9. Uzun teknik paragraflar arasında kısa pivot cümleleri var mı?
10. Metin, “en kapsamlı/ilk” sıfatları olmadan da neden gerekli olduğunu kanıtlayabiliyor mu?

Bu grup için kapsama sonucu: **25/25 Introduction okunmuş ve görünür biçimde değerlendirilmiştir.**
