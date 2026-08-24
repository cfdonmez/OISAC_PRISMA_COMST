# PROJECT_CONTEXT_OISAC_PRISMA.md

## Current Workflow State

### CURRENT RESUME AUTHORITY — Final Submission Closeout, 2026-08-24

- Kullanıcı bütün manuscript için son submission denetimini ve Figures 1--8'in
  tamamlanmasını onayladı.
- İlk güvenlik tabanı `codex/final-submission-20260824` dalında hazırlanır. Uzak
  depodaki `agent/full-corpus-survey-ready` dalı ve
  `9b29b221213786c9893134a36638c3d9a0739f49` başı değiştirilmeden korunur.
- Çalışma klasöründeki boş `.git` dizini ayrı bir yerel backup konumuna taşındı
  ve uzak geçmiş yalnız Git metadatası üzerinden geri bağlandı. Çalışma
  dosyalarının hiçbiri klondan alınmadı veya üzerine yazılmadı.
- Pre-edit manuscript tabanı 23 sayfa, 203,407 byte, 241 bibliography entry ve
  SHA-256
  `A258E699084D190186298EA95D279E459A75D5F9B9881EC2EF9DC03F505C5E35` olarak
  doğrulandı.
- Operasyon sırası güvenlik push'u, tam metin ve abbreviation audit'i, bütünsel
  prose revision, evidence/build/render QA, deterministic vector figure
  production ve final push'tur.
- Güncel checkpoint
  `systematic_review_workflow/09_kayitlar/checkpoints/final_submission_baseline_2026-08-24/README.md`
  dosyasıdır.

Bu authority, aşağıdaki 2026-08-19 author-reread durumunun yerini alır.

### CURRENT RESUME AUTHORITY — 2026-08-19, updated 2026-08-24

- Active title in `main.tex`: *Optical Integrated Sensing and Communication
  for 6G: A Systematic Review and Survey of Architectures, Metrics, and
  Tradeoffs Across Optical Platforms*.
- Active manuscript authority:
  `systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- Current PDF: 23 pages; 203,337 bytes; Tables I--VIII live; Figures 1--8 pending; 243
  bibliography entries; 206/206 included studies cited; ST-01 resolves all
  227 reports. PDF SHA-256:
  `4467D5816FA20A1A0D0E64B11A9EC0997EC786D168F04AE83582056DB4D3CBC8`.
- Current supplement: `OISAC_COMST_SUPPLEMENT_FINAL_V10_2026-08-17.zip`;
  42 entries; SHA-256
  `4f140851568a667ac0b9dde0b57c104742b0f747f2abb28335cffe37fe61617d`.
- Author reading: Abstract is deferred until the end; Sections I--IV are
  approved. Section V author reading is complete.
  Conditions for Comparison Across Studies closes V-D in 130 words, two
  paragraphs, and nine sentences. Its
  prohibited style marker count is zero, and the table/prose carrier separation
  remains intact. Section VI has been revised and technically verified as one
  survey unit. It awaits author rereading and approval, followed by Sections
  VII--IX.
- Section IV now contains 1,880 TeXcount text words, down from 2,880 by 1,000
  words (34.7%), in 25 prose paragraphs and 113 sentences. Table IV carries the
  exclusive family counts, task inventory, principal constraints, and transfer
  conditions. Family prose carries mechanism, recurring pattern, and
  engineering interpretation. The revised fiber, VLC/LiFi, free space optical,
  and hybrid/residual units total 564 words in eight paragraphs. Section IV-B
  now uses 678 words in ten paragraphs to explain coupling location, recurring
  mechanism, engineering consequence, and evidence form.
- Planned Fig. 5 remains restricted to the seven overlapping integration
  locations, their locked counts, and three mixed boundary cases. When active,
  it replaces the current numerical coupling inventory rather than duplicating
  it. Section IV contains 71 unique included-study keys in 56 citation commands.
  The cross-platform close uses four compact citation clusters for its concrete
  platform and shared-constraint claims. The regenerated crosswalk reports
  206/206 studies cited, zero missing, 415 included-study citation uses, 197 citation commands, and no cluster above
  seven. Table IV and pages
  5--10 passed rendered QA; undefined/fatal/overfull findings remain zero.
- The Section V opening now contains 159 words in three paragraphs and ten
  sentences. The opening, V-A lead, Table V, and its immediate interpretation
  use positive analytical roles without author-inserted semicolons, colons, or
  negative-marker cadence. The 4,779 denominator, overlapping 85/60/50 study
  coverage, and exact 118/4,661 analytical split remain unchanged. Table V is
  now a compact single-column survey map with five metric-domain rows and two
  analytical-role rows. It appears on PDF page 8 in source order between V-A
  and V-B. Section V-B owns metric semantics, S-Evidence owns record detail,
  and planned Fig. 6 owns tradeoff distributions. Pages 8--10 pass rendered QA.
  Metrics Across Functions is now complete. Communication Metrics uses 326 words
  in four paragraphs for rate accounting, reliability, measurement plane, and
  spatial or temporal scope. Sensing Metrics uses 275 words in four paragraphs
  for task definition, estimation evidence, dataset and decision context, and
  comparison conditions. Joint and Implementation Metrics uses 249 words in
  three paragraphs for matched or resource-linked evidence, model-bounded
  optimization, and platform burden. All retained study anchors remain claim
  adjacent and preserve their evidence settings. The revised units contain no
  author colon, semicolon, or defensive negative marker. How Communication and
  Sensing Performance Interact now uses 2,262 prose words in 30 paragraphs and
  149 sentences and preserves all 176 prior citation keys and 180 citation uses.
  Its two-paragraph opening explains the shared resources before introducing
  the evidence scope. The narrative then follows shared design choice, observed
  response, source condition, and engineering meaning, while planned Fig. 6
  owns the detailed family profile. Current Section V TeXcount text is 3,562
  words. The refreshed
  citation package remains 206/206 PASS, zero missing, 415 included-study uses,
  197 commands, and maximum cluster 7. The crosswalk CSV SHA-256 is
  `63C6343A57A18267CC9253BC09647D80130C97D2842694B12B9F6A3F5A14C5B9`,
  and the XLSX SHA-256 is
  `49EABFFABB9DC5B01FB3FECB467330714FE079E48E67686800023F56C6E3428B`.
  The Section V source SHA-256 is
  `D733C6CC379DC648CF058211F0A99146890BB8DFE772865829611F6D33FC12AF`.
- Table II and its linked Section II prose now use the same compact survey-map
  allocation. Four comparison components and three analytical uses remain in
  the reader-facing table, while exact fields, states, provenance, and
  rationales remain in S-Data Dictionary and S-Evidence. Section II contains
  711 prose words in 12 paragraphs and 46 sentences. Table II renders cleanly
  on page 3 between subsections II-B and II-C.
- Section III continues to provide the concise PRISMA/evidence bridge approved
  by the author. AI review-conduct narrative is absent from Sections I--IX;
  mandatory disclosure remains only in
  `sections/10_REPORTING_DECLARATIONS.tex`.
- Section VI now follows four reader questions covering validation settings
  and methods, field evidence across both functional domains, artifact access
  and reconstructability, and benchmark readiness. Table VI is a compact
  observed-access map. Planned Fig. 7 retains the exclusive setting and
  overlapping method distributions. The S7 boundary is explicit. Six of the
  12 field or deployment studies report outcomes in both domains, while timing
  and separate function locators remain unresolved. The section contains 1,300
  style-audit words with a mean sentence length of 16.049 and zero
  author-inserted colon, semicolon, `neither`, or avoidable alphabetic hyphen.
  Its source SHA-256 is
  `441D1767C96A8FAFA41C015C5E1C60880A4AE861897DC46AAA50AF764CB7B11C`.
- Governing current-text QA:
  `qa/SECTION6_VALIDATION_RECONSTRUCTABILITY_SURVEY_FIRST_QA_2026-08-24.md/json`
  for Section VI,
  `qa/SECTION5_TRADEOFF_MECHANISMS_SURVEY_FIRST_QA_2026-08-24.md/json` for V-C,
  `qa/SECTION5_CROSS_STUDY_COMPARISON_QA_2026-08-24.md/json` for V-D,
  `qa/SECTION2_TABLE2_SURVEY_MAP_QA_2026-08-21.md/json` for Section II/Table II
  and `qa/SECTION5_TABLE5_SURVEY_MAP_QA_2026-08-21.md/json` for Section V/Table
  V. The approved opening
  baseline remains `qa/SECTION5_OPENING_SURVEY_FIRST_QA_2026-08-21.md/json`.
  Approved Section IV
  remains governed by `qa/SECTION4_SURVEY_FIRST_QA_2026-08-20.md/json`. The approved Section III
  snapshot remains `qa/SECTION3_AUTHOR_REREAD_PREP_QA_2026-08-19.md/json`.
- Exact next operation: reread the revised Section VI in whole-section context
  and retain `awaiting author approval` until the author accepts it.
  Abstract remains last; figures follow prose approval.
- Full durable memory/rule map:
  `systematic_review_workflow/09_kayitlar/codex_memory_bank.md`, section
  `CURRENT RESUME AUTHORITY — 2026-08-19`.
- Standalone checkpoint:
  `systematic_review_workflow/09_kayitlar/checkpoints/comst_memory_handoff_2026-08-19/README.md`.

> All current/next blocks below are dated audit snapshots and are superseded
> operationally by this 2026-08-19 block, although their scoped scientific or
> editorial findings may remain valid.

### COMST v2 Section III survey-first compression — 2026-08-17

- Active manuscript authority remains `systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- Section III now contains 527 prose words excluding Table III and internal
  figure specifications. It has three reader jobs: corpus construction,
  evidence use, and technical appraisal/synthesis.
- PRISMA is identified without being taught. Search history, registration
  chronology, conduct detail, scoring caps, and evidence-body thresholds are
  kept in the named supplements.
- No AI review-conduct narrative remains in Sections I--IX; the required
  disclosure remains separately in the acknowledgment.
- The active 27-page PDF has eight live tables, 243 bibliography entries, and
  claim-matched citations for all 206 included studies. ST-01 resolves all 227
  eligible reports.
- Current package: `OISAC_COMST_SUPPLEMENT_FINAL_V10_2026-08-17.zip`; SHA-256
  `4f140851568a667ac0b9dde0b57c104742b0f747f2abb28335cffe37fe61617d`.
- Governing QA:
  `qa/FINAL_SECTION3_SURVEY_FIRST_QA_2026-08-17.md/json`; checkpoint:
  `systematic_review_workflow/09_kayitlar/checkpoints/comst_section3_survey_first_2026-08-17/README.md`.
- Figures 1--8 and the final figure-inclusive build/layout pass remain.

> The Table I/contribution block immediately below is retained as a dated
> snapshot and is operationally superseded by this block.

### COMST v2 Table I and contribution closeout — 2026-08-17

- Active manuscript authority remains `systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- The active 29-page PDF has nine sections, eight live tables, 243 bibliography
  entries, and claim-matched citations for all 206 included studies.
- Table I now stands on its own with 24 directly cited prior syntheses. Its
  former ST-RS1 note was removed.
- The four contribution bullets are noun-led scientific deliverables; no item
  begins with `We`.
- The 38-source contextual-synthesis matrix is retained only as an internal
  positioning audit. It is not an annex and is excluded from the submission
  supplement; ST-01 still carries the 206-study and 227-report traceability.
- Current package: `OISAC_COMST_SUPPLEMENT_FINAL_V7_2026-08-17.zip`; SHA-256
  `09def1dea6cb3b2a9bc49ef4c80d99a9193fb930888807a4217718bd4e049548`.
- Governing QA:
  `qa/FINAL_TABLE1_CONTRIBUTION_QA_2026-08-17.md/json`; checkpoint:
  `systematic_review_workflow/09_kayitlar/checkpoints/comst_table1_contributions_2026-08-17/README.md`.
- Figures 1--8 and the final figure-inclusive build/layout pass remain.

> The 2026-08-16 citation-complete block immediately below is retained as a
> dated snapshot and is operationally superseded by this block.

### COMST v2 citation-complete closeout — 2026-08-16

- Active manuscript authority: `systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- The survey has nine main sections. Its active compiled PDF is 29 pages, with
  eight live main-text tables and a 243-entry main bibliography.
- All 206 included studies are cited in scientifically matched main-text
  contexts. The main bibliography also contains 29 contextual or
  methodological sources and eight companion reports used for report-specific
  claims.
- Figures 1--8 are the sole missing manuscript content assets. After insertion,
  run one figure-inclusive compile, cross-reference check, rendered-page
  inspection, and final layout pass.
- ST-01 is a standalone 42-page supplement covering 206/206 included studies
  and 227 eligible reports: 206 primary reports plus 21 companion reports, all
  with resolvable report keys.
- Supplemental package V6 is
  `OISAC_COMST_SUPPLEMENT_FINAL_V6_2026-08-16.zip`; SHA-256
  `b0c5d7d636fedaa21b85de1087ba441521a15d7c98e535213e84d48d4a63f65b`.
- The unpublished 220/221-study manuscript remains historical. The OSF
  221-study record is a superseded predecessor snapshot, not direct attrition
  to 206.
- Governing QA:
  `qa/FINAL_CITATION_COMPLETION_QA_2026-08-16.md/json` under the active
  manuscript. Checkpoint:
  `systematic_review_workflow/09_kayitlar/checkpoints/comst_citation_complete_2026-08-16/README.md`.

> The 2026-08-14 nonvisual-closeout block immediately below is retained as a
> dated snapshot and is operationally superseded by this block.

### COMST v2 nonvisual closeout â€” 2026-08-14

- Active manuscript authority: `systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- The survey has nine main sections. Its active compiled PDF is 27 pages, with
  eight live main-text tables and 106 directly cited main-manuscript
  references.
- Figures 1--8 are the sole missing manuscript content assets. Their
  specifications are frozen; after they are produced and inserted, the page
  budget, cross-references, compile log, and all rendered pages must be checked
  again.
- ST-01 is a standalone supplement covering 206/206 included studies and the
  distinct 227-eligible-report lineage: 206 primary reports plus 21 companion
  reports.
- Supplemental package V4 was generated after final QA as
  `OISAC_COMST_SUPPLEMENT_FINAL_V4_2026-08-14.zip`; its SHA-256 is
  `3fe1304da89690a749a4527ccf28e16d7dd615b8ab1c259cb26a41783cda3f5f`.
- The unpublished 220/221-study manuscript remains historical and is not a
  scientific or editorial authority for v2. The OSF 221-study record is a
  superseded predecessor snapshot, not a direct attrition step to 206.
- Current operation: produce and integrate the eight contracted figures, then
  repeat page-budget and rendered-document QA. Do not reopen locked Phase C--F
  counts or treat historical roadmaps below as current instructions.
- Checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/comst_nonvisual_closeout_2026-08-14/README.md`.

