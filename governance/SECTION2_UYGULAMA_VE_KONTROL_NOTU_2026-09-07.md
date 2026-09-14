# Section II uygulama ve kontrol notu

Tarih: 2026-09-07. Çalışma ağacı: `C:\OISAC\worktrees\comst-v3-20260906`.

## Yazım öncesi beş soruluk çalışma haritası

| Alt bölüm | Temel soru | Öğretilecek kavram | Kritik bilimsel ayrım | Somut çıktı | Sonraki bağlantı |
|---|---|---|---|---|---|
| II-A | Fiziksel büyüklük hangi gözlemden elde edilir? | Etkileşim, işaret yolu, alıcı ve ölçüm noktası | İleri/geri gözlem ve doğrudan/koherent algılama. Optik üretim ile RF yayılımı | Göreve uygun gözlem ve alıcı yolunu belirleme | II-B bu yolda paylaşılabilen kaynağı ve ayarı belirler. IV fiziksel mimarileri inceler |
| II-B | Hangi kaynak hangi sınır altında paylaşılır? | Zaman/frekans tahsisi, dalga biçimi, alıcı bilgisi ve optik güç bütçesi | Yoğunluk kısıtı ile karmaşık örnek gösterimi. Bias ile veri taşıyan güç. Paylaşım ile bant değişmezliği | Uygulanabilir ayarları ve iki işlevi bağlayan mekanizmayı seçme | II-C bu ayarların etkisini ölçülebilir çıktılara bağlar |
| II-C | Bildirilen sayı hangi görevi ve istatistiği ölçer? | Hız, BER, çözünürlük, hata ve ölçüm yeri | Nominal ayırma ölçeği/ölçülen hata/teorik sınır. OSNR/elektriksel SNR | Anlamı ve koşulu belirlenmiş metrik çiftleri | II-D ortak ayarla bağlantıyı kurar. V performansı bu ayrımlarla yorumlar |
| II-D | Bir ayar iki sonucu hangi koşulda bağlar? | Ortak işletim noktası, kontrollü tarama, servis kısıtları ve baseline | Ayrı test/ortak ayar. Sabit haberleşme gücü/sabit toplam güç. Öğretici optimizasyon/ölçülmüş Pareto cephesi | Çalışma içi ilişkiyi yorumlama ve başka bir deneyle karşılaştırmanın koşullarını belirleme | III kaynak hazırlığı, IV/V sentez, VI doğrulama ve VIII deney öncelikleri |

Başlangıçta mevcut kullanıcı değişiklikleri saptandı. `main.tex`, I, II ve III
zaten Git'e göre değişmişti. Bu tur için mevcut dosyalar esas alındı.
Değiştirilecek iki dosyanın geri alınabilir kopyaları ve başlangıç SHA-256
manifesti `section2_before_prompt_application_2026-09-07/` altında tutuldu.
Ekli reçete ile governance kopyasının metin farkı yoktur, satır sonları farklıdır.

## Uygulanan değişiklikler

Section II metin revizyonu ve üç dış üretim promptu tamamlandı. Dört alt bölüm,
beş numaralı denklem, üç mevcut şekil ve sayısal tablonun görevleri korundu.
Metin 29 sayfalık güncel PDF'nin 3–6. sayfalarında bulunuyor. Yeni görsel
üretilmedi veya yerleştirilmedi. Mevcut şekiller metnin açıklamasını taşımaya
yeterli olduğundan metin için bekleyen zorunlu bir görsel bağımlılığı yok.

