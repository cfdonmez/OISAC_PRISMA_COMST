# Dengeli ve Tam Revizyon Karşılaştırması

Durum: `DECISION_SUPPORT_ONLY`

| Boyut | Dengeli revizyon | Tam revizyon |
|---|---|---|
| Ana amaç | Hoca yorumunu gönderimi aşırı geciktirmeden kapatmak | Hoca yorumunu mümkün olan en geniş kanıt yeniden doğrulamasıyla kapatmak |
| Sayısal kanıt kapsamı | Hedef 34--36, sert sınır 30--40 seçilmiş kayıt | Koşullu karşılaştırma bayraklı 118 kaydın tamamı |
| Kaynak kapsamı | Yaklaşık 11 rapor; seçim sonucuna göre kesinleşir | 15 çalışma / 16 rapor |
| İnsan doğrulaması | Seçilen bütün kayıtlar için iki bağımsız insan + adjudication | 118/118 kayıt için iki bağımsız insan + adjudication |
| Ana metin ürünü | 6--8 koşul-tam operating-point/karşılaştırma kartı ve bir yöntem-karar matrisi | 12--20 ana metin anchor'ı, karşılaştırma grupları ve tam 118 kayıtlık supplement atlası |
| Bölüm etkisi | Abstract, I, III, IV--IX; en büyük değişim V ve VIII | Abstract, I, III, IV--IX; IV--VIII bilimsel olarak geniş yeniden yazılır |
| Taxonomy | Korunur; karar ve lesson katmanıyla tamamlanır | Korunur; fiziksel rejim, operating point ve transfer sınırıyla yeniden bağlanır |
| Cross-study yaklaşımı | Yalnız tam eşleşen koşullarda sınırlı, sıralamasız kartlar | Tam comparison-group kataloğu; uygun grupta bounded comparison, diğerlerinde gerekçeli non-pooling |
| Roadmap | 5 öncelik için ölçülebilir deney reçeteleri | 5 öncelik + kanıt izleme + modality-specific stress test ve dependency |
| Tahmini emek | 44--52 kişi-saat | 99--124 kişi-saat |
| Tahmini takvim | 6 aktif gün; yazar döngüsüyle 7--10 gün | Paralel iki doğrulayıcıyla 3--4 hafta |
| Sayfa hedefi | 29--30; mevcut float'lar yeniden işlevlendirilir | 29--30; ayrıntının tamamı supplementte tutulur |
| Başlıca risk | Seçim yanlılığı ve modalite dengesizliği | Süre, uyuşmazlık yükü ve aşırı geniş yeniden yazım |
| Submission hızı | Yüksek | Orta/düşük |
| Savunulabilirlik | Yüksek, fakat seçilmiş kanıtla sınırlı | En yüksek, fakat daha pahalı ve daha yavaş |

## Karar kuralı

Gönderim önceliği baskınsa ve en az 30 çift-doğrulanmış kayıt koşuluyla
savunulabilir kartlar üretilebiliyorsa `balanced_revision` tercih edilir.

Tam 118 kayıt için iki doğrulayıcı ve adjudicator ayrılabiliyor, ekip 3--4
haftalık takvimi kabul ediyor ve amaç submission hızından çok gelecekte de
kullanılacak kapsamlı bir sayısal atlas üretmekse `full_revision` tercih edilir.

İki seçenek de şu durumlarda `NO-GO` olur:

- 27 sayfalık kaynak baseline hash ile doğrulanamazsa;
- insan doğrulaması tamamlanmadan yeni sayılar ana metne taşınırsa;
- uyumsuz platformlar tek bir performans sıralamasına zorlanırsa;
- yeni gönderim PDF'i 30 çift sütun sayfayı aşarsa;
- okuyucu yöntemi, koşulu, baseline'ı, sonucu ve sonraki deneyi çıkaramazsa.

## Seçeneklerin karşılaştırılacağı nihai puanlama

| Ölçüt | Ağırlık |
|---|---:|
| Kanıt doğruluğu ve izlenebilirlik | 25 |
| Okuyucu yararı ve lessons learned | 25 |
| Teknik karşılaştırma ve roadmap somutluğu | 20 |
| Genel iletişim okuyucusu için anlaşılabilirlik | 10 |
| Sayfa ekonomisi | 10 |
| Build, citation ve görsel QA | 10 |

Hard gate'lerin tamamını geçmeyen aday puanlanmaz. Gerekirse iki dal topluca
birleştirilmez; doğrulanmış baseline'dan yeni entegrasyon kopyası açılır ve
yalnız açıkça onaylanan değişiklikler tek tek taşınır.
