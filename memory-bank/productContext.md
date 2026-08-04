# Product Context

> **2026-08-04 target clarification:** IEEE Photonics Journal is the current submission target in this repository. The COMST corpus and Golden Model remain a survey-structure and writing-quality reference; they are not evidence that COMST is the active target. Scientific claims and counts come from the governed 206-study PRISMA corpus, not from the writing-model corpus.

## The Problem
The literature on Optical Integrated Sensing and Communication (O-ISAC) is **fragmented**.
*   **Fiber Sensing** communities (e.g., DAS, φ-OTDR) rarely cross-pollinate with **FSO/VLC** (Wireless) communities.
*   Terminology is inconsistent (e.g., "fiber sensing with comms" vs "ISAC").
*   No unified physical-layer taxonomy exists to describe the "trade-offs" between sensing and communication across these different media.

## The Goal
To create a **Unified Physical-Layer Framework** that:
1.  Classifies O-ISAC systems by **Medium** (Fiber vs Wireless).
2.  Identifies common **Waveform families** (e.g., OFDM, Chirp) used in both domains.
3.  Quantifies the **Sensing-Communication Trade-off** (e.g., Rate vs Resolution).

## The Golden Model (IEEE COMST Blueprint)
En son PRISMA standartlarını IEEE COMST'un yüksek yazım kalitesiyle birleştiriyoruz.
*   **76 IEEE COMST Paper Analizi:** En başarılı 76 survey kağıdı tersine mühendislik (reverse engineering) yöntemiyle analiz edildi.
*   **Analiz Kapsamı:** Bölüm yapıları, görsel yoğunluğu (ortalama 18 figür/5 tablo), kelime bütçeleri (~36k kelime) ve retorik stratejiler ("Yes, But..." yöntemi).
*   **Phrasebank:** Akademik yazımı otomatize etmek ve standartlaştırmak için corpus'tan 100+ kalıp cümle yapısı çıkarıldı.
*   **Amaç:** O-ISAC survey çalışmasını sadece bir veri listesi değil, COMST standartlarında "Blueprint" niteliğinde bir başyapıt haline getirmek.

## Success Criteria
*   Selection of high-quality, peer-reviewed studies (Journal/Conference).
*   Rigorous exclusion of non-optical (RF-only) or pure-sensing/pure-comms papers.
*   A data extraction dataset (CSV/JSON) that allows for quantitative descriptive analysis.
