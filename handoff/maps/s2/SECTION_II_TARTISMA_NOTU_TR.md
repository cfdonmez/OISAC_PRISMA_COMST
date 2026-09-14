# Section II: açılış, motivasyon bağlantısı ve COMST örnekleri

Tarih: 7 Eylül 2026. Bu not güncelleme öncesi tartışma içindir. Makale kaynakları değiştirilmedi. Kullanıcının netleştirdiği odak: **Section II açılışı ve motivasyonla bağlantısı**.

## İncelenen kaynaklar ve karşılaştırmanın sınırı

Kullanıcının belirttiği yolların mevcut dosya sistemindeki karşılıkları:

- `C:\GH\OISAC_PRISMA_COMST\data\corp_std`: 77 COMST Markdown kaydı. Başlık/Section II envanteri çıkarıldı; altı yakın örneğin ilgili bölümleri ayrıntılı okundu (014, 026, 044, 054, 067, 073). Üç tamamlayıcı örneğin açılış ve bağlantıları ayrıca incelendi (027, 037, 051). Bu, 77 makalenin tamamının ayrıntılı içerik değerlendirmesi değildir.
- `C:\OISAC\outputs\IKI_CALISMA_OKUMA_2026-09-06`: P01 ve P02'nin mevcut tam metinleri. P01, IEEE Communications Surveys & Tutorials; P02, Optical Switching and Networking makalesidir.
- Güncel kullanıcı metni: `C:\OISAC\worktrees\comst-v3-20260906\manuscript\sections\02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex`. Başlığı **Technical Foundations of O-ISAC**. **Background and Motivation**, Section I-A'dadır; yalnızca II ile bağlantısı açısından ele alındı. IV/V başlangıçları da bu bağlantının devamı açısından kontrol edildi.

TeX ve mevcut Markdown/metin çıktıları kullanıldı; PDF yeniden açılmadı, web taraması yapılmadı. Aşağıdaki sayılar ve değerlendirmeler bu oturumda yerel kaynaklardan kontrol edildi. Eski çalışma notları yalnızca sürüm ve yol bulmayı hızlandırdı. İnceleme sırasında Section I başka bir işlem tarafından güncellendi (dosya zamanı 22:19:22); bu ana notun motivasyon değerlendirmesi ve bağlantıları son metne göre yenilendi. Section II'nin hash değeri değişmedi. İlk ve son sayımlar ayrı kaydedildi; alt okuma notlarının ilk I değerlendirmeleri önceki anlık metne aittir.

## Ana değerlendirme

Section II'nin mevcut dört aşamalı düzeni tutarlı: **sinyal ve gözlem → kaynak paylaşımı ve optik kısıtlar → ölçütler → ortak çalışma noktaları**. Açılış da bütünüyle amaçsız değildir: ikinci cümle performansı yayılım, alıcı gözlemi ve paylaşıma bağlıyor; son cümle IV/V bağlantısını kuruyor. Bu iki özellik korunmalı.

Zayıflık ilk cümlenin görevinde: “O-ISAC combines data transmission and physical observation through shared optical or photonic resources.” Bu tanım I-A'da zaten verilmiş durumda. Son kontrol edilen I-A, optik altyapının iki işlevi desteklemesiyle açılıyor. Son paragrafında hangi bütünleştirme mekanizmasının uygulamaya uyduğu, iki işlevi nasıl etkilediği ve başka bir ortama taşımadan önce neyin sınanacağı ihtiyacını kuruyor. II, bu ihtiyacın fiziksel açıklamasına başlayabilir. Mevcut açılışta yeniden tanım → belirleyici etkenler → bölüm içeriği sırası var. Daha güçlü sıra **tasarım sorusu → fiziksel açıklamanın gereği → bölümün izleyeceği yol**.

Kaynaklar: [I-A'nın son paragrafı](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/01_INTRODUCTION.tex:52), [I-C'nin soruları ve katkıları](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/01_INTRODUCTION.tex:178), [II açılışı](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex:4).

## Örnekler bu işi nasıl yapıyor?

