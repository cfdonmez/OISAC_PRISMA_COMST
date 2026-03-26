# Section II-D Duzeltme Notu (Hakem Gozunden) — “Metric Contract” Tutarlilik ve Savunulabilirlik

Asagidaki notlar **II-D: Sensing Principles and the Metric Contract** metnini (D.1–D.4 + Lesson) bir **COMST hakemi** refleksiyle; (i) Section I’de kilitledigin metrik sozlesmesi, (ii) Section II sablon disiplinin ve (iii) “kanit/iddia ayrimi” acisindan degerlendirerek hazirlanmistir.

---

## 0) Genel durum (kisa hukum)

II-D, COMST icin beklenen “**kavramsal sozlesme**” rolunu dogru konumlandiriyor:
- **Delta r_min (rezolusyon)** / **sigma_r (dogruluk)** / **CRB (alt sinir)** / **Delta z (fiber uzaysal granulerlik)** ayrimini net kuruyor.
- “**Comparability warning**” ile yanlis metrik ikamelerini acikca yasakliyor.
- “Evidence alignment” bloklari **yalniz literatur iddiasinin oldugu yerde** kullanilmis; teorik tanimlar icin kanitsiz kalman dogru.

Bu haliyle “temel iskelet” **saglam**. Asagidaki duzeltmeler, hakem saldiri yuzeyini kucultmek icindir.

---

## 1) P0 (kritik) duzeltmeler — yapilmazsa hakem “ambiguity / overreach” der

### P0.1 — D.2 basligi “CRB/FIM” diyor ama FIM yok: ya basligi daralt ya 1 cumle FIM bagi kur
**Sorun:** D.2 basligi “CRB/FIM Bounds” iken icerik yalniz CRB uzerinden gidiyor. Hakem bunu “terminoloji tutarsizligi” olarak yakalar.

**Minimal duzeltme (tercih-1):** Basligi **CRB** ile sinirla.
- Ornek: `### D.2 Accuracy (Estimator-Dependent) and CRB Bounds`

**Minimal duzeltme (tercih-2):** Basligi koru ama **tek cumle** FIM baglantisi ekle:
- Onerilen ek cumle (CRB formulunun hemen ardindan):
  > “Equivalently, for a parameter vector, the CRB follows from the Fisher information matrix \( \mathbf{J}(\theta) \) via \( \mathrm{cov}(\hat\theta)\succeq \mathbf{J}(\theta)^{-1} \); the scalar bound above is a specialization.”

**Neden kritik?** COMST’te “sozlesme” bolumunde terminoloji *tam isabet* olmali; kucuk uyumsuzluklar guven eritir.

---

### P0.2 — D.2’deki “SNR” soyut ama “plane ambiguity” ile bagini daha acik kilitle
**Sorun:** Metin dogru bicimde “SNR is abstract unless plane explicitly defined” diyor; fakat Section I / II governance cizginin ozu su: **“SNR duzlemi belirsizse, nicel karsilastirma yapilmaz.”**
D.2’de bunu **tek cumleyle** daha sert kilitlemek hakem riskini dusurur.

**Minimal ek cumle (D.2’de ‘abstract SNR’ cumlesinin hemen ardindan):**
> “Accordingly, any numerical instantiation of this bound is treated as \(\pi(\mathrm{SNR})=\text{AMBIGUOUS}\) unless the source explicitly specifies OSNR (optical plane) or electrical SNR (post-detection plane).”

**Neden kritik?** Hakem su cumleyi arar: “plane ayrimi yalniz bir ‘not’ degil, **kullanim kuralidir**.”

---

### P0.3 — D.1’de \(B_{\text{eff}}\) ile D.2’deki \(\beta\) (RMS bandwidth) iliskisinin “esitleme yapmama” kuralini soyle
**Sorun:** D.1’de \(B_{\text{eff}}\), D.2’de \(\beta\) var. Ikisi teknik olarak iliskilidir ama ayni sey degildir; hakem “bandwidth tanimi kayiyor mu?” diye yuklenebilir.

**Minimal ek cumle (D.2’de \(\beta\) tanimina ek):**
> “We do not equate \(\beta\) with \(B_{\text{eff}}\) unless the receiver filtering/processing model is specified; \(\beta\) is an RMS-bandwidth descriptor, whereas \(B_{\text{eff}}\) is an effective usable bandwidth under the processing chain.”

**Neden kritik?** “Metric contract” bolumu; sembol kaymalarini affetmezler.

---

## 2) P1 (onemli) iyilestirmeler — savunmayi guclendirir, metni bozmaz

### P1.1 — D.3’te “spatial resolution” terimi icin fiber baglami notu
Fiber literaturunde “spatial resolution” bazen **Delta z (gauge/segment)** anlaminda kullanilir; bazen “olcum grid’i” gibi muglak gecer. D.3 bunu zaten yonlendiriyor; ama hakemin sevdigi net cumle su tiptir:

**Minimal ek cumle (D.3’te ilk paragrafin sonunda):**
> “When fiber papers use ‘spatial resolution,’ we interpret it as a \(\Delta z\)-type granularity only when it is explicitly tied to gauge/segment length.”

---

### P1.2 — D.4’te birim (bps/m) donusum notu (gelecekteki tablo/figur tutarliligi icin)
Sen CRQ_Delta birimini [bps/m] olarak dogru secmissin. Ancak ileride bazi calismalar Gbps/cm gibi verebilir. D.4’e 1 satir “normalize ediyoruz” notu eklemek, ileride Section IV–V tablolarinda surprizi onler:

**Minimal ek cumle (D.4’te CRQ_Delta tanimindan sonra):**
> “Where sources report mixed units (e.g., Gbps and cm-scale resolution), we normalize to SI (bps/m) before forming \(\mathrm{CRQ}_\Delta\).”

---

## 3) P2 (nice-to-have) — yalniz vakit varsa

### P2.1 — Lesson (D) cumlesi cok iyi; ama “governance” vurgusunu 1 kelime artir
Lesson zaten guclu. “contract” kelimesini eklemek daha ‘COMST’ kokar:

> “Without an explicit **metric contract** separating … comparability collapses.”

---

## 4) Hakem gozuyle “kirmizi bayrak” kontrol listesi (su an buyuk olcude temiz)

- **Forbidden tokens** (Delta R, sigma_R) yok: ✅
- \(\Delta r_{\min}=v/(2B_{\text{eff}})\) iki-yonlu sozlesme net: ✅
- \(\Delta z\) ile \(\Delta r_{\min}\) ikamesi acikca yasak: ✅
- CRQ_Delta yalniz \(\Delta r_{\min}\) ile tanimli: ✅
- OSNR vs electrical SNR “plane separation” bolumu D.2’ye **P0.2** eklenirse daha da “hakem-proof”: ⚠️ (kolay duzeltme)

---

## 5) Uygulanacak minimal patch set (en iyi “fayda/maliyet”)

1) **D.2 basligini duzelt** (CRB/FIM → CRB) **veya** 1 cumle FIM bagi ekle.
2) D.2’ye **\(\pi(\mathrm{SNR})\)** uzerinden “plane belirsizse sayisal instantiation yapilmaz” cumlesini ekle.
3) D.2’de \(\beta\)–\(B_{\text{eff}}\) **esitlememe** kuralini ekle.

Bunlar metni uzatmadan savunmayi ciddi guclendirir.

---
