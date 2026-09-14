# Section III için bölüm eşleştirme tablosu

Tarih: 12 Eylül 2026. Amaç, başka makalelerde **bizim Section III’ün yaptığı işi üstlenen parçaları** bulmak. Bölüm numaralarının aynı olması aranmıyor. Örneğin COMST_023’te karşılık Section V’in açılışında.

## Kapsam ve okuma düzeyi

Yerel COMST arşivindeki **77 Markdown metninin tamamı** başlıklar ve derleme yöntemine ilişkin ifadelerle tarandı. Eski notlardaki 76 sayısı yerine bu çalışmada mevcut dosya sayısı kullanıldı. P01 ve P02 ayrıca tarandı; bu iki başlık 77 COMST kaydında yinelenmiyor. Aday yöntem pasajları bağlamlarıyla okundu. PDF’ler yeniden açılmadı, bütün makaleler baştan sona yeniden okunmadı.

**Altı COMST çalışmasında doğrudan yöntem eşleşmesi doğrulandı.** İki ek COMST örneği yalnız seçim/kapsam açıklaması bakımından yakın. P01/P02’deki yakınlık kapsam, karşılaştırma tabloları ve sentez çıktısı düzeyinde. “Saptanmadı” kaydı, hedefli taramada doğrulanmış bir yöntem pasajı bulunmadığını belirtir; makalenin hiçbir yerinde böyle bir açıklama bulunmadığına dair kesin hüküm değildir.

## Bizim Section III’te aranan işlevler

| Parçamız | Aranan işlev | Salt teknik konu olarak benzer sayılmayanlar |
|---|---|---|
| III-A — Search, Eligibility, and Study Reconciliation | Kaynak/sorgu, zaman penceresi, uygunluk, eleme, yinelenen sürümler ve rapor–çalışma ilişkisi | Önceki derlemeleri tanıtmak veya makale organizasyonu vermek tek başına seçim yöntemi değildir |
| III-B — Extraction and Units of Analysis | Kaynak bağlantılı çıkarım, analiz birimi, ölçü/birim/koşul kayıtları | Birincil sistemde veri toplama, özellik çıkarma veya makine öğrenmesi veri kümesi hazırlama |
| III-C — Technical Appraisal and Synthesis | Çalışmaların teknik desteğini değerlendirme ve sonuçları sınıflandırıp koşullarıyla sentezleme | Sinyal kalitesi, saldırı başarısı veya model doğruluğunu değerlendirmek tek başına derleme kalitesi değerlendirmesi değildir |

## A. Doğrudan yöntem eşleşmeleri

