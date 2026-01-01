# <span id="page-0-0"></span>Beam Pattern Modulation Embedded Hybrid Transceiver Optimization for Integrated Sensing and Communication

Boxun Li[u](https://orcid.org/0000-0002-2182-2287) , *Graduate Student Member, IEEE*, Shijian Gao [,](https://orcid.org/0000-0002-8105-7927) *Member, IEEE*, Zonghui Yan[g](https://orcid.org/0009-0009-6946-451X) , *Graduate Student Member, IEEE*, Xiang Cheng [,](https://orcid.org/0000-0002-5943-0326) *Fellow, IEEE*, and Liuqing Yang [,](https://orcid.org/0000-0003-0231-6837) *Fellow, IEEE*

*Abstract*— Integrated sensing and communication (ISAC) emerges as a promising technology for 6G, particularly in the millimeter-wave (mmWave) band. However, the widely utilized hybrid architecture in mmWave systems compromises multiplexing gain due to the constraints of limited radio-frequency (RF) chains. Moreover, additional sensing functionalities exacerbate the impairment of spectrum efficiency (SE). In this paper, we present an optimized beam pattern modulation-embedded ISAC (BPM-ISAC) transceiver design, which spares one RF chain for sensing and uses the remaining ones for communication. To compensate for the reduced SE, index modulation across communication beams is applied. We formulate an optimization problem aimed at minimizing the mean squared error (MSE) of the sensing beampattern, subject to a symbol MSE constraint. This problem is then solved by sequentially optimizing the analog and digital parts. Both the multi-aperture structure (MAS) and the multi-beam structure (MBS) are considered in the analog part. We conduct theoretical analysis on the asymptotic pairwise error probability (APEP) and the Cramér-Rao bound (CRB) of direction of arrival (DoA) estimation. Numerical simulations

Received 15 May 2024; revised 5 October 2024 and 17 February 2025; accepted 17 February 2025. Date of publication 4 March 2025; date of current version 12 June 2025. This work was supported in part by the National Natural Science Foundation of China under Grant 62125101 and Grant 62341101; in part by the New Cornerstone Science Foundation through the Xplorer Prize; in part by the National Natural Science Foundation of China under Grant 62401488; in part by the Guangzhou-HKUST(GZ) Joint Funding Scheme under Grant 2025A03J3878; in part by the Guangdong Provincial Key Lab of Integrated Communication, Sensing and Computation for Ubiquitous Internet of Things under Grant 2023B1212010007; in part by the Natural Science Foundation of China Project under Grant #U23A20339; in part by the Guangzhou Municipal Science and Technology Project under Grant #2023A03J0011; and in part by the Guangdong Provincial Project under Grant #2023ZDZX1037 and Grant #2023ZT10X009. An earlier version of this paper was presented in part at the 2024-Spring IEEE Vehicular Technology Conference (VTC2024-Spring, Singapore) [DOI: 10.1109/VTC2024-Spring62846.2024.10683336]. The associate editor coordinating the review of this article and approving it for publication was Q. Wu. *(Corresponding authors: Xiang Cheng; Shijian Gao.)*

Boxun Liu, Zonghui Yang, and Xiang Cheng are with the State Key Laboratory of Advanced Optical Communication Systems and Networks, School of Electronics, Peking University, Beijing 100871, China (e-mail: boxunliu@stu.pku.edu.cn; yzh22@stu.pku.edu.cn; xiangcheng@pku.edu.cn).

Shijian Gao is with the Internet of Things Thrust, The Hong Kong University of Science and Technology (Guangzhou), Guangzhou 511400, China (e-mail: shijiangao@hkust-gz.edu.cn).

Liuqing Yang is with the Internet of Things Thrust and the Intelligent Transportation Thrust, The Hong Kong University of Science and Technology (Guangzhou), Guangzhou 511400, China, and also with the Department of Electronic and Computer Engineering and the Department of Civil and Environmental Engineering, The Hong Kong University of Science and Technology, Hong Kong, SAR, China (e-mail: lqyang@ust.hk).

Digital Object Identifier 10.1109/TWC.2025.3545372

validate the overall enhanced ISAC performance over existing alternatives.

*Index Terms*— Integrated sensing and communications (ISAC), mmWave, hybrid transceivers, beam pattern modulation.

# <span id="page-0-5"></span><span id="page-0-4"></span><span id="page-0-1"></span>I. INTRODUCTION

<span id="page-0-3"></span><span id="page-0-2"></span>I NTEGRATED sensing and communications (ISAC) [\[2\],](#page-13-0) [\[3\],](#page-13-1) [\[4\],](#page-13-2) [\[5\]](#page-13-3) is a pivotal technology for B5G/6G, striving for symbiosis and mutual enhancement of communication and sensing with sharing resources such as spectrum, hardware, and energy. Recently, millimeter-wave (mmWave) ISAC has gained substantial attention due to its broader bandwidth, facilitating higher data rates and improved detection accuracy for both communication and sensing. Moreover, sensing and communication share similar channel characteristics and signal processing techniques in the mmWave frequency band [\[6\],](#page-13-4) further enabling their seamless integration.

<span id="page-0-14"></span><span id="page-0-13"></span><span id="page-0-12"></span><span id="page-0-11"></span><span id="page-0-10"></span><span id="page-0-9"></span><span id="page-0-8"></span><span id="page-0-7"></span><span id="page-0-6"></span>Transceiver design is vital for mmWave ISAC system, aiming to realize better performance trade-offs between communication and sensing. A large proportion of ISAC transceivers [\[7\],](#page-13-5) [\[8\],](#page-13-6) [\[9\]](#page-13-7) rely on fully digital (FD) architectures, making them impractical to deploy in mmWave ISAC massive MIMO systems due to high hardware costs and power consumption. To address this issue, some studies have explored low-cost hybrid architectures [\[10\]](#page-13-8) for mmWave ISAC transceiver design [\[11\],](#page-13-9) [\[12\],](#page-13-10) [\[13\],](#page-13-11) [\[14\],](#page-13-12) [\[15\], w](#page-13-13)here the number of RF chains is fewer than the number of antennas. In [\[11\],](#page-13-9) a fully-connected hybrid transceiver design was proposed for the single-user mmWave ISAC scenario by approximating the optimal communication and radar precoder. To further lower the hardware cost, the partially-connected hybrid transceiver architecture [\[12\]](#page-13-10) has been adopted for enabling multi-user ISAC, which minimizes the Cramér-Rao bound (CRB) for direction of arrival (DoA) estimation under communication constraints. However, the spectral efficiency (SE) of hybrid ISAC systems is impaired due to two factors. On the one hand, the restricted number of RF chains damages the potential multiplexing gain (MG). On the other hand, additional sensing functions will consume system resources, inevitably causing a further decrease in SE.

To achieve higher SE, index modulation (IM) has emerged as a promising technology for delivering additional <span id="page-1-5"></span><span id="page-1-4"></span><span id="page-1-2"></span><span id="page-1-1"></span>information by selectively activating the state of certain resource domains [16], [17], [18], such as antennas and subcarriers [19]. Recently, some sensing-centric ISAC transceiver designs have been proposed in conjunction with IM to improve SE [7], [8], [9], [20]. In [7], a multi-carrier agile joint radar communication (MAJoRCom) system was proposed based on carrier agile phased array radar (CAESAR), where communication bits are transmitted through selective activation of radar waveforms on subcarriers and antennas. Furthermore, a hybrid index modulation (HIM) scheme was proposed [9] for frequency hopping MIMO radar communications system, where communication bits are transmitted through index modulation on entwined frequency, phase, and antenna tuples. While radar functionality remains unaffected in [7] and [9], it results in a significantly low communication rate. In [8], a spatial modulation-based communication-radar (SpaCoR) system was proposed, where individual sensing and communication waveforms are transmitted on different antennas, and generalized spatial modulation (GSM) is adopted to embed additional data bits through antenna selection. Nevertheless, the data rates are limited by the radar pulse period. In addition, these designs rely on antenna activation-based index modulation and are exclusively designed for FD architecture, limiting direct application to hybrid systems.

<span id="page-1-8"></span><span id="page-1-7"></span>To better cope with the hybrid structures, generalized beamspace modulation (GBM) was proposed in [18], which utilizes the unique sparsity of mmWave beamspace channel to elevate SE by implementing IM over beamspace. However, it is designed for mmWave communication-only systems without sensing capabilities. Built upon GBM, recent works [21], [22], [23] introduce similar IM schemes into mmWave ISAC systems to attain higher SE. In [21], the dual-functional beam pattern is selectively activated in a non-uniform manner for a higher SE. Nonetheless, the additional sensing capability of beam patterns inevitably compromises the communication performance. In [22], the ISAC transmitter selectively activates partial spatial paths for communication and employs a single fixed beam for sensing, termed SPIM-ISAC. The design of separate communication and sensing beams enhances communication SE while ensuring sensing performance. The subsequent work [23] delves further into the consideration of the beam squint effect in the terahertz frequency band. In fact, SPIM is a special case of GBM without beam optimization, which constructs beamspace through fixed strongest spatial paths. However, as it extends to non-line-of-sight (NLoS) scenarios, multi-angle sensing beams introduce potential disturbance to communication receivers due to the randomness of targets' angles, thereby deteriorating the error performance. Additionally, SPIM-ISAC achieves a performance trade-off solely through power allocation between optimal communications-only and sensing-only beamformers, lacking a comprehensive consideration of overall performance.

Considering the limitations highlighted in the previously mentioned works, we have developed a communication-centric mmWave ISAC transceiver design, where one dedicated RF chain is reserved for sensing. To address the decrease in SE resulting from the reduced number of RF chains allocated for communication, we have extended GBM to beam pattern modulation (BPM) for communication beams. Compared to GBM

<span id="page-1-3"></span>based on the ideal beamspace domain and SPIM based on the channel path domain, BPM considers a more generalized beam pattern concept, where each beam pattern is formed by the corresponding column of analog precoders. Nevertheless, more flexible beam pattern and additional sensing requirements increase the complexity of the transceiver optimization. In light of the sensing interference on the communication receiver, we formulate a joint optimization problem to minimize the sensing beampattern mean squared error (MSE) under the symbol MSE constraint. We solve it by optimizing analog and digital parts sequentially, where both the multi-aperture structure (MAS) and the multi-beam structure (MBS) are considered for analog part optimization. For MBS, a lowcomplexity 2-step beam selection algorithm based on the min-MSE criterion is proposed. For MAS, we adopt the branch and bound algorithm for analog sensing precoder design and the entry-wise iteration algorithm for analog communication parts design. With the fixed analog part, the digital part is optimized using the proposed alternating optimization algorithm for improved power allocation. Moreover, the communication and sensing performance are theoretically analyzed. The contributions of our work can be summarized as follows.

- We propose a beam pattern modulation-embedded hybrid transceiver design for mmWave ISAC systems (BPM-ISAC), where the ISAC transmitter provides multi beams for single-user communication and scanning beams for sensing, respectively. The communication beams are selectively activated to enhance SE.
- <span id="page-1-6"></span>We formulate an optimization problem to minimize sensing beampattern MSE with symbol MSE constraint and solve it via optimizing analog and digital parts sequentially. Two typical hybrid structures, namely MBS and MAS, are considered for the analog part design.
- We conduct a theoretical analysis of the complexity and convergence of the proposed algorithm. The asymptotic pairwise error probability (APEP) and the CRB are derived to illustrate the bit error and DoA estimation performance. Additionally, simulation results validate the proposed method's advantages in ISAC.

The rest of this paper is organized as follows: Section II introduces the system and signal model of the proposed BPM-ISAC system. Section III formulates an optimization problem and Section IV proposes a joint hybrid transceiver design to solve it. Then Section V gives the performance analysis and Section VI provides numerical simulations. Finally, Section VII concludes this paper.

Notation:  $(\cdot)^{\mathrm{T}}$ ,  $(\cdot)^{\mathrm{H}}$ ,  $(\cdot)^{\dagger}$ ,  $\|\cdot\|_2$ , and  $\|\cdot\|_F$  denote the transpose, the conjugate transpose, pseudo-inverse, 2 norm and Frobenius norm, respectively. a[i] is the i-th element of a vector a and A[i,j] denotes the element of matrix A at the i-th row and the j-th column.  $\dot{a}(\psi) = \frac{\partial a(\psi)}{\partial \psi}$  means the derivative of vector a over  $\psi$ .  $\mathcal{CN}(m,\sigma^2)$  represents the complex Gaussian distribution whose mean is m and covariance is  $\sigma^2$ .  $F_N$  denotes the N-dimensional discrete Fourier transform (DFT) matrix.  $I_K$  is the  $K \times K$  identity matrix and  $1_K$  denotes the  $K \times 1$  all-one column vector.

<span id="page-1-0"></span><sup>&</sup>lt;sup>1</sup>Simulation codes are provided to reproduce the results presented in this paper: https://github.com/liuboxun/BPM-ISAC

<span id="page-2-1"></span>![](_page_2_Figure_2.jpeg)

Fig. 1. An illustration of the symbol mapping scheme and the transceiver architecture for the proposed BPM-ISAC mmWave system. ( $N_C = 3, K = 4, W = 3$ ).

 $\operatorname{diag}(a)$  means diagonal matrix formed from vector a and  $\mathbb{E}(\cdot)$  means expectation operation.  $\mathbb{R}$  and  $\mathbb{C}$  denote the set of real numbers and complex numbers, respectively.

#### II. SYSTEM MODEL

<span id="page-2-0"></span>As shown in Fig. 1, we consider a mmWave ISAC system for point-to-point communication and multi-target detection, which consists of an ISAC base station (BS) and a communication receiver. The ISAC BS comprises an ISAC transmitter and an echo receiver for simultaneous communication and monostatic sensing. In our modeling, the communication receiver and sensing targets are assumed to be spatially distinct. Both the ISAC transmitter, the echo receiver, and the communication receiver adopt fully-connected hybrid architecture, equipped with  $N_{\rm t}$ ,  $N_{\rm e}$ , and  $N_{\rm r}$  half-wavelength spaced uniform linear antenna array, respectively.

### A. Beam Pattern Modulation for ISAC

At the ISAC transmitter, K communication beams and W sensing scanning beams are generated through corresponding digital and analog precoders, i.e.,

$$s = F_{\mathbf{C}} P_{\mathbf{C}} \bar{x}_{\mathbf{C}} + F_{\mathbf{S}} P_{\mathbf{S}} \bar{x}_{\mathbf{S}}, \tag{1}$$

where  $\bar{\boldsymbol{x}}_{\mathrm{C}} \in \mathbb{C}^{K \times 1}$  and  $\bar{\boldsymbol{x}}_{\mathrm{S}} \in \mathbb{C}^{W \times 1}$  are the mapped communication and sensing symbols, respectively.  $\boldsymbol{F}_{\mathrm{C}} \in \mathbb{C}^{N_{\mathrm{t}} \times K}$  and  $\boldsymbol{F}_{\mathrm{S}} \in \mathbb{C}^{N_{\mathrm{t}} \times W}$  are analog precoders for communication and sensing, respectively.  $\boldsymbol{P}_{\mathrm{C}} = \mathrm{diag}\left(\boldsymbol{p}\right) \in \mathbb{R}^{K \times K}$  and  $\boldsymbol{P}_{\mathrm{S}} = \mathrm{diag}\left(\boldsymbol{b}\right) \in \mathbb{R}^{W \times W}$  are the corresponding digital precoders, where each element of  $\boldsymbol{p}$  and  $\boldsymbol{b}$  represents the power allocation on the associated beam.

1) Communication: For communication, IM is implemented on the beam pattern domain. Specifically, in each symbol period, only  $N_{\rm C}$  out of K communication beams are activated. To realize the selective activation,  $N_{\rm C}$ -dimensional non-zero data stream  $\boldsymbol{x}_{\rm C} \in \mathbb{C}^{N_{\rm C} \times 1}$  is mapped to K-dimensional zero-containing  $\bar{\boldsymbol{x}}_{\rm C}$  with totally  $C_K^{N_{\rm C}}$  possible index patterns. Similar to [18],  $2^{\lfloor \log_2 C_K^{N_{\rm C}} \rfloor}$  of these patterns are utilized to transmit additional  $\lfloor \log_2 C_K^{N_{\rm C}} \rfloor$  index bits. Suppose M-ary phase shift keying/quadrature amplitude modulation (PSK/QAM) is adopted for communication, and the achievable SE is given by

$$\eta = N_{\rm C} \log_2 M + \lfloor \log_2 C_K^{N_{\rm C}} \rfloor \text{bps/Hz.}$$
(2)

2) Sensing: For sensing, to save RF chains, each of the W beams is sequentially activated to scan W directions of interest. Therefore, sensing signal  $x_{\rm S}$  is mapped to a W-dimensional one-hot vector  $\bar{\boldsymbol{x}}_{\rm S} \in \mathbb{C}^{W \times 1}$  before transmission. For more flexible sensing, the case of non-equal probability scanning is considered. Denote the activation probability matrix as  $\boldsymbol{D}={\rm diag}([d_1,\ldots,d_W])$ , where  $d_i$  represents the predefined activation probability of the i-th sensing beam and satisfies  $\sum_{i=1}^W d_i=1$ .

For the hardware implementation, as shown in Fig. 1, only  $N_{\rm C}$  and one RF chains are deployed at the ISAC transmitter for communication and sensing, respectively. The switching network is controlled to adjust the RF chain connection for non-zeros symbols transmission. In addition, we assume K and W RF chains are employed for the communication receiver and echo receiver, respectively.

# B. I-O Relationship of Communication

The classical Saleh-Valenzuela mmWave channel [24] with *P* dominant paths is adopted as

<span id="page-2-4"></span><span id="page-2-3"></span>
$$\boldsymbol{H} = \sqrt{\frac{N_{\rm t}N_{\rm r}}{P}} \sum_{i=1}^{P} \alpha_{i} \boldsymbol{a}_{N_{\rm r}} \left(\theta_{i}\right) \boldsymbol{a}_{N_{\rm t}}^{\rm H} \left(\phi_{i}\right), \tag{3}$$

where  $\alpha_i$  is the complex gain of the *i*-th path,  $a_{N_{\rm r}}(\theta_i)$  and  $a_{N_{\rm t}}(\phi_i)$  are the channel steering vectors of the *i*-th path, where  $a_N(\theta)[i] = \frac{1}{\sqrt{N_{\rm t}}}e^{-j\pi(i-1)\sin(\theta)}$ . We assume that H is available at the transmitter. In the time division duplex (TDD) system, this can be achieved via advanced channel estimation schemes [25] in the uplink, while in the frequency division duplex (FDD), this can resort to downlink estimation accompanied by dedicated feedback strategies [26].

The received signal processed by analog combiner  $m{W}_{\mathrm{RF}} \in \mathbb{C}^{N_{\mathrm{r}} imes K}$  becomes

<span id="page-2-6"></span><span id="page-2-5"></span>
$$y_{C} = W_{RF}^{H} H F_{C} P_{C} \bar{x}_{C} + W_{RF}^{H} H F_{S} P_{S} \bar{x}_{S} + \xi_{C}$$
$$= H_{C} P_{C} \bar{x}_{C} + H_{S} P_{S} \bar{x}_{S} + \xi_{C}, \tag{4}$$

<span id="page-2-2"></span>where  $\boldsymbol{H}_{\mathrm{C}}$  and  $\boldsymbol{H}_{\mathrm{S}}$  is the equivalent digital channel (EDC) for communication and sensing, and  $\boldsymbol{\xi}_{\mathrm{C}} \sim \mathcal{CN}(0, \sigma^2 \boldsymbol{I}_K)$  is additive white Gaussian noise (AWGN). It is noteworthy that the communication received signal is disturbed by sensing signal and noise. There exists a trade-off between sensing and communication, wherein higher sensing power will increase the symbol error rate.

To eliminate the sensing interference, one possible method is to estimate the sensing signal and then subtract it at the communication receiver [14]. However, this scheme assumes that the instantaneous sensing signal is known to the user, limiting the freedom degree of sensing waveform and increasing the operational complexity. In this paper, we suppose that only second-order statistics of the sensing signal are known at the communication receiver. Therefore, the well-known LMMSE equalizer is adopted as

$$W_{\mathrm{BB}} = R_{\bar{\boldsymbol{x}}_{\mathrm{C}}} P_{\mathrm{C}} H_{\mathrm{C}}^{\mathrm{H}} \left( H_{\mathrm{C}} P_{\mathrm{C}} R_{\bar{\boldsymbol{x}}_{\mathrm{C}}} P_{\mathrm{C}} H_{\mathrm{C}}^{\mathrm{H}} + H_{\mathrm{S}} P_{\mathrm{S}} R_{\bar{\boldsymbol{x}}_{\mathrm{S}}} P_{\mathrm{S}} H_{\mathrm{S}}^{\mathrm{H}} + \sigma^{2} I_{K} \right)^{-1}, \quad (5)$$

where  $m{R}_{m{ar{x}}_{\mathrm{C}}} = \mathbb{E}\left[m{ar{x}}_{\mathrm{C}}m{ar{x}}_{\mathrm{C}}^{\mathrm{H}}\right] = rac{N_{\mathrm{C}}}{K}m{I}_{K}$  and  $R_{m{ar{x}}_{\mathrm{S}}} = \mathbb{E}\left[m{ar{x}}_{\mathrm{S}}m{ar{x}}_{\mathrm{S}}^{\mathrm{H}}\right] = m{D}$ . Then the symbol  $m{ar{x}}_{\mathrm{C}}$  is estimated as

$$\tilde{\boldsymbol{x}}_{C} = \boldsymbol{W}_{\mathrm{BB}} \left( \boldsymbol{H}_{\mathrm{C}} \boldsymbol{P}_{\mathrm{C}} \bar{\boldsymbol{x}}_{\mathrm{C}} + \boldsymbol{H}_{\mathrm{S}} \boldsymbol{P}_{\mathrm{S}} \bar{\boldsymbol{x}}_{\mathrm{S}} + \boldsymbol{\xi}_{\mathrm{C}} \right).$$
 (6)

The information bits contained in  $x_{\rm C}$  and index bits can be estimated by the maximum likelihood (ML) detector or 2-step quantization detector [18], so the details are omitted here.

### C. I-O Relationship of Sensing

Suppose there are N pointed targets with i-th one locating at angles  $\psi_i$ . The ISAC transmitter sequentially transmits W sensing beams to cover the range of interest. Then the echoes are received to estimate the target parameters. Considering quasi-static sensing processes, it is equivalent to simultaneously scanning and receiving echoes from various directions. We assume that the self-interference on the echo receiver from the transmitter can be effectively mitigated [27]. Besides, the communication reflected signals at the target are ignored because they are relatively weak compared to the sensing signal [14]. During per scanning, the received echo signal is approximated as

$$\mathbf{y}_{\mathrm{R}} = \sum_{i=1}^{N} \beta_{i} \mathbf{a}_{N_{\mathrm{e}}} (\psi_{i}) \mathbf{a}_{N_{\mathrm{t}}}^{\mathrm{H}} (\psi_{i}) (\mathbf{F}_{\mathrm{S}} \mathbf{P}_{\mathrm{S}} \bar{\mathbf{x}}_{\mathrm{S}} + \mathbf{F}_{\mathrm{C}} \mathbf{P}_{\mathrm{C}} \bar{\mathbf{x}}_{\mathrm{C}}) + \boldsymbol{\xi}_{\mathrm{R}}$$

$$\stackrel{(a)}{\simeq} \sum_{i=1}^{N} \beta_{i} \mathbf{a}_{N_{\mathrm{e}}} (\psi_{i}) \mathbf{a}_{N_{\mathrm{t}}}^{\mathrm{H}} (\psi_{i}) \mathbf{F}_{\mathrm{S}} \mathbf{P}_{\mathrm{S}} \bar{\mathbf{x}}_{\mathrm{S}} + \boldsymbol{\xi}_{\mathrm{R}}, \tag{7}$$

where  $\beta_i$  denotes the i-th reflection coefficient of the target and  $\boldsymbol{\xi}_{\mathrm{R}} \in \mathbb{C}^{N_{\mathrm{e}} \times 1}$  is the additive white Gaussian noise. (a) is for that the communication beam will be selected to stay away from the target direction to avoid sensing interference, and  $\boldsymbol{a}_{\mathrm{N_t}}^{\mathrm{H}}(\psi_i)\boldsymbol{F}_{\mathrm{C}}\boldsymbol{P}_{\mathrm{C}}\bar{\boldsymbol{x}}_{\mathrm{C}}\simeq 0$  is satisfied. For cases where the sensing targets are close to the communication receiver, sensing can be achieved simply using the communication beam without additional optimization, which is not within the scope of our study. Denote  $\boldsymbol{\Xi}=\mathrm{diag}\left(\beta_1,\ldots,\beta_N\right)$  and  $\boldsymbol{A}_M=[\boldsymbol{a}_M\left(\psi_1\right),\ldots,\boldsymbol{a}_M\left(\psi_N\right)]$ , and we can obtain the compact form as

$$\boldsymbol{y}_{\mathrm{R}} \simeq \boldsymbol{A}_{N_{\mathrm{e}}} \Xi \boldsymbol{A}_{N_{\mathrm{t}}}^{\mathrm{H}} \boldsymbol{F}_{\mathrm{S}} \boldsymbol{P}_{\mathrm{S}} \bar{\boldsymbol{x}}_{\mathrm{S}} + \boldsymbol{\xi}_{\mathrm{R}}.$$
 (8)

For simplicity, we assume that  $N_{\rm t}=N_{\rm r}$  and denote  ${\bf A}={\bf A}_{N_{\rm t}}={\bf A}_{N_{\rm e}}$ . Since the direction of departure (DoD) and DoA of the target are the same, the sensing analog combiner

 $W_{\rm E}$  can be implemented as  $F_{\rm S}$ . Then the sensing baseband received signal is derived as

<span id="page-3-6"></span><span id="page-3-4"></span>
$$y_{\mathrm{B}} = F_{\mathrm{S}}^{\mathrm{H}} A \Xi A^{\mathrm{H}} F_{\mathrm{S}} P_{\mathrm{S}} \bar{x}_{\mathrm{S}} + F_{\mathrm{S}}^{\mathrm{H}} \xi_{\mathrm{R}}$$
$$= T_{\mathrm{R}}^{\mathrm{H}} \Xi T_{\mathrm{B}} P_{\mathrm{S}} \bar{x}_{\mathrm{S}} + \xi_{\mathrm{R}}, \tag{9}$$

where  $T_{\rm B} = A^{\rm H} F_{\rm S}$  and  $\xi_{\rm B} \sim \mathcal{CN}(0, R_{\rm B})$ . The target parameters can be estimated with existing algorithms. For example, DoA estimation can be performed using the beamspace MUSIC algorithm [28].

#### III. PROBLEM FORMULATION FOR BPM-ISAC

<span id="page-3-3"></span><span id="page-3-0"></span>In this section, we establish the performance criterion of sensing and communication, and formulate a joint optimization problem to achieve the desired sensing beampattern with reliable communication via optimizing the hybrid transceivers.

#### <span id="page-3-1"></span>A. Sensing Performance Criterion

For accurate parameter estimation, radiating sufficient energy in the directions of interest is crucial. Hence, the beampattern is adopted as the sensing performance metric, measuring the sensing power distribution in different directions. Denote  $\theta_t$  as the t-th direction of interest, then the actual sensing beampattern is defined as

$$v = [|b_1 a_{N_t}^{H}(\theta_1) F_S[:, 1]|, ..., |b_W a_{N_t}^{H}(\theta_W) F_S[:, W]|]^T, (10)$$

where  $b_i$  is the *i*-th element of **b** and represents the allocated power on *i*-th sensing beam.

<span id="page-3-5"></span>To augment sensing performance, the actual sensing beampattern needs to maximally match the ideal beampattern. We predefine the ideal beampattern as  $\boldsymbol{t} \in \mathbb{R}^{W \times 1}$ , which satisfies the power constraint  $\|\boldsymbol{D}^{\frac{1}{2}}\boldsymbol{t}\|_2^2 = \sum_{i=1}^W d_i t_i^2 = T_{\mathrm{R}}$ , where  $t_i$  is the i-th element of  $\boldsymbol{t}$  and  $T_{\mathrm{R}}$  is the average sensing power. The sensing beampattern MSE [29] is adopted as the criterion of sensing performance, which measures the discrepancy between sensing beampattern  $\boldsymbol{v}$  and ideal beampattern  $\boldsymbol{t}$ . Considering the activation probability of each beam, it is derived as

<span id="page-3-7"></span>
$$MSE_{S}(\boldsymbol{P}_{S}, \boldsymbol{F}_{S}) = \|\boldsymbol{D}^{\frac{1}{2}}(\boldsymbol{v} - \boldsymbol{t})\|_{2}^{2} = \sum_{i=1}^{W} d_{i}(v_{i} - t_{i})^{2}.$$
 (11)

# B. Communication Performance Criterion

The communication performance includes effectiveness and reliability, which are characterized by SE and symbol error, respectively. Since the SE of the proposed method is determined as Eq. (2), we resort to the symbol MSE under fixed SE as the performance metric to characterize the transmission reliability. According to Eq. (6), the symbol MSE of  $\bar{x}_{\rm C}$ ,  $\mathbb{E}\left(\|\tilde{x}_C - \bar{x}_{\rm C}\|_2^2\right)$ , is derived as

<span id="page-3-2"></span>
$$MSE_{C}(\boldsymbol{H}_{C}, \boldsymbol{H}_{S}, \boldsymbol{P}_{C}, \boldsymbol{P}_{S})$$

$$= \frac{N_{C}}{K} \|\boldsymbol{W}_{BB} \boldsymbol{H}_{C} \boldsymbol{P}_{C} - \boldsymbol{I}_{K}\|_{F}^{2}$$

$$+ \|\boldsymbol{D}^{\frac{1}{2}} \boldsymbol{W}_{BB} \boldsymbol{H}_{S} \boldsymbol{P}_{S}\|_{F}^{2} + \sigma^{2} \|\boldsymbol{W}_{BB}\|_{F}^{2}.$$
(12)

As can be seen, the MSE stems from three factors: symbol estimation residual, sensing interference, and noise. Since

<span id="page-4-7"></span>TABLE I
DESCRIPTION OF EACH COMPONENT IN ISAC HYBRID TRANSCEIVERS

| on of Each Component in 1971c Hibrid Transcel |                             |                                |  |
|-----------------------------------------------|-----------------------------|--------------------------------|--|
|                                               | Symbol                      | Parameter                      |  |
|                                               | $P_{ m C}$                  | Digital communication precoder |  |
|                                               | $P_{ m S}$                  | Digital sensing precoder       |  |
|                                               | $oldsymbol{F}_{\mathrm{C}}$ | Analog communication precoder  |  |
|                                               | $oldsymbol{F_{\mathrm{S}}}$ | Analog sensing precoder        |  |
|                                               | $W_{ m RF}$                 | Analog communication combiner  |  |

the sensing interference intensity may vary significantly with different channel realizations, it is difficult to determine a fixed MSE threshold remaining proper under all channel conditions. Therefore, we introduce a relative MSE threshold related to  $\boldsymbol{H}_{\mathrm{C}}$  and  $\boldsymbol{H}_{\mathrm{S}}$  as follows:

Assuming no processing is applied on the digital part, i.e.,  $P_{\rm S}={\rm diag}\left(t\right)$  and  $P_{\rm C}=I_K$ , the corresponding digital combiner becomes

$$\mathbf{W}_{\mathrm{BB},0} = \frac{N_{\mathrm{C}}}{K} \mathbf{H}_{\mathrm{C}}^{\mathrm{H}} \left( \frac{N_{\mathrm{C}}}{K} \mathbf{H}_{\mathrm{C}} \mathbf{H}_{\mathrm{C}}^{\mathrm{H}} + \mathbf{H}_{\mathrm{C}} (\operatorname{diag}(\mathbf{t}))^{2} \mathbf{D} \mathbf{H}_{\mathrm{S}}^{\mathrm{H}} + \sigma^{2} \mathbf{I}_{K} \right)^{-1}.$$
(13)

The relative symbol MSE threshold is defined as

$$\Gamma(\boldsymbol{H}_{\mathrm{C}}, \boldsymbol{H}_{\mathrm{S}}, \mu)$$

$$= \frac{N_{\mathrm{C}}}{K} \|\boldsymbol{W}_{\mathrm{BB},0} \boldsymbol{H}_{\mathrm{C}} - \boldsymbol{I}_{K}\|_{F}^{2}$$

$$+ \mu \|\boldsymbol{D}^{\frac{1}{2}} \boldsymbol{W}_{\mathrm{BB},0} \boldsymbol{H}_{\mathrm{S}} \mathrm{diag}(\boldsymbol{t})\|_{F}^{2} + \sigma^{2} \|\boldsymbol{W}_{\mathrm{BB},0}\|_{F}^{2}, \quad (14)$$

where  $0 \le \mu \le 1$  is the weighting coefficient, signifying the relative tolerance for sensing interference cancellation errors. As  $\mu$  increases, a lighter emphasis is placed on the communication side, resulting in improved sensing performance.

#### <span id="page-4-9"></span>C. Problem Formulation

To minimize sensing beampattern MSE while adhering to constraints on symbol MSE, transmit power, as well as the analog precoder, a joint optimization problem of hybrid transceivers is formulated as

$$\min_{\substack{\boldsymbol{P}_{\mathrm{C}}, \boldsymbol{P}_{\mathrm{S}} \\ \boldsymbol{F}_{\mathrm{C}}, \boldsymbol{F}_{\mathrm{S}}, \boldsymbol{W}_{\mathrm{RF}}}} \mathrm{MSE}_{\mathrm{S}}(\boldsymbol{P}_{\mathrm{S}}, \boldsymbol{F}_{\mathrm{S}})$$
 (15a)

s.t. 
$$MSE_C(\boldsymbol{H}_C, \boldsymbol{H}_S, \boldsymbol{P}_C, \boldsymbol{P}_S) \leq \Gamma(\boldsymbol{H}_C, \boldsymbol{H}_S, \mu)$$
, (15b)

$$\|P_C\|_E^2 < K, (15c)$$

$$\|\boldsymbol{D}^{\frac{1}{2}}\boldsymbol{b}\|_{F}^{2} < T_{\mathrm{R}},\tag{15d}$$

$$F_{\rm C} \in \mathcal{F},$$
 (15e)

$$F_{\rm S} \in \mathcal{F},$$
 (15f)

$$W_{\mathrm{RF}} \in \mathcal{W}.$$
 (15g)

The expressions of  $\chi$  and  $\Gamma(\mu)$  are provided in Eqs. (12) and (14), respectively. (15b) represents MSE constraint on communication symbol estimation, (15c) corresponds to the communication power constraint, and (15d) denotes the average sensing power constraint. In Eqs. (15e)-(15g),  $\mathcal{F}$  and  $\mathcal{W}$  represent the feasible analog precoder sets of the ISAC transmitter and communication receiver, respectively. We consider two representative analog configurations, i.e., MBS and MAS. For MBS, low-cost lens array antennas [10] are employed and each column of analog precoders is selected from N-dimensional DFT codebook  $\mathcal{F}_N = \{ \mathbf{F}_N[:,1], \ldots, \mathbf{F}_N[:,N] \}$ ,

where N takes on  $N_{\rm t}$  or  $N_{\rm r}$ . For MAS, the fully connected B-bit phase shifter network is adopted, and the adjustable angles of each element of analog precoders are selected from  $\mathcal{B} = \left\{0, \frac{2\pi}{2^B}, \dots, \frac{2\pi(2^B-1)}{2^B}\right\}$ . For convenience, the notations of all optimized variables are summarized in Table I.

#### <span id="page-4-0"></span>IV. HYBRID TRANSCEIVER DESIGN FOR BPM-ISAC

In this section, we propose an efficient transceiver design to address the optimization problem formulated above. Due to the coupling of all five variables in the non-convex constraint (15b) and the discrete nature of the feasible analog precoder set, the original problem is a complex mixed-integer non-convex large-scale combinatorial optimization problem that is difficult to solve. As a result, we address it by optimizing analog and digital parts sequentially.

# <span id="page-4-10"></span>A. Analog-Part Optimization for BPM-ISAC

Considering that the analog part forms the EDC and plays a fundamental role in digital part design [30], we first optimize the analog part with the unoptimized digital part. Then the symbol MSE is converted to the function of  $\boldsymbol{H}_{\rm S}$  and  $\boldsymbol{H}_{\rm C}$ , i.e.,

<span id="page-4-11"></span><span id="page-4-1"></span>
$$\overline{\text{MSE}}_{\text{C}}(\boldsymbol{H}_{\text{C}}, \boldsymbol{H}_{\text{S}})$$

$$= \frac{N_{\text{C}}}{K} \|\boldsymbol{W}_{\text{BB},0} \boldsymbol{H}_{\text{C}} - \boldsymbol{I}_{K}\|_{F}^{2}$$

$$+ \|\boldsymbol{D}^{\frac{1}{2}} \boldsymbol{W}_{\text{BB},0} \boldsymbol{H}_{\text{S}} \operatorname{diag}(\boldsymbol{t})\|_{F}^{2} + \sigma^{2} \|\boldsymbol{W}_{\text{BB},0}\|_{F}^{2}. \quad (16)$$

It is worth noting that  $\overline{\mathrm{MSE}}_{\mathrm{C}}(\boldsymbol{H}_{\mathrm{C}},\boldsymbol{H}_{\mathrm{S}})$  is the upper bound of the relative symbol MSE threshold, which measures the communication performance of EDC.

Firstly, the analog sensing precoder  $F_{\rm S}$  is optimized to point in the direction of interest by solving the following problem.

# $\mathcal{P}.1-1$ : Optimization for analog sensing precoder

$$\min_{\boldsymbol{F}_{\mathrm{S}}} \quad \mathrm{MSE}_{\mathrm{S}}(\boldsymbol{F}_{\mathrm{S}})$$
 $s.t. \quad \boldsymbol{F}_{\mathrm{S}} \in \mathcal{F}.$ 

<span id="page-4-3"></span><span id="page-4-2"></span>Then  $F_{\rm C}$  and  $W_{\rm RF}$  are jointly optimized with fixed  $F_{\rm S}$  to minimize symbol MSE as follows:

# <span id="page-4-5"></span><span id="page-4-4"></span> $\mathcal{P}.1\text{-}2$ : Optimization for communication's analog part

$$\min_{oldsymbol{F}_{\mathrm{C}}, oldsymbol{W}_{\mathrm{RF}}} \overline{\mathrm{MSE}}_{\mathrm{C}}(oldsymbol{H}_{\mathrm{C}}, oldsymbol{H}_{\mathrm{S}}) \ s.t. \ oldsymbol{F}_{\mathrm{C}} \in \mathcal{F}, \ oldsymbol{W}_{\mathrm{RF}} \in \mathcal{W}.$$

<span id="page-4-6"></span>Below,  $\mathcal{P}.1-1$  and  $\mathcal{P}.1-2$  are solved with the configuration of MBS and MAS, respectively.

1) Analog-Part for MBS: Firstly, the following proposition illustrates that  $\mathcal{P}.1$ -1 can be transformed into a series of parallel optimization problems.

