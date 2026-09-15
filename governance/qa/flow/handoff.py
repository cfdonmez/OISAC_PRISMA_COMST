"""Refresh the project handoff after the whole-manuscript revision."""
from pathlib import Path
import json, subprocess
root=Path(__file__).resolve().parents[3]
q=json.loads((root/'governance/qa/flow/result.json').read_text())
pages=q['pdfs']['flow']['pages']
sha=q['pdfs']['flow']['sha256']
state=f'''# Güncel durum — 16 Eylül 2026

## Nerede kaldık?

Tüm makale, yazarın 16 Eylül talimatıyla fiziksel paylaşım → tasarım değişkeni →
iki işlevin sonucu → doğrulama → uygulama → araştırma sorusu akışında yeniden
işlendi. Çalışma dalı **`rev/flow-20260916`**; bu dal henüz yereldir.
Güncel okuma kopyası [flow.pdf](../output/pdf/flow.pdf), **{pages} sayfa**.
[Karşılaştırma](../compare.md), [metin farkı](../archive/text.diff) ve
[önceki sürüm arşivi](../archive/base.zip) birlikte korunur. Referans commit
`0d5d6f869336266fde80d8e9ad829108c29b1c7e`; önceki dal değiştirilmedi.

| Bölüm | Güncel görev |
|---|---|
| I — Introduction | Motivasyon, önceki survey'ler, kısa I-C yöntemi ve teknik katkılar |
| II — Technical Foundations of O-ISAC | Sinyal yolu, paylaşım, ölçüm anlamı ve ortak çalışma noktası |
| III — Optical Platforms and Architecture Choices | Fiziksel yolun mümkün kıldığı tasarım tercihleri |
| IV — Shared Design Choices and Joint Performance | Kaynak/zaman, güç, geometri ve işleme değişikliklerinin iki çıktıya etkisi |
| V — Joint Validation Under Realistic Conditions | Deney ortamı, iki işlevde saha kanıtı, deneyin yeniden kurulması |
| VI — Application Requirements and Network Operation | Trafik, hareket, kestirim yaşı, öğrenme ve ağ işletimi |
| VII — Research Questions and Evaluation Priorities | Kanıttan türetilen beş sınanabilir soru ve incelemenin sınırları |
| VIII — Conclusion | Koşullara bağlı mühendislik bulgusu ve bundan sonraki deneyler |

Dosya numaraları tarihsel kaldı; gerçek sıralama
[MANUSCRIPT_BODY_INPUTS.tex](../manuscript/MANUSCRIPT_BODY_INPUTS.tex) içindedir.
Eski ayrı yöntem bölümü geri gelmedi. I-C kısa kaldı; işlem geçmişi ve cover-letter
anlatısı ana metne girmedi.

## Şekiller, tablolar ve supplement

Makale 5 şekil ve 7 tablo içeriyor. Seçim akışı Fig. 1 olarak korunur.
Fig. 2–5 sırasıyla `paths`, `sharing`, `coupling`, `validation` dosyalarıdır:
gömülü yazı tipleri olan PDF ve düzenlenebilir SVG, raster nesne yok.
En küçük şekil metni 7.5 pt; eski varlıklar arşivde ve Git geçmişinde korunur.

Ayrıntılı metrik/ilişki, TQAF, yöntem, teknoloji ve uygulama profilleri
[profiles.pdf](../output/pdf/profiles.pdf) içindedir. Kaynakları
`supplement/driver.tex`, `core.tex`, `late.tex`; bilimsel yöntem anlatısı
[methods.md](../supplement/methods.md), tüm taşıyıcılar
[index.md](../supplement/index.md) üzerinden erişilir.

## Korunan bilimsel sınırlar

227 rapor / 206 çalışma; 4,779 metrik; 404 tradeoff kaydının 402'si substantive.
118 kayıt koşullu karşılaştırma adayıdır, doğrulanmış bağımsız çalışmalar arası
karşılaştırma değildir. Sayımların ayrıntısı supplement'tedir.
12 saha/deployment çalışmasının altısı iki işlevde de o düzeyde çıktı raporlar;
bu sayılar eşzamanlı ortak çalışmayı kanıtlamaz. TQAF incelemeye özgüdür ve
bağımsız doğrulanmış değildir. Frozen `supplement/v10` dosyaları değişmedi.

SCR00057 güç süpürmesi iletişim launch gücünü sabit tutar; toplam güç sabit
değildir. Ayrı pre-compensation kazancı 2.4 dB'dir. SCR00083'te alıcı
konfigürasyonları, sweep/occupied bandwidth ve çözünürlük/hata ayrıdır.
SCR00007 pilot hatası hedef-konum hatası değildir. VI'daki kestirim yaşı ve
hareket açısı denklemleri açık varsayımlı öğretici kinematiktir; corpus verisine
fit edilmiş sonuç değildir.

## Kontrol ve açık işler

[QA](../governance/qa/flow/result.json): temiz kaynak/atıf/bağlantı kontrolleri;
son makale SHA-256 `{sha}`. Bütün sayfa incelemesi
`governance/qa/flow/paper/visual_checks.json` ile aynı hash'e bağlanır.
`python handoff/verify.py` frozen taşıyıcıları ve güncel PDF hash'ini denetler.

1. Yazar bu sürümü okuyacak; teknik QA, yazarın bilimsel onayı değildir.
2. OSF güncellemesi önceden kararlaştırılan ayrı ortak iştir. Makaledeki
   yazar-onaylı final-state arşiv cümlesi uzaktaki güncellemeyi kanıtlamaz.
3. Güncel raporlama-konumu haritası [flow.md](../governance/flow.md) içindedir;
   tamamlanmış bağımsız PRISMA checklist diye sunulmaz.
4. GitHub'a bu yeni dalın aktarılması ayrı adımdır. Eski dal/commit arşiv
   referansıdır; ham sohbetler veya global Codex ayarları bu pakete alınmadı.
5. Tarihsel COMST031 metadata sorunu bu revizyonda yeni bir corpus taramasına
   dönüştürülmedi.
'''
(root/'handoff/state.md').write_bytes(state.encode('utf-8'))
readme=f'''# O-ISAC COMST

Güncel yerel dal: **`rev/flow-20260916`**.
Okuma kopyası: [flow.pdf](output/pdf/flow.pdf), **{pages} sayfa**.
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
'''
(root/'README.md').write_bytes(readme.encode('utf-8'))
p=root/'README_V3_WORKING_DRAFT.md'
p.write_bytes(('''# O-ISAC COMST working draft

Current local branch: `rev/flow-20260916`; comparison baseline: `0d5d6f8`.
The whole-manuscript revision is described in [compare.md](compare.md).
Read [flow.pdf](output/pdf/flow.pdf) and the supplementary
[profiles.pdf](output/pdf/profiles.pdf). The current structure, checks and
open work are maintained in [handoff/state.md](handoff/state.md).

The 16 September author instructions authorize the complete revision,
including new vector figures. Older figure-only or section-only restrictions
do not define this task. Scientific source conditions, frozen evidence,
the cover-letter boundary and the separate joint OSF task remain in force.
''').encode('utf-8'))
p=root/'handoff/index.md'
s=p.read_text(encoding='utf-8').replace('[review.pdf](../output/pdf/review.pdf)','[flow.pdf](../output/pdf/flow.pdf)')
s=s.replace('14 Eylül yöntem yerleşimi ve en son yazar talimatı esas alınır.',
'16 Eylül bütün-makale revizyonu ve en son yazar talimatı esas alınır.')
s=s.replace('güncel okuma kopyası yalnız `review.pdf` olarak belirtilmiştir.',
'güncel okuma kopyası `flow.pdf` olarak belirtilmiştir. Eski `review.pdf` referans sürümdür.')
s=s.replace('| Güncel makale / okuma kopyası |','| Güncel makale / okuma kopyası |',1)
if '| Bütün-makale revizyonu' not in s:
    s=s.replace('| V3 reçeteleri,', '| Bütün-makale revizyonu ve karşılaştırma | [compare.md](../compare.md), [flow.md](../governance/flow.md), [base.zip](../archive/base.zip) |\n| V3 reçeteleri,')
p.write_bytes(s.encode('utf-8'))
p=root/'governance/review.md'
s=p.read_text(encoding='utf-8')
notice='''> Historical implementation record: 14 September 2026. Current section,
> figure and reporting locations are in [flow.md](flow.md); the current reading
> copy is [flow.pdf](../output/pdf/flow.pdf). The locations and QA below describe
> the preserved 29-page baseline, not the later revision.

'''
if not s.startswith('> Historical implementation record:'):
    p.write_bytes((notice+s).encode('utf-8'))
patch=subprocess.check_output(['git','diff','0d5d6f8','--','manuscript/sections','manuscript/main.tex','manuscript/MANUSCRIPT_BODY_INPUTS.tex'],cwd=root)
(root/'archive/text.diff').write_bytes(patch)
print('Updated current handoff and baseline-to-current text diff.')
