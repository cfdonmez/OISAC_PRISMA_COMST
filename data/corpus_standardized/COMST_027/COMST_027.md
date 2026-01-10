# A Tutorial on Beyond-Diagonal Reconfigurable Intelligent Surfaces: Modeling, Architectures, System Design and Optimization, and Applications

Hongyu Li, *Member, IEEE*, Matteo Nerini, *Member, IEEE*, Shanpu Shen, *Senior Member*, and Bruno Clerckx, *Fellow, IEEE* 

Abstract—Written by its inventors, this first tutorial on Beyond-Diagonal Reconfigurable Intelligent Surfaces (BD-RISs) provides the readers with the basics and fundamental tools necessary to appreciate, understand, and contribute to this emerging and disruptive technology. Conventional (Diagonal) RISs (D-RISs) are characterized by a diagonal scattering matrix  $\Theta$ (commonly denoted as phase shift matrix in the literature). Since a very small percentage of the entries of that matrix, namely only the phases of its diagonal entries (in its passive form), are tunable, the wave manipulation flexibility of D-RIS is extremely limited. In contrast, BD-RIS refers to a novel and general framework for RIS where its scattering matrix is not limited to be diagonal (hence, the "beyond-diagonal" terminology) and consequently, all entries of  $\Theta$  can potentially help shaping waves for much higher manipulation flexibility. In its passive form,  $\Theta$  satisfies the unitary property  $\Theta^H\Theta = I$  (for energy conservation in lossless ideal surfaces) and be either symmetric  $\Theta = \Theta^{\mathsf{T}}$  or asymmetric  $\Theta \neq \Theta^{\mathsf{T}}$  hence leading to reciprocal or non-reciprocal BD-RIS. Such scattering matrix properties correspondingly translate into novel passive (lossless) and reciprocal/non-reciprocal circuitry where each RIS element is not only connected to its own tunable impedance but also to other elements through reconfigurable components. This physically means that BD-RIS can artificially engineer and reconfigure coupling across elements of the surface thanks to inter-element reconfigurable components which allow waves absorbed by one element to flow through other elements. This offers an extra degree of freedom for reconfigurable surfaces that provides new opportunities and flexibility for manipulating, modulating, processing, and computing signals and waves in the analog domain. Consequently, BD-RIS opens the door to more general and versatile intelligent surfaces that subsumes existing RIS architectures as special cases. In this tutorial, we share all the secret sauce to model, design, and optimize BD-RIS and make BD-RIS transformative in many different applications. Topics discussed include physics-consistent and multi-port networkaided modeling; transmitting, reflecting, hybrid, and multi-sector

This work is funded by the National Natural Science Foundation of China (grant no. 62501509), by the Science and Technology Development Fund, Macau SAR (File/Project no. 001/2024/SKL), by University of Macau (File no. SRG2025-00060-IOTSC), and by UKRI grant EP/Y004086/1, EP/X040569/1, EP/Y037197/1, EP/X04047X/1, EP/Y037243/1 (Corresponding author: Bruno Clerckx).

- H. Li is with the Internet of Things Thrust, The Hong Kong University of Science and Technology (Guangzhou), Guangzhou 511400, China (e-mail:hongyuli@hkust-gz.edu.cn).
- M. Nerini is with the Department of Electrical and Electronic Engineering, Imperial College London, London SW7 2AZ, U.K. (e-mail:m.nerini20,@imperial.ac.uk).
- S. Shen is with the State Key Laboratory of Internet of Things for Smart City and Department of Electrical and Computer Engineering, University of Macau, Macau, China (e-mail:shanpushen@um.edu.mo).
- B. Clerckx is with the Department of Electrical and Electronic Engineering, Imperial College London, London SW7 2AZ, U.K. and also with Kyung Hee University, Seoul, Korea (e-mail:b.clerckx@imperial.ac.uk).

mode analysis; reciprocal and non-reciprocal architecture designs and optimal performance-complexity Pareto frontier of BD-RIS; signal processing, optimization, and channel estimation for BD-RIS; hardware impairments (discrete-value impedance and admittance, lossy interconnections and components, wideband effects, mutual coupling) of BD-RIS; benefits and applications of BD-RIS in communications, sensing, power transfer. We also point out challenges of BD-RIS which trigger directions that are promising for future research.

Index Terms—Beyond-diagonal reconfigurable intelligent surfaces, modes, reciprocal and non-reciprocal architecture designs, reconfigurable impedance unitary property.

#### I. INTRODUCTION

The sixth generation (6G) networks are driven by three important characteristics linked to human lifestyle and social changes in the near future: High-fidelity holographic society; connectivity for all things; and time sensitive/time engineered applications [1]-[3]. Consequently, 6G networks should be human-centric with the aim of achieving high security and privacy, seamless connectivity between devices, and real-time communications with extremely low latency [3]. To achieve these stringent requirements, several promising 6G candidate solutions have been proposed, such as advanced multiple access techniques that could better utilize resources [4], extremely large-scale multiple input multiple output (MIMO) that can significantly improve the spectral efficiency [5], multifunctional platforms that could simultaneously support wireless communications, sensing, and power transfer [6], [7], and reconfigurable intelligent surfaces (RISs) that provide wave manipulation flexibility to reconfigure the wireless propagation environment and enable new processing capabilities in the electromagnetic domain [8]–[11].

### A. Background and Motivation

Among various promising 6G candidate solutions, RIS has gained significant attention in recent years due to its capability to change the way of treating wireless propagation environments: from adapting to them by sophisticated signal processing strategies to manipulating them with low cost, negligible thermal noise, and low power consumption [8]. RIS is a generic term that is also referred to as intelligent reflecting surface (IRS) [9], intelligent surface (IS) [12], and programmable/dynamic metasurface [8]. RIS can be physically fabricated using different implementations, such

as using antenna arrays with tunable components and using metasurfaces, while the former way gains more attention in the wireless society since it has a more straightforward and physics-consistent model. Broadly speaking, an RIS is a planar surface consisting of numerous tunable elements, each of which is able to induce a controllable change of phase shift and/or amplitude to the incident signal. Benefiting from its shape and reconfigurable property, RIS can be flexibly deployed in complex wireless propagation environments, e.g., being attached on high buildings, to bypass obstacles and increase/decrease the directivity of waves according to specific requirements. RISs were primarily proposed as nearly passive devices, in the sense that they are not capable of amplifying incident waves and only minimal power is used to control the surface [9]. This property brings various practical advantages for RIS implementation, such as being free of power-hungry RF chains, power amplifiers, and thermal noise.

Inspired by the above advantages, the research on RIS has grown exponentially in the past few years, covering a wide range of areas that include but are not limited to beamforming design [13], [14], channel estimation [15], [16], hardware impairments analysis [17]-[19], and implementation and prototyping [11], [20]. To fully compensate for the huge path loss induced by RIS, the concept of active RIS, named due to the introduction of reflection-type power amplifiers, has been further proposed to provide significantly enhanced performance gain at the expense of affordable power consumption and cost [21]. Meanwhile, the industry has also achieved progress on demonstrating and testing RISs. The test mainly originated from NTT DOCOMO, a Japanese network operator, which demonstrated a fifth generation (5G) mobile system using a metasurface reflectarray operating in 28 GHz in 2018 and conducted a trail of a transparent dynamic metasurface for 5G radio signals in 2020, followed by a re-conduction in 2021 [8]. More recently, RIS has been used in a 5G commercial frequency range 2 band network that operates beyond 24 GHz, showing significant performance improvement in the indoor coverage and throughput [22]. In support of active academia and industrial progress on RIS, key organizations have started to consider the integration of RIS into future commercial networks. For example, RIS-related standardization has been kicked off in the China Communications Standards Association and the FuTURE Mobile Communication Forum from China [23]. For another example, within the European Telecommunications Standards Institute, an industry specific group on RISs has been proposed and approved in June 2021, and launched in September 2021 [23]. The technical details and practical considerations for applying RISs have been thoroughly discussed during 2021-2023 [12], [24].

Despite the comprehensive study and tests of RIS from both academia and industry, one fundamental limitation is that conventional (diagonal) RIS (D-RIS) is characterized by a diagonal scattering matrix  $\Theta$  (commonly denoted as phase shift matrices in the literature). This mathematical structure is realized by a simple architecture where each element of RIS is connected to ground through its own tunable load as illustrated in Fig. 1(a), thereby enabling only the independent control of each diagonal entry of the scattering matrix, as

![](_page_1_Picture_4.jpeg)

Fig. 1. Illustration of (a) D-RIS and (b) BD-RIS.

described in the left hand side of equation (1). In the passive form (at best lossless) of RIS, only phase shifts of its diagonal entries in the scattering matrix are tunable, such that waves impinging on one element can only be reflected by the same element. Therefore, the wave manipulation capability of D-RIS is limited. This limitation in D-RIS motivates a natural question as also mathematically described in equation (1): Can those zeros in the scattering matrix  $\Theta$  be freely tuned to potentially help shaping waves for more flexible manipulation?

$$\mathbf{\Theta} = \begin{bmatrix} ? & & & \\ & ? & & \\ & & \ddots & \\ & & & ? \end{bmatrix} \Rightarrow \mathbf{\Theta} = \begin{bmatrix} ? & ? & \dots & ? \\ ? & ? & \dots & ? \\ \vdots & & \ddots & \vdots \\ ? & ? & \dots & ? \end{bmatrix}. \tag{1}$$

The answer is *yes*, with the emerging technology, namely beyond-diagonal (BD) RIS [25].

### B. BD-RIS

BD-RIS refers to a novel and general framework for RIS whose scattering matrix  $\Theta$  is not limited to be diagonal, hence not only diagonal entries, but also off-diagonal entries which have been forced to zeros in D-RIS can be flexibly tuned to manipulate waves [25], [26]. This is realized by interconnecting (part of) elements by additional reconfigurable components as illustrated in Fig. 1(b), hence allowing waves absorbed by one element to flow through other elements and generating nonzero and tunable off-diagonal entries in  $\Theta$ . This brings extra degrees of freedom (DoF) for RIS from the following two perspectives.

Circuit Design Flexibility: While D-RIS has individually controllable elements supported by simple architectures, BD-RIS opens the door for diverse architectures by flexibly designing the circuit topology between elements using reciprocal or non-reciprocal devices. This leads to Θ with various mathematical structures, e.g., being full matrices, block-diagonal matrices, or permuted matrices, and constraints, e.g., being symmetric Θ = Θ<sup>T</sup> (realized by reciprocal circuits) or asymmetric Θ ≠ Θ<sup>T</sup> (realized

![](_page_2_Figure_1.jpeg)

Fig. 2. Examples of element arrangements in D-RIS and BD-RIS.

![](_page_2_Figure_3.jpeg)

Fig. 3. Illustration of future BD-RIS applications.

by non-reciprocal circuits). BD-RIS with multiple forms of **Θ** thus provides opportunities to manipulate waves in a smarter way.

*• Element Arrangement Flexibility:* In D-RIS, the arrangement of the elements is constrained by the absence of inter-element interconnections. Specifically, since elements in D-RIS are typically designed to cover half of space, they are often arranged as a 2D planar array, leading to practical location constraints for transmitters and receivers, as illustrated in Figs. 2(a) and 2(b). By contrast, BD-RIS enables more flexible element arrangements thanks to inter-element connections that allow signals to flow from one direction to another, as illustrated in Figs. 2(c) and 2(d). BD-RIS with diverse element arrangements thus provides opportunities to achieve larger wireless coverage and denser connectivity.

Due to the above extra DoF provided by flexible interelement reactions in BD-RIS, it is expected that BD-RIS will be able to achieve smarter wireless transmissions with higher quality, denser connectivity, and wider coverage. Fig. 3 shows an envisioned future application scenario supported by BD-RIS. For instance, BD-RIS can be particularly useful to extend the coverage in joint indoor and outdoor communications in Fig. 3. Properly deploying BD-RIS with flexible element arrangements can also help serving cell-edge users especially when there are obstacles between the base station

TABLE I LIST OF REPRESENTATIVE OVERVIEW/SURVEY/TUTORIAL PAPERS ON BD-RIS

| Ref.       | Type     | Highlights                                                                                                                                                                                                        |  |  |
|------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| [25]       |          | The first magazine to provide a high-level<br>overview of the concept of BD-RIS<br>without technical details                                                                                                      |  |  |
| [31]–[33]  | Overview | Briefly revisit the fundamentals of BD-RIS,<br>non-terrestrial networks (NTNs), and Internet<br>of Things (IoT), and outline the application<br>of BD-RIS in NTNs and IoT Networks                                |  |  |
| This Paper | Tutorial | Provide a tutorial of BD-RIS, including<br>fundamentals, signal processing techniques,<br>hardware impairments, and discuss the<br>benefits, emerging applications, challenges,<br>and future research directions |  |  |

and users. Another interesting application is to enable flexible and scalable integrated access and backhaul [27]. BD-RIS can be flexibly incorporated into real and complex environments to assist and enhance wireless backhauling between macrocells and picocells and wireless access between picocells and users. In addition to wireless communications, with proper power levels, suitable deployments, and locations, BD-RIS can be potentially used for higher-efficiency power relay and wireless power transfer (WPT) [7]. Besides, BD-RIS can also be leveraged to boost wireless sensing, especially in complicated propagation conditions, such as vehicle networks, where strong line-of-sight (LoS) links are not available between the radar and targets. Not limited to stand-alone functions (wireless communications, power transfer, and sensing), BD-RIS can support more advanced dual-functional systems, such as simultaneous wireless information and power transfer (SWIPT) [28] and integrated sensing and communications (ISAC) [6], [29], or multi-functional integrated communications, sensing, and power transfer systems [30]. Not limited to being used to realize smart radio environment, BD-RIS can also be integrated with transmitters/receivers and work as an auxiliary antenna array to enable RIS-aided or stacked surface-aided massive MIMO. Beyond the above, BD-RIS, as a comprehensive upgrade of D-RIS, is readily applicable to all D-RIS enabled scenarios while providing more flexible deployment, smarter wave manipulation and better performance, and wider coverage.

## *C. Contributions and Organization*

The appealing benefits and potential of BD-RIS have spurred active research. Specifically, a few overviews [25], [31]–[33] have appeared, focusing either on high-level illustrations to BD-RIS or specific applications of BD-RIS, as summarized in Table I. However, there is a lack of a comprehensive tutorial that pedagogically explains the basics and fundamental tools to understand BD-RIS. The main goal of this paper is thus to provide the first tutorial on BD-RIS including the fundamentals from a rigorous microwave engineering perspective, the state-of-the-art signal processing techniques, the hardware impairments, and the benefits, applications, technical challenges, and future research directions of BD-RIS. This further leads to the following contributions.

*First*, a toy example is given for BD-RIS-aided single input single output (SISO) systems to provide readers with an intuitive explanation on the rationale behind BD-RIS and its benefits over D-RIS.

*Second*, the physics-consistent modeling of BD-RIS using multi-port network analysis is explained, followed by a comprehensive summary of the reflecting, hybrid, and multi-sector modes and various reciprocal and non-reciprocal architectures supported by BD-RIS. The unification between architectures and modes is also discussed based on specific examples.

*Third*, representative optimization methods for various BD-RIS architectures are presented and summarized, taking the BD-RIS-aided SISO system as an example. An exhaustive survey of BD-RIS is provided from the perspective of beamforming design and channel estimation. In addition, the drawback of current channel estimation methods is pointed out with a discussion of possible future research directions.

*Fourth*, four important hardware impairments of BD-RIS (discrete-value impedance and admittance, lossy interconnections and admittance components, wideband effect, and mutual coupling effect) are modeled, evaluated, and analyzed to capture the practical issues and provide useful guidance for BD-RIS implementation.

*Fifth*, benefits of BD-RIS are highlighted with supporting simulation results, and applications of BD-RIS in wireless communications, sensing, and power transfer are summarized based on a thorough literature review.

*Sixth*, key technical challenges of BD-RIS are discussed, followed by directions that are promising for future research.

We hope this tutorial will provide a useful reference on the study and application of BD-RIS and serve as an inspiring resource for future research on BD-RIS.

*Organization:* The rest of this paper is organized as follows. Section II provides a toy example of BD-RIS-aided SISO systems to briefly explain the rationale and benefits of BD-RIS. Section III explains the basic modeling, mode analysis, and various architecture designs for BD-RIS. Section IV summarizes the key techniques for BD-RIS optimization and channel estimation. Section VI introduces hardware impairments in BD-RIS and illustrates their impacts on system performance. Section V discusses the benefits of BD-RIS supported by analytical and numerical results, and summarizes emerging applications. Section VIII points out challenges which should be tackled to facilitate the use of BD-RIS in future 6G networks, and sheds light on possible future research directions. Finally, Section IX concludes this paper. The outline of this paper is illustrated in Table II.

*Notations:* Boldface lower- and upper-case letters indicate column vectors and matrices, respectively. (*·*) <sup>T</sup>, (*·*) *∗* , (*·*) <sup>H</sup>, and (*·*) *<sup>−</sup>*<sup>1</sup> denote the transpose, conjugate, conjugate-transpose, and inverse operations, respectively. C, R, and Z denote the sets of complex, real, and integer numbers, respectively. The superscript of (*·*)*<sup>M</sup>×<sup>N</sup>* identifies the size of a matrix. E*{·}* denotes the statistical expectation. *ℜ{·}* and *ℑ{·}* denote the real and imaginary parts of complex numbers, respectively. ∠(*·*) denotes the angle of complex numbers. blkdiag(*·*) represents a block-diagonal matrix and diag(*·*) represents a diagonal matrix. *| · |*, *∥ · ∥*2, and *∥ · ∥*<sup>F</sup> denote the absolute value of

### TABLE II OUTLINE OF THE PAPER

#### Section I. Introduction

- A. Background and Motivation
- B. BD-RIS
- C. Contributions and Organization

### Section II. BD-RIS-Aided SISO: A Toy Example

### Section III. Modeling, Mode Analysis, and Architecture Design of BD-RIS

- A. Preliminaries on Multi-Port Network Analysis
- B. Modeling and Classification
- C. Mode Analysis
- D. Architecture Design: Reciprocal Architectures
- E. Architecture Design: Non-Reciprocal Architectures
- F. Unified Modes and Architectures

#### Section IV. Signal Processing of BD-RIS

- A. Optimizing BD-RIS: A Simple SISO Case
- B. Survey on BD-RIS Optimization and Performance Analysis
- C. Channel Estimation

### Section V. Benefits of BD-RIS

- A. Boosting Received Power and Rates
- B. Enabling Low-Complexity Architectures with High Performance
- C. Enabling Flexible Modes with Highly-Directional Wireless Coverage
- D. Providing Orders of Magnitude Gains in Distributed Deployments
- E. Enabling Simultaneously Optimal Transmissions for Uplink and Downlink with Non-Reciprocal Architectures
- F. Providing Enhanced Gains in Dual-Polarized Systems

### Section VI. BD-RIS with Hardware Impairments

- A. Discrete-Value Impedance and Admittance
- B. Lossy Interconnections and Admittance Components
- C. Wideband Effect
- D. Mutual Coupling Effect

### Section VII. Applications of BD-RIS

- A. BD-RIS for Communications
- B. BD-RIS for Sensing and ISAC
- C. BD-RIS for WPT and SWIPT
- D. BD-RIS with Other Techniques and Systems

### Section VIII. Challenges and Future Research Directions of BD-RIS

- A. BD-RIS Implementation
- B. Active BD-RIS
- C. AI-Driven Beamforming Solutions
- D. CSI-Free Protocols
- E. New BD-RIS Architectures

Section IX. Conclusion

a scalar, the *ℓ*<sup>2</sup> norm of a vector, and the Frobenius norm of a matrix, respectively. *ȷ* = *√ −*1 denotes the imaginary unit. *⊗* denotes the Kronecker product. vec(*·*) denotes the vectorization operation. tr(*·*) denotes the trace of a matrix. det(*·*) denotes the determinant of a square matrix. **I***<sup>M</sup>* denotes an *M ×M* identity matrix. **0***<sup>M</sup>×<sup>N</sup>* denotes an *M ×N* all-zero matrix. **A** *⪯* **B** (or **A** *⪰* **B**) indicates that **B** *−* **A** (or **A** *−* **B**) is positive semi-definite. *a ∼ CN* (0*, σ*<sup>2</sup> ) characterizes the circular symmetric complex Gaussian distribution. [**a**]*<sup>i</sup>* denotes the *i*-the entry of **a**. [**A**]*i*:*<sup>i</sup> ′ ,j*:*j ′* extracts the *i*-th to *i ′* -th rows and the *j*-th to *j ′* -th columns of **A**.

## II. BD-RIS-AIDED SISO: A TOY EXAMPLE

To introduce the rationale behind BD-RIS and understand its benefits, in this section, we analyze a BD-RIS-aided SISO system as a toy example. Consider a SISO wireless system between a single-antenna transmitter and a single-antenna receiver aided by a BD-RIS with *M* elements. Denoting the transmitted signal as *x ∈* C, the received signal *y ∈* C is given by *y* = *hx* + *n*, where *h ∈* C is the wireless channel matrix between the transmitter and receiver and  $n \in \mathbb{C}$  is the noise. The channel h is a function of the phase shift matrix of the RIS  $\Theta \in \mathbb{C}^{M \times M}$ , given by the well-known cascaded model

$$h = \mathbf{h}_{RI} \mathbf{\Theta} \mathbf{h}_{IT}, \tag{2}$$

where  $\mathbf{h}_{RI} \in \mathbb{C}^{1 \times M}$  is the channel between the RIS and receiver,  $\mathbf{h}_{IT} \in \mathbb{C}^{M \times 1}$  is the channel between the transmitter and RIS, and we neglect for simplicity the direct channel between the transmitter and receiver as it is assumed to be obstructed. Given the channel model in (2), the matrix  $\boldsymbol{\Theta}$  is commonly optimized to maximize the channel gain  $\rho = |h|^2$  subject to specific constraints depending on the properties of the RIS.

In a D-RIS,  $\Theta$  is a diagonal matrix given as

$$\mathbf{\Theta} = \operatorname{diag}\left(e^{j\theta_1}, e^{j\theta_2}, \dots, e^{j\theta_M}\right),\tag{3}$$

where  $e^{j\theta_m}$  is the reflection coefficient of the m-th RIS element. Note that we have implicitly assumed the D-RIS to be lossless in (3) by considering reflection coefficients with unit magnitude. The detailed derivation for obtaining such a diagonal phase shift matrix at D-RIS will soon be shown in Sections III-B and III-D. We can now write the channel gain as  $|h|^2 = |\mathbf{h}_{RI}\mathbf{\Theta}\mathbf{h}_{IT}|^2 = |\sum_{m=1}^M [\mathbf{h}_{RI}]_m e^{j\theta_m} [\mathbf{h}_{IT}]_m|^2$ . This allows us to obtain an optimal phase shift of the m-th element of RIS as  $\theta_m^* = -\angle([\mathbf{h}_{RI}]_m[\mathbf{h}_{IT}]_m)$ , yielding a maximum channel gain

$$\rho^{\mathsf{D}-\mathsf{RIS}} = \left(\sum_{m=1}^{M} \left| \left[ \mathbf{h}_{RI} \right]_m \left[ \mathbf{h}_{IT} \right]_m \right| \right)^2. \tag{4}$$

The matrix  $\Theta$  is commonly referred to as the "phase shift matrix" of the RIS, because conventionally it is a diagonal matrix containing phase shifts in its diagonal, as given by (3). Nevertheless, it has been shown through microwave theory that, more rigorously speaking,  $\Theta$  is the so-called "scattering matrix" of the RIS. In microwave theory, the scattering matrix is a matrix that can be used to characterize a linear microwave network linking the reflected waves to the incident waves at its ports. Intuitively speaking, the scattering matrix can be seen as the multidimensional generalization of the concept of reflection coefficient. As a lossless 1-port microwave network is characterized by a reflection coefficient having unit magnitude, a lossless multi-port microwave network is characterized by a unitary scattering matrix [34].

Since a lossless microwave network has a unitary scattering matrix, a lossless RIS is in principle allowed to have any unitary matrix  $\boldsymbol{\Theta}$ , i.e.,  $\boldsymbol{\Theta}^H \boldsymbol{\Theta} = \mathbf{I}_M$  or, equivalently,  $\boldsymbol{\Theta} \boldsymbol{\Theta}^H = \mathbf{I}_M$ , and is not limited to the diagonal constraint in (3).  $\boldsymbol{\Theta}$  in this case can have various expressions based on specific circuit designs, each of which will be explained in detail in Sections III-D and III-E. We refer to these RIS architectures, which are not limited to having a diagonal scattering matrix  $\boldsymbol{\Theta}$ , as BD-RIS. Remarkably, given that the unitary constraint  $\boldsymbol{\Theta}^H \boldsymbol{\Theta} = \mathbf{I}_M$  is a generalization of the constraint in (3), BD-RIS is a generalization of D-RIS and includes D-RIS as a special case. In this case, following the sub-multiplicity property of the spectral norm, we obtain that the channel gain  $|h|^2$  is upper bounded by

$$\rho^{\mathsf{BD-RIS}} = \|\mathbf{h}_{RI}\|_{2}^{2} \|\mathbf{h}_{IT}\|_{2}^{2}, \tag{5}$$

based on the Cauchy-Schwarz inequality and the constraint  $\mathbf{\Theta}^{\mathsf{H}}\mathbf{\Theta}=\mathbf{I}_{M}.$ 

Comparing the channel gain achievable with D-RIS and BD-RIS, in (5) and (4), respectively, we observe that  $\rho^{\text{BD-RIS}} \geq \rho^{\text{D-RIS}}$  for any channel realizations  $\mathbf{h}_{RI}$  and  $\mathbf{h}_{IT}$  because of the Cauchy-Schwarz inequality. Thus, BD-RIS always achieves a channel gain higher than D-RIS, and this is thanks to its additional flexibility. Intuitively, while D-RIS is reminiscent of equal gain combining, as it can only adjust the phases of the impinging signal, BD-RIS is reminiscent of maximal ratio combining since it can optimize both phases and amplitude of the impinging signal, increasing flexibility and performance.

To quantify the performance benefits of BD-RIS over D-RIS in a SISO system, we derive the scaling laws of the average channel gains  $\rho^{\text{D-RIS}}$  and  $\rho^{\text{BD-RIS}}$  under independent and identically distributed (i.i.d.) Rayleigh fading channels, i.e.,  $\mathbf{h}_{RI} \sim \mathcal{CN}(\mathbf{0}_{1\times M}, \mathbf{I}_M)$  and  $\mathbf{h}_{IT} \sim \mathcal{CN}(\mathbf{0}_{M\times 1}, \mathbf{I}_M)$ . In the case of a D-RIS, the average channel gain is obtained by taking the expectation of (4) as

$$\bar{\rho}^{\mathsf{D}-\mathsf{RIS}} = \mathbb{E}\left\{\left(\sum_{m=1}^{M} |[\mathbf{h}_{RI}]_{m}[\mathbf{h}_{IT}]_{m}|\right)^{2}\right\}$$

$$= \mathbb{E}\left\{\sum_{m=1}^{M} |[\mathbf{h}_{RI}]_{m}|^{2} |[\mathbf{h}_{IT}]_{m}|^{2} + \sum_{m_{1} \neq m_{2}} |[\mathbf{h}_{RI}]_{m_{1}}|\right.$$

$$\times |[\mathbf{h}_{IT}]_{m_{1}}| |[\mathbf{h}_{RI}]_{m_{2}}| |[\mathbf{h}_{IT}]_{m_{2}}|\right\},$$
(6)

by expanding the square term. By noticing that  $[\mathbf{h}_{RI}]_{m_1}$  and  $[\mathbf{h}_{IT}]_{m_2}$  are independent  $\forall m_1, m_2$ , and that  $[\mathbf{h}_{RI}]_{m_1}$  and  $[\mathbf{h}_{RI}]_{m_2}$  are independent if  $m_1 \neq m_2$ , we obtain

$$\bar{\rho}^{\text{D-RIS}} = \sum_{m=1}^{M} \mathbb{E} \left\{ |[\mathbf{h}_{RI}]_{m}|^{2} \right\}^{2} + \sum_{m_{1} \neq m_{2}} \mathbb{E} \left\{ |[\mathbf{h}_{RI}]_{m_{1}}| \right\}^{4}$$

$$= \sum_{m=1}^{M} 1 + \sum_{m_{1} \neq m_{2}} \left( \frac{\sqrt{\pi}}{2} \right)^{4},$$
(7)

where we exploited that  $\mathbb{E}\{|[\mathbf{h}_{RI}]_m|^2\}=1$  and  $\mathbb{E}\{|[\mathbf{h}_{RI}]_m|\}=\frac{\sqrt{\pi}}{2}$  in the second equality following the moments of the chi distribution with 2 degrees of freedom, yielding

 $\bar{\rho}^{\text{D-RIS}} = M + \frac{\pi^2}{16} M (M - 1).$  (8)

For a BD-RIS, the average channel gain is obtained by taking the expectation of (5), giving

$$\bar{\rho}^{\text{BD-RIS}} = \mathbb{E}\left\{ \|\mathbf{h}_{RI}\|_{2}^{2} \|\mathbf{h}_{IT}\|_{2}^{2} \right\}$$

$$= \mathbb{E}\left\{ \|\mathbf{h}_{RI}\|_{2}^{2} \right\} \mathbb{E}\left\{ \|\mathbf{h}_{IT}\|_{2}^{2} \right\}.$$
(9)

By noticing that  $\mathbb{E}\{\|\mathbf{h}_{RI}\|_2^2\} = \mathbb{E}\{\|\mathbf{h}_{IT}\|_2^2\} = M$  following the moments of the chi distribution with 2M degrees of freedom, we finally have

$$\bar{\rho}^{\text{BD-RIS}} = M^2. \tag{10}$$

In Fig. 4, we report the average channel gain offered by D-RIS and BD-RIS under i.i.d. Rayleigh distributed channels.

![](_page_5_Figure_1.jpeg)

Fig. 4. Average channel gain for D-RIS and BD-RIS-aided SISO systems. Both channels through RIS are i.i.d. Rayleigh distributed.

We compare the simulated channel gains, which are obtained by applying the proposed solutions detailed in Section IV-A and averaging over multiple channel realizations, with the theoretical channel gains derived in (10) and (8). As shown in Fig. 4, the simulation results confirm the accuracy of the closed-form scaling laws in (10) and (8). In the asymptotic regime where the number of RIS elements  $M \to \infty$ , the performance advantage of BD-RIS over D-RIS in a SISO system is quantified by the gain ratio

$$G^{\mathrm{BD}} = \lim_{M \to \infty} \frac{\bar{\rho}^{\mathrm{BD-RIS}}}{\bar{\rho}^{\mathrm{D-RIS}}} = \frac{16}{\pi^2} \approx 1.62,$$
 (11)

implying that BD-RIS achieves approximately a 62% higher channel gain than D-RIS. Although this fundamental result highlights the clear advantage of BD-RIS in SISO systems, the benefits of BD-RIS become even more pronounced in multiuser and multi-antenna scenarios. For instance, BD-RIS can provide up to 75% sum-rate improvement over D-RIS with M=128, as will be shown in Section V.

## III. MODELING, MODE ANALYSIS, AND ARCHITECTURE DESIGN OF BD-RIS

In this section, we introduce the modeling, architectures, and modes of BD-RIS, including the technical details, graphical illustrations, summaries and discussions.

### A. Preliminaries on Multi-Port Network Analysis

As a foundation on the BD-RIS modeling, we start by concisely reviewing the background knowledge on multiport network analysis, which is a simplified way to understand transmission properties compared to field analysis using Maxwell's equations, and a powerful and useful technique for modeling and studying wireless systems [34]. Specifically, each antenna in a wireless system is regarded as a port, whose behavior is characterized by its terminal voltage, current, incident wave, and reflected wave. This technique has been used to model and analyze MIMO systems [35]–[37], where some hardware impairments, such as mutual coupling and antenna mismatching, can be explicitly captured based on physics-consistent assumptions. Due to the fact that RIS is

![](_page_5_Picture_10.jpeg)

Fig. 5. An arbitrary M-port microwave network.

essentially a multi-port network regarding each element as one port, the multi-port network theory is naturally suitable for modeling RIS. Therefore, recently, this technique has also been used to model and study RIS-aided wireless communication systems [18], [26], [38], [39], by regarding transmit antennas, receive antennas, and RIS elements as a whole multi-port network. In this subsection, we briefly explain the concept of this technique, together with its three important parameters, namely, impedance, admittance, and scattering parameters, to lay the foundation for the modeling of BD-RIS [34].

