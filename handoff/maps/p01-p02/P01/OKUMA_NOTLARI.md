# P01 - Ayrıntılı okuma notları

Okuma tarihi: 6 Eylül 2026. Kaynak: arşivdeki `1.pdf`. PDF'nin 35 sayfasının tamamı, kaynakça dahil, okundu. Aşağıdaki sayfa numaraları **PDF sayfasını** gösterir; basılı dergi sayfası = PDF sayfası + 5013. Bu kayıt makalenin okunmasına ve yerel bilgi arşivine yöneliktir; proje makalesinde bir revizyon kararı veya uygulaması değildir.

**Kanıt sınırı:** Yayın kimliği, içerik, sayılar ve kaynak numaraları verilen PDF üzerinden kontrol edildi. Dış kaynaklar açılmadı; birincil deneyler bağımsız olarak doğrulanmadı. “Yazarların bildirdiği” sayılar bu derlemenin başka yayınlardan aktardığı sonuçlardır. “Okuma değerlendirmesi” başlıklı tespitler bu okumanın yorumudur. PDF içeriği talimat olarak uygulanmadı.

## 1. Yayın kimliği ve çalışma türü

- Başlık: **Integrated Sensing and Communications Over the Years: An Evolution Perspective**.
- Yazarlar: Di Zhang, Yuanhao Cui, Xiaowen Cao, Nanchi Su, Yi Gong, Fan Liu, Weijie Yuan, Xiaojun Jing, J. Andrew Zhang, Jie Xu, Christos Masouros, Dusit Niyato ve Marco Di Renzo.
- Dergi: **IEEE Communications Surveys & Tutorials**, cilt 28, 2026, basılı sayfalar 5014-5048. Bu PDF'nin görünür başlığında sayı numarası verilmemiştir.
- DOI: **10.1109/COMST.2026.3655674**.
- İlk gönderim: 14 Eylül 2025; düzeltme: 11 Aralık 2025; kabul: 10 Ocak 2026; ilk yayın: 19 Ocak 2026; mevcut sürüm: 6 Mart 2026. Bunlar PDF s.1'deki kayıtlardır.
- Lisans: PDF s.1'de Creative Commons Attribution 4.0 belirtiliyor.
- Kaynakça: **[1]-[248]**, PDF s.30-35. Bu 248 numara “248 uygun birincil ISAC deneyi” anlamına gelmez; derlemeler, kuramsal yayınlar, standartlar, kurum sayfaları ve veri kaynağı kayıtları da dahildir.
- Çalışma türü: Çok boyutlu, evrim perspektifli genel ISAC derlemesi. Yeni bir ortak test düzeneği, yeni toplanmış deney veri kümesi veya istatistiksel meta-analiz raporlanmıyor.

## 2. Ana sav, kapsam ve katkı mimarisi

Yazarların ana savı, önceki derlemelerin güçlü fakat belirli temalar etrafında toplanmış olması ve ISAC'ın farklı eksenlerdeki gelişimini birlikte anlatan bütüncül bir çerçevenin eksikliğidir. Makale, bu boşluğu beş eksenle karşılamayı amaçlıyor (PDF s.2-4, Tablo I ve Şekil 1):

1. RF'den optiğe ve hibrit RF-optik mimarilere genişleyen çalışma spektrumu.
2. Tek hücreden çok hücreli ve uzay-hava-yer ağlarına gelişen ağ mimarisi.
3. Tek modaliteden çok modaliteli algılamaya, uç zekâya ve görev odaklı işleme geçiş.
4. Haberleşme güvenliği, algılama mahremiyeti ve algılama yardımlı güvenlik.
5. 3GPP, IEEE ve ITU standartlaşması.

**Tablo I (s.3)** [5]-[30] arasındaki 26 önceki yayını bu beş kapsam boyutu ve uygulama senaryoları üzerinden karşılaştırıyor. İşaretler, önemli/yapılandırılmış kapsam, kısmi kapsam ve açıkça ele alınmama anlamına geliyor. Bunlar yazarların kapsam değerlendirmeleridir; bağımsız kalite puanı veya literatür tarama sonucunun yeniden üretilebilir kodlaması değildir. Tablodaki “systematic coverage” ifadesi de tek başına derlemenin sistematik inceleme yöntemi kullandığını göstermez. Kendi satırlarında bütün boyutlar işaretli. Optiğe ilişkin özel yayın [67], ana metinde kullanılsa da bu 26 satırlık tabloda yer almıyor; dolayısıyla tabloyu bütün optik derlemelerin eksiksiz karşılaştırması olarak okumamak gerekir.

## 3. Bölüm bölüm içerik haritası

### I. Giriş - PDF s.1-3

Kaynak ve donanım paylaşımı, radar ve iletişimin ayrı gelişmesinin maliyeti, 5G/6G uygulamaları ve endüstriyel ilgi üzerinden motivasyon kuruluyor. İlgili survey'ler dalga biçimi, kanal, RIS, ağ işbirliği, yapay zekâ ve güvenlik temalarıyla gruplandırılıyor. Yenilik iddiası tek bir fiziksel yöntemden çok bu temaların “evrim” anlatısında birleştirilmesine dayanıyor.

