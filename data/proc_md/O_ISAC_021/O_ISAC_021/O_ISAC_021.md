

{0}------------------------------------------------

# Optical Integrated Sensing and Communication: Architectures, Potentials and Challenges

Yunfeng Wen, Fang Yang, Jian Song, and Zhu Han

### **ABSTRACT**

Integrated sensing and communication (ISAC) is viewed as a crucial component of future mobile networks and has gained much interest in both academia and industry. Similar to the emergence of radio-frequency (RF) ISAC, the integration of free space optical communication and optical sensing yields optical ISAC (O-ISAC), which is regarded as a powerful complement to its RF counterpart. In this article, we first introduce the generalized system structure of O-ISAC, and then elaborate on three advantages of O-ISAC, i.e., increasing communication rate, enhancing sensing precision, and reducing interference. Next, waveform design and resource allocation of O-ISAC are discussed based on pulsed waveform, constant-modulus waveform, and multi-carrier waveform. Furthermore, we put forward future trends and challenges of O-ISAC, which are expected to provide some valuable directions for future research.

#### INTRODUCTION

Future mobile networks are anticipated to provide both large communication capacities and high-precision sensing abilities simultaneously, which is regarded as a key enabler for numerous applications, e.g. intelligent transportation systems (ITS), human-computer interactions [1], and the Internet of Things (IoT). However, the isolated development of sensing and communication has resulted in inefficient spectrum and hardware resource utilization, which have been increasingly scarce in recent years. Consequently, the concept of integrated sensing and communication (ISAC) is motivated in the evolution of future mobile networks such as the sixth-generation (6G) systems.

The scope of ISAC encompasses the coexistence, cooperation, and co-design of communication and sensing. The independent operation of communication and sensing is maintained by coexistence, which reduces their mutual interference. Furthermore, performance gains can be obtained through cooperation, where communication and sensing share valuable information with each other. Finally, the system architecture and parameters can be jointly designed for com-

munication and sensing, which achieves the global optimum for the whole system. While coexistence is cost-effective, cooperation and co-design are indispensable for superior performances in both communication and sensing.

Up to now, numerous research has been conducted on the radio-frequency (RF) ISAC, spanning several areas like waveform design, networking, resource allocation, and information theory. Among these areas, waveform design has gained much interest as a fundamental aspect of ISAC. The ISAC waveform can be designed in a communication-centric or sensing-centric approach and can also be conceived from the ground up [2]. Towards this end, an enormous amount of RF-ISAC waveforms have been designed based on index modulation, linear frequency modulation (LFM), and orthogonal frequency division multiplexing (OFDM).

In the context of ISAC, the optical band exhibits striking similarities to the RF band. First, well-established RF-ISAC waveforms like LFM and OFDM can be transformed into optical waveforms, enabling optical devices like laser radars to provide communication and active sensing abilities simultaneously. Second, both free-space optical (FSO) communication and optical sensing can adopt the intensity modulation and direct detection (IM/DD) scheme, allowing for the sharing of optical frontends and baseband units. Third, the principles of information sharing and joint optimization apply to both RF and optical waveform, through which cooperation between communication and sensing can be achieved. However, significant differences still exist between FSO systems and their RF counterparts. Specifically, the unique characteristics of optical front-ends and channels offer promising advantages for communication and sensing, thereby serving as a powerful complement to RF-ISAC. In consequence, the integration of FSO communication and optical sensing gives rise to the concept of optical ISAC (O-ISAC).

This article investigates the basic architectures, opportunities, and challenges of O-ISAC to explore its vast potential. First, we outline the generalized system structure and then highlight

This work was supported in part by National Key Research and Development Program of China under Grant 2022YFE0101700; and in part by NSF CNS-2107216, CNS-2128368, CMMI-2222810, ECCS-2302469, US Department of Transportation, Toyota. Amazon and JST ASPIRE JPMJAP2326.

Digital Object Identifier: 10.1109/IOTM.001.2300196

