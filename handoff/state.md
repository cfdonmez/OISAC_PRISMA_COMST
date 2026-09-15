# Güncel durum — 16 Eylül 2026

## Nerede kaldık?

Tüm makale, yazarın 16 Eylül talimatıyla fiziksel paylaşım → tasarım değişkeni →
iki işlevin sonucu → doğrulama → uygulama → araştırma sorusu akışında yeniden
işlendi. Çalışma dalı **`rev/flow-20260916`**; bu dal henüz yereldir.
Güncel okuma kopyası [flow.pdf](../output/pdf/flow.pdf), **20 sayfa**.
[Karşılaştırma](../compare.md), [metin farkı](../archive/text.diff) ve
[önceki sürüm arşivi](../archive/base.zip) birlikte korunur. Referans commit
`0d5d6f869336266fde80d8e9ad829108c29b1c7e`; önceki dal değiştirilmedi.

| Bölüm | Güncel görev |
|---|---|
| I — Introduction | Motivasyon, önceki survey'ler, kısa I-C yöntemi ve teknik katkılar |
| II — Technical Foundations of O-ISAC | Sinyal yolu, paylaşım, ölçüm anlamı ve ortak çalışma noktası |
| III — Optical Platforms and Architecture Choices | Fiziksel yolun mümkün kıldığı tasarım tercihleri |
| IV — Shared Design Choices and Joint Performance | Kaynak/zaman, güç, geometri ve işleme değişikliklerinin iki çıktıya etkisi |
| V — Joint Validation Under Realistic Conditions | Deney ortamı, iki işlevde saha kanıtı, deneyin yeniden kurulması |
| VI — Application Requirements and Network Operation | Trafik, hareket, kestirim yaşı, öğrenme ve ağ işletimi |
| VII — Research Questions and Evaluation Priorities | Kanıttan türetilen beş sınanabilir soru ve incelemenin sınırları |
| VIII — Conclusion | Koşullara bağlı mühendislik bulgusu ve bundan sonraki deneyler |

Dosya numaraları tarihsel kaldı; gerçek sıralama
[MANUSCRIPT_BODY_INPUTS.tex](../manuscript/MANUSCRIPT_BODY_INPUTS.tex) içindedir.
Eski ayrı yöntem bölümü geri gelmedi. I-C kısa kaldı; işlem geçmişi ve cover-letter
anlatısı ana metne girmedi.

## Şekiller, tablolar ve supplement

Makale 5 şekil ve 7 tablo içeriyor. Seçim akışı Fig. 1 olarak korunur.
Fig. 2–5 sırasıyla `paths`, `sharing`, `coupling`, `validation` dosyalarıdır:
gömülü yazı tipleri olan PDF ve düzenlenebilir SVG, raster nesne yok.
En küçük şekil metni 7.5 pt; eski varlıklar arşivde ve Git geçmişinde korunur.

Ayrıntılı metrik/ilişki, TQAF, yöntem, teknoloji ve uygulama profilleri
[profiles.pdf](../output/pdf/profiles.pdf) içindedir. Kaynakları
`supplement/driver.tex`, `core.tex`, `late.tex`; bilimsel yöntem anlatısı
[methods.md](../supplement/methods.md), tüm taşıyıcılar
[index.md](../supplement/index.md) üzerinden erişilir.

## Korunan bilimsel sınırlar

227 rapor / 206 çalışma; 4,779 metrik; 404 tradeoff kaydının 402'si substantive.
118 kayıt koşullu karşılaştırma adayıdır, doğrulanmış bağımsız çalışmalar arası
karşılaştırma değildir. Sayımların ayrıntısı supplement'tedir.
12 saha/deployment çalışmasının altısı iki işlevde de o düzeyde çıktı raporlar;
bu sayılar eşzamanlı ortak çalışmayı kanıtlamaz. TQAF incelemeye özgüdür ve
bağımsız doğrulanmış değildir. Frozen `supplement/v10` dosyaları değişmedi.

SCR00057 güç süpürmesi iletişim launch gücünü sabit tutar; toplam güç sabit
değildir. Ayrı pre-compensation kazancı 2.4 dB'dir. SCR00083'te alıcı
konfigürasyonları, sweep/occupied bandwidth ve çözünürlük/hata ayrıdır.
SCR00007 pilot hatası hedef-konum hatası değildir. VI'daki kestirim yaşı ve
hareket açısı denklemleri açık varsayımlı öğretici kinematiktir; corpus verisine
fit edilmiş sonuç değildir.

## Kontrol ve açık işler

[QA](../governance/qa/flow/result.json): temiz kaynak/atıf/bağlantı kontrolleri;
son makale SHA-256 `38b21adb5a55126176d3006ab6f80c059d9c6efd490093b5778a98664ee4a6b0`. Bütün sayfa incelemesi
`governance/qa/flow/paper/visual_checks.json` ile aynı hash'e bağlanır.
`python handoff/verify.py` frozen taşıyıcıları ve güncel PDF hash'ini denetler.

1. Yazar bu sürümü okuyacak; teknik QA, yazarın bilimsel onayı değildir.
2. OSF güncellemesi önceden kararlaştırılan ayrı ortak iştir. Makaledeki
   yazar-onaylı final-state arşiv cümlesi uzaktaki güncellemeyi kanıtlamaz.
3. Güncel raporlama-konumu haritası [flow.md](../governance/flow.md) içindedir;
   tamamlanmış bağımsız PRISMA checklist diye sunulmaz.
4. GitHub'a bu yeni dalın aktarılması ayrı adımdır. Eski dal/commit arşiv
   referansıdır; ham sohbetler veya global Codex ayarları bu pakete alınmadı.
5. Tarihsel COMST031 metadata sorunu bu revizyonda yeni bir corpus taramasına
   dönüştürülmedi.
