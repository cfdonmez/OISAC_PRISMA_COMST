**Artifact Map**
- `ROOT_DIR`: `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST`
- **Step-0 alignment source**: `drafts/section_01_introduction.md` (notation and taxonomy anchor).
- **Notation/terminology extracted from Section I**:
  - Symbols: \(B_{\text{eff}}, R, \Delta r_{\min}\) (used here as \(\Delta d \equiv \Delta r_{\min}\)), \(\sigma_r\), SNR, BER, CRB, \(\alpha\).
  - Modality taxonomy: Fiber, FSO, VLC/LiFi, Photo-THz.
  - Style: evidence-traceable, metric-normalized, cross-modal COMST survey tone.
- **Primary VI-A evidence artifacts**:
  - `analysis/VI_ev_v2/section6A_evidence.csv` (CSV, 5,045 rows): line-level quotes, heading-path locators, concept tags (`opa`, `ris`, etc.).
  - `analysis/VI_ev_v2/section6B_opa_metrics.csv` (CSV): structured OPA fields (emitters, steering range, beamwidth).
  - `analysis/VI_ev_v2/section6C_ris_metrics.csv` (CSV): structured RIS fields (elements, phase bits, type).
  - `analysis/VI_ev_v2/retrieval_hits.jsonl` (JSONL): raw retrieval hits for Section 6A.
  - `analysis/VI_ev_v2/readiness_report.md` (MD): corpus-wide availability checks and row counts.
- **Paper-level full-text artifacts used** (processed markdown):
  - `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md`
  - `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md`
  - `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md`
  - `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md`
  - `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md`
  - `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md`
  - `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md`
  - `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md`
  - `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md`
- **Structured extraction artifacts used**:
  - `data/ext_res_v4/O_ISAC_009_v4.json`
  - `data/ext_res_v4/O_ISAC_091_v4.json`
  - `data/ext_res_v4/O_ISAC_112_v4.json`
  - `data/ext_res_v4/O_ISAC_127_v4.json`
- **Ranked VI-A candidate paper IDs** (direct relevance + metric richness):
  1. `O_ISAC_008`
  2. `O_ISAC_091`
  3. `O_ISAC_061`
  4. `O_ISAC_098`
  5. `O_ISAC_112`
  6. `O_ISAC_009`
  7. `O_ISAC_054`
  8. `O_ISAC_011`
  9. `O_ISAC_127`
  10. `O_ISAC_106` (artifact is sparse; abstract-only markdown)

---

**Evidence Table**

| claim_id | claim | paper_id(s) | excerpt (<=2 sentences) | locator | metric(s) extracted |
|---|---|---|---|---|---|
| C01 | OPA enables simultaneous sensing+communication via joint waveform. | O_ISAC_008 | “A QPSK-FMCW joint waveform … implement[s] simultaneous Lidar sensing and data communication.” | `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md:19` | Joint waveform: QPSK-FMCW |
| C02 | Prior OPA steering is often limited by sidelobes/envelope. | O_ISAC_008 | “...steering range is limited … further limiting the steering range below 30°...” | `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md:17` | Prior steering limit: <30° |
| C03 | OPA ISAC-LiDAR demo reports high rate and wide steering. | O_ISAC_008 | “...higher data rate of 4Gbps and a wider steering range of 60°×32°...” | `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md:9` | \(R=4\) Gbps; steering \(60^\circ\times 32^\circ\) |
| C04 | OPA demo reports BER/SNR and sensing readout jointly. | O_ISAC_008 | “BER is 4.88×10^-4 ... data at 4Gbps ... distance 15.005m...” | `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md:69` | BER \(4.88\times10^{-4}\); SNR 14 dB |
| C05 | OPA hardware metrics include aperture scale and efficiency. | O_ISAC_008 | “...number of ... elements is ... 128 ... emission efficiency ... 55.5% ... beam resolution 0.64°×0.33°...” | `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md:77` | \(N=128\); \(\eta=55.5\%\); angular resolution |
| C06 | OPA-OW-ISAC uses explicit C\&S coupled metrics and optimization. | O_ISAC_091 | “...metrics, i.e., SINR ... and ISLR ... optimization ... tradeoff ...” | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:17` | SINR + ISLR co-optimization |
| C07 | OPA spacing/FoV constraints induce multi-beam ambiguity. | O_ISAC_091 | “distance ... larger than half wavelength ... grating lobes ... FOV ... limited.” | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:57` and `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:62` | FoV-limited sensing region |
| C08 | OPA scenario parameters quantify aperture and atmospheric loss. | O_ISAC_091 | Table parameters include “Number of edge emitters \(N_t=16\)” and “Atmospheric attenuation \(12\,\mathrm{dB/km}\).” | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:219` and `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:224` | \(N_t=16\), \(\alpha=12\) dB/km |
| C09 | OIRS can offload beam alignment and support wide+narrow beams. | O_ISAC_098 | “...offload the burden of beam alignment ... OIRS ... partitioning ... output both wide and narrow beams.” | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:27` and `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:35` | Functional partitioning of OIRS surface |
| C10 | OIRS study explicitly models pointing/jitter/turbulence and refresh limits. | O_ISAC_098 | “...aiming error, link jitter, atmospheric turbulence ...”; parameter table includes \(\alpha_o=0.95\), \(\Delta t=0.2\) s. | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:35`, `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:431`, `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:441` | \(\alpha_o=0.95\), OIRS refresh 0.2 s |
| C11 | Optical IRS introduces NLoS links to recover blocked-LoS localization. | O_ISAC_112 | “...NLoS links via the optical IRSs markedly enhances the RSS ... where LoS links are blocked.” | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:42` | LoS-blockage mitigation via IRS-NLoS |
| C12 | Optical IRS fingerprint system reports concrete localization gains. | O_ISAC_112 | “...average PE ... improvements of 77.33%, 45.53%, and 59.26% ...” | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:495` | PE improvements \(77.33\%/45.53\%/59.26\%\) |
| C13 | OFDM-based VLC ISAC resolves LoS/NLoS and supports cm/Gbps operation. | O_ISAC_009 | “...OFDM-based sensing ... improve resolution of CIRs ... capable of achieving centimeter-level ... and Gbps data rate.” | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:5` | cm-level positioning; Gbps-class data |
| C14 | RIS-aided NLoS separability condition is explicitly given. | O_ISAC_009 | “...condition ... \(d_{SRD_n}\ge(d_{SD}+c/\mathrm{BW})\) ... RIS-reflected NLoS path ...” | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:637` | Geometric/bandwidth condition for RIS path |
| C15 | LED O-ISAC beamforming must be intensity-domain (not phase-domain). | O_ISAC_054 | “LEDs emit incoherent light ... phase modulation ... unattainable ... beamforming impossible ...”; lens-based beamforming then gives large gains. | `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md:33` and `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md:51` | BER gain 63.35 dB; MSE gain 40.42 dB; intensity +65.45% |
| C16 | Retroreflective O-ISAC gives explicit range-resolution formula. | O_ISAC_011 | “\(\Delta d=cT_s/2\) ... ADC 15GSa/s ... range resolution is 1cm.” | `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md:73` and `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md:128` | \(\Delta d=1\) cm |
| C17 | Adaptive RIS-UOWC reports strong BER/secrecy/latency outcomes under coherence limits. | O_ISAC_127 | “41.4% reduction in BER ... minimum \(2.3\times10^{-5}\) ... secrecy rate 8.2 bps/Hz ... latency 47.3 ms ... 37.5 μs per element ... below 100 ms coherence.” | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:23`, `:39`, `:575` | BER, secrecy, latency, coherence-time compliance |

---

## VI-A. Optical Reconfigurable Intelligent Surfaces and Optical Phased Arrays as Enabling Technologies for O-ISAC

### VI-A.1 Motivation and Role in O-ISAC
Optical phased arrays (OPA) and optical RIS/OIRS are enabling technologies because they move O-ISAC from fixed LoS links to programmable propagation, i.e., beam synthesis, NLoS creation, and closed-loop C\&S operation [O_ISAC_008], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112]. OPA-based systems already demonstrate joint waveform operation and wide steering windows, with reported simultaneous \(R=4\) Gbps operation and \(60^\circ\times 32^\circ\) steering-scale demonstrations [O_ISAC_008]. In parallel, OIRS-assisted systems explicitly offload alignment burden from the base station to distributed optical surfaces and combine wide-beam sensing with narrow-beam communication [O_ISAC_098]. In indoor VLC, IRS-assisted NLoS links are used to recover localization reliability when LoS is blocked [O_ISAC_112], while OFDM-based VLC ISAC provides separable LoS/NLoS channel sensing for communication-aided localization [O_ISAC_009]. This directly addresses the Section-I fragmentation gap on “enablers”: the same programmable optics block now appears as a common design lever across VLC, FSO, and underwater optical settings [O_ISAC_054], [O_ISAC_127].

### VI-A.2 Evidence-Based Taxonomy
We classify VI-A enablers on four orthogonal axes.

1. **Passive vs. active programmable optics**: passive/metasurface-like optical IRS units (indoor fingerprint localization) [O_ISAC_112], versus active OIRS/OPA with control electronics and closed-loop update [O_ISAC_098], [O_ISAC_091], [O_ISAC_127].
2. **Field-control vs. intensity-control**: coherent field-control (OPA branches with EOPM/SOA and phase-amplitude synthesis) [O_ISAC_091], [O_ISAC_061], [O_ISAC_008], versus intensity-domain control (LED IM/DD with lens-based beam shaping; retroreflective OFDM with CCR) [O_ISAC_054], [O_ISAC_011].
3. **Propagation regime**: indoor VLC/VLP [O_ISAC_009], [O_ISAC_011], [O_ISAC_112], outdoor FSO/OWC [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], and underwater optical channels [O_ISAC_127].
4. **Integration depth**: opportunistic assistance (IRS for localization enhancement) [O_ISAC_112], medium-depth co-design (OIRS partitioned wide/narrow beam workflow) [O_ISAC_098], and full PHY joint design (joint waveform + beamforming + C\&S metric coupling) [O_ISAC_008], [O_ISAC_091], [O_ISAC_009].

**Mini taxonomy figure (textual description):**  
“Fig. VI-A(a) draws a 2D plane: horizontal axis = control type (intensity \(\rightarrow\) field), vertical axis = integration depth (opportunistic \(\rightarrow\) fully joint). O_ISAC_112 sits in low-depth/intensity-assisted quadrant; O_ISAC_098 in medium-depth mixed-control; O_ISAC_008/O_ISAC_091/O_ISAC_061 in high-depth field-control quadrant; O_ISAC_127 extends RIS control into severe nonstationary channels.”

### VI-A.3 Modeling and Fundamental Limits

We keep Section-I notation and set \(\Delta d \equiv \Delta r_{\min}\).

For coherent field-controlled OPA/ORIS links, a canonical baseband model is
$$
y = \big(h_d + \mathbf{g}^T \mathbf{\Theta}\mathbf{f}\big)x + n,\quad
\mathbf{\Theta}=\mathrm{diag}\left(\beta_1 e^{j\phi_1},\ldots,\beta_N e^{j\phi_N}\right).
$$
This abstraction is consistent with coherent optical beamforming pipelines where each branch controls optical magnitude/phase [O_ISAC_091], [O_ISAC_061].  
For IM/DD systems (LED/lens/retroreflective), the receive model is intensity-domain:
$$
r = \zeta\,\big|h_d+\mathbf{g}^T\mathbf{\Theta}\mathbf{f}\big|^2 p + z,\quad p\ge 0,
$$
matching noncoherent constraints emphasized for LED O-ISAC [O_ISAC_054] and RO-ISAC [O_ISAC_011].

Let \(f_n=|f_n|e^{j\psi_n}\), \(g_n=|g_n|e^{j\gamma_n}\). Then
$$
\mathbf{g}^T\mathbf{\Theta}\mathbf{f}
=\sum_{n=1}^N \beta_n|g_n||f_n|e^{j(\phi_n+\gamma_n+\psi_n)}.
$$
Choosing \(\phi_n=-(\gamma_n+\psi_n)\) aligns phases, giving
$$
\big|\mathbf{g}^T\mathbf{\Theta}\mathbf{f}\big|
=\sum_{n=1}^N \beta_n|g_n||f_n|= \mathcal{O}(N),
$$
hence received power from the reflected component scales as \(\mathcal{O}(N^2)\) under ideal coherent alignment. Practical scaling is sub-quadratic under grating lobes/FoV truncation, insertion loss, turbulence, and pointing errors [O_ISAC_091], [O_ISAC_061], [O_ISAC_008], [O_ISAC_098], [O_ISAC_127].

Bandwidth-limited sensing resolution remains
$$
\Delta d \approx \frac{v}{2B_{\text{eff}}},
$$
with \(v=c\) in free-space and \(v\approx c/n_g\) in guided media (Section I convention). OFDM-based optical sensing explicitly leverages this \(B_{\text{eff}}\)-resolution coupling [O_ISAC_009], while RO-ISAC gives \(\Delta d=cT_s/2\) and reports \(1\,\mathrm{cm}\) at 15 GSa/s [O_ISAC_011].

For estimation accuracy:
$$
\sigma_r^2 = \mathbb{E}\!\left[(\hat r-r)^2\right] \ge \frac{1}{J_{rr}},
$$
and a delay-estimation template (wideband SNR form) is
$$
\mathrm{var}(\hat d)\gtrsim \frac{c^2}{32\pi^2\beta^2\mathrm{SNR}_{\mathrm{eff}}}.
$$
CRB-aware C\&S formulations are directly discussed in OPA-OW-ISAC and related ISAC optimization contexts [O_ISAC_091], [O_ISAC_061].

For communication:
$$
R = B_{\text{eff}}\log_2\!\left(1+\mathrm{SNR}_{\mathrm{eff}}(\mathbf{\Theta},\mathbf{w})\right)
$$
(coherent form; IM/DD uses nonnegative-input lower bounds). In practice, OPA/OIRS design changes \(\mathrm{SNR}_{\mathrm{eff}}\) by steering gain, clutter suppression, and alignment stability [O_ISAC_008], [O_ISAC_091], [O_ISAC_098].

A canonical co-design is
$$
\max_{\mathbf{\Theta},\mathbf{w}}\;\alpha R(\mathbf{\Theta},\mathbf{w}) + (1-\alpha)\mathcal{S}(\mathbf{\Theta},\mathbf{w}),
\quad \alpha\in[0,1]
$$
subject to
$$
\phi_n \in \mathcal{Q}_b,\;
0\le \beta_n\le 1,\;
\|\mathbf{w}\|_2^2\le P_{\max},\;
T_{\text{update}}\le \tau_c,\;
P_{\text{out}}(\epsilon_p,\sigma_j)\le \epsilon_{\max}.
$$
The \(\alpha\)-controlled tradeoff is empirically supported by SINR–ISLR anti-correlation in OPA studies [O_ISAC_091], BER/MSE tradeoffs across directionless/directional phases in LED O-ISAC [O_ISAC_054], and secrecy-energy Pareto fronts in adaptive RIS underwater settings [O_ISAC_127].

**Optical-specific constraints with evidence:**  
- Turbulence/attenuation: Beer–Lambert and turbulence models are central in OPA-OW-ISAC and OIRS mobile FSO [O_ISAC_091], [O_ISAC_098], and strongly salinity-coupled underwater optical channels [O_ISAC_127].  
- Pointing/jitter: explicitly modeled in OIRS mobile scenarios [O_ISAC_098] and discussed in UOWC control robustness [O_ISAC_127].  
- Wavelength dependence: OPA at 1550 nm with efficiency-steering coupling [O_ISAC_008]; underwater absorption varies with salinity and wavelength (e.g., 520 nm model) [O_ISAC_127].  
- Quantization/update: RIS phase quantization and per-element update budgets are explicit in adaptive RIS-UOWC [O_ISAC_127].  
- Insertion-loss/efficiency: OIRS attenuation coefficient and emitter efficiency constraints are explicitly reported [O_ISAC_098], [O_ISAC_008].  
- Phase-noise-specific measurement in ORIS/OPA: **[TODO: evidence needed]**.

### VI-A.4 Comparative Performance Synthesis

**Table VI-A.1. ORIS/OPA Enabling-Technology Comparison (evidence-grounded).**

| Paper | Enabler / regime | Communication metric(s) | Sensing metric(s) | Enabler scale (\(N\), \(b\)) | Steering / FoV | Update latency | Key hardware/channel constraints | \(\mathrm{CRQ}_{\Delta}=R/\Delta d\) |
|---|---|---|---|---|---|---|---|---|
| O_ISAC_008 | OPA, coherent LiDAR/OWC | \(R=4\) Gbps; BER \(4.88\times10^{-4}\) | Beam res \(0.64^\circ\times0.33^\circ\); range demo at 15 m | 128 elements | \(60^\circ\times32^\circ\) aliasing-free | NR | Sidelobe suppression, envelope-limited steering, 1550 nm efficiency | NR |
| O_ISAC_009 | VLC OFDM ISAC (RIS-ready) | Gbps-class (radar-CE), RSS baseline <100 Mbps | cm-level; sub-cm in high-\(M\) hybrid cases | RIS deployment condition provided (no array size instantiated) | PD FoV-constrained | Single pilot for sensing+CSI | LoS/NLoS resolvability depends on \(B_{\text{eff}}\) | \(1.0^\dagger\) |
| O_ISAC_011 | RO-ISAC (OFDM+CCR), IM/DD | BER-vs-SNR curves (multi-modulation) | \(\Delta d=cT_s/2\), reported 1 cm | 4 LEDs + 1 CCR | Indoor geometry-dependent | NR | Passive retroreflection, cross-correlation length vs RMSE | \(1.0^\dagger\) |
| O_ISAC_054 | LED + collimating-lens O-ISAC | BER gain 63.35 dB vs separated baseline | MSE gain 40.42 dB; intensity +65.45% | NR (\(N\) not explicitly tabulated) | Directionless vs directional phases | Phase-based | Incoherent LEDs prohibit phase-array beamforming | \(0.1^\dagger\) |
| O_ISAC_061 | OPA OW-ISAC (journal) | SINR-constrained BER curves; Gbps-class claim | ISLR/RMSE imaging trends; cm-level asymptotic region | \(N_t=32\), \(N_r=7\) | FoV-limited PDs, multi-beam | NR | Grating lobes, atmospheric attenuation (12 dB/km config) | \(1.0^\dagger\) |
| O_ISAC_091 | OPA OW-ISAC (conference) | SINR-constrained optimization | ISLR-based sensing, C\&S anti-correlation | \(N_t=16\) | FoV-limited; grating-lobe interference | NR | \(\alpha=12\) dB/km in setup | \(0.1^\dagger\) |
| O_ISAC_098 | OIRS + PD array (mobile FSO) | BER/outage asymptotic analysis | Closed-loop alignment sensing + tracking | OIRS partitioned regions; \(b\) NR | Wide-beam sensing + narrow-beam comm | OIRS refresh slot 0.2 s | Pointing error, jitter, turbulence, OIRS attenuation \(\alpha_o=0.95\) | \(0.01^\dagger\) |
| O_ISAC_112 | Optical IRS-aided VLP | Localization-oriented (comm secondary) | Final PE down to 0.017 m; 90% PE 0.079 m | \(N_s=21\times21\) units per wall (dual-wall) | NLoS reconstruction through IRS | Offline+online fingerprint workflow | LoS blockage and NLoS path design | \(0.1^\dagger\) |
| O_ISAC_127 | Adaptive RIS-UOWC | BER min \(2.3\times10^{-5}\); secrecy 8.2 bps/Hz | Robust under salinity/turbulence dynamics | \(N=64\)–512; 5-bit phase | Adaptive RIS beam control | 47.3 ms loop; 37.5 \(\mu s\)/element | Coherence-time-constrained control, salinity-dependent attenuation | \(0.01^\dagger\) |

\(\dagger\) Indicative \(\mathrm{CRQ}_{\Delta}\) values computed from `scenario_level` structured fields in `data/ext_res_v4/*_v4.json`; manual figure/table verification is still needed before camera-ready finalization.

**Synthesis and Pareto interpretation.**  
The strongest **beam-agility frontier** is delivered by coherent OPA designs (high steering window + explicit beamforming metrics), but their gains are bounded by grating-lobe/FoV and atmospheric losses [O_ISAC_008], [O_ISAC_061], [O_ISAC_091]. The strongest **blockage-robustness frontier** is delivered by optical IRS/OIRS, especially where NLoS reconstruction or alignment offloading is central [O_ISAC_098], [O_ISAC_112], [O_ISAC_009]. Multi-objective curves repeatedly show a **communication-vs-sensing coupling**: stricter communication SINR (or secrecy) constraints consume spatial degrees of freedom and can degrade sensing contrast/accuracy [O_ISAC_091], [O_ISAC_127]. LED-based intensity-domain systems can still show very large practical gains without coherent phase control, but they require lens/geometry-based beam shaping rather than array-phase synthesis [O_ISAC_054]. Finally, evidence granularity is uneven across papers; several results are curve-level rather than table-level, which limits direct meta-analysis precision.

### VI-A.5 Open Challenges and Actionable Directions

1. **Metric contract for enabler papers**: Why it matters: cross-paper comparison is currently weak; evidence: mixed reporting across SINR/ISLR, PE, BER-only, and no common \(N,b,T_{\text{update}}\) tuple [O_ISAC_091], [O_ISAC_112], [O_ISAC_098]; hypothesis: enforce a minimal contract \(\{R,\mathrm{BER},\Delta d,\sigma_r,\mathrm{CRB},N,b,\eta,T_{\text{update}}\}\) with scenario metadata.
2. **Latency-aware control under channel coherence**: Why it matters: stale control invalidates RIS gains; evidence: underwater coherence/latency budgets are explicit and restrictive [O_ISAC_127], while many FSO/VLC works omit closed-loop timing [O_ISAC_061], [O_ISAC_112]; hypothesis: optimize \((\mathbf{\Theta},\mathbf{w})\) with hard \(T_{\text{update}}\le\tau_c\) constraints and predictor uncertainty.
3. **Quantized-phase-aware estimation bounds**: Why it matters: finite \(b\)-bit phase control changes both link and sensing Fisher information; evidence: 5-bit RIS quantization appears in adaptive RIS settings [O_ISAC_127], but CRB under quantization is rarely tabulated in optical enabler papers [O_ISAC_091]; hypothesis: derive \(\mathrm{CRB}(b,N,\sigma_j)\) and design robust codebooks for joint C\&S.
4. **Unified wide-/narrow-beam co-design**: Why it matters: practical systems need wide-beam discovery and narrow-beam throughput; evidence: explicit OIRS partitioning is effective but heuristic [O_ISAC_098]; hypothesis: formulate dynamic partition control \(S_w/S_n\) as a constrained MDP jointly minimizing outage and localization error.
5. **Grating-lobe-aware sensing quality control**: Why it matters: OPA multi-beam ambiguity directly contaminates sensing clutters; evidence: FoV-limited PD and ISLR degradation under tighter SINR are observed [O_ISAC_061], [O_ISAC_091]; hypothesis: jointly optimize transmitter precoding and receiver FoV orientation with clutter-aware regularization.
6. **Cross-modality robustness transfer (VLC/FSO/UOWC)**: Why it matters: current solutions are siloed by medium; evidence: distinct impairment sets dominate each modality (LoS blockage in indoor VLC, turbulence/pointing in FSO, salinity-turbulence in UOWC) [O_ISAC_112], [O_ISAC_098], [O_ISAC_127]; hypothesis: build modality-conditioned yet shared policy/state abstractions for transferable control.
7. **Hardware non-idealities in-the-loop**: Why it matters: insertion loss, efficiency roll-off, and jitter determine realized gains; evidence: \(\alpha_o=0.95\), emitter efficiency, and jitter terms materially alter outcomes [O_ISAC_098], [O_ISAC_008], [O_ISAC_127]; hypothesis: shift from idealized \(\Theta\)-only models to hardware-calibrated digital twins for robust optimization.
8. **Security-constrained sensing communication**: Why it matters: RIS shaping for secrecy may conflict with sensing observability; evidence: secrecy-energy gains are explicit in adaptive RIS [O_ISAC_127], while OPA studies report C\&S anti-correlation in SINR/ISLR [O_ISAC_091]; hypothesis: solve tri-objective optimization \( \max (R,\mathcal{S},R_{\text{sec}}) \) with uncertainty sets on eavesdropper CSI and clutter models.

**Section VI-A takeaway.**  
OPA and ORIS/OIRS are now demonstrably central to O-ISAC because they convert optical channels from fixed propagation to programmable propagation. OPA provides the strongest evidence for agile angle-domain C\&S co-design, while ORIS/OIRS provides the strongest evidence for blockage resilience and closed-loop alignment support. The governing tradeoff is no longer only rate-vs-resolution; it is a multi-objective surface involving sensing fidelity, communication QoS, control latency, and hardware non-idealities. A compact unified model using \(\mathbf{\Theta}\)-controlled channels with explicit IM/DD constraints is sufficient to compare these enablers across modalities, but standardized reporting is still missing. Advancing VI-A therefore requires benchmark-quality, latency-aware, hardware-calibrated evaluations rather than isolated proof-of-concept gains.
# VI. Enabling Technologies and System-Level Co-Design for Optical ISAC

---
Section VI consolidates the enabling technologies and design principles that determine whether optical integrated sensing and communication (O-ISAC) can scale from proof-of-concept links to reproducible systems. The evidence in the corpus consistently shows that optical phased arrays (OPA), ORIS control, robustness-aware optimization, and network coordination are coupled design problems rather than independent modules [O_ISAC_008], [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112], [O_ISAC_127]. To keep the main narrative readable, detailed traceability notes and extended audit material are retained in the supplementary material rather than in the core manuscript text.

**TODO (missing evidence / metrics)**
- `[TODO: evidence needed]` SLM/DMD-specific O-ISAC quantitative studies (phase bits, update rate, insertion loss) were not found in the high-confidence VI-A subset.
- `[TODO: evidence needed]` Direct phase-noise measurements (not just phase-control statements) for OPA/ORIS were not explicitly reported in the extracted lines.
- `[TODO: evidence needed]` Several papers provide figure-level BER/RMSE trends without tabulated points; digitization is needed for strict meta-statistics.
- `[TODO: evidence needed]` `O_ISAC_106` processed markdown is abstract-only in current artifact state; full text should be re-ingested before final camera-ready synthesis.

In this section, we use one canonical term: **ORIS (Optical Reconfigurable Intelligent Surface)**.

---
**Table VI-1. Unified Notation for Section VI.**

