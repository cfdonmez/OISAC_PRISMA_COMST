# 👁️ Phase 2: Görsel Analiz (Visual Analysis) Detayları

> **"Resimlere Fısıldayan Yapay Zeka"**

Mühendislik makalelerinde en kritik bilgiler (performans eğrileri, bit hata oranları, sistem şemaları) genellikle metinde değil, şekillerde gizlidir. **Phase 2**, bu "görünmez" veriyi görünür kılar.

---

## 🎯 Amaç
Phase 1'in ayırdığı resim dosyalarına bakıp şunları anlamak:
1.  Bu resim ne? (Sistem diyagramı mı? Sonuç grafiği mi?)
2.  Eğer grafikse, X ekseni ne? Y ekseni ne? En iyi sonuç kaç?
3.  Eğer diyagramsa, sistem nasıl kurulmuş?

---

## ⚙️ Motor: Google Gemini 2.5 Flash

Bu iş için Google'ın **Gemini 2.5 Flash** modeli seçilmiştir.

*   **Neden Flash?** Çok hızlıdır, maliyeti düşüktür (veya ücretsiz kotası cömerttir) ve görsel okuma yeteneği (OCR + Reasoning) çok yüksektir.

---

## 🛠️ Teknik İşleyiş (`process_visual_batch`)

Bu süreç `extraction_pipeline_v3.py` (ve V4 tarafından çağrılan) içinde `phase2_visual_analysis` fonksiyonuyla yönetilir.

### 1. Resim Filtreleme
Her resim analiz edilmez. Önce bir elemeden geçer:
*   Küçük ikonlar, logolar elenir (`width < 150px`).
*   Sadece `.jpg`, `.png`, `.jpeg` uzantıları alınır.

### 2. Batch (Toplu) İşleme
API limitlerine takılmamak ve hızlanmak için resimler gruplar (Batch) halinde gönderilir.
*   **Batch Size:** 5 Resim.
*   **Rate Limit:** Dakikada 15 istek (Free Tier sınırlarına saygı duyar). Arada bekleme (`time.sleep`) koyar.

### 3. Prompt Mühendisliği
Modele her resim için şu komut gönderilir:

> *"Analyze this image. If it's a chart, extract the data points (X vs Y). If it's a diagram, explain the flow. If it's setup photo, describe the hardware."*

---

## 📂 Çıktı Dosyası: `visual_analysis.txt`

Bu fazın çıktısı tek bir metin dosyasıdır. Makale klasörüne kaydedilir.

**Örnek İçerik:**

```text
Image [O_ISAC_045_3.jpg]:
This is a Bit Error Rate (BER) vs SNR graph.
- Modulation: 16-QAM
- It hits the FEC limit (3.8e-3) at roughly 18 dB SNR.
- The red line shows the proposed unified waveform performance.

Image [O_ISAC_045_7.png]:
Block diagram of the transmitter.
- Laser Source -> Phase Modulator -> EDFA -> Collimator.
- FPGA is used for digital signal generation.
```

---

## 💡 Neden Önemli?
Phase 3'teki ana beyin (Llama 3.3), resimleri **göremez** (veya görmek çok pahalıdır). Ona bu `visual_analysis.txt` dosyasını veririz.

Böylece Llama şunu diyebilir: *"Görsel analiz dosyasında belirtildiği üzere, Şekil 7'de FPGA tabanlı bir verici kullanılmış ve 18 dB SNR'da başarılı olunmuş."*

[🔙 Ana Kılavuza Dön](v4_pipe_expl.md)
