# IV. UNIFIED O-ISAC TAXONOMY

Section IV converts the physical-layer contracts of Section II and the systematic evidence base of Section III into a single taxonomy for cross-modality synthesis. The purpose is not to rank modalities, but to define a consistent classification frame that keeps communication-sensing comparisons traceable across fiber, FSO, VLC/LiFi, photonic-THz, and hybrid systems.

## A. Taxonomy Design Principles
### A.1 Design Requirements
Section IV builds a unified O-ISAC taxonomy for cross-modality synthesis, not modality ranking. This distinction is operational rather than rhetorical: the objective is to preserve valid comparisons across heterogeneous implementations by conditioning each comparison on explicit classification variables. Therefore, Section IV-A defines the contract that downstream sections must satisfy before reporting trends, tradeoffs, or representative operating points.

The design starts from a corpus of N=220 studies, which is sufficiently broad to expose repeated structural patterns and sufficiently diverse to reveal incompatibilities in reporting conventions. However, corpus size alone does not guarantee comparability. A taxonomy is useful only if it supports reproducible assignment decisions and traceable evidence paths from each paper to each synthesized statement. Consequently, the design is anchored in three requirements. First, cross-modality comparability: studies must be grouped using axes that separate substrate, integration architecture, observability conditions, and sensing objective. Second, evidence traceability: each axis label must be recoverable from document-level descriptors and retained even when reports are incomplete or partially contradictory. Third, metric-governance consistency with Section II: synthesis is admissible only if measurement plane and metric role remain explicitly governed.

These requirements are motivated by representative cross-modality evidence where integration and sensing objectives are shared but physical assumptions differ materially [O_ISAC_006], [O_ISAC_021], [O_ISAC_068], [O_ISAC_016]. The practical implication is that Section IV does not ask which modality is best in absolute terms. Instead, it asks whether two results are comparable under the same taxonomy state and governance contract. If the answer is no, the comparison is withheld or conservatively qualified.

### A.2 Axis Definitions
To enforce deterministic synthesis, each study \(p\) is mapped to
\[
T(p) = (m(p), i(p), d(p), s(p)).
\]
Here, \(m(p)\) denotes medium class, \(i(p)\) denotes integration class, \(d(p)\) denotes detection/observability class, and \(s(p)\) denotes sensing-task class. Therefore, each axis isolates one comparability condition, and joint interpretation requires all four axes simultaneously.

Axis 1 (Medium) captures propagation and deployment substrate. The dominant classes in the N=220 corpus are hybrid 116/220 (52.7%), fiber 45/220 (20.5%), VLC/LiFi 25/220 (11.4%), and FSO 19/220 (8.6%). These shares support a synthesis-first reading: hybrid systems are common enough to be central to transferability analysis, while fiber, VLC/LiFi, and FSO provide modality-specific anchors for controlled contrasts. However, medium share is not interpreted as superiority; it is interpreted as evidence concentration for conditioned comparison.

Axis 2 (Integration) captures whether sensing and communication rely on shared front-end resources or separate front-ends. Shared front-end designs account for 194/220 (88.2%), while separate front-ends account for 26/220 (11.8%). This skew indicates that most evidence evaluates coupled architectures, so claims about decoupled coexistence should be treated as a minority profile rather than as a default assumption.

Axis 3 (Detection/plane) captures dominant receiver observability through direct and coherent regimes. The corpus contains direct 118/220 and coherent 97/220. Consequently, synthesis across these groups must preserve plane semantics and estimator assumptions instead of collapsing both into one generic detection label.

Axis 4 (Task class) captures sensing objectives. Ranging is the primary task in 162/220 (73.6%), with additional classes including localization, vibration, and detection. Therefore, comparisons should be task-conditioned first and only then interpreted across medium and integration classes.

This axis design follows evidence-grounded cross-modality practice and remains compatible with downstream mapping and governance checks [O_ISAC_021], [O_ISAC_039], [O_ISAC_077].

### A.3 Mapping Rules
Deterministic mapping is required because many O-ISAC papers report multi-stage systems, multi-task outcomes, or partially implicit measurement assumptions. The mapping pipeline follows six fixed principles: structured descriptors first; textual fallback if missing; multi-task keeps all labels with one primary only for tabulation; hybrids remain hybrid; normalize labels before aggregation; contradictions retained and flagged. Therefore, assignment is reproducible while preserving uncertainty rather than hiding it.

Measurement-plane governance follows the Section II contract:
\[
\pi(m) \in \{\text{OPTICAL\_PLANE}, \text{ELECTRICAL\_PLANE}, \text{AMBIGUOUS}\}.
\]
No implicit OSNR-to-SNR substitution is allowed without an explicit receiver/noise model. This rule is falsifiable at extraction time because any substitution must be accompanied by a stated model, otherwise the record is tagged as governed ambiguity.

Metric governance is equally strict. Resolution and accuracy are distinct roles and must remain separate in synthesis statements. In particular, \(\Delta r_{\min}\) and \(\sigma_r\) are not aliases and cannot be pooled as interchangeable evidence. Consequently, aggregate claims are built from role-consistent subsets only, and mixed-role reporting is retained with reduced interpretive weight.

