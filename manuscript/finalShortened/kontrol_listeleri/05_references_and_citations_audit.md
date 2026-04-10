# References and Citations Audit

Hedef dosya:

- [bare_jrnl_new_sample4.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex)

Referans checklist:

- [05_references_and_citations_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/05_references_and_citations_checklist.md)

## Kapsam

- Ana manuscript govdesi `Introduction` ile `CONCLUSIONS` arasinda denetlendi.
- `CONCLUSIONS` sonrasi template/biography kuyrugu bu auditin kapsamina alinmadi.

## Durum Ozeti

- Gecti: `\usepackage{cite}` yuklu, in-text atiflar `\cite{...}` ile veriliyor, bibliography BibTeX akisi ile tanimli, `references.bib` projede mevcut, duplicate `.bib` key bulunmadi, adjacent cite zincirleri temizlendi, ve kontrol derlemesinde undefined citation/reference uyarisi kalmadi.
- Guncel kiyas sonucu: `CONCLUSIONS` oncesi govdede cite edilen `101` benzersiz key'in tamami `references.bib` icinde bulundu; govdede kullanilip `.bib` tarafinda eksik kalan key sayisi `0`.
- Duzeltildi: [bare_jrnl_new_sample4.tex#L854](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L854) satirindaki tanimsiz `Appendix~\ref{app:included_studies}` baglantisi kaldirildi ve archive-temelli bir ifade ile degistirildi.
- Duzeltildi: moving-argument icindeki tablo caption cite kullanimi [bare_jrnl_new_sample4.tex#L150](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L150) satirinda `\protect\cite{...}` yapisina cekildi.
- Duzeltildi: tum kalan `\cite{a}, \cite{b}` zincirleri tek bloklara indirildi.
- Duzeltildi: `codex_refs` jobname ile yapilan `pdflatex -> bibtex -> pdflatex -> pdflatex` kontrol zincirinde undefined citation/reference uyarisi kalmadi.

## Sayisal Ozet

- Ana govde `\cite{...}` kullanim sayisi: `378`
- Ana govdede cite edilen toplam key gecisi: `633`
- Ana govdede cite edilen benzersiz key: `101`
- `references.bib` icindeki benzersiz key: `223`
- Govdede kullanilip `.bib` icinde bulunamayan key: `0`
- `.bib` icinde bulunup ana govdede kullanilmayan key: `122`
- Kalan adjacent cite zinciri: `0`
- Duplicate `.bib` key: `0`

BibTeX uyarilari:

- Guncel cited-key taramasinda `CONCLUSIONS` oncesi govdede kullanilan key'ler arasinda eksik `title/author/editor` problemi kalan kayit bulunmadi.

Sorunlu kayit ayrintilari:

- Duzeltildi: [references.bib#L1107](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/references.bib#L1107) `O_ISAC_199`
  Eski durum: `Mechanical Engineering, Science and Technology International Conference` front-matter kaydina bagliydi ve metindeki `MIMO FSO with FBG sensors` ifadesiyle uyusmuyordu.
  Yeni durum: `Towards last-mile connectivity in 6G-IoT: An integrated MIMO-FSO communication system and FBG sensors under atmospheric attenuations, strain and temperature effects`, DOI `10.1016/j.jestch.2025.101958`

- Duzeltildi: [references.bib#L1257](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/references.bib#L1257) `O_ISAC_304`
  Eski durum: authorless `IEEE Communications Magazine` issue-intro kaydina bagliydi ve shared-waveform baglamiyla uyusmuyordu.
  Yeni durum: `W-band photonic-aided mm-wave ISAC system enabled by a shared OFDM signal waveform and a two-stage carrier frequency recovery algorithm`, DOI `10.1364/OL.537847`

- Duzeltildi: [bare_jrnl_new_sample4.tex#L1186](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1186) ve [bare_jrnl_new_sample4.tex#L1217](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1217) satirlarindaki semantik olarak uyumsuz `O_ISAC_166` atfi, shared-processing baglamina daha uygun olan `O_ISAC_039` ile degistirildi.
- Duzeltildi: kullanilmayan ve metadata acisindan bozuk `O_ISAC_166` kaydi [references.bib](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/references.bib) dosyasindan kaldirildi.

## Madde Bazli Kontrol

- [x] `\usepackage{cite}` yuklu.
  Kanit: [bare_jrnl_new_sample4.tex#L12](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L12)

- [x] Metin icindeki atiflar temel olarak `\cite{...}` ile veriliyor.
  Ornekler: [bare_jrnl_new_sample4.tex#L46](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L46), [bare_jrnl_new_sample4.tex#L270](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L270), [bare_jrnl_new_sample4.tex#L909](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L909)

- [x] Birden fazla kaynak gereken yerlerde tek `\cite{a,b,c}` blogu kullanimi tam standardize edilmis.
  Durum: gecti; ana govdede kalan adjacent cite zinciri sayisi `0`.

- [x] Elle yazilmis `[1]`, `[2]` tipi hard-coded citation kullanimi icin acik bir kacak bulunmadi.
  Not: regex taramasinda ana govdede yalnizca [bare_jrnl_new_sample4.tex#L1852](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1852) satirindaki matematik araligi `[0,1]` false-positive olarak gorundu.

- [x] Metindeki atiflar derleme sonunda tam cozuluyor; undefined citation yok.
  Durum: `codex_refs` jobname ile yapilan `pdflatex -> bibtex -> pdflatex -> pdflatex` kontrol zincirinde undefined citation/reference uyarisi gorulmedi.

- [x] Bibliography BibTeX akisi ile tanimli.
  Kanit: [bare_jrnl_new_sample4.tex#L2907](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2907), [bare_jrnl_new_sample4.tex#L2908](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2908)

- [x] Gerekli `.bib` dosyasi projede mevcut.
  Kanit: [references.bib](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/references.bib)

- [x] `.bib` key'leri duplicate degil.
  Sonuc: `0` duplicate key bulundu.

- [x] Ana govdede cite edilen key'lerin tamami `.bib` dosyasinda mevcut.
  Sonuc: `101/101` benzersiz govde citation key'i `references.bib` icinde bulundu; eksik key sayisi `0`.

- [x] Ana govdede cite edilen key'ler icin temel referans metadata alanlari makul duzeyde tam.
  Durum: guncel taramada cited key'ler arasinda eksik `title/author/editor` problemi kalmadi.

- [x] Referans zinciri tam derleme akisinda stabil.
  Durum: `codex_refs` gecici audit derlemesinde `.bbl` uretildi, `bibtex` warning vermedi, ve son iki `pdflatex` gecisinde undefined citation/reference uyarisi gorulmedi.

## Yapilan Duzeltmeler

1. [bare_jrnl_new_sample4.tex#L854](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L854) satirindaki tanimsiz appendix ref kaldirildi.
2. [bare_jrnl_new_sample4.tex#L150](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L150) satirindaki caption cite `\protect\cite` ile guvenli hale getirildi.
3. Dosya genelindeki tum adjacent cite zincirleri tek `\cite{...}` bloklarina indirildi.
4. `O_ISAC_199` ve `O_ISAC_304` yanlis/uyumsuz bibliography kayitlarindan dogru kaynaklara tasindi.
5. Semantik olarak uyumsuz `O_ISAC_166` atiflari `O_ISAC_039` ile degistirildi ve bozuk kayit kaldirildi.
6. `codex_refs` gecici derleme zinciri ile BibTeX/aux davranisi dogrulandi.

## Kalan Riskler

1. References checklist acisindan kritik acik bulgu kalmadi.
2. Dosyada halen overfull/underfull box gibi tipografik uyarilar olabilir; bunlar references katmanindan ayridir.

## Onerilen Sonraki Adim

- References katmani kapandi; siradaki mantikli tur [06_equations_and_math_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/06_equations_and_math_checklist.md) veya istenirse final-pass tipografi temizligi olabilir.