### II. RF ve optik çalışma spektrumu - PDF s.3-8

**RF alt bölümü (s.3-5):** Taşıyıcı üretimi, yükselticiler, filtreler, ADC ve DSP zinciri tanıtılıyor; anten merkezli araştırmaların ötesinde bütün ön ucun dikkate alınması gerektiği söyleniyor. Merkezi sık/seyrek diziler, dağıtık diziler, hareketli/akışkan antenler ve RIS karşılaştırılıyor. Tablo II, kapsama, donanım maliyeti, senkronizasyon karmaşıklığı ve temel sınırlamaları özetliyor. Seyrek dizilerde RF zinciri tasarrufu, dağıtık dizilerde uzamsal çeşitlilik ve konumlama; hareketli antenlerde yeniden konumlama kazanımı; RIS'te kanal kestirimi ve yeniden yapılandırma gecikmesi tartışılıyor. Yazarlar s.5'te iyi menzil çözünürlüğünün temel belirleyicisinin taşıyıcı frekansından ziyade kullanılabilir bant genişliği olduğunu açıkça belirtiyor.

**Optik alt bölümü (s.5-7):** VLC, FSO ve “photonic sensing” üçlüsü kuruluyor. Ayrıntılar aşağıdaki özel bölümde kaydedilmiştir.

**Hibrit RF-optik (s.7-8):** Üç birleşim düzeyi öneriliyor: kontrol/ağ katmanında gevşek eşgüdüm; paylaşılan dalga biçimi ve kontrol ile sıkı fiziksel entegrasyon; optik algılama veya geri taşıma ile RF uç iletişiminin işlevsel paylaşımı. Görev ve kaynak tahsisi, hava/engellenme koşullarına göre mod seçimi, mod değiştirme maliyeti, senkronizasyon, grup gecikmesi, ışın hizalama, SWaP ve donanım doğrusal olmama etkileri tartışılıyor. RF'nin geniş kapsama ve engellenmeye dayanımı ile optiğin dar ışın ve yüksek kapasitesinin tamamlayıcılığı vurgulanıyor. Soru biçimindeki dersler; ortak performans amaçları, modaliteye uyarlanan zekâ, eşzamanlı kalibrasyon ve zamanlama üzerinde yoğunlaşıyor.

### III. Tek hücreden çok hücreli ağlara - PDF s.8-18

**Dalga biçimleri (s.8-14):** Önce zaman/frekans/uzay/kod bölüşümlü ortogonal kaynak tahsisi; ardından sensing-centric, communication-centric ve joint co-design ayrımı yapılıyor. Tablo IV, ortogonal yöntemleri performans/avantaj/sınırlama sütunlarıyla; Tablo V, benzerlik, PAPR, frekans, enerji, adalet, WMMSE, SINR ve kapasite amaçlarını karşılaştırıyor. FMCW'nin düşük örnekleme gereksinimi ile sınırlı veri aktarımı; OFDM'nin uyumluluk ve esnekliği ile yan lob/Doppler hassasiyeti; OTFS'nin gecikme-Doppler alanında ortak kullanım potansiyeli açıklanıyor.

Matematiksel çekirdek: FMCW (Eş.1, s.11), OFDM ve hedef gecikme-Doppler gözlemi (Eş.2-3, s.12), OTFS ifadesi (Eş.4), ağırlıklı iletişim/algılama karşılıklı bilgisi (Eş.5) ve toplam güç/bant genişliği ile asgari iletişim hızı altında algılama QoS optimizasyonu (Eş.6). S.13'te tespit olasılığı, menzil/açı CRB'si ve takip PCRB'si açıklanıyor. Bunlar bütün makalede yeni bir deneyle sınanan birleşik model değildir; kullanılan kuramsal çerçevelerin öğretici sentezidir. PDF metin çıkarımındaki denklem karakterleri bozulabildiğinden eşitlikler görsel sayfadan kontrol edilmelidir.

**Topoloji (s.14-17):** BS, UE, ek sensörlü UE ve pasif hedef izleme terminalleri; tek hücre içinde BS-UE işbirliği; çoklu BS monostatik/bistatik ortaklığı; makro-mikro hücreler; C-RAN/RRU yapısı; uzay-hava-yer bağlantıları ele alınıyor. Kazanımın karşılığında saat/frekans ofseti, veri taşıma, füzyon, hücreler arası girişim ve koordinasyon maliyeti doğuyor. Şekil 4-6 bu mimarileri görselleştiriyor.

**Dersler (s.17-18):** Ölçeklenebilir asenkron algılama ve gecikme-füzyon doğruluğu dengesi. Yerel algılama düğümleri, ara toplayıcılar ve çekirdek algılama işlevinden oluşan üç katmanlı yapıda ilk işleme/füzyonun uca taşınması anlatılıyor. Topoloji genişlemesinin optik ortamda ayrıca gösterilmiş olduğunu varsaymamak gerekir; bu bölümün kanıtı ağırlıklı olarak RF/hücresel çalışmalardır.

