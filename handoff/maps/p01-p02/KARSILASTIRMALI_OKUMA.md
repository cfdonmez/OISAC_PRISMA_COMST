# İki çalışmanın karşılaştırmalı okuması

6 Eylül 2026. Bu belge yalnız verilen PDF'lerin karşılaştırmasıdır. Projenin mevcut makalesinin tam karşılaştırmalı denetimi veya revizyon kararı değildir. Sayfalar PDF sırasıdır.

| Boyut | P01: ISAC evrim perspektifi | P02: Optik ISAC temelleri ve uygulamaları |
|---|---|---|
| Ana soru | ISAC spektrum, ağ ölçeği, algılama modalitesi, güvenlik ve standartlaşmada nasıl evriliyor? | Optik ISAC hangi sistemler, dalga biçimleri, donanımlar, metrikler ve uygulamalarla kurulabilir? |
| Omurga | Beş evrim ekseni; bölüm sonlarında lessons learned ve sorular (s.2-4, 8, 17-18, 24, 26, 29). | Teknoloji kategorileri, fiber/DOFS, mimari ve waveform, temeller, uygulamalar ve açık sorunlar (s.3-5). |
| Optiğin yeri | Geniş ISAC survey'inin özel bir alt bölümü; hibrit RF-optik ile bağlantılı (s.5-8). | Makalenin ana konusu; fiberde birlikte çalışma/ortak waveform uzun bir bölüm (s.6-11). |
| Sınıflandırma | VLC, FSO ve photonic sensing; hibritte gevşek/sıkı/işlevsel birleşim. | Aynı ana üçlü; fiber, fotonik RF, optik sensörlü uygulamalar ayrıca genişletiliyor. |
| Önceki survey'lerle konumlandırma | Tablo I, 26 önceki kayıt ve This Survey satırı; beş boyutta işaretler (s.3). | Tablo 3, sekiz önceki yayın ve Our Work satırı; anlatısal katkı karşılaştırması (s.4). |
| Nicel içerik | Kaynaklardan hız, algılama, öğrenme, kaynak tahsisi ve standart KPI örnekleri; karma görevler. | Tablo 5 optik kablosuz konumlandırma/haberleşme; Tablo 7 MWP; metinde fiber ve uygulama deneyleri. |
| Veri kümeleri | Tablo VII'de 10 RF/CSI/mmWave/multimodal veri kaynağı (s.23). | Yeni bir veri kümesi sunmuyor; bazı örneklerde kullanılan veri ve sonuçları anlatıyor. |
| Yöntem raporlaması | İncelenen PDF'de yeniden üretilebilir arama/eleme protokolü bulunmadı. | İncelenen PDF'de yeniden üretilebilir arama/eleme protokolü bulunmadı. |
| Genel güçlü yanı | Farklı teknik katmanları bir sistem evrimi anlatısında birleştirmesi. | Optik alanı fiberden serbest uzaya ve farklı uygulamalara kadar geniş örneklerle işlemesi. |
| Aktarım sınırı | Optik hava kanalı ile fotonik destekli RF ayrımı; referans ve standart tarih sorunları. | Birlikte çalışma ile ortak tasarım ayrımı; heterojen hata ölçütleri; kaynak eşleme ve bazı geniş genellemeler. |

## Birlikte okunduğunda öne çıkan tespitler

**Optik kapsam artık tek başına yeterli ayırt edici özellik değil.** P01 optiği açık bir ISAC gelişim ekseni olarak işlerken P02 doğrudan optik platformları, waveform, metrik, deney ve uygulamalarla birlikte inceliyor. “Önceki derlemeler optiği ele almıyor” veya “fiber ve FSO'yu birlikte ilk biz kapsıyoruz” gibi cümleler bu iki kaynak karşısında gerekçesiz kalır. Bu bir kaynak okuma tespitidir; projemiz için yeni bir ilk/tek iddiası kurulmadı.

**Fiziksel sınıfların sınırı önemli.** Optik kablosuz taşıyıcı, fiberde algılama/haberleşme, fotonik destekli RF taşıyıcı ve optik sensör destekli RF sistemi farklı şeylerdir. İki makalede de bunlar geniş O-ISAC anlatısı içinde yakın konumlanıyor. Aynı başlık altında bulunmaları, sayısal sonuçlarının ortak koşullarda karşılaştırılabildiği anlamına gelmiyor.

**Paylaşılan kaynak ve görev tanımı ayrı kaydedilmeli.** Ortak fiber/ayrılmış WDM kanalı, ortak çerçeveye gömülü algılama probu, gerçekten ortak taşıyıcı, kamerayla eşzamanlı veri okuma ve yalnız sensör verisinin taşınması farklı entegrasyon düzeyleri. P02 s.9-11 bu ayrımı değerlendirmek için özellikle yararlı.

**Performans tablosu ile kıyaslanabilir kanıt tablosu aynı şey değil.** Mbaud/Mbps, konumlandırma hatası/menzil çözünürlüğü, ortalama hata/%90 eşiği, gerçek zamanlı haberleşme/çevrimdışı algılama, secret key rate/klasik veri hızı ayrı tutulmalı. Arşivdeki veriler koşul notlarıyla kaydedildi; ortak üstünlük sıralaması yapılmadı.

**İki derlemede geçen aynı deney iki bağımsız kanıt sayılmaz.** Seçili kaynak eşleme dosyası ortak optik yayınları bulmayı kolaylaştırıyor. P01 [69] ile P02 [29] aynı Shi vd. JLT yayını; P01 [74] ile P02 [34] aynı Yan vd. W-band yayını. P01 [68] ve P02 [6] ise başlığı benzer konferans/dergi sürümleri; aynı rapor kabul edilmedi. Bu eşlemeler PDF künyelerine dayanır, birincil tam metin doğrulaması değildir.

**Kaynağın kendi içinde de kontrol gerektiren noktalar var.** P01'in DCO/EADO atfı ve IEEE 802.11bf zaman ifadeleri; P02'nin [108]/[109] eşlemesi, Tablo 6 işaretleri ve deney olmadığı yönündeki geniş cümlesi ayrıntılı notlarda kayıtlı. Bunlar yayınları tümden geçersiz sayma gerekçesi olarak sunulmuyor; hangi iddia için özgün kaynağa dönüleceğini gösteriyor.

Bu okuma, sonraki görüşmenin kaynak temelini hazırladı. Makale yapısı, kapsam, tablolar veya katkı ifadeleri üzerinde uygulama yapılmadı.