### Previous verified Phase Aâ€“F full-corpus state and PRISMA closure gate â€” 2026-08-07

- Registration correction (2026-08-07): the review lineage was retrospectively registered on OSF on 12 February 2026 (`7f6wb`; DOI `10.17605/OSF.IO/7F6WB`). Search/screening were already complete and synthesis/manuscript drafting had begun; prospective preregistration must not be claimed.
- The registered 221-study state is a superseded predecessor snapshot with different dates, sources, procedures and denominators. The final executed state remains 227 eligible reports mapped to 206 studies; the values are not a direct attrition sequence.
- Registration-lineage amendment: `systematic_review_workflow/01_protokol/04_protocol_registration_lineage_correction_2026-08-07.md`; checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_registration_lineage_correction_2026-08-07/`.

- Phases Aâ€“C remain locked: 1,733 records identified, 1,259 screened, 330 unique reports sought, 58 not retrieved, 272 assessed, 227 included reports and **206 included studies**.
- Phase D source extraction and claim-governed survey-use adjudication are complete for all 206 studies: 3,041 evidence items, 4,861 metric rows and 404 trade-off rows (**8,306 claims**).
- Survey-use disposition: 3,206 qualitative, 4,997 quantitative, 31 context-only and 72 quarantined exact claims. Study status: 175 survey-ready and 31 survey-ready with claim restrictions.
- Canonical workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_survey_ready_2026-08-04/OISAC_PHASE_D_SURVEY_READY_2026-08-04.xlsx`; SHA-256 `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`; independent QA = PASS.
- Provenance boundary: the survey-use layer is AI-assisted and user-delegated; `independent_human_status = not_documented`. It must not be reported as independent duplicate human review.
- Exact source conflicts are quarantined at claim level; unaffected study evidence remains usable. No conflicting value is silently averaged or replaced.
- Phase E TQAF is complete for 206/206 studies: overall contribution 6 low, 75 adequate and 125 strong; 115 S1â€“S7 evidence bodies have certainty 54 high, 47 moderate, 10 limited and 4 unclear; QA PASS 43/43.
- Phase-E final-workbook invariance audit PASS: 206 studies, 46 check families, 9,476 comparisons, 0 mismatches and 0 failed studies.
- Phase F S1â€“S7 synthesis is complete. Primary synthesis uses 8,203 claims (3,020 evidence + 4,779 metric + 404 trade-off). The inclusive 8,234 non-quarantined universe contains 31 context-only metrics and is not the primary denominator. Internal QA PASS and independent artifact QA PASS 29/29.
- Multi-label `other` is fallback-only: integration=0, enabling technology=19 and application=15, with no recognized-category co-label violation.
- Phase-G writing package is complete: English Abstract, Methods, PRISMA Results, claim-governance, TQAF, S1â€“S7, Discussion/Conclusion, and a QA-passed appendix with 206 unique study rows and separate 227-report lineage.
- Final package-level status: `PASS_FOR_REVIEWED_MANUSCRIPT_INTEGRATION`; this does not claim submission readiness.
- A separate PRISMA 2020 working compliance matrix now covers all 42 checklist rows without changing the original checklist: `systematic_review_workflow/07_raporlama/03_prisma_2020_madde_artefakt_manuscript_uyum_matrisi_2026-08-05.md`. After the user's 2026-08-06 declarations and the 2026-08-07 OSF registration-lineage correction, artefact status = 16 ready, 20 partial, 4 justified non-applicable and 2 open; active manuscript integration = 0/42.
- English gap-closure passages are isolated in `systematic_review_workflow/07_raporlama/04_prisma_2020_gap_closure_drafts_EN_2026-08-05.md`. They preserve explicit placeholders for author-owned declarations, verified citations, supplements and persistent repository details.
- Working-gate checkpoint/QA: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_compliance_working_gate_2026-08-05/`. The original checklist and protected manuscript were not modified; no LaTeX compilation was performed.
- Item 25 author-declaration checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_item25_support_declaration_2026-08-06/`.
- Item 26 author-declaration checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_item26_competing_interests_declaration_2026-08-06/`.
- Item 9 author-contact checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_2020_item9_author_contact_boundary_2026-08-06/`.
- Git delivery: `agent/full-corpus-survey-ready`, scientific package commit `2292bfdb3021a3e1dd495ecaa89953350d494405`, delivery-record head `9b29b221213786c9893134a36638c3d9a0739f49`, draft PR `https://github.com/cfdonmez/OISAC_PRISMA_COMST/pull/1`.
- Item 9 author-contact boundary is confirmed: authors of included studies were not contacted; weekly meetings were internal review-team discussions with verbal methodological verification and are not reported as study-author data verification.
- Current operation: resolve the remaining method-text, supplement/pointer, verified external-citation and repository-availability gaps; only then integrate the approved dated package into the protected active manuscript. Legacy 220/221-derived material must be regenerated, not mechanically renumbered.

> The pre-closeout Phase-D progress statements below are retained as dated audit history and are operationally superseded by this block.

- Active baseline: `systematic_review_workflow/03_secim/title_abstract_screening/batch_B13_final_2026-06-22/title_abstract_screening_form_MASTER_BATCH_B13_APPLIED_2026-06-22.csv`.
- Baseline status: title_abstract_screening_complete; post_title_abstract_final_checkpoint_created.
- Canonical operational handoff and forward roadmap: `START_HERE_OISAC_PRISMA_CURRENT.md`. Every new agent/chat/computer must read that file before acting.
- Current step: **Phase D â€” continue corpus extraction after the first-25 human lock**. Phases A, B and C are complete.
- Step 5-C26 completed B13 human/User/ChatGPT title/abstract screening decisions and created the B13-applied master copy.
- Step 5-C27 confirmed master integrity: total records = 1259, unique `screening_record_id` = 1259, duplicate IDs = 0.
- Resolved title/abstract decisions: 1259 / 1259.
- Remaining `not_screened`: 0.
- Final title/abstract decision distribution: `exclude_title_abstract` = 864, `include_for_full_text` = 321, `contextual_only` = 61, `unclear_need_full_text` = 11, `duplicate_or_related_report_flag` = 2.
- Full-text-needed pool: 332 records (`include_for_full_text` + `unclear_need_full_text`).
- Phase C identification and screening counts are locked: 1,733 records identified; 472 duplicates and 2 records removed for other reasons before screening; 1,259 records screened; 927 did not advance to retrieval.
- The formal PRISMA flow uses the deduplicated unique-report layer: 330 reports sought, 58 not retrieved and 272 assessed. The historical source-record audit remains preserved at 332/60/272; two post-screening bibliographic aliases explain the difference.
- Contextual corpus: 67 records in total (61 retained after title/abstract screening and 6 after full-text assessment); not primary technical evidence.
- The original three-record related-report/version watchlist is historical; the authoritative report relationships are now in the final Phase B mapping register.
- Retrieval alias reconciliation: `SCR-01150` is an alias of retrieved `SCR-00886`, and `SCR-00669` is a bibliographic alias of external canonical record `SCR-00373`.
- Phase A final eligibility: 272/272 locked; 227 `include_primary`, 39 `exclude_full_text`, 6 `retain_contextual`, unresolved/HOLD = 0.
- Phase B final mapping: 272 reports â†’ 247 ledger-bearing clusters; 227 eligible reports â†’ **206 included studies**; total reduction = 21 (Phase A 18 + new Phase B 3); 50 `RPT02` rows; pending/HOLD = 0.
- The 39 full-text exclusion reasons reconcile exactly: FTX01 = 4, FTX02 = 2, FTX03 = 12, FTX04 = 5, FTX06 = 4 and FTX07 = 12.
- PB01-PB12 and PBD-01-PBD-09 carry delegated human approval. The final package and PASS QA are under `systematic_review_workflow/09_kayitlar/checkpoints/report_to_study_mapping_PHASE_B_FINAL_LOCK_2026-07-30/`.
- Phase C versioned counts, the populated PRISMA flow, Item 16a/16b register, reconciliation workbook, QA and manifest are under `systematic_review_workflow/09_kayitlar/checkpoints/prisma_flow_PHASE_C_FINAL_2026-07-30/`; final QA = PASS.
- Phase D pre-pilot setup is complete: a 206-study baseline, 232-row report/version lineage layer, evidence/metric/tradeoff schemas, controlled codebook, five-study pilot set and human checklist are in `systematic_review_workflow/04_veri_cekme/outputs/phase_d_setup_2026-07-30/OISAC_PHASE_D_EXTRACTION_BASELINE_2026-07-30.xlsx`; baseline QA = PASS.
- P01â€“P05 are human-approved and locked: 5/5 studies, 85/85 checklist items passed and 0 open pilot items. The pilot-locked v1.0 schema/codebook is active and the post-pilot extraction gate is open.
- The first post-pilot batch is source-extracted for 20 studies / 21 PDFs: 208 evidence items, 178 metric results, 26 trade-off records and 340 HC01â€“HC17 rows. Under the user's explicit delegation, all 20 received final human adjudication and were locked with report-specific caveats, `NR`, `UNC` and conflicts preserved.
- Cumulative Phase D progress is 25/206 source-extracted and 25/206 user-delegated human-approved/locked. This wording records authorization of the AI-assisted, source-open adjudication; it does not claim that the user personally opened or read every PDF. TQAF and synthesis have not started.
- AI suggestions are provisional only and are not final screening decisions; final title/abstract decisions are human/User/ChatGPT decisions.

## 2026-08-02 Phase D First-25 User-Delegated Human Lock

- Canonical pilot workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_pilot_human_locked_2026-08-02/OISAC_PHASE_D_PILOT_HUMAN_LOCKED_2026-08-02.xlsx`; SHA-256 `69462bd05f66c39172494b5e984ee6c245220720ba18027eb1145a0ab77db672`.
- Pilot checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_PILOT_HUMAN_LOCK_2026-08-02/`.
- Canonical first-25 workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_25_human_locked_2026-08-02/OISAC_PHASE_D_25_STUDIES_HUMAN_LOCKED_2026-08-02.xlsx`; SHA-256 `794ae6c74f61c5b9310e859559f39dd08cd0c1639fa9f53a29b213bbf64f48ca`.
- Final checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_25_HUMAN_LOCKED_2026-08-02/`.
- Final QA = PASS: 25/25 extracted studies are human-approved and locked (5 pilot + 20 post-pilot); the Batch-20 portion contains 21 PDFs, 208 evidence rows, 178 metric rows, 26 trade-off rows and 340 completed HC rows. Formula errors = 0, project graph digitization = 0 and Phase E TQAF scores = 0.
- The Batch-20 lock is user-delegated final approval of an AI-assisted source-open review. It is not evidence that the user personally read each PDF. The 21 PDF-specific Gemini audits and source-open extraction evidence are retained as provenance; the later folder-level Gemini answer is secondary only because it was not consistently grounded in the target PDFs.
- Next operation: continue Phase D extraction for the remaining 181/206 studies in versioned batches under the locked schema and the same caveat-preserving audit model. TQAF and synthesis remain not started.

## 2026-07-30 Phase D Pre-Pilot Baseline

- Extraction unit is the locked Phase B `study_cluster_id`; the baseline contains 206 unique included studies and 206 unique designated primary extraction reports.
- The workbook preserves 227 eligible reports and a 232-row known lineage layer: 227 eligible reports, 2 related excluded reports and 3 outside-272 alias/version records.
- Eligible report-family distribution is 187 single-report, 17 two-report and 2 three-report studies; 19 included-study families therefore contain more than one eligible report.
- Source integrity QA passed: 227/227 eligible PDFs and 206/206 primary extraction PDFs exist, are readable and have valid PDF signatures.
- Data are separated into study-level master, report lineage, evidence-item, metric-result and tradeoff-evidence tables. Important values require report/page provenance.
- Blank means not reviewed; assessed missingness uses `reported / NR / NA / UNC`. Calculated or figure-digitized values require method, formula and input lineage; unsupported inference is prohibited.
- Phase D stores raw validation, reproducibility and benchmark evidence only. TQAF 0â€“3/NA scoring and qualitative evidence-strength labels remain Phase E work.
- Pilot set: `SCR-00007`, `SCR-00008`, two-report family primary `SCR-00083`, `SCR-00941` and `SCR-00196`; 5 studies / 6 eligible PDFs.
- Checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_SETUP_2026-07-30/`.
- Next operation: complete source-open P01 human review in `08_HUMAN_CHECKLIST` (`HC01â€“HC17`) and resolve `QAL-004â€“QAL-006`; proceed to P02 only after P01 approval or revision closure.

## Historical intermediate checkpoint â€” 2026-07-30 Phase D Pilot P01

- Active pilot workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_pilot_2026-07-30/OISAC_PHASE_D_PILOT_WORKBOOK_2026-07-30.xlsx`.
- Workbook SHA-256: `27eb72384918b108698a248f3feb144ce947456049309548d47b76b4724a3c41`.
- P01 source: `SCR-00007`, 15-page original PDF; cluster `STC-SINGLETON-SCR-00007`.
- AI-assisted extraction populated 66 evidence items, 6 metric results and 2 tradeoff records with report/page/section/table/figure/equation provenance.
- P01 status is `pending_verification`; human review is `pending`; record lock is `not_locked`.
- Three human-decision issues remain open: AWGN-versus-fading channel label, MAPE/channel-sensing construct scope, and pilot-overhead proxy-axis classification.
- P02 `SCR-00008`, P03 `SCR-00083` family, P04 `SCR-00941` and P05 `SCR-00196` remain `not_started`; human approvals are 0/5.
- Phase D/Phase E boundary is preserved: no TQAF score was added; comparability/admissibility decisions remain pending human adjudication.
- Pilot checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_PILOT_P01_2026-07-30/`.
- Full-corpus gate remains blocked. Next action is the P01 `HC01â€“HC17` human check, especially `HC15`, `HC06` and `HC12`.

## 2026-07-30 Phase D Five-Pilot Extraction â€” Batch Human Verification Pending

- P01â€“P05 source extraction is complete for 5 included-study clusters and 6 eligible PDFs.
- Active workbook: `systematic_review_workflow/04_veri_cekme/outputs/phase_d_pilot_all_2026-07-30/OISAC_PHASE_D_PILOT_ALL_WORKBOOK_2026-07-30.xlsx`.
- Workbook SHA-256: `397fcad05ae5d9761c0d319904803b07694063a7a037e7f280bd219dcf93c2ed`.
- Extracted records: 274 evidence items, 122 metric results and 17 tradeoff records.
- Pilot counts are P01 `66/6/2`, P02 `50/32/3`, P03 `59/45/4`, P04 `38/12/5` and P05 `61/27/3` for evidence/metric/tradeoff.
- P03 preserves `SCR-00083` primary and `SCR-00553` supplementary provenance and keeps the companion, frequency-division and joint-waveform conditions separate.
- Deterministic, formula, reopened-workbook and 13-sheet visual QA passed. All evidence/metric/tradeoff IDs are present and unique; missing source/page locators = 0; calculated/digitized values = 0.
- The workbook contains 85 checklist rows and 35 open scientific human-decision issues. Human responses entered = 0.
- Final P03 QA preserves all multi-metric tradeoff links, marks its four qualitative/constraint tradeoffs non-quantitative, keeps `P03-Q004` open for human confirmation and retains 24 provisional pilot metric-family extensions instead of collapsing them to `other`.
- All five pilots remain `pending_verification / human_review=pending / not_locked`; human approvals are 0/5. No TQAF score or final comparability/admissibility adjudication was added.
- Batch checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_PILOT_ALL_PENDING_HUMAN_2026-07-30/`.
- Full-corpus gate remains blocked. Next action is source-open batch review in `12_ALL_PILOTS_REVIEW` and authoritative completion of P01â€“P05 `HC01â€“HC17` in `08_HUMAN_CHECKLIST`.