Proposition 1: Solving  $\mathcal{P}.1-1$  is equivalent to optimizing each column of  $\mathbf{F}_{S}$  individually as follows:

<span id="page-4-8"></span>
$$\begin{aligned} & \max_{\boldsymbol{F}_{\mathrm{S}}[:,l]} |\boldsymbol{a}_{N_{\mathrm{t}}}^{\mathrm{H}}(\theta_{l}) \boldsymbol{F}_{\mathrm{S}}[:,l]| \\ & s.t. \quad \boldsymbol{F}_{\mathrm{S}}[:,l] \in \mathcal{F}_{N_{\mathrm{t}}}. \end{aligned}$$

*Proof:* Under an unoptimized digital part,  $P_{\mathrm{S}} = \mathrm{diag}\,(t)$ . Then the objective function can be rewritten as

$$MSE_{S} = \sum_{l=1}^{W} d_{l}t_{l}(|\boldsymbol{a}_{N_{t}}^{H}(\theta_{l})\boldsymbol{F}_{S}[:,l]|-1)^{2}.$$
 (17)

Considering that  $0 \leq |\boldsymbol{a}_{N_{\mathrm{t}}}^{\mathrm{H}}(\theta_{l})\boldsymbol{F}_{\mathrm{S}}[:,l]| \leq 1$ , minimizing Eq. (17) is equivalent to maximizing  $|\boldsymbol{a}_{N_{\mathrm{t}}}^{\mathrm{H}}(\theta_{l})\boldsymbol{F}_{\mathrm{S}}[:,l]|$  parallelly.

