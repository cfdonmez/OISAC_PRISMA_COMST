# Historical project memory export

Exported 2026-09-14. Read ../state.md and the live writing rules first.
These records describe their original dates/worktrees; they do not override later author decisions.
Only O-ISAC manuscript/review groups were selected from the local Codex registry.

# Task Group: O-ISAC COMST V3 GitHub publication
scope: Commit and push reviewed COMST V3 manuscript sources, approved figures, governance notes, and final QA PDF to the correct GitHub branch.
applies_to: cwd=C:\OISAC\worktrees\comst-v3-20260906; reuse_rule=use for this V3 branch/repository publication workflow; re-discover remotes and re-check staged scope in any other worktree

## Task 1: Publish V3 manuscript updates, success

### rollout_summary_files

- r07.md (cwd=\\?\C:\OISAC, rollout_path=\\?\C:\Users\fatih\.codex\sessions\2026\09\14\rollout-2026-09-14T10-43-43-01a09edf-34f5-7391-b953-064cdca611e2.jsonl, updated_at=2026-09-14T11:32:09+00:00, thread_id=01a09edf-34f5-7391-b953-064cdca611e2, remote branch verified)

### keywords

- GitHub, cfdonmez/OISAC_PRISMA_COMST, rev/comst-v3-20260906, 766f4da, git remote, git ls-remote, git rev-list --left-right --count, whitespace, s3a.pdf

## User preferences

- when asking “şimdiki yaptıklarını github'a pushlasana yorumları falan da yap” -> prepare an explanatory commit and, when separately evidenced/authorized, add the relevant GitHub comment or PR discussion; do not claim a comment or PR was created when only a branch push occurred. [Task 1]
- when the user corrects “github'da onun reposu vardı” -> absence of a local `origin` is not proof that a GitHub repository is absent; search sibling checkouts, project records, and the connected GitHub account. [Task 1]

## Reusable knowledge

- The correct repository is `cfdonmez/OISAC_PRISMA_COMST`; the published V3 branch is `rev/comst-v3-20260906`. The selected scope had 32 reviewed files: Sections I–III, approved figures, governance notes, `governance/qa/s3a/result.json`, and `output/pdf/s3a.pdf`; temporary QA PNGs, `before_*` backups, browser profiles, and intermediate PDFs were excluded. [Task 1]
- Commit `766f4da8d2089ed84769fe4e4725f8bc959cff1e` (`Revise COMST Sections I-III and integrate reviewed figures`) was pushed. Verify publication with `git ls-remote --heads origin refs/heads/rev/comst-v3-20260906` and `git rev-list --left-right --count HEAD...origin/rev/comst-v3-20260906`; the verified state was matching SHA and `0 0`. [Task 1]

## Failures and how to do differently

- Symptom: a V3 worktree has no `origin` -> pivot to sibling checkout `C:\GH\OISAC_PRISMA_COMST` and accessible GitHub repositories before concluding the repo is absent. [Task 1]
- Symptom: staged whitespace validation flags Markdown EOF blank lines -> fix them and rerun CRLF-aware `git -c core.whitespace=cr-at-eol diff --cached --check` before committing. [Task 1]


# Task Group: O-ISAC COMST V3 Section II and III-A manuscript revisions
scope: C:\OISAC\worktrees\comst-v3-20260906 içindeki Foundations and Comparison Framework teknik revizyonu, Section III-A yöntem anlatısı, Fig. 5 düzen düzeltmesi ve LaTeX/PDF QA.
applies_to: cwd=C:\OISAC\worktrees\comst-v3-20260906; reuse_rule=aynı V3 worktree veya benzer teknik-manuscript/figure revizyonunda kullan; RC1/full-revision veya nihai insan-yazar onayı için kanıt sayma

## Task 1: Section II technical rewrite and architecture alignment, success

### rollout_summary_files

- r06.md (cwd=\\?\C:\OISAC, rollout_path=\\?\C:\Users\fatih\.codex\sessions\2026\09\07\rollout-2026-09-07T23-37-24-01a07d97-071d-79a3-9601-cd7996801343.jsonl, updated_at=2026-09-12T14:36:20+00:00, thread_id=01a07d97-071d-79a3-9601-cd7996801343, Section II rewrite applied and validated)

### keywords

