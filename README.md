# O-ISAC Systematic Review

**Optical Integrated Sensing and Communication (O-ISAC)** alanında PRISMA 2020 standartlarına uygun sistematik derleme projesi.

---

## 📊 Proje Durumu

| Aşama | Durum | Detay |
|-------|-------|-------|
| Protokol | ✅ Tamamlandı | `protocol/prisma_protocol.md` |
| Arama | ✅ Tamamlandı | 1200 kayıt bulundu |
| Eleme | ✅ Tamamlandı | 158 çalışma dahil edildi |
| PDF Toplama | 🟡 Devam | 32/158 (%20) |
| Veri Çıkarma | 🟡 Devam | CoT Pipeline hazır |
| Yazım | 🔴 Beklemede | - |

---

## 📁 Klasör Yapısı

```
OISAC_PRISMA_COMST/
│
├── protocol/          # PRISMA protokolü ve checklist
├── data/              # PDF'ler ve çıkarım sonuçları
│   ├── retrieved_docs/      # Orijinal PDF'ler
│   ├── processed_markdowns/ # Markdown dönüşümleri
│   └── extraction_results_v3/ # JSON çıktıları
│
├── analysis/          # Notebook'lar ve script'ler
│   ├── notebooks/           # Colab notebook'ları
│   └── cot_laboratory/      # Chain-of-Thought sistemi
│
├── screening/         # Eleme kayıtları
├── search/            # Arama logları
├── manuscript/        # LaTeX dosyaları
├── memory-bank/       # AI context dosyaları
└── docs/              # Dokümantasyon
```

---

## 🚀 Hızlı Başlangıç

### Pipeline Çalıştırma (Colab)

1. `analysis/notebooks/CoT_Master_Pipeline.ipynb` dosyasını Colab'da aç
2. GPU runtime seç (T4 veya A100)
3. 🔑 Secrets'a `GROQ_API_KEY` ekle
4. Sırayla çalıştır

### Dokümantasyon

- [Yol Haritası](docs/ROADMAP.md)
- [Proje Durumu](docs/PROJECT_STATUS.md)
- [AI Workflow](docs/AI_Co_Pilot_Workflow.md)
- [Yazım Rehberi](docs/survey_writing_guide.md)

---

## 📚 Kaynaklar

- **PRISMA 2020**: [prisma-statement.org](http://www.prisma-statement.org/)
- **Groq API**: [groq.com](https://groq.com)

---

## 📄 Lisans

Bu proje akademik araştırma amaçlıdır.

---

**Son Güncelleme:** 2025-12-11
