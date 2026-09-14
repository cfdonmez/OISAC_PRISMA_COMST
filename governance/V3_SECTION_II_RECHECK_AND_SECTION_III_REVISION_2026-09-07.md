# Section II yeniden kontrolü ve Section III revizyonu

Tarih: 2026-09-07. Çalışma ağacı: `C:\OISAC\worktrees\comst-v3-20260906`.

Kullanıcının onayı doğrultusunda önce Section II yazım reçeteleriyle yeniden
kontrol edildi, ardından Section III düzenlendi. Section IV bu turda
değiştirilmedi. Önceki ilişkilendirme haritasındaki II → III → IV → V akışı
korunuyor. Section II teknik anlamı kuruyor, III kaynakların analiz birimlerine
nasıl dönüştüğünü açıklıyor, IV fiziksel platform ve kaynak paylaşımını
inceleyecek, V ise ortak performans ilişkilerinin merkezi olarak kalacak.

## Section II'de bulunan ve giderilen konular

Ana teknik kurgu korunmaya uygundu. Yeniden kontrol, yalnız olumlu bir genel
hükümle kapatılmadı. Aşağıdaki somut düzeltmeler uygulandı.

- OFDM, DC, OSNR, SNR, BER ve RMSE gibi kısaltmaların açılımları verildi. FSO yerine ilgili paragrafta açık ad kullanıldı. Tabloya özgü modülasyon kısaltmaları tablo notunda tanımlandı.
- IM/DD denkleminde alıcı çıktısının elektriksel akım olduğu ve RMSE denklemindeki kestirim/referans değişkenleri açıklandı.
- Tekrarlanan olumsuz şekil/tablo açıklamaları, fiziksel anlamı doğrudan veren cümlelere çevrildi. Hesaplanan çözünürlük ile ölçülen hata ve ayrı deney koşulları arasındaki ayrımlar korundu.
- Fig. 2'de açılımsız DSP etiketi yerine “Detection and processing” kullanıldı.
- Kapanıştaki teknik yorum ile sonraki bölümlere geçiş ayrı paragraflara ayrıldı.
- Tablo II'nin performans sayıları, örnek çalışmaları ve Section II'nin üç şeklinin bilimsel rolleri değişmedi.

## Section III alt bölüm haritası

| Alt bölüm | Okuyucunun sorusu | Somut içerik ve çıktı | Taşıyıcı ve devir |
|---|---|---|---|
| III-A — Search, Eligibility, and Study Reconciliation | Hangi kaynaklar hangi ölçütlerle seçildi ve birden çok rapor nasıl çalışma birimine dönüştü? | Arama mantığı ve 22 Haziran 2026 yürütme tarihi, yayın penceresi, teknik uygunluk, 227 rapor/206 çalışma ayrımı, fiilen yürütülen süreç ve retrospektif kayıt | Fig. 5 ve ST-01. III-B'ye çalışma/rapor birimini verir |
| III-B — Extraction and Units of Analysis | Bir çalışmadan çıkan farklı ölçüm ve ilişkiler nasıl kaydedildi? | Kaynak konumu, metrik tanımı, koşul ve baseline; ölçüm ile ilişki ayrımı; iddia düzeyinde kaynak çatışması yönetimi | Yeniden kurulan Table III. IV–VI'nın kullandığı sayıları tanımlar |
| III-C — Technical Appraisal and Synthesis | Teknik değerlendirme hangi yorumu destekler ve sentez nasıl yapılır? | Sekiz boyutlu TQAF ve ayrı overall contribution, yorumlama/aktarım ayrımı, tematik sentez ve koşula bağlı sonuçlar | Fig. 6. IV'e fiziksel rol ve ortak kaynak incelemesini devreder |

Section III sayfa 6'da başlıyor ve sayfa 8'de bitiyor. Fig. 5 sayfa 7'de;
Table III ve Fig. 6 sayfa 8'de. Section IV sayfa 8'in sonunda başlıyor.

