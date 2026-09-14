# Introduction ve Table I: numaralı atıf düzeni

7 Eylül 2026. Kullanıcının tercihiyle yalnız V3 Introduction düzenlendi.

- Metindeki yazar adı ve et al. ifadeleri kaldırıldı. Cümleler çalışmanın
  konusu/yaklaşımı etrafında kuruldu; her iddianın cite anahtarı korundu.
- Table I ilk sütunu Ref. / year oldu; satırlar cite ile üretilen [n] (yıl)
  biçiminde. Yıllar, satır sırası, işaretler ve bilimsel hükümler aynı.
- Tablo dipnotundaki yazar adı da numaralı atfa dönüştürüldü.
- Tablo sonrası iki ayrı kaynak iddiası kendi atıflarıyla eşleştirildi.
- Kaynakça, IEEEtran, diğer bölümler, görsel ve katkılar değiştirilmedi.

IEEE Reference Guide, metinde yazar adı ve et al. kullanımına izin verir.
Dolayısıyla bu değişiklik yasak bir atıf biçimini düzeltme iddiası değil,
kullanıcının istediği tutarlı, yalnız numaralı metin ve tablo atfıdır.
Resmi kaynak: https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE_Reference_Guide.pdf

Önceki giriş: section1_before_numeric_citations_2026-09-07.tex.
Önceki SHA-256: 7824193A8DA784C056999C83076950EE14CDF113AA37205D5CE9D8BA3AB3E82F

Kontroller: 16 kaynak dosyasında yalnız Introduction değişti. Görünür yazar
adı/et al. eşleşmesi sıfır; 17 farklı cite anahtarı korundu. Scope and
Contributions önceki dosyayla birebir aynı. latexmk ve git diff --check geçti.
Final logda undefined reference, LaTeX Warning, Overfull veya Missing character
yok. PDF 27 sayfa; 1-4. sayfalar görüntülenerek kontrol edildi. Table I sayfa 3.

Çıktı: output/pdf/OISAC_COMST_V3_INTRO_NUMERIC_CITATIONS_2026-09-07.pdf