1) Impedance, Admittance, and Scattering Parameters: Consider an arbitrary M-port microwave network, as depicted in Fig. 5. At the m-th port, the terminal voltage, current, incident wave, and reflected wave are given by  $v_m \in \mathbb{C}$ ,  $i_m \in \mathbb{C}, \ a_m \in \mathbb{C}, \ \text{and} \ b_m \in \mathbb{C}.$  Define the terminal voltage vector  $\mathbf{v} = [v_1, \dots, v_M]^\mathsf{T} \in \mathbb{C}^{M \times 1}$ , the current vector  $\mathbf{i} = [i_1, \dots, i_M]^\mathsf{T} \in \mathbb{C}^{M \times 1}$ , the incident wave vector  $\mathbf{a} = [a_1, \dots, a_M]^\mathsf{T} \in \mathbb{C}^{M \times 1}$ , and the reflected wave vector  $\mathbf{b} = [b_1, \dots, b_M]^\mathsf{T} \in \mathbb{C}^{M \times 1}$  for the M-port network. These four vectors are related to each other by  $\mathbf{v} = \mathbf{a} + \mathbf{b}$ ,  $\mathbf{i} = \frac{\mathbf{a} - \mathbf{b}}{Z_0}$ . The impedance matrix  $\mathbf{Z} \in \mathbb{C}^{M \times M}$  of the M-port network then relates the terminal voltage vector and current vector by  $\mathbf{v} = \mathbf{Z}\mathbf{i}$ . In the impedance matrix  $\mathbf{Z}$ , each entry  $[\mathbf{Z}]_{m,n}$  is the impedance between ports m and n when all other ports are open-circuited, i.e.,  $[\mathbf{Z}]_{m,n} = \frac{v_m}{i_n}\Big|_{i_k=0, \forall k \neq n}$ . Similarly, the admittance matrix  $\mathbf{Y} \in \mathbb{C}^{M \times M}$  of the M-port network relates the current vector and voltage vector by i = Yv. Therefore, we have  $\mathbf{Y} = \mathbf{Z}^{-1}$ . In  $\mathbf{Y}$ , each entry  $[\mathbf{Y}]_{m,n}$ is the admittance between ports m and n when all other ports are short-circuited, i.e.,  $[\mathbf{Y}]_{m,n} = \frac{i_m}{v_n}\Big|_{v_k=0, \forall k \neq n}$ . The scattering matrix  $\mathbf{S} \in \mathbb{C}^{M \times M}$  relates the incident wave vector and reflected wave vector by  $\mathbf{b} = \mathbf{S}\mathbf{a}$ . In  $\mathbf{S}$ , each entry  $[S]_{m,n}$  is the scattering coefficient from port n to port m when all other ports are terminated in matched loads, i.e.,  $[\mathbf{S}]_{m,n} = \left. rac{b_m}{a_n} \right|_{a_k = 0, \forall k 
eq n}$  . Based on the above illustration, the three parameters are related to each other by

$$\mathbf{S} = (\mathbf{Z} + Z_0 \mathbf{I}_M)^{-1} (\mathbf{Z} - Z_0 \mathbf{I}_M)$$
  
=  $(Y_0 \mathbf{I}_M + \mathbf{Y})^{-1} (Y_0 \mathbf{I}_M - \mathbf{Y}),$  (12)

![](_page_6_Figure_1.jpeg)

Fig. 6. An M-element passive RIS modeled as an M-antenna array connected an M-port reconfigurable impedance network.

where  $Z_0$  denotes the reference impedance and  $Y_0 = Z_0^{-1}$  denotes the reference admittance.

2) Reciprocal and Lossless Networks: Among all microwave networks, particularly important in practice are networks which are either reciprocal or lossless, or both. These networks also have specific mathematical characteristics. Specifically, for a reciprocal M-port network, any current  $i_m$  injected into port m produces a voltage  $v_n$  at port n,  $n \neq m$ , and  $i_m$  injected into port n produces a voltage  $v_n$  at port m. Note that reciprocal networks are widely adopted in practice since commonly used impedance/admittance components are reciprocal, e.g., resistors, capacitors, and inductors. This mathematically means the impedance, admittance, and scattering matrices of a reciprocal network are all symmetric, that is

$$\mathbf{Z} = \mathbf{Z}^{\mathsf{T}}, \mathbf{Y} = \mathbf{Y}^{\mathsf{T}}, \mathbf{S} = \mathbf{S}^{\mathsf{T}}. \tag{13}$$

Further, for a reciprocal and lossless M-port network, the net real power delivered to the network is zero, that is

$$P_{\mathsf{net}} = \frac{1}{2} \Re\{ \mathbf{v}^{\mathsf{T}} \mathbf{i}^* \} = \frac{1}{2} \Re\{ \mathbf{i}^{\mathsf{T}} \mathbf{Z} \mathbf{i}^* \} = 0.$$
 (14)

This is achieved when all entries of impedance and admittance matrices are purely imaginary, and thus when the scattering matrix is unitary, that is

$$\Re{\{\mathbf{Z}\}} = \mathbf{0}_{M \times M}, \Re{\{\mathbf{Y}\}} = \mathbf{0}_{M \times M}, \mathbf{S}^{\mathsf{H}}\mathbf{S} = \mathbf{I}_{M}.$$
 (15)

### B. Modeling and Classification

An M-element passive RIS is generally modeled as an M-antenna array connected to an M-port reconfigurable impedance network as illustrated in Fig. 6, which can be characterized by its impedance matrix  $\mathbf{Z}_I \in \mathbb{C}^{M \times M}$ , admittance matrix  $\mathbf{Y}_I \in \mathbb{C}^{M \times M}$ , or scattering matrix  $\mathbf{\Theta} \in \mathbb{C}^{M \times M}$  [26], [38]. These matrices are linked to each other by

$$\Theta = (\mathbf{Z}_I + Z_0 \mathbf{I}_M)^{-1} (\mathbf{Z}_I - Z_0 \mathbf{I}_M) 
= (Y_0 \mathbf{I}_M + \mathbf{Y}_I)^{-1} (Y_0 \mathbf{I}_M - \mathbf{Y}_I),$$
(16)

where  $\mathbf{Y}_I = \mathbf{Z}_I^{-1}$ . According to microwave network theory [34], for a passive reconfigurable impedance network, we have

$$\Theta^{\mathsf{H}}\Theta \prec \mathbf{I}_{M}.$$
 (17)

This guarantees that the power of reflected waves is no larger than the power of the waves impinging on the surface.

Specifically when the reconfigurable impedance network is lossless, we have that

$$\mathbf{\Theta}^{\mathsf{H}}\mathbf{\Theta} = \mathbf{I}_{M},\tag{18}$$

indicating that it is a unitary matrix. As per the mathematical properties of  $\mathbf{Z}_I$ ,  $\mathbf{Y}_I$ , and  $\boldsymbol{\Theta}$ , we introduce the following two-layer classifications of RIS.

1) D-RIS and BD-RIS: Based on whether the three matrices,  $\mathbf{Z}_I$ ,  $\mathbf{Y}_I$ , and  $\boldsymbol{\Theta}$  are diagonal or not, we categorize RIS as D-RIS with diagonal matrices and BD-RIS with matrices not limited to being diagonal [25].

Remark 1: Here we give toy examples for a 4-element D-RIS with a diagonal scattering matrix  $\Theta^D$  and a 4-element BD-RIS with a full scattering matrix  $\Theta^{BD}$ . Specifically in the lossless form of D-RIS, (18) indicates that  $|[\Theta^D]_{1,1}| = \ldots = |[\Theta^D]_{4,4}| = 1$ , which is consistent with the constraint commonly considered in existing D-RIS literature [8], [9]. This shows that a lossless D-RIS can only support phase control of signals. However, for BD-RIS, (18) indicates that  $||[\Theta^{BD}]_{:,1}||_2 = \ldots = ||[\Theta^{BD}]_{:,4}||_2 = 1$ . Therefore, we have  $|[\Theta^{BD}]_{m,n}| \leq 1$ ,  $\forall m,n=1,\ldots,4$ , implying that both amplitudes and phases of entries in  $\Theta^{BD}$  are tunable even in the lossless case.

2) Reciprocal and Non-Reciprocal BD-RIS: Further, based on whether the reconfigurable impedance network is reciprocal or not, we categorize BD-RIS as reciprocal BD-RIS with

$$\mathbf{Z}_I = \mathbf{Z}_I^\mathsf{T}, \ \mathbf{Y}_I = \mathbf{Y}_I^\mathsf{T}, \ \mathbf{\Theta} = \mathbf{\Theta}^\mathsf{T},$$
 (19)

and non-reciprocal BD-RIS with

$$\mathbf{Z}_I \neq \mathbf{Z}_I^\mathsf{T}, \mathbf{Y}_I \neq \mathbf{Y}_I^\mathsf{T}, \mathbf{\Theta} \neq \mathbf{\Theta}^\mathsf{T}.$$
 (20)

Remark 2: Here we reuse the examples for 4-element D-RIS and BD-RIS in Remark 1 to provide more insights. It is obvious that  $\Theta^D$  is naturally symmetric such that D-RIS is only a special case of the reciprocal BD-RIS. However,  $\Theta^{BD}$  can be symmetric or not, hence leading to reciprocal and non-reciprocal BD-RISs. This implies that non-reciprocity is an additional DoF arising from BD-RIS.

Benefiting from the flexible arrangement of elements and the circuit topology design of the reconfigurable impedance network, both reciprocal and non-reciprocal BD-RIS enable various modes and architectures, allowing us to establish an RIS classification tree as illustrated in Fig. 7. In the following subsections, we will elaborate on the mode analysis and architecture designs of BD-RIS, providing schematic and mathematical illustrations.

### C. Mode Analysis

According to the element arrangements, RIS has the following three modes.

1) Reflecting Mode: In this mode, the M elements are uniformly located toward the same direction, as illustrated in Fig. 8(a). With this arrangement, signals impinging on one side of the RIS are all reflected toward the same side, yielding a half-space coverage.

![](_page_7_Figure_1.jpeg)

Fig. 7. RIS classification tree.

![](_page_7_Figure_3.jpeg)

Fig. 8. 3D views of BD-RIS modes: (a) reflecting mode; (b) hybrid transmitting and reflecting mode; (c) multi-sector mode.

- 2) Hybrid Transmitting and Reflecting Mode: In this mode, every two elements are placed back to back and interconnected with each other via reconfigurable admittance components, as illustrated in Fig. 8(b) [40]. With this arrangement, signals impinging on one sector of the RIS can be partially reflected toward the same sector and partially scattered toward the other sector, yielding a full-space coverage. This is also known as simultaneous transmitting and reflecting surface (STARS), STAR-RIS, or intelligent omni-surface (IOS) [41]. An extreme case of such a hybrid mode refers to the transmitting mode, which means the signals impinging on one sector of the surface are purely scattered toward the other sector.
- 3) Multi-Sector Mode: In this mode, every L,  $L \geq 2$  elements are placed at the edge of an L-sided polygon and interconnected with each other via reconfigurable admittance components, as illustrated in Fig. 8(c) [42]. With this arrangement, signals impinging on one sector of RIS can be partially reflected toward the same sector and partially scattered toward the other sectors. More importantly, this arrangement allows each antenna to have a uni-directional radiation pattern covering only  $\frac{1}{L}$  space to avoid overlapping among sectors, which provides higher gains than the hybrid mode. Consequently, multi-sector mode includes hybrid mode as a special case with L=2, while it goes beyond hybrid mode to achieve highly directional full-space coverage.

Remark 3: Note that the D-RIS can only support reflective mode, while hybrid and multi-sector modes can only be

supported by BD-RIS. This is because both hybrid and multisector modes require interconnections between elements to enable the signal to flow from one element to another, which mathematically leads to admittance, impedance, and scattering matrices with nonzero off-diagonal entries.

### D. Architecture Design: Reciprocal Architectures

In the M-port reciprocal reconfigurable impedance network, each port is connected to ground via its own reconfigurable admittance<sup>1</sup> component,  $Y_m$ , and to port m',  $m' \neq m$ ,  $\forall m, m' \in \mathcal{M}$  via a reconfigurable admittance component  $Y_{m,m'}$ , which satisfies  $Y_{m,m'} = Y_{m',m}$  for m' > m. Hence, the admittance matrix<sup>2</sup>  $\mathbf{Y}_I$  of the reconfigurable impedance

<sup>1</sup>We use admittance parameter instead of impedance parameter to describe each reconfigurable component since admittance parameter describes the short-circuited property, that is how easily a circuit allows a current to flow. This allows us to have an admittance component with simply a zero admittance to describe that two elements are not connected. By contrast, the corresponding impedance component between the two elements will have an infinite value, which is not as straightforward as using admittance parameter. This will also simplify the mathematical modeling of various BD-RIS architectures, as will be detailed in the sequel.

 $^2 \text{We}$  use admittance matrix  $\mathbf{Y}_I$  instead of impedance matrix  $\mathbf{Z}_I$  to describe BD-RIS architectures since, according to (21), there is a linear mapping between the locations of nonzero entries in  $\mathbf{Y}_I$  and the circuit topology of a given architecture. For example, when  $Y_{m,m'}=0,\ m\neq m'$ , indicating that ports m and m' are not connected, the (m,m')-th entry of  $\mathbf{Y}_I$  is zero. By contrast, the corresponding impedance parameter-based descriptions have  $Z_{m,m'}=Y_{m,m'}^{-1},\ m\neq m',\ Z_m=Y_m^{-1}$  and  $\mathbf{Z}_I=\mathbf{Y}_I^{-1},\ \text{implying a}$  nonlinear mapping between the structure of  $\mathbf{Z}_I$  and certain circuit topologies. This means when  $Y_{m,m'}=0$ , equivalently  $Z_{m,m'}=\infty$ , the (m,m')-th entry of  $\mathbf{Z}_I$  could be neither zero nor  $\infty$ .

network is symmetric and each entry,  $[\mathbf{Y}_I]_{m,m'}$  linking ports m and m', can be calculated by making all other ports short-circuited [34]. Therefore, we have

$$[\mathbf{Y}_{I}]_{m,m'} = \begin{cases} -Y_{m,m'}, & m \neq m', \\ Y_{m} + \sum_{k \neq m} Y_{m,k}, & m = m'. \end{cases}$$
(21)

As per the circuit topology of the M-port reconfigurable impedance network, the reconfigurable admittance components  $Y_{m,m'}$ ,  $m \neq m'$  can be zero (indicating port m is not directly connected to port m') or not (indicating port m is directly connected to port m'), leading to the following reciprocal architectures of BD-RIS.

1) Single-Connected (i.e., D-RIS): In this architecture, each port  $m, \forall m \in \mathcal{M}$ , in the reconfigurable impedance network is connected to ground via its own reconfigurable admittance component,  $Y_m$  without interacting with other ports, i.e.,  $Y_{m,m'}=0, m \neq m'$ . This indicates that the single-connected architecture is realized by in total M reconfigurable admittance components. An illustrative example for a 4-element RIS with single-connected architecture is given in Fig. 9(a). Hence,  $\mathbf{Y}_I$  is a diagonal matrix

$$\mathbf{Y}_I = \mathsf{diag}(Y_1, \dots, Y_M). \tag{22}$$

By (16) and (18), for a lossless network, its impedance matrix  $\mathbf{Z}_I$  and scattering matrix  $\boldsymbol{\Theta}$  are also diagonal, and each diagonal entry in the latter has unit modulus, i.e.,

$$\Theta = \operatorname{diag}(\Theta_1, \dots, \Theta_M), \ |\Theta_m| = 1, \forall m \in \mathcal{M},$$
 (23)

where  $\Theta_m = \frac{Y_0 - Y_m}{Y_0 + Y_m}$  following (16). The single-connected RIS is also referred to as D-RIS with a diagonal matrix (3) in Section II and has been widely studied and applied in wireless communication systems [8], [9]. The corresponding scattering matrix  $\Theta$  is very often named as the phase-shift matrix since only the phase shift of each diagonal entry can be tuned.

2) Fully-Connected: To break through the strict mathematical constraint of  $\Theta$  in D-RIS and fully make use of the off-diagonal entries in  $\Theta$ , a fully-connected architecture which could effectively improve the wave manipulation flexibility of RIS has been proposed in [26]. In this architecture, each port m in the reconfigurable impedance network is connected to ground via  $Y_m$  and to another port m',  $m' \neq m$ ,  $\forall m, m' \in \mathcal{M}$  via  $Y_{m,m'}$ , which satisfies  $Y_{m,m'} = Y_{m',m}$  for m' > m. This indicates that the fully-connected architecture is realized by in total  $\frac{M(M+1)}{2}$  reconfigurable admittance components. An illustrative example for a 4-element BD-RIS with fully-connected architecture is given in Fig. 9(b). Hence,  $\mathbf{Y}_I$  is a full and symmetric matrix. By (16), for a lossless network, its impedance matrix  $\mathbf{Z}_I$  is also a full and symmetric matrix, and the scattering matrix  $\mathbf{\Theta}$  is a symmetric and unitary matrix, i.e.,

$$\mathbf{\Theta} = \mathbf{\Theta}^{\mathsf{T}}, \ \mathbf{\Theta}^{\mathsf{H}} \mathbf{\Theta} = \mathbf{I}_{M}. \tag{24}$$

3) Group-Connected: The circuit complexity (characterized by the required number of reconfigurable admittance components) of the fully-connected architecture grows quadratically with the number of elements M. This makes it difficult to implement fully-connected BD-RISs in practice especially when a large dimension is required. To trade the circuit

![](_page_8_Figure_12.jpeg)

Fig. 9. Examples of reciprocal architectures: (a) A 4-element D-RIS with single-connected architectures; (b) a 4-element BD-RIS with fully-connected architectures; (c) a 6-element BD-RIS with group-connected architectures (each group containing 3 interconnected elements); (d) a 4-element tridiagonal BD-RIS with tree-connected architectures; (e) a 5-element arrowhead BD-RIS with tree-connected architectures; (f) a 6-element BD-RIS with forest-connected architectures (each group containing 3 interconnected elements).

complexity and wave manipulation flexibility of RIS, a groupconnected architecture has been proposed in [26]. In this architecture, the M ports in the reconfigurable impedance network are uniformly divided into G groups, and every  $M = \frac{M}{G}$  ports within one group are connected to each other to construct a fully-connected architecture. Specifically, in group  $g, \forall g \in \mathcal{G} = \{1, \dots, G\}, \text{ each port } m_g = (g-1)M + m$ is connected to ground via it own reconfigurable admittance component  $Y_{m_q}$  and to another port  $m'_q = (g-1)\bar{M} + m'$ ,  $m' \neq m, \forall m, m' \in \bar{\mathcal{M}} = \{1, \dots, \bar{M}\}, \text{ via } Y_{m_g, m'_g}, \text{ which}$ satisfies  $Y_{m_g,m'_g} = Y_{m'_g,m_g}$  for m' > m. This indicates that the group-connected architecture is realized by in total  $G\frac{\bar{M}(\bar{M}+1)}{2} = \frac{M(\bar{M}+1)}{2}$  reconfigurable admittance components. An illustrative example for a 6-element BD-RIS with groupconnected architecture is given in Fig. 9(c). Hence,  $\mathbf{Y}_I$  is a block-diagonal matrix

$$\mathbf{Y}_{I} = \mathsf{blkdiag}(\mathbf{Y}_{I,1}, \dots, \mathbf{Y}_{I,G}), \tag{25}$$

where each  $\mathbf{Y}_{I,g} \in \mathbb{C}^{\bar{M} \times \bar{M}}$  is a full and symmetric matrix. Accordingly,  $\mathbf{Z}_I$  is a block-diagonal matrix with each block

being a full and symmetric matrix. By (16), for a lossless network, its scattering matrix  $\Theta$  is a block-diagonal matrix, with each block,  $\Theta_g \in \mathbb{C}^{\bar{M} \times \bar{M}}$ , being symmetric and unitary, i.e.,

$$\begin{aligned} & \boldsymbol{\Theta} = \mathsf{blkdiag}(\boldsymbol{\Theta}_1, \dots, \boldsymbol{\Theta}_G), \\ & \boldsymbol{\Theta}_g = \boldsymbol{\Theta}_g^\mathsf{T}, \ \boldsymbol{\Theta}_g^\mathsf{H} \boldsymbol{\Theta}_g = \mathbf{I}_{\bar{M}}, \forall g \in \mathcal{G}. \end{aligned}$$
 (26)

This architecture is a general illustration, including the fully-connected architecture with G=1 and the single-connected architecture with G=M as two special cases.

- 4) Tree-Connected: While fully-connected architecture has the highest wave manipulation flexibility to achieve optimal performance, this is achieved at the cost of complicated circuit topology design requiring numerous reconfigurable admittance components. To reduce the circuit complexity while maintaining the optimal (i.e., same as fully-connected) performance in single-user multiple input single output (MISO) systems, tree-connected architecture where the circuit topology forms a tree based on graph theory [43] has been proposed in [44]. In this architecture, the circuit complexity reduces to in total 2M-1 admittance components, which can be much less than that of the fully-connected architecture. Two typical tree-connected architectures, leading to respectively tridiagonal and arrowhead admittance matrices, have been introduced in [44] and are reviewed as follows.
  - Tridiagonal: In this case, each port m is connected to ground via its own admittance  $Y_m$  and to port m+1 via an admittance  $Y_{m,m+1}$ ,  $\forall m \in \mathcal{M} \setminus \{M\}$ . An illustrative example for a 4-element BD-RIS with such architecture is given in Fig. 9(d). This mathematically leads to a tridiagonal admittance matrix

$$\mathbf{Y}_{I} = \begin{bmatrix} [\mathbf{Y}_{I}]_{1,1} & [\mathbf{Y}_{I}]_{1,2} & \cdots & 0 \\ [\mathbf{Y}_{I}]_{1,2} & \ddots & \ddots & \vdots \\ \vdots & \ddots & \ddots & [\mathbf{Y}_{I}]_{M-1,M} \\ 0 & \cdots & [\mathbf{Y}_{I}]_{M-1,M} & [\mathbf{Y}_{I}]_{M,M} \end{bmatrix},$$
(27)

which is symmetric and contains nonzero entries only on the main diagonal, the lower diagonal, and the upper diagonal.

• Arrowhead: In this case, each port m is connected to ground via its own admittance  $Y_m$  and there is a central port c which connects to all other ports via  $Y_{c,m}$ ,  $\forall m \neq c, m \in \mathcal{M}$ . An illustrative example for a 5-element BD-RIS with such architecture is given in Fig. 9(e). Assuming c=1, we have an arrowhead admittance matrix

$$\mathbf{Y}_{I} = \begin{bmatrix} [\mathbf{Y}_{I}]_{1,1} & [\mathbf{Y}_{I}]_{1,2} & \cdots & [\mathbf{Y}_{I}]_{1,M} \\ [\mathbf{Y}_{I}]_{1,2} & [\mathbf{Y}_{I}]_{2,2} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ [\mathbf{Y}_{I}]_{1,M} & 0 & \cdots & [\mathbf{Y}_{I}]_{M,M} \end{bmatrix}, (28)$$

which is symmetric and contains nonzero entries only on the main diagonal, the first row, and the first column.

Remark 4: Due to the non-linear relationships between  $\mathbf{Y}_I$  and  $\mathbf{\Theta}$  as in (16), and between  $\mathbf{Y}_I$  and  $\mathbf{Z}_I$ , i.e.,  $\mathbf{Z}_I = \mathbf{Y}_I^{-1}$ , both  $\mathbf{Z}_I$  and  $\mathbf{\Theta}$  will be full matrices, similar to fully-connected

architecture. Take Fig. 9(d) as an example. For a 4-element tridiagonal BD-RIS, the resulting admittance matrix writes as

$$\mathbf{Y}_{I} = \begin{bmatrix} [\mathbf{Y}_{I}]_{1,1} & [\mathbf{Y}_{I}]_{1,2} & 0 & 0\\ [\mathbf{Y}_{I}]_{1,2} & [\mathbf{Y}_{I}]_{2,2} & [\mathbf{Y}_{I}]_{2,3} & 0\\ 0 & [\mathbf{Y}_{I}]_{2,3} & [\mathbf{Y}_{I}]_{3,3} & [\mathbf{Y}_{I}]_{3,4}\\ 0 & 0 & [\mathbf{Y}_{I}]_{3,4} & [\mathbf{Y}_{I}]_{4,4} \end{bmatrix},$$
(29)

where the locations of nonzero entries are one-to-one mapped to the circuit topology of a tree-connected architecture. However, the resulting  $\mathbf{Z}_I$  and  $\boldsymbol{\Theta}$  will be full matrices, making it difficult to mathematically distinguish tree- and fully-connected architectures. This implies that using  $\boldsymbol{\Theta}$  or  $\mathbf{Z}_I$  cannot fully reflect the mathematical constraint of the tree-connected architecture.

- 5) Forest-Connected: Similar to the extension from fullyconnected to group-connected architectures, the circuit complexity of the tree-connected architecture can be further reduced by dividing the M ports into G groups and constructing each group as a M-port tree-connected architecture. This is referred to as the forest-connected architecture [44] with a circuit complexity G(2M-1). An illustrative example for a 6element RIS with forest-connected architecture is given in Fig. 9(f). Hence,  $\mathbf{Y}_I$  is a block-diagonal matrix with each block being a symmetric and tridiagonal (or arrowhead) matrix. Two extreme cases with G = M and G = 1 respectively correspond to single-connected and tree-connected architectures. For a lossless network with the forest-connected architecture, its impedance matrix  $\mathbf{Z}_I$  also has a block-diagonal shape with each block being full and symmetric, and its scattering matrix  $\Theta$  is generally a block-diagonal matrix with each block being symmetric and unitary. Therefore, using  $\Theta$  or  $\mathbf{Z}_I$  is, gain, not sufficient to fully reflect the mathematical constraint of the forest-connected architecture.
- 6) Band- and Stem-Connected: Inspired by the tree-connected architecture that can perfectly match the performance of fully-connected architecture in single-user MISO systems with significantly reduced circuit complexity, the optimal architectures that can perfectly match the performance of fully-connected architecture in multi-user MIMO systems have been proposed in [45]. In the optimal architectures, each port is connected to ground via its own reconfigurable admittance component, while the number of interconnections between ports is theoretically constrained by the DoF in multi-user MIMO systems, and is generally much less than that of fully-connected architectures. Two representative examples which could construct optimal architectures, namely band-connected [45] and stem-connected [45], [46], are reviewed as follows.
  - Band-Connected: In this case, each port m is connected to ground via  $Y_m$  and to the following q ports, i.e.,  $m+1,\ldots,m+q$  (if any), via corresponding admittance components, where q denotes the band width. An illustrative example for a 4-element BD-RIS with band-connected architecture (q=2) is given in Fig. 10(a). This

![](_page_10_Picture_1.jpeg)

![](_page_10_Picture_2.jpeg)

Fig. 10. Examples of band- and stem-connected architectures: (a) a 4-element BD-RIS with band-connected architectures (band width q = 2); (b) a 5element BD-RIS with stem-connected architectures (stem width q=2).

mathematically leads to a band admittance matrix

$$\mathbf{Y}_{I} = \begin{bmatrix} [\mathbf{Y}_{I}]_{1,1} & \cdots & [\mathbf{Y}_{I}]_{1,q+1} & \cdots & 0 \\ \vdots & \ddots & & \ddots & \vdots \\ [\mathbf{Y}_{I}]_{1,q+1} & \ddots & \ddots & & \vdots \\ \vdots & & \ddots & & [\mathbf{Y}_{I}]_{M-q,M} \\ & \ddots & & & \vdots \\ 0 & \cdots & [\mathbf{Y}_{I}]_{M-q,M} & \cdots & [\mathbf{Y}_{I}]_{M,M} \end{bmatrix},$$
(30)

which is a symmetric matrix containing nonzero entries only on the main diagonal, the q lower diagonal, and the q upper diagonal. When q = 1, the band matrix boils down to the tridiagonal matrix, and thus band-connected BD-RIS includes the tridiagonal tree-connected BD-RIS as a special case.

Stem-Connected: In this case, each port is connected to ground via  $Y_m$ . Meanwhile, there are q ports with qdenoting the stem width, marked as  $c_i, \forall i \in \{1, \dots, q\}$ , each of which connects to all other ports via corresponding admittance components. An illustrative example for a 5-element BD-RIS with such architecture (q = 2, $c_1 = 1$ ,  $c_2 = 2$ ) is given in Fig. 10(b). Assuming  $c_i \in \{1, \ldots, q\}$ , we have an admittance matrix with the following structure:

$$\mathbf{Y}_{I} = \begin{bmatrix} \mathbf{A}_{q} & \mathbf{C}_{q} \\ \mathbf{C}_{q}^{\mathsf{T}} & \mathbf{D}_{q} \end{bmatrix}, \tag{31}$$

where

$$\mathbf{A}_{q} = \begin{bmatrix} [\mathbf{Y}_{I}]_{1,1} & \cdots & [\mathbf{Y}_{I}]_{1,q} \\ \vdots & \ddots & \vdots \\ [\mathbf{Y}_{I}]_{1,q} & \cdots & [\mathbf{Y}_{I}]_{q,q} \end{bmatrix},$$
(32a)
$$\mathbf{C}_{q} = \begin{bmatrix} [\mathbf{Y}_{I}]_{1,q+1} & \cdots & [\mathbf{Y}_{I}]_{1,M} \\ \vdots & \ddots & \vdots \\ [\mathbf{Y}_{I}]_{q,q+1} & \cdots & [\mathbf{Y}_{I}]_{q,M}, \end{bmatrix},$$
(32b)

$$\mathbf{C}_{q} = \begin{bmatrix} [\mathbf{Y}_{I}]_{1,q+1} & \cdots & [\mathbf{Y}_{I}]_{1,M} \\ \vdots & \ddots & \vdots \\ [\mathbf{Y}_{I}]_{q,q+1} & \cdots & [\mathbf{Y}_{I}]_{q,M}, \end{bmatrix}, \tag{32b}$$

$$\mathbf{D}_{q} = \mathsf{diag}([\mathbf{Y}_{I}]_{q+1,q+1}, \dots, [\mathbf{Y}_{I}]_{M,M}). \tag{32c}$$

Similarly,  $Y_I$  is symmetric containing nonzero entries only on the main diagonal, the first q rows, and the first q columns. When q = 1, the matrix in (31) boils down

![](_page_10_Figure_14.jpeg)

Fig. 11. An example of a reciprocal dynamically connected architecture where every two ports are connected by the series of a reconfigurable admittance and a switch.

to the arrowhead matrix, and thus stem-connected BD-RIS includes the arrowhead tree-connected BD-RIS as a special case.

It is worth noting that, similar to tree- and forest-connected architectures, for a lossless network with band- and stemconnected architectures, its impedance matrix  $\mathbf{Z}_I$  and scattering matrices  $\Theta$  will both be full matrices<sup>3</sup>. Therefore,  $\mathbf{Y}_I$ should be used to accurately reflect the constraint of these two architectures.

7) Dynamically Connected: In addition to the aforementioned fixed architectures which do not adapt to the channel environment (i.e., the admittance components are tuned but the circuit topology dictated by the interconnections is fixed), a dynamically connected architecture whose circuit topology can be changed during the transmission has also been proposed in [47]. This can be implemented by an admittance-switch network which enables a joint control of the values of admittance components and the ON/OFF states of switches. In this architecture, every port m is connected to ground via its own admittance  $Y_m$  and connected to port m', m' > m,  $\forall m, m' \in$  $\mathcal{M}$  by the series of an admittance  $Y_{m,m'}$  and a switch  $SW_{m,m'}$ . This indicates that the dynamically connected architecture is realized by in total  $\frac{M(M+1)}{2}$  reconfigurable admittance components and  $\frac{M(M-1)}{2}$  switches. An illustrative example for a 6-element RIS with dynamically connected architecture is given in Fig. 11. It is important to highlight that the admittance-switch network can be regarded as a general framework, which enables single/fully/group/tree/forest/band/stemconnected architectures by activating the corresponding interconnection links between ports. For example, the fullyconnected architecture is realized when all switches are turned

<sup>3</sup>Note that all the reciprocal architectures we talk about are explicitly described by the admittance parameter, instead of the scattering parameter. For example, the band-connected architecture has a band admittance matrix, where each nonzero entry in the off-diagonal indicates two ports are connected. However, the resulting scattering matrix will not be a band matrix, but instead a full matrix. This is also physically correct since a band-connected architecture essentially makes all the ports connected to each other, such that all entries in the scattering matrix can contribute to the wave scattering.

![](_page_11_Figure_1.jpeg)

Fig. 12. Examples of a 64-element group-connected BD-RIS with (a) adjacent grouping and (b) interlaced grouping.

![](_page_11_Figure_3.jpeg)

Fig. 13. Examples of non-reciprocal architectures: (a) 2 elements interconnect with each other via an isolator or gyrator; (b) 3 elements interconnect with each other via a circulator.

ON, and the single-connected architecture is realized when all switches are turned OFF. Beyond that, this admittance-switch network can also support various grouping strategies, different from the group/forest-connected architectures where the ports are uniformly and adjacently grouped. For example, one can control the switches to realize group-connected architectures with various group size of each group [47], or to realize group-connected architectures where each group contains interlaced elements [48], as illustrated in Fig. 12.

Remark 5: Note that for D-RIS, its impedance, admittance, and scattering matrices are all diagonal. This friendly mathematical structure has simplified a lot the modeling and signal processing of D-RIS-aided wireless systems. However, for BD-RIS, its three matrices do not always convey equivalent information. For example, for group-connected architecture, its three matrices are all block-diagonal. In this sense, one can use each of them for further studies. For another example, for tree/forest/band/stem-connected architectures, the mathematical structures are only captured in their admittance matrices. This means one should use the admittance matrix  $\mathbf{Y}_I$  and cannot use the scattering matrix  $\mathbf{\Theta}$  or the impedance matrix  $\mathbf{Z}_I$  of these architectures as objective variables for possible optimization and performance analysis.

### E. Architecture Design: Non-Reciprocal Architectures

In addition to the reciprocal architectures [26], [44], [45], [47], [48] summarized in the previous subsection, there are also non-reciprocal architectures of BD-RIS realized by nonreciprocal circuits, e.g., isolators, gyrators, circulators [49]-[51]. Specifically, [51] proposes a physics-consistent device model, where all the M elements are uniformly divided into G groups with each containing  $\overline{M}$  elements interconnecting with a non-reciprocal device. In each group, each element is modeled as a 2-port reciprocal network where one port interacts with free space and the other is connected to a non-reciprocal M-port circuit. Two illustrative examples<sup>4</sup> for a 2-element interconnected architecture realized by the isolator/gyrator and a 3-element interconnected architecture realized by the circulator are respectively given in Fig. 13(a) and Fig. 13(b). Due to the introduction of non-reciprocal circuits in each interconnected group, the resulting scattering matrix for a lossless network is a block-diagonal matrix, i.e.,  $\Theta = \mathsf{blkdiag}(\Theta_1, \dots, \Theta_G)$  with each block being asymmetric and unitary, that is

$$\Theta_g \neq \Theta_g^\mathsf{T}, \ \Theta_g^\mathsf{H} \Theta_g = \mathbf{I}_{\bar{M}}, \forall g \in \mathcal{G}.$$
(33)

One extreme case corresponds to the most flexible non-reciprocal BD-RIS whose scattering matrix is simply a full and unitary matrix. Another extreme case corresponds to the non-diagonal RIS [49], whose scattering matrix is asymmetric and contains only M nonzero entries. In this case,  $\Theta$  has the following form

$$\Theta = \Gamma_{\mathsf{r}} \bar{\Theta} \Gamma_{\mathsf{t}}, \ \bar{\Theta} = \mathsf{diag}(e^{j\theta_1}, \dots, e^{j\theta_M}),$$
 (34)

where  $\theta_m \in [0,2\pi), \forall m \in \mathcal{M}, \Gamma_r \in \{0,1\}^{M\times M}$  and  $\Gamma_t \in \{0,1\}^{M\times M}$  are two permutation matrices. This implies that signals impinging on one element are purely reflected by another element. Here we provide a toy example for a 4-element non-diagonal BD-RIS having

$$\mathbf{\Theta}^{ND} = \begin{bmatrix} 0 & [\mathbf{\Theta}]_{1,2} & 0 & 0\\ 0 & 0 & 0 & [\mathbf{\Theta}]_{2,4}\\ [\mathbf{\Theta}]_{3,1} & 0 & 0 & 0\\ 0 & 0 & [\mathbf{\Theta}]_{4,3} & 0 \end{bmatrix}, \quad (35)$$

where, for instance,  $[\Theta]_{1,2} \neq 0$  controls the signal flow from element 2 to element 1, that is, the signal impinging on element 2 is purely reflected by element 1.

Remark 6: Based on the above illustration, we notice that both reciprocal and non-reciprocal architectures have their pros and cons. On the one hand, reciprocal architectures have advantages over non-reciprocal ones from the following two perspectives: 1) The reciprocal architectures have mathematical constraints whose locations of nonzero entries are directly reflected in the circuit topology, and this can potentially facilitate the development of various optimization methods; 2) the reciprocal architectures have simpler circuit designs without embedding non-reciprocal devices and can

