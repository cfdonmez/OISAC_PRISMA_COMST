# Önceki sürümle karşılaştırma

16 Eylül 2026 · Yerel dal: `rev/flow-20260916` · Referans: `0d5d6f8`

[Yeni makale](output/pdf/flow.pdf) · [Bilimsel ek profiller](output/pdf/profiles.pdf) ·
[Önceki sürümün kaynak ve PDF arşivi](archive/base.zip) · [Metin farkı](archive/text.diff)

## Sonuç

Makale artık fiziksel paylaşım → değiştirilen tasarım parametresi → iki işlevin
çıktısı → deney desteği → uygulama koşulları → yeni araştırma soruları sırasını
izliyor. Yalnız bölüm başlıkları değiştirilmedi; tekrarlanan sınıflandırma
turları, kaynak listeleri ve yöntem açıklamaları temizlendi.

| Gösterge | Önce | Sonra |
|---|---:|---:|
| Makale, kaynakça dahil | 29 sayfa | 20 sayfa |
| Ana bölüm | 8 | 8 |
| Şekil | 10 | 5 |
| Tablo | 7 | 7; işlevleri yeniden düzenlendi |
| Yaklaşık sözcük sayısı, başlık/tablo/açıklamalar dahil | 14.691 | 11.239 |
| Ana metindeki farklı atıf anahtarı | 229 | 134 |
| İnceleme kapsamı | 206 çalışma / 227 rapor | Aynı |

Sözcük hesabı aynı kaynak-temelli yöntemle yapıldı; yaklaşık %23,5 azalma var.
Atıf sayısındaki düşüş, uzun sıralamaların seçilmiş açıklayıcı örneklere
dönüştürülmesinden geliyor. 227 uygun raporun tam bibliyografyası, 206 çalışmanın
listesi ve kanıt kayıtları frozen ST-01/S-Evidence içinde korunuyor.
Bu revizyon yeni literatür taraması veya corpus elemesi yapmadı.

## Bölümler birlikte nasıl değişti?

| Bölüm | Yapılan değişiklik | Diğer bölümlerdeki karşılığı |
|---|---|---|
| I | Motivasyon ve katkılar korundu; tekrarlanan platform görseli kaldırıldı; I-C kısa kaldı. | Fiziksel açıklama tek yerde, II'deki yeni sinyal-yolu şekline bağlandı. |
| II | İki ikonlu şekil vektöre çevrildi; tek formülü tekrar eden çözünürlük grafiği kaldırıldı; sayısal örnekler üç okunaklı sütuna toplandı. | III mimari seçimi, IV sonuçların mekanizmasını kullanıyor; metrik tanımları tekrar edilmiyor. |
| III | Platform ve entegrasyon türlerini iki kez sıralamak yerine hedef yolu, paylaşılan eleman ve sınırlandırıcı etki izlendi. | Ortak ayarlanabilir değişken IV'ün başlangıcı; kontrol döngüleri VI'ya açılıyor. |
| IV | Kaynak/zaman → güç → geometri → waveform/işleme düzeni; yedi koşullu örnek ve somut mekanizma şekli. | V bu sonuçların hangi deneylerle desteklendiğini sorguluyor. |
| V | İki geniş sayım figürü yerine deney ortamı ve 12/6 saha ayrımı; artifact erişimi ile yeniden kurma koşulları açıklandı. | VI'daki hizmet iddiaları için hangi test desteğinin eksik olduğu belirginleşti. |
| VI | Teknoloji kataloğu yerine trafik, yönlendirme, insan/ortam, inference ve ağ işletimi. | VII'de ölçülebilir deneylere dönüşen gereksinimler; tablo tekrarları azaltıldı. |
| VII | Kayıt tutma görevleri yerine beş araştırma sorusu, değiştirilecek koşul ve bilgilendirici çıktı. | Olumsuz sonucun da hangi tasarım sınırını göstereceği açıklandı. |
| VIII ve Abstract | Gerçek mekanizmaları ve koşullu sonuçları özetleyecek şekilde yeniden yazıldı. | Gövdede gösterilmeyen bir benchmark, frontier veya üstünlük vaat edilmiyor. |

## Görseller ve tablolar

- Fig. 1 seçim akışı korundu. Yeni Fig. 2–5: fiziksel sinyal yolları, kaynak
  paylaşımı, üç somut mekanizma ve saha doğrulama kapsamı. Dört yeni şeklin
  tamamı düzenlenebilir SVG ve gömülü yazı tipli PDF; en küçük yazı 7,5 pt.
