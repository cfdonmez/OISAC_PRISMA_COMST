# Section IV Camera-Ready Notes

Son Guncelleme: 2026-03-10
Kapsam: `drafts/section_04_taxonomy.md` (Section IV-A..E)

---

## Amac

Section IV icin "data-correct but not fully camera-ready tone" durumunu kalici olarak kaydetmek ve polish pass icin net aksiyon listesi vermek.

Bu dosya, metin kalitesini teknik dogruluktan ayri bir kapanis adimi olarak takip eder.

---

## Section II Precedent Kontrolu

Benzer notlama yaklasimi Section II icin zaten mevcut:

- `memory-bank/activeContext.md` icinde:
  - "Section II (Fundamentals) - kalite kapama" blogu
  - Section II finalization/checklist referanslari
- `drafts/section_02_fundamentals_draft.md` sonunda:
  - COMST/PRISMA finalization checklist blogu

Sonuc: Section IV icin memory-bank not acma karari mevcut proje desenine uyumludur.

---

## Mevcut Durum (Section IV)

- Section IV-A..E bolumleri veri-temelli yeniden yazildi.
- Sayisal tutarlilik ve zorunlu kanit entegrasyonu yuksek.
- 2026-03-10 camera-ready prose polish pass uygulandi:
  - ham schema/pipeline etiketleri temizlendi
  - audit kategori adlari publication prose'a cevrildi
  - tablo basliklari ve satir adlari daha COMST-uyumlu hale getirildi
- Kalan is artik yeni veri/yeniden yazi degil; final manuskript entegrasyonu sirasinda kesisen ton ve referans kontroludur.

---

## Kalan Camera-Ready Gozlemleri

1) Cross-manuscript terminology consistency
- Section IV publication prose temizlendi, ancak Introduction / Section VI / Section VII ile ortak terimlerin final manuskript pass'inde yeniden eslenmesi gerekir.
- Etki: ayni kavramin farkli sectionlarda farkli tonla anlatilmasi COMST akisini zayiflatabilir.

2) Figure-caption and text-reference uniformity
- Fig. IV-1 / Fig. IV-2 / Table IV-* atiflari final manuskript yerlesiminde tekrar kontrol edilmelidir.
- Etki: section ici ton temiz olsa da son dizgide caption ve metin dili farklilasabilir.

3) Final release-gate consistency
- Section IV sayilari ve taxonomy etiketleri Section V-VII boyunca ayni corpus state ile konusmali.
- Etki: metodoloji-taksonomi-sonraki section zincirinde corpus drift riski olusabilir.

---

## Polish Pass Aksiyon Plani (Section IV Ozel)

Durum: 2026-03-10 pass'i ile ana polish adimlari uygulanmistir.

1. Terminolojiyi final manuskriptte koru
- `shared front-end`, `separate front-ends`, `structured receiver-detection annotation`

2. Audit isimlerini publication prose olarak koru
- `metric-aliasing`
- `measurement-plane ambiguity`

3. Table/caption dilini final dizgide tekrar kontrol et
- Caption fiilleri: summarizes, shows, provides
- Satir adlari: Title Case ve publication prose

4. Teknik iddialari dondur
- Sayilar, oranlar, branch degerleri, governance denklemleri degismeyecek.
- Sadece presentation ve tone duzeyi guncellenecek.

---

## Camera-Ready Cikis Kriterleri (Section IV)

- Metinde schema/pipeline etiketleri kalmamis olacak.
- Tanimlar ve alt-basliklar COMST tutorial dilinde tutarli olacak.
- Figure/table referanslari aktif fiil + audit edilebilir sayi seklinde kalacak.
- Governance cizgisi korunacak:
  - plane-aware yorum
  - no implicit OSNR-to-SNR substitution
  - no resolution/accuracy aliasing

Durum notu
- 2026-03-10 itibariyla section-ici prose temizligi uygulanmistir.
- Kalan durum, section-ici degil manuskriptler-arasi entegrasyon seviyesindedir.
