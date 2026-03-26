# Active Context

Son Guncelleme: 2026-03-15
Guncelleyen: AI + Kullanici

---

## Su Anki Faz

Section III (Methodology) repo-validated conditionally-freeze-ready duruma getirildi. Section IV section-ici camera-ready polish tamamlandi. Section VI authoritative recovery merge, core hardening, ve integration pass tamamlandi. Section VII icin survey-alignment, reporting-policy lock, ve manuscript-level consistency pass uygulandi. Section VIII editorial closeout ve QA refresh tamamlandi. Tam manuskript integration pass ve release-gate QA da uygulandi. Whole-manuscript figure inventory cikartildi ve section-bazli figure strategy lock notu olusturuldu; figure numbering policy artik freeze edildi. Aktif manuskript odagi artik Section V `Fig. V-1 / Fig. V-2` specification + asset production, Section V legacy denominator uzlasimi, bundle hygiene, ve sonrasinda abstract + Section IX skeleton kaynagidir. Abstract ve Section IX final yazimi ise bilerek sonraya birakildi; bunlar figure paketi ve kalan release-gate tutarliliklari kapandiktan sonra skeleton-draft olarak acilacak.

Figure numbering policy freeze snapshot (2026-03-15):
- Whole-manuscript figure numbering policy resmi olarak kilitlendi:
  - Section I acilis paketi global `Fig. 1-3` olarak korunacak
  - Section II ve sonrasi section-prefixed numbering kullanacak (`Fig. II-1`, `Fig. III-1`, `Fig. V-1`, `Fig. VI-1`, vb.)
- Bu karar ayri workflow notuna yazildi:
  - `.agent/workflows/whole_manuscript_figure_numbering_policy_20260315.md`
- Canonical Section V metni policy ile hizalandi:
  - `Fig. 4` -> `Fig. V-1`
  - `Fig. 5` -> `Fig. V-2`
- Sonuc:
  - onceki Section III / Section V figure collision resmi olarak kapandi
  - bundan sonraki figure prompt/spec/caption kararlarinda duz numeric labels Section I disinda yeniden acilmamali
- Yeni aktif global siralama:
  - Section V `Fig. V-1 / Fig. V-2` specification + asset production
  - Section V `221 -> 220` denominator reconciliation
  - sonra abstract + Section IX skeleton drafting

Section V figure prompt + table-status snapshot (2026-03-15):
- Section V icin kopyala-yapistir kullanilacak production-ready figure prompt dosyasi yazildi:
  - `.agent/workflows/section_05_figure_prompts_20260315.md`
- Kapsam:
  - `Fig. V-1` = governed operating cloud
  - `Fig. V-2` = sparse admissible frontier
  - her iki figure icin final prompt, negative prompt, control prefix, caption draft, veri-kaynak mantigi
- Net durum:
  - Section V tablolari artik "olusturulacak" durumda degil
  - canonical `drafts/section_05_template.md` icinde `Table V / Table VI / Table VII` doldurulmus durumda
  - aktif acik is gercek figure asset katmani ve `221 -> 220` denominator uzlasimidir

End-of-day handoff snapshot (2026-03-14):
- Bugun ana odak repo sadeleştirme + Section II + Section III closeout seviyesinde ilerledi.
- Yapilanlar:
  - `manuscript/current_bundle/` altinda tek merkezli okuma/paketleme kati acildi
  - Section II canonical metne `Fig. II-1`, `Fig. II-2`, `Table II-1`, `Table II-2` eklendi
  - Section II bundle ve current-bundle katmanina tam yansitildi
  - Section III metodoloji numbering temizlendi:
    - `Table III-1`
    - `Fig. III-1`
  - Section III'ten repo-ici dosya yolu dili cikarildi; publication-facing prose korundu
  - Section III PRISMA mermaid blogu VSCode preview uyumlu sade `flowchart TB` yapisina refresh edildi
- Su an geldigimiz nokta:
  - Section II yapisal paket tamam (`2 fig + 2 table`)
  - Section III section-level olarak temiz ve freeze-ready
  - current working hub artik `manuscript/current_bundle/`
- Siradaki mantikli isler:
  - whole-manuscript figure numbering policy freeze
  - Section V `Fig. 4 / Fig. 5` specification + asset production
  - Section V `221 -> 220` denominator reconciliation
  - daha sonra abstract + Section IX skeleton drafting
- Dikkat edilmesi gerekenler:
  - `current_bundle` canonical authoring source degil; sadece merkezi okuma/paketleme kati
  - canonical metinler hala `drafts/`, `analysis/`, ve secili durumlarda `review_package/` altinda
  - Section II'de acik kalan is tablo eksigi degil; yalnizca `fig_ii_1` visual polish ve `fig_ii_2` teknik cleanup
  - Section III local collision temizlendi ama whole-manuscript numbering policy global olarak hala acik
  - bundle provenance guvenli, fakat yayin oncesi genel bundle-hygiene/encoding/comment cleanup turu hala faydali olabilir

