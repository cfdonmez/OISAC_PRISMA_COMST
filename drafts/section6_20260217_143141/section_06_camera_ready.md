# VI. Enabling Technologies and System-Level Co-Design for Optical ISAC

Section VI consolidates the enabling technologies and design principles that determine whether optical integrated sensing and communication (O-ISAC) can scale from proof-of-concept links to reproducible systems. The evidence in the corpus consistently shows that optical phased arrays (OPA), ORIS control, robustness-aware optimization, and network coordination are coupled design problems rather than independent modules [O_ISAC_008], [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112], [O_ISAC_127]. To keep the main narrative readable, detailed traceability notes and extended audit material are retained in the supplementary material rather than in the core manuscript text.

In this section, we use one canonical term: **ORIS (Optical Reconfigurable Intelligent Surface)**.

**Table VI-1. Unified Notation for Section VI.**

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

### VI-A. OPA and ORIS as Enabling Technologies

OPA and ORIS are the main physical enablers that make optical propagation programmable for joint sensing and communication. OPA studies report explicit joint-waveform and steering gains, while ORIS studies report alignment offloading and blockage mitigation through controlled reflected paths [O_ISAC_008], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112]. Model VI-U captures this common structure by representing both direct and ORIS-assisted paths in one expression [O_ISAC_061], [O_ISAC_091].

A compact steering anchor for OPA is

$$
AF(\theta)=\sum_{m=0}^{M-1} a_m\exp\!\left(j\left(kdm\sin\theta+\phi_m\right)\right),
$$
$$
\phi_m^{\star}=-kdm\sin\theta_0,
$$

which steers the main lobe toward $\theta_0$ when phase control is accurate [O_ISAC_008], [O_ISAC_061], [O_ISAC_091]. In practice, finite FoV receivers, spacing-dependent grating-lobe behavior, and channel impairments limit ideal steering gains, so array control and sensing quality must be co-optimized [O_ISAC_061], [O_ISAC_091], [O_ISAC_098].

