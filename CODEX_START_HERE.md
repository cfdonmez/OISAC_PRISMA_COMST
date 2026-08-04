# Codex Start Here

## 2026-08-04 corpus override

Before using the older onboarding instructions below, read:

1. `memory-bank/full_corpus_206_source_of_truth_2026-08-04.md`
2. `memory-bank/activeContext.md`
3. `review_package/full_corpus_206_20260804/00_SOURCE_OF_TRUTH.md` when present

The current corpus is 227 included reports mapped to 206 studies, not 220/221. Phases D--F are complete: 8,306 governed claims, 8,203 primary synthesis claims, 206 TQAF rows, and finalized S1--S7 outputs. Phase G reviewed manuscript integration is current. The full-corpus process is investigator-supervised and AI-assisted; independent human verification is not documented. Do not overwrite dirty files under `manuscript/finalManuscript/`, and do not mechanically replace corpus numbers in old prose, figures or citation keys.

---

Bu dosya, repo icinde yeni bir Codex oturumu acildiginda en hizli ve en guvenli onboarding giris noktasidir.

Amac:
- kaldigimiz yeri hizla anlamak
- onceki calismalari tekrar etmemek
- aktif LaTeX manuscript zincirine dogru dosyadan girmek
- yeni edit oncesi archive ve is disiplini kurallarini korumak

## Kullanim

Yeni bir Codex oturumunda ilk mesaj olarak su yonlendirme yeterlidir:

```text
Bu repoda ise baslamadan once CODEX_START_HERE.md dosyasindaki onboarding promptunu uygula. Once durumu cikar, sonra bana nerede kaldigimizi ve simdi en dogru sonraki adimi soyle.
```

Istersen dogrudan asagidaki detayli prompt da yeni Codex'e verilebilir.

---

## Detailed Onboarding Prompt

```text
Bu repo icinde O-ISAC manuscript'i IEEE Photonics Journal hedefiyle review article olarak native LaTeX formatina tasiyoruz.

Oncelik:
- once mevcut durumu dogru anla
- sonra kaldigimiz yerden devam et
- ayni isi tekrar yapma
- yeni bir editten once mutlaka archive al

Ilk okuma sirasi:
1. memory-bank/activeContext.md
2. memory-bank/UPDATE_SUMMARY.md
3. memory-bank/latex_native_bibtex_transition_2026-03-24.md
4. memory-bank/techContext.md
5. memory-bank/journal_target_ieee_photonics_journal.md

Sonra aktif manuscript calisma alanini incele:
- manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/oisac_review_working.tex
- manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/oisac_frontmatter.tex
- manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/build_oisac_review_working.ps1
- manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/references.bib
- manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/sections/
- manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/oisac_review_working_build_20260324_214338.pdf

Calismayi su kabullerle ele al:
- manuscript artik survey degil, review/systematic review framing'indedir
- hedef dergi IEEE Photonics Journal'dir
- aktif authoring merkezi markdown bundle degil, native LaTeX template klasorudur
- native section migration Section I-IX icin tamamlanmistir
- BibTeX zinciri aktiftir
- son dogrulanan compile 32 sayfadir
- ana acik konular: page-budget reduction, float/layout cleanup, frontmatter, impact statement, graphical abstract brief
- buyuk islerde subagent metoduyla section-bazli veya gorev-bazli paralel ilerle
- kullanici ozellikle archive disiplinini onemsiyor; dosya editinden once legacy_archive altina snapshot al

Ek davranis kurallari:
- once memory-bank ve aktif LaTeX dosyalarini oku, sonra yorum yap
- eger yeni bir degisiklik yapacaksan once mevcut build/output ve ilgili section dosyasini kontrol et
- placeholder veya eski markdown kalintisi gorursen bunu once teyit et, sonra temizle
- journal-fit kararlarinda “compile oluyor” ile yetinme; sayfa butcesi ve submission gercekligini de dikkate al

Okumayi bitirdikten sonra bana sadece su 4 baslikta kisa ama net durum raporu ver:
1. Nerede kaldik
2. Neler tamamlandi
3. Hangi riskler ve acik isler var
4. Simdi en dogru sonraki adim ne

Bu rapordan sonra benim yonlendirmemi bekle veya eger talebim aciksa dogrudan uygulamaya gec.
```

---

## Fast Context Snapshot

- Hedef dergi: IEEE Photonics Journal
- Manuscript kimligi: review / systematic review
- Aktif authoring merkezi: `manuscript/IEEE-Transactions-LaTeX2e-templates-and-instructions/`
- Ana dosya: `oisac_review_working.tex`
- Cite/BibTeX zinciri aktif
- Son dogrulanan PDF: `oisac_review_working_build_20260324_214338.pdf`
- Son dogrulanan sayfa sayisi: `32`
- Ana acik isler:
  - kisaltma
  - float/layout cleanup
  - frontmatter
  - impact statement
  - graphical abstract brief

## Not

Bu dosya yeni Codex icin “ilk adres” olarak tasarlandi. En dogru kullanim, yeni oturumda once bu dosyayi okutup sonra detayli promptu uygulatmaktir.
