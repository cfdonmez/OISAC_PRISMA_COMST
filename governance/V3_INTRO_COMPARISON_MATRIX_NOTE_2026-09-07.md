# V3 Introduction karşılaştırma matrisi

Tarih: 7 Eylül 2026. Durum: Yazar okuma sürümü.

## Yapılan değişiklik

- Yalnız V3 içindeki `manuscript/sections/01_INTRODUCTION.tex` düzenlendi.
- Table I, konu grupları yerine beş tekil çalışma ve bizim survey'imiz için
  altı ortak inceleme boyutu kullanan karşılaştırma matrisine dönüştürüldü.
- Eski GH tablosunun çalışma-satır / inceleme-ekseni düzeni ve iki sütun
  genişliğindeki LaTeX yaklaşımı kullanıldı. Eski veri, kaynak hükümleri,
  Tier sınıfları ve puanlar taşınmadı.
- Kaynaklar geniş boyutlarda örtüştüğü için hücreler var/yok puanları yerine
  incelemenin nasıl yapıldığını gösteren kısa ifadelerle yazıldı.
- Related Surveys konumlandırma paragrafı ve üç katkı güncellendi.
  Katkılar fiziksel paylaşım, performans mekanizmaları ve değerlendirme
  öncelikleri üzerinden kuruldu.
- Bizim sayısal sütunumuz mevcut metindeki metrik/koşul yorumunu ifade eder.
  Gerçekleştirilmiş bağımsız çalışmalar arası sayısal benchmark iddiası yoktur.
- Yeni kaynak eklenmedi. Bu seçki, bütün ilgili survey'lerin envanteri değildir.
  Önceki ST-RS1 kaydı tarihsel haliyle korundu. O kayıttaki eski Table I
  yerleşim alanları bu V3 seçkisinin güncel eşlemesi olarak kullanılmamalıdır.
  Bu çalışma bir supplement/release güncellemesi değildir.

## Hücrelerin kaynak dayanağı

Aşağıdaki yerel tam metinlerde ilgili teknik bölümler kullanıldı.
Eski makalemizin hücre işaretleri bilimsel kanıt sayılmadı.

- Wen 2024, `C:/OISAC/git_recovery_agent_full_corpus_20260824_01/data/proc_md/O_ISAC_021/O_ISAC_021.md`.
  Sistem yapısı ve Fig. 1, satır 39-77. Sayısal simülasyon ve Fig. 4,
  131-149. Kaynak tahsisi 151-163. Gelecek yönleri 165-189.
- Liang 2024, aynı kökte `O_ISAC_303/O_ISAC_303.md`.
  Bölüm 3, satır 220-268. Table 3, 294-318 ve Table 4, 330-341.
  Prototip/model sınamaları 268 ve 360. Gelecek yönleri 428-494.
- Lyu 2026, aynı kökte `O_ISAC_070/O_ISAC_070.md`.
  Table I, satır 37-65. Bölüm II-III, 69-147. Deneyler ve koşulları
  Bölüm IV, 149-203. Bölüm V, 207. DOI mevcut bibliography ile eşleşir.
  Eski O_ISAC_070 kimliği Wang survey'i değildir.
- Zhang 2026, `C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/reading_text.md`.
  Optik kapsam ve örnekler 387-449. Hibrit mimariler ve ödünleşimler
  482-525. Uygulama koşulları 526-595. Yönler 600-625.
  Hücreler genel RF literatürünü değil optik/RF-optik kısmını temsil eder.
- Mohsan 2026, aynı okuma kökünde `P02/reading_text.md`.
  Kapsam 388-458 ve 662-680. Paylaşım 824-908. Table 5, 1038-1131.
  Tasarım ve kaynak tahsisi 1137-1361 ve 1554-1569. Araştırma yönleri
  2474-2690 ve Table 9, 2823-2940. Deney tablolarında Tx/Rx ve test alanı
  bulunduğu korunarak ifade edildi.
- Bizim satırımız, mevcut II ve IV'teki fiziksel paylaşım açıklaması,
  V'teki metrik/koşul ve mekanizma sentezi, VI'daki doğrulama incelemesi,
  VIII'deki benchmark ve ortak bozucu-etki test önerilerine dayanır.

## Koruma ve kontrol

- Önceki giriş `section1_before_comparison_matrix_2026-09-07.tex`
  dosyasında birebir korundu.
- İşlem öncesi/sonrası 16 kaynak dosyanın SHA-256 kontrolünde yalnız
  Introduction değişti. Diğer dokuz bölüm, dört BibTeX dosyası, main.tex
  ve onaylanan giriş görseli aynı kaldı.
- Girişin Background and Motivation metni ve Fig. 1 bloğu birebir aynı.
- Bir Table I, beş önceki çalışma satırı, bir This survey satırı ve üç
  katkı maddesi mevcut. Girişteki 17 farklı atıf anahtarı derlemede çözüldü.
- latexmk derlemesi başarıyla tamamlandı. Son logda undefined reference,
  LaTeX Warning veya Overfull kaydı yok. Önceden var olan bazı Underfull
  kayıtları diğer bölümlerde sürüyor.
- Son PDF 27 sayfa. Katkılar sayfa 2, Table I sayfa 3.
  Son çıktının 1-5. sayfaları yeniden görüntülenerek kontrol edildi.
- git diff --check geçti. Bu kontrol, önceki V3 değişikliklerini geri almaz.

PDF: `output/pdf/OISAC_COMST_V3_INTRO_COMPARISON_MATRIX_2026-09-07.pdf`

SHA-256

- PDF: FC5EDF3BC06B0B671B4FBC4B9BF64751ED8549CE5926273A4C80654137889F95
- Güncel giriş: 799FFE5654939F37F3E5A108FC4BC14AA210B1259B93416FB4142753D9388706
- Önceki giriş/yedek: 81AFD2B2966D8956BE32ABF481A15F2A67072CB5F536780161A3170456A1BC6E
