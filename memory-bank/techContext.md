# Tech Context

**Son Güncelleme:** 2025-12-16


---

## 🔬 Domain Terimleri (O-ISAC)

| Terim | Açıklama |
|-------|----------|
| **O-ISAC** | Optical Integrated Sensing and Communication |
| **Fiber-ISAC** | Fiber üzerinde sensing (DAS, vibration) + haberleşme |
| **Wireless O-ISAC** | FSO, VLC, LiDAR tabanlı ISAC |
| **FSO** | Free-Space Optical |
| **VLC** | Visible Light Communication |
| **DAS** | Distributed Acoustic Sensing |
| **OFDM** | Orthogonal Frequency-Division Multiplexing |
| **FMCW** | Frequency Modulated Continuous Wave |
| **LFM** | Linear Frequency Modulated (chirp) |
| **IM/DD** | Intensity Modulation / Direct Detection |
| **TFLN-MZM** | Thin-Film Lithium Niobate Mach-Zehnder Modulator |
| **THz** | Terahertz band |

---

## 🛠️ Kullanılan Teknolojiler

### Python Paketleri

| Paket | Amaç |
|-------|------|
| `marker-pdf` | PDF → Markdown dönüşümü (OCR) |
| `transformers` | Florence-2/BLIP görsel analiz |
| `torch` | PyTorch (GPU için) |
| `flash_attn` | Model hızlandırma (Florence-2) |
| `timm` | Vision model backbone |
| `groq` | Groq API client |
| `pandas` | Veri işleme |
| `pyyaml` | YAML okuma |


### API'ler

| API | Amaç |
|-----|------|
| Groq | LLM inference (Llama 3.3 70B) |

### Modeller

| Model | Amaç |
|-------|------|
| `llama-3.3-70b-versatile` | Metin extraction (default) |
| `meta-llama/llama-4-scout-17b-16e-instruct` | Vision + metin (resim varsa) |
| `microsoft/Florence-2-large` | **Lokal** görsel analiz (Captioning/OCR) |
| BLIP | Görsel captioning (Legacy/Backup) |
| DePlot | Chart/grafik analizi (Legacy/Backup) |


---

## 📊 Extraction Şeması (Schema v2.1)

**Dosya:** `analysis/cot_laboratory/modules/formatting/schema_v2.yaml`

### Ana Bölümler

1. **reasoning_trace** - Chain-of-Thought adımları
   - `step_0_visual_inspection`
   - `step_1_concept_analysis`
   - `step_2_benchmark_verification`
   - `step_3_strategic_critique`

2. **study_level** - Paper seviyesi bilgiler
   - bibliographic (title, authors, year, venue, doi)
   - classification (medium, band, environment)
   - application (domain, scenario)
   - evidence (type, baselines, reproducibility)
   - key_contribution (contribution, gap, enablers)

3. **scenario_level** - Experiment seviyesi bilgiler
   - transmitter (source, modulation, wavelength)
   - receiver (detection, detector, processing)
   - waveform (comm, sensing, relationship)
   - channel (fiber or wireless parameters)
   - comm_metrics (rate, BER, SNR)
   - sensing_metrics (range, resolution, accuracy)
   - tradeoff (coupling, type, control)

---

## 📏 Metrikler

### Communication Metrikleri
- Data Rate (Gbps)
- BER (Bit Error Rate)
- SNR (dB)
- Spectral Efficiency (bits/s/Hz)

### Sensing Metrikleri
- Range Resolution (m)
- Sensing Range (m)
- Range Accuracy (m)
- Velocity Resolution (m/s)

---

## 💻 Çalışma Ortamı

- **Platform:** Google Colab
- **GPU:** T4 veya A100 (Phase 1 & 2 için)
- **API Key:** Colab Secrets'da `GROQ_API_KEY`
- **Drive Path:** `/content/drive/MyDrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST`