Table IV-A summarizes the operational contract that binds axis assignment, deterministic mapping, and comparability protection.

| Element | Role in taxonomy | Operational rule | Comparability guard |
|:--|:--|:--|:--|
| Design requirements | Defines admissible synthesis scope | Enforce cross-modality comparability, evidence traceability, and Section II metric-governance consistency | Reject unconditioned cross-modality claims |
| Axis 1 (Medium) | Encodes propagation/deployment substrate | Map each study to one medium label, preserving hybrid when present | Compare results only within medium-conditioned subsets |
| Axis 2 (Integration) | Encodes coupling architecture | Assign shared front-end or separate front-ends from explicit implementation evidence | Do not merge co-designed and coexistence regimes |
| Axis 3 (Detection/plane) | Encodes observability regime | Assign direct or coherent with plane-aware interpretation | Block plane conflation across observability regimes |
| Axis 4 (Task class) | Encodes sensing objective | Keep all task labels; use one primary only for tabulation | Avoid cross-task pooling without task conditioning |
| Mapping pipeline | Guarantees reproducible assignment | Apply structured descriptors first, then textual fallback; normalize labels before aggregation | Preserve deterministic labels across reruns |
| Measurement-plane governance | Protects signal-domain validity | Enforce \(\pi(m)\) set membership; require explicit receiver/noise model for OSNR-SNR linkage | No implicit OSNR-to-SNR substitution |
| Metric governance | Protects metric-role validity | Keep resolution and accuracy separate; treat \(\Delta r_{\min}\) and \(\sigma_r\) as non-alias quantities | Prevent metric aliasing in pooled statistics |
| Ambiguity handling | Preserves uncertainty information | Retain contradictions and mark ambiguity at record level | Down-weight ambiguous evidence in conclusions |

A conservative limitation remains necessary. The taxonomy retains and conservatively interprets 84 ambiguity cases, comprising 75 metric-aliasing cases and 9 measurement-plane ambiguity cases. However, these cases are retained by design because exclusion would inflate apparent certainty and reduce auditability. The resulting synthesis is intentionally conservative: it prioritizes traceable comparability over maximal but potentially invalid aggregation [O_ISAC_021], [O_ISAC_039], [O_ISAC_077].

**Lesson (A):** Unified O-ISAC taxonomy is defensible only when four-axis classification, deterministic mapping, and measurement-metric governance are enforced jointly under explicit ambiguity retention.

---

## B. Medium-Based Classes
Section IV-B instantiates Axis 1 by grouping studies according to normalized medium labels and then conditioning mechanism, detection, and task interpretations on that grouping. The objective is cross-modality synthesis with explicit comparability guards, not medium ranking. At the corpus level (N=220), five classes define the main synthesis frame: hybrid 116/220 (52.7%), cabled fiber 45/220 (20.5%), VLC/LiFi 25/220 (11.4%), FSO 19/220 (8.6%), and terahertz 1/220 (0.5%). These five classes cover 206/220 studies (93.6%), while the remaining 14/220 records form a long tail that includes generic wireless, retroreflective wireless, RF-assisted wireless, UV wireless, retroreflective optical, and other low-support labels.

Cross-axis coupling is strong but not uniform. Shared front-end integration is dominant in every main class, yet detection profiles diverge by medium: cabled fiber is coherent-heavy, VLC/LiFi is strongly direct-detection dominant, FSO is mixed with a direct-leading balance, terahertz appears as a single direct-detection record, and hybrid remains near-balanced between coherent and direct with a small residual of other labels. Consequently, medium-based discussion is necessary to prevent false pooling across observability regimes.

Task emphasis is likewise medium-conditioned. Ranging is the primary task in all five main classes, but the secondary pattern differs: vibration and fault monitoring are visible in cabled fiber, localization tails are stronger in VLC/LiFi and hybrid, and FSO remains tightly ranging-centered. This corpus-level composition is consolidated in Fig. IV-1 and then unpacked through the class-specific discussion below. Therefore, each class discussion preserves Section II metric governance: plane-aware interpretation is enforced, no implicit OSNR-to-SNR substitution is made without explicit receiver/noise modeling, and resolution versus accuracy terms are not treated as aliases.

**Table IV-B summarizes medium-based taxonomy classes, corpus share, and dominant operational profiles.**