<sup>&</sup>lt;sup>4</sup>Although here we only give examples for 2-element and 3-element interconnected non-reciprical architectures for the purpose of easy illustration and simple hardware implementation, we would like to clarify that large-scale non-reciprocal architectures are practically feasible by using the combinations of multiple isolators and circulators.

![](_page_12_Picture_1.jpeg)

Fig. 14. Top views of BD-RIS modes: (a) hybrid transmitting and reflecting mode; (b) multi-sector mode.

be more cost-effective in practical implementations. On the other hand, non-reciprocal architectures have the advantage over reciprocal ones in providing more wave manipulation flexibility due to the relaxation of the symmetric constraint in the impedance/admittance/scattering matrix of BD-RIS.

### F. Unified Modes and Architectures

BD-RIS goes beyond D-RIS by introducing interconnections between elements, which provides the possibility to enable various circuit topologies offering more flexible beam manipulation and to enable various modes with enhanced coverage. To clearly show how the circuit topologies can support different modes, we provide the following two examples.

Example 1: Hybrid Mode Realized by Group-Connected Architecture. In this case, every two elements are back to back placed and interconnected with each other via a 2-port fully-connected architecture to construct a cell, and every  $\frac{\bar{M}}{2}$  cells are interconnected with each other to construct a group, as illustrated in Figs. 14(a) and 15(a). Therefore, we have the scattering matrix  $\Theta$  blocked as

$$\mathbf{\Theta} = \begin{bmatrix} \mathbf{\Theta}_{1,1} & \mathbf{\Theta}_{1,2} \\ \mathbf{\Theta}_{2,1} & \mathbf{\Theta}_{2,2} \end{bmatrix}, \tag{36}$$

where  $\Theta_{i,j} \in \mathbb{C}^{\frac{M}{2} \times \frac{M}{2}}$  describes the power scattering from sector j to sector i,  $\forall i, j \in \{1, 2\}$ , and each has a block-diagonal structure:

$$\Theta_{i,j} = \mathsf{blkdiag}(\Theta_{i,j,1}, \dots, \Theta_{i,j,G}), \forall i, j \in \{1, 2\},$$
 (37)

with  $\Theta_{i,j,g} \in \mathbb{C}^{\frac{\bar{M}}{2} \times \frac{\bar{M}}{2}}$ ,  $\forall g \in \mathcal{G}$ . When there is only one source located within the coverage of sector 1 as illustrated in Fig. 14(a), we introduce more intuitive notations, i.e.,  $\Theta_{\rm r} = \Theta_{1,1}$ ,  $\Theta_{\rm t} = \Theta_{2,1}$ ,  $\Theta_{\rm r,g} = \Theta_{1,1,g}$  and  $\Theta_{\rm t,g} = \Theta_{2,1,g}$ ,  $\forall g \in \mathcal{G}$  to describe the power reflecting (from sector 1 to sector 1) and transmitting (from sector 1 to sector 2) [40]. Then, when the group-connected reconfigurable impedance network is lossless, i.e.,  $\Theta^{\rm H}\Theta = \mathbf{I}_M$  and  $\Theta = \Theta^{\rm T}$ , we have the following constraint:

$$\Theta_{r,q}^{\mathsf{H}}\Theta_{r,g} + \Theta_{\mathsf{t},q}^{\mathsf{H}}\Theta_{\mathsf{t},g} = \mathbf{I}_{\underline{\bar{M}}}, \Theta_{r,g} = \Theta_{r,q}^{\mathsf{T}},$$
 (38)

which means the sum of the reflected power and transmitted power is conserved without loss. Specifically when  $G = \frac{M}{2}$ , both  $\Theta_{\rm r}$  and  $\Theta_{\rm t}$  are diagonal matrices, which correspond to the STARS, STAR-RIS or IOS [41].

![](_page_12_Figure_13.jpeg)

Fig. 15. Examples of (a) hybrid mode and (b) multi-sector mode realized by group-connected architectures.  $M=8,\,G=2,\,$  and  $\bar{M}=4$  for both examples, and L=4 for the multi-sector mode.

Example 2: Multi-Sector Mode Realized by Group-Connected Architecture. In this case, every L elements are located at the edge of a polygon and interconnected with each other via an L-port fully-connected architecture to construct a cell, as illustrated in Figs. 14(b) and 15(b). Here we focus on the case where cells are isolated from each other for simplicity, while we can also have inter-cell interconnections as in the hybrid mode. Therefore, we have the scattering matrix  $\Theta$  blocked as

$$\mathbf{\Theta} = \begin{bmatrix} \mathbf{\Theta}_{1,1} & \mathbf{\Theta}_{1,2} & \cdots & \mathbf{\Theta}_{1,L} \\ \mathbf{\Theta}_{2,1} & \mathbf{\Theta}_{2,2} & \cdots & \mathbf{\Theta}_{2,L} \\ \vdots & \vdots & \ddots & \vdots \\ \mathbf{\Theta}_{L,1} & \mathbf{\Theta}_{L,2} & \cdots & \mathbf{\Theta}_{L,L} \end{bmatrix}, \tag{39}$$

where  $\Theta_{i,j} \in \mathbb{C}^{\frac{M}{L} \times \frac{M}{L}}$  describes the power scattering from sector j to sector i,  $\forall i,j \in \mathcal{L} = \{1,\ldots,L\}$ , and, given the lack of inter-connections between cells in this example, each has a diagonal structure:

$$\Theta_{i,j} = \mathsf{diag}(\Theta_{i,j,1}, \dots, \Theta_{i,j,\frac{M}{2}}), \forall i, j \in \mathcal{L},$$
 (40)

with  $\Theta_{i,j,n} \in \mathbb{C}$ ,  $\forall n = 1, \dots, \frac{M}{L}$ . When there is only one source located within the coverage of sector 1, as illustrated in Fig. 14(b), we focus only on the first block-column of matrix  $\Theta$ , i.e.,  $\Theta_{l,1}$ ,  $\forall l \in \mathcal{L}$ , which describes the power scattering from sector 1 to all other sectors [42]. Then, when the reconfigurable impedance network is lossless, i.e.,  $\Theta^{\mathsf{H}}\Theta = \mathbf{I}_M$ , we have the constraint:

$$\sum_{l \in \mathcal{L}} |\Theta_{l,1,n}|^2 = 1, \forall n = 1, \dots, \frac{M}{L}.$$
 (41)

A special case with L=2 corresponds to the STARS, STAR-RIS, or IOS [41].

TABLE III
MATRIX PROPERTIES, SUPPORTED MODES, CIRCUIT COMPLEXITY, AND HIGHLIGHTS OF BD-RIS ARCHITECTURES

| Architectures         | Admittance Matrix Property                                                                                     | Supported Modes | Circuit Complexity                                             |  |  |
|-----------------------|----------------------------------------------------------------------------------------------------------------|-----------------|----------------------------------------------------------------|--|--|
| Single-Connected      | Diagonal                                                                                                       | Reflecting      | M Admittance Components                                        |  |  |
| Fully-Connected       | Full and Symmetric                                                                                             |                 | $\frac{M(M+1)}{2}$ Admittance Components                       |  |  |
| Group-Connected       | Block-Diagonal with                                                                                            | Reflecting,     | $\frac{M(\tilde{M}+1)}{2}$ Admittance Components               |  |  |
| 1                     | Each Block Full and Symmetric                                                                                  |                 | <u> </u>                                                       |  |  |
| Tree-Connected        | Tridiagonal/Arrowhead and Symmetric                                                                            | Hybrid,         | 2M-1 Admittance Components                                     |  |  |
| Forest-Connected      | Block-Diagonal with Each Block                                                                                 | Multi-Sector    | $G(2\bar{M}-1)$ Admittance Components                          |  |  |
| Totest Connected      | Tridiagonal/Arrowhead and Symmetric                                                                            | Train Sector    | , , ,                                                          |  |  |
| Band/Stem-Connected   | Band/Stem and Symmetric                                                                                        |                 | $(2M-q)\frac{q+1}{2}$ Admittance Components                    |  |  |
| Dynamically Connected | Permuted Block-Diagonal and Symmetric                                                                          |                 | $\frac{M(M+1)}{2}$ Admittances and $\frac{M(M-1)}{2}$ Switches |  |  |
| Non-Reciprocal        | Asymmetric                                                                                                     |                 | Depends on the Non-Reciprocal Circuit                          |  |  |
| Architectures         | Highlights                                                                                                     |                 |                                                                |  |  |
| Single-Connected      | The simplest architecture with the least circuit complexity and least beam manipulation flexibility            |                 |                                                                |  |  |
| Fully-Connected       | The most complex architecture with the highest circuit complexity and highest beam manipulation flexibility    |                 |                                                                |  |  |
| Group-Connected       | The flexibility-complexity trade-off between single-connected and fully-connected architectures                |                 |                                                                |  |  |
| Tree-Connected        | The simplest architecture with the least circuit complexity to achieve the optimum in single-user MISO systems |                 |                                                                |  |  |
| Forest-Connected      | The flexibility-complexity trade-off between single-connected and tree-connected architectures                 |                 |                                                                |  |  |
| Bound/Stem-Connected  | The simplest architecture with the least circuit complexity to achieve the optimum in multi-user MIMO systems  |                 |                                                                |  |  |
| Dynamically Connected | The circuit topology can be dynamically modified to adapt to channel state information (CSI)                   |                 |                                                                |  |  |
| Non-Reciprocal        | Can generate asymmetric beams for uplink and downlink to break the wireless channel reciprocity                |                 |                                                                |  |  |

Comparing the above two examples, we observe that the same circuit topologies can support various modes by modifying the element arrangements. Alternatively, the same mode can be realized by different architectures as long as elements within each cell are connected. For clarity, we have summarized the architectures, their matrix properties, the supported modes, circuit complexity (the required number of admittance components), and highlights in Table III.

### IV. SIGNAL PROCESSING FOR BD-RIS

In this section, we first focus on a simple SISO scenario to explain the representative tools for BD-RIS optimization. We then summarize the signal processing techniques, including optimization and performance analysis, and channel estimation, for more general BD-RIS-aided wireless communication systems.

### A. Optimizing BD-RIS: A Simple SISO Case

Consider a BD-RIS-aided SISO system, consisting of a single-antenna transmitter, a single-antenna receiver, and an M-element BD-RIS. Define the channels from transmitter to receiver, from the transmitter to BD-RIS, and from BD-RIS to receiver, respectively, as  $h_{RT} \in \mathbb{C}$ ,  $\mathbf{h}_{IT} \in \mathbb{C}^{M \times 1}$ , and  $\mathbf{h}_{RI} \in \mathbb{C}^{1 \times M}$ , which are perfectly known at the transmitter. According to [38], assuming perfect matching, no mutual coupling, no specular reflection, and unilateral approximation at all devices, the overall channel is given by  $h(\mathbf{\Theta}) = h_{RT} + \mathbf{h}_{RI}\mathbf{\Theta}\mathbf{h}_{IT}$ .

1) Solutions for Unitary  $\Theta$ : We start by considering the case that BD-RIS is characterized by a unitary matrix, i.e.,  $\Theta^{H}\Theta = \mathbf{I}_{M}$ . This corresponds to a lossless and non-reciprocal BD-RIS. Since  $\Theta$  can be easily rotated to align with the direct channel  $h_{RT}$  for channel strength maximization, here we

assume the direct link is blocked, i.e.,  $h_{RT} = 0$ , for the ease of illustration. Then, we formulated the following problem:

$$\max_{\mathbf{\Theta}} |\mathbf{h}_{RI} \mathbf{\Theta} \mathbf{h}_{IT}|^2$$
s.t.  $\mathbf{\Theta}^{\mathsf{H}} \mathbf{\Theta} = \mathbf{I}_M$ , (42)

which can be solved by the following three methods:

• Closed-Form Solution: Consider the matrix  $\mathbf{V}_{RI} \in \mathbb{C}^{M \times M}$  as a unitary matrix containing the right singular vectors of  $\mathbf{h}_{RI}$  in its columns. In other words, the first column of  $\mathbf{V}_{RI}$  is  $[\mathbf{V}_{RI}]_{:,1} = \frac{\mathbf{h}_{RI}^{\mathbf{h}}}{\|\mathbf{h}_{RI}\|_2}$  and the other columns of  $\mathbf{V}_{RI}$  are unit-norm vectors mutually orthogonal and orthogonal to  $[\mathbf{V}_{RI}]_{:,1}$ . Similarly, consider the matrix  $\mathbf{U}_{IT} \in \mathbb{C}^{M \times M}$  as a unitary matrix containing the left singular vectors of  $\mathbf{h}_{IT}$  in its columns. In other words, the first column of  $\mathbf{U}_{IT}$  is  $[\mathbf{U}_{IT}]_{:,1} = \frac{\mathbf{h}_{IT}}{\|\mathbf{h}_{IT}\|_2}$  and the other columns of  $\mathbf{U}_{IT}$  are unit-norm vectors mutually orthogonal and orthogonal to  $[\mathbf{U}_{IT}]_{:,1}$ . Given  $\mathbf{V}_{RI}$  and  $\mathbf{U}_{IT}$ , it is easy to see that a unitary matrix  $\mathbf{\Theta}$  globally solving problem (42) is

$$\mathbf{\Theta} = \mathbf{V}_{RI} \mathbf{U}_{IT}^{\mathsf{H}}.\tag{43}$$

The computational complexity mainly comes from the matrix multiplication and is thus  $\mathcal{O}(M^3)$ .

• Orthogonal Rotation: Following the idea in [52], any unitary matrix  $\Theta$  can be expressed using the following parameterization

$$\mathbf{\Theta} = \mathbf{\Theta}_0 \prod_{m=1}^{M-1} \prod_{n=m+1}^{M} \mathbf{R}_{m,n}, \tag{44}$$

where  $\Theta_0 \in \mathbb{C}^{M \times M}$  is an arbitrary unitary matrix and  $\mathbf{R}_{m,n} \in \mathbb{C}^{M \times M}$  denotes a Givens rotation matrix which performs an orthogonal rotation of the m-th and n-th columns of a unitary matrix with others fixed. A Givens rotation matrix  $\mathbf{R}_{m,n}$  is mathematically characterized

by two rotation parameters,  $\phi_{m,n}$  and  $\psi_{m,n}$ , and is constructed as

$$[\mathbf{R}_{m,n}]_{i,j} = \begin{cases} 1, & i = j, i \neq m, n, \\ \cos \phi_{m,n}, & i = j, i = m, n, \\ \sin \phi_{m,n} e^{j\psi_{m,n}}, & i = m, j = n, \\ -\sin \phi_{m,n} e^{-j\psi_{m,n}}, & i = n, j = m, \\ 0, & \text{otherwise.} \end{cases}$$
(45)

As such, the original problem is transformed into an unconstrained optimization containing M(M-1) rotation parameters of the corresponding rotation matrices, which can be directly solved by some searching-based methods, e.g., quasi-Newton methods. This solution requires around  $\mathcal{O}(I_1M^2(M-1)^2)$  complexity due to the use of quasi-Newton method to solve M(M-1) variables, where  $I_1$  denotes the number of iterations.

- Manifold: It is worth noting that the constraint  $\Theta^H\Theta = \mathbf{I}_M$  essentially forms a Manifold [53]. As such, a typical solution is to adopt the Manifold theory to construct an unconstrained optimization on the Manifold space, such that searching-based methods, such as Gradient-Descent, can be used on the Manifold space [54]. This solution requires  $\mathcal{O}(I_2M^3)$  complexity, where  $I_2$  denotes the number of iterations.
- 2) Solutions for Unitary and Symmetric  $\Theta$ : For the case of a reciprocal and lossless BD-RIS with fully-connected architecture, its scattering matrix is symmetric and unitary, that is  $\Theta = \Theta^{\mathsf{T}}$  and  $\Theta^{\mathsf{H}}\Theta = \mathbf{I}_M$ . In this case, the channel strength maximization problem becomes

$$\max_{\mathbf{\Theta}} |\mathbf{h}_{RI} \mathbf{\Theta} \mathbf{h}_{IT}|^{2}$$
s.t.  $\mathbf{\Theta} = \mathbf{\Theta}^{\mathsf{T}}, \mathbf{\Theta}^{\mathsf{H}} \mathbf{\Theta} = \mathbf{I}_{M}.$  (46)

One common idea to simplify the optimization is to decouple the unitary and symmetric constraint of  $\Theta$ . This can be done using the following three strategies.

• *Matrix Decomposition:* One way to decouple the constraints of  $\Theta$  is to decompose  $\Theta$  as  $\Theta = \mathbf{U}\mathbf{D}\mathbf{U}^\mathsf{T}$  [55], [56], where  $\mathbf{U} \in \mathbb{R}^{M \times M}$  is orthonormal, that is  $\mathbf{U}^\mathsf{T}\mathbf{U} = \mathbf{I}_M$  and  $\mathbf{D} \in \mathbb{C}^{M \times M}$  is a diagonal matrix whose diagonal entries have unit modulus, that is  $\mathbf{D} = \mathsf{diag}(D_1, \dots, D_M), |D_m| = 1, \forall m \in \mathcal{M}$ . Then the design of  $\Theta$  is transformed to the design of  $\mathbf{D}$  and  $\mathbf{U}$ :

$$\mathcal{T}' = \{ \{ \mathbf{U}, \mathbf{D} \} \mid \mathbf{U} \in \mathbb{R}^{M \times M}, \mathbf{U}^{\mathsf{T}} \mathbf{U} = \mathbf{I}_{M}, \\ \mathbf{D} = \mathsf{diag}(D_{1}, \dots, D_{M}), |D_{m}| = 1, \forall m \},$$
(47)

both having closed-form solutions as detailed in [55], [56]. Alternatively,  $\Theta$  can be decomposed as  $\Theta = \Psi \Psi^{\mathsf{T}}$  [57]. As such, the design of a unitary and symmetric matrix  $\Theta$  is equivalent to that of a unitary matrix  $\Psi \in \mathbb{C}^{M \times M}$ , that is

$$\mathcal{T}'' = \{ \mathbf{\Psi} \mid \mathbf{\Psi}^{\mathsf{H}} \mathbf{\Psi} = \mathbf{I}_M \}, \tag{48}$$

which can be obtained in closed form based on the knowledge of channels as detailed in [57]. The matrix decomposition requires around  $\mathcal{O}(M^3)$  due to the use of eigenvalue and Takagi's decomposition.

• *Projection:* One can first relax the two constraints of  $\Theta$  and find a solution for a more tractable problem, such as the following problem:

$$\max_{\mathbf{\Theta}} |\mathbf{h}_{RI}\mathbf{\Theta}\mathbf{h}_{IT}|^2$$
s.t.  $\|\mathbf{\Theta}\|_{\mathsf{F}}^2 \le M$ , (49)

and then applies the symmetric unitary projection to satisfy the original constraints [58]. That is, with  $\Theta_{\text{opt}}$  as the solution to (49) as detailed in [58], its symmetric projection is given by

$$\Theta_{\mathsf{sym}} = \frac{1}{2} (\Theta_{\mathsf{opt}} + \Theta_{\mathsf{opt}}^{\mathsf{T}}).$$
 (50)

Then,  $\Theta_{\text{sym}}$  is further projected to the unitary domain by solving an orthogonal Procrustes problem [59], i.e.,

$$\Theta_{\mathsf{symuni}} = \arg\min_{\boldsymbol{\Theta}^{\mathsf{H}}\boldsymbol{\Theta} = \mathbf{I}_{M}} \ \|\boldsymbol{\Theta} - \boldsymbol{\Theta}_{\mathsf{sym}}\|_{\mathsf{F}}^{2} = \mathbf{U}_{1}\mathbf{U}_{2}^{\mathsf{H}}, \ (51)$$

where  $\mathbf{U}_1 \in \mathbb{C}^{M \times M}$  and  $\mathbf{U}_2 \in \mathbb{C}^{M \times M}$  are unitary matrices from the singular value decomposition (SVD) of  $\Theta_{\text{sym}}$ , i.e.,  $\Theta_{\text{sym}} = \mathbf{U}_1 \mathbf{\Sigma} \mathbf{U}_2^{\text{H}}$  with  $\mathbf{\Sigma}$  being a diagonal matrix containing the singular values of  $\Theta_{\text{sym}}$  in a decreasing order. The projection requires around  $\mathcal{O}(M^3)$  due to the use of SVD.

• Introducing Auxiliary Variables: Another direct way to decouple the two constraints of  $\Theta$  is to introduce an auxiliary variable  $\Phi = \Theta$  [60], such that  $\Theta$  is only subject to the unitary constraint and  $\Phi$  is only subject to the symmetric constraint, or vise versa. In this way, the equality constraint  $\Phi = \Theta$  can be penalized to construct the associated Lagrangian function and problem (46) can be transformed into a double-variable optimization

$$\max_{\boldsymbol{\Theta}, \boldsymbol{\Phi}} |\mathbf{h}_{RI} \boldsymbol{\Theta} \mathbf{h}_{IT}|^2 - \frac{\rho_1}{2} \|\boldsymbol{\Phi} - \boldsymbol{\Theta}\|_{\mathsf{F}}^2 - \Re \{ \mathsf{tr}(\boldsymbol{\Lambda}^{\mathsf{H}} (\boldsymbol{\Phi} - \boldsymbol{\Theta})) \}$$
s.t.  $\boldsymbol{\Phi}^{\mathsf{H}} \boldsymbol{\Phi} = \mathbf{I}_M, \boldsymbol{\Theta} = \boldsymbol{\Theta}^{\mathsf{T}},$  (52)

where  $\rho_1 > 0$  is the penalty parameter and  $\mathbf{\Lambda} \in \mathbb{C}^{M \times M}$  is the dual variable. Then, the two variables can be alternatively designed. Specifically, the sub-problem for  $\mathbf{\Theta}$  with given  $\mathbf{\Phi}$  is essentially an unconstrained optimization when focusing only on the diagonal and upper-triangular (or equivalently lower-triangular) entries of  $\mathbf{\Theta}$ . As such, some well-known searching-based methods for unconstrained optimization, such as Gradient-Descent, can be directly adopted. The sub-problem for  $\mathbf{\Phi}$  with given  $\mathbf{\Theta}$  is again an orthogonal Procrustes problem [59], whose closed-form solution can be obtained by performing SVD to  $\rho_1\mathbf{\Theta} + \mathbf{\Lambda}$ . The overall complexity of such a solution depends on the specific methods used to solve the sub-problem for a symmetric  $\mathbf{\Theta}$ .

Remark 7: The matrix decomposition  $\Theta = \mathbf{U}\mathbf{D}\mathbf{U}^\mathsf{T}$  [55], [56] provides interesting insights to understand the relationship between BD-RIS and D-RIS. That is, a BD-RIS can be decoupled as a power divider controlled by  $\mathbf{U}$  and a phase shifter network characterized by  $\mathbf{D}$ . In D-RIS, we have  $\mathbf{U} = \mathbf{I}_M$ , indicating that signals impinging on one element can only be reflected by the same one. However, in BD-RIS, a flexible

power divider is enabled by inter-element connections such that the waves impinging on one element can (partially) flow to other elements and further be reflected.

3) Solutions for  $\mathbf{Y}_I$ : As discussed in Remark 4, for BD-RIS with tree/forest/stem/band-connected architectures, directly designing the scattering matrix  $\boldsymbol{\Theta}$  cannot fully reflect their mathematical constraints. In this case, we should design the admittance matrix  $\mathbf{Y}_I$  based on the following problem:

$$\max_{\mathbf{Y}_{I}} |\mathbf{h}_{RI} \mathbf{\Theta} \mathbf{h}_{IT}|^{2}$$
s.t. 
$$\mathbf{\Theta} = (Y_{0} \mathbf{I}_{M} + \mathbf{Y}_{I})^{-1} (Y_{0} \mathbf{I}_{M} - \mathbf{Y}_{I}), \qquad (53)$$

$$\mathbf{Y}_{I} \in \mathcal{Y}.$$

where  $\mathcal{Y}$  denotes the constraint of  $\mathbf{Y}_I$  varying according to architectures illustrated in Section III-D. The main difficulty in optimizing BD-RIS here lies in the matrix inverse due to the nonlinear mapping between  $\boldsymbol{\Theta}$  and  $\mathbf{Y}_I$ . To tackle this difficulty, there are in general three strategies.

• Closed-Form Solutions: As illustrated in Section II, the channel strength in (53) is upper-bounded by  $|\mathbf{h}_{RI}\mathbf{\Theta}\mathbf{h}_{IT}|^2 \leq \|\mathbf{h}_{RI}\|_2^2 \|\mathbf{h}_{IT}\|_2^2$ , where the equality is achieved when

$$\bar{\mathbf{h}}_{RI}^{\mathsf{H}} = \mathbf{\Theta} \bar{\mathbf{h}}_{IT},\tag{54}$$

with  $\bar{\mathbf{h}}_{RI}=\frac{\mathbf{h}_{RI}}{\|\mathbf{h}_{RI}\|_2}$  and  $\bar{\mathbf{h}}_{IT}=\frac{\mathbf{h}_{IT}}{\|\mathbf{h}_{IT}\|_2}.$  By (16), (54) can be rewritten as

$$(Y_0 \mathbf{I}_M + \mathbf{Y}_I) \bar{\mathbf{h}}_{RI}^{\mathsf{H}} = (Y_0 \mathbf{I}_M - \mathbf{Y}_I) \bar{\mathbf{h}}_{IT}$$
  
$$\Rightarrow \mathbf{Y}_I (\bar{\mathbf{h}}_{RI}^{\mathsf{H}} + \bar{\mathbf{h}}_{IT}) = Y_0 (\bar{\mathbf{h}}_{IT} - \bar{\mathbf{h}}_{RI}^{\mathsf{H}}).$$
(55)

It turns out that it is sufficient to solve linear equations in (55) as the global optimal solution of (53). Note that with a given architecture, one can always focus only on the nonzero entries in  $\mathbf{Y}_I$  and solve (55). Such a closed-form solution for tree/forest-connected architectures has been derived in [44], which requires  $\mathcal{O}(M^3)$  complexity due to the matrix inversion.

- Searching-Based Methods: The optimization problem (53) is essentially unconstrained by focusing only on the upper-triangular (or equivalently lower-triangular) and diagonal entries of  $\mathbf{Y}_I$ . This can be directly solved by some searching-based methods, such as the quasi-Newton method [26], which requires  $\mathcal{O}(I_3 \frac{M^2(M+1)^2}{4})$  to solve  $\frac{M(M+1)}{2}$  variables, where  $I_3$  denotes the number of iterations.
- Introducing Auxiliary Variables: One can introduce  $\mathbf{u} = \mathbf{h}_{RI}\boldsymbol{\Theta}$ , such that the matrix inverse can be eliminated by transferring it to a bilinear constraint [61]:

$$\Theta = (Y_0 \mathbf{I}_M + \mathbf{Y}_I)^{-1} (Y_0 \mathbf{I}_M - \mathbf{Y}_I)$$
  

$$\Rightarrow \mathbf{u}(Y_0 \mathbf{I}_M + \mathbf{Y}_I) = \mathbf{h}_{RI} (Y_0 \mathbf{I}_M - \mathbf{Y}_I).$$
(56)

Again, the equality constraint  $\mathbf{u}(Y_0\mathbf{I}_M + \mathbf{Y}_I) = \mathbf{h}_{RI}(Y_0\mathbf{I}_M - \mathbf{Y}_I)$  can be penalized to construct the

associated Lagrangian function and problem (53) can be transformed into the following form

