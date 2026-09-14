# COMST yerel arşivinde Section II işlev ve akış karşılaştırması

Tarih: 2026-09-07. İnceleme salt okunur yapılmıştır; makale dosyaları değiştirilmemiştir.

## Kapsam ve yöntem

`C:\GH\OISAC_PRISMA_COMST\data\corp_std` altındaki 77 Markdown dosyasının çalışma başlığı ve Section II başlığı tarandı. Bu, 77 çalışmanın tamamının ayrıntılı okunması anlamına gelmez. Konusal/işlevsel yakınlık için altı örneğin Section II metni, girişteki amaç/organizasyon bağlantıları ve sonraki bölüm geçişleri okundu: COMST_014, 026, 044, 054, 067, 073. Envanter: `std_structure_inventory.json`.

II numarası tek başına eşdeğerlik kurmaz. Arşivde II; fundamentals, system model, preliminaries, context, related work, applications, architecture, standards/timeline veya motivation/contributions olabilir. Örneğin COMST_073'te teknik bileşen öğretimi III'e; COMST_067'de fizik/kanal temelleri IV'e taşınır. Bu ikisi kapsam farkını göstermek için değerlendirilmiştir.

Sayım `std_structure.py` ile yerel Markdown üzerinden yaklaşık anlatı kelimeleri olarak yapılmıştır. Başlık satırları, tablo hücreleri, şekil/tablo altyazıları, görsel işaretleri, atıflar, gösterim ve metin içi matematik temizlenmiştir; açıklayıcı gövde ve madde metinleri tutulmuştur. COMST_067'nin Fig. 3'ündeki OCR ile metne giren bölüm-planı kutuları (135–189) ayrıca dışlanmıştır. Metin içindeki bazı küçük ara başlık etiketleri ve OCR birleşik kelimeleri sayımı birkaç kelime etkileyebilir. Bunlar TeX/texcount ile birebir aynı yöntem değildir; sunumda yuvarlamak gerekir.

| ID | Section II | Yaklaşık anlatı kelimesi | İlk paragraf | Gövde sınırı |
|---|---|---:|---:|---|
| COMST_014 | System Model | 840 | 53 | 101–149 |
| COMST_026 | Preliminaries on OWC Systems, Networks, and Standards | 4050 | 119 | 113–263 |
| COMST_044 | ISC System Model | 1780 | 56 (II-A; ayrı II girişi yok) | 127–243 |
| COMST_054 | Optical Wireless Communication Systems | 920 | 154 | 197–232 |
| COMST_067 | Overview of THz-Based 6G Systems | 2400 | 56 | 123–272 |
| COMST_073 | Context | 3930 | 51 (II-A; ayrı II girişi yok) | 53–167 |

Bu altı örnekten evrensel COMST hedefi/ortalaması türetilmemelidir. 026'nın network/standards kapsamı, 073'ün geniş kullanım gerekçesi/aydınlatma öğretimi ve 067'nin tarih/spektrum turu metni uzatmaktadır.

## 1. COMST_014: A Survey on Indoor Visible Light Positioning Systems: Fundamentals, Applications, and Challenges

Kaynak: `C:\GH\OISAC_PRISMA_COMST\data\corp_std\COMST_014\COMST_014.md`.

- Girişte vaat (95): homojen ve heterojen konumlama algoritmalarını; alıcı, accuracy, coverage, orientation bakımından karşılaştırma. Organizasyon (99) II'yi VLP'nin temeli olarak belirliyor.
- Açılış (103) VLC yararlarını kısaca anıyor, ardından sistem modelini PD ve kamera alıcıları üzerinden ayırıyor. Özgün kısa kesit: “The model is differentiated into two categories based on the type of receiver device employed”.
- Akış: A PD Based VLC (105) → LED/PD/camera temel farkı (107) → LoS/NLoS kazanç modeli (113–124) → LED ID/konum bilgisi ve PD ölçümünün konumlama algoritmasına girişi (126–128) → B Camera Based VLC (140) → rolling-shutter bilgi çıkarımı ve geometriyle konumlama (142–146).
- Kapanış (148) salt özet değil: blokaj, FoV, LED girişimi ve kamera işleme gecikmesi, iki alıcının konumlama karşılaştırması için hangi boyutların önemli olduğunu açıklıyor. III (150–156) artık VLC/VLP integrasyonu ve homojen sistem algoritmalarına geçebiliyor.
- Alınabilecek yöntem: cihaz tanımı → elde edilen gözlem → algoritma/performans sonucu. Donanım ayrımı sonraki karşılaştırma eksenlerinin gerekçesini oluşturuyor.
- Sınır: yalnızca VLP; koherent optik haberleşme/menzil hibridlerinin tamamı için ortak model değildir. Açılıştaki genel teknoloji övgüsü birebir örnek alınması gereken güçlü taraf değildir.

