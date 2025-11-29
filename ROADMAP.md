# 🧭 O-ISAC Systematic Review - Yol Haritası ve Durum Paneli

Bu dosya, projenin **PRISMA 2020** standartlarına uyumunu izlemek ve sistematik inceleme sürecindeki ilerlemeyi takip etmek için "canlı" bir kontrol paneli olarak tasarlanmıştır.

---

## 📊 1. Proje Durum Paneli (Dashboard)

| Aşama | Durum | Hedef Dosya / Klasör | Notlar |
| :--- | :--- | :--- | :--- |
| **Protokol** | 🟢 Tamamlandı | `protocol/prisma_protocol.md` | OSF kaydı bekleniyor. |
| **Arama (Search)** | 🟡 Devam Ediyor | `search/search_log.csv` | Veritabanı taramaları sürüyor. |
| **Eleme (Screening)** | 🔴 Başlamadı | `screening/screening_log.csv` | Duplicate temizliği sonrası başlayacak. |
| **Veri Çıkarma** | 🔴 Başlamadı | `extraction/schema/` | Şema hazır, pilot deneme yapılacak. |
| **Yazım (Writing)** | ⚪ Beklemede | `manuscript/comst_template.tex` | Analiz sonrası. |

*(Semboller: 🟢 Tamam, 🟡 Sürüyor, 🔴 Başlamadı, ⚪ Beklemede)*

---

## ✅ 2. PRISMA 2020 Uyumluluk Kontrol Listesi (Compliance Checklist)
*Makaleyi yazarken veya süreci işletirken bu maddeleri tamamladıkça işaretle (`[x]`).*

### Bölüm: Başlık ve Özet
- [ ] **Madde 1 (Title):** Başlıkta "Systematic Review" ifadesi var mı?
- [ ] **Madde 2 (Abstract):** Özet, PRISMA-Abstracts formatına uygun mu?

### Bölüm: Giriş (Introduction)
- [x] **Madde 3 (Rationale):** Neden bu incelemeye ihtiyaç duyulduğu açıklandı mı? (Bkz: `protocol/prisma_protocol.md` Sec 2)
- [x] **Madde 4 (Objectives):** Araştırma soruları (PICO/PECO) net mi? (Bkz: `protocol/prisma_protocol.md` Sec 3)

### Bölüm: Yöntem (Methods)
- [x] **Madde 5 (Eligibility Criteria):** Dahil etme/Dışlama kriterleri net mi? (Bkz: `protocol/prisma_protocol.md` Sec 4)
- [ ] **Madde 6 (Information Sources):** Tüm veritabanları ve son tarama tarihleri listelendi mi? (Bkz: `search/search_log.csv`)
- [ ] **Madde 7 (Search Strategy):** En az bir veritabanı için tam arama sorgusu verildi mi?
- [ ] **Madde 8 (Selection Process):** Eleme işleminin nasıl yapıldığı (kaç kişi, hangi araçlar) açıklandı mı?
- [ ] **Madde 9 (Data Collection Process):** Veri çekme yöntemi açıklandı mı?
- [ ] **Madde 10 (Data Items):** Hangi verilerin (sütunların) arandığı listelendi mi? (Bkz: `extraction/schema/oisac_extraction_schema.yaml`)
- [ ] **Madde 11 (Risk of Bias Assessment):** Çalışmaların kalitesini (yanlılık riski) ölçmek için hangi araç kullanıldı?
- [ ] **Madde 12 (Effect Measures):** Sonuçların nasıl özetlendiği (örn. fark tablosu, oranlar) belirtildi mi?
- [ ] **Madde 13 (Synthesis Methods):** Verilerin nasıl sentezlendiği/gruplandığı açıklandı mı? (O-ISAC için: Cabled vs Wireless ayrımı)

### Bölüm: Sonuçlar (Results)
- [ ] **Madde 16 (Study Selection):** Akış şeması (Flow Diagram) sayıları net mi? (Bkz: `screening/prisma_flow_counts.csv`)
- [ ] **Madde 17 (Study Characteristics):** Dahil edilen çalışmaların genel özellikleri tablosu var mı?
- [ ] **Madde 18 (Risk of Bias in Studies):** Her çalışma için kalite değerlendirme sonuçları sunuldu mu?
- [ ] **Madde 19 (Results of Individual Studies):** Her çalışma için özet veriler sunuldu mu?
- [ ] **Madde 20 (Results of Syntheses):** Sentez sonuçları (tablolar, grafikler) sunuldu mu?

### Bölüm: Tartışma (Discussion)
- [ ] **Madde 23a (Discussion):** Bulguların ana yorumu.
- [ ] **Madde 23b (Limitations):** İncelemenin sınırlılıkları tartışıldı mı? (Örn: Sadece İngilizce kaynaklar, gri literatür eksikliği vb.)
- [ ] **Madde 23c (Implications):** Gelecek çalışmalar (6G, O-ISAC) için öneriler.

### Bölüm: Diğer Bilgiler
- [ ] **Madde 24 (Registration):** OSF kayıt numarası eklendi mi?
- [ ] **Madde 27 (Availability of Data):** Veri setleri ve kodlar erişilebilir mi? (GitHub linki verildi mi?)

---

## 📝 3. Adım Adım Yapılacaklar Listesi (To-Do List)

### Aşama 1: Hazırlık & Arama
- [x] Protokolü hazırla.
- [ ] Veritabanı aramalarını tamamla (IEEE, Scopus, WoS, Optica, SPIE).
- [ ] Arama sonuçlarını ham dosyalara (`raw_results`) kaydet.
- [ ] `01_search_and_dedup.ipynb` notebook'unu çalıştırarak mükerrer kayıtları temizle.
- [ ] Temiz listeyi `screening_log.csv` dosyasına aktar.

### Aşama 2: Tarama (Screening)
- [ ] **Title/Abstract Screening:** Başlık ve özetlere bakarak ilgisizleri "EXCLUDE" olarak işaretle.
- [ ] **Full-Text Screening:** Kalanların tam metinlerini bul, "Include/Exclude" kararını ver.
- [ ] Hariç tutulanların nedenlerini (Reason) not et.
- [ ] PRISMA akış şeması sayılarını `prisma_flow_counts.csv` dosyasına işle.

### Aşama 3: Veri Çıkarma (Extraction)
- [ ] Pilot deneme: 5 makale ile YAML şemasını test et, gerekirse revize et.
- [ ] Dahil edilen (Included) tüm makalelerden verileri çek.
- [ ] Eksik veriler için gerekirse yazarlarla iletişime geç.

### Aşama 4: Analiz & Raporlama
- [ ] "Cabled vs Wireless" karşılaştırma tablolarını oluştur.
- [ ] Bibliyometrik analiz grafiklerini çiz (Yıllara göre yayın sayısı vb.).
- [ ] Makale taslağını (`manuscript/`) yazmaya başla.
- [ ] Kaynakçayı düzenle.