# Body, Sections, and Lists Audit

Hedef dosya:

- [bare_jrnl_new_sample4.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex)

Referans checklist:

- [02_body_sections_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/02_body_sections_checklist.md)

## Kapsam

- Ana manuscript govdesi `Introduction` ile `CONCLUSIONS` arasinda denetlendi.
- `CONCLUSIONS` sonrasindaki template kalintilari ana body denetimine dahil edilmedi, ancak ayri risk olarak not edildi.

## Durum Ozeti

- Gecti: `\IEEEPARstart` kullanimi mevcut, section/subsection/subsubsection hiyerarsisi ana govdede kurulu, listeler standart `itemize` / `enumerate` ortamlariyla yazilmis, liste satirlarinda belirgin noktalama sorunu tespit edilmedi.
- Duzeltildi: Section VI ve VII alt basliklarindaki elle yazilmis `VI-A.`, `VII-A.` vb. baslik numaralari kaldirildi; `Section VI Synthesis and Transition` basligi sadeleştirildi.
- Dikkat isteyen risk: `CONCLUSIONS` sonrasinda halen `Biography Section` adli template kalintisi bulunuyor.

## Madde Bazli Kontrol

- [x] Ilk paragraf gerekiyorsa `\IEEEPARstart{T}{his}` benzeri drop-cap yapisi ile basliyor.
  Kanit: [bare_jrnl_new_sample4.tex#L46](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L46)

- [x] Section basliklari `\section{...}` ile kurulmus.
  Kanit: [bare_jrnl_new_sample4.tex#L43](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L43), [bare_jrnl_new_sample4.tex#L398](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L398), [bare_jrnl_new_sample4.tex#L777](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L777), [bare_jrnl_new_sample4.tex#L898](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L898), [bare_jrnl_new_sample4.tex#L1421](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1421), [bare_jrnl_new_sample4.tex#L1681](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1681), [bare_jrnl_new_sample4.tex#L1982](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1982), [bare_jrnl_new_sample4.tex#L2307](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2307), [bare_jrnl_new_sample4.tex#L2891](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2891)

- [x] Alt basliklar `\subsection{...}` ile kurulmus.
  Not: ana govdede tum ana alt bolumler `\subsection` ile tasinmis.

- [x] Ucuncu seviye basliklar `\subsubsection{...}` ile kurulmus.
  Kanit: [bare_jrnl_new_sample4.tex#L145](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L145), [bare_jrnl_new_sample4.tex#L400](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L400), [bare_jrnl_new_sample4.tex#L904](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L904)

- [x] Section/subsection numaralari elle yazilmamis; LaTeX otomatik numaralandiriyor.
  Duzeltme: Section VI ve VII alt basliklarindaki manual `VI-A.`, `VII-A.` vb. onekler kaldirildi.
  Kanit: [bare_jrnl_new_sample4.tex#L1744](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1744), [bare_jrnl_new_sample4.tex#L2093](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2093)

- [x] Baslik sonrasindaki ilk paragraf icin gerekiyorsa `\noindent` kullanimi tutarli.
  Not: dosyada acik `\noindent` kullanimi yok. Bu durum tek basina sorun degil; IEEEtran/LaTeX section acilislarinda ilk paragraf duzenini zaten yonetiyor.

- [x] Govde akisi section -> subsection -> subsubsection hiyerarsisine uyuyor.
  Not: ana govdede baslik seviyesi atlama veya bozuk nesting gozlenmedi.

- [x] Govde icinde liste gerekiyorsa standart `itemize` veya `enumerate` ortami kullaniliyor.
  Kanit: [bare_jrnl_new_sample4.tex#L50](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L50), [bare_jrnl_new_sample4.tex#L227](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L227), [bare_jrnl_new_sample4.tex#L305](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L305), [bare_jrnl_new_sample4.tex#L317](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L317)

- [x] Liste maddeleri tutarli noktalama ile bitiyor.
  Not: hizli satir-tabanli taramada belirgin noktalama eksigi bulunmadi.

- [x] Govde icinde sabit elle yazilmis "Section II", "Subsection B" tipleri varsa bunlar editorial olarak bilincli kullanilmis.
  Not: dosyada `Section II`, `Section IV`, `Section VIII` benzeri gostergeler sık kullaniliyor; bunlar capraz-anlati ve roadmap yapisi icin bilincli editorial tercih gibi gorunuyor.

- [ ] Govde yapisi okunur, IEEEtran mantigina uygun ve hiyerarsik olarak temiz.
  Genel durum: ana govde buyuk oranda temiz; ancak `CONCLUSIONS` sonrasindaki template biography blogu submission temizligi acisindan ileride kaldirilmalidir.

## Yapilan Duzeltmeler

1. `\subsection{VI-A. ...}` -> `\subsection{...}`
2. `\subsection{VII-A. ...}` -> `\subsection{...}`
3. `\subsection{Section VI Synthesis and Transition}` -> `\subsection{Synthesis and Transition}`

## Kalan Riskler

1. `CONCLUSIONS` sonrasinda [bare_jrnl_new_sample4.tex#L2916](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L2916) satirinda `Biography Section` adli template blogu duruyor.
2. Bunu bu turda body denetiminden ayri tuttum; daha dogru yeri `07_back_matter_and_biographies_checklist.md` audit'idir.

## Onerilen Sonraki Adim

- Body/section checklist icin ana govdeyi "buyuk oranda gecti" kabul edebiliriz.
- Sonraki mantikli adim [03_figures_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/03_figures_checklist.md) ya da istersen once `Biography Section` template kalintisini temizlemek.