The optimal solution is obtained by exhaustive search and the computational complexity is  $\mathcal{O}(WN_{\rm t})$ , which is obviously acceptable. Considering the sensing beam set as  $\Omega = \{ \boldsymbol{F}_{\rm S}[:,1],\ldots,\boldsymbol{F}_{\rm S}[:,W] \}$ , communication transmitting beams should be selected from set difference  $\{\mathcal{F}_{N_{\rm t}}\backslash\Omega\}$  to avoid sensing interference on the communication receiver.

For  $\mathcal{P}.1$ -2, the optimization problem is reformulated as

$$\min_{\boldsymbol{F}_{\mathrm{C}}, \boldsymbol{W}_{\mathrm{RF}}} \overline{\mathrm{MSE}}_{\mathrm{C}}(\boldsymbol{H}_{\mathrm{C}}, \boldsymbol{H}_{\mathrm{S}})$$

$$s.t. \ \boldsymbol{F}_{\mathrm{C}}[:, i] \in \{\mathcal{F}_{N_{\mathrm{t}}} \backslash \Omega\},$$

$$\boldsymbol{W}_{\mathrm{RF}}[:, i] \in \mathcal{F}_{N_{\mathrm{r}}}.$$

Similar to [18],  $H_{\rm C}$  and  $H_{\rm S}$  are the submatrices of beamspace channel  $\bar{H} = F_{N_{\rm r}}^H H F_{N_{\rm t}}$ . Specifically, the indices of the selected sub-columns and sub-rows indicate the selected DFT codewords for transmitted and received beams respectively. Then the above problem can be regarded as determining a  $K \times K$  submatrix of  $\bar{H}$ .

Considering the exponential time complexity of the exhaustive search, we proposed a two-stage alternative to lower complexity. Firstly, a set of L largest elements in  $\bar{\boldsymbol{H}}$  are selected as candidate beam pairs. Secondly, the final columns and rows are chosen within the scope of these L candidate beam pairs using the min-MSE criterion. Then the overall computational complexity is reduced from  $\mathcal{O}(C_{N_{\mathrm{r}}}^K C_{N_{\mathrm{t}}-W}^K)$  to  $\mathcal{O}(N_r^2(N_t-W)^2+C_L^K)$ .

2) Analog-Part for MAS: Compared to MBS, MAS has higher degrees of freedom for more flexible beam patterns and better EDC. Below, we resort to the MAS with B-bit PSs for analog part design. In this case,  $\mathcal{P}.1$ -1 and  $\mathcal{P}.1$ -2 are integer programming problems, and the optimal solution can be solved by brutal search. However, it is impractical due to the exponential growth of time complexity with both the number of bits and antennas. Thus low-complexity methods are proposed for these two problems.

For  $\mathcal{P}.1$ -1, according to proposition 1, it is equivalent to solving the following problems parallelly.

$$\begin{aligned} & \max_{\boldsymbol{F}_{\mathrm{S}}[:,l]} |\boldsymbol{a}_{N_{\mathrm{t}}}^{\mathrm{H}}(\theta_{l}) \boldsymbol{F}_{\mathrm{S}}[:,l]| \\ & s.t. \ \boldsymbol{F}_{\mathrm{S}}[i,l] \in \frac{e^{j\mathcal{B}}}{\sqrt{N_{\mathrm{t}}}}, \forall i. \end{aligned}$$

