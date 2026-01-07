# Golden Model: IEEE COMST Survey Yazım Modeli

**Son Güncelleme:** 2026-01-05
**Durum:** ✅ Analiz Tamamlandı — Yazım Aşamasına Hazır

---

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
| 2025-12 | Structure Analysis | `extract_structure.py` ile bölüm yapıları çıkarıldı |
| 2025-12 | Phrasebank Mining | `extract_phrasebank.py` ile 1700+ kalıp cümle çıkarıldı |
| 2025-12 | Style Analysis | Paragraf istatistikleri, atıf tazeliği analiz edildi |
| 2025-12 | Rhetoric Analysis | Transition kelimeleri ve tablo referans dili belirlendi |
| 2025-12 | Synthesis | `synthesis_report.md` ana blueprint olarak oluşturuldu |
| 2026-01-05 | Memory-Bank Entegrasyonu | Bu dosya oluşturuldu |

---

## 📁 Golden Model Dosya Haritası

### Ana Çıktılar (Yazım Sırasında Kullan)

| Dosya | Amaç | Öncelik |
|-------|------|---------|
| `analysis/synthesis_report.md` | **ANA BLUEPRINT** — 7 bölümlü kapsamlı yazım rehberi | ⭐⭐⭐ |
| `analysis/phrasebank.json` | 1700+ akademik kalıp cümle (5 kategori) | ⭐⭐⭐ |
| `analysis/layout_stats.json` | Section bazlı kelime bütçeleri | ⭐⭐ |

### Destekleyici Analizler

| Dosya | İçerik |
|-------|--------|
| `analysis/corpus_structure.json` | 76 makalenin detaylı bölüm yapısı |
| `analysis/rhetoric_report.json` | Transition kelimeleri ve fiil kullanımı |
| `analysis/stylometric_report.json` | Atıf tazeliği, paragraf dinamikleri |

### Analiz Scriptleri

| Script | İşlev |
|--------|-------|
| `analysis/extract_structure.py` | Bölüm yapısı çıkarma |
| `analysis/extract_phrasebank.py` | Kalıp cümle çıkarma |
| `analysis/analyze_layout.py` | Görsel yoğunluğu ve kelime sayısı |
| `analysis/analyze_style.py` | Stilometrik analiz |
| `analysis/analyze_rhetoric.py` | Retorik pattern analizi |
| `analysis/standardize_corpus.py` | COMST dosyalarını standartlaştırma |

### Ham Veri

| Klasör | İçerik | Sayı |
|--------|--------|------|
| `data/comstPrev/` | Orijinal COMST PDF dosyaları | 77 PDF |
| `data/processed_markdowns_comstPrev/` | Markdown dönüşümleri (uzun isimli) | 77 klasör |
| `data/corpus_standardized/` | Standartlaştırılmış Markdown (COMST_XXX) | 76 klasör |

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
- `docs/survey_writing_guide.md` — PRISMA + COMST entegrasyon rehberi
- `protocol/prisma_protocol.md` — Metodoloji kuralları