- Eski platform turu ve sinyal yolu arasındaki tekrar kaldırıldı. Kutulardan
  oluşan entegrasyon dökümü ile zorunlu sıra izlenimi veren teknoloji zinciri
  ana metinden çıkarıldı. Fiziksel bileşenler uygun simge ve ikonlarla gösterildi.
- Platform tablosu artık sayı yanında mimari kararı ve fiziksel sınırı anlatıyor.
  Metrik dökümü yerini kaynak–değişken–iki çıktı–koşul tablosuna bıraktı.
- Uygulama ve araştırma tabloları tam genişlikte, kısa karşılaştırmalar olarak
  düzenlendi. Sayısal dağılımlar ve tam TQAF profili 6 sayfalık bilimsel ek
  dosyaya taşındı; özgün frozen kaynaklar değiştirilmedi.

## Bilimsel doğruluk ve sonuçların sınırı

- 118 kaydın doğrulanmış bağımsız karşılaştırma gibi sunulması düzeltildi;
  bunlar yalnız koşullu adaylar. Bu envanter detayı supplement'te bulunuyor.
- SCR00057'de sabit iletişim launch gücü ile sabit toplam güç ayrıldı.
  Alıcı kestirimiyle sağlanan 2,4 dB pre-compensation kazancı, güç süpürmesinin
  sonucu gibi sunulmuyor.
- SCR00083'te ortak ASK/FMCW üretimi, farklı alıcı konfigürasyonları ve
  sweep/occupied bandwidth ayrımı korundu. 0,55 cm hata ile 2,4 cm nominal
  çözünürlük birbirinin yerine kullanılmıyor.
- SCR00007 pilot hatası hedef konum hatası değil. Zero padding yeni bağımsız
  mesafe bilgisi veya kendi başına fiziksel çözünürlük artışı sağlamıyor.
- VI'daki kestirim yaşı ve hareket açısı örneği, varsayımları açıklanmış
  öğretici kinematiktir; veri fit'i veya literatürden yeni bir ölçüm değildir.
- Saha sayıları frozen S7'den doğrulandı: 12 çalışma, iki işlevde saha çıktısı
  raporlayan alt küme 6. Bu sayıların hiçbiri eşzamanlılık onayı değildir.

## Fizibilite ve etki değerlendirmesi

| Ölçüt | Değerlendirme |
|---|---|
| Ana fikir okunabiliyor mu? | Her bölümün sorusu, girdisi ve sonraki bölüme taşıdığı sonuç [flow.md](governance/flow.md) içinde eşlendi; katkılar gerçek gövdeyle denetlendi. |
| Kapsam kaybı oldu mu? | Altı fiziksel aile ve kritik istisnalar korunuyor. Ayrıntılı envanterler bilimsel supplement'te, uzun önceki anlatı karşılaştırma arşivinde. |
| Yeni iddialar destekli mi? | Ek deneyler açıkça öneri; hareket denklemleri açık varsayımlı örnek. Yeni ölçüm, havuzlanmış frontier veya evrensel platform üstünlüğü üretilmedi. |
| Sonuç başka sisteme aktarılabilir mi? | Yalnız tanımlanan görev, ölçüm düzlemi, bütçe ve koşullar altında; bunu sınayacak deneyler VII'de. Gerçek deneysel fizibilite iddiası yapılmıyor. |
| Dizgi ve taşınabilirlik | 20 sayfa; tüm şekil/tablo sayfaları incelendi. Hazır vektörlerle normal LaTeX derlemesi yeterli; yeni adlar kısa. |
| Kalan bağımlılıklar | Yazarın bilimsel okuması, birlikte OSF güncellemesi ve yeni dalın GitHub'a aktarılması. Bu işler makaleye iç süreç anlatısı olarak eklenmedi. |

Kaynak/atıf/sayı/derleme kontrolleri [result.json](governance/qa/flow/result.json)
içinde; görsel inceleme aynı PDF hash'ine bağlı. Hatalı veya eksik atıf/çapraz
atıf, kayıp görsel, overfull kutu, kırpılma veya çakışma bulunmadı. Makaledeki
yedi underfull dizgi uyarısı görünür sayfalarda incelendi; son kaynakça
sayfasında kalan beyaz alan için içerik veya yazı boyutu zorlanmadı.

Yazar onayı ve OSF güncellemesi teknik QA'dan ayrı aşamalardır.
