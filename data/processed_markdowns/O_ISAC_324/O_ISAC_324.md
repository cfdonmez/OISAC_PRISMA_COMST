# **RESEARCH ARTICLE**

# **Integrated Distributed Sensing and Quantum Communication Networks**

**Yuehan Xu1 , Tao Wang1,2,3\* , Peng Huang1,2,3 , and Guihua Zeng1,2,3\***

State Key Laboratory of Advanced Optical Communication Systems and Networks, Center of Quantum Sensing and Information Processing, Shanghai Jiao Tong University, Shanghai 200240, China. 2 Shanghai Research Center for Quantum Sciences, Shanghai 201315, China. <sup>3</sup> Hefei National Laboratory, Hefei 230088, China.

\*Address correspondence to: [tonystar@sjtu.edu.cn](mailto:tonystar@sjtu.edu.cn) (T.W.); [ghzeng@sjtu.edu.cn](mailto:ghzeng@sjtu.edu.cn) (G.Z.)

The integration of sensing and communication can achieve ubiquitous sensing while enabling ubiquitous communication. Within the gradually improving global communication, the integrated sensing and communication system based on optical fibers can accomplish various functionalities, such as urban structure imaging, seismic wave detection, and pipeline safety monitoring. With the development of quantum communication, quantum networks based on optical fiber are gradually being established. In this paper, we propose an integrated sensing and quantum network (ISAQN) scheme, which can achieve secure key distribution among multiple nodes and distributed sensing under the standard quantum limit. The continuous variables quantum key distribution protocol and the round-trip multiband structure are adopted to achieve the multinode secure key distribution. Meanwhile, the spectrum phase monitoring protocol is proposed to realize distributed sensing. It determines which node is vibrating by monitoring the frequency spectrum and restores the vibration waveform by monitoring the phase change. The scheme is experimentally demonstrated by simulating the vibration in a star structure network. Experimental results indicate that this multiuser quantum network can achieve a secret key rate of approximately 0.7 Mbits/s for each user under 10-km standard fiber transmission, and its network capacity is 8. In terms of distributed sensing, it can achieve a vibration response bandwidth ranging from 1 Hz to 2 kHz, a strain resolution of 0.50 n*𝜀*∕ √ Hz, and a spatial resolution of 0.20 m under shot-noise-limited detection. The proposed ISAQN scheme enables simultaneous quantum communication and distributed sensing in a multipoint network, laying a foundation for future large-scale quantum networks and high-precision sensing networks.

