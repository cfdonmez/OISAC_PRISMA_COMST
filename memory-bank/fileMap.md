# 📁 File Map - Tüm Dosyaların Rehberi

**Son Güncelleme:** 2025-12-11

Bu dosya repodaki tüm önemli dosyaların ne işe yaradığını açıklar.

---

## 🏠 Root Level

| Dosya/Klasör | Amaç |
|--------------|------|
| `README.md` | Ana giriş sayfası |
| `CITATION.cff` | Atıf bilgileri |
| `LICENSE` | Lisans |

---

## 📂 Klasör Yapısı

### `analysis/` - Analiz Araçları

#### `analysis/notebooks/` - Colab Notebook'ları

| Dosya | Amaç | Durum |
|-------|------|-------|
| `CoT_Master_Pipeline.ipynb` | **ANA NOTEBOOK** - Tek notebook ile tüm pipeline | ✅ Aktif |
| `01_Data_Prep_Factory.ipynb` | Alternatif: Sadece PDF→MD dönüşümü | Yedek |
| `02_LLM_Extraction_Lab.ipynb` | Alternatif: Eski LLM extraction | Yedek |
| `PRISMA_Flowchart_Generator.ipynb` | PRISMA akış diyagramı oluştur | Özel amaç |
| `extraction_pipeline_v3.py` | **MOTOR** - Phase 1 & 2 Python kodu | ✅ Aktif |
| `generate_prisma_flowchart.py` | PRISMA diyagramı için Python | Özel amaç |
| `test_v21_single_paper.py` | Tek paper test scripti | Test |
| `archive/` | Eski/kullanılmayan dosyalar | Arşiv |

#### `analysis/cot_laboratory/` - Chain-of-Thought Sistemi

```
cot_laboratory/
├── core/
│   ├── assembler.py       # Prompt builder + LLM API caller
│   ├── batch_runner.py    # Toplu işleme fabrikası
│   └── logger.py          # Çalıştırma kaydedici
│
├── modules/
│   ├── reasoning/         # Prompt "Lego" blokları
│   │   ├── 00_role_definition.md    # "Survey Architect" rolü
│   │   ├── 01_concept_tuning.md     # ISAC mekanizma doğrulama
│   │   ├── 02_benchmark_compare.md  # Fiziksel tutarlılık
│   │   └── 03_critical_analysis.md  # Açık problemler
│   │
│   └── formatting/
│       └── schema_v2.yaml  # JSON output şeması (v2.1, 878 satır)
│
├── recipes/
│   └── experiment_v1_full_analysis.yaml  # Ana deney tarifi
│
├── logs/                  # Çalıştırma kayıtları (*_RESULT.json)
└── run_prototype.py       # Tek paper test scripti
```

---

### `data/` - Veriler

| Klasör | İçerik | Sayı |
|--------|--------|------|
| `retrieved_docs/` | Orijinal PDF'ler | 32 PDF |
| `processed_markdowns/` | PDF→Markdown dönüşümleri | 32 klasör |
| `extraction_results_v3/` | **Güncel** JSON/CSV çıktıları | Aktif |
| `extraction_results_v2/` | Eski v2 pilot sonuçları | Arşiv |
| `extraction_results/` | Eski v1 sonuçları | Arşiv |
| `figures/` | PRISMA akış diyagramı | 2 dosya |

---

### `protocol/` - PRISMA Protokolü

| Dosya | Amaç |
|-------|------|
| `prisma_protocol.md` | **ANA PROTOKOL** - Tüm kurallar (86KB) |
| `PRISMA_2020_Checklist.md` | PRISMA 2020 kontrol listesi |

---

### `docs/` - Dokümantasyon

| Dosya | Amaç |
|-------|------|
| `ROADMAP.md` | Proje yol haritası |
| `PROJECT_STATUS.md` | Detaylı durum (eski REMINDER) |
| `AI_Co_Pilot_Workflow.md` | AI ile çalışma rehberi |
| `survey_writing_guide.md` | IEEE COMST yazım rehberi |

---

### `memory-bank/` - AI Bağlam Dosyaları

| Dosya | Amaç | AI Okumalı? |
|-------|------|-------------|
| `README.md` | Klasör açıklaması | Evet |
| `activeContext.md` | **ŞU ANKİ DURUM** | ✅ İLK OKU |
| `fileMap.md` | Bu dosya | ✅ 2. OKU |
| `projectbrief.md` | Proje özeti | Evet |
| `techContext.md` | Teknik terimler | Gerekirse |
| `systemPatterns.md` | Çalışma kuralları | Gerekirse |
| `productContext.md` | Problem tanımı | Gerekirse |

---

### `screening/` - Eleme Kayıtları

| Dosya | Amaç |
|-------|------|
| `screening_log.csv` | Eleme kararları |
| `excluded_fulltext_log.csv` | Tam metin sonrası çıkarılanlar |
| `prisma_flow_counts.csv` | PRISMA sayıları |

---

### `search/` - Arama Logları

| Dosya | Amaç |
|-------|------|
| `search_strings.md` | Kullanılan arama sorguları |
| `search_log.csv` | Arama tarihleri ve sonuçları |
| `dedup_log.csv` | Duplicate temizleme kaydı |

---

### `manuscript/` - LaTeX

| Dosya | Amaç |
|-------|------|
| `comst_template.tex` | IEEE COMST şablonu |

---

## 🔑 En Önemli Dosyalar (Top 10)

1. `analysis/notebooks/CoT_Master_Pipeline.ipynb` - Ana notebook
2. `analysis/cot_laboratory/core/assembler.py` - CoT motoru
3. `analysis/cot_laboratory/modules/formatting/schema_v2.yaml` - JSON şeması
4. `analysis/notebooks/extraction_pipeline_v3.py` - Phase 1&2 motoru
5. `protocol/prisma_protocol.md` - Ana protokol
6. `memory-bank/activeContext.md` - Güncel durum
7. `data/retrieved_docs/` - PDF'ler
8. `data/processed_markdowns/` - İşlenmiş veriler
9. `analysis/cot_laboratory/logs/` - Çalıştırma kayıtları
10. `analysis/cot_laboratory/recipes/experiment_v1_full_analysis.yaml` - CoT tarifi
