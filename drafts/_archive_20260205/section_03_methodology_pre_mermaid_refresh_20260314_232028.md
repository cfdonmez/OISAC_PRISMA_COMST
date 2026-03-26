# III. SURVEY METHODOLOGY (PRISMA 2020)

## A. Protocol and Registration
This systematic survey adheres to the **Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020** statement [14] and the PRISMA-S extension for literature search reporting [15]. To ensure transparency and minimize reporting bias, the study protocol—including research questions, search strategy, and eligibility criteria—was registered with the **Open Science Framework (OSF)** on **February 12, 2026** (Registration ID: `7f6wb`). The protocol and associated metadata are accessible via the OSF Registries at https://osf.io/7f6wb.

## B. Information Sources and Search Strategy
A comprehensive literature search for the formal PRISMA identification stage was conducted across three engineering and physics databases: **IEEE Xplore**, **Scopus**, and **Web of Science**, all last searched on **November 30, 2025**. Supplementary search templates were retained for **arXiv** and **TechRxiv** to support preprint monitoring and version tracing, but these supplementary sources did not contribute separate records to the canonical PRISMA flow reported in this review (`other_sources_results = 0`).

The search strategy employed two mandatory concept blocks and one optional refinement block:
1.  **Integrated Sensing and Communication Concepts:** Terms such as "integrated sensing and communication", ISAC, "joint sensing and communication", and related variants.
2.  **Optical Medium Terms:** Terms restricting retrieval to optical carriers and platforms, such as optical/photonic, fiber/fibre, FSO, VLC, LiFi, and LiDAR.
3.  **Physical-Layer Refinement (Optional):** Additional terms such as waveform, modulation, signal model, channel model, or optical front-end, used only when a database required extra disambiguation.

The exact executed search strings and run-level search logs were preserved in the study records for auditability and methodological traceability. The literature search was frozen as of **November 30, 2025**.

## C. Eligibility Criteria
To ensure the survey's coherence and focus on the *optical* domain, strict inclusion and exclusion criteria were applied (Table III-1).

**Inclusion Criteria:**
*   **Domain:** Systems utilizing optical carrier frequencies (infrared, visible, or ultraviolet) for *both* sensing and communication.
*   **Integration:** Studies proposing shared hardware, spectrum, or waveforms (True O-ISAC) or coordinated coexistence.
*   **Content and Time Frame:** Peer-reviewed journal articles and full-length conference papers providing technical depth on physical/link-layer architecture, performance limits, or experimental validation, primarily focused on the **2020–2025** period.

**Exclusion Criteria:**
*   **RF-Only:** ISAC systems operating solely in radio frequency/microwave/THz bands without an optical component.
*   **Disjoint Functionality:** Pure sensing (e.g., standard LiDAR) or pure communication (e.g., standard FSO) papers without integration mechanisms.
*   **Type:** Short abstracts, non-English publications, and grey literature (theses, white papers) lacking peer review.

### Table III-1: Eligibility Criteria Applied for Study Selection

| Criterion | Inclusion Requirements | Exclusion Conditions |
| :--- | :--- | :--- |
| **Domain Scope** | Systems utilizing **optical carrier frequencies** (IR, Visible, UV) for joint sensing and communication functionalities. | **RF-only ISAC** systems (sub-6 GHz, mmWave, THz) lacking an optical component; Biomedical or chemical sensing without data transmission. |
| **Integration Level** | **True O-ISAC** (shared hardware/waveform) or **Coexistence** (resource sharing) strategies operating at Physical or Link Layer. | **Disjoint systems:** Pure optical sensing (e.g., standard LiDAR) or pure optical communications (e.g., FSO link) without explicit integration mechanisms. |
| **Publication & Time** | Peer-reviewed **journal articles** and **full-length conference papers** published in English, primarily within the **2020–2025** core window. | Short abstracts, non-English publications, and **grey literature** (theses, white papers, patents, technical reports). |
| **Technical Content** | Studies reporting at least one **Sensing metric** (e.g., Detection Probability, CRB, RMSE) AND one **Communication metric** (e.g., BER, SINR, Data Rate). | Studies lacking technical depth on the integration mechanism, trade-offs, or performance evaluation (e.g., high-level vision papers without analysis). |


