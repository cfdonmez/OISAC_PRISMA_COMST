# VI. Enabling Technologies and System-Level Co-Design for Optical ISAC

Section VI explains how O-ISAC becomes practically realizable by linking enabling technologies to channel robustness, joint optimization, runtime overhead, and benchmarking discipline. Across the corpus, optical phased arrays (OPA), optical reconfigurable intelligent surfaces (ORIS), robustness-aware optimization, and network coordination appear as coupled levers rather than isolated modules [O_ISAC_008], [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112], [O_ISAC_127]. Accordingly, this section remains enabler-centric, but it interprets enablers through system-level feasibility rather than as a component catalog. To stay aligned with earlier sections, we preserve Section II measurement governance, reuse the Section IV medium/taxonomy framing, and keep the Section V governed-evidence caution visible when discussing maturity and prevalence.

Throughout this section, we use **ORIS (Optical Reconfigurable Intelligent Surface)** as the canonical umbrella term for optical RIS-style programmable surfaces. We also preserve one shared notation block so that OPA steering, ORIS-assisted links, robustness constraints, and multi-user optimization can be discussed without symbol drift across subsections.

**Table VI-1. Unified Notation for Section VI.**

| Symbol | Meaning | Used in |
|---|---|---|
| $x(t)$ | Optical transmit waveform or equivalent sampled signal | VI-C, VI-E |
| $\bar P$ | Average optical power budget | VI-C, VI-D |
| $P_{\max}$ | Peak optical power budget | VI-C, VI-D |
| $H$ | End-to-end channel coefficient or gain | VI-B |
| $H_l$ | Deterministic or path-loss component of $H$ | VI-B |
| $H_a$ | Atmospheric or medium-turbulence component of $H$ | VI-B |
| $H_p$ | Pointing or misalignment component of $H$ | VI-B |
| $\gamma$ | Instantaneous SNR or SINR proxy at the relevant detection plane | VI-B, VI-E |
| $\gamma_{\text{th}}$ | Reliability threshold for outage control | VI-B |
| $\varepsilon$ | Allowed outage probability target | VI-B, VI-C |
| $\Theta$ | ORIS diagonal response matrix | VI-A, VI-C, VI-E, VI-F |
| $\beta_n$ | ORIS amplitude coefficient of element $n$ | VI-A |
| $\theta_n$ | ORIS phase of element $n$ | VI-A, VI-E |
| $Q$ | Number of phase-quantization levels | VI-A, VI-E |
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
> Model VI-U is a compact abstraction reused across VI-A, VI-C, VI-E, and VI-F for notation consistency [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_127].

## VI-A. Programmable Optical Enablers

Programmable optical enablers matter because they convert optical propagation from a mostly fixed channel into a controllable channel. OPA studies expose transmit-side beam agility, angular selectivity, and joint waveform support, whereas ORIS studies expose environment-side path shaping, alignment assistance, and blockage mitigation through reflected or reconstructed paths [O_ISAC_008], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112]. This distinction is important: OPA and ORIS should be written as complementary control authorities rather than as interchangeable technologies.

A compact steering anchor for OPA is

$$
AF(\theta)=\sum_{m=0}^{M-1} a_m\exp\!\left(j\left(kdm\sin\theta+\phi_m\right)\right),
$$
$$
\phi_m^{\star}=-kdm\sin\theta_0,
$$

which steers the main lobe toward $\theta_0$ under accurate phase control [O_ISAC_008], [O_ISAC_061], [O_ISAC_091]. In practice, finite receiver FoV, grating-lobe behavior, insertion loss, and channel impairments prevent ideal steering gains from translating directly into reproducible O-ISAC gains [O_ISAC_061], [O_ISAC_091], [O_ISAC_098].

PIC and photonic-integration themes belong here only as enabling substrates beneath these control surfaces, not as a detached component inventory. At the current evidence level, Section VI should therefore treat PIC and photonic-generation themes conservatively unless they are directly anchored to measurable O-ISAC integration benefits. Likewise, prevalence language must remain cautious: structured metric traces for OPA/ORIS are broader than strong study-level evidence of deliberate co-design adoption.

**VI-A takeaway.** OPA evidence is strongest on beam agility and communication-sensing coupling, while ORIS evidence is strongest on alignment robustness and NLoS support. Across modalities, quantized control, insertion loss, and refresh latency remain practical bottlenecks. The most defensible near-term message is not that programmable optics are uniformly mature, but that they expose a rich and increasingly reusable optical control space.

## VI-B. Channel Impairments and Robustness

