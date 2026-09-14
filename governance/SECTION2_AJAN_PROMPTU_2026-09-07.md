O-ISAC survey çalışmamızın Section II metin revizyonunu yap. Makale İngilizce, bana açıklaman Türkçe olsun. Bu görevde figür üretme veya mevcut görsel dosyalarını değiştirme. Gerekli figürler için ayrı İngilizce üretim promptları hazırlayacaksın.

Çalışma ağacı:
C:\OISAC\worktrees\comst-v3-20260906

Önce aşağıdakileri tamamen oku:
1. governance\SECTION1_RECETESI_VE_SECTION2_UYGULAMA_REHBERI_2026-09-07.md
2. governance\V3_ACTIVE_WRITING_RULES.md
3. governance\SECTION2_FIGUR_PROMPTLARI_2026-09-07.md
Bunlar yukarıdaki çalışma ağacındadır. Rehberdeki COMST house-style ve iddia dili reçetelerini de oku. En güncel kullanıcı kararları, tarihsel şablonların çelişen yazım kurallarından önce gelir.

Asıl hedef:
C:\OISAC\worktrees\comst-v3-20260906\manuscript\sections\02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex

YAZMADAN ÖNCE MAKALENİN MİMARİSİNİ KONTROL ET
Güncel Abstract ve Section I-II'yi tamamen oku. III-IX'in amaçlarını, ilgili tanımlarını, sentez/kapanışlarını ve II'ye bağımlı pasajlarını incele. Gereken yerde okumayı genişlet. Yalnız başlık veya eski ilişkilendirme notuna güvenme.

Section I'in üç katkısını kısa çalışma notunda somut pasajlarla eşleştir:
- Fiziksel tasarım seçimi → II-A/B → IV.
- Ortak performansın yorumlanması → II-C/D → V.
- Deneysel değerlendirme temeli → II-D → VI/VIII.
III yöntem, VII uygulama/ağ gereksinimleri ve IX sonuçlarıyla terim, kapsam ve çıkarım düzeyi tutarlılığını da kontrol et. Bu haritayı ana makaleye bürokratik tablo olarak ekleme. Başka bölümde bulunmayan model, benchmark, karşılaştırma veya deneyi ileride sunulacakmış gibi vaat etme.

ANLATIYI ÖRNEKLERDEN ÖĞREN
C:\OISAC\outputs\IKI_CALISMA_OKUMA_2026-09-06 altındaki P01/P02 MD'lerinin ilgili teknik bölümlerini ve rehberdeki seçili COMST örneklerini kullan. Kısa notunda aldığın üç anlatı/bağlantı ilkesini ve bizim metindeki karşılığını göster. Yalnız “COMST jargonuna uygundur” deme. Kelimeleri, övgüleri veya kaynakların iddialarını kopyalama. 76 makalenin tamamını tekrar tarayarak zaman harcama. Eski kendi survey'imiz fikir kaynağı olabilir; eski veri sayıları ve puanlarını aktarma.

SECTION II'NİN GÖREVİ
Optik/fotonik sistemin nasıl çalıştığını, neyin paylaşıldığını, sonuçların neyi ölçtüğünü ve ortak tasarımın nasıl yorumlanacağını öğret. Genel tanım listesi, ikinci Introduction veya denetim prosedürü yazma. Cover-letter ifadeleri, dergiye uygunluk/başvuru beyanları, tarama emeği, korpus sayısı, kesin inceleme takvimi ve iç kontrol dili ekleme. Gerekli yöntem ayrıntıları Methods'ta kalır. Teknik sayıları, kaynak koşullarını ve öğretici denklemleri koru.

