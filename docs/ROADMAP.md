# 🧭 O-ISAC Systematic Review - Yol Haritası ve Durum Paneli

Bu dosya, projenin **PRISMA 2020** standartlarına uyumunu izlemek ve sistematik inceleme sürecindeki ilerlemeyi takip etmek için "canlı" bir kontrol paneli olarak tasarlanmıştır.

---

## 📊 1. Proje Durum Paneli (Dashboard)

| Aşama | Durum | Hedef Dosya / Klasör | Notlar |
| :--- | :--- | :--- | :--- |
| **Protokol** | 🟢 Tamamlandı | `protocol/prisma_protocol.md` | PRISMA Checklist (`protocol/PRISMA_2020_Checklist.md`) eklendi. |
| **Arama (Search)** | 🟢 Tamamlandı | `data/search_logs/` | Log şablonları hazırlandı. |
| **Eleme (Screening)** | 🟢 Tamamlandı | `data/status/prisma_metrics.json` | 158 çalışma dahil edildi. Akış şeması otomatize edildi (`notebooks`). |
| **PDF Toplama** | 🟡 Sürüyor | `data/retrieved_docs/` | 10/158 PDF indirildi. Devam ediyor. |
| **Veri Çıkarma** | 🟡 Sürüyor | `data/extraction_results_v3` | V3 Pipeline aktif. Tam metin işleme sürüyor. |
| **Yazım (Writing)** | 🟡 Hazırlık | `survey_writing_guide.md` | Yazım kılavuzu hazır. Sentez aşamasına geçiliyor. |

*(Semboller: 🟢 Tamam, 🟡 Sürüyor, 🔴 Başlamadı, ⚪ Beklemede)*

---

## ✅ 2. PRISMA 2020 Uyumluluk Durumu
*Detaylı eşleşme için `protocol/PRISMA_2020_Checklist.md` dosyasına bakınız.*

### Kritik Eksikliklerin Giderilmesi:
- [x] **Checklist:** Resmi PRISMA maddeleri protokole eşlendi.
- [x] **Flow Diagram:** Otomatik üretim scripti (`PRISMA_Flowchart_Generator.ipynb`) hazır.
- [x] **Writing Guide:** IEEE COMST ve PRISMA uyumlu yazım şablonu oluşturuldu.

---

## 📝 3. Adım Adım Yapılacaklar Listesi (To-Do List)

### Aşama 1: Hazırlık & Standartlar (TAMAMLANDI)
- [x] Protokolü hazırla.
- [x] PRISMA 2020 Checklist ve Akış Şeması altyapısını kur.
- [x] Arama Günlüğü (Search Log) şablonunu oluştur.
- [x] IEEE COMST Yazım Kılavuzunu hazırla.

### Aşama 2: Veri Çıkarma ve Analiz (ŞU ANKİ AŞAMA)
- [ ] **PDF Toplama:** Kalan 148 PDF'i `data/retrieved_docs/` klasörüne ekle.
- [ ] **Full Extraction:** V3 Pipeline ile tüm PDF'lerden yapısal veri çıkar.
- [ ] **Reasoning Extraction:** LLM ile derinlemesine analiz (Challenge, Future Direction) modülünü çalıştır.
- [ ] **Metrics Update:** Her parti bitiminde `prisma_metrics.json` dosyasını güncelle.

### Aşama 3: Sentez ve Yazım (GELECEK)
- [ ] **Fundamentals Bölümü:** `survey_writing_guide.md` rehberliğinde Temel Kavramlar bölümünü taslağa dök.
- [ ] **Taxonomy Visualization:** "Cabled vs Wireless" taksonomisi için Sunburst grafiği oluştur.
- [ ] **Trade-off Analysis:** Extraction sonuçlarından (Rate vs Sensing) performans grafiklerini çiz.
- [ ] **Drafting:** Makalenin diğer bölümlerini (Methods, Results, Discussion) yaz.

---

**Son Güncelleme:** 2025-12-09
**Aktif Görev:** Extraction & Reasoning Analizi