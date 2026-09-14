# Dengeli Revizyon Çalışma Ağacı

Durum: `PLAN_READY_EXECUTION_NOT_STARTED`

Bu seçeneğin amacı, mevcut 27 sayfalık survey'i yeniden baştan yazmadan hoca
yorumunun üç ana unsurunu görünür biçimde kapatmaktır:

1. teknik/sayısal sonuçları koşullarıyla göstermek;
2. yalnız sınıflandırma değil, yöntem seçimine yardım eden lessons learned
   üretmek;
3. sonraki çalışmalar için test edilebilir ve başarı ölçütü olan deney
   reçeteleri vermek.

## Somut teslim vaadi

Bu ağaç başarıyla tamamlandığında okuyucu şunları bulacaktır:

- 6--8 koşul-tam operating-point veya bounded-comparison kartı;
- yöntem, fiziksel koşul, baseline, metrik, sonuç, validation ve transfer
  sınırını aynı yerde gösteren kompakt bir teknik tablo;
- Sections IV--VII sonunda `ne öğrendik / ne zaman geçerli / hangi sınır var /
  tasarım kararı nedir` sentezi;
- beş araştırma önceliği için gap, hipotez, deney, baseline, stress değişkeni,
  başarı ölçütü, artifact ve dependency içeren roadmap;
- ana metindeki her yeni sayıyı metric ID ve PDF lokatörüne bağlayan crosswalk.

## Kapsam

- 118 koşullu aday içinden önceden kilitlenen kuralla 34--36 kayıt seçilir.
- Sert alt/üst sınır 30--40 kayıttır.
- Her seçilmiş kayıt iki insan tarafından bağımsız doğrulanır.
- Yaklaşık 11 rapor hedeflenir; rapor başına en fazla dört ek sonuç alınır.
- Fiber, photonics-assisted THz, VLC/LiFi ve FSO için kanıt varsa en az birer
  kart üretilir. Yapay kota uğruna zayıf kayıt alınmaz; boşluk açık yazılır.
- Communication, sensing ve joint/implementation alanları temsil edilir.
- Yeni literatür taraması, meta-analiz ve evrensel yöntem sıralaması yapılmaz.

## İş akışı

`G0 baseline -> seçim protokolü -> rapor manifesti -> Reviewer A ve B ->
adjudication -> evidence lock -> kartlar/matris -> manuscript revizyonu ->
30-sayfa/build/render QA -> bağımsız reader-value testi -> yazar onayı`

WP4 evidence lock tamamlanmadan manuscript'e yeni sayısal değer yazılmaz.

## Bu ağacın dosyaları

- `00_governance/`: kapsam, korunan kaynaklar ve go/no-go kapıları.
- `01_evidence/`: seçim, çift doğrulama ve adjudication planı/formları.
- `02_manuscript/`: bölüm değişiklik haritası ve sayfa bütçesi.
- `03_qa/`: bilimsel, editoryal, build ve reader-value kabul testleri.
- `04_management/`: WBS, takvim, RACI ve risk kaydı.
- `05_outputs/`: tamamlandığında üretilecek teslim paketi.

Tahmini emek 44--52 kişi-saat; iki doğrulayıcı paralel çalışırsa 6 aktif iş
günü, yazar geri bildirimiyle 7--10 takvim günüdür.