Repo simplification snapshot (2026-03-14):
- Kullanici geri bildirimi uzerine repo yapisinin artik fazla katmanli/kompleks hissedildigi acikca kayda gecirildi.
- Bu nedenle yeni bir "tek merkezli okuma/paketleme kati" acildi:
  - `manuscript/current_bundle/`
- Bu klasor icinde:
  - `OISAC_COMST_current_bundle.md` = guncel birlestirilmis manuskript kopyasi
  - `figures/` = bu bundle ile birlikte tutulacak mevcut figure assetleri
  - `FIGURE_STATUS.md` = aktif ve staged figure ayrimi
  - `RELEASE_GATE_QA.md` = bundle-level QA ozeti
- Yeni calisma kurali:
  - yeni bir konusmada "guncel manuskript + gorseller" birlikte gorulmek istenirse once `manuscript/current_bundle/` acilsin
  - section-level authoring kaynaklari yine `drafts/`, `analysis/`, ve `review_package/` altinda kalmaya devam etsin
- Section II figure assetleri bu merkezi pakete de kopyalandi ve artik canonical Section II metninden bundle'a propagate oluyor.

Conversation handoff snapshot (2026-03-14):
- Yeni konusmaya gecis icin son durum kaydi guncellendi.
- Section II figure work artik su olgunlukta:
  - strategy note hazir
  - production-spec note hazir
  - AI image prompts hazir
  - user-generated `Fig. II-1` review edildi ve "near-final / visual polish" seviyesinde
- Section II icin son pratik durum:
  - mevcut `Fig. II-1` conceptually usable
  - kalan duzeltmeler yalnizca kucuk visual polish adimlari
  - onerilen asset yolu `drafts/fig_ii_1.png` ve `drafts/fig_ii_2.png`
  - `Fig. II-1 / Fig. II-2` artik canonical `drafts/section_02_fundamentals_draft.md` icine baglandi ve hem `review_package` hem `manuscript/current_bundle` bundle katmanina yansitildi
  - `Table II-1 / Table II-2` de canonical Section II metnine eklendi; Section II artik planlanan `2 fig + 2 table` paketine ulasti
- Yeni konusmada en hizli acilis noktasi:
  - ya `Fig. II-2` teknik cleanup ve `Fig. II-1` visual polish adimlarina devam etmek
  - ya tum manuskript figure numbering / package kararina donmek
- Abstract ve Section IX halen bilerek deferred durumda; figure/release-gate kapanmadan final prose yazilmayacak.

Whole-manuscript integration snapshot (2026-03-14):
- `review_package/01_manuscript_bundle.md` ve `review_package/COMST_review_bundle_01_manuscript.md` canonical Section I-VIII kaynaklarindan UTF-8 olarak yeniden uretildi.
- Bundle icine Section VII ve Section VIII'in guncel camera-ready kaynaklari da dahil edildi; onceki review-package manuscript bundle stale/incomplete durumdaydi.
- Release-gate QA notu eklendi:
  - `review_package/05_release_gate_QA.md`
- QA sonucu:
  - `CONDITIONAL PASS`
  - Section I-VIII butunlesik bundle guncel
  - kalan release-gate kalemleri: Section V icindeki legacy `221 papers` denominator dili, final figure yerlestirmesi, ve eger final organization `I-IX` olarak korunacaksa Section IX source gap
- Sonuc:
  - review-package artik Section I-VIII seviyesinde guncel bir manuskript bundle tasiyor
  - siradaki pratik adim figure paketi ve kalan release-gate tutarliliklaridir

Abstract / Section IX timing reminder (2026-03-14):
- Kullanici ve AI ortak karariyla abstract ve Section IX icin final prose bu asamada zorlanmayacak.
- Gerekce:
  - bu iki bolum final section akisi, sayilar, ve figure paketi sabitlendikten sonra en dogru sekilde yazilabilir
  - icerik omurgasi buyuk olcude tamam olsa da submission-readiness son kapama dili bu iki bolumde toplaniyor
- Plan:
  - once final figure paketi ve kalan release-gate tutarliliklari
  - sonra abstract + Section IX icin kisa skeleton draft
  - en son final wording / polishing

Whole-manuscript figure inventory snapshot (2026-03-14):
- Figure inventory/workflow notu olusturuldu:
  - `.agent/workflows/whole_manuscript_figure_inventory_20260314.md`