$$\max_{\mathbf{u}, \mathbf{Y}_{I}} |\mathbf{u}\mathbf{h}_{IT}|^{2} - \frac{\rho_{1}}{2} \|\mathbf{u}(Y_{0}\mathbf{I}_{M} + \mathbf{Y}_{I}) - \mathbf{h}_{RI}(Y_{0}\mathbf{I}_{M} - \mathbf{Y}_{I})\|_{2}^{2} - \Re\{((\mathbf{u}(Y_{0}\mathbf{I}_{M} + \mathbf{Y}_{I}) - \mathbf{h}_{RI}(Y_{0}\mathbf{I}_{M} - \mathbf{Y}_{I}))\boldsymbol{\lambda}^{\mathsf{H}}\}$$
s.t.  $\mathbf{Y}_{I} \in \mathcal{Y}$ , (57)

where  $\rho_2 > 0$  denotes the penalty parameter and  $\lambda \in \mathbb{C}^{1 \times M}$  denotes the dual variable. Then the two variables can be alternatively optimized, where the sub-problem for  $\mathbf{u}$  is unconstrained and the sub-problem for  $\mathbf{Y}_I$  is also unconstrained when focusing on optimizing only the non-zero entries in  $\mathbf{Y}_I$ . The overall complexity of this solution depends on the specific methods used to solve two unconstrained sub-problems.

Based on the above explanations, there are some representative solutions using existing optimization techniques to deal with different BD-RIS constraints. The mapping between constraints of BD-RIS and their representative solutions is summarized in Table IV.

### B. Survey on BD-RIS Optimization and Performance Analysis

The representative solutions for BD-RIS optimization in SISO systems can be flexibly used to solve some extracted sub-problems in more general scenarios, such as MIMO and multi-user systems. In this subsection, we will provide a comprehensive survey on BD-RIS optimization and performance analysis in various scenarios.

Consider a general BD-RIS-aided multi-user MIMO system consisting of an N-antenna transmitter, an M-element BD-RIS, and K multi-antenna users, each of which has  $N_k$  antennas,  $\forall k \in \mathcal{K} = \{1,\ldots,K\}$ . Define the wireless channels from the transmitter to user k as  $\mathbf{H}_{RT,k} \in \mathbb{C}^{N_k \times N}$ , from the transmitter to BD-RIS as  $\mathbf{H}_{IT} \in \mathbb{C}^{M \times N}$ , and from the BD-RIS to user k as  $\mathbf{H}_{RI,k} \in \mathbb{C}^{N_k \times M}$ . According to [38], assuming perfect matching, no mutual coupling, no specular reflection, and unilateral approximation at all devices, the overall channel  $\mathbf{H}_k(\mathbf{\Theta}) \in \mathbb{C}^{N_k \times N}$  from the transmitter to user k, which is a function of the scattering matrix  $\mathbf{\Theta}$  of BD-RIS, writes as

$$\mathbf{H}_{k}(\mathbf{\Theta}) = \mathbf{H}_{RT,k} + \mathbf{H}_{RI,k}\mathbf{\Theta}\mathbf{H}_{IT}, \forall k \in \mathcal{K}.$$
 (58)

Define a precoder matrix  $\mathbf{W} = [\mathbf{W}_1, \mathbf{W}_2, \dots, \mathbf{W}_K] \in \mathbb{C}^{N \times (\sum_{k \in \mathcal{K}} N_{\mathsf{s},k})}$ , where  $\mathbf{W}_k \in \mathbb{C}^{N \times N_{\mathsf{s},k}}$  denotes the precoder matrix for user k and  $N_{\mathsf{s},k}$  denotes the number of data streams to be transmitted to user k. Assuming perfect CSI is known at the transmitter, the joint transmit precoder and BD-RIS design problem can be formulated as the following admittance matrix based form

$$\max_{\mathbf{W}, \mathbf{\Theta}, \mathbf{Y}_{I}} F(\mathbf{W}, {\mathbf{H}_{k}(\mathbf{\Theta})}_{\forall k})$$
s.t. 
$$\mathbf{\Theta} = (Y_{0}\mathbf{I}_{M} + \mathbf{Y}_{I})^{-1}(Y_{0}\mathbf{I}_{M} - \mathbf{Y}_{I}), \qquad (59)$$

$$\mathbf{Y}_{I} \in \mathcal{Y},$$

$$\mathbf{W} \in \mathcal{W},$$

TABLE IV BD-RIS ARCHITECTURES AND CONSTRAINTS, DIFFICULTIES, AND SOLUTIONS

| Architectures† and Constraints                                                                    | Difficulties                                   | Solutions‡                                                                                                                                                                                                                                                                                                                                                                                       | Optimality | Complexity                                          |
|---------------------------------------------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------|
|                                                                                                   |                                                | • Construct $\Theta$ by two unitary matrices based on $\mathbf{h}_{RI}$ and $\mathbf{h}_{IT}$ , i.e., $\Theta = \mathbf{V}_{RI}\mathbf{U}_{IT}^{H}$ with $[\mathbf{V}_{RI}]_{:,1} = \frac{\mathbf{h}_{RI}^{H}}{\ \mathbf{h}_{IT}\ _2} = \bar{\mathbf{h}}_{RI}^{H}$ and $[\mathbf{U}_{IT}]_{:,1} = \frac{\mathbf{h}_{IT}^{H}}{\ \mathbf{h}_{IT}\ _2} = \bar{\mathbf{h}}_{IT}$ . ( $\circledast$ ) | Yes        | $\mathcal{O}(M^3)$                                  |
| Non-reciprocal architecture with $\mathbf{\Theta}^{H}\mathbf{\Theta} = \mathbf{I}_{M}$            | Unitary<br>constraint                          | • Decouple $\Theta = \Theta_0 \prod_{m=1}^{M-1} \prod_{n=m+1}^{M} \mathbf{R}_{m,n}$ , transform to an unconstrained optimization and use searching-based methods, e.g., quasi-Newton method [52].                                                                                                                                                                                                | No         | $\mathcal{O}(I_1 M^2 (M-1)^2)$                      |
|                                                                                                   |                                                | Adopt the Manifold theory to construct a     Manifold and transform the constrained     optimization to unconstrained optimization     on Manifold space, on which the searching     -based methods, e.g., Gradient-Descent,     can be used [40], [54].                                                                                                                                         | No         | $\mathcal{O}(I_2M^3)$                               |
|                                                                                                   |                                                | • Matrix decomposition $\Theta = \mathbf{U}\mathbf{D}\mathbf{U}^T$ with $\mathcal{T}'$ [55], [56] or $\Theta = \Psi\Psi^T$ with $\mathcal{T}''$ [57];                                                                                                                                                                                                                                            | Yes        | $\mathcal{O}(M^3)$                                  |
| Fully/group-connected architectures with $\Theta^H \Theta = \mathbf{I}_M$ and $\Theta = \Theta^T$ | Coupled unitary and symmetric                  | • Symmetric and unitary projections by $\Theta_{\text{sym}} = \frac{1}{2}(\Theta_{\text{opt}} + \Theta_{\text{opt}}^{T})$ and solving the orthogonal Procrustes problem $\Theta = \arg\min_{\Theta^{H}\Theta = \mathbf{I}_{M}} \ \Theta - \Theta_{\text{sym}}\ _{F}^{2}$ [58];                                                                                                                   | No         | $\mathcal{O}(M^3)$                                  |
|                                                                                                   | constraints                                    | • Introduce auxiliary variables $\Phi = \Theta$ , with $\Phi = \Phi^{T}$ and $\Theta^{H}\Theta = \mathbf{I}_M$ , or vise versa [60].                                                                                                                                                                                                                                                             | No         | Θ                                                   |
| Arbitrary reciprocal architectures                                                                |                                                | • Extract non-zero entries in $\mathbf{Y}_I$ and globally solve linear equations $\mathbf{Y}_I(\bar{\mathbf{h}}_{RI}^H + \bar{\mathbf{h}}_{IT}) = Y_0(\bar{\mathbf{h}}_{IT} - \bar{\mathbf{h}}_{RI}^H). \ (\circledast)$                                                                                                                                                                         | Yes        | $\mathcal{O}(M^3)$                                  |
| with $\dot{\mathbf{\Theta}} = (\mathbf{\hat{Y}}_0 \mathbf{I}_M + \mathbf{Y}_I)^{-1}$              | Matrix inverse from $\Theta$ to $\mathbf{Y}_I$ | Searching-based methods, e.g., quasi-Newton<br>method [26] not sensitive to matrix structures.                                                                                                                                                                                                                                                                                                   | No         | $\mathcal{O}\left(I_3 \frac{M^2 (M+1)^2}{4}\right)$ |
| $	imes (\mathbf{Y}_0\mathbf{I}_M - \mathbf{Y}_I)$ and $\mathbf{Y}_I \in \mathcal{Y}$              |                                                | • Introduce auxiliary variables, e.g., $\mathbf{u} = \mathbf{h}_{RI} \mathbf{\Theta}$ , to eliminate the matrix inverse by $\mathbf{\Theta} = (Y_0 \mathbf{I}_M + \mathbf{Y}_I)^{-1} (Y_0 \mathbf{I}_M - \mathbf{Y}_I) \Rightarrow \mathbf{u}(Y_0 \mathbf{I}_M + \mathbf{Y}_I) = \mathbf{h}_{RI} (Y_0 \mathbf{I}_M - \mathbf{Y}_I)$ [61].                                                        | No         | Θ                                                   |

<sup>†</sup> The architectures are all reciprocal unless otherwise stated.

where  $F(\mathbf{W}, \{\mathbf{H}_k(\mathbf{\Theta})\}_{\forall k})$  denotes a general utility function varying according to performance metrics,  $\mathcal{Y}$  denotes the constraint of  $\mathbf{Y}_I$  varying according to architectures, and  $\mathcal{W}$  denotes the constraint of the precoder matrix varying according to budget requirements. Note that (59) can be used to optimize all reciprocal architectures in Section III-D where  $\mathbf{Y}_I$  is explicitly defined and constrained. Alternatively, the optimization problem can be formulated as the following scattering matrix based form

$$\max_{\mathbf{W}, \mathbf{\Theta}} F(\mathbf{W}, {\mathbf{H}_{k}(\mathbf{\Theta})}_{\forall k})$$
s.t.  $\mathbf{\Theta} \in \mathcal{T},$ 

$$\mathbf{W} \in \mathcal{W},$$
(60)

where  $\mathcal{T}$  denotes the constraints of  $\Theta$  and varying according to architectures. Note that (60) can be used to optimize single-, group-, fully-connected architectures in Section III-D and non-reciprocal architectures in Section III-E.

The expressions of utility functions and the constraints of variables adapting to various wireless scenarios and corresponding beamforming solutions to tackle the above difficulties are specified below.

1) Received Power Maximization for Multiple Input Single Output (MISO) and Single Input Multiple Output (SIMO): In MISO systems, we have  $N_k = K = N_{s,k} = 1$ , and the utility function becomes

$$F_{\mathsf{MISO}}(\mathbf{w}, \mathbf{h}(\mathbf{\Theta})) = |\mathbf{h}(\mathbf{\Theta})\mathbf{w}|^2,$$
 (61)

where  $\mathbf{h}(\mathbf{\Theta}) = \mathbf{h}_{RT} + \mathbf{h}_{RI}\mathbf{\Theta}\mathbf{H}_{IT}$  with  $\mathbf{h}_{RT} \in \mathbb{C}^{1 \times N}$  and  $\mathbf{w} \in \mathbb{C}^{N \times 1}$  denotes the precoder vector constrained by the set

$$\mathcal{W}_{\mathsf{MISO}} = \{ \mathbf{w} \mid \|\mathbf{w}\|_2^2 \le P \},\tag{62}$$

where P denotes the power budget at the transmitter. In this case, the optimization problem has multiple variables and the typical solution is to iteratively design the BD-RIS and the transmit precoder until the convergence of the objective function is guaranteed. Specifically, when the BD-RIS is given, the optimal transmit precoder takes the form of the maximum ratio transmission scheme. When the transmit precoder is given, the design of BD-RIS boils down to the SISO case such that the solutions for various fixed reciprocal and non-reciprocal architectures summarized in Section IV-A can be directly used. In the sequel, we elaborate the solutions for some dynamic BD-RIS architectures.

For reciprocal BD-RIS, with the form of (60) and the constraint of dynamically connected architectures, [48] has proposed an offline grouping strategy design adapting to the

<sup>‡</sup> The solutions that end up with (®) can only be used in SISO systems, while others are applicable to multi-antenna/user scenarios.

<sup>&</sup>lt;sup>†</sup> The notation  $I_i$ ,  $\forall i \in \{1, 2, 3\}$  denotes the number of iterations to guarantee the convergence of different methods.

<sup>&</sup>lt;sup>‡</sup> The complexity of solutions that marked as ⊝ is determined by specific methods used to solve unconstrained optimization problems.

static CSI. For non-reciprocal BD-RIS, the following beamforming design and performance analysis studies have been conducted. With the form of (60) and a non-reciprocal BD-RIS architecture having non-diagonal scattering matrices being constrained by the set

$$\mathcal{T}_{\text{non-diag}} = \{ \boldsymbol{\Theta} \mid \boldsymbol{\Theta} = \boldsymbol{\Gamma}_{\mathbf{r}} \bar{\boldsymbol{\Theta}} \boldsymbol{\Gamma}_{\mathbf{t}}, \\ \bar{\boldsymbol{\Theta}} = \text{diag}(e^{j\theta_1}, \dots, e^{j\theta_M}), \theta_m \in [0, 2\pi), \forall m \},$$
 (63)

closed-form solutions can be derived. Focusing primarily on SISO systems with the utility function  $F_{\text{SISO}}(h(\Theta))$ , [49] has derived the performance upper-bound and the closed-form solution for BD-RIS. The beamforming design is later extended to MISO systems with the utility function  $F_{\text{MISO}}(\mathbf{w}, \mathbf{h}(\Theta))$ . With the form of (60), [50] has further proposed a coordinated non-reciprocal group-connected architecture with scattering matrices having more than M non-zero entries, and derived the optimal grouping strategy which could maximize  $F_{\text{MISO}}(\mathbf{w}, \mathbf{h}(\Theta))$ . This architecture is further used to support the multi-sector mode and maximize  $F_{\text{MISO}}(\mathbf{w}, \mathbf{h}(\Theta))$  related to specific users [62].

From the problem formulation and optimization perspectives, the single input multiple output (SIMO) system is equivalent to the MISO system. Therefore, the aforementioned solutions for SISO systems in Section IV-A and MISO systems are readily applicable for SIMO systems.

2) Capacity Maximization for MIMO: In this case, we have K=1 and  $N_k=N_r$ . The utility function becomes

$$F_{\mathsf{MIMO}}(\mathbf{Q}, \mathbf{H}(\mathbf{\Theta})) = \log_2 \det \left( \mathbf{I}_{N_{\mathsf{r}}} + \frac{1}{\sigma^2} \mathbf{H}(\mathbf{\Theta}) \mathbf{Q} \mathbf{H}^{\mathsf{H}}(\mathbf{\Theta}) \right),$$
(64)

where  $\mathbf{H}(\mathbf{\Theta}) = \mathbf{H}_{RT} + \mathbf{H}_{RI}\mathbf{\Theta}\mathbf{H}_{IT}$  with  $\mathbf{H}_{RT} \in \mathbb{C}^{N_r \times N}$  and  $\mathbf{H}_{RI} \in \mathbb{C}^{N_r \times M}$ ,  $\sigma^2$  denotes the noise power. We also replace the precoder with the transmitting covariance matrix  $\mathbf{Q} \in \mathbb{C}^{N \times N}$ , which satisfies

$$\mathbf{Q} \in \mathcal{Q} = {\mathbf{Q} \mid \mathsf{tr}(\mathbf{Q}) \le P, \mathbf{Q} \succeq \mathbf{0}_{N \times N}}.$$
 (65)

With the form of (60), the following beamforming design studies have been conducted. Focusing on reciprocal and fully-connected architectures constrained by  $\mathcal{T}_{\mathsf{group-conn}}$  (G=1)

$$\mathcal{T}_{\mathsf{group-conn}} = \{ \boldsymbol{\Theta} = \mathsf{blkdiag}(\boldsymbol{\Theta}_1, \dots, \boldsymbol{\Theta}_G) \mid \\ \boldsymbol{\Theta}_q = \boldsymbol{\Theta}_q^\mathsf{T}, \boldsymbol{\Theta}_q^\mathsf{H} \boldsymbol{\Theta}_q = \mathbf{I}_{\bar{M}}, \forall g \in \mathcal{G} \},$$
 (66)

a common strategy is to iteratively design BD-RIS and the covariance matrix [63]. Specifically, the BD-RIS design can generally follow the idea of decoupling  $\Theta$  into  $\Theta = \Psi^H \Psi$  with  $\Psi$  being unitary. For more specific LoS MIMO channels (both  $\mathbf{H}_{RI}$  and  $\mathbf{H}_{IT}$  have rank 1), the closed-form solution of  $\Theta$  can be obtained by exploiting the rank-1 property of channels  $\mathbf{H}_{RI}$  and  $\mathbf{H}_{IT}$  [64]. Focusing on non-reciprocal BD-RIS architecture constrained by the set

$$\mathcal{T}_{\mathsf{non-recip}} = \{ \mathbf{\Theta} \mid \mathbf{\Theta}^{\mathsf{H}} \mathbf{\Theta} = \mathbf{I}_M \}, \tag{67}$$

the problem has been solved by the Manifold method [54]. Matrix decomposition based solutions have also been proposed in closed form considering either near-field [65] or far-field [66] scenarios, which are proved to be globally optimal.

3) Sum-Rate Maximization for Multi-User MISO: In multi-user MISO systems, we have  $N_k = N_{s,k} = 1, \forall k \in \mathcal{K}$ . The utility function for sum-rate maximization writes as

$$F_{\mathsf{MU-MISO}}^{\mathsf{sum-rate}}(\mathbf{W}, \{\mathbf{h}_{k}(\mathbf{\Theta})\}_{\forall k})$$

$$= \sum_{k \in \mathcal{K}} \log_{2} (1 + \gamma_{k}(\mathbf{W}, \mathbf{h}_{k}(\mathbf{\Theta}))),$$

$$\gamma_{k}(\mathbf{W}, \mathbf{h}_{k}(\mathbf{\Theta})) = \frac{|\mathbf{h}_{k}(\mathbf{\Theta})\mathbf{w}_{k}|^{2}}{\sum_{i \neq k} |\mathbf{h}_{k}(\mathbf{\Theta})\mathbf{w}_{i}|^{2} + \sigma^{2}}, \forall k \in \mathcal{K},$$
(68)

where  $\mathbf{h}_k(\boldsymbol{\Theta}) = \mathbf{h}_{RT,k} + \mathbf{h}_{RI,k}\boldsymbol{\Theta}\mathbf{H}_{IT}$  with  $\mathbf{h}_{RT,k} \in \mathbb{C}^{1\times N}$  and  $\mathbf{h}_{RI,k} \in \mathbb{C}^{1\times M}$ , and  $\mathbf{W} = [\mathbf{w}_1,\ldots,\mathbf{w}_K] \in \mathbb{C}^{N\times K}$  is constrained by the set

$$\mathcal{W}_{\mathsf{MU-MISO}}^{\mathsf{sum-rate}} = \{ \mathbf{W} \mid \| \mathbf{W} \|_{\mathsf{F}}^2 \le P \}. \tag{69}$$

This is again a multi-variable optimization problem, which can be solved either by separately designing BD-RIS and transmit precoder, or by block coordinate descent (BCD) methods [67].

For BD-RIS having reciprocal architectures, the following beamforming design and performance analysis studies have been conducted. With the form of (60) and group/fully-connected architectures constrained by  $\mathcal{T}_{\text{group-conn}}$ , a two-stage BD-RIS and precoder design has been proposed in [58] with low computational complexity. Specifically, the optimization of BD-RIS matrix is based on the symmetric unitary projection as detailed in Section IV-A. Following the idea of symmetric unitary projection, a joint precoder and BD-RIS design has been further proposed in [68]. With the form of (59) and group/fully-connected architectures constrained by  $\mathcal{Y}_{\text{group-conn}}$ , a quasi-Newton based solution together with a heuristic user scheduling scheme has been proposed in [69]. With the form of (60) and multi-sector mode BD-RIS constrained by the set

$$\mathcal{T}_{\mathsf{multi-sec}} = \Big\{ \mathbf{\Theta} \mid \sum_{l \in \mathcal{L}} |\Theta_{l,1,n}|^2 = 1, \forall n = 1, \dots, \frac{M}{L} \Big\},$$
(70)

where  $\Theta_{l,1,n}$ ,  $\forall l \in \mathcal{L}$ ,  $\forall n = 1, ..., \frac{M}{L}$  are extracted from  $\Theta$  according to Example 2 of Section III-F, an iteratively closed-form solution can be obtained by deriving the Karush-Kuhn-Tucker conditions [42]. In addition, [70] has derived the closed-form expression of the achievable sum-rate aided by multi-sector BD-RIS, with a further extension to other performance metrics, such as energy efficiency, error probability, outage probability [71].

For BD-RIS having non-reciprocal architectures, the following beamforming design studies have been conducted. For BD-RIS constrained by the set  $\mathcal{T}_{\text{non-recip}}$ , [72] and [73] have proposed learning-based methods which support larger-dimensional optimizations. For BD-RIS with hybrid mode and proper non-reciprocal architectures, the constraint  $\Theta_r = \Theta_r^\mathsf{T}$  from Example 1 of Section III-F can be dropped such that  $\Theta$  is constrained by the set

$$\mathcal{T}_{\mathsf{hyb}} = \{ \boldsymbol{\Theta} \mid \boldsymbol{\Theta}_{\mathsf{r},g}^{\mathsf{H}} \boldsymbol{\Theta}_{\mathsf{r},g} + \boldsymbol{\Theta}_{\mathsf{t},g}^{\mathsf{H}} \boldsymbol{\Theta}_{\mathsf{t},g} = \mathbf{I}_{\frac{\bar{M}}{2} \times \frac{\bar{M}}{2}}, \forall g \in \mathcal{G} \},$$

where  $\Theta_{r,g}$  and  $\Theta_{t,g}$ ,  $\forall g \in \mathcal{G}$  are extracted from  $\Theta$  according to Example 1 of Section III-F. It should be noted here that the constraint of hybrid BD-RIS essentially constructs a Stiefel

Manifold [53]. Therefore, an iterative searching-based solution can be obtained by using the Manifold theory [40]. For BD-RIS with hybrid mode and dynamically connected architectures adapting to the instantaneous CSI, [47] has proposed a heuristic grouping strategy design.

4) Energy Efficiency Maximization and Power Minimization for Multi-User MISO: In multi-user MISO systems, the utility functions for energy-efficiency maximization and power minimization are respectively given by

$$\begin{split} F_{\text{MU-MISO}}^{\text{energy-effi}}(\mathbf{W}, \{\mathbf{h}_{k}(\mathbf{\Theta})\}_{\forall k}) &= \frac{F_{\text{MU-MISO}}^{\text{sum-rate}}(\mathbf{W}, \{\mathbf{h}_{k}(\mathbf{\Theta})\}_{\forall k})}{\eta \|\mathbf{W}\|_{\text{F}}^{2} + P_{\text{d}}}, \\ F_{\text{MU-MISO}}^{\text{power-min}}(\mathbf{W}, \{\mathbf{h}_{k}(\mathbf{\Theta})\}_{\forall k}) &= -\|\mathbf{W}\|_{\text{F}}^{2} - \sum_{k \in \mathcal{K}} \mathbb{I}_{\mathcal{S}_{k}}(\mathbf{W}, \mathbf{\Theta}), \end{split}$$
(73)

where  $\eta$  denotes the power amplifier efficiency,  $P_{\mathsf{d}}$  denotes the power used for device operating, and  $\mathbb{I}_{\mathcal{S}_k}(\mathbf{W}, \mathbf{\Theta})$  denotes the indicator function of set  $\mathcal{S}_k$ 

$$S_k = \{ (\mathbf{W}, \mathbf{\Theta}) \mid \gamma_k(\mathbf{W}, \mathbf{h}_k(\mathbf{\Theta})) \ge \bar{\gamma}_k \}, \forall k \in \mathcal{K}, \quad (74)$$

with  $\bar{\gamma}_k$  being the signal-to-interference-plus-noise (SINR) threshold for user k.

For BD-RIS having reciprocal architectures, the following beamforming design and performance analysis studies have been conducted. With the form of (60) and group/fullyconnected architectures constrained by  $\mathcal{T}_{group-conn}$ , [60] has proposed an iterative framework by decoupling the unitary and symmetric constraints of  $\Theta$  with a newly introduced auxiliary variable  $\Phi = \Theta$ , such that  $\Theta$  is only subject to the unitary constraint and  $\Phi$  is only subject to the symmetric constraint, or vise versa. The proposed framework is applicable to sumrate maximization, energy-efficiency maximization, and power minimization problems. With the form of (60) and STARS, which is essentially a special case of multi-sector BD-RIS constrained by  $\mathcal{T}_{\mathsf{multi-sec}}$  when L=2 and also a special case of hybrid BD-RIS constrained by  $\mathcal{T}_{\mathsf{hyb}}$  when  $\bar{M}=2$ , [74] has proposed a meta-learning approach for joint optimization of BD-RIS, resource allocation, and antenna selection. With the form of (59), [61] has recently proposed a universal framework applicable to arbitrary constraints of BD-RIS admittance matrix, the aforementioned three utility functions, and sum-rate maximization for more general multi-user MIMO scenarios. The main idea is to introduce auxiliary variables  $\mathbf{u}_k = \mathbf{h}_{RLk}\mathbf{\Theta}, \ \forall k \in \mathcal{K}, \ \text{such that the matrix inverse in (59)}$ can be eliminated by transferring it to bilinear constrains to facilitate the optimization. The applicable BD-RIS constraints include but are not limited to those for group/fully-, forest/tree-, and band/stem-connected architectures in Section III-D.

The above literature about optimization and performance analysis for BD-RIS is summarized in Table V.

### C. Channel Estimation

Channel estimation is crucial for BD-RIS-aided wireless systems since the performance benefits of BD-RIS are supported by proper optimization, beamforming design methods and performance analysis, all of which rely highly on accurate CSI. In D-RIS systems, there are generally two approaches

to acquire instantaneous CSI, namely semi-passive channel estimation where RIS is mounted with RF chains for sensing signals, and passive channel estimation where RIS does not have the ability to sense signals [16]. The semi-passive channel estimation approach results in separate base station-RIS and RIS-user channels with relatively low training overhead, both of which are independent of RIS architectures. Therefore, this approach used in D-RIS systems [75]-[77] is readily applicable to BD-RIS systems. However, the drawback of this approach is that the channel estimation performance relates tightly to the number of RF chains. Intuitively, the more the RF chains, the better the estimation performance. This indicates that a satisfactory estimation performance is achieved at the cost of significant power consumption. The passive channel estimation approach is an alternative approach which eases the requirement for RF chains [15]. Take the time-division duplex (TDD) system as an example, the passive channel estimation usually happens in uplink. Specifically, on the uplink, the user consecutively transmits pilot signals to the base station through BD-RIS and the BD-RIS keeps varying its response based on a pre-defined pattern. In this sense, it is in general not easy to obtain exactly the separate base station-RIS and RIS-user channels. Instead, the cascaded channel, which is the combination of base station-RIS and RIS-user channels, can be estimated. The passive channel estimation approach has been widely studied in D-RIS literature, starting by simple orthogonal RIS pattern design [78]-[80] with the aim to demonstrate the feasibility of this approach, followed by advanced pattern and protocol design with reduced training overhead [81]-[83]. Nevertheless, it is worth noting that the above passive channel estimation studies for D-RIS do not work for BD-RIS due to the following reasons.

- The structure of the cascaded channel is mathematically determined by the structure of BD-RIS scattering matrix
   Θ, such that D-RIS with a diagonal scattering matrix leads to a cascaded channel different from BD-RIS with beyond-diagonal scattering matrix.
- The pattern design of D-RIS is subject to constraints different from BD-RIS architectures.

These two points will be explained in more details, based on a specific least-squares estimation.

1) Least-Squares Estimation: Consider a narrowband BD-RIS-aided MISO system consisting of an N-antenna base station, an M-antenna BD-RIS working on reflecting mode, and a single-antenna user. In the uplink, denote the channels from the user to BD-RIS as  $\mathbf{h}_{IR} \in \mathbb{C}^{M \times 1}$  and from the BD-RIS to the base station as  $\mathbf{H}_{TI} \in \mathbb{C}^{N \times M}$ . We assume the direct link from the user to the base station is blocked<sup>5</sup>,  $\mathbf{h}_{TR} = \mathbf{0}_{N \times 1}$ , and focus only on the estimation of BD-RIS-aided channels. The uplink channel is thus

$$\mathbf{h}_{\mathsf{up}} = \mathbf{H}_{TI} \mathbf{\Theta} \mathbf{h}_{IR} = \underbrace{\mathbf{h}_{IR}^{\mathsf{T}} \otimes \mathbf{H}_{TI}}_{=\mathbf{H}_{\mathsf{cas}}^{\mathsf{BD}} \in \mathbb{C}^{N \times M^2}} \mathsf{vec}(\mathbf{\Theta}), \tag{75}$$

 $^5$ In the case where a direct link exists, one can first turn OFF the BD-RIS by letting  $\Theta$  be a zero matrix and estimate the direct channel using well-established methods in conventional MIMO systems, and then estimate the cascaded channel related to BD-RIS by removing the contribution of the direct channel from the received data and using the proposed pattern design.

| TABLE V                                                     |
|-------------------------------------------------------------|
| RD-RIS I ITERATURE ON OPTIMIZATION AND PERFORMANCE ANALYSIS |

| Ref.                       | Architecture <sup>†</sup>             | Mode             | Scenario           | Metric                                 | Highlights                                                                                                                    |
|----------------------------|---------------------------------------|------------------|--------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [26]<br>[55], [57]<br>[56] | Fully/Group-Connected Fully-Connected |                  | SISO               |                                        | Derive the performance upper-bound and scaling law w.r.t the number of elements  Propose closed-form global optimal solutions |
| [44]                       | Tree/Forest-Connected                 | Reflecting       |                    | Received<br>Power Max.                 | Propose a closed-form solution to achieve MISO optimum                                                                        |
| [48]                       | Dynamically Connected                 |                  | MISO,<br>SIMO      | Power Max.                             | Propose an offline grouping strategy<br>design adapting to static CSI                                                         |
| [25], [50]<br>[62]         | Non-Reciprocal                        | Multi-Sector     | SIMO               |                                        | Derive the optimal permuting strategy Use non-reciprocal architectures to support multi-sector mode                           |
| [63]                       | Fully-Connected                       |                  |                    |                                        | Jointly design BD-RIS and transmitter covariance matrix                                                                       |
| [64]                       | Fully/Group-Connected                 |                  |                    | Composite                              | Derive the closed-form solution of BD-RIS for rank-1 channels                                                                 |
| [54]<br>[65]               | Non-Reciprocal                        | Reflecting       | MIMO               | MIMO Capacity Max.                     | Propose a Manifold-based solution with fast convergence Derive nearly-optimal solution of BD-RIS for near-field channels      |
| [66]                       | -                                     |                  |                    |                                        | Derive the closed-form solution of BD-RIS<br>for far-field channels                                                           |
| [58]                       | Fully/Group-Connected                 |                  |                    |                                        | Propose a two-stage design with low complexity                                                                                |
| [68]                       | Fully-Connected                       | Reflecting       |                    | Sum-Rate                               | Propose a joint design based on unitary symmetric projection                                                                  |
| [69]                       | Fully/Group-Connected                 |                  | Multi Usar         |                                        | Propose a heuristic user scheduling scheme                                                                                    |
| [72], [73]<br>[40]<br>[47] | Non-Reciprocal                        | Hybrid           |                    | Multi-User                             | Max.                                                                                                                          |
| [42]                       |                                       |                  | MISO               |                                        | Propose an iteratively closed-form solution                                                                                   |
| [70], [71]                 | Group-Connected                       | Multi-Sector     | MISO               | Sum-Rate<br>Max., Energy<br>Effi. Max. | Derive the closed-form expression of achievable sum-rate and energy efficiency aided by multi-sector BD-RIS                   |
| [74]                       | Group-Connected                       | Hybrid<br>(STAR) |                    | Energy Effi.<br>Max.                   | Propose a meta-learning approach                                                                                              |
| [60]                       | Fully/Group-Connected                 | Reflecting       |                    | Sum-Rate<br>Max., Energy               | Propose a unified optimization framework for sum-rate maximization, energy efficiency maximization, and power minimization    |
| [45], [61]                 | Arbitrary                             |                  | Multi-User<br>MIMO | Effi. Max.,<br>Power Min.              | Propose a unified optimization framework for commonly used metrics and arbitrary architectures                                |

<sup>&</sup>lt;sup>†</sup> The architectures are all reciprocal unless otherwise stated.

where  $\mathbf{H}_{\mathsf{cas}}^{\mathsf{BD}}$  is the cascaded channel to be estimated. Note that the expression in (75) holds for  $\boldsymbol{\Theta}$  with any structures, such as being diagonal, block-diagonal, or full. Specifically for D-RIS with  $\boldsymbol{\Theta} = \mathsf{diag}(\Theta_1, \dots, \Theta_M)$ , the uplink channel can be expressed differently as

$$\mathbf{h}_{\mathsf{up}} = \mathbf{H}_{TI} \mathbf{\Theta} \mathbf{h}_{IR} = \sum_{m=1}^{M} \underbrace{[\mathbf{h}_{IR}]_m [\mathbf{H}_{TI}]_{:,m}}_{=\mathbf{h}_{\mathsf{cas}}^{\mathsf{D}}, m} \mathbf{\Theta}_m = \mathbf{H}_{\mathsf{cas}}^{\mathsf{D}} \boldsymbol{\theta},$$
(7)

where  $\boldsymbol{\theta} = [\Theta_1, \dots, \Theta_M]^\mathsf{T}$  and the cascaded channel to be estimated is given by

$$\mathbf{H}_{\mathsf{cas}}^{\mathsf{D}} = [\mathbf{h}_{\mathsf{cas}}^{\mathsf{D}}, \dots, \mathbf{h}_{\mathsf{cas}}^{\mathsf{D}}] \in \mathbb{C}^{N \times M}. \tag{77}$$

Comparing  $\mathbf{H}_{cas}^{BD}$  and  $\mathbf{H}_{cas}^{D}$ , we could observe that the two cascaded channels have different dimensions and mathematical structures, such that the passive channel estimation designed for D-RIS does not work for BD-RIS. In the following, we will elaborate more on the difference in pattern design between BD-RIS and D-RIS. To do so, we first briefly revisit the channel estimation process [84], which generally works for any BD-RIS architectures and D-RIS.

Assuming the user sends pilot symbol vector  $x_j$ ,  $|x_j| = 1$  at time slot j,  $\forall j \in \mathcal{J} = \{1, \dots, J\}$ , the signal received at the base station is

$$\mathbf{y}_{j} = \sqrt{P_{\mathrm{u}}} \mathbf{H}_{\mathrm{cas}}^{\mathrm{BD}} \mathrm{vec}(\ddot{\boldsymbol{\Theta}}_{j}) x_{j} + \mathbf{n}_{j}, \tag{78}$$

where  $P_{\mathsf{u}}$  denotes the power transmitted at the user,  $\hat{\Theta}_{j}$  denotes the BD-RIS scattering matrix at time slot j,  $\mathbf{n}_{j} \sim \mathcal{CN}(\mathbf{0}_{N\times 1}, \sigma^{2}\mathbf{I}_{N})$  denotes the noise with power  $\sigma^{2}$ . Assuming  $x_{j} = 1$ ,  $\forall j \in \mathcal{J}$  without loss of channel estimation performance, the overall received signal stacking the received signal from all times slots is

$$\mathbf{Y}_{\mathsf{all}} = \sqrt{P_{\mathsf{u}}} \mathbf{H}_{\mathsf{cas}}^{\mathsf{BD}} \mathbf{\Theta}_{\mathsf{all}}^{\mathsf{BD}} + \mathbf{N},\tag{79}$$

where we define  $\mathbf{Y}_{\mathsf{all}} = [\mathbf{y}_1, \dots, \mathbf{y}_J]$ ,  $\boldsymbol{\Theta}_{\mathsf{all}}^{\mathsf{BD}} = [\mathsf{vec}(\ddot{\boldsymbol{\Theta}}_1), \dots, \mathsf{vec}(\ddot{\boldsymbol{\Theta}}_J)]$ , and  $\mathbf{N} = [\mathbf{n}_1, \dots, \mathbf{n}_J]$ . The simplest way to estimate  $\mathbf{H}_{\mathsf{cas}}^{\mathsf{BD}}$  is the least-squares method, resulting in the estimator