## 2026-07-19 PRISMA Pre-Full-Text Eligibility Gate Step 1 LOCK

- User approved the full-text eligibility criteria after four micro-corrections; Step 1 is locked before any report-level eligibility decision.
- Primary technical evidence eligibility requires an eligible peer-reviewed full report; sufficient English full-text content; publication/available date within 2020-01-01 through the actual final search cutoff 2026-06-22; a material optical/photonic platform; genuine joint sensingâ€“communication treatment; a technical contribution; and relevance to at least one prespecified synthesis domain.
- Bilingual reports are eligible when sufficient full technical content is available in English for reliable eligibility assessment and extraction. An English abstract alone is insufficient.
- Date eligibility uses the earliest verifiable publisher `online`, `available online`, or equivalent public availability date. Conflicting or incomplete dates receive `unclear_adjudication` until verified.
- Retracted or withdrawn reports are excluded from primary technical evidence with a dedicated full-text reason. Corrections and errata are linked to the underlying report and are not counted as independent studies.
- Full-text exclusions use one primary reason according to the locked hierarchy: retrieval/report dispositions first; then retraction, date, language, specific publication type, book chapter, other peer-review/publication status, topical scope/integration reasons, and finally insufficient technical content as a residual reason.
- Reports not retrieved are not full-text eligibility exclusions. The 60-report retrieval limitation must be reported transparently: 20 links had been opened without successful download and retrieval pursuit for the remaining 40 was stopped by user decision; the manuscript must not imply exhaustive access attempts for all 60.
- Contextual sources remain separate from primary technical evidence. Low reporting or methodological quality alone is not an exclusion reason and is handled through TQAF-style assessment.
- Potential duplicate, companion, correction, or conferenceâ€“journal reports are linked at report/study level to prevent double counting; they are not automatically treated as scientific ineligibility.
- Locked criteria: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/full_text_eligibility_criteria_LOCKED_2026-07-19.md`.
- Locked reason codes: `systematic_review_workflow/09_kayitlar/checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/full_text_exclusion_reason_codes_LOCKED_2026-07-19.csv`.
- No eligibility assessment, included-study count, extraction, TQAF scoring, synthesis, or formal PRISMA flow population occurred in Step 1.

## Historical Snapshot (Superseded) â€” 2026-07-04 Pre-Retrieval State Clarification

> Historical audit trail only. Its old absolute paths and â€œnext stepâ€ statements are superseded by the top `Current Workflow State` and `START_HERE_OISAC_PRISMA_CURRENT.md`.

- Canonical main project folder: `C:\Users\fatih\OneDrive - ASKERÄ° FABRÄ°KA VE TERSANE Ä°ÅLETME A.Å (ASFAT)\kisiselAlan\prisma2020Review`.
- External staging workspace only: `C:\Users\fatih\OneDrive - ASKERÄ° FABRÄ°KA VE TERSANE Ä°ÅLETME A.Å (ASFAT)\kisiselAlan\reviewmdS`; this folder is for PDF/Markdown staging and is not the canonical PRISMA project state.
- B13 applied master is the only active baseline: `systematic_review_workflow/03_secim/title_abstract_screening/batch_B13_final_2026-06-22/title_abstract_screening_form_MASTER_BATCH_B13_APPLIED_2026-06-22.csv`.
- B13 SHA-256 remains `5d8b675c54bbed9860b473b435ed5cbce724bb9882a186f1091e09baa1d59ad2`.
- Final B13 full-text-needed pool is 332 = 321 `include_for_full_text` + 11 `unclear_need_full_text`.
- Final B13 unclear list has 11 records: `SCR-00373`, `SCR-00462`, `SCR-00508`, `SCR-00623`, `SCR-00669`, `SCR-00689`, `SCR-00730`, `SCR-00931`, `SCR-01044`, `SCR-01141`, `SCR-01183`.
- External old `reviewmdS` unclear watchlist has 8 rows and is superseded by the final B13 11-record unclear list.
- Related-report/version watchlist has 3 records: `SCR-00373`, `SCR-00907`, `SCR-01084`.
- Contextual corpus has 61 records and is not primary technical evidence.
- `reviewmdS` current tracker has 164 rows and is partial/non-canonical; tracker counts must not be treated as final retrieval status.
- `reviewmdS` PDF/Markdown inventory must be reconciled against the B13 332-record pool before any retrieval continuation.
- PRISMA flow remains TBD / not populated.
- No eligibility assessment, synthesis, included-study count, or PRISMA count population before B13-vs-`reviewmdS` reconciliation.

## Amac

Bu dosya, repo icin ortak O-ISAC PRISMA calisma baglamini tanimlar. Repo icindeki sistematik derleme, tarama, veri cikarimi, kalite degerlendirmesi, sentez ve manuscript hazirlama isleri bu baglama gore yurutulmelidir.

## Calisma Konusu

Optical Integrated Sensing and Communication (O-ISAC) for 6G.

## Calisma Turu

PRISMA-grounded narrative systematic review with a scoping-style PCC component.

## Nihai Makale Dili

English.

## Workflow Dili

Turkish explanations + English manuscript-ready sections.

## Manuscript-Ready Title

Optical Integrated Sensing and Communication for 6G: A PRISMA-Grounded Systematic Review and Metric-Governed Cross-Modality Survey

## O-ISAC Operational Definition

In this review, O-ISAC refers to optical or photonic systems in which sensing and communication functions are jointly considered, integrated, co-designed, co-optimized, or evaluated within the same architecture, optical link, waveform/resource framework, hardware platform, channel model, or application scenario.

## Framework

PCC - Population / Concept / Context.

## Population

Peer-reviewed studies on Optical Integrated Sensing and Communication / O-ISAC systems.

## Concept

Cross-modality O-ISAC architectures, taxonomy, sensing/communication metric reporting, metric comparability, comparison admissibility, metric-governed comparison, rate-sensing tradeoff synthesis, enabling technologies, application mapping, validation maturity, and benchmarking readiness.

## Context

6G-oriented optical platforms, including fiber, free-space optical / FSO, VLC/LiFi, photonic-THz, and hybrid optical communication-sensing systems.

## Main Research Question

How has Optical Integrated Sensing and Communication (O-ISAC) been investigated across fiber, free-space optical, VLC/LiFi, photonic-THz, and hybrid optical platforms, and what do existing peer-reviewed studies reveal about cross-modality taxonomy, sensing and communication metric reporting, metric comparability, comparison admissibility, rate-sensing tradeoffs, enabling technologies, application domains, validation maturity, benchmarking readiness, and remaining research gaps for 6G-oriented O-ISAC systems?

## RQ1-RQ7

- RQ1 Taxonomy.
- RQ2 Metric reporting.
- RQ3 Metric comparability / comparison admissibility.
- RQ4 Rate-sensing tradeoff.
- RQ5 Enabling technologies and applications.
- RQ6 Validation maturity and benchmark readiness.
- RQ7 Research gaps and 6G roadmap.

## Primary Synthesis Domains

- O-ISAC modality taxonomy.
- Architecture and integration mechanisms.
- Communication metric reporting.
- Sensing metric reporting.
- Measurement-plane mapping.
- Metric comparability.
- Rate-sensing tradeoff.
- Validation maturity.
- Benchmark readiness.
- Research gaps and 6G roadmap.

## Corpus Distinction

- Primary technical evidence corpus: peer-reviewed journal articles, early-access journal articles, and full-length conference/proceedings papers.
- Contextual corpus: review/survey papers and pre-2020 foundational studies used only for background, terminology, taxonomy cross-checking, or technology lineage.
- Contextual records must not be counted as primary technical evidence.

## Pre-2020 Rule

The primary systematic corpus is limited to January 1, 2020 - June 30, 2026. Pre-2020 foundational studies may be cited for background, terminology, or technology lineage, but will be labeled separately and excluded from primary technical evidence synthesis unless explicitly justified.

## 6G Relevance

6G relevance is a coding variable, not a strict keyword-only inclusion criterion:

- direct
- inferred
- weak
- not applicable

## Search Window

January 1, 2020 - June 30, 2026.

## Search Freeze Date

Actual final search execution/cutoff date: June 22, 2026.

Previously planned search freeze date: June 30, 2026. After final exports were executed/logged on June 22, 2026, date cutoff flags for Step 4-A use the actual cutoff date, not the previously planned date.

## Date Eligibility Rule

If database filters retrieve the full 2026 publication year, records published or made available after the actual final search execution/cutoff date, June 22, 2026, will be excluded during later date eligibility screening. Records with unclear day/month information will be flagged as `date_uncertain` or date-uncertain equivalents during deduplication/screening preparation.

## Screening Decision Categories

- `include_primary`
- `include_contextual`
- `exclude`
- `unclear_full_text_needed`
- `duplicate`
- `date_uncertain`

## Core Primary Databases

- Scopus
- IEEE Xplore

## Selected Supplementary Publisher/Platform Sources

- ScienceDirect
- SpringerLink
- Wiley Online Library
- Taylor & Francis Online
- **Taylor & Francis Online pilotâ€‘tested on 2026â€‘06â€‘22:** lowâ€‘yield and noisy; no strong primary Oâ€‘ISAC candidates identified; remains optional only for tight exactâ€‘phrase supplementary testing.

## Supplementary Search Sources and Institutional Access

Core primary databases remain the starting point for reproducible bibliographic coverage, but the review is not limited to core sources. The user has access to additional databases through the following institutional database lists:

- `https://mk.gov.tr/veritabanlari/Veritabanlar%C4%B1%20Listesi/liste`
- `https://www.etu.edu.tr/tr/kutuphane/veritabanlari`

The current selected source set is Scopus, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online. Web of Science and other accessible databases are not part of the current selected source set unless they are re-added through a documented decision.

Web of Science and ACM Digital Library are excluded from the current formal source set because institutional access is not available.

Supplementary searches must be documented with source name, exact query, search date, filters, raw records, exported records, export format, and deduplication relationship to the core database searches. Publisher platforms may be used for supplementary search, retrieval, and sensitivity checking; contextual or non-peer-reviewed materials must not be mixed into the primary technical evidence corpus.

Formal information sources sentence for protocol/methods:

> Information sources: The systematic search will be conducted in Scopus and IEEE Xplore as the primary bibliographic and engineering databases. Supplementary platform searches will be conducted in ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online. Web of Science and ACM Digital Library will not be included because institutional access was not available during the search planning stage.

## Language

English only.

## Meta-Analysis

Meta-analysis is not planned because the O-ISAC literature is heterogeneous across optical modality, system architecture, sensing task, communication metric, sensing metric, validation method, and measurement plane.

## Synthesis Approach

- Structured narrative synthesis
- Scoping-style taxonomy mapping
- Evidence tabulation
- Metric-governed comparison
- Metric comparability and comparison admissibility assessment
- Validation maturity mapping
- Benchmark readiness assessment
- Research roadmap synthesis

## Metric Comparability Adjudication Rule

Metric comparability is a final adjudicated coding field with four categories:

| Category | Decision rule |
|---|---|
| directly comparable | Same metric, same measurement plane, similar scenario, and similar validation condition. |
| conditionally comparable | Same general metric family but different scenario or assumption; comparison is possible only when conditions are explicitly stated. |
| not comparable | Metric name may be similar, but measurement plane, definition, or validation context differs. |
| descriptive only | The study reports a metric, but information is insufficient for numerical or operational comparison. |

Uncertain cases should be resolved through reviewer notes and adjudication; the final metric comparability label should use one of the four categories above.

## Quality Approach

Low methodological/reporting quality should not automatically exclude a study. Use TQAF-style technical quality assessment to qualify evidence strength.

## TQAF Scoring Scale

Study-level TQAF-style assessment uses the following ordinal scale before evidence synthesis:

- 0 = not reported / insufficient
- 1 = weak or incomplete
- 2 = adequate
- 3 = strong / benchmark-ready
- NA = not applicable

TQAF fields:

- technical relevance
- metric clarity
- reporting completeness
- validation maturity
- reproducibility
- benchmark readiness
- comparison admissibility
- limitation transparency
- overall evidence contribution

Scores may later be translated into qualitative evidence labels: high / moderate / limited / unclear.

## Registration and Protocol Decision

The review lineage was retrospectively registered on the Open Science Framework on 12 February 2026 (`7f6wb`; DOI `10.17605/OSF.IO/7F6WB`). Because search and screening were already complete and synthesis/manuscript drafting had begun, this is not a prospective preregistration. The OSF 221-study record is a superseded predecessor snapshot and is reconciled with the final 206-study execution in `systematic_review_workflow/01_protokol/04_protocol_registration_lineage_correction_2026-08-07.md`. The earlier planning statement that external registration was not planned is retained only in dated historical artifacts and is superseded for current reporting.

## Codex Memory Bank

Repo-level Codex memory bank:

