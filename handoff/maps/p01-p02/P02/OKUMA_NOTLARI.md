# P02 - Ayrıntılı okuma notları

Okuma tarihi: 2026-09-06. Kaynak: kullanıcının verdiği `2.pdf`, 37 PDF sayfası. Aşağıdaki sayfa numaraları PDF'nin 1'den başlayan sayfa sırasıdır; bu dosyada basılı sayfalarla aynıdır. Bu kayıt belge okuması ve kaynak içi incelemedir; özgün deneylerin bağımsız doğrulaması veya insan hakem kararı değildir.

## Künye ve çalışmanın niteliği

S.A.H. Mohsan, Siyu Bai, Haoyu Huang, Yi Hao, Shichen Zheng, Qian Li ve H.Y. Fu. **Optical integrated sensing and communication: Fundamentals, applications, challenges and future aspects.** Optical Switching and Networking, 61 (2026), 100854. DOI: **10.1016/j.osn.2026.100854**.

İlk sayfada geliş 23 Aralık 2025, revizyon 3 Şubat 2026, kabul 4 Şubat 2026, çevrimiçi erişim 6 Şubat 2026 yazıyor. PDF üretim tarihi Nisan 2026; bunu makalenin yayın tarihi olarak kullanmamak gerekir. Kaynakça [1]-[174] olmak üzere 174 numaralı kayıttan oluşuyor; bunlar 174 dahil edilmiş birincil deney anlamına gelmiyor. 10 tablo ve 25 numaralı şekil bulunuyor. Tablo 10 iki sayfaya yayılıyor.

Makale, O-ISAC teknolojilerini temellerden uygulamalara uzanan geniş bir anlatısal derleme olarak sunuyor. İncelenen PDF'de yeniden çalıştırılabilir veri tabanı sorguları, son arama tarihi, tarama/eleme akışı, önceden tanımlı dahil etme ölçütleri veya çalışma bazında risk-of-bias değerlendirmesi raporlanmıyor. Bu tespit, yayının dışında böyle bir kayıt bulunmadığı iddiası değildir.

## Ana fikir ve katkı konumlandırması

Temel yaklaşım, optik haberleşme ve optik algılamanın donanım, spektrum, dalga biçimi ve kaynakları paylaşarak birleştirilmesi. Motivasyonlar yüksek veri hızı, hassas algılama ve girişimin azaltılması; bunların bedeli hizalama, dar görüş alanı, engellenme, atmosferik etkiler, donanım ve sinyal kısıtlarıdır.

Yazarlar geniş kapsamı, DOFS/fiber ayrıntısını, deneysel örnekleri ve uygulama çeşitliliğini ayırt edici katkı olarak gösteriyor. Tablo 3'te sekiz önceki yayının yanında **Our Work** satırı var (s.4). S.2'deki ilk kapsamlı inceleme ifadesi yazarların özgünlük iddiasıdır; burada bağımsız olarak doğrulanmış bir alan önceliği kabul edilmemiştir.

## Bölüm bölüm okuma

| Bölüm | PDF sayfaları | İçerik ve bilimsel işlev |
|---|---|---|
| 1. Introduction | 1-4 | RF/optik ayrımı, önceki derlemeler, katkılar ve kapsam. Tablo 1 sayısal tipik özellikler; Tablo 2 nitel özellikler; Tablo 3 önceki yayınlarla konumlandırma. |
| 2. Categories of O-ISAC | 3-6 | VLC, FSO ve photonic sensing sınıfları; Fig.2; Tablo 4. Fotonik destekli W/D-band örnekleri de bu çatıya dahil. |
| 3. Optical-fiber-based ISAC | 6-11; ilgili Tablo 5 s.12 | MoF, DOFS, WDM ile birlikte çalışma, ortak dalga biçimleri ve konumlandırma/haberleşme deneyleri. Fig.3-8, Tablo 5. |
| 4. System architecture, waveform designs and advantages | 11-13 | FSO/IM-DD ağırlıklı genel mimari; PPM, LFM-CPM ve OFDM. Fig.9-10. |
| 5. Key fundamentals | 13-20 | OPA/MEMS/donanım; metrikler; hibrit tasarım; optik OFDM; çoklu hüzme; kaynak çoğullama; öğrenme; fiber kanalından algılama. Fig.11-17, Tablo 6-7. |
| 6. O-ISAC applications | 20-29 | IoT, kuantum ağları, UAV, robotlar, sağlık, gaz izleme, köprüler ve araçlar. Fig.18-25. |
| 7. Open research issues and future aspects | 29-32 | Çok parametre, tradeoff, DSP, ortam dayanıklılığı, gerçekçi model, alanlar arası iletim, ortak tasarım, ML/FL/GAI ve standartlaşma. Tablo 8-9. |
| 8. Conclusion ve beyanlar | 32 | Genel kapsamın yeniden özeti, yazar katkıları ve çıkar çatışması beyanı. |
| Ek, veri beyanı, kaynakça | 33-37 | Tablo 10 kısaltmalar; s.34 veri beyanı; [1]-[174] kaynaklar. |

