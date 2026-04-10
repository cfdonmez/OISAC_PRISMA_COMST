# Figures Checklist

Kaynak:

- [New_IEEEtran_how-to.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/New_IEEEtran_how-to.tex)
- `How to Create Common Body Elements -> Figures`
- `Additional Advice`
- `A Final Checklist`

## Kontrol Listesi

- [ ] Gorsel paketi yuklu: `\usepackage{graphicx}`.
- [ ] Her figur `figure` veya gerekiyorsa `figure*` ortami icinde.
- [ ] IEEE float tercihi icin uygun yerde `[!t]` kullanilmis.
- [ ] `\centering` kullanilmis.
- [ ] Gorsel `\includegraphics[...] {...}` ile eklenmis.
- [ ] Her figurin bir `\caption{...}` satiri var.
- [ ] `\label{...}` satiri `\caption{...}` satirindan sonra geliyor.
- [ ] Her figur etiketi benzersiz.
- [ ] Label semasi tutarli, tercihen `fig:...`.
- [ ] Metin icinde figur numaralari elle yazilmamis.
- [ ] Metin icinde figurler `\ref{...}` ile refere ediliyor.
- [ ] Manuscript stiline gore referans formati tutarli: ornegin `Fig.~\ref{...}`.
- [ ] Tum gorsel dosyalari mevcut ve derleme sirasinda kayip dosya hatasi vermiyor.
- [ ] Caption metni figuru acikliyor; sadece dosya adini tekrar etmiyor.
- [ ] Ayni figurin hem caption hem metin icindeki yorumu birbiriyle uyumlu.

## Hizli Tarama

- [ ] `\begin{figure}`
- [ ] `\begin{figure*}`
- [ ] `\includegraphics`
- [ ] `\caption{`
- [ ] `\label{fig:`
- [ ] `Fig.~\ref{`

## Sik Hatalar

- [ ] `\label` satirini `\caption` oncesine koymak
- [ ] Figuru elle "Fig. 3" diye yazip `\ref` kullanmamak
- [ ] Gorsel dosyasi klasorde yokken kaynakta duruyor sanmak
- [ ] Caption'u asiri kisa veya baglamsiz birakmak
- [ ] Ayni label'i birden fazla figure icin kullanmak

## Gecis Kriteri

- [ ] Tum figurler derlenebilir, numaralari otomatik, metin baglantilari acik ve label yapisi temiz.