| Medium class | Corpus share | Dominant integration profile | Dominant detection profile | Dominant sensing emphasis | Representative studies |
|:--|:--|:--|:--|:--|:--|
| Fiber (cabled) | 45/220 (20.5%) | Shared front-end (43/45) | Coherent-leading (27 coherent, 18 direct) | Ranging primary (27), then vibration (8) and 2D localization (6) | [O_ISAC_006], [O_ISAC_033], [O_ISAC_046], [O_ISAC_041], [O_ISAC_090] |
| FSO | 19/220 (8.6%) | Shared front-end (14/19) | Direct/coherent mixed with direct lead (11/8) | Ranging primary (18), 2D localization tail (1) | [O_ISAC_021], [O_ISAC_035], [O_ISAC_005], [O_ISAC_023], [O_ISAC_199] |
| VLC/LiFi | 25/220 (11.4%) | Shared front-end dominant (18/25) | Direct-detection dominant (24/25) | Ranging (12) and localization-heavy tail (10 2D localization, 3 localization) | [O_ISAC_068], [O_ISAC_303], [O_ISAC_039], [O_ISAC_327], [O_ISAC_062], [O_ISAC_009] |
| Photonic-THz / terahertz proxy | 1/220 (0.5%) explicit terahertz class | Shared front-end (1/1) | Direct (1/1) | Ranging (1/1) | [O_ISAC_016], [O_ISAC_077], [O_ISAC_105], [O_ISAC_070], [O_ISAC_029] |
| Hybrid systems | 116/220 (52.7%) | Shared front-end dominant (106/116) | Near-balanced coherent/direct (59/53) with residual labels (4) | Ranging primary (95), 2D localization tail (12), broader multi-task remainder | [O_ISAC_021], [O_ISAC_077], [O_ISAC_041], [O_ISAC_199], [O_ISAC_010] |
| Long-tail media (outside main five) | 14/220 (6.4%) | Mixed, mostly shared front-end | Mostly direct-detection | Heterogeneous low-support tasks | [O_ISAC_039], [O_ISAC_070], [O_ISAC_090] |

### B.1 Fiber (Cabled) O-ISAC
Design rationale: the cabled-fibre class is the guided-medium anchor for O-ISAC because the propagation environment and infrastructure coupling are sufficiently controlled to expose integration and observability effects without free-space geometry uncertainty.

Evidence-conditioned synthesis from the N=220 corpus shows 45 cabled fiber records (20.5%). Integration is predominantly shared front-end (43/45), indicating that most fibre studies evaluate tight sensing-communication coupling rather than loose coexistence. Detection is coherent-leading (27 coherent versus 18 direct), which is consistent with the role of phase-sensitive observability in many fibre sensing pipelines. Primary task distribution is ranging-led (27), followed by vibration (8) and 2D localization (6), with a small remainder in temperature, fault localization, and non-task-labeled records. Consequently, fibre results in Section IV should be interpreted as communication-sensing co-design under guided-channel assumptions, not as a direct baseline for wireless classes [O_ISAC_006], [O_ISAC_033], [O_ISAC_046], [O_ISAC_041], [O_ISAC_090].

Comparability guard: fibre class comparisons remain valid only when measurement-plane semantics are explicit and metric roles are preserved. Therefore, resolution-type quantities and accuracy-type quantities are kept separate, and optical-plane indicators are not converted into electrical-plane SNR claims without explicit receiver/noise models.

### B.2 Free-Space Optical (FSO) O-ISAC
Design rationale: the FSO class isolates optical wireless links where atmospheric and alignment conditions materially affect both communication reliability and sensing confidence, so medium-specific conditioning is mandatory.

Evidence-conditioned synthesis identifies 19 FSO records (8.6%). Integration remains mostly shared front-end (14/19), but separate-front-end coexistence is non-negligible (5/19), so both tightly coupled and partially decoupled implementations appear in this class. Detection is mixed with a direct lead (11 direct, 8 coherent), unlike the stronger coherent bias in cabled fibre. Task concentration is narrow: 18 records are primarily ranging and one record is primarily 2D localization. In contrast to VLC/LiFi, where localization tails are larger, FSO evidence remains predominantly range-oriented. Therefore, cross-class statements involving FSO should be framed as ranging-dominant and observability-mixed, rather than extrapolated from one detection regime [O_ISAC_021], [O_ISAC_035], [O_ISAC_005], [O_ISAC_023], [O_ISAC_199].

Comparability guard: FSO synthesis must preserve explicit detection class and measurement-plane interpretation. Consequently, direct and coherent FSO outcomes are not merged into a single performance statistic when metric definitions differ, and accuracy claims are not inferred from resolution values.

### B.3 Visible Light / LiFi O-ISAC
Design rationale: the VLC/LiFi class captures intensity-domain indoor optical systems where communication, illumination, and sensing objectives are jointly constrained by the same optical front-end and deployment geometry.

Evidence-conditioned synthesis yields 25 VLC/LiFi records (11.3%). Integration is mostly shared front-end (18/25), while separate-front-end designs remain visible (7/25). Detection is highly concentrated in direct mode (24/25), with only one coherent-labeled record. Task emphasis is split between ranging (12) and localization-heavy tails (10 2D localization and 3 localization), which makes VLC/LiFi the strongest localization-oriented class among the main wireless media. However, this localization emphasis coexists with direct-detection observability assumptions; therefore, comparisons against coherent-leading classes require explicit conditioning on receiver model and metric role [O_ISAC_068], [O_ISAC_303], [O_ISAC_039], [O_ISAC_327], [O_ISAC_062], [O_ISAC_009].