Yunfeng Wen and Fang Yang (corresponding author) are with Tsinghua University, P. R. China, and also with the Research Institute of Tsinghua University in Shenzhen, P. R. China; Jian Song is with Tsinghua University, P. R. China, and also with the Shenzhen International Graduate School, Tsinghua University, P. R. China; Zhu Han is with the University of Houston, USA, and also with Kyung Hee University, South Korea.

{1}------------------------------------------------

![](_page_1_Figure_0.jpeg)

**FIGURE 1.** Generalized system structure of O-ISAC. The blocks in yellow, red, and green are those shared by communication and sensing, specific to communication, and specific to sensing, respectively.

![](_page_1_Figure_2.jpeg)

**FIGURE 2.** Three advantages of O-ISAC: increasing communication rate, enhancing sensing precision, and reducing interference.

three competitive advantages of O-ISAC. Second, waveform design and resource allocation aspects of O-ISAC are elaborated comprehensively based on widely adopted schemes such as pulsed waveform, constant-modulus waveform, and multi-carrier waveform. Third, we discuss the future trends of O-ISAC in conjunction with other emerging technologies, while also introducing the challenges to be addressed. We expect this article to provide valuable directions for future research in the field of O-ISAC.

## System Structure and Advantages of O-ISAC

O-ISAC integrates FSO communication and optical sensing in an individual system, where the appealing characteristics of optical band bring three advantages, i.e., increasing communication rate, enhancing sensing precision, and reducing multi-user interference (MUI), as illustrated in Fig. 2. In this section, the generalized system structure of O-ISAC is first outlined in the next section. Subsequently, the three advantages of O-ISAC are further elaborated in later sections, respectively.

#### System Structure of O-ISAC

The generalized system structure of O-ISAC is illustrated in Fig. 1. On the transmitter side, the communication data is first encoded and modu-

lated, and then integrated with the sensing signal to generate the O-ISAC signal. Then, the O-ISAC signal is direct-current (DC)-biased and transmitted to free space by the laser diode.

The O-ISAC signal propagates in an atmospheric channel and is impaired by attenuation, turbulence, and ambient light. While atmospheric attenuation and turbulence are usually considered at the receiver, the ambient light can be suppressed by incorporating a closed-loop circuit or photon coincidence detection [3]. Additionally, a portion of the O-ISAC signal is reflected by the target, whose spatial information is embedded into the reflected signal and then extracted by the sensing receiver.

On the receiver side, photon detector (PD) and analog-to-digital converter (A/D) are common modules shared by both communication and sensing receivers, followed by pre-processing units that suppress the ambient light and amplify the received signal. After the estimation of necessary parameters like the time of flight (ToF), target information like the distance and velocity can be attained by the sensing receiver, and the communication receiver can conduct synchronization, demodulation, and decoding.

Enlightened by the idea of perceptive mobile networks [4], the implementation of O-ISAC

On the receiver side, photon detector (PD) and analog-to-digital converter (A/D) are common modules shared by both communication and sensing receivers, followed by pre-processing units that suppress the ambient light and amplify the received signal.

{2}------------------------------------------------

The optical band provides even narrower beams than the millimeter-wave with the same aperture, and therefore different user devices and access points can be separated finely in the spatial domain.

| Characteristics          |                        | RF-ISAC        |            |                       |
|--------------------------|------------------------|----------------|------------|-----------------------|
|                          |                        | WiFi           | Mm-wave    | O-ISAC                |
| Physical properties      | Frequency              | 2.4 GHz, 5 GHz | 30–300 GHz | 28.3–845 THz          |
|                          | Amplitude              | Complex        |            | Real and non-negative |
|                          | (De)modulation         | Coherent       |            | IM/DD                 |
|                          | Channel                | LoS & NLoS     | Mostly LoS | LoS                   |
|                          | Interference           | Severe         | Moderate   | Slight                |
| Communication<br>metrics | Communication distance | < 100 m        | < 100 m    | < 1 km                |
|                          | Achievable data rate   | 100 Mb/s      | Gb/s      | Gb/s                 |
| Sensing metrics          | Sensing distance       | < 100 m        | < 1 km     | < 1 km                |
|                          | Distance resolution    | 0.1 m         | cm        | cm                   |
|                          | Angle resolution       | N/A            | 1 mrad    | 1 mrad               |