- Mevcut durum:
  - Section I icin `Fig. 1 / Fig. 2 / Fig. 3` gercek local asset olarak dogrulandi (`drafts/fig1.png`, `drafts/fig2.png`, `drafts/fig3.png`)
  - Section II icin `Fig. II-1 / Fig. II-2` artik canonical metne insert edildi ve bundle katmanina propagate edildi
  - Section II icin `Table II-1 / Table II-2` canonical metne insert edildi; onceki `2 fig + 2 table` hedefi artik yapisal olarak saglandi
  - Section III icin PRISMA anchor/caption local olarak `Fig. III-1` etiketine normalize edildi; metodoloji eligibility tablosu da `Table III-1` oldu
  - Section IV icin `Fig. IV-1 / Fig. IV-2` specification-level durumda
  - Section V icin `Fig. 4 / Fig. 5` planned durumda; Section III ile dogrudan `Fig. 5` collision artik kapali
  - Section VI icin `Fig. VI-1 / Fig. VI-2` comment-spec seviyesinde ve asset/placement kullanici tarafinda
  - Section VII / VIII icin aktif figure referansi bulunmadi
- Siradaki pratik karar:
  - whole-manuscript figure numbering policy'yi freeze etmek
  - sonra kullaniciyla final figure package kapsam ve placement kararini netlestirmek

Whole-manuscript section figure strategy snapshot (2026-03-14):
- Section-bazli COMST figure strategy notu olusturuldu:
  - `.agent/workflows/whole_manuscript_section_figure_strategy_20260314.md`
- Temel karar:
  - Section I orientation-figure agirlikli kalacak (`Fig. 1-3` yeterli; tarihi `Fig. 4` zorunlu kabul edilmeyecek)
  - Section II icin dogru paket `2 fig + 2 table`; bu bolum explanatory/governance visual ister, prevalence visual istemez
  - Section III tek PRISMA flow figure ile minimal kalacak
  - Section IV iki zorunlu taxonomy figure ister (`Fig. IV-1`, `Fig. IV-2`)
  - Section V iki zorunlu quantitative trade-off figure ister (`Fig. 4`, `Fig. 5`)
  - Section VI iki zorunlu systems/enabler figure ile kalir (`Fig. VI-1`, `Fig. VI-2`)
  - Section VII tablo-dominant kalabilir; en fazla bir optional cross-domain synthesis figure
  - Section VIII prose-dominant kalabilir; en fazla bir optional roadmap/dependency figure
  - Section IX ve abstract icin default olarak figure gerekmiyor
- Yeni pratik sira:
  - once whole-manuscript numbering policy / collision karari
  - sonra Section II `Fig. II-1 / Fig. II-2` spec yazimi
  - ardindan Section IV / V final figure package kararlarinin kullaniciyla netlestirilmesi

Section II figure-spec snapshot (2026-03-14):
- AI-assisted cizim icin ayrintili Section II figure brief'i yazildi:
  - `.agent/workflows/section_02_figure_specs_20260314.md`
- Kapsam:
  - `Fig. II-1` unified O-ISAC system abstraction
  - `Fig. II-2` metric contract and admissible comparison map
- Not:
  - Bu dosya production-spec seviyesinde yazildi; purpose, layout, zorunlu etiketler, caption draft, AI prompt draft, negative prompt, ve post-generation checklist iceriyor
- Kullanici bu spec'i AI gorsel uretiminde dogrudan kullanabilir

Section II table insertion snapshot (2026-03-14):
- Canonical `drafts/section_02_fundamentals_draft.md` icine iki tablo eklendi:
  - `Table II-1`: modality-aware channel / transceiver abstraction summary
  - `Table II-2`: metric contract and comparability guard summary
- Yerlesim:
  - `Table II-1` -> Section II-C sonrasinda
  - `Table II-2` -> Section II-D sonrasinda
- Bu ekleme sonrasi Section II artik hedeflenen `2 fig + 2 table` paketine ulasmis durumda.

Section III numbering cleanup snapshot (2026-03-14):
- Canonical `drafts/section_03_methodology.md` icinde local methodology labels normalize edildi:
  - `Table II` -> `Table III-1`
  - `Fig. 5` -> `Fig. III-1`
- Sonuc:
  - Section III icindeki metodoloji artefaktlari artik kendi section-yerel etiketini tasiyor
  - Section V ile onceki dogrudan `Fig. 5` collision kapandi
  - ancak whole-manuscript numbering policy yine de global olarak acik; Section I / V halen duz numeric scheme kullaniyor

Section III publication-language cleanup snapshot (2026-03-14):
- Canonical `drafts/section_03_methodology.md` icindeki repo-ici dosya yolu dili publication-facing prose'a cevrildi.
- Kaldirilan/normalize edilen ifade tipi:
  - `search/...`
  - `screening/...`
  - `analysis/...`
- Yeni yazi mantigi:
  - supplementary material / study records / structured screening ledger gibi survey-uygun metodoloji dili
- Sonuc:
  - Section III artik repo ic yapisini okuyucuya gostermiyor
  - metodoloji aciklamasi korunuyor, ama ic calisma yolu dili manuskriptte kalmiyor