| Çalışma | Gerçek bölüm / parça | Bizdeki karşılık | Pasajın yaptığı iş | Eşleşmenin sınırı | Kaynak satırları |
|---|---|---|---|---|---|
| COMST_010 | II-G. Motivation and Methodology for Choosing Literature; Fig. 5 | III-A; III-C sentez yöntemi | Araştırma sorusu ve amaç → arama stratejisi → ilişkili yayınları izleme → dahil etme/dışlama → katkıya göre kategorileştirme. Kitchenham–Charters yaklaşımına dayandığını açıklıyor. | Sınıflandırma; teknik kalite puanı değildir. “Quantitative approach” ifadesinin ayrıntısı verilmediği için nicel havuzlama anlamı çıkarılamaz. | [L280–300](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_010/COMST_010.md:280) |
| COMST_023 | V. Trust Models in Heterogeneous Networks — açılış paragrafı | III-A doğrudan; III-C sınıflandırma kısmen | 2016–2020 yayın penceresini, Web of Science/Google Scholar/IEEE Xplore/ACM kaynaklarını ve anahtar sözcükleri veriyor. Çalışmaları taksonomi ve ağ türü üzerinden değerlendiriyor. | Bu pasajda ayrıntılı eleme akışı, çıkarım şeması veya çalışma kalitesi protokolü yok. Bizim III’e benzeyen bölüm burada V numarasını taşıyor. | [L300–302](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_023/COMST_023.md:300) |
| COMST_025 | II-F. Survey Methodology | III-A; III-C sentez yöntemi | Freehaven arşivindeki 2010’dan başlayan güvenlik yayınlarından kapsam oluşturuyor. Sansür saldırılarını kapsam dışında tutuyor. Yukarıdan aşağıya ontoloji ve aşağıdan yukarıya zafiyet analiziyle kaynakları ilişkilendiriyor. | 2010 başlangıç yılıdır. Zafiyet analizi, makalelerin yöntem kalitesini puanlama değildir. Ontoloji ve mekanizma üzerinden sentez için örnektir. | [L334–340](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_025/COMST_025.md:334) |
| COMST_038 | I-B. Survey Methodology; I-C. Survey Scope | III-A doğrudan | PRISMA temelli seçim, Google Scholar/Semantic Scholar, anahtar sözcük birleşimleri, iki aşamalı filtreleme ve kapsam dışı konuları açıklıyor. Her sorgunun ilk beş sonuç sayfasını inceliyor; ana odak 2018–Mart 2023. | İlk beş sayfa sınırı korunmalı. 2018–Mart 2023 mutlak dahil etme kuralı olarak genişletilmemeli. III-B çıkarım birimleri ve III-C teknik kalite puanlaması bu pasajda yok. | [L85–93](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_038/COMST_038.md:85) |
| COMST_050 | I-C. Research Methodology; I-E1. Literature Categorization | III-A; III-C sınıflandırma/sentez; kalite ölçütü kısmi | Araştırma soruları, IEEE Xplore/ACM/Google Scholar araması, seçim ölçütleri, atıf zinciri ve temaya göre yinelemeli sentez veriliyor. 115 yayının alan ve kategori üzerinden nasıl düzenlendiği açıklanıyor. | “Quality assessment” burada yayın yerinin itibarıyla ilişkilendiriliyor; bizim teknik çalışma değerlendirmemize eşdeğer değil. 115 sayısı bağımsız çalışma değil “papers”. Ölçütlerden herhangi birini karşılama kuralı var. | [L162–179](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_050/COMST_050.md:162) · [L187–195](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_050/COMST_050.md:187) · [L223–229](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_050/COMST_050.md:223) |
| COMST_060 | I-B. Review Method | III-A doğrudan; sürüm ayıklama açısından kısmi yakınlık | Araştırma sorusundan Boolean sorgu türetiyor; IEEE Xplore ve geriye doğru kaynak izleme kullanıyor. Konu uygunluğunu ve aynı çalışmanın yayımlanmış sürümünü ön baskıya tercih etme kuralını açıklıyor. | Sürüm ayıklama, bizim tüm raporları bağımsız çalışmalara uzlaştırmamızın tam karşılığı değildir. Ayrıntılı çıkarım birimi veya TQAF benzeri çerçeve bu pasajda doğrulanmadı. | [L85–95](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_060/COMST_060.md:85) |

## B. COMST içinde sınırlı benzerlikler

Bu iki kayıt doğrudan yöntem sayısına dahil edilmedi.

| Çalışma | Gerçek bölüm / parça | Bizdeki karşılık | Pasajın yaptığı iş | Eşleşmenin sınırı | Kaynak satırları |
|---|---|---|---|---|---|
| COMST_006 | VII-A. Features of Quantum Machine Learning — Table XIV öncesi | III-A’ya sınırlı seçim açıklaması | Her kategoride daha fazla yaklaşım bulunduğunu ve ilginç buldukları birkaçını seçtiklerini açıkça söylüyor. | Seçimin öznel sınırını bildiriyor; tekrarlanabilir arama ve uygunluk protokolü vermiyor. | [L841–843](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_006/COMST_006.md:841) |
| COMST_024 | I-B. Article Scope and Contributions | III-A kapsam; III-C sınıflandırma açısından kısmi | Mobil cihazların yerleşik sensörleriyle insan etkinliği tanımayı kapsam olarak belirliyor. Etkinlik, veri, ön işleme, tanıma ve değerlendirme boyutlarına göre anlatım kuruyor. | Başlığındaki “Systematic Review” ifadesi tek başına açık yöntem protokolü kanıtı değil. Değerlendirme standartları esasen birincil tanıma sistemlerinin değerlendirilmesine ilişkin. | [L51–55](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_024/COMST_024.md:51) · [L81–85](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_024/COMST_024.md:81) |

## C. Paylaşılan iki çalışmadaki karşılıklar

- **P01:** Integrated Sensing and Communications Over the Years: An Evolution Perspective.
- **P02:** Optical integrated sensing and communication: Fundamentals, applications, challenges and future aspects.

