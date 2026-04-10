# Equations and Math Audit

Hedef dosya:

- [bare_jrnl_new_sample4.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex)

Referans checklist:

- [06_equations_and_math_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/06_equations_and_math_checklist.md)

## Kapsam

- Ana manuscript govdesi `Introduction` ile `CONCLUSIONS` arasinda denetlendi.
- `CONCLUSIONS` sonrasi template/biography kuyrugu bu auditin kapsamina alinmadi.

## Durum Ozeti

- Gecti: equation/math katmaninda `eqnarray` veya `$$ ... $$` kullanimi bulunmadi.
- Gecti: denklem ortamlari genel olarak `equation + split/aligned` yapisi ile dogru kurulmus.
- Gecti: hard-coded denklem numarasi veya `Eq. (1)` tipi manuel referans kacaklari bulunmadi.
- Gecti: `codex_eq` jobname ile yapilan `pdflatex -> bibtex -> pdflatex -> pdflatex` kontrolunde amsmath-ozel hata veya undefined citation/reference uyarisi gorulmedi.
- Gozlem: ana govdede `56` adet `equation` ortami var; bunlarin yalnizca `4` tanesi etiketli. Mevcut govdede denklem capraz referansi neredeyse hic kullanilmadigi icin bu durum islevsel sorun olusturmuyor.
- Duzeltildi: anlamsiz iki label adi semantik hale getirildi.

## Sayisal Ozet

- `equation` ortami sayisi: `56`
- Etiketli denklem sayisi: `4`
- Ana govdede bulunan denklem label'lari: `4`
- Ana govdede bulunan `\eqref{...}` kullanimi: `0`
- Ana govdede bulunan `\ref{eq:...}` kullanimi: `0`
- `eqnarray` kullanimi: `0`
- `$$ ... $$` kullanimi: `0`
- Kalan adjacent equation-reference kacagi: `0`

## Yapilan Duzeltmeler

1. [bare_jrnl_new_sample4.tex#L419](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L419) satirindaki `\label{eq11}` daha acik bir adla `\label{eq:measurement_plane_contract}` yapisina cevrildi.
2. [bare_jrnl_new_sample4.tex#L544](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L544) satirindaki `\label{eq1wq1}` daha acik bir adla `\label{eq:receiver_plane_contract}` yapisina cevrildi.

## Madde Bazli Kontrol

- [x] Numarali tek satir denklemler `equation` ortami ile yazilmis.
  Ornekler: [bare_jrnl_new_sample4.tex#L405](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L405), [bare_jrnl_new_sample4.tex#L411](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L411), [bare_jrnl_new_sample4.tex#L1825](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1825)

- [x] Gerekli denklemler `\label{...}` ile etiketlenmis.
  Kanit: [bare_jrnl_new_sample4.tex#L419](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L419), [bare_jrnl_new_sample4.tex#L478](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L478), [bare_jrnl_new_sample4.tex#L493](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L493), [bare_jrnl_new_sample4.tex#L544](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L544)
  Not: govdede denklem capraz referansi olmadigi icin etiket yogunlugu dusuk ama islevsel olarak yeterli.

- [x] Denklem referanslari hard-coded `(1)` seklinde degil.
  Sonuc: regex taramasinda manuel equation-number kacak bulunmadi.

- [x] Denklem numaralari makale boyunca ardiskil ve sirali.
  Sonuc: varsayilan IEEEtran numaralandirmasi kullaniliyor; section-based veya Roman numeral equation numbering yok.

- [x] Roman numeral veya section-based equation numbering kullanilmiyor.
  Sonuc: class varsayilan numaralandirma modeli korunuyor.

- [x] Uzun ve cok satirli denklemler `split` veya `aligned` ile dogru bolunmus.
  Ornekler: [bare_jrnl_new_sample4.tex#L484](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L484), [bare_jrnl_new_sample4.tex#L560](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L560), [bare_jrnl_new_sample4.tex#L1850](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L1850)

- [x] Hizalama icin `&` kullanilmis; elle bosluklarla sahte hizalama yapilmamis.
  Sonuc: incelenen multiline bloklarda `aligned/split` hizasi dogru.

- [x] Matris/cases/array tarafinda acik bir ortam hatasi bulunmadi.
  Sonuc: ana govdede problemli `array`/`cases` kullanimi yok; gereksiz el yapimi yapilar tespit edilmedi.

- [x] Standart matematik fonksiyonlari ve text-icerikleri okunabilir bicimde yazilmis.
  Ornekler: [bare_jrnl_new_sample4.tex#L418](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L418), [bare_jrnl_new_sample4.tex#L543](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L543)

- [x] `eqnarray` kullanilmiyor.
  Sonuc: `0`

- [x] `$$ ... $$` kullanilmiyor.
  Sonuc: `0`

- [x] Hard-coded equation number yok.
  Sonuc: `0`

## Derleme Bulgulari

- `codex_eq` gecici derleme zincirinde amsmath-ozel hata gorulmedi.
- Undefined citation/reference uyarisi gorulmedi.
- Log'da kalan box uyarilari daha cok tablo ve dar sutun paragrafi kaynaklidir; equation katmanina ozel kirici bir bulgu tespit edilmedi.

## Kalan Riskler

1. Denklem checklist acisindan kritik acik bulgu kalmadi.
2. Eger ileride denklem capraz referanslari eklenecekse, yeni referans verilecek denklemlere semantik `eq:...` label'lar eklenmesi gerekir.

## Onerilen Sonraki Adim

- Equation/math katmani kapandi; siradaki mantikli tur [08_final_pass_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/08_final_pass_checklist.md) veya istenirse [07_back_matter_and_biographies_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/07_back_matter_and_biographies_checklist.md) olabilir.
