# Golden Model: IEEE COMST Survey Yazım Modeli

> **2026-08-04 scope clarification:** this is a writing and structure reference. It does not define the current journal target, the PRISMA denominator, or the scientific evidence base. Current evidence authority: `full_corpus_206_source_of_truth_2026-08-04.md`.

**Son Güncelleme:** 2026-01-05
**Durum:** ✅ Analiz Tamamlandı — Yazım Aşamasına Hazır

---

**UYARI (2026-01-10):** Structure Analysis sonrasindaki script/regex tabanli ciktilar hatali kabul edildi. Tum cikarsimlar LLM destekli yeniden yapilacak.


## 🎯 Nedir?

**Golden Model**, 76 IEEE COMST survey makalesinin tersine mühendislik (reverse engineering) yöntemiyle analiz edilmesiyle oluşturulan bir **yazım kılavuzudur**. Bu model:

- En başarılı survey makalelerinin **yapısal şablonlarını**
- Akademik yazımda kullanılan **kalıp cümle bankasını** (Phrasebank)
- **Kelime bütçelerini** ve görsel yoğunluğu standartlarını
- **Retorik stratejileri** ("Yes, But..." argümantasyonu)

içerir ve O-ISAC survey çalışmasının IEEE COMST standartlarında yazılmasını sağlar.

---

## 📅 Tarihçe ve Oluşum Süreci

| Tarih | Aşama | Açıklama |
|-------|-------|----------|
| 2025-11 | PDF Toplama | 76 IEEE COMST makalesi (2020-2025 arası) indirildi |
| 2025-11 | Digitization | `marker-pdf` ile PDF → Markdown dönüşümü yapıldı |
| 2025-12 | Standardization | Dosyalar `COMST_001-076` formatında standartlaştırıldı |
| 2026-01 | Legacy ciktilar gozden cikarildi | Script/regex tabanli structure/phrase/rhetoric cikarsimlar hatali kabul edildi |
| 2026-01 | LLM Structure Rebuild (planli) | 76 Markdown dosyasindan LLM destekli heading/kategori/kelime butcesi cikartilacak |
| 2026-01 | LLM Phrasebank & Rhetoric (planli) | LLM ile paragraf orneklemeleri yapilip transition/caption fiilleri yeniden derlenecek |
| 2026-01 | LLM Blueprint Synthesis (planned) | New analysis/llm_synthesis_report.md and writing_recipes/COMST_master_recipe_llm.md will be synthesized; downstream artifacts updated accordingly |

---

## ? Analysis Policy (LLM Reconstruction)

- Include: Abstract through Conclusion/Challenges (main body only).
- Exclude: References, author bios/photos, acknowledgments, appendix, nomenclature.
- Rationale: non-body content inflates word budgets and distorts section ratios and correlations.

## ?? Golden Model Dosya Haritas?

### Core LLM Artifacts (Authoritative)

| File | Purpose | Priority |
|------|---------|----------|
| `analysis/llm_structure_model.json` | Section flow, frequency, objectives, word budgets | High |
| `analysis/llm_rhetoric_model.json` | Rhetorical moves, transitions, caption verbs | High |
| `analysis/llm_phrasebank.json` | LLM-extracted phrase templates by function | High |
| `analysis/llm_analysis_cards/COMST_XXX.json` | Per-paper analysis card | High |
| `analysis/llm_synthesis_report.md` | New golden blueprint narrative | High |
| `writing_recipes/COMST_master_recipe_llm.md` | Actionable writing recipe | High |

### Supporting LLM Artifacts (Optional)

| File | Purpose |
|------|---------|
| `analysis/llm_visual_table_patterns.json` | Figure/table types, placement logic, caption patterns |
| `analysis/llm_taxonomy_patterns.json` | Taxonomy axes, branch patterns, lesson rules |
| `analysis/llm_sampling_log.md` | Calibration/validation sample list and notes |
| `analysis/llm_decision_log.md` | Decisions, revisions, assumptions |

### Legacy Artifacts (Reference Only)

| File | Status |
|------|--------|
| `analysis/synth_rpt.md` | Legacy, script-derived; not authoritative |
| `analysis/pbank.json` | Legacy, script-derived; not authoritative |
| `analysis/lay_stats.json` | Legacy, script-derived; not authoritative |
| `analysis/corp_struct.json` | Legacy, script-derived; not authoritative |
| `analysis/rhet_rpt.json` | Legacy, script-derived; not authoritative |
| `analysis/stylo_rpt.json` | Legacy, script-derived; not authoritative |
| `analysis/wrt_bp_master.json` | Legacy, old pipeline output |

### Legacy Scripts (Do Not Use for New Synthesis)

> Note: script outputs are legacy and considered incorrect; keep only for reference.