| Kaynak | İlgili bölümün görevi ve akışı | Çalışmaya bağlantısı | Yaklaşık ana metin | Açılış paragrafı |
|---|---|---|---:|---:|
| COMST_014, *A Survey on Indoor Visible Light Positioning Systems: Fundamentals, Applications, and Challenges* | II, System Model: VLC → PD alıcı → kamera alıcı → fiziksel sınırlamalar | Algılayıcı farkını, sonraki konumlama algoritmalarının hangi bilgiyi kullanabildiğine bağlıyor | 840 | 53 |
| COMST_026, *A Top-Down Survey on Optical Wireless Communications for the Internet of Things* | II, Preliminaries: optik bantlar, temel bileşenler, sistem özellikleri, IoT ile ilişki ve standartlar | Geniş hazırlık bölümünü sonraki uygulama/ortam incelemeleri için kullanıyor | 4.050 | 119 |
| COMST_044, *Integrated Sonar and Communication: A Survey* | II, ISC System Model: monostatik/bistatik düzenek → çerçeve → verici ve alıcı modeli | Seçilen modelin kanal, donanım, dalga biçimi ve işleme bölümlerine temel olduğunu açıkça söylüyor | 1.780 | Bağımsız II açılışı yok; II-A ilk paragrafı 56 |
| COMST_054, *Optical Wireless Communication in Atmosphere and Underwater: Statistical Models, Improvement Techniques, and Recent Applications* | II, sistem temelleri: optik sinyal yolu → verici → alıcı → ortamla ilişkili yararlar | Bileşen/ortam farkları sonraki kanal ve iyileştirme konularını anlamayı sağlıyor | 920 | 154 |
| COMST_067, *Terahertz Communications and Sensing for 6G and Beyond: A Comprehensive Review* | II, genel bakış: 6G gelişimi, spektrum ve THz tarihçesi | Motivasyon/bağlam işlevi baskın; ayrıntılı fizik daha sonraki bölümlerde | 2.400 | 56 |
| COMST_073, *Visible Light Positioning as a Next-Generation Indoor Positioning Technology: A Tutorial* | II, Context: kullanım alanı → alternatif teknolojiler → gerekçe | Motivasyonu II içinde taşıyor; bizim teknik temellere tam eşdeğer değil | 3.930 | Bağımsız II açılışı yok; II-A ilk paragrafı 51 |
| P01, Zhang vd., *Integrated Sensing and Communications Over the Years: An Evolution Perspective* — COMST | II, Operating Spectrum Across RF and Optical: RF → optik → hibrit → çıkarılan dersler | Girişte vaat edilen RF–optik evrim boyutunu ilk teknik sentez bölümünde işliyor | 2.870 | Bağımsız II açılışı yok; II-A ilk paragrafı 107 |
| P02, Mohsan vd., *Optical integrated sensing and communication: Fundamentals, applications, challenges and future aspects* — OSN | 2, Categories of O-ISAC: kategoriler ve örnekler | Girişte vaat edilen kapsamı taksonomi üzerinden gerçekleştiriyor | 1.030 | 35 |
| P02, aynı makalenin Section 4'ü | Mimari, yararlar ve dalga biçimleri; teknik temellerin bir kısmı ayrıca Section 5'te | Bizim II-A/B ile bölüm numarasından daha anlamlı bir işlev eşleşmesi | 1.010 | 41 |
| Bizim Section II | Gözlem → kaynak ve kısıtlar → ölçütler → ortak çalışma noktası | IV'teki mimarileri ve V'teki ortak performansı yorumlamayı hazırlıyor | **1.338 (TeXcount)** | **62 (TeXcount)** |

Sayılar bir COMST hedefi/ortalaması oluşturmaz. Bölümler farklı işler yapıyor. Özellikle P01 II, teknik sentezin kendisi; P02 II ise kategorileştirmedir. P02'nin 4 ve 5. bölümlerini birlikte değerlendirmek gerekir; tablodaki 1.010 yalnızca Section 4'ün sayısıdır.

En yararlı üç yazım örneği:

