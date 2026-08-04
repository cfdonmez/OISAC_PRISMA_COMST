# Section 8 Master Reminder (Execution + Closure Plan)

> 2026-08-04 supersession note: regenerate Section VIII evidence anchors from the governed 206-study corpus. Do not reuse the old `n_total_papers=221` package or mechanically edit its denominator.

Date: 2026-02-10
Owner: AI + User
Purpose: Section 8 tamamlanirken tum section evidence baglarini kontrol etmek, sonra draft + figure/table + final COMST/PRISMA kapanisini risksiz tamamlamak.

---

## 1) Final Hedef (Definition of Done)

Makale su kosullar saglandiginda "finale hazir" kabul edilecek:
- Section 2, 4, 5, 6, 7, 8 evidence paketleri tamam ve birbirine tutarli.
- Cross-section consistency audit tamam (metric plane, metric alias, label normalization, scope).
- Draft metinler evidence-anchored ve claim bazinda izlenebilir.
- Grafik ve tablolar tekil kaynak dosyaya (csv/json/md) geri izlenebilir.
- COMST kalite kapisi ve PRISMA 2020 kapisi gecilmis.

---

## 2) Guncel Durum (Snapshot)

Tamamlanan evidence paketleri:
- `analysis/IV_ev_v2/`
- `analysis/V_ev_v2/`
- `analysis/VI_ev_v2/`
- `analysis/VII_ev_v2/`
- `analysis/VIII_ev_v1/`

Section 8 mevcut kritik sayilar:
- `n_total_papers=221`
- `n_standardization_interoperability_papers=55`
- `n_hardware_scalability_efficiency_papers=25`
- `n_channel_modeling_evaluation_papers=54`
- `n_security_privacy_reliability_papers=18`
- `n_deployment_convergence_roadmap_papers=0`
- `contract_violations_rows=242`
- Kaynak: `analysis/VIII_ev_v1/readiness_report.md`

Mevcut iyilestirme notlari:
- `.agent/workflows/section_02_improvement_notes.md`
- `.agent/workflows/section_03_improvement_notes.md`
- `.agent/workflows/section_04_improvement_notes.md`
- `.agent/workflows/section_06_improvement_notes.md`
- `.agent/workflows/section_07_improvement_notes.md`
- `.agent/workflows/section_08_improvement_notes.md`

---

## 3) Section 8 Icin Net Yol (Open Challenges + Research Roadmap + Alignment Audit)

Asama S8-1: Evidence hardening
- Deployment roadmap alaninda DIRECT anchor acigini kapat (simdilik 0 destekli paper).
- Upstream bridge bagimliligini ayir: strict_text_only ve strict_with_upstream birlikte raporla.
- `EVIDENCE_WEAK` yukunu drafting gate ile izole et.

Asama S8-2: Cross-section bag denetimi
- Section 8 challenge siniflari, Section 5 tradeoff, Section 6 enabler, Section 7 application ile birebir kontrol edilecek.
- "Section 8 sadece tekrar ediyor" riskine karsi, her challenge icin section-specific kanit zorunlu olacak.

Asama S8-3: Draft-ready output for A-E challenge domains
- Challenge bazli: observed gap -> technical cause -> measurable impact -> research direction zinciri yazima hazir olacak.
- Her challenge icin en az bir "what to measure next" metric notu uretilecek.

Asama S8-4: Capstone closure for VIII-F / VIII-G
- VIII-F yeni challenge domain olmayacak; dependency-aware capstone synthesis ve prioritized agenda olarak kalacak.
- VIII-G yeni challenge domain olmayacak; Sections V-VII ile continuity/control icin aggregate alignment audit olarak kalacak.

---

## 4) Tum Sectionlar Arasi Tutarlilik Denetimi (2-4-5-6-7-8)

Kontrol C1: Metric governance (Section II)
- OSNR optical-plane; SNR/ESNR electrical-plane.
- Model olmadan OSNR->SNR donusumu yazilmayacak.
- Resolution/accuracy alias hatasi olmayacak (`delta_r_min` vs `sigma_r`).

