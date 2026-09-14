# Revizyon Planları QA Raporu

Tarih: 2026-09-01  
Sonuç: `PASS_PLAN_STRUCTURE_AND_BASELINE_INTEGRITY`

## Yapı

- Toplam plan dosyası: 38 (bu QA raporu eklenmeden önceki sayım).
- Dengeli ağaç: 15 dosya.
- Tam ağaç: 21 dosya.
- Kök karşılaştırma/navigasyon: 2 dosya.
- Her iki ağaç governance, evidence/verification, manuscript, QA, management ve
  output sözleşmelerini kendi içinde taşır.

## Baseline doğrulaması

- Her iki `BASELINE_MANIFEST.tsv`: 10/10 path mevcut.
- Byte ve SHA-256 uyuşmazlığı: 0.
- Active `main.tex` SHA-256:
  `03216078BA9D26AB64E3F3CDBED529EB1753DC6F3F0EA48F6EB25D396F7FEC23`.
- Active `MANUSCRIPT_BODY_INPUTS.tex` SHA-256:
  `704CCB968C660CA88C1F04ECD48C1DB0096AF234F153043DD7FCE0D7710B8B49`.
- Active `main.pdf` SHA-256:
  `6A195C6856E5BD784DEF0A5149B1DF025771E5E50D7B2C02A7D229108B450DC2`.
- Plan yazımı sonrasında bu üç active kaynak hash'i değişmedi.

## Evidence register doğrulaması

- Dengeli çekirdek aday: 11 satır, 11 benzersiz metric ID.
- Kaynak `ST-19` içinde bulunmayan dengeli çekirdek ID: 0.
- Tam register: 118 satır, 118 benzersiz metric ID.
- Tam register study cluster: 15.
- Tam register source report: 16.
- Kaynak 118-ID setine göre missing: 0; extra: 0.
- Tam register'daki bütün satırlar `candidate_not_reverified`; plan hiçbirine
  insan doğrulaması atfetmiyor.

## Format doğrulaması

- 15 CSV dosyasının tamamı parse edildi.
- CSV parse failure: 0.
- Boş şablon CSV'ler header-only olarak bilinçli bırakıldı.
- Balanced QA gate rows: 9.
- Full QA gate rows: 11.

## Koruma sınırı

- Active manuscript'e edit uygulanmadı.
- Phase A--F artefact'ları değiştirilmedi.
- Git branch/worktree oluşturulmadı.
- Publisher PDF kopyalanmadı.
- LaTeX build çalıştırılmadı; bu rapor plan QA'sıdır, revize-manuscript QA'sı
  değildir.