| Yer | Önce | Sonra ve öğretici sonuç |
|---|---|---|
| II-A | Modelin nicelikleri ve B'ye geçiş daha örtüktü | Güç, akım, responsivity ve parametre vektörü açıklanıyor. Doğrudan algılama modeli kendi rejiminde kalıyor. Fiziksel yolun sonunda paylaşılabilir kaynak sorusu doğuyor |
| II-B | İşbirliği, desteklenmeyen `without changing the occupied bandwidth` genellemesine bağlanıyordu | Alıcı frekans cevabı ve uzamsal/zamansal ayrıştırma mekanizmaları açıklanıyor. Bias, ortalama güç ve tepe sınırı birlikte yorumlanıyor. OFDM örneği açıkça simülasyon ve nominal frekans ızgarası olarak sunuluyor |
| II-C | Bazı değerler tabloda ve metinde tekrarlanıyordu. Ölçüm tanımları önceki ayardan kopuk açılıyordu | Ayarın etkisinden metrik anlamına geçiliyor. Tahmini hız/throughput, nominal çözünürlük/ölçülen hata/teorik sınır ve OSNR/elektriksel SNR ayrılıyor. Fiber ve VLC değerleri tabloda, ilişkileri metinde tutuluyor |
| II-D | Ortak nokta tanımı doğrudan ayrı testleri de içeren tabloya bağlanıyordu | Tablo metrik ve koşul örneği olarak tanıtılıyor. Ortak koşul, ayrı test ve eşzamanlı çalışma ayrılıyor. Fiber ön telafisi ile güç taraması ayrı kalıyor. Servis kısıtlı formülasyon öğretici olarak niteleniyor. Eş kaynak bütçeli baseline, VI/VIII'e gerçek içerik üzerinden bağlanıyor |

## Üç katkının güncel makale içindeki karşılığı

Güncel Abstract ve I–II tamamen okundu. Bağımsız mimari okuma güncel I–IX
TeX'lerini kapsadı. Ana uygulamada III–IX'in amaç, tanım, ilgili sentez ve
II'ye bağlı pasajları ayrıca kontrol edildi. Eski ilişkilendirme notu veya
önceki PDF sayfa sayısı güncel doğrulama sayılmadı.

| Section I katkısı ve somut pasajı | Revize II temeli | Mevcut sonraki kullanım |
|---|---|---|
| I-C 187–193, `sensing paths` ve `allocated resources` üzerinden fiziksel seçim | II-A 15–79, gözlem/alıcı/ölçüm yolu. II-B 84–150, paylaşım ve uygulanabilir işaret | IV 5–11 fiziksel platform ve bağlaşım eksenleri. IV 274–299 donanım/taşıyıcı/dalga biçimi. IV 352–369 mimariden tasarım kararına sentez |
| I-C 195–201, çalışma içi ilişki ve koşullu karşılaştırma | II-C 155–236, metrik anlamı. II-D 241–384, ortak ayar ve karşılaştırma koşulları | V 87–184 metrik anlamları, 199–205 ve 313–327 ortak değişkenler, 550–567 karşılaştırma koşulları |
| I-C 203–209, ayrı işlev baseline'ları ve ortak testler | II-D 375–391, kaynak bütçesi, görev koşulu ve doğrulama | VI 43–67 test koşulları, 89–102 aynı konfigürasyon/zaman bağı, 172–184 benchmark gereksinimleri. VIII 72–80 ve 111–116 bozucu etkiler ve baseline'larla ortak testler |

III 68–80, ayrı ölçümleri ancak kaynak ortak ayara bağladığında birlikte
yorumlar ve II-D'ye yönlendirir. II inceleme sürecini tekrar etmez. VII 34–66
fiziksel gözlem zincirini, 144–153 ve 264–270 uygulama koşullarını taşır.
VII 283–296 ağ rolünü standart uygunluğu veya hazır olma iddiasından ayırır.
IX 3–27 fiziksel rol, koşullu performans ve deneysel ilerleme yönünü toplar.
Abstract 13–20 görev, ölçüm düzlemi, koşul ve doğrulamayı birlikte tutar.
II, bu bölümlerde bulunmayan deney, model, benchmark veya ortak Pareto cephesi
vaat etmez. Aşağıdaki kapsam dışı uyumsuzluklar bu eşleşmeden ayrıdır.

## Kaynaklardan alınan üç anlatı ilkesi