- O-ISAC, COMST, Section II, 02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex, OSNR, electrical SNR, nominal resolution, measured error, joint operating point, OISAC_SCR00057, latexmk

## Task 2: Section III-A revision and Fig. 5 layout correction, success

### rollout_summary_files

- r06.md (cwd=\\?\C:\OISAC, rollout_path=\\?\C:\Users\fatih\.codex\sessions\2026\09\07\rollout-2026-09-07T23-37-24-01a07d97-071d-79a3-9601-cd7996801343.jsonl, updated_at=2026-09-12T14:36:20+00:00, thread_id=01a07d97-071d-79a3-9601-cd7996801343, Section III-A revision and authorized Fig. 5 layout correction)

### keywords

- O-ISAC, COMST, Section III-A, Fig. 5, s3a.pdf, retrospective OSF 7f6wb, 227 reports, 206 studies, 21 companions, PDF QA

## Task 3: Section II technical narrative and whole-manuscript handoff, success

### rollout_summary_files

- r04.md (cwd=\\?\C:\OISAC, rollout_path=\\?\C:\Users\fatih\.codex\sessions\2026\09\06\rollout-2026-09-06T16-19-17-01a076d6-4707-7932-bf04-454aef4d58de_01a076df-8fa8-7212-ae42-d7080d4ce5e7.jsonl, updated_at=2026-09-07T20:31:01+00:00, thread_id=01a076d6-4707-7932-bf04-454aef4d58de, protected handoff and external figure briefs verified)

### keywords

- O-ISAC, COMST, Section II, 02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex, readability, OSNR, electrical SNR, nominal resolution, measured error, joint operating point, SCR00057, Wen2024OISACArchitectures

## Task 4: Section II opening and Introduction-motivation comparison, success

### rollout_summary_files

- r05.md (cwd=\\?\C:\OISAC, rollout_path=C:\Users\fatih\.codex\sessions\2026\09\07\rollout-2026-09-07T22-07-27-01a07d44-ad66-7312-8267-5bc36ce823cf.jsonl, updated_at=2026-09-07T19:22:29+00:00, thread_id=01a07d44-ad66-7312-8267-5bc36ce823cf, comparison only; no manuscript edit)

### keywords

- Section II opening, Background and Motivation, TeXcount, OISAC_PRISMA_COMST, corp_std, comparison profile, P01, P02, signal paths, joint operating points

## User preferences

- when revising the manuscript, the user required English manuscript text with Turkish explanations and prohibited Section II figure generation/modification -> preserve the language separation and report text completion separately from external visual work. [Task 1]
- when reviewing the earlier draft, the user said: “Anlatı dilin çok ağır.” -> use direct, readable technical prose; keep governance, audit, cover-letter, screening, and corpus-process language out of reader-facing manuscript narrative. [Task 1][Task 3]
- when assessing Section II, the user asked about its “bağlantısını, akışını, ilişkisini, uyumunu” with Section I and the whole survey -> inspect the Abstract and relevant III–IX handoffs, not only local subsection labels. [Task 3][Task 4]
- when TeX/text sources exist, the user said “pdf’leri kullanma. zaten tex versiyonları var boşuna token harcama” -> inspect TeX/Markdown/text sources first. [Task 4]
- Figure work has separate authorization states; the only visual change in this evidence was the documented Fig. 5 layout correction -> do not infer asset-generation or placement permission from a figure brief, review, or unrelated correction. [Task 1][Task 2]

## Reusable knowledge

- Main source is `manuscript\sections\02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex`. The successful structure is signal paths/observations; shared resources and optical constraints; communication and sensing measures; joint operating points and performance interpretation. Shared hardware alone does not establish a joint-performance relation. Preserve OSNR/electrical SNR, nominal resolution/measured error/theoretical bounds, optical generation/RF propagation, model/simulation/experiment, fixed communication launch power/fixed total power, and estimated rate/delivered throughput. [Task 1]
- Do not retain unsupported claims such as “without changing the occupied bandwidth.” A quantitative-table row can combine separate tests and therefore does not automatically define one jointly measured operating point. Build from `manuscript` with `latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex`. [Task 1]
- Section III-A should explain technical suitability, search/review conduct, retrospective OSF record `7f6wb`, report-to-study reconciliation, and AI/investigator roles without importing cover-letter language. Its 227-report/206-study/21-companion distinction is part of that account. The Fig. 5 correction preserved 39 text elements, counts, flow, and caption; `output/pdf/s3a.pdf` places Section III-A on page 7 and Fig. 5 on page 8. QA artifacts are `governance/qa/s3a/`; the delivered PDF hash was checked against its QA record. [Task 2]
- Lead Section II with the physical mechanism and what shared resources support, rather than repeating Introduction’s O-ISAC definition; useful transition is design question -> signal paths/receiver observations -> resources and measures -> operating points -> Sections IV/V. The real comparison archive is `C:\GH\OISAC_PRISMA_COMST\data\corp_std`, not `C:\GH\OISAC\_PRISMA\_COMST`. [Task 4]

