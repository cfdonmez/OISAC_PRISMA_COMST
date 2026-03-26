# VI. Enabling Technologies and System-Level Co-Design for Optical ISAC

Section VI explains how O-ISAC becomes practically realizable by linking enabling technologies to channel robustness, joint optimization, runtime overhead, and benchmarking discipline. Across the current evidence base, optical phased arrays (OPA), optical reconfigurable intelligent surfaces (ORIS), robustness-aware optimization, and network coordination recur as coupled design levers rather than isolated modules [O_ISAC_008], [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112], [O_ISAC_127]. Accordingly, this section remains enabler-centric: the named anchors promised in Section I, namely ORIS, OPA, photonics-assisted signal generation, and machine learning integration, are retained here, but they are interpreted through system-level feasibility rather than as a component catalog. In the survey flow, this chapter bridges the measured trade-off logic of Section V to the deployment and application focus of Section VII by asking which enablers create usable design freedom under realistic channel, control, and evaluation constraints. To stay aligned with earlier sections, we preserve Section II measurement governance, reuse the Section IV medium/taxonomy framing, and keep the Section V governed-evidence caution visible when discussing maturity and prevalence. Where the study-level core remains limited, the prose below therefore emphasizes design opportunity and constraint structure rather than deployment maturity.

Throughout this section, we use **ORIS (Optical Reconfigurable Intelligent Surface)** as the canonical umbrella term for optical RIS-style programmable surfaces. We also preserve one shared notation block so that OPA steering, ORIS-assisted links, robustness constraints, and multi-user optimization can be discussed without symbol drift across subsections.

**Table VI-1 defines unified notation for Section VI.**

| Symbol | Meaning | Used in |
|---|---|---|
| $x(t)$ | Optical transmit waveform or equivalent sampled signal | VI-C, VI-E |
| $\ell$ | Link distance in benchmark scenario disclosure | VI-D |
| $\bar P$ | Average optical power budget | VI-C, VI-D |
| $P_{\max}$ | Peak optical power budget | VI-C, VI-D |
| $H$ | End-to-end channel coefficient or gain | VI-B |
| $H_l$ | Deterministic or path-loss component of $H$ | VI-B |
| $H_a$ | Atmospheric or medium-turbulence component of $H$ | VI-B |
| $H_p$ | Pointing or misalignment component of $H$ | VI-B |
| $\gamma$ | Instantaneous reliability proxy evaluated on a fixed detection plane; no cross-plane substitution is implied | VI-B, VI-E |
| $\gamma_{\text{th}}$ | Reliability threshold for outage control | VI-B |
| $\varepsilon$ | Allowed outage probability target | VI-B, VI-C |
| $m_{\text{res}}$ | Role-consistent resolution or granularity metric | VI-D |
| $m_{\text{acc}}$ | Empirical sensing accuracy metric | VI-D |
| $m_{\text{bnd}}$ | Bound-type sensing metric family | VI-D |
| $\sigma_r$ | Estimator-dependent sensing accuracy metric when reported | VI-D |
| $\Theta$ | ORIS diagonal response matrix | VI-A, VI-C, VI-E, VI-F |
| $\beta_n$ | ORIS amplitude coefficient of element $n$ | VI-A |
| $\theta_n$ | ORIS phase of element $n$ | VI-A, VI-E |
| $Q$ | Number of phase-quantization levels | VI-A, VI-E |
| $\mathbf{w}_k$ | Beamforming vector for user $k$ | VI-C, VI-E |
| $\mathrm{SINR}_k$ | User-$k$ communication quality metric | VI-E |
| $\mathrm{CRB}$ | Bound-type sensing metric; not interchangeable with empirical accuracy metrics | VI-C, VI-D, VI-E, VI-F |

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

PIC, programmable photonics, and photonics-assisted signal-generation themes belong here only as enabling substrates beneath these control surfaces, not as a detached component inventory. At the current evidence level, Section VI should therefore treat these families conservatively unless they are directly anchored to measurable O-ISAC integration benefits. In this survey, their main value is explanatory: they clarify packaging, integration pathway, and hardware-stack feasibility behind OPA/ORIS-style controllability, but they do not yet carry the same headline evidence weight as the primary programmable-surface and beam-steering narratives. Likewise, prevalence language must remain cautious: structured metric traces for OPA/ORIS are broader than strong study-level evidence of deliberate co-design adoption, so OPA/ORIS discussion in this survey should be read as a high-signal but still limited adoption core rather than as evidence of uniform platform maturity.

