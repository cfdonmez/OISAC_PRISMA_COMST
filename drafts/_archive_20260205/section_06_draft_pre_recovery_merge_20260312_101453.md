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