## Tablo ve şekil kararları

Table III, yalnız nicel/nitel kullanım sayımı yerine analiz birimini açıklayan
bir tablo oldu. 206 çalışma, 8,203 birincil kodlama kaydı, 4,779 metrik kaydı,
402 bilimsel ilişki ve 115 sentez grubu birbirinden ayrıldı. Bu sayılar bir
eleme hunisi veya bağımsız deney toplamı olarak sunulmuyor.

- 8,203 = 3,020 evidence + 4,779 metric + 404 tradeoff kaydı.
- 404 tradeoff kaydının 402'si bilimsel ilişki görünümünde. İki kayıt, kaynakta tradeoff bildirilmemesini belgeleyen kayıtlar. Bunlar iki ölçülmüş olumsuz sonuç gibi yorumlanmadı.
- 115 sentez grubu içinde 111 tematik grup ve dört geniş sınıflama grubu bulunuyor. Dört sınıflama grubu bilimsel sonuç dayanağına yükseltilmedi.
- 8,306 tam kayıt = 8,203 birincil + 31 bağlamsal + 72 kaynak çatışmalı kayıt. S-Evidence yalnız kendi birincil kayıt kapsamına uygun biçimde adreslendi.

Fig. 5'in akışı ve bütün sayıları korundu. Eski PRISMA SVG'sinde
“Screening dispositions” başlığı ilk gövde satırına değiyordu. Ayrı V3
SVG/PDF kopyasında yalnız başlık 5 pt yukarı taşındı. Özgün görseller
değiştirilmedi. Fig. 6'nın veri ve çizimi korundu, açıklaması yeni anlatıyla
eşleştirildi. Bu bölümün işi performans kıyaslaması olmadığı için yeni bir
performans grafiği eklenmedi.

## Yöntem beyanlarının kaynak karşılığı

Başlıca tamamlanmış-süreç kaynakları aşağıdaki paketlerde doğrudan kontrol edildi.

- `C:\OISAC\prisma2020Review\submission_supplement_final_v10_2026-08-17\reporting\protocol\protocol_amendment_actual_workflow_2026-08-04.md` — araştırmacı gözetimi, AI destek rolleri, belirli karar paketlerinin yetkilendirilmesi ve rutin bağımsız çift inceleme sınırı.
- Aynı paketin `reporting\protocol\protocol_registration_lineage_correction_2026-08-07.md` dosyası — 12 Şubat 2026 tarihli 7f6wb retrospektif kayıt. Eski 221 sayısı ile 206 arasında doğrudan eleme hesabı kurulmadı.
- Aynı paketin `evidence\ST-22_EVIDENCE_BODY_CERTAINTY_115.csv` dosyası — 111/4 ayrımı; `ST-19_GOVERNED_TRADEOFFS_404.csv` ve `ST-19_SUBSTANTIVE_TRADEOFFS_402.csv` — 404/402 ayrımı.
- `C:\OISAC\prisma2020Review\systematic_review_workflow\07_raporlama\outputs\comst_prose_revision_2026-08-08\manuscript\comst_206_v2_9section\supplements\reporting\search\FINAL_SEARCH_METHODS_AND_EXECUTION_FOR_REPORTING_2026-08-14.md` — altı kaynak ve gerçek arama tarihi.
- Aynı reporting klasöründeki `S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md` — TQAF, anlatı sentezi ve gerçekleştirilmeyen istatistiksel değerlendirmelerin kapsamı.

Önemli sürüm ayrımı: manuscript altındaki actual-workflow kopyası AI sözünü
genelleştirmiş olsa da V10 actual-workflow dosyası AI yardımını açıkça
belgeliyor. Ana metin bu belgeli destek rolünü belirtir. AI, bağımsız insan
reviewer veya üçüncü hakem gibi sunulmaz. Sonradan incelenen 118 kayıt da bütün
tarihsel korpusun bağımsız çift insan incelemesi gibi gösterilmedi.