Section III figure prompt snapshot (2026-03-14):
- Kullanici talebi uzerine Section III icin PRISMA flow figure prompt dosyasi yazildi:
  - `.agent/workflows/section_03_figure_prompt_20260314.md`
- Kapsam:
  - `Fig. III-1` icin final prompt
  - negative prompt
  - short control prefix

Section III mermaid refresh snapshot (2026-03-14):
- Kullanici VSCode icinde Mermaid preview kullanacagini belirttigi icin canonical Section III icindeki PRISMA block sade bir `flowchart TB` yapisina refresh edildi.
- Amaç:
  - markdown icinden dogrudan goruntulenebilir olmak
  - renk/asama mantigini korurken renderer-uyumlulugunu artirmak
- Bu degisiklik bundle katmanlarina da propagate edildi.

Section II figure prompt snapshot (2026-03-14):
- Kullanici talebi uzerine AI gorsel uretiminde dogrudan kopyala-yapistir kullanilacak nihai prompt dosyasi da yazildi:
  - `.agent/workflows/section_02_figure_ai_prompts_20260314.md`
- Dosya iki katman iceriyor:
  - `Fig. II-1` final prompt + negative prompt
  - `Fig. II-2` final prompt + negative prompt
- Ozel koruma:
  - caption'in resmin icine yazilmamasi
  - uzun aciklama paragraflarinin gorsele gomulmemesi
  - prevalence chart / decorative infographic / 3D style / metric-role karisimi gibi hata tiplerinin engellenmesi

Section II figure review snapshot (2026-03-14):
- Kullanici tarafinda uretilen `Fig. II-1` icin late-stage review notu yazildi:
  - `.agent/workflows/section_02_figure_review_notes_20260314.md`
- Degerlendirme:
  - `fig_ii_1` conceptually usable / near-final
  - ana structural issue olan duplicated output box cozuldu
  - `fig_ii_1` kalan is visual polish seviyesinde
  - `fig_ii_2` survey-appropriate concept tasiyor, ancak teknik relation cleanup gerektiriyor
- Kalan fix sirası:
  - `fig_ii_1`: `Joint design` kutusunu aktiflestir, ortak output box'i kompaktlastir, output label hizasini toparla, sag paneli biraz geri cek, basligi hafif kucult
  - `fig_ii_2`: `tau -> Delta r_min` iliskisini kaldir, `Delta z` blocked iliskilerini temizle, `CRQ_Delta`'yi yalnizca `R + Delta r_min` ile turet, `Delta r_min` notasyonunu duzelt, `Ambiguous SNR` ikonunu kaldir
- Repo icinde onerilen asset placement:
  - `drafts/fig_ii_1.png`
  - `drafts/fig_ii_2.png`

Section IV/VII consistency snapshot (2026-03-14):
- Section IV taxonomy contract yeniden kontrol edildi; normalized medium vocabulary ve metric-governance cizgisi canonical referans olarak korundu.
- `analysis/VII_cr_mrg_v1/section_07_camera_ready.md` icinde Section VII manuscript-level consistency pass uygulandi:
  - Section IV normalized medium labels daha gorunur hale getirildi (`cabled fiber`, `VLC/LiFi`, vb.)
  - Section VI contextual-enabler policy acikca yankilandi
  - Section II metric-plane guard icin SNR-family ifadeleri source-reported communication-plane degisken olarak nitelendi
- `analysis/VII_cr_mrg_v1/section_07_final_QA.md` refresh edildi:
  - word count (`section_07_camera_ready.md`) = `5483`
  - SHA256 (`section_07_camera_ready.md`) = `D8E2AA704D171D856D18C8D7B5FCEB0CEB8299C05CF8149EC968FC5A50F1810C`
  - status = `PASS`
- Sonuc:
  - Section IV / VII cross-section consistency gate tamamlandi; bundan sonra bu iki section yalnizca whole-manuscript integration veya sonraki text degisikligi durumunda yeniden acilacak.

Section VIII closeout snapshot (2026-03-14):
- `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md` icinde editorial standardization pass uygulandi.
- `VIII-A..VIII-E` boyunca section-title tonu, case basliklari, math-anchor basliklari, ve key-takeaway stili publication-uniform hale getirildi.
- Bilimsel icerik, cite-key union, ve `VIII-F / VIII-G` rol sinirlari korunarak yalnizca editorial duzenleme yapildi.
- `analysis/VIII_cr_mrg_v1/section_08_final_QA.md` refresh edildi:
  - total word count = `5842`
  - SHA256 (`section_08_camera_ready.md`) = `C2E9EE36E85BBC9ED17078E7D17CB30BDA533297013884E00D4CDB5F6123FF37`
  - status = `READY: PASS`
