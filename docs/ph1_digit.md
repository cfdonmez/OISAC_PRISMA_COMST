# 📄 Phase 1: Dijitalleştirme (Digitization) Detayları

> **"Kağıdı Veriye Çevirmek"**

Bu belge, O-ISAC Veri Çıkarma Hattı'nın ilk ve en temel aşaması olan **Phase 1: PDF to Markdown** sürecinin teknik detaylarını içerir.

---

## 🎯 Amaç
Bilimsel makaleler genellikle PDF formatındadır. PDF, bilgisayarların okuması için değil, insanların "baskı alması" için tasarlanmış bir formattır. İçindeki yazı, tablo ve resimler birbirine karışmıştır.

**Phase 1'in görevi:** PDF'i, yapısal, temiz ve makine tarafından okunabilir bir format olan **Markdown**'a çevirmektir.

---

## ⚙️ Motor: `marker-pdf`

Bu işlem için `marker` adlı açık kaynaklı bir yapay zeka kütüphanesi kullanılır. Sadece "yazıyı Kopyala-Yapıştır" yapmaz, sayfayı *görür* ve analiz eder.

### Nasıl Çalışır?
1.  **OCR (Optik Karakter Tanıma):** Yazıları tanır.
2.  **Layout Analizi:** Metnin sütunlarını (column) anlar ve birleştirir.
3.  **Matematik:** Formülleri algılar ve LaTeX formatına (`$E=mc^2$`) çevirir.
4.  **Görsel Ayıklama:** Sayfadaki şekilleri kesip ayrı bir resim dosyası olarak kaydeder.

---

## 🛠️ Teknik Kurulum ve Komutlar

`extraction_pipeline_v3.py` içindeki `phase1_marker_conversion` fonksiyonu bu işi yapar. Arka planda şu komutu çalıştırır:

```bash
marker_single [PDF_DOSYASI] --output_dir [HEDEF_KLASOR] --paginate_output
```

*   `--paginate_output`: Sayfa numaralarının markdown içinde korunmasını sağlar.

---

## 📂 Girdi ve Çıktı Yapısı

### Girdi (Input)
*   Konum: `data/ret_docs/`
*   Dosya: `O_ISAC_045.pdf`

### Çıktı (Output)
`marker`, `data/proc_markdowns/` altında makale ID'si ile bir klasör oluşturur.

```text
data/proc_markdowns/O_ISAC_045/
├── O_ISAC_045.md        # <-- KRİTİK DOSYA: Makalenin tam metni
├── O_ISAC_045/          # Görseller klasörü
│   ├── O_ISAC_045_1.jpg # Sayfa 1'deki resim
│   ├── O_ISAC_045_2.png # Sayfa 3'teki tablo görüntüsü
│   └── ...
└── meta.json            # İşlem istatistikleri
```

---

## 🚨 Sık Karşılaşılan Sorunlar ve Çözümler

1.  **Tablo Kayması:** Bazen karmaşık tablolar markdown'a düzgün aktarılamaz.
    *   *Çözüm:* Phase 2 (Görsel Analiz) burada devreye girer. Tabloyu "resim" olarak ayrıca okuruz.
2.  **Formül Hataları:** Çok karmaşık denklemlerde (örn: matrisler) bazen karakter hatası olabilir.
    *   *Etki:* Genelde ihmal edilebilir, çünkü "sayısal veri" (data rate, bandwidth) genelde metin içindedir.
3.  **İşlem Süresi:** GPU kullanılırsa sayfa başına ~2 saniye sürer. CPU ile çok yavaştır.

---

## 🔗 Sonraki Adım
Burada ayrıştırılan **Metin (.md)** Phase 3'e, **Resimler (.jpg/.png)** ise Phase 2'ye gönderilir.

[🔙 Ana Kılavuza Dön](v4_pipe_expl.md)
