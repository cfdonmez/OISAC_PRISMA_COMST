# Önceki 220 çalışmalık taslak ile V3 karşılaştırma notları

6 Eylül 2026. İnceleme yalnız TeX ve metin kayıtları üzerinden yapıldı; PDF açılmadı, çıkarılmadı veya yeniden derlenmedi. Manuscript kaynakları değiştirilmedi. [Dört eserlik karşılaştırma tablosuna dön](BIZIM_SURVEY_ILE_KARSILASTIRMA.md).

## Hangi eski sürüm incelendi?

Kullanıcının verdiği `C:/GH/OISAC/_PRISMA/_COMST` yolu bulunmadı. `C:/GH` altında bulunan ilgili depo **`C:/GH/OISAC_PRISMA_COMST`**. Depoda `current_bundle`, `finalManuscript` ve `finalShortened` katmanları bulunuyor. Karşılaştırmada, son manuscript değişikliklerini içeren **`finalShortened/bare_jrnl_new_sample4.tex`** esas alındı. Kısaltma takip belgesi de bu dosyayı ana manuscript olarak gösteriyor. TeX dosyasının son commit'i 15 Nisan 2026 tarihli `84578c00142f4c52e6bd2f2b9e0a51b1fc4825b7`; inceleme öncesi depo temizdi.

Başlık: **Optical Integrated Sensing and Communication: A Systematic Review of Fiber, Free-Space, VLC/LiFi, and Photonic-THz Platforms**. Yazarlar Fatih Dönmez, Ahmet Altuncu ve Mustafa Namdar. Özet ve I–IX bölümleri okundu. Sayfa sayısı veya görsel yerleşim değerlendirilmedi. [Kaynak kimlikleri ve hash kaydı](ONCEKI_SURVEY_TEX_SNAPSHOT.json).

## Ana sonuç

**Eski çalışma fiziksel temelleri daha geniş anlatıyor; V3'ün yeni çerçevesi ise bir mimarinin gerçekten hangi ortak performans ilişkisini kanıtladığını daha açık sorguluyor.** Sistematik derleme, ölçüm düzlemi ayrımı ve çözünürlük–doğruluk disiplini her iki sürümde de mevcut. Dolayısıyla bunlar önceki çalışmamıza göre V3'te ilk kez geliştirilen fikirler olarak sunulmamalı.

Eski sürümün öğretici parçaları yeniden değerlendirilmeye değer. Bununla birlikte eski sayısal özetlerin ve bütün denklemlerin olduğu gibi geri getirilmesi sorunu çözmez: iki sürümde de tam koşulları gösterilmiş, ortak değişkenin iki sonuca etkisini baştan sona izleyen gerçek bir örnek eksik.

## 1. 220 ile 206 aynı sayımın iki tarihi değildir

| Özellik | Eski 220 | V3 |
|---|---|---|
| Formal arama kaynakları | IEEE Xplore, Scopus, Web of Science | Altı kaynak |
| Arama kapsamı | 2000–30 Kasım 2025; sentezin ağırlığı 2020–2025 | 1 Ocak 2020–22 Haziran 2026 |
| Bildirilen dahil etme | 220 çalışma | 227 rapor, 206 benzersiz çalışma |
| Sayım birimleri | Metinde study/article/paper ifadeleri birlikte kullanılıyor | Rapor, benzersiz çalışma ve companion rapor ayrımı açıklanıyor |
| Yöntemin önemli sınırı | İlk arama/eleme aşamaları kısmen yeniden kurulmuş toplu kayıtlara dayanıyor | Geriye dönük kayıt, erişilemeyen tam metinler ve insan kontrolü sınırları açıklanıyor |

Bu fark **14 çalışmanın çıkarıldığı**, V3'ün daha az kapsamlı olduğu veya eski çalışmanın daha kaliteli olduğu anlamına gelmez. Bunun için DOI/başlık ve çalışma–rapor düzeyinde ayrıca eşleme gerekir; bu görevde böyle bir corpus eşlemesi yapılmadı.