**VI-B Artifact Map**
- `ROOT_DIR`: `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST`
- **Alignment source (notation/taxonomy):** `drafts/section_01_introduction.md`
  - Notation preserved from Section I: `B_eff`, `R`, `\Delta r_{min}`, `\sigma_r`, `SNR`, `BER`, and `\mathrm{CRQ}_{\Delta}=R/\Delta r_{min}`.
  - Modality boundaries preserved: Fiber, FSO, VLC/LiFi, Photo-THz.
- **Scope/TOC detection:** `review_package/surveyOutline.md` exists; no explicit `VI-B` heading token was found via keyword scan, so user-provided VI-B scope is applied.
- **Primary corpus files mined for VI-B impairments/robustness evidence (markdown):**
  - `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md` (FSO-ISAC channel model, lognormal turbulence, Rytov, quantile-robust QoS, RMSE-vs-`C_n^2`).
  - `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md` (Gamma-Gamma turbulence, Beer-Lambert attenuation, Rayleigh pointing/jitter model, visibility and BER sensitivity).
  - `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md` (OPA OW-ISAC atmospheric/shot-noise model, SINR-ISLR tradeoff, 0.05-quantile robustness).
  - `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md` (OPA OW-ISAC compact model with turbulence/attenuation/noise and C&S tradeoff).
  - `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md` (OIRS mobile channel with pointing+turbulence+attenuation, outage/BER asymptotics, tracking-refresh effects).
  - `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md` (LoS blockage evidence and optical-IRS NLoS robustness gains).
  - `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md` (underwater turbulence/salinity robustness, latency/coherence coupling, RIS adaptation gains).
  - `data/proc_markdowns/O_ISAC_199/O_ISAC_199.md` (weather attenuation ranges, lognormal/Gamma-Gamma comparisons, MIMO+compensator robustness gains).
  - `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md` (VLC AWGN decomposition with shot/thermal/background terms, LoS/NLoS separability).
  - `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md` (RO-ISAC AWGN robustness trends and sampling-limited range resolution).
  - `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md` (survey-level evidence on blockage/noise mitigation via MIMO/RIS/hybrid fallback).
- **Extraction/analysis artifacts (metrics/index support):**
  - `analysis/VI_ev_v2/section6A_evidence.csv` (line-level evidence anchors; reusable locator index).
  - `analysis/VI_ev_v2/section6B_opa_metrics.csv` (OPA fields: array and steering attributes).
  - `analysis/VI_ev_v2/section6C_ris_metrics.csv` (RIS fields: element/bit/type descriptors).
  - `analysis/VI_ev_v2/retrieval_hits.jsonl`, `analysis/VI_ev_v2/anchor_table.csv`, `analysis/VI_ev_v2/readiness_report.md` (retrieval traces and readiness checks).
  - `data/ext_res_v4/O_ISAC_*.json` (structured per-paper metric cards; used for cross-checking units where available).
- **Ranked VI-B candidate paper_ids (relevance to impairments + quantitative richness):**
  1. `O_ISAC_098`
  2. `O_ISAC_061`
  3. `O_ISAC_023`
  4. `O_ISAC_035`
  5. `O_ISAC_091`
  6. `O_ISAC_127`
  7. `O_ISAC_199`
  8. `O_ISAC_009`
  9. `O_ISAC_112`
  10. `O_ISAC_011`
| Symbol | Meaning | Used in |
|---|---|---|
| $x(t)$ | Optical transmit waveform (or equivalent sampled signal) | VI-C, VI-E |
| $\bar P$ | Average optical power budget | VI-C, VI-D |
| $P_{\max}$ | Peak optical power budget | VI-C, VI-D |
| $H$ | End-to-end channel coefficient/gain | VI-B |
| $H_l$ | Deterministic/path-loss component of $H$ | VI-B |
| $H_a$ | Atmospheric/medium turbulence component of $H$ | VI-B |
| $H_p$ | Pointing/misalignment component of $H$ | VI-B |
| $\gamma$ | Instantaneous SINR/SNR proxy | VI-B, VI-E |
| $\gamma_{\text{th}}$ | Reliability threshold for outage control | VI-B |
| $\varepsilon$ | Allowed outage probability target | VI-B, VI-C |
| $\Theta$ | ORIS diagonal response matrix | VI-A, VI-C, VI-E, VI-F |
| $\beta_n$ | ORIS amplitude coefficient of element $n$ | VI-A |
| $\theta_n$ | ORIS phase of element $n$ | VI-A, VI-E |
| $Q$ | Number of phase quantization levels | VI-A, VI-E |
| $\mathbf{w}_k$ | Beamforming vector for user $k$ | VI-C, VI-E |
| $\mathrm{SINR}_k$ | User-$k$ communication quality metric | VI-E |
| $\mathrm{CRB}$ | Cramer-Rao bound for sensing estimation quality | VI-C, VI-E, VI-F |

**VI-B Evidence Table**
> **Model VI-U (Unified Channel/Signal Model).**
>
> $$
> y_k = \left(h_{d,k} + \mathbf{h}_{r,k}^{T}\Theta\mathbf{g}\right)x + n_k,
> $$
> $$
> \Theta = \operatorname{diag}\!\left(\beta_n e^{j\theta_n}\right),
> $$
> $$
> \theta_n \in \left\{0,\frac{2\pi}{Q},\ldots,\frac{2\pi(Q-1)}{Q}\right\}.
> $$
>
> Model VI-U is a compact abstraction used in VI-A, VI-C, VI-E, and VI-F for consistent cross-section notation [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_127].

