# System Patterns

**Son Güncelleme:** 2025-12-11

---

## 📁 Klasör Kuralları

### Ana Yapı
```
OISAC_PRISMA_COMST/
├── analysis/          # Tüm notebook ve script'ler
├── data/              # Tüm veriler (input + output)
├── protocol/          # Değişmeyen protokol dosyaları
├── docs/              # Dokümantasyon
├── memory-bank/       # AI bağlam dosyaları
└── screening/, search/ # PRISMA kayıtları
```

### Adlandırma Kuralları

| Öğe | Format | Örnek |
|-----|--------|-------|
| Paper ID | `O_ISAC_XXX` | O_ISAC_029 |
| PDF | `[Paper_ID].pdf` | O_ISAC_029.pdf |
| Markdown klasörü | `[Paper_ID]/[Paper_ID]/` | O_ISAC_029/O_ISAC_029/ |
| Log dosyası | `[timestamp]_[paper]_[model]_RESULT.json` | 20251210_144637_O_ISAC_029_*.json |

---

## 🔄 Pipeline Akışı

```
Phase 1: PDF → Markdown
  Input:  data/retrieved_docs/O_ISAC_XXX.pdf
  Output: data/processed_markdowns/O_ISAC_XXX/O_ISAC_XXX/O_ISAC_XXX.md
  Motor:  extraction_pipeline_v3.py → phase1_marker_conversion()

Phase 2: Visual Analysis
  Input:  data/processed_markdowns/O_ISAC_XXX/.../*.jpg
  Output: data/processed_markdowns/O_ISAC_XXX/.../visual_analysis.txt
  Motor:  extraction_pipeline_v3.py → phase2_visual_analysis()

Phase 3: CoT Extraction
  Input:  Markdown + Visual Analysis
  Output: cot_laboratory/logs/*_RESULT.json
  Motor:  cot_laboratory/core/assembler.py → run_extraction()

Phase 5: Agentic Research (Deep Research)
  Input:  Paper Text / Web Search (Future)
  Output: analysis/deep_research/output/*_Evidence.md
  Motor:  analysis/deep_research/run_calibration.py → Gemini Agent
```

---

## 📝 Çalışma Kuralları

### 1. Read-Only Inputs
Kaynak CSV'leri değiştirme. Her zaman yeni output oluştur.

### 2. Protocol-Driven
Her karar `protocol/prisma_protocol.md`'ye dayanmalı.

### 3. Checkpoint Kullan
`data/extraction_results_v3/checkpoint.json` işlenmiş paper'ları takip eder.

### 4. Log Everything
Her extraction çalıştırması `cot_laboratory/logs/`'a kaydedilir:
- `*_PROMPT.md` - Kullanılan tam prompt
- `*_RESULT.json` - LLM çıktısı

### 5. Archive Don't Delete
Eski dosyaları silme, `archive/` klasörüne taşı.

---

## 🔑 Kritik Dosya Konumları

| Amaç | Dosya |
|------|-------|
| Ana notebook | `analysis/notebooks/CoT_Master_Pipeline.ipynb` |
| CoT motoru | `analysis/cot_laboratory/core/assembler.py` |
| JSON şeması | `analysis/cot_laboratory/modules/formatting/schema_v2.yaml` |
| PRISMA protokolü | `protocol/prisma_protocol.md` |
| Güncel durum | `memory-bank/activeContext.md` |
| Checkpoint | `data/extraction_results_v3/checkpoint.json` |

---

## ⚙️ Colab Ayarları

1. **Runtime:** GPU (T4 veya A100)
2. **Secrets:** `GROQ_API_KEY` ekle
3. **Drive Mount:** `/content/drive/MyDrive/...`
4. **sys.path:** Notebooks ve project root eklenmeli

---

## 🚨 Dikkat Edilecekler

- Phase 1&2 GPU gerektirir
- Groq API rate limiti var (2 saniye delay)
- JSON parse hataları olabilir (markdown wrapper)
- Drive sync gecikebilir