| Script | Legacy role |
|--------|-------------|
| `analysis/ext_struct.py` | Legacy structure extraction |
| `analysis/ext_pbank.py` | Legacy phrasebank extraction |
| `analysis/an_lay.py` | Legacy layout and word budget stats |
| `analysis/an_sty.py` | Legacy stylometric analysis |
| `analysis/an_rhet.py` | Legacy rhetoric pattern analysis |
| `analysis/std_corp.py` | Legacy corpus standardization |

### Raw Data

| Folder | Contents | Count |
|--------|----------|-------|
| `data/cprev/` | Original COMST PDFs | 77 PDF |
| `data/proc_markdowns_comstPrev/` | Markdown conversions (long names) | 77 folders |
| `data/corp_std/` | Standardized markdown (COMST_XXX) | 76 folders |

---
## 📊 Temel Bulgular (Özet)

### Yapısal Standartlar

```
Standart COMST Survey Akışı:
1. ABSTRACT              (100% sıklık, ~250 kelime)
2. INTRODUCTION          (100% sıklık, ~4,300 kelime)
2. RELATED WORK          (85% sıklık,  ~4,400 kelime)
3. FUNDAMENTALS          (83% sıklık,  ~9,600 kelime)
4. TECHNICAL TAXONOMY    (71% sıklık,  ~7,200 kelime)
5. CHALLENGES & FUTURE   (93% sıklık,  ~4,600 kelime)
6. CONCLUSION            (100% sıklık, ~500 kelime)
```

### Sayısal Standartlar

| Metrik | Ortalama | Hedef |
|--------|----------|-------|
| Toplam kelime | ~36,000 | 35,000-40,000 |
| Figür sayısı | 19 | 18-22 |
| Tablo sayısı | 12 | 10-15 |
| Referans tazeliği | %61 son 5 yıl | ≥%60 |

### Phrasebank Kategorileri

| Kategori | Örnek Sayısı | Kullanım Yeri |
|----------|--------------|---------------|
| `timeline_trends` | 100+ | Introduction paragraf 1 |
| `problem_statement` | 50+ | Introduction paragraf 2-3 |
| `gap_identification` | 80+ | Related Work |
| `contribution` | 60+ | Introduction sonu |
| `paper_organization` | 40+ | Introduction son paragraf |

---

## 🔑 Yazım Sırasında Kritik Kurallar

### 1. "Gap Selling" Stratejisi
Her COMST survey'ı "Neden başka bir survey?" sorusuna cevap vermeli.

**Zorunlu:** Mevcut survey'lerle karşılaştırma tablosu (Table I veya II)

```markdown
| Ref. | Year | Scope | Contributions | Limitations |
|------|------|-------|---------------|-------------|
| [1]  | 2023 | RF ISAC | ... | No optical discussion |
| [2]  | 2024 | VLC only | ... | Ignores fiber sensing |
| **Ours** | **2026** | **Unified O-ISAC** | **First optical survey** | N/A |
```

### 2. "Yes, But..." Retoriği
Önceki çalışmaları övüp sonra sınırlandır:
> "While [Ref] provides an excellent overview of [X], it primarily focuses on [Old Standard] and neglects [New Trend]."

### 3. "However" Kullanımı
- COMST makalelerinde ortalama **7 kez "However"** kullanılıyor
- Mevcut durumdan eksikliğe geçişte kullan
- Paragraf sonlarında "Therefore" veya "Consequently" ile bağla

### 4. Görsel Dağılımı
- **System Model/Scenario:** %20 (Zorunlu, erken bölümlerde)
- **Performance Graphs:** %13 (Sadece simülasyon varsa)
- **Taxonomy Diagram:** %4 (Contribution bölümünde kritik)

---

## 🚀 Survey Yazım Aşamasında Kullanım

### Başlangıçta
1. `synthesis_report.md` oku — Genel strateji
2. `layout_stats.json` kontrol et — Kelime bütçeleri

### Yazım Sırasında
1. Her section için `phrasebank.json` dan template al
2. `corpus_structure.json` dan örnek yapıları incele

### Bitimde
1. Kelime sayılarını `layout_stats.json` ile karşılaştır
2. Figür/tablo sayılarını kontrol et
3. Referans tazeliğini doğrula (%61 son 5 yıl)

---

## ⚠️ Hatırlatmalar

- **Bu model sadece rehberdir** — Birebir kopyalama yapılmamalı
- **O-ISAC'a özgü uyarlamalar gerekebilir** — Optical domain terminolojisi
- **Phrasebank'taki cümleler şablon olarak kullanılmalı** — İçerik değiştirilmeli
- **COMST editörleri yapısal uyumu kontrol eder** — Bu modele uyum kritik

---

## 🔗 İlgili Dosyalar

- `memory-bank/activeContext.md` — Güncel proje durumu
- `memory-bank/productContext.md` — Problem tanımı ve hedef
- `docs/surv_write_guide.md` — PRISMA + COMST entegrasyon rehberi
- `protocol/prisma_proto.md` — Metodoloji kuralları