| claim_id | claim | paper_id(s) | excerpt (<=2 sentences) | locator (heading + line range or page) | metric(s) extracted |
|---|---|---|---|---|---|
| B01 | FSO-ISAC total channel includes attenuation, scintillation, and geometric loss. | O_ISAC_023 | “The atmospheric-propagation term contains atmospheric attenuation, scintillation, and geometric loss.” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:133-143` (channel model paragraph) | Composite channel factors (`L_a,L_t,L_g`) |
| B02 | Weak turbulence is modeled by lognormal fading with Rytov-based scintillation index. | O_ISAC_023 | “The log-normal distribution is adopted under weak turbulence; scintillation index is obtained by Rytov approximation.” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:143-155` (turbulence model) | `\sigma_t^2(D)`, Rytov mapping |
| B03 | Communication/sensing noise is modeled as shot+thermal AWGN. | O_ISAC_023 | “Thermal and shot noise are modeled as AWGN in communication and sensing chains.” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:183`, `:212` (noise model) | AWGN PSD terms (`N_c`, `N_s`) |
| B04 | A 0.05 lower-quantile substitution is used to guarantee >95% QoS under turbulence. | O_ISAC_023 | “Scintillation is replaced by the 0.05 lower quantile so target ISAC performance is achieved with probability above 95%.” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:262` (robust optimization simplification) | Quantile level `q=0.05` |
| B05 | Sensing RMSE worsens as turbulence strength (`C_n^2`) increases. | O_ISAC_023 | “RMSE curves deteriorate with stronger scintillation indices and improve with electrical SNR.” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:753-757` (RMSE simulation discussion) | RMSE vs SNR and `C_n^2` |
| B06 | Gamma-Gamma is adopted for turbulence with explicit scintillation-index relation. | O_ISAC_035 | “Gamma-Gamma models atmospheric turbulence; scintillation index is `\sigma_I^2=(1/a)+(1/b)+(1/ab)`.” | `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md:70-75` (model section) | Gamma-Gamma parameters `(a,b)` |
| B07 | Pointing error is modeled by Rayleigh radial displacement and equivalent-beam ratio `\gamma=w_{z_{eq}}/(2\sigma_s)`. | O_ISAC_035 | “Radial displacement follows Rayleigh; pointing PDF uses `\gamma=w_{z_{eq}}/(2\sigma_s)`.” | `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md:79-83` (pointing model) | `\sigma_s`, `w_{z_{eq}}`, `\gamma` |
| B08 | Fog and misalignment produce strong BER penalties. | O_ISAC_035 | “Visibility 10 km vs 0.5 km maps to −0.44 vs −33.98 dB/km; adding jitter `\sigma_s=0.05 m` worsens BER.” | `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md:244`, `:251` (Table II + BER analysis) | attenuation dB/km; jitter std |
| B09 | OPA OW-ISAC uses Beer-Lambert attenuation and lognormal turbulence with Rytov/`C_n^2`. | O_ISAC_061 | “Atmospheric attenuation (fog/haze) and lognormal scintillation with Rytov approximation are explicitly modeled.” | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:116-133` (atmospheric channel) | `\alpha` dB/km, `C_n^2`, `\sigma_t^2` |
| B10 | OPA robustness uses 0.05-quantile scintillation for >95% communication reliability constraints. | O_ISAC_061 | “The 0.05-lower quantile replacement guarantees desired communication performance with probability larger than 95%.” | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:346` (QoS constraint) | Quantile robust SINR constraint |
| B11 | Practical OW-ISAC curves show BER-RMSE tradeoff and cm-level asymptotic sensing precision. | O_ISAC_061 | “Raising communication SINR constraints degrades sensing; RMSE converges to centimeter-level asymptotic region.” | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:640-652` (Fig.11/12 discussion) | BER/SNR slope; cm-level RMSE region |
| B12 | OPA conference model confirms shot/thermal noise and SINR-ISLR anticorrelation. | O_ISAC_091 | “Communication and sensing noises are shot+thermal; increasing SINR threshold deteriorates ISLR.” | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:101-117`, `:275-285` | SINR-ISLR tradeoff trend |
| B13 | Mobile OIRS channel is explicitly multiplicative in pointing, turbulence, and attenuation factors. | O_ISAC_098 | “Channel fading includes pointing gain, atmospheric turbulence gain, and atmospheric attenuation gain.” | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:78-83` (channel decomposition) | `h_{p}`, `h_a`, `h_l` terms |
| B14 | Tracking-refresh mismatch induces beam-alignment error coupled to user speed and OIRS deflection. | O_ISAC_098 | “Alignment error follows `\tau_c=|v_u\Delta t-d_o|`; refresh lag causes substantial BER/outage degradation.” | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:57`, `:486` | `\Delta t=0.2 s`, `\tau_c` model |
| B15 | Turbulence regime switch uses lognormal for `\sigma_R^2<0.3` and Gamma-Gamma otherwise. | O_ISAC_098 | “Weak turbulence uses lognormal; medium/strong uses Gamma-Gamma with threshold at `\sigma_R^2=0.3`.” | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:122-145` (turbulence subsection) | regime boundary `\sigma_R^2=0.3` |
| B16 | LoS blockage severely harms indoor VLP, and optical IRS NLoS reconstruction recovers robustness. | O_ISAC_112 | “LoS blockage can reduce accuracy drastically; introducing IRS-assisted NLoS links improves blocked-area RSS and PE.” | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:36-42`, `:495` | PE improvements `77.33%`, `45.53%`, `59.26%` |
| B17 | VLC noise floor includes shot, thermal, and ambient-background current terms. | O_ISAC_009 | “AWGN variance is decomposed into shot and thermal terms, including background current contribution.” | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:174` (noise model) | `N_0^{shot}`, `N_0^{thermal}`, `I_bg` |
| B18 | RIS-UOWC robustness is limited by coherence time and solved via low-latency adaptation. | O_ISAC_127 | “Channel coherence is often under 100 ms; measured loop latency is 47.3 ms with 37.5 `\mu s` per element.” | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:39`, `:497`, `:505` | `\tau_c` (100–300 ms), latency |
| B19 | Weather attenuation and MIMO diversity strongly alter availability-level operating range and BER. | O_ISAC_199 | “Attenuation increase shrinks max range (69.6 km to 2.4 km); 4x4 MIMO+compensator reaches log(BER) −35.018 and 58.9 dB power.” | `data/proc_markdowns/O_ISAC_199/O_ISAC_199.md:368`, `:275` | weather dB/km table; BER/power gains |

**Table VI-B.1. Impairment Models Used in O-ISAC Literature**

| paper_id | medium | model family | key parameters reported | scenario | sensing impact analyzed? |
|---|---|---|---|---|---|
| O_ISAC_023 | FSO (DCO-OFDM ISAC) | Lognormal turbulence + Beer-Lambert attenuation + AWGN | `\sigma_t^2(D)` via Rytov, `\alpha` (−12.8 dB/km config), 0.05 quantile | Outdoor terrestrial FSO | Yes (Fisher info / RMSE) |
| O_ISAC_035 | FSO (OCDM-FMCW) | Gamma-Gamma turbulence + Rayleigh pointing + Beer-Lambert | `(a,b)`, `\sigma_I^2`, `\gamma=w_{z_{eq}}/(2\sigma_s)`, visibility 10/0.5 km, `\sigma_s=0.05 m` | FSO-ISAC link (exp+sim) | Yes (ranging + BER coupling) |
| O_ISAC_061 | OPA OW-ISAC | Lognormal scintillation + atmospheric attenuation + DD noise | `\alpha=12 dB/km`, `C_n^2=5\times10^{-14}`, quantile 0.05 | Outdoor OPA, multi-UE | Yes (ISLR/RMSE) |
| O_ISAC_091 | OPA OW-ISAC | Lognormal turbulence + Beer-Lambert attenuation + DD noise | `\alpha=12 dB/km`, `C_n^2=5\times10^{-14}`, quantile 0.05 | Outdoor OPA, compact formulation | Yes (ISLR tradeoff) |
| O_ISAC_098 | OIRS mobile OWC | Composite pointing+turbulence+attenuation; weak-LN/strong-GG | `\tau_c=|v_u\Delta t-d_o|`, `\Delta t=0.2 s`, `\alpha_o=0.95`, `\sigma_R^2` regime split | Mobile user with closed-loop tracking | Yes (outage/BER + tracking) |
| O_ISAC_009 | VLC OFDM-ISAC | LoS/NLoS CIR + AWGN (shot+thermal+ambient) | `N_0^{shot}`, `N_0^{thermal}`, `I_bg`, separability condition `d_{SRD}\ge d_{SD}+c/BW` | Indoor multipath VLC | Yes (range RMSE, CE) |
| O_ISAC_011 | RO-ISAC (retroreflective) | AWGN + sampling-limited ranging | `\Delta d=cT_s/2`, ADC 15 GSa/s (`1 cm`) | Indoor retroreflective ISAC | Yes (distance RMSE) |
| O_ISAC_112 | Optical IRS-assisted VLP | Blockage-aware LoS/NLoS model + AWGN | IRS array `21\times21`, `\mathrm{SNR}=30 dB` setting | Indoor blocked-LoS localization | Yes (positioning error) |
| O_ISAC_127 | RIS-UOWC | Absorption+scattering+turbulence with dynamic salinity model | salinity 31.9–34.4 PSU, coherence 100–300 ms, 5-bit RIS, latency 47.3 ms | Underwater dynamic channel | Yes (BER/secrecy robustness) |
| O_ISAC_199 | FSO-FBG integrated link | Lognormal/Gamma-Gamma + weather attenuation + pointing-coupling | attenuation set {0.54,2,6.9,18.3,28.9,75} dB/km; MIMO modes | Open-environment FSO IoT | Yes (BER/power + sensor feedback) |
### VI-A. OPA and ORIS as Enabling Technologies

**Table VI-B.2. Mitigation Techniques vs. Impairments (Evidence-Grounded)**

| mitigation technique | turbulence | pointing | blockage / intermittency | background / noise | evidence paper_ids + reported gains |
|---|---|---|---|---|---|
| Quantile-robust resource allocation (`q=0.05`) | Strong | Partial | No | Partial | `O_ISAC_023`, `O_ISAC_061`, `O_ISAC_091`: replaces stochastic scintillation with 0.05 lower-quantile to guarantee >95% QoS |
| Closed-loop OIRS adaptive beam tracking | Strong | Strong | Partial | No | `O_ISAC_098`: adaptive alignment improves BER/outage versus non-adaptive baseline; refresh-aware model with `\Delta t=0.2 s` |
| Optical IRS NLoS channel reconstruction | No | No | Strong | Partial | `O_ISAC_112`: PE improvements `77.33%/45.53%/59.26%` in blocked-LoS indoor localization |
| OFDM radar-assisted LoS/NLoS separation + hybrid Radar-RSS | Partial (multipath-induced) | No | Strong (NLoS recovery) | Strong | `O_ISAC_009`: RSS-only becomes meter-level in multipath, hybrid sensing reaches centimeter/sub-centimeter regimes |
| Spatial diversity + compensator (MIMO-FSO) | Strong | Strong | Partial | Partial | `O_ISAC_199`: log(BER) improves to `-35.018`, received power to `58.9 dB`, required Tx power reduced `65 -> 46.6 dBm` |
| Predictive RIS control under coherence constraints | Strong | Partial | Partial (link continuity) | Strong | `O_ISAC_127`: BER reduction `41.4%`, secrecy `+46.4%`, latency `47.3 ms` within coherence budget |
| SINR-constrained beamforming (SDR/LP) | Partial | No | No | Strong | `O_ISAC_061`, `O_ISAC_091`: communication-SINR protection with explicit sensing metric penalty (ISLR deterioration) |
| Noise-robust sensing accumulation (longer correlation/averaging) | No | No | No | Strong | `O_ISAC_011`: increasing cross-correlation symbol count lowers distance RMSE under AWGN |
| Hybrid VLC-RF fallback for blocked optical links | No | No | Strong | Partial | `O_ISAC_303`: survey evidence reports RF side-link activation when VLC is blocked |

## VI-B. Channel Impairments and Robustness Mechanisms for O-ISAC (Turbulence, Pointing, Blockage, and Noise)

### VI-B.1 Why Channel Robustness Is an Enabling Pillar for O-ISAC
O-ISAC couples communication and sensing on the same optical waveform, so any channel impairment simultaneously perturbs `R`, `BER`, and sensing fidelity (`\Delta r_{min}`, `\sigma_r`). The corpus repeatedly reports this dual degradation mechanism: stronger turbulence raises BER and sensing RMSE [O_ISAC_023], [O_ISAC_035], communication-priority SINR constraints can worsen sensing-side sidelobe metrics [O_ISAC_061], [O_ISAC_091], and mobile misalignment can raise both outage and BER if control latency is not matched to motion dynamics [O_ISAC_098]. For indoor VLC localization, LoS blockage causes severe collapse unless NLoS reconstruction mechanisms are introduced [O_ISAC_112]. For underwater optical channels, non-stationary salinity and turbulence invalidate static RIS settings on timescales comparable to channel coherence, making robustness a first-order design requirement rather than a post-processing add-on [O_ISAC_127].

### VI-B.2 Impairment Taxonomy and Modeling Choices (Evidence-Based)
We organize VI-B impairments by physical origin and modeling convention used in the corpus.
OPA and ORIS are the main physical enablers that make optical propagation programmable for joint sensing and communication. OPA studies report explicit joint-waveform and steering gains, while ORIS studies report alignment offloading and blockage mitigation through controlled reflected paths [O_ISAC_008], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112]. Model VI-U captures this common structure by representing both direct and ORIS-assisted paths in one expression [O_ISAC_061], [O_ISAC_091].

1. **Atmospheric/medium turbulence:** weak-regime lognormal models and moderate/strong-regime Gamma-Gamma models are both used in O-ISAC papers; several studies explicitly map turbulence strength through Rytov-related terms and `C_n^2` [O_ISAC_023], [O_ISAC_035], [O_ISAC_098], [O_ISAC_061], [O_ISAC_091].
2. **Pointing and misalignment:** two modeling levels appear. The first level uses isotropic jitter with Rayleigh radial displacement and equivalent beam radius parameters [O_ISAC_035]. The second level augments this with mobility-induced non-zero boresight error tied to refresh interval and user velocity (`\tau_c`-type alignment error) [O_ISAC_098].
3. **Weather/obscuration attenuation:** Beer-Lambert attenuation and visibility-based coefficients dominate atmospheric loss modeling, with reported attenuation spanning mild clear-air to severe fog regimes [O_ISAC_035], [O_ISAC_061], [O_ISAC_091], [O_ISAC_199].
4. **Blockage and intermittency:** indoor LoS occlusion is treated as a structural reliability problem, mitigated by optical-IRS induced NLoS path construction [O_ISAC_112].
5. **Receiver noise and detection regime:** IM/DD chains commonly model shot and thermal noise, and VLC studies further include ambient-background current terms [O_ISAC_009], [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_011].

**Textual mini-taxonomy figure (VI-B):** a four-layer stack: *Layer-1 medium* (FSO/VLC/UOWC), *Layer-2 impairments* (turbulence, pointing, weather/blockage, background noise), *Layer-3 models* (lognormal, Gamma-Gamma, Rayleigh-jitter, Beer-Lambert, AWGN decomposition), and *Layer-4 mitigations* (quantile-robust design, adaptive tracking, RIS/NLoS reconstruction, diversity/hybrid fallback).
A compact steering anchor for OPA is

### VI-B.3 Fundamental Limits and Analytical Insights
Let the impairment-aware scalar optical channel be
$$
 h = h_L\,h_T\,h_P\,h_W,
$$
where `h_L` is deterministic path/interface loss, `h_T` is turbulence fading, `h_P` is pointing loss, and `h_W` is weather attenuation [O_ISAC_023], [O_ISAC_098], [O_ISAC_061].

For coherent detection, a standard normalization is
$$
y = h x + n,\qquad \gamma_{\text{coh}} \propto |h|^2.
AF(\theta)=\sum_{m=0}^{M-1} a_m\exp\!\left(j\left(kdm\sin\theta+\phi_m\right)\right),
$$
For IM/DD links used in most VLC/OWC prototypes,
$$
y = \mathcal{R} P_t h s + n,\qquad
\gamma_{\text{IM/DD}} = \frac{(\mathcal{R}P_t h)^2}{\sigma_n^2},
\phi_m^{\star}=-kdm\sin\theta_0,
$$
with shot/thermal (and, in VLC, background) terms included in `\sigma_n^2` [O_ISAC_009], [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_011].

For weak turbulence, a lognormal family is used:
$$
h_T = e^{X},\quad X\sim\mathcal{N}\!\left(-\frac{\sigma_X^2}{2},\sigma_X^2\right),\quad \mathbb{E}[h_T]=1,
$$
with `\sigma_X^2` linked to Rytov variance and `C_n^2` [O_ISAC_023], [O_ISAC_098], [O_ISAC_061], [O_ISAC_091].
For moderate/strong regimes, Gamma-Gamma is used [O_ISAC_035], [O_ISAC_098], [O_ISAC_199]:
$$
f_{h_T}(h)=\frac{2(\alpha\beta)^{\frac{\alpha+\beta}{2}}}{\Gamma(\alpha)\Gamma(\beta)}h^{\frac{\alpha+\beta}{2}-1}K_{\alpha-\beta}\!\left(2\sqrt{\alpha\beta h}\right),
$$
with scintillation index template
$$
\mathrm{SI}=\frac{1}{\alpha}+\frac{1}{\beta}+\frac{1}{\alpha\beta}
$$
as reported in the corpus [O_ISAC_035].
which steers the main lobe toward $\theta_0$ when phase control is accurate [O_ISAC_008], [O_ISAC_061], [O_ISAC_091]. In practice, finite FoV receivers, spacing-dependent grating-lobe behavior, and channel impairments limit ideal steering gains, so array control and sensing quality must be co-optimized [O_ISAC_061], [O_ISAC_091], [O_ISAC_098].

For pointing jitter with isotropic displacement,
$$
r\sim\text{Rayleigh}(\sigma_s),\qquad h_P = A_0\exp\!\left(-\frac{2r^2}{w_{eq}^2}\right),
$$
which induces
$$
f_{h_P}(h)=\frac{\gamma^2}{A_0^{\gamma^2}}h^{\gamma^2-1},\;0<h\le A_0,\quad \gamma=\frac{w_{eq}}{2\sigma_s},
$$
and moments
$$
\mathbb{E}[h_P^k]=A_0^k\frac{\gamma^2}{\gamma^2+k}.
$$
The mobile OIRS model extends this baseline by non-zero boresight terms governed by refresh-mismatch kinematics [O_ISAC_098].
**Key takeaways and open problems.** OPA evidence is strongest on beam agility and communication-sensing coupling, while ORIS evidence is strongest on alignment robustness and NLoS support [O_ISAC_008], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112]. Across modalities, quantized control, insertion loss, and refresh latency are repeatedly reported as practical bottlenecks [O_ISAC_098], [O_ISAC_127]. A near-term research priority is to report OPA and ORIS gains with a common tuple $(R,\mathrm{BER},\mathrm{CRB},\text{latency})$ under identical geometry and impairment settings [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Another open direction is model-consistent design under quantized ORIS control and nonstationary channels in a single optimization loop [O_ISAC_098], [O_ISAC_127].

Define outage as
$$
P_{out}(\gamma_{th})=\Pr\{\gamma<\gamma_{th}\}.
$$
Under IM/DD with `\gamma=\gamma_0(h_L h_T h_P h_W)^2`,
$$
P_{out}=\int_0^{A_0}
F_{h_T}\!\left(\frac{\sqrt{\gamma_{th}/\gamma_0}}{h_L h_W h_P}\right)
 f_{h_P}(h_P)\,dh_P,
$$
and availability is `1-P_out`. This integration roadmap is consistent with asymptotic outage analyses in the mobile OIRS corpus [O_ISAC_098].
### VI-B. Channel Impairments and Robustness Mechanisms

For sensing, Section-I notation is preserved with `\Delta d \equiv \Delta r_{min}` and
$$
\Delta r_{min} \approx \frac{v}{2B_{eff}},
$$
while estimator variance is Fisher-limited:
$$
\operatorname{Var}(\hat\theta)\ge J^{-1}(\theta),\qquad
\operatorname{Var}(\hat d)\propto \frac{1}{\mathrm{SNR}_{eff}B_{eff}^2}.
$$
Therefore turbulence, pointing, and weather losses jointly reduce `\mathrm{SNR}_{eff}`, degrading both `R` and sensing RMSE/CRB trends [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_011], [O_ISAC_127].
Robustness is a first-order requirement in O-ISAC because the same optical channel impairments degrade communication reliability and sensing fidelity simultaneously. The corpus repeatedly models end-to-end channel gain as a product of deterministic loss, atmospheric or medium turbulence, and pointing/misalignment components [O_ISAC_023], [O_ISAC_035], [O_ISAC_061], [O_ISAC_098], [O_ISAC_199].

A practical robustness-coupling indicator from corpus parameters is
$$
\kappa_{\mathrm{fog/clear}}(D)=10^{-\frac{(\alpha_{fog}-\alpha_{clear})D}{10}}.
$$
Using `\alpha_{fog}=33.98` dB/km and `\alpha_{clear}=0.44` dB/km from [O_ISAC_035],
$$
\kappa_{\mathrm{fog/clear}}(1\,\mathrm{km})\approx 4.43\times10^{-4},
$$
which corresponds to an inferred `\approx 33.54` dB effective SNR penalty (assuming identical transmit/receiver settings).
A compact robustness anchor is

A canonical robust co-design is
$$
\max_{\mathbf{u}}\; \alpha R(\mathbf{u})-(1-\alpha)\sigma_r(\mathbf{u})
H=H_l H_a H_p,
$$
subject to
$$
\Pr\{\gamma(\mathbf{u},\xi)<\gamma_{th}\}\le\varepsilon,\quad
\mathrm{CRB}_d(\mathbf{u})\le\delta,\quad
P_t\le P_{max},\quad
T_{update}\le\tau_c,
P_{\text{out}}=\Pr\!\left(\gamma(H)<\gamma_{\text{th}}\right)\le \varepsilon.
$$
plus hardware constraints (e.g., phase quantization/update limits in RIS controllers). Here `\alpha` controls C\&S priority, while `\varepsilon` and `\tau_c` encode robustness targets directly motivated by quantile-constrained OW-ISAC and coherence-limited adaptive RIS evidence [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127], [O_ISAC_098].

### VI-B.4 Mitigation Mechanisms (System-Level Synthesis)
The evidence-supported mitigation stack is summarized in Table VI-B.2 and can be read as three layers.

First, **statistical robustness at optimization time** substitutes difficult stochastic integrals with risk-aware surrogates (0.05 quantiles), yielding explicit `>95%` communication reliability constraints under turbulence [O_ISAC_023], [O_ISAC_061], [O_ISAC_091].

Second, **control-loop robustness at runtime** is achieved by adaptive beam tracking and predictive RIS control. Mobile OIRS studies show that refresh mismatch directly maps into alignment error and outage/BER loss [O_ISAC_098]; underwater RIS studies report that maintaining end-to-end latency below coherence budgets preserves BER/secrecy stability under non-stationary salinity/turbulence [O_ISAC_127].

Third, **propagation-path robustness by spatial/route diversity** uses IRS-NLoS reconstruction for blocked indoor links [O_ISAC_112], OFDM delay-domain separability for LoS/NLoS discrimination [O_ISAC_009], and MIMO/diversity-plus-compensation for severe weather/pointing scenarios [O_ISAC_199]. Hybrid fallback concepts (optical downlink + RF side link when blocked) are also documented at survey level [O_ISAC_303].

**Coverage limits in current corpus:** adaptive-optics/wavefront-correction gains are largely discussed in references but not reported with standardized O-ISAC cross-metrics in the mined high-confidence set `[TODO: evidence needed]`. Likewise, explicit FEC/interleaving/ARQ gain tables under joint sensing-communication constraints are sparse `[TODO: evidence needed]`.

### VI-B.5 Open Challenges and Research Directions (Actionable)
1. **Standardized robustness reporting contract:** Metric impact is on cross-paper comparability of `P_out`, BER, RMSE, and CRB; evidence is heterogeneous metric planes across [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_009]; direction is a mandatory tuple `{R, BER, P_out, \Delta r_{min}, \sigma_r, CRB, noise model, detection regime}` per experiment.
2. **Composite-fading calibration beyond single-regime fits:** Metric impact is biased outage prediction; evidence is regime switching (lognormal vs Gamma-Gamma) in [O_ISAC_098], [O_ISAC_035], [O_ISAC_199]; direction is hierarchical model selection with online posterior weights over turbulence families.
3. **Pointing model unification with mobility latency:** Metric impact is outage and link continuity; evidence is explicit `\tau_c=|v_u\Delta t-d_o|` degradation in [O_ISAC_098]; direction is to couple kinematic prediction error into closed-form pointing-loss moments.
4. **Chance-constrained design under mixed impairments:** Metric impact is reliability at fixed sensing quality; evidence is 0.05-quantile practice in [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]; direction is distributionally robust optimization over jointly uncertain `{h_T,h_P,h_W}`.
5. **Robust sensing bounds under IM/DD nonlinearities:** Metric impact is `\sigma_r`/CRB realism; evidence is IM/DD noise and clipping-aware models in [O_ISAC_009], [O_ISAC_023], [O_ISAC_011]; direction is Fisher-information derivation with clipping and background-current terms retained.
6. **Blockage-aware topology co-design with optical IRS:** Metric impact is availability/PE in indoor dense environments; evidence is large PE improvements via IRS-NLoS in [O_ISAC_112]; direction is graph-based path redundancy optimization with blockage priors.
7. **Latency-coherence co-design for adaptive RIS controllers:** Metric impact is stale-control BER floors; evidence is coherence/latency coupling in [O_ISAC_127] and refresh sensitivity in [O_ISAC_098]; direction is to optimize policy complexity under hard timing constraints `T_update\le\tau_c`.
8. **Weather-to-SNR transfer functions for planning:** Metric impact is link budgeting and outage forecasting; evidence is large visibility attenuation swing in [O_ISAC_035] and weather-range collapse in [O_ISAC_199]; direction is standardized `\kappa_W` maps tied to meteorological covariates.
9. **Cross-modal robustness transfer (FSO-VLC-UOWC):** Metric impact is generalization and sample efficiency; evidence is modality-specific robust designs in [O_ISAC_023], [O_ISAC_112], [O_ISAC_127]; direction is shared latent impairment embeddings with modality-conditioned decoders.
10. **Joint security-robustness-sensing optimization:** Metric impact is secrecy/BER/RMSE trade-space; evidence is secrecy-aware RIS gains in [O_ISAC_127] and SINR-ISLR tension in [O_ISAC_091], [O_ISAC_061]; direction is tri-objective Pareto design with outage and CRB chance constraints.
11. **Diversity order interpretation for optical ISAC datasets:** Metric impact is asymptotic reliability claims; evidence is asymptotic BER/outage derivations in [O_ISAC_098] and diversity gains in [O_ISAC_199]; direction is dataset-backed estimation of effective diversity order under non-i.i.d. impairments.
12. **Hybrid fallback protocol benchmarks:** Metric impact is service continuity under optical blockage; evidence is hybrid VLC-RF fallback discussion in [O_ISAC_303]; direction is benchmark suites with switching latency, sensing degradation, and throughput loss jointly reported.
This chance-constraint view links physical impairment statistics directly to reliability targets and is consistent with quantile-robust formulations used in optical ISAC optimization studies [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Practical mitigation then combines statistical robustness at design time with runtime adaptation (tracking, refresh control, and environment-aware reconfiguration) [O_ISAC_098], [O_ISAC_112], [O_ISAC_127], [O_ISAC_199].

**VI-B takeaway.**
The literature converges on a clear message: O-ISAC robustness must be modeled as a composite channel problem where turbulence, pointing, weather/blockage, and receiver noise interact multiplicatively rather than additively. Across FSO, OPA, OIRS, VLC, and UOWC studies, outage and sensing degradation are both driven by the same effective-SNR contraction, so communication-only robustness tuning is insufficient. Quantile-robust optimization and latency-aware adaptive control are the two most consistent mechanisms that already show evidence-backed gains in current prototypes. Path diversity mechanisms (IRS-NLoS, MIMO, hybrid fallback) provide additional protection, but their gains are reported with non-uniform metrics and scenario definitions. The structurally weak point of the field is therefore not model availability, but comparability: standardized impairment-aware reporting and cross-modal benchmark design remain underdeveloped.
**Key takeaways and open problems.** Turbulence, weather attenuation, and pointing jitter are now well represented in single-paper evaluations, but cross-paper outage definitions remain heterogeneous [O_ISAC_023], [O_ISAC_035], [O_ISAC_061], [O_ISAC_199]. Current evidence supports robustness-aware design, yet common reporting of confidence intervals and unified $P_{\text{out}}$ protocols is still limited [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. A concrete open problem is distributionally robust co-design that jointly handles $(H_a,H_p)$ uncertainty while preserving sensing CRB targets [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Another open problem is latency-coherence-aware robustness control in dynamic ORIS loops [O_ISAC_098], [O_ISAC_127].

**TODO (VI-B missing evidence / metrics)**
- `[TODO: evidence needed]` Direct O-ISAC papers with quantitative adaptive-optics/wavefront-correction gains (same-table BER/RMSE/latency) were not found in the high-confidence VI-B set.
- `[TODO: evidence needed]` Explicit FEC/interleaving/ARQ gain curves jointly tied to sensing metrics (`\sigma_r` or CRB) are sparse.
- `[TODO: evidence needed]` Availability targets (e.g., 99.9%) are rarely reported with unified outage definitions and confidence intervals.
- `[TODO: evidence needed]` Some robustness results remain figure-level; machine-readable point extraction is needed for strict meta-analysis.
### VI-C. Joint Co-Design and Resource Optimization

---
Joint co-design is needed because waveform, beam, and ORIS controls are coupled through shared physical constraints. In O-ISAC implementations with IM/DD links, feasible signaling must satisfy nonnegativity and optical power limits, which changes both algorithm design and achievable tradeoff surfaces [O_ISAC_009], [O_ISAC_023], [O_ISAC_054], [O_ISAC_061]. Model VI-U provides the shared variable structure for transmitter, ORIS, and sensing terms [O_ISAC_061], [O_ISAC_091], [O_ISAC_127].

**VI-C Artifact Map**
- `ROOT_DIR`: `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST`
- **Step-0 alignment source**: `drafts/section_01_introduction.md`
  - Reused Section I notation: `B_eff`, `R`, `\Delta r_{min}`, `\sigma_r`, `\mathrm{SNR}`, `\mathrm{BER}`, `\alpha`, `\mathrm{CRB}`.
  - Reused taxonomy boundaries: Fiber, FSO, VLC/LiFi, Photo-THz.
- **TOC/scope detection artifact**: `review_package/surveyOutline.md`
  - `VI-C` is not explicitly titled in this outline scan; therefore, the user-specified VI-C scope is used: joint co-design and resource optimization for O-ISAC.
- **Primary corpus files for VI-C evidence (models/problem formulations/metrics):**
  - `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md` (FSO DCO-OFDM; communication-centric and sensing-centric joint power allocation; Fisher-information metric; KKT/BCD).
  - `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md` (OPA-OW-ISAC joint optimization of precoding and PD orientations; SDR/LP/BCD; complexity and trade-offs).
  - `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md` (OPA-OW-ISAC compact SINR-ISLR optimization; SDR/LP trade-off).
  - `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md` (LSTM-DRL-NSGA-II multi-objective RIS-UOWC; Pareto and latency-complexity metrics).
  - `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md` (VLPC-DCO-OFDM; IM/DD and DC-bias constraints; sensing-aided CSI; pilot overhead).
  - `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md` (LED O-ISAC two-phase optimization: source layout + radiation pattern; shared intensity objective).
  - `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md` (OCDM-FMCW waveform/resource split; guard-band and rate-range trade-off; PAPR discussion).
  - `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md` (OIRS wide/narrow beam partition and closed-loop control; `S_w/S_n` trade-off).
  - `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md` (IRS fingerprint localization; two-step strategy; complexity-accuracy trade-off).
  - `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md` (retroreflective OFDM O-ISAC; communication BER vs sensing RMSE trade-off through correlation length).
  - `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md` (joint waveform and GA-based array thinning design in OPA ISAC).
- **Extraction/analysis artifacts used for indexing and cross-checking:**
  - `analysis/VI_ev_v2/section6A_evidence.csv`
  - `analysis/VI_ev_v2/section6D_evidence.csv`
  - `analysis/VI_ev_v2/section6B_opa_metrics.csv`
  - `analysis/VI_ev_v2/section6C_ris_metrics.csv`
  - `analysis/VI_ev_v2/retrieval_hits.jsonl`
  - `data/ext_res_v4/O_ISAC_023_v4.json`
  - `data/ext_res_v4/O_ISAC_061_v4.json`
  - `data/ext_res_v4/O_ISAC_091_v4.json`
  - `data/ext_res_v4/O_ISAC_127_v4.json`
  - `data/ext_res_v4/O_ISAC_009_v4.json`
- **Ranked VI-C candidate paper_ids (with one-line rationale):**
  1. `O_ISAC_023` - Explicit dual-objective resource-allocation formulation with KKT, BCD, and Fisher-information coupling.
  2. `O_ISAC_061` - Joint precoder/receiver-orientation optimization with SDR/LP/BCD and quantified complexity.
  3. `O_ISAC_091` - Clear SINR-ISLR trade-off formulation and solver-level comparison.
  4. `O_ISAC_127` - Multi-objective Pareto optimization with explicit latency/coherence constraints and complexity classes.
  5. `O_ISAC_054` - Two-phase optical co-design with analytic optimization (layout and radiation pattern).
  6. `O_ISAC_009` - IM/DD-safe OFDM co-design with pilot-overhead and sensing-assisted communication decoding.
  7. `O_ISAC_035` - Explicit rate-range trade-off via guard-band/resource split in OCDM-FMCW.
  8. `O_ISAC_098` - Closed-loop OIRS partition/control variables linking sensing and communication power.
  9. `O_ISAC_112` - Optimization-driven weighting/two-step localization with complexity formulas.
  10. `O_ISAC_008` - Joint waveform + GA-optimized OPA array design with reported C&S performance.
  11. `O_ISAC_011` - Parameter-level C&S trade-off via cross-correlation depth and BER/RMSE behavior.

**VI-C Evidence Table**

| claim_id | claim | paper_id(s) | excerpt (<=2 sentences) | locator (heading + line range or page) | extracted variables/metrics |
|---|---|---|---|---|---|
| VC01 | FSO DCO-OFDM O-ISAC uses explicit joint C&S power-allocation formulations. | O_ISAC_023 | "joint power allocation problems are formulated for both communication-centric and sensing-centric scenarios." | `O_ISAC_023.md:5-7` (Abstract) | objective classes, `b`, subcarrier power |
| VC02 | IM/DD imposes real and nonnegative constraints and introduces DC-bias/clipping design variables. | O_ISAC_023 | "an optical waveform based on IM/DD is restricted to being real and nonnegative... DC bias becomes a critical parameter." | `O_ISAC_023.md:31-33` (Introduction) | nonnegativity, `b`, clipping level |
| VC03 | Sensing metric is estimation-theoretic (Fisher information/CRB linkage). | O_ISAC_023 | "The Fisher information... sensing precision can approach CRB asymptotically." | `O_ISAC_023.md:231-245` (Theorem 2) | Fisher information, CRB |
| VC04 | Robust optimization is enforced by 0.05 lower-quantile replacement to meet >95% target reliability. | O_ISAC_023 | "substitute... with the 0.05-lower quantile... performance can be obtained at a probability of more than 95%." | `O_ISAC_023.md:262-263` (Sec. III simplification) | quantile `q=0.05` |
| VC05 | The joint problem is nonconvex and solved by decomposition + BCD. | O_ISAC_023 | "joint optimization ... is nonconvex... decomposed... BCD algorithm." | `O_ISAC_023.md:334-336` (Sec. III-B/C) | decomposition, BCD |
| VC06 | KKT/water-filling structure yields explicit trade-off operating cases. | O_ISAC_023 | "optimal solution ... iff KKT conditions hold... tradeoff exist between communication and sensing metrics." | `O_ISAC_023.md:392-427` (Sec. III-C) | KKT, water-filling, dual variables |
| VC07 | OPA-OW-ISAC formulates joint optimization over precoding and PD orientations. | O_ISAC_061 | "The joint optimization problem of precoding matrices and PD orientations is formulated..." | `O_ISAC_061.md:45` (Contributions) | `W`, `\phi` |
| VC08 | Direct detection and shot/thermal noise are explicit optical constraints in beamforming design. | O_ISAC_061 | "OW-ISAC ... adopts direct detection" and "noise term arises from shot noise and thermal noise." | `O_ISAC_061.md:36`, `O_ISAC_061.md:101-117` | DD model, noise terms |
| VC09 | Communication QoS is encoded as SINR thresholds after quantile robustification. | O_ISAC_061 | "0.05-lower quantile ... >95%" and "SINR ... should exceed a threshold." | `O_ISAC_061.md:346-357` (Sec. IV-A) | `\Gamma_k`, quantile-SINR coupling |
| VC10 | Solver complexity and convergence behavior are quantified for implementability. | O_ISAC_061 | "objective values converge within 3 iterations" and complexity expressions for PEP/TP/LP are provided. | `O_ISAC_061.md:548`, `O_ISAC_061.md:594-600` (Sec. IV-D/V-A) | complexity classes, iteration counts |
| VC11 | Increasing communication SINR constraints degrades sensing-side metrics (trade-off). | O_ISAC_061 | "increased demand for light-field SINR... contrast metrics deteriorate" and ISLR worsens with SINR. | `O_ISAC_061.md:600`, `O_ISAC_061.md:612-618` (Sec. V) | SINR-ISLR trade-off |
| VC12 | Conference OPA formulation optimizes sensing metric under communication QoS constraints. | O_ISAC_091 | "optimization ... optimizes the sensing performance metric under the constraint of communication quality." | `O_ISAC_091.md:17`, `O_ISAC_091.md:181` | objective/constraint split |
| VC13 | SDR and LP produce a complexity-performance trade-off in OW-ISAC precoding. | O_ISAC_091 | "LP ... lower complexity ... sub-optimal" and LP suffers DoF loss with performance deterioration. | `O_ISAC_091.md:261`, `O_ISAC_091.md:275-285` | SDR vs LP, DoF loss |
| VC14 | RIS-UOWC adopts explicit multi-objective co-design with LSTM+DRL+NSGA-II. | O_ISAC_127 | "LSTM... DRL... NSGA-II multi-objective optimization" balancing BER, secrecy, and energy. | `O_ISAC_127.md:39`, `O_ISAC_127.md:260-262` | multi-objective variables, rewards |
| VC15 | Pareto fronts quantify secrecy-energy trade-offs with nontrivial operating points. | O_ISAC_127 | "NSGA-II ... Pareto front... 22.2% reduction in power ... <3% secrecy loss." | `O_ISAC_127.md:487-497` (Fig.6 discussion) | secrecy rate, energy saving |
| VC16 | Real-time feasibility is tied to latency/coherence and computational complexity. | O_ISAC_127 | "complexity `O(T n_h^2)` ... `O(NP^2)`... end-to-end 47.3 ms within coherence window." | `O_ISAC_127.md:501-511` | complexity, 47.3 ms latency |
| VC17 | VLPC-DCO-OFDM enforces IM/DD positivity and DC-bias/clipping behavior. | O_ISAC_009 | "IM/DD ... requires real- and positive-valued signals" and "DC bias ... clipped at zero." | `O_ISAC_009.md:29`, `O_ISAC_009.md:237` | positivity, `\eta_0`, clipping |
| VC18 | A single OFDM pilot jointly serves sensing and CSI estimation, reducing overhead. | O_ISAC_009 | "only a single OFDM pilot symbol is required" for delay-domain sensing and CSI support. | `O_ISAC_009.md:53`, `O_ISAC_009.md:577` | pilot overhead |
| VC19 | LED O-ISAC defines a shared utility via received intensity for both communication and sensing. | O_ISAC_054 | "we can work toward optimizing ... with a shared objective" and maximize summed received intensity. | `O_ISAC_054.md:306-308` | shared objective `\sum I^{rx}` |
| VC20 | Two-phase optimization is explicit: source-layout optimization and radiation-pattern optimization. | O_ISAC_054 | "we formulated two optimization problems across these phases" (layout and beamformed radiation pattern). | `O_ISAC_054.md:44-49`, `O_ISAC_054.md:685` | `\varepsilon,\xi_m,R(\varphi_m)` |
| VC21 | OCDM-FMCW allocates guard-band/power resources, inducing an explicit rate-range trade-off. | O_ISAC_035 | "ranging distance and communication capacity are inversely related... linear to guard-band length." | `O_ISAC_035.md:265-275` | `N_{GB}`, `R_max`, `C` |
| VC22 | OIRS partition variables (`S_w/S_n`) create direct sensing-communication power trade-offs. | O_ISAC_098 | "wide beam and narrow beam" region control and "relative proportion of `S_n` and `S_w` makes a trade-off." | `O_ISAC_098.md:59-70`, `O_ISAC_098.md:332` | `S_w/S_n`, BER/outage |
| VC23 | IRS fingerprint localization uses optimization-based weighting and complexity-accounted two-step strategy. | O_ISAC_112 | "two-step localization strategy" with complexity formulas and PE improvements. | `O_ISAC_112.md:359-371`, `O_ISAC_112.md:443-445` | FLOPs expressions, PE |
| VC24 | Retroreflective OFDM O-ISAC exhibits sensing-noise robustness via correlation-length tuning. | O_ISAC_011 | "more samples used ... lower distance RMSE" while BER curves are separately characterized. | `O_ISAC_011.md:145-155` | RMSE vs symbol number |

**Table VI-C.1. O-ISAC Co-Design Problem Formulations in Optical Literature**

| paper_id | objective(s) | constraints | variables | sensing metric used | comm metric used | solution method |
|---|---|---|---|---|---|---|
| O_ISAC_023 | Communication-centric and sensing-centric joint resource allocation | sensing precision / communication QoS, nonnegativity, total power | DC bias `b`, subcarrier powers `\tilde P(k)` | Fisher information, CRB-linked precision | spectral efficiency, SNDR | decomposition + BCD + KKT/dual iterations |
| O_ISAC_061 | maximize contrast (or minimize ISLR) under communication QoS | SINR thresholds, power constraints, DD model | precoding covariance, PD orientations | contrast / ISLR / RMSE | light-field SINR, BER | SDR/SDP, LP simplification, barrier method, BCD |
| O_ISAC_091 | optimize sensing metric under comm-quality constraints | SINR threshold, power budget, PSD/rank constraints | precoding matrices | ISLR | SINR | SDR and LP formulations |
| O_ISAC_127 | multi-objective secure/energy-efficient adaptive RIS control | latency `<\tau_c`, power budget, quantized phase control | RIS phases, policy actions, NSGA population | robustness proxy via BER/noise resilience | secrecy rate, BER, energy | LSTM prediction + DRL + NSGA-II Pareto refinement |
| O_ISAC_009 | sensing-aided communication with joint radar-CSI workflow | IM/DD positivity, DC bias, pilot structure | OFDM parameters, pilot, `\eta_0` | ranging RMSE, LoS/NLoS resolvability | BER, data rate | algorithmic co-design (Radar-CE + hybrid Radar-RSS) |
| O_ISAC_054 | phase-1 source layout + phase-2 radiation-pattern optimization | LED physical/incoherence constraints, target geometry | O-AP coordinates, radiation pattern, lens profile | positioning MSE | BER / equivalent gain | theorem-driven closed-form approximations (P1/P2) |
| O_ISAC_035 | joint waveform/resource split between sensing and communication subcarriers | guard-band feasibility (`B_GB/2>f_b`), FSO impairments | guard-band length, subcarrier power, symbol period | ranging accuracy / beat-frequency quality | EVM, BER, capacity | parametric optimization and trade-off analysis |
| O_ISAC_098 | closed-loop OIRS partition and alignment design for mobile O-ISAC | tracking refresh, pointing/turbulence effects, IM/DD-OOK | `S_w/S_n`, deflection angle, refresh interval | positioning error via beam alignment term `\tau_c` | BER, outage | closed-form analysis + feedback control design |
| O_ISAC_112 | fingerprint-localization co-design with IRS and weighted estimators | offline/online complexity, IRS deployment geometry | weight vectors, KNN size `K`, fingerprint tensor | positioning error (PE) | RSS-related link quality | DE-WI / WKNN + two-step strategy |
| O_ISAC_008 | joint waveform and thinned-array design | steering/SMSR and hardware structure constraints | waveform parameters, ring-element positions | ranging accuracy / beam resolution | BER, data rate | GA-based array optimization + joint waveform design |
| O_ISAC_011 | passive ranging-communication integration with OFDM | sampling/range constraints, modulation choices | symbol length for cross-correlation, ADC rates | RMSE, `\Delta d` | BER | heuristic parameter sweep with diversity-assisted link |

**Table VI-C.2. Algorithm Families vs Trade-Off Outcomes**

| algorithm family | representative paper_ids | guarantee type | complexity / runtime evidence | required channel-state knowledge | reported trade-off outcomes |
|---|---|---|---|---|---|
| Convex SDR/SDP | O_ISAC_061, O_ISAC_091 | convex-relaxation upper bound; rank-1 recovery via randomization | `O((K+1)^{3.5}N_t^7\log(1/\varepsilon_R))` (O_ISAC_061) | channel/beam model + QoS thresholds | better sensing-comm frontier than LP, but heavier complexity |
| LP simplification | O_ISAC_061, O_ISAC_091 | feasible lower-complexity sub-optimal solution | lower than SDP; reported low-iteration practical operation | reduced structural channel knowledge | easier implementation with measurable performance loss (e.g., ~7 dB in cited scenario) |
| Alternating/BCD | O_ISAC_023, O_ISAC_061 | monotonic empirical convergence (no global proof in these implementations) | geometric-like residual decay; few outer iterations in simulations | iterative updates of coupled variables | practical handling of nonconvex coupling (`b` vs `P(k)`, `W` vs `\phi`) |
| KKT + dual iteration / water-filling | O_ISAC_023 | optimality for convex subproblems under KKT conditions | bisection/log-scale iteration terms; per-subcarrier `O(N)` terms | subcarrier-level SNDR/constraint parameters | explicit communication-sensing trade-off cases (water-filling vs sensing-prioritized allocations) |
| Evolutionary multi-objective (NSGA-II/GA/DE-WI) | O_ISAC_127, O_ISAC_008, O_ISAC_112 | Pareto-set search, no global optimality guarantee | NSGA-II part scales as `O(NP^2)` (O_ISAC_127); DE-WI depends on iteration/population (O_ISAC_112) | scenario observations + fitness functions | directly reveals Pareto fronts and complexity-accuracy trade-offs |
| Learning-assisted control | O_ISAC_127 | policy convergence is empirical in reported setup | `O(Tn_h^2)` for LSTM + DRL stage; 47.3 ms loop (O_ISAC_127) | predicted environment states + online rewards | robust adaptation under fast channel variation; secrecy/BER/energy balancing |
| Closed-form geometric optimization | O_ISAC_054 | theorem-based approximations under model assumptions | low online burden after offline parameterization | geometry/radiation model parameters | large BER/MSE gains through phase-1/phase-2 design separation |
| Heuristic parametric co-tuning | O_ISAC_035, O_ISAC_011, O_ISAC_098 | no formal global guarantee | low to moderate; simulation-driven sweeps | partial CSI/geometry and operating-point data | transparent engineering trade-offs (`N_GB`, symbol length, `S_w/S_n`) |
| ADMM / manifold methods in optical O-ISAC | [TODO: evidence needed] | [TODO: evidence needed] | [TODO: evidence needed] | [TODO: evidence needed] | [TODO: evidence needed] |

## VI-C. Joint Co-Design and Resource Optimization for O-ISAC (Waveform/Beam/Time-Frequency/Power Trade-Offs)

### VI-C.1 Motivation: Why Co-Design Is the Enabling "Brain" of O-ISAC
The corpus indicates that naive separation of communication and sensing is structurally suboptimal once both functions share optical power, bandwidth, and hardware states [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_054]. In FSO DCO-OFDM, communication-centric and sensing-centric formulations are both necessary because a single allocation policy cannot preserve spectral efficiency and sensing precision across all operating points [O_ISAC_023]. In OPA-OW-ISAC, raising communication SINR thresholds reallocates spatial resources and worsens sensing-side sidelobe/contrast indicators, revealing a coupled Pareto surface rather than independent objectives [O_ISAC_061], [O_ISAC_091]. LED-based O-ISAC also confirms coupling in intensity-domain physics: both communication BER and sensing MSE are improved by maximizing received intensity under jointly designed source geometry and radiation patterns [O_ISAC_054]. Multi-objective RIS-UOWC results further show that secrecy, BER, and energy cannot be optimized independently in dynamic channels, and that explicit Pareto control is required [O_ISAC_127].

### VI-C.2 Problem Taxonomy in Optical O-ISAC
We classify co-design problems by decision variables and by utility families.

1. **Waveform and time-frequency resource variables.**
   DCO-OFDM and OCDM-FMCW studies optimize DC bias, subcarrier powers, guard-band widths, and symbol periods to balance ranging and communication capacity [O_ISAC_023], [O_ISAC_035], [O_ISAC_009].

2. **Beam/phase and spatial variables.**
   OPA/OIRS works optimize precoding covariances, PD orientations, and surface partition variables (`S_n/S_w`) for concurrent imaging/localization and link quality [O_ISAC_061], [O_ISAC_091], [O_ISAC_098].

3. **Power-split and operating-phase variables.**
   Two-phase LED O-ISAC separates global discovery and directional service, with explicit optimization of source layout (phase-1) and radiation profile (phase-2) [O_ISAC_054].

4. **Pilot/overhead variables.**
   VLPC-DCO-OFDM reports a one-pilot design serving both sensing and CSI support, exposing a pilot-overhead vs estimation-fidelity trade-off [O_ISAC_009].

5. **Algorithmic control variables under nonstationarity.**
   RIS-UOWC introduces predictive control parameters (LSTM state, DRL policy actions, NSGA-II population) constrained by coherence time and actuation latency [O_ISAC_127].

By objective family, the literature uses (i) information-theoretic communication utilities (rate/SINR/SNDR), (ii) estimation-theoretic sensing utilities (Fisher information, CRB, RMSE), and (iii) mixed utilities where sensing contrast or localization error is optimized under communication QoS constraints [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_112].
A minimal feasible set and objective anchor are

### VI-C.3 Unified Analytical Framework and Fundamental Limits
Let the aggregate design vector be
$$
\mathbf{u} := \{\mathbf{W},\boldsymbol{\phi},b,\mathbf{P},N_{GB},T_{sym},\mathbf{\Theta},\eta_0,S_n/S_w,\tau_{update}\}.
$$
To remain modality-consistent, we use a two-regime signal template.

For coherent/field-centric formulations:
$$
\mathbf{y}_c = \mathbf{H}(\mathbf{u})\mathbf{x} + \mathbf{n},
\qquad
\mathbf{y}_s = \mathbf{G}(\mathbf{u})\mathbf{s}(\boldsymbol{\theta}) + \mathbf{v}.
$$
For IM/DD-dominant optical links:
$$
y = h(\mathbf{u})x + n,\qquad x\ge 0,
$$
with practical constraints from DCO-OFDM and DD receivers (real/nonnegative signaling, DC bias, clipping distortion, shot/thermal/background noise) [O_ISAC_023], [O_ISAC_009], [O_ISAC_061], [O_ISAC_091], [O_ISAC_011].

A generic scalarized trade-off is
$$
\max_{\mathbf{u}\in\mathcal{U}}\; \alpha\,\mathcal{C}(\mathbf{u}) + (1-\alpha)\,\mathcal{S}(\mathbf{u}),\quad \alpha\in[0,1],
\mathcal U=\{x(t):x(t)\ge 0,\;\mathbb{E}[x(t)]\le \bar P,\;\max_t x(t)\le P_{\max}\},
$$
where
$$
\mathcal{C}(\mathbf{u}) = R(\mathbf{u})
\approx B_{eff}\log_2\!\big(1+\mathrm{SNR}_{eff}(\mathbf{u})\big)
\max_{\mathbf{w},\Theta,\,x\in\mathcal U}\;\alpha R(\mathbf{w},\Theta)-(1-\alpha)\,\mathrm{CRB}(\mathbf{w},\Theta),\quad \alpha\in[0,1].
$$
and
$$
\mathcal{S}(\mathbf{u})\in\{J(\boldsymbol{\theta};\mathbf{u}),\,-\mathrm{CRB}(\boldsymbol{\theta};\mathbf{u}),\,-\sigma_r(\mathbf{u}),\,-\mathrm{ISLR}(\mathbf{u})\}.
$$
The estimation backbone is
$$
\mathbf{J}(\boldsymbol{\theta};\mathbf{u})
=\mathbb{E}\!\left[\nabla_{\boldsymbol{\theta}}\log p(\mathbf{y}|\boldsymbol{\theta},\mathbf{u})\,\nabla_{\boldsymbol{\theta}}\log p(\mathbf{y}|\boldsymbol{\theta},\mathbf{u})^{\!\top}\right],
\qquad
\mathrm{CRB}(\boldsymbol{\theta};\mathbf{u})=\mathbf{J}^{-1}(\boldsymbol{\theta};\mathbf{u}),
$$
and range resolution keeps the Section-I convention
$$
\Delta r_{\min}\approx \frac{v}{2B_{eff}}.
$$
Hence
$$
\sigma_r^2(\mathbf{u})\propto \frac{1}{\mathrm{SNR}_{eff}(\mathbf{u})B_{eff}^2}
$$
as a template consistent with Fisher-information based formulations [O_ISAC_023] and RMSE trends in OPA/VLC studies [O_ISAC_061], [O_ISAC_009], [O_ISAC_011].

A practical feasible set is
$$
\mathcal{U}=\Big\{\mathbf{u}:\;x\ge 0,\;\mathbb{E}[x]\le P_{avg},\;x\le P_{peak},\;\eta_0\ge\eta_{0,min},\;\tau_{update}\le\tau_c,\;\phi_i\in\mathcal{Q}_b,\;\gamma_k\ge\Gamma_k,\;\Pi_{pilot}\le\Pi_{max}\Big\},
$$
where nonnegativity and bias constraints are from IM/DD implementations [O_ISAC_023], [O_ISAC_009], quantized RIS constraints are reported in underwater adaptive RIS implementations [O_ISAC_127], and QoS-SINR constraints are explicit in OPA studies [O_ISAC_061], [O_ISAC_091]. Eye-safety explicit thresholds are not uniformly reported in the VI-C core set `[TODO: evidence needed]`.

Two canonical optimization archetypes follow directly.

1. **Weighted-sum form**
$$
\max_{\mathbf{u}\in\mathcal{U}}\; \alpha R(\mathbf{u})-(1-\alpha)\,\mathrm{CRB}_d(\mathbf{u}).
$$

2. **Constrained form**
$$
\max_{\mathbf{u}\in\mathcal{U}}\;R(\mathbf{u})
\quad\text{s.t.}\quad \mathrm{CRB}_d(\mathbf{u})\le \delta.
$$

When the decomposed subproblem is convex (e.g., subcarrier allocation under affine constraints), KKT conditions yield closed-form or water-filling-like updates [O_ISAC_023]. When transmitter and receiver variables are bilinearly coupled (`\mathbf{W}` and `\boldsymbol{\phi}`), alternating/BCD updates are used in practice [O_ISAC_061], [O_ISAC_091]. For nonstationary channels and three-objective settings (secrecy/BER/energy), Pareto evolutionary search and learning-assisted control are used [O_ISAC_127].

### VI-C.4 Algorithmic Landscape and Comparative Synthesis
Table VI-C.1 and Table VI-C.2 indicate three stable trends.

First, the strongest analytical rigor appears in **structured convex-decomposition families**. DCO-OFDM FSO co-design derives explicit KKT regimes and BCD loops with interpretable trade-off curves [O_ISAC_023]. OPA beamforming co-design provides SDR/LP formulations with quantified complexity and explicit SINR-sensing trade-offs [O_ISAC_061], [O_ISAC_091].

Second, **optical-specific constraints are decisive**. IM/DD nonnegativity, DC bias, and clipping terms reshape feasible waveform sets and make direct transfer of RF formulations invalid without modification [O_ISAC_023], [O_ISAC_009], [O_ISAC_054]. In dynamic channels, latency and coherence constraints become hard optimization constraints rather than post-hoc implementation checks [O_ISAC_127], [O_ISAC_098].

Third, **implementability and theory are not aligned by default**. SDR-quality solutions can be expensive; LP and heuristic reductions improve deployability but may lose sensing or communication margins [O_ISAC_061], [O_ISAC_091]. Evolutionary and learning-assisted methods improve adaptability and Pareto exploration, yet formal global guarantees are generally absent in reported optical studies [O_ISAC_127], [O_ISAC_112], [O_ISAC_008].

A practical interpretation is therefore: "theory-only" approaches are those requiring heavy SDP/randomization loops or full-state assumptions; "deployable" approaches are those with bounded control latency, reduced feedback burden, and explicit hardware-compatible constraints. The corpus currently reports both classes, but with non-uniform metric contracts.

### VI-C.5 Open Challenges and Research Directions (Actionable)
1. **Unified optical co-design metric contract is missing.**
   Why it matters: inconsistent metrics prevent reproducible Pareto comparison (`R`, BER, `\sigma_r`, CRB, latency). Evidence: O_ISAC_023 reports that \"joint power allocation problems are formulated for both communication-centric and sensing-centric scenarios,\" while O_ISAC_061/091 optimize SINR-ISLR and O_ISAC_054 uses a shared intensity objective. Hypothesis: define a mandatory tuple `{R, BER, \Delta r_{min}, \sigma_r, CRB, complexity, latency, feedback overhead}` and benchmark all VI-C algorithms on that tuple.

2. **Robust co-design under imperfect CSI/SSI remains weakly formalized.**
   Why it matters: QoS and sensing can collapse when channel statistics drift. Evidence: O_ISAC_023 and O_ISAC_061 explicitly \"substitute ... with the 0.05-lower quantile\" so performance is guaranteed at probability above 95%. Hypothesis: distributionally robust multi-objective design with ambiguity sets on turbulence/pointing states.

3. **IM/DD-safe waveform families need explicit co-design theory.**
   Why it matters: clipping and positivity constraints bias both communication and sensing estimators. Evidence: O_ISAC_023 states optical IM/DD waveforms are \"real and nonnegative,\" and O_ISAC_009 reports \"DC bias ... clipped at zero.\" Hypothesis: derive constrained mutual-information/Fisher joint bounds for clipped IM/DD OFDM families.

4. **Pilot-overhead vs sensing freshness trade-off is underreported.**
   Why it matters: pilot cost reduces throughput and stale sensing degrades tracking. Evidence: O_ISAC_009 reports that \"only a single OFDM pilot symbol is required\" for dual sensing/CSI use. Hypothesis: optimize pilot periodicity jointly with prediction error dynamics and QoS constraints.

5. **Complexity-aware real-time optimization is not standardized.**
   Why it matters: high-quality formulations may be infeasible on edge hardware. Evidence: O_ISAC_061 gives high-order SDP complexity forms, while O_ISAC_127 reports complexity `O(Tn_h^2)`/`O(NP^2)` and 47.3 ms loop latency. Hypothesis: add complexity and runtime as explicit constraints in the primary optimization problem.

6. **Quantized RIS/OPA control needs estimation-aware analysis.**
   Why it matters: finite control resolution shifts both SNR and sensing error floor. Evidence: O_ISAC_127 uses RIS phase settings with \"5-bit quantization control,\" whereas O_ISAC_061/091 optimize continuous-like beamforming variables. Hypothesis: derive CRB and rate penalties as functions of quantization bits and update intervals.

7. **Cross-modal transfer (FSO/VLC/UOWC) is still limited.**
   Why it matters: siloed algorithms hinder reuse and benchmarking. Evidence: O_ISAC_035 highlights FSO rate-range allocation, O_ISAC_009/054 emphasize VLC IM/DD constraints, and O_ISAC_127 targets underwater dynamics/coherence windows. Hypothesis: modality-conditioned meta-optimization with shared latent design variables.

8. **Security-rate-sensing tri-objective design is immature in optics.**
   Why it matters: secrecy optimization can reallocate resources away from sensing fidelity. Evidence: O_ISAC_127 reports an NSGA-II \"Pareto front\" for secrecy-energy trade-offs, while O_ISAC_061/091 report SINR-ISLR anti-correlation. Hypothesis: formulate tri-objective chance-constrained problems with explicit CRB and secrecy constraints.

9. **Model-to-hardware mismatch remains a major risk.**
   Why it matters: simulation-optimal policies may fail under hardware drift. Evidence: O_ISAC_127 reports \"37.5 \\mu s per element\" and end-to-end latency budgets, and O_ISAC_035 ties feasible performance to guard-band and bandwidth settings. Hypothesis: hardware-in-the-loop calibration terms should be embedded into solver objectives.

10. **PAPR-aware optical co-design needs stronger integration with C&S objectives.**
   Why it matters: high PAPR affects linearity and may bias sensing and BER outcomes. Evidence: O_ISAC_035 explicitly states PAPR behavior and discusses PAPR-reduction implications for practical devices. Hypothesis: include PAPR penalties in weighted-sum co-design with BER/CRB constraints.

11. **Spatial partition co-design (wide/narrow beams) lacks principled optimization under mobility.**
   Why it matters: `S_w/S_n` directly shifts sensing accuracy and communication power. Evidence: O_ISAC_098 states that the \"relative proportion of `S_n` and `S_w` will make a trade-off\" between communication and positioning. Hypothesis: dynamic partition control via receding-horizon optimization with mobility prediction.

12. **Offline-online complexity trade-off for fingerprint/learning methods needs rigorous budgets.**
   Why it matters: high offline complexity and large databases impede scalable deployment. Evidence: O_ISAC_112 provides explicit FLOPs forms and two-step localization gains, while O_ISAC_127 reports module-level runtime budgets for real-time loops. Hypothesis: jointly optimize database granularity, inference complexity, and localization/sensing error under fixed compute envelopes.

**VI-C takeaway.**
The literature converges on the need for explicit joint optimization, because communication and sensing utilities in optical systems are coupled through shared waveform, beam, and power states. The most mature formulations are currently convex-decomposition and SDR/LP-based frameworks, while adaptive learning and evolutionary methods provide stronger nonstationary robustness but weaker formal guarantees. IM/DD constraints (nonnegativity, bias, clipping, DD noise) are not peripheral details; they are central to feasible co-design spaces and must be represented explicitly in objective and constraint sets. Current results already show measurable Pareto structures (rate-sensing, secrecy-energy, complexity-performance), yet cross-paper comparability remains weak due to heterogeneous metric contracts. Progress in VI-C will depend on moving from isolated solver demonstrations to latency-bounded, hardware-aware, and benchmark-standardized co-design pipelines.

**TODO (VI-C missing evidence / metrics)**
- `[TODO: evidence needed]` Optical O-ISAC papers with ADMM/manifold formulations and reproducible complexity-accuracy trade-off tables were not found in the high-confidence VI-C subset.
- `[TODO: evidence needed]` Unified reporting of feedback overhead (bits/s or symbols/frame) is sparse across OPA/RIS co-design papers.
- `[TODO: evidence needed]` Eye-safety constraints are often implicit in hardware settings but rarely encoded as explicit optimization constraints with numeric limits.
- `[TODO: evidence needed]` Several results are figure-level without machine-readable numeric points (especially Pareto and BER-RMSE curves), limiting strict meta-analysis.
- `[TODO: evidence needed]` Cross-paper CRQ-style co-design indicators (`R/\Delta r_{min}` under identical definitions) are insufficiently reported for robust normalization.

---

**VI-D Artifact Map**
- `ROOT_DIR`: `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST`
- **Alignment source (notation/taxonomy):** `drafts/section_01_introduction.md`
  - Preserved symbols and metrics: `B_eff`, `R`, `\Delta r_{min}`, `\sigma_r`, `SNR`, `BER`, `CRB`, `\mathrm{CRQ}_{\Delta}`.
  - Preserved modality taxonomy: Fiber, FSO, VLC/LiFi, Photo-THz.
- **Scope/TOC detection:**
  - `review_package/surveyOutline.md` contains an older Section-VI scheme (`VI-D` appears as `AI/ML in O-ISAC` in that file).
  - Current draft structure (`VI-A/B/C`) already follows the new user-defined decomposition; therefore this VI-D is instantiated as: **Prototyping, Experimental Validation, Benchmarking, and Standardization Gaps**.
- **Primary VI-D evidence artifacts (analysis/extraction):**
  - `analysis/VI_ev_v2/section6D_evidence.csv` (CSV; retrieval index, high-noise but useful for discovery).
  - `analysis/VI_ev_v2/retrieval_hits.jsonl` (JSONL; retrieval traces).
  - `analysis/VI_ev_v2/anchor_table.csv` (CSV; line anchors).
  - `data/ext_res_v4/O_ISAC_*.json` (structured metric cards).
- **Primary corpus files mined for VI-D claims (processed markdown):**
  - `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md` (OPA-ISAC lab-style experiment, BER/SNR/range-rate values).
  - `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md` (FSO proof-of-concept waveform bench + simulation-extended impairments).
  - `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md` (indoor simulation protocol with explicit resolution/noise settings).
  - `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md` (numerical protocol, Table-I scenario settings, Monte Carlo).
  - `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md` (benchmark-against-separated-system evaluation design).
  - `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md` (complexity + convergence + practical BER/RMSE simulation stack).
  - `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md` (simulation-based OPA validation and tradeoff curves).
  - `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md` (closed-loop OIRS, refresh/update constraints, Monte Carlo BER/outage).
  - `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md` (offline/online workflow, FLOPs accounting, calibration caveat).
  - `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md` (dataset-backed experimental validation, latency/coherence coupling, data-availability statement).
  - `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md` (benchmark CE baselines, pilot overhead and sync assumptions).
- **Standardization-support files (optional VI-D.3 evidence):**
  - `data/proc_markdowns/O_ISAC_327/O_ISAC_327.md`
  - `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md`
  - `data/proc_markdowns/O_ISAC_082/O_ISAC_082.md`
  - `data/proc_markdowns/O_ISAC_161/O_ISAC_161.md`
- **Ranked candidate paper_ids for VI-D (evidence density + KPI richness):**
  1. `O_ISAC_127` - strongest implementation-aware evidence: latency budget, coherence compliance, dataset-backed evaluation, data statement.
  2. `O_ISAC_035` - strongest explicit optical prototype workflow for FSO waveform-level validation.
  3. `O_ISAC_098` - strongest closed-loop update/tracking/Monte-Carlo validation for mobile OIRS.
  4. `O_ISAC_061` - strongest complexity-convergence reporting in OPA OW-ISAC optimization.
  5. `O_ISAC_054` - explicit benchmark-style evaluation criteria (BER/MSE thresholds).
  6. `O_ISAC_009` - explicit baseline hierarchy and pilot-overhead benchmarking.
  7. `O_ISAC_023` - structured numerical protocol and Monte-Carlo robustness checks.
  8. `O_ISAC_008` - concrete experiment-level BER/SNR/range-rate in joint OPA-LiDAR communications.
  9. `O_ISAC_112` - explicit reproducibility hints (MATLAB version, FLOPs) with practical calibration caveat.
  10. `O_ISAC_091` - simulation validation for OPA tradeoff behavior.
The weight $\alpha$ sets the communication-sensing operating point, and the formulation can be extended with reliability and update-latency constraints when channel dynamics are explicit [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127].

**VI-D Evidence Table**
**Key takeaways and open problems.** Evidence is strongest for structured decomposition methods in OPA and DCO-OFDM settings and for adaptive multi-objective search under nonstationary underwater channels [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. The main gap is not the absence of optimization methods, but the absence of harmonized constraint disclosure (optical power, quantization, update period, and overhead terms) across papers [O_ISAC_009], [O_ISAC_023], [O_ISAC_061], [O_ISAC_127]. A priority open problem is solver-independent benchmark reporting for complexity-versus-performance tradeoffs under identical scenario contracts [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Another open problem is integrating explicit eye-safety constraints into the same objective stack when those limits are reported by the experimental setup [O_ISAC_054].

| claim_id | claim | paper_id(s) | excerpt (<=2 sentences) | locator (heading + line range or page) | extracted experimental variables/KPIs |
|---|---|---|---|---|---|
| VD01 | FSO-ISAC OCDM-FMCW reports experiment-backed joint performance. | O_ISAC_035 | “Experiments demonstrate … centimeter-level ranging accuracy … simultaneously achieving a communication rate of 3.182 Gbps.” | `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md:5` | \(R=3.182\) Gbps; cm-level ranging |
| VD02 | The paper uses a proof-of-concept optical bench rather than only abstract analysis. | O_ISAC_035 | “Fig. 4 illustrates the experimental setup … In our proof-of-concept experiment … generated by an arbitrary waveform generator (AWG).” | `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md:163` | AWG-based optical testbed |
| VD03 | FSO delay is emulated with a fiber delay line in the prototype. | O_ISAC_035 | “we mimic the FSO channel delay by a fiber delay line … common and accepted practice … in proof-of-concept experiments.” | `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md:173` | fiber-delay emulation method |
| VD04 | Beat-frequency measurements are numerically cross-checked against known delay lengths. | O_ISAC_035 | “we obtain the beat frequency of 14.652 MHz, 24.409 MHz and 72.260 MHz … measured fiber delay lengths are 3.0599, 5.0976 and 15.0904 m.” | `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md:204` | beat frequencies; recovered distances |
| VD05 | Impairment robustness is partly simulation-extended due to hardware limits. | O_ISAC_035 | “due to the lack of FSO hardware, our work currently relies on simulation … plan to extend this work with practical FSO experiments.” | `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md:251` | visibility (10 km/0.5 km), pointing jitter \(0.05\) m |
| VD06 | OPA-LiDAR work reports concrete experiment settings for joint sensing and communication. | O_ISAC_008 | “actual experiment setups … 4Gbps QPSK signal … target … 15m … coherent detection … communication is also verified.” | `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md:69` | 4 Gbps, 15 m target, coherent RX |
| VD07 | The same experiment reports communication quality metrics with sensing operation active. | O_ISAC_008 | “SNR is 14dB … BER is calculated as 4.88×10^-4 … recover the data at 4Gbps.” | `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md:69` | SNR 14 dB; BER \(4.88\times10^{-4}\) |
| VD08 | RO-ISAC study is simulation-based with explicit indoor geometry assumptions. | O_ISAC_011 | “a series simulation results in an indoor space … simulation setup will be first described.” | `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md:101` | indoor 5m×5m×3m setup |
| VD09 | Sampling settings explicitly determine the stated ranging resolution. | O_ISAC_011 | “DAC sampling rate is 5GSa/s, and ADC sampling rate is 15GSa/s, so the range resolution is 1cm.” | `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md:128` | \(\Delta d=1\) cm |
| VD10 | Noise-limited sensing behavior is quantitatively characterized. | O_ISAC_011 | “distance measurement RMSE changes with transmitted SNR … increase of noise will hugely increase the RMSE.” | `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md:157` | RMSE vs SNR curves |
| VD11 | DCO-OFDM FSO-ISAC validation is numerical and reveals C&S tradeoff. | O_ISAC_023 | “numerical simulations demonstrate … reveal the tradeoff between communication and sensing functionalities.” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:5` | tradeoff validation via simulation |
| VD12 | Table-I simulation protocol discloses transceiver/scenario assumptions. | O_ISAC_023 | “As shown in Table I … 905-nm LiDAR … unambiguous distance … 300 m … channel gain for resource allocation is generated by the physical model.” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:638` | wavelength, distance, channel-gain assumptions |
| VD13 | Monte Carlo configuration is explicitly disclosed for sensing RMSE. | O_ISAC_023 | “Monte Carlo simulation configurations are the same as Table I … \(N=512\) and \(w_{\Phi}=0.5\).” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:753` | Monte Carlo, \(N=512\), \(w_{\Phi}=0.5\) |
| VD14 | Robust cm-level sensing performance is tied to electrical SNR in simulations. | O_ISAC_023 | “all the simulated curves achieve cm-level precision for an electrical SNR of larger than 2 dB.” | `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md:759` | cm-level for SNR > 2 dB |
| VD15 | LED O-ISAC explicitly benchmarks against separated sensing/communication design. | O_ISAC_054 | “evaluations … comparing them against a setup where sensing and communication operate independently … parameter settings are summarized in Table II.” | `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md:637` | benchmark protocol + Table II |
| VD16 | The benchmark threshold itself is back-calculated from KPI targets. | O_ISAC_054 | “threshold … \(\rho_I=0.8\times10^{-4}\) … derived by back-calculating from benchmark values for BER and MSE.” | `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md:639` | benchmark threshold construction |
| VD17 | OPA OW-ISAC includes parameterized simulation setup tables for reproducible runs. | O_ISAC_061 | “numerical results … Table I shows parameter configurations for simulations.” | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:552` | simulation parameter table |
| VD18 | Algorithmic implementability is quantified via complexity expressions. | O_ISAC_061 | “complexities … \(\mathcal{O}((K+1)^{3.5}N_t^7\log(1/\varepsilon_R))\) … and LP lower-order form.” | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:548` | complexity classes |
| VD19 | Fast convergence evidence is explicitly provided. | O_ISAC_061 | “the objective values converge within 3 iterations, thus guaranteeing a low-complexity implementation.” | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:600` | 3 BCD iterations |
| VD20 | Conference OPA study is simulation-validated using explicit Table-I parameters. | O_ISAC_091 | “numerical simulations are conducted … Table I shows parameter configurations for simulations.” | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:265` | simulation parameter table |
| VD21 | Communication-vs-sensing anti-correlation is shown in quantitative benchmark curves. | O_ISAC_091 | “The anti-correlation between the threshold SINR and the average ISLR … embodies the C&S tradeoff.” | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:285` | SINR-ISLR tradeoff curves |
| VD22 | OIRS mobile-system validation uses physically grounded simulation with jitter/aiming-error injection. | O_ISAC_098 | “The simulation is based entirely on physical modeling and optical laws … added independent jitter … aiming errors.” | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:420` | jitter models, aiming error injection |
| VD23 | BER/outage estimation uses large-scale Monte Carlo and explicit control-update settings. | O_ISAC_098 | “OIRS refresh time slot … 0.2 s … simulated \(10^8\) independent optical signals … calculate outage probability and BER.” | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:441` and `:443` | \(\Delta t=0.2\) s; Monte Carlo \(10^8\) |
| VD24 | Adaptive alignment is benchmarked against a traditional no-adaptation baseline. | O_ISAC_098 | “traditional FSO link without adaptive beam alignment … performance … will become worse or even interrupted.” | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:447` | baseline comparison (adaptive vs non-adaptive) |
| VD25 | Fingerprint VLP explicitly separates offline data collection and online real-time localization. | O_ISAC_112 | “offline phase … construction of a comprehensive fingerprint database … online phase … real-time localization.” | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:119` | offline/online protocol |
| VD26 | Complexity accounting is disclosed as FLOPs and implementation environment is specified. | O_ISAC_112 | “complexity … focusing on FLOPs … detailed complexity calculations are presented in Table I … MATLAB R2018a.” | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:363` and `:384` | FLOPs table; MATLAB version |
| VD27 | Practical deployment caveat explicitly highlights calibration and dynamics. | O_ISAC_112 | “practical implementation … necessitates additional considerations, including the accuracy of calibration and the impact of dynamic environmental factors.” | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:491` | calibration and nonstationarity caveat |
| VD28 | UOWC RIS work reports experiment-backed BER/secrecy/latency/energy improvements. | O_ISAC_127 | “Experimental evaluations demonstrate … 41.4% reduction in BER … secrecy rate 8.2 bps/Hz … latency of 47.3 ms.” | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:23` | BER, secrecy, latency, energy |
| VD29 | Control feasibility is explicitly tied to channel coherence and per-element update budget. | O_ISAC_127 | “coherence time \((\tau_c)\) is often under 100 ms … adaptation (37.5 \(\mu\)s) … well below the 100 ms coherence time threshold.” | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:39` | \(T_c\), per-element latency |
| VD30 | Statistical reporting quality is significantly higher than typical optical ISAC papers. | O_ISAC_127 | “mean over 10 independent trials … 95% confidence intervals … paired t-tests … significant at \(\alpha=0.01\).” | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:471` | trial count, CI, p-values |
| VD31 | Simulation-to-measurement agreement is explicitly quantified. | O_ISAC_127 | “experimental values closely align with simulation predictions, with deviations consistently remaining below 8%.” | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:533` | <8% deviation |
| VD32 | Data availability is explicitly documented for reproducibility. | O_ISAC_127 | “data … based on open salinity and turbulence datasets … additional simulation results and raw data … upon request.” | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:579` | open dataset + upon-request raw data |
| VD33 | VLPC-DCO-OFDM minimizes pilot overhead by reusing one pilot for dual functions. | O_ISAC_009 | “only a single OFDM pilot symbol is required … dual functionalities of sensing and CSI estimation.” | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:53` and `:577` | pilot overhead reduction |
| VD34 | Baseline benchmarking is explicitly structured (TD/FD/DD CE comparators). | O_ISAC_009 | “As benchmarks … conventional CE methods … TD-CE, FD-CE, DD-CE … pilot overhead is negligible.” | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:419` and `:421` | CE baselines; pilot-overhead statement |
### VI-D. Prototyping, Benchmarking, and Standardization Gaps