Kontrol C2: Taxonomy and labels (Section IV)
- Medium etiketleri tek normalize listeye sabitlenecek.
- Section 6 enabler ve Section 7 domain etiketleri taxonomy ile uyumlu olacak.

Kontrol C3: Tradeoff and enabler/application bridge (Section V/VI/VII)
- Tradeoff verisi Section 8 onceliklendirme skorlarini aciklayacak.
- Enabler kisitlari Section 8 hardware/deployment challenge metnine baglanacak.
- Application bosluklari Section 8 roadmap risklerini besleyecek.

Kontrol C4: PRISMA scope lock
- Section bazli tum sayilar dahil edilen corpus ile sinirli kalacak.
- Manuscript sayilari tek kaynaktan beslenecek (`screening/prisma_flow_counts.csv` ve ilgili readiness dosyalari).

---

## 5) Draft, Grafik, Tablo, Metrik Uretim Sirasi

Faz D1: Draft olusturma
1. Section 8
2. Section 7
3. Section 6
4. Section 5
5. Section 4
6. Section 1-2 bag revizyonu
7. Section 3 PRISMA wording freeze

Faz D2: Grafik ve tablo paketi
- Section 4: taxonomy figures + classification tables
- Section 5: tradeoff tables + pareto/trend visuals
- Section 6: enabler capability tables + constraint visuals
- Section 7: application coverage tables + domain comparison
- Section 8: A-E challenge summary + VIII-F capstone agenda tables + VIII-G alignment/audit summary

Faz D3: Metrik butunlestirme
- Tum sectionlarda ayni metrik isimlendirmesi kullanilacak.
- Tablo captionlarinda metrik tanimi ve kaynak kolonlari zorunlu olacak.
- "strict view" ve "supporting/raw view" acikca ayrilacak.

---

## 6) COMST Final Gate (Zorunlu Kontrol Listesi)

- Problem framing gap-driven ve net mi?
- Katki maddeleri kanitla savunuluyor mu?
- Metin listeleme degil sentez odakli mi?
- Tablolar/sekiller metin akisini destekliyor mu?
- Overclaim var mi ("first/comprehensive" ifadesi kanitli mi)?
- Limitation ve threat-to-validity paragraflari acik mi?

---

## 7) PRISMA Final Gate (Zorunlu Kontrol Listesi)

- Databases, search strings, last search date acik mi?
- Dedup, screening, eligibility adimlari tutarli mi?
- Flow sayilari manuscriptte birebir mi?
- Protocol/registration durumu net mi?
- Included corpus sayilari tum sectionlarda tutarli mi?
- Exclusion reasons and logs referanslanmis mi?

---

## 8) Dikkatten Kacabilecek Kritik Noktalar (Ek Hatirlatma)

1. Section 8 deployment roadmap alaninda support=0 iken kesin iddia yazmak.
2. Cross-section linked count ile strict evidence count birebir ciktiginda bunu aciklamadan kullanmak.
3. Section 6/7 dual-view farklarini metinde belirtmeden tek sayi vermek.
4. Section 1 contribution maddelerini son evidence dagilimina gore guncellememek.
5. VIII-F veya VIII-G'yi yeni challenge domain gibi yazmak.
6. Section 2 metric governance dilini Section 5-8 metnine tasimayi unutmak.
7. Figure/table kaynak dosya izini (path + output id) kaydetmemek.
7. PRISMA sayilarini readiness ve screening dosyalari arasinda capraz kontrol etmemek.
8. Weak-evidence satirlarini ana bulgu gibi yazmak.
9. "Temsili" ve "kapsamli" ifadelerini ayni paragrafta celiskili kullanmak.
10. Final proofreading oncesi line-level claim->anchor kontrolunu atlamak.

---

## 9) Kisa Operasyon Rutini (Gunluk)

Her calisma gunu:
1. `memory-bank/activeContext.md` oku.
2. Bu dosyadan en yuksek etkili 1-2 gorevi sec.
3. Cikti olusturunca ilgili workflow notunu guncelle.
4. Gun sonunda `memory-bank/UPDATE_SUMMARY.md` ve `memory-bank/activeContext.md` senkronize et.