TABLE 1. Comparisons between RF-ISAC and O-ISAC.

becomes cost-effective on existing optical communication or sensing devices. Note that if the communication blocks in Fig. 1 are omitted, the working principle of the O-ISAC system is the same as a laser radar, i.e., the optical counterpart of a radar. Meanwhile, by modulating the transmitted optical signal, the laser radar can also conduct FSO communication with other existing FSO receivers. Therefore, implementing O-ISAC on a laser radar or other optical sensors is more appealing than developing a new system from the ground up, just like the deployment of RF-ISAC based on existing base stations.

However, even if O-ISAC resembles RF-ISAC in the ideologies of hardware reuse and unified waveform design, the main differences between them consist in optical front-ends and channels. For instance, RF-ISAC signal propagates through a dispersive channel where frequency-selective fading is non-negligible. On the contrary, FSO channels are usually recognized as atmospheric-turbulence channels, where atmospheric attenuation and turbulence are the main factors affecting the O-ISAC signal. Moreover, large antenna arrays in RF-ISAC are also substituted by laser diodes and PDs to transceive O-ISAC signal. To further understand these distinctions, comparisons between O-ISAC and well-established RF-ISAC schemes, i.e. WiFi and mm-wave, are described in Table 1. While the information on RF-ISAC can be found in [2], we elaborate on O-ISAC in the following subsections.

# Increasing Communication Rate

Contrary to the crowded RF spectrum, the optical band offers a broad unlicensed spectrum to conduct high-rate communication, and the communication rate of an experimental prototype utilizing 1550-nm laser can reach 100 Gbps at a distance of about 700 m [5]. Additionally, benefiting from the excellent monochromaticity, collimation, and coherence of laser beams, multiple independent data channels can be transmitted in parallel with multiplexing schemes like wavelength division multiplexing (WDM) and mode division multiplexing (MDM), through which the communication rate can be further enhanced.

Wavelength Division Multiplexing: The line-

width of laser diodes can be less than 1 nm, while their wavelength span can be in the order of 50 nm. Therefore, different optical signal can be divided finely in the wavelength domain, which lays the foundation for WDM. Considering the FSO data transmission system in [6], 16 modes with a spacing of 40 GHz (192.78–193.38 THz) are combined at the transmitter, and the receiver harnesses tunable optical bandpass filters to separate different signal. In consequence, 16 channels of communication data can be transmitted simultaneously, which increases the communication rate by 16 times.

Mode Division Multiplexing: Multiple data channels can also be loaded on different spatial modes, among which orbital angular momentum (OAM) is a common set of orthogonal modes. Laser beams with helical phase front can be quantified as different OAM states, and are orthogonal while propagating coaxially. Moreover, OAM-based MDM can be adopted concurrently with WDM to further increase the communication rate, and therefore the FSO data transmission system in [6] utilizes 16-WDM and 4-OAM beams simultaneously to provide 64 parallel channels in total.

# Enhancing Sensing Precision

As widely utilized optical sensors, laser radars are capable of detection, ranging, imaging, and recognition. Compared to their RF counterparts, laser radars can achieve a higher resolution and obtain more delicate spatial information under the same working principle, thanks to the wide bandwidth and small divergence angle of laser beams.

High Distance Resolution: The distance resolution is inversely proportional to the signal bandwidth. Since the optical band provides a wider bandwidth than that of the RF band, O-ISAC is anticipated to achieve a higher distance resolution than RF-ISAC. For instance, a frequency-modulated continuous-wave laser radar with downlink communication capability is demonstrated in [7], where an LFM signal with a bandwidth of 5 GHz is adopted to achieve a distance accuracy of ±2.2 cm under a signal-to-noise ratio (SNR) of 22.5 dB. Although a higher resolution is achieved by O-ISAC, it is not the only bottleneck in sensing, since the bandwidth of A/D, sampling rate, and noise also affect the sensing precision. Towards