TQAF'ın 0–3 puanlanan, bu review için geliştirilmiş teknik/raporlama
değerlendirmesi olduğu açıklandı. Bağımsız doğrulanmış standart bir risk-of-bias
aracı gibi tanıtılmadı. Puanlama kuralları S-Protocol'a, çalışma puanları
S-Appraisal'a yönlendirildi.

P01/P02'nin mevcut MD dosyaları anlatı ve teknik kapsamın örnekleri olarak
incelendi. Ayrı sistematik seçim prosedürü bulunmadığı için bu çalışmaların
PRISMA yöntemi sunduğu varsayılmadı. Eski kendi survey'imizden seçim → çıkarım →
değerlendirme → sentez akışı yararlı bulundu; eski sayılar ve yöntem beyanları
aktarılmadı.

## Yazım ve teknik kontrol sonuçları

Kullanılan reçeteler `governance/v3_source_snapshot_2026-09-06` içindeki
COMST house style ve author-governed claim-language belgeleridir.

Otomatik önce/sonra raporları `governance/qa/SECTION_II_III_STYLE_BEFORE_2026-09-07.md`
ve `SECTION_II_III_STYLE_AFTER_2026-09-07.md` içinde.

| Ölçüm | Section II son durum | Section III son durum |
|---|---:|---:|
| Ayrıştırıcıya göre ortalama cümle uzunluğu | 15.065 | 14.131 |
| 35 kelimeyi aşan cümle oranı | %0 | %0 |
| Liste yoğun cümle oranı | %4.3 | %1.6 |
| Okura görünen metinde iki nokta/noktalı virgül | 0 | 0 |
| Yazar adı + et al. biçimi | 0 | 0 |
| Ham iç durum kodu | 0 | 0 |

Bu ölçümler şekil/tablo dışındaki otomatik TeX ayrıştırmasına dayanır; bilimsel
doğruluk veya insan onayı değildir. Reçetedeki 20–24 kelime ortalaması mekanik
bir alt sınır sayılmadı. Açık cümleler bu sayıyı tutturmak için uzatılmadı.
Section III için otomatik aracın “explicit transitions sparse” uyarısı kaldı.
Paragrafların çalışma → sonuç kaydı → teknik değerlendirme → sentez devri
ayrıca okundu; sırf uyarıyı sıfırlamak için geçiş zarfı eklenmedi.

Sayısal/yöntemsel destek ve dil/akış ayrı ajan kontrollerinden geçti. Son
öneriler uygulandı. Bu kontroller insan reviewer kararı olarak kaydedilmedi.

Son latexmk derlemesi başarılı. Çözümlenmemiş atıf, eksik karakter ve overfull
uyarısı yok. Bazı underfull satır/sayfa boşluğu uyarıları sürüyor. PDF becerisiyle
yalnız değişen şekil/tablo ve bölüm geçişi sayfaları kontrol edildi. PRISMA
başlığındaki çakışma giderildi ve son 7. sayfa yeniden kontrol edildi.

Başlangıç hash envanterindeki 28 dosyanın 25'i aynı kaldı. Değişenler yalnız
Section II, Section III ve Fig. 2'nin yerel TeX kaynağı. Yeni PRISMA SVG/PDF
kopyaları ayrıca eklendi. Introduction, Abstract, IV–IX, bibliyografya ve diğer
mevcut şekiller korunuyor. Önceki dosyalar
`governance/before_section3_revision_2026-09-07/` içinde yedeklendi.

## Teslim edilen çalışma kopyası

`output/pdf/OISAC_COMST_V3_SECTION3_REVISED_2026-09-07.pdf`

29 sayfa, 2366148 bayt. Derlenen dosya ve teslim kopyası SHA-256 eşleşmesi:

`FEFDF5086AF1FC2E286B4F393A185A31192C17CFAC3DEE1F740C825649962259`

Section III yazımı bu tur için tamamlandı. Sonraki içerik revizyonu Section IV.
Bu kayıt bütün makalenin yayın veya gönderim onayı değildir.