**Table VI-D.1. O-ISAC Experimental Testbeds and Field Validations**
The literature now includes both experimental demonstrations and simulation-heavy studies, but cross-paper comparability remains weak because scenario definitions and KPI contracts differ. Parameter tables and controlled simulation protocols are often present, yet baseline choices and reporting granularity are inconsistent across works [O_ISAC_023], [O_ISAC_035], [O_ISAC_054], [O_ISAC_061], [O_ISAC_091], [O_ISAC_112], [O_ISAC_127].

| paper_id | modality | environment | range | hardware highlights | comm KPIs | sensing KPIs | joint KPI | reproducibility (data/code) |
|---|---|---|---|---|---|---|---|---|
| O_ISAC_008 | OPA-based optical LiDAR/OWC | controlled experiment setup | target at 15 m | coherent RX, DSP recovery, QPSK-FMCW joint waveform | 4 Gbps, SNR 14 dB, BER \(4.88\times10^{-4}\) | target distance 15.005 m, velocity 7.772 m/s | simultaneous sensing+comm in one waveform | Data: NR, Code: NR |
| O_ISAC_035 | FSO OCDM-FMCW | proof-of-concept optical bench + simulation-extended impairments | fiber delays 3/5/15 m (cm-level reported) | AWG, MZM, EDFA, oscilloscope, fiber delay line | \(R=3.182\) Gbps; EVM for 4/16/64-QAM; BER vs turbulence | beat-frequency distance recovery; cm-level | shared waveform with guard-band tradeoff | Data: NR, Code: NR |
| O_ISAC_011 | RO-ISAC (OFDM, IM/DD) | indoor simulation (5m×5m×3m) | indoor room-scale | synchronized LED/PD architecture in model; Table I/II setup | BER vs SNR under modulation orders | \(\Delta d=1\) cm; RMSE vs SNR/symbols | dual-function OFDM chain | Data: NR, Code: NR |
| O_ISAC_023 | DCO-OFDM FSO-ISAC | numerical simulations with terrestrial scenario | target distance 200 m; unambiguous 300 m | 905-nm LiDAR transceiver model, Table-I parameterization | spectral efficiency under resource allocation | RMSE vs SNR and \(C_n^2\); cm-level for SNR>2 dB | tradeoff curves via joint optimization | Data: NR, Code: NR |
| O_ISAC_054 | LED O-ISAC (directionless/directional) | numerical + simulation benchmark study | indoor room scenario (Table II) | two-phase O-AP design, lens-based optical beamforming | BER gains vs separated system; BER thresholding | positioning MSE; thresholded coverage area | benchmarked O-ISAC vs separated baseline | Data: NR, Code: NR |
| O_ISAC_061 | OPA OW-ISAC (journal) | numerical simulations + realistic ITS scenario simulation | UE distances 11.5 m and 22 m | SDR/LP/BCD optimization, Table-I setup | SINR-constrained BER behavior | imaging RMSE, ISLR/contrast metrics | practical C&S tradeoff + complexity | Data: NR, Code: NR |
| O_ISAC_091 | OPA OW-ISAC (conference) | numerical simulations | UE distances 11.5 m and 22 m | OPA beamforming model + Table-I params | SINR/QoS constraints | ISLR-based sensing metric | SINR-ISLR anti-correlation | Data: NR, Code: NR |
| O_ISAC_098 | OIRS + PD array mobile OWC | physical-law simulation + Monte Carlo | mobility-oriented (speed-dependent); \(\Delta t=0.2\) s | closed-loop alignment with OIRS partitioning | BER/outage asymptotics and simulations | alignment error model, positioning support | adaptive alignment gains vs traditional FSO baseline | Data: NR, Code: NR |
| O_ISAC_112 | optical IRS-aided indoor VLP | simulation study with offline/online phases | indoor IRS arrays (21×21 each wall) | fingerprint DB pipeline, DE-WI/WKNN, FLOPs analysis | comm KPI secondary (RSS quality context) | PE improvements; cm-level class under selected settings | localization robustness under LoS blockage | Data: NR, Code: NR |
| O_ISAC_127 | RIS-assisted UOWC | dataset-backed experimental evaluation + simulation | up to 50 m tested in benchmark plots | LSTM-DRL-NSGA-II control, FPGA/edge implementation, 5-bit RIS | BER \(2.3\times10^{-5}\), secrecy 8.2 bps/Hz | environment-state prediction MAE 0.008 PSU; robustness under \(\sigma_n^2\) variations | end-to-end latency 47.3 ms within coherence window | Data: Yes (open + upon request), Code: NR |
| O_ISAC_009 | VLPC-DCO-OFDM | detailed indoor simulation protocol with multipath grids | user-grid sweeps; multiple LED-user pairs | one-pilot Radar-CE design; benchmark CE baselines | Gbps-class vs <100 Mbps RSS baseline; BER vs SNR | ranging RMSE (sub-cm in high-\(M\) settings) | single-pilot dual-function operation | Data: NR, Code: NR |