**Table VI-A.1 compares programmable optical enabler families by control role, evidence posture, and deployment constraints.**

| Enabler family | Primary control role in O-ISAC | Strongest evidence posture in this survey | Main deployment constraints | Role in Section VI argument |
|---|---|---|---|---|
| OPA | Transmit-side beam agility, angular selectivity, joint communication-sensing steering | Primary evidence core; Section I contribution count is 7 study-level papers, while broader structured traces are treated only as support context | Grating lobes, finite receiver FoV, insertion loss, atmospheric/channel loss sensitivity | Carries the strongest beam-control narrative in VI-A |
| ORIS | Environment-side path shaping, blockage mitigation, alignment assistance, NLoS reconstruction | Primary evidence core; Section I contribution count is 8 study-level papers, while broader structured traces are treated only as support context | Refresh latency, attenuation, phase quantization, coherence-time mismatch, control overhead | Carries the strongest propagation-control narrative in VI-A |
| PIC / programmable photonics | Integration substrate for packaging, routing, and scalable optical control | Qualitative/supporting only; used to explain how controllable optics may be integrated, not to claim mature O-ISAC adoption | Calibration burden, packaging complexity, insertion loss, hardware-stack dependence | Supplies integration context beneath OPA/ORIS rather than a separate headline storyline |
| Photonics-assisted signal generation / photonic-THz bridge | Source and distribution pathway for hybrid optical-wireless control chains | Bridge evidence only; relevant for hybrid system interpretation but not a standalone maturity claim in VI-A | Stage-aware modeling, cross-plane reporting, front-end chain complexity | Connects enabler discussion to hybrid and transfer-oriented system views |

Evidence note: OPA/ORIS prevalence wording follows the strict study-level contribution view used in Section I; broader structured traces from the wider Section VI evidence audit remain contextual and are not interpreted here as direct adoption prevalence. In whole-manuscript terms, Table VI-A.1 is the compact enabler-capability artifact that later application and challenge sections can inherit without re-inflating prevalence claims.

These medium-conditioned asymmetries are better read as an enabler landscape than as a flat prevalence ranking, and Fig. VI-1 summarizes that view in a medium-conditioned form without converting contextual traces into direct adoption claims.

![Fig. VI-1. Section VI enabler landscape across medium classes. The matrix reports canonical corpus concentration by medium while preserving the stricter study-level headline interpretation used in Section I for OPA, ORIS, and ML/AI. OPA and ORIS should therefore be read as primary programmable-enabler evidence cores, whereas PIC, photonic generation, and programmable photonics remain supporting substrate families whose contextual traces do not by themselves imply co-equal maturity.](fig_vi_1.jpg)

**VI-A takeaway.** OPA evidence is strongest on beam agility and communication-sensing coupling, while ORIS evidence is strongest on alignment robustness and NLoS support. Across modalities, quantized control, insertion loss, and refresh latency remain practical bottlenecks. For the survey narrative, OPA/ORIS therefore carry the primary evidence load in VI-A, while PIC and photonic-integration themes remain supporting context on how those capabilities might be packaged and scaled. The most defensible near-term message is not that programmable optics are uniformly mature, but that they expose a promising yet unevenly validated optical control space whose practical value is still scenario- and impairment-dependent. That conclusion naturally shifts the discussion to VI-B: controllability matters only if it remains useful under the impairment profile of the actual optical channel.

## VI-B. Channel Impairments and Robustness

Robustness is a first-order concern in O-ISAC because the same optical channel impairments degrade communication reliability and sensing fidelity together. Across FSO, VLC/LiFi, and hybrid optical settings, the literature repeatedly models end-to-end gain as a composition of deterministic loss, atmospheric or medium turbulence, and pointing or alignment components [O_ISAC_023], [O_ISAC_035], [O_ISAC_061], [O_ISAC_098], [O_ISAC_199]. Guided-fiber cases remain important, but they require different impairment abstractions and should not be silently collapsed into the same wireless robustness template. This is the point where enabler value becomes conditional: a programmable surface or beam-steering mechanism is only useful insofar as it remains effective under the dominant impairment regime.

A compact robustness anchor is