**Citation:** Xu Y, Wang T, Huang P, Zeng G. Integrated Distributed Sensing and Quantum Communication Networks. *Research* 2024;7:Article 0416. [https://doi.](https://doi.org/10.34133/research.0416) [org/10.34133/research.0416](https://doi.org/10.34133/research.0416)

Submitted 2 April 2024 Accepted 28 May 2024 Published 5 August 2024

Copyright © 2024 Yuehan Xu et al. Exclusive licensee Science and Technology Review Publishing House. No claim to original U.S. Government Works. Distributed under a [Creative](https://creativecommons.org/licenses/by/4.0/)  [Commons Attribution License 4.0](https://creativecommons.org/licenses/by/4.0/)  [\(CC BY 4.0\).](https://creativecommons.org/licenses/by/4.0/)

# **Introduction**

In recent years, various communication networks have been applied worldwide, creating an era of interconnected information. Due to the sensitivity of communication media to environmental changes, communication media can be used not only for information transmission but also for sensing. Thus, the concept of integrated sensing and communication (ISAC) emerged. ISAC requires sensing to be conducted simultaneously during the communication process, rather than building a separate sensing network. Its goal is to achieve ubiquitous ISAC networks, providing large-scale sensing for urban structure imaging, seismic wave detection, pipeline safety monitoring, etc. Initially, ISAC was proposed in wireless communication. Recently, ISAC in optical communication has been implemented, enabling sensing demodulation while conducting optical communication. By using optical fibers as the transmission medium, ISAC can achieve high-speed communication while also achieving high-precision sensing.

Quantum communication is one of the most concerned communication methods. Quantum key distribution (QKD) is the core technology of quantum communication, providing secure keys for legitimate parties guaranteed by the basic principles of quantum mechanics [[1\]](#page-13-0). QKD was proposed in 1984, and researchers have currently completed its security proof, experimental verification, field verification, chip integration, and prototype implementation [\[2](#page-13-1)–[19](#page-13-2)]. Furthermore, several new protocols have been proposed and experimentally validated [[20](#page-13-3)–[25](#page-13-4)]. Beyond traditional point-to-point QKD system, QKD network [[26](#page-13-5)[–34\]](#page-13-6) can ensure that multiple users share quantum secure keys. It can be classified into backbone networks, metropolitan area networks, and access networks based on their coverage area. A typical backbone QKD network is the Beijing– Shanghai trunk line [\[35\]](#page-13-7), which achieves QKD transmission at a distance of over 4,600 km. In addition, the Cambridge QKD metropolitan area network is constructed with high-bandwidth data transmission [[36](#page-14-0)], which has been operating for several years with 3 nodes separated by 5- to 10-km optical fiber [[37](#page-14-1)]. The 46-node QKD metropolitan area network in Hefei realizes real-time voice telephone, text messaging, and file transmission [[38](#page-14-2)]. The implementation of a QKD access network for multiple users was proposed by Fröhlich et al. [[39](#page-14-3)] through an upstream quantum access network.

In the practical implementation of QKD, optical signals are used as the carrier for transmitting secure key information. They are very sensitive to changes in phase, amplitude, wavelength, etc., and environmental disturbances can cause corresponding changes. Pilot signals are commonly employed to eliminate those effects on QKD signals. This characteristic can in turn be used for distributed optical fiber sensing (DOFS). DOFS technology utilizes specific effects of vibration, acoustic, and temperature on the phase, amplitude, and wavelength of light in the optical fiber to achieve distributed fiber vibration sensing (DVS), distributed fiber acoustic sensing, and distributed fiber temperature sensing [[40](#page-14-4)[,41\]](#page-14-5). It is mainly divided into two types. One uses backscattering light to achieve sensing also known as phase-sensitive optical time-domain reflectometry (*ϕ*-OTDR [\[42](#page-14-6)[–51\]](#page-14-7)), while the other uses the forward-transmitting light to achieve sensing. The backscattering light sensing scheme can achieve a spatial resolution of 0.8 m, a strain resolution of about 0.25 n*𝜀*∕ √ Hz, and a vibration response bandwidth of 5 kHz along the total 9.8-km sensing fiber [[50\]](#page-14-8). The forwardtransmitting light scheme is capable of detecting earthquakes over terrestrial and submarine links with lengths ranging from 75 to 535 km and a geographical distance from the earthquake's epicenter ranging from 25 to 18,500 km [[52](#page-14-9)]. In addition, it can achieve a spatial resolution of 1 km in the frequency calibration fiber link of QKD [\[53\]](#page-14-10). Besides, quantum approaches can achieve higher detection precision [[54](#page-14-11)[,55](#page-14-12)], typically using entanglement, single photons, and squeezed states to surpass the standard quantum limit [\[56](#page-14-13)[–59\]](#page-14-14).

Recently, DOFS has been integrated into classical optical communication to enable both communication and sensing, thereby constructing an ISAC system [[60](#page-14-15)[–64\]](#page-14-16). Correspondingly, the integrated sensing and quantum communication system requires simultaneous sensing and QKD without additional devices, while ensuring there is no interference between the two procedures. Furthermore, an integrated sensing and quantum network (ISAQN) composed of multiple integrated sensing and quantum communication systems requires the differentiation of QKD signals and sensing signals from different nodes. Each network node can serve as a QKD node and also serve as a sensing node, thereby achieving ISAQN. However, two issues urgently need to be addressed. The first lies in the inability of weak QKD signals to achieve precise sensing, thus making it impossible to perform high-precision sensing based on QKD signals. Specifically, the average number of photons in QKD signals is very small, whereas the DOFS based on backscattering requires a strong optical signal. The second lies in the difficulty of discerning between multiple QKD signals and sensing signals. Since both sensing information and key information are loaded onto the same coherent state, extracting the key information and demodulating the sensing information pose challenges. Therefore, a reasonable scheme is needed to implement ISAQN.

In order to achieve signal sensing in multipoint QKD networks, we propose the time-frequency-multiplexing ISAQN. This scheme utilizes both quantum signals and pilot signals for transmission. Quantum signals are used for continuous variables QKD (CV-QKD), while pilot signals are used for sensing. Additionally, the pilot signal inserted by the time division multiplexing (TDM) can restore the phase of the quantum signal when there is no vibration. For multiple nodes, we use frequency division multiplexing (FDM) to transmit multiple QKD signals of different nodes. When the vibration is happening, the nodes experiencing vibrations can be determined and the vibration waveform can be restored based on the spectrum phase monitoring (SPM) protocol. The precision of ISAQN's distributed sensing can reach the standard quantum limit. To demonstrate the feasibility of our scheme, experiments were carried out by simulating the vibration in a star network structure with a network capacity of 8. The results indicate that this network can achieve a secret key rate (SKR) of approximately 0.7 Mbits/s under 10-km standard fiber transmission, a vibration response bandwidth ranging from 1 Hz to 2 kHz, a strain resolution of 0.50 n*𝜀*∕ √ Hz, and a spatial resolution of 0.20 m under shot-noise-limited detection.

In this paper, our ISAQN scheme is introduced in detail. First, we describe the physical structure of ISAQN and how it works. In addition, we have analyzed the theoretical principles of CV-QKD and DOFS. Based on this physical structure, we construct a proof-of-principle experiment and verify the feasibility of the ISAQN. Finally, we come up with a conclusion.

# **Results**

# **Integrated distributed sensing and quantum communication networks**

In order to achieve point-to-multipoint quantum communication and distributed sensing in the same network, we propose the timefrequency-multiplexing ISAQN. This network conducts quantum communication and sensing simultaneously through coherent states. Firstly, we will describe this point-to-multipoint quantum network in part 1. Secondly, we will explain how distributed sensing is integrated into this quantum network in part 2.

### *Point-to-multipoint quantum networks*

CV-QKD uses coherent states to distribute secure keys, thus ensuring the security of communication. The commonly used point-to-point Gaussian modulated coherent states (GMCS) CV-QKD protocol is shown in Table [1.](#page-2-0) However, this protocol does not directly support multipoint QKD. Therefore, we propose the round-trip structure for constructing the point-tomultipoint QKD network [[34](#page-13-6)], shown in Fig. [1.](#page-3-0) This network enables QKD between the center node and each of the child nodes. It can be understood that the child node is Alice and the center node is Bob in the classical scheme. As illustrated in Fig. [1](#page-3-0), the Telecommunication as center node performs pointto-multipoint QKD with Community, Supermarket, School, Government, and Factory as child nodes. In the round-trip structure, the center node holds the laser and detector for transmitting and receiving light, while each child node only performs quantum signal modulation. This process can be divided into two steps. First, light is transmitted from the center node to each child node, with every child node receiving 1/*N* of the light, where *N* is the network capacity. Subsequently, each child node modulates the quantum signal with information and transmits it back to the center node, resulting in a 1/*N* transmittance loss. The modulated coherent states from each child node are received at the center node, which aggregates the quantum state transmitted from every node. Therefore, it only requires a laser and a detector to efficiently complete a point-to-multipoint QKD network.

For the multipoint QKD network, differentiating quantum signals from different nodes is also a challenge. In the practical implementation, we use FDM to differentiate individual child

#### <span id="page-2-0"></span>Table 1. The steps of point-to-point GMCS CV-QKD

- 1. Alice selects 2 sets of Gaussian distributed random sequences  $x_A$  and  $p_A$ , with length n, mean 0, and variance of  $V_A$ . Based on these, n coherent states  $|x_A+jp_A\rangle$  are prepared by Alice and then transmitted to Bob through a quantum channel. The quantum channel can be characterized by the transmittance T and the noise  $\varepsilon$ .
- 2. After receiving the coherent state, Bob will simultaneously measure both quadrature components, which is heterodyne detection. The measurement results are denoted as  $x_B$  and  $p_B$ . The practical detector at Bob's input can be characterized with the quantum efficiency  $\eta$  and the electrical noise  $v_{el}$ .
- Because heterodyne detection is adopted, Alice retains all the data.
- 4. Alice randomly selects a portion of the retained data for parameter evaluation and publicly discloses this data. Bob estimates parameters based on the measurement data, including channel transmittance, channel excess noise, and modulation variance. Then, Bob evaluates the secure key rate using these parameters. If the secure key rate is less than 0, the key distribution is terminated and retransmitted.
- 5. Alice and Bob perform data postprocessing on the remaining data, including steps such as reverse reconciliation and privacy amplification. Eventually, both parties obtain the same secure key of *m* bits.

nodes in the point-to-multipoint QKD network. FDM is a multiplexing technique that facilitates the modulation of multiple base-band signals onto various carrier frequencies. In other words, different frequency bands are multiplexed by modulating the carrier wave at different rates, which can be equivalently represented as different rotation speeds in the phase space. In Fig. 1, when each child node receives a continuous wave, it modulates quantum signals at its respective carrier frequency and transmits them back to the center node. Subsequently, these signals are superimposed to form a multiband signal at the center node. During the demodulation process, different frequency bands are filtered to distinguish different child nodes. Hence, the multiband structure brought by FDM technology is suitable for QKD in multiuser networks. Although TDM is another feasible alternative, it necessitates tighter control over time slots.

In the following, we will provide a detailed description of the specific principles for implementing the round-trip multiband QKD network. First, the center node transmits a continuous wave to each child node. The i-th child node selects Gaussian distribution values  $x_i$  and  $p_i$  with equal probability, producing a random sequence of length n, mean 0, and variance of  $V_i$ . Then, the i-th child node creates n coherent states based on this random sequence, which can be represented as

<span id="page-2-1"></span>
$$|\alpha_i\rangle = |x_i + jp_i\rangle e^{j\omega_i t}, i \in \{1, 2, \dots, N\},$$
(1)

where j is the imaginary number unit, N denotes the network capacity,  $\alpha_i^2 = V_i/2 = V_A/2$ ,  $\omega_i$  is the carrier frequency of the i-th child node, and t represents time. We can expand the formula for the i-th child node's coherent state as

$$|x_i + jp_i\rangle e^{j\omega_i t} = |(x_i \cos(\omega_i t) - p_i \sin(\omega_i t)) + j(x_i \sin(\omega_i t) + p_i \cos(\omega_i t))\rangle,$$
(2)

where the real part  $x_i \cos{(\omega_i t)} - p_i \sin{(\omega_i t)}$  and the imaginary part  $x_i \sin{(\omega_i t)} + p_i \cos{(\omega_i t)}$  refer to the radio frequency signals respectively added to the two paths of the in-phase and quadrature modulator (IQM). When transmitted through optical fibers, the coherent state undergoes a rotation of angle  $\theta$ . Each child node experiences a different rotation angle, and  $\theta_i$  represents the rotation angle of the i-th child node. The splitter collects the signals modulated by every child node to form a signal with N frequency bands. Finally, the signal returns to the center node through the round-trip structure. Therefore, the coherent state received by the coherent detector can be expressed as

$$\sum_{i=1}^{N} |\alpha_{i}\rangle e^{j\theta_{i}}$$

$$= \sum_{i=1}^{N} |x_{i} + jp_{i}\rangle e^{j(\omega_{i}t + \theta_{i})}$$

$$= \sum_{i=1}^{N} |(x_{i} + jp_{i})\cos(\omega_{i}t + \theta_{i}) + j(x_{i} + jp_{i})\sin(\omega_{i}t + \theta_{i})\rangle.$$
(3)

The center node obtains a spectrum consisting of mixed multifrequency bands, which are difficult to distinguish in the time domain but can be clearly distinguished in the frequency domain. Then, the center node checks the frequency bands registered by the child nodes. The center node examines the registered frequency bands to determine which child nodes are currently communicating. This registration method can effectively prevent the unauthorized use of illegal frequency bands by Eve to steal information. For these legal bands, the center node uses band-pass filtering to isolate them. Therefore, the quantum signal of the *i*-th child node can be separated and expressed as

$$\begin{split} |\alpha_{i}\rangle e^{j\theta_{i}} &= |x_{i}+jp_{i}\rangle e^{j(\omega_{i}t+\theta_{i})} \\ &= |(x_{i}+jp_{i})\cos(\omega_{i}t+\theta_{i})+j(x_{i}+jp_{i})\sin(\omega_{i}t+\theta_{i})\rangle \\ &= |(x_{i}+jp_{i})(\cos(\omega_{i}t)\cos\theta_{i}-\sin(\omega_{i}t)\sin\theta_{i}) \\ &+ j(x_{i}+jp_{i})(\sin(\omega_{i}t)\cos\theta_{i}+\cos(\omega_{i}t)\sin\theta_{i})\rangle \\ &= |(x_{i}\cos(\omega_{i}t)\cos\theta_{i}-x_{i}\sin(\omega_{i}t)\sin\theta_{i}) \\ &- p_{i}\sin(\omega_{i}t)\cos\theta_{i}-p_{i}\cos(\omega_{i}t)\sin\theta_{i}) \\ &+ j(x_{i}\sin(\omega_{i}t)\cos\theta_{i}+x_{i}\cos(\omega_{i}t)\sin\theta_{i}) \\ &+ p_{i}\cos(\omega_{i}t)\cos\theta_{i}-p_{i}\sin(\omega_{i}t)\sin\theta_{i})\rangle, \end{split}$$

$$(4)$$

where the real part  $|Re(\alpha_i e^{j\theta_i})\rangle$  and imaginary part  $|Im(\alpha_i e^{j\theta_i})\rangle$  are respectively the two results detected by the heterodyne detection (also known as dual-homodyne detection). The center node can eliminate the carrier frequency of every child node via coherent demodulation, obtaining base-band signals. The specific steps are as follows. First, the real part and the imaginary part are multiplied by  $\cos(\omega_i t)$  to obtain

![](_page_3_Picture_2.jpeg)

**Fig. 1.** Schematic diagram of the round-trip multiband QKD network. The Telecommunication as center node performs point-to-multipoint QKD with Community, Supermarket, School, Government, and Factory as child nodes. A continuous wave is transmitted from the center node to each child node. Every child node modulates quantum signals at their respective carrier frequencies and transmits them back to the center node. Subsequently, these signals are superimposed to form a multiband signal at the center node.

<span id="page-3-0"></span>
$$|Re(\alpha_{i}e^{j\theta_{i}})\rangle\cos(\omega_{i}t)$$

$$= \left|\frac{1}{2}(\cos(2\omega_{i}t) + 1)(x_{i}\cos\theta_{i} - p_{i}\sin\theta_{i})\right|$$

$$-\frac{1}{2}\sin(2\omega_{i}t)(x_{i}\sin\theta_{i} + p_{i}\cos\theta_{i})\rangle,$$

$$|Im(\alpha_{i}e^{j\theta_{i}})\rangle\cos(\omega_{i}t)$$

$$= \left|\frac{1}{2}(\cos(2\omega_{i}t) + 1)(x_{i}\sin\theta_{i} + p_{i}\cos\theta_{i})\right|$$

$$+\frac{1}{2}\sin(2\omega_{i}t)(x_{i}\cos\theta_{i} - p_{i}\sin\theta_{i})\rangle.$$
(5)

After filtering out the high-frequency components with a low-pass filter, we can obtain

$$|X_{i}\rangle = |x_{i}\cos\theta_{i} - p_{i}\sin\theta_{i}\rangle,$$
  

$$|P_{i}\rangle = |x_{i}\sin\theta_{i} + p_{i}\cos\theta_{i}\rangle.$$
(6)

Then, we use the pilot signal inserted in the quantum signal by the TDM method to estimate  $\theta$  and then recover the quantum signal. The pilot signal corresponds to the state of  $x_i = 1$  and  $p_i = 0$ . The angle  $\theta_i$  can be acquired as

$$\theta_i = \arctan(|P_i\rangle/|X_i\rangle).$$
 (7)

Subsequently, the center node performs frame synchronization to align the data. Upon completion of parameter evaluation, reverse reconciliation, and privacy amplification, the QKD process is finalized. We summarized the process of point-to-multipoint GMCS CV-QKD in Table 2. In this scheme, every child node requires only one modulator and one circulator to access the round-trip multiband QKD network, with only one laser and detector required for the entire network, which is highly efficient. Besides, since the key information is transmitted from the child nodes to the center node, the transmittance and noise introduced during the process of continuous wave passing from the center

<span id="page-3-1"></span>Table 2. The steps of point-to-multipoint GMCS CV-QKD

- 1. The *i*-th child node select two sets of Gaussian distributed random sequences  $x_i$  and  $p_i$ , with length n, mean 0, and variance of  $V_i$ . Based on these, n coherent states  $|x_i + jp_i\rangle e^{j\omega_i t}$  are prepared by the *i*-th child node and then register its own frequency band with the center node. Eventually, the n coherent states generated by n child nodes are transmitted to the center node through a quantum channel.
- 2. After receiving the multiband coherent state  $\sum_{i=1}^{N} |x_i + jp_i\rangle e^{i(\omega_i t + \theta_i)}, \text{ the center node separates the coherent state } |x_i + jp_i\rangle e^{i(\omega_i t + \theta_i)} \text{ of the } i\text{-th child node using a filter. Then, the center node eliminates the carrier through coherent demodulation to obtain <math>x_i$  and  $p_i$  of the i-th child node. Finally, the coherent state modulated by each child node can be acquired through the phase shift recovery using the pilot signal.
- Because heterodyne detection is adopted, every child node retains all the data.
- 4. Each child node acts as Alice and the center node acts as Bob to perform the same step 4 as shown in Table 1.
- 5. Each child node acts as Alice and the center node acts as Bob to perform the same step 5 as shown in Table 1.

node to the child nodes are not considered in the security key calculation. Moreover, this scheme avoids the issue of wavelength misalignment caused by different laser sources. The detector bandwidth is fully utilized due to the FDM method. In brief, the network possesses remarkable scalability, robustness, and noise suppression capabilities.

#### Distributed sensing integrated in quantum networks

DOFS technology achieves sensing by assessing the impact of environmental influences on various parameters of optical fibers. It can be categorized into DVS, distributed fiber acoustic sensing, and distributed fiber temperature sensing based on its functionalities [40,41]. Classical DOFS usually uses backscattering light to achieve sensing, which is also known as  $\phi$ -OTDR. It is mainly affected by the length of the optical fiber. The longer the optical fiber, the weaker the reflected backscattering light, which affects sensing effectiveness. Therefore, this method requires strong optical power and usually uses an erbium-doped fiber amplifier to enhance the optical power [42–46,51], which is impossible in QKD.

Although the optical power of QKD is too weak to use the  $\phi$ -OTDR method, the QKD system can achieve sensing through the forward-transmitting light. Recently, the DOFS scheme using the forward-transmitting light has detected earthquakes in New Zealand and Japan using underwater fiber [52]. In addition, DVS using the frequency locking link of QKD has also been proven to be feasible [53]. The scheme requires sensitivity to phase variations and the ability to demodulate phase changes in the signal. It is mainly affected by the frequency-locking effect of the two lasers.

Through the above description of QKD, it is known that QKD signals are highly sensitive to the phase  $\theta$ . By utilizing the pilot signal within the QKD system, it becomes feasible to demodulate

the phase  $\theta$  and consequently restore the QKD signal. When this QKD system is affected by the environment and the phase  $\theta$ changes, the demodulation and analysis of the sensing phase turn it into an ISACQ system. Furthermore, the  $\theta_i$  of the *i*-th child node in different frequency bands can be distinguished in the round-trip multiband QKD network. If each child node is considered as a sensing element, this network enables simultaneous sensing and QKD on the shared infrastructure, forming an ISAQN illustrated as Fig. 2. As shown in Fig. 2A, the ISAQN system functions normally when no vibration event occurs. The center node transmits light to each child node, and each child node transmits their respective coherent state  $|\alpha_i\rangle$  back to the center node. When a vibration event is occurring, the coherent state  $|\alpha_i\rangle$  modulated by the *i*-th child node will rotate at a time-variant angle of  $\varphi_i(t)$  instead of a time-invariant angle of  $\theta_i$ , shown as Fig. 2B. At this moment, the coherent state modulated by the *i*-th child node becomes  $|\alpha_i\rangle e$  $^{j\varphi_{i}(t)}$ . By extracting  $\varphi_{i}(t)$  through pilot signals, the waveform of each child node's vibration can be reconstructed. The position and magnitude of the vibration event can be obtained by joint calculation of the vibration waveforms from all child nodes.

In the following, we will provide a detailed description of the specific principles for implementing the ISAQN. The phase delay  $\varphi$  of the light transmitted through the optical fiber is

$$\varphi = \beta L, \tag{8}$$

where  $\beta$  is the propagation constant and L is the length of the optical fiber. When the optical fiber at the child node senses a vibration event, it withstands axial stress and radial stress. This will change its length L, refractive index n, and core diameter D, thus causing

![](_page_4_Figure_6.jpeg)

<span id="page-4-0"></span>**Fig. 2.** Schematic diagram of integrated sensing and QKD network (ISAQN) with and without vibration events. (A) When there are no vibration events, point-to-multipoint QKD operates normally. Each child node modulates its coherent state  $|\alpha_i\rangle$  and returns it to the center node. (B) When vibration events occur, the coherent state of the *i*-th child node  $|\alpha_i\rangle$  will rotate at an angle of  $\varphi_i(t)$  and transform into  $|\alpha_i\rangle e^{i\varphi_i(t)}$ .

a change in the optical phase. Each child node experiences a different phase change. The expression for the phase change is

$$\Delta \varphi = \beta \Delta L + \Delta \beta L$$

$$= \beta \Delta L + L \frac{d\beta}{dn} \Delta n + L \frac{d\beta}{dD} \Delta D,$$
(9)

where  $\Delta L$  is the change in optical fiber length,  $\Delta n$  denotes the change in refractive index, and  $\Delta D$  represents the change in core diameter. The first term describes the strain effect caused by the change in optical fiber length due to axial stress. The second term represents the photoelastic effect caused by the change of refractive index in the optical fiber. The third term is the Poisson effect caused by the change in optical fiber diameter due to radial stress. Since the Poisson effect is very small (usually 0.2% of the photoelastic effect), it can be ignored. In addition,  $\beta$  and  $\Delta n$  can be expressed as

$$\beta = \frac{2\pi n}{\lambda}$$

$$\Delta n = -\frac{1}{2}n^3 \varepsilon_z \left[ (1-\mu)p_{12} - \mu p_{11} \right], \tag{10}$$

where  $\lambda$  is the wavelength of light,  $\varepsilon_z$  denotes the axial strain coefficient of the optical fiber, and has a relationship with the length change  $\Delta L$  given by  $\Delta L = \varepsilon_z L$ .  $\mu$  repesents the Poisson's ratio of the fiber, and  $p_{11}$  and  $p_{12}$  are the photoelastic constants of the fiber. Therefore, the phase change of the i-th child node is given by

$$\Delta \varphi_i = \Delta L_i \frac{2\pi}{\lambda} \left\{ n - \frac{1}{2} n^3 \left[ (1 - \mu) p_{12} - \mu p_{11} \right] \right\}, \tag{11}$$

<span id="page-4-1"></span>where  $\Delta L_i$  denotes the length change of the optical fiber in the i-th child node. It can be observed that the length change  $\Delta L_i$  is directly proportional to the phase change  $\Delta \phi_i$ . According to the above formula, the sensing effect can be amplified by changing the parameters of the optical fiber at the child nodes, thus making the child nodes serve as sensing elements. In a practical scenario, the long-distance fiber is placed in seismic-resistant pipelines, while the fibers at child nodes are more likely to be exposed to outside environments. It means that child nodes are more suitable as sensing elements. Therefore, the optical fiber in the child nodes is more sensitive to a vibration event compared to the long-distance fiber channels.

The schematic diagram of ISAQN in the time and frequency domains is shown in Fig. 3. Each child node modulates its quantum signal and pilot signal by TDM method according to Eq. 1. The presence of pilot signals aims to enhance the performance of quantum communication networks and distributed sensing networks. The optical power of the pilot signal is stronger than that of the quantum signal. The splitter collects the coherent states of all the child nodes and directs them to a coherent detector. The quantum signals from different users received by the detector do not interfere with each other in the frequency domain, and the same applies to the pilot signal. The constructed ISAQN is capable of sensing vibration events, such as an earthquake illustrated in Fig. 3. When the vibration waveform changes over time, the phase change and length change of the *i*-th child node  $\Delta \varphi_i$  and  $\Delta L_i$ becomes the time-variant  $\varphi_i(t)$  and  $L_i(t)$ . The coherent state  $|\alpha_i\rangle$ modulated by the *i*-th child node will rotate at an angle of  $\varphi_i(t)$ . At this point, the coherent state modulated by the *i*-th child node is derived from

$$|\alpha_i\rangle e^{j\varphi_i(t)} = |x_i + jp_i\rangle e^{j(\omega_i t + \varphi_i(t))}, i \in \{1, 2, \dots, N\}. \quad (12)$$

![](_page_5_Picture_2.jpeg)

**Fig. 3.** Schematic diagram of ISAQN in the frequency domain and time domain. Different child node modulates quantum signals and pilot signals with different carrier frequencies. Then, they are converged through the optical fiber to the splitter and enter the detector for coherent detection. When the modulated coherent state and pilot signals do not experience fiber vibration events, the detected results remain a normal multiband signal. When a vibration event occurs, the spectrum of the detected results experiences spectrum castdown due to the enhancement of Rayleigh backscattering, and the spectrum of the pilot experiences spectrum splitting in its centerline. The detection results are processed using the SPM protocol. By employing coherent demodulation, arctangent, and phase unwrapping, phase recovery can be accomplished, thereby obtaining the vibration waveform.

<span id="page-5-0"></span>As shown in Fig. 3, both the quantum signal and the pilot signal will result in the registered spectrum with spectrum cast-down, indicating the perception of vibrations. This phenomenon is caused by the change in the refractive index of the optical fiber, which enhances the backscattering light and reduces the power of forward-transmitting light. Due to the unique expression form of the pilot signal, it will also exhibit a phenomenon of spectrum splitting. By observing the location of the castdown or the splitting in the spectrum, we can determine which child nodes are experiencing vibration. The phase change of the i-th child node  $\varphi_i(t)$  induced by vibration event can be demodulated through the coherent demodulation, which can be expressed as

$$\left| Re\left(\alpha_{i}e^{j\varphi_{i}(t)}\right)\right\rangle \cos(\omega_{i}t) \\
= \left| \frac{1}{2}(\cos(2\omega_{i}t) + 1)(x_{i}\cos\varphi_{i}(t) - p_{i}\sin\varphi_{i}(t)) - \frac{1}{2}\sin(2\omega_{i}t)(x_{i}\sin\varphi_{i}(t) + p_{i}\sin\varphi_{i}(t))\right\rangle, \\
\left| Im\left(\alpha_{i}e^{j\varphi_{i}(t)}\right)\right\rangle \cos(\omega_{i}t) \\
= \left| \frac{1}{2}(\cos(2\omega_{i}t) - 1)(x_{i}\sin\varphi_{i}(t) + p_{i}\cos\varphi_{i}(t)) + \frac{1}{2}\sin(2\omega_{i}t)(x_{i}\cos\varphi_{i}(t) - p_{i}\sin\varphi_{i}(t))\right\rangle.$$
(13)

By applying a low-pass filter, the high-frequency components are effectively filtered out. As a result, we can obtain the quadrature components

$$|X_{i}\rangle = |x_{i}\cos\varphi_{i}(t) - p_{i}\sin\varphi_{i}(t)\rangle,$$
  

$$|P_{i}\rangle = |x_{i}\sin\varphi_{i}(t) + p_{i}\cos\varphi_{i}(t)\rangle.$$
(14)

Through substituting  $x_i = 1$  and  $p_i = 0$  of pilot signal into the above equation, the phase change of the *i*-th child node can be obtained by

$$\varphi_i(t) = \arctan(|P_i\rangle/|X_i\rangle).$$
 (15)

However, due to the limited value range of the arctangent function, which is constrained between  $(-\pi,\pi)$ , the phase change appears as a wrapped phase. In cases where the practical phase change exceeds this range, the demodulation results exhibit jumps at  $\pm \pi$ , with an amplitude of  $2\pi$ . This is known as the phasewrapping effect. Therefore, for phase variations caused by vibrations, we cannot directly observe regular waveforms such as sine waves in the demodulation results. Instead, we can only observe signals that vary in frequency over time, as shown in Fig. 3. By employing phase unwrapping, the demodulation results can be restored to the correct vibration waveform. The principle of phase unwrapping is to expand the value range of demodulated results. By detecting the differences between phases and adding or subtracting integer multiples of  $2\pi$ , the phase becomes continuously changing, which can be expressed as

$$\phi_i(t) = \varphi_i(t) + 2\pi m, \ \varphi_i \in (-\pi, \pi), \ m = 0, \pm 1, \pm 2, \ \cdots$$
 (16)

As shown in Fig. 3, the result of phase unwrapping is a stable and continuous sinusoidal waveform, which matches the seismic vibration waveform that we set. Through experimental

calibration or Eq. 11, it can be obtained that the length change of vibration is

$$L_i(t) = \phi_i(t) \frac{\lambda}{2\pi} \left\{ n - \frac{1}{2} n^3 \left[ (1 - \mu) p_{12} - \mu p_{11} \right] \right\}^{-1}, \quad (17)$$

The functionality of ISAQN sensing can be achieved by monitoring the spectrum and phase. Therefore, we refer to this sensing protocol as the SPM protocol. The SPM protocol can be summarized in Table 3.

In the following, we will calculate the quantum limit that the measurement precision  $\delta \varphi_i$  and  $\delta L_i$  of sensing phase  $\varphi_i$  and sensing length  $L_i$  can achieve [65]. Assuming the average photon numbers of the signal and the local oscillator (LO) are  $N_s$  and  $N_L$ , their annihilation operators are denoted as  $\widehat{a}_s$  and  $\widehat{a}_L$ . After heterodyne detection, the annihilation operators of the i-th child node are represented as

$$\widehat{\mathbf{a}}_{1} = \frac{1}{2} \left( \widehat{\mathbf{a}}_{\mathbf{s}} e^{j\varphi_{i}} + \widehat{\mathbf{a}}_{\mathbf{L}} e^{j\theta_{\mathbf{sL}}} \right), 
\widehat{\mathbf{a}}_{2} = \frac{1}{2} \left( \widehat{\mathbf{a}}_{\mathbf{s}} e^{j\varphi_{i}} - \widehat{\mathbf{a}}_{\mathbf{L}} e^{j\theta_{\mathbf{sL}}} \right), \tag{18}$$

where  $\theta_{sL} = \pi/2$  is the phase difference between LO and the signal, and  $\hat{a}$  is the annihilation operator. Then, the average photon numbers of  $\hat{a}_1$  and  $\hat{a}_2$  can be denoted as

$$\begin{split} \widehat{\mathbf{n}}_{1} &= \widehat{\mathbf{a}}_{1}^{\dagger} \widehat{\mathbf{a}}_{1} \\ &= \frac{1}{4} \left( \widehat{\mathbf{a}}_{s}^{\dagger} \widehat{\mathbf{a}}_{s} + \widehat{\mathbf{a}}_{L}^{\dagger} \widehat{\mathbf{a}}_{L} + \widehat{\mathbf{a}}_{s}^{\dagger} \widehat{\mathbf{a}}_{L} e^{j(-\varphi_{i} + \theta_{sL})} + \widehat{\mathbf{a}}_{L}^{\dagger} \widehat{\mathbf{a}}_{s} e^{-j(-\varphi_{i} + \theta_{sL})} \right), \\ \widehat{\mathbf{n}}_{2} &= \widehat{\mathbf{a}}_{2}^{\dagger} \widehat{\mathbf{a}}_{2} \end{split}$$
(19)
$$&= \frac{1}{4} \left( \widehat{\mathbf{a}}_{s}^{\dagger} \widehat{\mathbf{a}}_{s} + \widehat{\mathbf{a}}_{L}^{\dagger} \widehat{\mathbf{a}}_{L} - \widehat{\mathbf{a}}_{s}^{\dagger} \widehat{\mathbf{a}}_{L} e^{j(-\varphi_{i} + \theta_{sL})} - \widehat{\mathbf{a}}_{L}^{\dagger} \widehat{\mathbf{a}}_{s} e^{-j(-\varphi_{i} + \theta_{sL})} \right), \end{split}$$

where  $\hat{a}^{\dagger}$  is the creation operator. The average photon numbers after subtraction is

$$\widehat{\mathbf{n}} = \widehat{\mathbf{n}}_1 - \widehat{\mathbf{n}}_2 = \frac{1}{2} \left( \widehat{\mathbf{a}}_s^{\dagger} \widehat{\mathbf{a}}_L e^{j(-\varphi_i + \theta_{sL})} + \widehat{\mathbf{a}}_L^{\dagger} \widehat{\mathbf{a}}_s e^{-j(-\varphi_i + \theta_{sL})} \right). (20)$$

Since LO is much stronger than the signal, we can obtain  $\alpha_L \gg \alpha_s$ . In the case of calculating precision, sensing phase  $\varphi_i$  can be viewed as infinitesimal. For a very small phase  $\varphi_i$ , the annihilation operator of LO can be treated as a classical quantity, represented as  $\widehat{\mathbf{a}}_L^{\dagger} = \widehat{\mathbf{a}}_L = \alpha_L$ . Therefore, we can get

$$\widehat{\mathbf{n}} = \frac{\alpha_{\mathrm{L}}}{2} \left( \widehat{\mathbf{a}}_{\mathrm{s}}^{\dagger} e^{j(-\varphi_{i} + \theta_{\mathrm{sL}})} + \widehat{\mathbf{a}}_{\mathrm{s}} e^{-j(-\varphi_{i} + \theta_{\mathrm{sL}})} \right). \tag{21}$$

By substituting  $\theta_{\rm sL}=\pi/2$ , the above formula can be simplified to

$$\widehat{\mathbf{n}} = \frac{j\alpha_{\mathbf{L}}}{2} \left( \widehat{\mathbf{a}}_{\mathbf{s}}^{\dagger} e^{-j\varphi_{i}} - \widehat{\mathbf{a}}_{\mathbf{s}} e^{j\varphi_{i}} \right). \tag{22}$$

Utilizing linearization formulas  $\hat{a}_s = \alpha_s + \delta \hat{a}_s$  and  $\hat{a}_s^{\dagger} = \alpha_s^* + \delta \hat{a}_s^{\dagger}$ , we can obtain the following equation

$$\widehat{\mathbf{n}} = \alpha_{\mathrm{L}} \left( \alpha_{\mathrm{s}} \sin(\varphi_{i}) - j \left( \delta \widehat{\mathbf{a}}_{\mathrm{s}} - \delta \widehat{\mathbf{a}}_{\mathrm{s}}^{\dagger} \right) \right). \tag{23}$$

Since  $\varphi_i$  is infinitesimal, it follows that  $\sin(\varphi_i) = \varphi_i$ . The real numbers  $\alpha_L$  and  $\alpha_s$  can be replaced by average photon number  $\alpha_L = \sqrt{N_L}$  and  $\alpha_s = \sqrt{N_s}$  to derive the following formula

$$\widehat{\mathbf{n}} = \sqrt{N_{\mathrm{L}}} \left( \sqrt{N_{\mathrm{s}}} \varphi_{i} - j \left( \delta \widehat{\mathbf{a}}_{\mathrm{s}} - \delta \widehat{\mathbf{a}}_{\mathrm{s}}^{\dagger} \right) \right). \tag{24}$$

#### <span id="page-6-0"></span>**Table 3.** The steps of SPM protocol

- 1. When the point-to-multipoint GMCS CV-QKD in Table 2 is operating normally, the center node monitors the frequency spectrum of quantum signals and pilot signals from all the child nodes. If the spectrum of the quantum signals and pilot signals from the *i*-th child node experience spectrum castdown, or if the spectrum of the pilot signal experiences spectrum splitting, it can be inferred that the *i*-th child node is perceiving vibrations.
- 2. If the vibration frequency and amplitude are low, the phase of the QKD signal can still be recovered by the pilot signal. In this case, the protocol proceeds directly to step 3. Otherwise, if the vibration frequency and amplitude are too high, the phase of the QKD signal can no longer be recovered from the pilot signal. At this point, the center node instructs the *i*-th child node to stop modulating the QKD signal and modulate only the pilot signal.
- 3. The center node performs coherent demodulation on the pilot signal of the *i*-th child node to obtain quadrature components. Subsequently, the arctangent operation is applied to the quadrature components. Then, all phase jumps are eliminated in the results by employing phase unwrapping. Finally, the center node obtains the vibration waveform sensed by the *i*-th child node.

<span id="page-6-1"></span>Thus, the quantum limit of sensing phase precision  $\delta \varphi_i$  can be expressed as

$$\delta \varphi_i = \frac{\delta \hat{Y}_s}{\sqrt{N_s}},\tag{25}$$

where  $\delta \hat{Y}_s = j \left( \delta \hat{a}_s - \delta \hat{a}_s^{\dagger} \right)$  is the vacuum fluctuation. From this formula, it can be inferred that the sensing phase precision is related to the vacuum fluctuation  $\delta \hat{Y}_s$  and the average photon number  $N_s$ , which reaches the standard quantum limit. By substituting in Eq. 25, Eq. 11 can be derived to

$$\delta L_{i} = \frac{2\pi\delta \hat{Y}_{s}}{\lambda \sqrt{N_{s}}} \left\{ n - \frac{1}{2} n^{3} \left[ (1 - \mu) p_{12} - \mu p_{11} \right] \right\}, \tag{26}$$

where  $\delta L_i$  is the measurement precision of sensing length  $L_i$ . In conclusion, the detection precision of ISAQN can reach the standard quantum limit, which is consistent with the shot noise limit in the experiment. Although the precision of this sensing method cannot reach the Heisenberg quantum limit, it can achieve a standard quantum limit that is difficult to attain by other classical sensing methods.

To illustrate how ISAQN facilitates distributed sensing of vibration events, we use an earthquake as an example to describe it. Assuming the seismic wave is denoted as E(t), the phase detected by the i-th child node can be represented as

$$E_i(t) = \gamma_i E(t + t_i), \tag{27}$$

where  $\gamma_i \propto t_i$  is the attenuation coefficient when the seismic wave arrives at the i-th child node, and  $t_i$  represents the time spent. Once the vibration waveforms of each child node are demodulated in the center node, the position and magnitude of the vibration can be calculated, as shown in Fig. 4. It is achieved by analyzing the vibration waveform with different arrival time  $t_i$  or different attenuation coefficient  $\gamma_i$ . The time difference of the vibration waveforms arriving at different child nodes, obtained through cross-correlation, allows for the derivation of the position. The magnitude of the vibration experienced by each child node can be determined by the amount of phase change. This enables the reconstruction of the original vibration event, including its position and magnitude. At least 3 child nodes are required to complete this process. In the following, we will present a comprehensive explanation of the calculation process.

For example, assuming an earthquake occurs at position  $(x_0, y_0)$ , the child node located at position  $(x_3, y_3)$  detects the vibration first, represented by the purple waveform in the phase recovery. Next, the child node located at position  $(x_2, y_2)$  senses the vibration, represented by the green waveform. Finally, the child node located at position  $(x_1, y_1)$  senses the vibration, represented by the blue waveform. The vibration waveforms of these 3 child nodes are plotted in Fig. 4, where  $\Delta t_{12}$  represents the time difference between the first and second arriving vibration waveforms, and  $\Delta t_{23}$  represents the time difference between the second and third arriving vibration waveforms. Assuming that the propagation speed of the seismic wave is v, the time required for the wave to reach child node  $(x_1, y_1)$ ,  $(x_2, y_2)$ , and  $(x_3, y_3)$  are  $t_1$ ,  $t_2$ , and  $t_3$ . In addition,  $L_1$ ,  $L_2$ , and  $L_3$  are used to represent the distances between the center node and child nodes  $(x_1, y_1)$ ,  $(x_2, y_2)$ , and  $(x_3, y_3)$ , respectively. Due to the attenuation of seismic waves with increasing distance during propagation, the

![](_page_7_Figure_4.jpeg)

<span id="page-7-0"></span>**Fig. 4.** Schematic diagram of calculating the earthquake's position and magnitude. When an earthquake occurs at  $(x_0,y_0)$ , it's detected by 3 child nodes at  $(x_1,y_1)$ ,  $(x_2,y_2)$ , and  $(x_3,y_3)$ . Phase recovery depicts the vibration waveforms sensed by 3 child nodes. Due to their different positions, the arrival times  $t_1$ ,  $t_2$ ,  $t_3$  and  $\Delta\phi$  vary, but the period T and waveforms remain the same.  $\Delta t_{12}$  and  $\Delta t_{23}$  are the time differences between the arrival of the waveforms. Assuming seismic wave propagation speed is v, the distances for the wave to reach nodes are  $vt_1$ ,  $vt_2$ , and  $vt_3$ . Moreover,  $t_1$ ,  $t_2$ , and  $t_3$  represent distances from these nodes to the center node.

phase change  $\Delta \phi$  and arrival times  $t_1$ ,  $t_2$ , and  $t_3$  differ. However, the period T and waveform remain the same. Therefore, the following equations can be obtained

$$(x_{1}-x_{0})^{2} + (y_{1}-y_{0})^{2} = (vt_{1})^{2},$$

$$(x_{2}-x_{0})^{2} + (y_{2}-y_{0})^{2} = (vt_{2})^{2},$$

$$(x_{3}-x_{0})^{2} + (y_{3}-y_{0})^{2} = (vt_{3})^{2},$$

$$t_{2}-t_{3} = \Delta t_{12} + (L_{2}-L_{3})/c,$$

$$t_{1}-t_{2} = \Delta t_{23} + (L_{1}-L_{2})/c,$$
(28)

where c is the speed of light in the optical fiber. The intersection of the 3 circles corresponds to a unique point, allowing for the determination of the vibration position. Since the phase change  $\Delta \phi$  is proportional to the magnitude of the vibration, the original magnitude of the vibration can be determined by measuring the phase change at each child node.

In conclusion, the ISAQN achieves the coexistence of QKD and sensing. Without the requirement for additional devices, the round-trip multiband QKD network can be transformed into an ISAQN through the SPM protocol. It can also sense the location and magnitude of a vibration event, such as an earthquake.

#### Conclusion

When the frequency of the vibration is too high, the pilot signal will no longer be able to totally recover the phase of the quantum signal. This is because the pilot signal is inserted into the quantum signal through the TDM method. If the pilot signal is transmitted together with the quantum signal through the FDM method, this limitation can be overcome. In this way, the recovery of the quantum signal can be achieved regardless of the vibrations at any high frequency and big amplitude. Moreover, we also consider implementing sensing throughout the entire optical fiber link to integrate with DOFS. These will be the content of our future research. Due to space constraints, we will not continue to elaborate further.

In terms of practical security, this round-trip structure is susceptible to the eavesdropper Eve's practical security attacks, including the phase remapping attack [66,67] and the Trojanhorse attack [68]. In order to resist the phase remapping attack, the child node can verify if the correct modulation is applied correctly by monitoring the arrival time of the reference pulse and the signal pulse [66]. As we cannot use isolators in the round-trip structure, a filter can be used to exclude Eve's input light to prevent the Trojan-horse attack [68]. Moreover, 3 technical countermeasures exist, including the use of a watchdog mechanism with a switch at the entrance of the round trip that randomly diverts a small fraction of incoming signals to this detector, allowing access to the eavesdropper for a shorter duration, and reducing the width of the phase modulation voltage pulse [69]. From a theoretical perspective, a higher amount of privacy amplification can help the ISAQN eliminate the information leakage caused by Trojan-horse attacks. It is necessary to estimate the maximum information leakage due to Trojanhorse attacks and incorporate these elements into the security proof [68,70,71].

In this paper, ISAQN has been proposed and verified both theoretically and experimentally. We integrate QKD and sensing through SPM protocol. ISAQN only requires a laser and a detector to achieve point-to-multipoint QKD and DOFS. Experimental

results demonstrate the network's ability to distinguish quantum signals and sensing signals from different child nodes simultaneously. This provides a new perspective for future ubiquitous quantum networks and distributed sensing.

# **Methods**

Based on the theoretical derivation of ISAQN, we conducted a proof-of-principle experiment. This experiment simultaneously implemented point-to-multipoint quantum networks and distributed sensing networks in ISAQN. Firstly, we will illustrate the experiment setup in part 1. Secondly, we will present a performance analysis for quantum communication and sensing in part 2.

# **Experiment setup**

The optical structure of ISAQN used in this experiment is illustrated in Fig. [5.](#page-8-0) First, the light transmitted from the center node is divided into two beams of light by a 99:1 beam splitter (BS). The high-power light is used as the LO for coherent detection, while the low-power light passes through a variable optical attenuator (VOA) before reaching the optical circulator (OC). The VOA of the center node reduces the light to the quantum level. After the light is transmitted from port 1 to port 2 of the OC, it is evenly distributed to 8 child nodes through an 8×1 BS. The network capacity of the ISAQN constructed in the experiment is 8. However, due to experimental equipment limitations, only 3 child nodes were used in the experiment. Each child node is connected to a 10-km optical fiber. After reaching the child nodes, the light is transmitted from port 2 to port 3 of the OC and then passes through another VOA. The VOA of the child node is used to balance the optical power. The optical signal is then modulated using an arbitrary waveform generator (AWG) through IQM. Child node 1, child node 2, and child node 3 modulate carrier frequencies of 100, 200, and 300 MHz, respectively, while the base-band frequency for each child node is 50 MHz. After modulation, the signal from each child node is adjusted for polarization using a polarization controller. Then, the signal enters a 2.5-m optical fiber wound around the piezoelectric transducer (PZT), with dimensions of 53.10 mm × 55.00 mm × 3.95 mm. In the experiment, different voltages are applied to the PZT to simulate different vibration events. Subsequently, the signal returns to the 10-km optical fiber from port 1 to port 2 of the OC. After the signals of all child nodes pass through the 8×1 BS once again, they return to the center node via ports 2 and 3 of the OC. At the center node, the signals are integrally adjusted for polarization using a polarization controller and then reach the integrated coherent receiver (ICR) together with LO. The detected signal is sampled by an oscilloscope.

# **Experiment result**

For QKD, the distributions of experimental data in the phase space for 3 child nodes are shown in Fig. [6](#page-9-0). The modulation variance of each child node is set to *V*<sup>A</sup> = *V*<sup>1</sup> = *V*<sup>2</sup> = *V*<sup>3</sup> = 12 SNU, where SNU is the shot noise unit. The spectrum of the

![](_page_8_Figure_10.jpeg)

<span id="page-8-0"></span>**Fig. 5.** Optical structure of ISAQN. The light from the center node is split by a 99:1 BS into a high-power LO and low-power light that passes through a VOA and an OC. VOA reduces light to the quantum level and the 8×1 BS distributes it to 8 child nodes. The network capacity of the ISAQN constructed in the experiment is 8. Due to experimental equipment limitations, only 3 nodes are used, each connected to a 10-km optical fiber. This light passes through another VOA for power balance, is modulated via an AWG, and then reaches child nodes. Child nodes 1, 2, and 3 modulate 100-, 200-, and 300-MHz carrier frequencies, respectively, with a base-band frequency of 50 MHz. Then, the signal enters an optical fiber wound around the PZT, which is used to simulate vibration events. After passing through the 10-km optical fiber, the signals are merged back via the 8×1 BS and return to the center node where polarization is adjusted again before reaching the ICR.

signal received by the center node through ICR is presented in Fig. 7. The mixed spectrum received by the center node has frequencies of 100, 200, and 300 MHz, and there is no occurrence of spectrum aliasing phenomenon. In order to make the spectrum more visual and distinct, we increased the optical power when drawing Fig. 7. The actual spectrum of the quantum signal is much smaller than what is shown in Fig. 7. Additionally, Fig. 8 exhibits the results of the cross-correlation between the signals modulated by each child node and received by the center node. The cross-correlation results demonstrate the success of frame synchronization, as indicated by the prominent vertical lines that remain visible. The excess noise scatter plots and excess noise mean of 100 data frames with 10<sup>5</sup> points from 3 child nodes are depicted in Fig. 9. The excess noise means of 3 child nodes are 4.7, 2.4, and 3.6 mSNU, respectively. It can be inferred that ISAQN has excellent noise suppression capability.

In this experiment, we also evaluate the reachable SKR for GMCS CV-QKD. The formula of the SKR for unit system repetition frequency is in Appendix. For the practical CV-QKD system, SKR *K* can be calculated as

$$K = RK_r, (29)$$

where R is the repetition frequency of the CV-QKD system. The other parameters introduced in the calculation are quantum efficiency  $\eta=0.42$ , electrical noise  $v_{el}=0.18$ , reconciliation efficiency  $\beta=0.98$ , modulation variance  $V_A=12$  SNU, and repetition frequency R=50 MHz. The  $N\times 1$  BS on the return path would introduce a 1/N loss on each arm, thereby reducing the SKR of all child nodes. The transmittance will be changed to  $T=10^{-\alpha L/10}/N$ , where  $\alpha=0.2$  dB/km denotes the attenuation coefficient of optical fiber, and N is the network capacity of ISAQN and branch number of the  $N\times 1$  BS. In the experiment, we substituted N=8 into the formula and obtained the secure key rates for 3 child nodes as shown in Fig. 10. At the transmission distance L=10 km, the SKR of 3 child nodes are respectively 0.70, 0.71, and 0.72 Mbits/s. In conclusion, ISAQN has achieved outstanding experimental results in multipoint QKD.

For DOFS, each child node has a PZT to simulate the vibration waveform when it reaches the child node. According to the d-type piezoelectric equation of PZT, the length change of

![](_page_9_Figure_7.jpeg)

<span id="page-9-0"></span>Fig. 6. Distribution of experimental data in the phase space for 3 child nodes. (A to C) The experimental data of each child node follows a Gaussian distribution.

![](_page_9_Figure_9.jpeg)

<span id="page-9-1"></span>**Fig. 7.** Frequency spectrum of the signal received by the center node. There are 3 frequency bands of 3 child nodes, which are 100, 200, and 300 MHz. When light attenuates to the quantum level, its band becomes difficult to observe. To enhance the visual clarity and distinction of the spectrum, we increased the optical power during the drawing process.

![](_page_9_Figure_11.jpeg)

<span id="page-9-2"></span>**Fig. 8.** Cross-correlation of 3 child nodes and center node. Since AWG and oscilloscope are clock-synchronized, the frame synchronization offset of each node is the same.

![](_page_10_Figure_2.jpeg)

<span id="page-10-0"></span>**Fig. 9.** Excess noise of 3 child nodes.  $10^5$  points are collected per second to calculate the excess noise. The blue scattered points represent the excess noise at different times. The red straight line denotes the mean excess noise over 100 seconds. The excess noise means of 3 child nodes are 4.7, 2.4, and 3.6 mSNU, respectively, where SNU is the shot noise unit.

![](_page_10_Figure_4.jpeg)

<span id="page-10-1"></span>**Fig. 10.** SKR of 3 child nodes. As the transmission distance increases, the SKR of the 3 child nodes decreases. At the transmission distance  $L\!=\!10$  km, the SKR of 3 child nodes are respectively 0.70, 0.71, and 0.72 Mbits/s.

the optical fiber wound on the PZT due to the applied radial voltage can be obtained by

$$\Delta L = d\pi r \Delta E,\tag{30}$$

where d is the piezoelectric parameter, r denotes the outer diameter, and  $\Delta E$  represents the change in electric field intensity. By utilizing the relationship between electric field intensity and electric potential E = V/t, we can obtain

$$\Delta L = \frac{d\pi r}{t} \Delta V,\tag{31}$$

where t is the thickness of the tube-type PZT, and  $\Delta V$  denotes the change in voltage. According to Eq. 11, the phase change of the i-th child node can be obtained by

$$\Delta \varphi_i = \Delta V_i \frac{2\pi}{\lambda} \left\{ n - \frac{1}{2} n^3 \left[ (1 - \mu) p_{12} - \mu p_{11} \right] \right\} \frac{d\pi r}{t}, \quad (32)$$

where  $\Delta V_i$  represents the voltage change of PZT in the *i*-th child node. It can be observed that the voltage change  $\Delta V_i$  is directly proportional to the phase change  $\Delta \varphi_i$ . In the experiment, Fig. 11 displays the relationship between the phase obtained by phase unwrapping and the voltage loaded on PZT over time. The blue solid line represents the phase waveform, while the red dashed line represents the voltage waveform at the same time. This corresponds precisely to the theoretical results. Additionally, Fig. 12 shows the frequency spectrum obtained when different child nodes sense vibration in the experiment. By observing the phenomenon of spectrum castdown or spectrum splitting, we can easily determine which child node perceives the vibration. To establish the relationship between the length change and voltage change, we conducted measurements using a capacitance micrometer with an accuracy of 0.2 nm, as shown in Fig. 13. It indicates the existence of a hysteresis effect in the open-loop PZT, which leads to the fact that the length change does not exhibit an ideal proportional relationship with voltage change. Thus, we can find that the sinusoidal waveforms depicted in the experimental results are not perfect sinusoidal waveforms. However, we can establish the relationship between phase change and length change, as shown in Fig. 14. It can be observed that the phase change is proportional to the length change.

The detection precision in the experiment is close to the shot noise limit, as indicated by the black line displayed in Fig. 15. The blue dots represent the detection precision of each individual

![](_page_10_Figure_14.jpeg)

<span id="page-10-2"></span>**Fig. 11.** Phase waveform recovered by ISAQN and voltage waveform loaded on PZT. The blue solid line represents the phase waveform, while the red dashed line represents the voltage waveform at the same time.

![](_page_11_Figure_2.jpeg)

<span id="page-11-0"></span>Fig. 12. Frequency spectrum of the signal received by the center node when a child node is vibrating. In the (A), (B), and (C) scenarios, one child node is vibrating while the other two are not. The vibrating child node's registered band exhibits spectrum castdown and spectrum splitting.

![](_page_11_Figure_4.jpeg)

<span id="page-11-1"></span>**Fig.13.** Relationship between voltage change and length change. Due to the hysteresis effect in the open-loop PZT, the voltage change and length change are not proportional.

![](_page_11_Figure_6.jpeg)

<span id="page-11-2"></span>**Fig. 14.** Relationship between phase change and length change. The phase change and length change are proportional, which is consistent with the theory.

experiment. The red dots represent the detection precision obtained by averaging over a large amount of data, with the corresponding red error bars representing the standard deviation. As shown in Fig. 15, the mean detection precision of multiple experiments from 3 child nodes are (1.0038606,1.0068994), (0.9997877,1.007847), and (1.0048642,0.9993358), which are approximately equal to the values of the shot noise limit (1, 1). The spatial resolution is 0.20 m, mainly limited by the bandwidth of the ICR. The maximum phase change is 891.18 rad. The vibration magnitude of the vibration center can be derived according to the vibration magnitude of the child nodes. By calculating the phase power spectrum density, the noise power is around  $-50~{\rm rad}^2~{\rm dB/Hz}$ . Therefore, its strain resolution is 0.50 ne /  $\sqrt{{\rm Hz}}$ . The vibration response bandwidth ranges from 1 Hz to 2 kHz.

Since the same vibration event can be detected by different nodes at different times, as shown in Fig. 16, we can calculate the specific location of the vibration event by the time difference. Moreover, precise time differences can be obtained using cross-correlation. In the experiment, different voltage waveforms are loaded on the PZT of 3 child nodes, which simulate the different effects of a vibration event on the child nodes. Assuming the velocity of the vibration event is 6 km/s, 3 child nodes are arranged in an equilateral triangular structure, with a distance from the center node of 10 km. The center node is at the center of this equilateral triangle. Under these circumstances, we can determine the center coordinate of the vibration event. Figure 16 shows the results of 3 tests. In the first vibration test, the time difference is 0 s,  $\Delta t_{12} = \Delta t_{23} = 0$  s, so the coordinates of the vibration center are located at the center node. Taking child node 1 as the reference origin, the coordinates of the vibration center are (8660.25,5000.00). In the second vibration test, the time difference is approximately 0.001 s,  $\Delta t_{12} = \Delta t_{23} = 0.001$  s. Therefore, the coordinates of the vibration center are (8663.72,5006.00). In the third vibration test, the time difference is approximately 0.01 s,  $\Delta t_{12} = \Delta t_{23} = 0.01$  s. Thus, the coordinates of the vibration center are (8695.00,5059.94). In conclusion, ISAQN has successfully achieved detection precision at the standard quantum limit, enabling the coexistence of QKD and sensing under the shot-noise-limited detection.

#### **Appendix**

Here, we give the SKR calculation process for the unit system repetition rate in the asymptotic case. Firstly, the SKR for reverse reconciliation with heterodyne detection is calculated as [72]

![](_page_12_Figure_2.jpeg)

<span id="page-12-0"></span>Fig. 15. Detection accuracy of sensing in ISAQN. (A to C) The mean detection accuracy of multiple experiments conducted by 3 child nodes is (1.0038606,1.0068994), (0.9997877,1.007847), and (1.0048642,0.9993358), respectively. These values closely approximate the shot noise limit values of (1,1).

![](_page_12_Figure_4.jpeg)

<span id="page-12-1"></span>**Fig. 16.** Sensing waveforms recovered from 3 different scenarios. The period of the vibration waveform is 2 kHz. The time differences for the start of the vibration in the 3 experiments are 0, 0.001, and 0.01 s, respectively. The arrival time of the sensing waveform accurately reflects the differences in vibration start time.

$$K_r = \beta I_{AB}^{het} - \chi_{BE}^{het}, \tag{33}$$

where  $\beta \in (0,1)$  is the efficiency of reverse reconciliation,  $I_{AB}^{het}$  is the mutual information between Alice and Bob, and  $\chi_{BE}^{het}$  is the maximum information available to Eve on Bob's key bounded by the Holevo quantity. Specifically,  $I_{AB}^{het}$  can be identified as

$$I_{AB}^{het} = \log_2 \frac{V + \chi_{tot}}{1 + \chi_{tot}},\tag{34}$$

where  $V=V_A+1$ , and  $\chi_{tot}$  representing the total noise referred to the channel input can be calculated as  $\chi_{tot}=\chi_{line}+\chi_{het}/T$ , in which  $\chi_{line}=1/T-1+\varepsilon$ , and  $\chi_{het}=[1+(1-\eta)+2v_{el}]/\eta$ . Besides,  $\chi_{BE}^{het}$  is identified as follows

$$\chi_{BE}^{het} = \sum_{m=1}^{2} G\left(\frac{\lambda_{m} - 1}{2}\right) - \sum_{m=3}^{5} G\left(\frac{\lambda_{m} - 1}{2}\right), (35)$$

where  $G(x) = (x + 1)\log_2(x + 1) - x\log_2 x$ .  $\lambda_m$  are symplectic eigenvalues derived from the covariance matrices and can be expressed as

$$\lambda_{1,2}^{2} = \frac{1}{2} \left( A \pm \sqrt{A^{2} - 4B} \right),$$

$$\lambda_{3,4}^{2} = \frac{1}{2} \left( C \pm \sqrt{C^{2} - 4D} \right),$$

$$\lambda_{5} = 1,$$
(36)

where

$$A = V^{2}(1 - 2T) + 2T + T^{2}(V + \chi_{line})^{2},$$

$$B = T^{2}(V\chi_{line} + 1)^{2},$$

$$C = \frac{1}{(T(V + \chi_{tot}))^{2}}$$

$$\left[A\chi_{het}^{2} + B + 1 + 2\chi_{het}(V\sqrt{B} + T(V + \chi_{line})) + 2T(V^{2} - 1)\right],$$

$$D = \left(\frac{V\sqrt{B}\chi_{het}}{T(V + \chi_{tot})}\right)^{2}.$$
(37)

# **Acknowledgments**

**Funding:** This work is supported by Innovation Program for Quantum Science and Technology (Grant No. 2021ZD0300703), the National Natural Science Foundation of China (Grant No. 62101320), the Shanghai Municipal Science and Technology Major Project (Grant No. 2019SHZDZX01), and the Hebei Provincial Science and Technology Project (Grant No. 22310701D).

**Author contributions:** G.Z. conceived the research. Y.X. and T.W. carried out the experiment. Y.X. and T.W. analyzed the data and wrote the manuscript. P.H. provided the technical guide for SKR analysis and postprocessing. All authors contributed to the data collection, discussed the results, and reviewed the manuscript.

**Competing interests:** The authors declare that there is no conflict of interest regarding the publication of this article.

### **Data Availability**

The data that support the plots within this paper are available from the corresponding authors upon reasonable request.

# **References**

- <span id="page-13-0"></span>1. Gisin N, Ribordy G, Tittel W, Zbinden H. Quantum cryptography. *Rev Mod Phys*. 2002;74(1):145–195.
- <span id="page-13-1"></span>2. Grosshans F, Grangier P. Continuous variable quantum cryptography using coherent states. *Phys Rev Lett*. 2002;88(5):Article 057902.
- 3. Grosshans F, Van Assche G, Wenger J, Brouri R, Cerf NJ, Grangier P. Quantum key distribution using gaussianmodulated coherent states. *Nature*. 2003;421:238–241.
- 4. Weedbrook C, Lance AM, Bowen WP, Symul T, Ralph TC, Lam PK. Quantum cryptography without switching. *Phys Rev Lett*. 2004;93(17):Article 170504.
- 5. Renner R, Cirac JI. de Finetti representation theorem for infinitedimensional quantum systems and applications to quantum cryptography. *Phys Rev Lett*. 2009;102(11):Article 110504.
- 6. Leverrier A, Grangier P. Unconditional security proof of long-distance continuous-variable quantum key distribution with discrete modulation. *Phys Rev Lett*. 2009;102(18):Article 180504.
- 7. Leverrier A, Garcı́a-Patrón R, Renner R, Cerf NJ. Security of continuous-variable quantum key distribution against general attacks. *Phys Rev Lett*. 2013;110(3):Article 030502.
- 8. Jouguet P, Kunz-Jacques S, Leverrier A, Grangier P, Diamanti E. Experimental demonstration of long-distance continuous-variable quantum key distribution. *Nat Photonics*. 2013;7:378–381.
- 9. Qi B, Lougovski P, Pooser R, Grice W, Bobrek M. Generating the local oscillator "locally" in continuous-variable quantum key distribution based on coherent detection. *Phys Rev X*. 2015;5(4):Article 041009.
- 10. Soh DB, Brif C, Coles PJ, Lütkenhaus N, Camacho RM, Urayama J, Sarovar M. Self-referenced continuousvariable quantum key distribution protocol. *Phys Rev X*. 2015;5(4):Article 041010.
- 11. Huang D, Huang P, Lin D, Zeng G. Long-distance continuousvariable quantum key distribution by controlling excess noise. *Sci Rep*. 2016;6:19201.
- 12. Kleis S, Rueckmann M, Schaeffer CG. Continuous variable quantum key distribution with a real local oscillator using simultaneous pilot signals. *Opt Lett*. 2017;42(8):1588–1591.
- 13. Leverrier A. Security of continuous-variable quantum key distribution via a Gaussian de Finetti reduction. *Phys Rev Lett*. 2017;118(20):Article 200501.
- 14. Zhang G, Haw JY, Cai H, Xu F, Assad SM, Fitzsimons JF, Zhou X, Zhang Y, Yu S, Wu J, et al. An integrated silicon photonic chip platform for continuous-variable quantum key distribution. *Nat Photonics*. 2019;13:839–842.
- 15. Zhang Y, Chen Z, Pirandola S, Wang X, Zhou C, Chu B, Zhao Y, Xu B, Yu S, Guo H. Long-distance continuous-variable quantum key distribution over 202.81 km of fiber. *Phys Rev Lett*. 2020;125(1):Article 010502.
- 16. Wang H, Pi Y, Huang W, Li Y, Shao Y, Yang J, Liu J, Zhang C, Zhang Y, Xu B. High-speed Gaussian-modulated continuousvariable quantum key distribution with a local local oscillator based on pilot-tone-assisted phase compensation. *Opt Express*. 2020;28:32882–32893.
- 17. Ren S, Yang S, Wonfor A, White I, Penty R. Demonstration of high-speed and low-complexity continuous variable quantum key distribution system with local local oscillator. *Sci Rep*. 2021;11(1):9454.
- 18. Xu Y, Wang T, Li L, Zhao H, Huang P, Zeng G. Simultaneous continuous-variable quantum key distribution and classical

- optical communication over a shared infrastructure. *Appl Phys Lett*. 2023;123(15):Article 154001.
- <span id="page-13-2"></span>19. Li W, Zhang L, Tan H, Lu Y, Liao SK, Huang J, Li H, Wang Z, Mao HK, Yan B, et al. High-rate quantum key distribution exceeding 110 Mb s–1. *Nat Photonics*. 2023;17:416–421.
- <span id="page-13-3"></span>20. Wang S, Yin ZQ, He DY, Chen W, Wang RQ, Ye P, Zhou Y, Fan-Yuan GJ, Wang FX, Chen W, et al. Twin-field quantum key distribution over 830-km fibre. *Nat Photonics*. 2022;16: 154–161.
- 21. Liu Y, Zhang WJ, Jiang C, Chen JP, Zhang C, Pan WX, Ma D, Dong H, Xiong JM, Zhang CJ, et al. Experimental twin-field quantum key distribution over 1000 km fiber distance. *Phys Rev Lett*. 2023;130(21):Article 210801.
- 22. Wang W, Wang R, Hu C, Zapatero V, Qian L, Qi B, Curty M, Lo HK. Fully passive quantum key distribution. *Phys Rev Lett*. 2023;130(22):Article 220801.
- 23. Lu FY, Wang ZH, Zapatero V, Chen JL, Wang S, Yin ZQ, Curty M, He DY, Wang R, Chen W, et al. Experimental demonstration of fully passive quantum key distribution. *Phys Rev Lett*. 2023;131(11):Article 110802.
- 24. Li W, Zhang L, Lu Y, Li ZP, Jiang C, Liu Y, Huang J, Li H, Wang Z, Wang XB, et al. Twin-field quantum key distribution without phase locking. *Phys Rev Lett*. 2023;130(25):Article 250802.
- <span id="page-13-4"></span>25. Zhou L, Lin J, Xie YM, Lu YS, Jing Y, Yin HL, Yuan Z. Experimental quantum communication overcomes the rate-loss limit without global phase tracking. *Phys Rev Lett*. 2023;130(25):Article 250801.
- <span id="page-13-5"></span>26. Dianati M, Alléaume R, Gagnaire M, Shen X. Architecture and protocols of the future European quantum key distribution network. *Secur Commun Netw*. 2008;1:57–74.
- 27. Stucki D, Legre M, Buntschu F, Clausen B, Felber N, Gisin N, Henzen L, Junod P, Litzistorf G, Monbaron P, et al. Long-term performance of the SwissQuantum quantum key distribution network in a field environment. *New J Phys*. 2011;13:Article 123001.
- 28. Wang S, Chen W, Yin ZQ, Li HW, He DY, Li YH, Zhou Z, Song XT, Li FY, Wang D, et al. Field and long-term demonstration of a wide area quantum key distribution network. *Opt Express*. 2014;22:21739–21756.
- 29. Bedington R, Arrazola JM, Ling A. Progress in satellite quantum key distribution. *npj Quantum Inf*. 2017;3:Article 30.
- 30. Tajima A, Kondoh T, Ochi T, Fujiwara M, Yoshino K, Iizuka H, Sakamoto T, Tomita A, Shimamura E, Asami S, et al. Quantum key distribution network for multiple applications. *Quantum Sci Technol*. 2017;2(3):Article 034003.
- 31. Kiktenko EO, Pozhar NO, Duplinskiy AV, Kanapin AA, Sokolov AS, Vorobey SS, Miller AV, Ustimchik VE, Anufriev MN, Trushechkin AS, et al. Demonstration of a quantum key distribution network in urban fibre-optic communication lines. *Quantum Electron*. 2017;47(9):798.
- 32. Zhang Q, Xu F, Chen YA, Peng CZ, Pan JW. Large scale quantum key distribution: Challenges and solutions. *Opt Express*. 2018;26(18):24260–24273.
- 33. Fan-Yuan GJ, Lu FY, Wang S, Yin ZQ, He DY, Chen W, Zhou Z, Wang ZH, Teng J, Guo GC, et al. Robust and adaptable quantum key distribution network without trusted nodes. *Optica*. 2022;9(7):812–823.
- <span id="page-13-6"></span>34. Xu Y, Wang T, Zhao H, Huang P, Zeng G. Round-trip multi-band quantum access network. *Photonics Res*. 2023;11(8):1449–1464.
- <span id="page-13-7"></span>35. Chen YA, Zhang Q, Chen TY, Cai WQ, Liao SK, Zhang J, Chen K, Yin J, Ren JG, Chen Z, et al. An integrated space-

- to-ground quantum communication network over 4,600 kilometres. *Nature*. 2021;589:214–219.
- <span id="page-14-0"></span>36. Dynes J, Wonfor A, Tam WS, et al. Cambridge quantum network. *npj Quantum Inf*. 2019;5:Article 101.
- <span id="page-14-1"></span>37. Wonfor A, White C, Lord A, Nejabati R, Spiller TP, Dynes JF, Shields AJ, Penty RV, Quantum networks in the UK. In: *Metro and Data Center Optical Networks and Short-Reach Links* IV. Vol. 11712. SPIE. 2021:9–19.
- <span id="page-14-2"></span>38. Chen TY, Jiang X, Tang SB, Zhou L, Yuan X, Zhou H, Wang J, Liu Y, Chen LK, Liu WY, et al. Implementation of a 46-node quantum metropolitan area network. *npj Quantum Inf*. 2021;7:Article 134.
- <span id="page-14-3"></span>39. Fröhlich B, Dynes JF, Lucamarini M, Sharpe AW, Yuan Z, Shields AJ. A quantum access network. *Nature*. 2013;501:69–72.
- <span id="page-14-4"></span>40. Taylor HF, Lee CE. Apparatus and method for fiber optic intrusion sensing. US Patent 5,194,847. 1993.
- <span id="page-14-5"></span>41. Pan Z, Liang K, Ye Q, Cai H, Qu R, Fang Z. Phase-sensitive OTDR system based on digital coherent detection. In: *2011 Asia Communications and Photonics Conference and Exhibition (ACP)*. IEEE. 2011:1–6.
- <span id="page-14-6"></span>42. Juarez JC, Maier EW, Choi KN, Taylor HF. Distributed fiber-optic intrusion sensor system. *J Lightwave Technol*. 2005;23(6):2081–2087.
- 43. Selker JS, Thevenaz L, Huwald H, Mallet A, Luxemburg W, van de Giesen N, Steskal M, Zeman J, Westhoff M, Parlange MB. Distributed fiber-optic temperature sensing for hydrologic systems. *Water Resour Res*. 2006;42[:https://doi.](https://doi.org/10.1029/2006WR005326) [org/10.1029/2006WR005326.](https://doi.org/10.1029/2006WR005326)
- 44. Zhang Z, Bao X. Distributed optical fiber vibration sensor based on spectrum analysis of Polarization-OTDR system. *Opt Express*. 2008;16(14):10240–10247.
- 45. Koyamada Y, Imahama M, Kubota K, Hogari K. Fiber-optic distributed strain and temperature sensing with very high measurand resolution over long range using coherent OTDR. *J Lightwave Technol*. 2009;27(9):1142–1146.
- <span id="page-14-17"></span>46. Lu Y, Zhu T, Chen L, Bao X. Distributed vibration sensor based on coherent detection of phase-OTDR. *J Lightwave Technol*. 2010;28(22):3243–3249.
- 47. Peng F, Wu H, Jia XH, Rao YJ, Wang ZN, Peng ZP. Ultra-long high-sensitivity Φ-OTDR for high spatial resolution intrusion detection of pipelines. *Opt Express*. 2014;22:13804–13810.
- 48. Dong Y, Chen X, Liu E, Fu C, Zhang H, Lu Z. Quantitative measurement of dynamic nanostrain based on a phasesensitive optical time domain reflectometer. *Appl Opt*. 2016;55:7810–7815.
- 49. Chen D, Liu Q, He Z. Distributed fiber-optic acoustic sensor with sub-nano strain resolutionbased on time-gated digital OFDR. In: *Asia Communications and Photonics Conference*. Optica Publishing Group. 2017:S4A–2.
- <span id="page-14-8"></span>50. Chen D, Liu Q, He Z. High-fidelity distributed fiber-optic acoustic sensor with fading noise suppressed and sub-meter spatial resolution. *Opt Express*. 2018;26:16138–16146.
- <span id="page-14-7"></span>51. Lu P, Lalam N, Badar M, Liu B, Chorpening BT, Buric MP, Ohodnicki PR. Distributed optical fiber sensing: Review and perspective. *Appl Phys Rev*. 2019;6:Article 041302.
- <span id="page-14-9"></span>52. Marra G, Clivati C, Luckett R, Tampellini A, Kronjäger J, Wright L, Mura A, Levi F, Robinson S, Xuereb A, et al. Ultrastable laser interferometry for earthquake detectionwith terrestrial and submarine cables. *Science*. 2018;361(6401):486–490.
- <span id="page-14-10"></span>53. Chen JP, Zhang C, Liu Y, Jiang C, Zhao DF, Zhang WJ, Chen FX, Li H, You LX, Wang Z, et al. Quantum key

- distribution over 658 km fiber with distributed vibration sensing. *Phys Rev Lett*. 2022;128(18):Article 180502.
- <span id="page-14-11"></span>54. Degen CL, Reinhard F, Cappellaro P. Quantum sensing. *Rev Mod Phys*. 2017;89:Article 035002.
- <span id="page-14-12"></span>55. Pirandola S, Bardhan BR, Gehring T, Weedbrook C, Lloyd S. Advances in photonic quantum sensing. *Nat Photonics*. 2018;12:724–733.
- <span id="page-14-13"></span>56. Xu C, Zhang L, Huang S, Ma T, Liu F, Yonezawa H, Zhang Y, Xiao M. Sensing and tracking enhanced by quantum squeezing. *Photonics Res*. 2019;7:A14–A26.
- 57. Lawrie BJ, Lett PD, Marino AM, Pooser RC. Quantum sensing with squeezed light. *ACS Photonics*. 2019;6(6):1307–1318.
- 58. Guo X, Breum CR, Borregaard J, Izumi S, Larsen MV, Gehring T, Christandl M, Neergaard-Nielsen JS, Andersen UL. Distributed quantum sensing in a continuousvariableentangled network. *Nat Phys*. 2020;16:281–284.
- <span id="page-14-14"></span>59. Zhao SR, Zhang YZ, Liu WZ, Guan JY, Zhang W, Li CL, Bai B, Li MH, Liu Y, You L, et al. Field demonstration of distributed quantum sensing without post-selection. *Phys Rev X*. 2021;11:Article 031009.
- <span id="page-14-15"></span>60. Huang MF, Salemi M, Chen Y, Zhao J, Xia TJ, Wellbrock GA, Huang Y-K, Milione G, Ip E, Ji P, et al. First field trial of distributed fiber optical sensing and high-speed communication over an operational telecom network. *J Lightwave Technol*. 2019;38(1):75–81.
- 61. Huang YK, Ip E. Simultaneous optical fiber sensing and mobile front-haul access over a passive optical network. In: *Optical Fiber Communication Conference*. Optica Publishing Group. 2020:Th1K–4.
- 62. Guerrier S, Benyahya K, Dorize C, Awwad E, Mardoyan H, Renaudier J. Vibration detection and localization in buried fiber cable after 80km of SSMF using digital coherent sensing system with co-propagating 600Gb/s WDM channels. In: *2022 Optical Fiber Communications Conference and Exhibition (OFC)*. IEEE. 2022:1–3.
- 63. Ip E, Huang YK, Huang MF, Yaman F, Wellbrock G, Xia T, Wang T, Asahi K, Aono Y. DAS over 1,007-km hybrid link with 10-Tb/s DP-16QAMco-propagation using frequency-diverse chirped pulses. *J Lightwave Technol*. 2022;41(4):1077–1086.
- <span id="page-14-16"></span>64. He H, Jiang L, Pan Y, Yi A, Zou X, Pan W, Willner AE, Fan X, He Z, Yan L. Integrated sensing and communication in an optical fibre. *Light Sci Appl*. 2023;12:25.
- <span id="page-14-18"></span>65. Giovannetti V, Lloyd S, Maccone L. Advances in quantum metrology. *Nat Photonics*. 2011;5:222–229.
- <span id="page-14-19"></span>66. Xu F, Qi B, Lo HK. Experimental demonstration of phaseremapping attack in a practical quantum key distribution system. *New J Phys*. 2010;12:Article 113026.
- <span id="page-14-20"></span>67. Xu F, Ma X, Zhang Q, Lo HK, Pan JW. Secure quantum key distribution with realistic devices. *Rev Mod Phys*. 2020;92(2):Article 025002.
- <span id="page-14-21"></span>68. Gisin N, Fasel S, Kraus B, Zbinden H, Ribordy G. Trojan-horse attacks on quantum-key-distribution systems. *Phys Rev A*. 2006;73(2):Article 022320.
- <span id="page-14-22"></span>69. Jain N, Anisimova E, Khan I, Makarov V, Marquardt C, Leuchs G. Trojan-horse attacks threaten the security of practical quantum cryptography. *New J Phys*. 2014;16:Article 123030.
- <span id="page-14-23"></span>70. Jain N, Stiller B, Khan I, Makarov V, Marquardt C, Leuchs G. Risk analysis of Trojan-horse attacks on practical quantum key distribution systems. *IEEE J Sel Top Quantum Electron*. 2014;21(3):168–177.

- <span id="page-15-0"></span>71. Lucamarini M, Choi I, Ward MB, Dynes JF, Yuan Z, Shields AJ. Practical security bounds against the trojan-horse attack in quantum key distribution. *Phys Rev X*. 2015;5(3): Article 031030.
- <span id="page-15-1"></span>72. Fossier S, Diamanti E, Debuisschert T, Tualle-Brouri R, Grangier P. Improvement of continuous-variable quantum key distribution systems by using optical preamplifiers. *J Phys B Atomic Mol Phys*. 2009;42:Article 114014.