<span id="page-5-4"></span>Since the definition domain of the variable is finite, it can be solved by the widely-used branch and bound (B&B) algorithm [31], which adopts tree search strategy but applies pruning rules to skip suboptimal regions of the tree. The tree has  $N_{\rm t}+1$  levels, and the n-th level branch represents the

<span id="page-5-3"></span>**Algorithm 1** Branch and Bound Algorithm for Optimizing Analog Sensing Precoder

```
Input: a(\theta_l).

1: Initialization: \mathcal{G} = \{v_0\}, q^* = q_0 and \mathcal{L} = \mathcal{L}_0.

2: for n = 1 : N_t do

3: Replace each node in \mathcal{G} with its descendant nodes.

4: for v \in \mathcal{G} do

5: Calculate f_{\mathrm{UB}} and f_{\mathrm{LB}} by Eq. (18) and Eq. (21).

6: Update \mathcal{G} as \mathcal{G} \setminus \{v\} if f_{\mathrm{UB}} \leq \mathcal{L}.

7: Update \mathcal{L} and q^* if f_{\mathrm{LB}} > \mathcal{L}.

8: end for

9: end for

Output: F_{\mathrm{S}}[:,l] = q^*.
```

value of n-th PSs, which has  $2^B$  child nodes. We perform a breadth-first search with  $N_{\rm t}$  iterations, during which it maintains the currently best available solution  $q^*$ , global lower bound  $\mathcal L$  and available set  $\mathcal G$ . The overall algorithm is summarized in Algorithm 1. At initialization,  $\mathcal G$  is consist of the root note  $v_0$ ,  $q^*$  is randomly set as  $q_0$  and  $\mathcal L$  is initialized as  $\mathcal L_0 = |a_{N_{\rm t}}^{\rm H}(\theta_l)q_0|$ . In the n-th iteration, for each new node, its upper bound and lower bound are calculated for updates.

For each node v, denote the first n elements of  $\boldsymbol{F}_{\mathrm{S}}[:,l]$  as  $\boldsymbol{q}_{\mathrm{L}} \in \mathbb{C}^{n \times 1}$  and the remained  $N_{\mathrm{t}} - n$  elements as  $\boldsymbol{q}_{\mathrm{R}} \in \mathbb{C}^{(N_{\mathrm{t}} - n) \times 1}$ . The objective function can be rewritten as  $f = |\boldsymbol{a}_{N_{\mathrm{t}}}^{\mathrm{H}}(\theta_{l})[1:n]\boldsymbol{q}_{\mathrm{L}} + \boldsymbol{a}_{N_{\mathrm{t}}}^{\mathrm{H}}(\theta_{l})[n+1:N_{\mathrm{t}}]\boldsymbol{q}_{\mathrm{R}}|$ . According to triangle inequality, the upper bound can be achieved as

<span id="page-5-1"></span>
$$f_{\rm UB} = |\boldsymbol{a}_{N_{\rm t}}^{\rm H}(\theta_l)[1:n]\boldsymbol{q}_{\rm L}| + N_{\rm t} - n$$
 (18)

with  $q_{\mathrm{R}}=q_{\mathrm{R,UB}}$ . The *i*-th phase of  $q_{\mathrm{R,UB}}$  satisfies

$$\angle \boldsymbol{q}_{\mathrm{R,UB}}[i] = \angle (\boldsymbol{a}_{N_{\mathrm{t}}}^{\mathrm{H}}(\theta_{l})[1:n]\boldsymbol{q}_{\mathrm{L}}) + \angle (\boldsymbol{a}_{N_{\mathrm{t}}}(\theta_{l})[i]), \quad (19)$$

where  $\angle(x)$  represents the phase of x. If  $f_{\mathrm{UB}}$  is lower than the current global lower bound  $\mathcal{L}$ , all leaves below node v are suboptimal and will be pruned. Otherwise, feasible  $q_{\mathrm{R}}$  will be obtained as  $q_{\mathrm{R,LB}}$  by quantifying  $q_{\mathrm{R,UB}}$  nearby with given B bit resolution, i.e.,

<span id="page-5-2"></span>
$$\boldsymbol{q}_{\mathrm{R,LB}} = \underset{\boldsymbol{q}_{R}[i] \in \frac{e^{j\mathcal{B}}}{\sqrt{N_{\mathrm{L}}}}, \forall i}{\arg \min} \|\boldsymbol{q}_{\mathrm{R}} - \boldsymbol{q}_{\mathrm{R,UB}}\|_{2}.$$
(20)

Meanwhile, the lower bound can be obtained as

$$f_{\text{LB}} = \left| \boldsymbol{a}_{N_{\text{t}}}^{\text{H}}(\theta_l)[1:n]\boldsymbol{q}_{\text{L}} + \boldsymbol{a}_{N_{\text{t}}}^{\text{H}}(\theta_l)[n+1:N_{\text{t}}]\boldsymbol{q}_{\text{R,LB}} \right|.$$
(21)

<span id="page-5-5"></span>If  $f_{\rm LB}$  is larger than  $\mathcal{L}$ ,  $\mathcal{L}$  will be updated as  $f_{\rm LB}$  and  $q^*$  should be updated as  $[q_{\rm L}^{\rm T}, q_{\rm R, LB}^{\rm T}]^{\rm T}$ . It is noteworthy that the solution of B&B algorithm is optimal with reduced computation time in comparison with the exhaustive search. For  $\mathcal{P}.1$ -2, it has been shown [32] that entry-wise iteration can be a low-complexity effective method for finite resolution PSs case. In detail, for columns z from 1 to K, the  $\mathbf{F}_{\rm C}[:,z]$  and  $\mathbf{W}_{\rm RF}[:,z]$  are optimized successively. For each column, each entry is optimized to minimize objective function while keeping the

Input: H,  $F_{\rm S}$ .

others fixed until convergence. For example,  ${m F}_{\rm C}[i,z]$  can be updated by solving

$$\min_{\mathbf{F}_{\mathrm{C}}[i,z]} \overline{\mathrm{MSE}}_{\mathrm{C}}$$

$$s.t. \ \mathbf{F}_{\mathrm{C}}[i,z] \in \frac{e^{j\mathcal{B}}}{\sqrt{N_{\mathrm{t}}}}.$$

Considering that appropriate initialization can improve the performance of the proposed iteration algorithm [33], an improved initializer is proposed below, especially for the low-bit case. Firstly, the following proposition illustrates the transformation of the initial problem.

<span id="page-6-2"></span>Proposition 2: As the SNR increases, P.1-2 with B-bit PSs tends to be asymptotically equivalent to the following mixed-integer semi-definite programming (MISDP) problem:

$$\min_{w, F_C, \mathbf{W}_{PF}} w \tag{22a}$$

s.t. 
$$Z = \begin{bmatrix} \frac{w}{K+W} I_{K+W} & G \\ G^{H} & J \end{bmatrix} \succeq 0,$$
 (22b)

$$F_{\rm C}[i,j] \in \frac{e^{j\mathcal{B}}}{\sqrt{N_{\rm t}}}, \forall i, j,$$
 (22c)

$$\mathbf{W}_{\mathrm{RF}}[i,j] \in \frac{e^{j\mathcal{B}}}{\sqrt{N_{\mathrm{t}}}}, \forall i, j,$$
 (22d)

where

$$m{G} = egin{bmatrix} ext{diag}(m{t}) m{D}^{rac{1}{2}} m{F}_{ ext{S}} m{H}^{ ext{H}} m{W}_{ ext{RF}} \ \sigma m{I}_K \end{pmatrix},$$

and

$$\boldsymbol{J} = \boldsymbol{W}_{\mathrm{RF}}^{\mathrm{H}} \boldsymbol{H} \boldsymbol{F}_{\mathrm{C}} \boldsymbol{F}_{\mathrm{C}}^{\mathrm{H}} \boldsymbol{H}^{\mathrm{H}} \boldsymbol{W}_{\mathrm{RF}}.$$

*Proof:* See Appendix A.

Considering that  $F_{\rm C}$  and  $W_{\rm RF}$  are coupled in the nonlinear constraint (22b), we solve the problem by alternatively optimizing  $F_{\rm C}$  and  $W_{\rm RF}$  until convergence. Below, we take  $F_{\rm C}$  as an example to illustrate how to transform the constraint (22b) into a linear matrix inequality (LMI) constraint.

straint (22b) into a linear matrix inequality (LMI) constraint. Denote  $\boldsymbol{a} = \frac{\pi}{2^{B-1}}[-(2^B-1),\ldots,(2^B-1)]^{\mathrm{T}}, \ \boldsymbol{c} = \cos(\boldsymbol{a})$  and  $\boldsymbol{s} = \sin(\boldsymbol{a})$ . A series of binary vectors  $\boldsymbol{x}^{i,j} \in \mathbb{C}^{(2^{B+1}-1)\times 1}$  and  $\boldsymbol{y}^{i,j,i',j'} \in \mathbb{C}^{(2^{B+1}-1)\times 1}$  are introduced, where  $\boldsymbol{x}^{i,j}[t]$  indicates whether  $\angle \boldsymbol{F}_{\mathrm{C}}[i,j]$  is  $\boldsymbol{a}[t]$  and  $\boldsymbol{y}^{i,j,i',j'}[t]$  indicates whether  $\angle \boldsymbol{F}_{\mathrm{C}}[i,j] - \angle \boldsymbol{F}_{\mathrm{C}}[i',j']$  is  $\boldsymbol{a}[t]$ .

Lemma 1: The problem in proposition 2 with fixed  $oldsymbol{W}_{\mathrm{RF}}$  can be equivalently transformed as

$$egin{aligned} \min \limits_{m{w}, m{x}^{i,j}, m{y}^{i,j,i',j'}} & w \ s.t. & (22b), \|m{x}^{i,j}\|_1 = 1, m{e}^{\mathrm{T}} m{x}^{i,j} = 0, \ & m{a}^{\mathrm{T}} (m{x}^{i,j} - m{x}^{i',j'}) = m{a}^{\mathrm{T}} m{y}^{i,j,i',j'}, \end{aligned}$$

where  $e \in \mathbb{C}^{(2^{B+1}-1)\times 1}$  is a constant vector whose first  $2^B - 1$  elements are 1 and others are 0. J is the linear function of  $u^{i,j,i',j'}$ .

Similarly, for the solution of  $W_{\rm RF}$ , we can transform G and J to the linear function of  $x^{i,j}$  and  $y^{i,j,i',j'}$ . The above problem is a MISDP problem with linear constraints and can be solved using the outer approximation method, which can seek existing optimization toolboxes such as YALMIP [34]. The algorithm is summarized as Algorithm 2.

<span id="page-6-3"></span>**Algorithm 2** Entry-Wise Iteration Algorithm With MISDP Initialization for Optimizing Communication's Analog Part

```
1: Initialization: F_{\rm C} = \mathbf{1}_{N_{\rm t} \times K}, W_{\rm RF} = \mathbf{1}_{N_{\rm r} \times K}.
2: Alternatively optimize F_{\rm C} and W_{\rm RF} by solving MISDP
    problem until convergence to obtain an initial value
3: for z=1:K do
4:
         repeat
              for i=1:N_{\rm r} do
5:
                   Optimize F_C[i, z] to minimize \bar{\chi}.
6:
7:
              for i=1:N_{\rm t} do
8:
                   Optimize W_{RF}[i,z] to minimize \bar{\chi}.
9:
10:
              end for
11:
         until Convergence.
12: end for
Output: F_{\rm C}, W_{\rm RF}.
```

# <span id="page-6-1"></span>B. Digital-Part Optimization for BPM-ISAC

With the fixed analog part, the original optimization problem in Section III-C is transformed as follows:

# $\mathcal{P}.2$ : Optimization for communication and sensing's digital part

$$\min_{\boldsymbol{P}_{\mathrm{C}},\boldsymbol{P}_{\mathrm{S}}} \mathrm{MSE}_{\mathrm{S}}(\boldsymbol{P}_{\mathrm{S}})$$
s.t.  $(15b) - (15d)$ .

Since  $P_{\rm S}$ ,  $P_{\rm C}$  and  $W_{\rm BB}$  are coupled in Eq. (5) in a non-convex manner,  $\mathcal{P}.2$  is still non-convex. Thus an alternating optimization algorithm is proposed to alternatively update  $\{P_{\rm S}, P_{\rm C}\}$  and  $W_{\rm BB}$ . For initialization, we set  $P_{\rm S}$ ,  $P_{\rm C}$ , and  $W_{\rm BB}$  as  ${\rm diag}(t)$ ,  $I_K$ , and  $W_{\rm BB,0}$ , respectively. For each iteration, the following two steps are executed in order.

1) Update  $P_{\rm S}$  and  $P_{\rm C}$  with fixed  $W_{\rm BB}$ .  $\mathcal{P}.2$  can be recast into the following problem with p and b as variables.

$$\min_{\boldsymbol{b},\boldsymbol{p}} \sum_{i=1}^{W} d_{i}(|\boldsymbol{a}_{N_{t}}^{H}(\theta_{i})\boldsymbol{F}_{S}[:,i]|b_{i}-t_{i})^{2}$$

$$s.t. \|\operatorname{diag}(\boldsymbol{p})\|_{F}^{2} \leq K,$$

$$\|\boldsymbol{D}^{\frac{1}{2}}\boldsymbol{b}\|_{F}^{2} \leq T_{R},$$

$$\frac{N_{C}}{K} \|\boldsymbol{W}_{BB}\boldsymbol{H}_{C}\operatorname{diag}(\boldsymbol{p}) - \boldsymbol{I}_{K}\|_{F}^{2}$$

$$+ \|\boldsymbol{D}^{\frac{1}{2}}\boldsymbol{W}_{BB}\boldsymbol{H}_{S}\operatorname{diag}(\boldsymbol{b})\|_{F}^{2} + \sigma^{2}\|\boldsymbol{W}_{BB}\|_{F}^{2} \leq \Gamma. \quad (23)$$

Since both the objective function and constraints are quadratic, the above problem is a convex quadratically constrained quadratic program (QCQP) problem, which can be solved via convex optimization toolbox [34].

2) Update  $W_{\rm BB}$  with fixed  $P_{\rm S}$  and  $P_{\rm C}$  according to Eq. (5). The overall alternating algorithm is presented in Algorithm 3.

# <span id="page-6-4"></span>V. ISAC PERFORMANCE ANALYSIS

<span id="page-6-6"></span><span id="page-6-0"></span>In this section, the complexity and convergence performance of the proposed algorithm are theoretically analyzed. The APEP and CRB are derived to illustrate the theoretical

<span id="page-7-0"></span>**Algorithm 3** Alternating Optimization Algorithm for Optimizing Communication and Sensing's Digital Part