**Table VI-D.2. Benchmarking Practices and Missing Comparability Layers**

| benchmark element | what literature does (evidence) | what is missing | why it matters (quantitatively) |
|---|---|---|---|
| Channel-model disclosure | Detailed scenario/channel tables are provided in `O_ISAC_023` (Table I), `O_ISAC_061` (Table I), and `O_ISAC_091` (Table I). | Common scenario schema across papers is absent. | Without a common schema, BER/RMSE deltas are not directly comparable across modalities and distances. |
| Calibration protocol | `O_ISAC_112` explicitly states calibration accuracy as a practical concern. | Most papers do not provide calibration procedures or residual-bias budgets. | Calibration bias directly contaminates sensing RMSE and can dominate variance-limited predictions. |
| Synchronization assumptions | `O_ISAC_023`, `O_ISAC_061`, and `O_ISAC_091` assume perfect synchronization; `O_ISAC_009` discusses non-perfect sync implications. | No standardized sync-error reporting field (timing jitter, clock drift). | Synchronization errors affect both BER and ranging accuracy, shifting fair baseline comparisons. |
| Baseline definition | `O_ISAC_009` compares TD/FD/DD CE baselines; `O_ISAC_098` compares with traditional non-adaptive FSO; `O_ISAC_127` compares static/heuristic/GA/DRL classes. | Baseline stacks are heterogeneous across papers. | Different baselines can inflate or understate reported gains by multiple dB or large BER factors. |
| KPI contract | `O_ISAC_054` uses BER+MSE thresholds; `O_ISAC_061/091` use SINR+ISLR; `O_ISAC_035` uses EVM+BER+rate. | No unified mandatory KPI tuple (\(R\), BER/FER, outage, \(\Delta r_{min}\), \(\sigma_r\), latency, complexity). | Lacking a shared KPI tuple prevents reproducible Pareto-front reconstruction. |
| Statistical confidence | `O_ISAC_127` reports 10 trials, confidence intervals, and significance tests. | Most optical O-ISAC studies do not report CIs/p-values in extracted evidence. | Without uncertainty bars, “improvement” claims cannot be ranked by statistical confidence. |
| Simulation-to-measurement closure | `O_ISAC_127` reports <8% simulation-vs-measurement deviation; `O_ISAC_035` combines bench + model extension. | Many studies remain simulation-only with no closure metric. | Absence of closure metrics limits hardware transferability estimates. |
| Real-time timing disclosure | `O_ISAC_127` provides per-stage latency and coherence-budget ratio; `O_ISAC_098` provides refresh interval \(\Delta t\). | Timing decomposition (estimation/control/hardware actuation) is usually omitted. | Latency budget determines whether adaptive algorithms are feasible under channel dynamics. |
| Data sharing | `O_ISAC_127` cites open Marine Institute datasets and additional raw data on request. | Dataset availability is not explicit in most other extracted papers. | No shared datasets means limited repeatability and no common benchmarking corpus. |
| Code and implementation artifacts | Complexity formulas appear (`O_ISAC_061`, `O_ISAC_112`, `O_ISAC_127`) but code links are generally absent in extracted lines. | Reproducible code and scripts are rarely disclosed. | Reimplementation error can dominate algorithmic performance differences, especially in nonconvex solvers. |

**Table VI-D.3. Standardization-Relevant Requirements Mentioned in Corpus (Optional)**

| paper_id | body/standard mention | requirement/KPI context | implication for O-ISAC design |
|---|---|---|---|
| O_ISAC_303 | IEEE 802.15.7 | Modulation/dimming/flicker constraints for VLC operation | O-ISAC prototypes must report illumination-safe operating points with comm+sensing metrics. |
| O_ISAC_303 | IEEE 802.11-compliant vehicular VLC mention | Compliance-oriented outdoor vehicular VLC development is highlighted | Benchmark suites should include protocol-compliant operating modes, not only unconstrained PHY demos. |
| O_ISAC_082 | 3GPP TR 22.837 + 5G NR waveform parameters | ISAC use-case framing and standards-referenced waveform setup | Optical ISAC benchmarking can reuse standardized waveform/reporting templates where applicable. |
| O_ISAC_327 | ITU/IEEE channel-model references (`ITU M.2412`, IEEE 802.15.7r1, IEEE 802.11bb) | Calls for standard VLC channel model with complexity-accuracy balance | O-ISAC needs a shared channel-model contract to improve cross-paper comparability. |
| O_ISAC_161 | Explicit “standardization efforts” and interoperability/certification barriers | Notes lack of industry-wide consensus in operating/testing modes | Testbed reports should map KPIs to candidate standard profiles to support certification pathways. |

## VI-D. Prototyping, Experimental Validation, Benchmarking, and Standardization Gaps in O-ISAC

### VI-D.1 Why Validation and Benchmarking Are Structurally Hard in O-ISAC
The extracted corpus shows a clear asymmetry between analytical maturity and validation maturity. Some works already provide experiment-backed joint operation, e.g., OPA/FMCW-based demonstration with simultaneous BER/SNR and sensing outputs [O_ISAC_008], and OCDM-FMCW FSO proof-of-concept with \(R=3.182\) Gbps and centimeter-class ranging [O_ISAC_035]. However, a large portion of literature remains simulation-dominant, even when impairment-aware and algorithmically sophisticated, as seen in OPA/OIRS/VLPC works [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_009], [O_ISAC_112], [O_ISAC_023].

Cross-paper comparability is additionally weakened by heterogeneous KPI contracts. For example, one line of work emphasizes BER/MSE thresholds [O_ISAC_054], another emphasizes SINR/ISLR tradeoff [O_ISAC_091], and another emphasizes secrecy/energy/latency under dynamic channels [O_ISAC_127]. Even when baselines are present, they differ by paper (TD/FD/DD CE, static RIS, or traditional non-adaptive FSO), which prevents direct synthesis of a unified benchmark frontier [O_ISAC_009], [O_ISAC_098], [O_ISAC_127]. This fragmentation directly mirrors the Section-I concern on benchmark and reporting inconsistency, now visible at the implementation-validation layer.

### VI-D.2 Experimental Landscape: Testbeds, Prototypes, and Field Trials
Table VI-D.1 indicates three broad validation strata in current O-ISAC literature.

1. **Hardware prototype stratum (limited but critical).**
   FSO/OPA papers show concrete bench-level validation with explicit optical chains and measured KPIs [O_ISAC_008], [O_ISAC_035]. Yet even these works frequently hybridize hardware and simulation to cover atmospheric regimes and broader operating conditions [O_ISAC_035].

2. **High-fidelity numerical stratum (dominant).**
   Multiple papers provide rich simulation protocols (parameter tables, Monte Carlo details, solver convergence), enabling controlled intra-paper comparisons [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_009], [O_ISAC_112]. This stratum is strong for methodological benchmarking but weak for hardware-transfer inference unless supplemented by closure metrics.

3. **Implementation-aware data-backed stratum (emerging).**
   `O_ISAC_127` advances beyond conventional simulation by combining experimental evaluations, latency/coherence budgeting, confidence intervals, and explicit dataset provenance, plus simulation-measurement deviation reporting (<8%) [O_ISAC_127]. This pattern is currently atypical but provides a practical template for reproducible O-ISAC benchmarking.

Overall, validation maturity is therefore uneven across modalities: outdoor FSO and underwater RIS show stronger implementation details in selected works, while many indoor VLC/VLP and OPA optimization studies remain primarily simulation-centered.
A minimal benchmark contract can be written as

### VI-D.3 Benchmarking Methodology: KPIs, Baselines, and Reproducibility
An evidence-backed minimal KPI bundle for O-ISAC benchmarking should include:
$$
\mathcal{K}_{\text{min}}=\{R,\; \text{BER/FER},\; P_{\text{out}},\; \Delta r_{\min},\; \sigma_r,\; \text{latency},\; \text{complexity},\; \text{baseline class}\}.
\mathbf{s}=\{d,\,C_n^2,\,\sigma_{\text{jitter}},\,\lambda,\,B,\,N_{\text{ORIS}},\,M_{\text{OPA}},\,\bar P,\,P_{\max},\,T_{\text{update}}\},
$$
When jointly available, a compound indicator consistent with Section I can be reported as
$$
\mathrm{CRQ}_{\Delta}=\frac{R}{\Delta r_{\min}}.
\mathbf{m}=(R,\,\mathrm{BER},\,\mathrm{CRB},\,P_{\text{out}},\,\text{latency},\,\text{energy}).
$$
In the extracted VI-D set, this quantity is often not explicitly reported and should be marked as missing rather than inferred from incomparable definitions.

The baseline situation is partially positive: several works do provide structured comparators (e.g., TD/FD/DD CE baselines, separated O-Sensing+O-Communication baselines, static vs adaptive RIS baselines) [O_ISAC_009], [O_ISAC_054], [O_ISAC_127]. Yet baseline taxonomies are not aligned across papers, so “gain” values remain context-dependent. Reproducibility indicators are also imbalanced: only `O_ISAC_127` explicitly states dataset provenance and raw-data availability in the extracted lines, while most others provide parameter tables and figures but not executable artifact disclosure [O_ISAC_127], [O_ISAC_061], [O_ISAC_023], [O_ISAC_112].
The contract makes scenario assumptions explicit before interpreting gains and avoids comparing values measured under incompatible conditions [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127].

Consequently, Table VI-D.2 highlights a central gap: current literature validates *within-paper* claims reasonably well, but validates *across-paper comparability* weakly.
**Table VI-2. Recommended Reporting Checklist for Reproducible O-ISAC Experiments and Simulations.**

### VI-D.4 Practical Constraints That Shape Realizability
To connect measurement reality with analytical claims, consider an implementation-aware sensing observation model:
$$
z = s(\theta) + \epsilon_{\text{cal}} + \epsilon_{\text{sync}} + \epsilon_{\text{noise}},
$$
where \(\epsilon_{\text{cal}}\) denotes calibration residuals, \(\epsilon_{\text{sync}}\) denotes synchronization/timestamp errors, and \(\epsilon_{\text{noise}}\) aggregates shot/thermal/ambient terms (regime-dependent). The reported sensing error decomposes as
$$
\mathrm{RMSE}^2 = \mathrm{Bias}^2 + \mathrm{Var}.
$$
This decomposition is practically important because several works either assume perfect synchronization or abstract synchronization into ideal conditions [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], while other works explicitly acknowledge calibration and dynamic-environment residual effects [O_ISAC_112]. Therefore, CRB-only reporting can underestimate measured RMSE when \(\epsilon_{\text{cal}}\) and \(\epsilon_{\text{sync}}\) are not characterized:
$$
\mathrm{Var}(\hat{\theta}) \ge J^{-1}(\theta), \quad
\text{but } \mathrm{RMSE}^2 \not\approx J^{-1}(\theta)\text{ if bias terms dominate.}
$$
| Item | Minimum required fields | Why it matters |
|---|---|---|
| Scenario vector disclosure | Full $\mathbf{s}$ values, mobility profile, channel model family | Prevents hidden scenario drift across papers [O_ISAC_023], [O_ISAC_061], [O_ISAC_091] |
| KPI contract disclosure | Full $\mathbf{m}$ values with units and confidence intervals | Supports fair comparison of communication and sensing quality [O_ISAC_023], [O_ISAC_035], [O_ISAC_127] |
| Baseline taxonomy | At least one separated baseline and one practical baseline | Prevents inflated gains from weak references [O_ISAC_054], [O_ISAC_061], [O_ISAC_127] |
| Runtime and control budget | Solver runtime, $T_{\text{update}}$, hardware timing, feedback overhead | Distinguishes deployable from offline-only designs [O_ISAC_098], [O_ISAC_112], [O_ISAC_127] |
| Reproducibility package | Parameter files, script versions, data provenance, random seeds | Enables external replication and audit [O_ISAC_023], [O_ISAC_112], [O_ISAC_127] |
| Safety and operating envelope | Optical power settings and safety margin reporting method | Necessary for translation to certified deployments [O_ISAC_054], [O_ISAC_061] |

For dynamic OIRS/RIS operation, feasibility is controlled by update latency:
$$
T_{\text{update}}=\max\{T_{\text{hw}},T_{\text{est}},T_{\text{feedback}}\},
\qquad
T_{\text{update}} \ll T_c.
$$
Evidence from underwater RIS control reports end-to-end \(47.3\) ms (with \(37.5\,\mu s\) per element actuation) against coherence windows on the order of \(100\text{--}300\) ms [O_ISAC_127], whereas mobile OIRS studies show that fixed deflection over a refresh slot (\(\Delta t=0.2\) s) can significantly degrade BER as user speed changes [O_ISAC_098]. This indicates that algorithmic quality without timing compliance is insufficient for practical robustness.

Pilot/synchronization overhead further couples communication and sensing:
$$
R_{\text{eff}} = \left(1-\frac{\tau_p}{\tau_{\text{frame}}}\right)R.
$$
`O_ISAC_009` shows that dual-function reuse of one OFDM pilot can reduce overhead relative to multi-pilot baselines [O_ISAC_009]. An analogous sensing-side information-loss model can be written as
$$
J_{\text{eff}}(\theta)\approx \left(1-\frac{\tau_p}{\tau_{\text{frame}}}\right)J(\theta),
$$
but direct corpus-level quantitative validation of this exact scaling remains sparse `[TODO: evidence needed]`.

**Eye-safety / explicit peak-power compliance reporting.**  
The extracted VI-D core papers rarely provide standardized eye-safety margin reporting alongside BER/\(\sigma_r\)/latency in one table `[TODO: evidence needed]`. Power-level operating points are reported in selected works (e.g., phased operation in LED O-ISAC), but certification-grade optical safety mapping is generally not explicit in the mined lines [O_ISAC_054].

### VI-D.5 Open Challenges and Research Directions (Actionable, Benchmark-Centric)
1. **Unified benchmark card for optical O-ISAC remains missing.**  
   Why it matters: metric heterogeneity distorts claimed gains. Evidence: `“BER and MSE threshold”` framing in O_ISAC_054 contrasts with `“SINR and ISLR”` in O_ISAC_091 and secrecy-latency framing in O_ISAC_127.  
   Deliverable: publish a mandatory benchmark card \(\{R,\text{BER},P_{out},\Delta r_{\min},\sigma_r,\text{latency},\text{complexity},\text{baseline}\}\) per experiment.
**Key takeaways and open problems.** The strongest immediate need is a shared benchmark contract rather than additional isolated case studies [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Current evaluations are often rigorous within each paper, but weakly aligned across papers for meta-comparison [O_ISAC_054], [O_ISAC_112], [O_ISAC_127]. Open problems include standardized outdoor validation protocols and unified control-overhead reporting under mobility [O_ISAC_098], [O_ISAC_127]. A second open problem is safety-aware benchmarking where power margins, sensing quality, and latency are reported together [O_ISAC_054], [O_ISAC_061].

2. **Calibration residuals are underreported despite explicit practical impact.**  
   Why it matters: unreported calibration bias inflates cross-paper RMSE uncertainty. Evidence: O_ISAC_112 states practical deployment requires handling `“accuracy of calibration”` and `“dynamic environmental factors.”`  
   Deliverable: require calibration protocol + post-calibration residual statistics in every testbed table.

3. **Synchronization uncertainty is often idealized.**  
   Why it matters: timing errors jointly degrade communication decoding and ranging. Evidence: O_ISAC_023/O_ISAC_061/O_ISAC_091 assume perfect synchronization, while O_ISAC_009 discusses extra-LED requirements when sync is imperfect.  
   Deliverable: add synchronization-jitter budget and timestamp-error model to benchmark metadata.

4. **Simulation-to-hardware closure metrics are not standardized.**  
   Why it matters: deployment risk depends on prediction-to-measurement mismatch. Evidence: O_ISAC_127 reports <8% deviation; O_ISAC_035 explicitly notes missing full FSO hardware for some conditions.  
   Deliverable: define a closure KPI \(E_{\text{gap}}=\frac{|m_{\text{meas}}-m_{\text{sim}}|}{m_{\text{meas}}}\) for BER/RMSE/throughput.

5. **Latency-coherence compliance is not universally reported.**  
   Why it matters: stale control invalidates adaptive gains. Evidence: O_ISAC_127 reports 47.3 ms within \(T_c\), while O_ISAC_098 shows speed changes can sharply worsen BER under fixed refresh assumptions.  
   Deliverable: require \(T_{\text{update}}/T_c\) and stage-wise timing breakdown in all adaptive studies.

6. **Baseline taxonomies are inconsistent across papers.**  
   Why it matters: “improvement” percentages are baseline-dependent. Evidence: O_ISAC_009 uses TD/FD/DD CE baselines, O_ISAC_098 uses non-adaptive FSO baseline, O_ISAC_127 uses static/heuristic/GA/learning baselines.  
   Deliverable: benchmark with a shared 3-tier baseline set (static, model-based adaptive, learning-based adaptive).
### VI-E. Networked and Multi-User O-ISAC

7. **Statistical confidence reporting is sparse outside a few papers.**  
   Why it matters: confidence intervals and significance tests materially alter interpretation of gains. Evidence: O_ISAC_127 reports 10 trials, CI, and paired tests; similar reporting is not explicit in most other extracted VI-D lines.  
   Deliverable: mandate trial count, CI, and significance methodology for all primary KPIs.
Networked O-ISAC introduces coordination burdens that do not appear in single-link settings: multi-user interference, feedback overhead, and sensing-fusion consistency. The corpus reports explicit FoV and grating-lobe interference effects in multi-user OPA setups, tracking burden growth with user count in mobile ORIS systems, and protocol-level overhead sensitivity in VLC-based networked settings [O_ISAC_009], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_303].

8. **Dataset availability is the exception, not the norm.**  
   Why it matters: repeatability and independent benchmarking require shared data. Evidence: O_ISAC_127 gives explicit dataset provenance and raw-data availability statement, while other core papers mostly do not in extracted evidence.  
   Deliverable: release modality-tagged benchmark datasets (FSO/VLC/UOWC) with scenario metadata and train/test splits.

9. **Code artifacts and executable pipelines are rarely cited.**  
   Why it matters: solver and implementation details can change performance materially. Evidence: papers provide formulas and complexity (e.g., O_ISAC_061/O_ISAC_112/O_ISAC_127) but extracted lines generally lack explicit code-release statements.  
   Deliverable: require minimal executable package (config files + scripts + seed control) for each benchmarked result.

10. **Joint KPI normalization remains incomplete.**  
    Why it matters: separate reporting of \(R\) and \(\Delta r_{\min}\) obscures C&S efficiency tradeoffs. Evidence: many papers report strong single-side KPIs but not a unified normalized joint score in extracted lines.  
    Deliverable: report \(\mathrm{CRQ}_{\Delta}=R/\Delta r_{\min}\) with explicit bandwidth, SNR definition, and confidence bounds.