{3}------------------------------------------------

![](_page_3_Figure_0.jpeg)

FIGURE 3. Waveform design for O-ISAC: a) pulsed waveform; b) constant-modulus waveform; c) multi-carrier waveform in the frequency domain.

this end, signal processing techniques like subspace methods can be adopted to enhance the sensing performance within limited hardware and bandwidth resources.

High Angle Resolution: The divergence angle of an electro-magnetic wave declines as its wavelength decreases under the same aperture. For instance, an 80-µrad divergence angle can be achieved by the 1550-nm laser ranging system in [8], which is much smaller than the milliradian-level divergence angle of mm-wave ISAC. Thereby, laser radars with collimated beams are capable of distinguishing targets that are probably located in the same angle unit of conventional radars, thus achieving a higher angle resolution than their RF counterparts. However, a higher angle resolution also demands a more delicate acquisition, tracking, and pointing mechanism, which poses more stringent requirements for both hardware and algorithms.

#### REDUCING INTERFERENCE

One of the urgent tasks for ISAC is to mitigate the interference between communication and sensing. The optical band provides even narrower beams than the millimeter-wave with the same aperture, and therefore different user devices and access points can be separated finely in the spatial domain. Furthermore, O-ISAC generally depends on LoS channels, which eliminates the potential interference as optical beams cannot penetrate opaque obstacles. Meanwhile, beam steering and beam management techniques can also be introduced to reduce interference.

LoS Channel: Regardless of the negligible penetration for opaque obstacles, the path loss of an optical channel is primarily determined by the propagation distance and the reflectance factor. The reflectance factor varies dramatically with the material and roughness of the reflector, ranging from 0.2 for rough concrete to 0.8 for silvered mirrors. However, even for a high reflectance factor, the multiplicative attenuation brought by the extra propagation distance still limits the power of none-LoS (NLoS) channels. Therefore, the interference that depends on NLoS channels can be ignored in general, which yields superior anti-interference abilities for O-ISAC.

**Beam Steering:** Similar to the beamforming techniques in RF-ISAC, O-ISAC can also exploit beam-steering techniques to achieve spatial divi-

sion multiplexing. By dynamically adjusting the direction and shape of laser beams, O-ISAC systems can avoid interference from unexpected sources and focus the beams precisely on the targets. While most existing beam-steering systems are bulky, fragile, and expensive, an acousto-optic beam-steering technique is reported in [9], which achieves 2-mrad angular resolution in a chip-scale system. Towards this end, it is worth studying to integrate these miniaturized beam-steering system into O-ISAC for superior communication and sensing performances.

## Waveform Design for O-ISAC

Waveform design is recognized as the foundation of ISAC, which focuses on designing an individual waveform that provides communication and sensing abilities simultaneously. Extensive research has been conducted on the waveform design for RF-ISAC, ranging from non-overlapped resource allocation to fully joint waveform design. However, an O-ISAC waveform based on the IM/DD scheme is restricted to being real and non-negative, and therefore most of the existing RF-ISAC waveforms are not readily applicable to O-ISAC, as they are complex in nature. To address this issue, several modifications have been proposed to make RF-ISAC waveform compatible with O-ISAC, like pulsed waveform, constant-modulus waveform, and multi-carrier waveform. Subsequently, waveform optimization and resource allocation can be further conducted for the prototype waveform to achieve the global optimal waveform design.

#### Pulsed Waveform

The pulsed waveform is broadly embraced by both optical wireless communication and optical sensing owing to its high energy efficiency and cost-effective implementation. Pulse position modulation (PPM), which encodes communication data onto pulses in specific binary slots, is proven to be optimal in terms of energy efficiency. Moreover, distance information can also be extracted from the ToF of pulses once they are reflected by targets, which is a common working principle for pulsed laser radars.

Since the position of pulses holds the information of communication data and target distance simultaneously, an O-ISAC scheme based on PPM is appealing, as illustrated in Fig. 3a. For instance, To obtain a real and non-negative optical signal, DC bias is necessary to guarantee that the negative part is not clipped. 

