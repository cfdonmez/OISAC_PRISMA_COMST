# Project Brief: O-ISAC Systematic Review

## 2026-08-04 current brief

The project now uses a locked PRISMA denominator of **227 included reports / 206 included studies** and a claim-governed full-corpus extraction of **8,306 claims**. Phase E TQAF and Phase F S1–S7 synthesis are complete; primary synthesis uses **8,203 claims**. The old 221-study status table below is historical. Current scope, counts, provenance limits and manuscript migration rules are authoritative in `full_corpus_206_source_of_truth_2026-08-04.md`.

The survey's core purpose remains a unified cross-modality O-ISAC account spanning fiber, FSO, VLC/LiFi, photonic-THz and hybrid systems, with explicit governance of metric comparability, trade-offs, validation maturity and benchmark readiness. The repository's current journal target is IEEE Photonics Journal; COMST remains a survey-writing reference.

---

**Son Güncelleme:** 2025-12-11

---

## 🎯 Core Objective

**PRISMA 2020** standartlarına uygun bir **Sistematik Derleme** hazırlamak.

**Konu:** Optical Integrated Sensing and Communication (O-ISAC)

**Hedef Dergi:** IEEE Communications Surveys & Tutorials (COMST)

---

## 📊 Scope (Kapsam)

İki ana domain:

### 1. Cabled O-ISAC (Fiber-based)
- Fiber üzerinde joint sensing + haberleşme
- DAS (Distributed Acoustic Sensing)
- Vibration, temperature sensing
- φ-OTDR, BOTDA, BOTDR

### 2. Wireless O-ISAC
- Free-Space Optical (FSO)
- Visible Light Communication (VLC)
- LiDAR-based ISAC
- THz photonic systems

---

## 📋 Critical Constraints

1. **Protocol Adherence** - Tüm kararlar `protocol/prisma_proto.md`'ye uygun
2. **Data Integrity** - Orijinal veriler korunmalı
3. **Reproducibility** - Tüm metodoloji version-controlled
4. **PRISMA Compliance** - 27 maddelik checklist

---

| Çıktı | Durum |
|-------|-------|
| PRISMA Protokolü | ✅ Tamamlandı |
| Tarama (Screening) | ✅ 221 çalışma dahil |
| Extraction Schema | ✅ v2.1 (Chain-of-Thought) |
| COMST Analizi (76 Paper) | ✅ Golden Model Hazır |
| Veri Çıkarma | ✅ Phase 2 Tamam (221 PDF) |
| CoT Extraction | 🟡 Phase 3 Başlıyor |
| Taxonomy | 🔴 Beklemede |
| Manuscript | 🔴 Beklemede |

---

## 📈 Current Numbers

| Metrik | Değer |
|--------|-------|
| Belirlenen kayıt | 1500+ |
| Dahil edilen (Included) | 221 |
| PDF toplanan | 221 |
| Visual Analysis tamamlanan | 221 |
| COMST Corpus analizi | 76 paper |

---

## 🔗 Ana Referanslar

- **PRISMA 2020:** [prisma-statement.org](http://www.prisma-statement.org/)
- **Protokol:** `protocol/prisma_proto.md`
- **Extraction Schema:** `analysis/cot_lab/modules/formatting/schema_v2.yaml`