Input:  $H_{\rm C}$ ,  $H_{\rm S}$ ,  $N_{\rm C}$ , K,  $\sigma$ .

1: Set  $P_{\rm S}^{(0)}={\rm diag}(t)$ ,  $P_{\rm C}^{(0)}=I_K$  and  $W_{\rm BB}^{(0)}=W_{\rm BB,0}$ .

2: repeat

3: Update  $P_{\rm S}^{(i+1)}$  and  $P_{\rm C}^{(i)}$  with fixed  $W_{\rm BB}^{(i)}$  by solving QCQP problem (23).

4: Update  $W_{\rm BB}^{(i+1)}$  with  $P_{\rm S}^{(i+1)}$  and  $P_{\rm C}^{(i+1)}$  as Eq. (5).

5: until the value of the objective function converges.

Output:  $P_{\rm S}$ ,  $P_{\rm C}$ ,  $W_{\rm BB}$ .

performance of communication and sensing. In addition, the number of RF chains for sensing are discussed.

### A. Complexity Analysis

The complexity of the analog part design with MBS structures has been derived in Section IV-A. For algorithm 1, the worst-case theoretical complexity of the B&B algorithm is  $\mathcal{O}(2^{BN_t})$ , but the pruning rules can substantially reduce actual solving time. For algorithm 2, the overall complexity includes the initialization process and entry-wise iteration. For initialization, the problem in proposition 2 can be transformed into mix-integer linear programming problems and solved by the branch and bound algorithm, the complexity of which is  $\mathcal{O}(2^{BN_{\mathrm{t}}K})$ . Since the initialization scheme is only applied to low-bit cases, the complexity is acceptable. The complexity of the entry-wise iteration part is  $\mathcal{O}(N_{\text{iter}}K(N_{\text{t}}+N_{\text{r}})2^{B})$ , where  $N_{\text{iter}}$  denotes the number of iterations. For algorithm 3, the complexity of solving QCQP problems is  $\mathcal{O}(N'_{\text{iter}}(T^{3.5} +$  $W^{3.5})\log(1/\epsilon)$  [35] by the interior-point method given accuracy level  $\epsilon$ , where  $N'_{\text{iter}}$  is the number of iteration rounds.

# <span id="page-7-4"></span>B. Convergence Analysis

Algorithm 1 has a finite number of operational steps. Algorithm 2 converges because the objective function is non-increasing and is lower-bounded by 0. For Algorithm 3, the convergence and existence of the solution are not obvious and analyzed as below. For the first iteration, it can be observed that  $\boldsymbol{b}^{(1)} = \mu \boldsymbol{t}$  and  $\boldsymbol{p}^{(1)} = \boldsymbol{p}^{(0)}$  are the feasible solution for the first step. Therefore, a solution must exist in the first iteration. Suppose after *i*-th iteration, all constraints are satisfied. During (i+1)-th iteration, denote the objective value at step j as  $\varepsilon_j$ . For step 1), we have

$$\varepsilon_1(\boldsymbol{b}^{(i+1)}) \le \varepsilon_1(\boldsymbol{b}^{(i)}),$$
 (24)

and all constraints except for Eq. (5) are satisfied. After step 2), Eq. (5) is satisfied and

$$\varepsilon_3(\boldsymbol{b}^{(i+1)}) = \varepsilon_2(\boldsymbol{b}^{(i+1)}). \tag{25}$$

It is worth noting that the constraint (15b) is still satisfied since  $\boldsymbol{W}_{\mathrm{BB}}^{(i+1)}$  is the LMMSE equalizer, which further lowers the symbol MSE. Therefore, after (i+1)-th iteration, we have

$$\varepsilon_3(\boldsymbol{b}^{(i+1)}) \le \varepsilon_1(\boldsymbol{b}^{(i)}),$$
 (26)

<span id="page-7-1"></span>![](_page_7_Figure_14.jpeg)

Fig. 2. Algorithm 3's convergence behaviour with  $N_{\rm r}=32$ . (a):  $N_{\rm t}=32$ ,  $\mu=0.1,0.5,0.8$ ; (b):  $N_{\rm t}=32,64,128,\,\mu=0.1$ .

i.e., the objective function is non-increasing and all constraints are satisfied. Recalling that the objective value is lower bounded, the convergence of the proposed alternating optimization is guaranteed. For the optimality of the convergence point, we have the following proposition.

Proposition 3: It can be proven that the convergence point of Algorithm 3 satisfies the Karush-Kuhn-Tucher (KKT) conditions of  $\mathcal{P}.2$ .

<span id="page-7-3"></span>*Proof:* See Appendix 
$$\mathbb{C}$$
.

In Fig. 2, we set the convergence tolerance as 0.001 and the convergence performance of Algorithm 3 with different  $\mu$  and  $N_t$  is presented. It can be observed that the convergence speed slows down as the value of  $\mu$  decreases and the number of transmit antennas increases.

## C. APEP Analysis

The APEP is derived to illustrate the theoretical BER performance of the proposed scheme. Due to the presence of finite-bit PSs and digital part optimization, obtaining an exact APEP is challenging. For simplicity, we analyze sub-beamspace with MBS and the unoptimized digital part, assuming infinite sensing interference power.

Firstly, we explain how the number of effective paths decreases due to the interference of sensing beams. As shown in Fig. 3, there are P=7 paths in the original  $N_{\rm r}\times N_{\rm t}=7\times 7$  beamspace channel and we neglect the off-grid beam leakage. BPM refers to the communication-only version of the proposed approach. For BPM-ISAC, W sensing beams cover  $M_{\rm R}=3$  paths, which further cover  $M_{\rm B}=2$  received beams. For example, the path  $\bar{H}(1,2)$  cannot be used for communication because its received beam will be interfered with by  $\bar{H}(1,5)$ . Therefore, the communication paths can only be chosen from the rest unaffected  $(N_{\rm t}-W)\times(N_{\rm r}-M_{\rm B})$  beam pairs. In this case, the number of effective paths is  $M_{\rm C}=3$ . In proposition 4, the probability distribution of the number of effective paths is derived.

<span id="page-7-2"></span>Proposition 4: For the case where the mmWave channel contains P paths and there are W sensing beams, the probability distribution of the number of effective communication

<span id="page-8-0"></span>![](_page_8_Figure_2.jpeg)

Fig. 3. An illustration of beamspace channel for BPM and BPM-ISAC.

<span id="page-8-1"></span>![](_page_8_Figure_4.jpeg)

Fig. 4. The probability distribution of the number of effective paths with  $N_{\rm r}=32$ . (a): W=3; (b):  $N_t=32$ .

paths is

$$P(M_{\rm C} = c) = \begin{cases} P_{M_{\rm R}}(0), c = P \\ \sum_{r=1}^{P-c} \sum_{b=1}^{r} P_{M_{\rm R}}(r) P_{M_{\rm B}}(r, b) P_{M_{\rm C}}(c, r, b), \\ c = 0, \dots, P - 1. \end{cases}$$
(27)

where

$$P_{M_{\rm R}}(r) = \frac{C_{N_{\rm r}(N_{\rm t}-W)}^{P-r}C_{N_{\rm r}W}^{r}}{C_{N_{\rm t}N_{\rm r}}^{P}},$$

$$\left\{P_{M_{\rm B}}(r-1,b-1)\frac{(N_{\rm r}-b+1)W}{N_{\rm r}W-r+1}\right\}$$
(28)

$$P_{M_{\rm B}}(r,b) = \begin{cases} P_{M_{\rm B}}(r-1,b-1) \frac{(N_{\rm r}-b+1)W}{N_{\rm r}W-r+1} \\ +P_{M_{\rm B}}(r-1,b) \frac{bW-r+1}{N_{\rm r}W-r+1}, o.w. \\ 0, \qquad (r,b) = (1,1) \quad or \quad b = 0. \end{cases}$$

$$P_{M_{\rm C}}(c,r,b) = \frac{C_{b(N_{\rm t}-W)}^{P-r-c}C_{(N_{\rm r}-r)(N_{\rm t}-W)}^{c}}{C_{N_{\rm r}(N_{\rm t}-W)}^{P-r}}.$$
(30)

<span id="page-8-2"></span>*Proof:* See Appendix D.

In Fig. 4, the probability of the number of effective paths  $M_C \geq c$  is given. It can be observed that a larger number of transmit antennas and fewer sensing beams will render more effective communication beams.

Proposition 5: For the case where the mmWave channel contains P paths and there are W sensing beams, the pairwise error probability  $P(\bar{x}_C \to \hat{x}_C)$  through maximum-likelihood (ML) detection algorithm is derived as Eq. (31), shown at the bottom of the next page.

*Proof:* See Appendix E.  $\Box$ 

Then the expression of APEP is derived as

$$P_{\text{APEP}} = \frac{1}{\eta 2^{\eta}} \sum_{\bar{\boldsymbol{x}}_C} \sum_{\hat{\boldsymbol{x}}_C} P(\bar{\boldsymbol{x}}_C \to \hat{\boldsymbol{x}}_C) e(\bar{\boldsymbol{x}}_C, \hat{\boldsymbol{x}}_C), \quad (32)$$

where  $P(\bar{x}_C \to \hat{x}_C)$  is given by proposition 5 and  $e(\bar{x}_C, \hat{x}_C)$  denotes the number of error bits between  $\bar{x}_C$  and  $\hat{x}_C$ .

As shown in Eq. (31), compared to GBM [18], the change in APEP originates from the damage caused by additional sensing beams to the effective communication paths. In fact, GBM is a special case of BPM-ISAC when W=0, i.e.,

<span id="page-8-3"></span>
$$P(M_{\rm C} = c) = \begin{cases} 1, c = P \\ 0, c = 0, \dots, P - 1. \end{cases}$$
 (33)

It is noted that the reduction in effective communication paths lowers the lower bound of APEP, denoted as  $P_{\rm APEP}^*$ . As the noise approaches zero, APEP of BPM-ISAC approaches its lower bound, given by

$$P_{\text{APEP}}^* = \frac{1}{\eta 2^{2\eta}} P\left(M_{\text{C}} < K\right) \sum_{\bar{\boldsymbol{x}}_{\text{C}}} \sum_{\hat{\boldsymbol{x}}_{\text{C}}} e(\bar{\boldsymbol{x}}_{\text{C}}, \hat{\boldsymbol{x}}_{\text{C}}). \tag{34}$$

Therefore, the number of sensing beams determines the boundary of the theoretical BER performance.

#### D. CRB Analysis

<span id="page-8-5"></span>To further illustrate the sensing performance of the proposed scheme, the CRB [36] of DoA estimation is derived. Employing the Swerling-II model [37], the reflection coefficient  $\beta_i$  is assumed to be constant during each scanning. According to Eq. (9), for L sample times per scanning, the baseband signal  $Y_{\rm B} = [y_{\rm B}^1, \ldots, y_{\rm B}^L]$  can be derived as

<span id="page-8-10"></span><span id="page-8-9"></span>
$$\boldsymbol{Y}_{\mathrm{B}} = \boldsymbol{T}_{\mathrm{B}}^{\mathrm{H}} \Xi \boldsymbol{T}_{\mathrm{B}} \boldsymbol{P}_{\mathrm{S}} \bar{\boldsymbol{X}}_{\mathrm{S}} + \boldsymbol{N}_{\mathrm{B}}, \tag{35}$$

<span id="page-8-6"></span>where  $\bar{X}_{\mathrm{S}} = [\bar{x}_{\mathrm{S}}^{1}, \ldots, \bar{x}_{\mathrm{S}}^{L}]$ .  $\bar{x}_{\mathrm{S}}^{l}$  and  $y_{\mathrm{B}}^{l}$  are the transmitted sensing signal and baseband received echo signal of the l-th sample.  $Y_{\mathrm{B}}$  obeys complex Gaussian distribution  $\mathcal{CN}(M_{\mathrm{Y}}, R_{\mathrm{Y}})$ , where  $M_{\mathrm{Y}} = T_{\mathrm{B}}^{\mathrm{H}} \Xi T_{\mathrm{B}} P_{\mathrm{S}} \bar{X}_{\mathrm{S}}$  and  $R_{\mathrm{Y}} = R_{\mathrm{B}}$ . For the target located in the direction of  $\psi_{i}$ , given the directions of other targets, the CRB of its DoA estimation can be obtained as follows (See [36], Section 8.2.3):

<span id="page-8-4"></span>
$$\overline{\text{CRB}}(\psi_i)$$

<span id="page-8-8"></span><span id="page-8-7"></span>(30) 
$$= \left\{ -\operatorname{Tr} \left( \frac{\partial \mathbf{R}_{Y}^{-1}}{\partial \psi_{i}} \frac{\partial \mathbf{R}_{Y}}{\partial \psi_{i}} \right) + 2\Re \left\{ \operatorname{Tr} \left( \frac{\partial \mathbf{M}_{Y}^{H}}{\partial \psi_{i}} \mathbf{R}_{Y}^{-1} \frac{\partial \mathbf{M}_{Y}}{\partial \psi_{i}} \right) \right\} \right\}^{-1}$$

$$= \left\{ 2\Re \left\{ \operatorname{Tr} \left( \frac{\partial \left( \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S} \right)^{H}}{\partial \psi_{i}} \mathbf{R}_{B}^{-1} \frac{\partial \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S}}{\partial \psi_{i}} \right) \right\} \right\}^{-1}$$

$$= \left\{ 2\Re \left\{ \operatorname{Tr} \left( \frac{\partial \left( \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S} \right)^{H}}{\partial \psi_{i}} \mathbf{R}_{B}^{-1} \frac{\partial \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S}}{\partial \psi_{i}} \right) \right\} \right\}^{-1}$$

$$= \left\{ 2\Re \left\{ \operatorname{Tr} \left( \frac{\partial \left( \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S} \right)^{H}}{\partial \psi_{i}} \mathbf{R}_{B}^{-1} \frac{\partial \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S}}{\partial \psi_{i}} \right) \right\} \right\}^{-1}$$

$$= \left\{ 2\Re \left\{ \operatorname{Tr} \left( \frac{\partial \left( \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S} \right)^{H}}{\partial \psi_{i}} \mathbf{R}_{B}^{-1} \frac{\partial \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S}}{\partial \psi_{i}} \right) \right\} \right\}^{-1}$$

$$= \left\{ 2\Re \left\{ \operatorname{Tr} \left( \frac{\partial \left( \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S} \right)^{H}}{\partial \psi_{i}} \mathbf{R}_{B}^{-1} \frac{\partial \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S}}{\partial \psi_{i}} \right) \right\} \right\}^{-1}$$

