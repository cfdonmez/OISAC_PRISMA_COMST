# 🔄 O-ISAC Günlük Çalışma Akışı (Daily Workflow)

Bu belge, O-ISAC sistematik literatür taramasının güncel kalması ve veri çıkarma sürecinin düzenli işlemesi için takip edilmesi gereken **Standart Uygulama Prosedürüdür (SOP)**. Bu adımlar, yeni bir kullanıcı için en basit haliyle kurgulanmıştır.

---

## 🌅 Sabah: Yeni Yayın Kontrolü (Arama & Eleme)
**Hedef:** Literatürdeki en yeni çalışmaları anında yakalamak.

### 1. Günlük Arama (Living Search)
*   **İşlem:** Google Scholar ve IEEE Xplore üzerindeki kayıtlı alarmlarınızı kontrol edin.
*   **Kayıt:** Yeni bir çalışma bulduğunuzda `search/search_log.csv` dosyasına DOI ve başlık bilgilerini ekleyin.
*   **Geçici ID:** Çalışmaya `O_ISAC_NEW_YYYYMMDD_01` gibi bir geçici ID atayın.

### 2. Hızlı Eleme (Living Screening)
*   **Kriter:** `protocol/prisma_proto.md` dosyasındaki Section 4 kriterlerine bakın.
*   **Karar:** `Include` (Dahil et) veya `Exclude` (Ele) kararını `screening/screening_log.csv` dosyasına işleyin.
*   **PDF:** Dahil edilenlerin PDF'ini indirin ve `data/ret_docs/` klasörüne `O_ISAC_[ID].pdf` ismiyle kaydedin.

---

## ☀️ Öğlen: Veri Fabrikasını Çalıştırma (Pipeline)
**Hedef:** Ham PDF'leri yapılandırılmış verilere (JSON/CSV) dönüştürmek.

### 3. Pipeline'ı Başlatma
*   **Dosya:** `analysis/nb/CoT_Master_Pipeline.ipynb` (Ana Notebook).
*   **Uygulama:** Colab üzerinde notebook'u açın, Drive'ı bağlayın (Mount Drive) ve tüm hücreleri çalıştırın.
*   **Otomatik Süreç:**
    1.  **Phase 1:** PDF → Markdown (Metinleştirme).
    2.  **Phase 2:** Görsel Analiz (Grafik ve diyagramların PhD seviyesinde analizi).
    3.  **Phase 3:** CoT Extraction (LLM kullanarak detaylı veri çıkarma).

---

## 🌙 Akşam: Kalite Kontrol & Senkronizasyon
**Hedef:** Çıkarılan verilerin doğruluğunu kontrol etmek ve ilerlemeyi kaydetmek.

### 4. Veri Doğrulama (QC)
*   **Kontrol:** `analysis/cot_lab/logs/` klasöründeki en son `_RESULT.json` dosyasını açın.
*   **Audit:** Teknik verilerin (EVM, Range, Data Rate vb.) makaledeki rakamlarla uyuşup uyuşmadığına hızlıca göz atın.

### 5. Kayıt ve Git (Commit)
*   **İşlem:** Çalışmalarınızı GitHub'a gönderin.
*   **Yeni PDF'ler:** `data/ret_docs/` klasöründeki yeni dosyaları da eklediğinizden emin olun.
*   **Not:** Git komutlarını biz (agent'lar) sizin için çalıştırabiliriz, sadece "commit et" demeniz yeterli.

---

## 🛠️ Temel Bilgiler Panosu

| Aşama | Girdi | Kullanılan Araç | Çıktı |
| :--- | :--- | :--- | :--- |
| **Arama** | IEEE / Scholar | Tarayıcı | `O_ISAC_XXX.pdf` |
| **İşleme** | PDF | `CoT_Master_Pipeline.ipynb` | Markdown + `.jpg` Figürler |
| **Çıkarma** | Markdown + Figür | Groq API / Llama 3.3 | `*_RESULT.json` |

---
**Son Güncelleme:** 2025-12-28
