# Table I sembollü sürüm

Tarih: 7 Eylül 2026. V3 yazar okuma sürümü.

- Kullanıcı isteğiyle optik kapsam kısa metin olarak korundu ve diğer beş
  sütun dolu daire, yarım dolu daire ve kapsam dışı çizgisiyle tanımlandı.
- Dolu daire, ayrılmış bir tartışma veya tabloda ayrıntılı incelemeyi;
  yarım daire sınırlı tartışma ya da seçili örnekleri gösterir.
  İşaretler kapsam içindeki inceleme derinliğini anlatır, kalite puanı değildir.
- Kaynak dayanakları V3_INTRO_COMPARISON_MATRIX_NOTE_2026-09-07.md dosyasında
  korunmuştur. Eski GH tablosunun hücre hükümleri aktarılmadı.

Sütun sırası paylaşım / sayısal sonuçlar / ortak tasarım / koşul ve doğrulama /
araştırma yönleri şeklindedir. A = ayrıntılı, K = kısmi.

| Çalışma | Sembol kararları | Gerekçe |
|---|---|---|
| Wen | A / A / A / A / A | Fig. 4 koşulları ve dalga biçimi/kaynak tahsisi ayrıntılıdır. |
| Liang | A / A / A / K / A | Bölüm 3 ortak tasarımı işler. Doğrulama prototip işaretleri ve seçili sistem sınamalarıyla sınırlıdır. |
| Lyu | A / A / A / A / A | Metrik tablosu, ortak amaçlar, koşullu deneyler ve araştırma yönleri ayrılmış bölümlerdedir. |
| Zhang | A / K / A / A / A | Yalnız optik ve RF-optik kısım değerlendirilir. Sayısal sonuçlar seçili örneklerdir. |
| Mohsan | A / A / A / A / A | Deney tabloları, kaynak tahsisi, test koşulları ve teknik araştırma yönleri birlikte işlenir. |
| Bu survey | A / K / A / A / A | Sayısal sonuçların mevcut ana metindeki kullanımı metrik/koşul ve mekanizma yorumuna dayanır. Araştırma yönleri somut değerlendirme öncelikleri olarak ele alınır. |

- Seçkide kapsam dışı bir hücre olmadığından çizgi yalnız açıklamada yer alır.
- Yalnız Table I ve tabloya yönlendiren cümle değişti. Contributions, diğer
  bölümler, main.tex, BibTeX dosyaları ve görsel değişmedi. 16 dosyanın
  önce/sonra hash kontrolünde 15 dosya aynı, yalnız Introduction farklıdır.
- Önceki giriş section1_before_symbol_matrix_2026-09-07.tex dosyasında korundu.
- Wasy sembolleri yalnız tablo grubunda tanımlandı. Ek preamble değişikliği yok.
- latexmk tamamlandı. Undefined reference, LaTeX Warning, Missing character
  ve Overfull hatası yok. git diff --check geçti.
- 27 sayfalık PDF'de Table I sayfa 3'tedir. Sayfa 2-5 görüntülenerek kontrol
  edildi. İlk denemedeki tek satırlık taşma, yönlendirme cümlesi kısaltılarak
  giderildi. Son PDF, görüntülenen main.pdf ile byte düzeyinde aynıdır.

Çıktı: output/pdf/OISAC_COMST_V3_INTRO_SYMBOL_MATRIX_2026-09-07.pdf

SHA-256 PDF: C9873E0D84CA877ED1166A2D91B3B4F7E845D6AF0D8CDD0E1D73B302F45B1A79
SHA-256 Introduction: 17065E6EAFE68A830A8FD31B03DC745305FB5B4BBB02F0A1C7905C118ED39AA8
