# Go/No-Go Kapıları — Dengeli Revizyon

| Gate | Kontrol | PASS ölçütü | FAIL sonucu |
|---|---|---|---|
| G0 Baseline | Gönderilmiş kaynak ve PDF dondurma | Manifest hash'leri eşleşir; temiz build 27 sayfayı yeniden üretir | Çalışma başlamaz; gerçek gönderim kaynağı belirlenir |
| G1 Selection lock | 118 adaydan seçim kuralı | Inclusion/exclusion, strata, stop rule ve bütün dışlama nedenleri sonuç yazımından önce kilitli | Seçim yeniden tasarlanır; sayı yazılmaz |
| G2 Source manifest | Seçilen raporların kaynağı | Her raporda ID, DOI/title, güvenli yerel yol, PDF SHA-256 ve erişim durumu var | İlgili kayıt çıkarılır veya yedek aday seçilir |
| G3 Dual verification | İki bağımsız insan okuması | En az 30 kayıt iki insan tarafından doğrulanmış; 0 çözümsüz uyuşmazlık | Dengeli plan NO-GO veya kontrollü minimum pakete düşer |
| G4 Evidence lock | Kart ve matris üretimi | Her hücre metric ID, study/report ID, koşul, baseline, unit ve source locator taşır | Hücre ana metne alınmaz |
| G5 Manuscript utility | Lessons ve roadmap | IV--VII kapanışları tam; beş roadmap satırı sekiz alanı taşıyor | Bölüm revizyonu geri döner |
| G6 COMST build | Derleme ve sayfa | Temiz build; undefined citation/reference yok; PDF <=30 sayfa | Yeni içerik durur, tekrar/supplement ayrımı düzeltilir |
| G7 Render and reader | Görsel ve okuyucu testi | Tüm sayfalar okunur; okuyucu beş sorunun en az dördünü ana metinden yanıtlar | Candidate release edilmez |
| G8 Author release | Bilimsel ve editoryal onay | Tüm yazarlar onaylar; source/PDF/manifest hash'lenir | Submission yapılmaz |

Reader-value soruları:

1. Hangi yaklaşım hangi koşulda ne başardı?
2. Neye karşı kıyaslandı?
3. Sonuç hangi modality/validation setting dışına taşınamaz?
4. Bir O-ISAC araştırmacısı hangi benchmark veya deneyi kurmalı?
5. Başarı hangi ölçütle değerlendirilmeli?

