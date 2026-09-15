# O-ISAC COMST

Güncel yerel dal: **`rev/flow-20260916`**.
Okuma kopyası: [flow.pdf](output/pdf/flow.pdf), **20 sayfa**.
Ayrıntılı bilimsel profiller: [profiles.pdf](output/pdf/profiles.pdf).

[Eski–yeni karşılaştırma](compare.md) · [Önceki sürüm](archive/base.zip) ·
[Metin farkı](archive/text.diff)

Yeni görevde önce [AGENTS.md](AGENTS.md), [handoff/state.md](handoff/state.md)
ve [handoff/index.md](handoff/index.md) okunmalı. Referans sürüm `0d5d6f8`,
`rev/comst-v3-20260906` dalındadır. Yeni dalın uzaktaki durumu push yapılmadan
varsayılmamalıdır.

## Derleme

TeX Live / MiKTeX, IEEEtran, pdfLaTeX, BibTeX ve latexmk gerekir.
`manuscript/` içinde:

```sh
latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

`supplement/` içinde aynı komutu `driver.tex` için çalıştırın. Hazır vektör
figürler normal derleme için yeterlidir; şekil üreticisini çalıştırmak gerekmez.

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
