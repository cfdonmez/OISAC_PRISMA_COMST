# İki çalışma - okuma ve kaynak arşivi

**Tarih:** 6 Eylül 2026  
**Durum:** OKUNDU / ARŞİVLENDİ  
**Kapsam:** Kullanıcının verdiği iki PDF'nin incelenmesi, bilgilerinin ve PDF içinde raporlanan verilerinin proje içinde saklanması. Ana survey metnine değişiklik uygulanmadı. Sonraki çalışma adımı kullanıcıyla birlikte belirlenecek.

## Hızlı erişim

| Kayıt | Çalışma | Kaynak | Ayrıntılı not |
|---|---|---|---|
| P01 | Zhang vd. (2026), *Integrated Sensing and Communications Over the Years: An Evolution Perspective* | [1.pdf](P01/1.pdf), 35 sayfa | [P01 okuma notları](P01/OKUMA_NOTLARI.md) |
| P02 | Mohsan vd. (2026), *Optical integrated sensing and communication: Fundamentals, applications, challenges and future aspects* | [2.pdf](P02/2.pdf), 37 sayfa | [P02 okuma notları](P02/OKUMA_NOTLARI.md) |

[İki çalışmanın karşılaştırmalı okuma özeti](KARSILASTIRMALI_OKUMA.md) sonraki görüşmeye kısa bir giriş sağlar. Çalışmaların yöntemi, kapsamı, güçlü yanları, veri sunumu ve aktarım sınırları burada birlikte görülebilir.

## Saklanan bilgi ve veriler

- **Özgün PDF kopyaları:** Downloads içindeki iki kaynakla SHA-256 eşleşmesi doğrulandı. PDF'ler yeniden üretilmedi veya içerikleri değiştirilmedi.
- **Tam metin ve sayfa kayıtları:** Her çalışma için `fulltext.txt`, `fulltext_layout.txt`, `pages.jsonl` ve sayfa başlıklarıyla `reading_text.md`. Toplam 72 sayfa.
- **Sayfa görselleri:** Her PDF sayfasının PNG görüntüsü `rendered_pages` içinde. Önemli tablo sayfalarının daha yüksek çözünürlüklü kopyaları da var.
- **Ayrıntılı Türkçe notlar:** Bölüm haritası, yöntem, ana savlar, metrikler, teknik sonuçlar, sayfa ve atıf bilgileri; gözlenen kaynak içi tutarsızlıklar.
- **Seçili sayısal kayıtlar:** [P01](P01/structured_evidence.json) ve [P02](P02/structured_evidence.json) içinde toplam 18 kayıt grubu. PDF'deki her sayının eksiksiz yapılandırılmış dökümü değildir.
- **Tablo verileri:** [P02 Tablo 5, 6 ve 7](P02/EXPERIMENT_TABLES.json), sırasıyla 9, 8 ve 7 satır. Tablo 6 nitel işaret karşılaştırmasıdır; diğer iki tablo sayısal sonuçlar içerir. Özgün birimler, eksik hücre işaretleri ve koşullar korundu.
- **Veri kümesi kataloğu:** [P01 Tablo VII](P01/DATASET_CATALOGUE.json), 10 kayıt. Ad, modalite, uygulama işaretleri, tabloda verilen büyüklük, sağlayıcı ve PDF'de bulunan bazı URL'ler.
- **Tablo/şekil dizinleri:** [P01](P01/table_figure_inventory.json) ve [P02](P02/table_figure_inventory.json); toplam 17 tablo ve 39 şekil için sayfa konumları. Tablo 10'un devamı ayrı tablo sayılmadı.
- **Künyeler:** [bibliography.json](bibliography.json), [references.bib](references.bib). P01'in 248, P02'nin 174 numaralı kaynak kaydı ayrıca `references_pages.txt` içinde sayfalarıyla korunuyor; kaynakça sayıları dahil edilen birincil deney sayısı değildir.
- **Ortak kaynak eşlemesi:** [shared_reference_crosswalk.json](shared_reference_crosswalk.json), seçili 13 optik kaynak ilişkisi. Konferans/dergi sürümü ilişkisi olan kayıt ayrıca işaretli.
- **Bütünlük ve köken:** [source_manifest.json](source_manifest.json), her klasörde `metadata.json` ve `pdf_links.json`, [QA_REPORT.json](QA_REPORT.json), [SHA256SUMS.txt](SHA256SUMS.txt).

## Verinin anlamı

Bu arşiv **PDF'leri ve PDF'lerde raporlanan bilgileri/verileri** saklar. Özgün çalışmaların ham deney ölçümleri, CSI/video dosyaları veya yazar depolarındaki veri setleri indirilmedi. P02, s.34'te araştırmasında veri kullanılmadığını açıkça belirtiyor. P01'deki 10 veri kümesi kaydı bir katalogdur; bu veri kümelerinin kendisi değildir. İki PDF'de gömülü ek dosya bulunmadı.

Kaynakların iddiaları ile okuma yorumları ayrıldı. Kaynak içi referans ve birim sorunları sessizce düzeltilmedi. Aktarılan sayılar birincil deneylerden bağımsız olarak doğrulanmış veya insan hakemlerce onaylanmış kayıtlar olarak kullanılmamalıdır. Dış web taraması yapılmadı; tarih ve standart bilgileri PDF'de bildirildiği haliyle ele alındı.

Otomatik metin çıkarımı özellikle denklemler, çok sütunlu sayfalar ve raster tablolar için eksik olabilir. P01 Tablo VII'nin hücreleri metin katmanında bulunmadığından görselden aktarıldı. Kesin kaynak metni ve görsel için PDF esas alınır.

## Mevcut çalışma noktası

İki çalışmanın okuması ve yerel saklama işlemi tamamlandı. Köklü değişikliklerin içeriğine ilişkin karar verilmedi. Yeni görüşmede, bu notlar üzerinden kullanıcının belirleyeceği ilk revizyon adımı ele alınabilir.
