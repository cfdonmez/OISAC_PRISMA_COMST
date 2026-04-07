# References and Citations Checklist

Kaynak:

- [New_IEEEtran_how-to.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/New_IEEEtran_how-to.tex)
- `Citations to the Bibliography`
- `Bibliographies`
- `Accented Characters in References`
- `Use of BibTeX`
- `Additional Advice`
- `A Final Checklist`

## In-Text Citation Kontrolu

- [ ] Ustte `\usepackage{cite}` yuklu.
- [ ] Metin icindeki atiflar `\cite{...}` ile veriliyor.
- [ ] Birden fazla kaynak gerekiyorsa tek `\cite{a,b,c}` blogunda gruplanmis.
- [ ] Elle yazilmis `[1]`, `[2]` gibi hard-coded atiflar yok.
- [ ] Metindeki atiflar derleme sonunda cozuluyor; tanimsiz citation yok.

## Bibliography Kontrolu

- [ ] Kaynakca ya `thebibliography` icinde ya da harici BibTeX akisi ile tanimli.
- [ ] `\bibitem{...}` anahtarlari benzersiz.
- [ ] Metindeki `\cite{...}` anahtarlari ile bibliography anahtarlari uyusuyor.
- [ ] BibTeX kullaniliyorsa gerekli `.bib` dosyasi projeye dahil.
- [ ] Tum referanslarin yazar, baslik, yayin, yil ve sayfa bilgileri makul duzeyde tam.
- [ ] Referans yazim bicimi genel olarak tutarli.

## Accent ve Tipografi Kontrolu

- [ ] Referanslardaki ozel karakterler standart LaTeX accent kodlari ile yazilmis.
- [ ] Accent icin math mode hackleri kullanilmamis.
- [ ] Italic, proceedings, journal vb. stiller karmasik ama duzenli.

## Sik Hatalar

- [ ] `\cite{...}` kullanmak yerine numarayi elle yazmak
- [ ] BibTeX kullanip `.bib` dosyasini gondermemek
- [ ] Ayni key'i farkli iki kaynakta kullanmak
- [ ] Accented karakterleri math ile yazmak
- [ ] Metinde cagirilan kaynagin bibliography'de olmamasi

## Gecis Kriteri

- [ ] Metin ici atiflar otomatik, bibliography tam, ve kayip/undefined citation yok.