$$= \left\{ 2\Re \left\{ \operatorname{Tr} \left( \frac{\partial \left( \mathbf{T}_{B}^{H} \Xi \mathbf{T}_{B} \mathbf{P}_{S} \bar{\mathbf{X}}_{S} \right)^{H} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S} \mathbf{T}_{S}$$

Taking the expectation of  $\overline{\text{CRB}}(\psi_i)$  with respect to  $\bar{X}_{\text{S}}$  and considering  $R_{\bar{x}_{\text{S}}} = D$ , the final expression is written as

$$\operatorname{CRB}(\psi_{i}) = \frac{1}{2|\beta_{i}|^{2}} \left( Tr \left( \mathbf{P}_{S}^{H} \mathbf{F}_{S}^{H} \dot{\mathbf{A}}_{i}^{H} \mathbf{F}_{S} \mathbf{R}_{B}^{-1} \mathbf{F}_{S}^{H} \dot{\mathbf{A}}_{i} \mathbf{F}_{S} \mathbf{P}_{S} \mathbf{D} \right) \right)^{-1},$$
(37)

where  $\dot{A}_i = \dot{a}(\psi_i)a^{\rm H}(\psi_i) + a(\psi_i)\dot{a}^{\rm H}(\psi_i)$ . Furthermore, denoting matrix  $F_{\rm S}^{\rm H}A_i^{\rm H}F_{\rm S}R_{\rm B}^{-1}F_{\rm S}^{\rm H}A_iF_{\rm S}$  as M, the CRB can be expressed in the following form:

$$CRB(\psi_i) = \frac{1}{2|\beta_i|^2 \sum_{i=1}^{W} b_i^2 d_i M_{ii}}.$$
 (38)

Clearly, M is a positive definite matrix, and  $M_{ii} \geq 0$ . With the fixed activation probability  $d_i$  and the analog precoder, a higher transmission power results in a lower CRB. Therefore, sensing beampattern MSE minimization under a given transmission power constraint helps improve the performance of DoA estimation.

#### E. Extension to Multiple RF Chains for Sensing

In the previous modeling, only a single RF chain is dedicatedly spared for sensing. Indeed, the number of RF chains can be extended to  $W_S$ , where  $1 \leq W_S \leq W$ . In this case, there are  $W_S$  out of W beams simultaneously activated, resulting in a total of  $\mathbf{C}_W^{W_S}$  patterns. The activation probability matrix D is no longer a diagonal matrix and is determined by the predefined activation probability of each pattern. For instance, when  $W_S = W$ , D becomes a matrix filled with 1. By substituting the correct matrix D, the proposed transceiver design can be easily applied to the scenario with multiple RF chains for sensing. It is worth noting that increasing the number of RF chains for sensing can accelerate scanning speed, improving sensing accuracy, especially in high dynamic scenarios. Nevertheless, such an improvement comes at the cost of increased hardware overhead. Therefore, the selection of the number of sensing RF chains should carefully balance the sensing efficiency and hardware cost.

# VI. SIMULATIONS

<span id="page-9-0"></span>In this section, we evaluate the communication and sensing performance of the proposed BPM-ISAC method through numerical simulation. We consider a hybrid mmWave ISAC system, where  $N_{\rm t}=N_{\rm r}=N_{\rm e}=32$  unless otherwise

<span id="page-9-2"></span>![](_page_9_Figure_11.jpeg)

Fig. 5. BER comparison among BPM-ISAC-MBS ( $\mu=0.5$ ), its variants, and other transceiver designs ( $\eta=8$  bps/Hz).

<span id="page-9-3"></span>![](_page_9_Figure_13.jpeg)

Fig. 6. BER performance of BPM-ISAC-MBS ( $N_{\rm r}=32$ ).

<span id="page-9-1"></span>specified. Suppose there are P=8 non-line-of-sight (NLoS) paths with  $\alpha_i \sim \mathcal{CN}(0,1)$ , and  $\theta_i$  and  $\phi_i$  are uniformly distributed in  $[-\pi/2,\pi/2)$ . For communication, we adopt 4-QAM modulation and set K=4,  $N_{\rm C}=3$ , and L=20. For sensing, we set W=3 and  $T_{\rm R}=5$ . Without loss of generality, we assume two targets are located at  $\psi_1=39^\circ$  and  $\psi_2=43^\circ$  with reflection coefficients of  $|\beta_1|=|\beta_2|=1$ . The scanning directions of interest is set as  $[38^\circ,44^\circ,50^\circ]$ . The ideal beampattern is  $t=\sqrt{T_{\rm R}}\mathbf{1}_W$  and the activation

$$P(\bar{\boldsymbol{x}}_{\mathrm{C}} \to \hat{\boldsymbol{x}}_{C}) \simeq \sum_{c=K}^{P} \frac{c! P\left(M_{\mathrm{C}} = c\right)}{(c-K)!} \left( \frac{\mathbb{B}\left(\sum_{i=1}^{K} \left(\frac{N_{\mathrm{t}} N_{\mathrm{r}}}{4P\sigma^{2}} \triangle x_{i}^{2} + 1\right), c - K + 1\right)}{12 \prod_{j=2}^{K} \sum_{i=j}^{K} \left(\frac{N_{\mathrm{t}} N_{\mathrm{r}}}{4P\sigma^{2}} \triangle x_{i}^{2} + 1\right)} + \frac{\mathbb{B}\left(\sum_{i=1}^{K} \left(\frac{N_{\mathrm{t}} N_{\mathrm{r}}}{3P\sigma^{2}} \triangle x_{i}^{2} + 1\right), c - K + 1\right)}{4 \prod_{j=2}^{K} \sum_{i=j}^{K} \left(\frac{N_{\mathrm{t}} N_{\mathrm{r}}}{3P\sigma^{2}} \triangle x_{i}^{2} + 1\right)} + \frac{1}{2^{\eta}} P\left(M_{\mathrm{C}} < K\right).$$
(31)

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

Fig. 7. BER performance of BPM-ISAC-MBS and BPM-ISAC-MAS ( $\mu$ =0.5).

<span id="page-10-1"></span>![](_page_10_Figure_4.jpeg)

Fig. 8. Instantaneous normalized beampattern with BPM-ISAC-MBS and BPM-ISAC-MAS ( $\mu$ =0.5 or 0.8, sensing beam points at 38°).

probability matrix is  $D=\frac{1}{W}I_W$ . For algorithms 2 and 3, convergence tolerance is set as 0.001, and the maximum number of iterations is set as 50. The signal-to-noise ratio (SNR) is defined as  $\frac{E_b}{N_0}=\frac{N_{\rm C}}{\eta\sigma^2}$ .

To simplify the representation, 'BPM-ISAC-MBS' and 'BPM-ISAC-MAS' denote our proposed method with MBS and MAS, respectively. For comparison, some relevant methods and variants are introduced. 'SPIM-ISAC' refers to [22] which utilizes K strongest spatial paths for communication and 'GBM' refers to [18]. 'P-BPM-ISAC' denotes the plain version of 'BPM-ISAC-MBS', which utilizes K beams simultaneously without index modulation. 'BPM-ISAC-MBS' with maximum SINR-based beam selection criterion is also presented, i.e., the beam pairs with the largest signal-to-interference-plus-noise-ratio (SINR) are selected, where the SINR of beam pairs (i, j) is defined as

SINR[i, j] = 
$$\frac{|\bar{\boldsymbol{H}}[i, j]|^2}{\sum_{k \in \mathcal{O}} |\bar{\boldsymbol{H}}[i, k]|^2 + \sigma^2}.$$
 (39)

For 'EDC-ISAC', fully digital architecture is adopted and eigenvectors corresponding to K largest eigenvalue of the spatial channel are utilized to construct EDC.

#### A. Communication Performance

In Fig. 5, we compare the BER performance of BPM-ISAC-MBS with  $\mu=0.5$ , its variants, and other schemes. For a fair comparison, all schemes adopt the 4-QAM modulation to keep the same SE as 8 bps/Hz. SPIM-ISAC [22] exhibits high BER at high SNR due to severe sensing interference. BPM-ISAC-MBS with max-SINR beam selection criterion performs worse, indicating the advantage of the proposed min-MSE criterion. In high SNR regions, BPM-ISAC demonstrates lower BER than P-BPM-ISAC, highlighting the superiority of beam pattern modulation. In addition, the performance of GBM is provided as a reference, which is the special case of BPM-ISAC-MBS without sensing interference.

In Fig. 6, the BER performance of BPM-ISAC-MBS with different  $N_{\rm t}$  and  $\mu$  is presented. As  $\mu$  increases, strengthening the communication constraint, the BER performance gradually decreases. The BER performance of  $N_{\rm t}=64$  is better than the case of  $N_{\rm t}=32$  due to the array gain. The BER performance with the on-grid beamspace channel and unoptimized digital precoder is presented, which is consistent with APEP analysis at high SNR regions. The APEP lower bound is also presented according to Eq. (34). It can be observed that the on-grid case has better BER performance than the normal case at the low SNR region. This is due to that Gaussian noise is the main interference factor at low SNR and the communication beams of the on-grid case have more concentrated energy without beam leakage. At high SNR, sensing interference becomes the main interference and these two cases perform similarly.

In Fig. 7, the BER performance of BPM-ISAC-MBS and BPM-ISAC-MAS with different bit resolutions are illustrated. For BPM-ISAC-MAS, the BER decreases with the increase in bit number due to the higher freedom degree of the optimized beam pattern. In addition, the BER performance of MISDP-initialized BPM-ISAC-MAS with 1-bit PSs is presented. To reduce computation time,  $F_{\rm C}$  and  $W_{\rm RF}$  have been optimized only once alternatively. It is observed that with proper initialization, the BER of 1-bit BPM-ISAC-MAS approaches BPM-ISAC-MBS at high SNR.

#### B. Sensing Performance

In Fig. 8, we present the normalized beampattern of the proposed method at a certain moment when the sensing beam pointing at 38°. It can be observed that the strongest beam points in the direction of interest, while multiple other beams are activated for communication. Due to the discrete codewords, there exists a certain deviation from the desired direction for BPM-ISAC-MBS, which can be neglected for massive antennas. Compared with BPM-ISAC-MBS based on beamspace, BPM-ISAC-MAS offers a more flexible beam pattern, enhancing the equality of the equivalent digital channel.

In Fig. 9, the beampattern MSE versus weighting coefficient  $\mu$  is presented to illustrate the beampattern performance of the proposed method under different  $\mu$  values. The beampattern

<span id="page-11-2"></span>![](_page_11_Figure_2.jpeg)

Fig. 9. Sening beampattern MSE of BPM-ISAC-MBS and BPM-ISAC-MAS.

<span id="page-11-3"></span>![](_page_11_Figure_4.jpeg)

Fig. 10. The RMSE performance of BMUSIC-based DoA estimation algorithm versus sensing SNR ( $\mu=0.5$  or 0.8).

<span id="page-11-4"></span>![](_page_11_Figure_6.jpeg)

Fig. 11. BER and beampattern MSE performance trade-off among different ISAC transceiver designs (SNR = 0 dB).

MSE decreases with the increase of  $\mu$  because the augmented communication constraint compromises the power allocation of sensing beams. In addition, the BPM-ISAC-MBS without

communication digital precoder optimization has a higher beampattern MSE. This is because optimized communication power allocation can improve communication performance and implicitly relax the constraint on sensing power.

To further validate the sensing performance of the proposed method, root mean square error (RMSE) of DoA estimation versus sensing SNR using beamspace MUSIC algorithm [28] is shown in Fig. 10. The sensing SNR is defined as the ratio between the  $T_{\rm R}$  and the noise power of  $\xi_{\rm R}$ . It can be observed that, at high SNR, there are different gaps between the RMSE of DoA estimation and the ideal CRB defined in Eq. (36). This is due to the varying degrees of suppression of sensing power under different constraints. The performance of DoA estimation is generally consistent with the beampattern performance, indicating the effectiveness of choosing the beampattern as the sensing performance metric.

### C. Communication and Sensing Trade-off

In Fig. 11, the communication and sensing trade-off curves between BER and beampattern MSE among different schemes are presented for fair comparison. Within the testing scope, BPM-ISAC consistently outperforms other alternatives. It is notable that for large beampattern MSE, i.e., the sensing power is limited, the EDC-ISAC scheme achieves similar BER performance as BPM-ISAC-MBS with 2-bit PSs. However, as the sensing power increases, the BER performance of EDC-ISAC and SPIM-ISAC sharply deteriorates, whereas the proposed scheme demonstrates significant advantages thanks to effective optimization. BPM-ISAC-MBS with 2-bit PSs demonstrates an advantage over BPM-ISAC-MAS due to the higher degree of freedom of analog precoders. In addition, the performance of BPM-ISAC without digital-part optimization and P-BPM-ISAC are provided to demonstrate the effectiveness of power allocation and beam pattern modulation, respectively.

# VII. CONCLUSION

<span id="page-11-0"></span>In this paper, we have proposed a novel beam pattern modulation embedded mmWave ISAC hybrid transceiver design, termed BPM-ISAC. BPM-ISAC aims to retain the SE benefits of primitive beamspace modulation schemes while addressing performance bottlenecks in their extension to ISAC functionalities. To ensure near-optimal performance for BPM-ISAC, we formulated an optimization problem to minimize the sensing beampattern MSE under the symbol MSE constraint and solved it by optimizing analog and digital parts sequentially. Both the MBS and MAS hybrid structures are considered for analog configurations. Theoretical analysis and simulation results have verified that the proposed BPM-ISAC offers an overall improved trade-off in sensing and communication performance.

# <span id="page-11-1"></span>APPENDIX A PROOF OF PROPOSITION 1

At high SNR,  $\boldsymbol{W}_{\mathrm{BB},0}\simeq\boldsymbol{H}_{\mathrm{C}}^{\dagger}=(\boldsymbol{H}_{\mathrm{C}}^{\mathrm{H}}\boldsymbol{H}_{\mathrm{C}})^{-1}\boldsymbol{H}_{\mathrm{C}}^{\mathrm{H}}$ . Thus  $\frac{N_{\mathrm{C}}}{K}\|\boldsymbol{W}_{\mathrm{BB},0}\boldsymbol{H}_{\mathrm{C}}-\boldsymbol{I}_{K}\|_{F}^{2}\simeq0$  and the objective function is simplified as

$$\overline{\mathrm{MSE}}_{\mathrm{C}} \simeq \mathrm{Tr} \bigg( \left( \boldsymbol{W}_{\mathrm{RF}}^{\mathrm{H}} \boldsymbol{H} \boldsymbol{F}_{\mathrm{C}} \mathrm{diag} \left( \boldsymbol{t} \right)^{2} \boldsymbol{D} \boldsymbol{F}_{\mathrm{S}} \boldsymbol{H}^{\mathrm{H}} \boldsymbol{W}_{\mathrm{RF}} + \sigma^{2} \boldsymbol{I}_{K} \right)$$

$$\left(\boldsymbol{W}_{\mathrm{RF}}^{\mathrm{H}}\boldsymbol{H}\boldsymbol{F}_{\mathrm{C}}\boldsymbol{F}_{\mathrm{C}}^{\mathrm{H}}\boldsymbol{H}^{\mathrm{H}}\boldsymbol{W}_{\mathrm{RF}}\right)^{-1}\right). \tag{40}$$

<span id="page-12-11"></span>Let  $\overline{\mathrm{MSE}}_{\mathrm{C}} = \mathrm{Tr}\left(\frac{w}{K+T}\boldsymbol{I}_{K+T}\right)$ . With the Schur complement [38], it can be proved [39] that minimizing  $\overline{\mathrm{MSE}}_{\mathrm{C}}$  is equivalent to minimizing w and  $\mathcal{P}.1-2$  can be reformulated as shown in proposition 1.

# <span id="page-12-12"></span><span id="page-12-0"></span>APPENDIX B PROOF OF PROPOSITION 2

Let  $\bar{F} = F_{\rm C} F_{\rm C}^{\rm H}$ . For each element, we have

$$\bar{\boldsymbol{F}}[i,j] = \sum_{k=1}^{K} \boldsymbol{F}_{\mathrm{C}}[i,k] \overline{\boldsymbol{F}_{\mathrm{C}}[j,k]}$$

$$= \sum_{k=1}^{K} e^{j(\angle \boldsymbol{F}_{\mathrm{C}}[i,k] - \angle \boldsymbol{F}_{\mathrm{C}}[j,k])}$$

$$= \sum_{k=1}^{K} \cos \triangle \theta_{i,k,j,k} + j \sin \triangle \theta_{i,k,j,k}$$

$$= \sum_{k=1}^{K} c^{\mathrm{T}} \boldsymbol{y}^{i,k,j,k} + j s^{\mathrm{T}} \boldsymbol{y}^{i,k,j,k}, \tag{41}$$

where  $\triangle \theta_{i,k,j,k} = \angle \boldsymbol{F}_{\mathrm{C}}[i,k] - \angle \boldsymbol{F}_{\mathrm{C}}[j,k]$ . Thus  $\boldsymbol{F}_{\mathrm{C}}\boldsymbol{F}_{\mathrm{C}}^{\mathrm{H}}$  is transformed into the linear function of  $\boldsymbol{y}^{i,j,i',j'}$ .

# <span id="page-12-1"></span>APPENDIX C PROOF OF PROPOSITION 3

The lagrange function of  $\mathcal{P}.2$  is derived as

$$L(\boldsymbol{p}, \boldsymbol{b}, \lambda_{1}, \lambda_{2}, \lambda_{3})$$

$$= \sum_{i=1}^{W} d_{i}(|\boldsymbol{a}_{N_{t}}^{H}(\boldsymbol{\theta}_{i})\boldsymbol{F}_{S}[:, i]|b_{i} - t_{i})^{2}$$

$$+ \lambda_{1}(\|\operatorname{diag}(\boldsymbol{p})\|_{F}^{2} - K) + \lambda_{2}(\|\boldsymbol{D}^{\frac{1}{2}}\boldsymbol{b}\|_{F}^{2} - T_{R})$$

$$+ \lambda_{3}(\operatorname{MSE}_{C}(\boldsymbol{p}, \boldsymbol{b}) - \Gamma)$$
(42)

Denote the convergence solution of  $\mathcal{P}.2$  with alternating optimization algorithm as  $P_{\rm C}=p^*$  and  $P_{\rm S}=p^*$ . Denote  $W_{\rm BB}(p^*,b^*)$  as  $W_{\rm BB}^*$ . The KKT conditions of  $\mathcal{P}.2$  are given by

$$\begin{split} & \frac{\partial L}{\partial \boldsymbol{p}} \bigg|_{\boldsymbol{p} = \boldsymbol{p}^*} = \boldsymbol{0}, \frac{\partial L}{\partial \boldsymbol{b}} \bigg|_{\boldsymbol{b} = \boldsymbol{b}^*} = \boldsymbol{0}, \\ & \| \operatorname{diag}(\boldsymbol{p}^*) \|_F^2 \le K, \| \boldsymbol{D}^{\frac{1}{2}} \boldsymbol{b}^* \|_F^2 \le T_{\mathrm{R}}, \operatorname{MSE}_{\mathrm{C}}(\boldsymbol{p}^*, \boldsymbol{b}^*) \le \Gamma, \end{split}$$
(43a)

$$(43b)$$

$$\lambda_1 \geq 0, \lambda_2 \geq 0, \lambda_3 \geq 0,$$

$$\lambda_1(\|\operatorname{diag}(\boldsymbol{p}^*)\|_F^2 - K) = 0, \lambda_2(\|\boldsymbol{D}^{\frac{1}{2}}\boldsymbol{b}^*\|_F^2 - T_{\mathrm{R}}) = 0,$$

$$\lambda_3(\operatorname{MSE}_{\mathrm{C}}(\boldsymbol{p}^*, \boldsymbol{b}^*) - \Gamma) = 0$$

$$(43d)$$

For the convex QCQP problem (23) of the step 1),  $(p^*, b^*)$  is its optimal solution and naturally satisfies KKT conditions. Different from  $\mathcal{P}.2$ ,  $W_{\mathrm{BB}}$  in Problem (23) is fixed as constant matrix  $W_{\mathrm{BB}}^*$ . It is clear that in this case, constraint (43b),

(43c), and (43d) are satisfied. In addition, the stationarity condition satisfies

$$\left. \frac{\partial L(\boldsymbol{W}_{\mathrm{BB}} = \boldsymbol{W}_{\mathrm{BB}}^{*})}{\partial \boldsymbol{p}} \right|_{\boldsymbol{p} = \boldsymbol{p}^{*}} = 0, \left. \frac{\partial L(\boldsymbol{W}_{\mathrm{BB}} = \boldsymbol{W}_{\mathrm{BB}}^{*})}{\partial \boldsymbol{b}} \right|_{\boldsymbol{b} = \boldsymbol{b}^{*}} = 0$$
(44)

Note that condition (43a) holds only when the following condition is satisfied.

$$\frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{p})}{\partial \boldsymbol{p}}\bigg|_{\boldsymbol{p}=\boldsymbol{p}^{*}} = \frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{p}, \boldsymbol{W}_{\text{BB}} = \boldsymbol{W}_{\text{BB}}^{*})}{\partial \boldsymbol{p}}\bigg|_{\boldsymbol{p}=\boldsymbol{p}^{*}}, \tag{45a}$$