$$\widehat{\mathbf{H}}_{\mathsf{cas}}^{\mathsf{BD}} = \sqrt{P_{\mathsf{u}}^{-1}} \mathbf{Y}_{\mathsf{all}} (\mathbf{\Theta}_{\mathsf{all}}^{\mathsf{BD}})^{\mathsf{H}} (\mathbf{\Theta}_{\mathsf{all}}^{\mathsf{BD}} (\mathbf{\Theta}_{\mathsf{all}}^{\mathsf{BD}})^{\mathsf{H}})^{-1}, \tag{80}$$

with  $J \geq M^2$  to guarantee the successful estimation. This leads to the mean square error (MSE) as  $\operatorname{err}_{\widehat{\mathbf{H}}_{\operatorname{cas}}^{\operatorname{BD}}} = \mathbb{E}\{\|\mathbf{H}_{\operatorname{cas}}^{\operatorname{BD}} - \widehat{\mathbf{H}}_{\operatorname{cas}}^{\operatorname{BD}}\|_{\operatorname{F}}^2\} = \frac{N\sigma^2}{P_{\mathrm{u}}}\operatorname{tr}((\mathbf{\Theta}_{\operatorname{all}}^{\operatorname{BD}}(\mathbf{\Theta}_{\operatorname{all}}^{\operatorname{BD}})^{\operatorname{H}})^{-1}),$  which indicates that the channel estimation performance depends purely on the design of  $\mathbf{\Theta}_{\operatorname{all}}^{\operatorname{BD}}$ . We assume the BD-RIS has a non-reciprocal architecture, where the scattering matrices  $\ddot{\mathbf{\Theta}}_j, \ \forall j \in \mathcal{J}$  are constrained by  $\mathcal{T}_{\operatorname{non-recip}}$  in (67), for the ease of illustration

TABLE VI BD-RIS LITERATURE ON CHANNEL ESTIMATION

| Ref.‡      | Estimate Type | Overhead†               | Highlights                                                                                    |
|------------|---------------|-------------------------|-----------------------------------------------------------------------------------------------|
| [84], [85] |               | $M^2$                   | The first least-squares estimation scheme based on a closed-form BD-RIS pattern               |
| [86], [87] | Cascaded      | 2M                      | A two-phase estimation scheme by exploring the cascaded channel characteristics               |
| [88]       | Cascaucu      | 3M                      | A three-stage estimation scheme by exploring the property of non-diagonal scattering matrices |
| [89]       |               | $M^2$                   | A decoupled estimation method based on Khatri-Rao Factorization                               |
| [90], [91] | Separate      | Much smaller than $M^2$ | A decoupled estimation method based on Tucker decomposition and alternating least squares     |
| [92]       | Separate      | 1                       | A semi-blind estimation method that avoids the pilot-assisted training stage                  |

<sup>&</sup>lt;sup>†</sup> The overhead is calculated for a MISO system, which will scale with the number of users and/or antennas for more complex multi-user MIMO systems. <sup>‡</sup> [84]–[87], [89]–[92] focus on non-reciprocal BD-RIS constrained by  $\mathcal{T}_{non-recip}$  and [88] focuses on non-reciprocal BD-RIS constrained by  $\mathcal{T}_{non-diag}$ .

and comparison. This motivates the following problem

$$\begin{split} & \underset{\boldsymbol{\Theta}_{\text{all}}^{\text{BD}}}{\min} \ \operatorname{tr}((\boldsymbol{\Theta}_{\text{all}}^{\text{BD}}(\boldsymbol{\Theta}_{\text{all}}^{\text{BD}})^{\text{H}})^{-1}) \\ & \text{s.t.} \ \boldsymbol{\Theta}_{\text{all}}^{\text{BD}} = [\operatorname{vec}(\ddot{\boldsymbol{\Theta}}_{1}), \dots, \operatorname{vec}(\ddot{\boldsymbol{\Theta}}_{J})], \\ & \ddot{\boldsymbol{\Theta}}_{j}^{\text{H}} \ddot{\boldsymbol{\Theta}}_{j} = \mathbf{I}_{M}, \forall j \in \mathcal{J}, \\ & \operatorname{rank}(\boldsymbol{\Theta}_{\text{all}}^{\text{BD}}) = M^{2}, \end{split} \tag{81}$$

where the training overhead is minimized as  $J_{\text{LS}}^{\text{BD}} = M^2$  without introducing estimation ambiguities. Similarly, for the case of D-RIS, we define the RIS pattern  $\Theta_{\text{all}}^{\text{D}} = [\theta_1, \dots, \theta_J] \in \mathbb{C}^{M \times J}$ , where  $\theta_j = [\ddot{\Theta}_{j,1}, \dots, \ddot{\Theta}_{j,M}]^{\text{T}}$  collects the diagonal entries in  $\ddot{\Theta}_j = \text{diag}(\ddot{\Theta}_{j,1}, \dots, \ddot{\Theta}_{j,M})$  of D-RIS at time slot j, with  $|\ddot{\Theta}_{j,m}| = 1$ ,  $\forall j \in \mathcal{J}$  when the RIS is lossless. To minimize the channel estimation error, we have

$$\begin{split} & \underset{\boldsymbol{\Theta}_{\text{all}}^{\text{D}}}{\min} \ \operatorname{tr}((\boldsymbol{\Theta}_{\text{all}}^{\text{D}}(\boldsymbol{\Theta}_{\text{all}}^{\text{D}})^{\text{H}})^{-1}) \\ & \text{s.t.} \ \boldsymbol{\Theta}_{\text{all}}^{\text{D}} = [\boldsymbol{\theta}_{1}, \dots, \boldsymbol{\theta}_{J}], \\ & |\ddot{\boldsymbol{\Theta}}_{j,m}| = 1, \forall j \in \mathcal{J}, \forall m \in \mathcal{M}, \\ & \operatorname{rank}(\boldsymbol{\Theta}_{\text{all}}^{\text{D}}) = M, \end{split} \tag{82}$$

where the training overhead is minimized as  $J_{LS}^{\rm D} = M$  here for the same reason as in problem (81). Problems (81) and (82) clearly show the difference between BD-RIS and D-RIS in pattern design. Specifically, for (82), one can directly use orthogonal matrices, such as the discrete Fourier matrix or the Hadamard matrix, to construct  $\Theta_{\rm all}^{\rm D}$  [15]. However, the solutions for (82) are not feasible for (81) due to the unique constraints of BD-RIS.

2) Related Works and Discussions: To perfectly capture the constraints of BD-RIS architectures and facilitate the least-squares estimation, [84] has proposed a global optimal closed-form solution to (81), followed by a further extension to BD-RIS with hybrid/multi-sector modes in more general multi-user MIMO systems [85]. Based on the proposed pattern design, [84], [85] for the first time provide a comprehensive study for BD-RIS-aided systems from channel estimation to beamforming design and data transmission. However, the drawbacks of the method in [84], [85] are 1) the high training overhead, e.g.,  $J_{\rm LS}^{\rm BD} = M^2$  for a non-reciprocal BD-RIS constrained by  $\mathcal{T}_{\rm non-recip}$ , 2) the limited performance without exploring the structural characteristics of the cascaded channel, and 3) the channel estimation error for non-reciprocal BD-RIS that theoretically scales with the group size  $\bar{M}$  [85]:

$$err^{BD} = \frac{\sigma^2}{P_{\rm u}} N\bar{M},\tag{83}$$

which indicates that the estimation error increases with the circuit complexity of BD-RIS (i.e., a larger M leads to higher estimation error). To further reduce the channel estimation error, tensor decomposition has been applied in [89] based on the designed pattern in [84], which leads to the possibility of separate estimation of base station-RIS and RIS-user channels. Beyond that, two tensor decomposition based algorithms have been proposed in [90] with a milder requirement of the training overhead and enhanced estimation performance. [91] again explores the tensor decomposition for BD-RISaided channel estimation, which further facilitates the channel prediction with channel aging. [92] proposes a semi-blind channel and symbol estimation method that avoids the pilotassisted estimation by exploring also the tensor decomposition for BD-RIS-aided channels. In addition, [86] has focused on the protocol design for a single-user MISO system and proposed a novel two-phase estimation scheme, where the cascaded channel related to the first element of BD-RIS is estimated, followed by fast estimation of the other channel coefficients. The two-phase estimation scheme explores the dependence between entries of the cascaded channel  $\mathbf{H}_{cas}^{\mathsf{BD}}$ and thus helps to significantly reduce the training overhead from  $J_{\rm LS}^{\rm BD}=M^2$  to  $J_{\rm 2-phase}^{\rm BD}=2M$ . This channel estimation scheme has been further extended to more general multi-user MIMO systems, with the training overhead in the same order as in D-RIS-aided system [87]. Besides, [88] has proposed a three-stage protocol for a non-reciprocal BD-RIS aided MISO system where the BD-RIS is characterized by a non-diagonal scattering matrix constrained by  $\mathcal{T}_{non-diag}$  in (63). Using the special signal flowing property in the non-diagonal scattering matrix, i.e., the signal impinging on one element is purely reflected by another one, the training overhead can be as low as  $J_{3-\text{stage}}^{\text{ND}} = 3M$ . For clarity, the aforementioned works have been summarized in Table VI.

The channel estimation study for BD-RIS-aided wireless systems is still at the very early stage. It is worth noting that, the passive channel estimation approach relies on the BD-RIS pattern design and results in a cascaded channel (or separate channels based on tensor decomposition whose process relies on BD-RIS constraints), both of which are related to BD-RIS architectures. In this sense, the existing literature [84]–[91] based on non-reciprocal architectures cannot be readily extended to other BD-RIS architectures. Moreover, in practice, BD-RIS inevitably has hardware impairments that will induce new mathematical constraints and communications models, as will be detailed in Section VI. Therefore, those works based

![](_page_21_Figure_1.jpeg)

Fig. 16. Sum-rate of a 4-user system with the aid of a 32-element BD-RIS versus transmit power for different BD-RIS architectures. Channels through BD-RIS follow Rician fading with a Rician factor 2 dB. The direct transmitter-user links are assumed to be blocked. The transmitter-RIS distance is set as 50 m and the RIS-user distance is set as 2.5 m [61].

on BD-RIS with perfect hardware may not be applicable to BD-RIS with practical hardware impairments. Another critical issue for passive channel estimation is the training overhead that grows with the number of elements and the circuit complexity. Therefore, it remains unexplored, but it is important to develop BD-RIS pattern designs automatically adapting to architectures and hardware impairments, and to study better channel estimation schemes with affordable training overhead.

### V. BENEFITS OF BD-RIS

Thanks to the flexible interconnections between elements to support various architectures and modes, BD-RIS has multiple benefits, such as enhancing channel gain, increasing transmission quality, enlarging coverage, etc. In this section, we summarize the key benefits of BD-RIS, each of which is supported by numerical results.

### A. Boosting Received Power and Rates

Compared to (lossless) D-RIS which can only manipulate the phase shift of the diagonal entries in the scattering matrix, BD-RIS has higher flexibility in manipulating both amplitude and phase shift of diagonal and off-diagonal entries in its scattering matrix. This flexibility boosts the performance of various systems, such as increasing the received power by up to 62% for SISO as shown in Fig. 4 and increasing the sumrate for MU-MISO by up to 43% as shown in Fig. 16.

## B. Enabling Low-Complexity Architectures with High Performance

The flexibility provided by the interconnections between BD-RIS elements enables various circuit topology designs to support different architectures as illustrated in Sections III-D and III-E. More importantly, this flexibility enables architectures with least hardware complexity (i.e., number of tunable components) to achieve optimal performance in various systems.

![](_page_21_Figure_10.jpeg)

Fig. 17. Pareto frontier between performance and circuit complexity including single-, group-, fully-, forest-, and tree-connected BD-RIS, with different group sizes  $\bar{M}$  labeled on two sides of the curve [93]. The direct transmitter-receiver channel is assumed to be blocked and channels through BD-RIS follow i.i.d. Rayleigh fading.

![](_page_21_Figure_12.jpeg)

Fig. 18. Pareto frontier between performance and circuit complexity including single-, group-, fully-, stem-, and band-connected BD-RIS, with different group sizes  $\bar{M}$  and stem/band width q labeled on two sides of the curves. The direct transmitter-user channels are assumed to be blocked and channels through BD-RIS follow Rician fading with a Rician factor 2 dB. The transmitter-RIS distance is set as 50 m and the RIS-user distance is set as 2.5 m. (N=K=4, M=64, P=10 dBm) [45].

For the MISO system, [44] has theoretically proven that the least circuit complexity for MISO optimal BD-RIS is

$$C_{\text{MISO}}^{\text{opt}} = 2M - 1.$$
 (84)

This condition essentially forms a tree-connected architecture, and two representative examples are arrowhead BD-RIS and tridiagonal BD-RIS. Based on this conclusion, [93] has analyzed the Pareto frontier between performance and circuit complexity for a SISO system. Fig. 17 shows that tree-connected architecture can reach the performance achieved by fully-connected BD-RIS with the lowest possible complexity, thus achieving the best performance-complexity trade-off.

For more general multi-user MIMO systems, [45] has theoretically proved that the least circuit complexity for multi-

![](_page_22_Figure_1.jpeg)

Fig. 19. Sum-rate for a BD-RIS-aided multi-user MISO system versus the number of elements M. "CW-FC", "CW-GC", and "CW-SC", respectively, refer to cell-wise fully-, group-, and single-connected. Channels through BD-RIS follow Rician fading with a Rician factor 0 dB. The transmitter-user channels are fully blocked. The transmitter-RIS distance is set as 100 m and the RIS-user distance is set as 10 m. The group size for hybrid and multisector modes with CW-GC architectures are respectively set as 4 and 8. The number of sectors for the multi-sector mode is set as 4. N=K=4 with four users distributed evenly across the sectors covered by BD-RIS, that is, all users on the same side for reflecting mode, every two users on one side for hybrid mode, and one user within each sector for multi-sector mode.

### user MIMO optimal BD-RIS is

$$C_{\mathsf{MU-MIMO}}^{\mathsf{opt}} = \min\left\{D, \frac{M}{2}\right\} \left(2M - 2\min\left\{D, \frac{M}{2}\right\} + 1\right),$$
(85)

where  $D = \min\{\sum_{k \in \mathcal{K}} N_k, N\}$  is the DoF of the multiuser MIMO channel. Two representative examples which can reach such condition are band- and stem-connected BD-RIS with band and stem width  $q = 2\min\{D, \frac{M}{2}\} - 1$ . Fig. 18 reports the Pareto frontier between performance and circuit complexity achieved by BD-RIS-aided multi-user MISO systems, indicating that band/stem-connected BD-RIS with proper band/stem width q can reach the performance achieved by fully-connected BD-RIS, with much less circuit complexity.

## C. Enabling Flexible Modes with Highly-Directional Wireless Coverage

The inter-element connections in BD-RIS not only boost the channel strength and system performance, but also provide possibility to flexibly arrange the locations and orientations of elements. This leads to different modes with enlarged wireless coverage, such as hybrid mode proposed in [40] and multisector modes proposed in [42]. Results in Fig. 19 demonstrate that a reflecting BD-RIS can achieve up to 75% of sumrate improvement over D-RIS (single-conn.) when M = 128. More importantly, a 4-sector BD-RIS with cell-wise fullyconnected architecture can increase the sum-rate by 150% over STAR-RIS with M = 128, thanks to the higher antenna gains provided by more directional antennas.

![](_page_22_Picture_8.jpeg)

Fig. 20. Illustration of (a) localized and (b) distributed RIS-aided wireless communication systems.

## D. Providing Orders of Magnitude Gains in Distributed De-

In most existing literature, an RIS has been regarded as an antenna array whose inter-element spacing is comparable with (typically smaller than) the wavelength. This setting results in a localized RIS whose elements are localized in a specific site. The localized RIS has been widely studied in far-field scenarios, where the wireless channels related to each RIS element share approximately the same large-scale fading, as shown in Fig. 20(a). In this sense, the gain of BD-RIS over D-RIS mainly comes from the better exploration of small-scale fading effects. To understand if the joint effects of small- and large-scale fading in wireless channels can provide additional flexibility to be captured by BD-RIS architectures, [94] has proposed the concept of distributed RIS. In the distributed RIS, elements are distributed over a wide region with interelement spacing much larger than the wavelength, such that the large-scale fading between transmitter/receiver and each RIS element can be quite different, as shown in Fig. 20(b).

To quantify the benefit of distributed RIS, [94] has derived the gain of distributed over localized fully-connected BD-RIS in SISO systems under Rayleigh fading channels, which is bounded by

$$G^{\text{dis}} > \left(\frac{d_R d_T}{\sqrt[a]{M^2} \min\{\mathbf{d}_R\} \min\{\mathbf{d}_T\}}\right)^a, \qquad (86a)$$

$$G^{\text{dis}} < \left(\frac{d_R d_T}{\min\{\mathbf{d}_R\} \min\{\mathbf{d}_T\}}\right)^a, \qquad (86b)$$

$$G^{\mathsf{dis}} < \left(\frac{d_R d_T}{\min\{\mathbf{d}_R\}\min\{\mathbf{d}_T\}}\right)^a,\tag{86b}$$

where  $d_R$  and  $d_T$ , respectively, denote the distance between the localized RIS and the receiver/transmitter;  $\mathbf{d}_R \in \mathbb{R}^{M \times 1}$ and  $\mathbf{d}_T \in \mathbb{R}^{M \times 1}$ , respectively, denote the distance between all M elements of the distributed RIS and the receiver/transmitter; a denotes the path-loss exponent. The bounds in (86) indicate that to guarantee  $G^{\text{dis}} > 1$ , a sufficient condition is to have  $d_R d_T > \sqrt[a]{M^2} \min\{\mathbf{d}_R\} \min\{\mathbf{d}_T\}$  and a necessary condition is to have  $d_R d_T > \min\{\mathbf{d}_R\} \min\{\mathbf{d}_T\}$ , both of which are mild and can be easily achieved. This is also numerically evaluated in Fig. 21(a), showing that  $G^{\text{dis}}$  grows exponentially with a and reaches as high as several orders of magnitude.

![](_page_23_Figure_1.jpeg)

(a) Gain of distributed over localized BD-RIS  $G^{\mathsf{dis}}$ 

![](_page_23_Figure_3.jpeg)

(b) Gain of distributed over localized BB-Ris G

Fig. 21.  $G^{\rm dis}$  (in dB) for different values of path-loss exponent, number of RIS elements, and locations of receiver [94].

The impact of locations of the receiver is reported in Fig. 21(b), showing that the distributed arrangement has the most significant performance benefit when the receiver is far from localized BD-RIS while being close to distributed BD-RIS.

## E. Enabling Simultaneously Optimal Transmissions for Uplink and Downlink with Non-Reciprocal Architectures

One key property of non-reciprocal BD-RIS is that its admittance/impedance/scattering matrices are asymmetric, which naturally break the uplink-downlink reciprocity of the wireless channels. For example, given an uplink BD-RIS-aided MISO channel  $\mathbf{h}_{\text{up}} = \mathbf{H}_{TI} \mathbf{\Theta} \mathbf{h}_{IR}$  as shown in (75), the downlink channel  $\mathbf{h}_{\text{down}} = \mathbf{h}_{RI} \mathbf{\Theta} \mathbf{H}_{IT} = \mathbf{h}_{IR}^{\mathsf{T}} \mathbf{\Theta} \mathbf{H}_{TI}^{\mathsf{T}}$  is not equal to the transpose of the uplink channel, i.e.,  $\mathbf{h}_{\text{down}} \neq \mathbf{h}_{\text{up}}^{\mathsf{T}}$  since  $\mathbf{\Theta} \neq \mathbf{\Theta}^{\mathsf{T}}$ . This property provides unique benefits to scenarios where uplink and downlink transmissions behave differently, such as full-duplex systems [95].

To visualize the benefit of applying non-reciprocal BD-RIS in full-duplex systems, [96] has derived the general RIS-aided full-duplex system model, and the theoretical conditions for non-reciprocal BD-RIS to simultaneously maximize the received powers of the signal of interest in the uplink and downlink. Results in the top two figures of Fig. 22 show that, when the uplink and downlink users are not aligned, both the

![](_page_23_Figure_10.jpeg)

Fig. 22. The impinging and reflected beam patterns of reciprocal and non-reciprocal BD-RISs. The channels between devices are assumed to be pure LoS. The base station (marked as "BS") is located at  $\frac{\pi}{6}$ ; the downlink user is located at  $\frac{\pi}{2}$ ; and the uplink user is located at  $\frac{2\pi}{3}$  in the top figures and at  $\frac{\pi}{2}$  in the bottom figures [96].

impinging and reflected beams of non-reciprocal BD-RIS can exactly point to the directions of the signal of interest with the maximum power, while those of reciprocal BD-RIS fail to point to the downlink user. Meanwhile, the bottom two figures in Fig. 22 show that, only when the uplink and downlink users are aligned, both the impinging and reflected beams of reciprocal and non-reciprocal BD-RIS can exactly point to the directions of signal of interest. Due to the unique property of non-reciprocal BD-RIS, if a wave hits the non-reciprocal BD-RIS from one direction, the surface behaves differently than if it hits from the opposite direction. This finally enables an uplink user and a downlink user at different locations to optimally communicate with the same full-duplex base station. While [96] primarily focuses on a single-antenna scenario, the benefit of non-reciprocal BD-RIS in full-duplex systems has been recently shown in more general multi-user multi-antenna scenarios [97].

## F. Providing Enhanced Gains in Dual-Polarized Systems

Existing BD-RIS literature has focused on uni-polarized systems for the ease of analysis. However, modern MIMO systems use dual-polarized antenna arrays to have more antennas within limited space to provide more beamforming gains [98]. Dual-polarized D-RIS-aided systems have been studied in [99], [100], while it remains unknown if BD-RIS still has performance gains over D-RIS in dual-polarized systems. Taking into account this practical consideration, [101] has modeled and analyzed a dual-polorized BD-RIS-aided SISO system, where the BD-RIS has half vertically polarized elements and half horizontally polarized elements, and the receiving and transmitting antennas can have the same or opposite polarizations, as illustrated in Fig. 23.

When the transmitter and receiver have the same polarizations, as illustrated in Fig. 23(a), the limit of the power gain of dual-polarized fully-connected BD-RIS over D-RIS remains

![](_page_24_Figure_1.jpeg)

Fig. 23. Dual-polarized BD-RIS-aided system where transmitter and receiver (a) have the same polarization and (b) have the opposite polarization.

![](_page_24_Figure_3.jpeg)

Fig. 24. Gain of BD-RIS over D-RIS  $\lim_{M \to \infty} G^{\text{dual-polarized}}$  as a function of  $\chi$  when the transmitter and receiver have the same/opposite polarization and with Rayleigh/LoS channels [101].

the same as the uni-polarized case [26]. That is, dual-polarized BD-RIS can increase the received power in SISO by up to 62% compared to dual-polarized D-RIS. When the transmitter and receiver have opposite polarizations, the limit of the power gain of dual-polarized fully-connected BD-RIS over D-RIS varies with channel fadings, and is expressed as [101]

$$\lim_{M \to \infty} G^{\mathsf{dual-polarized}} = \begin{cases} \frac{4(1+\chi)^2}{\pi^2 \chi}, & \mathsf{Rayleigh}, \\ \frac{(1+\chi)^2}{4\chi}, & \mathsf{LoS}, \end{cases} \tag{87}$$

where  $0<\chi<1$  denotes the inverse of the cross-polar discrimination. This analytical result indicates that BD-RIS can offer a gain  $G^{\text{dual-polarized}}>1$  for both Rayleigh fading and LoS channels. To visualize the impact of  $\chi$  on performance gain, Fig. 24 illustrates the gain of BD-RIS over D-RIS as a function of  $\chi$ . These analytical results show that BD-RIS has more significant benefits over D-RIS with a smaller  $\chi$ , as small values of  $\chi$  increase disparity between the channel entries.

### VI. BD-RIS WITH HARDWARE IMPAIRMENTS

The discussions on BD-RIS so far have mainly focused on idealized and simplified hardware, such as lossless reconfigurable impedance networks with continuously tunable admittance components, with no frequency dependence, and with no mutual coupling between elements. These idealized assumptions help to understand the fundamentals and study the performance limit of BD-RIS. However, they cannot be perfectly achieved in real-world implementations. In this section, we thus briefly revisit some important hardware impairments of BD-RIS and their impacts on system performance. Similar to Section IV-C where we discussed channel estimation errors alone assuming perfect hardware at BD-RIS, below we will also show the impact of each hardware impairment assuming perfect other factors to guide readers from scratch. Analyzing real-world BD-RIS-aided scenarios by jointly considering multiple practical factors can be a meaningful future direction.

### A. Discrete-Value Impedance and Admittance

In Sections III and IV, the reconfigurable impedance network of BD-RIS is assumed to have continuous-value admittance and scattering matrices for the ease of modeling, optimization and performance analysis, as well as channel estimation. Nevertheless, admittance components tunable with finer resolution require a much more complex circuit design, especially for BD-RIS architectures with sophisticated interconnections. In D-RIS, the modeling of discrete-value scattering matrices can be very simple by uniformly quantifying the phase of each reflection coefficient. Specifically, for D-RIS with a diagonal scattering matrix  $\Theta = \text{diag}(\Theta_1, \ldots, \Theta_M)$ ,  $|\Theta_m| = 1$ , its discrete-value set is expressed as a codebook

$$\Theta_m \in \left\{ e^{j\frac{2\pi}{2B}b} \mid b \in \mathcal{B} = \{0, 1, 2^B - 1\} \right\}, \forall m \in \mathcal{M}, \quad (88)$$

where B denotes the number of resolution bits. In D-RIS literature, typical beamforming and channel estimation solutions are to quantize continuous-value results to (88), or to directly design each scattering coefficient by selecting from (88). This, however, does not work for BD-RIS with scattering matrices whose entries are dependent on each other. To model the discrete-value BD-RIS, [102] has focused on the lossless fully/group-connected architectures, and, for the first time, proposed to model the discrete-value reactance matrix  $\mathbf{X}_I = \Im\{\mathbf{Z}_I\} = \text{blkdiag}(\mathbf{X}_{I,1},\ldots,\mathbf{X}_{I,g})$ , where  $\mathbf{X}_{I,g} \in \mathbb{R}^{\tilde{M} \times \tilde{M}}$ ,  $\mathbf{X}_{I,g} = \mathbf{X}_{I,g}^{\mathsf{T}}$  denotes the reactance matrix for group g of the group-connected architecture. Then, each entry of  $\mathbf{X}_{I,g}$  is constrained by<sup>6</sup>

$$[\mathbf{X}_{I,g}]_{m,m'} \in \{\pm X_{I,b} \mid b \in \mathcal{B}\}, \forall g \in \mathcal{G}, \forall m, m' \in \bar{\mathcal{M}}, (89)$$

where  $X_{I,b} > 0$ ,  $\forall b \in \mathcal{B}$ . Comparing (88) and (89), we observe that the codebook for D-RIS is known based on a finite interval, while that for BD-RIS contains unknown candidates  $\pm X_{I,b}$ . Therefore, the design of discrete-value BD-RIS

 $^6$ In D-RIS, the reactance matrix  $\mathbf{X}_I$  boils down to a diagonal matrix and each diagonal entry  $[\mathbf{X}_I]_{m,m}$  is linked to  $\Theta_m$  in  $\mathbf{\Theta}$  as  $\Theta_m = \frac{\jmath[\mathbf{X}_I]_{m,m}+\mathcal{Z}_0}{\jmath[\mathbf{X}_I]_{m,m}-\mathcal{Z}_0}$ , such that one can directly obtain the discrete-value phase shift  $\angle\Theta_m$  with a discrete-value reactance  $[\mathbf{X}_I]_{m,m}$ .

![](_page_25_Figure_1.jpeg)

Fig. 25. Average received signal power versus the group size. The transmitter, RIS, and receiver are located at a 3D coordinate system with respectively (5,-250,25), (0,0,5), and (5,5,1.5) in meters (m). The channels from the transmitter to receiver and through RIS have i.i.d. Rayleigh fading.  $(N=4, N_r=2, M=64)$  [102].

includes an additional step, that is to determine the codebook first. To effectively solve this problem, [102] has proposed an offline learning method to obtain the codebook, which relies on a training set including sufficient channel realizations. With the determined codebook, the online deployment based on instantaneous CSI is conducted by iteratively designing individual reactance  $[\mathbf{X}_{I,g}]_{m,m'}$  through a one-dimensional search. Based on the above design, results in Fig. 25 show that one resolution bit is sufficient in fully-connected BD-RIS to achieve satisfactory performance close to the continuous-value case. Such a mild requirement of the resolution bits is beneficial for the practical implementation of BD-RIS.

The design in [102] is also applicable to other reciprocal architectures. To have a unified framework of the discrete-value BD-RIS design, it is suggested to discretize the nonzero entries of admittance matrices as explained in Remarks 4 and 5. That is, given a lossless and reciprocal reconfigurable impedance network with admittance matrix  $\mathbf{Y}_I$ , each nonzero entry of the corresponding susceptance matrix  $\mathbf{B}_I = \Im\{\mathbf{Y}_I\} \in \mathbb{R}^{M \times M}$  is constrained by

$$[\mathbf{B}_I]_{m,m'} \in \mathcal{C} = \{ \pm B_{I,b} \mid b \in \mathcal{B} \},\tag{90}$$

for  $[\mathbf{B}_I]_{m,m'} \neq 0, m, m' \in \mathcal{M}$ , where  $B_{I,b} > 0, \forall b \in \mathcal{B}$ . The offline codebook design problem aiming at maximizing the average strength of a MIMO channel is formulated as

$$\max_{C} \mathbb{E}\{\|\mathbf{H}(\mathbf{\Theta})\|_{\mathsf{F}}^{2}\}$$
s.t. 
$$\mathbf{\Theta} = (Y_{0}\mathbf{I}_{M} + \mathbf{Y}_{I})^{-1}(Y_{0}\mathbf{I}_{M} - \mathbf{Y}_{I}),$$

$$\mathbf{Y}_{I} \in \mathcal{Y}, \mathbf{B}_{I} = \Im\{\mathbf{Y}_{I}\},$$

$$[\mathbf{B}_{I}]_{m,m'} \in \mathcal{C}, \ \forall \ [\mathbf{B}_{I}]_{m,m'} \neq 0, m, m' \in \mathcal{M},$$

$$B_{I,b} > 0, \forall b \in \mathcal{B},$$
(91)

where  $\mathbf{H}(\boldsymbol{\Theta}) = \mathbf{H}_{RT} + \mathbf{H}_{RI}\boldsymbol{\Theta}\mathbf{H}_{IT}$  according to Section IV-B. The proposed offline learning method in [102] is readily adapted to BD-RIS architectures with different constraints  $\mathcal{Y}$  as illustrated in Section III-D. Once the codebook design is

![](_page_25_Picture_9.jpeg)

Fig. 26. Illustration of lossy interconnections. (a) Port m connected to ground through  $Y_m$  and (b) port m connected to port m' through  $Y_{m,m'}$  and a transmission line of length  $\ell_{m,m'}$ .

obtained, the discrete-value BD-RIS can be designed based on iteratively exhaustive search as in [102], or by directly quantizing the continuous-value solutions from Section IV-B.

The discrete-value expression and design for non-reciprocal BD-RIS still remain unexplored. For non-reciprocal architectures, at the current stage there is no clear mapping between the circuit topology and its admittance/impedance matrices. Alternatively, it is possible to directly discretize its scattering matrix  $\Theta$ . Specifically, given a non-reciprocal BD-RIS architecture constrained by  $\mathcal{T}_{non-recip}$ , the discrete-value expression could be

$$\Theta \in \mathcal{C}_{\mathsf{non-recip}} = \{ \Phi_b \mid \forall b \in \mathcal{B} \}, \tag{92}$$

where  $\Phi_b^H \Phi_b = \mathbf{I}_M$ ,  $\forall b \in \mathcal{B}$ . The simplest way is to randomly generate unitary matrices to construct  $\mathcal{C}_{\mathsf{non-recip}}$ , which may suffer significant performance loss. Alternatively, we can follow the idea for reciprocal architectures, and formulate the following offline codebook design problem

$$\max_{\mathcal{C}_{\mathsf{non-recip}}} \mathbb{E}\{\|\mathbf{H}(\mathbf{\Theta})\|_{\mathsf{F}}^{2}\}$$
s.t.  $\mathbf{\Theta} \in \mathcal{C}_{\mathsf{non-recip}},$ 

$$\mathbf{\Phi}_{b}^{\mathsf{H}} \mathbf{\Phi}_{b} = \mathbf{I}_{M}, \forall b \in \mathcal{B}.$$

$$(93)$$

There has not been existing literature solving exactly the problem (93), while it can be viewed as a vector quantization problem and potentially solved by the Lloyd algorithm [103]. The detailed design will be left as an interesting future work.

### B. Lossy Interconnections and Admittance Components

Power loss is a very important factor in hardware devices. Modeling the hardware without capturing accurately the loss could cause non-negligible performance degradation. In D-RIS, the power loss comes from the circuit of each reconfigurable component [17]. However, in BD-RIS architectures, the power loss comes from two aspects: 1) the interconnection loss between ports of the reconfigurable impedance network and 2) the loss from the circuit of reconfigurable admittance components. These two kinds of losses have been recently modeled and analyzed, respectively in [94] and [104], both focusing on reciprocal BD-RIS architectures. Below we will briefly revisit how to capture these two kinds of losses in BD-RIS architectures.

1) Lossy Interconnections: The reciprocal BD-RIS with lossy interconnections is modeled as an M-port reconfigurable impedance network, characterized by its admittance matrix  $\mathbf{Y}_I \in \mathbb{C}^{M \times M}$ . Similar to the model in Section III-B, each port

m is connected to a reconfigurable admittance component  $Y_m$ to ground, as illustrated in Fig. 26(a). The main difference is port m and port m',  $m' \neq m$ , if interconnected, are interconnected via a reconfigurable admittance component  $Y_{m,m'}$  in series with a transmission line with length  $\ell_{m,m'}$ ,  $\forall m, m' \in \mathcal{M}$ , as illustrated in Fig. 26(b). According to the derivation in [94], the entries in  $\mathbf{Y}_I$  have expressions

$$[\mathbf{Y}_{I}]_{m,m'} = \begin{cases} \frac{-2}{Y_{m,m'}^{-1} \zeta_{m,m'}^{+} + Z_{0} \zeta_{m,m'}^{-}}, & m \neq m', \\ Y_{m} - \sum_{n \neq m} \frac{\zeta_{m,m'}^{+}}{2} [\mathbf{Y}_{I}]_{m,n}, & m = m', \end{cases}$$