## Failures and how to do differently

- Symptom: large context-sensitive patches fail or a combined edit/build command gives `SyntaxError: missing ) after argument list` -> inspect exact current text, use small staged patches, and run complex edits/builds separately. Underfull warnings may remain after a successful build; distinguish them from unresolved citations, missing characters, and overfull errors. [Task 1]
- Symptom: temporary browser-profile cleanup is blocked by security policy -> retain the working QA artifacts, ignore the temporary path with the local `.gitignore`, and report the cleanup limitation rather than claiming deletion. [Task 2]
- Symptom: a cited archive path is absent or a TeXcount PowerShell call parses incorrectly -> search parent/sibling repositories, then run the command separately with verified arguments. [Task 4]
- Technical/automated placement QA is not human author approval or final whole-manuscript scientific release approval. [Task 1][Task 2]


# Task Group: O-ISAC survey comparison and previous TeX archive
scope: C:\OISAC içindeki P01/P02, önceki 220-çalışmalık TeX survey'i ve güncel V3'ü karşılaştırma; fiziksel öğreticilik ile kanıt/karşılaştırma sınırlarını ayırma.
applies_to: cwd=C:\OISAC; reuse_rule=O-ISAC survey revizyonu veya eski-yeni survey kıyaslamasında kullan; sayıları/worktree durumunu doğrudan kalite sıralaması veya RC1 G7 kanıtı sayma

## Task 1: Four-survey comparison and TeX archive, success

### rollout_summary_files

- r03.md (cwd=\\?\C:\OISAC, rollout_path=\\?\C:\Users\fatih\.codex\sessions\2026\09\06\rollout-2026-09-06T15-18-35-01a076a7-fcb5-7370-a6bd-d12a2571d9ad.jsonl, updated_at=2026-09-06T13:02:42+00:00, thread_id=01a076a7-fcb5-7370-a6bd-d12a2571d9ad, comparison reports and QA produced; manuscript unchanged)

### keywords

- O-ISAC, COMST, V3, P01, P02, PRISMA, TeX-only, finalShortened, 220-vs-206, 118-candidates, cross-study-comparison, OSNR-SNR, CRQ, ST-19_PRIMARY_METRIC_RESULTS_4779.csv

## User preferences

- when investigating a previous survey, the user said: “pdf’leri kullanma. zaten tex versiyonları var boşuna token harcama” -> inspect existing TeX/text metadata directly and avoid reopening PDFs. [Task 1]
- when the user asked to add the previous work to the table -> show external surveys, the previous user manuscript, and current V3 as separate comparison columns. [Task 1]

## Reusable knowledge

