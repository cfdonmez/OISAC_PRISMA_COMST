# Final Pass Checklist

Kaynak:

- [New_IEEEtran_how-to.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/New_IEEEtran_how-to.tex)
- `Additional Advice`
- `A Final Checklist`

## Soft Reference Kontrolu

- [ ] Denklem referanslari hard-coded degil; `\eqref{...}` veya `(\ref{...})` ile verilmis.
- [ ] Figur referanslari hard-coded degil; `\ref{...}` tabanli.
- [ ] Tablo referanslari hard-coded degil; `Table~\ref{...}` tabanli.
- [ ] Section/appendix icindeki capraz referanslarda otomatik mantik korunmus.

## Label Hijyeni

- [ ] Ayni label iki farkli nesnede tekrar kullanilmamis.
- [ ] Figure/table `\label` satiri `\caption` sonrasinda.
- [ ] Label adlari alan bazli: `fig:`, `tab:`, `eq:`, vb.

## Denklem Son Kontrol

- [ ] Denklem numaralari ardiskil; eksik veya duplicate yok.
- [ ] Alt numarali denklemler IEEE stilinde.
- [ ] Cok satirli denklemler uygun ortamlarla kirilmis.
- [ ] `eqnarray` ve `$$` bulunmuyor.

## Figur ve Tablo Son Kontrol

- [ ] Tum gorsel dosyalari projede mevcut.
- [ ] Tum figurlerin caption ve label'i mevcut.
- [ ] Tum tablolarin caption ve label'i mevcut.
- [ ] Tum figurler metin icinde en az bir kez refere ediliyor.
- [ ] Tum tablolar metin icinde en az bir kez refere ediliyor.

## Referans Son Kontrol

- [ ] Tum `\cite{...}` anahtarlari cozuluyor.
- [ ] Bibliography tam ve proje ile birlikte gonderilebilir durumda.
- [ ] BibTeX kullaniliyorsa `.bib` dosyasi mevcut.

## Derleme Son Kontrol

- [ ] En az iki gecis derleme yapildi.
- [ ] Undefined reference / missing file / duplicate label uyarilari gozden gecirildi.
- [ ] Son PDF'de numaralar ve capraz referanslar gorsel olarak kontrol edildi.

## Gecis Kriteri

- [ ] Makale IEEEtran acisindan derlenebilir, izlenebilir ve editor denetimine hazir.