### IV. Tek modaliteden çok modaliteli uç algılamaya - PDF s.18-24

“Edge perception”, sensör, yerel işlem ve haberleşme modüllerinin birlikte çalışması olarak tanımlanıyor (Şekil 7). AI-enabled ISAC, ISAC-facilitated AI ve karşılıklı AI-ISAC synergy üçlüsü kuruluyor (Şekil 8). Sensing-enhanced iletişim için ışın seçimi, CSI, kamera/LiDAR/radar füzyonu; algılama için insan etkinliği, endüstriyel izleme ve hareketli araç örnekleri veriliyor. Yerel çıkarım ile federated learning'in dağıtık eğitimi birbirinden ayıran açıklama mevcut.

Sonraki aşama tekil hız/doğruluk metrikleri yerine görevin tamamlanmasına göre algılama-haberleşme-hesaplama tahsisi. Tablo VI; CNN, GNN, RNN, LSTM, transformer, gözetimli/gözetimsiz öğrenme, federated learning ve multi-agent learning örneklerini karşılaştırıyor. LLM'lerde sensör sinyalini metinleştirme, anlamsal çıkarım, edge/cloud/hybrid yerleşimi ve gecikme/enerji kısıtları anlatılıyor. Şekil 9 başka bir yayının RIS ışın oluşturma ağına, Şekil 10 Penetrative AI yapısına dayanıyor; P01'in kendi yeni sinir ağı deneyi değildir.

Veri alt bölümü hedef tanımlama, çok modaliteli toplama, temizleme/etiketleme ve kamusal paylaşım adımlarını anlatıyor. Tablo VII'de 10 veri kaynağı var: SDP, ImgFi, WiMANS, Radar Signatures of Human Activities, EyeFi, OPERAnet, MmWave Gesture Dataset, DeepSense 6G, WALDO ve M3SC. Bunlar RF, Wi-Fi/CSI, mmWave, kamera, LiDAR vb. bileşimlerdir; tamamını “optik kablosuz ISAC veri kümesi” diye adlandırmak uygun değildir. Simülasyonun kontrol edilebilirliği ile saha verisinin gerçekçilik/çeşitliliği karşılaştırılıyor. Birleşik donanım ve heterojen veri füzyonu açık sorun olarak kalıyor.

### V. Güvenlik ve mahremiyet - PDF s.24-26

Şekil 11 iki farklı tehdidi ayırıyor: haberleşme içeriğinin sızması ve hedef/ortam bilgisinin yetkisiz algılanması. İletişim güvenliğinde yapay gürültü ve yönlü modülasyon; algılama mahremiyetinde ışın oluşturma, CSI/konum anonimleştirme ve pilot maskeleme; algılama yardımlı güvenlikte tehdit konumuna uyarlanan PLS ve covert communication çerçeveleri gözden geçiriliyor. Yazarlar, yüksek katman şifrelemesinin pasif fiziksel algılama sızıntısını tek başına çözmediğini vurguluyor. Mükemmel saldırgan konumu/CSI varsayımları, kısıtlı prototip doğrulaması ve ortak çapraz alan tehdit modellerinin yetersizliği sınır olarak belirtiliyor. Burada özel optik ISAC güvenlik deneyi veya optik kaynaklardan kurulmuş ayrı bir karşılaştırma sunulmuyor.

### VI. Standartlaşma - PDF s.26-29

3GPP Rel-15 temel NR, Rel-16 konumlama, Rel-17 yüksek frekans/MIMO, Rel-18 gelişmiş konumlama ve Rel-19+ ISAC servisleri üzerinden anlatılıyor. Şekil 12 zaman çizgisi, Şekil 13 Multi-RTT mesajlaşması. IEEE 802.11bf Wi-Fi sensing ve ITU IMT-2030/spektrum başlıkları tamamlayıcı rol üstleniyor. Uygulama güdümlü standartlaştırmada alçak irtifa/UAV örneği öne çıkıyor (Şekil 14). Metin, güncel standart durumu için güvenilir tek başına kontrol listesi değildir: aynı PDF içinde tarih ve kaynak eşleme sorunları mevcut, aşağıda kaydedildi.

### VII. Sonuç ve gelecek yönler - PDF s.29-30

Genel yönler; nesne/saçılma/clutter içeren ortak kanal modeli, çok amaçlı kaynak tahsisi ve yerleşik güvenlik/mahremiyet. Başarıyı yalnız fiziksel uygulanabilirlikten ziyade uygulama yararı ve sistem dayanıklılığıyla ilişkilendiriyor. Yeni bir nicel birleştirilmiş sonuç veya deneysel benchmark üretilmiyor. S.30'da yazar kurumları ve kaynakça başlıyor; kaynakça s.35'te [248] ile bitiyor.

## 4. Optik ISAC için ayrıntılı kayıt

### 4.1. Üçlü optik sınıflama

