# O-ISAC COMST V3

Güncel çalışma dalı: `rev/comst-v3-20260906`.

**Yeni bilgisayarda başlangıç:** [durum özeti](handoff/state.md),
[dosya rehberi](handoff/index.md) ve [Codex çalışma kuralları](AGENTS.md).
Son okuma kopyası: [review.pdf](output/pdf/review.pdf), 29 sayfa.

```sh
git clone --single-branch --branch rev/comst-v3-20260906 https://github.com/cfdonmez/OISAC_PRISMA_COMST.git OISAC
cd OISAC
```

Bu klasörü Codex'te proje olarak açıp yeni sohbete şunu yazın:

> AGENTS.md, handoff/state.md ve handoff/index.md dosyalarını oku. Güncel
> dosyaları kontrol ederek nerede kaldığımızı ve açık işleri kısaca özetle.
> Eski reçetelerle güncel kararları ayır; ben yeni görev vermeden makaleyi değiştirme.

Proje kuralları `AGENTS.md` üzerinden yüklenir; ayrıntılı kayıtlar bu dosyanın
yönlendirdiği Markdown dosyalarındadır.
[OpenAI'nin AGENTS.md belgesi](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
bu proje düzeyindeki kullanım biçimini açıklar. Paket, sohbet arayüzünü veya
hesap ayarlarını yeniden kurmaz; araştırma bağlamını okunabilir dosyalarla taşır.

## Pakette bulunanlar

- Güncel makale, bibliyografya, onaylı figürler ve düzenlenebilir kaynakları.
- Son PDF, önceki çalışma sürümleri, yerel revizyon yedekleri ve QA kayıtları.
- Supplement yöntem anlatısı ve bütün frozen v10 kaynak paketi.
- Gerçek proje `codex_memory_bank`, karar/ilerleme günlükleri ve konuya ait
  Codex hafıza özetleri; COMST/P01/P02 analizleri, reçeteler ve bölüm haritaları.
- Güncel durum, açık işler, kaynakların nereden taşındığı ve bütünlük kontrolü.

Ana metin sekiz bölümlüdür. Review Methodology, Introduction I-C içindedir;
ayrıntıları [supplement/methods.md](supplement/methods.md) taşır.
**OSF güncellemesi hâlâ yapılacak ayrı ortak iştir.** GitHub aktarımı bunu tamamlamaz.

## Kontrol ve derleme

Python 3.9 veya üzeri ile, ek Python paketi gerektirmeden:

```sh
python handoff/verify.py
```

TeX Live veya MiKTeX içinde pdfLaTeX, BibTeX, latexmk, IEEEtran ve kullanılan
LaTeX paketleri bulunmalıdır. Ardından:

```sh
cd manuscript
latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

Figürler hazır PDF/PNG olarak geldiği için normal derleme figür üretim
araçlarına ihtiyaç duymaz. Eski figür/QA üretim betiklerinin bağımlılıkları ve
yazma davranışları [dosya rehberinde](handoff/index.md) açıklanmıştır.

Uzun yol sorunlarını azaltmak için kısa bir checkout yolu kullanın
(örneğin `C:\OISAC`). Dalın geçmişi bağımsız V3 baseline'dan başlar;
repo varsayılan `main` dalı farklı tarihsel çalışma ağacıdır.
