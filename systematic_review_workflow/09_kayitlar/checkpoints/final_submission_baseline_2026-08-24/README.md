# Final Submission Baseline — 2026-08-24

## Amaç

Bu checkpoint, bütün manuscript dili yeniden denetlenmeden ve sekiz ana metin
şekli üretilmeden önceki kullanıcı onaylı güvenlik tabanını kaydeder. Mevcut
LaTeX kaynakları ve PDF bu noktada değiştirilmemiştir.

## Git kurtarma ve koruma

- Çalışma klasöründeki `.git` dizini bulunduğunda boştu.
- Uzak depo `https://github.com/cfdonmez/OISAC_PRISMA_COMST.git` olarak
  doğrulandı.
- Kayıtlı teslim dalı `agent/full-corpus-survey-ready` ve başı
  `9b29b221213786c9893134a36638c3d9a0739f49` olarak doğrulandı.
- Boş `.git` dizini çalışma klasörünün dışındaki
  `C:/Users/fdonmez/Gdri/OISAC/git_metadata_backups/prisma2020Review_empty_git_20260824`
  konumuna taşındı.
- Git metadatası yalnız nesne ve geçmiş bilgisi içeren kısmi klondan geri
  bağlandı. Mevcut proje dosyalarının hiçbiri klondan kopyalanmadı veya üzerine
  yazılmadı.
- Finalizasyon dalı `codex/final-submission-20260824` adıyla önceki teslim
  başından ayrıldı. Böylece eski uzak dal değişmeden korunur.

## Değişiklik öncesi manuscript tabanı

- Aktif proje
  `systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`
  dizinidir.
- `main.pdf` 23 sayfa ve 203,407 byte'tır.
- PDF SHA-256 değeri
  `A258E699084D190186298EA95D279E459A75D5F9B9881EC2EF9DC03F505C5E35` olarak
  doğrulandı.
- `main.bbl` içinde 241 kaynak girdisi vardır.
- Sekiz tablo canlıdır. Sekiz ana metin şekli bu tabanda henüz üretilmemiştir.
- Son derleme denetiminde undefined citation, undefined reference, changed
  label, overfull box, oversized float ve fatal error sayıları sıfırdır.

## GitHub güvenlik paketinin kapsamı

İlk güvenlik commit'i aktif manuscript kaynaklarını, derlenmiş PDF'yi,
bibliyografyayı, manuscript QA kayıtlarını, güncel supplement kaynaklarını ve
projenin current-state, progress, decision-log ve memory-bank dosyalarını
taşır. Yerel çalışma ağacındaki türetilmiş render klasörleri, geçici dosyalar ve
GitHub'ın 100 MB tek dosya sınırını aşan `.inspect.ndjson` çıktıları bu güvenlik
commit'ine alınmaz. Bu dosyalar yerel diskte değişmeden korunur ve kanonik
bilimsel girdilerin yerine geçmez.

## Kilitli finalizasyon sırası

1. Başlangıç tabanını commit edip GitHub'a gönder.
2. Tüm manuscript boyunca akış, tekrar, kısaltma, tire, olumsuzluk, savunmacı
   ifade ve tamamlanmamış süreç dili denetimi yap.
3. Sections IV ve V'te onaylanan survey tonunu bütün bölümlere uygula.
4. Denominator, citation ve evidence sınırlarını yeniden doğrula.
5. Sekiz şekli yalnız izlenebilir veri ve düzenlenebilir vektör kaynaklarla
   üret. Üretken görsel sistemi kullanma.
6. Figure-inclusive derleme, tam PDF render denetimi ve son GitHub teslimini
   tamamla.

## Uzak güvenlik noktası

- Baseline commit
  `64a3dc2c5371c1aa7a4d61a595a1df3ed26c3b03` olarak oluşturuldu ve
  `origin/codex/final-submission-20260824` dalına başarıyla gönderildi.
- GitHub dalı
  `https://github.com/cfdonmez/OISAC_PRISMA_COMST/tree/codex/final-submission-20260824`
  konumundadır.
- Bundan sonraki manuscript değişiklikleri bu doğrulanmış uzak güvenlik
  noktasının üzerine ayrı commitler olarak eklenecektir.
- Final commit kimliği, figure-inclusive closeout tamamlandığında bu dosyaya
  eklenecektir.

## Figure-inclusive closeout sonucu

- Final yerel aday 2026-08-25 tarihinde tamamlandı.
- `main.pdf` 27 sayfa, 598,488 byte, sekiz şekil, sekiz tablo ve 241 kaynak
  girdisi içerir.
- Final PDF SHA-256 değeri
  `6A195C6856E5BD784DEF0A5149B1DF025771E5E50D7B2C02A7D229108B450DC2` olarak
  doğrulandı.
- Figures 1--8 düzenlenebilir SVG ve vektör PDF olarak deterministik biçimde
  üretildi. Üretken görsel veya dış sanat eseri kullanılmadı.
- Tam dil, akış, tekrar, kısaltma, iddia ve olumlu anlatım denetimi tamamlandı.
- Derleme ve 27 sayfalık görsel QA geçti. Governing record
  `checkpoints/comst_final_submission_closeout_2026-08-25/README.md` ve
  manuscript QA `qa/FINAL_SUBMISSION_QA_2026-08-25.md` dosyalarıdır.
- Focused final content commit
  `564d0fa866c22114affbffd08e149b9260a60aaf` olarak oluşturuldu ve
  `origin/codex/final-submission-20260824` dalına gönderildi. Uzak dal başı aynı
  hash ile doğrulandı.