$$(94)$$

where  $\zeta_{m,m'}^+=e^{\zeta\ell_{m,m'}}+e^{-\zeta\ell_{m,m'}}$  and  $\beta_{m,m'}^-=e^{\zeta\ell_{m,m'}}$  $e^{-\zeta \ell_{m,m'}}$  with  $\zeta \in \mathbb{C}$  being the propagation constant of the transmission line. Specifically, in  $\zeta = \alpha + j\beta$ , the real part  $\alpha$  denotes the attenuation constant<sup>7</sup> and the imaginary part  $\beta$ denotes the phase constant. It is difficult to gain insights from (94) given its complex expressions. To understand how the lossy interconnections in BD-RIS impact the feasible range of entries in  $Y_I$ , [94] has simplified (94) by assuming a special case where  $\ell_{m,m'}$  is a multiple of half of wavelength  $\lambda$ ,  $\lambda = \frac{2\pi}{\beta}$ . That is,  $\ell_{m,m'} = \frac{\pi}{\beta} A_{m,m'}$ , where  $A_{m,m'} \in \mathbb{Z}$ . In addition, to focus purely on the impact of lossy interconnections, each reconfigurable admittance component is assumed to be lossless, i.e.,  $\Re\{Y_m\}=0$ ,  $\Re\{Y_{m,m'}\}=0$ ,  $\forall m,m'\in\mathcal{M}$ . Then, the constraint of  $[\mathbf{Y}_I]_{m,m'}$  with  $m \neq m'$  can be simplified to

$$[\mathbf{Y}_I]_{m,m'} = \underbrace{\frac{-(-1)^{A_{m,m'}}}{Y_{m,m'}^{-1}\cosh(\alpha\ell_{m,m'})} + \underbrace{Z_0 \sinh(\alpha\ell_{m,m'})}_{\text{purely imaginary}}}_{\text{purely real}}, \quad (95)$$

indicating that  $[\mathbf{Y}_I]_{m,m'}$ , if is not zero, must have a nonzero real part resulting in power loss. More interestingly, the existence of lossy interconnections makes the value of  $[Y_I]_{m,m'}$  being constrained on a circle in the complex plane. An extreme case ( $\alpha = 0$ ) that the real parts of  $[\mathbf{Y}_I]_{m,m'}$ are zeros corresponds to BD-RIS with lossless interconnections. The constraint (95) referring to BD-RIS with lossy interconnections and lossless BD-RIS can be visualized in Fig. 27. From Fig. 27 we observe that the real and imaginary parts of  $[\mathbf{Y}_I]_{m,m'}$  are dependent on each other in lossy cases and the possible value of  $[\mathbf{Y}_I]_{m,m'}$  depends on the value of  $\alpha$ , while the imaginary part of  $[\mathbf{Y}_I]_{m,m'}$  for lossless cases can take arbitrary values, consistent with existing BD-RIS literature [26], [44], [61]. The impact of lossy interconnections in BD-RIS to system performance has also been shown in Fig. 28, from which we observe that the impact of lossy interconnections in BD-RIS is negligible due to the small interelement spacing.

2) Lossy Admittance Components: In D-RIS, the power loss of each reconfigurable component can be individually characterized in the amplitude of its reflection coefficients [17]. That is, for a lossy D-RIS, each entry  $\Theta_m$  in the scattering matrix has  $|\Theta_m| < 1$ . The smaller the value of  $|\Theta_m|$ , the larger the loss in D-RIS. However, it is not possible

![](_page_26_Figure_8.jpeg)

Fig. 27. Values of  $[\mathbf{Y}_I]_{m,m'}$  modeled as (95) with  $Z_0 = 50\Omega$  and  $\ell_{m,m'} =$ 

![](_page_26_Figure_10.jpeg)

Fig. 28. Average received signal power versus the number of RIS elements with different values of  $\alpha$ . The transmitter, RIS, and, receiver are located at a 3D coordinate system with respectively (0,0,0), (20,0,2), and (20,0,0) in meters (m). The inter-element spacing in BD-RIS is set as 0.05 m. The direct transmitter-receiver channel is assumed to be fully obstructed. Channels through RIS follow i.i.d. Rayleigh fading  $(N = N_r = 1)$  [94].

to model individually the entries in the scattering matrix  $\Theta$ of BD-RIS since they are coupled with each other due to interconnections. To tackle this difficulty, [104] has recently proposed to directly analyze the loss of each reconfigurable admittance component, and the scattering matrix for lossy BD-RIS can be naturally obtained by (16) and (21). This is done by modeling each reconfigurable admittance component as a lumped circuit consisting of inductors  $L_1$ ,  $L_2$ , a tunable capacitance C, and an equivalent resistor R that accounts for the parasitic resistance of the varactor, as illustrated in Fig. 29. The admittance (if is not zero), with a given frequency of signals  $\omega_{c} = 2\pi f_{c}$ , is a function of the tunable capacitance C

$$Y_{m,m'}(C) = \frac{1}{\jmath\omega_{c}L_{1}} + \frac{1}{\jmath\omega_{c}L_{2} + \frac{1}{\jmath\omega_{c}C} + R},$$

$$= \jmath\left(-\frac{1}{\omega_{c}L_{1}} + \frac{-\omega_{c}L_{2} + \frac{1}{\omega_{c}C}}{R^{2} + \left(\omega_{c}L_{2} - \frac{1}{\omega_{c}C}\right)^{2}}\right)$$

$$+ \frac{R}{R^{2} + \left(\omega_{c}L_{2} - \frac{1}{\omega_{c}C}\right)^{2}}, \forall m, m' \in \mathcal{M},$$
(96)

where  $Y_{m,m} = Y_m$ . Specifically, the value of R reflects the amount of power loss in each reconfigurable component and

<sup>&</sup>lt;sup>7</sup>The value of  $\alpha$  depends on the transmission line parameters, including series resistance and inductance, and shunt conductance and capacitance per unit length of the lumped-element equivalent circuit [34].

Fig. 29. An example of a 6-element BD-RIS with group-connected architectures and the equivalent lossy circuit for each admittance component.

![](_page_27_Figure_3.jpeg)

Fig. 30. Values of  $Y_{m,m'}$  modeled as (96). The frequency is set as  $f_{\rm c}=2.4$  GHz.  $L_1=6$  nH,  $L_2=0.7$  nH. Circles represent all possible values of  $Y_{m,m'}$  for varing R, while the practical range is constrained by tha value of capacitance  $C\in[0.35,3.2]$  pF [104].

 $R \neq 0$  in practical devices. Interestingly, the existence of losses in each reconfigurable admittance component makes the real part  $\Re\{Y_{m,m'}\}$  and the imaginary part  $\Im\{Y_{m,m'}\}$  being constrained by a circle in the complex plane, given by

$$\left(\Re\{Y_{m,m'}\} - \frac{1}{2R}\right)^2 + \left(\Im\{Y_{m,m'}\} - \left(-\frac{1}{\omega_{\rm c}L_1}\right)\right)^2 = \left(\frac{1}{2R}\right)^2.$$

An extreme case (R=0) that the real parts of  $Y_{m,m'}$  are zeros corresponds to BD-RIS with lossless reconfigurable admittance components, implying that the feasible range of  $Y_{m,m'}$  lies in the y-axis of the complex plane. This phenomenon can be visualized in Fig. 30 based on a practical varactor SMV2020-079. The impact of lossy admittance components in BD-RIS to system performance is also shown in Fig. 31, from which we observe that the optimum of fully/tree-connected architectures in SISO systems can be destroyed by significant power losses from a large number of lossy reconfigurable admittance components.

The above modeling of lossy interconnections and admittance components is applicable to all reciprocal BD-RIS architectures as illustrated in Section III-D. Given a specific circuit topology, one can simply set  $Y_{m,m'}=0$  to indicate that there are no direct interconnections between port m and m', and adopt (94) or (95) to construct the admittance matrix with

![](_page_27_Figure_9.jpeg)

Fig. 31. Average rate versus R for a lossy BD-RIS-aided SISO system. The channels through BD-RIS follow Rician fading with a Rician factor 2 dB, and the direct channel from the transmitter to the receiver follows Rayleigh fading. The transmitter-receiver, transmitter-RIS, and RIS-receiver distances are respectively set as 52 m, 50 m, and 2.5 m (M=30,  $\bar{M}=6$  for the group/forest-connected architecture, P=20 dBm) [104].

lossy interconnections, and to adopt (96) and (21) to construct the admittance matrix with lossy reconfigurable admittance components. However, the joint consideration of the impact of two kinds of losses to system performance remains unexplored and is a meaningful future research direction.

### C. Wideband Effect

Frequency dependence is an intrinsic phenomenon in circuits, where the response of inductance and capacitance varies with the frequency of an applied signal. Therefore, the response of RIS, i.e., its impedance/admittance/scattering matrices of the reconfigurable impedance network, is naturally frequency dependent [105]. In narrowband communications, since the bandwidth of signals is much less than the central frequency, it is reasonable to approximately assume the response of RIS to be frequency independent. However, when it comes to wideband communications, the frequency dependence in RIS is not negligible. To show how significant is the frequency dependence in RIS-aided wideband communication systems, there have been a few representative works on the wideband modeling, optimization, and implementation of D-RIS [19], [106], [107]. Nevertheless, these works model the wideband effect of D-RIS by characterizing the frequency dependence of the individual entries of its scattering matrix. This does not work for BD-RIS with interconnected elements, and thus coupled entries in its scattering matrix, making it difficult to accurately yet efficiently capture the frequency dependence in BD-RIS. In addition, there have been a few works on applying BD-RIS in wideband systems [108], [109], while they primarily assume a frequency-independent BD-RIS model, which is essentially not consistent with the behavior of BD-RIS in wideband scenarios. To establish a physically consistent BD-RIS model suitable for wideband systems, [110] and [111] have proposed to model the frequency dependence of the individual reconfigurable admittance component based

![](_page_28_Figure_1.jpeg)

![](_page_28_Figure_2.jpeg)

- (a) Susceptance versus frequency
- (b) Susceptance variation

Fig. 32. The susceptance  $\Im\{Y_{m,m'}\}$  as a function of (a) frequency and (b) the value of susceptance at the central frequency  $f_{\rm c}=2.4$  GHz with  $L_1=2.5$  nH,  $L_2=0.7$  nH, and  $C\in[0.2,3]$  pF for a practical varactor diode [110].

on specific circuit designs. Below, we will briefly revisit how to model the frequency dependence in BD-RIS.

In reciprocal BD-RIS architectures, each reconfigurable admittance component can be modeled as a lumped circuit consisting of inductors  $L_1$ ,  $L_2$ , and one tunable capacitor  $C^8$ . Accordingly, the admittance of this circuit is a function of C and the angular frequency  $\omega = 2\pi f$  for the incident signals:

$$Y_{m,m'}(C,\omega) = \frac{1}{j\omega L_1} + \frac{1}{j\omega L_2 + \frac{1}{j\omega C}}, \forall m, m' \in \mathcal{M}, \quad (98)$$

where  $Y_{m,m}$  boils down to the admittance component  $Y_m$ connected to ground. We observe from (98) that, the values of  $Y_{m,m'}$  at different frequencies are linked to each other by a common capacitor C. The relationship can be numerically illustrated in Fig. 32, based on a wideband system with central frequency  $f_c = 2.4$  GHz and a practical varactor diode SMV1231-079 [110]. Results in Fig. 32(a) show that within some practical bandwidth for wideband signals, the susceptance  $\Im\{Y_{m,m'}\}$  can be regarded as a linear function of frequency. This further implies that  $\Im\{Y_{m,m'}\}$  varies approximately linearly with the susceptance at central frequency, as illustrated in Fig. 32(b). This motivates possible simplifications to (98) to benefit BD-RIS optimization. The impact of having frequency-dependent BD-RIS matrices on the performance of a SISO orthogonal frequency division multiplexing (OFDM) system is shown in Fig. 33. Results show that, with increasing circuit complexity (more admittance components) in BD-RIS architectures, an increasing performance gap appears between taking into account the wideband modeling when designing BD-RIS or not. This is attributed to the more significant variation of BD-RIS matrices between subcarriers, so ignoring this variation will cause non-negligible performance loss.

The above modeling is again applicable to all reciprocal BD-RIS architectures as illustrated in Section III-D. Intuitively,

![](_page_28_Figure_12.jpeg)

(a) Group-connected BD-RIS with and without wideband modeling

![](_page_28_Figure_14.jpeg)

(b) Forest-connected BD-RIS with and without wideband modeling

Fig. 33. Average rate versus transmit power P with BD-RIS having different reciprocal architectures ( $M=48,\ M\in\{1,3,6\}$ ). The OFDM channels from the transmitter to the reciever and through BD-RIS are modeled as multitap finite duration impulse response sequences with i.i.d. complex Gaussian random variables. The legend "WM" is short for wideband modeling; "GC" is short for group-connected; "FC" is short for forest-connected. For both "GC" and "FC" architectures, the case of  $\bar{M}=1$  refers to the D-RIS [110].

the higher the circuit complexity (the larger the required number of admittance components) in BD-RIS architectures, the more significant the impact of wideband modeling at BD-RIS. In addition, [112] has proposed to model and analyze the frequency dependence of non-reciprocal BD-RIS with constraint  $\mathcal{T}_{\text{non-diag}}$ , by individually modeling the frequency-dependent scattering parameter of each reconfigurable element. Nevertheless, due to the lack of a unified circuit topology illustration as in reciprocal architectures, the wideband modeling and optimization for more general non-reciprocal BD-RIS architectures still remain unexplored. For clarity, the BD-RIS literature on wideband modeling and optimization has been summarized in Table VII.

## D. Mutual Coupling Effect

Mutual coupling, which refers to the electromagnetic interaction between antenna elements in an array, is an important factor in array design. Mutual coupling is in general inversely proportional to the spacing between elements: the smaller the inter-element spacing, the stronger the mutual coupling. In

<sup>&</sup>lt;sup>8</sup>Here we consider a lossless model with R=0 in Fig. 29 to focus purely on the modeling and analysis of frequency dependence in BD-RIS.

| TABLE VII                                                 |
|-----------------------------------------------------------|
| RD-RIS I ITED ATURE ON WIDERAND MODELING AND OPTIMIZATION |

| Ref.         | Architecture†                                                                                         | Frequency Dependence | Highlights                                                                                                                   |
|--------------|-------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------|
| [108]        | Group-Connected<br>(Multi-Sector Mode)                                                                | No                   | Optimize the spectral and energy efficiency of a multi-user MIMO OFDM system aided by multi-sector BD-RIS                    |
| [109]        | Group-Connected                                                                                       |                      | Derive the wideband system model aided by BD-RIS from time domain and maximize the capacity of a MIMO-OFDM system            |
| [110], [111] | Proposed for Group- and Forest<br>-Connected but also applicable to<br>other Reciprocal Architectures | Yes                  | Propose the wideband modeling of the individual reconfigurable admittance component in BD-RIS based on lumped circuit models |
| [112]        | Non-Diagonal                                                                                          |                      | Propose the wideband modeling of the individual phase shifter in<br>non-diagonal RIS using scattering parameter analysis     |

<sup>†</sup> The BD-RIS works on the reflecting mode unless otherwise stated.

most existing RIS literature, the mutual coupling is ignored by assuming sufficiently large inter-element spacing. However, this strong assumption cannot be easily achieved in practice, given that RIS usually consists of numerous densely spaced elements within a limited aperture to provide sufficient beamforming gain [8], [113]. There have been existing works on the modeling and analysis of the mutual coupling between D-RIS elements [18], [114], [115], which have been recently extended to BD-RIS-aided channels [116]–[118]. Below, we will briefly revisit the modeling of mutual coupling aware BD-RIS-aided channels, and how the existence of mutual coupling impacts the system performance.

Consider a BD-RIS-aided MIMO system consisting of an N-antenna transmitter, an M-element BD-RIS, and an  $N_r$  receiver, as also illustrated in Section IV-B. To capture explicitly the mutual coupling at BD-RIS, [18], [38], [115], [116] have made physics-consistent assumptions and derived the following three equivalent wireless channel models<sup>9</sup>

$$\mathbf{H}_{\mathsf{S}}(\mathbf{\Theta}) = \mathbf{S}_{RT} + \mathbf{S}_{RI}(\mathbf{I}_{M} - \mathbf{\Theta}\mathbf{S}_{II})^{-1}\mathbf{\Theta}\mathbf{S}_{IT}, \tag{99a}$$

$$\mathbf{H}_{\mathsf{Z}}(\mathbf{Z}_{I}) = \frac{1}{2Z_{0}} (\mathbf{Z}_{RT} - \mathbf{Z}_{RI}(\mathbf{Z}_{II} + \mathbf{Z}_{I})^{-1} \mathbf{Z}_{IT}), \qquad (99b)$$

$$\mathbf{H}_{\mathsf{Y}}(\mathbf{Y}_{I}) = \frac{1}{2Y_{0}}(-\mathbf{Y}_{RT} + \mathbf{Y}_{RI}(\mathbf{Y}_{II} + \mathbf{Y}_{I})^{-1}\mathbf{Y}_{IT}), (99c)$$

where  $\mathbf{S}_{RT} \in \mathbb{C}^{N_r \times N}$ ,  $\mathbf{Z}_{RT} \in \mathbb{C}^{N_r \times N}$ , and  $\mathbf{Y}_{RT} \in \mathbb{C}^{N_r \times N}$ , respectively, denote the transmission scattering, impedance, and admittance matrices from the transmitter to receiver;  $\mathbf{S}_{RI} \in \mathbb{C}^{N_r \times M}$ ,  $\mathbf{Z}_{RI} \in \mathbb{C}^{N_r \times M}$ , and  $\mathbf{Y}_{RI} \in \mathbb{C}^{N_r \times M}$ , respectively, denote the transmission scattering, impedance, and admittance matrices from RIS to the receiver;  $\mathbf{S}_{IT} \in \mathbb{C}^{M \times N}$ ,  $\mathbf{Z}_{IT} \in \mathbb{C}^{M \times N}$ , and  $\mathbf{Y}_{IT} \in \mathbb{C}^{M \times N}$ , respectively, denote the transmission scattering, impedance, and admittance matrices from the transmitter to RIS;  $\mathbf{S}_{II} \in \mathbb{C}^{M \times M}$ ,  $\mathbf{Z}_{II} \in \mathbb{C}^{M \times M}$ , and  $\mathbf{Y}_{II} \in \mathbb{C}^{M \times M}$ , respectively, denote the mutual coupling scattering, impedance, and admittance matrices at RIS. Based on the derivations in [38] and [116], these terms are related to one another by  $\mathbf{S}_{RT} = \frac{\mathbf{Z}_{RT}}{2Z_0} - \frac{\mathbf{Z}_{RI}}{2Z_0} (\mathbf{Z}_{II} + Z_0\mathbf{I}_M)^{-1}\mathbf{Z}_{IT}$ ,  $\mathbf{S}_{RI} = \mathbf{Z}_{RI} (\mathbf{Z}_{II} + Z_0\mathbf{I}_M)^{-1}, \mathbf{S}_{IT} = (\mathbf{Z}_{II} + Z_0\mathbf{I}_M)^{-1}\mathbf{Z}_{IT}$ ,  $\mathbf{S}_{II} = (\mathbf{Z}_{II} + Z_0\mathbf{I}_M)^{-1}(\mathbf{Z}_{II} - Z_0\mathbf{I}_M), \mathbf{Y}_{RT} = \frac{1}{Z_0^2} (-\mathbf{Z}_{RT} +$ 

<sup>9</sup>Note that the scattering matrices  $\mathbf{S}_{RT}$ ,  $\mathbf{S}_{RI}$ , and  $\mathbf{S}_{IT}$  in (99a) are not one-to-one mapped to the channels  $\mathbf{H}_{RT}$ ,  $\mathbf{H}_{RI}$ , and  $\mathbf{H}_{IT}$  in the widely adopted model  $\mathbf{H}(\mathbf{\Theta}) = \mathbf{H}_{RT} + \mathbf{H}_{RI}\mathbf{\Theta}\mathbf{H}_{IT}$ . The detailed analysis can be found in [38], [39], [119].

$$\mathbf{Z}_{RI}\mathbf{Z}_{II}^{-1}\mathbf{Z}_{IT}$$
),  $\mathbf{Y}_{RI}=-\frac{\mathbf{Z}_{RI}\mathbf{Z}_{II}^{-1}}{Z_{0}}$ ,  $\mathbf{Y}_{IT}=-\frac{\mathbf{Z}_{II}^{-1}\mathbf{Z}_{IT}}{Z_{0}}$ , and  $\mathbf{Y}_{II}=\mathbf{Z}_{II}^{-1}$ .

Remark 8: The sum of  $\mathbf{Z}_I + \mathbf{Z}_{II}$  in (99b) really highlights the essence of BD-RIS, i.e.,  $\mathbf{Z}_I + \mathbf{Z}_{II}$  acts as a general impedance matrix that captures the joint effect of artificial coupling (induced by inter-element interconnections) and the physical mutual coupling (induced by the closely spaced elements). In the presence of non-zero off-diagonal elements in  $\mathbf{Z}_{II}$ , the non-zero off-diagonal elements of  $\mathbf{Z}_I$  can be engineered and reconfigured, through inter-element inter-connections, to either compensate or exploit the physical mutual coupling. These non-zero off-diagonal elements highlight the underpinning new DoF offered by inter-connecting ports/elements in the surfaces/multi-port impedance network and hence artificially engineering and reconfiguring the coupling across elements of the surface.

Remark 9: We would like to clarify again based on (99a) that the mutual coupling here refers to the physical coupling between antenna elements and is characterized by the matrix  $S_{II}$ , which is determined by the design of the antenna array and is independent of the scattering matrix  $\Theta$  of the reconfigurable impedance network. Readers may argue that by rewriting the channel model  $H_S(\Theta)$  in (99a) as

$$\mathbf{H}_{\mathsf{S}}(\mathbf{\Theta}) = \mathbf{S}_{RT} + \mathbf{S}_{RI}\mathbf{\Theta}_{\mathsf{eff}}\mathbf{S}_{IT},\tag{100}$$

where  $\Theta_{\rm eff} = (\mathbf{I}_M - \Theta \mathbf{S}_{II})^{-1} \Theta$ , one can also obtain a beyond-diagonal matrix  $\Theta_{\rm eff}$  for D-RIS. However, the BD-RIS terminology is used to describe the scattering matrix  $\Theta$ . In this sense, within the BD-RIS, a kind of tunable coupling is artificially introduced between ports of the reconfigurable impedance network, thereby generating  $\Theta$  itself that is not limited to be diagonal.

Remark 10: Another interpretation of BD-RIS has been recently presented in [120], whose main idea is that an M-element BD-RIS-aided channel can be represented as a channel involving an effective D-RIS matrix  $\tilde{\mathbf{\Theta}} \in \mathbb{C}^{\tilde{M} \times \tilde{M}}$ , where  $\tilde{M}$  denotes the number of reconfigurable admittance components in BD-RIS. Specifically, the channel model can be described as

$$\mathbf{H}_{S}(\tilde{\mathbf{\Theta}}) = \tilde{\mathbf{S}}_{RT} + \tilde{\mathbf{S}}_{RI}(\mathbf{I}_{\tilde{M}} - \tilde{\mathbf{\Theta}}\tilde{\mathbf{S}}_{II})^{-1}\tilde{\mathbf{\Theta}}\tilde{\mathbf{S}}_{IT}, \quad (101)$$

where  $\tilde{\mathbf{S}}_{RT} \in \mathbb{C}^{N_{\mathsf{r}} \times N}$ ,  $\tilde{\mathbf{S}}_{RI} \in \mathbb{C}^{N_{\mathsf{r}} \times \tilde{M}}$ , and  $\tilde{\mathbf{S}}_{IT} \in \mathbb{C}^{\tilde{M} \times N}$  can be regarded as some transformations of  $\mathbf{S}_{RT}$ ,  $\mathbf{S}_{RI}$ , and  $\mathbf{S}_{IT}$ . Meanwhile,  $\tilde{\mathbf{S}}_{II} \in \mathbb{C}^{\tilde{M} \times \tilde{M}}$  can be regarded as an

![](_page_30_Figure_1.jpeg)

Fig. 34. Channel gain versus the number of BD-RIS elements (M=16,  $\bar{M}=4$  for group-connected architecture). The direct transmitter-receiver link are assumed to be fully blocked. The markers "FC", "GC", "SC" respectively refer to fully-connected, group-connected, and single-connected (D-RIS); "w/MC" refers to the case accounting for mutual coupling at BD-RIS and "w/o MC" refers to the case where the off-diagonal entries of  $\mathbf{Z}_{II}$  are forced to zero [116].

equivalent "mutual coupling" matrix. In this way, a BD-RISaided wireless channel can be transformed to an effective D-RIS-aided wireless channel with some "mutual coupling".

The impedance matrix  $\mathbf{Z}_{II}$  characterizes the mismatching and mutual coupling at the RIS elements. Specifically, the diagonal entries of  $\mathbf{Z}_{II}$  refer to the self impedance and the off-diagonal entries refer to the mutual coupling depending on the inter-element spacing. Most existing literature assumes perfect matching and no mutual coupling at RIS elements, which is mathematically described as  $\mathbf{Z}_{II} = Z_0 \mathbf{I}_M$ . This assumption makes  $\mathbf{S}_{II} = \mathbf{0}_{M \times M}$  and the wireless channel  $\mathbf{H}_{S}(\Theta)$  in (99) a linear function of  $\Theta$ , as widely assumed in most existing RIS literature. However, as discussed above, it is difficult to achieve such a strong assumption in practice. That is, the off-diagonal entries of  $\mathbf{Z}_{II}$  are generally nonzero, and can be modeled as functions of inter-element spacing [18], [115].

To evaluate how the existence of mutual coupling impacts the system performance, [116] has primarily focused on a group/fully-connected BD-RIS-aided SISO system and proposed an iterative algorithm to design the BD-RIS impedance matrix. Simulation results in Fig. 34 demonstrate that, under purely LoS channels, the performance gap between BD-RIS and D-RIS increases with decreasing inter-element distance since the stronger mutual coupling is better exploited by BD-RIS architectures. This indicates that BD-RIS is suitable for compact deployment with small inter-element spacing. In addition, [117] has proposed decoupling networks as a solution to compensate for the mutual coupling at BD-RIS. The decoupling network can transform the system into a structure equivalent to a system without mutual coupling. As

such, the beamforming design algorithms primarily proposed for systems without mutual coupling can be directly used for the case where the mutual coupling exists. Following the idea of using decoupling networks, [118] has proposed global optimal closed-form solutions for fully-connected and tree-connected BD-RIS-aided SISO systems, and provided the channel gain scaling law in the presence of mutual coupling. Specifically, for a SISO system with Rayleigh fading channels, [118] has derived the average power gain in the presence of mutual coupling at fully/tree-connected BD-RIS over that without mutual coupling, that is

$$G^{\rm MC} = Z_{II}^2 \frac{{\rm tr}(\mathbf{R}^2) + {\rm tr}^2(\mathbf{R}) + \sqrt{\pi {\rm tr}(\mathbf{R}^2)} {\rm tr}(\mathbf{R})}{M + M^2 + \sqrt{\pi M} M}, \quad (102)$$

where  $\mathbf{R}=\Re\{\mathbf{Z}_{II}\}^{-1}$  and  $[\mathbf{Z}_{II}]_{m,m}=Z_{II}, \forall m\in\mathcal{M},$  and theoretically proved that  $G^{\text{MC}}\geq 1$  using the fact that  $\operatorname{tr}(\mathbf{R})\geq \frac{M}{Z_{II}}$  and that  $\operatorname{tr}(\mathbf{R}^2)\geq \frac{M}{Z_{II}^2}$ . This highlights that mutual coupling in fully/tree-connected BD-RIS can increase the average channel gain under Rayleigh fading channels. Not limited to SISO systems, [121] has considered more general multi-user multi-antenna systems, derived the mutual coupling aware channel model, and optimized BD-RIS under different modes to maximize the system sum-rate. Results show that not accurately capturing the mutual coupling effect at BD-RIS will cause a non-negligible sum-rate performance loss. More recently, [122] has proven that band-connected architecture can achieve the same channel shaping capability as fully-connected architecture in multi-user MIMO systems with practical channel models capturing mutual coupling and other electromagnetic factors, which further generalizes the results in [44], [45], [118]. While the aforementioned works [116]-[118], [121], [122] assume idealized BD-RIS hardware to better understand the impact of mutual coupling, [123] has focused on more general situations to discover optimal BD-RIS architectures that have the best performance-complexity tradeoff with mutual coupling, losses, and discrete values.

## VII. APPLICATIONS OF BD-RIS

The appealing benefits of BD-RIS have spawned an explosion of application-oriented works together with other promising 5G/6G techniques, such as advanced multiple access techniques, sensing, and WPT. In this section, we summarize the emerging applications of BD-RIS, as detailed below and summarized in Table VIII.

## A. BD-RIS for Communications

1) BD-RIS for Channel Shaping: Most existing BD-RIS literature focuses on specific metrics, such as channel gain, sum-rate, transmit power consumption, to evaluate the performance benefit of BD-RIS, while a fundamental question which has not been answered is, to what extent a BD-RIS can shape the wireless channels (in terms of their singular values). To answer this question, [54] has theoretically proven that BD-RIS is able to reach a larger dynamic range of channel singular values than D-RIS. Results in [54] have shown that this capability of BD-RIS can help to increase power gain and achievable rates. Further, [124], [125] have recently shown that

TABLE VIII
LITERATURE ON APPLICATIONS OF BD-RIS

| Ref.         | Application             | Architecture          | Mode         | Metric                                        |
|--------------|-------------------------|-----------------------|--------------|-----------------------------------------------|
| [54]         |                         | Non-Reciprocal        | Reflecting   | Channel Gain & Sum-Rate Max.                  |
| [124]        | Channel Shaping         | Fully/Group-Connected |              | Sum-Rate Max. & Interference Nulling          |
| [125]        |                         | runy/Group-Connected  |              | Interference Min.                             |
| [126]        | Physical Layer Security |                       |              | Secrecy Rate Max. & Secrecy Outage Prob. Min. |
| [127]        | Thysical Layer Security |                       |              | Sum-rate Max.                                 |
| [128], [129] | Reciprocity Attack      | Non-Reciprocal        |              | Sum-Rate Min.                                 |
| [130]        | THz Commun.             |                       | Hybrid       | Sum-Rate Max.                                 |
| [131]        |                         | [                     | Reflecting   | Max. Min. Rate                                |
| [132]        | Massive MIMO            | Fully/Group-Connected | Hybrid       | Bit Error Rate Min. & Rate. Max.              |
| [133]        |                         | Non-Reciprocal        | ,            | Sum-Rate Max.                                 |
| [134]        | Wireless Sensing        | Group-Connected       | Multi-Sector | Mean Square Error Min.                        |
| [135]        | Localization            | Fully-Connected       | Reflecting   | Cramér-Rao Lower Bound Analysis               |
| [136]        |                         | Non-Reciprocal        | Hybrid       | Max. Min. Signal-to-Clutter-Plus-Noise Ratio  |
| [137]        |                         | Fully-Connected       |              | Weighted Sum of Radar and Commmun. SNRs Max.  |
| [138]        | ISAC                    |                       |              | Power Min.                                    |
| [139]        | ] ISAC                  |                       | Reflecting   | Sum-Rate (Throughput) Max.                    |
| [140]        |                         |                       |              | Joint Sum-Rate Max. & Cramér-Rao Bound Min.   |
| [141]        |                         |                       |              | Outage Probability Analysis                   |
| [142], [143] | WPT                     |                       |              | Direct Current Harvested Power Max.           |
| [144]        | SWIPT                   |                       |              | Sum-Rate Max. & Harvested Power Max.          |
| [145]        | SIM                     | Fully/Group-Connected | Hybrid       | Channel Gain Max.                             |
| [146]        | NOMA                    | Fully/Group-Connected |              | Sum-Rate Max.                                 |
| [147]        | NOWA                    | Non-Reciprocal        | Reflecting   | Max. Min. Rate                                |
| [148]–[150]  |                         | Fully/Group-Connected | Reflecting   | Sum-Rate Max.                                 |
| [151]        | RSMA                    | 1                     |              | Max. Min. Rate                                |
| [152]        |                         | Group-Connected       | Multi-Sector | Ergodic Sum-Rate Max. (Imperfect CSI)         |
| [153]        |                         | Non-Reciprocal        | -            | Sum-Rate Max.                                 |
| [154]        | UAV                     | 1                     |              | Min. Max. Computational Time                  |
| [155]        |                         | Fully/Group-Connected | Reflecting   | Zero Secrecy Rate Prob. Min.                  |
| [156]        | NTN                     | Non-Reciprocal        |              | Secrecy Rate Max.                             |
| [157]        |                         | •                     |              | Rate Max.                                     |
| [158]        | MEC                     | Non-Reciprocal        | Hybrid       | No. of Completed Task Bits Max.               |

BD-RIS can achieve better interference nulling/minimization to MIMO interference channels, which can be explained by the potential of BD-RIS to reduce the DoF.

2) BD-RIS Aiding Channel Reciprocity Attack and Physical Layer Security: According to microwave engineering, conventional wireless channels are naturally reciprocal, in the sense that the uplink channel is the transpose of the downlink channel. However, as explained in the previous subsection, introducing non-reciprocal BD-RIS in the wireless propagation environment can break the uplink-downlink reciprocity of wireless channels. From the perspective of physical layer security, this property of non-reciprocal BD-RIS can be beneficial to support simultaneously optimal uplink and downlink transmission when downlink and uplink legitimate users are not aligned, as illustrated in Fig. 22. Non-reciprocal BD-RIS can also be helpful to enhance the secrecy rate and secrecy outage probability [126] and enable a wireless circulator for one-way secure communications [127] in the presence of eavesdroppers. From an attacker's perspective, this property can still be useful since a non-reciprocal BD-RIS can be potentially deployed to maliciously degrade the downlink network performance [128], [129].

3) BD-RIS in Terahertz Communications and Massive MIMO: The need for more spectrum resources and higher frequency bands, such as Terahertz frequency bands, to provide higher spectrum efficiency and support emerging applications is one important trend for future networks. However, one bottleneck of Terahertz communications is the severe path loss

in wireless channels, which makes the transmission vulnerable to blockages [159]. BD-RIS has been shown to be a reliable solution to Terahertz communications, which can be useful to bypass blockages, increase coverage and system rates [130].

To compensate for the severe path loss in higher frequency bands, serve numerous users in the same time-frequency resource, and support increasing connectivity in 6G, another promising technique is massive MIMO [160]. However, the high spectrum efficiency of massive MIMO is achieved at the cost of numerous RF chains, leading to energy inefficiency in the network. To reduce the required number of RF chains while maintaining satisfactory spectrum efficiency, [131], [132] have recently proposed to integrate BD-RIS within the radome of a transmitter as an auxiliary passive array, enabling a small-dimensional active antenna array at the transmitter to provide highly-directional beams reconfigured by BD-RIS. While [131], [132] focused on single-transmitter scenarios, [133] has considered a more general cell-free network and verified the performance benefits provided by BD-RIS.

## B. BD-RIS for Sensing and ISAC

Future networks are expected to support an increasing number of spectrum-demanding applications, which will cause increasing radio spectrum congestion. This growth motivates the design of shared paradigms, which enable cooperative spectrum and resource sharing among systems. One such solution is the emerging ISAC technique [6], which realizes dual functions with shared hardware, platform, and resources to

reduce costs and increase resource utilization. However, since wireless sensing relies on strong LoS channels, which can be obstructed by obstacles in complex wireless propagation environments, it might be difficult to achieve a satisfactory ISAC performance in practical scenarios. To tackle this challenge, [134] has proposed a multi-sector BD-RIS self-sensing system, where an active source controller is installed on one sector such that signals can be scattered toward other sectors to achieve full-space coverage. BD-RIS can also perform as a bridge to link active and passive localization [135] and effectively increase localization precision. Beyond enabling sensing and localization, there have been a few works on BD-RIS-aided ISAC [136]–[141]. Specifically, [136] proposed a hybrid BD-RIS-aided ISAC system where targets and users are located at both transmitting and reflecting sectors of BD-RIS, such that the performance of both functions and coverage is improved. In addition, deploying BD-RIS in ISAC systems can also help to increase signal-to-noise ratio (SNR) for both functions [137], reduce transmit power [138], enhance network throughput [139], achieve better communication-sensing tradeoff [140], and meet ISAC outage requirements [141].

## *C. BD-RIS for WPT and SWIPT*

Energy harvesting techniques are fundamental enablers for realizing seamless and green connectivity between low-power devices and supporting IoT in future wireless networks [161]. Among various energy harvesting techniques, WPT is a paradigm making full use of wireless to deliver energy [7]. Beyond WPT, a shared paradigm has been proposed, namely SWIPT [7], [28], which enables using wireless to not only deliver energy but also convey information to best use the RF spectrum. To further enlarge the effective distance of WPT/SWIPT and improve the power transfer efficiency, [142], [143] have deployed BD-RIS in the wireless system, showing that BD-RIS can flexibly shape the wireless channel to facilitate WPT. In addition, [144] has focused on a SWIPT system and demonstrated that BD-RIS is beneficial in improving both harvested energy of energy users and spectral efficiency of information users.

## *D. BD-RIS with Other Techniques and Systems*

- *1) BD-RIS and Stacked Intelligent Metasurface (SIM):* Stacked intelligent surface (SIM) [162] consists in stacking multiple layers of RIS or metasurfaces to provide more flexible wave manipulations. While SIM layers have been implemented using D-RIS [162], [145] has recently shown that SIM layers can be implemented using BD-RIS. Theoretical and numerical results have demonstrated that 1-layer SIM implemented with BD-RIS (tree-connected) is sufficient to achieve performance upper-bound in SISO systems, while multi-layer SIM implemented with D-RIS is suboptimal.
- *2) BD-RIS with Advanced Multiple Access:* Multiple access refers to techniques that make use of resource dimensions, such as time, frequency, space, and power, to serve multiple users. Non-orthogonal multiple access (NOMA) has been actively studied recently due to its benefits in exploiting

the available resources more efficiently with the aid of superposition coding at the transmitter and successive interference cancellation (SIC) at the receiver [163]. To further boost system performance, the interaction between NOMA and BD-RIS has been studied in [146], [147], showing that better user fairness can be achieved. In addition, rate-splitting multiple access (RSMA) is a novel and general framework for non-orthogonal transmissions, softly including NOMA as an extreme case [164] and moving beyond that to provide enhanced performance. Given that channel acquisition of RISaided wireless systems is generally challenging while RSMA is robust to CSI imperfections, the integration of the two has emerged [148]–[152]. Specifically, [148]–[151] have focused mainly on perfect CSI and have shown the benefits of such an integration in increasing spectral efficiency, fairness rate, and fairness energy efficiency. [152] has further shown that the integration of the two can still increase system sum-rate when only imperfect CSI is available at the transmitter.

- *3) BD-RIS Aiding Unmanned Aerial Vehicle (UAV) and Non-Terrestrial Networks (NTN):* Unmanned Aerial Vehicle (UAV) has gained attention for 5G and 6G networks due to its advantages in extending coverage, easing the deployment, and supporting controllable mobility [165]. These advantages of UAVs can be further strengthened by cooperating with BD-RIS. [153] and [155] studied the transmission strategy and user scheduling schemes of a ground-based BD-RIS in a network consisting of multiple UAVs, showing that the system performance can be much improved with the aid of BD-RIS. [154] proposed to colocate BD-RIS and UAVs to minimize the computation latency and UAV hovering time. Not limited to UAV-enabled systems, BD-RIS can also provide performance benefits in general non-terrestrial networks (NTN) typically realized by satellites, high-altitude platform stations (HAPS), and UAVs [166]. Results in [156], [157] have shown that having a BD-RIS mounted UAV [156] or HAPS [157] as a secondary transmitter in a cognitive radio enabled NTN helps increase secrecy rate and spectral efficiency.
- *4) BD-RIS Aiding Mobile Edge Computing (MEC):* Mobile edge computing (MEC) [167] is a platform that pushes mobile computing, network control, and storage to the network edges, such as base stations and access points. In this way, MEC enables resource-limited mobile devices to complete computational-intensive tasks with much reduced latency. To further improve the scalability and performance of MEC to meet the growing user demands in 5G and future 6G networks, [158] has proposed deploying BD-RIS in the wireless propagation environment as an enabler to significantly improve the number of completed task bits.

## VIII. CHALLENGES AND FUTURE RESEARCH DIRECTIONS OF BD-RIS

Despite the significant benefits of BD-RIS architectures and modes, the study of BD-RIS is still in its infancy. There exist technical challenges in designing and implementing BD-RIS for practical wireless systems, which motivate meaningful future research directions. In this section, we discuss key challenges in BD-RIS from the perspectives of implementation,

![](_page_33_Figure_1.jpeg)

(a) Inner and side views of hybrid BD-RIS

![](_page_33_Figure_3.jpeg)

(b) An overall view of hybrid BD-RIS

Fig. 35. Photograph of the prototype of the hybrid BD-RIS with 4 *×* 4 cells and the controlling systems [168].

circuit design, optimization, and transmission protocol, each of which is followed by potential research directions.

### *A. BD-RIS Implementation*

The hardware implementation of BD-RIS is a fundamental yet challenging issue. Until now, there has been the implementation of one special type of BD-RIS, namely STAR-RIS (or IOS, STARS) [41]. In addition, a hybrid mode BD-RIS has been recently implemented using power splitters as shown in Fig. 35, enabling independent beam control of reflected and transmitted waves [168]. Furthermore, a reflective mode BD-RIS, specifically a tridiagonal BD-RIS, has been implemented through a tunable load network allowing interconnections among adjacent RIS elements as shown in Fig. 36 [169]. These results show that it is physically feasible to implement BD-RIS using existing RF techniques, designs, and devices. However, the comprehensive implementation of various BD-RIS modes and architectures is still on its way. Based on the illustration in Section III, an *M*-element BD-RIS consists of an *M*-antenna array and an *M*-port reconfigurable impedance network.

- *•* The implementation of the *M*-antenna array varies with operation modes. For the reflective mode, the conventional uniform linear or planar array can be directly used. For the hybrid mode, each pair of antennas with uni-directional radiation pattern (such as patch antennas) should be back to back placed to construct a cell, and all cells should be arranged in a uniform array. For the multi-sector mode, every *L* antennas with corresponding beamwidth should be placed as a polygon and all cells should be arranged in a uniform array.
- *•* The implementation of the *M*-port reconfigurable impedance network varies with architectures. For

![](_page_33_Figure_11.jpeg)

(a) Photo of the tridiagonal BD-RIS showing an antenna array (top) connected to a tunable load network (bottom)

![](_page_33_Figure_13.jpeg)

![](_page_33_Figure_14.jpeg)

![](_page_33_Figure_15.jpeg)

(b) Schematic of the tridiagonal BD-RIS and its matrix **Y***<sup>I</sup>* determined by the switch configuration in the schematic

Fig. 36. Photograph and schematic of the prototype of the tridiagonal BD-RIS with 8 elements [169].

fully/group-, tree/forest-, stem/band-connected architectures, as per the circuit topology, varactors consisting of inductance and tunable capacitance can be used to implement continuous-value reconfigurable admittance components; PIN diodes can be used to implement discretevalue reconfigurable admittance components. For dynamically connected architectures, additional switches are required between every two elements. For non-reciprocal architectures, non-reciprocal devices, such as circulators, isolators, and gyators, are required and the number of them depends on specific circuit designs.

*1) Challenge:* The unique challenge of implementing BD-RIS compared to D-RIS lies in the increasing circuit complexity, cost, and power losses of the reconfigurable impedance network. Especially when the number of elements and/or groups increases, the required number of reconfigurable admittance components significantly increases. This will cause a heavy burden on circuit design and, more importantly, accumulated power losses, and power consumption of drive circuits and elements induced by more reconfigurable admittance components [170], which may weaken the performance benefits of BD-RIS architectures. In addition, for future system-level experiments, the theoretical channel estimation and beamforming optimization methods might require too much time such that an effective data transmission cannot be guaranteed.

*2) Future Research Direction:* Although the tree/forestconnected architecture [44] and the stem/band-connected architecture [45] have been proposed to achieve the best performance-complexity trade-off in, respectively, MISO and multi-user MIMO systems, these conclusions still stop in the analytical layer. The practical limitation of these architectures taking into account the circuit design feasibility, cost, and power losses still remains unexplored. In addition, it is important to establish a fair power consumption model for BD-RIS architectures and validate its feasibility by practical measurements. How to balance the circuit complexity, computational complexity for optimization, and system performance for a practical BD-RIS-assisted test bed is also a crucial problem. Therefore, it is challenging but worthwhile to implement and prototype different BD-RIS architectures to have a practical picture on which kind of architecture could best balance the performance, hardware considerations, and computational complexity.

