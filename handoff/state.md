# Güncel durum — 14 Eylül 2026

Bu dosya, eski hafıza ve reçetelerden önce okunacak devir özetidir.
Canlı metin ve en son kullanıcı kararı her zaman esas alınır.

## Nerede kaldık?

Makale sekiz ana bölüme indirildi. Ayrı yöntem bölümü kaldırıldı; kısa Review
Methodology anlatısı Introduction I-C'ye taşındı. Güncel okuma kopyası
[review.pdf](../output/pdf/review.pdf), 29 sayfadır. Ayrıntılı uygulama kaydı
[review.md](../governance/review.md), onaylanan plan ise
[plan.md](maps/s3/plan.md) içindedir.

| Güncel bölüm | İşlev / kaynak |
|---|---|
| I — Introduction | Mühendislik problemi, önceki survey'ler, I-C yöntem özeti, katkılar ve organizasyon; `01_INTRODUCTION.tex` |
| II — Technical Foundations of O-ISAC | Sinyal yolları, paylaşılan kaynaklar, metrikler ve ortak çalışma noktaları; `02_...tex` |
| III — Optical Platforms and Integration Architectures | `04_...tex` |
| IV — Performance Metrics and Joint Design Tradeoffs | `05_...tex`; extraction koşulları ve claim düzeyindeki çatışmalar korunur |
| V — Validation Evidence, Reconstructability, and Benchmark Readiness | `06_...tex`; TQAF tanımı ve profili buradadır |
| VI — Enabling Technologies, Application Requirements, and 6G Network Evidence | `07_...tex` |
| VII — Discussion, Research Roadmap, and Limitations | `08_...tex`; yöntemsel sınırlar korunur |
| VIII — Conclusion | `09_CONCLUSION.tex` |

Kaynak dosyası numaraları ile güncel bölüm numaraları farklıdır. Sıralamanın
otoritesi [MANUSCRIPT_BODY_INPUTS.tex](../manuscript/MANUSCRIPT_BODY_INPUTS.tex)
dosyasıdır; sırf isimleri eşitlemek için dosyaları yeniden adlandırmayın.

## Tamamlanan iyileştirmeler

- Introduction katkıları teknik sorular etrafında kuruldu; önceki survey
  karşılaştırmaları ve anlatı geliştirildi. Kullanıcının son kararıyla yöntem
  tarih/sayıları I-C'de yer alır; katkı iddiası olarak kullanılmaz.
- Section II fiziksel yol → paylaşılan kaynak → ölçüm anlamı → çalışma noktası
  sırasına göre yeniden yazıldı. Optik/RF ayrımı, OSNR/elektriksel SNR,
  çözünürlük/hata/bound ve ayrı deney/ortak çalışma noktası ayrımları korundu.
  Onaylı ikonlu figürler ve bant genişliği–çözünürlük figürü yerleştirildi.
- Eski III-A'nın geliştirilmesi ve eski Fig. 5 aralık düzeltmesi 12 Eylül'deki
  ara aşamaydı. 14 Eylül'de kısa yöntem özeti I-C'ye, ayrıntılar supplement'e
  taşındı. Eski `s3a.pdf` ve o tarihteki Fig. 5 numarası güncel değildir.
- Seçim akışı şimdi Fig. 2'dir (`selection.svg` / `.pdf`). TQAF profili güncel
  Section V / Fig. 8 içindedir. Eski analiz birimleri tablosu Table S1 olarak
  [methods.md](../supplement/methods.md) içindedir.
- Aktarım sırasında frozen v10 taşıyıcıları
  [supplement/v10](../supplement/v10/) altına eksiksiz kopyalandı ve
  [supplement index](../supplement/index.md) taşınabilir bağlantılara çevrildi.
  Özgün v10 dosyaları değişmedi; hash manifestleri korunur.

## Bilimsel sınırlar ve kararlar

227 uygun rapor = 206 çalışma + 21 companion report. 8,203 primary coding
record, 4,779 metric record ve 402 substantive relationship aynı birim değildir.
404 tradeoff kaydının ikisi tradeoff yokluğunu kaydeder. 115 synthesis group'un
111'i substantive'dır. Bunlar tek bir havuzlanmış etki veya karşılaştırma sayısı
olarak sunulmaz. 118 conditional candidate, doğrulanmış cross-study comparison
anlamına gelmez. RC1 kanıt kilitleri kendi sınırlı kapsamlarıyla okunmalıdır.

TQAF sekiz boyut ve ayrı overall contribution içerir; GRADE veya standart
risk-of-bias değerlendirmesinin yerine geçmez. Fiilî insan/AI iş akışı,
retrospektif kayıt geçmişi, rutin bağımsız çift değerlendirme ve yapılmayan
analizlere ilişkin sınırlar supplement'te korunur. Cover-letter savunusu ve
iç QA anlatısı bilimsel metne taşınmaz.

## Açık işler

1. **Birlikte OSF güncellemesi:** v10 kaynakları artık GitHub kopyasında var.
   V3 supplement anlatısı ve son makaleyle sürüm uyumunu değerlendirip OSF
   taşıyıcılarını güncellemek, erişimi ve makaledeki bağlantıyı doğrulamak kaldı.
   Metindeki final-state arşiv cümlesi yazarın açık isteğiyle kullanılmıştır;
   bu cümle uzaktaki arşivin güncellendiğini kanıtlamaz. Bu aktarım OSF'ye yazmaz.
2. Bağımsız tamamlanmış bir PRISMA checklist bulunmuş değildir. Mevcut
   reporting-location haritası checklist veya tam uyum onayı diye sunulmaz.
3. Yeni kullanıcı göreviyle kalan teknik bölümlere geçilebilir. Son turdaki
   geçiş/TQAF/limit düzeltmeleri bütün sonraki bölümlerin yeniden yazıldığı
   anlamına gelmez. Bilimsel son okuma ve yazar onayı ayrı aşamalardır.
4. Eski kaynak profillerindeki COMST031 dışlama/DOI atfı tarihsel ve çözülmemiş
   metadata sorunudur. Yeni doğrulama yapılmadan kesin corpus kuralına dönüştürmeyin.

## Kontrol durumu

14 Eylül kayıtlı QA: 29 sayfa, tüm sayfaların contact-sheet incelemesi ve
etkilenen sayfaların ayrıntılı incelemesi; undefined citation/reference,
duplicate label, missing figure/character veya overfull yok. Underfull
uyarıları kayıtlıdır. [QA sonucu](../governance/qa/review/result.json)
ve [figür kontrolü](../governance/qa/review/selection.json) korunur.

Okuma kopyasının SHA-256 değeri:
`f2e99ccbd1ea7068eb970fa99cc61a8bbf69672c4cf203b707cfb5c1aba7e84d`.
Aktarım kontrolleri `checks.json` içinde kaydedilir. Teknik kontrol sonuçları
insan bilimsel incelemesi veya submission-ready kararı değildir.