- `systematic_review_workflow/09_kayitlar/codex_memory_bank.md`

Bu dosya, yeni Codex oturumlari icin mevcut durum, kilit kararlar, sonraki isler, acik sorular ve dokunulmayacak alanlari ozetleyen calisma hafizasi olarak kullanilir. Bu memory bank, `PROJECT_CONTEXT_OISAC_PRISMA.md` dosyasinin yerine gecmez; herhangi bir celiskide bu proje baglami birincil kaynak kabul edilir.

## Karar Notlari

- PRISMA temelli akis korunacaktir; calisma narrative systematic review olarak konumlandirilacaktir.
- 2026-06-22 Step 4-C duplicate cluster adjudication: Kullanici duzeltmeleriyle verilen duplicate cluster kararlari islendi. Iki metadata/dedup adjudication removal ve sifir otomatik merge sonrasi 1259 kayitlik approved deduplicated screening input olusturuldu. Cikarilan kayitlar master raw records icinde korunur; PRISMA flow counts TBD kalir ve screening baslatilmamistir.
- PCC component, calismanin kapsamlama ve taxonomy haritalama tarafini guclendirmek icin kullanilacaktir.
- Cross-modality comparison, yalnizca platformlari listelemekle sinirli kalmayacak; metric comparability, comparison admissibility, validation maturity ve benchmark readiness uzerinden yonetilecektir.
- Metric comparability nihai kodlamasi directly comparable, conditionally comparable, not comparable veya descriptive only olarak yapilacak; karar ayni metrik, measurement plane, scenario, validation condition, definition ve reporting adequacy uzerinden verilecektir.
- Evidence synthesis, heterojen optik platformlar arasinda dogrudan nicel pooling yapmak yerine metric-governed comparison ve structured narrative synthesis yaklasimiyla yurutulecektir.
- Review/survey papers ve pre-2020 foundational studies contextual corpus olarak tutulacak; primary technical evidence synthesis'e karistirilmayacaktir.
- Dusuk methodological/reporting quality, calisma disi birakma icin otomatik neden degildir; teknik kanit gucu TQAF-style assessment ile acikca isaretlenecektir.
- Search freeze tarihi arama yurutulene kadar planli tarih olarak kalacaktir.
- TQAF-style assessment icin study-level skor olcegi 0 / 1 / 2 / 3 / NA olarak kullanilacak; qualitative evidence labels daha sonra high / moderate / limited / unclear olarak turetilebilecektir.
- Secilmis arama kaynaklari Scopus, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library ve Taylor & Francis Online olarak guncellendi; Web of Science ve ACM Digital Library, search planning asamasinda institutional access olmadigi icin dahil edilmeyecektir.
- 2026-06-18 IEEE Xplore pilot search, planned search freeze date oncesi yurutulen pilot test olarak kaydedildi; pilot kayit sayilari final PRISMA flow count sayilari degildir.
- Legacy `included_studies_canonical.csv` formal PRISMA workflow icin seed set olarak kullanilmayacaktir; no seed study set will be used karari korunur.
- IEEE Xplore pilotunda S1A ve S1B-R2 candidate final package sorgulari olarak tutulacak; S1B ve S1B-R1 mevcut haliyle fazla genis oldugu icin reddedildi; S1C/S1D/S1E broad modality aramalari refinement gerektirir; S1F-R1 valuable but noisy olarak isaretlendi ve S1F-R2 pending kalir.
- 2026-06-19 Step 2B pilot update ile IEEE-PILOT-S1F-R2 tamamlandi ve S1F-R1 yerine candidate photonic-THz/mmWave IEEE sorgusu olarak tutuldu.
- 2026-06-19 Scopus pilot search, IEEE pilotundan sonra tamamlayici core source pilotu olarak kaydedildi; Scopus pilot counts final PRISMA flow count degildir.
- Candidate pilot package: IEEE-PILOT-S1A, IEEE-PILOT-S1B-R2, IEEE-PILOT-S1F-R2, SCO-PILOT-S1A, SCO-PILOT-S1B ve SCO-PILOT-S1F.
- SCO-PILOT-S1B reported/export mismatch 35 vs 60 ve SCO-PILOT-S1F minor mismatch 103 vs 104 final search oncesi dogrulanmalidir.
- Legacy `included_studies_canonical.csv` validation set olarak da kullanilmayacaktir; formal PRISMA workflow disinda kalir.
- 2026-06-19 Step 2B cleanup ile `AGENTS.md` kaynak seti proje baglamiyla hizalandi; Web of Science ve ACM Digital Library mevcut formal source set disinda kalir.
- IEEE-PILOT-S1A, IEEE-PILOT-S1B-R2 ve IEEE-PILOT-S1F-R2 exact query stringleri chat log kaydindan geri alinip arama planina ve `search_log.csv` dosyasina islendi; Scopus exact query stringleri pending kalir.
- 2026-06-19 ScienceDirect supplementary platform pilot CSV package workflow'a islendi; SD-PILOT-P1/P2A/P2B/P2C/P2D/P2E/P3/P4 search log'a pilot olarak eklendi.
- ScienceDirect pilot package icindeki 350 all-row ve 172 unique-record degerleri pilot audit diagnostics olarak kalir; final PRISMA flow count degildir.
- SD-PILOT-P1, SD-PILOT-P3 ve SD-PILOT-P4 exact ScienceDirect UI query stringleri pending kalir; query string uydurulmayacaktir.
- ScienceDirect original P2 query platform tarafindan "Use fewer boolean connectors (max 8 per field)" uyarisi nedeniyle kabul edilmedi; P2 daha kucuk exact/modality-specific subquery'lere bolunerek pilot edildi.
- ScienceDirect pilot kayitlari supplementary platform pilot assessment icindir; review/survey kayitlar contextual corpus olarak isaretlenecek ve primary technical evidence sayilmayacaktir.
- 2026-06-21 SpringerLink supplementary platform pilot workflow'a islendi; SPR-PILOT-P1B ve SPR-PILOT-P2A/P2B/P2C/P2D/P2E search log'a pilot olarak eklendi.
- SpringerLink SPR-PILOT-P1A uploaded export icinde bulunmadigi icin pending/TODO kalir; query/export uydurulmayacaktir.
- SpringerLink pilot package icindeki 159 raw exported rows, 126 unique deduplicated records ve 29 duplicate groups pilot audit diagnostics olarak kalir; final PRISMA flow count degildir.
- SpringerLink icin SPR-PILOT-P2C, SPR-PILOT-P2D ve SPR-PILOT-P2E useful focused candidates olarak tutulur; SPR-PILOT-P1B, SPR-PILOT-P2A ve SPR-PILOT-P2B noisy/rescue-only olarak isaretlenir.
- SpringerLink chapter records primary technical evidence sayilmayacaktir; gerekli olursa yalnizca contextual corpus olarak degerlendirilecektir.
- 2026-06-21 Wiley Online Library supplementary platform pilot workflow'a islendi; WLY-PILOT-P1A/P1B ve WLY-PILOT-P2A/P2B/P2C/P2D/P2E search log'a pilot olarak eklendi.
- Wiley pilot package icindeki 57 raw exported rows, 49 unique deduplicated records ve 7 duplicate groups pilot audit diagnostics olarak kalir; final PRISMA flow count degildir.
- Wiley icin WLY-PILOT-P2D ve WLY-PILOT-P2E focused candidate olarak tutulur; WLY-PILOT-P1B, WLY-PILOT-P2A ve WLY-PILOT-P2C supplementary/rescue candidate olarak tutulur; WLY-PILOT-P2B rescue-only/noisy, WLY-PILOT-P1A likely false-positive/deprioritized olarak isaretlenir.
- Wiley review/survey/chapter/contextual records primary technical evidence sayilmayacaktir; Wiley pilot kayitlari formal screening tamamlanmadan included study olarak kullanilmayacaktir.
- 2026-06-22 Taylor & Francis Online supplementary platform pilot cleanup tamamlandi: 25 raw rows, 21 unique records, 0 strong primary O-ISAC candidates, 1 unclear/full-text-needed candidate ve 20 likely noise records pilot audit diagnostics olarak kaydedildi. TF-PILOT-P2A low-yield rescue-only tutulur; TF-PILOT-P2B ve TF-PILOT-P2C deprioritized kalir. Bu pilot degerleri final PRISMA flow count degildir ve Taylor & Francis yalnizca optional tight exact-phrase supplementary source olarak kalabilir.
- 2026-06-22 Step 2D preparation baslatildi; IEEE, Scopus, ScienceDirect, SpringerLink, Wiley ve Taylor & Francis pilot kayitlari final search package taslagi oncesinde konsolide edildi. Pilot counts non-PRISMA count olarak kalir.
- 2026-06-22 Step 3-A Scopus final raw exports logged: SCO-FINAL-S1A=41, SCO-FINAL-S1B=1128, SCO-FINAL-S1F=104; total raw Scopus rows=1273. Scopus audit unique diagnostic=1122 ve duplicate groups diagnostic=141 formal PRISMA deduplication sonucu degildir. Deduplication/screening baslatilmadi; PRISMA flow counts TBD kalir.
- 2026-06-22 Step 3-B IEEE Xplore final raw exports logged: IEEE-FINAL-S1A=31, IEEE-FINAL-S1B=252, IEEE-FINAL-S1F=46; total raw IEEE rows=329. IEEE audit unique diagnostic=261 ve duplicate groups diagnostic=68 formal PRISMA deduplication sonucu degildir. IEEE exportlarinda 2026-06-22 cutoff sonrasi Online Date tespit edilmedi; 19 DOI-missing row sonraki title-based fallback deduplication icin isaretlendi. Deduplication/screening baslatilmadi; PRISMA flow counts TBD kalir.
- 2026-06-22 Step 3-C supplementary final raw exports logged: ScienceDirect total raw rows=24 / diagnostic unique=23, SpringerLink total raw rows=75 / diagnostic unique=72, Wiley Online Library total raw rows=29 / diagnostic unique=27, Taylor & Francis Online total raw rows=3 / diagnostic unique=3. Total supplementary final raw rows parsed=131, total supplementary diagnostic unique records=125 ve duplicate groups diagnostic=5 formal PRISMA deduplication sonucu degildir. Taylor & Francis Online low-yield ve query mapping pending olarak optional/tight-only kalir; core veya strong supplementary kaynak gibi raporlanmayacaktir. Deduplication/screening/full-text assessment baslatilmadi; PRISMA flow counts TBD kalir.
- 2026-06-22 Step 4-A final export consolidation and formal deduplication draft completed: final raw rows=1733, duplicate groups=312, deduplicated screening input records=1261, possible duplicate manual review pairs=37. Bu degerler draft/dedup report degerleridir; PRISMA flow counts henuz final degildir ve title/abstract screening baslatilmamistir.
- 2026-06-22 Step 4-B possible duplicate cluster review preparation completed: 37 possible duplicate pairs connected-component mantigiyla 7 manual review clusterina donusturuldu. Otomatik merge yapilmadi; deduplication approval, PRISMA identification counts finalization ve title/abstract screening oncesi manual adjudication gerekir.
- 2026-06-22 Step 5-A title/abstract screening preparation completed: Approved 1259 not_screened records were used to create the master screening form, decision guide, reason code set, 50-record calibration batch, screening batch plan, reviewer instructions and conflict resolution plan. Screening decisions were not made; calibration screening is pending; PRISMA flow counts remain TBD.
- 2026-06-22 Step 5-B calibration AI suggestions completed: The 50-record calibration batch was processed only for AI-assisted provisional screening suggestions. Final human decisions remain blank, the master screening form was not modified, full title/abstract screening has not started, and PRISMA flow counts remain TBD.
- 2026-06-22 Step 5-B2 calibration human review preparation completed: AI-assisted provisional suggestions were transformed into a human review workbook and attention list. A contextual_over_inclusion risk was identified for generic photonics/enabling technology records, and CTX02 refinement was proposed for user/ChatGPT review. Human calibration decisions remain pending; master screening form unchanged; PRISMA flow counts remain TBD.
- 2026-06-23 Step 5-B2 partial calibration human review update: User-provided human calibration decisions were recorded for 16 of 50 calibration records in the human review workbook only. Current human calibration distribution for reviewed records: 11 exclude_title_abstract, 4 contextual_only, and 1 include_for_full_text. Remaining 34 calibration records are pending; master screening form unchanged; PRISMA flow counts remain TBD.
- 2026-06-23 Step 5-B2 calibration human review completed: User-provided human calibration decisions were recorded for all 50 calibration records in the human review workbook only. Calibration human decision distribution: 28 exclude_title_abstract, 16 include_for_full_text, 5 contextual_only, and 1 unclear_need_full_text. Master screening form unchanged; full title/abstract screening not started; PRISMA flow counts remain TBD.
- 2026-06-22 Step 5-B3 calibration finalization completed: The 50 human calibration decisions were logged as final calibration decisions, calibrated screening guide v2 and reason codes v2 were created, and a 1259-record calibration-applied master copy was generated. Original master screening form remains unchanged; full title/abstract screening has not started; PRISMA flow counts remain TBD.
- 2026-06-22 Step 5-C1 Batch B01 AI suggestions completed: TAB-2026-06-22-B01 contains 100 records; 31 calibration_resolved records were skipped and AI-assisted provisional suggestions were created for 69 not_screened records only. Human review is pending; master screening forms unchanged; PRISMA flow counts remain TBD.
- 2026-06-23 Step 5-C1 Batch B01 partial human review update: User-provided human decisions were recorded for the first 20 medium-priority B01 records in the B01 human review workbook only. Current B01 workbook status: 20 resolved and 49 pending; master screening forms unchanged; PRISMA flow counts remain TBD.
- 2026-06-23 Step 5-C1 Batch B01 partial human review update 2: User-provided human decisions were recorded for B01 medium-priority records 21-40 in the B01 human review workbook only. Current B01 workbook status: 40 resolved and 29 pending; master screening forms unchanged; PRISMA flow counts remain TBD.
- 2026-06-23 Step 5-C1 Batch B01 human review completed: User-provided human decisions were recorded for all 69 not_screened B01 records in the B01 human review workbook only. Final B01 workbook distribution: 54 exclude_title_abstract, 14 include_for_full_text, 1 contextual_only, 0 unclear_need_full_text. Master screening forms unchanged; PRISMA flow counts remain TBD.

