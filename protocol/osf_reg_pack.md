# OSF Registration Pack for O-ISAC Systematic Survey

Prepared on: 2026-02-12  
Target: IEEE Communications Surveys & Tutorials (COMST) survey article.  
Scope: Register this survey on OSF using the "Generalized Systematic Review" template (closest available OSF template for PRISMA-based work).

---

## 1) OSF Submission Runbook (Current)

Use this flow in OSF:

1. Open your OSF project.
2. Click `Registrations` -> `New registration`.
3. Choose template: `Generalized Systematic Review`.
4. Complete the form using Section 3 of this file.
5. Choose visibility:
   - Public now, or
   - Embargo (OSF allows embargoed registrations; max duration is up to 4 years).
6. Submit registration.
7. Track status in `Registrations`; OSF indicates submissions enter pending moderation and are typically approved within about 48 hours.

Notes from OSF docs:
- Registrations are read-only snapshots after submission.
- A DOI is minted once registration is accepted.

Official references:
- https://help.osf.io/article/330-create-registrations
- https://help.osf.io/article/193-read-only-link-for-registrations

---

## 2) Files to Attach in OSF Project Before Registration

Upload or confirm these files exist in the OSF project before freezing:

- `protocol/prisma_proto.md`
- `protocol/prisma_2020_chk.md`
- `search/search_strings.md`
- `drafts/section_03_methodology.md`
- `screening/prisma_flow_counts.csv`
- `screening/excluded_fulltext_log.csv`
- `README.md`

Optional but recommended:

- `search/search_log.csv` (finalized formal database log for the 2025-11-30 IEEE/Scopus/WoS freeze)
- `search/dedup_log.csv` (best available row-level dedup ledger; still partial relative to the canonical `duplicates_removed = 280`)
- `search/dedup_reconstruction_status.md` (documents the remaining dedup evidence gap)

---

## 3) Copy-Paste Answers for OSF "Generalized Systematic Review" Form

Use the following answers directly. Replace all `TO_FILL` values before submit.

### Review Methods

- Type of review *
  - Systematic survey for IEEE COMST, employing PRISMA 2020 and PRISMA-S methodology, with qualitative narrative synthesis and quantitative descriptive trade-off synthesis (no pooled-effect meta-analysis).

- Review stages *
  - Preparation -> Search -> Deduplication -> Title/Abstract Screening -> Full-Text Eligibility -> Data Extraction -> Technical Quality Appraisal (TQAF) -> Synthesis -> Reporting.

- Current review stage *
  - Synthesis and manuscript drafting stage. Search/screening completed and current included corpus is N=220 (as documented in `drafts/section_03_methodology.md` and `screening/prisma_flow_counts.csv`).

- Start date *
  - `TO_FILL_START_DATE_YYYY-MM-DD`

- End date *
  - `TO_FILL_END_DATE_YYYY-MM-DD`

- Background *
  - This survey addresses the lack of a unified, systematic synthesis of Optical Integrated Sensing and Communication (O-ISAC) across both cabled fiber systems and wireless optical systems (FSO/VLC/LiDAR-like). Existing surveys are fragmented by modality and rarely use PRISMA-style reproducible workflows. This survey builds a unified physical-layer taxonomy covering four optical modalities (fiber, FSO, VLC/LiFi, photonic-THz), maps sensing-communication coupling mechanisms, and analyzes reported trade-offs (rate, range, resolution, reliability) with explicit methodological quality appraisal (TQAF). The target venue is IEEE Communications Surveys & Tutorials (COMST).

- Primary research question(s) *
  - RQ1: How are sensing and communication jointly realized in cabled and wireless optical systems via shared hardware, spectrum, and/or waveforms under a unified physical-layer model?
  - RQ2: Which signal/channel models and trade-off quantification practices are used, and how are communication and sensing performances jointly characterized?
  - RQ3: Which methodological and architectural gaps remain, and what are the implications for 6G-oriented enabling technologies (including optical RIS/OPA contexts)?

- Secondary research question(s) *
  - How consistently are metrics reported across modalities (fiber, FSO, VLC, LiDAR-like/retroreflective)?
  - Which reporting and reproducibility gaps most limit cross-study comparability?

- Expectations / hypotheses *
  - We expect strong heterogeneity in metrics and scenarios, preventing formal pooled meta-analysis.
  - We expect recurrent rate-range-resolution and communication-sensing coupling trade-offs.
  - We expect frequent methodological optimism patterns (idealized assumptions, incomplete uncertainty reporting) in parts of the literature.

- Dependent variable(s) / outcome(s) / main variables *
  - Communication outcomes: data rate, spectral efficiency, BER/BLER, latency, reliability.
  - Sensing outcomes: range, resolution, estimation error (RMSE), detection metrics, CRB/FIM-linked indicators when available.
  - Joint outcomes: explicit sensing-communication trade-off characterizations (curves/fronts or controlled operating points).

