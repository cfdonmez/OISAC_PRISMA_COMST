# 📓 Analysis Notebooks

Bu klasör O-ISAC Systematic Review için Jupyter Notebook'ları ve script'leri içerir.

---

## 🎯 Ana Notebook

### `CoT_Master_Pipeline.ipynb` ⭐ YENİ
**Tek notebook ile tüm pipeline'ı çalıştır!**

| Section | Açıklama | Gereksinim |
|---------|----------|------------|
| 1. Setup & Mount | Drive bağla, API key yükle | - |
| 2. Phase 1 - Data Prep | PDF → Markdown | GPU (T4+) |
| 3. Phase 2 - Visual Analysis | BLIP/DePlot | GPU |
| 4. Phase 3 - CoT Extraction | Chain-of-Thought | Groq API |
| 5. Results & Export | Log görüntüle, CSV export | - |

**Kullanım:**
1. Colab'da aç
2. Runtime → Change runtime type → GPU (T4)
3. 🔑 Secrets'a GROQ_API_KEY ekle
4. Sırayla çalıştır

---

## 📂 Destekleyici Dosyalar

| Dosya | Rol |
|-------|-----|
| `extraction_pipeline_v3.py` | Phase 1&2 motor (PDF→Markdown, Vision) |
| `01_Data_Prep_Factory.ipynb` | Alternatif: Sadece Phase 1&2 |
| `02_LLM_Extraction_Lab.ipynb` | Alternatif: Sadece eski LLM extraction |

---

## 🧪 CoT Laboratory

Chain-of-Thought extraction sistemi `../cot_laboratory/` klasöründe:

```
cot_laboratory/
├── core/           # Python motor (assembler, batch_runner)
├── modules/        # Prompt "Lego"ları
├── recipes/        # Deney konfigürasyonları
└── logs/           # Çalıştırma kayıtları
```

Detaylar için: `../cot_laboratory/README.md`

---

## 📦 Arşiv

Eski/legacy notebook'lar `archive/` klasöründe saklanıyor:

- `PRISMA_Extraction_v2_Colab.ipynb` - Eski monolitik notebook
- `CoT_Vision_Factory_Runner.ipynb` - Legacy vision runner
- `extractionpipe.ipynb` - Çalışma defteri
- `prisma_extraction_v2.py` - Eski v2 script
- `reasoning_extraction_v1.py` - Stage 2 reasoning (CoT ile değiştirildi)

---

**Son Güncelleme:** 2025-12-11