{4}------------------------------------------------

On the transmitter side, the complex baseband LFM-CPM signal is modulated to an intermediate frequency, whose real part is then DC-biased and utilized to modulate the intensity of the laser.

![](_page_4_Figure_1.jpeg)

FIGURE 4. Numerical results of O-ISAC based on DCO-OFDM. The SNR is defined as the ratio between the transmitted power and the noise power at the receiver, while the attenuation of the channel is normalized: a) BER versus SNR; b) RMSE for target distance versus SNR.

a pulse sequence sensing and pulse position modulation (PSS-PPM) scheme is proposed in [10], which modulates the position of pulses spread by m-sequences. Numerical simulations indicate that PSS-PPM can provide simultaneous communication and sensing abilities, even in the presence of severe MUI.

## CONSTANT-MODULUS WAVEFORM

The constant-modulus waveform is a subset of the subcarrier intensity modulation (SIM), where data is first modulated onto an electronic signal and then utilized to modulate the intensity of an optical signal [11]. To obtain a real and non-negative optical signal, DC bias is necessary to guarantee that the negative part is not clipped. However, the constant-modulus characteristics reduce the demand for DC bias, and constant-modulus waveform remains energy-efficient compared with non-constant-modulus waveforms like pulse amplitude modulation or quadrature amplitude modulation (QAM).

One example for the constant-modulus waveform is the combination of continuous phase modulation (CPM) and LFM, as displayed in Fig. 3b. On the transmitter side, the complex baseband LFM-CPM signal is modulated to an intermediate frequency, whose real part is then DC-biased and utilized to modulate the intensity of the laser. On the receiver side, the Hilbert transform and down-conversion are adopted to recover the baseband signal. Afterwards, the sensing receiver calculates the cross-correlation to obtain a maximum-likelihood estimation of the target distance. Meanwhile, the communication receiver multiplies the baseband signal with the conjugate LFM signal for de-chirp, followed by the Viterbi decoding. When the sensing precision is set as a constraint, the LFM-CPM waveform is demonstrated to achieve a higher spectral efficiency than conventional CPM waveforms [12].

#### Multi-Carrier Waveform

The multi-carrier waveform, as another subset of SIM, sends data over multiple subcarriers in parallel, and OFDM is one of the multi-carrier waveforms with orthogonal subcarriers. As illustrated in Fig. 3c, an element-wise-division method can be adopted by the OFDM-sensing receiver to eliminate the influences of transmitted sym-

bols in the frequency domain [13]. Note that the element-wise-division method is also readily applicable to O-ISAC, and therefore an O-ISAC system based on DC-biased optical OFDM (DCO-OFDM) is demonstrated by numerical simulations as follows.

To evaluate communication and sensing performances of the proposed O-ISAC system, 1 × 10<sup>4</sup> Monte-Carlo simulations are conducted to obtain the bit error rate (BER) for communication and the root mean square error (RMSE) for target distance estimation, as displayed in Fig. 4a and 4b, respectively. Each OFDM frame contains 32 OFDM symbols, while each OFDM symbol consists of 256 subcarriers with a spacing of 3.9 MHz, yielding a total bandwidth of nearly 1 GHz. For simplicity, all subcarriers adopt the same modulation scheme, i.e., 4QAM or 16QAM. Meanwhile, the sensing receiver utilizes the whole OFDM frame for target distance estimation, yielding a processing gain of 39.1 dB [13]. In addition, the DC bias b is set according to the standard deviation  $\sigma$  of the DCO-OFDM signal that is not clipped. Moreover, the channel model in [11] is adopted for a 200-m FSO link, which set the attenuation for communication and sensing as -2.2 dB and -23.2 dB, respectively.