- Independent variable(s) / intervention(s) / treatment(s) *
  - Optical medium/domain (fiber, FSO, VLC, LiDAR-like, retroreflective).
  - Waveform/modulation and transceiver design choices.
  - Channel/impairment model assumptions (e.g., turbulence, pointing error, nonlinearities, ambient noise).
  - Resource-sharing/integration strategy (time/frequency/power/waveform co-design).

- Additional variable(s) / covariate(s) *
  - Validation type (analytical/simulation/experimental/hybrid), uncertainty reporting, baseline presence, reproducibility signals, publication venue/year.

- Software *
  - Python 3.x scripts and notebooks for data handling and screening workflows.
  - CSV-based logs for search/screening/exclusion tracking.
  - Digitization tooling for figure-only values when needed (flagged with provenance).

- Funding *
  - `TO_FILL_FUNDING_STATEMENT` (or "No external funding.")

- Conflicts of interest *
  - `TO_FILL_CONFLICTS_STATEMENT` (or "No conflicts of interest declared.")

- Overlapping authorships *
  - Potential overlap with included studies will be handled by excluding conflicted reviewer(s) from screening/extraction/quality decisions for those records; adjudication will be delegated to an independent co-reviewer/supervisor.

### Search Strategy

- Databases *
  - IEEE Xplore, Scopus, Web of Science Core Collection.
  - Supplementary/targeted sources (as planned in protocol): Optica Publishing Group platform, SPIE Digital Library.

- Interfaces *
  - IEEE Xplore web interface, Scopus web interface, Web of Science web interface.
  - Platform-native interfaces for Optica and SPIE.

- Grey literature *
  - Preprints tracked via arXiv and TechRxiv; preprints linked to peer-reviewed versions when available.

- Inclusion and exclusion criteria *
  - Inclusion: peer-reviewed journal articles and full conference papers with optical ISAC at physical/link layer and sufficient technical detail for taxonomy/trade-off extraction.
  - Exclusion: RF-only ISAC without optical carrier, pure sensing-only, pure communication-only, non-peer-reviewed sources, non-English items.

- Query strings *
  - Full database-specific strings are archived in `search/search_strings.md`.
  - Core logic: `(ISAC/joint sensing-communication terms) AND (optical medium terms)`.

- Search validation procedure *
  - Validation set approach: ensure known O-ISAC papers are retrievable; iteratively adjust query blocks and test exclusion terms to avoid false negatives.

- Other search strategies *
  - Backward/forward snowballing and targeted venue checks in optics/communications proceedings.

- Procedures to contact authors *
  - For critical missing parameters in key studies, corresponding authors may be contacted using structured requests.

- Results of contacting authors *
  - Contact outcomes (response/no response and data receipt status) will be documented in survey artifacts if author contact is performed.

- Search expiration and repetition *
  - Search updates are planned before final manuscript freeze; living-search checks may continue during drafting.

- Search strategy justification *
  - Multi-database design is required to cover communications + photonics ecosystems and reduce venue-specific bias. Query design balances recall and precision using block logic and validation checks.

- Miscellaneous search strategy details *
  - Last recorded search date in current working materials: 2025-11-30 (see `drafts/section_03_methodology.md` and `search/search_strings.md`).

### Screening

- Screening stages *
  - Deduplication -> title/abstract screening -> full-text eligibility.
  - Human-led process with two independent reviewers for screening decisions.

- Screened fields / blinding *
  - Title, abstract, keywords (phase 1); full text (phase 2).
  - No formal blinding currently planned.

- Used exclusion criteria *
  - Wrong domain (RF-only), pure sensing-only, pure communication-only, insufficient physical-layer detail, non-eligible publication type, language/type exclusions.

- Screener instructions *
  - Criteria and operational rules are defined in `protocol/prisma_proto.md` (Section 4 and Section 7) and operational logs in `screening/`.

- Screening reliability *
  - Two independent reviewers; calibration screening prior to full pass; agreement monitored and disagreements resolved by consensus or third-party arbitration.

- Screening reconciliation procedure *
  - Consensus discussion first; unresolved cases escalated to third reviewer/supervisor.

- Sampling and sample size *
  - No sampling planned; all records passing eligibility are retained.

- Screening procedure justification *
  - Conservative screening rule minimizes false exclusions and supports PRISMA-traceable reproducibility.

- Data management and sharing *
  - Screening decisions and exclusions logged in structured CSV files under `screening/`, version-controlled and auditable.

- Miscellaneous screening details *
  - Current corpus status in draft methodology: 222 full-text assessed, 2 full-text excluded, 220 included.

### Extraction

- Entities to extract *
  - Study-level metadata, modality/system class, architecture/waveform/channel descriptors, communication outcomes, sensing outcomes, joint trade-off descriptors, and methodological quality indicators.

- Extraction stages *
  - Pilot extraction calibration -> main extraction -> discrepancy resolution -> schema-validated dataset finalization.

- Extractor instructions *
  - Extraction rules and schema logic are defined in `protocol/prisma_proto.md` (Section 8 and Section 9).

- Extractor masking *
  - No formal masking planned; reliability controls are implemented via independent checks and adjudication.