- Sonuc:
  - Section VIII aktif drafting backlog'undan cikti; bundan sonra ancak whole-manuscript integration veya sonraki text degisiklikleri sonrasinda QA refresh baglaminda yeniden acilacak.

Section VII alignment snapshot (2026-03-12):
- Section VII canonical structure `VII-A..VII-G` olarak kilitlendi.
- `VII-F` cross-domain application synthesis olarak tutuldu.
- `VII-G` dual-view consistency / audit layer olarak tutuldu.
- Section VII manuscript body icin reporting policy kilitlendi:
  - primary counts: strict evidence view
  - secondary consistency lens: structured `study_flag_count`
- Canonical Section VII cross-domain coverage sayilari 220-paper included corpus ile hizalandi:
  - smart infrastructure: `203`
  - indoor environments: `81`
  - automotive transportation: `104`
  - underwater/harsh: `23`
  - space/satellite: `34`
- `memory-bank/review/reference` outline kopyalari Section VII `A-G` yapisi ile hizalandi.
- Section VII bu pass sonrasi section-level freeze-ready durumdadir.
- Bundan sonra yalnizca:
  - final whole-manuscript integration sirasinda gerekiyorsa son QA refresh
  - legacy analysis artefact'larinda gerekirse sonraki refresh turu

Section VI closeout snapshot (2026-03-12):
- Section VI section-level AI yazim/duzenleme isi kapatildi.
- Canonical working draft:
  - `drafts/section_06_draft.md`
- Section VI icinde tamamlanan ana isler:
  - recovery merge
  - claim-hardening
  - metric-governance alignment
  - weak-evidence cleanup
  - publication-flow polish
  - cross-section consistency
  - numbering / cross-reference / integration pass
- Section VI icinde kalanlar:
  - `Fig. VI-1 / Fig. VI-2` gercek asset uretimi ve yerlestirme kullanici tarafinda
  - final whole-manuscript QA turunda Section I / VII / VIII ile son bridge/crossref kontrolu
- Sonuc:
  - Section VI aktif drafting backlog'undan cikti; bundan sonra ancak whole-manuscript integration veya figure placement baglaminda yeniden acilacak.

Ek guncel odak (2026-03-12):
- Section VI authoritative recovery merge uygulandi.
- `drafts/draft6_FD.md` icerigi kontrollu olarak `drafts/section_06_draft.md` yoluna geri tasindi.
- Pre-merge archive alindi:
  - `drafts/_archive_20260205/section_06_draft_pre_recovery_merge_20260312_101453.md`
- `drafts/section_06_draft.md` artik VI-A..VI-F govdesini tekrar tasiyor.
- Section VI icin bu recovery-sonrasi kalite katmani daha sonra tamamlandi:
  - strict-vs-raw prevalence / claim-hardening
  - metric-governance alignment
  - weak-anchor families icin stronger anchor veya qualitative-only sinirlama
- Section V production re-entry basladi; draft survey mimarisi baglaminda yeniden okunup aciklar ayrildi.
- `drafts/section_05_template.md` icinde publication-prose pass uygulandi ve `Table V / VI / VII` summary katmani eklendi.
- Section V icin kalici architecture/camera-ready note eklendi:
  - `memory-bank/section5_camera_ready_notes.md`
- Kalan Section V aciklari daraltildi:
  - `Fig. 4 / Fig. 5` asset uretimi
  - Section I / IV / VIII consistency + final numbering/crossref kontrolu
- Section V structure karari uygulandi:
  - `V-E` bagimsiz alt-bolum yerine Section V sonunda closeout synthesis olarak tutuldu
- Section V Table VII scope karari uygulandi:
  - `Table VII` head-to-head comparative artifact olarak tutuldu
  - CRQ/frontier semantics metin + `Fig. 5` tarafinda birakildi
- Re-entry hatirlatmasi:
  - Siradaki ortak karar/uygulama adimi `Fig. 4 / Fig. 5` icin kisa specification pass, hemen ardindan gercek asset uretimidir
  - "Asset production" hem figure tasarimini netlestirmeyi hem de gercek figure dosyalarini uretmeyi ifade eder

Section VI icin ek durum guncellemesi (late 2026-03-12):
- `drafts/section_06_draft.md` publication-facing core yapida stabilize edildi.
- Uygulanan kalite adimlari:
  - claim-hardening pass
  - metric-governance pass
  - weak-evidence / qualitative-only cleanup
  - publication-prose / section-flow polish
  - cross-section consistency pass (Section I / IV / VIII hizasi)
- Section VI final core artifact seti artik su sekildedir:
  - `Table VI-1`
  - `Table VI-A.1`
  - `Table VI-2`
  - `Fig. VI-1` comment-spec
  - `Fig. VI-2` comment-spec