- 2026-06-22 Step 5-C2D pre-B02 workflow integrity audit and global normalization completed: Step 1-Step 5-C2/C2b workflow files, search/dedup/screening counts, B01/calibration decisions and master lineage were audited before B02. A pre-B02 global-normalized master baseline was created with 119 resolved title/abstract records and 1140 not_screened records; PRISMA flow remains TBD.
- 2026-06-22 Step 5-C3 Batch B02 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B02 contains 100 records; 7 calibration_resolved records were excluded from re-screening and 93 not_screened records received AI-assisted provisional suggestions only. Human review is pending; master screening form remains unchanged; resolved title/abstract decisions remain 119/1259 draft tracking only; PRISMA flow remains TBD.
- 2026-06-24 Step 5-C3 Batch B02 partial human review update: User-provided human decisions were recorded for 18 high-priority B02 records in the B02 human review workbook only. Current B02 workbook status: 18 resolved and 75 pending among the 93 B02 not_screened records. Master screening form unchanged; resolved title/abstract decisions remain 119/1259 draft tracking only until B02 human decisions are formally logged to a master copy; PRISMA flow remains TBD.
- 2026-06-24 Step 5-C3 Batch B02 partial human review update 2: User-provided human decisions were recorded for the first 25 medium-priority B02 records in the B02 human review workbook only. Current B02 workbook status: 43 resolved and 50 pending among the 93 B02 not_screened records. Master screening form unchanged; resolved title/abstract decisions remain 119/1259 draft tracking only until B02 human decisions are formally logged to a master copy; PRISMA flow remains TBD.
- 2026-06-24 Step 5-C3 Batch B02 partial human review update 3: User-provided human decisions were recorded for medium-priority B02 records 26-50 in the B02 human review workbook only. Current B02 workbook status: 68 resolved and 25 pending among the 93 B02 not_screened records. Master screening form unchanged; resolved title/abstract decisions remain 119/1259 draft tracking only until B02 human decisions are formally logged to a master copy; PRISMA flow remains TBD.
- 2026-06-24 Step 5-C3 Batch B02 human review completed: User-provided human decisions were recorded for the final 25 B02 records in the B02 human review workbook only. B02 workbook status: 93 resolved and 0 pending among the 93 B02 not_screened records. Human decision distribution for B02: exclude_title_abstract=77, include_for_full_text=15, contextual_only=1, unclear_need_full_text=0. Human-decided title/abstract tracking after B02 = 212/1259, with 1047 records remaining if B02 decisions are formally applied to the master. Master screening form is still unchanged in this workbook-only step; master-applied resolved count remains 119/1259 until the next B02 decision logging/master update step; PRISMA flow remains TBD.
- 2026-06-22 Step 5-C4 Batch B02 human decisions logging/master update completed: The 93 B02 human title/abstract decisions were logged into a new B02-applied master copy only. B02 human decisions: exclude_title_abstract=77, include_for_full_text=15, contextual_only=1, unclear_need_full_text=0. Master-applied resolved title/abstract records now equal 212/1259, with 1047 not_screened records remaining. B02 is completed; B03 remains pending; PRISMA flow remains TBD and was not populated.
- 2026-06-22 Step 5-C5 Batch B03 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B03 contains 100 records and no previously resolved calibration/B01/B02 records; AI-assisted provisional suggestions were generated for all 100 not_screened records only. AI suggestion distribution: exclude_title_abstract=73, include_for_full_text=20, contextual_only=7, unclear_need_full_text=0. Human review is pending; master screening form remains unchanged; resolved title/abstract decisions remain 212/1259 draft tracking only; PRISMA flow remains TBD.
- 2026-06-24 Step 5-C5 Batch B03 partial human review update: User-provided human decisions were recorded for the 17 high-priority B03 records in the B03 human review workbook only. Current B03 workbook status: 17 resolved and 83 pending among the 100 B03 not_screened records. Human decision distribution for reviewed high-priority records: exclude_title_abstract=12, contextual_only=4, include_for_full_text=1, unclear_need_full_text=0. Notable agent-human changes: SCR-00224 contextual_only/CTX02 to exclude_title_abstract/EX05, and SCR-00268 exclude_title_abstract/EX05 to include_for_full_text/IN05. Master screening form unchanged; PRISMA flow remains TBD.
- 2026-06-24 Step 5-C5 Batch B03 partial human review update 2: Kullanici tarafindan verilen B03 medium-priority ilk 25 kaydin insan kararlari B03 human review workbook icine islendi. Bu 25 kaydin tamami exclude_title_abstract olarak cozuldu; reason code dagilimi EX05=15, EX01=7, EX03=1, EX07=1, EX08=1. Guncel B03 workbook durumu: 42 resolved ve 58 pending. Kumulatif B03 human decision dagilimi: exclude_title_abstract=37, contextual_only=4, include_for_full_text=1, unclear_need_full_text=0. Yeni agent-human kod farki: SCR-00240 agent EX06 iken insan karari EX08 olarak kaydedildi. Master screening form unchanged; PRISMA flow remains TBD.
- 2026-06-24 Step 5-C5 Batch B03 partial human review update 3: Kullanici tarafindan verilen B03 medium-priority ikinci 25 kaydin insan kararlari B03 human review workbook icine islendi. Bu alt grupta 24 kayit exclude_title_abstract ve 1 kayit contextual_only olarak cozuldu; reason code dagilimi EX05=14, EX01=6, EX03=1, EX04=1, EX06=1, EX07=1, CTX01=1. Guncel B03 workbook durumu: 67 resolved ve 33 pending. Kumulatif B03 human decision dagilimi: exclude_title_abstract=61, contextual_only=5, include_for_full_text=1, unclear_need_full_text=0. Yeni agent-human karar/kod farki yoktur. Master screening form unchanged; PRISMA flow remains TBD.
- 2026-06-24 Step 5-C5 Batch B03 human review completed: Kullanici tarafindan verilen B03 medium-priority son 14 kayit ve low-priority 19 kayit insan kararlari B03 human review workbook icine islendi. Bu son 33 kaydin dagilimi: include_for_full_text=20, exclude_title_abstract=12, contextual_only=1, unclear_need_full_text=0. Son blok reason code dagilimi: EX05=9, EX01=2, EX07=1, IN02=2, IN03=3, IN04=6, IN05=7, IN06=2, CTX01=1. B03 human review workbook durumu 100/100 resolved oldu. Nihai B03 human decision dagilimi: exclude_title_abstract=73, include_for_full_text=21, contextual_only=6, unclear_need_full_text=0. Nihai B03 reason code dagilimi: EX05=46, EX01=15, EX02=2, EX03=4, EX04=1, EX06=1, EX07=3, EX08=1, IN02=2, IN03=3, IN04=6, IN05=8, IN06=2, CTX01=2, CTX02=4. Human-decided title/abstract tracking after B03 = 312/1259 with 947 records remaining if B03 decisions are formally applied to the master in Step 5-C6. Master screening form unchanged in this workbook-only completion step; PRISMA flow remains TBD and was not populated.
- 2026-06-22 Step 5-C6 Batch B03 human decisions logging/master update completed: B03 icindeki 100 insan title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B03-applied master copy olusturuldu. B03 human decisions: exclude_title_abstract=73, include_for_full_text=21, contextual_only=6, unclear_need_full_text=0. Master-applied resolved title/abstract records now equal 312/1259, with 947 not_screened records remaining. B03 is completed; B04 remains pending. PRISMA flow remains TBD and was not populated.
- 2026-06-22 Step 5-C7 Batch B04 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B04 contains 100 records; 1 calibration_resolved record (SCR-00312) was excluded from re-screening and AI-assisted provisional suggestions were generated only for the remaining 99 not_screened records. AI suggestion distribution: exclude_title_abstract=75, include_for_full_text=17, contextual_only=5, unclear_need_full_text=2. Human review is pending; master screening form remains unchanged; resolved title/abstract decisions remain 312/1259 draft tracking only; remaining not_screened remains 947 until B04 human decisions are logged. PRISMA flow remains TBD and was not populated.
- 2026-06-24 Step 5-C7 Batch B04 high-priority partial human review update: User-provided human decisions were recorded for the 20 high-priority B04 records in `batch_B04_human_review_workbook_2026-06-22.csv` only. Reviewed high-priority decision distribution: exclude_title_abstract=17, contextual_only=1, include_for_full_text=1, unclear_need_full_text=1. Reviewed high-priority reason code distribution: EX05=11, EX01=2, EX03=2, EX04=2, CTX02=1, IN02=1, UN01=1. Current B04 workbook status: 20 resolved and 79 pending among the 99 B04 not_screened records. Notable agent-human changes: SCR-00351 exclude_title_abstract/EX05 to contextual_only/CTX02, and SCR-00382 unclear_need_full_text/UN01 to include_for_full_text/IN02. Master screening form unchanged; resolved title/abstract decisions remain 312/1259 draft tracking only until B04 human decisions are formally logged; PRISMA flow remains TBD and was not populated.
- 2026-06-24 Step 5-C7 Batch B04 medium-priority partial human review update 1: User-provided human decisions were recorded for the first 25 medium-priority B04 records in `batch_B04_human_review_workbook_2026-06-22.csv` only. This subset decision distribution: exclude_title_abstract=24, include_for_full_text=1, contextual_only=0, unclear_need_full_text=0. Subset reason code distribution: EX05=11, EX01=9, EX07=1, EX08=1, EX03=1, EX06=1, IN03=1. Current B04 workbook status: 45 resolved and 54 pending among the 99 B04 not_screened records. Master screening form unchanged; resolved title/abstract decisions remain 312/1259 draft tracking only until B04 human decisions are formally logged; PRISMA flow remains TBD and was not populated.
- 2026-06-24 Step 5-C7 Batch B04 medium-priority partial human review update 2: User-provided human decisions were recorded for medium-priority B04 records 26-50 in `batch_B04_human_review_workbook_2026-06-22.csv` only. This subset decision distribution: exclude_title_abstract=21, contextual_only=4, include_for_full_text=0, unclear_need_full_text=0. Subset reason code distribution: EX05=11, EX01=9, EX06=1, CTX01=2, CTX05=2. Current B04 workbook status: 70 resolved and 29 pending among the 99 B04 not_screened records. Master screening form unchanged; resolved title/abstract decisions remain 312/1259 draft tracking only until B04 human decisions are formally logged; PRISMA flow remains TBD and was not populated.
- 2026-06-24 Step 5-C7 Batch B04 human review completed: Kullanici tarafindan verilen B04 medium-priority son 14 kayit ve low-priority 15 kayit insan kararlari `batch_B04_human_review_workbook_2026-06-22.csv` icine islendi. Bu son 29 kaydin dagilimi: include_for_full_text=15, exclude_title_abstract=12, contextual_only=2, unclear_need_full_text=0. B04 human review workbook durumu 99/99 resolved oldu. Nihai B04 human decision dagilimi: exclude_title_abstract=74, include_for_full_text=17, contextual_only=7, unclear_need_full_text=1. Nihai B04 reason code dagilimi: EX05=38, EX01=27, EX03=3, EX04=2, EX06=2, EX07=1, EX08=1, IN02=3, IN03=3, IN04=6, IN05=5, CTX01=3, CTX02=2, CTX05=2, UN01=1. Notable agent-human changes listesine SCR-00309 include_for_full_text/IN04 to contextual_only/CTX02 eklendi; SCR-00388 and SCR-00387 include_for_full_text kararlarinda full-text eligibility/role verification notlari korundu. Human-decided title/abstract tracking after B04 = 411/1259 with 848 records remaining if B04 decisions are formally applied to the master in Step 5-C8. Master screening form unchanged in this workbook-only completion step; PRISMA flow remains TBD and was not populated.
- 2026-06-22 Step 5-C8 Batch B04 human decisions logging/master update completed: B04 icindeki 99 insan title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B04-applied master copy olusturuldu. B04 human decisions: exclude_title_abstract=74, include_for_full_text=17, contextual_only=7, unclear_need_full_text=1. Final reason code distribution: EX05=38, EX01=27, EX03=3, EX04=2, EX06=2, EX07=1, EX08=1, IN02=3, IN03=3, IN04=6, IN05=5, CTX01=3, CTX02=2, CTX05=2, UN01=1. Agent-human comparison summary: exact agreement=94, decision disagreement=3, same-decision reason refinement=2. Master-applied resolved title/abstract records now equal 411/1259, with 848 not_screened records remaining. B04 is completed; B05 remains pending. PRISMA flow remains TBD and was not populated.
- 2026-06-22 Step 5-C9 Batch B05 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B05 contains 100 records; 2 calibration_resolved records were excluded from re-screening and AI-assisted provisional suggestions were generated only for the remaining 98 not_screened records. AI suggestion distribution: exclude_title_abstract=77, include_for_full_text=15, contextual_only=3, unclear_need_full_text=3. Human review is pending; master screening form remains unchanged; resolved title/abstract decisions remain 411/1259 draft tracking only; remaining not_screened remains 848 until B05 human decisions are logged. PRISMA flow remains TBD and was not populated.
- 2026-06-25 Step 5-C9 Batch B05 high-priority partial human review update: Kullanici tarafindan verilen 13 high-priority B05 kaydin insan kararlari `batch_B05_human_review_workbook_2026-06-22.csv` icine islendi. Bu alt grubun karar dagilimi: include_for_full_text=6, exclude_title_abstract=4, contextual_only=2, unclear_need_full_text=1. Reason code dagilimi: CTX02=2, EX05=2, EX01=1, EX03=1, IN02=2, IN03=1, IN04=1, IN05=2, UN01=1. Guncel B05 workbook durumu: 13 resolved ve 85 pending among 98 B05 not_screened records. Notable agent-human changes: SCR-00415 unclear_need_full_text/UN01 -> exclude_title_abstract/EX01; SCR-00451 unclear_need_full_text/UN01 -> include_for_full_text/IN02; SCR-00460 include_for_full_text/IN01 -> include_for_full_text/IN03; SCR-00483 contextual_only/CTX02 -> exclude_title_abstract/EX05. Master screening form unchanged; master-applied resolved title/abstract records remain 411/1259 until B05 human decisions are formally logged; PRISMA flow remains TBD and was not populated.
- 2026-06-25 Step 5-C9 Batch B05 medium-priority partial human review update 1: Kullanici tarafindan verilen B05 medium-priority ilk 25 kaydin insan kararlari `batch_B05_human_review_workbook_2026-06-22.csv` icine islendi. Bu alt grubun tamami exclude_title_abstract olarak cozuldu; reason code dagilimi: EX05=15, EX01=4, EX03=2, EX07=3, EX06=1. Guncel B05 workbook durumu: 38 resolved ve 60 pending among 98 B05 not_screened records. Kumulatif B05 human decision dagilimi: exclude_title_abstract=29, include_for_full_text=6, contextual_only=2, unclear_need_full_text=1. Bu alt grupta yeni agent-human karar/kod farki yoktur. Master screening form unchanged; master-applied resolved title/abstract records remain 411/1259 until B05 human decisions are formally logged; PRISMA flow remains TBD and was not populated.
- 2026-06-25 Step 5-C9 Batch B05 medium-priority partial human review update 2: Kullanici tarafindan verilen B05 medium-priority ikinci 25 kaydin insan kararlari `batch_B05_human_review_workbook_2026-06-22.csv` icine islendi. Bu alt grubun tamami exclude_title_abstract olarak cozuldu; reason code dagilimi: EX05=11, EX01=5, EX07=4, EX03=2, EX06=2, EX02=1. Guncel B05 workbook durumu: 63 resolved ve 35 pending among 98 B05 not_screened records; pending priority dagilimi: medium=26, low=9. Kumulatif B05 human decision dagilimi: exclude_title_abstract=54, include_for_full_text=6, contextual_only=2, unclear_need_full_text=1. Bu alt grupta yeni agent-human karar/kod farki yoktur. Master screening form unchanged; master-applied resolved title/abstract records remain 411/1259 until B05 human decisions are formally logged; PRISMA flow remains TBD and was not populated.
- 2026-06-25 Step 5-C9 Batch B05 human review completed in workbook: Kullanici tarafindan verilen B05 medium-priority son 26 kayit ve low-priority 9 kayit insan kararlari `batch_B05_human_review_workbook_2026-06-22.csv` icine islendi. Medium son 26 karar dagilimi: exclude_title_abstract=25, include_for_full_text=1; reason code dagilimi: EX05=15, EX01=4, EX04=2, EX07=1, EX06=1, IN06=1. Low 9 karar dagilimi: include_for_full_text=9; reason code dagilimi: IN05=3, IN04=3, IN02=2, IN03=1. B05 human review workbook durumu 98/98 resolved oldu. Nihai B05 human decision dagilimi: exclude_title_abstract=79, include_for_full_text=16, contextual_only=2, unclear_need_full_text=1. Nihai B05 reason code dagilimi: EX05=45, EX01=14, EX07=8, EX03=5, EX06=4, IN05=5, IN04=4, IN02=4, EX04=2, CTX02=2, IN03=2, EX02=1, IN06=1, UN01=1. Nihai B05 agent-human farklari: SCR-00415 unclear_need_full_text/UN01 -> exclude_title_abstract/EX01; SCR-00451 unclear_need_full_text/UN01 -> include_for_full_text/IN02; SCR-00460 include_for_full_text/IN01 -> include_for_full_text/IN03; SCR-00483 contextual_only/CTX02 -> exclude_title_abstract/EX05. Human-decided title/abstract tracking after B05 would be 509/1259 with 750 records remaining if B05 decisions are formally applied to the master in the next logging/master update step. Master screening form unchanged in this workbook-only completion step; PRISMA flow remains TBD and was not populated.
- 2026-06-22 Step 5-C10 Batch B05 human decisions logging/master update completed: B05 icindeki 98 insan title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B05-applied master copy olusturuldu. B05 human decisions: exclude_title_abstract=79, include_for_full_text=16, contextual_only=2, unclear_need_full_text=1. Final reason code distribution: EX05=45, EX01=14, EX03=5, EX07=8, EX06=4, EX04=2, EX02=1, IN05=5, IN04=4, IN03=2, IN02=4, IN06=1, CTX02=2, UN01=1. Agent-human comparison summary: agreement/retained exact decision-reason alignment=94, decision disagreement=3, same-decision reason refinement=1. Master-applied resolved title/abstract records now equal 509/1259, with 750 not_screened records remaining. B05 is completed; B06 remains pending. PRISMA flow remains TBD and was not populated.
- 2026-06-22 Step 5-C11 Batch B06 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B06 contains 100 records; no calibration_resolved or batch_resolved records were present; AI-assisted provisional suggestions were generated for all 100 not_screened records using B05-applied master as baseline. AI suggestion distribution: exclude_title_abstract=81, include_for_full_text=15, contextual_only=3, unclear_need_full_text=1. Reason code distribution: EX05=45, EX01=19, IN05=8, EX03=6, EX06=6, IN02=2, IN03=2, IN04=2, EX07=2, CTX02=2, EX02=1, EX04=1, EX08=1, IN06=1, CTX01=1, UN01=1. Human review is pending; master screening form unchanged; resolved title/abstract decisions remain 509/1259 draft tracking only; remaining not_screened remains 750 until B06 human decisions are logged. PRISMA flow remains TBD and was not populated.
- 2026-06-25 Step 5-C11 Batch B06 high-priority partial human review update: User-provided human decisions from `B06_high_priority_10_human_decisions_patch_2026-06-25.csv` were recorded in `batch_B06_human_review_workbook_2026-06-22.csv` only. Reviewed high-priority decision distribution: exclude_title_abstract=6, include_for_full_text=2, contextual_only=1, unclear_need_full_text=1. Reviewed high-priority reason code distribution: EX01=2, EX03=2, EX05=2, IN03=1, IN05=1, CTX05=1, UN01=1. Current B06 workbook status: 10 resolved and 90 pending among 100 B06 not_screened records. Agent-human comparison: exact agreement=4, decision disagreement=3, same-decision reason refinement=3. Notable changes: SCR-00506 unclear_need_full_text/UN01 -> include_for_full_text/IN03; SCR-00508 exclude_title_abstract/EX03 -> unclear_need_full_text/UN01; SCR-00566 contextual_only/CTX02 -> include_for_full_text/IN05; SCR-00510 EX03 -> EX01; SCR-00568 CTX02 -> CTX05; SCR-00584 EX03 -> EX01. Master screening form unchanged; master-applied resolved title/abstract records remain 509/1259 until B06 human decisions are formally logged; PRISMA flow remains TBD and was not populated.
- 2026-06-26 Step 5-C11 Batch B06 reviewed-85 partial human review update: User-provided human decisions from `B06_reviewed_85_human_decisions_patch_2026-06-25.csv` were recorded in `batch_B06_human_review_workbook_2026-06-22.csv` only. The patch contained 85 resolved B06 records: 75 newly pending records were updated and the prior 10 resolved high-priority records matched exactly. Current B06 workbook status: 85 resolved and 15 pending among 100 B06 not_screened records. Cumulative reviewed decision distribution: exclude_title_abstract=80, include_for_full_text=2, contextual_only=2, unclear_need_full_text=1. Cumulative reviewed reason code distribution: EX05=45, EX01=21, EX06=6, EX03=3, EX07=2, EX02=1, EX04=1, EX08=1, IN03=1, IN05=1, CTX01=1, CTX05=1, UN01=1. Agent-human comparison among 85 resolved B06 records: exact agreement=79, decision disagreement=3, same-decision reason refinement=3. Remaining pending B06 records are 15 low-priority include candidates. Master screening form unchanged; master-applied resolved title/abstract records remain 509/1259 until B06 human decisions are formally logged; PRISMA flow remains TBD and was not populated.
- 2026-06-22 Step 5-C12 Batch B06 human decisions logging/master update completed: B06 icindeki 100 insan title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B06-applied master copy olusturuldu. B06 human decisions: exclude_title_abstract=80, include_for_full_text=17, contextual_only=2, unclear_need_full_text=1. Final reason code distribution: EX05=45, EX01=21, EX06=6, EX03=3, EX07=2, EX02=1, EX04=1, EX08=1, IN05=9, IN03=3, IN02=2, IN04=2, IN06=1, CTX01=1, CTX05=1, UN01=1. Agent-human comparison summary: exact agreement=94, decision disagreement=3, same-decision reason refinement=3. Master-applied resolved title/abstract records now equal 609/1259, with 650 not_screened records remaining. B06 is completed; B07 remains pending. PRISMA flow remains TBD/draft_not_populated and was not populated.
- 2026-06-22 Step 5-C13 Batch B07 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B07 contains 100 records and all were not_screened at baseline; AI-assisted provisional suggestions were generated for all 100 B07 records using the B06-applied master as baseline. AI suggestions were provisional only and were not final screening decisions. Master screening form remained unchanged; resolved title/abstract decisions remained 609/1259 draft tracking only; PRISMA flow remained TBD and was not populated.
- 2026-06-22 Step 5-C14 Batch B07 human decisions logging/master update completed: B07 icindeki 100 insan/User/ChatGPT title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B07-applied master copy olusturuldu. B07 human decisions: exclude_title_abstract=78, include_for_full_text=14, contextual_only=5, unclear_need_full_text=3. Final reason code distribution: EX05=44, EX01=23, IN04=6, IN05=6, CTX02=4, EX03=3, EX06=3, EX07=3, UN01=3, CTX05=1, EX04=1, EX08=1, IN02=1, IN06=1. Agent-human comparison summary: exact agreement=94, decision disagreement=5, same-decision reason refinement=1. Master-applied resolved title/abstract records now equal 709/1259, with 550 not_screened records remaining. B07 is completed; B08 remains pending. PRISMA flow remains TBD/draft_not_populated and was not populated.
- 2026-06-22 Step 5-C14b Batch B07 human_notes exact correction completed: B07 karar, reason code, flag ve count alanlari degistirilmeden yalnizca `human_notes` alanlari ChatGPT/User correction patch dosyasindaki exact string degerleriyle yeni corrected kopyalarda duzeltildi. Corrected B07-applied master active baseline olarak kullanilmalidir. Master-applied resolved title/abstract records 709/1259, remaining not_screened 550 ve PRISMA flow TBD/draft_not_populated olarak degismeden kalir.
- 2026-06-27 Step 5-C16 Batch B08 human decisions logging/master update completed: B08 icindeki 100 insan/User/ChatGPT title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B08-applied master copy olusturuldu. B08 human decisions: exclude_title_abstract=84, include_for_full_text=13, contextual_only=2, unclear_need_full_text=1. Final reason code distribution: EX05=56, EX01=15, IN04=6, IN05=5, EX07=3, EX03=3, CTX02=2, EX04=2, EX06=2, EX08=2, EX02=1, IN02=1, IN03=1, UN01=1. Agent-human comparison summary: exact agreement=99, decision disagreement=1, same-decision reason refinement=0. Master-applied resolved title/abstract records now equal 809/1259, with 450 not_screened records remaining. B08 is completed; B09 remains pending. PRISMA flow remains TBD/draft_not_populated and was not populated.
- 2026-06-22 Step 5-C17 Batch B09 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B09 contains 100 records and all were not_screened at baseline; AI-assisted provisional suggestions were generated for all 100 B09 records using the B08-applied master as baseline. AI suggestion distribution: exclude_title_abstract=78, include_for_full_text=21, contextual_only=1, unclear_need_full_text=0. Reason code distribution: EX05=54, IN05=18, EX03=6, EX06=6, EX02=5, EX07=3, EX08=3, IN02=3, CTX02=1, EX04=1. Human review is pending; master screening form unchanged; resolved title/abstract decisions remain 809/1259 draft tracking only; remaining not_screened remains 450 until B09 human decisions are logged. PRISMA flow remains TBD and was not populated.
- 2026-06-27 Step 5-C18 Batch B09 human decisions logging/master update completed: B09 icindeki 100 insan/User/ChatGPT title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B09-applied master copy olusturuldu. B09 human decisions: exclude_title_abstract=78, include_for_full_text=21, contextual_only=1, unclear_need_full_text=0. Final reason code distribution: EX05=54, IN05=18, EX03=6, EX06=6, EX02=4, EX07=4, EX08=3, IN02=3, EX04=1, CTX02=1. Agent-human comparison summary: exact agreement=98, decision disagreement=0, same-decision reason refinement=2. Master-applied resolved title/abstract records now equal 909/1259, with 350 not_screened records remaining. B09 is completed; B10 remains pending. PRISMA flow remains TBD/draft_not_populated and was not populated.
- 2026-06-22 Step 5-C19 Batch B10 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B10 contains 100 records and all were not_screened at baseline; AI-assisted provisional suggestions were generated for all 100 B10 records using the B09-applied master as baseline. AI suggestion distribution: include_for_full_text=81, contextual_only=12, exclude_title_abstract=5, unclear_need_full_text=1, duplicate_or_related_report_flag=1. Reason code distribution: IN05=37, IN01=15, IN03=15, CTX01=9, IN02=5, IN04=5, IN06=4, CTX02=3, EX01=3, EX04=1, EX06=1, UN01=1, UN04=1. Human review is pending; master screening form unchanged; resolved title/abstract decisions remain 909/1259 draft tracking only; remaining not_screened remains 350 until B10 human decisions are logged. PRISMA flow remains TBD and was not populated.
- 2026-06-27 Step 5-C20 Batch B10 human decisions logging/master update completed: B10 icindeki 100 insan/User/ChatGPT title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B10-applied master copy olusturuldu. B10 human decisions: include_for_full_text=80, contextual_only=13, exclude_title_abstract=5, duplicate_or_related_report_flag=1, unclear_need_full_text=1. Final reason code distribution: IN05=37, IN03=16, IN01=13, CTX01=9, IN02=5, IN04=5, IN06=4, CTX02=4, EX01=3, UN04=1, UN01=1, EX04=1, EX06=1. Agent-human comparison summary: exact agreement=97, decision disagreement=1, same-decision reason refinement=2. Related-report flag: SCR-00907, likely related to SCR-00901, to be mapped during full-text/related-report stage. Master-applied resolved title/abstract records now equal 1009/1259, with 250 not_screened records remaining. B10 is completed; B11 remains pending. PRISMA flow remains TBD/draft_not_populated and was not populated.
- 2026-06-22 Step 5-C21 Batch B11 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B11 contains 100 records and all were not_screened at baseline; AI suggestions were generated for all B11 not-screened records using the B10-applied master as read-only baseline. B11 AI suggestion distribution: include_for_full_text=55, exclude_title_abstract=32, contextual_only=10, unclear_need_full_text=2, duplicate_or_related_report_flag=1. Reason code distribution: IN05=18, EX05=16, IN04=15, IN02=11, EX01=7, CTX02=6, IN03=5, CTX05=4, EX04=4, IN06=3, IN01=3, EX02=2, UN01=2, EX06=2, EX03=1, UN04=1. Human review is pending; master screening form unchanged; resolved title/abstract decisions remain 1009/1259 and remaining not_screened remains 250 until B11 human decisions are logged. PRISMA flow remains TBD and was not populated.
- 2026-06-27 Step 5-C22 Batch B11 human decisions logging/master update completed: B11 icindeki 100 insan/User/ChatGPT title/abstract karari workflow'a final batch artefactleri olarak islendi ve yeni B11-applied master copy olusturuldu. B11 human decisions: include_for_full_text=56, exclude_title_abstract=32, contextual_only=10, unclear_need_full_text=1, duplicate_or_related_report_flag=1. Final reason code distribution: IN05=19, EX05=15, IN04=15, IN02=11, EX01=8, CTX02=5, CTX05=5, IN03=5, EX04=4, IN01=3, IN06=3, EX02=2, EX06=2, UN01=1, EX03=1, UN04=1. Agent-human comparison summary: exact agreement=97, decision disagreement=2, same-decision reason refinement=1. Related-report flag: SCR-01084, likely related to SCR-01054, to be mapped during full-text/related-report stage. Master-applied resolved title/abstract records now equal 1109/1259, with 150 not_screened records remaining. B11 is completed; B12 remains pending. PRISMA flow remains TBD/draft_not_populated and was not populated.
- 2026-06-22 Step 5-C23 Batch B12 AI-assisted provisional screening suggestions completed: TAB-2026-06-22-B12 contains 100 records; 7 calibration_resolved records were excluded from re-screening and AI-assisted provisional suggestions were generated only for the remaining 93 not_screened records using the B11-applied master as read-only baseline. AI suggestion distribution: exclude_title_abstract=67, include_for_full_text=18, contextual_only=6, unclear_need_full_text=2. Reason code distribution: EX05=23, EX01=13, EX08=9, IN04=8, IN05=8, EX03=7, EX04=4, CTX05=4, EX02=4, EX06=4, EX07=3, UN01=2, IN03=1, CTX02=1, IN06=1, CTX01=1. Human review is pending; master screening form unchanged; resolved title/abstract decisions remain 1109/1259 and remaining not_screened remains 150 until B12 human decisions are logged. PRISMA flow remains TBD and was not populated.