11. **Eye-safety and certification-grade constraints are weakly integrated in benchmark reports.**  
    Why it matters: realizability is constrained by optical safety and regulatory limits. Evidence: corpus includes standard-facing discussions (e.g., IEEE/3GPP/ITU references in O_ISAC_303/O_ISAC_082/O_ISAC_327) but few direct O-ISAC prototype tables link BER/RMSE outcomes to safety margins.  
    Deliverable: include safety-constrained operating envelopes in all benchmark tables `[TODO: evidence needed]`.

12. **Standardization mapping is fragmented across optical ISAC sub-communities.**  
    Why it matters: interoperability and certification depend on shared channel/model/reporting assumptions. Evidence: O_ISAC_161 explicitly mentions `“lack of industry-wide consensus … barrier to interoperability and certification”`, and O_ISAC_327 calls for a standard VLC channel model aligned with ITU methodology.  
    Deliverable: define an O-ISAC “minimum compliance profile” linking channel model, KPI set, and test protocol to candidate standards.

**VI-D takeaway.**  
The corpus demonstrates that O-ISAC validation is progressing, but unevenly: a small set of works provides true prototype or dataset-backed evidence, while most studies remain simulation-centric. The strongest implementation-aware evidence now includes explicit latency-coherence compliance, statistical confidence reporting, and simulation-to-measurement closure, yet this remains atypical rather than standard practice. Benchmarking is currently fragmented by non-aligned KPI contracts and baseline choices, which limits defensible cross-paper synthesis even when individual studies are technically rigorous. A minimum benchmark infrastructure should therefore include a shared KPI tuple, explicit baseline taxonomy, uncertainty reporting, and reproducibility artifacts (data and executable scripts). Without this infrastructure, gains in BER, rate, or sensing accuracy will continue to be difficult to compare across modality boundaries. The immediate field-level priority is not only better algorithms, but standardized and implementation-aware validation protocols.

**TODO (VI-D missing evidence / metrics)**
- `[TODO: evidence needed]` Eye-safety/IEC-style numeric compliance margins jointly reported with BER/\(\sigma_r\)/latency were not consistently found in the extracted VI-D core set.
- `[TODO: evidence needed]` Open-source code release statements are sparse in extracted lines; most works provide parameters/figures but not executable artifacts.
- `[TODO: evidence needed]` Cross-paper CRQ-style normalization under identical \(\Delta r_{\min}\) definitions is still insufficient for strict meta-analysis.
- `[TODO: evidence needed]` More true outdoor field-trial reports (beyond controlled lab emulation) are needed for OPA/OIRS mobile scenarios.

---

**VI-E Artifact Map**
- `ROOT_DIR`: `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST`
- **Alignment source (notation/taxonomy):** `drafts/section_01_introduction.md`
  - Preserved symbols/metrics: `B_eff`, `R`, `\Delta r_{\min}`, `\sigma_r`, `SNR`, `BER`, `CRB`, `\mathrm{CRQ}_{\Delta}`.
  - Preserved modality boundaries: Fiber / FSO / VLC-LiFi / Photo-THz.
- **TOC/scope detection:**
  - `paper_outline.md` not found.
  - `review_package/surveyOutline.md` uses an older Section-VI structure; current draft (`VI-A/B/C/D`) already follows the user-defined decomposition. This VI-E is therefore instantiated as: **Networked and Multi-User O-ISAC**.
- **Primary VI-E evidence artifacts (analysis/extraction):**
  - `analysis/VI_ev_v2/section6E_summary.json` (JSON; coarse prevalence summary).
  - `analysis/VI_ev_v2/section6E_summary_table.csv` (CSV; same summary in tabular form).
  - `analysis/VI_ev_v2/section6E_medium_slices.csv` (CSV; modality slices).
  - `analysis/VI_ev_v2/retrieval_hits.jsonl` (JSONL; retrieval traces).
  - `analysis/VI_ev_v2/anchor_table.csv` (CSV; line anchors for corpus retrieval).
- **Primary corpus files mined for VI-E claims (processed markdown):**
  - `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md`
  - `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md`
  - `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md`
  - `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md`
  - `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md`
  - `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md`
  - `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md`
  - `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md`
  - `data/proc_markdowns/O_ISAC_068/O_ISAC_068.md`
  - `data/proc_markdowns/O_ISAC_199/O_ISAC_199.md`
- **Ranked candidate paper_ids for VI-E (relevance to networked/multi-user + KPI richness):**
  1. `O_ISAC_061` - strongest optical multi-user model with SINR/ISLR coupling and explicit algorithmic complexity.
  2. `O_ISAC_091` - compact multi-UE OPA formulation with explicit QoS constraints and tradeoff curves.
  3. `O_ISAC_098` - strongest evidence on alignment overhead, feedback delay, mobility sensitivity, and distributed OIRS control.
  4. `O_ISAC_009` - strongest pilot-overhead/CSI-sensing reuse evidence in optical multi-pair scenarios.
  5. `O_ISAC_303` - strongest VLC network/MAC synthesis (TDMA/CSMA/OFDMA/NOMA/cell-free references) and overhead-aware statements.
  6. `O_ISAC_127` - strongest latency-coherence-compute co-design and scaling discussion for adaptive RIS control.
  7. `O_ISAC_112` - strongest dual-IRS architecture with explicit offline/online computational pipeline.
  8. `O_ISAC_054` - explicit two-phase distributed O-AP scheduling (TDMA) and IM/DD constraints.
  9. `O_ISAC_068` - integrated protocol and distributed-intelligence framing for cross-layer coordination.
  10. `O_ISAC_199` - network-adjacent MIMO-FSO benchmark with outage/BER/SNR under optical impairments.

**VI-E Evidence Table**

| claim_id | claim | paper_id(s) | excerpt (<=2 sentences) | locator (heading + line range or page) | extracted network variables/KPIs |
|---|---|---|---|---|---|
| VE01 | OPA OW-ISAC is explicitly formulated for concurrent multi-user service. | O_ISAC_061 | "...OPA-based OW-ISAC framework to enable concurrent multi-user communication and environment imaging." | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:5` | multi-user support; joint C&S system model |
| VE02 | OW-ISAC tasks are split into cooperative and uncooperative regimes. | O_ISAC_061 | "Contemporary research on OW-ISAC delineates two primary categories: cooperative and uncooperative types." | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:27` | architecture class for sensing cooperation |
| VE03 | OPA multi-beam/grating-lobe behavior creates network-side interference pressure. | O_ISAC_061 | "...OPA exhibits an inherent multi-beam property and may disperse optical energy in unexpected directions..." | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:35` | interference source in multi-user beam sharing |
| VE04 | MUI mitigation is more urgent in OPA OW-ISAC than RF counterparts. | O_ISAC_061 | "...the OPA-based OW-ISAC system has a more urgent need for MUI mitigation..." | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:241` | \(\mathrm{SINR}_k\) sensitivity to grating-lobe collisions |
| VE05 | Communication QoS is enforced by per-UE SINR constraints in joint design. | O_ISAC_061 | "...the light-field SINR ... should exceed a threshold \(\Gamma_k\) to ensure the communication QoS..." | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:357` | QoS thresholds \(\Gamma_k\), chance-like guarantee |
| VE06 | The joint solver complexity is explicitly reported and scales with user/problem size. | O_ISAC_061 | "...complexities ... \(\mathcal{O}((K+1)^{3.5}N_t^7\log(1/\varepsilon_R))\)..." | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:548` | complexity classes; dependence on \(K\), \(N_t\) |
| VE07 | Iterative optimization convergence is fast in reported simulations. | O_ISAC_061 | "...objective values converge within 3 iterations..." | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:600` | \(N_b \approx 3\) iterations |
| VE08 | A realistic scenario uses two cooperative targets (multi-user sensing/comm). | O_ISAC_061 | "...conduct OWC with ... two cooperative targets, i.e., autonomous vehicles." | `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md:662` | \(K=2\) cooperative targets |
| VE09 | A conference OPA study also targets multiple UEs with explicit SINR/ISLR metrics. | O_ISAC_091 | "...serve multiple communication user equipments ... derive ... SINR ... and ISLR ..." | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:17` | \(\mathrm{SINR}\), ISLR, multi-UE objective |
| VE10 | OPA field-of-view is explicitly limited by array spacing and grating-lobe effects. | O_ISAC_091 | "The grating lobes cause spatial ambiguity ... As a result, the field of view (FOV) for OPA is limited..." | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:62` | FoV bound; spatial ambiguity |
| VE11 | Communication and sensing metrics are anti-correlated in multi-UE OPA results. | O_ISAC_091 | "The anti-correlation between the threshold SINR and the average ISLR ... embodies the C&S tradeoff..." | `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md:285` | tradeoff frontier (SINR vs ISLR) |
| VE12 | Mobile OWC burden scales at the BS as user count rises. | O_ISAC_098 | "As the user count rises, the base station encounters challenges ... track multiple users ... [and] crosstalk..." | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:25` | scaling pressure with user count; crosstalk risk |
| VE13 | Alignment responsibility can be distributed to multiple OIRS units. | O_ISAC_098 | "...offload the burden of beam alignment ... to one or more OIRSs ... Each OIRS can be responsible for beam tracking in an area." | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:27` | distributed architecture by service area |
| VE14 | Closed-loop feedback is explicitly modeled between user and OIRS. | O_ISAC_098 | "...user sends a feedback signal to the OIRS to modify the beam control mode..." | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:59` | feedback signaling loop |
| VE15 | Control overhead includes uplink generation/transmission/processing delay. | O_ISAC_098 | "...uplink signal generation, transmission and processing all take time..." | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:314` | \(t_s\) processing/feedback overhead |
| VE16 | Mobility mismatch across refresh intervals degrades BER/outage robustness. | O_ISAC_098 | "...if the user suddenly changes the moving speed ... system performance will be greatly reduced." | `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md:486` | refresh interval \(\Delta t\), mobility sensitivity |
| VE17 | Optical VLPC reuses one pilot for both sensing and CSI acquisition. | O_ISAC_009 | "...only a single OFDM pilot symbol is required ... dual functionalities of sensing and CSI estimation." | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:53` and `:577` | pilot overhead minimization |
| VE18 | Benchmark DD-CE requires more pilot overhead than Radar-CE. | O_ISAC_009 | "...DD-domain CSI estimation ... requires an increased number of N = 4 OFDM pilot symbols." | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:571` | pilot count \(N=4\) baseline |
| VE19 | Synchronization uncertainty explicitly changes LED requirements in positioning. | O_ISAC_009 | "...when the LEDs and the PD are not perfectly synchronized, four LEDs have to be harnessed..." | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:208` | sync overhead (extra anchors/signals) |
| VE20 | Sensing-aided CSI materially changes network throughput regime. | O_ISAC_009 | "...RSS-assisted sensing ... below 100 Mbps ... [while] Gbps-level data rates can be achieved..." | `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md:571` and `:629` | sub-100 Mbps vs Gbps regime |
| VE21 | VLC LiSAC explicitly includes TDMA for multi-user sharing. | O_ISAC_303 | "TDMA ... divide[s] ... channels into multiple time slots ... more than one user can share..." | `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md:196` | MAC scheduling class (TDMA) |
| VE22 | CSMA enhancement reports significant saturation-throughput gains. | O_ISAC_303 | "...increased the saturation throughput by nearly 50% and 100% under the two- and four-node scenarios..." | `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md:200` | throughput gains under node scaling |
| VE23 | OFDMA/NOMA are reported as combined multiple-access options in VLC. | O_ISAC_303 | "...OFDMA ... data rate of 13.6 Mb/s ... often integrated with ... NOMA..." | `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md:202` | OFDMA data rate; MA hybridization |
| VE24 | Multi-cell multi-user MIMO VLC identifies ICI/IUI and IA mitigation. | O_ISAC_303 | "Inter-cell inference (ICI) and inter-user inference (IUI) are the two major factors ... [IA] to mitigate IUI and ICI..." | `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md:228` | interference terms + mitigation |
| VE25 | Cell-free VLC is explicitly cited as a multi-user distributed architecture. | O_ISAC_303 | "DenseVLC ... is a massive cell-free MIMO VLC system ... distributed LED transmitters ..." | `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md:230` | cell-free architecture |
| VE26 | Localization-assisted CSI estimation is reported to reduce overhead. | O_ISAC_303 | "CSI is estimated based on localization ... [which] can reduce the system overhead significantly." | `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md:268` | CSI/SSI coupling and overhead reduction |
| VE27 | Integrated VL protocols explicitly target synchronization/fusion and overhead reduction. | O_ISAC_068 | "...protocols define ... channel access, synchronization, and sensor data fusion ... reduce overhead..." | `data/proc_markdowns/O_ISAC_068/O_ISAC_068.md:105` | control-plane protocol overhead |
| VE28 | Cross-layer direction toward edge/distributed intelligence is explicitly stated. | O_ISAC_068 | "...integration ... into ... edge computing and distributed intelligence ... realtime decision-making..." | `data/proc_markdowns/O_ISAC_068/O_ISAC_068.md:145` | edge/distributed processing architecture |
| VE29 | Distributed O-AP service with TDMA appears in LED O-ISAC design. | O_ISAC_054 | "...Phase 2 ... each device is individually served in a time-division multiple access (TDMA) fashion." | `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md:49` | scheduling in distributed AP setting |
| VE30 | IM/DD nonnegativity constraints are explicit in LED-based O-ISAC. | O_ISAC_054 | "...IM/DD ... [requires] introducing a dc bias ... ensure the signal remains nonnegative." | `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md:128` | optical power/nonnegativity constraint |
| VE31 | Dual-IRS multi-LED architecture is explicitly parameterized. | O_ISAC_112 | "...presence of M LED transmitters ... two opposing walls ... each array consisting of \(N^s\) reflective units..." | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:60` | \(M\), \(2N^s\), structural scale |
| VE32 | Localization pipeline is explicitly split into offline and online stages. | O_ISAC_112 | "...offline phase ... comprehensive fingerprint database ... online phase ... real-time localization..." | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:119` | training/online split; runtime burden |
| VE33 | Two-step IRS selection strategy is used to stabilize localization over space. | O_ISAC_112 | "...two-step localization strategy ... first ... IRS I ... then ... IRS II..." | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:359` | distributed fusion decision flow |
| VE34 | Complexity explicitly includes offline + online and two-step overhead. | O_ISAC_112 | "...algorithmic complexity ... cumulative complexity of both the offline stage ... and the online stage..." | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:371` | complexity disclosure |
| VE35 | Coherence-time constrained adaptation is explicit in adaptive RIS-UOWC. | O_ISAC_127 | "...coherence time ... often under 100 ms ... end-to-end ... 47.3 ms ... within [coherence] budget..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:39` and `:497` | \(T_c\), adaptation latency |
| VE36 | Closed-loop compute/actuation latency decomposition is reported. | O_ISAC_127 | "...LSTM 12.3 ms, DRL 18.7 ms, NSGA-II 6.7 ms, RIS actuation 9.6 ms ... total 47.3 ms..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:505` | stage-wise latency and complexity |
| VE37 | Scalability bottlenecks include synchronization/processing and call for hierarchical/distributed RIS control. | O_ISAC_127 | "...scalability beyond 512 RIS elements introduces synchronization and processing latency ... hierarchical coordination or distributed RIS architectures should be explored..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:551` | scalability limit; coordination direction |
| VE38 | MIMO-FSO evidence reports strong BER/power gains and outage-oriented metrics. | O_ISAC_199 | "...10 Gb/s ... MIMO-FSO ... reduces bit errors ... and increase signal power ..." and "...performance metrics ... BER, outage probability (OP), and SNR." | `data/proc_markdowns/O_ISAC_199/O_ISAC_199.md:27` and `:128` | BER/OP/SNR; aperture diversity |

**Table VI-E.1. Networked O-ISAC Scenarios and KPIs Reported in Optical Literature**

| paper_id | modality | K/M | architecture (centralized/distributed) | multiple-access/scheduling | comm KPIs | sensing KPIs | overhead disclosure |
|---|---|---|---|---|---|---|---|
| O_ISAC_061 | OPA-based OW-ISAC (FSO/OWC) | \(K=2\) UEs (simulation) | centralized OPA Tx + PD-array Rx | spatial multi-beam with QoS-constrained optimization | light-field SINR, BER-vs-SNR | ISLR/contrast, imaging RMSE | BCD iterations + complexity disclosed; explicit pilot overhead not reported |
| O_ISAC_091 | OPA-based OW-ISAC (conference) | two cooperative targets in evaluation | centralized | QoS-constrained beamforming (SDR/LP variants) | SINR thresholds | ISLR, FOV-clutter behavior | solver complexity disclosed; signaling overhead `[TODO: evidence needed]` |
| O_ISAC_098 | OIRS+PD mobile OWC | single-user baseline; multi-user scaling discussion | distributed OIRS area responsibility + closed-loop user feedback | region-partitioned wide/narrow beams; refresh-slot control | BER, outage | alignment error \(\tau_c\), tracking accuracy/stability | explicit \(\Delta t=0.2\) s refresh + processing-delay terms |
| O_ISAC_009 | VLPC-DCO-OFDM (VLC, IM/DD) | multi LED-user pairs (room-wide maps) | centralized multi-LED/multi-pair | pilot-assisted OFDM sensing/communication reuse | CCMC/DCMC rates, BER | ranging/localization RMSE | one pilot dual use vs DD-CE \(N=4\) pilots |
| O_ISAC_054 | LED O-ISAC with distributed O-APs | \(\mu\) distributed O-APs | distributed transmitters, centrally designed phases | Phase-2 TDMA service | BER, equivalent channel gain | localization MSE/tracking | two-phase protocol disclosed; frame/control overhead not numerically normalized |
| O_ISAC_112 | IRS-assisted fingerprint VLP | \(M\) LEDs, \(2N^s\) IRS units, \(L\) targets | centralized database + dual-IRS two-step decision | time-division acquisition in fingerprint construction | RSS-centric support (rate not primary KPI) | positioning error (PE), average PE | offline+online complexity explicitly reported |
| O_ISAC_127 | RIS-assisted UOWC | single legit link + eavesdropper; \(N_{\mathrm{RIS}}\in\{64,128,256,\dots\}\) | centralized edge control; distributed/hierarchical extension discussed | closed-loop predictive control (no classical OMA/NOMA focus) | BER, secrecy rate, energy | environment prediction MAE; robustness against turbulence/salinity | full stage-wise latency and coherence-budget reporting |
| O_ISAC_303 | LiSAC VLC survey | multi-user and multi-cell classes | centralized, multi-cell, and cell-free (DenseVLC) are all reported | TDMA/SDMA/CSMA/OFDMA/NOMA/CDMA | throughput/data-rate classes | VLP/VLS and CRLB-oriented statements | localization-based CSI estimation reported to reduce overhead |
| O_ISAC_068 | VL-JCS survey | architecture-level (not fixed \(K,M\)) | protocol-centric integrated architecture | integrated channel-access/sync/fusion protocols | reliability/efficiency class metrics | cooperative sensing/joint detection statements | overhead reduction explicitly claimed at protocol level |
| O_ISAC_199 | MIMO-FSO + sensing-assisted link | aperture-level scaling (1x1, 2x2, 4x4) | point-to-point/multi-aperture | diversity combining (MRC/SC/EGC) | BER, OP, SNR, link range | strain/temperature sensing via FBG | control-plane overhead not disclosed `[TODO: evidence needed]` |

**Table VI-E.2. Cross-Layer Mechanisms vs Network Bottlenecks**

| mechanism | alignment overhead | CSI/SSI acquisition | interference | fronthaul/backhaul | computation | mobility |
|---|---|---|---|---|---|---|
| OIRS closed-loop feedback and regional control | `O_ISAC_098`: offloads BS alignment to distributed OIRS; explicit refresh/feedback delay terms | `O_ISAC_098`: PD-array estimates direction and feeds control to OIRS | `O_ISAC_098`: mitigates beam misalignment but residual crosstalk remains as users scale | `[TODO: evidence needed]` explicit fronthaul model in optical corpus | `O_ISAC_098`: realtime correction but processing time \(t_s\) enters loop | `O_ISAC_098`: speed changes during \(\Delta t\) sharply degrade BER/outage |
| Sensing-aided CSI with pilot reuse | `O_ISAC_009`: single pilot reused for sensing+CSI reduces alignment/training cycle burden | `O_ISAC_009`: one-pilot Radar-CE vs DD-CE \(N=4\) pilot baseline | `O_ISAC_009`: improved CSI reduces decoding errors in multipath | `[TODO: evidence needed]` network transport of CSI not quantified | `O_ISAC_009`: lower training overhead than multi-pilot baselines | `O_ISAC_009`: synchronization errors require extra anchors/LEDs |
| Multi-user OPA joint precoding + receiver orientation | `O_ISAC_061`: joint precoder/PD-orientation optimizes coverage under FoV limits | `O_ISAC_061`: QoS enforced via \(\Gamma_k\), turbulence-quantile SINR model | `O_ISAC_061`/`O_ISAC_091`: grating-lobe MUI/ICI is dominant and needs active mitigation | `[TODO: evidence needed]` explicit fronthaul split unavailable | `O_ISAC_061`: high-order SDP/LP+BCD complexity reported | `O_ISAC_061`: shown in ITS scenario with cooperative moving targets |
| VLC MAC-layer multiple access stack | `O_ISAC_303`: TDMA/SDMA/CSMA/OFDMA partition access in dense lighting networks | `O_ISAC_303`: localization-assisted CSI can reduce pilot overhead | `O_ISAC_303`: reports ICI/IUI in multi-cell MIMO VLC and IA mitigation | `[TODO: evidence needed]` backhaul bottlenecks in optical LiSAC rarely quantified | `O_ISAC_303`: CSMA/OFDMA/precoding complexity exists but non-unified reporting | `O_ISAC_303`: hybrid RF/IR uplink helps in blockage/mobility-sensitive setups |
| Fingerprint-based dual-IRS two-step localization | `O_ISAC_112`: two-step IRS selection reduces wall-edge localization degradation | `O_ISAC_112`: offline DB construction + online matching explicitly defined | `O_ISAC_112`: mitigates LoS-blockage distortions via IRS-enhanced NLoS fingerprints | `[TODO: evidence needed]` distributed database/fusion signaling cost not provided | `O_ISAC_112`: offline+online FLOPs disclosed; two-step raises complexity | `O_ISAC_112`: dynamic-environment/calibration sensitivity explicitly noted |
| Predictive RIS control (LSTM-DRL-NSGA-II) | `O_ISAC_127`: adaptation explicitly bounded by coherence-time budgets | `O_ISAC_127`: prediction-driven state update mitigates stale CSI effects | `O_ISAC_127`: secrecy/BER robustness under turbulence/noise conditions | `O_ISAC_127`: edge platform feasibility discussed; explicit fronthaul remains limited | `O_ISAC_127`: stage-wise latency and \(O(Tn_h^2)\), \(O(NP^2)\) complexity reported | `O_ISAC_127`: transfer learning + distributed/hierarchical coordination needed for scaling mobility/nonstationarity |

## VI-E. Networked and Multi-User O-ISAC: Multi-Node Coordination, Multiple Access, Interference, and Cross-Layer Design

### VI-E.1 Why Networked O-ISAC Is Qualitatively Harder Than Single-Link O-ISAC
At network scale, O-ISAC inherits three coupled stressors that are weaker or absent in single-link formulations: (i) multi-user interference and beam collision, (ii) control/estimation overhead, and (iii) sensing-fusion consistency under mobility. OPA multi-user studies show that grating-lobe behavior can push inter-user interference into the same FoV region used by sensing receivers, creating direct C&S contention in the observation process [O_ISAC_061], [O_ISAC_091]. In mobile OIRS settings, user-count growth shifts tracking and computation burden to coordination layers, and stale control updates can dominate BER/outage behavior [O_ISAC_098]. In VLC networked VLPC, pilot and synchronization choices directly determine whether rates stay in sub-100 Mbps regimes or move to Gbps-class operation under multipath [O_ISAC_009].
A compact network objective anchor is

The same evidence indicates that communication-only network abstractions are insufficient. LiSAC survey evidence reports explicit MAC and multi-access families (TDMA/CSMA/OFDMA/NOMA) together with multi-cell/cell-free VLC structures and localization-assisted CSI overhead reduction, implying that PHY and MAC are already coupled in practice [O_ISAC_303]. Protocol-centric JCS analyses similarly stress that channel access, synchronization, and sensor fusion must be co-designed to control overhead [O_ISAC_068]. Therefore, networked O-ISAC should be treated as a cross-layer control system rather than a per-link waveform problem.

### VI-E.2 Taxonomy of Network Architectures and Protocols in Optical O-ISAC
An evidence-grounded taxonomy for VI-E can be organized along four axes.

1. **Fusion/control architecture: centralized vs distributed.**  
   Centralized optimization dominates OPA beamforming studies (`O_ISAC_061`, `O_ISAC_091`), whereas OIRS mobile studies explicitly distribute alignment duties across one or more OIRS units with local feedback loops (`O_ISAC_098`). Dual-IRS fingerprint systems are centralized at the database level but execute spatially distributed sensing through IRS-I/IRS-II selection (`O_ISAC_112`).

2. **Network topology: cell-based vs cell-free optical networking.**  
   Cell-based and multi-cell MIMO VLC structures are widely reported with ICI/IUI concerns (`O_ISAC_303`), while DenseVLC-style cell-free operation is explicitly cited as a distributed LED architecture for multi-user service (`O_ISAC_303`).

3. **Access/scheduling family.**  
   Optical networked studies report TDMA, SDMA, CSMA, OFDMA, and NOMA variants (`O_ISAC_303`), and two-phase O-ISAC with explicit TDMA service is also reported in LED-centric design (`O_ISAC_054`). In OPA/OIRS studies, scheduling is often implicit through beam and control cycles rather than explicit MAC labels (`O_ISAC_061`, `O_ISAC_098`).

4. **Overhead/estimation strategy.**  
   Pilot reuse and sensing-aided CSI estimation reduce signaling load (`O_ISAC_009`, `O_ISAC_303`), while protocol-level integration of synchronization and sensor fusion is proposed to reduce overhead in VL-JCS settings (`O_ISAC_068`). Coherence-time-coupled adaptive control appears in RIS-UOWC with explicit latency decomposition (`O_ISAC_127`).

### VI-E.3 Unified Analytical Framework and Fundamental Coupling Mechanisms
We keep Section-I notation and use \(\Delta d \equiv \Delta r_{\min}\) for range-resolution references.