1. **Fiziksel yol → gözlem → model.** [P02 teknik pasajı](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:1394) ileri/yansıyan yol ve IM/DD uyarlamasını ilişkilendirir. [COMST_041](C:/OISAC/git_recovery_agent_full_corpus_20260824_01/data/proc_md_cprev/COMST_041/COMST_041.md:140) modeli ölçüm noktasına ve ortam kaybına bağlar. II-A'da model, ortam ve alıcı açıklamasından sonra gelir ve optik üretim/RF yayılımı ayrı kalır.
2. **Ayarın işlevi ile tükettiği kaynağı birlikte açıkla.** [P02](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/reading_text.md:1182) bias gereksiniminden bias/alt taşıyıcı güç seçimine ilerler. [P01](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:780) tasarım stratejisini iki görevin gereksinimlerinden türetir. II-B'de biasın kırpmaya ve güç bütçesine etkisi, sonra iki çıktının farklı tepkisi açıklanır.
3. **Sayısal/model sonucunu yorumlayarak sonraki soruyu doğur.** [COMST_041](C:/OISAC/git_recovery_agent_full_corpus_20260824_01/data/proc_md_cprev/COMST_041/COMST_041.md:191) kapasite rejimlerini yorumlayıp modülasyon/kodlama ihtiyacına geçer. [P01](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md:808) haberleşme çıktısını algılama koşuluyla birlikte sunar. II-C çözünürlük hesabından hata istatistiğine, II-D ise ortak koşul ve kontrollü değişime geçer.

P01 COMST, P02 Optical Switching and Networking makalesidir. Bu turda seçili
teknik pasajlar okundu, 76 makalenin tamamı yeniden incelenmedi. Örneklerin
anlatı işlevi kullanıldı, kalıp cümleleri veya bilimsel iddiaları aktarılmadı.
Aktif kurallar, house-style ve iddia dili reçetesi okundu. Güncel kullanıcı
kararları tarihsel biçim/kelime kotası kurallarından önce uygulandı.

## Birincil kaynak ve sayı kontrolü

| Kaynak ve doğrudan okunan pasaj | Kontrol sonucu |
|---|---|
| [Fiber SCR00057](C:/OISAC/reviewmdS/01_fulltext/include/B01/FT016_SCR-00057_pre_compensation_of_lfm_sensing_probe_via_integrated_sensing_and_communi.md:48), satır 26 ve 48–54 | 40 km, iki 30 GBaud 16-QAM, 500 MHz prob, 200 Hz, 1 m nominal çözünürlük ve 10 m gauge length doğrulandı. 2.4 dB titreşim spektrumu SNR kazancı ön telafi karşılaştırmasına ait. Ayrı taramada haberleşme launch gücü 0 dBm, toplam güç sabit değil |
| [VLC SCR00196](C:/OISAC/git_recovery_agent_full_corpus_20260824_01/data/proc_md/O_ISAC_185/O_ISAC_185.md:47), satır 47–59, 71–118 ve 150–158 | Ortalama alma/filtreleme mekanizması doğrulandı. 225 mW, 1 GHz, 2 m, 0.6 × 0.6 m, tahmini 3.35 Gbit/s ve 3.16–3.52 aralığı kaynakla uyumlu. 1 mm/4 cm statik ayrıştırma ve 39 fps farklı testler. Satır 114 ayrıca eşzamanlı dinamik veri/konum gösterimini destekliyor. Öngörülen upload feedback gerçek zamanlı kapalı döngü diye sunulmadı |
| [THz SCR00083](C:/OISAC/reviewmdS/01_fulltext/include/B01/FT019_SCR-00083_terahertz_isac_with_simultaneous_fast_swept_fmcw_radar_and_high_speed_wi.md:129), satır 129–149 | 262.1–268.3 GHz, 6.2 GHz, 400 ns/chirp, 1 m'de 15 Gbit/s ve BER 2.97e-3, yaklaşık 36.2 GHz işgal bandı doğrulandı. İki ayrı alıcı düzeni ile eşzamanlı ASK/FMCW modülasyonu ayrıldı. 0.55 cm maksimum hata, 20–45 cm statik hedefler ve yaklaşık 2.4 cm nominal çözünürlük aynı ölçü değildir |
| [Wen optik OFDM kaynağı](C:/OISAC/git_recovery_agent_full_corpus_20260824_01/data/proc_md/O_ISAC_021/O_ISAC_021.md:145), satır 145–163 | 256 × 3.9 MHz = 998.4 MHz nominal ızgara, 32 sembol ve 200 m FSO modeli simülasyondur. Bias/kırpma açıklaması kaynağa dayanır. Kaynaktaki normalize SNR tanımı OSNR veya ölçülen receiver SNR diye aktarılmadı |

