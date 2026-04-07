# Body, Sections, and Lists Checklist

Kaynak:

- [New_IEEEtran_how-to.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/New_IEEEtran_how-to.tex)
- `How to Create Common Body Elements`

## Kontrol Listesi

- [ ] Ilk paragraf gerekiyorsa `\IEEEPARstart{T}{his}` benzeri drop-cap yapisi ile basliyor.
- [ ] Section basliklari `\section{...}` ile kurulmus.
- [ ] Alt basliklar `\subsection{...}` ile kurulmus.
- [ ] Ucuncu seviye basliklar `\subsubsection{...}` ile kurulmus.
- [ ] Section/subsection numaralari elle yazilmamis; LaTeX otomatik numaralandiriyor.
- [ ] Baslik sonrasindaki ilk paragraf icin gerekiyorsa `\noindent` kullanimi tutarli.
- [ ] Govde akisi section -> subsection -> subsubsection hiyerarsisine uyuyor.
- [ ] Govde icinde liste gerekiyorsa standart `itemize` veya `enumerate` ortami kullaniliyor.
- [ ] Liste maddeleri tutarli noktalama ile bitiyor.
- [ ] Govde icinde sabit elle yazilmis "Section II", "Subsection B" tipleri varsa bunlar editorial olarak bilincli kullanilmis.

## Hizli Tarama

- [ ] `\IEEEPARstart`
- [ ] `\section{`
- [ ] `\subsection{`
- [ ] `\subsubsection{`
- [ ] `\noindent`
- [ ] `\begin{itemize}` veya `\begin{enumerate}`

## Sik Hatalar

- [ ] Baslik seviyelerini atlayarak kullanmak
- [ ] Elle numara yazarak baslik olusturmak
- [ ] Section acilip ilk paragrafi fazla girintili veya bicimsiz birakmak
- [ ] Liste maddelerinde noktalama ve buyuk/kucuk harf tutarsizligi

## Gecis Kriteri

- [ ] Govde yapisi okunur, IEEEtran mantigina uygun ve hiyerarsik olarak temiz.
