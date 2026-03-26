# COMST-Hakem Notlari (Hatirlatici) — O-ISAC Survey (Section I–II Durum)

> Amac: Taslak yazimi devam ederken “hakemin takilacagi” yerleri unutmamak ve final revizyonda sistematik duzeltmek.

---

## 0) Kisa Hakem Karari (Simdilik)
- Genel izlenim: **Dogru yolda, denetlenebilir (audit edilebilir) bir survey insa ediliyor.**
- Egitim: **Major Revision** (icerikten cok *iddia–kanit–notasyon–metric governance* tutarliligi kaynakli).
- En buyuk arti: “Metric governance + evidence anchors + context verification” mimarisi.

---

## 1) En Guclu Yonler (Korunacak / Bozulmayacak)
### 1.1 Metric Governance yaklasimi (cok guclu)
- **OSNR (optical-plane) vs electrical SNR/ESNR (electrical-plane)** ayrimi net ve hakem acisindan degerli.
- **OSNR→SNR donusumu yasak** kurali, literaturdeki terminoloji kirliligine karsi dogru bir “sozlesme” yaklasimi.
- Bu, survey’i “anlatan” degil “norm koyan” duzeye yaklastiriyor.

### 1.2 Evidence anchoring + context window verification (cok guclu)
- “Kanit satiri + heading_path + Lx–Ly + context-verified” mekanizmasi, hakem tartismalarinda
  “Bu cumleyi nereden cikardin?” sorusunu dogrudan kapatir.
- Bu disiplin **Section II** icin ozellikle dogru bir tercih.

### 1.3 Section I omurgasi iyi
- Katkilar acik ve organizasyon mantikli (taxonomy + trade-offs vaatleri dogru sirada).
- Hakemin aradigi “survey route-map” hissi var.

---

## 2) Major Riskler (Hakemin buyuk olasilikla isaretleyecegi)
### 2.1 Notasyon / metrik sozlesmesi tutarliligi (Δd/σ_d ↔ Δr_min/σ_r ↔ Δz)
- Section I’de notasyon tablosu **d, Δd, σ_d** uzerinden gidiyor.
- Section II governance ise **Δr_min** (ranging) ve **Δz** (fiber spatial granularity/gauge length) ayrimini “binding” yapiyor.
- Hakem riski: Okur “d mi r mi? Δd mi Δr_min mi?” diye takilirsa Section II’nin norm koyma iddiasi zayiflar.

**Onerilen duzeltme (yuksek getiri, dusuk maliyet):**
- “Notation reconciliation” icin:
  - ya Section II basinda 2–3 cumlelik bir **esleme paragrafi**,
  - ya da Table/Notation kismina tek satirlik bir **esdegerlik notu**:
    - “Bu survey’de range icin r kullanilir; Section I’deki d ile esdegerdir; ranging cozunurlugu governance geregi Δr_min ile raporlanir; fiber icin Δz kullanilir.”

### 2.2 ESNR anchor zayifligi (plane-separation kirilganligi)
- Evidence coverage raporuna gore **ESNR icin anchor sayisi dusuk** olabilir; bu durum plane-separation iddiasini “kil payi” gecer hale getirir.
- Hakem riski: “Bu ayrimin literatur temsiliyeti zayif” elestirisi.

**Onerilen duzeltme:**
- ESNR/electrical-plane ankora **hedef artirimi** (orn. 2 → 4–6 arasi).
- Varsa candidate listeleri uzerinde pattern genisletme + manuel dogrulama ile anchor sayisini guclendirme.

### 2.3 Mutlak / superlatif dil (“highest-performing”, “unattainable”, vb.)
- Section I’de bazi mutlak ifadeler hakemi “selection bias” itirazina goturebilir.
- Hakem riski: “Bu iddia hangi secim kuralina gore? Literatur geneli mi, secilmis ornekler mi?”

**Onerilen duzeltme:**
- “the literature” yerine:
  - “representative works”, “selected demonstrations”, “reported exemplars” gibi daraltilmis dil.
- Alternatif: Metodolojiye mini bir “selection rule” paragrafi:
  - orn. “peak data rate reported”, “reported range resolution”, “demonstration constraints” gibi.

---

## 3) Minor ama Can Sikici Tutarsizliklar
### 3.1 “Generic SNR” sembolu ve plane-ambiguity
- Section I/II arasinda “SNR” sembolunun duzlem belirsizligi konusunda kucuk bir not yararli olabilir:
  - “Generic ‘SNR’ ifadesi, optical/electrical duzlem belirtilmediginde AMBIGUOUS kabul edilir.”

### 3.2 Template kaynagi tekillestirme
- “Authoritative template path” karisikligi ileride agent ciktilarinin sapmasina yol acabilir.
- Audit’te “resolved path” raporlanmasi iyi; fakat repo icinde tek bir canonical path’i sabitlemek uzun vadede daha guvenli.

---

## 4) Su an COMST standardina yakinlik (ozet)
- **Section I:** guclu; fakat mutlak dil secilim kuraliyla emniyete alinmali / yumusatilmali.
- **Section II-A/B/C:** audit mantigi dogru; plane-separation ve notasyon koprusu daha da guclendirilirse hakem dayanimliligi artar.

---

## 5) En Yuksek Getirili “Bir Sonraki Hamle” (Final revizyona saklanabilir)
1) **Notation reconciliation** (Δd/σ_d ↔ Δr_min/σ_r ↔ Δz) → kucuk edit, buyuk etki.
2) **ESNR anchor artirimi** → plane-separation iddiasini “fragile” olmaktan cikarir.
3) **Mutlak dilin guvenceye alinmasi** (secim kriteri veya dil yumusatma).

---

## 6) Revizyon Stratejisi (Kendime not)
- Simdilik draft uretimi devam.
- Tum survey tamamlandiginda:
  - once “governance + notation consistency pass”
  - sonra “anchor coverage + prevalence language pass”
  - en son “COMST tone + redundancy + flow” pass.

---