### *B. Active BD-RIS*

The existing literature of BD-RIS has focused purely on its passive (at best lossless) form, in the sense that the power scattered by the surface is no larger than the incident power. This assumption comes from D-RIS literature and brings many advantages to both D-RIS and BD-RIS, such as low cost, low power consumption, and negligible thermal noise [8]. However, since the array gain provided by numerous elements of RIS cannot fully compensate for the huge multiplicative fading induced by RIS, the performance improvement of passive RIS is very limited. For D-RIS, the gain in some scenarios is even not visible when the direct link between the transmitter and receiver exists. For BD-RIS, in SISO systems, the fully-connected architecture achieves a maximum of 62% gain over D-RIS [26] with the absence of the direct link, which is not sufficiently high, especially when the direct link is strong. To break the fundamental performance bottleneck caused by multiplicative fading, the concept of active D-RIS has been proposed in [21]. The key feature of such D-RIS is its ability to reflect signals with amplified powers, thanks to the introduction of power amplifiers in RIS elements. The benefits of active D-RIS has also been shown in many aspects, such as achieving a substantial sum-rate gain of 130% [21], achieving higher energy efficiency than passive D-RIS [171], and further enhancing both communication quality and sensing performance [172]. This motivates the consideration of active BD-RIS: *Will integrating active power amplifiers in BD-RIS architectures provide orders of gains?*

*1) Challenge:* To answer the above question, one fundamental yet challenging issue is to establish a physics-consistent model for active BD-RIS. Different from passive BD-RIS which is modeled as an antenna array connected to a multiport reconfigurable impedance network, the active BD-RIS, following the modeling principle in [21], should be modeled as a series connection of an antenna array, a multi-port reconfigurable impedance network, and a reflection power amplifier network. In this sense, the admittance/impedance/scattering matrices themselves of the reconfigurable impedance network are not sufficient to characterize the active BD-RIS, and the impact of power amplifiers should be carefully taken into account.

*2) Future Research Direction:* The consideration of making BD-RIS active opens many interesting and meaningful research directions, such as theoretically deriving the power scaling law of active BD-RIS for different channel fading conditions; revisiting the optimal performance-circuit complexity Pareto frontier or exploring the optimal performancepower consumption Pareto frontier for active BD-RIS; and fully making use of the active property to reduce channel estimation error and overhead. Beyond these examples, other fundamental directions in passive BD-RIS, such as the impact of hardware impairments, will also be worth studying in active BD-RIS. In this case, hardware impairments will not be limited to those summarized in Section VI, but will also include the imperfections of power amplifiers.

## *C. Artificial Intelligence (AI)-Driven Beamforming Solutions*

From the beamforming design perspective, most existing literature on BD-RIS uses conventional optimization methods to design BD-RIS beamforming, aiming at either finding closedform solutions with a guaranteed performance or finding iterative solutions with a guaranteed convergence. However, these optimization methods have the following drawbacks: 1) They depend heavily on accurate physics modeling of wireless channels and thus are not easy to be used in practical scenarios where theoretical models cannot fully reflect the true characteristics of wireless environments; 2) The computational complexity can be extremely high when considering largedimensional scenarios, which are unfortunately quite common in the modern world. Although BD-RIS theoretically has appealing benefits supported by these optimization methods, it is important to improve the scalability and feasibility of BD-RIS design methods to prepare for the possible future commercialization of BD-RIS. This thus motivates the consideration of using artificial intelligence (AI)-driven solutions, since they are not sensitive to models and suitable for largescale problems [173], [174].

- *1) Challenge:* Although adopting AI-driven solutions in BD-RIS-aided wireless systems presents significant opportunities for optimization, automation, and efficiency, several challenges must be addressed. For example, in BD-RIS-aided wireless communication systems, it is expected to flexibly tune BD-RIS to adapt to the time-varing dynamic environments, which requires fast real-time decisions and is thus challenging due to the practical limitations of resources, costs, and hardware. For another example, AI-driven solutions heavily depend on high-quality training data, while it is challenging to acquire such data in BD-RIS-aided systems due to practical hardware limitations, channel dynamics, and measurement overhead.
- *2) Future Research Direction:* Although [72], [73] have adopted deep reinforcement learning (DRL) and meta-learning to design BD-RIS-aided wireless communication systems and shown the benefits of such AI-driven solutions in being

friendly to large-scale wireless systems, the study in this direction is still in its infancy. Future research avenues include, but are not limited to, designing more efficient online adaptation schemes to enable highly reliable instantaneous transmissions and establishing proper AI models that can properly adapt to various BD-RIS architectures, that are robust to real hardware constraints of BD-RIS, and that have good training overheadperformance trade-offs.

## *D. CSI-Free Protocols*

Channel estimation*→*feedback and beamforming*→*data transmission is a protocol typically used in wireless communication systems [175]. Most studies on RIS-aided wireless communication systems also adopts this protocol, in which the data transmission performance depends highly on the channel estimation accuracy. However, as discussed in Section IV-C, due to the passive property of RIS, the channel estimation of BD-RIS-aided systems suffers high channel estimation error and/or high training overhead which grow with the circuit complexity of architectures. This motivates the consideration on making the protocol itself less dependent on accurate channel acquisition.

- *1) Challenge:* In D-RIS-aided systems, protocols based on beam training schemes have been proposed to reduce overhead and avoid the requirement for accurate CSI acquisition [176]–[178]. Specifically, a codebook consisting of possible scattering matrices of RIS is predefined in an offline stage. During the online stage, the transmitter consecutively sends pilot signals while the RIS switches between codewords in the codebook. The receiver collects the received signal powers corresponding to all codewords, finds the index of the codeword which leads to the best received power, and feeds this index back to the transmitter. In this way, the channel estimation and beamforming phases in the typically used protocol are replaced with a beam training phase supported by a predefined codebook, such that the RIS can be optimized without explicitly knowing the CSI. The main difficulty in this protocol lies in the construction of RIS codebook. Especially when it comes to BD-RIS with various architectures, it is challenging to construct codebooks whose codewords perfectly follow the constraints of corresponding architectures and have sufficiently large diversity to reflect the flexibility of BD-RIS architectures compared to D-RIS.
- *2) Future Research Direction:* Based on the above discussions, before going to the design of the codebook, it remains unexplored but is important to establish suitable and rigorous criteria to evaluate if a codebook for a specific BD-RIS architecture is "good". With these criteria, it is interesting to explore the relationship between the weights in a neural network and codewords in a codebook, such that learning-based methods can be adopted to facilitate the codebook design. Beyond this, the idea of end-to-end learning for communication systems [179] can be potentially adopted in practical BD-RIS-aided systems without even knowing the channel model.

## *E. New BD-RIS Architectures*

BD-RIS represents a general class of RIS architectures that are more flexible than D-RIS as they include additional tunable components interconnecting the RIS elements with each other. Thanks to this additional flexibility, BD-RIS can further improve the channel shaping capabilities of D-RIS, leading to superior performance in wireless systems, e.g., in terms of channel gain in single-user systems [26] or sumrate in multi-user systems [40]. Since this performance gain comes at the cost of increased hardware complexity due to the additional impedance components, the fundamental question that arises when considering the deployment of BD-RIS is "*Is the additional hardware complexity justified by the resulting performance improvements?*"

- *1) Challenge:* To answer this question, the limits of the trade-off between performance and hardware complexity enabled by BD-RIS need to be studied. In this direction, a model of BD-RIS architectures based on graph theory has been used in previous literature to derive the tree-, forest-, stem-, and band-connected BD-RIS architectures as efficient BD-RIS architectures with reduced complexity [44]–[46]. In addition, the set of BD-RIS architectures achieving the Pareto frontier of this performance-complexity trade-off has been characterized for SISO systems, uni-polarized [93] as well as dualpolarized [101]. However, only a limited number of BD-RIS architectures have been explored so far, which are proven to achieve a good trade-off between performance and complexity only under ideal assumptions, e.g., arbitrarily reconfigurable components, lossless RIS, and absence of mutual coupling.
- *2) Future Research Direction:* From the graph theoretical model of BD-RIS, we find that the number of possible *M*element BD-RIS architectures is 2*M*(*M−*1)*/*<sup>2</sup> , as there are *M*(*M −* 1)*/*2 possible interconnections between the *M* elements. This huge number of potential BD-RIS architectures offers a vast design space that remains largely unexplored. A promising direction for future research is the development of novel BD-RIS architectures that offer favorable performancecomplexity trade-offs, particularly under practical constraints such as hardware impairments and real-world non-idealities.

## IX. CONCLUSION

The existing literature has shown that the capability of BD-RIS in reconfiguring the coupling between elements with interelement admittance components provides additional flexibility to manipulate signals and waves in the analog domain. This capability of BD-RIS has generated multidimensional benefits to enable higher performance, larger coverage, and denser connectivity for future wireless networks. In this paper, we have provided the first holistic tutorial on BD-RIS as a brandnew advance in the RIS technique. We have thoroughly shared all the technical tools and strategies to model, design, and optimize BD-RIS. In support of these fundamentals, we have highlighted key benefits, emerging applications, challenges, and possible future research directions of BD-RIS. The scope of this tutorial spanned from fundamental physics-consistent modeling using multi-port network analysis, mode analysis, reciprocal and non-reciprocal architecture designs; representative signal processing strategies for BD-RIS beamforming and channel estimation; and modeling and analysis of key hardware impairments of BD-RIS, to higher-level summaries of benefits supported by flexible modes and architectures; applications in wireless communications, sensing, and power transfer; and challenges from perspectives of hardware implementation and signal processing which triggered directions crucial for promoting the possible commercialization of BD-RIS. We hope that this paper will serve as a useful resource to teach and inspire readers in the wireless society, and provide fresh blood to activate interesting and meaningful future research on BD-RIS.

## REFERENCES

- [1] H. Tataria, M. Shafi, A. F. Molisch, M. Dohler, H. Sjoland, and ¨ F. Tufvesson, "6G wireless systems: Vision, requirements, challenges, insights, and opportunities," *Proc. IEEE*, vol. 109, no. 7, pp. 1166– 1199, 2021.
- [2] C.-X. Wang, X. You, X. Gao, X. Zhu, Z. Li, C. Zhang, H. Wang, Y. Huang, Y. Chen, H. Haas *et al.*, "On the road to 6G: Visions, requirements, key technologies, and testbeds," *IEEE Commun. Surveys & Tuts.*, vol. 25, no. 2, pp. 905–974, 2023.
- [3] S. Dang, O. Amin, B. Shihada, and M.-S. Alouini, "What should 6G be?" *Nature Electronics*, vol. 3, no. 1, pp. 20–29, 2020.
- [4] B. Clerckx, Y. Mao, Z. Yang, M. Chen, A. Alkhateeb, L. Liu, M. Qiu, J. Yuan, V. W. Wong, and J. Montojo, "Multiple access techniques for intelligent and multifunctional 6G: Tutorial, survey, and outlook," *Proc. IEEE*, 2024.
- [5] H. Lu, Y. Zeng, C. You, Y. Han, J. Zhang, Z. Wang, Z. Dong, S. Jin, C.-X. Wang, T. Jiang *et al.*, "A tutorial on near-field XL-MIMO communications towards 6G," *IEEE Commun. Surveys & Tuts.*, 2024.
- [6] F. Liu, Y. Cui, C. Masouros, J. Xu, T. X. Han, Y. C. Eldar, and S. Buzzi, "Integrated sensing and communications: Toward dualfunctional wireless networks for 6G and beyond," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 6, pp. 1728–1767, 2022.
- [7] B. Clerckx, K. Huang, L. R. Varshney, S. Ulukus, and M.-S. Alouini, "Wireless power transfer for future networks: Signal processing, machine learning, computing, and sensing," *IEEE J. Sel. Topics Signal Process.*, vol. 15, no. 5, pp. 1060–1094, 2021.
- [8] M. Di Renzo, A. Zappone, M. Debbah, M.-S. Alouini, C. Yuen, J. De Rosny, and S. Tretyakov, "Smart radio environments empowered by reconfigurable intelligent surfaces: How it works, state of research, and the road ahead," *IEEE J. Sel. Areas Commun.*, vol. 38, no. 11, pp. 2450–2525, 2020.
- [9] Q. Wu, G. Chen, Q. Peng, W. Chen, Y. Yuan, Z. Cheng, J. Dou, Z. Zhao, and P. Li, "Intelligent reflecting surfaces for wireless networks: Deployment architectures, key solutions, and field trials," *IEEE Wireless Commun.*, 2025.
- [10] N. Kaina, M. Dupre, G. Lerosey, and M. Fink, "Shaping complex ´ microwave fields in reverberating media with binary tunable metasurfaces," *Scientific reports*, vol. 4, no. 1, p. 6693, 2014.
- [11] W. Tang, M. Z. Chen, J. Y. Dai, Y. Zeng, X. Zhao, S. Jin, Q. Cheng, and T. J. Cui, "Wireless communications with programmable metasurface: New paradigms, opportunities, and challenges on transceiver design," *IEEE Wireless Commun.*, vol. 27, no. 2, pp. 180–187, 2020.
- [12] Q. Wu, B. Zheng, C. You, L. Zhu, K. Shen, X. Shao, W. Mei, B. Di, H. Zhang, E. Basar *et al.*, "Intelligent surfaces empowered wireless network: Recent advances and the road to 6G," *Proc. IEEE*, 2024.
- [13] H. Guo, Y.-C. Liang, J. Chen, and E. G. Larsson, "Weighted sumrate maximization for reconfigurable intelligent surface aided wireless networks," *IEEE Trans. Wireless Commun.*, vol. 19, no. 5, pp. 3064– 3076, 2020.
- [14] Q. Wu and R. Zhang, "Intelligent reflecting surface enhanced wireless network via joint active and passive beamforming," *IEEE Trans. Wireless Commun.*, vol. 18, no. 11, pp. 5394–5409, 2019.
- [15] A. L. Swindlehurst, G. Zhou, R. Liu, C. Pan, and M. Li, "Channel estimation with reconfigurable intelligent surfacesA general framework," *Proc. IEEE*, vol. 110, no. 9, pp. 1312–1338, 2022.
- [16] B. Zheng, C. You, W. Mei, and R. Zhang, "A survey on channel estimation and practical passive beamforming design for intelligent reflecting surface aided wireless communications," *IEEE Commun. Surveys & Tut.*, vol. 24, no. 2, pp. 1035–1071, 2022.
- [17] S. Abeywickrama, R. Zhang, Q. Wu, and C. Yuen, "Intelligent reflecting surface: Practical phase shift model and beamforming optimization," *IEEE Trans. Commun.*, vol. 68, no. 9, pp. 5849–5863, 2020.

- [18] G. Gradoni and M. Di Renzo, "End-to-end mutual coupling aware communication model for reconfigurable intelligent surfaces: An electromagnetic-compliant approach based on mutual impedances," *IEEE Wireless Commun. Lett.*, vol. 10, no. 5, pp. 938–942, 2021.
- [19] H. Li, W. Cai, Y. Liu, M. Li, Q. Liu, and Q. Wu, "Intelligent reflecting surface enhanced wideband MIMO-OFDM communications: From practical model to reflection optimization," *IEEE Trans. Commun.*, vol. 69, no. 7, pp. 4807–4820, 2021.
- [20] A. Araghi, M. Khalily, M. Safaei, A. Bagheri, V. Singh, F. Wang, and R. Tafazolli, "Reconfigurable intelligent surface (RIS) in the sub-6 GHz band: Design, implementation, and real-world demonstration," *IEEE Access*, vol. 10, pp. 2646–2655, 2022.
- [21] Z. Zhang, L. Dai, X. Chen, C. Liu, F. Yang, R. Schober, and H. V. Poor, "Active RIS vs. passive RIS: Which will prevail in 6G?" *IEEE Trans. Commun.*, vol. 71, no. 3, pp. 1707–1725, 2022.
- [22] H. Yang, S. Kim, H. Kim, S. Bang, Y. Kim, S. Kim, K. Park, D. Kwon, and J. Oh, "Beyond limitations of 5G with RIS: Field trial in a commercial network, recent advances, and future directions," *IEEE Commun. Mag.*, vol. 62, no. 10, pp. 132–138, 2023.
- [23] R. Liu, Q. Wu, M. Di Renzo, and Y. Yuan, "A path to smart radio environments: An industrial viewpoint on reconfigurable intelligent surfaces," *IEEE Wireless Commun.*, vol. 29, no. 1, pp. 202–208, 2022.
- [24] Reconfigurable intelligent surfaces (RIS); technological challenges, architecture and impact on standardization. ETSI GR RIS 002-V1.2.1. [Online]. Available: https://www.etsi.org/deliver/etsi gr/RIS/001 099/ 002/01.02.01 60/gr ris002v010201p.pdf
- [25] H. Li, S. Shen, M. Nerini, and B. Clerckx, "Reconfigurable intelligent surfaces 2.0: Beyond diagonal phase shift matrices," *IEEE Commun. Mag.*, vol. 62, no. 3, pp. 102–108, 2024.
- [26] S. Shen, B. Clerckx, and R. Murch, "Modeling and architecture design of reconfigurable intelligent surfaces using scattering parameter network analysis," *IEEE Trans. Wireless Commun.*, vol. 21, no. 2, pp. 1229–1243, 2021.
- [27] C. Madapatha, B. Makki, C. Fang, O. Teyeb, E. Dahlman, M.- S. Alouini, and T. Svensson, "On integrated access and backhaul networks: Current status and potentials," *IEEE Open J. Commun. Soc.*, vol. 1, pp. 1374–1389, 2020.
- [28] T. D. P. Perera, D. N. K. Jayakody, S. K. Sharma, S. Chatzinotas, and J. Li, "Simultaneous wireless information and power transfer (SWIPT): Recent advances and future challenges," *IEEE Commun. Surveys & Tuts.*, vol. 20, no. 1, pp. 264–302, 2017.
- [29] M. Hua, Q. Wu, W. Chen, O. A. Dobre, and A. L. Swindlehurst, "Secure intelligent reflecting surface-aided integrated sensing and communication," *IEEE Trans. Wireless Commun.*, vol. 23, no. 1, pp. 575– 591, 2023.
- [30] Z. Zhou, X. Li, G. Zhu, J. Xu, K. Huang, and S. Cui, "Integrating sensing, communication, and power transfer: Multiuser beamforming design," *IEEE J. Sel. Areas Commun.*, 2024.
- [31] W. U. Khan, A. Mahmood, M. A. Jamshed, E. Lagunas, M. Ahmed, and S. Chatzinotas, "Beyond diagonal RIS for 6G non-terrestrial networks: Potentials and challenges," *IEEE Network*, 2024.
- [32] W. U. Khan, E. Lagunas, A. Mahmood, M. Asif, M. Ahmed, and S. Chatzinotas, "Integration of beyond diagonal RIS and UAVs in 6G NTNs: Enhancing aerial connectivity," *IEEE Wireless Commun.*, vol. 32, no. 3, pp. 56–63, 2025.
- [33] W. U. Khan, C. K. Sheemar, E. Lagunas, and S. Chatzinotas, "Beyond diagonal RIS: A new frontier for 6G internet of things networks," *arXiv:2502.03637*, 2025.
- [34] D. M. Pozar, *Microwave engineering: theory and techniques*. John wiley & sons, 2021.
- [35] J. W. Wallace and M. A. Jensen, "Mutual coupling in MIMO wireless systems: A rigorous network theory analysis," *IEEE Trans. Wireless Commun.*, vol. 3, no. 4, pp. 1317–1325, 2004.
- [36] ——, "Termination-dependent diversity performance of coupled antennas: Network theory analysis," *IEEE Trans. Antennas Propag.*, vol. 52, no. 1, pp. 98–105, 2004.
- [37] M. L. Morris and M. A. Jensen, "Network model for MIMO systems with coupled antennas and noisy amplifiers," *IEEE Trans. Antennas Propag.*, vol. 53, no. 1, pp. 545–552, 2005.
- [38] M. Nerini, S. Shen, H. Li, M. Di Renzo, and B. Clerckx, "A universal framework for multiport network analysis of reconfigurable intelligent surfaces," *IEEE Trans. Wireless Commun.*, vol. 23, no. 10, pp. 14 575– 14 590, 2024.
- [39] J. A. Nossek, D. Semmler, M. Joham, and W. Utschick, "Physically consistent modelling of wireless links with reconfigurable intelligent surfaces using multiport network analysis," *IEEE Wireless Commun. Lett.*, 2024.