### Sınıflandırma ve fiziksel kapsam

VLC, FSO ve photonic sensing ana üçlüsü, fiberin ayrıca işlendiği bir üst sınıflandırma oluşturuyor. Ancak sınıflandırma tek bir fiziksel ölçüte dayanmıyor: VLC/FSO yayılım veya uygulama türüyken photonic sensing donanımı, fiber algılamasını ve fotonik destekli mikrodalga sistemlerini de kapsıyor. Bu nedenle bir sistemi kaydederken optiğin rolünü ayrıca belirtmek gerekiyor: hava/su ortamındaki optik taşıyıcı, fiberde haberleşme ve çevresel algılama, RF dalgasını üreten/işleyen fotonik ön uç veya optik sensörle desteklenen RF haberleşmesi.

Örneğin s.4-6'daki 28 GHz, 96.5/97.5 GHz ve D-band sonuçları fiber ve fotonik donanım içerse de kablosuz bölümde RF/mmWave/sub-THz taşıyıcı kullanıyor. Bunları FSO kanalındaki optik haberleşme sonuçlarıyla aynı sınıfa kaydetmek yanıltıcı olur. S.21-22'deki quantum-transformer örneği de kuantum anahtar dağıtımı deneyi değil, mmWave hüzme tahmininde kuantum öğrenme örneğidir.

### Fiberde birlikte çalışma ve gerçek ortak tasarım

DOFS bölümü Rayleigh tabanlı DAS, Brillouin tabanlı sıcaklık/gerinim ve Raman tabanlı sıcaklık algılamasını açıklıyor. Haberleşmenin eşitleyerek gidermeye çalıştığı kanal değişimleri, algılama açısından çevresel bilgi taşıyabiliyor (s.7-9).

WDM örneğinde algılama ve haberleşme aynı fiberde ayrı kanalları kullanıyor. [52] üzerinden 36.8 Tbps ile saha uygulaması anlatılıyor (s.8-9). Ortak fiber kullanımı ile aynı dalga biçiminin çift görevli kullanımı arasındaki ayrım s.9-10'da açıkça tartışılıyor. Ayrılmış algılama kanallarının spektrum maliyeti ve güçlü probların doğrusal olmayan etkileri temel tradeoff.

[59] örneğinde LFM probları haberleşme çerçevelerine yerleştiriliyor: 60 GBaud 16-QAM ile 0.5 m uzamsal çözünürlük (s.10). GBaud simge hızıdır; bit hızına sessizce dönüştürülmemelidir. [10] örneğinde LFM taşıyıcı üzerine PAM4 yükleniyor; aynı spektrum/fiberde haberleşme ve titreşim algılama yapılıyor. Derleme 56 Gbit/s, 24.5 km fiber, 4 m uzamsal çözünürlük ve 42 kHz etkin örnekleme raporluyor (s.11). Aynı anlatımda optimum launch power farkı 7 dB ve iki sistem kendi optimum güçlerinde karşılaştırıldığında 7% FEC eşiğinde yaklaşık 1.3 dB kazanç var. Bunlar aynı tür kazanç değildir. Yaklaşık 1.25 dB algılama kaybının tam ölçütü bu derlemeden tek başına açık biçimde yeniden kurulamaz.

### Deneysel karşılaştırma tabloları

Tablo 5 (s.12) dokuz optik kablosuz haberleşme/konumlandırma örneğini yıl, modülasyon, konumlandırma algoritması, veri hızı, konumlandırma doğruluğu, verici/alıcı ve test hacmiyle karşılaştırıyor. Deney alanlarının boyutu ve alıcı geometrisi var; ancak her satır için aynı hata istatistiği, persentil, veri hızının net/brüt niteliği ve çalışma koşulları sağlanmıyor. Bu tablo bir performans sıralaması veya meta-analiz değildir.

[29] metin açıklamasında dört optik antenli sistemin pre-FEC hızı 12 Mbps, BER'i 3.8 × 10^-3 altında ve deneylerin %90'ında hata 5.9 cm altında veriliyor (s.11). Tablo hücresinde yalnız 5.9 cm yazıyor; metindeki persentil bilgisi mutlaka korunmalı. [70] için metinde 8 cm altında, tabloda 8 cm yazması da eşik ile çıplak sayının farklı ifade edildiğini gösteriyor.

