# Section II — teknik yeniden yazım ve okuma haritası

Tarih: 2026-09-07. Çalışma ağacı: `C:\OISAC\worktrees\comst-v3-20260906`.

Section II yeniden yazıldı. Yeni başlık **Technical Foundations of O-ISAC**.
Bölüm artık dört alt bölüm, beş numaralı denklem, üç teknik şekil ve bir
sayısal örnek tablosu içeriyor. Bu kayıt yazım ve teknik kontrolün tamamlandığını
belgeler; yeni bir insan incelemesi veya bütün makale için gönderim onayı değildir.

## Alt bölüm bazında okuma ve görsel haritası

| Alt bölüm | Yanıtladığı temel soru | Öğrettiği teknik ayrım | Şekil veya tablo | Sonraki adıma katkı |
|---|---|---|---|---|
| II-A — Signal Paths and Sensing Observations | Fiziksel büyüklük hangi sinyal yolunda gözlenir? | İleri iletim, geri saçılma, yansıma ve uzamsal yoğunluk gözlemleri; doğrudan/koherent algılama; optik üretim ile RF yayılımının ayrılması | Fig. 2, sayfa 4. İki panelli sinyal zinciri ve ölçüm noktaları | Paylaşılan kaynağın ve ölçüm yerinin fiziksel anlamını II-B ve II-C için belirler |
| II-B — Shared Resources and Optical Signal Constraints | İletişim ve algılama neyi paylaşır, optik donanım bunu nasıl sınırlar? | Zaman/frekans bölüşümü, ortak dalga biçimi, ortak altyapı ve işlem bilgisi; optik yoğunluğun negatif olamaması; bias, kırpma ve güç bütçesi | Fig. 3, sayfa 4. Üç zaman–frekans kaynak tahsisi | Ortak tasarım değişkenini ve uygulanabilir ayarları II-D'ye taşır |
| II-C — Communication and Sensing Measures | Bildirilen sayı fiziksel olarak neyi ölçer? | Net veri hızı/sembol hızı/BER; nominal çözünürlük/RMSE/maksimum hata; fiber ölçüm uzunlukları; optik OSNR/elektriksel SNR | Fig. 4, sayfa 5. Bant genişliği–nominal menzil çözünürlüğü eğrisi | Sayısal sonuçların hangi tanım ve koşulla yorumlanacağını II-D için açıklar |
| II-D — Joint Operating Points and Performance Interpretation | Ortak bir ayar iletişim ve algılama sonuçlarını nasıl birlikte değiştirir? | Aynı ayar taramasından elde edilen ödünleşim ile ayrı deneylerin sonuçları; rekabet ile işbirliği; servis gereksinimleri altında tasarım | Table II, sayfa 6. Üç kaynaklı teknik yapılandırma ve metrik örneği; denklem (5) | III'e yöntem geçişi, IV'e mimari yorum, V'e ortak tasarım ilişkileri ve VI'ya doğrulama bağlamı sağlar |

Section II sayfa 3'te başlıyor ve sayfa 6'nın başında bitiyor. Şekiller metnin
içinde atıfla tanıtıldı; tabloyu izleyen açıklama rakamları yeniden sıralamak
yerine fiziksel ilişkilerini yorumluyor.

## Sayısal içeriğin kaynakları ve korunmuş ayrımlar

### Fiber — OISAC_SCR00057

Kaynak: `C:\OISAC\reviewmdS\01_fulltext\include\B01\FT016_SCR-00057_pre_compensation_of_lfm_sensing_probe_via_integrated_sensing_and_communi.md`, satır 26–54.

- 40 km fiber, iki adet 30 GBaud 16-QAM alt taşıyıcı ve 500 MHz LFM probu.
- Eşzamanlı algılama sırasında bildirilen iletişim hızı 2 × 120 Gbit/s.
- 1 m fiber parçasına 200 Hz titreşim uygulanması; 1 m nominal uzamsal çözünürlük ve 10 m gauge length ayrı kavramlar.
- 2.4 dB algılama SNR kazanımı, iletişim alıcısının frekans cevabına dayalı prob ön dengelemesi karşılaştırmasına ait.
- Ayrı prob-gücü taramasında iletişim çıkış gücü 0 dBm'de sabit. Prob gücü arttıkça algılama SNR'si ve veri alt taşıyıcılarının BER'i artıyor. Bu tarama ile ön dengeleme kazanımı tek deney sonucu gibi birleştirilmedi.

### Görünür ışık — OISAC_SCR00196

Kaynak: `C:\OISAC\git_recovery_agent_full_corpus_20260824_01\data\proc_md\O_ISAC_185\O_ISAC_185.md`, satır 75–114 ve 147–154.

- 225 mW beyaz lazer diyot, 1 GHz alıcı, 2 m mesafede 0.6 × 0.6 m desen alanı.
- Desenler üzerinden hesaplanan veri hızı 3.16–3.52 Gbit/s, ortalama 3.35 Gbit/s.
- Ayrı deneylerde 1 mm yanal ve yaklaşık 4 cm derinlik yer değiştirmelerini ayırt etme; dinamik konumlama güncellemesi 39 frame/s.
- 1 mm bütün konumlama görevleri için bir hata sınırı olarak sunulmadı. Statik çözümleme, desen ortalaması ve dinamik güncelleme tek eşzamanlı çalışma noktasına dönüştürülmedi.

