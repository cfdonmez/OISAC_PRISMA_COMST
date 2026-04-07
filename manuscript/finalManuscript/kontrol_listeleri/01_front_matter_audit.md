# Front Matter Audit

Hedef dosya:

- [bare_jrnl_new_sample4.tex](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex)

Referans checklist:

- [01_front_matter_checklist.md](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/kontrol_listeleri/01_front_matter_checklist.md)

## Durum Ozeti

- Gecti: `\title`, `\author`, `\thanks`, `\markboth`, `\maketitle`, `abstract`, `IEEEkeywords` bloklari teknik olarak mevcut.
- Duzeltildi: gereksiz `\IEEEpubid` kaldirildi, abstract icindeki math tabanli ifade duz yaziya cevrildi, keyword listesi alanla uyumlu hale getirildi, gercek makale basligi yerlestirildi, tum yazarlar ve affiliation bilgileri girildi, yazar e-posta adresleri eklendi, Fatih D\"onmez corresponding author olarak belirtildi, running head cok yazarli yapiya uyarlandi.
- Eksik / duzeltilecek: varsa IEEE membership bilgileri, ek ORCID bilgileri, ve istenirse daha resmi journal running head metni.

## Madde Bazli Kontrol

- [x] Baslik `\title{...}` ile tanimli.
  Kanit: [bare_jrnl_new_sample4.tex#L20](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L20)
  Not: repo icindeki `oisac_frontmatter.tex` taslagiyla uyumlu gercek baslik yerlestirildi.

- [x] Baslikta mumkunse matematik veya kimyasal formul kullanilmamis.
  Kanit: [bare_jrnl_new_sample4.tex#L20](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L20)

- [x] Yazar blogu `\author{...}` icinde kurulu.
  Kanit: [bare_jrnl_new_sample4.tex#L22](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L22)
  Not: ilk uc yazar girildi.

- [x] IEEE uyelik durumu gerekiyorsa `\IEEEmembership{...}` ile belirtilmis.
  Not: su an uyelik bilgisi verilmedi; bu nedenle `\IEEEmembership` eklenmedi. Checklist mantigina gore sorun yok.

- [x] Affiliation / tesekkur satirlari `\thanks{...}` ile verilmis.
  Kanit: [bare_jrnl_new_sample4.tex#L23](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L23), [bare_jrnl_new_sample4.tex#L24](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L24)
  Not: ilk uc yazarin affiliation ve e-posta bilgileri girildi; ORCID su an yalnizca ilk yazar icin mevcut.

- [x] `\author{...}` kapanis suslu parantezi, `\thanks{...}` grubunun sonunda kapatilmis.
  Kanit: [bare_jrnl_new_sample4.tex#L23](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L23)

- [x] Journal formatinda gerekiyorsa `\markboth{...}{...}` tanimli.
  Kanit: [bare_jrnl_new_sample4.tex#L25](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L25), [bare_jrnl_new_sample4.tex#L26](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L26)
  Not: running head artik cok yazarli yapiya uygun.

- [x] Submission asamasinda gerekmiyorsa gereksiz copyright satiri eklenmemis.
  Duzeltme: template `\IEEEpubid` satiri kaldirildi.

- [x] `\maketitle` sonrasinda `abstract` ortami yer aliyor.
  Kanit: [bare_jrnl_new_sample4.tex#L35](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L35), [bare_jrnl_new_sample4.tex#L37](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L37)

- [x] Abstract icinde mumkunse matematik ve kimyasal formulden kacinilmis.
  Duzeltme: `$\mathrm{CRQ}_{\Delta}$` ifadesi duz yaziya cevrildi.
  Kanit: [bare_jrnl_new_sample4.tex#L37](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L37)

- [x] Keyword alani `\begin{IEEEkeywords} ... \end{IEEEkeywords}` ile tanimli.
  Kanit: [bare_jrnl_new_sample4.tex#L45](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L45), [bare_jrnl_new_sample4.tex#L47](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L47)

- [x] Keyword listesi alanla ilgili, tutarli ve tekrar etmeyen terimlerden olusuyor.
  Duzeltme: keyword blogu O-ISAC odakli terimlerle yenilendi.
  Kanit: [bare_jrnl_new_sample4.tex#L42](C:/Users/fdonmez/Documents/githubRepos/manuscript/finalManuscript/bare_jrnl_new_sample4.tex#L42)

- [ ] Front matter tek parca, derli toplu ve IEEEtran semasina uygun.
  Genel durum: teknik iskelet buyuk oranda temiz; kalanlar istege bagli metadata detaylari.

## Oncelikli Duzeltmeler

1. Varsa IEEE membership veya ek ORCID bilgilerini ekle.
2. Istenirse running head metnini daha resmi journal formuna getir.

## Benden Hazir Olanlar

- Keyword listesi icin onerili taslak uygulandi.
- Abstract icindeki math ifade IEEE-uyumlu duz yaziya cevrildi.
- `\IEEEpubid` satiri kaldirildi.

## Senden Bilgi Gerektirenler

- Varsa IEEE membership unvanlari
- Varsa Ahmet Altuncu ve Mustafa Namdar icin ORCID bilgileri