Comparability guard: VLC/LiFi evidence is interpreted under intensity-domain measurement semantics, and pooled results preserve Section II separation between resolution and accuracy. In contrast to narrative summaries that interchange these terms, this section treats them as non-alias quantities.

### B.4 Photonic-THz / Optical-THz Bridging
Design rationale: photonic-THz analysis must be framed as a bridge between optical distribution and high-frequency wireless operation, so an explicit single-medium class alone cannot represent the full evidence footprint.

Evidence-conditioned synthesis from the normalized table shows one explicit terahertz record (1/220, 0.5%), labeled as a shared front-end, direct-detection, ranging-primary system. However, anchor-level evidence indicates broader photonic-THz relevance beyond this explicit class: among 39 papers with direct photonic-THz anchors, 31 are mapped to hybrid medium labels, while only one is mapped to explicit terahertz. Therefore, terahertz is used in Section IV-B as an explicit proxy class, while the system-level bridge behavior is interpreted jointly with Section B.5 hybrid evidence [O_ISAC_016], [O_ISAC_077], [O_ISAC_105], [O_ISAC_070], [O_ISAC_029].

Comparability guard: photonic-THz reporting is stage-aware by construction. Consequently, optical-plane and electrical-plane claims are not conflated, and no implicit OSNR-to-SNR substitution is admitted without an explicit cross-plane receiver/noise model.

### B.5 Hybrid Systems
Design rationale: hybrid systems are the structural core of O-ISAC synthesis because they expose cross-medium transferability and integration tradeoffs in one model, rather than isolating single-substrate behavior.

Evidence-conditioned synthesis confirms that hybrid is the majority class with 116/220 records (52.7%). Integration is strongly shared-front-end (106/116), signaling that most hybrid studies pursue deep functional coupling. Detection is near-balanced between coherent and direct (59 and 53), with a four-record residual in envelope detection, unknown, and other labels; this residual is small but analytically important because it signals edge-case observability classes that should not be silently merged. Task profile is ranging-dominant (95), followed by 2D localization (12) and a low-volume multi-task tail (including localization, motion detection, vibration, target detection, and volcanic-ash detection). Consequently, hybrid evidence supports broad transferability analysis, but only when mechanism and detection conditioning remain explicit [O_ISAC_021], [O_ISAC_077], [O_ISAC_041], [O_ISAC_199], [O_ISAC_010].

Comparability guard: hybrid conclusions are valid only under full axis conditioning and Section II governance. Therefore, cross-link reports that mix measurement planes or blur resolution and accuracy are retained as constrained evidence rather than pooled as homogeneous performance, consistent with the contract-violation audit used in Section IV.

**Lesson (B):** Medium class determines dominant physical constraints, but comparability is recovered only when all classes are interpreted under a common metric-governance contract.

---

## C. Integration Mechanisms
This subsection instantiates Axis 2 using the normalized mechanism labels of shared front-end and separate front-ends. At corpus scale (N=220), the mechanism split is strongly asymmetric, with shared front-end architectures in 194/220 studies (88.2%) and separate front-end architectures in 26/220 studies (11.8%). However, the asymmetry is not uniform across media. The medium-conditioned taxonomy tree shows shared front-end dominance in hybrid (106/116, 91.4%) and cabled fiber (43/45, 95.6%), while VLC/LiFi (18/25, 72.0%) and FSO (14/19, 73.7%) retain larger separate front-end fractions. Therefore, integration conclusions must be conditioned on medium and cannot be inferred from global counts alone.

Section IV-C further resolves this axis into four recurrent coupling modes extracted from the Section IV-C evidence table: shared waveform, shared hardware, shared resources, and shared processing. Evidence intensity is reported as unique-paper support under combined direct+indirect anchors, with direct-only counts as a stricter secondary support level. Consequently, the mechanism narrative below is both structural (axis assignment) and evidential (anchor intensity), while remaining compatible with mapping rules that prioritize structured fields, apply label normalization, and retain contradictory anchors for auditability.

**Table IV-C summarizes integration mechanisms, evidence intensity, and dominant trade-off implications.**

| Mechanism Class | Evidence Intensity (Unique Papers, Direct+Indirect) | Typical Coupling Layer | Dominant Benefit | Primary Risk | Representative Studies |
|:--|:--|:--|:--|:--|:--|
| Shared Waveform | 34 (direct+indirect); direct-only: 13 | Signal and waveform design chain | Joint reuse of modulation degrees of freedom under tight synchronization | Strong objective coupling can amplify tradeoffs between rate, robustness, and estimator stability | [O_ISAC_035], [O_ISAC_190], [O_ISAC_304], [O_ISAC_016] |
| Shared Hardware | 15 (direct+indirect); direct-only: 5 | Optical/electrical front-end components and transceiver chain | Reduced platform duplication and tighter timing alignment | Hardware impairment coupling reduces decoupling flexibility and calibration margin | [O_ISAC_021], [O_ISAC_164], [O_ISAC_324], [O_ISAC_056], [O_ISAC_161] |
| Shared Resources | 43 (direct+indirect); direct-only: 16 | Time/frequency/power scheduling and allocation plane | Flexible balancing of sensing and communication utility under deployment constraints | Resource contention can degrade both links if sensing and traffic loads are co-peaked | [O_ISAC_061], [O_ISAC_114], [O_ISAC_142], [O_ISAC_141], [O_ISAC_021] |
| Shared Processing | 30 (direct+indirect); direct-only: 8 | Joint estimation/decoding and algorithmic inference stack | Cross-task feature reuse and improved end-to-end decision coherence | Model mismatch and task interference can bias both communication and sensing outputs | [O_ISAC_086], [O_ISAC_166], [O_ISAC_134], [O_ISAC_381], [O_ISAC_161] |