1. **COMST_014:** modelin varlık gerekçesi somut. PD ve kameranın farklı gözlemleri farklı konumlama yollarını mümkün kılıyor. Bölüm sonunda görüş alanı, tıkanma, girişim ve işleme gecikmesini anarak modelin tasarım sonuçlarını çıkarıyor. Bizde bunun karşılığı, doğrudan/koherent gözlemin hangi algılama bilgisini sağladığını ve bunun kaynak paylaşımını nasıl etkilediğini açıklamak. [II açılışı](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_014/COMST_014.md:103), [tasarım sonuçları](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_014/COMST_014.md:148).
2. **COMST_044:** bir model tanıtıp bırakmıyor; mimari ayrımın eşzamanlama, kanal ve alıcı bilgisine etkisinden kendi kapsamını türetiyor. Sonunda modelin sonraki dört teknik konuya temel olduğunu bildiriyor. Bizde aynı hareket, optiğin farklı rolünden hangi performans ilişkisinin inceleneceğine geçmek olabilir. [Açılış](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_044/COMST_044.md:131), [sonraki bölümlere köprü](C:/GH/OISAC_PRISMA_COMST/data/corp_std/COMST_044/COMST_044.md:242).
3. **P01:** fiziksel açıklamadan kısıta, kısıttan bir sonraki tasarım ihtiyacına geçiyor. RF'nin sınırları optik incelemeyi, optiğin sınırları hibrit incelemeyi hazırlıyor; bölüm sonundaki dersler araştırma sorularına dönüşüyor. Bizim çıkaracağımız ders bu nedensel ilerleyiş. Geniş RF arka planını veya bölüm uzunluğunu almak gerekmiyor. [II başlangıcı](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:234), [geçiş](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:366), [çıkarılan dersler](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:600).

COMST_027/037/051 açılışları da tek bir dergi kalıbı olmadığını gösteriyor. Örneğin 027, girişte katkı olarak vaat ettiği basit modeli II'de doğrudan kuruyor. 051 daha geniş fiziksel arka planla, 037 makaleyi örgütleyen mimariyle başlıyor. Ayrıca 026 açıkça bölümün ne yapacağını söyleyen bir açılış kullanıyor. Dolayısıyla “COMST'ta This section ile başlanmaz” gibi bir kural çıkarmak doğru olmaz. Ayrıntılar [bağımsız okur notunda](C:/OISAC/outputs/SECTION2_KARSILASTIRMA_2026-09-07/motivation_review.md).

## Kelime sayısı ve yoğunluk

Güncel TeX, `texcount -utf8 -sub` ile sayıldı:

| Parça | Ana metin kelimesi |
|---|---:|
| Açılış | 62 |
| II-A: Signal Paths and Sensing Observations | 294 |
| II-B: Shared Resources and Optical Signal Constraints | 315 |
| II-C: Communication and Sensing Measures | 365 |
| II-D: Joint Operating Points and Performance Interpretation | 302 |
| Toplam | **1.338** |

Ayrıca 168 altyazı ve 25 başlık kelimesi var. Bölüm üç şekil, bir tablo ve beş ayrı denklem ortamı içeriyor. Tablo hücreleri, şekillerin içindeki etiketler ve matematiksel ifadeler ana metin sayısında değil; 1.338, bölümde basılan bütün sözcüklerin toplamı değildir. Ana metin+başlık+altyazı toplamı 1.531; bu da tablo/şekil içi yazılar dahil tam bölüm toplamı sayılmamalı.

Dış kaynakların sayıları mevcut Markdown/OCR metinlerinin temizlenmesine dayanıyor: başlıklar, tablolar, şekil altyazıları, atıflar ve matematik ayrılıyor; P01/P02'de bazı kısa satır içi alt başlıklar kalabiliyor. Bu nedenle tabloda yuvarlanmış değerler verildi. Yöntem farkı küçük farkları anlamlı kılmaz. Ayrı bir yaklaşık TeX temizliği 1.345 verdi; güncel kaynak için esas alınan sayı TeXcount'un 1.338 sonucudur.

**Editoryal değerlendirme:** mevcut uzunluk, kısa bir teknik hazırlık bölümü için savunulabilir. Karşılaştırma, zorunlu bir büyütme ihtiyacı göstermiyor. Açılış için 80–110 sözcük kullanılabilir; bu dört altbölümü açıkça bağlamak için önerilen bir çalışma aralığıdır, dergi şartı değildir. Bölümün geri kalanını salt kelime hedefine göre uzatmamak gerekir.

## Bizim konuda geliştirme yönü