- Extraction reliability *
  - Hybrid double-extraction approach: independent extraction for core fields; secondary verification for deep technical fields; agreement monitored (including kappa-based checks for categorical fields).

- Extraction reconciliation procedure *
  - Consensus with source-provenance verification; unresolved conflicts sent to third reviewer/supervisor.

- Extraction procedure justification *
  - Balances engineering-level detail requirements with feasibility, while preserving reproducibility via schema constraints and provenance fields.

- Data management and sharing *
  - Structured extraction artifacts (CSV/JSON + schema definitions) are version-controlled in repository paths under `data/` and `protocol/`.

- Miscellaneous extraction details *
  - Missingness uses explicit coding (`NR` vs `NA`); figure-digitized values are flagged and verified.

### Synthesis and Quality Assessment

- Planned data transformations *
  - Unit normalization, harmonization of reported metrics, and optional derived variables when computable from reported quantities.

- Missing data *
  - Missing fields coded explicitly (`NR`/`NA`); critical gaps may trigger author contact; otherwise handled transparently in synthesis.

- Data validation *
  - Schema checks, provenance validation, discrepancy resolution, and consistency checks between extracted values and source evidence.

- Quality assessment *
  - Technical Quality Appraisal Framework (TQAF): modeling fidelity, validation rigor, experimental validity, metric completeness, reproducibility/reporting completeness (ordinal 0-2 scale per dimension).

- Synthesis plan *
  - Qualitative structured narrative plus quantitative descriptive trade-off analysis; no pooled inferential meta-analysis due heterogeneity.

- Criteria for conclusions / inference criteria *
  - Conclusions prioritize consistency across studies, methodological quality, and directness to RQs over single-study peak performance claims.

- Synthesist blinding *
  - No formal synthesist blinding planned.

- Synthesis reliability *
  - Lead synthesis with co-author/reviewer checks and explicit reconciliation for contested interpretation.

- Synthesis reconciliation procedure *
  - Discussion-based consensus; unresolved interpretation differences arbitrated by supervisor/third reviewer.

- Publication bias analyses *
  - Engineering-oriented meta-bias checks: venue concentration, selective metric reporting asymmetry, optimistic assumption prevalence, and multi-version/report bias.

- Sensitivity analyses / robustness checks *
  - Sensitivity-style narrative checks based on TQAF strata and scenario robustness patterns.

- Synthesis procedure justification *
  - Heterogeneous outcome definitions and scenario conditions make pooled effect-size models inappropriate; descriptive and taxonomy-driven synthesis is methodologically better aligned.

- Synthesis data management and sharing *
  - Synthesis scripts/notes/outputs will be archived in repository artifacts and linked via OSF project files.

- Miscellaneous synthesis details *
  - Domain-level confidence ratings (High/Moderate/Low) are assigned using evidence quantity, quality, consistency, and theory-practice agreement criteria.

---

## 4) Mandatory TO_FILL Items Before Final Submit

Fill these before clicking submit in OSF:

1. `TO_FILL_START_DATE_YYYY-MM-DD`
2. `TO_FILL_END_DATE_YYYY-MM-DD`
3. `TO_FILL_FUNDING_STATEMENT`
4. `TO_FILL_CONFLICTS_STATEMENT`
5. Final author list and roles in OSF metadata
6. Embargo decision:
   - `Public now`, or
   - `Embargo until TO_FILL_DATE` (max 4 years)

---

## 5) Post-Registration Repo Updates (Once OSF ID/DOI Exists)

After OSF approves and provides registration URL/DOI, update:

- `protocol/prisma_proto.md` (Section 1.2 Registration)
- `drafts/section_03_methodology.md` (Section A)
- `protocol/prisma_2020_chk.md` (Item 24a note)

Use this text:

### A) `protocol/prisma_proto.md` Section 1.2

`This protocol is registered on the Open Science Framework (OSF): TO_FILL_OSF_REG_URL (Registration DOI: TO_FILL_OSF_DOI; registered on TO_FILL_DATE).`

### B) `drafts/section_03_methodology.md` Section A

`This systematic survey follows PRISMA 2020 and PRISMA-S methodology. The protocol was finalized prior to literature search and registered on OSF (TO_FILL_OSF_REG_URL; DOI: TO_FILL_OSF_DOI). Any post-registration amendments are documented in the protocol amendment log.`

### C) `protocol/prisma_2020_chk.md` Item 24a

Replace:
- `UPDATE NEEDED (Add OSF ID)`

With:
- `Compliant - OSF registration recorded: TO_FILL_OSF_REG_URL (DOI: TO_FILL_OSF_DOI).`

---

## 6) If Registration Cannot Be Submitted Now (Fallback Statement)

If OSF submission is delayed, keep PRISMA transparency with a clear temporary statement:

`Protocol registration is planned on OSF but not yet completed as of TO_FILL_DATE; registration identifier and DOI will be reported immediately after approval.`

This fallback should be replaced as soon as registration is live.