**Key takeaways and open problems.** OPA evidence is strongest on beam agility and communication-sensing coupling, while ORIS evidence is strongest on alignment robustness and NLoS support [O_ISAC_008], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112]. Across modalities, quantized control, insertion loss, and refresh latency are repeatedly reported as practical bottlenecks [O_ISAC_098], [O_ISAC_127]. A near-term research priority is to report OPA and ORIS gains with a common tuple $(R,\mathrm{BER},\mathrm{CRB},\text{latency})$ under identical geometry and impairment settings [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Another open direction is model-consistent design under quantized ORIS control and nonstationary channels in a single optimization loop [O_ISAC_098], [O_ISAC_127].

### VI-B. Channel Impairments and Robustness Mechanisms

Robustness is a first-order requirement in O-ISAC because the same optical channel impairments degrade communication reliability and sensing fidelity simultaneously. The corpus repeatedly models end-to-end channel gain as a product of deterministic loss, atmospheric or medium turbulence, and pointing/misalignment components [O_ISAC_023], [O_ISAC_035], [O_ISAC_061], [O_ISAC_098], [O_ISAC_199].

A compact robustness anchor is

$$
H=H_l H_a H_p,
$$
$$
P_{\text{out}}=\Pr\!\left(\gamma(H)<\gamma_{\text{th}}\right)\le \varepsilon.
$$

This chance-constraint view links physical impairment statistics directly to reliability targets and is consistent with quantile-robust formulations used in optical ISAC optimization studies [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Practical mitigation then combines statistical robustness at design time with runtime adaptation (tracking, refresh control, and environment-aware reconfiguration) [O_ISAC_098], [O_ISAC_112], [O_ISAC_127], [O_ISAC_199].

**Key takeaways and open problems.** Turbulence, weather attenuation, and pointing jitter are now well represented in single-paper evaluations, but cross-paper outage definitions remain heterogeneous [O_ISAC_023], [O_ISAC_035], [O_ISAC_061], [O_ISAC_199]. Current evidence supports robustness-aware design, yet common reporting of confidence intervals and unified $P_{\text{out}}$ protocols is still limited [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. A concrete open problem is distributionally robust co-design that jointly handles $(H_a,H_p)$ uncertainty while preserving sensing CRB targets [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Another open problem is latency-coherence-aware robustness control in dynamic ORIS loops [O_ISAC_098], [O_ISAC_127].

### VI-C. Joint Co-Design and Resource Optimization

Joint co-design is needed because waveform, beam, and ORIS controls are coupled through shared physical constraints. In O-ISAC implementations with IM/DD links, feasible signaling must satisfy nonnegativity and optical power limits, which changes both algorithm design and achievable tradeoff surfaces [O_ISAC_009], [O_ISAC_023], [O_ISAC_054], [O_ISAC_061]. Model VI-U provides the shared variable structure for transmitter, ORIS, and sensing terms [O_ISAC_061], [O_ISAC_091], [O_ISAC_127].

A minimal feasible set and objective anchor are

$$
\mathcal U=\{x(t):x(t)\ge 0,\;\mathbb{E}[x(t)]\le \bar P,\;\max_t x(t)\le P_{\max}\},
$$
$$
\max_{\mathbf{w},\Theta,\,x\in\mathcal U}\;\alpha R(\mathbf{w},\Theta)-(1-\alpha)\,\mathrm{CRB}(\mathbf{w},\Theta),\quad \alpha\in[0,1].
$$

The weight $\alpha$ sets the communication-sensing operating point, and the formulation can be extended with reliability and update-latency constraints when channel dynamics are explicit [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127].

**Key takeaways and open problems.** Evidence is strongest for structured decomposition methods in OPA and DCO-OFDM settings and for adaptive multi-objective search under nonstationary underwater channels [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. The main gap is not the absence of optimization methods, but the absence of harmonized constraint disclosure (optical power, quantization, update period, and overhead terms) across papers [O_ISAC_009], [O_ISAC_023], [O_ISAC_061], [O_ISAC_127]. A priority open problem is solver-independent benchmark reporting for complexity-versus-performance tradeoffs under identical scenario contracts [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Another open problem is integrating explicit eye-safety constraints into the same objective stack when those limits are reported by the experimental setup [O_ISAC_054].

### VI-D. Prototyping, Benchmarking, and Standardization Gaps

The literature now includes both experimental demonstrations and simulation-heavy studies, but cross-paper comparability remains weak because scenario definitions and KPI contracts differ. Parameter tables and controlled simulation protocols are often present, yet baseline choices and reporting granularity are inconsistent across works [O_ISAC_023], [O_ISAC_035], [O_ISAC_054], [O_ISAC_061], [O_ISAC_091], [O_ISAC_112], [O_ISAC_127].

A minimal benchmark contract can be written as

$$
\mathbf{s}=\{d,\,C_n^2,\,\sigma_{\text{jitter}},\,\lambda,\,B,\,N_{\text{ORIS}},\,M_{\text{OPA}},\,\bar P,\,P_{\max},\,T_{\text{update}}\},
$$
$$
\mathbf{m}=(R,\,\mathrm{BER},\,\mathrm{CRB},\,P_{\text{out}},\,\text{latency},\,\text{energy}).
$$

The contract makes scenario assumptions explicit before interpreting gains and avoids comparing values measured under incompatible conditions [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127].

**Table VI-2. Recommended Reporting Checklist for Reproducible O-ISAC Experiments and Simulations.**

| Item | Minimum required fields | Why it matters |
|---|---|---|
| Scenario vector disclosure | Full $\mathbf{s}$ values, mobility profile, channel model family | Prevents hidden scenario drift across papers [O_ISAC_023], [O_ISAC_061], [O_ISAC_091] |
| KPI contract disclosure | Full $\mathbf{m}$ values with units and confidence intervals | Supports fair comparison of communication and sensing quality [O_ISAC_023], [O_ISAC_035], [O_ISAC_127] |
| Baseline taxonomy | At least one separated baseline and one practical baseline | Prevents inflated gains from weak references [O_ISAC_054], [O_ISAC_061], [O_ISAC_127] |
| Runtime and control budget | Solver runtime, $T_{\text{update}}$, hardware timing, feedback overhead | Distinguishes deployable from offline-only designs [O_ISAC_098], [O_ISAC_112], [O_ISAC_127] |
| Reproducibility package | Parameter files, script versions, data provenance, random seeds | Enables external replication and audit [O_ISAC_023], [O_ISAC_112], [O_ISAC_127] |
| Safety and operating envelope | Optical power settings and safety margin reporting method | Necessary for translation to certified deployments [O_ISAC_054], [O_ISAC_061] |

**Key takeaways and open problems.** The strongest immediate need is a shared benchmark contract rather than additional isolated case studies [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Current evaluations are often rigorous within each paper, but weakly aligned across papers for meta-comparison [O_ISAC_054], [O_ISAC_112], [O_ISAC_127]. Open problems include standardized outdoor validation protocols and unified control-overhead reporting under mobility [O_ISAC_098], [O_ISAC_127]. A second open problem is safety-aware benchmarking where power margins, sensing quality, and latency are reported together [O_ISAC_054], [O_ISAC_061].

### VI-E. Networked and Multi-User O-ISAC

Networked O-ISAC introduces coordination burdens that do not appear in single-link settings: multi-user interference, feedback overhead, and sensing-fusion consistency. The corpus reports explicit FoV and grating-lobe interference effects in multi-user OPA setups, tracking burden growth with user count in mobile ORIS systems, and protocol-level overhead sensitivity in VLC-based networked settings [O_ISAC_009], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_303].

A compact network objective anchor is

$$
\max_{\{\mathbf{w}_k\},\Theta}\;\sum_{k}\omega_k\log\!\left(1+\mathrm{SINR}_k\right)-\lambda\,\mathrm{CRB}(\Theta)
$$
$$
\text{s.t.}\quad \sum_k\|\mathbf{w}_k\|_2^2\le P,\quad \theta_n\in\mathcal Q.
$$

Using Model VI-U, this objective makes communication, sensing, and ORIS quantization constraints explicit in one multi-user program [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. The practical bottleneck is scaling control overhead: CSI refresh, scheduling updates, and feedback timing can dominate gains if not included in the optimization itself [O_ISAC_009], [O_ISAC_068], [O_ISAC_098], [O_ISAC_303].

**Key takeaways and open problems.** Multi-user OPA/ORIS designs show clear gains, but current studies rarely standardize network-level overhead metrics in a common unit system [O_ISAC_009], [O_ISAC_061], [O_ISAC_091], [O_ISAC_303]. Control-plane modeling and sensing-fusion policies are often analyzed separately, even though evidence indicates strong coupling under mobility [O_ISAC_068], [O_ISAC_098], [O_ISAC_127]. A near-term open problem is fairness-aware and latency-aware optimization with explicit reporting of control symbols, feedback bits, and scheduling delay [O_ISAC_009], [O_ISAC_303]. Another open problem is reproducible cooperative benchmark suites that vary PHY, MAC, and fusion policy jointly [O_ISAC_068], [O_ISAC_303].

### VI-F. AI/ML and Security-Aware O-ISAC

AI-assisted adaptation and security-aware design are increasingly coupled in O-ISAC, especially in dynamic channels where static policies underperform. The corpus reports learning-driven adaptation for nonstationary environments and complementary security formulations around secrecy, authentication, and resilience, but jointly validated AI-plus-security optical benchmarks remain limited [O_ISAC_127], [O_ISAC_145], [O_ISAC_156], [O_ISAC_163].

A compact secrecy anchor is

$$
R_s=[R_b-R_e]^+,
$$

with $R_b$ and $R_e$ denoting legitimate and eavesdropper rates, respectively [O_ISAC_145], [O_ISAC_163]. A conservative robust framing is

$$
\max_{\mathbf{u}}\;\min_{a\in\mathcal A}\;\alpha R(\mathbf{u})+\beta R_s(\mathbf{u},a)-(1-\alpha-\beta)\,\mathrm{CRB}(\mathbf{u}),
$$
$$
\alpha\ge 0,\;\beta\ge 0,\;\alpha+\beta\le 1,
$$

where $\mathbf{u}$ includes transmitter and ORIS controls from Model VI-U [O_ISAC_127], [O_ISAC_145], [O_ISAC_163]. This form captures the central design tension: performance gains from adaptation must be preserved under attack and uncertainty, not only under nominal channels [O_ISAC_156], [O_ISAC_163].

**Key takeaways and open problems.** Existing evidence supports AI-based performance improvements and security-aware optimization, but co-verification protocols are still immature for optical O-ISAC [O_ISAC_127], [O_ISAC_145], [O_ISAC_163]. The key methodological gap is missing standardized attack models with reproducible runtime and overhead accounting [O_ISAC_156], [O_ISAC_163]. An open problem is unified disclosure of adaptation latency, memory footprint, and secrecy-performance degradation under domain shift [O_ISAC_127], [O_ISAC_163]. Another open problem is integrating privacy and trust constraints into the same benchmark contract used for communication and sensing metrics [O_ISAC_156], [O_ISAC_163].