Robustness is a first-order concern in O-ISAC because the same optical channel impairments degrade communication reliability and sensing fidelity together. Across FSO, VLC, and hybrid optical settings, the literature repeatedly models end-to-end gain as a composition of deterministic loss, atmospheric or medium turbulence, and pointing or alignment components [O_ISAC_023], [O_ISAC_035], [O_ISAC_061], [O_ISAC_098], [O_ISAC_199]. This is the point where enabler value becomes conditional: a programmable surface or beam-steering mechanism is only useful insofar as it remains effective under the dominant impairment regime.

A compact robustness anchor is

$$
H=H_l H_a H_p,
$$
$$
P_{\text{out}}=\Pr\!\left(\gamma(H)<\gamma_{\text{th}}\right)\le \varepsilon.
$$

This chance-constrained view links physical impairment statistics directly to reliability targets and is consistent with quantile-robust formulations already used in optical ISAC optimization studies [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Practical mitigation then combines design-time robustness with runtime adaptation through tracking, refresh control, environment-aware reconfiguration, and fallback or diversity mechanisms [O_ISAC_098], [O_ISAC_112], [O_ISAC_127], [O_ISAC_199].

The prose here should stay medium-aware. Turbulence and weather attenuation dominate many FSO and hybrid scenarios, finite FoV and geometry dominate many VLC scenarios, and control latency cuts across most programmable optical platforms. Section VI therefore cannot write "robustness" as if one impairment model covers all optical modalities equally well.

**VI-B takeaway.** Current literature supports robustness-aware optical design, but cross-paper outage definitions and confidence reporting remain heterogeneous. The main open issue is no longer whether robustness matters, but how to compare robustness claims under common impairment and reporting contracts.

## VI-C. Joint Co-Design and Resource Optimization

Joint co-design is required because waveform, beam, power, and ORIS controls share physical constraints. In IM/DD implementations, feasible signaling must satisfy nonnegativity and optical power bounds, while coherent or programmable settings add quantization, steering, and update constraints [O_ISAC_009], [O_ISAC_023], [O_ISAC_054], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Model VI-U is useful here because it keeps transmitter, ORIS, and sensing terms in one variable structure.

A minimal feasible-set and objective anchor is

$$
\mathcal U=\{x(t):x(t)\ge 0,\;\mathbb{E}[x(t)]\le \bar P,\;\max_t x(t)\le P_{\max}\},
$$
$$
\max_{\mathbf{w},\Theta,\,x\in\mathcal U}\;\alpha R(\mathbf{w},\Theta)-(1-\alpha)\,\mathrm{CRB}(\mathbf{w},\Theta),\quad \alpha\in[0,1].
$$

The weight $\alpha$ sets the communication-sensing operating point and can be extended with reliability and latency constraints when channel dynamics are explicit [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. However, this subsection must preserve one important maturity caveat: Section VI contains more structured OPA/ORIS metric traces than strong study-level evidence of deliberate full-stack co-design adoption. It is therefore safer to say that the literature exposes a rich control space for co-design than to say that all metric-bearing OPA/ORIS studies already instantiate mature multi-objective O-ISAC design.

**VI-C takeaway.** Evidence is strongest for structured optimization in OPA and DCO-OFDM settings and for adaptive multi-objective control in dynamic underwater channels. The main gap is not the absence of optimization methods, but the absence of harmonized disclosure of constraints, runtime burden, and operating assumptions across papers.

## VI-D. Experimental Validation, Benchmarking, and Reporting Contract

The literature now contains both experimental demonstrations and simulation-heavy studies, but cross-paper comparability remains weak because scenario definitions, baselines, and KPI contracts differ. This makes benchmarking the hinge of Section VI: the earlier subsections show that the control space is rich, but this subsection explains why that richness does not automatically translate into cumulative scientific maturity [O_ISAC_023], [O_ISAC_035], [O_ISAC_054], [O_ISAC_061], [O_ISAC_091], [O_ISAC_112], [O_ISAC_127].

A minimal benchmark contract can be written as

$$
\mathbf{s}=\{d,\,C_n^2,\,\sigma_{\text{jitter}},\,\lambda,\,B,\,N_{\text{ORIS}},\,M_{\text{OPA}},\,\bar P,\,P_{\max},\,T_{\text{update}}\},
$$
$$
\mathbf{m}=(R,\,\mathrm{BER},\,\mathrm{CRB},\,P_{\text{out}},\,\text{latency},\,\text{energy}).
$$

The contract makes scenario assumptions explicit before gains are interpreted and prevents comparisons across incompatible operating conditions.

**Table VI-2. Recommended Reporting Checklist for Reproducible O-ISAC Experiments and Simulations.**

| Item | Minimum required fields | Why it matters |
|---|---|---|
| Scenario vector disclosure | Full $\mathbf{s}$ values, mobility profile, channel model family | Prevents hidden scenario drift across papers |
| KPI contract disclosure | Full $\mathbf{m}$ values with units and confidence intervals | Supports fair comparison of communication and sensing quality |
| Baseline taxonomy | At least one separated baseline and one practical baseline | Prevents inflated gains from weak references |
| Runtime and control budget | Solver runtime, $T_{\text{update}}$, hardware timing, feedback overhead | Distinguishes deployable from offline-only designs |
| Reproducibility package | Parameter files, script versions, data provenance, random seeds | Enables external replication and audit |
| Safety and operating envelope | Optical power settings and safety-margin reporting method | Necessary for translation to certified deployments |

**VI-D takeaway.** The strongest immediate need is a shared benchmark contract rather than more isolated case studies. Benchmark discipline is what turns promising enablers into cumulative evidence.

## VI-E. Networked and Multi-User O-ISAC

Networked O-ISAC introduces burdens that do not appear in single-link settings: multi-user interference, feedback overhead, sensing-fusion consistency, and coordination delay. The corpus already reports explicit FoV and grating-lobe interference effects in multi-user OPA settings, tracking burden growth with user count in mobile ORIS systems, and protocol-level overhead sensitivity in VLC-based networked settings [O_ISAC_009], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_303].

A compact network objective anchor is

$$
\max_{\{\mathbf{w}_k\},\Theta}\;\sum_{k}\omega_k\log\!\left(1+\mathrm{SINR}_k\right)-\lambda\,\mathrm{CRB}(\Theta)
$$
$$
\text{s.t.}\quad \sum_k\|\mathbf{w}_k\|_2^2\le P,\quad \theta_n\in\mathcal Q.
$$

This formulation makes communication, sensing, and ORIS quantization constraints explicit in one multi-user program [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. More importantly for the survey narrative, this subsection is where Section VI begins to connect directly to Section VII: once user count, fusion policy, fairness, and control overhead become dominant, the question is no longer whether an enabler exists but whether a deployment setting can absorb its coordination cost.

**VI-E takeaway.** Multi-user optical O-ISAC is now plausible in the literature, but network-level overhead metrics, control-plane timing, and cooperative benchmark contracts remain under-standardized.

## VI-F. AI/ML and Security-Aware Adaptation

AI-assisted adaptation and security-aware design are increasingly coupled in O-ISAC, especially in dynamic channels where static policies underperform. The literature reports learning-driven adaptation for nonstationary environments together with secrecy, authentication, and resilience formulations, but jointly validated AI-plus-security optical benchmarks remain limited [O_ISAC_127], [O_ISAC_145], [O_ISAC_156], [O_ISAC_163].

A compact secrecy and robust-control anchor is

$$
R_s=[R_b-R_e]^+,
$$
$$
\max_{\mathbf{u}}\;\min_{a\in\mathcal A}\;\alpha R(\mathbf{u})+\beta R_s(\mathbf{u},a)-(1-\alpha-\beta)\,\mathrm{CRB}(\mathbf{u}),
$$
$$
\alpha\ge 0,\;\beta\ge 0,\;\alpha+\beta\le 1,
$$

where $\mathbf{u}$ includes transmitter and ORIS controls inherited from Model VI-U [O_ISAC_127], [O_ISAC_145], [O_ISAC_163]. This framing captures the central tension of this subsection: adaptation gains are only meaningful if they survive uncertainty, overhead, and adversarial pressure rather than only nominal channels.

This is also the place where Section VI must keep maturity asymmetry visible. OPA and ORIS mechanics are presently better evidenced than long-horizon AI adaptation, trust, and adversarial robustness under reproducible protocols. That should be written as a maturity signal, not as a dismissal of the topic, because this distinction helps keep Section VIII grounded later in the manuscript.

**VI-F takeaway.** AI/ML and security already matter in optical O-ISAC, but current evidence is uneven and should be synthesized cautiously. The field still needs reproducible attack models, overhead-aware reporting, and benchmark-quality evaluation of adaptation under domain shift.

## Section VI Synthesis and Transition

Taken together, VI-A to VI-F suggest that the main bottleneck in optical ISAC is no longer the absence of promising enablers, but the absence of stable reporting and benchmarking contracts that let the community compare those enablers under common assumptions. OPA and ORIS broaden controllability, robustness models broaden survivability, optimization enlarges the design space, and AI/security layers extend adaptivity and trustworthiness. Yet without explicit disclosure of control overhead, update latency, benchmark assumptions, and sensing-quality definitions, these advances remain difficult to stack into a reproducible system narrative.

This framing gives Section VII a clean handoff: the next question is no longer "what enabling components exist?" but "which deployment patterns and application settings can absorb these coupled design choices in a defensible way?"
