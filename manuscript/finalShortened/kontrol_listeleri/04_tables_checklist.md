# Tables Checklist

Kaynak:

- [New_IEEEtran_how-to.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/New_IEEEtran_how-to.tex)
- `How to Create Common Body Elements -> Tables`
- `Additional Advice`

## Kontrol Listesi

- [ ] Her tablo `table` veya gerekiyorsa `table*` ortami icinde.
- [ ] Tablo ortalanmasi `\centering` veya `center` yaklasimi ile duzenli.
- [ ] Her tabloda `\caption{...}` mevcut.
- [ ] `\label{...}` satiri `\caption{...}` satirindan sonra geliyor.
- [ ] Her tablo etiketi benzersiz.
- [ ] Label semasi tutarli, tercihen `tab:...`.
- [ ] Metin icinde tabloya referans `Table~\ref{...}` ile veriliyor.
- [ ] Elle yazilmis `Table I`, `Table II` gibi sabit numaralar kullanilmiyor.
- [ ] Tablolarin metinde en az bir acik baglanti cumlesi var.
- [ ] Caption tablonun neyi gosterdigini acik sekilde tarif ediyor.
- [ ] Sutun yapisi tutarli; gereksiz karmasa veya bozuk satir yok.
- [ ] Genis tablolar icin `table*` karari bilincli verilmis.
- [ ] Metin, tabloyu sadece tekrar etmiyor; yorumluyor veya baglama oturtuyor.

## Hizli Tarama

- [ ] `\begin{table}`
- [ ] `\begin{table*}`
- [ ] `\caption{`
- [ ] `\label{tab:`
- [ ] `Table~\ref{`

## Sik Hatalar

- [ ] `\label` satirini `\caption` oncesine koymak
- [ ] Tablolari metin icinde hic refere etmemek
- [ ] Elle tablo numarasi yazmak
- [ ] Ayni `tab:` label'ini tekrar kullanmak
- [ ] Caption'u sadece kisa bir baslik gibi birakmak

## Gecis Kriteri

- [ ] Tum tablolar otomatik numarali, metinle bagli ve label/caption sirasi dogru.
