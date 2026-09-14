# Karşılaştırma ve Ana Metin Seçim Planı — Tam Revizyon

## Analiz sırası

1. Kaynak-doğrulanmış 118-row envanter.
2. Study/report/condition düzeyinde deduplication.
3. Ortak metric definition, plane, task, unit, baseline ve condition taşıyan
   comparison groups.
4. Within-study operating-point comparisons.
5. Gerçekten hizalanan gruplarda bounded cross-study comparison.
6. Heterojen gruplarda explicit non-pooling reason.

Varsayılan çıktı universal rank veya meta-analysis değildir. Direction ve
magnitude yalnız support eden source contract içinde yorumlanır.

## Comparison group minimum sözleşmesi

`modality + metric definition/family + exact unit + measurement plane + task +
validation type + scenario/condition + baseline role`

Bir alan eşleşmiyorsa group bölünür veya `non_poolable` olur. Fiziksel olarak
eşdeğer görünen unit'ler otomatik normalize edilmez.

## Ana metin anchor protokolü

Ana metinde 12--20 condition-complete tuple hedeflenir. Seçim sonuç yazılmadan
önce şu coverage testine bağlıdır:

- en az dört ana modality, kanıt izin veriyorsa;
- communication, sensing, joint ve implementation sonuç sınıfları;
- en az üç gerçek bounded comparison group, veri izin veriyorsa;
- en az 8/15 included study'den temsil;
- laboratory/model/field validation farklılıkları;
- olumlu performans yanında constraint/degradation örnekleri;
- bütün 118 kayıt supplementte;
- her dışlama/non-pooling gerekçesi kayıtlı.

Her tuple şu yedi soruyu yanıtlar:

1. Hangi yöntem veya konfigürasyon?
2. Hangi koşulda?
3. Hangi baseline'a karşı?
4. Hangi sonuç ve unit?
5. Ne kadar/yönde değişti?
6. Hangi validation düzeyinde?
7. Hangi sınırla yorumlanabilir?

## Üretilecek analiz dosyaları

- `COMPARISON_GROUP_CATALOG.csv`
- `STUDY_CONDITION_MATRIX.csv`
- `NONPOOLING_DECISIONS.csv`
- `MAIN_TEXT_ANCHORS.csv`
- `MAIN_TEXT_EVIDENCE_CROSSWALK.csv`
- `ROADMAP_EVIDENCE_TRACE.csv`