### C.1 Shared Waveform
Design rationale: shared-waveform integration uses one coordinated signal structure to support communication payload transfer and sensing observability, so coupling is introduced at the earliest stage of system design rather than after front-end partitioning.

Evidence-conditioned synthesis shows 34 unique papers with combined direct+indirect support for shared waveform (15.5% of N=220), including 13 unique papers with direct-only support. This intensity places shared waveform below shared resources but above shared hardware, indicating that waveform-level co-design is a substantial, yet not universal, strategy in the current corpus. In medium terms, the high prevalence of shared front-end architectures in hybrid and cabled-fiber classes provides a structural context in which waveform reuse is operationally feasible; however, the larger separate front-end shares in VLC/LiFi and FSO indicate that waveform unification is not a necessary condition for integration. Consequently, shared-waveform designs should be interpreted as high-coupling operating points that can improve joint efficiency while tightening cross-objective constraints [O_ISAC_035], [O_ISAC_190], [O_ISAC_304], [O_ISAC_016].

Comparability and governance guard: waveform-level results are compared only when receiver/noise assumptions are explicit; therefore, no implicit OSNR-to-SNR substitution is accepted, and resolution-type and accuracy-type outcomes remain non-alias metrics under Section II rules.

### C.2 Shared Hardware
Design rationale: shared-hardware integration couples sensing and communication through common transceiver or front-end components, aiming to reduce duplication while preserving deterministic synchronization across both functions.

Evidence intensity for shared hardware is 15 unique papers under combined direct+indirect support (6.8% of N=220), with 5 unique papers under direct-only support. In contrast to shared waveform and shared resources, this is the lowest concept-level support among the four mechanism classes. Therefore, explicit hardware-sharing claims appear as a selective strategy rather than a dominant one, even though the axis-level shared front-end label is common in the corpus. This gap is expected: axis assignment captures integration structure at paper level, whereas concept anchors isolate explicit mechanism articulation. Consequently, shared-hardware interpretation should emphasize implementation pragmatics, including impairment co-propagation and calibration discipline, rather than assume broad generality across all shared front-end records [O_ISAC_021], [O_ISAC_164], [O_ISAC_324], [O_ISAC_056], [O_ISAC_161].

Comparability and governance guard: hardware-sharing claims are admissible for cross-study synthesis only when measurement plane and metric role are explicitly separated; in particular, optical-plane quantities are not merged with electrical-plane SNR statements without a stated conversion model, and accuracy is not inferred from reported resolution alone.

### C.3 Shared Resources
Design rationale: shared-resources integration coordinates time, frequency, and power allocation between sensing and communication without requiring full waveform or hardware unification, which makes it a practical mechanism under heterogeneous deployment constraints.

Shared resources has the highest concept-level evidence intensity, with 43 unique papers under combined direct+indirect support (19.5% of N=220) and 16 unique papers under direct-only support. This high support is consistent with the non-negligible separate front-end fractions in VLC/LiFi (7/25) and FSO (5/19), where resource coupling often provides integration without complete physical co-design. However, the same mechanism is also present in shared front-end-dominant classes, indicating that resource coupling is complementary rather than mutually exclusive with tighter integration modes. Therefore, resource sharing should be interpreted as a control-plane mechanism that spans both co-designed and coexistence architectures, with performance governed by contention patterns and scheduling policy quality [O_ISAC_061], [O_ISAC_114], [O_ISAC_142], [O_ISAC_141], [O_ISAC_021].

Comparability and governance guard: resource-level tradeoff claims are retained only when sensing and communication metrics are role-consistent; consequently, statements that blur resolution with accuracy or mix optical-plane and electrical-plane indicators without model disclosure are treated as constrained evidence, not pooled facts.

### C.4 Shared Processing
Design rationale: shared-processing integration couples communication decoding and sensing inference at the algorithmic level to exploit cross-task information and improve decision consistency at system output.

Evidence intensity for shared processing reaches 30 unique papers under combined direct+indirect support (13.6% of N=220), with 8 unique papers under direct-only support. In contrast to shared resources, this mechanism is less frequently explicit, but it remains materially represented across the corpus and is especially relevant in hybrid-dominant settings where multi-stage pipelines benefit from joint inference. Therefore, shared processing should be interpreted as an algorithmic integration layer that can absorb heterogeneity across links, provided that model assumptions remain transparent and task interference is controlled. Consequently, gains attributed to shared-processing pipelines should be evaluated alongside robustness to mismatch and not solely by best-case communication or sensing endpoints [O_ISAC_086], [O_ISAC_166], [O_ISAC_134], [O_ISAC_381], [O_ISAC_161].