| Çalışma | Gerçek bölüm / parça | Bizdeki karşılık | Pasajın yaptığı iş | Eşleşmenin sınırı | Kaynak satırları |
|---|---|---|---|---|---|
| P01 | I-B. Related Survey Papers; Table I | III-A’ya yalnız bağlam | Önceki derlemeleri konu ve uygulama eksenleriyle karşılaştırarak kendi kapsamını gerekçelendiriyor. | Kaynakların nasıl arandığını, seçildiğini veya elendiğini açıklayan yöntem yerine geçmez. | [L129–182](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:129) · [L222–223](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:222) |
| P01 | I-C. Contributions | III-A kapsam; III-C sentez eksenleri kısmen | Spektrum, ağ mimarisi, algılama kipleri, güvenlik ve standardizasyonu ortak evrim çerçevesinde topluyor. | Bu eksenler sentez düzenidir; çalışma uygunluğu veya kalite puanlama kuralları değildir. | [L183–214](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:183) |
| P01 | II-D. Lessons Learned | III-C’ye kısmi — sentez çıktısı | RF–optik bütünleşmesi üzerine ortak tasarım, uyarlama, eşzamanlama ve kalibrasyon gereksinimleri çıkarıyor. | Anlatısal sentezin nasıl göründüğüne örnektir; sentez yöntemi ya da çalışma kalitesi değerlendirme protokolü değildir. | [L600–625](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:600) |
| P02 | 1.2. Existing works; 1.3. Salient contributions | III-A kapsam kısmen | Önceki çalışmaların kapsamını ve kendi O-ISAC kategori, deney ve tasarım odağını tanımlıyor. | Açık veri tabanı, sorgu, dahil etme/dışlama veya eleme protokolü olarak alınmamalı. | [L238–253](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:238) · [L318–327](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:318) · [L365–384](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:365) |
| P02 | 3.5. Existing experimental works on O-ISAC; Table 5 | III-B’ye kısmi — çıkarım çıktısı | Deneyleri kaynak/yıl, modülasyon, konumlama algoritması, veri hızı, doğruluk, verici/alıcı ve test alanıyla karşılaştırıyor. | Koşullarıyla sonuç kaydına en yakın örnek. Ancak çıkarım prosedürü, analiz birimi veya veri doğrulama kuralı açıklamıyor. | [L979–1004](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:979) · [L1038–1054](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:1038) |
| P02 | 7. Open research issues and future aspects — Real-time practice; Table 9 | III-C’ye kısmi — sentez çıktısı | Uygulama ve saha deneyi eksiklerini tartışıyor; sistemlerin yöntem, algılama nesnesi, fayda ve gelecek yönlerini karşılaştırıyor. | Uygulama eksikliği yorumu, yapılandırılmış çalışma kalitesi veya yanlılık değerlendirmesiyle eşdeğer değil. | [L2596–2607](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:2596) · [L2823–2834](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:2823) |

P01’in I-C içindeki organizasyon paragrafı (L225–233), P02’nin “2. Categories of O-ISAC” (L388–392) ve “5.2. Performance metrics” (L1230–1238, L1268–1284) parçaları da ayrıştırıldı. Bunlar teknik kapsam/organizasyon ve sistem performansına ilişkindir; derleme yöntemi diye sınıflandırılmadı. P01’in kendi Section III’ü ağ mimarisini anlatır; bizim Section III ile numarası dışında doğrudan yöntem eşleşmesi yoktur.

İki çalışmada bu hedefli incelemeyle açık sorgu/veri tabanı protokolü, eleme akışı, rapor–çalışma uzlaştırması veya yapılandırılmış teknik kalite değerlendirme süreci doğrulanmadı.

## D. Bizim alt bölümlerimize göre okuma sırası

| Bakılacak iş | En yakın yerler | Dikkat edilecek sınır |
|---|---|---|
| III-A’yı nasıl anlatabiliriz? | COMST_060 I-B; COMST_038 I-B/I-C; COMST_010 II-G | Yöntemin somut kaynak, sorgu ve kapsam kararlarıyla anlatılması. Başka çalışmanın eksik raporlaması bizim gereksinimlerimizi kaldırmaz |
| III-B’de koşullarıyla sonuç kaydı nasıl görünür? | P02 3.5 / Table 5 | Bu bir çıkarım çıktısı örneği; bizim çıkarım şeması ve analiz birimleri için tam yöntem karşılığı doğrulanmadı |
| III-C’de sentez yaklaşımı nasıl açıklanır? | COMST_025 II-F; COMST_010 II-G; COMST_050 I-C/I-E1 | Sentez yaklaşımını, teknik kalite değerlendirmesini ve sentez çıktısını ayrı okumak gerekir |
| III-C’de teknik kalite çerçevesine karşılık var mı? | COMST_050 I-C yalnız kısmi yakınlık | Yayın yeri itibarı, TQAF boyutlarıyla eşdeğer değil. Doğrulanan pasajlarda tam eşdeğer bulunmadı |

