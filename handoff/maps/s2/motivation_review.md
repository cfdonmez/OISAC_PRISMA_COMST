# Section II açılışı ve motivasyon bağlantısı: bağımsız okur notu

Tarih: 2026-09-07. Yalnızca yerel TeX ve Markdown metinleri incelendi. Makale kaynağı değiştirilmedi. Odak Section II açılışıdır; I-A yalnızca bağlantı ve tekrar açısından değerlendirildi.

## Temel değerlendirme

Mevcut Section II açılışı yanlış veya amaçsız değil. Kaynak satır 4–11 şu zinciri kuruyor: ortak optik/fotonik kaynaklar → yayılım, alıcı gözlemi ve paylaşım → modeller ve örnekler → mimari ve performans incelemesi. Bu zaten makalenin özgül amacına bağlanan bir iskelet. Daha güçlü açılış için gereken, O-ISAC tanımını yeniden vermek yerine incelemenin açıklayacağı fiziksel tasarım sorusunu öne almak.

`02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex:4–11`: “O-ISAC combines data transmission and physical observation through shared optical or photonic resources.” Girişteki `01_INTRODUCTION.tex:16–26` optiğin farklı platformlardaki rolünü zaten açıklıyor. II'nin ilk cümlesi bu nedenle okuyucuyu bir adım ileri götürmek yerine kısa bir yeniden başlama hissi verebilir. Bu bir doğruluk sorunu değil, anlatı verimliliği sorunu.

II açılışının en iyi kısmı satır 5–7: performansın yayılım yoluna, alıcı gözlemine ve paylaşılan kaynağa bağlı olduğu cümle. Bilimsel hareket noktası burada. “They provide the technical basis for reading…” (9–11) ise bölümün okura kazandıracağı yetiyi zayıf bir fiille anlatıyor. Okur bölümü bitirdiğinde hangi mimarinin neden uygun olduğunu ve aynı paylaşım kararının iki sonucu nasıl etkilediğini açıklayabilmeli.

## Giriş ile bölüm arasındaki görev paylaşımı

- I-A satır 40–60, kaynak paylaşımının yarar/ödünleşim üretebildiğini ve fiziksel bağlamın tasarım seçimine yön verdiğini söyleyerek gerekçeyi kuruyor.
- I-C satır 182–210, üç soruyu ve ilk iki katkıyı açıkça tanımlıyor: ne paylaşılıyor, performans nasıl etkileniyor, sonuç başka sisteme ne ölçüde taşınabilir. Section II açılışı bunları aynen tekrarlamak yerine cevaplamayı sağlayacak kavramlara geçmeli.
- II-A fiziksel gözlemi, II-B paylaşım ve optik kısıtları, II-C ölçütleri, II-D ortak çalışma noktalarını açıklıyor. Sıra tutarlı; dört altbölümü yeniden kurmak gerekmiyor.
- Mevcut açılış “signal models, resource-sharing schemes, and numerical examples” diyor; II-C'nin ölçüt tanımları ve II-D'nin ortak çalışma noktaları görünür değil. Kısa yol haritasına bunları eklemek bölümün makale katkısına bağlantısını güçlendirir.

Tekrarlar otomatik olarak silinmemeli. I-A:41–49'daki fiber güç ödünleşimi, II-D:292–299'da pre-compensation karşılaştırmasından ayrılarak teknik derinlik kazanıyor; bunun ikinci kullanımı işlevsel. I-A:16–26 ile II-A:66–74'te optik üretim/RF yayılım ayrımı da aynı şekilde kısa tanıtım ve teknik açıklama görevlerini üstleniyor. İleride bir uzunluk azaltımı yapılacaksa girişteki örnekleri sıkıştırıp açıklamayı II'de tutmak mantıklı; II'nin öğretici ayrımlarını kaldırmak değil.

## Üç tamamlayıcı COMST örneği

Kaynak kökü: `C:\GH\OISAC_PRISMA_COMST\data\corp_std`.