**VLC (s.6, Tablo III s.7):** LED verici, fotodetektör veya görüntü sensörü alıcı; IM/DD, optik OFDM ve CAP. Tablo taşıyıcı aralığını **400-700 nm** veriyor. Algılama görevleri ortam izleme, hareket ve uzamsal haritalama; s.6'da iç mekân konumlama da ayrıntılı anlatılıyor. Aydınlatmayla uyumlu dalga biçimi ve ortak işleme [67], LED çift modlu prototip [68], çok bantlı CAP ve RSS konumlama [69] örnekleri. LoS bağımlılığı, NLoS'ta kısa mesafe, ortam ışığı, engellenme/yayılma ve mobilite/hizalama sınırları vurgulanıyor. Bu anlatı “VLC yalnız LoS'ta çalışır” sonucu vermez; aynı PDF [81]'de NLoS VLC çalışması da içeriyor.

**FSO (s.6-7):** Yakın kızılötesi lazer, dar ışın, LoS kapasitesi ve mesafe/hız/açı çıkarımı. Tablo III taşıyıcı aralığını **740-1600 nm** olarak yazıyor; bu makalenin tablo aralığıdır, tüm FSO teknolojilerinin evrensel sınırı diye kullanılmamalı. Temel limitlerde kapasite-distortion, ML/MAP kestirim ve Bayesian CRB [70]; kaynak tahsisi ve clipping [71], [80]; LFM-CPM [76] yer alıyor. Türbülans, sis/yağış/duman, pointing loss, hizalama, FoV, saha ölçeklenmesi sorunları belirtiliyor. “Sıklıkla Tbit/s” ifadesi genel FSO kapasite söylemidir; bu paragrafta eşzamanlı optik ISAC için düzenek/mesafe/BER ile verilmiş belirli bir Tbit/s deney sonucu yoktur.

**Photonic sensing (s.6-7):** LiDAR, fiber titreşim/deformasyon ve diğer hassas optik ölçümler aynı başlıkta; ardından fotonik destekli W-band/mmWave ISAC deneyleri örnekleniyor. [73]-[75] örneklerinin kablosuz ölçüm frekansları RF/mmWave'dir. Tablo III yer değiştirme, titreşim ve strain/optical time-domain reflectometry görevlerini; maliyet, ölçek, çevresel gürültü ve “static sensing” sınırını veriyor.

**Okuma değerlendirmesi:** Bu taksonomi spektral taşıyıcıyı, iletim ortamını ve ön uç teknolojisini tek düzeyde birleştiriyor. Optik hava kanalı, optik fiber algılama ve fotonik destekli RF hava kanalı ayrımını korumadan Tablo III'ü doğrudan kapsam tanımı olarak almak farklı kanıt ailelerini karıştırır. “Static sensing” satırını tüm LiDAR/fotonik algılamaya genellemek de metindeki hız/radar örnekleriyle gerilim yaratır. Bu, P01'in geniş vizyonuna ilişkin bir sınıflama değerlendirmesidir; kapsamı yeniden belirleyen proje kararı değildir.

### 4.2. Optik bölümdeki sayısal veriler ve izlenebilirlik

| PDF yeri | P01'in bildirdiği değer | P01'de atıf | Doğru okuma sınırı |
|---|---|---|---|
| s.5, II-A özeti | W-band **48.04 Gbps**, **1.02 cm** algılama çözünürlüğü, **16 GHz** bant genişliği | [64] | Fotonik destekli RF-W-band sonuç; optik hava-kanalı veri hızı değildir. P01 bunları tek cümlede beraber veriyor; ham veri yok. |
| s.5 | Yaklaşık **275 GHz**, **30 GHz** etkin bant, santimetre altı çözünürlük | [65] | Fotoniğin kullanıldığı THz-ISAC; farklı bant/düzenek. 48.04 Gbps örneğiyle ortak benchmark değildir. |
| s.6, VLC | **1.2 m × 1.2 m × 2.16 m** iç mekân; santimetre seviyesinde konumlama | [69] | P01 bu paragrafta belirli RMSE, güven aralığı veya aynı koşuldaki veri hızını vermiyor. “Santimetre seviyesi”ni keyfi bir sayıya dönüştürmemek gerekir. |
| s.6, photonic sensing | **47.54 Gbps**, radar tespiti | [74] | W-band mmWave, OFDM ve iki aşamalı taşıyıcı toparlama. P01 bu cümlede sayısal radar hatası/çözünürlüğü vermiyor. |
| s.6 | Tek kullanıcılı durumda **20 mm'den iyi menzil doğruluğu**; iki kullanıcılı algılamada desimetre seviyesinde çözünürlük; **28 GHz** | [75] | Doğruluk, çözünürlük ve kullanıcı sayısı ayrı koşullardır; tek bir ortak hata değeri değildir. |
| s.7, senkronizasyon | RF için sub-ns, optik ön uç için ps mertebesi | [83]-[84] çevresindeki tartışma | Yazarların mühendislik genellemesi; bütün RF/optik mimariler için ölçülmüş evrensel gereksinim değildir. |

**Önemli optik/hibrid kaynakların PDF'de görülen kimlikleri:**