## Kapsam Disi Islemler

- Mevcut PDF, Word ve checklist dosyalari degistirilmeyecektir.
- Mevcut klasor yapisi bozulmayacaktir.
- `Final search date` / actual cutoff ifadesi yalnizca gercekten yurutulen ve loglanan source exportlari icin kullanilacaktir.

## 2026-07-09 Retrieval Stop Decision - OPERATIONAL_ONLY_NOT_PRISMA_FLOW_DRAFT_PRISMA_INPUT

- User decision: stop pursuing the remaining 60 missing full-text PDFs after the documented operational retrieval phase.
- PRISMA-compliant classification: the 60 records are `reports_not_retrieved` / `full_text_not_retrieved`, not `full_text_excluded_for_eligibility_reason`.
- Current retrieval state: full-text-needed pool = 332; reports retrieved = 272; reports not retrieved = 60.
- The 272 retrieved reports may proceed to future PDF-to-Markdown conversion/readiness QA and later full-text eligibility preparation.
- No full-text eligibility assessment, data extraction, TQAF assessment, synthesis, or included-study count has started.
- Formal PRISMA flow remains TBD and must not be populated until a dedicated formal PRISMA flow step is approved.
- B13 master and existing PDF/Markdown artifacts must remain unchanged by this lock decision.