Tablo 6 (s.17) iletişim merkezli, algılama merkezli ve kaynak çoğullamalı MWP düzenlerini co-frequency/co-time/co-space/no-tradeoff işaretleriyle karşılaştırıyor. Tablo 7 aynı sayfada yedi MWP örneği için Gbps ve cm değerleri sunuyor. Her üç tablonun bütün satırları **EXPERIMENT_TABLES.json** dosyasında özgün birimleri ve işaretleriyle korunmuştur. Bu dosyadaki sayılar derlemeden aktarılmış ikincil kayıtlardır.

### Dalga biçimleri ve donanım

IM/DD dalga biçiminin gerçek ve negatif olmayan olması gereği, RF'deki karmaşık tabanbant biçimlerinin doğrudan aktarılmasını kısıtlıyor. PPM enerji verimliliği/ToF; LFM-CPM zarf ve mesafe kestirimi; OFDM ise alt taşıyıcılar, veri hızı ve algılama kaynak paylaşımı üzerinden açıklanıyor (s.12-15). DCO-OFDM'nin DC bias maliyeti ile kırpma gürültüsü; ACO/ADO/EADO/LACO ve diğer biçimlerin kaynak tahsisi farkları tartışılıyor. SIC'nin haberleşme alıcısında çalışması aynı iptal adımının algılama yankısında doğrudan uygulanacağını garanti etmiyor.

OPA, MEMS ve diğer hüzme yönlendirme teknolojilerinde küçük hacim ve dayanıklılık hedefleniyor. Fig.9'daki atmosferik ve DC-bias içeren mimari tüm fiber/koherent/fotonik RF sistemlerine genellenebilen evrensel bir devre değildir. S.13'te [75] için haberleşme ve hız çıkarımı bağlamında 50 m/200 m değerleri veriliyor; bunlar eşzamanlı tek ISAC çalışma noktası diye birleştirilmemeli, özgün yayındaki deney düzenleri ayrı incelenmeli.

### Metrikler ve tradeoff düşüncesi

Haberleşme ölçütleri BER, SINR, veri hızı, spektral/enerji verimliliği, gecikme ve kapasite; algılama ölçütleri hata, MSE, CRB, tespit ve yanlış alarm olasılığı. Fig.12 ve s.14, mutual information ve joint communication-sensing probability (JCSP) üzerinden ortak değerlendirmeyi tartışıyor. JCSP, iki gereksinimin birlikte sağlanma olasılığı olarak anlatılıyor. Bu, bütün platformlar ve görevler için kabul edilmiş evrensel metrik sunulduğu anlamına gelmiyor.

Hibrit RF/optik bölümü kapsam/engellenme dayanıklılığı ile optik bant genişliği/hassasiyetini birleştirmeyi amaçlıyor. Ana kaynaklar güç, zaman, frekans ve uzay. S.17'deki DL/RL açıklamaları çoğunlukla yöntem potansiyeli; her önerinin O-ISAC donanımında gerçek zamanlı doğrulandığı sonucu çıkarılamaz.

### Kanal bilgisinden algılama ve uygulamalar

S.18-20 fiberde kanal izleme, göz diyagramları ve polarizasyon bilgisiyle algılama yapmayı ele alıyor. [107] örneğinde CO-OFDM uçtan uca deneyde %100 dinleme tespiti ve %92.76 konumlandırma doğruluğu raporlanıyor; bir normal durum ve 20 dinleme durumu, 0-90 km konumlar ve %5/%10 ayırma oranları belirtiliyor. Başarı yüzdeleri bu sınıflandırma düzenine aittir; genel ağ güvenlik garantisi değildir.

Kuantum ağları için [117] örneği 10 km'de kullanıcı başına yaklaşık 0.7 Mbps secret key rate, sekiz kullanıcı kapasitesi, 0.20 m uzamsal çözünürlük ve 1-2 kHz titreşim yanıtı veriyor (s.21). Secret key rate klasik veri hızıyla aynı ölçüt değildir. Aynı bölümdeki [123] mmWave beam prediction örneği ise konum verisi için 0.8832, multimodal veri için 0.9124 distance-aided accuracy bildiriyor.

UAV örneği algılama ile APT/haberleşme kaynaklarını TDM üzerinden birleştiriyor; FoV büyütmenin bağlantı dayanıklılığı ile hız üzerindeki maliyeti tartışılıyor (s.22-23). Robotik örneği [139] ekran-kamera haberleşmesi ile kamera algılamasını ROS içinde birleştiriyor; Fig.20'de EKF ile yörünge/frenleme karşılaştırması var. Grafikten yeni sayılar üretilmedi.

Sağlık örneği [152] SiN/mikrohalka tabanlı optik algılama ve haberleşme demonstrasyonudur; s.25'teki deney koşulları su ve NaCl çözeltileridir. Klinik tanısal başarı deneyi olarak kaydedilmemiştir. Gaz örneği [156] MIR optik haberleşme ve absorpsiyonla H2S algılamayı ortak kaynakta birleştiriyor. Fig.22'de artan konsantrasyonun haberleşme BER'i üzerindeki etkisi anlatılıyor. S.26'da %10 H2S için BER'in FEC eşiği altında kaldığı bildiriliyor; bu veri endüstriyel saha doğrulaması veya belirli uzun menzil kanıtı sayılmamalıdır.