Figure 4a indicates that the BER is affected by both the DC bias and the noise at the receiver. For an insufficient DC bias, the signal is severely distorted by the non-negative clipping, which deteriorates the communication performance even at the high-SNR region. On the contrary, an exorbitant DC bias reduces the energy efficiency, since the DC bias does not carry any communication data. Likewise, the RMSE can converge to an asymptotic region, as shown in Fig. 4b. The sensing receiver shows superior resistance to the non-linear distortion brought by an insufficient DC bias, as a declined DC bias leaves more power to resist larger channel attenuation for sensing.

#### RESOURCE ALLOCATION AND WAVEFORM OPTIMIZATION

Once the prototype waveform is selected for O-ISAC, it can be further optimized to achieve superior communication and sensing performances. Taking the LFM-CPM waveform from earlier as an example, optimization can be conducted on critical parameters like the chirp rate of LFM, the modulation index, and the modulation order

{5}------------------------------------------------

![](_page_5_Figure_0.jpeg)

FIGURE 5. Future trends of O-ISAC integrated with other emerging technologies.

her emerging technologies.

of CPM. For a fixed modulation order, the optimal values of chirp rate and modulation index are restricted on an ellipse determined by the sensing constraint, and an elliptical search algorithm is proposed to obtain these optimal values [12]. Once critical parameters are optimized, the optimal LFM-CPM waveform is also attained.

DCO-OFDM serves as another example for waveform optimization, which achieves the optimal waveform design by power allocation. On one hand, Fig. 4 indicates that a trade-off exists between the DC bias and the power on other subcarriers under the total power constraint. A guasi-concave relationship between the DC bias and the SNR on other subcarriers is revealed in [14], based on which the Newton method can be adopted to obtain the optimal DC bias for flat channels. On the other hand, once the Cramèr-Rao Bound (CRB) is selected as the performance metric, the optimal power allocation for sensing is to allocate all the power to the highest subcarrier. Since the optimal power allocation for communication follows a water-filling form in general, the power allocation on other subcarriers also embodies the trade-off between communication and sensing functionalities. Thereby, to obtain the optimal DCO-OFDM waveform for O-ISAC, a joint optimization problem can be formulated to optimize the DC bias and the power allocation for subcarriers simultaneously.

## FUTURE TRENDS AND CHALLENGES FOR O-ISAC

As a concept in the ascendant, O-ISAC is confronted with both opportunities and challenges. Advanced hardware and novel performance metrics are in urgent need, while emerging technologies like the hybrid system and deep learning (DL) can also be integrated with O-ISAC. To depict the future trends and challenges, a deep-learning-based O-ISAC system is illustrated in Fig. 5, while several potential directions and their corresponding challenges are discussed in the following subsections.

#### ADVANCED HARDWARE FOR O-ISAC

The widespread applications of O-ISAC rely on superior durability and miniaturization of optical hardware, which demands the replacement of bulky mechanical components in an optical system. Towards this end, micro-electro-mechanical system, liquid crystal, and optical phased array (OPA) have gained much interest, among which

OPA is an attractive scheme for both solid-state laser radars and FSO communication. OPA achieves beam steering by tuning the phases of an optical antenna array, which alters the phase front of the emitted optical beam. An OPA-based laser radar and FSO communication demonstrator is presented by [15], which achieves velocity extraction and chip-to-chip FSO communication at a distance of nearly 200 m and up to 50 m, respectively. Although advanced hardware contributes to the evolution of O-ISAC systems, theoretical models are urgently required to bridge the gap between novel hardware implementation and optimal system design.

#### Performance Metrics for O-ISAC

Owing to narrow beams and LoS channels, the received signal for an O-ISAC sensing receiver generally comes from the reflection of a point target, in contrast to the common extended target in RF-ISAC. This difference causes the invalidity of plentiful performance metrics dedicated to multi-target scenarios, like peak-to-sidelobe ratio and integrated-sidelobe ratio. Moreover, establishing an information-theory foundation for sensing is another urgent task for O-ISAC, which contributes to a unified performance metric in joint optimization. The main challenge lies in non-linear distortions of the O-ISAC signal, which yields complicated expressions for performance metrics [14]. A concise relationship between the waveform design and performance metrics deserves more consideration in future research of O-ISAC.