## 2026-07-19 Step 2 Full-Text Reviewer / AI / Human Adjudication Process â€” USER APPROVED LOCK

- User approved the full-text reviewer model on 2026-07-19.
- Operational model: one human final reviewer (`H1`, User) + AI-assisted provisional assessment (`A1`, Codex/ChatGPT) + deterministic structural QA.
- AI is not an independent reviewer, adjudicator, or final decision maker. AI recommendations and human final decisions must remain in separate fields.
- No dual-independent-human screening claim may be made unless a second human reviewer is actually assigned and documented.
- Human source-open review is mandatory for every proposed full-text exclusion, contextual disposition, unclear/adjudication case, related/correction report, retrieved title/abstract unclear record, date/language/publication/retraction issue, source/identity problem, low-confidence or unsupported recommendation, translation/contact consideration, and every B01 pilot record.
- Straightforward `include_primary` recommendations require explicit human batch approval plus stratified source-open QA of at least 10% and at least two records per batch. Any eligibility decision error in that sample expands source-open human review to all straightforward includes in the affected batch.
- AI tool/model or version and assessment timestamp must be recorded; unknown historical versions must not be guessed.
- Automatic translation may assist navigation only and cannot independently satisfy the English full-technical-content eligibility criterion. Author/investigator contact requires explicit user approval and an audit record.
- PRISMA 2020 Item 8 disclosure will transparently describe the single-human, AI-assisted, non-independent workflow and its limitation.
- Step 2 is a process lock only: no full-text eligibility decision, extraction, TQAF, synthesis, included-study count, or formal PRISMA flow population has occurred.
- Next gate: prepare the canonical full-text eligibility form and B01 pilot plan; do not apply eligibility decisions until that gate is reviewed.

## 2026-07-23 B01-P01 Full-Text Eligibility Kalibrasyonu

- KullanÄ±cÄ± `SCR-00001`, `SCR-00007`, `SCR-00011`, `SCR-00087` ve `SCR-00094` kaynaklarÄ±nÄ± 5/5 aÃ§arak kontrol etti.
- `SCR-00001`, `SCR-00007` ve `SCR-00011` insan onayÄ±yla `include_primary` olarak kilitlendi.
- `SCR-00087` ve `SCR-00094` iÃ§in AI Ã¶nerisi `exclude_full_text / FTX07` olmakla birlikte kullanÄ±cÄ± `Hold` seÃ§ti; bu iki kayÄ±t `unclear_adjudication / ADJ01` durumunda aÃ§Ä±k ve kilitsizdir. PRISMA full-text exclusion sayÄ±sÄ±na henÃ¼z girmez.
- B01-P01 mevcut durum: 3 tamamlanmÄ±ÅŸ `include_primary`, 2 pending adjudication. Formal PRISMA flow hÃ¢lÃ¢ TBD/not populated.
- Aktif karar Ã§alÄ±ÅŸma kitabÄ±: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_P01_2026-07-23/full_text_eligibility_B01_P01_APPLIED_2026-07-23.xlsx`.

### B01-P01 nihai adjudication dÃ¼zeltmesi

- KullanÄ±cÄ± daha sonra `SCR-00087` ve `SCR-00094` iÃ§in `exclude_full_text / FTX07` kararÄ±nÄ± aÃ§Ä±kÃ§a onayladÄ±.
- B01-P01 nihai ve kilitli daÄŸÄ±lÄ±mÄ±: 3 `include_primary`, 2 `exclude_full_text / FTX07`; pending kayÄ±t kalmadÄ±.
- Aktif nihai workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_P01_2026-07-23/full_text_eligibility_B01_P01_FINAL_2026-07-23.xlsx`.

## 2026-07-23 B01-P02 Full-Text Eligibility Final

- B01-P02 5/5 insan kaynak incelemesiyle tamamlandÄ±, QA PASS aldÄ± ve kilitlendi.
- `include_primary`: `SCR-00009`, `SCR-00038`, `SCR-00052`, `SCR-00083`.
- `exclude_full_text / FTX04`: `SCR-00060`; ayrÄ± cihaz iÅŸlevleri gerÃ§ek bir ortak sensingâ€“communication sistemi veya ortak deÄŸerlendirme oluÅŸturmuyor.
- P01 + P02 kÃ¼mÃ¼latif B01 durumu: 10/22 reviewed/locked; 7 `include_primary`; 3 `exclude_full_text` (`FTX07` = 2, `FTX04` = 1); 12 kayÄ±t kaldÄ±.
- Aktif nihai workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_P02_2026-07-23/full_text_eligibility_B01_P02_FINAL_2026-07-23.xlsx`.
- Formal PRISMA flow hÃ¢lÃ¢ TBD/not populated; data extraction, TQAF ve synthesis baÅŸlamadÄ±.
- SÄ±radaki operasyon B01-P03 beÅŸ kayÄ±tlÄ±k kaynak incelemesidir.

## 2026-07-23 B01-P03 Full-Text Eligibility Backfill Final

- B01-P03 kapsamÄ±ndaki `SCR-00008`, `SCR-00012`, `SCR-00013`, `SCR-00036` ve `SCR-00057` kullanÄ±cÄ± onayÄ±yla `include_primary` olarak kilitlendi.
- BeÅŸ kayÄ±tta 35/35 FTI kriteri `yes`; insan kararÄ±, AI provisional Ã¶nerisi ve final karar 5/5 uyumludur. Birincil dÄ±ÅŸlama nedeni alanlarÄ± boÅŸ/null bÄ±rakÄ±ldÄ±.
- Alan normalizasyonu: kullanÄ±cÄ± yanÄ±tÄ±ndaki `primary_code: include_primary`, `human_decision` ve `final_decision = include_primary` olarak kaydedildi; sÄ±ra numarasÄ± Ã¶nekleri kanonik `SCR-xxxxx` kimliklerine taÅŸÄ±nmadÄ±.
- Tarih normalizasyonu: `SCR-00036` iÃ§in acceptance tarihi yerine PDF Crossmark `VoR / 2026-01-10`; `SCR-00057` iÃ§in PDF PRISM `coverDisplayDate / 2025-06-29` kullanÄ±ldÄ±.
- P01-P03 kÃ¼mÃ¼latif B01 durumu: 15/22 reviewed/locked; 12 `include_primary`; 3 `exclude_full_text` (`FTX07` = 2, `FTX04` = 1); 7 retrieved rapor kaldÄ±.
- Nihai workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_P03_2026-07-23/full_text_eligibility_B01_P03_FINAL_2026-07-23.xlsx`.
- P02 finaline gÃ¶re beklenmeyen hÃ¼cre deÄŸiÅŸikliÄŸi ve formÃ¼l deÄŸiÅŸikliÄŸi yoktur; QA PASS.
- Formal PRISMA flow TBD/not populated olarak korundu; B13 master, extraction, TQAF ve synthesis deÄŸiÅŸtirilmedi.
- B01 backfill iÃ§in sÄ±radaki operasyon B01-P04â€™tÃ¼r; daha sonra tamamlanan B02-B04 geÃ§miÅŸ kayÄ±tlarÄ± korunmuÅŸtur.

## 2026-07-25 B01-P04/P05 Full-Text Eligibility and B01 Final

- User and Codex completed source-open review of the remaining seven retrieved B01 reports; factual assessments and final decisions agreed 7/7.
- B01-P04 `include_primary`: `SCR-00002`, `SCR-00015`, `SCR-00086`, `SCR-00091`, `SCR-00099`.
- B01-P05 `include_primary`: `SCR-00056`, `SCR-00072`.
- All seven reports satisfy FTI01â€“FTI07; 49/49 FTI assessments are `yes`. Human and final decisions are `include_primary`; primary exclusion-reason fields remain blank.
- B01 final: 22/22 reviewed and locked; 19 `include_primary`; 3 `exclude_full_text` (`SCR-00087 / FTX07`, `SCR-00094 / FTX07`, `SCR-00060 / FTX04`); contextual and unresolved/Hold = 0.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B01_FINAL_2026-07-25/full_text_eligibility_B01_FINAL_2026-07-25.xlsx`.
- B13 active master and formal PRISMA flow were not modified; extraction, TQAF and synthesis were not started.
- Next operation: B05 retrieved-report full-text eligibility source review.

## 2026-07-26 B05-P01 Full-Text Eligibility Final

- User and Codex completed source-open review of `SCR-00406`, `SCR-00407`, `SCR-00409`, `SCR-00418`, and `SCR-00432`; decision and reason agreement was 5/5.
- Final decisions: `SCR-00406`, `SCR-00407`, `SCR-00418`, and `SCR-00432` = `include_primary`; `SCR-00409` = `exclude_full_text / FTX07`.
- FTI matrix total: 34 `yes`, 1 `no`; only `SCR-00409 / FTI02` failed because pp.1-11 are the Chinese technical body and pp.12-13 are only a structured English Abstract.
- `SCR-00407` and `SCR-00432` were recorded as HRT13 stratified include-QA samples. No Hold, conflict, protocol amendment, second reviewer, or author contact was required.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B05_P01_2026-07-26/full_text_eligibility_B05_P01_FINAL_2026-07-26.xlsx`.
- B05-P01 QA PASS. Operational progress is 72/272; 56 primary, 2 contextual, 14 excluded; 200 retrieved reports remain.
- B13 active master, formal PRISMA flow, extraction, TQAF and synthesis were not modified.
- Next operation: B05-P02 source review.

## 2026-07-26 B05-P02 Full-Text Eligibility Final

- User and Codex completed source-open review of `SCR-00436`, `SCR-00440`, `SCR-00451`, `SCR-00456`, and `SCR-00460`; all five final decisions are `include_primary`.
- FTI matrix total: 35 `yes`, 0 `no`; exclusion-reason fields are blank and no Hold remains.
- Initial decision agreement was 4/5. The external source review proposed `SCR-00451 / FTX04`; Codex applied the locked FTI05 architecture/application-scenario rule and recommended inclusion. The user explicitly approved `include_primary`, and the conflict is recorded as `decision_disagreement / resolved_user_approved`.
- HRT13 include-QA samples: `SCR-00436`, `SCR-00440`; HRT03 adjudication resolved for `SCR-00451`; HRT08 publication-type verification resolved for `SCR-00460`.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B05_P02_2026-07-26/full_text_eligibility_B05_P02_FINAL_2026-07-26.xlsx`.
- Workbook SHA-256: `04781c71602cb81e5db022b85ba002c28563e1e60b00872b8d3ce217639405ab`.
- B05 cumulative after P01-P02: 10/14 reviewed; 9 primary includes; 1 `exclude_full_text / FTX07`; 4 pending.
- Operational progress is 77/272; 61 primary, 2 contextual, 14 excluded; 195 retrieved reports remain.
- B13 active master, formal PRISMA flow, extraction, TQAF and synthesis were not modified.
- Next operation: B05-P03 source review (`SCR-00473`, `SCR-00488`, `SCR-00492`, `SCR-00496`).

## 2026-07-26 B05-P03 and B05 Full-Text Eligibility Final

- User and Codex completed source-open review of `SCR-00473`, `SCR-00488`, `SCR-00492`, and `SCR-00496`; all four final decisions are `include_primary`.
- FTI matrix total: 28 `yes`, 0 `no`; independent Codex assessment and user decisions agreed 4/4, and no adjudication was required.
- HRT13 include-QA samples: `SCR-00473`, `SCR-00492`; HRT06 date check resolved for `SCR-00488`; HRT08 publication-type check resolved for `SCR-00496`.
- Final workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B05_P03_2026-07-26/full_text_eligibility_B05_P03_FINAL_2026-07-26.xlsx`.
- Workbook SHA-256: `5ca43de0e9649fd3d5b4d76ec819b8dee9e6bd0b6f14140093a275ee752ca41e`.
- B05 final: 14/14 reviewed; 13 primary inclusions; 1 `exclude_full_text / FTX07`; 0 pending or unresolved.
- Operational progress is 81/272; 65 primary, 2 contextual, 14 excluded; 191 retrieved reports remain.
- B13 active master, formal PRISMA flow, extraction, TQAF and synthesis were not modified.
- Next operation: B06-P01 source review (`SCR-00502`, `SCR-00506`, `SCR-00508`, `SCR-00523`, `SCR-00527`).

