## A. Executive summary

The article is a systematic review of how optical and photonic systems combine communication and sensing, and when reported results can support design comparisons. Its frozen evidence base is **227 eligible reports representing 206 studies**. The current author-reading draft is the September eight-section, 20-page manuscript in `OISAC_PRISMA_COMST_current`; the August nine-section manuscript in `prisma2020Review` is earlier work. Technical QA passed for the current PDF, but author scientific approval, the joint OSF update, and journal submission remain open. (`C/handoff/state.md:1–37,75–86`; `P/START_HERE_OISAC_PRISMA_CURRENT.md:7–38`)

*Path key throughout: `P/` = `C:\OISAC\prisma2020Review\`; `C/` = `C:\OISAC\OISAC_PRISMA_COMST_current\`. Inspection was read-only on 1 October 2026.*

## B. Project identity card and verification

- **Current title:** *Optical Integrated Sensing and Communication for 6G Through a Systematic Review of Architectures, Metrics, and Tradeoffs Across Optical Platforms*. (`C/manuscript/main.tex:34–36`)
- **Topic and review type:** O-ISAC across fiber, free-space optical, VLC/LiFi, photonic terahertz, and hybrid systems; a PRISMA-grounded narrative systematic review with scoping-style PCC mapping. No meta-analysis. (`P/AGENTS.md:21–48`; `C/supplement/methods.md:5–11,85–93`)
- **Research questions:** The protocol’s main question asks what the literature establishes about architectures, metric reporting and comparability, tradeoffs, validation, benchmarking, and 6G gaps; RQ1–RQ7 divide those topics. The live Section VII instead presents five **prospective experimental questions**, not seven new review results. (`P/systematic_review_workflow/00_baslangic/01_konu_ve_soru_formu.md:160–194`; `C/manuscript/sections/08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex:25–34`)
- **Intended journal:** *IEEE Communications Surveys & Tutorials* (COMST), as shown in the live IEEEtran header. The 20–30-page target is a project rule, not a locally verified publisher limit. (`C/manuscript/main.tex:1,56–58`; `C/governance/V3_ACTIVE_WRITING_RULES.md:3–12`)
- **Primary scope:** Peer-reviewed full technical reports first publicly available **1 January 2020–22 June 2026**, with sufficient English technical content, a material optical/photonic role, genuine joint treatment, and an assessable contribution. A “6G” keyword or two numerical metrics is not required. (`P/systematic_review_workflow/09_kayitlar/checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/full_text_eligibility_criteria_LOCKED_2026-07-19.md:27–57`)

**Fifteen source spot-checks**

| # | Claim checked | Finding | Direct source |
|---:|---|---|---|
| 1 | Current title | **VERIFIED** | `C/manuscript/main.tex:34–36` |
| 2 | PCC narrative systematic review; protocol RQ1–RQ7 | **VERIFIED** | `P/AGENTS.md:21–24`; `P/.../01_konu_ve_soru_formu.md:160–194` |
| 3 | COMST is the intended journal | **VERIFIED as intent**, not as a submission or publisher-rule check | `C/manuscript/main.tex:56–58`; `C/governance/V3_ACTIVE_WRITING_RULES.md:3–12` |
| 4 | September draft is current: eight sections, 20 pages, five figures, seven tables | **VERIFIED**; PDF SHA-256 matches QA | `C/handoff/state.md:5–37`; `C/governance/qa/flow/result.json:1–9,66–83`; live `C/output/pdf/flow.pdf` hash |
| 5 | Executed eligibility cutoff is 22 June, superseding planned 30 June | **VERIFIED** | locked criteria above, `:27–46`; `C/supplement/methods.md:9–11` |
| 6 | Six sources, 19 runs, 1,733 exports | **VERIFIED** | `C/supplement/methods.md:13–29` |
| 7 | 472 duplicates plus two metadata records removed; 1,259 screened | **VERIFIED** | `P/systematic_review_workflow/09_kayitlar/checkpoints/prisma_flow_PHASE_C_FINAL_2026-07-30/PHASE_C_PRISMA_FLOW_FINAL_REPORT_2026-07-30.md:25–39` |
| 8 | 330 unique reports sought, 58 unretrieved, 272 assessed | **VERIFIED**; historical 332/60 uses source records before two alias consolidations | Phase C report `:14–23` |
| 9 | M5 calls all 227 “primary reports” | **WRONG:** 227 are **eligible reports**: 206 primary plus 21 companions, yielding 206 studies | `C/supplement/methods.md:31–45`; `P/.../PHASE_B_REPORT_TO_STUDY_FINAL_LOCK_REPORT_2026-07-30.md:20–42` |
| 10 | 39 full-text exclusions, six contextual-only, 227 eligible | **VERIFIED** | Phase C report `:41–67` |
| 11 | OSF `7f6wb` is retrospective; its 221 is a predecessor state | **VERIFIED**; 221→206 is not attrition | `P/systematic_review_workflow/01_protokol/04_protocol_registration_lineage_correction_2026-08-07.md:7–36` |
| 12 | 8,306 governed claims; 8,203 primary synthesis records; 72 quarantined | **VERIFIED** | `P/.../data_extraction_PHASE_D_SURVEY_READY_2026-08-04/README.md:3–24`; `C/supplement/methods.md:65–75` |
| 13 | No routine independent duplicate human review; TQAF is review-specific | **VERIFIED** | `C/supplement/methods.md:49–58,77–83` |
| 14 | The final-state materials are already accessible on OSF | **UNVERIFIABLE from local files**; the manuscript says “available,” while the handoff says the update remains open | `C/manuscript/sections/01_INTRODUCTION.tex:194–200`; `C/handoff/state.md:75–79`; `C/supplement/index.md:105–109` |
| 15 | Git working state | **VERIFIED locally:** `P` at `439c991` has 9,823 tracked deletions; `C` is clean at `2389545` on `rev/flow-20260916` | Read-only `git status`, `rev-parse`, and `show`; `C/handoff/state.md:5–14` |

**Conflicts resolved:** The September live source governs article wording; the August handoff governs dated review history. The locked **22 June** cutoff overrides older 30 June plans. **332/60** and **330/58** are different counting units, not competing eligibility outcomes. M3’s Section VII label is stale: the live heading is **“Research Questions and Evaluation Priorities.”** The manuscript’s OSF availability sentence must be checked against the remote archive before submission. (`C/manuscript/sections/08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex:1`; sources in checks 4, 5, 8, 14)

## C. Methods status

| Step | Status | Governing file |
|---|---|---|
| Protocol and registration lineage | Documented; OSF registration retrospective | `P/systematic_review_workflow/01_protokol/04_protocol_registration_lineage_correction_2026-08-07.md` |
| Eligibility | Locked | `P/systematic_review_workflow/09_kayitlar/checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/full_text_eligibility_criteria_LOCKED_2026-07-19.md` |
| Search | Executed; Taylor & Francis query mapping and interface counts incomplete | `C/supplement/methods.md` |
| Screening, retrieval, full text | Locked; counting units reconciled | `P/systematic_review_workflow/09_kayitlar/checkpoints/prisma_flow_PHASE_C_FINAL_2026-07-30/PHASE_C_PRISMA_FLOW_FINAL_REPORT_2026-07-30.md` |
| Report-to-study mapping | Locked: 227 reports → 206 studies | `P/systematic_review_workflow/09_kayitlar/checkpoints/report_to_study_mapping_PHASE_B_FINAL_LOCK_2026-07-30/PHASE_B_REPORT_TO_STUDY_FINAL_LOCK_REPORT_2026-07-30.md` |
| Extraction and claim governance | Complete; 72 exact claims quarantined | `P/systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_SURVEY_READY_2026-08-04/README.md` |
| TQAF and S1–S7 synthesis | Complete, descriptive; no pooled model | `P/systematic_review_workflow/05_kalite_kanit/01_yanlilik_riski_ve_kanit_kesinligi.md`; `C/supplement/methods.md` |
| Current reporting checklist and archive | Open | `C/governance/flow.md:39–53`; `C/supplement/index.md:101–109` |

## D. Manuscript readiness

| Section | Status | Main gap |
|---|---|---|
| Title, abstract, front matter | Live in `C/manuscript/main.tex` and `sections/00_ABSTRACT.tex` | Author and coauthor approval |
| I, including Methods I-C | Live; Fig. 1 present | Verify OSF availability sentence; complete current PRISMA checklist |
| II–IV, foundations through paired outcomes | Live and technically QA-checked | Author scientific reading; retain source conditions |
| V–VI, validation and applications | Live and technically QA-checked | Author reading; keep 12/6 field evidence and illustrative equations bounded |
| VII–VIII, prospective questions, limitations, conclusion | Live and technically QA-checked | Author reading |
| References and supplement | BibTeX compiles; six-page profiles and frozen v10 indexed | Historical COMST031 metadata issue; OSF update |

The current QA reports PASS, but explicitly does not confer scientific approval. (`C/governance/qa/flow/result.json:1–9,51–83`; `C/handoff/state.md:75–86`)

## E. Constraints and rules

- This request is read-only: no file or Git changes and no access to `tmp/pdfs/pb01-visual/chrome-profile`. (`C:\OISAC\CLAUDE.md:9–16`)
- Preserve frozen evidence and distinguish records, reports, studies, metrics, and relationships. (`C/AGENTS.md:20–23`)
- Use source locations, metric definitions, measurement planes, budgets, conditions, and baselines for scientific claims. (`C/supplement/methods.md:57–75`)
- AI-assisted proposals and deterministic QA do not establish independent duplicate human review. (`C/supplement/methods.md:49–58`)
- TQAF is neither conventional risk of bias nor GRADE; low quality alone did not exclude studies. (`C/supplement/methods.md:77–83`)
- The 118 comparison records are conditional candidates; six of 12 field studies reporting both domains do not prove simultaneous operation. (`C/handoff/state.md:45–52`)
- No meta-analysis, universal frontier, platform ranking, formal publication-bias analysis, or sensitivity analysis was performed. (`C/supplement/methods.md:85–93`)
- The 58 unretrieved reports are not full-text exclusions; search provenance has stated gaps. (`C/supplement/methods.md:27–33`)
- The August PRISMA worktree’s 9,823 tracked deletions need reconciliation before any Git write; recovery copies remain read-only. (`C:\OISAC\CLAUDE.md:13–15`; read-only Git status)
- Keep publisher full texts and credentials outside a public package; GitHub transfer does not update OSF. (`C/AGENTS.md:29–39`; `C/supplement/index.md:105–109`)

## F. Where we left off

The **last recorded session, 30 September**, transferred the September branch and changed five continuity files only; the scientific revision was committed on **16 September**. There is no identified half-edited manuscript file. Resume with **author scientific reading of `C/output/pdf/flow.pdf`, `C/output/pdf/profiles.pdf`, and `C/compare.md`**, recording page-specific corrections or explicit approval. (`C/handoff/state.md:1–14,75–86`; read-only Git `show 2389545`)

**Next 10 tasks, dependency order:**

1. Record the author’s scientific comments or approval on the current reading package.
2. Apply approved corrections in the September source.
3. Rebuild, recheck citations and figures, and visually inspect changed pages against a new PDF hash.
4. Agree the exact OSF carrier set and rights for release.
5. Complete the joint OSF update while retaining retrospective-registration history.
6. Verify remote files and reconcile the article’s present-tense access sentence.
7. Complete a PRISMA 2020 checklist against the **current** section and supplement locations.
8. Resolve and document COMST031’s historical style-corpus metadata classification.
9. Record final coauthor approval and submission declarations; decide whether the separate sanitized data/code release and requested GitHub comment are still wanted.
10. Prepare journal metadata and cover letter, run final QA on the approved build, then obtain submission authorization. (`C/handoff/state.md:75–86`; `C/supplement/index.md:101–109`)

## G. Friction points with Codex

- The author called earlier prose too heavy. Keep the technical chain and plain English in the article; put process history in handoff or supplement. (`C/handoff/history/memory.md:81–95`)
- The author asked Codex to use existing TeX before spending effort on PDFs. Read source first; use the PDF for layout checks. (`C/handoff/history/memory.md:84–86`)
- Absence of a local Git `origin` was mistaken for absence of the GitHub repository. Check sibling checkout records and the named repository before concluding it is missing. (`C/handoff/history/r07.md:14–31`)
- A reported relationship-map patch had no file at its target path. Verify deliverable existence and content before reporting completion. (`C/handoff/history/memory.md:182–212`)
- Historical section gates, figure restrictions, checklist scores, and QA PASS labels were mistaken for current authority or author approval. Start with `C/AGENTS.md`, `handoff/state.md`, and the live TeX. (`C/AGENTS.md:3–32`; `C/handoff/index.md:30–42`)

## H. Questions only the user can settle

- Do you approve the September scientific draft, or which pages and claims need revision?
- Which supporting files and release rights do you approve for the joint OSF update?
- Do you still want a separate sanitized public data/code release?
- Did “comments” mean a GitHub PR or issue comment, beyond the completed push?
- Have any coauthor approvals, OSF actions, or journal submissions occurred since the 30 September handoff?

## I. Key file index

1. `C:\OISAC\CLAUDE.md` — workspace protections; **current rule**.
2. `P/AGENTS.md` — PRISMA project rules; **current for evidence work**.
3. `P/START_HERE_OISAC_PRISMA_CURRENT.md` — August handoff; **stale for manuscript layout**.
4. `P/PROJECT_CONTEXT_OISAC_PRISMA.md` — detailed review history; **dated context**.
5. `P/systematic_review_workflow/00_baslangic/01_konu_ve_soru_formu.md` — protocol questions; **historical wording**.
6. `P/systematic_review_workflow/09_kayitlar/checkpoints/prisma_pre_full_text_eligibility_gate_step1_2026-07-19/full_text_eligibility_criteria_LOCKED_2026-07-19.md` — **current locked eligibility**.
7. `P/systematic_review_workflow/09_kayitlar/checkpoints/prisma_flow_PHASE_C_FINAL_2026-07-30/PHASE_C_PRISMA_FLOW_FINAL_REPORT_2026-07-30.md` — **locked flow**.
8. `P/systematic_review_workflow/09_kayitlar/checkpoints/report_to_study_mapping_PHASE_B_FINAL_LOCK_2026-07-30/PHASE_B_REPORT_TO_STUDY_FINAL_LOCK_REPORT_2026-07-30.md` — **locked report mapping**.
9. `P/systematic_review_workflow/09_kayitlar/checkpoints/data_extraction_PHASE_D_SURVEY_READY_2026-08-04/README.md` — extraction and quarantine closeout; **current evidence**.
10. `P/systematic_review_workflow/05_kalite_kanit/01_yanlilik_riski_ve_kanit_kesinligi.md` — TQAF rules/results; **current evidence**.
11. `P/systematic_review_workflow/06_sentez/outputs/phase_f_s1_s7_2026-08-04/PHASE_F_S1_S7_PUBLICATION_SUMMARY.md` — synthesis counts; **current evidence**.
12. `C/AGENTS.md` — September worktree rules; **current**.
13. `C/handoff/state.md` — resume point and open work; **current**.
14. `C/compare.md` — September revision comparison; **current**.
15. `C/manuscript/main.tex` — title, authors, article driver; **current**.
16. `C/manuscript/MANUSCRIPT_BODY_INPUTS.tex` — eight-section input order; **current**.
17. `C/manuscript/sections/01_INTRODUCTION.tex` — Methods I-C and OSF sentence; **current, archive claim pending verification**.
18. `C/supplement/methods.md` — executed methods and limitations; **current**.
19. `C/supplement/index.md` — frozen v10 carrier map and checklist status; **current**.
20. `C/output/pdf/flow.pdf` — 20-page author-reading copy; **current, not author-approved**.