#### HYBRID RF AND OPTICAL ISAC

Although O-ISAC possesses superior anti-interference abilities, it is also vulnerable to obstacles that cause blind areas, which can be covered by RF-ISAC instead. Furthermore, the delay-doppler analysis enables RF-ISAC to sense multiple moving targets simultaneously, while IM/DD-based O-ISAC cannot extract velocity information directly. Therefore, O-ISAC and RF-ISAC should become powerful complements to each other, yielding a hybrid RF and optical ISAC system illustrated in Fig. 5. A hybrid RF and optical ISAC system can be implemented in a parallel-transmission-based approach, where power and bandwidth are allocated to both RF-ISAC and O-ISAC simultaneously. Besides, the hybrid system can also be implemented by switching between

Although O-ISAC possesses superior anti-interference abilities, it is also vulnerable to obstacles that cause blind areas, which can be covered by RF-ISAC instead.

{6}------------------------------------------------

RF-ISAC and O-ISAC according to channel states and user requirements. The critical problem to be solved is to unify the performance metrics of both RF-ISAC and O-ISAC, through which joint optimization can be conducted to achieve the global optimal design for the hybrid system.

# Deep Learning forO-ISAC

As the scenarios and requirements of O-ISAC are increasingly complicated, the end-to-end optimization method of DL can be introduced to enhance the performances of O-ISAC. DL can serve the waveform design and resource allocation process of O-ISAC instead of conventional optimization algorithms. In addition, DL can also provide functionalities of target recognition, behaviour prediction, and semantic communication, which are not included in traditional ISAC. However, the requirements for high-quality datasets and tremendous computing resources are not negligible when designing a DL-based O-ISAC system. One approach to resolving these problems is to conduct training and deduction at computing centers, which adds extra payloads of data transmission. Therefore, while a conventional O-ISAC system mainly focuses on the trade-off between communication and sensing, computing will also become progressively more important in a DL-based O-ISAC system.

# Conclusions

In this article, the generalized system structure of O-ISAC was introduced, based on which three appealing advantages of FSO systems were presented, i.e., increasing communication rate, enhancing sensing precision, and reducing interference. Additionally, waveform design, as the foundation of O-ISAC, was discussed comprehensively based on the commonly adopted pulsed waveform, constant-modulus waveform, and multi-carrier waveform. Furthermore, future trends and challenges for O-ISAC were also put forward, which called for the integration of several cutting-edge technologies with O-ISAC. By addressing these issues, O-ISAC is expected to become a powerful complement to RF-ISAC and also a crucial enabler for numerous applications that will change lives in the near future.

## References

- [1] O. Rinchi *et al.*, "LiDAR Technology for Human Activity Recognition: Outlooks and Challenges," *IEEE Internet Things Mag.*, vol. 6, no. 2, June 2023, pp. 143–50.
- [2] F. Liu *et al.*, "Integrated Sensing and Communications: Toward Dual-Functional Wireless Networks for 6G and Beyond," *IEEE JSAC*, vol. 40, no. 6, June 2022, pp. 1728–17.
- [3] M. Beer *et al.*, "SPAD-Based Flash LiDAR Sensor with High Ambient Light Rejection for Automotive Applications," *Quantum Sensing and Nano Electronics and Photonics XV*, vol. 10540, San Francisco, CA, Jan. 2018, p. 105402G.
- [4] A. Zhang *et al.*, "Perceptive Mobile Networks: Cellular Networks with Radio Vision via Joint Communication and Radar Sensing," *IEEE Vehic. Tech. Mag.*, vol. 16, no. 2, Dec. 2020, pp. 20–30.