## 2026-07-27 B06 Full-Text Eligibility Final

- User-provided source-open assessments and Codex checks were completed for all 13 retrieved B06 reports; all final decisions are human/User approved and locked.
- `include_primary` (9): `SCR-00502`, `SCR-00506`, `SCR-00527`, `SCR-00553`, `SCR-00557`, `SCR-00576`, `SCR-00589`, `SCR-00592`, `SCR-00594`.
- `exclude_full_text` (4): `SCR-00508 / FTX03`; `SCR-00523 / FTX07`; `SCR-00528 / FTX07`; `SCR-00571 / FTX07`. Contextual and Hold = 0.
- `SCR-00527` was resolved from an external-source-set Hold to `include_primary`: the local 14-page English full text was opened and showed the same m-CAP VLC signal supporting data transmission and RSS trilateration; the user explicitly approved inclusion.
- Canonical workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B06_FINAL_2026-07-27/full_text_eligibility_B06_FINAL_2026-07-27.xlsx`.
- Workbook SHA-256: `dd67e541b9672f4dd3442b3814683a5e8ed1620db56c9c5be4ea9b4288fda4c0`.
- Workbook QA: 13/13 source-opened, 13/13 locked, 13/13 row QA PASS, formula-driven QA PASS, formula-error matches = 0, Hold = 0.

## 2026-07-27 B07 Full-Text Eligibility Final

- User-provided source-open assessments and Codex checks were completed for all 13 retrieved B07 reports; all final decisions are human/User approved and locked.
- `include_primary` (9): `SCR-00602`, `SCR-00607`, `SCR-00619`, `SCR-00626`, `SCR-00631`, `SCR-00647`, `SCR-00665`, `SCR-00679`, `SCR-00680`.
- `retain_contextual` (1): `SCR-00656`, a directly relevant 6G-EWOC architecture/roadmap without completed independently evaluable technical validation.
- `exclude_full_text` (3): `SCR-00606 / FTX01`; `SCR-00623 / FTX03`; `SCR-00689 / FTX06`. Hold = 0.
- Canonical workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B07_FINAL_2026-07-27/full_text_eligibility_B07_FINAL_2026-07-27.xlsx`.
- Workbook SHA-256: `52cf6ed54d30bb659f170469f9e7b92fce3c3e8b849bbab6542a4d9a6ed6afe8`.
- Workbook QA: 13/13 source-opened, 13/13 locked, 13/13 row QA PASS, formula-driven QA PASS, formula-error matches = 0, Hold = 0.
- Cumulative operational state after B07: 107/272 reviewed; 83 primary, 3 contextual, 21 excluded; 165 retrieved reports remain.

## 2026-07-27 B08â€“B13 Source-Review Prompt Package

- A complete prompt package was generated for every remaining retrieved report: 165 reports in 35 standalone parts (`B08`=2, `B09`=4, `B10`=13, `B11`=11, `B12`=4, `B13`=1).
- Package: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_prompt_packages_B08_B13_2026-07-27/`.
- ZIP SHA-256: `ee2c27220830a0f76c267f4370f815da5002cb1cfd69b1ca68dfb2b322486f71`.
- Independent QA confirmed exact canonical ID/title/batch/source order, 165 unique manifest rows, 35 valid part sizes, 165 existing PDF paths, correct per-prompt source counts and output templates, and no premature eligibility decisions.
- Five B12 `report_not_retrieved` records (`SCR-01148`, `SCR-01150`, `SCR-01157`, `SCR-01163`, `SCR-01164`) remain outside the 272-report eligibility universe and appear only in the package README appendix.
- This package changes no B08â€“B13 scientific decision. Next operation: run `B08/B08_P01_prompt.txt` and return its source-review output for human/Codex comparison and lock.

## 2026-07-27 B08 Full-Text Eligibility Final

- User-approved source-open B08 review is complete for 10/10 reports.
- `include_primary` (7): `SCR-00719`, `SCR-00722`, `SCR-00730`, `SCR-00731`, `SCR-00761`, `SCR-00763`, `SCR-00784`.
- `exclude_full_text` (3): `SCR-00715 / FTX06`, `SCR-00755 / FTX02`, `SCR-00766 / FTX04`; contextual/Hold = 0.
- `SCR-00755` was adjudicated from external inclusion to communication-only exclusion because the current experiment does not integrate optical-cable/DAS sensing. `SCR-00766` is a valid full conference paper, so the external FTX05 code was refined to FTX04.
- Four related-report mappings were documented for study-level double-count control without changing report-level eligibility.
- Canonical workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B08_FINAL_2026-07-27/full_text_eligibility_B08_FINAL_2026-07-27.xlsx`.
- Workbook SHA-256: `ebf3a848b0de49378f49a566a81b5eb8265152c3bedddc20688c36ec6205bf1a`.
- Workbook QA: 10/10 source-opened, 10/10 locked, 10/10 row QA PASS, formula-driven QA PASS, formula-error matches = 0, Hold = 0.
- Cumulative operational state after B08: 117/272 reviewed; 90 primary, 3 contextual, 24 excluded; 155 retrieved reports remain.
- Formal PRISMA flow, extraction, TQAF and synthesis remain unchanged/not started.

## 2026-07-27 B09-P02 Full-Text Eligibility Lock

- The user explicitly approved the independently source-checked B09-P02 package with `P02 OK`.
- `include_primary` (5): `SCR-00884`, `SCR-00885`, `SCR-00886`, `SCR-00887`, `SCR-00889`; contextual, exclusion and Hold = 0.
- Two related-report mappings were documented: `SCR-00886` is the OFC conference version extended by `SCR-01075`, while `SCR-01150` is an exact DOI-alias duplicate of the same OFC W4J.2 report; `SCR-00889` is provisionally linked to the distinct-results predecessor/companion `SCR-00900`, pending reciprocal confirmation in B09-P04.
- `SCR-01150` is superseded from historical `RPT01` to `RPT02 / exact_duplicate`. The locked 2026-07-09 60-row retrieval checkpoint remains unchanged for auditability; the current unresolved RPT01 interpretation is 59.
- Part-lock workbook: `systematic_review_workflow/09_kayitlar/checkpoints/full_text_eligibility_B09_P02_LOCK_2026-07-27/full_text_eligibility_B09_P02_LOCK_2026-07-27.xlsx`.
- Workbook SHA-256: `58ef65e57260034681b62fd5e50915fa6bd999563b7ebef1c10ce10e80a27244`.
- Workbook QA: 5/5 source-opened, 5/5 locked, 5/5 row QA PASS, formula-driven QA PASS, formula-error matches = 0, two mapping rows documented.
- Cumulative operational state after B09-P02: 122/272 reviewed; 95 primary, 3 contextual, 24 excluded; 150 retrieved reports remain.
- Current submitted group is B09-P01; B09-P03/P04 remain pending. Formal PRISMA flow, extraction, TQAF and synthesis remain unchanged/not started.

## 2026-08-07 PRISMA public-release staging package

- A clean, versioned staging package was built without modifying the active manuscript.
- Canonical Phase-D source SHA-256: `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`.
- Public workbook SHA-256: `faba81fb212deb1851b44d75b6cfc742ad9c78c9c917dc58f050dc5da16a8f74`.
- Workbook/CSV projections cover 206 studies, 232 lineage rows, 39 exclusions, 3,041 evidence rows, 2,559 conditions, 4,861 metrics, 404 trade-offs, 8,306 claim decisions, 206 TQAF rows, 115 evidence bodies and 4,931 body-membership links.
- Reopen, row-count, local-path/email, prohibited-field and formula-error QA passed with zero findings; a checksum manifest was generated.
- Only the review-authored PRISMA flow PDF is included. Publisher PDFs, full text, restricted database exports, local paths, actor identifiers and long source-derived prose were excluded.
- External publication is blocked only by creator/affiliation/ORCID metadata, rights-holder/license confirmation, clean GitHub route and Zenodo DOI.
- Existing `review_ISAC` GitHub release is a legacy 220-study state and must be marked superseded, not reused or deleted.
- Existing monorepo tracks 317 PDFs; whole-repository GitHub/Zenodo source archiving is prohibited for this release.

## 2026-08-13 COMST 206 nine-section survey candidate â€” historical snapshot

- A non-destructive survey-first manuscript candidate was created at `systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`.
- Source/rollback candidate `comst_206_v1/` remains present and preserved. No v1 file was replaced as part of the v2 restructuring.
- Observed structure is one abstract plus nine main sections, matching `MANUSCRIPT_STRUCTURE.json` and `MANUSCRIPT_BODY_INPUTS.tex`.
- Final manuscript integrity QA, evidence-assertion QA and survey-architecture QA all report `PASS`. Candidate-lineage QA also reports `PASS`. The final artifacts are under the candidate's `qa/` directory.
- Visual-contract QA reports `PASS` for 16/16 carriers and 221/221 checks with zero failures. This is a specification gate, not evidence that figures or pending tables have been generated.
- The visual/table contract contains 16 main-text carriers: eight figures and eight tables. Table I is implemented in the Introduction; seven tables and eight figures remain blueprints. No figure was generated in this pass.
- LaTeX compilation, rendered inspection and page-layout QA were intentionally not performed.
- Author review is pending. The candidate is not submission-ready and must not be described as approved, typeset or final.
- Locked review science and denominators were not changed. The Phase-C, Phase-D, Phase-E and Phase-F authorities, public-release staging package and historical unpublished 220/221-study manuscript remain separate and unchanged.
- Deterministic directory digests, calculated as SHA-256 over sorted `relative-path<TAB>file-SHA256` lines at checkpoint time: v1 `CA0A7B234901779061CB3F7EF996C261BF62655382047420945E0388B4C04F2B`; v2 `BE1BC69DD190BC891323308D183CCB81F08EFBA871A51D7DC8BC0AC367363F37`.
- Key v2 hashes: `MANUSCRIPT_STRUCTURE.json` `8BF797BB6B18984E6FE438A178795D1C3C4D57968308C95803640062172931E6`; `MANUSCRIPT_BODY_INPUTS.tex` `C6079E3FD39D8985845A7A2ED09FB1D49F7EFBEEF06CB0F3BA5EA337EF002E1A`; final integrity QA `CF1DBA5A4E44E509831DB6EE45FC7B75E359A18999EABCE1C2051AAEBB52E4F7`; final evidence QA `341F65AF3BC1CEBC69BF0B7301B59D42DD06640E9571499CC7D074DB55FF7520`; final architecture QA `10C5734C71FEEBC008F5B54B0F7DA17A2FCA9404D46034E5AC60289AB00DE93D`; final lineage QA `E51110DEDD965F86D2C43F74641686213B400DBED6FFDDD293F4D45947EE1D6B`; final visual-contract QA `3BE665CF2E62854E16B1B8FD5ABAE3B25CE230A9911FAA77CB1DE5EFF765D8CB`.
- Checkpoint: `systematic_review_workflow/09_kayitlar/checkpoints/comst_manuscript_9section_RESTRUCTURED_2026-08-13/README.md`.
- Next operation: author review of the complete nine-section reading version; only after that review should the remaining 15 visual/table carriers be materialized and the manuscript compiled and rendered for layout QA.

## 2026-08-14 COMST 206 post-fix full re-audit â€” superseded by the current nonvisual-closeout block above

- A first-principles re-audit was triggered by the discovery that the active
  prose exposed only 76 of the 206 included studies through citation commands.
  The 76-paper COMST corpus remained a style/architecture benchmark only; the
  locked 206-study evidence remained the scientific authority.
- PRISMA Item 17 is now locally closed with citation-linked ST-01: 206 study
  rows, 206 real row citations, 206 exact bibliography keys, and 227 eligible
  report rows. The main prose retains selective claim-attached citations rather
  than becoming a citation catalogue.
- Journal-candidate supplements now materialize 39 exclusions; 3,020 evidence
  rows; 4,779 metrics; 404 governed and 402 substantive tradeoffs; 206 TQAF
  rows; 115 evidence bodies; 4,931 memberships; 38 contextual syntheses; and a
  206/12/6 paired-function validation join. Missing function-specific S7
  locators remain `NR` and were not inferred.
- Search, protocol, four dated protocol records, eight deviations, 446 data
  dictionary fields, and conduct boundaries are packaged locally. Two Taylor
  & Francis query-to-export mappings remain explicitly unreconstructed.
- The abstract is exactly 250 words. A source-verified front-matter candidate
  records Fatih DÃ¶nmez, Ahmet Altuncu, and Mustafa Namdar in survey order,
  verified affiliations and emails, Fatih DÃ¶nmez's ORCID, no support, no
  competing interests, and retrospective OSF registration. Coauthor ORCIDs and
  CRediT roles were not invented.
- Sentence-level claim re-audit corrected 11 findings. The post-fix integrated
  gate passes 32/32 checks; the post-fix static integrity audit has zero hard
  failure groups; the post-fix PRISMA distribution is 29 READY, 6 PARTIAL,
  0 OPEN, and 7 JUSTIFIED_NA.
- The live QA pointer is `comst_206_v2_9section/qa/CURRENT_QA_INDEX_2026-08-13.md`.
  Earlier `FINAL_*` and pre-fix PRISMA reports are historical snapshots.
- Submission and public release remain false. Table I is live, but eight
  figures and Tables II--VIII, the driver, compilation/rendering, final author
  approval, rights/licenses, and persistent release are still pending.
- Checkpoint:
  `systematic_review_workflow/09_kayitlar/checkpoints/comst_manuscript_POSTFIX_FULL_REAUDIT_2026-08-13/README.md`.

