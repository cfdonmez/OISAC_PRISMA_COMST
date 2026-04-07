# Figures Audit

Hedef dosya:

- [bare_jrnl_new_sample4.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex)

Referans checklist:

- [03_figures_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/03_figures_checklist.md)

## Kapsam

- Ana manuscript govdesi `Introduction` ile `CONCLUSIONS` arasinda denetlendi.
- `CONCLUSIONS` sonrasindaki biography/template kalintilari ana figure denetimine dahil edilmedi, ancak ayri not olarak belirtildi.

## Durum Ozeti

- Gecti: `graphicx` paketi yuklu, ana govdede `14` figure var, `14/14` figure etiketi mevcut, duplicate figure label yok, tum ana figure label'lari metin icinde en az bir kez refere ediliyor, figure dosyalari mevcut, derlemede kayip gorsel hatasi cikmiyor.
- Duzeltildi: ana manuscript icindeki `[htbp]` figure float secimleri IEEEtran'a daha uygun olacak sekilde `[!t]` yapisina cekildi.
- Risk / not: `CONCLUSIONS` sonrasinda `Biography Section` template blogu var ve orada `fig1` kullanan ornek bir biyografi fotografi yer aliyor; bu ana manuscript figure setinin parcasi degil.

## Sayisal Ozet

- Ana govde figure sayisi: `14`
- Ana govde figure label sayisi: `14`
- Duplicate figure label: `0`

Label listesi:

- `fig:fig1`
- `fig:fig2`
- `fig:fig3`
- `fig:fig_ii_1`
- `fig:fig_ii_2`
- `fig:fig_iii_1`
- `fig:fig_iv_1`
- `fig:fig_iv_2`
- `fig:fig_v_1`
- `fig:fig_v_2`
- `fig:fig_vi_1`
- `fig:fig_vi_2`
- `fig:fig_vii_1`
- `fig:fig_viii_1`

## Madde Bazli Kontrol

- [x] Gorsel paketi yuklu: `\usepackage{graphicx}`.
  Kanit: [bare_jrnl_new_sample4.tex#L11](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L11)

- [x] Her figur `figure` veya gerekiyorsa `figure*` ortami icinde.
  Ornekler: [bare_jrnl_new_sample4.tex#L58](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L58), [bare_jrnl_new_sample4.tex#L747](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L747), [bare_jrnl_new_sample4.tex#L2315](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2315)

- [x] IEEE float tercihi icin uygun yerde `[!t]` kullanilmis.
  Duzeltme: ana manuscript icindeki `[htbp]` figure ortamları `[!t]` olarak standardize edildi.

- [x] `\centering` kullanilmis.
  Ornekler: [bare_jrnl_new_sample4.tex#L59](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L59), [bare_jrnl_new_sample4.tex#L748](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L748), [bare_jrnl_new_sample4.tex#L2316](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2316)

- [x] Gorsel `\includegraphics[...] {...}` ile eklenmis.
  Ornekler: [bare_jrnl_new_sample4.tex#L60](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L60), [bare_jrnl_new_sample4.tex#L1325](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1325), [bare_jrnl_new_sample4.tex#L2317](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2317)
  Not: [bare_jrnl_new_sample4.tex#L857](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L857) satirindaki PRISMA figure'u `tabular/parbox` ile inline ciziliyor; bu bilincli bir istisna.

- [x] Her figurin bir `\caption{...}` satiri var.
  Ornekler: [bare_jrnl_new_sample4.tex#L61](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L61), [bare_jrnl_new_sample4.tex#L750](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L750), [bare_jrnl_new_sample4.tex#L2318](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2318)

- [x] `\label{...}` satiri `\caption{...}` satirindan sonra geliyor.
  Ornekler: [bare_jrnl_new_sample4.tex#L61](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L61) -> [bare_jrnl_new_sample4.tex#L62](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L62), [bare_jrnl_new_sample4.tex#L876](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L876) -> [bare_jrnl_new_sample4.tex#L877](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L877)

- [x] Her figur etiketi benzersiz.
  Sonuc: duplicate `fig:` label bulunmadi.

- [x] Label semasi tutarli, tercihen `fig:...`.
  Sonuc: ana govdedeki tum figure label'lari `fig:` oneki tasiyor.

- [x] Metin icinde figur numaralari elle yazilmamis.
  Sonuc: `CONCLUSIONS` oncesinde hard-coded `Fig. 1`, `Fig. II-1` tipi kacis bulunmadi.

- [x] Metin icinde figurler `\ref{...}` ile refere ediliyor.
  Ref count ozetleri:
  - `fig:fig1` -> `1`
  - `fig:fig2` -> `3`
  - `fig:fig3` -> `1`
  - `fig:fig_ii_1` -> `1`
  - `fig:fig_ii_2` -> `1`
  - `fig:fig_iii_1` -> `1`
  - `fig:fig_iv_1` -> `4`
  - `fig:fig_iv_2` -> `5`
  - `fig:fig_v_1` -> `7`
  - `fig:fig_v_2` -> `5`
  - `fig:fig_vi_1` -> `1`
  - `fig:fig_vi_2` -> `1`
  - `fig:fig_vii_1` -> `2`
  - `fig:fig_viii_1` -> `4`

- [x] Manuscript stiline gore referans formati tutarli: ornegin `Fig.~\ref{...}`.
  Ornekler: [bare_jrnl_new_sample4.tex#L56](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L56), [bare_jrnl_new_sample4.tex#L459](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L459), [bare_jrnl_new_sample4.tex#L2309](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2309)

- [x] Tum gorsel dosyalari mevcut ve derleme sirasinda kayip dosya hatasi vermiyor.
  Not: ana govdede dis dosya kullanan tum `figures/...` yolları bulundu ve `pdflatex -draftmode` kontrolunde kayip gorsel hatasi cikmadi.

- [x] Caption metni figuru acikliyor; sadece dosya adini tekrar etmiyor.
  Not: ana govdedeki caption'lar aciklayici ve anlatiyla uyumlu.

- [x] Ayni figurin hem caption hem metin icindeki yorumu birbiriyle uyumlu.
  Not: daha once yapilan semantic figure ref temizligi bu uyumu guclendirmis durumda.

- [ ] Tum figurler derlenebilir, numaralari otomatik, metin baglantilari acik ve label yapisi temiz.
  Genel durum: ana manuscript icin bu madde buyuk olcude gecti; ancak submission temizligi acisindan `CONCLUSIONS` sonrasindaki biography/template blogu daha sonra ayiklanmalidir.

## Yapilan Duzeltmeler

1. Ana manuscript icindeki figure float secimleri `[htbp]` yerine `[!t]` olacak sekilde standardize edildi.

## Kalan Riskler

1. [bare_jrnl_new_sample4.tex#L2916](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2916) sonrasindaki `Biography Section` template kalintisi kendi ornek foto blogunu tasiyor.
2. Bu bolum ana manuscript figure audit'inin parcasi degil, ama final submission temizligi icin sonra ele alinmali.

## Onerilen Sonraki Adim

- Figures checklist ana govde icin "gecti" seviyesine geldi.
- Sonraki mantikli adim [04_tables_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/04_tables_checklist.md) ya da istersen en sonda biography/template kuyrugunu temizlemek.