## D. Study Selection and PRISMA Flow
Study selection followed a three-step PRISMA workflow:
1.  **Deduplication:** Automatic removal of duplicate records across databases.
2.  **Screening:** Title and abstract screening to remove clearly irrelevant (e.g., RF-only or biomedical sensing) records.
3.  **Eligibility:** Full-text review of candidate papers against the inclusion criteria.

Following the registered protocol, two reviewers first calibrated the eligibility criteria on a pilot sample of 50 records, then independently conducted title/abstract screening and full-text eligibility assessment. Any record marked as *Include* or *Unsure* by at least one reviewer advanced to full-text review. Disagreements were resolved by consensus discussion and, where needed, third-reviewer arbitration, with adjudications archived in the structured screening logs.

The canonical aggregate PRISMA counts were maintained in a structured screening ledger and reconciled against stage-specific audit records. Earlier-stage artefacts covered deduplication and title/abstract screening, while later-stage artefacts directly backed the full-text assessment, exclusion, and final inclusion ledgers. In the reconciled record, **222** full-text articles were assessed, **2** were excluded at the full-text stage, and the final included corpus comprised **N = 220** studies. The attrition process is summarised in Fig. III-1.

```mermaid
graph TD
    A[<b>Identification</b><br>Records identified from databases<br>(n = 980)<br><i>IEEE Xplore, Scopus, WoS</i>] --> B[Duplicated records removed<br>(n = 280)]
    B --> C[<b>Screening</b><br>Records screened via Title/Abstract<br>(n = 700)]
    C --> D[Records excluded<br>(n = 478)<br><i>Irrelevant topic, RF-only, etc.</i>]
    C --> E[<b>Eligibility</b><br>Full-text articles assessed<br>(n = 222)]
    E --> F[Full-text articles excluded<br>(n = 2)<br><i>Reasons: non-O-ISAC / unverifiable full-text record</i>]
    E --> G[<b>Included</b><br>Studies included in review<br>(n = 220)]
    style G fill:#bef67a,stroke:#33691e,stroke-width:2px
```
*Fig. III-1. PRISMA 2020 flow diagram describing the systematic literature search and selection process.*


## E. Data Extraction and Taxonomical Classification
Data extraction was performed using a standardized structured schema to rigorously map the O-ISAC landscape. Key extracted variables include modality coverage (categorizing fiber, FSO, VLC/LiFi, or hybrid regimes), integration depth (distinguishing true waveform/hardware sharing from resource coexistence), quantitative performance metrics (capturing sensing resolution and range alongside communication data rate and BER), and validation level (coding empirical evidence as simulation, experiment, prototype, or analytical). This structured extraction directly feeds the quantitative trade-off frontiers evaluated in Section V.

## F. Quality Appraisal (TQAF)
To assess the reliability of the surveyed literature, we developed a custom **Technical Quality Assessment Form (TQAF)**. Each included study was evaluated independently by two reviewers across five formal dimensions:
1.  **Modelling Fidelity:** Realism of channel and noise models, and their suitability for physical/link-layer evaluation.
2.  **Experimental Validity:** Presence of hardware proof-of-concept versus pure analytical simulation.
3.  **Metric Completeness:** Reporting of joint sensing and communication metrics versus cherry-picked single-function reporting.
4.  **Reproducibility:** Explicitness of parameter assumptions and availability of code or datasets.
5.  **Clarity:** Clear definition of assumptions and physical limitations.

Each dimension was scored on a 0–2 scale (low/moderate/high quality). Any scoring disagreements were resolved by consensus discussion or third-party arbitration. While TQAF scores did not determine study exclusion, they are used throughout Sections IV, VI, and VIII to formally weight the strength of evidence, highlighting methodological gaps where high-impact claims lack rigorous validation.

## G. Data Synthesis Strategy
Given the heterogeneity of metrics across fiber, FSO, and VLC domains—combined with varying assumptions in channel modeling and hardware bounds—a formal statistical meta-analysis was not feasible. Instead, we employ a structured qualitative and quantitative descriptive synthesis driven by the taxonomic model. The literature is first organized by physical modality (Section IV) to reveal domain-specific integration techniques. Following this taxonomic mapping, we conduct a quantitative trade-off analysis (Section V) using visual synthesis tools, such as rate-resolution scatter plots, to identify empirical Pareto frontiers within the joint sensing and communication performance space.
