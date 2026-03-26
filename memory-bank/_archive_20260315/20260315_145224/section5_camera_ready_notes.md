# Section V Camera-Ready Notes

Son Guncelleme: 2026-03-15
Kapsam:
- `drafts/section_05_template.md` (Section V-A..E)
- `analysis/V_ev_v2/*`
- `drafts/section_05_correction_notes.md`
- `.agent/workflows/section_05_draft_playbook.md`

---

## Amac

Section V icin icerik tamamlama ile camera-ready entegrasyon islerini birbirinden ayirmak ve survey mimarisi icindeki gercek aciklari kalici olarak kaydetmek.

Bu dosya, Section V'in yalnizca bir metric ozeti degil, ayni zamanda Section I'de vaat edilen reporting contract + trade-off synthesis teslim noktasi oldugunu takip eder.

---

## Mevcut Durum (Section V)

- `analysis/V_ev_v2/` readiness pack'i mevcut ve gerekli dosyalar hazir.
- `drafts/section_05_template.md` 2026-03-12 production re-entry pass'i ile yeniden okundu.
- Core anlatimda playbook tonu azaltildi; publication prose'a gecis baslatildi.
- Section-level scope notu acik:
  - Section V varsayilan olarak corpus-level study counts degil, scenario-level governed records uzerinden raporlaniyor.
- Table omurgasi canonical taslakta doldurulmus durumda:
  - `Table V`
  - `Table VI`
  - `Table VII`
- Governance cizgisi korunuyor:
  - no implicit OSNR-to-SNR pooling
  - no `dz`-to-`drmin` substitution
  - no `drmin`/`sigma_r` aliasing
  - CRQ yalnizca eligible records uzerinden yorumlanacak

---

## Survey Mimarisi Acisindan Section V'in Rolü

Section V yalnizca performans rakamlarini listeleyen bir bolum degildir. Survey mimarisinde dort islev gorur:

1. Section I'deki Gap 3 vaadini teslim eder
- standardized reporting contract
- trade-off synthesis
- `drmin`, `sigma_r`, `CRQ` tabanli nicel sentez

2. Section IV taxonomy'den Section VI-VIII'e gecis koprusudur
- medium labels
- coupling dili
- metric-governance kisitlari

3. Raw prevalence ile governed evidence arasindaki farki kalici olarak sabitler
- study-level corpus coverage ile scenario-level usable subset karistirilmayacak

4. Section VIII cross-section alignment audit'i icin sabit output uretir
- sparse frontier evidence'in fazla yorumlanmasi burada engellenmeli

---

## Kalan Camera-Ready / Architecture Gozlemleri

1) Figure asset production pending
- `Fig. V-1` icin governed operating-cloud / trade-off gorseli henuz uretilmis degil.
- `Fig. V-2` icin Pareto/frontier gorseli henuz uretilmis degil.
- Etki: metin gorsellere referans veriyor, ancak final manuskriptte gercek figure asset katmani eksik.

2) Global numbering and cross-reference freeze resolved (2026-03-15)
- whole-manuscript numbering policy freeze edildi.
- Section I `Fig. 1-3` korunuyor.
- Section II ve sonrasi section-prefixed numbering kullaniyor.
- Section V artik:
  - `Fig. V-1`
  - `Fig. V-2`
- Etki: onceki Section III / Section V figure collision kapandi.

3) Section structure freeze resolved (2026-03-12)
- Official outline Section V'i `V-A..V-D` olarak ciziyor.
- `V-E` bagimsiz alt-bolum olarak tutulmadi.
- Pareto/design-implication katmani Section V sonunda kisa ve bounded bir closeout synthesis olarak korundu.
- Etki: Section V quantitative-descriptive synthesis rolunu korurken, Section VIII'in challenge/agenda alanina tasma riski azaltildi.

4) Table VII scope freeze resolved (2026-03-12)
- Section outline'ta `Table VII` head-to-head comparative table olarak konumlaniyor ve bu rol korundu.
- `Table VII` primary comparative artifact olarak freeze edildi:
  - fiber
  - wireless
  - hybrid bridge