## 2. COMST_026: A Top-Down Survey on Optical Wireless Communications for the Internet of Things

Kaynak: `C:\GH\OISAC_PRISMA_COMST\data\corp_std\COMST_026\COMST_026.md`.

- Açılış (115) açık bir bölüm-yol haritasıdır: temellerin daha sonraki tartışma/analizleri anlamaya hizmet edeceğini söyler; sistem bileşenleri/performans → ağ katmanları → standartlar sırasını duyurur. Kesit: “to establish a fundamental background on the topic and facilitate a better perception of discussions and analyses”.
- Akış: A Taxonomy (159): Tx/Rx, FSO/VLC/OCC; B Networks (176): PHY'den application'a beş katman; C Standards (207); D Summary, Insights, and Open Problems (258).
- Bileşen bilgisi soyut bırakılmaz: LED/LD ışın yayılması mesafe/çok noktalı kullanımına; PD/camera bant genişliği ve FoV kullanım alanına; modülasyon enerji/verimlilik karmaşıklığı IoT düğümüne bağlanır (163–191).
- Son paragraf (262) standartların terrestrial ve pure-OWC odağını iki kapsam kısıtı olarak yorumlayıp sonraki ortam/hibrid incelemelerini gerekçelendirir. III (264) terrestrial IoT; IV (442) underwater IoT'ye geçer.
- Alınabilecek yöntem: bölümün sonunda tanımların sonuçlarını birkaç somut ayrımla göstermesi; sonraki sentezin neden ortam ve teknolojiye göre ayrıldığını okura açıklaması.
- Sınır: 4050 kelimenin büyük bölümü ağ katmanları ve standartlar içindir. O-ISAC teknik comparison framework'üne aynı hacmi veya ağ ayrıntısını taşımak gereksiz olur. Ayrıca bu örnek doğrudan “This section provides...” türü açılış kullanır: COMST'ta bunun hiç yapılmadığı söylenemez.

## 3. COMST_044: Integrated Sonar and Communication: A Survey

Kaynak: `C:\GH\OISAC_PRISMA_COMST\data\corp_std\COMST_044\COMST_044.md`.