Comparability and governance guard: processing-level synthesis remains valid only under explicit plane labeling and metric separation, so no implicit OSNR-to-SNR substitution is permitted and no resolution/accuracy aliasing is accepted in aggregated conclusions.

**Lesson (C):** Integration mechanisms should be interpreted as evidence-weighted coupling layers over the shared front-end/separate front-end axis, where stronger coordination improves joint efficiency only when governance constraints preserve metric and measurement-plane comparability.

---

## D. Signal Dimension and Detection
This subsection instantiates Axis 3 and formalizes how detection model and signal observability constrain valid cross-study comparison. In the N=220 corpus, detection labels are concentrated in direct 118/220 and coherent 97/220, with five residual records distributed across unknown (2), other (1), envelope detection (1), and MIMO (1). Therefore, most synthesis statements can be anchored in direct/coherent regimes, but residual classes must remain explicit rather than silently absorbed. Structured receiver typing further supports auditability: the structured receiver-detection annotation is populated in 218/220 records, which enables deterministic detection mapping for nearly the full corpus. This high structured-field coverage is operationally important because mapping rules prioritize structured descriptors and invoke textual fallback only when structured fields are missing; consequently, only a small minority of records requires fallback handling for Axis 3 assignment. However, frequency of occurrence is not interpreted as modality superiority; it only indicates evidence concentration under the current extraction contract.

**Table IV-D summarizes detection and observability classes, evidence intensity, and governance implications.**

| Detection / observability class | Evidence intensity | Corpus-level anchor | Governance implication | Representative references |
|:--|:--|:--|:--|:--|
| IM/DD regime | 29 unique papers (direct+indirect); direct-only 23 | Direct-detection-heavy VLC/LiFi plus direct subsets in FSO and fiber | Interpret under intensity-domain and post-detection electrical-plane semantics; no implicit OSNR-to-SNR transfer | [O_ISAC_001], [O_ISAC_023], [O_ISAC_028], [O_ISAC_029] |
| Coherent detection | 45 unique papers (direct+indirect); direct-only 25 | Fiber and hybrid anchors with coherent-leading subclusters | Preserve receiver/noise-model transparency before cross-regime comparison | [O_ISAC_006], [O_ISAC_021], [O_ISAC_077], [O_ISAC_190] |
| Intensity-only observability | 118 unique papers (direct+indirect); direct-only 58 | Dominant in direct-detection corpora and especially VLC/LiFi | Do not infer phase-sensitive or complex-field behavior from intensity-only evidence | [O_ISAC_021], [O_ISAC_082], [O_ISAC_039], [O_ISAC_056] |
| Complex-field observability | 17 unique papers (direct+indirect); direct-only 4 | Coherent-leading fiber/hybrid subset | Keep field-aware estimator behavior separate from intensity-only aggregation | [O_ISAC_021], [O_ISAC_082], [O_ISAC_056] |
| Residual receiver labels / structured tail | 5 residual corpus labels; structured receiver typing populated in 218/220 studies | Unknown, envelope-detection, MIMO, and other low-support labels | Retain explicit tail labels and do not silently absorb them into direct/coherent bins | [O_ISAC_132], [O_ISAC_061], [O_ISAC_050] |

### D.1 IM/DD vs Coherent Detection
Design rationale: IM/DD and coherent detection are not interchangeable implementation choices because they operate on different observables and induce different estimator and impairment sensitivities. IM/DD pipelines are anchored in intensity-domain observations with non-negativity constraints, whereas coherent pipelines retain field amplitude/phase information and typically require tighter optical front-end control.

Evidence-conditioned synthesis supports this distinction at two levels. At taxonomy level, direct and coherent detections account for 215/220 records (97.7%), which establishes these regimes as the primary basis for Section IV-D interpretation. Medium-conditioned counts sharpen this view: cabled fiber is coherent-leading (27 coherent, 18 direct), VLC/LiFi is strongly direct-heavy (24 direct, 1 coherent), FSO is mixed with direct lead (11 direct, 8 coherent), and hybrid remains near-balanced (59 coherent, 53 direct, plus four residual labels). At concept-evidence level, Table IV-D reports 29 unique papers with combined direct+indirect support for IM/DD (23 direct-only) and 45 unique papers with combined direct+indirect support for coherent detection (25 direct-only). In contrast to paper-by-paper descriptions, these counts indicate that both regimes are materially represented but differently articulated in textual evidence. Consequently, comparisons across these regimes must be framed as model-conditioned contrasts, not as one-dimensional performance rankings [O_ISAC_001], [O_ISAC_023], [O_ISAC_028], [O_ISAC_029], [O_ISAC_190].