Eski metnin PRISMA akışı 980 kayıt, 700 tarama, 222 tam metin ve 220 dahil etme bildiriyor. TeX ve ek paket açıklaması, üst aşamaların yeniden kurulmuş toplu verilerle; sonraki aşamaların satır kayıtlarıyla desteklendiğini ayırıyor. Bu, yeniden üretilebilirliğin bütün zincirde aynı düzeyde olduğu iddiasını sınırlar. [Eski TeX:747](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:747), [TeX:822](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:822), [ek paket açıklaması](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/prisma_evidence_pack/README.md).

## 2. Fiziksel öğreticilik eski sürümün önemli avantajı

Eski II. bölüm; koherent kompleks alan ile IM/DD gözlemini, fiber dispersiyonunu, FSO atmosfer ve hizalama etkilerini, VLC kanalını, fotonik-THz zincirini ve menzil/CRLB ilişkilerini denklemlerle açıklıyor. VI. bölüm OPA'nın vericide ışın yönlendirmesi ile ORIS'in ortamda yol düzenlemesini ayırıyor; görüş alanı, grating lobe, ekleme kaybı ve kontrol gecikmesini tasarım kısıtlarına bağlıyor. Çok kullanıcılı bölüm koordinasyon ve geri bildirim maliyetini de tartışıyor. Bunlar V3'ün daha sınırlı fiziksel temel anlatımını geliştirebilecek içerikler. [TeX:365](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:365), [TeX:433](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:433), [TeX:1574](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:1574), [TeX:1757](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:1757).

Ancak denklem görünürlüğü tek başına tamamlanmış teknik açıklama değildir. Örneğin gecikme sınırının varsayımları ve parametreleri ile farklı birimli hedeflerin ortak amaç fonksiyonunda nasıl ölçeklendiği yeterince açılmıyor. Aktarım sırasında her denklem fiziksel varsayımları ve okuyucuya sağladığı tasarım kararıyla birlikte ele alınmalı. [TeX:588](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:588), [TeX:715](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:715).

## 3. V3'ün ilerlemesi: doğru metrikten açık ortak ilişkiye

Eski sürüm zaten OSNR ile elektriksel SNR'yi, çözünürlük ile doğruluğu ve fiber uzamsal ayrımını kablosuz menzil çözünürlüğünden ayırıyor. V3'ün yeni II. bölümü bunları **P/G/X/C/S/M/E** kaydında fiziksel bağlam, paylaşım yeri, ortak değişken, iki sonuç, ölçüm koşulları ve kanıt sınırlarıyla birleştiriyor. Aynı yayında iki sonuç bulunması ile bu sonuçların aynı etkene bağlı olması arasındaki ayrım daha belirgin. [Eski TeX:606](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:606), [V3 II:14](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex:14).

V3'ün bazı teknik paragrafları da daha güçlü neden–sonuç sentezi kuruyor: sequence shaping ile girişimin oluşumunu azaltma ve DC offset ile enerji dağılımını değiştirme ayrımı buna örnek. Ancak yeni çerçevenin bütün corpus üzerinde tamamlanmış uygulaması varmış gibi yazılmamalı; önceki raporda açıklanan 118 koşullu kayıt sorunu sürüyor. [V3 V:370](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:370).

## 4. Eski sayısal grafikler daha görünür, karşılaştırma güvencesi yine sınırlı

Eski V. bölüm 225 senaryo noktası, 170 CRQ adayı, 20 CRQ-geçerli nokta ve iki Pareto noktası bildiriyor. Hız ve çözünürlük aralıkları ile medyanlar metinde açıkça görülüyor. Metnin sınırı iki noktalı örnek olarak tanımlaması yerinde. Bununla birlikte **CRQ = R/Δr** oranı, farklı hedef/mesafe/güç/bant genişliği/alıcı koşullarını kendiliğinden eşitlemez; bu noktalardan ortak mühendislik üstünlüğü çıkarılamaz. [TeX:616](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:616), [TeX:1422](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:1422).

Eski **20 nokta**, V3'ün **118 koşullu metrik kaydı** ile aynı birim veya filtre değildir. Bu sayılardan önce/sonra iyileşme oranı hesaplanamaz. Eski metindeki “299 MAJOR violation / 169 paper” ifadesi de kaynak yayınların hata oranı diye yorumlanmamalı: ihlalin kaynak metinden mi yoksa çıkarım/normalizasyon işleminden mi geldiği bu paragrafta gösterilmiyor. [TeX:1433](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:1433).

