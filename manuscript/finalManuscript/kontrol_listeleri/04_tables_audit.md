# Tables Audit

Hedef dosya:

- [bare_jrnl_new_sample4.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex)

Referans checklist:

- [04_tables_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/04_tables_checklist.md)

## Kapsam

- Ana manuscript govdesi `Introduction` ile `CONCLUSIONS` arasinda denetlendi.
- `CONCLUSIONS` sonrasindaki biography/template kalintilari ana table denetimine dahil edilmedi.

## Durum Ozeti

- Gecti: ana govdede `24` tablo var, `24/24` table etiketi mevcut, duplicate table label yok, tum table ortamlarinda `\centering` var, tum table float secimleri `[!t]`, tum label'lar `\caption{...}` sonrasinda geliyor, tum ana table label'lari metin icinde en az bir kez refere ediliyor.
- Gecti: metin icindeki table referanslari otomatik hale getirilmis durumda; `Table~\ref{...}` kullanimi `43`, `Tables~\ref{...}` kullanimi `1` kez goruluyor.
- Duzeltildi: onceki temizlik turunda manuel `Table I`, `Table VI-A` benzeri kullanimlar `Table~\ref{...}` yapisina cevrildi, anlamsal olarak tabloyu anlatan ama acik adres vermeyen guclu cumlelere de uygun ref baglari eklendi.
- Duzeltildi: duplicate label riski olusturan sonraki table etiketi `tab:section7_dualview` ayrildi ve [bare_jrnl_new_sample4.tex#L2792](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2792) satirinda `tab:viii_g_1` olarak temizlendi.
- Risk / not: iki gecisli `pdflatex -draftmode` kontrolunde `tab:` kaynakli unresolved ya da multiply-defined warning kalmadi. Derlemede kalan undefined ref ozeti tabloya degil, kaynakca islenmemesi ve [bare_jrnl_new_sample4.tex#L854](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L854) satirindaki `app:included_studies` referansina bagli.

## Sayisal Ozet

- Ana govde table sayisi: `24`
- Ana govde table label sayisi: `24`
- Duplicate table label: `0`
- `\centering` kullanan table bloklari: `24/24`
- `\caption` sonra `\label` sirasini koruyan table bloklari: `24/24`
- `[!t]` float kullanan table bloklari: `24/24`

Label listesi:

- `tab:axis_comparison`
- `tab:performance_comparison`
- `tab:math_notation`
- `tab:acronyms`
- `tab:ii1`
- `tab:ii2`
- `tab:iii1`
- `tab:taxonomy_contract`
- `tab:medium_classes`
- `tab:integration_mechanisms`
- `tab:detection_observability`
- `tab:taxonomy_clusters`
- `tab:comm_metrics`
- `tab:sensing_metrics`
- `tab:comparative_slices`
- `tab:section6_notation`
- `tab:vi_a_enablers`
- `tab:vi_d_reporting`
- `tab:section7_portfolio`
- `tab:section7_dualview`
- `tab:viii_f_1`
- `tab:viii_f_2`
- `tab:viii_g_1`
- `tab:viii_g_2`

## Madde Bazli Kontrol

- [x] Her tablo `table` veya gerekiyorsa `table*` ortami icinde.
  Ornekler: [bare_jrnl_new_sample4.tex#L71](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L71), [bare_jrnl_new_sample4.tex#L332](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L332), [bare_jrnl_new_sample4.tex#L1595](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1595), [bare_jrnl_new_sample4.tex#L2850](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2850)

- [x] IEEE float tercihi icin uygun yerde `[!t]` kullanilmis.
  Sonuc: ana govdedeki `24/24` table blogu `[!t]` ile aciliyor.

- [x] Table bloklarinda `\centering` kullanilmis.
  Sonuc: ana govdedeki `24/24` table blogunda `\centering` mevcut.

- [x] Her tablonun bir `\caption{...}` satiri var.
  Ornekler: [bare_jrnl_new_sample4.tex#L72](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L72), [bare_jrnl_new_sample4.tex#L333](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L333), [bare_jrnl_new_sample4.tex#L1596](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1596), [bare_jrnl_new_sample4.tex#L2851](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2851)

- [x] `\label{...}` satiri `\caption{...}` satirindan sonra geliyor.
  Ornekler: [bare_jrnl_new_sample4.tex#L72](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L72) -> [bare_jrnl_new_sample4.tex#L73](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L73), [bare_jrnl_new_sample4.tex#L1596](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1596) -> [bare_jrnl_new_sample4.tex#L1597](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1597)

- [x] Her table etiketi benzersiz.
  Sonuc: duplicate `tab:` label bulunmadi.

- [x] Label semasi tutarli, tercihen `tab:...`.
  Sonuc: ana govdedeki tum table label'lari `tab:` oneki tasiyor.

- [x] Metin icinde tablo numaralari elle yazilmamis.
  Sonuc: ana govdede manuel `Table I`, `Table IV-A`, `Table VIII-F-2` tipi kullanimlar temizlenmis durumda; referanslar otomatik.

- [x] Metin icinde tablolar `\ref{...}` ile refere ediliyor.
  Ornekler: [bare_jrnl_new_sample4.tex#L69](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L69), [bare_jrnl_new_sample4.tex#L147](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L147), [bare_jrnl_new_sample4.tex#L331](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L331), [bare_jrnl_new_sample4.tex#L569](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L569), [bare_jrnl_new_sample4.tex#L1685](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1685), [bare_jrnl_new_sample4.tex#L1984](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1984), [bare_jrnl_new_sample4.tex#L2633](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2633), [bare_jrnl_new_sample4.tex#L2787](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2787)

- [x] Manuscript stiline gore referans formati tutarli: `Table~\ref{...}` ve gerekiyorsa `Tables~\ref{...}`.
  Sonuc: ana govdede `Table~\ref{...}` `43` kez, `Tables~\ref{...}` `1` kez geciyor.

- [x] Tablolar yalniz bir kere gecen izole nesneler degil; anlatiyla eslesen metin anchor'lari mevcut.
  Not: onceki semantic ref temizligi sayesinde ozellikle Section VI-VIII tablolari anlatida acik anchor cumleleriyle baglandi.

- [x] Iki gecisli draft derlemede `tab:` kaynakli unresolved ya da duplicate warning kalmiyor.
  Kontrol: `pdflatex -draftmode -jobname=codex_tableaudit bare_jrnl_new_sample4.tex` iki kez calistirildi; kalan undefined ref ozeti table label'larindan kaynaklanmiyor.

- [ ] Tum tablolar otomatik numarali, metin baglantilari acik, label yapisi temiz ve submission'a hazir.
  Genel durum: ana manuscript icin bu madde buyuk olcude gecti; ancak final submission temizligi icin `CONCLUSIONS` sonrasi template kuyrugu ve ayri bibliography isleme adimi sonra ele alinmali.

## Yapilan Duzeltmeler

1. Manuel table numaralari ve hard-coded table referanslari otomatik `Table~\ref{...}` / `Tables~\ref{...}` yapisina cevrildi.
2. Table'lari aciklamasina ragmen ref vermeyen guclu metin anchor'larina uygun table referanslari eklendi.
3. Duplicate label riski tasiyan sonraki `tab:section7_dualview` etiketi `tab:viii_g_1` olarak ayrildi.

## Kalan Riskler

1. [bare_jrnl_new_sample4.tex#L854](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L854) satirindaki `app:included_studies` referansi hala tanimsiz; bu tabloya degil appendix/back matter zincirine bagli bir unresolved ref.
2. `pdflatex` draft gecislerinde kaynakca henuz islenmedigi icin cite warning'leri suruyor; bu table audit sonucunu degistirmiyor.
3. `CONCLUSIONS` sonrasi template kuyrugu bu audit kapsamina alinmadi; final submission oncesi ayri temizlenmeli.

## Onerilen Sonraki Adim

- Tables checklist ana govde icin "gecti" seviyesine geldi.
- Sonraki mantikli adim [05_references_and_citations_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/05_references_and_citations_checklist.md); cunku artik figure-table-eksenindeki otomatik baglar temiz ve kaynakca/citation zinciri daha anlamli denetlenebilir durumda.