Comparability guard: direct/IM-DD and coherent outcomes are comparable only after explicit receiver/noise-model alignment; therefore, no implicit OSNR-to-SNR substitution is admissible when transferring conclusions across detection regimes.

### D.2 Intensity-Only vs Complex-Field Observability
Design rationale: observability class determines which information is directly measurable and, consequently, which estimation structures are physically admissible. Intensity-only observability supports robust low-complexity chains in many settings, whereas complex-field observability can expose phase-dependent structure at the cost of stricter calibration and front-end requirements.

Evidence-conditioned synthesis reveals strong asymmetry in explicit observability reporting. The intensity-only regime has combined direct+indirect support in 118 unique papers (58 direct-only), while the complex-field regime has combined direct+indirect support in 17 unique papers (4 direct-only). In contrast, this asymmetry should be interpreted as reporting concentration under current corpus composition, not as evidence that one observability class is intrinsically superior. The practical implication is that identical task labels such as ranging or localization can encode materially different uncertainty behavior depending on whether phase information is directly observable. Therefore, observability conditioning is mandatory before cross-medium or cross-algorithm aggregation, and cross-task synthesis must preserve the detection-observability pair as a coupled label rather than treating observability as an optional annotation [O_ISAC_021], [O_ISAC_082], [O_ISAC_039], [O_ISAC_056].

Comparability guard: task-level metrics are aggregated only within compatible observability classes; consequently, intensity-only and complex-field records are not merged into a single estimator-performance trend without explicit model harmonization.

### D.3 Metric Reporting Implications
Design rationale: once detection and observability are fixed, metric comparability depends on measurement-plane governance and metric-role separation. Section II remains binding through
\[
\pi(m)\in\{\text{OPTICAL\_PLANE},\;\text{ELECTRICAL\_PLANE},\;\text{AMBIGUOUS}\},
\]
and
\[
\Delta r_{\min}\neq \sigma_r.
\]
The first constraint enforces explicit plane typing and forbids implicit OSNR-to-SNR substitution without an explicit receiver/noise model. The second constraint prevents resolution and accuracy from being treated as aliases during pooled synthesis.

Receiver-side structured typing mitigates, but does not eliminate, governance risk: although structured receiver-detection coverage reaches 218/220, plane ambiguity can still arise when reported SNR-family metrics are not explicitly tagged as optical-plane or electrical-plane quantities in the narrative or tables.

Evidence-conditioned auditing confirms that this governance is necessary rather than optional. The contract-violation audit reports 84 flagged records in total, split into 75 metric-aliasing cases and 9 measurement-plane ambiguity cases. However, these records are retained for transparency and interpreted conservatively, because removing them would artificially increase apparent agreement at the cost of traceability. Consequently, Section IV-D conclusions prioritize defensible comparability over maximal aggregation: claims are pooled only when plane labels are explicit and metric roles are non-aliased [O_ISAC_132], [O_ISAC_061], [O_ISAC_013], [O_ISAC_050], [O_ISAC_056].

Comparability guard: any cross-study statement that mixes optical-plane and electrical-plane metrics without explicit conversion, or that interchanges \(\Delta r_{\min}\) and \(\sigma_r\), is treated as non-comparable evidence under the taxonomy contract.

**Lesson (D):** Detection and observability labels are only the first step; valid O-ISAC synthesis requires joint enforcement of receiver-model transparency, measurement-plane separation, and non-alias metric reporting.

---

## E. Taxonomy Summary Views
### E.1 Taxonomy Figure
Section IV-E consolidates taxonomy evidence into figure and matrix views that are auditable against the mapping contract. In the revised visual treatment, Fig. IV-1 is intentionally reader-facing: rather than asking the reader to decode dense taxonomy labels first, it turns the dominant O-ISAC medium classes into semantic schematics and then connects them to integration style and detection regime. Thus, the figure is designed to teach what fiber, FSO, VLC/LiFi, hybrid, and THz-linked O-ISAC mean at a glance before the reader moves to count-heavy or matrix-style synthesis.

The explanatory figure remains grounded in the canonical N=220 corpus summarized elsewhere in this section. Medium composition is hybrid 116/220 (52.7%), cabled fiber 45/220 (20.5%), VLC/LiFi 25/220 (11.4%), FSO 19/220 (8.6%), and terahertz 1/220 (0.5%), with the remaining 14/220 records in minor classes. Integration composition is shared front-end 194/220 (88.2%) and separate front-ends 26/220 (11.8%), while detection composition is direct 118/220 (53.6%), coherent 97/220 (44.1%), and five residual labels. However, these shares indicate evidence concentration only; they do not establish modality superiority. Their role here is to support the taxonomy narrative, while the figure itself prioritizes conceptual legibility.

To preserve readability, Fig. IV-1 foregrounds the dominant medium classes and their semantic meanings, while low-support media remain compressed into the surrounding textual and tabular synthesis rather than overloaded into the main visual. Consequently, the figure should be read as a taxonomy explainer, whereas Table IV-E and Fig. IV-2 preserve the denser cluster and specialization views needed for auditability.