Sayısal eğri yeniden çizilmedi. Mevcut PGFPlots kaynağında
`14.9896229 / B_s(GHz)` dönüşümü, çift log eksenler ve 6.2 GHz noktasının
2.4176811129 cm verdiği hesapla doğrulandı. Yeni deneysel nokta türetilmedi.
Kaynak MD'lerdeki mevcut şekil açıklamaları kullanıldı; bu turda birincil
PDF şekilleri yeniden açılmadı. Yeni/genişletilmiş nicel sonuç üretilmedi.

## Görsel ve tablo görevleri

- Şekil 2 fiziksel yol ve ölçüm noktalarını, Şekil 3 kavramsal zaman/frekans tahsisini, Şekil 4 hesaplanan nominal çözünürlük ölçeğini taşır.
- Tablo II üç sistemin sayısal değerlerini kendi koşullarıyla verir. Aynı satır tek eşzamanlı ölçüm olarak tanımlanmaz.
- II-D'de tablo ve kısıtlı optimizasyon yeterlidir. Yeni bir şeklin açıklayacağı gerekli ek ilişki saptanmadı.
- [Figür prompt dosyası](C:/OISAC/worktrees/comst-v3-20260906/governance/SECTION2_FIGUR_PROMPTLARI_2026-09-07.md) üç ayrı, bağımsız İngilizce blok içerir. Caption, tam etiketler, yerleşim, oklar, veri/denklem ve üretim sonrası kontrol her bloğun içindedir.
- Mevcut caption'lar mevcut içerikle sınırlı tutuldu. Şema bloklarının alıcı aşamalarını topladığı ve probun seçenek olduğu açıklandı. Yeni brif etiketleri/panelleri makaleye yerleştirilmiş gibi anlatılmadı.

## Kapsam dışında kalan düzeltmeler

1. [V 25–29](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:25) ve [VI 156–161](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex:156) hâlâ II'de adlandırılmış bir `comparison profile` tanımlandığını söylüyor. II teknik koşulları açıklıyor, bu isimle kayıt profili tanımlamıyor. Öneri, ilgili ifadeleri II'deki `measurement definitions and comparison conditions` ile ilişkilendirmek. II'ye J kodu eklenmedi.
2. [IV 324–328](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex:324) SCR00083 için `measured concurrent configuration` diyor. Kaynak eşzamanlı ASK/FMCW modülasyonunu, ancak iki ayrı performans alıcı düzenini destekliyor. Öneri, eşzamanlı modülasyonla farklı alıcılarda yapılan performans değerlendirmelerini açıkça ayırmak. Bu bulgu eşzamanlı sinyal üretiminin olmadığı anlamına gelmez.
3. [V 63](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:63) ve [V 552–555](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:552), 118 kaydın çalışmalar arası karşılaştırma rolünü ileri sürüyor. Bu mimari okuma fiilen yapılmış karşılaştırma gruplarını doğrulamaz. İddianın karşılaştırma grupları ve taşıyıcılarıyla ayrıca temellendirilmesi gerekir. Bu, bu turda kesinleşmiş sayısal veri hatası değildir.