- Tabloda su alanlar tutulacak:
  - governed points / papers
  - median rate
  - median `drmin`
  - median `sigma_r`
  - median CRQ (yalnizca contextual field)
  - coupling composition
- Frontier/eligibility compression mantigi tabloya yuklenmeyecek; bu yuk `V-C` trade-off metni, Section V closeout synthesis, ve `Fig. V-2` caption/text katmaninda kalacak.
- Etki: Table VII COMST-style comparative table rolunu korurken, summary-dump'a donusme riski azaltilmis oldu.

5) Contribution-level consistency pass pending
- Section I, Section V icin standardized reporting contract + trade-off synthesis vaadinde bulunuyor.
- Bu vaat study-level coverage diliyle kurulmus durumda.
- Section V ise governed scenario-level subset dili kullaniyor.
- Etki: final metinde acik scope bridge cümlesi korunmazsa katkilar birbiriyle celisiyor gibi gorunebilir.

6) Cross-manuscript consistency pending
- Section IV taxonomy labels birebir korunmali.
- Section VI ve Section VIII, Section V ciktilarini kullanirken sparse Pareto / low-support medium slices'i fazla yorumlamamali.
- Etki: V'teki ihtiyatli metric-politika dili sonraki sectionlarda zayiflayabilir.

7) Final caption and note policy pending
- `Table V`, `Table VI`, `Table VII` caption'lari aktif fiille baslamali.
- `Fig. V-1` ve `Fig. V-2` caption'lari raw cloud / governed cloud / CRQ-valid / Pareto ayrimini acikca belirtmeli.
- Etki: aksi durumda figure/table seti survey mimarisindeki governance mesaji zayiflatir.

---

## Halihazirda Kayda Gecmis Notlar

- `drafts/section_05_correction_notes.md`
  - figure-index conflict notu
  - scenario-level scope note ihtiyaci
  - table/figure deliverables checklist
- `.agent/workflows/section_05_draft_playbook.md`
  - canonical source map
  - figure/table plan
  - governance guardrails
  - final QA checklist

Sonuc:
- Section V icin notlar mevcut, ancak bu dosya memory-bank seviyesinde ilk kalici architecture/camera-ready kaydidir.

---

## Aksiyon Plani (Section V Ozel)

1. `Fig. V-1` ve `Fig. V-2` asset'lerini canonical `analysis/V_ev_v2/*.csv` kaynaklarindan uret.
2. Section I contribution language ile Section V governed-count language arasina acik scope bridge koy.
3. Section IV / V / VIII arasinda label-count-caveat consistency pass yap.
4. Final numbering/crossref kararlarini manuscript integration asamasinda kilitle.

---

## Re-Entry Reminder (2026-03-12)

Son mutabakat:
- `V-E` bagimsiz alt-bolum olarak kaldirildi.
- Section V sonunda bounded bir closeout synthesis olarak tutuldu.
- `Table VII` head-to-head comparative artifact olarak freeze edildi.
- Frontier/eligibility compression mantigi tabloya yuklenmeyecek; metin + `Fig. 5` tarafinda kalacak.

Bir sonraki adim:
1. Once `Fig. V-1` ve `Fig. V-2` icin kisa bir figure specification gecilecek.
2. Hemen ardindan canonical CSV kaynaklarindan gercek figure asset uretimine gecilecek.

Acik not:
- Bu asamada "asset production" yalnizca ne cizilecegini yazmak degil, gercek figure dosyalarinin uretilmesini de kapsiyor.

---

## Camera-Ready Cikis Kriterleri (Section V)

- `Fig. V-1` ve `Fig. V-2` gercek asset olarak mevcut olacak.
- `Table V`, `Table VI`, `Table VII` caption ve note dili freeze edilecek.
- `Table VII` comparative-table rolu korunacak; frontier semantics tabloya asiri yuklenmeyecek.
- Section V closeout synthesis yapisi freeze edilmis olacak.
- Section I ile Section V arasinda study-level vs governed-scenario-level scope karisikligi kalmayacak.
- Section IV taxonomy labels ve Section VIII challenge yorumlari Section V metric-politika diliyle uyumlu olacak.
- No plane-mix, no metric-alias, no `dz`-to-`drmin` substitution regresyonu kalmayacak.