$$\frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{b})}{\partial \boldsymbol{b}}\bigg|_{\boldsymbol{b}=\boldsymbol{b}^{*}} = \frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{b}, \boldsymbol{W}_{\text{BB}} = \boldsymbol{W}_{\text{BB}}^{*})}{\partial \boldsymbol{b}}\bigg|_{\boldsymbol{b}=\boldsymbol{b}^{*}}. \tag{45b}$$

Taking (45a) as an example. According to the chain rule of differentiation, we have

<span id="page-12-10"></span><span id="page-12-8"></span>
$$\frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{p})}{\partial \boldsymbol{p}} \Big|_{\boldsymbol{p}=\boldsymbol{p}^{*}}$$

$$= \frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{p}, \boldsymbol{W}_{\text{BB}} = \boldsymbol{W}_{\text{BB}}^{*})}{\partial \boldsymbol{p}} \Big|_{\boldsymbol{p}=\boldsymbol{p}^{*}}$$

$$+ \frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{W}_{\text{BB}})}{\partial \boldsymbol{W}_{\text{BB}}} \Big|_{(\boldsymbol{p}, \boldsymbol{W}_{\text{BB}}) = (\boldsymbol{p}^{*}, \boldsymbol{W}_{\text{BB}}(\boldsymbol{p}^{*}))}$$

$$\frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{W}_{\text{BB}})}{\partial \boldsymbol{p}} \Big|_{\boldsymbol{p}=\boldsymbol{p}^{*}}.$$
(46)

Since Eq. (5) is satisfied for convergence solution,  $W_{\rm BB}$  is the LMMSE equalizer to minimize  ${\rm MSE_C}$  and satisfies

<span id="page-12-9"></span>
$$\frac{\partial \text{MSE}_{\text{C}}(\boldsymbol{W}_{\text{BB}})}{\boldsymbol{W}_{\text{BB}}} = 0. \tag{47}$$

Thus the second term on the right side of Eq. (46) is 0 and condition (45a) is satisfied. Similarly, condition (45b) is also satisfied. Then condition (43a) is satisfied. Therefore, the convergence point satisfies the KKT conditions of  $\mathcal{P}.2$ .

# <span id="page-12-2"></span>APPENDIX D PROOF OF PROPOSITION 4

<span id="page-12-7"></span><span id="page-12-5"></span><span id="page-12-4"></span>Let  $P_{M_{\rm R}}(r)$  and  $P_{M_{\rm B}}(r,b)$  represent the probability that sensing beams cover  $M_{\rm R}=r$  paths and these paths cover  $M_{\rm B}=b$  received beams, respectively. Let  $P_{M_{\rm C}}(c,r,b)$  represents the probability that  $M_{\rm C}=c$  paths are available for communication when  $M_{\rm R}=r$  and  $M_{\rm B}=b$ . Then the probability distribution of  $M_{\rm C}$  can be easily obtained as Eq. (27). Both  $P_{M_{\rm R}}(r)$  and  $P_{M_{\rm C}}(c,r,b)$  belong to the classical probability model and can be derived as Eq. (28) and Eq. (30) using the combination number formula. For  $P_{M_{\rm B}}(r,b)$ , we can obtain it through a recursive process as Eq. (29).

# <span id="page-12-3"></span>APPENDIX E PROOF OF PROPOSITION 5

<span id="page-12-6"></span>Supposing  $M_{\rm C} < K$ , effective communication cannot be achieved and BER is set to 0.5. When  $M_{\rm C} \ge K$ , denote  $\gamma_i =$ 

 $\frac{P}{N_{\rm t}N_{\rm r}}\boldsymbol{H}_{\rm C}^2[i,i]$  and  $\triangle x_i=\bar{\boldsymbol{x}}_{\rm C}[i]-\hat{\boldsymbol{x}}_C[i]$ , and then the pairwise error probability is given as

$$P(\bar{\boldsymbol{x}}_{\mathrm{C}} \to \hat{\boldsymbol{x}}_{C})$$

$$= \sum_{c=K}^{P} \mathbb{E}_{M_{\mathrm{C}}=c} \left\{ Q(\sqrt{\frac{\|\boldsymbol{H}_{\mathrm{C}}(\bar{\boldsymbol{x}}_{\mathrm{C}} - \hat{\boldsymbol{x}}_{C})\|_{2}^{2}}{2\sigma^{2}}}) \right\} + \frac{1}{2^{\eta}} P(M_{\mathrm{C}} < K)$$

$$\stackrel{(b)}{\simeq} \sum_{c=K}^{P} \mathbb{E}_{M_{\mathrm{C}}=c} \left\{ \frac{1}{12} \exp(-\frac{N_{\mathrm{t}}N_{\mathrm{r}}}{4P\sigma^{2}} \sum_{i=1}^{K} \gamma_{i}^{2} \triangle x_{i}^{2}) \right\}$$

$$+ \frac{1}{4} \exp(-\frac{N_{\mathrm{t}}N_{\mathrm{r}}}{3P\sigma^{2}} \sum_{i=1}^{K} \gamma_{i}^{2} \triangle x_{i}^{2}) \right\} + \frac{1}{2^{\eta}} P(M_{\mathrm{C}} < K),$$

$$[12]$$

$$(48)$$

where (b) is for that  $Q(x)\simeq \frac{1}{12}e^{-\frac{x^2}{2}}+\frac{1}{4}e^{-\frac{2x^2}{3}}$ . According to Eq. (3),  $\gamma_i$  follows a unit exponential distribution. Assume that K out of c largest paths are selected, satisfying  $\gamma_1<\gamma_2\cdots<\gamma_K$ . Thus the probability distribution of  $\gamma=[\gamma_1,\cdots,\gamma_K]^{\rm T}$  is given by

$$f(\gamma) = \frac{c!}{(c-K)!} (1 - e^{-\gamma_1})^{c-K} \prod_{i=1}^{K} e^{-\gamma_i}.$$
 (49)

Then the first item of Eq. (48) is derived as

$$\int_{0}^{+\infty} \int_{\gamma_{1}}^{+\infty} \cdots \int_{\gamma_{K-1}}^{+\infty} f(\gamma) e^{-\frac{N_{t}N_{r}}{4P\sigma^{2}} \sum_{i=1}^{K} \gamma_{i}^{2} \Delta x_{i}^{2}} d\gamma_{1} \cdots \gamma_{K}$$

$$= \frac{c!}{(c-K)! \prod_{j=2}^{K} n_{j}} \int_{0}^{+\infty} e^{-\gamma_{1}n_{1}} (1 - e^{-\gamma_{1}})^{c-K} d\gamma_{1}$$

$$= \frac{c!}{(c-K)! \prod_{j=2}^{K} n_{j}} \mathbb{B}(n_{1}, c - K + 1), \tag{50}$$

where  $n_j = \sum_{i=j}^K (\frac{N_{\rm t}N_{\rm r}}{4P\sigma^2} \triangle x_i^2 + 1)$  and  $\mathbb{B}(p,q) = \int_0^1 x^{p-1} (1-x)^{q-1} dx$  is the Beta function [40]. Similarly, we can obtain the second item of (48). Then, the pairwise error probability arrives at Eq. (31).

#### <span id="page-13-29"></span>REFERENCES

- B. Liu, S. Gao, Z. Yang, and X. Cheng, "Beam pattern modulation embedded mmWave hybrid transceiver design towards ISAC," in *Proc. IEEE 99th Veh. Technol. Conf. (VTC-Spring)*, Singapore, Jun. 2024, pp. 1–5.
- <span id="page-13-0"></span>[2] F. Liu et al., "Seventy years of radar and communications: The road from separation to integration," *IEEE Signal Process. Mag.*, vol. 40, no. 5, pp. 106–121, Jul. 2023.
- <span id="page-13-1"></span>[3] X. Cheng, D. Duan, S. Gao, and L. Yang, "Integrated sensing and communications (ISAC) for vehicular communication networks (VCN)," *IEEE Internet Things J.*, vol. 9, no. 23, pp. 23441–23451, Dec. 2022.
- <span id="page-13-2"></span>[4] X. Cheng et al., "Intelligent multi-modal sensing-communication integration: Synesthesia of machines," *IEEE Commun. Surveys Tuts.*, vol. 26, no. 1, pp. 258–301, 1st Quart., 2024.
- <span id="page-13-3"></span>[5] Y. Fan, S. Gao, D. Duan, X. Cheng, and L. Yang, "Radar integrated MIMO communications for multi-hop V2V networking," *IEEE Wireless Commun. Lett.*, vol. 12, no. 2, pp. 307–311, Feb. 2023.
- <span id="page-13-4"></span>[6] F. Liu et al., "Integrated sensing and communications: Toward dual-functional wireless networks for 6G and beyond," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 6, pp. 1728–1767, Jun. 2022.
- <span id="page-13-5"></span>[7] T. Huang, N. Shlezinger, X. Xu, Y. Liu, and Y. C. Eldar, "MAJoRCom: A dual-function radar communication system using index modulation," *IEEE Trans. Signal Process.*, vol. 68, pp. 3423–3438, 2020.