Bu dosyalara dokunulmadı. Section II revizyonu tamamlanmıştır, bütün makalenin
anlamsal uyumu tamamlanmış sayılmaz. Bu düzeltmeler ayrı kullanıcı yönlendirmesi
gerektiren kapsam dışı işler olarak bırakıldı.

## Nihai doğrulama

- Kaynak/teknik yorum ve anlatı/makale bağlantısı için iki bağımsız AI son okuması yapıldı. Revize II içinde düzeltme gerektiren yeni sorun saptanmadı. Bunlar insan reviewer veya yazar onayı değildir.
- Section II'nin 14 etiketi korundu. Tüm bölüm dosyalarındaki 28 farklı çapraz atıf hedefi ve 229 farklı cite anahtarı çözümleniyor. Denklemler, birimler ve kısaltmalar gözden geçirildi.
- Okura görünen metin, caption ve tablo notlarında iki nokta/noktalı virgül yok. Yazar adı + et al., cover-letter/dergi uygunluğu, tarama emeği, korpus/takvim ve iç süreç dili taraması temiz. Denklem ve float gövdeleri dışındaki sezgisel cümle taramasında 38 kelimeyi aşan cümle bulunmadı. Bu tarama otomatik bir bilimsel kalite puanı değildir.
- `latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex` manuscript klasöründe başarıyla tamamlandı. Çözümlenmemiş/mükerrer atıf-etiket, eksik karakter ve overfull sayısı sıfır.
- Son logda 10 underfull uyarısı var. Biri II-B'deki OFDM paragrafına ait, diğerleri yazar bilgisi, başka bölümler, sayfa yerleşimi ve kaynakçadadır. Bunlar saklanmadı. Windows Perl locale uyarısı derlemeyi durdurmadı.
- Yalnız etkilenen 3–6. sayfalar son derleme üzerinden bir kez render edilip açıldı. Metin, denklem ve tablo kesilmesi/çakışması görülmedi. Tablonun tüm satırları ve notları okunuyor. Bütün PDF görsel olarak yeniden taranmadı.
- Başlangıç manifestindeki 121 dosyanın 119'u aynı hash'te. Değişen mevcut dosyalar yalnız II TeX'i ve figür prompt dosyası. Section I ve tablosu/şekli, Abstract, III–IX, main.tex, bibliyografyalar ve 14 görsel girdisi başlangıçla aynı. Orijinal/V2, RC1 ve veri tabanlarına yazılmadı.
- Tek kapsamlı önce/sonra farkı ve makine kontrol sonuçları [QA klasöründe](C:/OISAC/worktrees/comst-v3-20260906/governance/qa/section2_prompt_application_2026-09-07) saklandı. Yedekler [başlangıç klasöründe](C:/OISAC/worktrees/comst-v3-20260906/governance/section2_before_prompt_application_2026-09-07) bulunuyor.

## Teslim dosyaları

- [Güncel Section II TeX](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex)
- [Güncel derleme PDF'si](C:/OISAC/worktrees/comst-v3-20260906/manuscript/main.pdf)
- [29 sayfalık okuma PDF'si](C:/OISAC/worktrees/comst-v3-20260906/output/pdf/OISAC_COMST_V3_SECTION2_PROMPT_APPLICATION_2026-09-07.pdf)
- [Üç bağımsız İngilizce figür promptu](C:/OISAC/worktrees/comst-v3-20260906/governance/SECTION2_FIGUR_PROMPTLARI_2026-09-07.md)

Okuma PDF'si yeniden açıldı ve derleme çıktısıyla aynı SHA-256 değerini verdi.
`B5001B42162171D15A75FEA54748624AACC8513AAE1ABAD84DA46EAE800056EB`

Metin ve prompt teslimi tamamlandı. Dış görsel üretimi, üretilmiş yeni görsellerin
kontrolü ve makaleye yerleştirilmesi bu turun teslimi değildir. Teknik doğrulama
bilimsel kabul veya gönderim onayı sayılmaz.