- [40] H. Li, S. Shen, and B. Clerckx, "Beyond diagonal reconfigurable intelligent surfaces: From transmitting and reflecting modes to single- , group-, and fully-connected architectures," *IEEE Trans. Wireless Commun.*, vol. 22, no. 4, pp. 2311–2324, 2022.
- [41] H. Zhang and B. Di, "Intelligent omni-surfaces: Simultaneous refraction and reflection for full-dimensional wireless communications," *IEEE Commun. Surveys & Tut.*, vol. 24, no. 4, pp. 1997–2028, 2022.
- [42] H. Li, S. Shen, and B. Clerckx, "Beyond diagonal reconfigurable intelligent surfaces: A multi-sector mode enabling highly directional full-space wireless coverage," *IEEE J. Sel. Areas Commun.*, vol. 41, no. 8, pp. 2446–2460, 2023.
- [43] J. A. Bondy and U. S. R. Murty, *Graph theory*. Springer Publishing Company, Incorporated, 2008.
- [44] M. Nerini, S. Shen, H. Li, and B. Clerckx, "Beyond diagonal reconfigurable intelligent surfaces utilizing graph theory: Modeling, architecture design, and optimization," *IEEE Trans. Wireless Commun.*, 2024.
- [45] Z. Wu and B. Clerckx, "Beyond diagonal RIS in multiuser MIMO: Graph theoretic modeling and optimal architectures with low complexity," *arXiv:2502.16509*, 2025.
- [46] X. Zhou, T. Fang, and Y. Mao, "A novel Q-stem connected architecture for beyond-diagonal reconfigurable intelligent surfaces," *arXiv:2411.18480*, 2024.
- [47] H. Li, S. Shen, and B. Clerckx, "A dynamic grouping strategy for beyond diagonal reconfigurable intelligent surfaces with hybrid transmitting and reflecting mode," *IEEE Trans. Veh. Technol.*, vol. 72, no. 12, pp. 16 748–16 753, 2023.
- [48] M. Nerini, S. Shen, and B. Clerckx, "Static grouping strategy design for beyond diagonal reconfigurable intelligent surfaces," *IEEE Commun. Lett.*, 2024.
- [49] Q. Li, M. El-Hajjar, I. A. Hemadeh, A. Shojaeifard, A. Mourad, B. Clerckx, and L. Hanzo, "Reconfigurable intelligent surfaces relying on non-diagonal phase shift matrices," *IEEE Trans. Veh. Technol.*, vol. 71, no. 6, pp. 6367–6383, 2022.
- [50] Q. Li, M. El-Hajjar, I. Hemadeh, A. Shojaeifard, and L. Hanzo, "Coordinated reconfigurable intelligent surfaces: Non-diagonal groupconnected design," *IEEE Trans. Veh. Technol.*, 2024.
- [51] J. Xu, H. Wang, R. Liu, J. A. Nossek, and A. L. Swindlehurst, "Nonreciprocal reconfigurable intelligent surfaces," *arXiv:2411.15617*, 2024.
- [52] R. De Francisco and D. T. Slock, "An optimized unitary beamforming technique for mimo broadcast channels," *IEEE Trans. Wireless Commun.*, vol. 9, no. 3, pp. 990–1000, 2010.
- [53] J. M. Lee, *Introduction to Riemannian manifolds*. Springer, 2018, vol. 2.
- [54] Y. Zhao, H. Li, M. Franceschetti, and B. Clerckx, "Channel shaping using beyond diagonal reconfigurable intelligent surface: Analysis, optimization, and enhanced flexibility," *arXiv:2407.15196*, 2024.
- [55] M. Nerini, S. Shen, and B. Clerckx, "Closed-form global optimization of beyond diagonal reconfigurable intelligent surfaces," *IEEE Trans. Wireless Commun.*, vol. 23, no. 2, pp. 1037–1051, 2023.
- [56] W. Sun, S. Sun, T. Shi, X. Su, and R. Liu, "A new model of beyond diagonal reconfigurable intelligent surfaces (BD-RIS) for the corresponding quantization and optimization," *IEEE Trans. Wireless Commun.*, 2024.
- [57] I. Santamaria, M. Soleymani, E. Jorswieck, and J. Gutierrez, "SNR ´ maximization in beyond diagonal RIS-assisted single and multiple antenna links," *IEEE Signal Process. Lett.*, vol. 30, pp. 923–926, 2023.
- [58] T. Fang and Y. Mao, "A low-complexity beamforming design for beyond-diagonal RIS aided multi-user networks," *IEEE Commun. Lett.*, vol. 28, no. 1, pp. 203–207, 2023.
- [59] J. H. Manton, "Optimization algorithms exploiting unitary constraints," *IEEE Trans. Signal Process.*, vol. 50, no. 3, pp. 635–650, 2002.
- [60] Y. Zhou, Y. Liu, H. Li, Q. Wu, S. Shen, and B. Clerckx, "Optimizing power consumption, energy efficiency and sum-rate using beyond diagonal RIS–A unified approach," *IEEE Trans. Wireless Commun.*, 2023.
- [61] Z. Wu and B. Clerckx, "Optimization of beyond diagonal RIS: A universal framework applicable to arbitrary architectures," *arXiv:2412.15965*, 2024.
- [62] Y. Dong, Q. Li, S. X. Ng, and M. El-Hajjar, "Reconfigurable intelligent surface relying on low-complexity joint sector non-diagonal structure," *IEEE Open J. Veh. Technol.*, 2024.
- [63] I. Santamaria, M. Soleymani, E. Jorswieck, and J. Gutierrez, "MIMO ´ capacity maximization with beyond-diagonal RIS," in *IEEE 25th Int. Workshop on Signal Process. Advances in Wireless Commun. (SPAWC)*. IEEE, 2024, pp. 936–940.

- [64] I. Santamaria, J. Gutierrez, M. Soleymani, and E. Jorswieck, "Rate analysis and optimization of LoS beyond diagonal RIS-assisted MIMO systems," *arXiv:2504.07647*, 2025.
- [65] G. Bartoli, A. Abrardo, N. Decarli, D. Dardari, and M. Di Renzo, "Spatial multiplexing in near field MIMO channels with reconfigurable intelligent surfaces," *IET Signal Processing*, vol. 17, no. 3, p. e12195, 2023.
- [66] E. Bjornson and ¨ O. T. Demir, "Capacity maximization for MIMO ¨ channels assisted by beyond-diagonal RIS," *arXiv:2411.18298*, 2024.
- [67] S. P. Boyd and L. Vandenberghe, *Convex optimization*. Cambridge university press, 2004.
- [68] X. Zhou, T. Fang, and Y. Mao, "Joint active and passive beamforming optimization for beyond diagonal RIS-aided multi-user communications," *IEEE Commun. Lett.*, 2025.
- [69] M.-A. Kim, S.-G. Yoo, H.-D. Kim, K.-H. Shin, and H.-K. Song, "Scattering matrix design of reconfigurable intelligent surface based on group connected impedance network in MU-MIMO system," in *Fourteenth Int. Conf. Ubiquitous and Future Networks (ICUFN)*. IEEE, 2023, pp. 642–645.
- [70] M. Samy, A. B. Adam, K. Ntontin, H. Al-Hraishawi, S. Chatzinotas, and B. Otteresten, "Enhancing spectral and energy efficiency with multi-sector beyond-diagonal RIS," in *IEEE 25th Int. Workshop on Signal Process. Advances in Wireless Commun. (SPAWC)*. IEEE, 2024, pp. 941–945.
- [71] M. Samy, H. Al-Hraishawi, A. B. Adam, S. Chatzinotas, and B. Otteresten, "Beyond diagonal RIS-aided networks: Performance analysis and sectorization tradeoff," *IEEE Open J. Commun. Soc.*, 2024.
- [72] S. Sobhi-Givi, M. Nouri, H. Behroozi, and Z. Ding, "Joint BS and beyond diagonal RIS beamforming design with DRL methods for mmWave 6G mobile communications," in *IEEE Wireless Commun. and Network. Conf. (WCNC)*. IEEE, 2024, pp. 1–6.
- [73] R. C. Loli and B. Clerckx, "Meta-learning based optimization for large scale wireless systems," *arXiv:2407.01823*, 2024.
- [74] A. Farhadi, R. Hatami, M. R. Mili, C. Masouros, and M. Bennis, "A meta-learning approach for energy-efficient resource allocation and antenna selection in STAR-BD-RIS aided wireless networks," *IEEE Wireless Commun. Lett.*, 2025.
- [75] X. Hu, R. Zhang, and C. Zhong, "Semi-passive elements assisted channel estimation for intelligent reflecting surface-aided communications," *IEEE Trans. Wireless Commun.*, vol. 21, no. 2, pp. 1132–1142, 2021.
- [76] G. C. Alexandropoulos and E. Vlachos, "A hardware architecture for reconfigurable intelligent surfaces with minimal active elements for explicit channel estimation," in *IEEE Int. Conf. Acoustics, Speech and Signal process. (ICASSP)*. IEEE, 2020, pp. 9175–9179.
- [77] A. Taha, M. Alrabeiah, and A. Alkhateeb, "Deep learning for large intelligent surfaces in millimeter wave and massive MIMO systems," in *IEEE Global Commun. Conf. (GLOBECOM)*. IEEE, 2019, pp. 1–6.
- [78] Y. Yang, B. Zheng, S. Zhang, and R. Zhang, "Intelligent reflecting surface meets OFDM: Protocol design and rate maximization," *IEEE Trans. Commun.*, vol. 68, no. 7, pp. 4522–4535, 2020.
- [79] B. Zheng and R. Zhang, "Intelligent reflecting surface-enhanced OFDM: Channel estimation and reflection optimization," *IEEE Wireless Commun. Lett.*, vol. 9, no. 4, pp. 518–522, 2019.
- [80] C. You, B. Zheng, and R. Zhang, "Channel estimation and passive beamforming for intelligent reflecting surface: Discrete phase shift and progressive refinement," *IEEE J. Sel. Areas Commun.*, vol. 38, no. 11, pp. 2604–2620, 2020.
- [81] Z. Wang, L. Liu, and S. Cui, "Channel estimation for intelligent reflecting surface assisted multiuser communications: Framework, algorithms, and analysis," *IEEE Trans. Wireless Commun.*, vol. 19, no. 10, pp. 6607–6620, 2020.
- [82] X. Guan, Q. Wu, and R. Zhang, "Anchor-assisted channel estimation for intelligent reflecting surface aided multiuser communication," *IEEE Trans. Wireless Commun.*, vol. 21, no. 6, pp. 3764–3778, 2021.
- [83] G. Zhou, C. Pan, H. Ren, P. Popovski, and A. L. Swindlehurst, "Channel estimation for RIS-aided multiuser millimeter-wave systems," *IEEE Trans. Signal Process.*, vol. 70, pp. 1478–1492, 2022.
- [84] H. Li, Y. Zhang, and B. Clerckx, "Channel estimation for beyond diagonal reconfigurable intelligent surfaces with group-connected architectures," in *IEEE Int. Workshop Computational Advances in Multi-Sensor Adaptive Process. (CAMSAP)*. IEEE, 2023, pp. 21–25.
- [85] H. Li, S. Shen, Y. Zhang, and B. Clerckx, "Channel estimation and beamforming for beyond diagonal reconfigurable intelligent surfaces," *IEEE Trans. Signal Process.*, 2024.
- [86] R. Wang, S. Zhang, and L. Liu, "Low-overhead channel estimation for beyond diagonal reconfigurable intelligent surface aided single-

- user communication," in *Int. Conf. Wireless Commun. Signal Process. (WCSP)*. IEEE, 2024, pp. 305–310.
- [87] R. Wang, S. Zhang, B. Clerckx, and L. Liu, "Low-overhead channel estimation framework for beyond diagonal reconfigurable intelligent surface assisted multi-user MIMO communication," *arXiv:2504.10911*, 2025.
- [88] M. Samy, H. Al-Hraishawi, A. Adam, M. Alsenwi, S. Chatzinotas, and B. Otteresten, "Low-complexity channel estimation protocol for non-diagonal RIS-assisted communications," *arXiv:2504.19791*, 2025.
- [89] B. Sokal, A. L. de Almeida, H. Li, B. Clerckx *et al.*, "A decoupled channel estimation method for beyond diagonal RIS," *arXiv:2412.06683*, 2024.
- [90] A. L. de Almeida, B. Sokal, H. Li, and B. Clerckx, "Channel estimation for beyond diagonal RIS via tensor decomposition," *arXiv:2407.20402*, 2024.
- [91] N. Ginige, A. S. de Sena, N. H. Mahmood, N. Rajatheva, and M. Latvaaho, "Efficient channel prediction for beyond diagonal RIS-assisted MIMO systems with channel aging," *arXiv:2411.17725*, 2024.
- [92] G. T. de Araujo and A. L. de Almeida, "Semi-blind channel estimation ´ for beyond diagonal RIS," in *58th Asilomar Conf. Signals, Syst., and Computers*. IEEE, 2024, pp. 1586–1590.
- [93] M. Nerini and B. Clerckx, "Pareto frontier for the performancecomplexity trade-off in beyond diagonal reconfigurable intelligent surfaces," *IEEE Commun. Lett.*, vol. 27, no. 10, pp. 2842–2846, 2023.
- [94] M. Nerini, G. Ghiaasi, and B. Clerckx, "Localized and distributed beyond diagonal reconfigurable intelligent surfaces with lossy interconnections: Modeling and optimization," *IEEE Trans. Commun.*, 2025.
- [95] Z. Zhang, K. Long, A. V. Vasilakos, and L. Hanzo, "Full-duplex wireless communications: Challenges, solutions, and future research directions," *Proc. IEEE*, vol. 104, no. 7, pp. 1369–1409, 2016.
- [96] H. Li and B. Clerckx, "Non-reciprocal beyond diagonal RIS: Multiport network models and performance benefits in full-duplex systems," *IEEE Trans. Commun.*, 2025.
- [97] Z. Liu, H. Li, and B. Clerckx, "Non-reciprocal beyond diagonal RIS: Sum-rate maximization in full-duplex communications," *arXiv:2411.18523*, 2024.
- [98] T. Kim, B. Clerckx, D. J. Love, and S. J. Kim, "Limited feedback beamforming systems for dual-polarized MIMO channels," *IEEE Trans. wireless Commun.*, vol. 9, no. 11, pp. 3425–3439, 2010.
- [99] Y. Han, X. Li, W. Tang, S. Jin, Q. Cheng, and T. J. Cui, "Dual-polarized RIS-assisted mobile communications," *IEEE Trans. Wireless Commun.*, vol. 21, no. 1, pp. 591–606, 2021.
- [100] Z. Zheng, H. Huang, H. Zhang, and A. L. Swindlehurst, "RIS-aided dual-polarized MIMO: How large a surface is needed to beat single polarization?" *IEEE Commun. Lett.*, 2024.
- [101] M. Nerini and B. Clerckx, "Dual-polarized beyond diagonal RIS," *IEEE Commun. Lett.*, 2025.
- [102] M. Nerini, S. Shen, and B. Clerckx, "Discrete-value group and fully connected architectures for beyond diagonal reconfigurable intelligent surfaces," *IEEE Tran. Veh. Technol.*, vol. 72, no. 12, pp. 16 354–16 368, 2023.
- [103] M. Sabin and R. Gray, "Global convergence and empirical consistency of the generalized lloyd algorithm," *IEEE Trans. Info. Theory*, vol. 32, no. 2, pp. 148–155, 1986.
- [104] Y. Peng, H. Li, Z. Wu, and B. Clerckx, "Lossy beyond diagonal reconfigurable intelligent surfaces: Modeling and optimization," *arXiv:2504.19744*, 2025.
- [105] Q. Hu, H. Yang, X. Zeng, and X. Y. Zhang, "Wideband reconfigurable intelligent surface using dual-resonance element," *IEEE Antennas Wireless Propaga. Lett.*, vol. 22, no. 10, pp. 2422–2426, 2023.
- [106] Z. Zhang and L. Dai, "A joint precoding framework for wideband reconfigurable intelligent surface-aided cell-free network," *IEEE Trans. Signal Process.*, vol. 69, pp. 4085–4101, 2021.
- [107] R. Wang, Y. Yang, B. Makki, and A. Shamim, "A wideband reconfigurable intelligent surface for 5G millimeter-wave applications," *IEEE Trans. Antennas Propaga.*, vol. 72, no. 3, pp. 2399–2410, 2024.
- [108] M. Soleymani, I. Santamaria, A. Sezgin, and E. Jorswieck, "Maximizing spectral and energy efficiency in multi-user MIMO OFDM systems with RIS and hardware impairment," *arXiv:2401.11921*, 2024.
- [109] O. T. Demir and E. Bj ¨ ornson, "Wideband channel capacity maximiza- ¨ tion with beyond diagonal RIS reflection matrices," *IEEE Wireless Commun. Lett.*, 2024.
- [110] H. Li, M. Nerini, S. Shen, and B. Clerckx, "Beyond diagonal reconfigurable intelligent surfaces in wideband OFDM communications: Circuit-based modeling and optimization," *IEEE Trans. Wireless Commun.*, 2025.

- [111] A. S. De Sena, M. Rasti, N. H. Mahmood, and M. Latva-Aho, "Beyond diagonal RIS for multi-band multi-cell MIMO networks: A practical frequency-dependent model and performance analysis," *IEEE Trans. Wireless Commun.*, 2024.
- [112] K. D. Katsanos, P. Di Lorenzo, and G. C. Alexandropoulos, "Multi-RIS-empowered multiple access: A distributed sum-rate maximization approach," *IEEE J. Sel. Topics Signal Process.*, 2024.
- [113] M. Di Renzo, F. H. Danufane, and S. Tretyakov, "Communication models for reconfigurable intelligent surfaces: From surface electromagnetics to wireless networks optimization," *Proc. IEEE*, vol. 110, no. 9, pp. 1164–1209, 2022.
- [114] X. Qian and M. Di Renzo, "Mutual coupling and unit cell aware optimization for reconfigurable intelligent surfaces," *IEEE Wireless Commun. Lett.*, vol. 10, no. 6, pp. 1183–1187, 2021.
- [115] M. Akrout, F. Bellili, A. Mezghani, and J. A. Nossek, "Physically consistent models for intelligent reflective surface-assisted communications under mutual coupling and element size constraint," in *57th Asilomar Conf. Signals, Systems, and Computers*. IEEE, 2023, pp. 1589–1594.
- [116] H. Li, S. Shen, M. Nerini, M. Di Renzo, and B. Clerckx, "Beyond diagonal reconfigurable intelligent surfaces with mutual coupling: Modeling and optimization," *IEEE Commun. Lett.*, vol. 28, no. 4, pp. 937–941, 2024.
- [117] D. Semmler, J. A. Nossek, M. Joham, B. Bock, and W. Utschick, ¨ "Decoupling networks and super-quadratic gains for RIS systems with mutual coupling," *arXiv:2411.17779*, 2024.
- [118] M. Nerini, H. Li, and B. Clerckx, "Global optimal closed-form solutions for intelligent surfaces with mutual coupling: Is mutual coupling detrimental or beneficial?" *arXiv:2411.04949*, 2024.
- [119] M. Nerini, G. Gradoni, and B. Clerckx, "Physics-compliant modeling and scaling laws of multi-RIS aided MIMO systems," *arXiv:2411.06309*, 2024.
- [120] P. Del Hougne, "A physics-compliant diagonal representation for wireless channels parametrized by beyond-diagonal reconfigurable intelligent surfaces," *IEEE Trans. Wireless Commun.*, 2025.
- [121] D. Wijekoon, A. Mezghani, G. C. Alexandropoulos, and E. Hossain, "Physically-consistent modeling and optimization of nonlocal RIS-assisted multi-user MIMO communication systems," *arXiv:2406.05617*, 2024.
- [122] Z. Wu, M. Nerini, and B. Clerckx, "Beyond-diagonal RIS architecture design and optimization under physics-consistent models," *arXiv:2510.12366*, 2025.
- [123] B. Zhou and B. Clerckx, "Beyond-diagonal RIS under nonidealities: Learning-based architecture discovery and optimization," *arXiv:2510.15701*, 2025.
- [124] H. Yahya, H. Li, M. Nerini, B. Clerckx, and M. Debbah, "Beyond diagonal RIS: Passive maximum ratio transmission and interference nulling enabler," *IEEE Open J. Commun. Soc.*, 2024.
- [125] I. Santamaria, M. Soleymani, E. Jorswieck, and J. Gutierrez, "Interfer- ´ ence minimization in beyond-diagonal RIS-assisted MIMO interference channels," *IEEE Open J. Veh. Technol.*, 2025.
- [126] A. Agarwal and K. Singh, "Enhanced physical layer security for wireless systems with non-diagonal IRS," in *IEEE Int. Conf. Advanced Networks and Telecommun. Syst. (ANTS)*. IEEE, 2023, pp. 1–6.
- [127] Z. Liu and B. Clerckx, "A secure full-duplex wireless circulator enabled by non-reciprocal beyond-diagonal ris," *arXiv:2507.23381*, 2025.
- [128] H. Wang, Z. Han, and A. L. Swindlehurst, "Channel reciprocity attacks using intelligent surfaces with non-diagonal phase shifts," *IEEE Open J. Commun. Soc.*, 2024.
- [129] H. Wang, J. Nossek, and A. L. Swindlehurst, "Beyond-diagonal RIS attacks on physical layer key generation," in *IEEE 25th Int. Workshop Signal Process. Advances Wireless Commun. (SPAWC)*. IEEE, 2024, pp. 946–950.
- [130] A. Mahmood, T. X. Vu, S. Chatzinotas, and B. Ottersten, "Enhancing indoor and outdoor THz communications with Beyond Diagonal-IRS: Optimization and performance analysis," in *IEEE Int. Symp. Personal, Indoor and Mobile Radio Commun. (PIMRC)*. IEEE, 2024, pp. 1–6.
- [131] A. Mishra, Y. Mao, C. DAndrea, S. Buzzi, and B. Clerckx, "Transmitter side beyond-diagonal reconfigurable intelligent surface for massive MIMO networks," *IEEE Wireless Commun. Lett.*, vol. 13, no. 2, pp. 352–356, 2023.
- [132] M. Raeisi, H. Chen, H. Wymeersch, and E. Basar, "Modern base station architecture: Enabling passive beamforming with beyond diagonal RISs," *arXiv:2501.15382*, 2025.
- [133] Y. Li, J. Zheng, B. Xu, Y. Zhu, J. Zhang, and B. Ai, "Beamforming design for beyond diagonal RIS-aided cell-free massive MIMO systems," *arXiv:2503.07189*, 2025.

- [134] Y. Zhang, X. Shao, H. Li, B. Clerckx, and R. Zhang, "Full-space wireless sensing enabled by multi-sector intelligent surfaces," *IEEE Trans. Wireless Commun.*, 2025.
- [135] M. Raeisi, H. Chen, H. Wymeersch, and E. Basar, "Efficient localization with base station-integrated beyond diagonal RIS," *arXiv:2411.13295*, 2024.
- [136] B. Wang, H. Li, S. Shen, Z. Cheng, and B. Clerckx, "A dualfunction radar-communication system empowered by beyond diagonal reconfigurable intelligent surface," *IEEE Trans. Commun.*, 2024.
- [137] T. Esmaeilbeig, K. V. Mishra, and M. Soltanalian, "Beyond diagonal RIS: Key to next-generation integrated sensing and communications?" *IEEE Signal Process. Lett.*, 2024.
- [138] Z. Guang, Y. Liu, Q. Wu, W. Wang, and Q. Shi, "Power minimization for ISAC system using beyond diagonal reconfigurable intelligent surface," *IEEE Trans. Veh. Technol.*, 2024.
- [139] Z. Liu, Y. Liu, S. Shen, Q. Wu, and Q. Shi, "Enhancing ISAC network throughput using beyond diagonal RIS," *IEEE Wireless Commun. Lett.*, 2024.
- [140] K. Chen and Y. Mao, "Transmitter side beyond-diagonal RIS for mmwave integrated sensing and communications," in *IEEE Int. Workshop Signal Process. Advances Wireless Commun. (SPAWC)*. IEEE, 2024, pp. 951–955.
- [141] T. L. Nguyen, G. Kaddoum, B. Selim, and C. Assi, "Beyond diagonal RIS for ISAC network: Statistical analysis and network parameter estimation," *arXiv:2502.12916*, 2025.
- [142] A. Azarbahram, O. L. Lopez, B. Clerckx, M. Di Renzo, and M. Latva- ´ aho, "Beyond diagonal reconfigurable intelligent surfaces for multicarrier RF wireless power transfer," *arXiv:2501.01787*, 2025.
- [143] A. Azarbahram, O. L. Lopez, B. Clerckx, M. Di Renzo, and M. Latva-Aho, "Beamforming and waveform optimization for RF wireless power transfer with beyond diagonal reconfigurable intelligent surfaces," *arXiv:2502.19176*, 2025.
- [144] T. D. Hua, M. Mohammadi, H. Q. Ngo, and M. Matthaiou, "Cell-free massive MIMO SWIPT with beyond diagonal reconfigurable intelligent surfaces," in *IEEE Wireless Commun. Network. Conf. (WCNC)*. IEEE, 2024, pp. 1–6.
- [145] M. Nerini and B. Clerckx, "Physically consistent modeling of stacked intelligent metasurfaces implemented with beyond diagonal RIS," *IEEE Commun. Lett.*, 2024.
- [146] Q. Zhang, G. Luo, Z. Dong, F. Sun, X. Wang, and J. Liu, "Beyonddiagonal reconfigurable intelligent surface enhanced NOMA systems," *IEEE Wireless Commun. Lett.*, 2024.
- [147] A. Agarwal *et al.*, "Fairness driven joint phase and PAC optimization for NOMA transmission with D/ND-IRS," *IEEE Trans. Veh. Technol.*, 2025.
- [148] T. Fang, Y. Mao, S. Shen, Z. Zhu, and B. Clerckx, "Fully connected reconfigurable intelligent surface aided rate-splitting multiple access for multi-user multi-antenna transmission," in *IEEE Int. Conf. Commun.Workshops (ICC Workshops)*. IEEE, 2022, pp. 675–680.
- [149] M.-A. Kim, S.-G. Yoo, H.-D. Kim, K.-H. Shin, Y.-H. You, and H.-K. Song, "Group-connected impedance network of RIS-assisted rate-splitting multiple access in MU-MIMO wireless communication systems," *Sensors*, vol. 23, no. 8, p. 3934, 2023.
- [150] S. Khisa, A. Amhaz, M. Elhattab, C. Assi, and S. Sharafeddine, "Gradient-based meta learning for uplink RSMA with beyond diagonal RIS," *arXiv:2410.17896*, 2024.
- [151] M. Soleymani, I. Santamaria, E. A. Jorswieck, and B. Clerckx, "Optimization of rate-splitting multiple access in beyond diagonal RISassisted URLLC systems," *IEEE Trans. Wireless Commun.*, vol. 23, no. 5, pp. 5063–5078, 2023.
- [152] H. Li, S. Shen, and B. Clerckx, "Synergizing beyond diagonal reconfigurable intelligent surface and rate-splitting multiple access," *IEEE Trans. Wireless Commun.*, vol. 23, no. 8, pp. 8717–8729, 2024.
- [153] A. M. Huroon, Y.-C. Huang, and L.-C. Wang, "Optimized transmission strategy for UAV-RIS 2.0 assisted communications using rate splitting multiple access," in *IEEE Veh. Technol. Conf. (VTC2023-Fall)*. IEEE, 2023, pp. 1–6.
- [154] A. Mahmood, T. X. Vu, W. U. Khan, S. Chatzinotas, and B. Ottersten, "Joint computation and communication resource optimization for beyond diagonal UAV-IRS empowered MEC networks," *arXiv:2311.07199*, 2023.
- [155] S. Lin, Y. Zou, Y. Jiang, L. Yang, Z. Cui, and L.-N. Tran, "Securing FC-RIS and UAV empowered multiuser communications against a randomly flying eavesdropper," *IEEE Wireless Commun. Lett.*, 2024.
- [156] W. U. Khan, C. K. Sheemar, E. Lagunas, and S. Chatzinotas, "Enhancing physical layer security in cognitive radio-enabled NTNs with beyond diagonal RIS," *arXiv:2503.15787*, 2025.

- [157] ——, "Beyond diagonal RIS enhanced cognitive radio enabled multilayer non-terrestrial networks," *arXiv:2503.10866*, 2025.
- [158] X. Qin, W. Yu, Q. Ni, Z. Song, T. Hou, and X. Sun, "Joint resource allocation and beamforming design for BD-RIS-assisted wirelesspowered cooperative mobile edge computing," *IEEE Commun. Lett.*, 2025.
- [159] I. F. Akyildiz, C. Han, Z. Hu, S. Nie, and J. M. Jornet, "Terahertz band communication: An old problem revisited and research directions for the next decade," *IEEE Trans. Commun.*, vol. 70, no. 6, pp. 4250–4285, 2022.
- [160] E. Bjornson, J. Hoydis, L. Sanguinetti ¨ *et al.*, "Massive MIMO networks: Spectral, energy, and hardware efficiency," *Found. Trends® Signal Process.*, vol. 11, no. 3-4, pp. 154–655, 2017.
- [161] O. L. Lopez, H. Alves, R. D. Souza, S. Montejo-S ´ anchez, E. M. G. ´ Fernandez, and M. Latva-Aho, "Massive wireless energy transfer: ´ Enabling sustainable IoT toward 6G era," *IEEE Int. Things J.*, vol. 8, no. 11, pp. 8816–8835, 2021.
- [162] J. An, C. Xu, D. W. K. Ng, G. C. Alexandropoulos, C. Huang, C. Yuen, and L. Hanzo, "Stacked intelligent metasurfaces for efficient holographic MIMO communications in 6G," *IEEE J. Sel. Areas Commun.*, vol. 41, no. 8, pp. 2380–2396, 2023.
- [163] Y. Liu, Z. Qin, M. Elkashlan, Z. Ding, A. Nallanathan, and L. Hanzo, "Nonorthogonal multiple access for 5G and beyond," *Proceed. IEEE*, vol. 105, no. 12, pp. 2347–2381, 2017.
- [164] Y. Mao, O. Dizdar, B. Clerckx, R. Schober, P. Popovski, and H. V. Poor, "Rate-splitting multiple access: Fundamentals, survey, and future research trends," *IEEE Commun. Surveys & Tuts.*, vol. 24, no. 4, pp. 2073–2126, 2022.
- [165] L. Gupta, R. Jain, and G. Vaszkun, "Survey of important issues in UAV communication networks," *IEEE Commun. surveys & Tuts.*, vol. 18, no. 2, pp. 1123–1152, 2015.
- [166] M. M. Azari, S. Solanki, S. Chatzinotas, O. Kodheli, H. Sallouha, A. Colpaert, J. F. M. Montoya, S. Pollin, A. Haqiqatnejad, A. Mostaani *et al.*, "Evolution of non-terrestrial networks from 5G to 6G: A survey," *IEEE Commun. Surveys & Tuts.*, vol. 24, no. 4, pp. 2633–2672, 2022.
- [167] G. Chen, Q. Wu, R. Liu, J. Wu, and C. Fang, "IRS aided MEC systems with binary offloading: A unified framework for dynamic IRS beamforming," *IEEE J. Sel. Areas Commun.*, vol. 41, no. 2, pp. 349– 365, 2022.
- [168] Z. Ming, S. Shen, J. Rao, Z. Li, J. Zhang, C. Y. Chiu, and R. Murch, "A hybrid transmitting and reflecting beyond diagonal reconfigurable intelligent surface with independent beam control and power splitting," *arXiv:2504.09618*, 2025.
- [169] J. Tapie, M. Nerini, B. Clerckx, and P. del Hougne, "Beyond-diagonal RIS prototype and performance evaluation," *arXiv:2505.13392*, 2025.
- [170] J. Wang, W. Tang, J. C. Liang, L. Zhang, J. Y. Dai, X. Li, S. Jin, Q. Cheng, and T. J. Cui, "Reconfigurable intelligent surface: Power consumption modeling and practical measurement validation," *IEEE Trans. Commun.*, vol. 72, no. 9, pp. 5720–5734, 2024.
- [171] K. Zhi, C. Pan, H. Ren, K. K. Chai, and M. Elkashlan, "Active RIS versus passive RIS: Which is superior with the same power budget?" *IEEE Commun. Lett.*, vol. 26, no. 5, pp. 1150–1154, 2022.
- [172] Q. Zhu, M. Li, R. Liu, and Q. Liu, "Joint transceiver beamforming and reflecting design for active RIS-aided ISAC systems," *IEEE Trans. Veh. Technol.*, vol. 72, no. 7, pp. 9636–9640, 2023.
- [173] Y. C. Eldar, A. Goldsmith, D. Gund ¨ uz, and H. V. Poor, ¨ *Machine learning and wireless communications*. Cambridge University Press, 2022.
- [174] C. Jiang, H. Zhang, Y. Ren, Z. Han, K.-C. Chen, and L. Hanzo, "Machine learning paradigms for next-generation wireless networks," *IEEE Wireless Commun.*, vol. 24, no. 2, pp. 98–105, 2016.
- [175] A. F. Molisch, *Wireless communications*. John Wiley & Sons, 2012, vol. 34.
- [176] X. Mu, J. Xu, Y. Liu, and L. Hanzo, "Reconfigurable intelligent surface-aided near-field communications for 6G: Opportunities and challenges," *IEEE Veh. Technol. Mag.*, vol. 19, no. 1, pp. 65–74, 2024.
- [177] P. Wang, J. Fang, W. Zhang, Z. Chen, H. Li, and W. Zhang, "Beam training and alignment for RIS-assisted millimeter-wave systems: State of the art and beyond," *IEEE Wireless Commun.*, vol. 29, no. 6, pp. 64–71, 2022.
- [178] W. Liu, C. Pan, H. Ren, F. Shu, S. Jin, and J. Wang, "Low-overhead beam training scheme for extremely large-scale RIS in near field," *IEEE Trans. Commun.*, vol. 71, no. 8, pp. 4924–4940, 2023.
- [179] F. Ait Aoudia and J. Hoydis, "Model-free training of end-to-end communication systems," *IEEE J. Sel. Areas Commun.*, vol. 37, no. 11, pp. 2503–2516, 2019.