- Section VI artik recovery veya scaffold separation asamasinda degil; `core manuscript stabilized` seviyesindedir.
- O asamada acik kalan kalemler figure assetleri ve whole-manuscript integration idi; bunlar daha sonra ayri kararlarla ele alindi.

Section VI icin ek durum guncellemesi (integration late 2026-03-12):
- whole-manuscript numbering / cross-reference / integration pass uygulandi.
- Section I contribution dili, Section IV taxonomy etiketleri, Section VII handoff cizgisi ve Section VIII challenge/roadmap baglamlari Section VI icinde son kez hizalandi.
- `drafts/section_06_draft.md` icinde:
  - Section I'in named-anchor vaadi opener'da acikca yankilandi
  - `photonics-assisted signal generation` dili normalize edildi
  - `Table VI-A.1` ve `Table VI-2` butun-manuskript artefakt rolu ile konumlandi
- Kullanici karari:
  - `Fig. VI-1 / Fig. VI-2` gercek asset uretimi ve dokumana gorsel yerlestirme kullanici tarafinda yapilacak
  - `OPA/RIS filtering` ve benzeri pipeline-hijyeni kalemleri Section VI ana yapilacaklar listesinden cikarildi
- Section VI icin AI tarafinda aktif teknik/pipeline kalemi tutulmuyor.

Ek guncel odak (2026-03-11):
- Survey'nin late-stage uretim fazinda figure/table/equation/cross-reference planlamasi repo-icindeki COMST-jargon ve metric-governance kaynaklarindan turetilecek; disaridan ad-hoc terminoloji listesi kullanilmayacak.
- Canonical COMST writing/jargon kaynaklari:
  - `memory-bank/goldenModel.md`
  - `memory-bank/master_writing_guide.md`
- Canonical metric/mapping kaynaklari:
  - `analysis/V_ev_v2/axis_definitions.md`
  - `analysis/V_ev_v2/s5b_met_gov.csv`
  - `analysis/VI_ev_v2/axis_definitions.md`
  - `analysis/VII_ev_v2/axis_definitions.md`
  - `analysis/VIII_ev_v1/axis_definitions.md`
- Yakin donem geri giris odagi:
  - Section IV production inventory + cross-manuscript integration-check

Ek guncel odak (2026-03-10):
- Final canonical late-stage PRISMA durumu:
  - `222` full-text assessed
  - `2` full-text excluded
  - `220` studies included
- Section III validator geciyor:
  - `screening/validate_section3_freeze.py`
- Section III icin memory-bank destekli inferred provenance katmani eklendi:
  - `search/inferred_freeze_provenance_timeline_20260310.csv`
  - `search/inferred_freeze_provenance_from_memory_bank_20260310.md`
- Kalan tek buyuk Section III acigi arsivsel:
  - freeze-time WoS / raw-search bundle eksik
  - takip notu: `.agent/workflows/section3_external_input_need_20260310.md`
- Section IV 2026-03-10 camera-ready prose polish pass'i uygulandi; kalan durum cross-manuscript terminology/caption/release-gate kontroludur.
- Section VI accidental overwrite sonrasi recovery zinciri netlestirildi.
- User-preserved Section VI recovery source bulundu:
  - `drafts/draft6_FD.md`
- Section VI recovery hierarchy:
  - authoritative recovery source: `drafts/draft6_FD.md`
  - partially restored working draft: `drafts/section_06_draft.md`
  - archival reconstruction: `drafts/section_06_draft_reconstructed_20260310.md`
  - incident note: `drafts/section_06_recovery_note_20260310.md`
- Section VIII manuscript-level reference sweep tamamlandi ve Section VIII near-freeze durumda.
- Survey genel backlog:
  - `memory-bank/survey_global_backlog_2026-03-09.md`

Odak degisimi:
- Section II kalite kapama notlari korunuyor (referans baseline).
- Section III artik birincil manuskript blokaji olmaktan cikti; kalan acik raw-export seviyesinde.
- Section IV artik birincil rewrite isi degil; polish sonrasi integration-check seviyesinde.
- Section VI recovery merge, quality hardening, ve integration pass tamamlandi; kalan is yalnizca figure placement + final QA baglamindadir.
- Section VIII sadece editorial standardization + gerekirse QA refresh bekliyor.
- Siradaki ana manuskript isi: Section VIII editorial closeout + final cross-manuscript integration.

---

## Yapilanlar (bu asamaya kadar)

### Section II (Fundamentals) - kalite kapama
- II-A..II-E citation destek kontrolu v3 CSV'lerle tekrar dogrulandi.
- II-E tarafinda unsupported anchor riski temizlendi; destekli anchor setine gecildi.
- II-D tarafinda metric-governance kontrati (plane separation + delta_z / delta_r_min ayrimi) final pass ile dogrulandi.
- Section II draft sonuna COMST/PRISMA finalization checklist eklendi:
  - Figure/Table hedefleri (Section II icin 2 fig + 2 table)
  - freeze oncesi kontrol listesi