$$
H=H_l H_a H_p,
$$
$$
P_{\text{out}}=\Pr\!\left(\gamma(H)<\gamma_{\text{th}}\right)\le \varepsilon.
$$

This chance-constrained view links physical impairment statistics directly to reliability targets and is consistent with quantile-robust formulations already used in optical ISAC optimization studies [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Here $\gamma$ must stay tied to one declared detection plane per scenario; the expression does not permit implicit OSNR-to-electrical-SNR conversion or blind pooling of coherent and direct observations. Practical mitigation then combines design-time robustness with runtime adaptation through tracking, refresh control, environment-aware reconfiguration, and fallback or diversity mechanisms [O_ISAC_098], [O_ISAC_112], [O_ISAC_127], [O_ISAC_199].

The prose here should stay medium-aware. Turbulence and weather attenuation dominate many FSO and hybrid scenarios, finite FoV and geometry dominate many VLC scenarios, and control latency cuts across most programmable optical platforms. Section VI therefore cannot write "robustness" as if one impairment model covers all optical modalities equally well.

**VI-B takeaway.** Current literature supports robustness-aware optical design, but cross-paper outage definitions and confidence reporting remain heterogeneous. The survey-level lesson is that controllability becomes meaningful only after impairment-aware conditioning, not before it. The main open issue is therefore no longer whether robustness matters, but how to compare robustness claims under common impairment and reporting contracts. Once that conditioning is made explicit, the next question becomes how communication, sensing, and robustness constraints should be optimized jointly, which motivates VI-C.

## VI-C. Joint Co-Design and Resource Optimization

Joint co-design is required because waveform, beam, power, and ORIS controls share physical constraints. In IM/DD implementations, feasible signaling must satisfy nonnegativity and optical power bounds, while coherent or programmable settings add quantization, steering, and update constraints [O_ISAC_009], [O_ISAC_023], [O_ISAC_054], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Model VI-U is useful here because it keeps transmitter, ORIS, and sensing terms in one variable structure.

A minimal feasible-set and objective anchor is

$$
\mathcal U=\{x(t):x(t)\ge 0,\;\mathbb{E}[x(t)]\le \bar P,\;\max_t x(t)\le P_{\max}\},
$$
$$
\max_{\mathbf{w},\Theta,\,x\in\mathcal U}\;\alpha R(\mathbf{w},\Theta)-(1-\alpha)\,\mathrm{CRB}(\mathbf{w},\Theta),\quad \alpha\in[0,1].
$$

The weight $\alpha$ sets the communication-sensing operating point and can be extended with reliability and latency constraints when channel dynamics are explicit [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Within this subsection, $\mathrm{CRB}$ is retained as a bound-type sensing term; it should not be read as interchangeable with empirical accuracy metrics such as $\sigma_r$ or with bandwidth-limited resolution terms. However, this subsection must preserve two maturity caveats. First, Section VI contains more structured OPA/ORIS metric traces than strong study-level evidence of deliberate full-stack co-design adoption. Second, many reported formulations remain exemplar-driven studies under controlled assumptions rather than reproducibly benchmarked integrated stacks. It is therefore safer to say that the literature exposes a structured control space for co-design than to say that metric-bearing OPA/ORIS papers already establish mature multi-objective O-ISAC practice.

**VI-C takeaway.** Evidence is strongest for structured optimization in a limited set of well-specified OPA, DCO-OFDM, and dynamic underwater exemplars. The main gap is not the absence of optimization methods, but the absence of harmonized disclosure of constraints, runtime burden, operating assumptions, and replication quality across papers. In survey terms, VI-C shows that the co-design space is already nontrivial, yet still weakly comparable across studies. That comparability problem is exactly why VI-D becomes the hinge subsection of the chapter.

## VI-D. Experimental Validation, Benchmarking, and Reporting Contract

The literature now contains both experimental demonstrations and simulation-heavy studies, but cross-paper comparability remains weak because scenario definitions, baselines, and KPI contracts differ. This makes benchmarking the hinge of Section VI: the earlier subsections show that the control space is rich, but this subsection explains why that richness does not automatically translate into cumulative scientific maturity [O_ISAC_023], [O_ISAC_035], [O_ISAC_054], [O_ISAC_061], [O_ISAC_091], [O_ISAC_112], [O_ISAC_127].

A minimal benchmark contract can be written as

$$
\mathbf{s}=\{\ell,\,C_n^2,\,\sigma_{\text{jitter}},\,\lambda,\,B,\,N_{\text{ORIS}},\,M_{\text{OPA}},\,\bar P,\,P_{\max},\,T_{\text{update}}\},
$$
$$
\mathbf{m}=(R,\,\mathrm{BER},\,m_{\text{res}},\,m_{\text{acc}},\,m_{\text{bnd}},\,P_{\text{out}},\,\text{latency},\,\text{energy}).
$$

Here $\ell$ denotes link distance, $m_{\text{res}}$ denotes a role-consistent resolution or granularity metric, $m_{\text{acc}}$ denotes an empirical accuracy metric such as $\sigma_r$, and $m_{\text{bnd}}$ denotes a bound-type metric such as $\mathrm{CRB}$ or CRLB. For Section II consistency, $m_{\text{res}}$ may be instantiated by $\Delta r_{\min}$ in bandwidth-limited ranging settings or by $\Delta z$ in fiber spatial-granularity settings, but these are not interchangeable and should never be collapsed into a single pooled number without task and medium conditioning. The contract makes scenario assumptions explicit before gains are interpreted and prevents comparisons across incompatible operating conditions.

**Table VI-2 lists the reporting fields needed for reproducible O-ISAC experiments and simulations.**

| Item | Minimum required fields | Why it matters |
|---|---|---|
| Scenario vector disclosure | Full $\mathbf{s}$ values, mobility profile, channel model family | Prevents hidden scenario drift across papers |
| KPI contract disclosure | Full $\mathbf{m}$ values with units, confidence intervals, and metric-role notes | Supports fair comparison of communication and sensing quality without role aliasing |
| Baseline taxonomy | At least one separated baseline and one practical baseline | Prevents inflated gains from weak references |
| Runtime and control budget | Solver runtime, $T_{\text{update}}$, hardware timing, feedback overhead | Distinguishes deployable from offline-only designs |
| Reproducibility package | Parameter files, script versions, data provenance, random seeds | Enables external replication and audit |
| Safety and operating envelope | Optical power settings and safety-margin reporting method | Necessary for translation to certified deployments |

The benchmark chain in VI-D is also the structural backbone of the section as a whole, and Fig. VI-2 captures that systems-level coupling from enabler choice to deployment-ready evaluation. In whole-manuscript terms, Table VI-2 is the reporting and constraint contract that later deployment-oriented discussion in Section VII and challenge synthesis in Section VIII can inherit directly.

![Fig. VI-2. From programmable enablers to deployment-ready O-ISAC. The layered systems map shows how optical enablers, medium-specific impairments, control logic, and benchmark discipline are coupled in Section VI. The deployment/benchmark gate should be read as the hinge that determines whether enabler-level gains remain comparable beyond isolated demonstrations and can be handed off to application-facing synthesis in Section VII.](fig_vi_2.jpg)

**VI-D takeaway.** The strongest immediate need is a shared benchmark contract rather than more isolated case studies. Benchmark discipline is what turns promising enablers into cumulative evidence and determines which claims remain credible once the discussion moves beyond single-link exemplars. With that reporting contract in place, Section VI can shift from feasibility to scale, which is the purpose of VI-E.

## VI-E. Networked and Multi-User O-ISAC

Networked O-ISAC introduces burdens that do not appear in single-link settings: multi-user interference, feedback overhead, sensing-fusion consistency, and coordination delay. The corpus already reports explicit FoV and grating-lobe interference effects in multi-user OPA settings, tracking burden growth with user count in mobile ORIS systems, and protocol-level overhead sensitivity in VLC-based networked settings [O_ISAC_009], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_303].

A compact network objective anchor is

$$
\max_{\{\mathbf{w}_k\},\Theta}\;\sum_{k}\omega_k\log\!\left(1+\mathrm{SINR}_k\right)-\lambda\,\mathrm{CRB}(\Theta)
$$
$$
\text{s.t.}\quad \sum_k\|\mathbf{w}_k\|_2^2\le P,\quad \theta_n\in\mathcal Q.
$$

This formulation makes communication, sensing, and ORIS quantization constraints explicit in one multi-user program [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Its interpretation still requires fixed detection semantics for $\mathrm{SINR}_k$ and a role-consistent sensing objective rather than a mixed resolution-accuracy score. More importantly for the survey narrative, this subsection is where Section VI begins to connect directly to Section VII: once user count, fusion policy, fairness, and control overhead become dominant, the question is no longer whether an enabler exists but whether a deployment setting can absorb its coordination cost.

**VI-E takeaway.** Multi-user optical O-ISAC is supported by a growing set of targeted studies, but network-level overhead metrics, control-plane timing, and cooperative benchmark contracts remain under-standardized. For the survey narrative, this is the point where enabler analysis becomes deployment analysis: coordination cost, fairness, and sensing-fusion policy begin to shape whether an otherwise promising design is application-ready. Those same pressures also explain why adaptive and security-aware control enters the discussion in VI-F.

## VI-F. AI/ML and Security-Aware Adaptation

AI-assisted adaptation and security-aware design are emerging layers in O-ISAC, especially in dynamic channels where static policies may underperform. At the study-level tag view fixed in Section I, machine learning appears in 53 studies, but only a more limited subset supports direct interpretation as reproducible adaptation or security-aware control in Section VI. The available literature therefore contains targeted reports of learning-driven adaptation for nonstationary environments together with secrecy, authentication, and resilience formulations, but jointly validated AI-plus-security optical benchmarks remain limited [O_ISAC_127], [O_ISAC_145], [O_ISAC_156], [O_ISAC_163]. In the survey flow, this subsection is not meant to compete with the physical enabler evidence in VI-A; it functions as a forward-looking systems layer that explains how controllable optical platforms may later absorb adaptation, trust, and resilience requirements.

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

where $\mathbf{u}$ includes transmitter and ORIS controls inherited from Model VI-U [O_ISAC_127], [O_ISAC_145], [O_ISAC_163]. This framing captures the central tension of this subsection: adaptation gains are only meaningful if they survive uncertainty, overhead, and adversarial pressure rather than only nominal channels. Here again, $R$, $R_s$, and $\mathrm{CRB}$ must be interpreted as role-specific quantities rather than as mutually convertible scores. In most cases, the current evidence should be read as focused demonstrations of learning or secrecy mechanisms, not yet as reproducible proof of mature end-to-end AI-secure O-ISAC stacks.

This is also the place where Section VI must keep maturity asymmetry visible. OPA and ORIS mechanics are presently better evidenced than long-horizon AI adaptation, trust, and adversarial robustness under reproducible protocols. That should be written as a maturity signal, not as a dismissal of the topic, because this distinction helps keep Section VIII grounded later in the manuscript. Put differently, AI/security belongs in Section VI as an emerging overlay on top of better-evidenced optical controllability, not yet as a co-equal maturity tier.

**VI-F takeaway.** AI/ML and security are relevant emerging directions in optical O-ISAC, but current evidence is uneven and should be synthesized cautiously. The field still needs reproducible attack models, overhead-aware reporting, and benchmark-quality evaluation of adaptation under domain shift before strong maturity claims are warranted. Within the survey architecture, VI-F should therefore be read as a bounded forward layer on top of better-evidenced optical controllability, not as the new center of gravity of current evidence. That bounded reading prepares a cleaner handoff to Section VII, where the question becomes which application settings can realistically absorb these layered design choices.

## Section VI Synthesis and Transition

Taken together, VI-A to VI-F suggest that one of the main bottlenecks in optical ISAC is no longer the absence of promising enablers, but the absence of stable reporting and benchmarking contracts that let the community compare those enablers under common assumptions. Read in sequence, the chapter develops a layered argument: OPA and ORIS broaden controllability, robustness models determine whether that controllability survives real channels, co-design methods organize the resulting trade space, benchmarking decides which gains are actually comparable, and networked plus adaptive layers reveal what is required for deployment-facing viability. Supporting substrate themes such as PIC and photonic integration help explain how these levers may be packaged, but they currently play a secondary interpretive role rather than carrying the section's strongest evidence claims. This same layered reading is also what Section VIII later needs: Section VI contributes enabler-linked hardware, control, benchmarking, and deployment constraints, but it deliberately stops short of claiming a standalone roadmap. Yet without explicit disclosure of control overhead, update latency, benchmark assumptions, and sensing-quality definitions, these advances remain difficult to stack into a reproducible system narrative.

This framing gives Section VII a clean handoff: the next question is no longer "what enabling components exist?" but "which deployment patterns and application settings can absorb these coupled design choices in a defensible way?"
