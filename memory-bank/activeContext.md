# Active Context

**Son Güncelleme:** 2026-01-04

**Güncelleyen:** AI + Kullanıcı

---

## 🎯 Şu Anki Faz: Phase 2 & Git Sync Complete → Phase 3 Ready

**Git Senkronizasyonu ve Derin Temizlik** tamamlandı. Tüm kod ve analiz sonuçları GitHub'a aktarıldı. 76 IEEE COMST makalesinin analiziyle **"Golden Model"** (Yazım Kılavuzu) oluşturuldu. Sistem artık toplu CoT Extraction (Phase 3) ve makale yazımı için hazır.

---

## 📊 Güncel Sayılar

| Metrik | Değer |
|--------|-------|
| Dahil edilen çalışma | 221 |
| PDF toplanan | 221 |
| Markdown dönüştürülen | 221 |
| **Visual Analysis tamamlanan** | **221 klasör** ✅ |
| CoT extraction test edilen | 1 (O_ISAC_029) |
| Batch extraction tamamlanan | Hazırlanıyor |


---

## ✅ Bu Session'da Yapılanlar (2026-01-03)


### 1. PhD-Level Görsel Analiz (O_ISAC_350-388) Tamamlandı 👁️✨
Aşağıdaki klasörler için granüler veri çıkarımı **tamamlandı**:

| Klasör | Görüntü Sayısı | Anahtar Bulgular |
|--------|----------------|------------------|
| O_ISAC_350 | - | GaN Monolithic ISAC |
| O_ISAC_351 | - | Hamiltonian Coding |
| O_ISAC_354 | - | Green GaN ISAC |
| O_ISAC_356 | - | 120 Gbps THz ISAC |
| O_ISAC_368 | - | Review of Optical ISAC |
| O_ISAC_371 | - | VLC-OCC-CDMA Rake |
| O_ISAC_377 | - | DC-Offset QPSK-LFMCW |
| O_ISAC_379 | - | Adaptive Flexible ISAC |
| O_ISAC_381 | 12 | LED Display-Camera ISAC |
| O_ISAC_386 | 6 | Android Flashlight/Camera VLC |
| O_ISAC_388 | 6 | OCC-CDMA VLC |
| O_ISAC_159 | 17 | (Catch-up) D-band SCIE 88Gbps |


### 2. Çıkarım Formatı

Her `visual_analysis.txt` dosyası şu formatı izler:
- **Chart/Graph:** Eksen aralıkları, veri noktaları, trendler
- **System Diagram:** Bileşenler, sinyal akışı
- **Constellation:** Modülasyon formatı, EVM kalitesi

---

## 🔧 Aktif Pipeline

```
📓 CoT_Master_Pipeline.ipynb (Tek notebook ile tüm işlemler)
├── Section 1: Setup & Mount
├── Section 2: Phase 1 - PDF → Markdown (GPU) ✅
├── Section 3: Phase 2 - Visual Analysis (GPU) ✅ COMPLETED
├── Section 4: Phase 3 - CoT Extraction (Groq API) ⏳ READY
└── Section 5: Results & Export
```

**Motor Dosyaları:**
- `extraction_pipeline_v3.py` → Phase 1 & 2
- `cot_laboratory/` → Phase 3 (Chain-of-Thought)

---

## 🚀 Sonraki Adımlar

1. [x] ~~Phase 2 Visual Analysis~~ ✅ TAMAMLANDI
2. [ ] **Living Search:** Yeni araştırma ekleme (günlük rutin)
3. [ ] **Phase 3:** CoT Extraction çalıştır
4. [ ] **Batch Extraction:** 32+ paper
5. [ ] **Robustness:** Gemini kotası dolarsa fallback

---

## 🔄 Günlük Rutin (DAILY_WORKFLOW)

| Saat | Görev | Açıklama |
|------|-------|----------|
| Sabah | Living Search | Arama alarmlarını kontrol et (Scholar/IEEE) |
| Sabah | Living Screening | Yeni yayınları `search_log` ve `screening_log`a işle |
| Öğlen | PDF Collection | Dahil edilenlerin PDF'ini `retrieved_docs`a indir |
| Akşam | Batch Extraction | `CoT_Master_Pipeline.ipynb` notebookunu çalıştır |
| Gece | Analysis & QC | `logs/` altındaki sonuçları kontrol et |

---

## ⚠️ Dikkat Edilecekler

- **Unified Daily Workflow defined**: Consolidated protocols into `docs/DAILY_WORKFLOW.md` (Turkish).
- **Collaborative Screening Executed**: Processed user-provided IEEE CSV (29 items), removed 6 duplicates, and added 5 new studies (`O_ISAC_159-163`) to the inclusion list and extraction dataset.
- **BibTeX Entries Added**: Manually added `O_ISAC_001` to `O_ISAC_010` in `references.bib`.
- **API Key:** Colab Secrets'da `GROQ_API_KEY` olmalı
- **GPU:** Phase 1 & 2 için T4 veya A100 gerekli
- **Schema:** `cot_laboratory/modules/formatting/schema_v2.yaml` (v2.1) kullanılıyor
- **Dil:** İletişim **Türkçe**, Proje/Araştırma **İngilizce**

---

## 📁 Son Değişen Dosyalar

```
✏️ data/processed_markdowns/O_ISAC_*/visual_analysis.txt (20+ dosya)
✏️ memory-bank/activeContext.md (bu dosya)
✏️ docs/PROJECT_STATUS.md (güncellendi)
```
