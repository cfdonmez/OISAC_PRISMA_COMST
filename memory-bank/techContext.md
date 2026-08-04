# Tech Context

## 2026-08-04 authoring safety override

- The completed Phase A–F corpus-migration package is `review_package/full_corpus_206_20260804/`; Phase G reviewed manuscript integration is current.
- `manuscript/finalManuscript/bare_jrnl_new_sample4.tex` contains user changes and must not be overwritten by automated migration.
- The older active-path statements below describe historical authoring phases; verify the current Git status before editing any manuscript source.
- Corpus-derived tables and figures must be regenerated from 206 unique studies rather than edited by denominator substitution.

---

**Son Guncelleme:** 2026-03-24

---

## Operational LaTeX Context

- Aktif journal-track authoring klasoru:
  - `manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/`
- Ana manuscript dosyasi:
  - `oisac_review_working.tex`
- Frontmatter dosyasi:
  - `oisac_frontmatter.tex`
- Native section yapisi:
  - `sections/section_01_introduction.tex`
  - `sections/section_02_technical_fundamentals.tex`
  - `sections/section_03_review_methodology.tex`
  - `sections/section_04_taxonomy.tex`
  - `sections/section_05_tradeoff.tex`
  - `sections/section_06_enablers.tex`
  - `sections/section_07_applications.tex`
  - `sections/section_08_challenges.tex`
  - `sections/section_09_conclusion.tex`
- Lokal bibliography:
  - `references.bib`
- Lokal figure kaynaklari:
  - `figures/`
  - `fig_v_1.png`
  - `fig_v_2.png`
  - `fig_vi_1.jpg`
  - `fig_vi_2.jpg`
- Build script:
  - `build_oisac_review_working.ps1`
- Build zinciri:
  - `pdflatex -> bibtex -> pdflatex -> pdflatex`
- Son dogrulanan cikti:
  - `manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/oisac_review_working_build_20260324_214338.pdf`
  - `32 sayfa`
- Teknik durum:
  - unresolved citation yok
  - undefined reference yok
  - LaTeX error yok
  - overfull/underfull box ve float/page-budget sorunlari devam ediyor

---

## Domain Terimleri (O-ISAC)

| Terim | Aciklama |
|-------|----------|
| **O-ISAC** | Optical Integrated Sensing and Communication |
| **Fiber-ISAC** | Fiber uzerinde sensing (DAS, vibration) ve haberlesme |
| **Wireless O-ISAC** | FSO, VLC, LiDAR tabanli ISAC |
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

## Kullanilan Teknolojiler

### Python Paketleri

| Paket | Amac |
|-------|------|
| `marker-pdf` | PDF to Markdown donusumu (OCR) |
| `transformers` | Florence-2 / BLIP tabanli gorsel analiz |
| `torch` | PyTorch |
| `flash_attn` | Florence-2 hizlandirma |
| `timm` | Vision model backbone |
| `groq` | Groq API client |
| `pandas` | Veri isleme |
| `pyyaml` | YAML okuma |

### API'ler

| API | Amac |
|-----|------|
| Groq | LLM inference (Llama 3.3 70B) |

### Modeller

| Model | Amac |
|-------|------|
| `llama-3.3-70b-versatile` | Metin extraction |
| `meta-llama/llama-4-scout-17b-16e-instruct` | Vision + metin |
| `microsoft/Florence-2-large` | Lokal gorsel analiz (captioning/OCR) |
| BLIP | Gorsel captioning (legacy/backup) |
| DePlot | Chart/grafik analizi (legacy/backup) |

---

## Extraction Semasi (Schema v2.1)

**Dosya:** `analysis/cot_lab/modules/formatting/schema_v2.yaml`

### Ana Bolumler

1. **reasoning_trace**
   - `step_0_visual_inspection`
   - `step_1_concept_analysis`
   - `step_2_benchmark_verification`
   - `step_3_strategic_critique`

2. **study_level**
   - bibliographic
   - classification
   - application
   - evidence
   - key_contribution

3. **scenario_level**
   - transmitter
   - receiver
   - waveform
   - channel
   - comm_metrics
   - sensing_metrics
   - tradeoff

---

## Metrikler

### Communication
- Data Rate (Gbps)
- BER
- SNR (dB)
- Spectral Efficiency (bits/s/Hz)

### Sensing
- Range Resolution (m)
- Sensing Range (m)
- Range Accuracy (m)
- Velocity Resolution (m/s)

---

## Calisma Ortami

- Platform:
  - onceki extraction turlari agirlikli olarak Google Colab tabanli ilerledi
- GPU:
  - T4 veya A100 kullanildi
- API key:
  - `GROQ_API_KEY`
- Tarihsel drive path:
  - `/content/drive/MyDrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST`
- Guncel local workspace:
  - host-specific path intentionally omitted; use the repository root checked out on the current machine