Her subsection için temel soru, öğretilecek kavram, kritik bilimsel ayrım, somut anlayış/karar ve sonraki bağlantıyı belirle. Mevcut dört subsection'ı birlikte değerlendir:
- Signal Paths and Sensing Observations
- Shared Resources and Optical Signal Constraints
- Communication and Sensing Measures
- Joint Operating Points and Performance Interpretation
Akış fiziksel yol → ortak kaynak/kısıt → ölçüm anlamı → ortak performans yorumu olsun. III'ün yöntemini, IV'ün mimari envanterini veya V'in kapsamlı sentezini tekrarlama. İyi çalışan içeriği koru; gerçek kopuş varsa yalnız sözcük değişikliğiyle yetinme.

TEKNİK VE DİL KONTROLÜ
Rehberdeki kaynak/ölçüm sınırlarını uygula. OSNR/elektriksel SNR, nominal çözünürlük/ölçülen hata, hesap/simülasyon/deney ve sabit haberleşme gücü/sabit toplam güç ayrımlarını koru. Fiberde 2.4 dB ön telafi kazancını güç taramasıyla birleştirme. Aynı tablo satırındaki ayrı testleri tek eşzamanlı işletim noktası sanma. II-B'deki “without changing the occupied bandwidth” iddiasını ve II-D'nin tabloya geçişini kaynaktan yeniden değerlendir. Sayı, koşul, grafik noktası veya üstünlük iddiası uydurma.

Açık teknik İngilizce ve sayısal IEEE atıfları kullan. Yazar adı + et al. katalogları, genel fayda tekrarları, aşırı isim yığınları ve okura görünen cümle/caption/tablo notlarında iki nokta veya noktalı virgül kullanma. Kelime uzunluklarını zorunlu kota sayma. İç durum etiketlerini anlatıya taşıma; sonucu değiştiren eksik koşul veya karşı kanıtı gizleme.

GÖRSELLERİ ÇİZME, PROMPTLARINI TESLİM ET
Mevcut üç görsel işlevini başlangıç olarak değerlendir ve gerçekten gerekli figür sayısını gerekçelendir. Her figür için ayrı İngilizce prompt ver. Subsection/amaç/yerleşim, panel ve oklar, tam etiketler, eksen/birim, denklem veya doğrulanmış değerler, çizimin kavramsal/analitik/deneysel niteliği, yasak yanlış yorumlar, çıktı özellikleri ve önerilen caption açık olsun. Rehberdeki hazır üç brifi nihai anlatıya göre güncelle; dışarıda üretilecekler.

Hiçbir görsel dosyasını üretme/düzenleme. Mevcut figürleri değişmeden derlemede kullanabilirsin. Metin ve mevcut caption'lar yalnız gerçekten gösterilen içerikten söz etsin. Yeni figür/panel varmış gibi atıf yapma veya olmayan dosyayı LaTeX'e ekleme. Önerilen yeni caption ve yerleşim brifte kalsın.

KAPSAM VE TESLİM
Yalnız Section II TeX'ini ve görev notu/figür promptlarını düzenle. Section I, Abstract, III-IX, main.tex, bibliyografya, tüm görsel dosyaları, veri tabanları, orijinal ve RC1 sürümleri korunsun. Başlangıç durumunu/hash'leri al, değişecek dosyaları yedekle, mevcut kullanıcı değişikliklerini koru. Kapsam dışı zorunlu düzeltmeyi bildir ve kullanıcı yönlendirmesini bekle.

Sadece öneri raporunda durma. Metin revizyonunu uygula; kaynak, dil, cover-letter/prosedür dili, makale içi bağlantılar ve LaTeX kontrollerini tamamla. Mümkünse bağımsız bir teknik/anlatı okuması yaptır. Her aşamada PDF görüntüsü açma.

Sonunda güncel TeX/PDF yollarını, kısa üç-katkı/subsection eşleşmesini, yapılan düzeltmeleri, figür sayısı ve ayrı İngilizce promptlarını, kontrol sonuçlarını ver. Section I ve tüm görsellerin korunduğunu doğrula. Metin tamamlanması ile dış görsel üretimini ayrı raporla. Karşılanmayan bir kontrolü veya eksik görsel bağımlılığını gizleyerek “her şey tamam” deme.