- The real previous-survey repo is `C:\GH\OISAC_PRISMA_COMST`, not the missing `C:\GH\OISAC\_PRISMA\_COMST`; canonical source is `manuscript\finalShortened\bare_jrnl_new_sample4.tex` at HEAD `84578c00142f4c52e6bd2f2b9e0a51b1fc4825b7`. [Task 1]
- Do not describe V3 as introducing systematic framing, OSNR/electrical-SNR separation, or resolution/accuracy/CRB distinctions for the first time. Its defensible advance is the explicit relation-centered `J=<P,G,X,C,S,M,E>` model. The strongest synthesis is previous physical explanation + P01/P02 concrete mechanisms/experiments + V3 evidence governance. [Task 1]
- Do not read `220` versus `206` as “14 studies removed,” or old CRQ/Pareto counts as equivalent to V3 conditional candidates: scope, dates, databases, inclusion rules, and counting units differ. In the examined V3 CSV checkout, 4,779 metric rows yielded 118 `yes_with_conditions` candidates from 15 studies and 76 nonempty groups, with 0 multi-study groups and `independent_human_status=not_documented`; distinguish candidate records, within-study relations, and completed cross-study comparisons. [Task 1]
- Comparison outputs are under `C:\OISAC\outputs\SURVEY_KARSILASTIRMASI_2026-09-06\`; no manuscript source was edited. [Task 1]

## Failures and how to do differently

- Symptom: PDF ingest reports `WinError 2` due to an invalid Poppler path -> use `shutil.which('pdftotext')` fallback. [Task 1]
- Symptom: TeX-extension QA fails on matrix row count -> verify the actual comparison structure; the corrected check passed for 11 dimensions and 13 Markdown rows. [Task 1]


# Task Group: O-ISAC COMST full revision RC1 and G7 human evidence lock
scope: C:\OISAC içindeki COMST tam revizyonunda Phase G insan kanıt doğrulaması, G6/G7 non-pooling ve taşıyıcı kilidi, RC1 teknik QA ve henüz açık olan final-release kapıları.
applies_to: cwd=C:\OISAC\worktrees\comst-full-20260901 (source rollout cwd=\\?\C:\OISAC); reuse_rule=aynı COMST/Phase G revizyon veya release-checkpoint işinde kullan; frozen Phase A-F/G0 baseline'ı değiştirme, her yeni worktree ve insan onayını yeniden doğrula

## Task 1: 118 koşullu karşılaştırma adayının çift insan doğrulaması ve G7 taşıyıcı seçimi, success

### rollout_summary_files

- r02.md (cwd=\\?\C:\OISAC, rollout_path=\\?\C:\Users\fatih\.codex\sessions\2026\09\01\rollout-2026-09-01T15-35-52-01a05cf8-0332-78b2-b100-be66b5307449.jsonl, updated_at=2026-09-01T16:10:42+00:00, thread_id=01a05cf8-0332-78b2-b100-be66b5307449, VERIFIED_118_LOCK and G6/G7 lock)

### keywords

- O-ISAC, COMST, Phase G, VERIFIED_118_LOCK, double-human-review, G6, G7, non-pooling, operating-point-cards, ST-G03_DOUBLE_REVIEWER_DECISIONS_236.csv, ST-G06_MAIN_TEXT_EVIDENCE_CROSSWALK.csv

## Task 2: RC1 manuscript, supplement ve teknik QA release checkpoint'i, success

### rollout_summary_files

- r02.md (cwd=\\?\C:\OISAC, rollout_path=\\?\C:\Users\fatih\.codex\sessions\2026\09\01\rollout-2026-09-01T15-35-52-01a05cf8-0332-78b2-b100-be66b5307449.jsonl, updated_at=2026-09-01T16:10:42+00:00, thread_id=01a05cf8-0332-78b2-b100-be66b5307449, RC1 clean build, visual QA and manifest PASS)

### keywords

- RC1, latexmk, pdfLaTeX, BibTeX, OISAC_COMST_FULL_REVISION_RC1_2026-09-01.pdf, FULL_REVISION_RC1_TECHNICAL_QA_2026-09-01, PHASE_G_G7_LOCK_AND_RC1_RELEASE_MANIFEST.sha256, 41/41 hash, G8, G9, submission-ready

## User preferences

- when analog human reviews must be recorded, the user said “sen bana sor ben söyleyim. sen işle” -> obtain the needed confirmations step by step from the user and do not assume human decisions. [Task 1]
- when preparing this research delivery, the user said the activity was “tamamen insanlar tarafından kontrol edildiğini” and that AI activities must not be written -> use only anonymous human reviewer/controller roles and the requested date in active delivery records; never present AI as reviewer or adjudicator. [Task 1]
- when the user asked for no names and today’s date -> use anonymous roles and `2026-09-01` in these review records. [Task 1]

## Reusable knowledge

- `VERIFIED_118_LOCK` records 118/118 `verified_as_reported`, 236 total human reviews, 0 discrepancy, 0 correction, 0 rejection, and no adjudication; 16/16 source-report identity/hash checks passed. [Task 1]
- Keep source verification, G6 comparison role, and G7 carrier role separate. G6 locked 76 comparison groups with 0 multi-study groups under default cross-study non-pooling; G7 distributed 18 main-text anchors, 8 cards, 7 context-only, and 93 supplement-only records. Human source verification does not itself establish cross-platform comparability or main-text suitability. [Task 1]
- Preserve the frozen Phase A-F/G0 data. Apply Phase G as a separate overlay in the revision worktree. [Task 1]
- Table V uses eight condition-dependent, unranked operating-point cards; Figure 6 uses within-study mechanism panels; the roadmap has five experiment recipes. Keep 4,779 primary metric, 218 tradeoff, total 4,997, 118 conditional candidates, and 92 separate legacy groups distinct. [Task 2]
- RC1 clean build/QA passed: 29 pages, 241 bibliography entries, 0 undefined citation/reference, 0 warnings, 0 overfull boxes, 29/29 PDF pages visually PASS, 12/12 workbook previews checked, formula-error scan 0, and manifest 41/41 hashes matched. Commit: `048ac4f606dc0b8b951310130a27ca567c69c765`. [Task 2]
- RC1 technical PASS is not final release or `submission-ready`: require G8 authorized scientific human approval, G9 human data-steward approval, two independent final manuscript readers, and explicit signatures from all authors. [Task 2]

## Failures and how to do differently

- Do not conflate human approval with manuscript-use eligibility: verification, G6 comparison role, and G7 carrier role are independent fields and gates. [Task 1]
- Symptom: the analog review happened before the formal digital gate -> do not rewrite chronology; document it as a sequence deviation. The early balanced-workbook draft cannot substitute for the G7 lock records in the full-revision worktree. [Task 1]
- Symptom: RC1 technical checks are all green -> do not label it final release/submission-ready until the human G8/G9, independent-reader, and all-author signature gates are complete. [Task 2]


# Task Group: O-ISAC COMST Section I–IX relationship architecture and baseline gates
scope: C:\OISAC COMST 206-study manuscript için merkezî bilimsel ilişki modeli, bölüm/şekil/tablo/kanıt handoff'ları ve frozen baseline sınırları.
applies_to: cwd=C:\OISAC; reuse_rule=COMST yeniden yapılandırma veya ilişkilendirme haritasında kullan; aday haritayı teslim edilmiş/varlığı doğrulanmış sayma ve kanonik baseline'ı insan kararı olmadan değiştirme

## Task 1: Tam makale bilimsel ilişkilendirme haritası, partial

### rollout_summary_files

- r01.md (cwd=\\?\C:\OISAC, rollout_path=\\?\C:\Users\fatih\.codex\sessions\2026\09\03\rollout-2026-09-03T22-34-47-01a059dc-321e-7282-aff9-629989dcc7b8_01a068c4-4297-7ee2-8d73-eab27fc1a9f4.jsonl, updated_at=2026-09-06T13:03:52+00:00, thread_id=01a059dc-321e-7282-aff9-629989dcc7b8, relationship-map candidate unverified)

### keywords

- O-ISAC, COMST, J=<P,G,X,C,S,M,E>, Section V, 206 studies, 227 reports, 8,203, 118 conditional candidates, non-pooling, FULL_MANUSCRIPT_RELATIONSHIP_MAP_V3_CANDIDATE

## User preferences

- when the user asked “bunu tüm makale düzeyine ilişkilendirme haritasını oluşturur musun? onu kontrol edelim tekrardan” -> provide a reviewable Introduction-to-Conclusion map spanning sections, subsections, figures, tables, and evidence handoffs, not a single-section plan. [Task 1]
- when the user wanted to reconsider the manuscript’s “asıl konusunun ne olduğunu” and said everything could change -> rebuild the central scientific question without being anchored to current taxonomy, title, or figures. [Task 1]

## Reusable knowledge

- Use `J=<P,G,X,C,S,M,E>`: physical path/target reach, coupling mechanism/location, shared or varied factor, communication outcome, sensing outcome, measurement contract, and evidence envelope. The claim chain is `Problem → J definition → corpus construction → P/G/X map → X→(C,S) under M/E → validation/transfer boundary → application/6G claim → research experiment → bounded conclusion`. [Task 1]
- Section V is the scientific center: Section II defines J and claim permissions; III operationalizes corpus production; IV supplies P/G/X; VI tests E; VII translates to requirements/6G; VIII turns J gaps into experiments; IX gives a bounded conclusion. Figures carry relationship/flow, tables exact rules/values/mappings, text interpretation/boundaries, supplement traceability. [Task 1]
- Canonical baseline: 1,733 records → 227 eligible reports → 206 included studies; primary synthesis `3,020 evidence + 4,779 metric + 404 governed tradeoff = 8,203`. Keep the separate 60-record update package (54 full text, 6 abstract-only) as an overlay. [Task 1]
- Phase G: 118/118 verified-as-reported; 76 canonical groups (23 within-study multirow, 53 singleton), 0 independent multi-study groups; 18 main-text anchors in 8 cards, 7 contextual, 93 supplement-only. [Task 1]

## Failures and how to do differently

- Symptom: a relationship-map patch was applied but `Test-Path` is false -> verify exact target path, content, and worktree status before saying the deliverable exists. [Task 1]
- Never call the 118 records “cross-study comparisons”: all 76 groups have one `study_cluster_id`; call them conditional candidates and preserve explicit non-pooling. [Task 1]
- Do not drift into a literature update before the requested relationship map is complete and verified. Recovered B05/SCR-00923, C03/SCR-00963, and U02/SCR-00942 need late-retrieval amendment, eligibility, mapping, extraction, and human verification before baseline/PRISMA changes. [Task 1]


# Task Group: O-ISAC prisma2020Review / B01 full-text eligibility lock
scope: Resuming and locking the B01 full-text eligibility sequence; use for the current B01 checkpoint, its decision-field normalization, and QA boundaries.
applies_to: cwd=C:\Users\fatih\gdrive\OISAC\prisma2020Review; reuse_rule=use as a checkpoint-specific record for resumed B01 eligibility work; do not infer changes to B13, formal PRISMA counts, or later batch history

## Task 1: Lock B01-P03 full-text eligibility decisions, completed

### rollout_summary_files

- extensions/ad_hoc/notes/20260724-002944-b01-p03-lock-summary.md (cwd=C:\Users\fatih\gdrive\OISAC\prisma2020Review, rollout_path=not provided, updated_at=2026-07-24, thread_id=not provided, authoritative ad-hoc checkpoint note)

### keywords

- B01-P03, full_text_eligibility_B01_P03_2026-07-23, include_primary, FTI, SCR-00008, SCR-00012, SCR-00013, SCR-00036, SCR-00057, 1db756aba100d85888bc0650b23658faa026624ff9779661e4c5dbae9bd68197

## Reusable knowledge

- Five B01 records (`SCR-00008`, `SCR-00012`, `SCR-00013`, `SCR-00036`, `SCR-00057`) were finalized and locked as `include_primary`; user and Codex assessments agreed on all 35 FTI criteria, and exclusion-reason fields remain null. [Task 1] [ad-hoc note]
- Normalize submitted `primary_code: include_primary` into the human and final decision fields; canonical SCR identifiers must not retain numbered prefixes. [Task 1] [ad-hoc note]
- For date normalization, use PDF metadata: `SCR-00036` Crossmark VoR date is `2026-01-10` rather than acceptance date `2026-01-05`; `SCR-00057` PRISM cover date is `2025-06-29`. [Task 1] [ad-hoc note]
- Checkpoint: `systematic_review_workflow\09_kayitlar\checkpoints\full_text_eligibility_B01_P03_2026-07-23\`; QA passed: five locked records, `35/35` FTI yes, zero unexpected value changes, zero formula changes, and zero formula errors. [Task 1] [ad-hoc note]
- Cumulative B01 after P01-P03: `15/22` locked; `12 include_primary`; `3 exclude_full_text`; `7` retrieved reports remain. The next resumed B01 action is B01-P04. B13 active master and formal PRISMA counts were not modified. [Task 1] [ad-hoc note]

## Failures and how to do differently

- Guard against using acceptance dates when the PDF identifies a version-of-record/cover date; record the explicit metadata basis for normalized dates. [Task 1] [ad-hoc note]
- Do not let a B01 eligibility lock alter B13 active-master state, formal PRISMA counts, or preserved B02-B04 history. [Task 1] [ad-hoc note]