For a generic downlink multi-user optical network:
$$
\mathbf{y}_k = \mathbf{H}_k(\mathbf{u})\sum_{j=1}^{K}\mathbf{w}_j s_j + \mathbf{n}_k,
\max_{\{\mathbf{w}_k\},\Theta}\;\sum_{k}\omega_k\log\!\left(1+\mathrm{SINR}_k\right)-\lambda\,\mathrm{CRB}(\Theta)
$$
where \(\mathbf{u}\) collects network controls (beam weights, RIS/OIRS phases, scheduling, resource blocks, power split, and feedback decisions). In coherent/light-field models, \(\mathbf{H}_k\) is field-domain [O_ISAC_061], [O_ISAC_091]; in IM/DD settings, constraints must enforce nonnegative optical signals and optical power limits [O_ISAC_054], [O_ISAC_009]:
$$
x_j(t)\ge 0,\quad \mathbb{E}[x_j(t)]\le P_{\mathrm{avg}},\quad x_j(t)\le P_{\mathrm{peak}}.
\text{s.t.}\quad \sum_k\|\mathbf{w}_k\|_2^2\le P,\quad \theta_n\in\mathcal Q.
$$

Define per-user effective SINR (or IM/DD-equivalent SNR) as \(\mathrm{SINR}_k(\mathbf{u})\), then
$$
R_k(\mathbf{u}) = B_k\log_2\!\big(1+\mathrm{SINR}_k(\mathbf{u})\big).
$$
Control/pilot/synchronization overhead yields
$$
R_{k,\mathrm{eff}} = \left(1-\frac{\tau_{\mathrm{oh}}}{\tau_{\mathrm{frame}}}\right)R_k,
$$
consistent with reported pilot and sync burden differences between single-pilot and multi-pilot optical CE strategies [O_ISAC_009], and with protocol-level overhead discussions [O_ISAC_068], [O_ISAC_303].
Using Model VI-U, this objective makes communication, sensing, and ORIS quantization constraints explicit in one multi-user program [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. The practical bottleneck is scaling control overhead: CSI refresh, scheduling updates, and feedback timing can dominate gains if not included in the optimization itself [O_ISAC_009], [O_ISAC_068], [O_ISAC_098], [O_ISAC_303].

For cooperative sensing/fusion with \(M\) optical sensing nodes:
$$
z_m = s_m(\theta;\mathbf{u}) + v_m,\qquad m=1,\dots,M.
$$
If conditional independence holds,
$$
\mathbf{J}_{\mathrm{tot}}(\theta;\mathbf{u}) = \sum_{m=1}^{M}\mathbf{J}_m(\theta;\mathbf{u}),\qquad
\mathrm{Cov}(\hat{\theta}) \succeq \mathbf{J}_{\mathrm{tot}}^{-1}.
$$
Independence may fail under shared clutter/background and common hardware-control couplings `[TODO: evidence needed]`. Optical evidence does, however, explicitly show that FoV overlap and grating-lobe contamination can make user-linked echoes leak into sensing channels [O_ISAC_061], [O_ISAC_091].
**Key takeaways and open problems.** Multi-user OPA/ORIS designs show clear gains, but current studies rarely standardize network-level overhead metrics in a common unit system [O_ISAC_009], [O_ISAC_061], [O_ISAC_091], [O_ISAC_303]. Control-plane modeling and sensing-fusion policies are often analyzed separately, even though evidence indicates strong coupling under mobility [O_ISAC_068], [O_ISAC_098], [O_ISAC_127]. A near-term open problem is fairness-aware and latency-aware optimization with explicit reporting of control symbols, feedback bits, and scheduling delay [O_ISAC_009], [O_ISAC_303]. Another open problem is reproducible cooperative benchmark suites that vary PHY, MAC, and fusion policy jointly [O_ISAC_068], [O_ISAC_303].

Two canonical networked O-ISAC optimization archetypes follow.
### VI-F. AI/ML and Security-Aware O-ISAC

1. **Weighted-sum utility**
$$
\max_{\mathbf{u}\in\mathcal{U}}
\alpha\sum_{k=1}^{K}R_{k,\mathrm{eff}}(\mathbf{u})
+(1-\alpha)\,\Phi\!\big(\mathbf{J}_{\mathrm{tot}}(\theta;\mathbf{u})\big),
\quad \alpha\in[0,1].
$$
Here \(\Phi(\cdot)\) may be \(\mathrm{tr}(\mathbf{J})\), \(-\log\det(\mathbf{J}^{-1})\), or CRB proxies depending on sensing task.
AI-assisted adaptation and security-aware design are increasingly coupled in O-ISAC, especially in dynamic channels where static policies underperform. The corpus reports learning-driven adaptation for nonstationary environments and complementary security formulations around secrecy, authentication, and resilience, but jointly validated AI-plus-security optical benchmarks remain limited [O_ISAC_127], [O_ISAC_145], [O_ISAC_156], [O_ISAC_163].

2. **Constrained service-guarantee form**
$$
\max_{\mathbf{u}} \sum_{k=1}^{K}R_{k,\mathrm{eff}}(\mathbf{u})
\;\text{s.t.}\;
\mathrm{RMSE}_{\mathrm{loc}}(\mathbf{u})\le \delta,\;
P_{\mathrm{out}}(\mathbf{u})\le \epsilon,\;
\mathbf{u}\in\mathcal{U}_{\mathrm{optical}}.
$$
\(\mathcal{U}_{\mathrm{optical}}\) includes IM/DD nonnegativity, peak/average optical power, FoV/pointing constraints, RIS/OPA quantization, and update-latency constraints [O_ISAC_054], [O_ISAC_009], [O_ISAC_061], [O_ISAC_098], [O_ISAC_127].
A compact secrecy anchor is

**Scalability/overhead insight.**  
Guided by corpus evidence, a practical overhead decomposition is
$$
\tau_{\mathrm{oh}}(K,M) \approx \tau_0 + K\,\tau_{\mathrm{ctrl}} + M\,\tau_{\mathrm{sense}} + \tau_{\mathrm{sync}},
$$
where \(\tau_{\mathrm{ctrl}}\) is control/feedback delay (explicitly discussed in `O_ISAC_098`), \(\tau_{\mathrm{sense}}\) captures sensing/pilot burden (`O_ISAC_009`), and feasibility requires
R_s=[R_b-R_e]^+,
$$
T_{\mathrm{update}} \ll T_c
$$
in dynamic optical channels (`O_ISAC_127`). This scaling law is a synthesis model, not a fully standardized result `[TODO: evidence needed]`.

### VI-E.4 Comparative Synthesis: What the Literature Demonstrates (and What It Does Not)
Tables VI-E.1 and VI-E.2 show four converging patterns.

1. **Multi-user optical O-ISAC is demonstrated, but mostly at small \(K\).**  
   OPA papers present explicit multi-UE formulations and tradeoff curves with strong algorithmic detail [O_ISAC_061], [O_ISAC_091], but large-\(K\) scaling with realistic control-plane load is rarely quantified.

2. **Overhead-aware designs exist, yet reporting contracts remain inconsistent.**  
   One-pilot dual-function optical CE, synchronization caveats, and localization-assisted overhead reduction are concrete advances [O_ISAC_009], [O_ISAC_303], but common normalized overhead KPIs (e.g., control symbols/frame, feedback bits/s) are mostly absent `[TODO: evidence needed]`.

3. **Distributed alignment/control is a strong enabler under mobility.**  
   OIRS closed-loop tracking and distributed area responsibilities directly address alignment bottlenecks [O_ISAC_098], while predictive RIS control closes the latency-coherence loop in fast channels [O_ISAC_127].

4. **Cross-layer claims outpace cross-layer benchmarks.**  
   Literature increasingly calls for integrated protocol/fusion/edge-intelligence operation [O_ISAC_068], [O_ISAC_303], but side-by-side benchmarks that jointly vary MAC, sensing-fusion policy, and control latency are scarce `[TODO: evidence needed]`.

### VI-E.5 Open Challenges and Research Directions (Actionable; Network-Centric)
1. **Large-\(K\) scaling laws for optical O-ISAC are underdeveloped.**  
   Metric bottleneck: sum-rate and outage under rising user count. Evidence: `O_ISAC_098` states BS tracking burden rises with user count and beam crosstalk.  
   Deliverable: derive and validate \(R_{\Sigma,\mathrm{eff}}(K)\) under explicit alignment-control budgets.

2. **Overhead-normalized KPI reporting is missing.**  
   Metric bottleneck: \(R_{k,\mathrm{eff}}\) comparability across papers. Evidence: `O_ISAC_009` contrasts single-pilot vs \(N=4\)-pilot baselines, while many works omit normalized overhead.  
   Deliverable: mandate \(\tau_{\mathrm{oh}}/\tau_{\mathrm{frame}}\), pilot count, and feedback-rate disclosure in all networked studies.

3. **MAC-layer and beam-layer co-design remains fragmented.**  
   Metric bottleneck: fairness/throughput under interference. Evidence: `O_ISAC_303` lists TDMA/CSMA/OFDMA/NOMA and multi-cell ICI/IUI issues, but without a unified co-design contract.  
   Deliverable: joint scheduler that optimizes access mode and beam control using sensing freshness constraints.

4. **FoV/grating-lobe-aware interference modeling needs standardization.**  
   Metric bottleneck: sensing RMSE and per-user SINR under beam collisions. Evidence: `O_ISAC_061`/`O_ISAC_091` show FoV-limited sensing and grating-lobe-induced interference.  
   Deliverable: standardized angular interference model with validated cross-paper parameters.

5. **Synchronization uncertainty is still weakly integrated into optimization.**  
   Metric bottleneck: localization RMSE and CE accuracy. Evidence: `O_ISAC_009` states extra anchor requirements under non-perfect sync.  
   Deliverable: robust co-design with explicit timing-error states in both rate and Fisher-information objectives.

6. **Distributed fusion under correlated optical impairments is under-modeled.**  
   Metric bottleneck: CRB/RMSE of cooperative tracking. Evidence: current works use distributed structures (`O_ISAC_098`, `O_ISAC_112`) but generally do not model cross-node correlation explicitly.  
   Deliverable: cooperative FIM models with correlated clutter/turbulence terms `[TODO: evidence needed]`.

7. **Fronthaul/backhaul constraints are rarely quantified in optical networked O-ISAC.**  
   Metric bottleneck: latency and stale fusion updates. Evidence: protocol-level integration is discussed (`O_ISAC_068`), but explicit fronthaul budgets are largely absent.  
   Deliverable: end-to-end latency model splitting sensing upload, fusion, and control return paths.

8. **Fairness metrics are not consistently reported in multi-user optical ISAC.**  
   Metric bottleneck: user-level QoS guarantees under sum-rate optimization. Evidence: many studies emphasize SINR/BER/tradeoff curves but not Jain-type fairness indices (`O_ISAC_061`, `O_ISAC_091`, `O_ISAC_009`).  
   Deliverable: include fairness-constrained optimization and fairness KPI reporting `[TODO: evidence needed]`.

9. **Computation-aware control remains limited to few implementations.**  
   Metric bottleneck: real-time viability under nonconvex optimization. Evidence: `O_ISAC_061` provides complexity formulas and convergence; `O_ISAC_127` provides full latency breakdown.  
   Deliverable: hardware-calibrated algorithm benchmarks (CPU/GPU/FPGA) with fixed time budgets.

10. **Mobility and sensing freshness coupling is under-explored.**  
    Metric bottleneck: BER/outage spikes under speed changes. Evidence: `O_ISAC_098` shows performance loss when motion changes within refresh slots.  
    Deliverable: scheduling with age-of-sensing-information and predictive beam updates.

11. **Cell-free optical O-ISAC needs dedicated ISAC-level formulations.**  
    Metric bottleneck: interference and localization consistency in dense deployments. Evidence: cell-free VLC is reported (`O_ISAC_303`) but ISAC-specific co-design formulations remain sparse.  
    Deliverable: cell-free O-ISAC models with joint AP clustering, sensing fusion, and user assignment.

12. **RIS/OPA coordination across multiple panels lacks optical-native protocols.**  
    Metric bottleneck: scalability and control conflicts in large arrays. Evidence: `O_ISAC_127` flags hierarchical/distributed coordination as a future necessity.  
    Deliverable: multi-panel coordination protocol with stability guarantees and bounded signaling overhead.

13. **Benchmark suites for networked optical O-ISAC are not yet unified.**  
    Metric bottleneck: reproducible comparison of cross-layer gains. Evidence: heterogeneous KPI sets across `O_ISAC_061/091/098/009/054/112/127/303`.  
    Deliverable: open benchmark package with standardized scenarios, KPIs, and baseline stacks `[TODO: evidence needed]`.

14. **Joint networked coupling indicators remain inconsistent.**  
    Metric bottleneck: unified communication-sensing efficiency assessment. Evidence: Section-I style \(\mathrm{CRQ}_{\Delta}\) is available conceptually, but networked papers rarely provide comparable definitions under identical setup constraints.  
    Deliverable: report \(\sum_k R_{k,\mathrm{eff}}\) under explicit sensing RMSE (or CRB) constraints, plus confidence intervals.

**VI-E takeaway.**  
The current optical corpus confirms that multi-user and network-aware O-ISAC is technically feasible, with concrete progress in OPA multi-UE optimization, OIRS mobility-aware control, and pilot-overhead-aware VLC designs. The literature converges on the same structural bottlenecks: interference from narrow-beam spatial ambiguity, alignment and synchronization overhead, and timing feasibility against channel dynamics. Strong implementation evidence now exists for latency-aware adaptive control, but mostly in narrow scenario classes rather than standardized network benchmarks. Cross-layer formulations are increasingly explicit, yet fronthaul/backhaul and fairness reporting remain comparatively under-specified. The near-term priority is therefore an overhead-normalized benchmarking contract that joins PHY/MAC/fusion/control metrics within one reproducible evaluation pipeline. Without that contract, network-level claims will remain difficult to compare across optical modalities and deployment assumptions.

**TODO (VI-E missing evidence / metrics)**
- `[TODO: evidence needed]` Cross-paper fairness metrics (e.g., Jain index) are seldom disclosed in optical networked O-ISAC studies.
- `[TODO: evidence needed]` Fronthaul/backhaul latency and control signaling loads are largely absent in extracted optical corpus lines.
- `[TODO: evidence needed]` Cooperative sensing fusion under explicitly correlated impairments (shared clutter/turbulence) is not sufficiently quantified.
- `[TODO: evidence needed]` A unified, publicly released networked O-ISAC benchmark suite with standardized overhead fields is still missing.
- `[TODO: evidence needed]` Common definitions for network-level coupling indicators (beyond per-paper bespoke metrics) remain limited.

---

**VI-F Artifact Map**
- `ROOT_DIR`: `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST`
- **Alignment source (notation/taxonomy):** `drafts/section_01_introduction.md`
  - Preserved notation: `B_eff`, `R`, `\Delta r_{\min}`, `\sigma_r`, `SNR`, `BER`, `CRB`, `\mathrm{CRQ}_{\Delta}`.
  - Preserved modality boundaries: Fiber / FSO / VLC-LiFi / Photo-THz.
- **TOC/scope detection:**
  - `paper_outline.md` was not found in the workspace.
  - Section VI-F is instantiated with default scope and explicit **MODE C (Hybrid AI + Security)**.
- **MODE C keyword set used:**
  - AI/ML set: `learning-based`, `DRL`, `policy`, `federated`, `transfer learning`, `domain shift`, `sample efficiency`, `latency`, `complexity`.
  - Security set: `secrecy rate`, `wiretap`, `jamming`, `authentication`, `privacy`, `trust`, `adversarial`, `attack surface`, `RIS security`.
- **Primary VI-F extraction artifacts:**
  - `analysis/VI_ev_v2/section6F_dual_view_report.md` (MD; dual-view audit statistics for OPA/RIS/ML flags).
  - `analysis/VI_ev_v2/s6f_dual_view_ex.csv` (CSV; paper-id groups for flag-only/supported-only analyses).
  - `analysis/VI_ev_v2/s6f_dual_view_cmp.csv` (CSV; aggregate counts).
- **Primary corpus files mined for VI-F:**
  - `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md`
  - `data/proc_markdowns/O_ISAC_039/O_ISAC_039/O_ISAC_039.md`
  - `data/proc_markdowns/O_ISAC_145/O_ISAC_145/O_ISAC_145.md`
  - `data/proc_markdowns/O_ISAC_163/O_ISAC_163.md`
  - `data/proc_markdowns/O_ISAC_156/O_ISAC_156/O_ISAC_156.md`
  - `data/proc_markdowns/O_ISAC_068/O_ISAC_068.md`
  - `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md`
  - `data/proc_markdowns/O_ISAC_030/O_ISAC_030.md`
  - `data/proc_markdowns/O_ISAC_041/O_ISAC_041.md`
  - `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md`
  - `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md`
- **Ranked candidate paper_ids for VI-F (MODE C):**
  1. `O_ISAC_127` - strongest hybrid AI+security evidence with explicit latency, robustness, secrecy, and energy metrics.
  2. `O_ISAC_145` - strongest formal secrecy-rate/SEE optimization backbone with convergence and complexity discussion.
  3. `O_ISAC_039` - strongest optical FL/MTL co-design with CRLB/FIM and nonstationary adaptation evidence.
  4. `O_ISAC_163` - strongest RIS attack surface and authentication/pilot-overhead security framing.
  5. `O_ISAC_156` - strongest PLS taxonomy and assumptions/limitations framing spanning OWC/VLC/FSO/THz + JCAS.
  6. `O_ISAC_030` - explicit adversarial domain adaptation evidence for visible-light ISAC robustness.
  7. `O_ISAC_303` - LiSAC-level evidence on security differences and localization-assisted overhead reduction.
  8. `O_ISAC_068` - explicit security/privacy/interference challenges and integrated-protocol direction.
  9. `O_ISAC_041` - implementation-aware optical ISAC with real-time ML recognition KPIs.
  10. `O_ISAC_112` - optical IRS localization algorithms with complexity-performance trade-offs.

**VI-F Evidence Table**

| claim_id | claim | paper_id(s) | excerpt (<=2 sentences) | locator (heading + line range or page) | extracted variables/KPIs |
|---|---|---|---|---|---|
| VF01 | RIS-UOWC is explicitly co-designed with LSTM+DRL+NSGA-II. | O_ISAC_127 | "...adaptive framework integrating: Long Short-Term Memory (LSTM)... Deep Reinforcement Learning (DRL)... and ... NSGA-II..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:23` | model family: LSTM/DRL/evolutionary optimization |
| VF02 | Joint gains include BER reduction, secrecy-rate and energy gains. | O_ISAC_127 | "...41.4% reduction in BER... secrecy rate of 8.2 bps/Hz, 22.2% energy savings..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:23` | BER, `R_s=8.2` bps/Hz, energy saving 22.2% |
| VF03 | Nonstationary channel adaptation is tied to coherence-time constraints. | O_ISAC_127 | "...coherence time (\(\tau_c\)) is often under 100 ms..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:39` | `\tau_c<100 ms` (conservative regime) |
| VF04 | Closed-loop latency is experimentally decomposed by pipeline stage. | O_ISAC_127 | "...LSTM inference (12.3 ms), DRL control (18.7 ms), NSGA-II optimization (6.7 ms), and RIS actuation (9.6 ms)... total ... 47.3 ms..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:505` | per-stage latency, total 47.3 ms |
| VF05 | Complexity classes are explicitly provided for learning/optimization modules. | O_ISAC_127 | "...LSTM ... \(O(Tn_h^2)\)... DRL-NSGA-II ... \(O(NP^2)\)..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:501` and `:511` | `O(Tn_h^2)`, `O(NP^2)` |
| VF06 | Sim-to-measurement fidelity under dynamic channels is quantified. | O_ISAC_127 | "...experimental values closely align with simulation predictions, with deviations... below 8%." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:533` | measurement deviation <8% |
| VF07 | Large RIS scaling is explicitly limited by synchronization/processing latency. | O_ISAC_127 | "...scalability beyond 512 RIS elements introduces synchronization and processing latency..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:551` | threshold at >512 elements |
| VF08 | Transfer learning is explicitly used for cross-region generalization. | O_ISAC_127 | "...validated using salinity datasets from the Mediterranean Sea... LSTM maintained an 82% prediction accuracy without retraining..." | `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md:571` | transfer-learning accuracy 82% |
| VF09 | VIPAC jointly models positioning and channel estimation via MTL. | O_ISAC_039 | "...VIPAC framework... positioning... and channel estimation... integrated into a unified architecture..." | `data/proc_markdowns/O_ISAC_039/O_ISAC_039/O_ISAC_039.md:9` | joint task definition |
| VF10 | Federated multi-user training is introduced for nonstationary optical environments. | O_ISAC_039 | "...federated learning technique ... improve the generalization ability in spatiotemporally nonstationary environments while preserving data privacy." | `data/proc_markdowns/O_ISAC_039/O_ISAC_039/O_ISAC_039.md:9` | FL, privacy, generalization |
| VF11 | VIPAC shares pilots and sparse features to improve resource efficiency. | O_ISAC_039 | "...pilot subcarriers are also shared to implement the two tasks simultaneously, which greatly saves the spectrum resources..." | `data/proc_markdowns/O_ISAC_039/O_ISAC_039/O_ISAC_039.md:44` | pilot/resource reuse |
| VF12 | Estimation-theoretic lower bounds are derived for both tasks. | O_ISAC_039 | "...the CRLB of channel estimation..." and "...the CRLB of the estimated distance..." | `data/proc_markdowns/O_ISAC_039/O_ISAC_039/O_ISAC_039.md:359` and `:402` | CRLB/FIM-based sensing-comm bounds |
| VF13 | Channel-estimation gain is quantified as >10 dB SNR under target NMSE. | O_ISAC_039 | "...at the target NMSE of \(7 \times 10^{-3}\)... achieves an SNR gain of greater than 10 dB..." | `data/proc_markdowns/O_ISAC_039/O_ISAC_039/O_ISAC_039.md:649` | SNR gain >10 dB |
| VF14 | Positioning reaches centimeter-level under both MTL and MTFL studies. | O_ISAC_039 | "...positioning error of 6.72 cm at the SNR of 35 dB..." and "...finally converges to 6.77 cm..." | `data/proc_markdowns/O_ISAC_039/O_ISAC_039/O_ISAC_039.md:675` and `:709` | 6.72 cm, 6.77 cm |
| VF15 | MTFL adapts after environment switches while centralized MTL degrades. | O_ISAC_039 | "...MTFL scheme can reduce rapidly again... while the MTL scheme cannot adapt... positioning error ... increases to 196.0 cm..." | `data/proc_markdowns/O_ISAC_039/O_ISAC_039/O_ISAC_039.md:723` | domain-shift adaptation behavior |
| VF16 | A secrecy-energy metric is explicitly introduced for optical/hybrid links. | O_ISAC_145 | "...introduces Secrecy Energy Efficiency (SEE) ... quantify secure communication under power-constrained conditions." | `data/proc_markdowns/O_ISAC_145/O_ISAC_145/O_ISAC_145.md:9` | SEE metric definition |
| VF17 | Non-convex secrecy/SEE optimization is solved with SFP + Dinkelbach. | O_ISAC_145 | "...sequential fractional programming..." and "...can be solved by Dinkelbach's algorithm." | `data/proc_markdowns/O_ISAC_145/O_ISAC_145/O_ISAC_145.md:315` and `:474` | algorithmic pipeline |
| VF18 | Convergence and optimality guarantees are stated (KKT point). | O_ISAC_145 | "...Algorithm 1 is provably convergent to a point that fulfils the KKT optimality conditions..." | `data/proc_markdowns/O_ISAC_145/O_ISAC_145/O_ISAC_145.md:422` | convergence/KKT claim |
| VF19 | Numerical SEE benchmark is around 3 bit/Hz/J for NIR. | O_ISAC_145 | "...SEE peak for NIR is approximately 3 bit/Hz/Joule..." | `data/proc_markdowns/O_ISAC_145/O_ISAC_145/O_ISAC_145.md:590` | SEE~3 bit/Hz/J |
| VF20 | Optimized power allocation materially outperforms random allocation. | O_ISAC_145 | "...Algorithm 1 provides higher SEE levels than other schemes..." | `data/proc_markdowns/O_ISAC_145/O_ISAC_145/O_ISAC_145.md:600` | optimization gain vs random |
| VF21 | RIS security cannot be treated as optional and includes false-RIS/privacy threats. | O_ISAC_163 | "...successful integration of RIS... will largely depend on its security..." and "...false MF-RIS attack..." | `data/proc_markdowns/O_ISAC_163/O_ISAC_163.md:134` and `:520` | threat model: false-RIS/jamming/privacy |
| VF22 | Continuous authentication mechanisms for RIS controllers are explicitly proposed. | O_ISAC_163 | "...necessary to connect an MF-RIS to the network to ensure its continuous authentication and secure operation..." | `data/proc_markdowns/O_ISAC_163/O_ISAC_163.md:524` | authentication link design |
| VF23 | Pilot-overhead bottlenecks and two-timescale channel estimation are explicitly discussed. | O_ISAC_163 | "...pilot overhead can be excessively large..." and "...two-timescale channel estimation methodology." | `data/proc_markdowns/O_ISAC_163/O_ISAC_163.md:542` and `:544` | pilot overhead, two-timescale CE |
| VF24 | AI/ML inclusion is itself a security-risk amplifier in next-generation systems. | O_ISAC_156 | "...inclusion of machine learning (ML) and artificial intelligence (AI) algorithms ... expose an additional surface for predatory attackers..." | `data/proc_markdowns/O_ISAC_156/O_ISAC_156/O_ISAC_156.md:191` | attack-surface expansion |
| VF25 | Secrecy-capacity formulations are acknowledged to rely on restrictive assumptions. | O_ISAC_156 | "...Secrecy capacity-based PLS is founded assuming that the legitimate channel is always greater than the illegitimate (wiretap) one..." | `data/proc_markdowns/O_ISAC_156/O_ISAC_156/O_ISAC_156.md:199` | modeling limitation |
| VF26 | Optical modalities (OWC/VLC/FSO/THz) are explicitly included in PLS-for-JCAS scope. | O_ISAC_156 | "...cutting-edge technologies ... RIS, optical wireless communications (OWC); i.e., VLC, FSO; THz ... JCAS..." | `data/proc_markdowns/O_ISAC_156/O_ISAC_156/O_ISAC_156.md:210` | modality/threat taxonomy scope |
| VF27 | VL-JCS highlights security/privacy/interference and calls for integrated protocols. | O_ISAC_068 | "...challenges include standardization, privacy, security, interference..." and "...integrated protocols ... reduce overhead..." | `data/proc_markdowns/O_ISAC_068/O_ISAC_068.md:9` and `:105` | challenge classes, overhead coupling |
| VF28 | LiSAC reports security-overhead coupling and CSI reduction via localization. | O_ISAC_303 | "Wi-Fi ... lacks a security guarantee..." and "CSI is estimated based on localization ... reduce the system overhead significantly." | `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md:420` and `:268` | security baseline contrast, overhead reduction |
| VF29 | Adversarial domain adaptation is explicitly used for VLC-ISAC robustness. | O_ISAC_030 | "...adversarial learning technique to distill only the features relevant to hand gestures..." and "...average accuracy of all cross-scene results ... are over 85%..." | `data/proc_markdowns/O_ISAC_030/O_ISAC_030.md:5` and `:258` | domain adaptation, cross-scene robustness |
| VF30 | Real-time optical ISAC with ML is validated at high recognition accuracy. | O_ISAC_041 | "...real-time classification..." and "...99.7% ... 97.7% ... 98%..." | `data/proc_markdowns/O_ISAC_041/O_ISAC_041.md:5` | 99.7/97.7/98% KPIs |
| VF31 | Optical IRS localization includes explicit algorithmic complexity and accuracy trade-off. | O_ISAC_112 | "...algorithmic complexity ... cumulative complexity of both the offline stage ... and the online stage." | `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md:371` | FLOP-oriented complexity model |
| VF32 | IM/DD nonnegativity constraints remain active in optical O-ISAC models. | O_ISAC_054 | "...IM/DD ... [requires] introducing a dc bias ... ensure the signal remains nonnegative." | `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md:128` | nonnegativity/optical power constraints |

**Table VI-F.1A. Learning Paradigms Used for O-ISAC Optimization (MODE C: AI View)**

| paper_id | learning type | input features/state | outputs/actions | objective | constraints modeled | complexity/latency notes | reported gains |
|---|---|---|---|---|---|---|---|
| O_ISAC_127 | LSTM + DRL + evolutionary MO (NSGA-II) | salinity/turbulence context, channel state, noise regime | RIS phase updates, power-security operating point | minimize BER, maximize secrecy rate and energy efficiency | coherence-time budget, RIS quantization, actuation delay | `O(Tn_h^2)` and `O(NP^2)`; 47.3 ms end-to-end | BER -41.4%, `R_s=8.2` bps/Hz, energy +22.2% |
| O_ISAC_039 | Supervised MTL | sparse pilot/CIR features | joint channel estimate + position estimate | joint estimation accuracy improvement | sparse channel structure, pilot budget | depth-adaptive shared net; theoretical CRLB analysis | >10 dB SNR gain at target NMSE |
| O_ISAC_039 | Federated MTL (MTFL) | local UE datasets across clusters/time | global model weights | nonstationary generalization + privacy preservation | non-IID local data, communication rounds | iterative rounds with convergence analysis | NMSE `1.3e-3`; adapts after environment switching |
| O_ISAC_030 | CNN + adversarial domain adaptation | reflected VLC intensity carriers from multiple surfaces | gesture class and domain-invariant embedding | cross-scene robustness under concurrent VLC | table-surface domain shift | feature extractor + GRL + discriminator | >85% average cross-scene accuracy |
| O_ISAC_041 | Classical ML (RF/SVM/NB/KNN) | OTDR/FFT/WPD extracted features | co-route and event class labels | real-time identification and warning | online operation constraints | ML favored for faster response than DL | 99.7%/97.7%/98% task accuracies |
| O_ISAC_112 | DE-WI + WKNN (data-driven localization) | fingerprint matrix/tensor RSS maps | user location estimate | minimize localization PE | IRS topology, K-nearest selection | explicit offline+online complexity formulas | IRSPad improves average PE vs IRSPba |
| O_ISAC_303 | MTL/FL LiSAC framing (surveyed evidence) | positioning + CSI context | unified VIPAC estimation outputs | overhead-reduced integrated C&S | pilot and CSI estimation burden | CRLB and achievable-rate analyses cited | localization-assisted CSI reduces overhead |
| O_ISAC_068 | ML-assisted VLS/VL-JCS direction | multimodal optical sensing context | perception/classification and control support | improve low-latency closed-loop operation | protocol and synchronization coupling | architecture-level evidence; KPI granularity limited | identifies low-latency closed-loop potential |
| O_ISAC_145 | Optimization-driven (SFP, Dinkelbach) with ML-oriented extension notes | channel/secrecy-energy parameters | power allocation across optical/RF and jamming links | maximize SEE and secrecy rate | common power budget, non-convex fractional structure | converges to KKT; polynomial subproblem complexity | NIR SEE ~3 bit/Hz/J; optimized > random |
| O_ISAC_163 | Surveyed learning-assisted CE trends in RIS security context | high-dimensional cascaded channels | extrapolated channel estimates | reduce pilot burden under mobility | pilot overhead and nonstationarity | deep-learning extrapolation reported as overhead mitigation | reduced pilot signaling direction identified |
**Table VI-F.1B. Threat Models and Defenses in O-ISAC Literature (MODE C: Security View)**

| paper_id | adversary model | attack surface | defended layer | security metric | sensing impact | comm impact | overhead | evidence excerpt |
|---|---|---|---|---|---|---|---|---|
| O_ISAC_127 | dynamic eavesdropper + adverse channel | RIS-controlled optical link | PHY + control loop | secrecy rate, BER | robust sensing-state prediction required | secure throughput preserved under turbulence | latency budgeted to coherence time | "...dynamic eavesdropper locations..."; 8.2 bps/Hz |
| O_ISAC_145 | passive eavesdropper + intentional jammer | optical and hybrid power allocation | PHY (wiretap/jamming) | `R_s`, SEE | sensing not primary in this paper | optimized secrecy-energy operating point | optimization iterations and control complexity | SEE and secrecy maximization via SFP |
| O_ISAC_163 | false MF-RIS attack, jamming, privacy leakage | RIS controller/network interface | PHY + control/authentication plane | secrecy-oriented PLS indicators (surveyed) | mobility tracking data can leak | core-link compromise risk | continuous authentication mechanisms required | false-RIS attack and privacy threat statements |
| O_ISAC_156 | spoofing/intrusion/Sybil/jamming classes | IoT PHY channels incl. optical | PLS confidentiality/authentication/malicious-node detection | secrecy capacity, PLA metrics | JCAS context noted | keyless PLS versus key-based trade-off | implementation assumptions highlighted | broad PLS taxonomy with OWC/JCAS |
| O_ISAC_039 | privacy leakage from centralized data collection | training data and localization traces | learning/training plane | privacy preservation (FL design target) | positioning data protected by local training | generalization improved without raw data sharing | communication rounds in FL | local data are not shared; privacy preserved |
| O_ISAC_303 | comparative security weakness of RF baseline | network technology choice and CSI workflow | system architecture | qualitative security guarantee comparison | localization aids CSI for sensing-comm coupling | overhead can be reduced by localization-aided CSI | pilot overhead reduced by CSI-from-localization | Wi-Fi lacks guarantee; VLC advantage stated |
| O_ISAC_068 | privacy/security/interference in VL-JCS | protocol and integration layers | protocol/cross-layer | challenge-level risk statements | sensor-fusion trust and sync issues | interference and protocol inefficiency | integrated protocols target overhead reduction | challenge taxonomy explicitly includes security/privacy |
| O_ISAC_030 | non-malicious but severe domain shift (robustness threat) | sensing feature distribution across scenes | model robustness layer | cross-scene accuracy | sensing performance collapses without adaptation | VLC traffic still supported | added model complexity via adversarial training | adversarial domain adaptation improves robustness |
| O_ISAC_041 | sudden fault/vibration events threatening service continuity | optical transport sensing plane | operations and fault-alert layer | recognition accuracy, NAR | event detection quality determines warning reliability | improves survivability of communication services | real-time warning pipeline required | co-route/event recognition in real-time |
| O_ISAC_112 | LoS blockage/occlusion risk in IRS localization | optical propagation geometry | localization/sensing layer | PE/CDF metrics | wall/corner errors and blockage sensitivity | indirect impact through CSI/localization quality | two-step localization raises complexity | two-step IRS strategy reduces high-PE regions |

**Table VI-F.2. Limitations and Failure Modes (MODE C, Evidence-Grounded)**

| limitation class | observed in literature (paper_ids) | quantitative symptom (which KPI degrades) | mitigation attempt (paper_ids) | remaining gap |
|---|---|---|---|---|
| data scarcity / narrow-domain training | O_ISAC_127, O_ISAC_039, O_ISAC_030 | prediction/generalization degrades under unseen environments; cross-scene accuracy drops | transfer learning, MTFL online updates, adversarial domain adaptation (O_ISAC_127, O_ISAC_039, O_ISAC_030) | public benchmark splits for domain shift are missing `[TODO: evidence needed]` |
| domain shift / nonstationarity | O_ISAC_127, O_ISAC_039 | model mismatch after environment switching; centralized model error spikes | MTFL and transfer-learning adaptation (O_ISAC_039, O_ISAC_127) | no unified domain-shift protocol across optical modalities `[TODO: evidence needed]` |
| imperfect CSI/SSI and pilot burden | O_ISAC_163, O_ISAC_303 | pilot overhead inflation, stale estimates, BER/outage sensitivity | two-timescale CE and localization-assisted CSI (O_ISAC_163, O_ISAC_303) | overhead normalized as bits/symbol/frame is rarely reported `[TODO: evidence needed]` |
| adversarial/security risk under programmable surfaces | O_ISAC_163, O_ISAC_156, O_ISAC_145 | secrecy degradation and potential core-network compromise under false-RIS/jamming/eavesdropping | authentication links, PLS optimization, secrecy-energy co-design (O_ISAC_163, O_ISAC_145) | optical O-ISAC attack testbeds with reproducible protocols are sparse `[TODO: evidence needed]` |
| compute/latency budget mismatch | O_ISAC_127, O_ISAC_041, O_ISAC_112 | if `T_update` approaches channel dynamics scale, adaptation quality drops | edge execution, modular ML pipeline, complexity-aware algorithm design (O_ISAC_127, O_ISAC_041, O_ISAC_112) | cross-paper hardware-normalized runtime comparison is absent `[TODO: evidence needed]` |
| optical constraints (IM/DD, power, clipping/quantization) | O_ISAC_054, O_ISAC_127, O_ISAC_163 | nonnegativity/power/phase-control limits can distort ideal co-design gains | DC-bias IM/DD signaling, quantized RIS control, pilot-aware CE (O_ISAC_054, O_ISAC_127, O_ISAC_163) | joint AI+security optimization with full optical hardware constraints remains limited `[TODO: evidence needed]` |

## VI-F. AI/ML and Security-Aware O-ISAC: Learning-Driven Adaptation, Trust, Privacy, and Resilience

### VI-F.1 Motivation: Why VI-F Is an Enabling Pillar, Not an Accessory
The extracted corpus indicates that AI-enabled adaptation and security design are now structurally coupled in optical O-ISAC, rather than independent add-ons. In dynamic channels, learning-driven control can materially shift operating points: `O_ISAC_127` reports simultaneous BER, secrecy-rate, and energy improvements with explicit latency compliance to the channel coherence budget. In VLC-VLP integration, `O_ISAC_039` shows that multi-task and federated training improve channel/sensing estimation while preserving local data privacy in nonstationary settings. In parallel, `O_ISAC_145`, `O_ISAC_156`, and `O_ISAC_163` show that secrecy and trust assumptions (wiretap superiority, authentication continuity, attack surface under programmable RIS) directly bound what learning-driven control can safely deliver.
with $R_b$ and $R_e$ denoting legitimate and eavesdropper rates, respectively [O_ISAC_145], [O_ISAC_163]. A conservative robust framing is

Therefore, under MODE C, VI-F is treated as a coupled design space where adaptation quality and trust guarantees must be optimized jointly. The field is mature enough to support quantitative synthesis (e.g., secrecy rate, SEE, BER, latency, CRLB-linked estimation metrics), but still lacks unified reporting for cross-paper security-overhead costs and domain-shift robustness `[TODO: evidence needed]`.

### VI-F.2 Integrated Taxonomy (AI + Security)
An evidence-grounded integrated taxonomy can be organized along four axes.

1. **Learning paradigm and supervision regime.**
   Supervised MTL/MTFL (VIPAC) uses shared sparse channel features for positioning and channel estimation (`O_ISAC_039`), adversarial domain adaptation targets cross-scene robustness in VLC-ISAC (`O_ISAC_030`), and RL-centric adaptive control appears in RIS-UOWC with explicit stage-wise latency (`O_ISAC_127`). Complementary model-driven optimization (SFP/Dinkelbach) provides secrecy-energy guarantees and convergence for hybrid optical-RF settings (`O_ISAC_145`).

2. **Threat model and defended asset.**
   The corpus spans passive eavesdroppers and active jamming (`O_ISAC_145`), false-RIS/controller-level attacks and privacy leakage from mobility tracking (`O_ISAC_163`), and broader PLS confidentiality-authentication-malicious-node classes (`O_ISAC_156`). Security limitations are not only cryptographic; they also include estimation/control-plane vulnerabilities.

3. **Feature/action spaces under optical constraints.**
   Feature spaces include channel/pilot/CIR tensors, sensing trajectories, and environmental context (salinity/turbulence in UOWC). Action spaces include RIS phase control, power allocation, and task-coupled estimation parameters (`O_ISAC_127`, `O_ISAC_039`, `O_ISAC_112`). IM/DD nonnegativity and optical power constraints remain active when LED/VLC links are involved (`O_ISAC_054`).

4. **Deployment regime and robustness objective.**
   Some works are algorithmic/theory-heavy (`O_ISAC_145`, `O_ISAC_156`, `O_ISAC_163`), while others include implementation-grade evidence with real datasets or prototypes (`O_ISAC_127`, `O_ISAC_041`, `O_ISAC_030`). Across both groups, domain shift and overhead are recurrent bottlenecks (`O_ISAC_039`, `O_ISAC_303`, `O_ISAC_068`).
### VI-F.3 Unified Analytical Framework and Limits
We define uncertain environment state as `\omega` (channel, mobility, interference, and adversarial context), and design variables as `u` (beam/waveform/power/schedule/pilot/security controls). A generic coupled objective is
$$
\max_{u\in\mathcal{U}}\; \alpha\,\mathcal{C}(u;\omega) + (1-\alpha)\,\mathcal{S}(u;\omega),\quad \alpha\in[0,1],
$$
where `\mathcal{C}` is communication utility (e.g., `R` or `R_{\mathrm{eff}}`) and `\mathcal{S}` is sensing utility (e.g., `-\mathrm{CRB}`, `-\mathrm{RMSE}`, or FIM-based score). This structure is consistent with multi-objective secure-energy co-design in `O_ISAC_145` and joint estimation-centric VIPAC design in `O_ISAC_039`.

For learning-based adaptation, policy parameterization is
$$
u^*(\omega)\approx \pi_{\theta}(\omega),
\max_{\mathbf{u}}\;\min_{a\in\mathcal A}\;\alpha R(\mathbf{u})+\beta R_s(\mathbf{u},a)-(1-\alpha-\beta)\,\mathrm{CRB}(\mathbf{u}),
$$
and, in RL form,
$$
\mathcal{M}=(\mathcal{S},\mathcal{A},P,r,\gamma),\quad
\nabla_{\theta}J(\theta)=\mathbb{E}\!\left[\nabla_{\theta}\log\pi_{\theta}(a|s)\,A^{\pi}(s,a)\right].
\alpha\ge 0,\;\beta\ge 0,\;\alpha+\beta\le 1,
$$
A practical reward template, aligned with extracted studies, is
$$
r_t = \alpha R_{\mathrm{eff}}(u_t) - (1-\alpha)\,\mathrm{RMSE}(u_t) - \lambda\,\mathcal{L}_{\mathrm{sec}}(u_t),
$$
where `\mathcal{L}_{\mathrm{sec}}` is a secrecy/attack-risk surrogate (`O_ISAC_127`, `O_ISAC_145`, `O_ISAC_163`).

Domain-shift sensitivity can be summarized as
$$
\Delta_{\mathrm{dom}}(\theta)=\mathbb{E}_{p_{\mathrm{test}}}[\ell(\pi_\theta)]-\mathbb{E}_{p_{\mathrm{train}}}[\ell(\pi_\theta)].
$$
Empirically, `O_ISAC_039` and `O_ISAC_127` show that online FL updates and transfer-learning steps can reduce this gap in nonstationary scenarios.
where $\mathbf{u}$ includes transmitter and ORIS controls from Model VI-U [O_ISAC_127], [O_ISAC_145], [O_ISAC_163]. This form captures the central design tension: performance gains from adaptation must be preserved under attack and uncertainty, not only under nominal channels [O_ISAC_156], [O_ISAC_163].

For security-theoretic coupling, we use the standard wiretap template:
$$
R_s=[C_b-C_e]^+,
\qquad
P_{s,\mathrm{out}} = \Pr(R_s < R_{s,\mathrm{th}}).
$$
`O_ISAC_145` further introduces secrecy-energy efficiency,
$$
\mathrm{SEE}=\frac{R_s}{\mu P + P_c},
$$
and solves non-convex variants with SFP + Dinkelbach under KKT-convergent procedures.

Communication-sensing-security coupling under overhead can be written as
$$
R_{\mathrm{eff}} = \left(1-\frac{\tau_{\mathrm{oh}}}{\tau_{\mathrm{frame}}}\right)R,
$$
where `\tau_{\mathrm{oh}}` includes pilot, control, and authentication overhead (`O_ISAC_163`, `O_ISAC_303`, `O_ISAC_068`). On the sensing side,
$$
\mathrm{Var}(\hat{\theta})\succeq \mathbf{J}(\theta;u)^{-1},
$$
with practical range-resolution ties to Section-I notation through `\Delta r_{\min}`. In current VI-F corpus, direct `\mathrm{CRQ}_{\Delta}=R/\Delta r_{\min}` reporting is rare `[TODO: evidence needed]`.

Finally, feasibility requires latency and optical hardware compliance:
$$
T_{\mathrm{update}}\ll T_c,
$$
supported by explicit 47.3 ms closed-loop evidence in `O_ISAC_127`, and by IM/DD nonnegativity/optical power constraints (`O_ISAC_054`).

### VI-F.4 Comparative Synthesis (Tables VI-F.1A, VI-F.1B, VI-F.2)
Table VI-F.1A indicates that optical O-ISAC learning practice is bifurcating into two families: (i) direct adaptive-control pipelines with explicit runtime/latency decomposition (`O_ISAC_127`, `O_ISAC_041`) and (ii) estimation-centric learning formulations with stronger theoretical bounds (`O_ISAC_039`, `O_ISAC_112`). The former provides deployment evidence but narrower scenario coverage; the latter provides analytical clarity but weaker implementation disclosures.

Table VI-F.1B shows that threat modeling is currently strongest in RIS/PLS-adjacent literature (`O_ISAC_145`, `O_ISAC_156`, `O_ISAC_163`), while explicit optical ISAC experiments under active attacks remain limited. This asymmetry means many studies optimize adaptation without jointly auditing trust assumptions (authentication continuity, false-surface attacks, attack-aware overhead).

Table VI-F.2 reveals the dominant failure modes: domain shift, pilot/feedback burden, compute-latency mismatch, and incomplete benchmark contracts for adversarial evaluation. Hence, the current literature demonstrates that AI can improve performance and security can be optimized, but the co-verification of both under unified optical constraints remains structurally incomplete.
### VI-F.5 Open Challenges and Research Directions (Actionable)
1. **Domain-shift-robust policy design.**
   KPI bottleneck: `R`, BER, RMSE collapse under environment switches. Evidence: `O_ISAC_039` and `O_ISAC_127` report strong nonstationarity effects. Deliverable: benchmarked robust-policy training with explicit train/test distribution-shift protocols.

2. **Latency-bounded learning under coherence-time constraints.**
   KPI bottleneck: stale-control loss when `T_update` approaches `T_c`. Evidence: stage-wise 47.3 ms decomposition in `O_ISAC_127`. Deliverable: hard real-time schedulers coupling model size, inference path, and RIS actuation.

3. **Scalable multi-surface coordination.**
   KPI bottleneck: synchronization delay and secrecy degradation at larger RIS sizes. Evidence: >512-element bottleneck in `O_ISAC_127`. Deliverable: hierarchical/distributed control with provable stability and bounded signaling cost.

4. **Joint secrecy-sensing-communication KPI reporting.**
   KPI bottleneck: incomparable co-design claims across papers. Evidence: `O_ISAC_145` reports SEE and secrecy; most others omit unified coupling metrics. Deliverable: mandatory reporting of `R`, sensing RMSE/CRB, secrecy KPI, and overhead in one table.

5. **Adversarially robust optical learning loops.**
   KPI bottleneck: policy vulnerability to spoofed/false control states. Evidence: false-RIS and privacy risks in `O_ISAC_163`, AI attack-surface warning in `O_ISAC_156`. Deliverable: adversarial training and runtime anomaly detectors for control-plane integrity.

6. **Authentication overhead quantification for programmable optical surfaces.**
   KPI bottleneck: `R_eff` erosion and delayed updates. Evidence: continuous authentication need in `O_ISAC_163`. Deliverable: closed-form overhead models including authentication exchange periodicity.

7. **Pilot/feedback overhead-aware security co-design.**
   KPI bottleneck: throughput and outage under large pilot burdens. Evidence: pilot-overhead concerns in `O_ISAC_163`, localization-assisted reduction in `O_ISAC_303`. Deliverable: chance-constrained optimization with explicit pilot/security control budgets.

8. **Privacy-preserving federated optical ISAC benchmarks.**
   KPI bottleneck: privacy-risk versus adaptation performance trade-off remains unquantified. Evidence: privacy-preserving FL claim in `O_ISAC_039`. Deliverable: standardized FL benchmarks with privacy budgets and adaptation latency metrics.

9. **Cross-modal transferability across optical regimes (VLC/FSO/UOWC/fiber).**
   KPI bottleneck: poor portability of learned models. Evidence: cross-region transfer in `O_ISAC_127`; modality heterogeneity in `O_ISAC_156`. Deliverable: representation-learning pipelines with modality-shift calibration layers.

10. **Security-aware reward engineering in RL.**
    KPI bottleneck: policies optimize rate/sensing but ignore trust constraints. Evidence: secrecy-aware objectives in `O_ISAC_145` and attack-risk framing in `O_ISAC_163`. Deliverable: reward structures with explicit secrecy outage and authentication penalties.

11. **CRB/FIM integration with secure control.**
    KPI bottleneck: sensing guarantees decoupled from security constraints. Evidence: CRLB/FIM rigor in `O_ISAC_039`; secrecy optimization in `O_ISAC_145`. Deliverable: unified constrained formulations `\max R_s` s.t. `\mathrm{CRB}\le\delta`.

12. **Model explainability for mission-critical optical operation.**
    KPI bottleneck: low interpretability reduces trust in high-risk settings. Evidence: operational survivability framing in `O_ISAC_041`. Deliverable: interpretable policy auditing and confidence-calibrated decisions.

13. **Hardware-normalized complexity reporting.**
    KPI bottleneck: algorithm comparisons remain non-portable across hardware. Evidence: `O_ISAC_127` reports detailed latency, many papers report only asymptotic complexity. Deliverable: standardized runtime profile fields (device class, batch size, update interval).

14. **IM/DD-safe AI waveform/control families.**
    KPI bottleneck: physically infeasible learned actions under optical constraints. Evidence: IM/DD nonnegativity requirement in `O_ISAC_054`. Deliverable: constrained policy parameterizations that enforce optical feasibility by construction.

15. **Public attack-aware datasets for optical O-ISAC.**
    KPI bottleneck: weak reproducibility in security/robustness claims. Evidence: dataset-backed evaluations exist (`O_ISAC_127`, `O_ISAC_041`) but attack labels/protocols are not standardized. Deliverable: open datasets with benign/adversarial splits and synchronized sensing-communication traces.

16. **Unified benchmark protocol for MODE C studies.**
    KPI bottleneck: heterogeneous KPI definitions block fair comparison. Evidence: cross-paper inconsistency across `O_ISAC_127/039/145/163/303/068`. Deliverable: benchmark suite with fixed scenario templates, baselines, and confidence-interval reporting.

17. **Secure distributed edge intelligence for LiSAC control.**
    KPI bottleneck: centralized control fragility and latency accumulation. Evidence: distributed-intelligence direction in `O_ISAC_068`; FL multi-user structure in `O_ISAC_039`. Deliverable: edge-fusion protocols with authenticated model updates.

18. **Joint overhead-security accounting in standards discussions.**
    KPI bottleneck: practical adoption risk due to hidden control/security costs. Evidence: standardization need in `O_ISAC_068`; security dependence in `O_ISAC_163`. Deliverable: standards-oriented KPI template including secrecy outage, auth delay, and pilot share.

**VI-F takeaway.**
Current optical O-ISAC literature confirms that learning-driven adaptation can produce tangible gains in rate-reliability-security-energy metrics, particularly when latency is explicitly engineered and measured. The same corpus also shows that trust assumptions are fragile: false-surface attacks, privacy leakage, and pilot/control overhead can negate nominal algorithmic gains if not modeled in-loop. Estimation-theoretic and secrecy-theoretic foundations are individually mature, yet their unified deployment under optical hardware constraints is still uneven. Federated and transfer-learning directions are promising for nonstationary environments, but benchmark protocols for adversarial robustness and reproducibility remain incomplete. The field is therefore transitioning from isolated "AI-for-performance" and "security-for-protection" threads toward a single constrained co-design problem. Progress now depends on overhead-aware, attack-aware, and hardware-aware evaluation contracts shared across optical modalities.

**TODO (VI-F missing evidence / metrics)**
- `[TODO: evidence needed]` Covert communication metrics (e.g., warden detection error constraints) are not explicitly reported in the extracted optical O-ISAC lines.
- `[TODO: evidence needed]` Differential-privacy budgets and quantified privacy leakage are rarely disclosed for FL-based optical ISAC.
- `[TODO: evidence needed]` Cross-paper reporting of inference FLOPs, memory footprint, and end-to-end control jitter is inconsistent.
- `[TODO: evidence needed]` Direct reporting of `\mathrm{CRQ}_{\Delta}=R/\Delta r_{\min}` under identical setups is still sparse in VI-F candidate papers.
- `[TODO: evidence needed]` Reproducible optical attack testbeds with open scripts/datasets remain limited.
- `[TODO: evidence needed]` Unified standards-oriented KPI templates that jointly include sensing, communication, and security overhead are not yet established.
**Key takeaways and open problems.** Existing evidence supports AI-based performance improvements and security-aware optimization, but co-verification protocols are still immature for optical O-ISAC [O_ISAC_127], [O_ISAC_145], [O_ISAC_163]. The key methodological gap is missing standardized attack models with reproducible runtime and overhead accounting [O_ISAC_156], [O_ISAC_163]. An open problem is unified disclosure of adaptation latency, memory footprint, and secrecy-performance degradation under domain shift [O_ISAC_127], [O_ISAC_163]. Another open problem is integrating privacy and trust constraints into the same benchmark contract used for communication and sensing metrics [O_ISAC_156], [O_ISAC_163].