- [67] Y. Wen, F. Yang, J. Song, Z. Han, *Optical integrated sensing and communication: Architectures, potentials and challenges*, IEEE Internet Things Magazine 7(4), 68-74, Temmuz 2024 (kaynakça s.31).
- [68] R. Zhang, Y. Shao, M. Li, L. Lu, Y. C. Eldar, *Optical integrated sensing and communication with light-emitting diode*, ICC Workshops 2024, 2059-2064 (s.31).
- [69] L. Shi, Z. Liu, B. Béchadergue, H. Guan, L. Chassagne, X. Zhang, *Experimental demonstration of integrated optical wireless sensing and communication*, JLT 42(20), 7070-7084, 15 Ekim 2024 (s.31).
- [70] A. Ghazavi Khorasgani, M. Mirmohseni, A. Elzanaty, *Optical ISAC: Fundamental performance limits and transceiver design*, 2024, arXiv:2408.11792 (s.31; P01'in aktardığı sürüm).
- [71] Y. Wen ve ark., *Optical wireless integrated sensing and communication based on EADO-OFDM: A flexible resource allocation perspective*, IEEE TWC 24(8), 6964-6979, Ağustos 2025 (s.31).
- [72] J. Bohata ve ark., *Performance evaluation of seamless 5G outdoor RoFSO transmission at 39 GHz*, IEEE PTL 34(1), 7-10, 1 Ocak 2022 (s.31).
- [73] B. Dong ve ark., *Photonic-based flexible integrated sensing and communication with multiple targets detection capability for W-band fiber-wireless network*, IEEE TMTT 72(8), 4878-4891, Ağustos 2024 (s.31).
- [74] H. Yan ve ark., *W-band photonic-aided mm-wave ISAC system enabled by a shared OFDM signal waveform and a two-stage carrier frequency recovery algorithm*, Optics Letters 49(18), 5280-5283, 2024 (s.31).
- [75] M. Lei ve ark., *Photonics-aided integrated sensing and communications in mmW bands based on a DC-offset QPSK-encoded LFMCW*, Optics Express 30(24), 43088-43103, 2022 (s.31).
- [76] Y. Wen ve ark., *Free space optical integrated sensing and communication based on LFM and CPM*, IEEE Communications Letters 28(1), 43-47, Ocak 2024 (s.31).
- [77] L. Ma ve ark., *On the hardware-limited sensing parameter extraction for integrated sensing and communication system towards 6G*, ICCT 2023, 451-455 (s.31).
- [78] Z. Huang ve ark., *Hybrid optical wireless network for future SAGO-integrated communication based on FSO/VLC heterogeneous interconnection*, IEEE Photonics Journal 9(2), 1-10, Nisan 2017 (s.31).
- [79] H. He ve ark., *Integrated sensing and communication in an optical fibre*, Light: Science & Applications 12(1), 25, Ocak 2023 (s.31).
- [80] Y. Wen ve ark., *Free-space optical integrated sensing and communication based on DCO-OFDM: Performance metrics and resource allocation*, IEEE IoT Journal 12(2), 2158-2173, Ocak 2025 (s.31).
- [81] P. Zhang, J. Wu, Z. Wei, Y. Sun, R. Deng, Y. Yang, *Channel modeling for NLoS visible light networks with integrated sensing and communication*, Optics Letters 49(11), 2861-2864, 2024 (s.32).
- [82] S. Phuchortham, H. Sabit, *A survey on free-space optical communication with RF backup: Models, simulations, experience, machine learning, challenges and future directions*, Sensors 25(11), 3310, Mayıs 2025 (s.32).
- [83] Y. Cui ve ark., *Retroreflective optical ISAC using OFDM: Channel modeling and performance analysis*, Optics Letters 49(15), 4214-4217, 2024 (s.32).
- [84] J. Jia ve ark., *Demonstration of radar-aided flexible communication in a photonics-based W-band distributed integrated sensing and communication system for 6G*, Chinese Optics Letters 22(4), 043901, 2024 (s.32).
- [85] E. Balti ve ark., *Mixed RF/FSO relaying systems with hardware impairments*, GLOBECOM 2017, 1-6 (s.32).
- [86] C. A. Gutiérrez ve ark., *Channel modeling for integrated sensing and communications in vehicular environments: Conceptualization and challenges*, IEEE Vehicular Technology Magazine 20(2), 104-113, Haziran 2025 (s.32).

Bu liste, dışsal bibliyografik doğrulama yapılmış temiz kaynakça değildir; P01'in referans zincirini korur.

## 5. Diğer seçilmiş nicel sonuçlar

Aşağıdaki kayıtlar makalenin kanıt stilini ve kapsamını anlamak içindir; optik performans havuzuna alınmış veriler değildir.

- S.4, [45]: Aynı açıklıkta yoğun ULA'nın **dörtte biri RF zinciri**; sub-0 dB SNR'de sum-rate ve DOA RMSE avantajı. Aynı sayfada [46]: seçim arama uzayında **dokuz büyüklük mertebesi azalma**, **0-20 dB** boyunca **%5'ten az** spektral verim kaybı. Dizilim ve baz yöntem bağımlılığı korunmalı.
- S.4, [50]: Kooperatif multistatik yapıda mono/bistatik karşılaştırmaya göre **%30'dan fazla RMSE azalması**. Tek bir genel ISAC kazanımı değildir.
- Tablo IV, s.9, [87]: Hedef tespit hatasında **%18.5 azalma**, **2.2 Gbps** aktarım. [94]: düşük SNR'de **30.1 dB** kazanç ve karşılaştırılabilir doğrulukta **3 dB SINR** kazancı. Satırların deney koşulları ortaklaştırılmamış.
- S.12, [117]: **%19.3** algılama doğruluğu ve **%8.6** iletişim kapasitesi iyileşmesi; [119]: **15 dB** sensing gain; [121]: **20 dB'ye kadar** yan lob bastırma; [124]: **%35'ten fazla** NMSE azalması. Bunlar farklı yöntem ve bazlarla verilmiş ayrı sonuçlar.
- S.15, [138]: **8 dB'ye kadar SINR** kazancı. [140]: radar bilgi hızında **%20'den**, iletişim spektral veriminde **%15'ten fazla** iyileşme.
- S.20, [176]: CSI tabanlı hafif HAR uygulamasında **2.1 MB** bellek, Raspberry Pi sınıfı donanımda **18 frame/s**. [183]: **%52** algılama maliyeti ve **%77** iletişim enerjisi azalması; [184]: **%25.6** algılama doğruluğu iyileşmesi, **%31.4** kanal kestirim hatası azalması.
- S.21, [203]: Cloud çıkarımı için tipik **>100 ms**, edge için **<50 ms**; [204]: beam prediction'da yaklaşık **%78 Top-1** ve **>%94 Top-3**. Bunlar model/düzenek bağımlı olarak aktarılan örneklerdir; gerçek zamanlılığın evrensel sınırı değildir.
- S.23, WiMANS [207]: **9.4 saat**, en çok **5 kullanıcı**, **9 günlük etkinlik**. OPERAnet [210]: yaklaşık **8 saat**, **2 iç mekân**, **6 katılımcı**, **6 etkinlik**. Veri kataloglarındaki “>” işaretleri ile anlatıdaki yaklaşık/eşit sayıların farkı korunmalı.

## 6. Yöntem, veri ve karşılaştırılabilirlik değerlendirmesi

**PDF'de görülenler:** Beş eksenli anlatı, önceki survey'lerle kapsam tablosu, 248 numaralı kaynak, öğretici eşitlikler, teknoloji/algoritma/veri kümesi karşılaştırma tabloları ve örnek yayınların nicel sonuçları. Bölümlerin çoğu bir özet ve araştırma soruları ile bitiyor.

**PDF'de raporlandığını saptamadığım öğeler:** Yeniden üretilebilir bibliyografik arama dizgeleri, veritabanı bazında arama tarihleri, tarama/eleme akışı, açık dahil etme/dışlama ölçütleri, çalışma bazında risk-of-bias değerlendirmesi, bağımsız çift tarayıcı işlemi, protokol kaydı, ham çalışma çıkarım tablosuna bağlı bir meta-analiz. Bu ifade yöntemin raporlama sınırıdır; yazarların hiç literatür araması yapmadığını iddia etmez.

**Karşılaştırma sınırı:** Veri hızı, hata, resolution, accuracy, SINR, NMSE, enerji ve çıkarım süresi farklı koşullarda aktarılıyor. Örnekler arasında bant genişliği, mesafe, kullanıcı/hedef sayısı, SNR, anten, donanım, veri kümesi bölünmesi ve baz yöntem her satırda tam verilmediği için nicel üstünlük sıralaması veya havuzlama yapılamaz. Tablo VI aynı tabloda insan etkinliği sınıflaması, beam prediction ve kaynak tahsisi kullanıyor; yüzdeler aynı ölçüme karşılık gelmez.

**Veri erişimi sınırı:** P01, başka veri kümelerinin adlarını ve bazı bibliyografik/URL bağlantılarını sağlıyor. Bu, söz konusu verilerin bu klasöre indirildiği veya lisansları/erişim durumlarının kontrol edildiği anlamına gelmez. P01'in kendi yeni ham deney verisini sağlayan belirgin bir data-availability bölümü tespit edilmedi. Yerel arşiv; kaynak PDF, çıkarılan metin, sayfa verileri ve bu okuma kaydını içerir. İlgili dış veri kümelerinin ham CSI/RF/video dosyaları bu okuma sırasında temin edilmedi.

## 7. PDF içi tutarsızlıklar ve dikkat gerektiren aktarım noktaları

Bu liste bağımsız bir yayın hata düzeltmesi değildir. Metin ile kendi kaynakçası/tablosu arasındaki görünür uyuşmazlıklar ve tanımı eksik nicel noktalar kayıt altına alınmıştır.

| Konum | Gözlenen sorun | Kullanım sınırı |
|---|---|---|
| s.6, [71]; kaynakça s.31 | Ana metin DCO-OFDM diye anlatıyor; [71]'in başlığında **EADO-OFDM** var. DCO-OFDM başlıklı ayrı yayın [80]. | İki yayının yöntemleri/sonuçları eşitlenmemeli; hangisinin hangi iddiayı desteklediği birincil metinden çözülmeli. |
| s.7 ve s.8, [81]; kaynakça s.32 | S.7'de **Singh et al.** adı ve VLC-assisted RF/urban NLoS sonucu yazılı; [81] ise **P. Zhang vd., NLoS visible-light channel modeling**. | Yazar adı uyuşmazlığı PDF içinde kesindir. RF-optik hibrit kazanım iddiasının destek kapsamı ayrıca teyit gerektirir. |
| s.7, [77]; kaynakça s.31 | Optik ISAC için ortak metrik/standart yöntem yokluğu, başlığı genel donanım sınırlı parametre çıkarımı olan [77]'ye bağlanıyor. | Başlıktan kaynak içeriği hakkında kesin hüküm verilmez; iddia-kaynak uyumu bu PDF ile kapanmıyor. |
| s.7-8, [78], [79], [86] | FSO/VLC iletişim ağı, fiber ISAC ve vehicular kanal kavramsallaştırması, oldukça geniş RF-optik birleşim iddialarında kullanılıyor. | Salt başlıktan bu çalışmaların iddiaları desteklemediği söylenemez; gerçek hibrit zincir ve doğrulanan görev ayrıca okunmalı. |
| s.2 ve s.28 | IEEE 802.11bf için girişte **Ekim 2024'te tamamlandı**, ileride **nihai onay 2024'te bekleniyor** ifadeleri var. | Aynı 2026 PDF içinde zaman tutarsızlığı; güncel standart durumu buradan kesinleştirilmemeli. |
| s.21, [186]; Şekil 10 ve kaynakça s.34 | Sensör sinyalinin LLM için metinleştirilmesi [186]'ya atfediliyor; [186] **TS-I3D radar hand-gesture recognition**. Şekil 10 ise **[185] Penetrative AI** diyor. | Metin/şekil/kaynak eşleme problemi; LLM cümlesi kaynak kontrolü olmadan taşınmamalı. |
| s.27, Rel-18 [226]; kaynakça s.35 | Konumlama protokolü paragrafındaki [226], kaynakçada secrecy ISAC beamforming konferans yayını. | Standart/protokol iddiasına karşılık gelen referans eşlemesi kontrol edilmeli. |
| s.27, [237]; kaynakça s.35 | Ana metin TR 22.837'yi 32 ISAC kullanım durumu için kullanıyor; bibliyografik başlık **Feasibility Study for NR in Unlicensed Spectrum**. | Belge numarası ile başlık arasındaki uyumsuzluk dış standart kaydından çözülmeden düzeltilmiş sayılmamalı. |
| kaynakça s.35, [239] | Belge adı **R1-240xxxx** biçiminde yer tutucu içeriyor. | Tam standart katkı belgesi kimliği doğrulanmış değildir. |
| s.27 | **400 MHz** için **0.1875 m resolution** yazıyor. | Basit monostatik nominal ΔR=c/(2B), c≈3×10^8 m/s ile **0.375 m** verir. Makale burada farklı etkin bant/çözünürlük tanımını açıklamıyor; doğrudan evrensel formül doğrulaması gibi kullanılamaz. |
| s.15, [137] | Girişim gücündeki azalma **“more than 10 dBm”** diye yazılmış. | dBm mutlak güç birimidir; fark/azalma için dB beklenmesi nedeniyle metrik/birim tanımı belirsiz. Orijinal değeri sessizce değiştirmemek gerekir. |
| Tablo VI s.22, [193] | “Angle prediction accuracy **>15%**” ifadesi var. | Yüzde doğruluk mu iyileşme mi açıklanmıyor; değer anlamlı bir genel başarı oranı olarak yeniden yorumlanmamalı. |
| Tablo VII s.23 ve veri anlatısı s.22-23 | Tablo SDP **>400 hours**, WiMANS **>9.4 hours**, OPERAnet **>8 hours** diyor; anlatıda 400, 9.4, yaklaşık 8 saat. | İşaret ve yaklaşık değer farkları özgün biçimleriyle tutulmalı; yapay kesinlik üretilmemeli. |

Ek kapsam gerilimi: RF bölümünde bant genişliğinin menzil çözünürlüğüne etkisi doğru biçimde vurgulanırken optiğe geçişte kısa dalga boyu/ince çözünürlük ilişkisi geniş bir ifadeyle kuruluyor. Menzil çözünürlüğü, açısal çözünürlük ve kestirim doğruluğu ayrı fiziksel metriklerdir; bunları tek “yüksek hassasiyet” kategorisinde birleştirmek koşul farklarını örter.

## 8. Şekil ve tablo okuma envanteri

Tüm numaralı şekil ve tabloların yer aldığı sayfalar görsel olarak incelendi; aşağıdaki 14 şekil ve 7 tablo P01'in tamamını kapsar.

| Öğe | PDF sayfası | İşlev |
|---|---:|---|
| Tablo I | 3 | 26 önceki survey ve P01'in beş kapsam eksenindeki karşılaştırması. |
| Tablo II | 5 | Merkezi/dağıtık/hareketli anten ve RIS'in kapsama, maliyet, senkronizasyon ve sınırlamaları. |
| Tablo III | 7 | VLC/FSO/photonic sensing için taşıyıcı, iletişim, algılama ve sınırlama sınıflaması. |
| Tablo IV | 9 | Ortogonal zaman/frekans/uzay/kod tahsis yöntemleri ve yayın bazlı performanslar. |
| Tablo V | 11 | Algılama ve iletişim merkezli tasarımın matematiksel kısıt/amaçları. |
| Tablo VI | 22 | Farklı AI yöntemleri, sinyal işleme, uygulama ve ikincil performans sonuçları. |
| Tablo VII | 23 | 10 veri kaynağı; modalite, görev, hacim ve sağlayıcı. |
| Şekil 1 | 4 | Makalenin beş eksenli yapısı. |
| Şekil 2 | 6 | VLC, FSO ve photonic sensing görsel sınıflaması. |
| Şekil 3 | 10 | Zaman/frekans/uzay/kod kaynak tahsis örnekleri; bazı sayılar örnek şemaya aittir. |
| Şekil 4 | 14 | Tek hücrede BS/UE/ek UE ve pasif izleme terminalleri. |
| Şekil 5 | 15 | Çok hücreli, C-RAN, mono/bistatik ve makro/mikro işbirliği. |
| Şekil 6 | 16 | Uzay-hava-yer ağı; irtifa/uygulama yerleşimi. |
| Şekil 7 | 18 | Sensör, yerel özellik çıkarımı, iletişim ve edge server zinciri. |
| Şekil 8 | 19 | AI-enabled ISAC, ISAC-facilitated AI ve karşılıklı etkileşim. |
| Şekil 9 | 21 | [169]'dan RIS-ISAC ışın oluşturma sinir ağı. |
| Şekil 10 | 21 | [185]'ten Penetrative AI / fiziksel sinyallerle LLM çerçevesi. |
| Şekil 11 | 25 | İletişim güvenliği ve algılama mahremiyeti tehdit ayrımı. |
| Şekil 12 | 26 | 3GPP sürüm ilerleyişi; zaman çizgisi kaynak kontrolü gerektirir. |
| Şekil 13 | 27 | LMF-gNB-UE Multi-RTT mesajlaşma prosedürü. |
| Şekil 14 | 28 | [244]'ten döner kanatlı UAV ile ortak iletişim/hedef konumlama senaryosu. |

## 9. Kendi O-ISAC survey'imizle ilişkisi - yalnız tartışma kaydı

Bu yayın, **genel ISAC içinde optiğin artık açık bir kapsam ekseni olarak yer aldığını** gösteren güçlü bir konumlandırma kaynağıdır. “Önceki ISAC survey'leri optiği hiç ele almıyor” gibi bir iddia P01 karşısında savunulamaz. Buna karşılık P01'de optik kısım, bütün alanın özgün kanal/donanım/ölçüm koşullarını çalışma bazında karşılaştıran kapsamlı bir optik evidence synthesis değildir.

Bizim tartışmamız açısından ayırt edilmesi gereken kavramlar: optik hava yolu/fiber/fotonik RF; algılama ve haberleşmenin gerçekten paylaştığı kaynak; görev/metrik eşleşmesi; deney/kuram/simülasyon ayrımı; NLoS'un geometrisi ve yansıma yolu; hizalama/FoV/aydınlatma/clipping/hava şartları; maliyet ve senkronizasyon. Bunlar P01 okumasından çıkan karşılaştırma boyutlarıdır, yeni proje planı veya sonuçta varılmış özgünlük kararı değildir.

Makalenin güçlü tarafı geniş sistem anlatısı, bölüm sonu soruları ve modüler karşılaştırma tablolarıdır. En belirgin temkin noktaları heterojen kanıtların ortak başlıkta birleştirilmesi, sayıların eksik koşullarla sunulması ve görünür referans/tarih uyuşmazlıklarıdır. P01'den bir sayıyı ana makaleye taşımak gerekirse bu kayıt, ilgili birincil kaynağa geri dönülecek yeri gösterir; o doğrulamanın yapılmış olduğunu göstermez.

## 10. Tamamlama kaydı

- Metinsel okuma: PDF s.1-35, bütün bölümler ve [1]-[248] kaynakça.
- Görsel kontrol: başlık/kimlik; 14 şekil ve 7 tablonun tamamı; temel eşitlik sayfaları 11-13; optik kaynakça ve tutarsızlıkların bulunduğu ilgili sayfalar.
- Ana çıkarımlar ve sınırlamalar: bu dosyada sayfa/atıf düzeyinde kayıtlı.
- Dış web, ham veri indirme, bağımsız deney yeniden üretimi, insan reviewer doğrulaması ve proje ana metni değişikliği: bu okuma görevinin çıktısı değildir.