- <span id="page-13-6"></span>[8] D. Ma et al., "Spatial modulation for joint radar-communications systems: Design, analysis, and hardware prototype," *IEEE Trans. Veh. Technol.*, vol. 70, no. 3, pp. 2283–2298, Mar. 2021.
- <span id="page-13-7"></span>[9] J. Xu, X. Wang, E. Aboutanios, and G. Cui, "Hybrid index modulation for dual-functional radar communications systems," *IEEE Trans. Veh. Technol.*, vol. 72, no. 3, pp. 3186–3200, Mar. 2023.
- <span id="page-13-8"></span>[10] X. Gao, L. Dai, and A. M. Sayeed, "Low RF-complexity technologies to enable millimeter-wave MIMO with large antenna array for 5G wireless communications," *IEEE Commun. Mag.*, vol. 56, no. 4, pp. 211–217, Apr. 2018.
- <span id="page-13-9"></span>[11] F. Liu and C. Masouros, "Hybrid beamforming with sub-arrayed MIMO radar: Enabling joint sensing and communication at mmWave band," in *Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP)*, Sep. 2019, pp. 7770–7774.
- <span id="page-13-28"></span><span id="page-13-10"></span>[12] X. Wang, Z. Fei, J. A. Zhang, and J. Xu, "Partially-connected hybrid beamforming design for integrated sensing and communication systems," *IEEE Trans. Commun.*, vol. 70, no. 10, pp. 6648–6660, Oct. 2022.
- <span id="page-13-11"></span>[13] J. A. Zhang, X. Huang, Y. J. Guo, J. Yuan, and R. W. Heath Jr., "Multibeam for joint communication and radar sensing using steerable analog antenna arrays," *IEEE Trans. Veh. Technol.*, vol. 68, no. 1, pp. 671–685, Jan. 2019.
- <span id="page-13-12"></span>[14] Y. Zhuo, Z. Sha, and Z. Wang, "Multibeam joint communication and radar sensing: Beamforming design and interference cancellation," *IEEE Commun. Lett.*, vol. 26, no. 8, pp. 1888–1892, Aug. 2022.
- <span id="page-13-13"></span>[15] Z. Gao et al., "Integrated sensing and communication with mmWave massive MIMO: A compressed sampling perspective," *IEEE Trans. Wireless Commun.*, vol. 22, no. 3, pp. 1745–1762, Mar. 2023.
- <span id="page-13-14"></span>[16] A. Younis, N. Serafimovski, R. Mesleh, and H. Haas, "Generalised spatial modulation," in *Proc. 44th Asilomar Conf. Signals, Syst. Comput.*, Pacific Grove, CA, USA, Nov. 2010, pp. 1498–1502.
- <span id="page-13-15"></span>[17] Y. Ding, V. F. Fusco, A. P. Shitvov, Y. Xiao, and H. Li, "Beam index modulation wireless communication with analog beamforming," *IEEE Trans. Veh. Technol.*, vol. 67, no. 7, pp. 6340–6354, Jul. 2018.
- <span id="page-13-16"></span>[18] S. Gao, X. Cheng, and L. Yang, "Spatial multiplexing with limited RF chains: Generalized beamspace modulation (GBM) for mmWave massive MIMO," *IEEE J. Sel. Areas Commun.*, vol. 37, no. 9, pp. 2029–2039, Sep. 2019.
- <span id="page-13-17"></span>[19] Z. Yang, S. Gao, X. Cheng, and L. Yang, "Superposed IM-OFDM (S-IM-OFDM): An enhanced OFDM for integrated sensing and communications," *IEEE Trans. Veh. Technol.*, vol. 73, no. 10, pp. 15832–15836, Oct. 2024.
- <span id="page-13-18"></span>[20] D. Ma, T. Huang, N. Shlezinger, Y. Liu, and Y. C. Eldar, "Index modulation based ISAC," in *Integrated Sensing and Communications*. Cham, Switzerland: Springer, 2023, pp. 241–268.
- <span id="page-13-19"></span>[21] S. Guo, D. Cong, J. Ye, S. Dang, and N. Saeed, "Non-uniform beam pattern modulation for joint sensing and communication in 6G networks," in *Proc. 1st ACM MobiCom Workshop Integr. Sens. Commun. Syst.*, Oct. 2022, pp. 31–36.
- <span id="page-13-20"></span>[22] A. M. Elbir, K. V. Mishra, A. Celik, and A. M. Eltawil, "Millimeter-wave radar beamforming with spatial path index modulation communications," in *Proc. IEEE Radar Conf. (RadarConf23)*, May 2023, pp. 1–6.
- <span id="page-13-21"></span>[23] A. M. Elbir, K. V. Mishra, A. Abdallah, A. Celik, and A. M. Eltawil, "Spatial path index modulation in mmWave/THz band integrated sensing and communications," *IEEE Trans. Wireless Commun.*, vol. 23, no. 9, pp. 10788–10802, Sep. 2024.
- <span id="page-13-22"></span>[24] A. A. M. Saleh and R. Valenzuela, "A statistical model for indoor multipath propagation," *IEEE J. Sel. Areas Commun.*, vol. JSAC-5, no. 2, pp. 128–137, Feb. 1987.
- <span id="page-13-23"></span>[25] S. Gao, X. Cheng, and L. Yang, "Estimating doubly-selective channels for hybrid mmWave massive MIMO systems: A doublysparse approach," *IEEE Trans. Wireless Commun.*, vol. 19, no. 9, pp. 5703–5715, Sep. 2020.
- <span id="page-13-24"></span>[26] J. Guo, C. Wen, S. Jin, and G. Y. Li, "Overview of deep learning-based CSI feedback in massive MIMO systems," *IEEE Trans. Commun.*, vol. 70, no. 12, pp. 8017–8045, Dec. 2022.
- <span id="page-13-25"></span>[27] Z. Liu, S. Aditya, H. Li, and B. Clerckx, "Joint transmit and receive beamforming design in full-duplex integrated sensing and communications," *IEEE J. Sel. Areas Commun.*, vol. 41, no. 9, pp. 2907–2919, Sep. 2023.
- <span id="page-13-26"></span>[28] H. B. Lee and M. S. Wengrovitz, "Resolution threshold of beamspace MUSIC for two closely spaced emitters," *IEEE Trans. Acoust., Speech, Signal Process.*, vol. 38, no. 9, pp. 1545–1559, Sep. 1990.
- <span id="page-13-27"></span>[29] Z. Cheng and B. Liao, "QoS-aware hybrid beamforming and DOA estimation in multi-carrier dual-function radar-communication systems," IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1890–1905, Jun. 2022.

- <span id="page-14-0"></span>[\[30\]](#page-4-11) S. Gao, X. Cheng, and L. Yang, "Mutual information maximizing wideband multi-user (wMU) mmWave massive MIMO," *IEEE Trans. Commun.*, vol. 69, no. 5, pp. 3067–3078, May 2021.
- <span id="page-14-1"></span>[\[31\]](#page-5-4) D. R. Morrison, S. H. Jacobson, J. J. Sauppe, and E. C. Sewell, "Branch-and-bound algorithms: A survey of recent advances in searching, branching, and pruning," *Discrete Optim.*, vol. 19, pp. 79–102, Feb. 2016.
- <span id="page-14-2"></span>[\[32\]](#page-5-5) Z. Wang, M. Li, Q. Liu, and A. L. Swindlehurst, "Hybrid precoder and combiner design with low-resolution phase shifters in mmWave MIMO systems," *IEEE J. Sel. Topics Signal Process.*, vol. 12, no. 2, pp. 256–269, May 2018.
- <span id="page-14-3"></span>[\[33\]](#page-6-5) S.-X. Yu, M.-C. Lee, and T.-S. Lee, "Dynamic-connected hybrid precoding for MIMO-OFDM systems with low-resolution phase shifters," in *Proc. IEEE Global Commun. Conf. (GLOBECOM)*, Dec. 2022, pp. 2400–2406.
- <span id="page-14-4"></span>[\[34\]](#page-6-6) J. Lofberg, "YALMIP: A toolbox for modeling and optimization in MATLAB," in *Proc. IEEE Int. Conf. Robot. Autom.*, Taipei, Taiwan, Sep. 2004, pp. 284–289.
- <span id="page-14-5"></span>[\[35\]](#page-7-4) Z.-Q. Luo, W.-K. Ma, A. So, Y. Ye, and S. Zhang, "Semidefinite relaxation of quadratic optimization problems," *IEEE Signal Process. Mag.*, vol. 27, no. 3, pp. 20–34, May 2010.
- <span id="page-14-6"></span>[\[36\]](#page-8-9) H. L. Van Trees, *Optimum Array Processing: Part IV of Detection, Estimation, and Modulation Theory*. Hoboken, NJ, USA: Wiley, 2002.
- <span id="page-14-7"></span>[\[37\]](#page-8-10) M. I. Skolnik et al., *Introduction To Radar Systems*, vol. 3. New York, NY, USA: McGraw-Hill, 1980.
- <span id="page-14-8"></span>[\[38\]](#page-12-11) P. Chen, Z. Chen, Z. Cao, and X. Wang, "A new atomic norm for DOA estimation with gain-phase errors," *IEEE Trans. Signal Process.*, vol. 68, pp. 4293–4306, 2020.
- <span id="page-14-9"></span>[\[39\]](#page-12-12) B. Di, H. Zhang, L. Song, Y. Li, Z. Han, and H. V. Poor, "Hybrid beamforming for reconfigurable intelligent surface based multi-user communications: Achievable rates with limited discrete phase shifts," *IEEE J. Sel. Areas Commun*, vol. 38, no. 8, pp. 1809–1822, Aug. 2020.
- <span id="page-14-10"></span>[\[40\]](#page-13-29) I. S. Gradshteyn and I. M. Ryzhik, *Table of Integrals, Series, and Products*. New York, NY, USA: Academic, 2014.

![](_page_14_Picture_13.jpeg)

Boxun Liu (Graduate Student Member, IEEE) received the B.E. degree from the University of Electronic Science and Technology of China, Chengdu, China, in 2023. He is currently pursuing the Ph.D. degree with the School of Electronics, Peking University, Beijing, China. His current research interests include integrated sensing and communication (ISAC) and AI-empowered wireless system design.

Shijian Gao (Member, IEEE) received the Ph.D. degree from the University of Minnesota, Minneapolis, USA, in 2022. After graduation, he was a Senior RF Engineer with the Samsung SoC Laboratory, San Diego, USA. In February 2024, he joined the Internet of Things Thrust, The Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China, as an Assistant Professor. His research lies

![](_page_14_Picture_15.jpeg)

in the broad areas of statistical signal processing, wireless communication, RF systems, and machine learning. He was a co-recipient of the 2021 MICCAI Young Scientist Paper Award. He serves as an Associate Editor for *IET*

![](_page_14_Picture_17.jpeg)

![](_page_14_Picture_18.jpeg)

Zonghui Yang (Graduate Student Member, IEEE) received the B.S. degree from the Department of Electronic Engineering, Tsinghua University, Beijing, China, in 2022. He is currently pursuing the Ph.D. degree with the School of Electronics, Peking University, Beijing. His current research interests include AI-aided wireless communications and integrated sensing and communications.

![](_page_14_Picture_20.jpeg)

Xiang Cheng (Fellow, IEEE) received the joint Ph.D. degree from Heriot-Watt University and The University of Edinburgh, Edinburgh, U.K., in 2009. He is currently a Boya Distinguished Professor with Peking University. His research interests include channel modeling, wireless communications, and data analytics, the subject on which he has published more than 280 journals and conference papers, 11 books, and holds 30 patents. He was a recipient of the IEEE Asia–Pacific Outstanding Young Researcher Award in 2015 and the Xplorer Prize

in 2023. He was a co-recipient of the 2016 IEEE Journal on Selected Areas in Communications Best Paper Award, the Leonard G. Abraham Prize, the 2021 IET Communications Best Paper Award, and the Premium Award. He has also received the Best Paper Awards at IEEE ITST'12, ICCC'13, ITSC'14, ICC'16, ICNC'17, GLOBECOM'18, ICCS'18, and ICC'19. He has been a Highly Cited Chinese Researcher since 2020. In 2021 and 2023, he was selected into two world scientist lists, including the World's Top 2% Scientists released by Stanford University and top computer science scientists released by Guide2Research. He has served as the symposium lead chair, the co-chair, and a member of the technical program committee for several international conferences. He led the establishment of four Chinese standards (including industry standards and group standards) and participated in the formulation of ten 3GPP international standards and two Chinese industry standards. He is currently a Subject Editor of *IET Communications*; and an Associate Editor of IEEE TRANSACTIONS ON WIRELESS COM-MUNICATIONS, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, IEEE WIRELESS COMMUNICATIONS LETTERS, and *Journal of Communications and Information Networks*. He was a Distinguished Lecturer of the IEEE Vehicular Technology Society.

![](_page_14_Picture_23.jpeg)

Liuqing Yang (Fellow, IEEE) received the Ph.D. degree from the University of Minnesota, Minneapolis, MN, USA, in 2004. She has been a Faculty Member with the University of Florida, Colorado State University, and the University of Minnesota. She is currently a Chair Professor with The Hong Kong University of Science and Technology (Guangzhou), where she is also the Acting Director of the Low-Altitude Systems and Economy Research Institute (LASERi) and the Head of the Intelligent Transportation (INTR) Thrust. Her

research interests include communications, sensing, and networked intelligence, subjects on which she has published more than 400 journal and conference papers, four book chapters, and five books. She is a fellow of AAIA. She was a recipient of the ONR YIP Award in 2007, the NSF CAREER Award in 2009, and multiple best paper awards. She is an Executive Editorial Committee (EEC) Member of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS. She has also served as the Editor-in-Chief for *IET Communications*. She has also served on the editorial board for an array of elite journals, including IEEE TRANSACTIONS ON SIGNAL PROCESSING, IEEE TRANSACTIONS ON COMMUNICATIONS, and IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, in various roles of IEEE ComSoc and IEEE ITSS, and in leadership roles for many conferences.