1. **İlk cümlede tanımdan performans sorusuna geçmek.** Ortak kaynağın veri geri kazanımını ve algılama gözlemini nasıl desteklediğini başa almak, I-A'nın motivasyonunu teknik açıklamaya taşır.
2. **Optik/fotonik kapsamı açık tutmak.** Fiberdeki fiziksel değişim, optik kablosuzdaki ışık yolu ve fotonik üretimli RF yayılımı aynı gözlem modeli değildir. II-A'daki ayrım korunmalı. IM/DD denkleminden bütün O-ISAC sistemlerinin aynı sinyal kısıtına tabi olduğu izlenimi doğmamalı; mevcut sınır açıklaması bu açıdan yararlıdır.
3. **Dört altbölüm arasına gerekçeyi taşımak.** A→B: alıcının erişebildiği bilgi, paylaşımın nasıl yapılabileceğini etkiler. B→C: paylaşımın iki işleve etkisini anlayabilmek için ölçütlerin neyi ölçtüğü açıklanır. C→D: iki ölçütün tanımı, aynı tasarım ayarına bağlandıklarında ortak performans yorumuna dönüşür. Bunlar ek bir uzun arka plan yerine birer kısa geçiş cümlesiyle sağlanabilir.
4. **Tekrarların görevini ayırmak.** I-A'da fiber güç örneği motivasyon sağlar; II-D'de güç rekabetinin alıcı bilgisinden yararlanarak elde edilen kazançtan ayrılması açıklama sağlar. İkinci kullanım yararlı. Aynı şekilde çözünürlük/hata ve OSNR/elektriksel SNR ayrımları korunmalı.
5. **Tablodan ortak performansa geçişi açık tutmak.** II-D tablosundaki her satırın tek bir ortak deney koşulu olduğunu varsaymamak gerekir. Özellikle fotonik THz satırı ayrı alıcı koşullarını zaten belirtiyor. Ortak çalışma noktasını açıklayan asıl güçlü örnek, iki çıktının aynı kontrollü güç değişimine bağlandığı fiber paragrafıdır. Bu paragrafın öğretici rolü görünür kalmalı.
6. **Sonraki bölümle terimleri eşlemek.** V-A, “Applying the comparison profile defined in Section II” diyor; güncel II'de “comparison profile” adlı açık tanım bulunmuyor. II gerekli fiziksel koşulları anlatıyor, fakat V eski adlandırmayı sürdürüyor. İleride revizyonda V'nin göndermesini mevcut teknik kavramlara uyarlamak veya kısa, okuyucuya yararlı bir tanımı uygun yerde kurmak gerekir. [V-A göndermesi](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:25), [II'deki mevcut yorum](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex:323).

## Tartışma için önerilen açılış

Bu paragraf öneridir; makaleye uygulanmadı. Mevcut ikinci cümlenin güçlü fiziksel fikrini ilk sıraya alır ve ölçütler/ortak çalışma noktalarını da görünür kılar:

> The performance of an O-ISAC system depends on how its shared resources support data recovery and the physical measurement of interest. Fiber, optical wireless, and photonics-enabled wireless systems differ in their signal paths, receiver observations, and hardware constraints. This section explains how these differences shape resource sharing and communication and sensing performance. We introduce the relevant signal models and performance measures, then use representative examples to connect design choices to joint operating points. These foundations support the analysis of architectures and joint-design results in Sections IV and V.

88 boşlukla ayrılmış İngilizce sözcük; tireli ifadeler tek sözcük sayıldı. Uygulama aşamasında bölüm numaraları mevcut LaTeX referanslarıyla yazılabilir. Bu paragraf yeni bir deney sonucu veya evrensel model iddiası eklemiyor. Girişin kurduğu tasarım ihtiyacını II'nin fiziksel açıklamasına bağlıyor.

## Kanıt ve yeniden üretim dosyaları

- [Güncel TeX sayımı ve kaynak hashleri](C:/OISAC/outputs/SECTION2_KARSILASTIRMA_2026-09-07/current_counts.json)
- [TeXcount çalıştırma betiği](C:/OISAC/outputs/SECTION2_KARSILASTIRMA_2026-09-07/count_current.py)
- [77 kaynak başlık/II envanteri](C:/OISAC/outputs/SECTION2_KARSILASTIRMA_2026-09-07/std_structure_inventory.json)
- [Altı örnek için yaklaşık sayımlar](C:/OISAC/outputs/SECTION2_KARSILASTIRMA_2026-09-07/std_structure_counts.json)
- [Markdown sayım yöntemi](C:/OISAC/outputs/SECTION2_KARSILASTIRMA_2026-09-07/std_structure.py)
- [P01/P02 ayrıntılı okuma ve sayım aralıkları](C:/OISAC/outputs/SECTION2_KARSILASTIRMA_2026-09-07/p01_p02.md)
- [Bağımsız okur değerlendirmesi ve ek örnekler](C:/OISAC/outputs/SECTION2_KARSILASTIRMA_2026-09-07/motivation_review.md)