- [5] S. M. Walsh *et al.*, "Demonstration of 100 Gbps Coherent Free-Space Optical Communications at LEO Tracking Rates," *Sci. Rep.*, vol. 12, no. 1, Oct. 2022.
- [6] B. Dutta *et al.*, "640 Gbps FSO Data Transmission System Based on Orbital Angular Momentum Beam Multiplexing Employing Optical Frequency Comb," *Opt. Quantum Electron.*, vol. 54, no. 2, Feb. 2022, p. 132.
- [7] Z. Xu *et al.*, "Frequency-Modulated Continuous-Wave Coherent Lidar with Downlink Communications Capability," *IEEE Photon. Technol. Lett.*, vol. 32, no. 11, Apr. 2020, pp. 655–58.
- [8] B. Du *et al.*, "Highspeed Photon-Counting Laser Ranging for Broad Range of Distances," Sci. Rep., vol. 8, no. 1, Mar. 2018, p. 4198.
- [9] B. Li, Q. Lin, and M. Li, "Frequency–Angular Resolving LiDAR Using Chip-Scale Acousto-Optic Beam Steering," *Nature*, vol. 620, no. 7973, June 2023, pp. 316–322.
- [10] Y. Wen *et al.*, "Pulse Sequence Sensing and Pulse Position Modulation for Optical Integrated Sensing and Communication," *IEEE Commun. Lett.*, vol. 27, no. 6, Apr. 2023, pp. 1525–29.
- [11] H. Liu *et al.*, "BER Analysis of A Hybrid Modulation Scheme Based on PPM and MSK Subcarrier Intensity Modulation," *IEEE Photon. J.*, vol. 7, no. 4, June 2015, pp. 1–10.
- [12] Y. Wen *et al.*, "Free Space Optical Integrated Sensing and Communication Based on LFM and CPM," *IEEE Commun. Lett.*, vol. 28, no. 1, Nov. 2023, pp. 43–47.
- [13] C. Sturm and W. Wiesbeck, "Waveform Design and Signal Processing Aspects for Fusion of Wireless Communications and Radar Sensing," *Proc. IEEE*, vol. 99, no. 7, May 2011, pp. 1236–59.
- [14] X. Ling *et al.*, "Offset and Power Optimization for DCO-OFDM in Visible Light Communication Systems," *IEEE Trans. Signal Process.*, vol. 64, no. 2, Sept. 2016, pp. 349–63.
- [15] C. V. Poulton *et al.*, "Long-range LiDAR and Free-Space Data Communication with High-Performance Optical Phased Arrays," *IEEE J. Sel. Topics Quantum Electron.*, vol. 25, no. 5, pp. 1–8, Mar. 2019.

## Biographies

Yunfeng Wen (wenyf22@mails.tsinghua.edu.cn) received his B.S. degree from the Department of Electronic Engineering, Tsinghua University, Beijing, China, in 2022. He is currently pursuing his Ph.D. degree with the DTV Technology R&D Center, Department of Electronic Engineering, Tsinghua University, Beijing, 100084, China. His research interests include free space optical communication, optical sensing, and in particular, integrated sensing and communication.

Fang Yang [SM] (fangyang@tsinghua.edu.cn) is an associate professor with the Department of Electronic Engineering, Tsinghua University, Beijing 100084, China. He received his B.S.E. and Ph.D. degrees in electronic engineering from Tsinghua University, Beijing, China, in 2005 and 2009, respectively. His research interests include visible and wireless communications. He received the IEEE Scott Helt Memorial Award (2015). He is an Institution of Engineering and Technology Fellow.

Jian Song [F] (jsong@tsinghua.edu.cn) is the director of the Tsinghua DTV Technology R&D Center, Tsinghua University, Beijing 100084, China. He received his B. Eng and Ph.D. degrees in electrical engineering from Tsinghua University, in 1990 and 1995, respectively. His current research interest is in the area of digital TV broadcasting. He has published more than 300 peer-reviewed journal and conference papers. He holds two U.S. and more than 80 Chinese patents. He is a Fellow of IET.

Zhu Han [F] (hanzhu22@gmail.com) is a professor in the Electrical and Computer Engineering Department and the Computer Science Department at the University of Houston, Houston, Texas 77004 USA. He received his B.S. degree in electronic engineering from Tsinghua University in 1997, and his M.S. and Ph.D. degrees in electrical and computer engineering from the University of Maryland, College Park, in 1999 and 2003, respectively.