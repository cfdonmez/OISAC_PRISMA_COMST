# O-ISAC COMST

Güncel GitHub dalı: **[`rev/flow-20260916`](https://github.com/cfdonmez/OISAC_PRISMA_COMST/tree/rev/flow-20260916)**.
Okuma kopyası: [flow.pdf](output/pdf/flow.pdf), **20 sayfa**.
Ayrıntılı bilimsel profiller: [profiles.pdf](output/pdf/profiles.pdf).

[Eski–yeni karşılaştırma](compare.md) · [Önceki sürüm](archive/base.zip) ·
[Metin farkı](archive/text.diff)

Yeni görevde önce [AGENTS.md](AGENTS.md), [handoff/state.md](handoff/state.md)
ve [handoff/index.md](handoff/index.md) okunmalı. Referans sürüm `0d5d6f8`,
`rev/comst-v3-20260906` dalındadır. Bütün-makale revizyonu 16 Eylül'de
tamamlandı; güncel dal 30 Eylül 2026'da GitHub'a aktarıldı.

## Diğer bilgisayarda devam

Yeni bir klasöre indirmek için (Git gerekir; `OISAC` klasörü mevcut olmamalı):

```sh
git clone --single-branch --branch rev/flow-20260916 https://github.com/cfdonmez/OISAC_PRISMA_COMST.git OISAC
cd OISAC
python handoff/verify.py
```

Bütünlük kontrolü Python 3.9+ ve standart kütüphane kullanır; ek paket veya
LaTeX kurulumu gerekmez. `PASS` sonrasında hazır PDF'ler okunabilir.

Önceki dalı zaten indirdiyseniz, mevcut repo kökünde `git status` ile başlayın.
Yerel değişiklik varsa önce koruyun; aşağıdaki geçiş temiz çalışma ağacı içindir:

```sh
git remote set-branches --add origin rev/flow-20260916
git fetch origin
git switch --track origin/rev/flow-20260916
git pull --ff-only origin rev/flow-20260916
python handoff/verify.py
```

Yerel `rev/flow-20260916` dalı zaten varsa `git switch --track ...` yerine
`git switch rev/flow-20260916` kullanın. Açılan dal `main` veya eski V3 dalı
değil, `rev/flow-20260916` olmalıdır.

Klasörü Codex'te açıp şu mesajla başlayın:

> AGENTS.md, handoff/state.md ve handoff/index.md dosyalarını oku. Güncel dalı
> ve handoff/verify.py sonucunu kontrol et. compare.md ile güncel yazım
> kararlarından yararlanarak tamamlanan değişiklikleri, korunacak bilimsel
> sınırları ve açık işleri kısa özetle. Güncel okuma kopyası flow.pdf;
> eski reçetelerdeki bölüm numaralarını güncel yapı sanma. Önce durum özeti
> ver, ardından benim yönlendirmemle devam edelim.

## Derleme

TeX Live / MiKTeX, IEEEtran, pdfLaTeX, BibTeX ve latexmk gerekir.
`manuscript/` içinde:

```sh
latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

`supplement/` içinde aynı komutu `driver.tex` için çalıştırın. Derleme sırasıyla
`manuscript/main.pdf` ve `supplement/driver.pdf` üretir; kayıtlı okuma kopyalarını
otomatik değiştirmez. `output/pdf/flow.pdf` veya `output/pdf/profiles.pdf`
güncellenecekse kaynak, görsel QA ve hash kayıtları da yeni çıktıyla eşleştirilir.
Hazır vektör figürler normal derleme için yeterlidir; şekil üreticisini
çalıştırmak gerekmez.

Repo kökünde `python handoff/verify.py`, frozen kaynakları, canlı derleme
girdilerini, güncel PDF hash'ini ve etkin dosya bağlantılarını kontrol eder.

## Bilimsel kayıt ve devamlılık

Ana metin sekiz bölümdür; yöntem özeti Introduction I-C'dedir. Detaylı yöntem,
rapor/çalışma listeleri, kaynak kayıtları ve TQAF kuralları
[supplement/index.md](supplement/index.md) üzerinden bulunur.
206 çalışma / 227 rapor tabanı ve frozen v10 değişmedi.

Proje reçeteleri, karşılaştırma haritaları, kararlar ve tarihsel memory bank
devir rehberinde korunur. Global Codex ayarları, kimlik bilgileri, tarayıcı
profilleri, ham sohbet kayıtları ve yayıncı tam metinleri eklenmez.

OSF güncellemesi ayrı ortak iştir. Güncel çalışma yazarın bilimsel okuması
için hazırlanmıştır; teknik kontroller gönderim onayı sayılmaz.
