# AGENTS.md

## Kapsam

Bu dosya repo genelinde geçerlidir. Bu repoda çalışırken güncel operasyon ve kalan işler için kökteki `START_HERE_OISAC_PRISMA_CURRENT.md`, ayrıntılı çalışma bağlamı için `PROJECT_CONTEXT_OISAC_PRISMA.md` esas alınır.

## Zorunlu İlk Okuma

Bu projede herhangi bir forward işlem yapmadan önce:

1. `START_HERE_OISAC_PRISMA_CURRENT.md`
2. `PROJECT_CONTEXT_OISAC_PRISMA.md`
3. START HERE dosyasının “Yeni ajan için zorunlu okuma sırası” bölümünde gösterilen locked criteria, reviewer-process, tracker, decision-log ve memory-bank dosyaları

okunmalı ve güncel state dosya/hash kanıtıyla doğrulanmalıdır.

`START_HERE_OISAC_PRISMA_CURRENT.md`, güncel operasyonel handoff ve forward roadmap’tir. Eski checkpoint, handoff ve memory-bank bölümleri audit trail’dir; START HERE tarafından açıkça kanonik gösterilmedikçe current truth veya current next step olarak kullanılmamalıdır.

Başka bilgisayarda absolute path değişebileceği için proje içi dosyalarda mümkün olduğunca repo köküne göre relative path kullanılmalıdır. Sibling `../reviewmdS` yalnızca PDF/HTML/Markdown artifact staging alanıdır; kanonik PRISMA karar state’i değildir.

## Çalışma Bağlamı

- Çalışma konusu: Optical Integrated Sensing and Communication (O-ISAC) for 6G.
- Çalışma türü: PRISMA-grounded narrative systematic review with a scoping-style PCC component.
- Nihai bilimsel manuscript dili: English.
- Repo açıklamaları, workflow yönlendirmeleri, karar notları ve ara çalışma notları Türkçe yazılmalıdır.
- Manuscript-ready section, abstract, title, research question, table caption ve akademik metin taslakları English hazırlanmalıdır.

## Terim Kullanımı

Aşağıdaki teknik terimler gereksiz Türkçeleştirilmemelidir:

O-ISAC, PRISMA, PCC, narrative systematic review, scoping-style mapping, metric-governed comparison, taxonomy, benchmark readiness, validation maturity, rate–sensing tradeoff, CRB, FIM, OSNR, SNR, ESNR, VLC, LiFi, FSO, photonic-THz, hybrid optical systems.

## Dosya ve Klasör Koruma Kuralları

- Mevcut PDF, Word ve checklist dosyalarına dokunulmaz.
- Mevcut klasör yapısı bozulmaz.
- Kullanıcı açıkça istemedikçe kapsam dışı dosyalar düzenlenmez, taşınmaz, silinmez veya yeniden adlandırılmaz.
- PRISMA materyalleri, veri çıkarım tabloları, checklist dosyaları ve manuscript taslakları üzerinde çalışırken planlanan işlem ile tamamlanmış işlem açıkça ayrıştırılır.

## Workflow İlkeleri

- Ana metodolojik çerçeve PCC - Population / Concept / Context olarak tutulur.
- Protocol search window: January 1, 2020 - June 30, 2026; actual final search execution/cutoff date: June 22, 2026. Eligibility date decisions use the actual June 22, 2026 cutoff.
- Core primary databases: Scopus and IEEE Xplore.
- Selected supplementary platform sources: ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online.
- Web of Science and ACM Digital Library are excluded from the current formal source set because institutional access is not available.
- Primary technical eligibility requires sufficient full technical content in English for reliable assessment and extraction. Bilingual reports may qualify when that requirement is met; an English abstract alone is insufficient.
- Meta-analysis planlanmamıştır; gerekçe O-ISAC literatürünün optical modality, system architecture, sensing task, communication metric, sensing metric, validation method ve measurement plane açısından heterojen olmasıdır.
- Synthesis yaklaşımı structured narrative synthesis, scoping-style taxonomy mapping, evidence tabulation, metric-governed comparison, validation maturity mapping, benchmark readiness assessment ve research roadmap synthesis olarak korunmalıdır.
- Düşük methodological/reporting quality tek başına dışlama nedeni yapılmamalıdır; TQAF-style technical quality assessment ile kanıt gücü nitelendirilmelidir.

## Çalışma Disiplini

- Yeni kararlar eklendiğinde `PROJECT_CONTEXT_OISAC_PRISMA.md`, `progress_tracker.md`, `decision_log.md` ve `codex_memory_bank.md` birlikte güncellenmelidir. Current state veya next step değişiyorsa `START_HERE_OISAC_PRISMA_CURRENT.md` de aynı işlemde güncellenir.
- PRISMA akışı, inclusion/exclusion gerekçeleri ve search kararları tarihli ve izlenebilir tutulmalıdır.
- Final manuscript içeriği İngilizce, çalışma açıklamaları ve yönlendirmeler Türkçe olacak şekilde ayrım korunmalıdır.