### Fotonik THz — OISAC_SCR00083

Kaynak: `C:\OISAC\reviewmdS\01_fulltext\include\B01\FT019_SCR-00083_terahertz_isac_with_simultaneous_fast_swept_fmcw_radar_and_high_speed_wi.md`, satır 125–151.

- 262.1–268.3 GHz ASK/FMCW dalga biçimi, 6.2 GHz tarama, chirp başına 400 ns.
- 1 m iletişim deneyinde 15 Gbit/s ve BER 2.97 × 10^-3. Kaynakta yaklaşık 36.2 GHz toplam işgal edilen bant genişliği.
- Ayrı alıcı yapılandırmasında 20–45 cm statik hedefler için en büyük menzil hatası 0.55 cm.
- Yaklaşık 2.4 cm nominal menzil çözünürlüğü, tarama bant genişliğinden geliyor. Hata ile çözünürlük; hedef mesafesi ile iletişim mesafesi; tarama bandı ile toplam işgal edilen bant genişliği ayrı tutuldu.
- Fig. 4 doğrudan ölçülmüş hata eğrisi değil, açıkça belirtilmiş bir fiziksel hesap. c = 299792458 m/s yaklaşımıyla 6.2 GHz için 2.417681 cm hesaplanıyor.

### Optik OFDM öğretici örneği

Kaynak: `C:\OISAC\git_recovery_agent_full_corpus_20260824_01\data\proc_md\O_ISAC_021\O_ISAC_021.md`, satır 138–159; `Wen2024OISACArchitectures`.

256 × 3.9 MHz = 998.4 MHz, yaklaşık 1 GHz frekans ızgarası; 32 sembollük çerçeve,
200 m FSO modeli. Metin bunu bir model örneği olarak tanıtıyor. Yeni birincil
çalışma veya yeni korpus kaydı olarak eklenmedi.

## İki örnek çalışma ve önceki survey nasıl kullanıldı?

- `C:\OISAC\outputs\IKI_CALISMA_OKUMA_2026-09-06\P01\reading_text.md` ve P02'nin aynı adlı dosyası üzerinden mekanizma → teknik yapılandırma → sonuç → yorum akışı incelendi. Sayısal değerler bu örneklerden kopyalanmadı; kendi kaynaklarımızdan doğrulandı.
- Eski kendi çalışmamız `C:\GH\OISAC_PRISMA_COMST\manuscript\finalShortened\bare_jrnl_new_sample4.tex` ve eski `fig_ii_1.png`, `fig_ii_2.png`, `fig2.png` görselleri referans olarak incelendi.
- Sinyal zinciri ve bant genişliği–çözünürlük fikri yeniden çizildi. THz yayılımı optik yayılımın içine yerleştirilmedi. Eski CRQ oranı, entegrasyon puanları ve eski korpus sayıları aktarılmadı.
- Grafiklerde kaynakta metin olarak bulunmayan deneysel nokta koordinatları üretilmedi. Ortak güç taramasının yönü kaynak desteğiyle metinde anlatıldı; hesaplanan çözünürlük eğrisi deneysel ölçümden açıkça ayrıldı.

## Değişiklik kapsamı ve kontrol

- Ana yeniden yazım yalnız `manuscript/sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` içinde.
- `main.tex` içine denklemler ve yerel vektör çizimler için amsmath, amsfonts, TikZ ve PGFPlots paketleri eklendi.
- Section III'te kaldırılan `tab:comparison_record` atfı, `sec:joint_performance_interpretation` atfıyla değiştirildi. Başka içerik değişikliği yapılmadı.
- Başlangıçta hash'i alınan 16 dosyadan yalnız bu üçü değişti. Introduction, Abstract, Sections IV–IX, dört bib dosyası ve Introduction görseli aynı kaldı.
- Önceki Section II, Section III ve main.tex kopyaları `governance/section2_before_technical_rewrite_2026-09-07/` içinde korundu. Orijinal ve RC1 çalışma ağaçlarında değişiklik yapılmadı.
- Kaynak/sayı denetimi ve anlatı/scope denetimi ayrı ajanlarla yapıldı. Bunlar insan hakem veya yazar onayı olarak kaydedilmedi.
- Yeni Section II metninde yazar adı + et al. biçimi yok. Sayısal IEEE atıfları kullanıldı. Okura görünen bölüm metninde iki nokta ve noktalı virgül taraması sıfır sonuç verdi.
- Son latexmk derlemesi başarılı. 28 sayfalık PDF'de çözümlenmemiş atıf, eksik karakter veya overfull uyarısı yok. Bazı underfull boşluk uyarıları devam ediyor; bunlar derleme hatası değil.
- PDF becerisiyle yalnız Section II'nin 3–6. sayfaları kontrol edildi. Son küçük denklem/şekil düzeltmesinden sonra yalnız etkilenen 4–5. sayfalar yeniden incelendi. Yeni şekillerde üst üste binen etiket veya kesilmiş içerik görülmedi.

## Çıktı

`output/pdf/OISAC_COMST_V3_SECTION2_TECHNICAL_REWRITE_2026-09-07.pdf`

28 sayfa, 2343208 bayt. Derlenmiş PDF ile dışa aktarılan kopyanın SHA-256 değerleri aynı.

`47340A307D581B8D6E4B99EA3395DE506845EB9E10928BA4A30F80FE8CA85BDC`