| Çalışma ve kanıt konumu | II'nin açılışı nasıl bağlanıyor? | Bizim için alınacak ders |
|---|---|---|
| COMST_027, *A Tutorial on Beyond-Diagonal Reconfigurable Intelligent Surfaces: Modeling, Architectures, System Design and Optimization, and Applications*. `COMST_027/COMST_027.md:74–80,154–160,217–222` | Girişte sezgisel bir oyuncak örnek sunmayı katkı olarak vaat ediyor; II ilk cümlede bu amacı söylüyor ve doğrudan SISO modeline geçiyor. Sonunda bulunan kazancı ilerideki daha geniş sistemlere bağlıyor. | II, girişte vaat edilen bir işi somut olarak başlatıyor. Bizde eşdeğeri tek evrensel model değil, gözlem→kaynak→iki performans sonucu bağlantısını görünür kılan sınırlı örnekler. |
| COMST_051, *Near-Field Communications: A Comprehensive Survey*. `COMST_051/COMST_051.md:172–182,289–299` | II, EM geçmişinden başlayıp fizik, haberleşme ve bilgi kuramı bakışlarına gerekçe veriyor; ardından kanal modeli→anten→EMIT sırasını açıklıyor. III açılışı bu temelleri kanal modellemeye taşıyor. | Disiplinleri tek cümlede sıralamak yerine her birinin okuyucuya neden gerekli olduğunu açıklama ilkesi yararlı. Fakat tarihsel/genel giriş bizim mevcut açılıştan daha sıkı değil; yayımlanmış olması tüm üslup seçimlerini model yapmaz. |
| COMST_037, *Enabling Intelligent Connectivity: A Survey of Secure ISAC in 6G Networks*. `COMST_037/COMST_037.md:59–64,157–163,236–246,263–267` | Giriş yeni üç katmanlı mimariyi katkı sayıyor; II doğrudan bu mimariyi tanıtıyor. Mimari→ölçütler→platform akışı sonraki katman bölümlerinin düzenini kuruyor. | Kavramsal yapı makalenin geri kalanını organize ediyor. Bununla birlikte bu çalışmanın tanıtım ağırlıklı üstünlük dili ve çok genel ölçüt listesi, bizim kaynak temelli fiziksel karşılaştırmamız için uygun örnek değil. |

Bu üçü, tek bir COMST açılış kalıbı olmadığını gösteriyor. Ortak başarılı hareket, girişteki katkı vaadini II'de teknik işleme dönüştürmek. Bizim bölüm başlığı *Technical Foundations of O-ISAC* bu görevle uyumlu.

## Önerilen açılış yönü

Tercihim mevcut ikinci cümlenin bilimsel ilişkisini ilk sıraya alan B seçeneği. A, platform çeşitliliğini daha belirgin vurguluyor. Bunlar tartışma taslaklarıdır; kaynağa uygulanmadı. Kelime sayıları İngilizce boşlukla ayrılmış sözcük sayısıdır; tireli ifadeler tek sözcük sayılır.

### A — fiziksel çeşitlilikten tasarım yorumuna (101 sözcük)

> Across fiber, optical wireless, and photonics-enabled wireless systems, O-ISAC relies on different physical interactions and receiver observations. These differences determine what can be sensed, which resources can be shared, and how a design choice affects communication and sensing performance. Understanding them is therefore necessary to interpret the reported benefits and limitations of integration. This section explains the signal paths and sensing observations, examines resource sharing and optical signal constraints, and defines the relevant performance measures. Representative examples then show how joint operating points connect shared design choices to both outcomes, providing a basis for the architecture and joint-design analyses that follow.

### B — tasarım kararından fiziksel açıklamaya (88 sözcük)

> The performance of an O-ISAC system depends on how its shared resources support data recovery and the physical measurement of interest. Fiber, optical wireless, and photonics-enabled wireless systems differ in their signal paths, receiver observations, and hardware constraints. This section explains how these differences shape resource sharing and communication and sensing performance. We introduce the relevant signal models and performance measures, then use representative examples to connect design choices to joint operating points. These foundations support the analysis of architectures and joint-design results in Sections IV and V.

Her iki taslakta da optiğin tüm platformlarda hedefe yayıldığı varsayılmıyor, paylaşımın zorunlu performans kazancı olduğu söylenmiyor ve tek modelin tüm modaliteleri kapsadığı iddia edilmiyor. Girişte kurulan motivasyon, II'de fiziksel açıklama ve yorumlama becerisine dönüştürülüyor.

## Küçük yapısal öneriler

1. Bölüm açılışını yaklaşık 80–100 sözcükte, bir amaç ve bir sıra açıklamasıyla tutmak yeterli. Bu bir dergi kuralı değil; mevcut dört altbölüm için editoryal hedef.
2. II-A ilk paragrafındaki haberleşme ve algılama tanımları (16–24) kısa ve öğretici; sırf tekrar korkusuyla silinmemeli. Sensing'in ölçtüğü parametreyi alıcı gözlemine bağlaması bölümün omurgası.
3. II-B'de IM/DD modele geçerken platform sınırlarının görünürlüğü korunmalı; bütün O-ISAC için nonnegative intensity model sunuyormuş gibi genellenmemeli. Mevcut 124–127 ayrımı bu açıdan değerli.
4. II-C'deki nominal çözünürlük/ölçülen hata ve OSNR/elektriksel SNR ayrımları tutulsun. Makalenin asıl katkısını destekleyen teknik açıklamalar bunlar.
5. II-D sonundaki ölçüm uyumluluğu paragrafı (323–332) teknik yorumdan derleme yöntemine uygun geçiş; bu kuralları açılışın baskın gerekçesi yapmak bölümü öğreticilikten yöntem/denetim diline çeker.