## E. Tüm COMST metinlerinin tarama durumu

**D:** Yukarıdaki A tablosunda kaynak pasajıyla doğrulanan doğrudan yöntem eşleşmesi. **K:** B tablosundaki sınırlı seçim/kapsam benzerliği. **T:** Başlık ve yöntem ifadesi tarandı; doğrudan yöntem pasajı doğrulanmadı. T, tam okuma sonrası verilmiş bir “yok” hükmü değildir. Genel teknik taksonomi ve lessons-learned bölümlerinin tümü ayrıca çıkarılmadı.

| ID ve kaynak | Makale başlığı | Durum | Doğrulanan yakın yer |
|---|---|---|---|
| [COMST_001](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_001/COMST_001.md) | 6G Communication New Paradigm: The Integration of Autonomous Aerial Vehicles and Intelligent Reflecting Surfaces | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_002](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_002/COMST_002.md) | A Comprehensive Survey on Full-Duplex Communication: Current Solutions, Future Trends, and Open Issues | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_003](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_003/COMST_003.md) | A Comprehensive Survey on Radio Resource Management in 5G HetNets: Current Solutions, Future Trends and Open Issues | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_004](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_004/COMST_004.md) | A Survey and Comparison of Post-Quantum and Quantum Blockchains | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_005](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_005/COMST_005.md) | A Survey of Beam Management for mmWave and THz Communications Towards 6G | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_006](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_006/COMST_006.md) | A Survey of Important Issues in Quantum Computing and Communications | K | VII-A. Features of Quantum Machine Learning — Table XIV öncesi |
| [COMST_007](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_007/COMST_007.md) | A Survey of mmWave-Based Human Sensing: Technology, Platforms and Applications | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_008](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_008/COMST_008.md) | A Survey of Quantum Internet Protocols From a Layered Perspective | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_009](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_009/COMST_009.md) | A Survey of Security in UAVs and FANETs: Issues, Threats, Analysis of Attacks, and Solutions | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_010](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_010/COMST_010.md) | A Survey on Approximate Edge AI for Energy Efficient Autonomous Driving Services | D | II-G. Motivation and Methodology for Choosing Literature; Fig. 5 |
| [COMST_011](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_011/COMST_011.md) | A Survey on Beyond 5G Network Slicing for Smart Cities Applications | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_012](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_012/COMST_012.md) | A Survey on Controller Area Network Reverse Engineering | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_013](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_013/COMST_013.md) | A Survey on IEEE 802.11bn Wi-Fi 8: Advantages of Ultra High Reliability for Next Generation Wireless LANs | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_014](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_014/COMST_014.md) | A Survey on Indoor Visible Light Positioning Systems: Fundamentals, Applications, and Challenges | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_015](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_015/COMST_015.md) | A Survey on Integrated Sensing, Communication, and Computation | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_016](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_016/COMST_016.md) | A Survey on Integration of Network Communication into Vehicle Real-Time Motion Control | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_017](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_017/COMST_017.md) | A Survey on IoT-Enabled Home Automation Systems: Attacks and Defenses | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_018](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_018/COMST_018.md) | A Survey on Mobility of Edge Computing Networks in IoT: State-of-the-Art, Architectures, and Challenges | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_019](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_019/COMST_019.md) | A Survey on Model-Based, Heuristic, and Machine Learning Optimization Approaches in RIS-Aided Wireless Networks | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_020](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_020/COMST_020.md) | A Survey on Multi-AP Coordination Approaches Over Emerging WLANs: Future Directions and Open Challenges | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_021](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_021/COMST_021.md) | A Survey on Nongeostationary Satellite Systems: The Communication Perspective | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_022](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_022/COMST_022.md) | A Survey on Scheduling Techniques in Computing and Network Convergence | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_023](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_023/COMST_023.md) | A Survey on Trust Models in Heterogeneous Networks | D | V. Trust Models in Heterogeneous Networks — açılış paragrafı |
| [COMST_024](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_024/COMST_024.md) | A Systematic Review of Human Activity Recognition Based on Mobile Devices: Overview, Progress and Trends | K | I-B. Article Scope and Contributions |
| [COMST_025](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_025/COMST_025.md) | A Systematic Survey on Security in Anonymity Networks: Vulnerabilities, Attacks, Defenses, and Formalization | D | II-F. Survey Methodology |
| [COMST_026](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_026/COMST_026.md) | A Top-Down Survey on Optical Wireless Communications for the Internet of Things | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_027](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_027/COMST_027.md) | A Tutorial on Beyond-Diagonal Reconfigurable Intelligent Surfaces: Modeling, Architectures, System Design and Optimization, and Applications | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_028](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_028/COMST_028.md) | Active Reconfigurable Intelligent Surfaces: Expanding the Frontiers of Wireless Communication-A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_029](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_029/COMST_029.md) | Advances in Machine Learning-Driven Cognitive Radio for Wireless Networks: A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_030](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_030/COMST_030.md) | Aerospace Integrated Networks Innovation for Empowering 6G: A Survey and Future Challenges | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_031](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_031/COMST_031.md) | AI-driven Wireless Positioning: Fundamentals, Standards, State-of-the-art, and Challenges | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_032](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_032/COMST_032.md) | An Overview on IEEE 802.11bf: WLAN Sensing | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_033](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_033/COMST_033.md) | Beam Alignment in mmWave V2X Communications: A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_034](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_034/COMST_034.md) | Computational Intelligence Algorithms for UAV Swarm Networking and Collaboration: A Comprehensive Survey and Future Directions | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_035](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_035/COMST_035.md) | Data and Model Poisoning Backdoor Attacks on Wireless Federated Learning, and the Defense Mechanisms: A Comprehensive Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_036](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_036/COMST_036.md) | Design Guidelines on Trust Management for Underwater Wireless Sensor Networks | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_037](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_037/COMST_037.md) | Enabling Intelligent Connectivity: A Survey of Secure ISAC in 6G Networks | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_038](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_038/COMST_038.md) | Evasion Attack and Defense on Machine Learning Models in Cyber-Physical Systems: A Survey | D | I-B. Survey Methodology; I-C. Survey Scope |
| [COMST_039](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_039/COMST_039.md) | Evolution of Non-Terrestrial Networks From 5G to 6G: A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_040](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_040/COMST_040.md) | Holographic MIMO Communications: Theoretical Foundations, Enabling Technologies, and Future Directions | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_041](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_041/COMST_041.md) | How Can Optical Communications Shape the Future of Deep Space Communications? A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_042](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_042/COMST_042.md) | In-Network Machine Learning Using Programmable Network Devices: A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_043](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_043/COMST_043.md) | Integrated 5G and Time Sensitive Networking for Emerging Applications: A Survey of Advancements, Challenges, and Future Directions | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_044](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_044/COMST_044.md) | Integrated Sonar and Communication: A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_045](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_045/COMST_045.md) | Intellicise Wireless Networks From Semantic Communications: A Survey, Research Issues, and Challenges | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_046](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_046/COMST_046.md) | Metaverse Communications, Networking, Security, and Applications: Research Issues, State-of-the-Art, and Future Directions | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_047](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_047/COMST_047.md) | MIMO Satellite Communication Systems: A Survey From the PHY Layer Perspective | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_048](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_048/COMST_048.md) | Models, Methods, and Solutions for Multicasting in 5G/6G mmWave and Sub-THz Systems | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_049](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_049/COMST_049.md) | Multi-Modal Data-Enhanced Foundation Models for Prediction and Control in Wireless Networks: A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_050](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_050/COMST_050.md) | Navigating Industry 5.0: A Survey of Key Enabling Technologies, Trends, Challenges, and Opportunities | D | I-C. Research Methodology; I-E1. Literature Categorization |
| [COMST_051](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_051/COMST_051.md) | Near-Field Communications: A Comprehensive Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_052](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_052/COMST_052.md) | Network Slicing-Based Learning Techniques for IoV in 5G and Beyond Networks | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_053](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_053/COMST_053.md) | On the Road to 6G: Visions, Requirements, Key Technologies, and Testbeds | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_054](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_054/COMST_054.md) | Optical Wireless Communication in Atmosphere and Underwater: Statistical Models, Improvement Techniques, and Recent Applications | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_055](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_055/COMST_055.md) | Post-Quantum Blockchain Security for the Internet of Things: Survey and Research Directions | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_056](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_056/COMST_056.md) | Precoding for High-Throughput Satellite Communication Systems: A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_057](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_057/COMST_057.md) | Principles, Applications, and Challenges of Reconfigurable Intelligent Surface-Enabled Backscatter Communication: A Comprehensive Survey and Outlook | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_058](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_058/COMST_058.md) | Quantum AI-Enhanced IoT-Fog Communication: A Survey from Cybersecurity and Data Privacy Perspective | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_059](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_059/COMST_059.md) | Rate-Splitting Multiple Access: Fundamentals, Survey, and Future Research Trends | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_060](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_060/COMST_060.md) | Reconfigurable Intelligent Surfaces in 6G Radio Localization: A Survey of Recent Developments, Opportunities, and Challenges | D | I-B. Review Method |
| [COMST_061](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_061/COMST_061.md) | RIS-Assisted Physical Layer Security in Emerging RF and Optical Wireless Communications Systems: A Comprehensive Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_062](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_062/COMST_062.md) | RIS-Empowered Satellite-Aerial-Terrestrial Networks With PD-NOMA | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_063](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_063/COMST_063.md) | Seamless Connectivity: The Power of Integrating Power Line and Wireless Communications | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_064](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_064/COMST_064.md) | Security and Privacy on 6G Network Edge: A Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_065](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_065/COMST_065.md) | Semantics-Empowered Space-Air-Ground-Sea Integrated Network: New Paradigm, Frameworks, and Challenges | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_066](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_066/COMST_066.md) | Spectrum Sharing and Interference Management for 6G LEO Satellite–Terrestrial Network Integration | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_067](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_067/COMST_067.md) | Terahertz Communications and Sensing for 6G and Beyond: A Comprehensive Review | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_068](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_068/COMST_068.md) | Toward 6G Optical Fronthaul: A Survey on Enabling Technologies and Research Perspectives | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_069](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_069/COMST_069.md) | Two Decades of Research Progress in Resource Allocation for PLC Systems: From Core Concepts to Frontiers | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_070](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_070/COMST_070.md) | UAV-Assisted Communications With RF Energy Harvesting: A Comprehensive Survey | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_071](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_071/COMST_071.md) | Unleashing the Power of Edge-Cloud Generative AI in Mobile Networks: A Survey of AIGC Services | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_072](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_072/COMST_072.md) | Vehicle as a Service (VaaS): Leverage Vehicles to Build Service Networks and Capabilities for Smart Cities | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_073](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_073/COMST_073.md) | Visible Light Positioning as a Next-Generation Indoor Positioning Technology: A Tutorial | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_074](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_074/COMST_074.md) | WiFi Sensing on the Edge: Signal Processing Techniques and Challenges for Real-World Systems | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_075](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_075/COMST_075.md) | Wireless Access for V2X Communications: Research, Challenges and Opportunities | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_076](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_076/COMST_076.md) | Wireless Backhaul in 5G and Beyond: Issues, Challenges and Opportunities | T | Doğrudan yöntem pasajı doğrulanmadı |
| [COMST_077](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_077/COMST_077.md) | Terahertz Channel Propagation Phenomena, Measurement Techniques and Modeling for 6G Wireless Communication Applications: A Survey, Open Challenges and Future Research Directions | T | Doğrudan yöntem pasajı doğrulanmadı |

## Kontrol kaydı

Eşleştirme, `C:/GH/OISAC_PRISMA_COMST/data/corp_std` arşivinde yapıldı. Aynı 77 kaynak, kurtarma arşivindeki kopyalarıyla SHA-256 üzerinden aynı bulundu. Arama ifadeleri ve satır adayları `scan.json` dosyasında, tablo üretimi `build.py` dosyasında tutuldu. Makale TeX dosyaları değiştirilmedi.

Altı doğrudan eşleşmenin bölüm numaraları ve yorum sınırları ikinci bir AI okumasıyla kontrol edildi. P01/P02 adayları ayrı bir AI okumasıyla incelendi. Bu, bağımsız insan değerlendirmesi değildir.

Bu belge karşılaştırma ve kaynak bulma tablosudur. Section III’e yeni içerik eklemez; bütün korpusun her paragrafını eksiksiz yorumladığımızı veya bizim yöntemimizin diğerlerinden üstün olduğunu ileri sürmez.