Köprü/fiber sensör ağı ve araç/aydınlatma/LiDAR örneklerinde gerçekleşmiş deney, mimari fikir ve gelecekte önerilen uygulama metinleri iç içe. Sensör verisini bir fiber üzerinden iletmek ile haberleşme taşıyıcısından ek algılama çıkarmak ayrı entegrasyon türleridir (s.26-29).

## Kaynak içi dikkat noktaları

1. **Deney varlığına ilişkin genelleme:** S.30'da sistemlerin yalnız teori ve simülasyonla doğrulandığı yazarken s.8-12 saha ve laboratuvar örnekleri sunuluyor. Daha savunulabilir okuma, ölçekli saha ve endüstriyel doğrulamanın sınırlı olduğudur; deney olmadığı iddiası doğrudan alınmamalıdır.
2. **[108]/[109] eşlemesi:** S.18'de [108] ML/polarizasyon derlemesi olarak anlatılıyor; s.36'daki [108] Naeem vd.'nin OFDR ve bandwidth-division multiplexing çalışması. ML/polarizasyon derlemesine benzeyen başlık [25]'te bulunuyor. S.19-20 ve Fig.17'de [109] ile anlatılan BDM sisteminde de kaynak eşlemesi inceleme gerektiriyor. Burada kaynak numaraları sessizce düzeltilmedi.
3. **Tablo 9 [43] satırı:** S.32'de ionic liquids (ILs) ifadesi geçiyor; s.6'daki MoF/polarizasyon anlatısıyla uyuşması belirsiz. Bunun interleaver terimi olup olmadığı özgün [43] görülmeden kesinleştirilmedi.
4. **Tablo 6 işaretleri:** TDM/FDM co-frequency/co-time işaretleri, s.17'deki zaman ve frekans bölüşümü açıklamasıyla potansiyel olarak uyuşmuyor. İşaretler aynen korundu; açıklama EXPERIMENT_TABLES.json içinde.
5. **IM/DD kapsamı:** Tablo 1-2'de O-ISAC için verilen gerçek/negatif olmayan ve IM/DD nitelikleri, metnin başka yerlerinde anlatılan koherent/fotonik RF örneklerinin tamamı için tek başına yeterli tanım değildir.
6. **Referans numarası kanıt değildir:** Örneğin s.29'daki çok parametreli fiber algılama cümlesinin [12] atfı, kaynakçadaki optik kablosuz ortak dalga biçimi başlığıyla doğrudan uyuşmuyor. Birincil kaynağa gitmeden aynı atıfla iddia taşınmamalıdır.
7. **Başlık ve dil hataları:** s.3 paper outline'da Section 2 tekrarı; Tablo 8 başlığında O-SAC; Tablo 10'da DCO açılımı, TSG ve MAR gibi işaretlemeler var. Bunlar teknik kavram sözlüğüne otomatik olarak doğru kabul edilerek aktarılmamalıdır.

Bu noktalar tam bir atıf denetiminin sonucu değil, okuma sırasında PDF içinde belirlenen somut sorunlardır. Dış kaynak düzeltmesi yapılmadı.

## Veri varlığı ve saklama sınırı

S.34'teki Data availability beyanı: **“No data was used for the research described in the article.”** PDF içinde ek dosya bulunmadı. Dolayısıyla bu çalışmaya ait yeni bir ham deney veri seti teslim alınmış değildir. Korunan materyal: özgün PDF, tam metin, sayfa metinleri, PDF içi bağlantılar, kaynakça sayfaları, 37 sayfanın görselleri, bu notlar, tablo/şekil dizini ve seçili veri/iddia kayıtlarıdır. Harici makale, kod veya veri seti indirilmedi. Tablo ve metin değerleri birincil çalışmaların yeniden doğrulanmış sonuçları sayılmaz.

## Survey'imizle sonraki görüşme için tespit

Bu makale, geniş O-ISAC platform kapsamı, fiber/DOFS, deney tabloları, waveform, metrik, ML ve uygulama çeşitliliğini zaten birlikte sunuyor. Bu nedenle çalışmamızın ayrımını yalnız bu konu başlıklarını kapsamak üzerinden kurmak yeterli görünmüyor. Bu cümle iki belgeyi okumaya dayalı bir konumlandırma gözlemidir; mevcut manuscript'e değişiklik, yeni özgünlük iddiası veya kapsam kararı uygulanmadı. Sonraki adım kullanıcıyla birlikte belirlenecek.
