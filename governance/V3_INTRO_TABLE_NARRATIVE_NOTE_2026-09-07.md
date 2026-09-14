# V3 Introduction: tablo ve anlatının birlikte yeniden kurulması

7 Eylül 2026. Yazar okuma sürümü.

## Kapsam ve kurgu

Yalnız manuscript/sections/01_INTRODUCTION.tex içindeki Related Surveys,
Table I ve katkı maddeleri düzenlendi. Background and Motivation, Fig. 1,
korpus kapsamı ve diğer bölümler korundu. Önceki giriş
section1_before_table_narrative_2026-09-07.tex dosyasında saklandı.

Kaynaklar hazır MD/metin sürümlerinden incelendi; kaynak PDF'ler yeniden
işlenmedi. Örneklerin sözcükleri değil, karşılaştırmayı gerekçelendirme yapısı
kullanıldı: teknik ihtiyaç, önceki incelemelerin odakları, bu ayrımı gösteren
tablo, açık kalan yorumlama sorusu ve onu karşılayan katkılar.

- P01 Zhang: reading_text.md 129-233. Tematik literatür grupları, sentez,
  Table I bağlantısı ve aynı eksenlere bağlı katkılar.
- P02 Mohsan: reading_text.md 238-253, 318-384. Önceki çalışmalar, kapsam
  karşılaştırması, amaç ve katkılar. Tanıtım/ilk olma iddiaları aktarılmadı.
- COMST_002: data/proc_md_cprev/COMST_002/COMST_002.md 45-105.
  Teknik problem, related surveys, Table I, ihtiyaç ve katkılar.
- COMST_005: data/proc_md_cprev/COMST_005/COMST_005.md 63-88, 165-213.
  Yaklaşım eksenleri beam-management sorusuna bağlıdır. Ayrıntılı tablo
  Section II-C'dedir; katkılar Introduction'da daha önce gelir.

COMST kaynak kökü:
C:/OISAC/git_recovery_agent_full_corpus_20260824_01/

P01/P02 kaynak kökü:
C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/

## Tablo eksenleri ve hücre dayanakları

Genel numerical results / joint design / future directions sütunları yerine
Main focus, üç optik platform ve iki review-approach sütunu kullanıldı.
Kaynakların sayısal/kontrollü analizleri Related Surveys metninde açıkça
anlatıldı. Yeni sütunlar, eski sütunların yeniden puanlanması değildir.

- Fiber, fiberin kendisindeki algılamayı gösterir; yalnız fiber taşıma sayılmaz.
- Study selection, açık arama ve uygunluk prosedürünü gösterir.
- Cross-study comparison rules, bağımsız çalışmalarda metrik anlamı, ölçüm
  noktası, koşul, baseline ve kanıt bakımından karşılaştırma kurallarıdır.
  Tek modelde/deneyde kontrollü dalga biçimi karşılaştırmasıyla aynı değildir.
- Dolu sembol yapılandırılmış inceleme, yarım sembol seçili tartışma veya
  tanımlanmış araştırma ihtiyacı, çizgi tanımlanan anlamda geliştirilmemiş
  boyut demektir. Çizgi bir kalite hükmü değildir.

Wen: data/proc_md/O_ISAC_021/O_ISAC_021.md 19, 43-55, 131, 145-189.
FSO mimarisi; ortak simülasyon şartlarında BER/RMSE karşılaştırması vardır.
Liang: data/proc_md/O_ISAC_303/O_ISAC_303.md 49-57, 216-370, 428-508.
VLC/hibrit performans tabloları vardır; abstract'taki systematically reviews
ifadesi tek başına açık bir çalışma-seçimi prosedürü olarak değerlendirilmedi.
Lyu: data/proc_md/O_ISAC_070/O_ISAC_070.md 27-39, 121-207.
Photonic wireless; ortak hedef tanımları ve kontrollü waveform deneyleri vardır.
Bu üç kaynakta son sütundaki çizgi, bu gerçek karşılaştırmaları inkâr etmez.

Zhang: P01/reading_text.md 387-449 fiziksel kapsamı destekler. Fiber algılama
seçili tartışma; optik ve fotonik wireless yapılandırılmış incelemedir.
474-481 ve 607-614 ortak performans ölçütü ihtiyacını destekler: son sütun yarım.
Mohsan: P02/reading_text.md 388-458, 662-680 üç platformu destekler.
1230-1293 ve 2793-2809 metrik/benchmark ihtiyacını destekler: son sütun yarım.
P01/P02'nin Introduction ve bölüm yapıları açık arama/uygunluk prosedürü sunmaz.

Bizim seçim ve karşılaştırma sütunları Section III ve Section II'ye dayanır.
Dolu comparison-rules sembolü tamamlanmış çalışmalar-arası sayısal benchmark
iddiası değildir. Katkılar II/IV, II/V ve VI/VIII bölüm çıktılarıyla eşleştirildi.
Sistematik seçim, tek başına bilimsel yenilik diye sunulmadı.

## Kontroller

- 16 kaynak dosyasının önce/sonra SHA-256 karşılaştırmasında yalnız Introduction
  değişti; diğer 15 dosya aynı. Yeni bir kaynak eklenmedi.
- Bir Table I ve üç katkı maddesi var. Kaynak-desteği ve sade dil için ayrı
  salt-okunur AI kontrolleri yapıldı; insan hakem onayı iddia edilmez.
- latexmk başarıyla tamamlandı; final logda undefined reference, LaTeX Warning,
  Overfull veya Missing character kaydı yok. git diff --check geçti.
- Final PDF 27 sayfa; 1-4. sayfalar görüntülenerek kontrol edildi. Table I
  sayfa 3, Related Surveys ve katkılar sayfa 1-3'tedir.
- Çıktı PDF ile görüntülenen manuscript/main.pdf hashleri eşleşir.

PDF: output/pdf/OISAC_COMST_V3_INTRO_TABLE_NARRATIVE_2026-09-07.pdf

SHA-256 PDF: E513F0D2B969881168A199AA420566CD1C77897487452A2927ADC4E6652A233B

SHA-256 Introduction: 7824193A8DA784C056999C83076950EE14CDF113AA37205D5CE9D8BA3AB3E82F

SHA-256 önceki giriş: 17065E6EAFE68A830A8FD31B03DC745305FB5B4BBB02F0A1C7905C118ED39AA8
