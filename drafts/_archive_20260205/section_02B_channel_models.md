## B. Propagation and Channel Models Across Modalities
This subsection abstracts each modality's propagation as an operator/channel mapping consistent with the observation models in Section II-A, while emphasizing that dominant impairments differ across media. The measurement-plane contract remains binding: channel modeling does not justify OSNR-to-SNR conversion, and plane separation is preserved throughout (Metric Governance).

### B.1 Fiber Channel (Guided Medium)
Design rationale: A guided fiber link is well captured by a linear dispersive baseband model for coherent communication, with a nonlinear wave equation as a conceptual extension when power or length scales demand it. This separation provides a minimal, modality-consistent abstraction while allowing later sections to specialize the impairment regime.

A linear dispersive baseline is
\[
\mathbf{y}(t)=\mathbf{G}_{\text{disp}}(t)\ast \mathbf{s}(t)+\mathbf{w}(t),
\]
where \(\mathbf{s}(t)\) is the transmitted baseband signal, \(\mathbf{G}_{\text{disp}}(t)\) is the dispersive impulse response, and \(\mathbf{w}(t)\) is additive noise. As a conceptual extension, the nonlinear Schrodinger equation (NLSE) captures loss, dispersion, and Kerr nonlinearity:
\[
\frac{\partial A(z,t)}{\partial z}= -\frac{\alpha}{2}A - j\frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2} + j\gamma|A|^2A + \eta(z,t),
\]
where \(A(z,t)\) is the optical field envelope, \(\alpha\) is attenuation, \(\beta_2\) is group-velocity dispersion, and \(\gamma\) is the nonlinear coefficient. For sensing, the effective channel is the distributed backscatter/impulse response along the fiber, whereas the communication view typically emphasizes the forward transmission path. Fiber sensing spatial granularity is reported as \(\Delta z\) (gauge/segment length), not \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: This subsection presents theory-standard channel abstractions and does not assert paper-specific modeling choices; hence no evidence anchors are invoked here.

### B.2 FSO Channel (Atmosphere + Pointing)
Design rationale: Free-space optical channels are dominated by multiplicative impairments (turbulence and pointing) and path attenuation, which are naturally expressed in an IM/DD-friendly intensity model. This abstraction keeps the optical nonnegativity constraint explicit while isolating the dominant propagation factors.

A compact IM/DD-friendly form is
\[
y = h_{\text{turb}}\,h_{\text{point}}\,x + n,\qquad x\ge 0,
\]
where \(x\) is the transmitted optical intensity, \(h_{\text{turb}}\) captures turbulence-induced fading, \(h_{\text{point}}\) captures pointing/misalignment loss, and \(n\) is additive noise. A standard attenuation factor is the Beer-Lambert law,
\[
h_{\text{att}}=\exp(-\kappa d),
\]
with \(\kappa\) as the extinction coefficient and \(d\) the propagation distance. Turbulence statistics are commonly represented by lognormal or Gamma-Gamma distributions as theory-standard options.

Evidence alignment: Representative FSO works compute atmospheric loss using Beer-Lambert attenuation in their channel modeling and simulation setup [O_ISAC_035], [O_ISAC_034]. <!-- evidence: ⟦O_ISAC_035 | ### II. SYSTEM MODEL AND METHODOLOGY > # B. FSO Channel | L75-L79 | strength_final=strong | claim_tag=attenuation_beer_lambert | context-verified=YES⟧; ⟦O_ISAC_034 | # IV. NUMERICAL RESULTS | L205-L205 | strength_final=strong | claim_tag=attenuation_beer_lambert | context-verified=YES⟧ -->

### B.3 VLC Channel (Lambertian + Multipath + Ambient Light)
Design rationale: VLC channels are geometry-driven and are naturally modeled by Lambertian emission with an intensity impulse response that captures both direct and reflected paths. This abstraction preserves IM/DD constraints while enabling later sections to compare sensing and communication performance under common channel primitives.

A compact representation uses an intensity impulse response \(h(t)\) with a Lambertian DC gain for the LoS path, while NLoS reflections are captured by additional impulse-response components. Multipath/NLoS effects are thus expressed through \(h(t)\) rather than an equivalent complex baseband model. Shot noise, thermal noise, and ambient-light-induced noise are standard components in VLC receiver models.

Evidence alignment: Representative VLC/OWC works model the channel impulse response as a sum of LOS and NLOS components, explicitly framing multipath via LoS/NLoS impulse-response components [O_ISAC_022], [O_ISAC_039]. <!-- evidence: ⟦O_ISAC_022 | ## <span id="page-3-0"></span>D. The Optical Wireless Channel | L136-L136 | strength_final=strong | claim_tag=multipath_nlos_impulse_response | context-verified=YES⟧; ⟦O_ISAC_039 | # 2 VISIBLE LIGHT INTEGRATED POSITIONING AND COMMUNICATION FRAMEWORK > ## 2.1 System Model of Indoor Visible Light Positioning and Communication | L67-L71 | strength_final=strong | claim_tag=multipath_nlos_impulse_response | context-verified=YES⟧ -->

### B.4 Photonic-THz Bridging (Optical Generation/Distribution + THz Propagation)
Design rationale: Photonic-THz links are hybrid by construction: optical carriers are used for signal generation, distribution, and local-oscillator delivery, while the wireless propagation occurs in the THz band. A split-channel abstraction therefore cleanly separates optical-domain impairments from THz wireless propagation effects.

We treat the link as an optical generation/distribution stage feeding a THz wireless channel, which enables consistent modeling of end-to-end performance without conflating measurement planes. In representative photonic-THz links, laser-induced phase noise and frequency offset are treated as dominant impairments that shape performance and system design choices.

Evidence alignment: Photonic-THz works explicitly discuss laser-induced phase noise and frequency-offset effects in their experimental or system-performance analyses [O_ISAC_044], [O_ISAC_077]. <!-- evidence: ⟦O_ISAC_044 | #### I. INTRODUCTION | L41-L41 | strength_final=strong | claim_tag=phase_noise_freq_offset | context-verified=YES⟧; ⟦O_ISAC_077 | ### III. PHOTONIC THZ ISAC LINK > #### A. Experimental Setup | L58-L58 | strength_final=strong | claim_tag=phase_noise_freq_offset | context-verified=YES⟧ -->

**Lesson (B):** Channel models differ in dominant impairments, but the reporting contract and measurement-plane separation remain invariant across modalities.
