# O-ISAC Extraction Tracker

Bu dosya, projenin "Soğan Yapısı" (Layered Structure) prensibine göre veri extraction süreçlerini takip eder.

### 🧅 O-ISAC Layered (Onion) Structure
Bu kampanya, veriyi merkezden dışa doğru şu katmanlarla işler:

1. **Öz (Core):** Ham PDF verisi ve Marker V1.0 ile dijitalleştirme.
2. **1. Katman (Legacy):** Temel meta-veri (O_ISAC_001 - 066).
3. **2. Katman (V4 Vision + CoT):** LLM (Llama-3.3-70b) + Vision entegreli derin analiz (O_ISAC_001 - 388+).
4. **3. Katman (Benchmark):** V4 vs Legacy kıyaslaması ve doğruluk kalibrasyonu.
5. **Dış Katman (PRISMA):** Sistematik inceleme raporu ve sentez.

---

## 📊 2. Katman (V4 Vision + CoT) Durumu
**Kapsam:** 001 - 388+ nolu tüm dahil edilen makaleler.

| Makale Grubu | Durum | Teknik Notlar |
|--------------|-------|---------------|
| **001 - 066** | ✅ Tamamlandı | Legacy verilerle kıyaslanmak üzere V4 sonuçları hazır. |
| **067 - 206** | ✅ Tamamlandı | Groq Llama-3.3-70b ile işleme tamamlandı. |
| **207 - 388+** | ✅ Tamamlandı | Batch 2 süreci sona erdi. Toplam 221 makale işlendi. |
| **Özel: O_ISAC_029**| ✅ Doğrulandı | Altın standart (Gold Standard) referans olarak belirlendi. |

---

## � Çıktı Dosyaları
- **JSON Sonuçları**: `data/ext_res_v4/`
- **Birleştirilmiş Özet**: `data/ext_res_v4/extraction_v4_summary.csv`
- **Kontrol Listesi**: `data/ext_res_v4/checkpoint_v4.json`

---

## 🔬 3. Katman (Benchmark & Kalibrasyon)
**Araç:** [06_Extraction_Benchmark_Lab.ipynb](file:///c:/Users/fatih/gdrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST/analysis/nb/06_Extraction_Benchmark_Lab.ipynb)

| Kıyaslama | Sonuç | Gözlem |
|-----------|-------|--------|
| Veri Zenginliği | 🚀 Yüksek | V4, Legacy'deki "NR" alanları %40+ oranında doldurabiliyor. |
| Akıl Yürütme | 🧠 Derin | Görsel analiz sayesinde parametrelerin "neden" seçildiği açıklanıyor. |
| Doğruluk | ✅ Orta-Yüksek | 60 GHz heterodyning gibi teknik detaylar Vision katmanında daha net yakalanıyor. |

---

## 🌍 Dış Katman (Sentez) - Gelecek Adım
- PRISMA Akış Diyagramı (Flow Diagram) oluşturulması.
- Tematik taksonomi haritasının çıkarılması.
- "Gap Analysis" temelli tez önerilerinin listelenmesi.
