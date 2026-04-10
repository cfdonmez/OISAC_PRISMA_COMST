# Equations and Math Checklist

Kaynak:

- [New_IEEEtran_how-to.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/New_IEEEtran_how-to.tex)
- `Mathematical Typography and Why It Matters`
- `Additional Advice`
- `A Final Checklist`

## Numbered Equations

- [ ] Numarali tek satir denklemler `equation` ortami ile yazilmis.
- [ ] Gerekli denklemler `\label{...}` ile etiketlenmis.
- [ ] Denklem referanslari hard-coded `(1)` seklinde degil; `(\ref{...})` veya `\eqref{...}` ile veriliyor.
- [ ] Denklem numaralari makale boyunca ardiskil ve sirali.
- [ ] Roman numeral veya section-based equation numbering kullanilmiyor.
- [ ] Appendix denklemleri varsa stil bilincli: devam eden numara veya `(A1), (A2)` mantigi.

## Multiline and Alignment

- [ ] Uzun ama hizalama gerektirmeyen denklemler icin uygun yerde `multline` kullanilmis.
- [ ] Hizalanacak cok satirli denklemler icin `align` veya `align*` kullanilmis.
- [ ] Numarasiz tek satir denklemler `\[...\]` veya `equation*` ile verilmis.
- [ ] Numarasiz cok satirli ve hizali denklemler `align*` ile verilmis.
- [ ] Hizalama icin `&` kullanilmis; elle bosluklarla sahte hizalama yapilmamis.

## Subnumbering

- [ ] Alt numarali denklem gruplari gerekiyorsa `subequations` ortami kullanilmis.
- [ ] Alt numaralar `(1a)`, `(1b)` stilinde; hyphen veya period yok.

## Math Structures

- [ ] Matrisler icin uygun ortam secilmis: `matrix`, `pmatrix`, `bmatrix`, `Bmatrix`, `vmatrix`, `Vmatrix`.
- [ ] `array` yalnizca gercekten gerekli ise kullanilmis.
- [ ] `cases` yapilarinda `cases` ortami kullanilmis.
- [ ] `cases` icinde kelimeler `\text{...}` ile verilmis.
- [ ] `cases` ve `array` icinde kolon hizasi `&` ile dogru kurulmus.

## Function and Text Formatting

- [ ] Standart matematik fonksiyonlari dogru bicimde yazilmis.
- [ ] Gerekli text tabanli ifadeler `\text{...}` ile yazilmis.
- [ ] Equation icindeki metin akronimleri `\text{MSE}` benzeri bicimde verilmis.

## Yasak / Kacinilacaklar

- [ ] `eqnarray` kullanilmiyor.
- [ ] `$$ ... $$` kullanilmiyor.
- [ ] `array` icinde `\nonumber` veya `\notag` kullanilmiyor.
- [ ] Hard-coded equation number yok.

## Sik Hatalar

- [ ] Uzun denklemi tek satira sikistirmak
- [ ] `align` gerekirken `equation` icinde zorlamak
- [ ] `cases` yerine `array` ile gereksiz el yapimi kurulum yapmak
- [ ] Denklem numaralarini elle yazmak
- [ ] `\label` / `\ref` zincirini kurmamak

## Gecis Kriteri

- [ ] Denklem tipografisi temiz, ortam secimi dogru, numbering ve cross-reference otomatik.