- Ilgili dosyalar:
  - `drafts/section_02_fundamentals_draft.md`
  - `.agent/workflows/section_02D_crosscheck.md`
  - `.agent/workflows/section_02E_crosscheck.md`
  - `.agent/workflows/section_02D_v3_change_notes.md`

### Section III (Methodology) - freeze hardening ve audit reconstruction
- Registration truth lock tamamlandi; OSF kaydi metodoloji/protokol/checklist dosyalarina islendi.
- Search consistency lock tamamlandi; formal source policy IEEE Xplore + Scopus + Web of Science olarak netlestirildi.
- PRISMA flow integrity canonical dosyalarda kilitlendi:
  - `search/search_log.csv`
  - `screening/prisma_flow_counts.csv`
  - `screening/excluded_fulltext_log.csv`
- Full-text ve included corpus reconstruction tamamlandi:
  - `screening/fulltext_assessed_reconstruction.csv` -> `222`
  - `screening/included_studies_canonical.csv` -> `220`
  - `screening/canonical_included_corpus_ledger.csv` -> `220`
- `O_ISAC_347` canonical corpus disina alindi ve `EXC-UNVERIFIED-FULLTEXT` olarak kapatildi.
- `O_ISAC_044` repo-verified included olarak uzantisiz PDF iziyle reconcile edildi.
- Section III icin reconstructed search-stage freeze pack olusturuldu:
  - `search/formal_identification_reconstruction_20251130.csv`
  - `search/upstream_prisma_reconstruction_20260310.csv`
  - `search/reconstructed_freeze_bundle_note_20260310.md`
- Memory-bank destekli inferred provenance katmani eklendi:
  - `search/inferred_freeze_provenance_timeline_20260310.csv`
  - `search/inferred_freeze_provenance_from_memory_bank_20260310.md`
- Section III validation script'i eklendi ve PASS verdi:
  - `screening/validate_section3_freeze.py`
- Durum notlari:
  - `screening/section3_evidence_reconstruction.md`
  - `.agent/workflows/section3_freeze_closure_note_20260310.md`
  - `.agent/workflows/section3_completion_task_list_20260310.md`
  - `.agent/workflows/section3_external_input_need_20260310.md`

### Section IV (Taxonomy) - camera-ready not kaydi
- Section IV-A..E bolumleri zorunlu veri dosyalariyla (v2 evidence setleri) yeniden yazildi.
- 2026-03-10 camera-ready prose polish pass'i uygulandi:
  - ham schema/pipeline etiketleri temizlendi
  - audit kategori adlari publication prose'a cevrildi
  - tablo basliklari ve satir adlari daha COMST-uyumlu hale getirildi
- Kalici not dosyasi olusturuldu:
  - `memory-bank/section4_camera_ready_notes.md`
- Section II benzer kayit kontrolu dogrulandi:
  - Bu dosyada "Section II (Fundamentals) - kalite kapama" blogu mevcut
  - Section II draft sonunda finalization checklist mevcut (`drafts/section_02_fundamentals_draft.md`)

### Section V (Performance / Trade-off) - production re-entry ve architecture note
- Section V draft survey mimarisi baglaminda yeniden okundu; section-ici aciklar ile cross-manuscript aciklar ayrildi.
- `drafts/section_05_template.md` icinde publication-prose pass uygulandi.
- Canonical `analysis/V_ev_v2/*` kaynaklarindan `Table V`, `Table VI`, ve `Table VII` summary katmani taslaga eklendi.
- `V-E` bagimsiz alt-bolum olmaktan cikarilip Section V sonunda bounded closeout synthesis olarak yeniden konumlandi.
- `Table VII` kapsam karari freeze edildi; tablo comparative slice rolunde tutuldu.
- Kalici memory-bank notu eklendi:
  - `memory-bank/section5_camera_ready_notes.md`
- Kalan durum yeni veri/yeniden extraction degil; figure asset ve cross-manuscript consistency seviyesindedir.

### Section VI (Enablers / System-Level Co-Design) - recovery merge + hardening prep
- Section VI working draft path'inde accidental overwrite sonrasi recovery calismasi kayda alindi.
- `drafts/section_06_draft.md` restored canonical working draft olarak tutuluyor.
- `drafts/section_06_draft_reconstructed_20260310.md` overwrite sonrasi archival reconstruction olarak saklaniyor.
- `drafts/section_06_recovery_note_20260310.md` olay izi olarak olusturuldu.
- User-saved richer working draft bulundu:
  - `drafts/draft6_FD.md`
- Recovery source priority kilitlendi:
  1. `drafts/draft6_FD.md`
  2. `drafts/section_06_draft.md`
  3. `drafts/section_06_draft_reconstructed_20260310.md`
  4. `drafts/section_06_recovery_note_20260310.md`