## 5. Taksonomi adları aynı görünse de sınıflar aynı değil

Eski metin 116/220 hibrit ve yalnız bir explicit terahertz kaydı bildiriyor; ayrıca 39 doğrudan fotonik-THz dayanağının 31'inin hibrit etiketlendiğini açıklıyor. V3'te fotonik terahertz 69/206, hibrit optik 9/206. Bu dağılım değişimini alanın zaman içindeki gelişimi diye okumak yanlış olur: örneklem ve sınıflandırma tanımları değişmiş. Eski metnin geniş hibrit sınıfı fiziksel farklılıkları daha fazla bir araya getiriyor. [Eski TeX:963](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:963), [TeX:1044](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:1044), [V3 IV:28](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex:28).

## 6. Giriş ve yöntemden doğrudan taşınmaması gereken ifadeler

- Eski tabloda **“This Review”** satırı var; bu görünürlük V3'te eksik. Ancak bütün analitik eksenlerde güçlü puan verilmesi ve önceki yayınların kapsamının dar tanımlanması yeniden denetlenmeli. P02'nin geniş optik kapsamı karşısında “bu ortamları birleştiren derleme yok” ifadesi güncel konumlandırmada kullanılamaz. P02'nin 2026 yayını olması, 2025 arama dondurması içinde bulunmamasını tek başına yöntem hatası yapmaz. [TeX:123](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:123), [TeX:265](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:265).
- OSF kayıt tarihi metinde 12 Şubat 2026; belirtilen arama dondurmasından sonra. Bu nedenle buradan prospektif ön kayıt sonucu çıkarılamaz. İki bağımsız insan değerlendiriciye ilişkin ifadeler de bu okumada doğrulanmış faaliyetler değildir. [TeX:742](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:742), [TeX:820](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:820).
- Giriş yalnız 208 çalışma için tam beş boyutlu TQAF bildirirken yöntem bütün dahil edilen çalışmaları değerlendirdiğini söylüyor. Kalan 12 kaydın durumu açıklanmadan değerlendirme kapsamı eşit kabul edilmemeli. Ayrıca girişte bir derlemenin 220 çalışma içinde anılması, birincil/bağlamsal kaynak ayrımını açıklamayı gerektiriyor. [TeX:277](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:277), [TeX:851](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:851).

## 7. Yeniden kullanılabilecek parçalar

| Eski metinden yararlı unsur | V3'e katkısı | Yeniden kullanım koşulu |
|---|---|---|
| Kanal, alıcı ve menzil modelleri | Yeni çerçeveye fiziksel temel kazandırır | Varsayım, sembol, ölçüm düzlemi ve örnek bağlantısı tamamlanmalı |
| OPA–ORIS ve çok kullanıcılı kontrol açıklaması | Tasarım seçimini somutlaştırır | Güncel corpus kapsamı ve fiziksel uygulanabilirlik eşlenmeli |
| Seçilmiş deney/uygulama örnekleri | Sayısal ölçek ve teknik sezgi verir | Sonuç çifti, birim ve aynı koşul doğrulanmalı; örneğin dB ile yazılan “BER gains” açıklanmalı |
| Deney raporlama alanları | V3'ün saptadığı yeniden üretim eksiklerine uygulanabilir cevap verir | Asgari kayıt listesi, gerçek eksiklerle ilişkilendirilmeli |
| Yol haritasındaki somut arıza ve kontrol vakaları | Denenebilir araştırma sorularına dönüşebilir | Genel kapsam sayıları yerine deney, ölçüt ve başarı koşulu kurulmalı |

Dayanaklar: [uygulama tablosu:1839](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:1839), [BER ifadesi:1855](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:1855), [raporlama sözleşmesi:1690](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:1690), [yol haritası:2141](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex:2141).

Eski sonuç bölümü de ağırlıkla metrik ve raporlama kurallarına dönüyor. Bu nedenle eskiye dönmek tek başına daha öğretici bir survey oluşturmaz. Önerilen yön, **seçilmiş fiziksel açıklama → koşulları belli gerçek sonuç çifti → V3'ün ilişki değerlendirmesi → çıkan tasarım dersi** sırasını kurmak. Bu rapor karşılaştırmayı genişletir; herhangi bir manuscript revizyonu uygulamaz.
