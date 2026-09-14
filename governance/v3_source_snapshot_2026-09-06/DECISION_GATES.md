# Go/No-Go Kapıları — Tam Revizyon

V3-S1, mevcut Phase G `G0`–`G10` zincirini yeniden numaralandırmayan bir V3
ön-kapısıdır. Yalnızca yeni makale mimarisinin bilimsel çekirdeğini kilitler;
makine-okunur durumu ayrı `../04_qa/V3_QA_GATE_REGISTER.csv` dosyasında izlenir.

| Gate | PASS ölçütü | FAIL sonucu |
|---|---|---|
| V3-S1 Scientific core lock | Kanonik merkezî soru, J tanımı, temel jointness kararı ve aynı payload hash'i bütün yazarlarca onaylı; S1-01–S1-08 testleri PASS | Architecture Lock başlamaz; ilişkilendirme haritası candidate olarak kalır |
| G0 Input freeze | Source ZIP/PDF hash eşleşir; temiz build 27 sayfa; Phase A--F hash'leri kayıtlı | Çalışma durur |
| G1 Amendment lock | Korpus değişmediği, 118/15/16 kapsamı, overlay-only ve non-pooling varsayımı onaylı | Verification başlamaz |
| G2 Pilot | Farklı modality/metric sınıflarından 12 kayıt çift review; kritik value/unit/locator anlaşması >=90%; bütün farklar çözümlü | Protokol düzeltilir ve pilot tekrarlanır |
| G3 Report packets | 16/16 rapor identity/path/hash ve row mapping tamam | İlgili report paketi review'a açılmaz |
| G4 Double verification | 118/118 x 2 review tamam; AI insan reviewer değildir | Analysis başlamaz |
| G5 Adjudication lock | 0 unresolved; corrected/rejected kayıtlar overlay'de; companion duplication yok | G3 lock verilmez |
| G6 Analysis lock | Comparison groups, independence ve non-pooling kararları onaylı; pseudo-replication yok | Carrier üretimi durur |
| G7 Carrier approval | Main-text anchor selection önceden tanımlı coverage testini geçer; her sayı crosswalk'li | Manuscript yazımı geri döner |
| G8 Scientific content | IV--VIII lessons/decision chain ve beş adet sekiz-alan roadmap tam | Candidate build release'e ilerlemez |
| G9 Supplement | 118-row atlas, reviewer/adjudication, group ve errata dosyaları tam; schema/hash QA PASS | RC üretilmez |
| G10 COMST/release | Clean build, <=30 sayfa, render/reader/scientific QA, bütün yazar onayı, immutable hashes | Submission yapılmaz |