- Girişte amaç/organizasyon (121–123): waveform/signal-processing yöntemlerini kategorize etmek, communication/detection metrikleriyle değerlendirmek, ardından simulation ile integrated performance kıyaslamak. II sistemi tanıtır; III/IV kanal/donanım kısıtlarını; V metrikleri; VI/VII tasarımları kurar.
- II başlığı (127) sonrası doğrudan A Types and Characteristics (129) gelir. Ayrı editoryal giriş yok. İlk paragraf (131) uygulamaya göre monostatic/bistatic ayrımı yapar. Kısa kesit: “Depending on the application scenario, ISC systems can be categorized as monostatic or bistatic/multistatic”.
- Ayrımın önemi hemen belirtilir (133–138): yerleşim; gidiş/dönüş kanal simetrisi; dalga biçiminin alıcı tarafından bilinirliği; senkronizasyon; işlem yükü. Ardından kapsam kararı fiziksel gerekçeyle verilir (148): monostatic tekniklerin bistatic'e doğrudan taşınamayacağını söyledikten sonra monostatic'i temel/temsilî düzenek seçer.
- Akış: A mimari → B Frame Structure (152; continuous/pulse tercihi ve rate/range/update trade-off'u 158) → C Received Signal Model (176; communication ve target echo yolları 178–238) → D Summary (240).
- Ara köprü (174) sinyalin özel biçiminin VI'da uygulama gereksinimleriyle seçileceğini söyler. Son paragraf (242) kurulmuş modelin kanal, donanım, waveform ve signal-processing sorunlarının sonraki incelemesini taşıdığını açıkça belirtir.
- Alınabilecek yöntem: fiziksel fark → tasarım sonucu → inceleme kapsamı → ölçüm/model → sonraki sentez. O-ISAC'a editoryal olarak en güçlü analog budur; sonar fiziksel formülleri optiğe doğrudan aktarılmaz.

## 4. COMST_054: Optical Wireless Communication in Atmosphere and Underwater: Statistical Models, Improvement Techniques, and Recent Applications

Kaynak: `C:\GH\OISAC_PRISMA_COMST\data\corp_std\COMST_054\COMST_054.md`.

- Giriş (189–193) ortamlar arasındaki kanal modellerini ve performans değerlendirmesini birlikte ele alma ihtiyacını tarif eder; organizasyon (195) ortak Tx/Rx temellerini sınırlamalar, deneyler, kanal modelleri ve iyileştirme yöntemleri için basamak yapar.
- Açılış (199) doğrudan sinyal zinciridir. Kesit: “OWCS utilize visible, Ultraviolet (UV) and IR light regions of the electromagnetic (EM) spectrum to establish high-speed communication links.” Ardından elektriksel veri → optik taşıyıcı/sürücü → kaynak/optik → atmosfer veya su → alıcı optiği/detektör → demodülasyon anlatılır.
- Akış: A Transmitter (201; LED/LD'nin mesafe/ışın/enerji seçimine etkisi 203–213) → B Receiver (215; IM/DD ve coherent işlem farkı, karmaşıklık ve kullanım koşulu 217–223) → C Benefits (225).
- Son cümleler (231) vaat edilen faydaları gerçekleştirmek için karşılaşılan kısıtlara yönlendirir; III açılışı (235) atmosfer/su ortamının absorption/scattering/turbulence/alignment/blockage kısıtlarını sıralar.
- Alınabilecek yöntem: herkesin aynı fiziksel sistemi hayal edebileceği bir sinyal yolu ile başlamak; bileşen özelliklerini doğrudan hangi kullanım koşullarını etkilediğine bağlamak. O-ISAC'ta ortak optik iletimden ayrı communication ve sensing observations'a geçiş için uygundur.
- Sınır: III'e geçiş son cümlede genel “challenges” bağlantısıdır; 044 kadar güçlü ve spesifik sentez köprüsü değildir. Kendi metnimizde yalnızca benefit listesiyle bitirmek yeterli olmaz.

## 5. COMST_067: Terahertz Communications and Sensing for 6G and Beyond: A Comprehensive Review

Kaynak: `C:\GH\OISAC_PRISMA_COMST\data\corp_std\COMST_067\COMST_067.md`.

- Survey amacı (121): THz communication/sensing sistemlerini tasarlamak/kurmak için gereken geniş görünümü vermek.
- Açılış (125) bölüm planını söyler. Kısa kesit: “this section summarizes the current state of the art in the related fields”.
- Akış A global 6G development (127) → B spectrum use (209) → C early THz exploration (259). Büyük ölçüde girişimler/tarih/standartlar ve spektrum bağlamıdır.
- II sonu (271) ilk THz standardizasyon deneyiminde biter. III (275) geniş spektrum ve küçük dalga boyunun communication/sensing uygulamalarına açtığı fırsatlarla geçişi yapar. Fiziksel ön bilgi IV'ün görevidir (372 başlığı; Fig.3 metni 143 bu görevi ayrıca açıklar).
- Kullanımı: Section II'nin tek bir COMST kuralına bağlı olmadığını gösteren karşı örnek. O-ISAC için tarih/6G turunu genişletme tavsiyesine dayanak değildir. Kullanıcının teknik Section II'siyle en güçlü doğrudan eşdeğer olarak sunulmamalıdır.
- QA: Fig.3'ün kutu metinleri 135–189 arasında paragraf olarak OCR edilmiştir. Temizlenmeden saymak II gövdesini yanlış büyütür.

## 6. COMST_073: Visible Light Positioning as a Next-Generation Indoor Positioning Technology: A Tutorial

Kaynak: `C:\GH\OISAC_PRISMA_COMST\data\corp_std\COMST_073\COMST_073.md`.

- Giriş boşluk/vaat (49): algoritmaların ötesinde tüm VLP sistemini kurmak için illumination, hardware, modulation ve positioning ön bilgisini sağlama. Organizasyon (51): II context/taxonomy; III components; IV algorithms; V concrete RSS-PD primer.
- Ayrı II giriş paragrafı yok; II-A Location-Based Services (55) ile açılır. Açılıştaki kısa kesit (57): “‘Location, location, location’ is a mantra that extends way beyond the world of real estate transactions.” Bu retorik dil seçeneğidir; bilimsel metnimizde zorunlu örnek değildir.
- Akış: A kullanım ihtiyacı → B indoor positioning seçenekleri/altyapı gereği (61–85) → C Rationale of VLP (87–105: cost/accuracy/coverage ve mevcut ışık altyapısı gerekçesi) → D Illumination Requirements (107–166).
- Kapsam açıkça uygulamadan türetilir (79): room-level self-positioning. D açılışı (109) ışığı konumlama için kullanmanın illumination uyumluluğunu da gerektirdiğini söyleyerek motivasyonu teknik kısıta çevirir.
- Son bölümler (160–166) flicker, uniformity, glare ve lamp selection'ın VLP tasarımına etkisini açıklar. III açılışı (170–172) birbirinden farklı Tx/Rx/modulation/algorithm/quality seçeneklerinden dolayı sistem taksonomisine ihtiyaç olduğunu anlatır.
- Alınabilecek yöntem: “bu teknolojiyi niçin kullanıyoruz?” sorusunu, “kullanınca hangi ölçülebilir ve pratik kısıtları devralıyoruz?” sorusuna çevirmek. O-ISAC'ta optical propagation/detection ayrımlarının ortak tasarım değerlendirmesini niçin gerekli kıldığı gösterilebilir.
- Sınır: 3930 kelimelik II context'tir; geniş motivasyon ve illumination ayrıntısını içerir. Bizim foundations kelime hedefimiz bununla eşitlenmemelidir.

## O-ISAC için aktarılabilecek editoryal karar

Kaynakların ortak yararlı davranışı tek bir kalıp cümle kullanmaları değil, gereken ön bilgiyi kendi inceleme sorularına bağlamalarıdır. Somut model örneklerinde bu ilişki en görünür biçimde şöyledir: fiziksel sistem/ölçüm → belirleyici fark → tasarım ve performans sonucu → sonraki sınıflandırma/karşılaştırma ihtiyacı.

O-ISAC açılışında makalenin “bu bölümde yapılacaklar” listesinden önce, aynı optik iletimin iletişim verisini ve fiziksel çevre bilgisini nasıl taşıdığı ortaya konabilir. Ardından doğrudan/koherent/görüntülemeli algılamanın hangi gözlemleri erişilebilir kıldığı ve kanal/yerleşim farklarının iki işlevi nasıl farklı etkilediğiyle inceleme gereği kurulabilir. Son cümlede yalnız bu temellerin neden daha sonraki architecture/performance karşılaştırmasını taşıdığı söylenir. Kaynaklar bu sıralamayı destekleyen editoryal analoglardır; O-ISAC'a özgü teknik savlar kendi birincil kaynaklarıyla desteklenmelidir.

Güçlü taşıyıcılar 044 (fiziksel düzenek → tasarım etkisi → kapsam), 054 (optik sinyal zinciri), 014 (alıcı gözlemi → algoritma/performans sınırı). 026'nın bölüm sonunda teknik ayrımların sonraki ortam incelemesini gerekçelendirmesi eklenebilir. 073/067 daha geniş bağlam bölümleri olarak ayrılmalıdır.

1338 kelimelik mevcut Section II bilgisi ana incelemeyi yürüten ajanın texcount sonucudur. Yukarıdaki arşiv sayımlarıyla karşılaştırıldığında bölümün sırf kısa/uzun olması esas editoryal problem olarak görünmez. 840–1780 kelimelik daha dar teknik eşdeğerler vardır; 4 bin kelime civarındaki örnekler farklı işler yapmaktadır. Hedef, teknik motivasyonu belirginleştirmek ve her altbölümün sonraki senteze ne kazandırdığını birer somut sonuçla göstermek olmalıdır.