- 2026-03-12 authoritative recovery merge uygulandi:
  - `drafts/draft6_FD.md` icerigi `drafts/section_06_draft.md` yoluna geri tasindi
  - pre-merge archive: `drafts/_archive_20260205/section_06_draft_pre_recovery_merge_20260312_101453.md`
  - `drafts/section_06_draft.md` artik VI-A..VI-F drafting malzemesini yeniden tasiyor
- Mevcut Section VI kalite/acik notlari hala aktif:
  - `.agent/workflows/section_06_improvement_notes.md`
  - `.agent/workflows/section_06_action_plan.md`
- Kalici memory-bank notu eklendi:
  - `memory-bank/section6_recovery_notes.md`

### Section VIII (Challenges / Outlook) - closeout prep
- Section VIII icin manuscript-wide reference sweep tamamlandi.
- Stale referanslar aktif manuscript/review/template katmaninda temizlendi.
- Kalan is editorial standardization + metin degisirse QA refresh olarak daraltildi.
- Ilgili notlar:
  - `.agent/workflows/section_08_improvement_notes.md`
  - `analysis/s08_ref_swp_note.md`

---

## Yapilacaklar (hemen siradaki adimlar)

0) Section VI closeout durumu
- `drafts/section_06_draft.md` core manuscript stabilized durumdadir.
- whole-manuscript numbering / cross-reference / integration pass uygulanmistir.
- `Fig. VI-1 / Fig. VI-2` gercek asset uretimi ve dokumana yerlestirme kullanici tarafinda yapilacaktir.
- Section VI icin AI tarafinda ek bir pipeline-hijyeni gorevi aktif backlog'da tutulmayacaktir.

1) Section VIII closeout
- `VIII-A..VIII-E` baslik/subheading standardization (yalnizca editorial pass).
- Section VIII metni degisirse `analysis/VIII_cr_mrg_v1/section_08_final_QA.md` refresh.
- Opsiyonel: legacy outline/template encoding artefact temizligi.

2) Section IV / VI / VII cross-manuscript consistency hardening
- Section IV icin final manuskriptte terminology/caption consistency kontrolu yap.
- Section VI icin terminology/caption/bridge dili consistency'sini final manuskriptte koru.
- Section VII icin terminology/handoff consistency'sini final manuskriptte koru; primary strict-count policy'den sapma olmasin.
- Tum bu adimlarda Section II metric-governance dili korunacak.

3) Whole-manuscript integration prep
- Section-level sayi ve label senkronunu I-IX boyunca son kez kontrol et.
- Introduction, methodology, taxonomy ve challenge/roadmap akisinin ayni corpus sayilariyla konustugundan emin ol.
- Final QA/release gate icin notlari tek yerde topla.

4) Section V figure specification + asset production
- `Fig. 4` ve `Fig. 5` icin kisa specification pass'i tamamla.
- Hemen ardindan canonical `analysis/V_ev_v2/*.csv` kaynaklarindan gercek figure asset'lerini uret.
- Final numbering/crossref kararlarini Section I / IV / VIII consistency pass'i ile kilitle.

5) Section III archival recovery (non-blocking but valuable)
- Bulunursa freeze-time WoS / merged raw-search export bundle geri kazanilacak.
- Takip:
  - `.agent/workflows/section3_external_input_need_20260310.md`

---

## Aktif Riskler

- Section VI core manuscript stabilized durumda, ancak `Fig. VI-1 / Fig. VI-2` asset uretimi ve final placement kullanici tarafinda oldugu icin final whole-manuscript QA'da son kez kontrol edilmelidir.
- Section III upstream PRISMA zinciri (`980 / 280 / 700`) hala tam row-level raw-export-backed degil.
- Eksik dis girdi:
  - WoS / Clarivate freeze export
  - `data/raw_search_results/` veya esdeger merged raw-search bundle
- Section IV icin section-ici polish tamamlandi, ancak final manuskriptte terminology/caption drift riski kaldi.
- Section VII manuscript body kilitlendi, ancak legacy analysis raporlarinda pre-canonical count izi kalirsa sonraki refresh turunda temizlenmesi gerekebilir.
- Section II metninde yayin oncesi teknik temizlik (BOM + ic yorum temizligi) gerekebilir.

---

## Degismez Governance Kurallari

- Plane separation: OSNR optical-plane; SNR/ESNR electrical-plane.
- Metric aliasing yok: resolution, accuracy, `delta_r_min`, `sigma_r`, `delta_z` ayrimi korunacak.
- Her claim icin anchor + context zorunlu.
- PRISMA scope lock: canonical corpus ve flow sayilari sectionlar arasi degismeyecek.
- Current canonical Section III late-stage lock:
  - `222 assessed`
  - `2 excluded`
  - `220 included`