![Fig. IV-1. Reader-facing semantic taxonomy map for O-ISAC. The figure makes the dominant medium classes visually identifiable through compact schematics for fiber, FSO, VLC/LiFi, hybrid, and THz-linked systems, and then links these classes to integration style (shared front-end versus separate front-ends) and detection regime (coherent versus direct). Its role is explanatory rather than rank-implying: it teaches what each taxonomy class means before the denser matrix and count-based synthesis in Table IV-E and Fig. IV-2.](fig_iv_1.png)

Section II governance remains binding at figure level. Even with a more didactic visual language, Fig. IV-1 interpretation is valid only under plane-aware metric semantics: no implicit OSNR-to-SNR substitution is allowed without explicit receiver/noise modeling, and no resolution-versus-accuracy aliasing is admitted when comparing taxonomy states [O_ISAC_021], [O_ISAC_039], [O_ISAC_077], [O_ISAC_132], [O_ISAC_061].

### E.2 Taxonomy Table
The matrix companion to Fig. IV-1 must encode clustered patterns rather than one-row-per-paper listings, so Sections IV-VI can reference stable taxonomy clusters with explicit comparability guards. Table IV-E summarizes the cluster-level synthesis contract by linking deployment context, integration mechanism, detection/observability class, and metric roles within a single textual anchor.

| Taxonomy Cluster | Dominant Deployment Scenario | Integration Mechanism | Detection/Observability Class | Representative Sensing Tasks | Primary Communication Metrics | Primary Sensing Metrics | Representative References |
|:--|:--|:--|:--|:--|:--|:--|:--|
| Fiber-guided O-ISAC cluster | Long-reach cabled links with distributed monitoring overlays | Shared front-end dominant | Coherent-leading with direct subset | Ranging primary, vibration concentration, fault-localization tail | BER, FEC margin, communication robustness | Spatial granularity/ranging and vibration indicators | [O_ISAC_006], [O_ISAC_041], [O_ISAC_013] |
| FSO wireless optical cluster | Line-of-sight outdoor and inter-building optical links | Shared front-end with non-negligible separate front-ends | Direct/coherent mixed | Ranging dominant with small localization tail | BER, outage, spectral efficiency | Range estimation and resolution-class indicators | [O_ISAC_021], [O_ISAC_023], [O_ISAC_199] |
| VLC/LiFi indoor cluster | Illumination-constrained indoor access and positioning | Shared front-end dominant | Direct-detection and intensity-only dominant | Ranging plus strong localization concentration | Throughput, BER, link reliability | Localization error and ranging metrics | [O_ISAC_068], [O_ISAC_039], [O_ISAC_009] |
| Hybrid bridge cluster | Fiber-wireless and photonic-THz bridging pipelines | Shared front-end dominant | Near-balanced coherent/direct with residual labels | Ranging dominant with multi-task tail | Throughput and BER under cross-link coupling | Range/localization and task-specific errors | [O_ISAC_077], [O_ISAC_010], [O_ISAC_190] |
| Residual low-support cluster | Specialized or emerging deployment cases | Mixed mechanisms | Mostly direct with sparse alternatives | Heterogeneous low-support tasks | Context-dependent | Context-dependent | [O_ISAC_070], [O_ISAC_056] |

An explicit ambiguity note is required for cluster interpretation. The contract audit reports 84 ambiguity flags, split into 75 metric-aliasing cases and 9 measurement-plane ambiguity cases. Therefore, ambiguity-prone clusters are retained but interpreted conservatively, and cross-cluster claims are qualified when aliasing or plane ambiguity remains unresolved.

In the revised visual treatment, Fig. IV-2 complements Table IV-E with a more reader-facing specialization view rather than a dense count-first graphic. Its function is to show how the main medium classes align with their dominant sensing emphases and where the literature remains task-concentrated versus task-diverse. Ranging remains globally dominant at 162/220 (73.6%). However, VLC/LiFi exhibits a stronger localization profile (13/25 across 2D localization and localization primary tokens), fiber retains a visible vibration concentration (8/45), and hybrid preserves a broader multi-task tail beyond ranging (21/116 non-ranging primary tokens). Consequently, Fig. IV-2 should be read as a conceptual medium-to-task explainer that makes specialization structure easier to recognize before the reader moves back to the denser table-level synthesis [O_ISAC_006], [O_ISAC_068], [O_ISAC_077], [O_ISAC_039].

![Fig. IV-2. Reader-facing medium-task specialization view for O-ISAC. The figure highlights how the dominant medium classes connect to their representative sensing emphases, making ranging dominance, VLC/LiFi localization concentration, fiber vibration salience, and hybrid multi-task breadth visually legible without implying that higher prevalence means superiority. Its role is explanatory and complementary to the denser cluster-level synthesis in Table IV-E.](fig_iv_2.png)

**Lesson (E):** Figure-table dual representation is necessary to keep taxonomy synthesis transparent, auditable, and governance-consistent when translating corpus structure into downstream trade-off analysis.
