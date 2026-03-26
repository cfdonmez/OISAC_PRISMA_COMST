![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_1.jpeg)

*Article*

# **Optical Camera-Based Integrated Sensing and Communication for V2X Applications: Model and Optimization**

**Ke Dong 1,2,[\\*](https://orcid.org/0000-0001-9801-0984) , Wenying Cao <sup>1</sup> and Mingjun Wang 1,2**

- <sup>1</sup> School of Automation and Information Engineering, Xi'an University of Technology, Xi'an 710049, China; 3210432028@stu.xaut.edu.cn (W.C.); wangmingjun@xaut.edu.cn (M.W.)
- <sup>2</sup> Xi'an Key Laboratory of Wireless Optical Communication and Network Research, Xi'an 710049, China
- **\*** Correspondence: kedong@xaut.edu.cn

#### **Abstract**

An optical camera-based integrated sensing and communication (OC-ISAC) system model is proposed to address the intrinsic requirements of vehicular-to-everything (V2X) applications in complex outdoor environments. The model enables the coexistence and potential mutual enhancement of environmental sensing and data transmission within the visible light spectrum. It characterizes the OC-ISAC channel by modeling how light, either actively emitted for communication or passively reflected from the environment, originating from any voxel in three-dimensional space, propagates to the image sensor and contributes to the observed pixel values. This framework is leveraged to systematically analyze the impact of camera imaging parameters, particularly exposure time, on the joint performance of sensing and communication. To address the resulting trade-off, we develop an analytically tractable suboptimal algorithm that determines a near-optimal exposure time in closed form. Compared with the exhaustive numerical search for the global optimum, the suboptimal algorithm reduces computational complexity from *O*(*N*) to *O*(1), while introducing only a modest average normalized deviation of 5.71%. Both theoretical analysis and experimental results confirm that, in high-speed communication or mobile sensing scenarios, careful selection of exposure time and explicit compensation for the camera's low-pass filtering effect in receiver design are essential to achieving optimal dual-functional performance.

**Keywords:** visible light communication; optical camera communication; integrated sensing and communication; OC-ISAC; vehicle-to-everything communication; channel model; exposure effect

![](_page_0_Picture_11.jpeg)

Academic Editor: Sicong Liu

Received: 11 October 2025 Revised: 14 November 2025 Accepted: 16 November 2025 Published: 19 November 2025

**Citation:** Dong, K.; Cao, W.; Wang, M. Optical Camera-Based Integrated Sensing and Communication for V2X Applications: Model and Optimization. *Sensors* **2025**, *25*, 7061. <https://doi.org/10.3390/s25227061>

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license [\(https://creativecommons.org/](https://creativecommons.org/licenses/by/4.0/) [licenses/by/4.0/\)](https://creativecommons.org/licenses/by/4.0/).

# **1. Introduction**

In vehicular communication networks, optical camera communication (OCC) has emerged as a promising alternative to traditional radio-frequency systems for vehicle-toeverything (V2X) connectivity [\[1,](#page-18-0)[2\]](#page-18-1). By leveraging the widespread deployment of LED light sources and vehicle-mounted cameras, OCC enables low-cost, lightweight transceivers operating over the unlicensed optical spectrum. Its inherently limited coverage further enhances communication security by reducing the likelihood of eavesdropping. Despite these advantages, applying OCC to V2X scenarios encounters two categories of challenges. First, the outdoor vehicular environment is highly dynamic, with rapidly changing propagation conditions, fluctuating illumination, and strong natural and artificial light interference, leading to severe attenuation and multipath distortion [\[3\]](#page-18-2). Second, using a camera as

*Sensors* **2025**, *25*, 7061 2 of 20

the communication receiver introduces inherent non-idealities from the imaging mechanism—such as exposure-dependent integration, low frame rates, sensor nonlinearities, and shutter constraints—that significantly distort the recovered waveform [\[4\]](#page-18-3). These environmental and sensor-induced impairments jointly shape the received optical signal, thereby tightly coupling communication and sensing behaviors.

To address these limitations, intensive research has been conducted in multiple dimensions. From a channel characterization perspective, studies have focused on modeling the propagation environment [\[5\]](#page-18-4), camera imaging models [\[6\]](#page-18-5), and exposure-effect analysis [\[7\]](#page-18-6). In terms of communication mechanisms, advancements include efficient modulation and coding schemes [\[8](#page-18-7)[–11\]](#page-18-8), resource multiplexing strategies [\[12](#page-19-0)[,13\]](#page-19-1), channel equalization techniques [\[14–](#page-19-2)[16\]](#page-19-3), and region-of-interest (RoI) detection and tracking approaches [\[17](#page-19-4)[,18\]](#page-19-5). Performance evaluation studies have investigated how bit error rate (BER) [\[19\]](#page-19-6) and channel capacity [\[20\]](#page-19-7) are affected by exposure effects and link distance [\[21\]](#page-19-8). On the standardization front, several physical-layer techniques for OCC have been specified within the amended IEEE 802.15.7 standard [\[22\]](#page-19-9). In addition, studies have demonstrated that OCC can be integrated with object detection [\[23\]](#page-19-10) and localization techniques [\[24](#page-19-11)[,25\]](#page-19-12), proving the coexistence and mutual enhancement of communication and sensing.

The dual role of the camera as a sensor and receiver makes OCC similar to integrated sensing and communication (ISAC) in radio frequency vehicular communication [\[26–](#page-19-13)[28\]](#page-19-14), which explores service coexistence, functional cooperation, and network reciprocity. However, the conclusions for ISAC cannot be directly applied to optical camera-based ISAC (OC-ISAC) because of the differences in system architecture. In recent years, integrated optical communication and sensing (O-ISAC) has gained significant attention in fields such as fiber-optic communication, free-space optical (FSO) communication, and visible light communication (VLC) [\[29–](#page-19-15)[34\]](#page-19-16).

Although OCC has been widely studied, existing work typically addresses either its communication challenges or the use of communication signals to support sensing, without situating OCC within a unified ISAC framework. Current O-ISAC studies are further limited to indoor or low-dynamic settings and do not account for the rapidly changing illumination and mobility inherent to outdoor V2X scenarios. As a result, no existing approach leverages the camera's optical imaging mechanism to establish a unified model that jointly analyzes and optimizes sensing and communication, nor to quantify the potential performance gains of optical camera-based integrated sensing and communication (OC-ISAC) for vehicular applications.

This paper introduces a novel OC-ISAC system model for outdoor V2X communication that accounts for the camera's dual role in both imaging and communication. An integrated channel model is proposed accordingly, incorporating voxel-dependent reflection and luminous factors to characterize pixel value variations caused by transceiver mobility and LED flicker. This model enables performance analysis of both environmental sensing and data communication. Additionally, an optimization problem is formulated for camera exposure time, and a suboptimal yet analytically tractable solution is derived to balance the trade-offs between the two functionalities.

The rest of this paper is organized as follows. Section [2](#page-2-0) introduces the proposed OC-ISAC system architecture and develops an integrated channel model for sensing and communication based on the camera's imaging mechanism. Section [3](#page-7-0) assesses the impact of the integrated channel on the performance of both sensing and communication. Section [4](#page-9-0) addresses optimizing the camera's exposure time to maximize the average signal-to-noise ratio (SNR) for communication and sensing. Section [5](#page-11-0) presents numerical and simulation results to validate the theoretical analysis. Finally, Section [6](#page-17-0) concludes the paper and suggests potential directions for future research.

*Sensors* **2025**, *25*, 7061 3 of 20

# <span id="page-2-0"></span>**2. System Model**

### *2.1. OC-ISAC Architecture*

Figure [1](#page-2-1) illustrates a typical V2X communication scenario based on OCC. While driving, vehicles exchange information with other vehicles (V2V) or infrastructure (V2I/I2V) to enhance traffic efficiency and safety. At the transmitter side, LEDs embedded in headlights, taillights, or traffic signals modulate the data. On the receiver side, onboard and surveillance cameras capture the optical signals to retrieve the transmitted information. Before that, in dynamic outdoor environments, the receivers must detect, identify, and track communication sources despite significant interference from line-of-sight (LOS) and nonline-of-sight (NLOS) paths. This highlights the importance of integrating sensing and communication. Therefore, establishing an OC-ISAC system is crucial for ensuring reliable V2X communications in complex outdoor conditions.

<span id="page-2-1"></span>![](_page_2_Picture_4.jpeg)

**Figure 1.** Illustration of a typical OCC-based V2X communication scenario. V2V: vehicle's head/tail lights to onboard camera. V2I: vehicle's head/tail lights to surveillance camera. I2V: traffic lights to onboard camera.

Figure [2](#page-3-0) illustrates the architecture of the OC-ISAC system, which leverages the optoelectronic conversion capabilities of image sensors to enable simultaneous environmental perception and data communication. The system categorizes light sources into two types: communication light and sensing light. Communication light is emitted by vehicle and infrastructure LEDs and transmitted through intensity modulation. In contrast, sensing light, which includes sunlight, moonlight, and artificial illumination, provides environmental information through reflection.

This paper examines a typical scenario in which communication light travels along direct line-of-sight paths to optimize the SNR. In contrast, sensing light arrives through NLOS paths, often via reflection. In practice, both communication and sensing light can reach the camera through LOS and NLOS paths. For example, wet road reflections or backlighting make these signals deviate from their expected paths, which complicates reliable sensing and communication.

*Sensors* **2025**, *25*, 7061 4 of 20

<span id="page-3-0"></span>![](_page_3_Figure_1.jpeg)

**Figure 2.** Architecture of the OC-ISAC system, which simultaneously enables communication (blue area) and sensing (green area) with a shared camera. Data-modulated communication light and environment-reflected sensing light, propagating via LOS and/or NLOS paths, are captured by a camera and converted into digital pixel values through photoelectric detection. The spatial–temporal distribution of these pixel values is jointly exploited by the communication and sensing receivers to extract data symbols and environmental information, respectively. Moreover, the two functions mutually assist each other, enabling collaborative communication and sensing.

At the receiver, the optical camera serves as the system core. Converting incident light into digital image sequences generates pixel sets that simultaneously encode data and environmental information. The communication domain demodulates the transmitted data according to pixel spatiotemporal patterns and outputs payloads to higher layers. In parallel, the sensing domain extracts features from image sequences, enabling scene understanding and providing standardized metrics for sensing applications.

In this manner, OC-ISAC achieves the dual function of sensing and communication through a shared hardware infrastructure (LEDs and cameras). More importantly, the two functions are mutually enhanced. For instance, reliable communication links depend on real-time light-source tracking, essentially a sensing task, while camera-based VLC positioning benefits from communication-derived source information, significantly improving localization accuracy.

#### *2.2. List of Symbols*

For clarity and convenience, the key symbols and definitions employed in this work are listed in Table [1.](#page-3-1)

<span id="page-3-1"></span>**Table 1.** List of symbols.

| Symbol     | Description                                                  | Unit       |
|------------|--------------------------------------------------------------|------------|
| A          | Conversion gain of the image sensor                          | -          |
| β(d)       | Signal attenuation for light propagation over distance d     | -          |
| Te         | Exposure time of image sensor                                | µs         |
| ⃗r         | Position vector in 3-D space                                 | m          |
| Ic         | Maximum intensity of the communication light source          |            |
| fc, ac, ϕc | Amplitude, frequency, and phase of the communication carrier | V, Hz, rad |

*Sensors* **2025**, *25*, 7061 5 of 20

**Table 1.** *Cont.*

| Symbol | Description                                                    | Unit    |
|--------|----------------------------------------------------------------|---------|
| Ie     | Maximum intensity of the sensing light source                  |         |
| fx, ϕx | Spatial frequency and phase of sensing along given direction x | Hz, rad |
| v      | Speed of motion                                                | m/s     |
| η      | Luminous factor caused by data modulation                      | -       |
| ξ      | Reflective factor caused by environmental mobility             | -       |

#### *2.3. Voxel-to-Pixel Channel Model*

The OCC-based V2X application scenario in Figure [1](#page-2-1) and the OC-ISAC architecture in Figure [2](#page-3-0) highlight that the communication and sensing functions rely on the light propagated through a complex three-dimensional environment and captured by a camera-based receiver. Such characteristics cannot be sufficiently described by conventional wireless channel models or standard optical LOS formulations. To capture the spatially distributed nature of light interaction in OC-ISAC, it is necessary to introduce the concept of a voxel, which represents a small volumetric element in the 3D environment. Each voxel acts as an elementary optical contributor whose reflectance or self-emission influences one or more pixels depending on its geometric projection and distance to the camera. Modeling the channel via a voxel-to-pixel mapping explicitly describes how the environmental structure transforms emitted or reflected light into a pixel-wise intensity distribution. This modeling approach allows the contributions of voxels to be integrated into the camera exposure process, thereby linking the physical propagation, spatial geometry, and temporal integration into a unified analytical form suitable for ISAC analysis.

Figure [3](#page-4-0) illustrates the proposed voxel-to-pixel (VP) channel model for OC-ISAC. For a given pixel *k* on the 2-D image sensor, we can determine its corresponding voxel at a position vector⃗*r* in 3-D space using the pinhole camera geometry, which relies on the camera's parameters and the physical environment. This process establishes a mapping from voxel to pixel. The information represented by the pixel value is directly related to the optical properties of the corresponding voxel, particularly how it interacts with communication and sensing light. Utilizing this voxel-to-pixel mapping, we systematically describe the OC-ISAC channel model from three perspectives: the communication channel, the sensing channel, and the pixel value generation process.

<span id="page-4-0"></span>![](_page_4_Picture_6.jpeg)

**Figure 3.** Illustration of the voxel-to-pixel channel model for OC-ISAC. The *k*-th pixel value corresponding to a vehicle's taillights in the camera output image is determined by the sum of the light intensities incident on the pixels, which results from the propagation path loss *β* of two components originating from a voxel on the taillight at the position ⃗*r* in 3-D space: (1) illumination used as communication light for data modulation, and (2) reflection of ambient light used as sensing light for acquiring environmental information.

*Sensors* **2025**, *25*, 7061 6 of 20

## 2.3.1. Communication Channel

When a voxel is part of a communication light source (e.g., a car's headlamp or taillight), it emits light to a corresponding pixel. In an intensity modulation and direct detection (IM/DD) system, the transmitter modulates data by varying the light intensity over time. The voxel's optical property is the product of a time-varying luminous factor (LF), *η*(⃗*r*, *t*) ∈ [0, 1], and the source's maximum luminous intensity, *Ic*. The modulation scheme defines LF's temporal behavior. For example, in On-Off Keying (OOK), LF is binary (0 or 1), while in continuous wave modulation, LF can vary continuously between 0 and 1. Thus, LF's temporal behavior models the communication method in the OC-ISAC system. The received luminous intensity at pixel *k* from the voxel, assuming distance *d*, is expressed as follows:

<span id="page-5-0"></span>
$$i_{k,c}(t) = \beta(d) \cdot I_c \cdot \eta(\vec{r}, t) \tag{1}$$

where *β*(*d*) represents the path loss factor over the distance *d*.

#### 2.3.2. Sensing Channel

When a voxel is illuminated by light, it reflects off its surface and projects onto the camera's image sensor, creating a second incident light beam. Assuming constant ambient light intensity, *I<sup>e</sup>* , the voxel's reflectance determines the light intensity at a pixel. As the voxel corresponding to a pixel changes over time due to relative motion, the reflectance varies. The reflectance of voxel⃗*r* at pixel *k* can be modeled as a time-varying reflection factor (RF) *ξ*(⃗*r*, *t*) ∈ [0, 1]. RF's temporal variation depends on relative motion, speed, and surrounding voxel reflectance. Thus, the luminous intensity of ambient light projected onto the pixel after reflection from a voxel at a distance *d* is expressed as follows:

$$i_{k,e}(t) = \beta(d) \cdot I_e \cdot \xi(\vec{r}, t). \tag{2}$$

In practical scenarios, a given voxel corresponding to a pixel may simultaneously function as both a communication light source and a sensing object, which means it can both emit and reflect light. Therefore, the total luminous intensity incident on a pixel is the sum of the two light beams:

$$i_k(t) = i_{k,c}(t) + i_{k,e}(t) = \beta(d)[I_c\eta(\vec{r},t) + I_e\xi(\vec{r},t)].$$
 (3)

# 2.3.3. Pixel Value

An image sensor converts the optical intensity incident on each pixel into a digital pixel value, which is organized in a two-dimensional matrix to form an image. The imaging process is governed by a precisely controlled exposure mechanism. As illustrated in Figure [4,](#page-6-0) a chain of "photodetector, integration, and sampling" summarizes the conversion from incident light to pixel value output for each pixel in the image sensor.

Each pixel integrates the incident optical power during exposure, which is controlled by the shutter. The photodetector generates a photocurrent that accumulates over the exposure duration *T<sup>e</sup>* . The accumulated current is converted into a voltage through a trans-impedance amplifier (TIA) and subsequently sampled at the end of the exposure. The digital value of a pixel is obtained after saturation and analog-to-digital conversion (ADC). For analytical tractability, the effects of ADC quantization and saturation are neglected. Therefore, the output of the *k*-th pixel can then be approximated as the accumulated photocurrent during *T<sup>e</sup>* as follows:

<span id="page-5-1"></span>
$$v_k(t) = A \int_{t-T_e}^t i_k(\tau) d\tau + n(t), \tag{4}$$

*Sensors* **2025**, *25*, 7061 7 of 20

where *A* represents the conversion gain of the image sensor, which accounts for the responsibility of the photodetector and the amplification factor of the trans-impedance amplifier [\[6\]](#page-18-5), and *n*(*t*) represents additive white Gaussian noise (AWGN) with zero mean and power spectral density *N*0. The digital pixel value is obtained by sampling *v<sup>k</sup>* (*t*) at the end of the exposure.

<span id="page-6-0"></span>![](_page_6_Figure_2.jpeg)

**Figure 4.** Schematic diagram of the photoelectric conversion process in pixels of image sensors

### *2.4. Signal Model*

This section derives the output signal expressions for communication and sensing under given modulation, environmental, and imaging parameters.

### 2.4.1. Communication Signal

Assuming a single-tone continuous wave modulation scheme (the derivation also holds for other schemes, e.g., OOK), the LF in Equation [\(1\)](#page-5-0) is as follows:

<span id="page-6-2"></span>
$$\eta(\vec{r},t) = a_c \left[ \frac{1}{2} + \frac{1}{2} \cos(2\pi f_c t + \phi_c) \right]$$
(5)

where *a<sup>c</sup>* ∈ [0, 1], *f<sup>c</sup>* > 0, and *ϕ<sup>c</sup>* ∈ [0, 2*π*] denote the carrier's amplitude, frequency, and phase, respectively. The constant offset 1/2 ensures non-negativity of the intensitymodulated signal.

#### 2.4.2. Sensing Signal

Imaging maps object reflectance in 3-D space to pixel values in 2-D images, enabling environment sensing. Camera motion causes translational shifts in output images, and excessive speed introduces motion blur, degrading sensing quality. In the VP channel model, mobility alters voxel–pixel mapping, making pixel values fluctuate based on environmental complexity (i.e., reflectance differences between adjacent voxels) and motion speed. We use a simplified model to study temporal variations in pixel values as the camera perceives environments of different complexities during motion.

Suppose that the reflectance of the voxels in a given environment along the *x*-axis follows a cosine distribution:

<span id="page-6-1"></span>
$$u(\vec{r}) = \frac{1}{2} + \frac{1}{2}\cos(2\pi f_x \vec{r}) \tag{6}$$

where *f<sup>x</sup>* is the spatial frequency characterizing scene complexity, the direct current (DC) component with a scaling factor 1/2 ensures *u*(⃗*r*) ∈ [0, 1]. Although actual reflectance variations can be expressed as a Fourier series with infinite spatial frequencies in all directions, *Sensors* **2025**, *25*, 7061 8 of 20

Equation [\(6\)](#page-6-1) represents the simplest form, featuring a single frequency component *f<sup>x</sup>* along a specific direction *x*.

If the voxel moves uniformly along the *x*-axis with speed *v*, the reflectance evolves as a temporal modulation given by the following:

<span id="page-7-1"></span>
$$\xi(\vec{r},t) = u(\vec{r} - vt) = \frac{1}{2} + \frac{1}{2}\cos(2\pi f_x vt - \phi_x(\vec{r}))$$
 (7)

where *ϕx*(⃗*r*) is an initial phase determined by voxel position. It implies that the incident light intensity oscillates at a frequency *fxv*, i.e., the product of environment complexity and motion speed.

Substituting Equations [\(5\)](#page-6-2) and [\(7\)](#page-7-1) into Equation [\(4\)](#page-5-1) yields the induced voltage after exposure:

$$v_k(t) = C_c + E_c \cos(2\pi f_c t + \phi - D_c) + C_e + E_e \cos(2\pi f_x v t + \phi_x(\vec{r}) - D_e) + n(t)$$
(8)

<span id="page-7-2"></span>where

<span id="page-7-3"></span>
$$C_{c} = \frac{A\beta(d)a_{c}I_{c}T_{e}}{2}, \qquad C_{e} = \frac{A\beta(d)I_{e}T_{e}}{2}$$

$$E_{c} = \frac{A\beta(d)a_{c}I_{c}\sin(\pi f_{c}T_{e})}{2\pi f_{c}}, \qquad E_{e} = \frac{A\beta(d)I_{e}\sin(\pi f_{x}vT_{e})}{2\pi f_{x}v}$$

$$D_{c} = \pi f T_{e}, \qquad D_{e} = \pi f_{x}vT_{e}.$$

$$(9)$$

The final pixel value is obtained following sampling, ADC, and saturation, governed by the shutter mechanism.

# <span id="page-7-0"></span>**3. Performance Analysis**

This section examines how the camera imaging mechanism affects OC-ISAC performance. Communication seeks to recover source fluctuations from pixel values to estimate the carrier and symbols, while sensing aims to recover voxel reflectance to infer the environment. However, pixel values deviate from incident light levels depending on imaging settings, which inevitably complicates parameter estimation. Thus, analyzing imaging parameters—especially exposure time—is essential for understanding and optimizing OC-ISAC systems.

#### *3.1. Exposure Effect*

From Equations [\(8\)](#page-7-2) and [\(9\)](#page-7-3), it can be observed that, in addition to amplitude attenuation caused by propagation distance and photoelectric conversion, the camera exposure effect also changes the signal structure. Specifically, when the incident light intensity varies as a cosine function, the induced voltage of a pixel retains a cosine with the same frequency, but subject to a frequency-dependent amplitude attenuation (e.g., *E<sup>c</sup>* and *Ee*) and additional phase shift (e.g., *D<sup>c</sup>* and *De*). Such a transmission characteristic reflects the low-pass filtering behavior of the pixel-level photoelectric conversion process. Given the exposure time *T<sup>e</sup>* , the corresponding frequency response is as follows:

<span id="page-7-4"></span>
$$H(f, T_e) = e^{-j\pi f T_e} \frac{\sin(\pi f T_e)}{\pi f},$$
(10)

for *f* ≥ 0, *T<sup>e</sup>* > 0. As a result, high-frequency components of the modulated signal are attenuated, and the captured image intensity can be expressed as a convolution of the incident signal with a rectangular window of width *T<sup>e</sup>* . This temporal integration leads to waveform distortion, where the edges of square-wave modulation or high-speed flicker Sensors **2025**, 25, 7061 9 of 20

signals become smoothed, manifesting as amplitude compression and phase delay in the sampled optical signal. Therefore, the choice of  $T_e$  directly determines the extent of this distortion and the achievable communication bandwidth in the OC-ISAC system.

Figure 5 illustrates the amplitude–frequency characteristics of the induced voltage  $v_k(t)$  for a pixel. The communication and sensing signals consist of DC and alternating current (AC) components. The DC components correspond to  $C_c$  and  $C_e$  in Equation (8), originating from the optical bias in the incident light, and carry no information. The AC components comprise two cosine functions with frequency  $f_c$  and amplitude  $E_c$  for communication, and frequency  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and amplitude  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and  $f_xv$  and

<span id="page-8-1"></span>
$$E_c = C_c |H(f_c, T_e)| \tag{11}$$

and

<span id="page-8-2"></span>
$$E_e = C_e |H(f_x v, T_e)|. \tag{12}$$

<span id="page-8-0"></span>![](_page_8_Figure_6.jpeg)

**Figure 5.** Frequency response of the induced voltage in communication and sensing signals, illustrating the low-pass filtering effect of camera exposure with duration  $T_e$ .

#### 3.2. Normalized Gains for Communication and Sensing

The SNR of the received signal is a key performance indicator for communication. As shown in Figure 5, the effective SNR for communication is defined as a ratio of the power spectrum density of the AC component and AWGN:

$$\rho_c = \frac{E_c^2}{N_0}.\tag{13}$$

Given an average received SNR, i.e.,  $\bar{\rho}_c = C_c^2/N_0$ , we have the following:

$$\rho_c = \frac{E_c^2}{C_c^2} \cdot \frac{C_c^2}{N_0} = G_c^2 \bar{\rho}_c \tag{14}$$

Sensors 2025, 25, 7061 10 of 20

where  $G_c = E_c/C_c$  is defined as the modulation gain, quantifying the relative attenuation of the information-bearing AC component with respect to the DC component under the exposure effect. From Equation (11), it follows that

<span id="page-9-1"></span>
$$G_c = |H(f_c, T_e)|.$$
 (15)

In sensing applications, image quality is often assessed using contrast gain, which is defined as the ratio of the maximum range of pixel values to the average pixel value. This metric indicates how visible features are against the background. A higher contrast gain enhances the detectability of important features. Therefore, evaluating the sensing performance in OC-ISAC involves analyzing the average contrast gain across all pixels. As indicated in Figure 5 and Equation (12), the contrast gain is as follows:

<span id="page-9-2"></span>
$$G_e = \frac{E_e}{C_e} = |H(f_x v, T_e)|.$$
 (16)

The analysis shows that the camera's exposure effect significantly impacts communication and sensing performance in OC-ISAC. Using cameras with different exposure times across various frequencies and mobility scenarios yields distinct trade-offs in performance between the two areas. It is noteworthy that, although this paper does not use bit error rate (BER) or mean square error (MSE) as performance indicators for communication and sensing services, respectively, we use the normalized gains to construct evaluation indicators and optimization problems, which have the same effect.

### <span id="page-9-0"></span>4. Optimization of the Camera's Exposure Time

As noted, rapid flickering and transceiver motion cause temporal variations in pixel intensity. However, camera exposure's low-pass filtering limits accurate reconstruction, degrading both communication and sensing performance, especially in high data rate or mobility scenarios, where exposure time limits system bandwidth, reducing reliability and accuracy. In practical applications, communication and sensing may have conflicting exposure time requirements. For example, a short exposure time is needed for high-speed communication, but it reduces image brightness and sensing quality. Extending the exposure to improve brightness blurs the communication signal. Therefore, it is crucial to optimize exposure time based on performance analysis.

#### 4.1. Problem Formulation

In an outdoor V2X communication scenario, the objective of OC-ISAC performance optimization is to determine an appropriate camera exposure time  $T_e$  such that the average performance of both communication and sensing is maximized:

<span id="page-9-3"></span>
$$\widehat{T}_e = \underset{T_e > 0}{\arg\max} \{ Y(T_e) \} = \underset{T_e > 0}{\arg\max} \{ G_c + G_e \}. \tag{17}$$

Although the weights for combining sensing and communication services in the objective function can be adjusted based on specific scenarios; an equal weight strategy is employed here to suit a neutral situation.

By substituting Equations (10), (15) and (16) into Equation (17), the objective function is as follows:

<span id="page-9-4"></span>
$$Y(T_e) = \left| \frac{\sin(\pi f_c T_e)}{\pi f_c} \right| + \left| \frac{\sin(\pi f_x v T_e)}{\pi f_x v} \right|. \tag{18}$$

*Sensors* **2025**, *25*, 7061 11 of 20

As shown in Figure [6,](#page-10-0) changes in *T<sup>e</sup>* the shift of the maxima and zeros of the Sincshaped response, altering the effective amplitudes at *f<sup>c</sup>* and *fxv*. Thus, solving the optimization problem involves finding the optimal main-lobe width 1/*T<sup>e</sup>* that maximizes the sum of the vertical cut-line values at these frequencies.

<span id="page-10-0"></span>![](_page_10_Figure_2.jpeg)

**Figure 6.** Variation trend of the optimization objective function with respect to exposure time.

#### *4.2. Suboptimal Solution*

The optimization problem formulated in Equation [\(17\)](#page-9-3) is analytically intractable. While the globally optimal exposure time can be obtained via numerical search over a discretized grid within a feasible range—requiring *O*(*N*) computational complexity, where *N* denotes the number of candidate points—this approach is impractical for real-time vehicular applications. To address this, we propose a low-complexity suboptimal algorithm with *O*(1) complexity that analytically computes a near-optimal exposure time, effectively balancing communication and sensing performance.

The algorithm is summarized as follows.

- 1. **Input parameters:** Obtain the communication modulation frequency *f<sup>c</sup>* and the sensing frequency *fxv*.
- 2. **Frequency classification:** Determine the higher and lower characteristic frequencies:

$$f_{\max} = \max(f_c, f_x v), \quad f_{\min} = \min(f_c, f_x v). \tag{19}$$

3. **Compute the frequency ratio:** Evaluate the ratio

<span id="page-10-1"></span>
$$\varepsilon = \frac{f_{\text{max}}}{f_{\text{min}}},\tag{20}$$

which reflects the disparity between the communication and sensing frequency components.

4. **Determine the side-lobe index:** Estimate the integer parameter *γ* indicating the number of side lobes between *f<sup>c</sup>* and *fxv* in the Sinc-shaped response:

$$\gamma = \max\left(\left\lfloor \frac{\varepsilon}{2} - 0.5 \right\rfloor, 0\right). \tag{21}$$

*Sensors* **2025**, *25*, 7061 12 of 20

5. **Compute the suboptimal exposure time:** The exposure time that approximately maximizes the joint performance is given by the following:

$$\tilde{T}_e = \frac{\gamma + 0.5}{f_{\text{max}}}. (22)$$

6. **Output:** The obtained *T*˜ *e* represents the suboptimal exposure time balancing communication reliability and sensing accuracy in the OC-ISAC system.

It is noteworthy that when *f<sup>c</sup>* ≈ *fxv* (i.e., *ε* ≈ 1), the algorithm simplifies to the following:

$$\tilde{T}_e = \frac{1}{2f_{\text{max}}},\tag{23}$$

corresponding to the main-lobe alignment condition. The algorithm's computational complexity is *O*(1), making it well-suited for real-time camera control in vehicular scenarios where computational efficiency is often prioritized over achieving a mathematically perfect optimum.

# <span id="page-11-0"></span>**5. Experiment and Results**

An OCC testbed is developed using an electric turntable and an annular grating as the transmitter to validate the impact of camera exposure on flicker detection and motionaware sensing. Additionally, numerical simulations are performed to demonstrate the effectiveness of the proposed exposure time optimization algorithm for OC-ISAC.

#### *5.1. Experiment Setup*

The setup schematic and photograph are shown in Figure [7.](#page-12-0) The transmitter uses an arbitrary waveform generator (AWG) to generate square-wave signals that modulate a 3 W LED light source via a metal-oxide-semiconductor field-effect transistor (MOSFET) driver, emulating communication beacons at different modulation rates (*fc*). The annular grating lampshades with different slot widths, mounted on an electric turntable, are used to simulate different spatial complexities (*fx*). When the turntable rotates at various speeds (*v*), the sensing signals are thus produced. In addition, a rolling-shutter camera with configurable exposure time at the receiver is about 30 cm away from the source to capture video clips. The recorded image frames are extracted and processed in MATLAB 2021a for frequency-domain analysis, yielding normalized gains for both communication and sensing functions.

#### *5.2. Methodology*

The experiments evaluate the signal gain of light-intensity modulations caused by source flicker and environmental motion under camera exposure, using frequency-domain analysis for both communication and sensing. Experimental parameters and the analysis flowchart are summarized in Table [2](#page-12-1) and Figure [8.](#page-13-0)

The grating was kept stationary in the communication scenario while the light source was modulated at different frequencies. Conversely, a constant light source was used for the sensing scenario, and the grating was rotated at a constant angular speed, resulting in a linear speed of *v* = *πDrNr*/60.

As shown in Figure [8,](#page-13-0) the experiment utilizes the aforementioned setup under two initial conditions—(i) a flickering light source with a stationary grating, and (ii) an always-ON light source with a rotating grating—to evaluate the performance metrics of communication and sensing tasks, denoted as *G<sup>c</sup>* and *G<sup>e</sup>* , respectively, through the following steps.

*Sensors* **2025**, *25*, 7061 13 of 20

<span id="page-12-0"></span>![](_page_12_Picture_1.jpeg)

![](_page_12_Picture_2.jpeg)

**Figure 7.** Schematic of the experimental setup. The signal generated by an arbitrary waveform generator (AWG) modulates the light intensity emitted by an LED light source placed inside an annular grating lampshade, through a MOSFET driver. The light passing through the grating is captured by a camera, producing a corresponding image sequence. These images are fed into MATLAB for analysis of the performance metrics of the communication and sensing functions. (**a**) schematic diagram and (**b**) photograph of the prototype.

<span id="page-12-1"></span>**Table 2.** Experimental parameters for the OCC testbed.

| Parameter                    | Unit | Value                        |
|------------------------------|------|------------------------------|
| Image sensor                 | -    | SONY IM291 (Shenzhen, China) |
| Image resolution, W × N      | -    | 1080 × 720                   |
| Frame rate                   | FPS  | 30                           |
| Readout time, Tr             | µs   | 22.2                         |
| Exposure time, Te            | µs   | 622, 1202, 2404, 4981        |
| Camera distance              | m    | 0.3                          |
| Annular grating diameter, Dr | m    | 0.15                         |
| Turntable rotation speed, Nr | rpm  | 223                          |
| Communication frequency, fc  | Hz   | 0, 200, 500, 700             |
| Grating width                | m    | 0.01, 0.005, 0.002           |
| Environmental complexity, fx | m−1  | 100, 200, 500                |

Sensors 2025, 25, 7061 14 of 20

<span id="page-13-0"></span>![](_page_13_Figure_1.jpeg)

Figure 8. Flowchart of the signal processing chain for frequency-domain analysis in the receiver.

- 1. **Input parameters:** Confirm the parameter sets of  $\{v = 0, f_x > 0, f_c > 0\}$  and  $\{v > 0, f_x > 0, f_c = 0\}$  for communication and sensing scenarios, respectively.
- 2. **Pixel vector:** In each scenario, select an arbitrary column of pixels from the output image (in the sensing scenario, choose a column that can be transmitted through the grating) to obtain the pixel value vector,  $\{x(n)\}$  for  $x(n) \in [0, 255]$  and  $n \in [0, N-1]$ .
- 3. **Fast Fourier Transformation (FFT):** Compute an *N*-point FFT of x(n) to obtain its frequency spectrum vector,  $X(k) = \mathcal{F}(x(n))$  for k = 0, 1, ..., N 1.
- 4. **Normalized gains:** Compute the normalized gains by the following:

$$G = \frac{2|X(m)|}{X(0)} \frac{\pi}{4} \tag{24}$$

where *m* is the index of the frequency component in DFT caused by data modulation and mobility, which is determined by the following:

$$m = \begin{cases} \lfloor NT_r f_c \rfloor & \text{, for communication} \\ \lfloor NT_r f_x v \rfloor & \text{, for sensing} \end{cases}$$
 (25)

To simplify the experimental implementation, binary square-wave signals rather than sinusoidal signals were employed to control both temporal light intensity and spatial environmental variations. As a square wave can be represented as a superposition of a fundamental frequency component  $f_1$  and its odd harmonics:

$$squ(t) = \frac{4}{\pi} \sum_{n=1,3,5,\dots} \frac{1}{n} \sin(2\pi n f_1 t), \tag{26}$$

The measurement is normalized by the coefficient of the fundamental frequency component  $(4/\pi)$  when calculating the single-frequency signal gain from the square wave measurements (as shown in Figure 8).

#### 5.3. Normalized Gains for Communication and Sensing

Figure 9 shows the captured images and pixel value distributions for both communication and sensing scenarios. In the communication scenario (Figure 9a), the turntable is stationary, and the light source flickers at  $f_c = 200$  Hz, with videos recorded at three exposure times, i.e., (A)  $T_e = 2401$  µs, (B)  $T_e = 1202$  µs, and (C)  $T_e = 622$  µs. In the sensing scenario (Figure 9b), the light source is constant, and the turntable rotates at 215 RPM (1.75 m/s) with three environmental complexity (or grating widths), i.e., (A)  $f_x = 100$  m<sup>-1</sup>, (B)  $f_x = 200$  m<sup>-1</sup>, and (C)  $f_x = 500$  m<sup>-1</sup>, with videos recorded at a fixed exposure time  $T_e = 1202$  µs.

The periodic pixel value variations in both cases show that the flickering light source and environmental motion cause periodic changes in incident light intensity. This is due to the rolling shutter mechanism, which converts temporal variations into a spatial pattern along pixel columns. The camera's exposure acts as a low-pass filter, affecting both

*Sensors* **2025**, *25*, 7061 15 of 20

communication and sensing performance. Therefore, this effect must be considered to reconstruct the source state and environmental information accurately.

<span id="page-14-0"></span>![](_page_14_Figure_2.jpeg)

**Figure 9.** Acquired pixel values from the captured images in communication (**a**) and sensing (**b**) scenarios. The communication used a *f<sup>c</sup>* = 200 Hz flickering light source with a stationary turntable and the camera's exposure times of (A) 2404 µs, (B) 1202 µs, and (C) 622 µs, while the sensing used a constant light source and a turntable with different grating slots rotating at an equivalent linear speed of *v* = 1.75 m/s with environmental complexities of (A) 100 m−<sup>1</sup> , (B) 200 m−<sup>1</sup> , and (C) 500 m−<sup>1</sup> .

Using the frequency-domain analysis in Figure [8,](#page-13-0) we determined the normalized signal gain from square waves, reflecting the gains of a single-frequency signal after the camera's exposure effect. We recorded approximately one minute of video under each of two experimental configurations—communication and sensing—using a camera with *Sensors* **2025**, *25*, 7061 16 of 20

exposure times of 4981 µs, 2404 µs, 1202 µs, and 622 µs, respectively. For each configuration, we processed approximately 1800 image frames for each exposure time using the method illustrated in Figure [8](#page-13-0) to compute the normalized gains, i.e., *G<sup>c</sup>* and *G<sup>e</sup>* , and reported their average values.

Figure [10](#page-15-0) shows the averaged normalized gains measured in the communication scenario by transmitting square waves with *f<sup>c</sup>* equal to 200 Hz, 500 Hz, and 700 Hz. The results show a decrease in signal gain as frequency increases, consistent with theoretical analysis. It indicates that exposure time is a critical parameter that influences the distortion introduced by the camera in response to incident optical signals. In fact, a longer exposure time results in a lower cutoff frequency of the low-pass filtering effect, which reduces the bandwidth of the OCC channel and consequently limits the effective data transmission rate.

<span id="page-15-0"></span>![](_page_15_Figure_3.jpeg)

**Figure 10.** Normalized channel gain in the communication scenario, with varying data rates (*fc*) and camera exposure times (*Te*).

Figure [11](#page-16-0) shows the averaged normalized gains for the sensing scenario at different exposure times, with gratings simulating environments of spatial complexities 100 m−<sup>1</sup> , 200 m−<sup>1</sup> , and 500 m−<sup>1</sup> , while the turntable rotates at a linear speed of 1.75 m/s. The gain behavior in sensing is analogous to communication, where *fxv* acts as a "sensing frequency". Under a fixed exposure time, faster relative motion between the transceiver and the environment—or sensing in a more complex scene—leads to a reduction in sensing gain (i.e., decreased image contrast), thereby degrading environmental sensing performance. In such cases, appropriately reducing the camera's exposure time effectively increases the bandwidth of the sensing channel, facilitating the recognition of environmental features in dynamic scenes. These results show that the communication and sensing are reciprocal in OC-ISAC, and the camera's exposure effect has a consistent impact on both functions.

#### *5.4. Optimization of Exposure Time*

When communication and sensing coexist, selecting an appropriate camera exposure time is crucial for optimizing both performances. Typically, the communication rate *f<sup>c</sup>* exceeds the environmental variation frequency *fxv* (i.e., *f<sup>c</sup>* > *fxv*). Figure [12](#page-16-1) shows the objective function in Equation [\(18\)](#page-9-4) versus exposure time for *f<sup>c</sup>* = 200 Hz and *fxv* values of 100 Hz, 150 Hz, and 200 Hz. A larger frequency gap (e.g., high-speed communication in a static environment) shifts the optimal exposure time to higher values, making joint Sensors **2025**, 25, 7061 17 of 20

optimization more challenging. Conversely, a smaller frequency gap (e.g., low-speed communication or high-speed communication under mobility) leads to lower optimal exposure times, where the requirements of both tasks become more aligned and easier to satisfy. The comparison between square- and circle-marked curves shows that the proposed suboptimal solution closely approximates the global optimum by numerical search, confirming its feasibility.

<span id="page-16-0"></span>![](_page_16_Figure_2.jpeg)

**Figure 11.** Normalized channel gain in the sensing scenario, with varying environmental complexities  $(f_x)$  and camera exposure times  $(T_e)$ . The motion speed was held constant at v = 1.75 m/s.

<span id="page-16-1"></span>![](_page_16_Figure_4.jpeg)

**Figure 12.** Optimal and suboptimal numerical solutions of the objective function for different exposure times under communication service at  $f_c = 200$  Hz and sensing services at  $f_x v = 100$ , 150, and 200 Hz.

*Sensors* **2025**, *25*, 7061 18 of 20

To evaluate the effectiveness of the proposed suboptimal algorithm, we set *f*min = *fxv* and *f*max = *fc*. Using the sensing frequency *fxv*=100 Hz as a reference, we uniformly sample 1/*ϵ* over the interval (0, 1] at 100 discrete points to determine the communication frequency according to Equation [\(20\)](#page-10-1). For each frequency ratio, the optimal exposure time *T*ˆ *e* is obtained via numerical search within the feasible range (0, 1/ *fxv*], while the suboptimal solution *T*˜ *e* is computed analytically using the proposed algorithm. The corresponding values of the objective function for both solutions are plotted in Figure [13.](#page-17-1) The normalized deviation (defined as the relative loss in objective function value with respect to the optimum) is on average only 5.71% across the 100 frequency ratios, with a minimum near 0 and a maximum of 36.62%. This close agreement validates the efficacy of the suboptimal approach. The performance gap arises because the suboptimal method places the high-frequency communication component at the center of a sidelobe of the Sincshaped frequency response, which is a practical heuristic that, while not always globally optimal, enables closed-form computation and real-time implementation.

<span id="page-17-1"></span>![](_page_17_Figure_2.jpeg)

**Figure 13.** Objective function values achieved with optimal and suboptimal exposure times under different frequency offsets.

# <span id="page-17-0"></span>**6. Conclusions**

This work theoretically demonstrates the feasibility of integrating communication and sensing using visible-light image sensors within a unified OC-ISAC framework. The analysis identifies camera exposure time as a critical parameter governing the trade-off between communication and sensing performance. Specifically, the exposure-induced low-pass filtering effect distorts the captured pixel response relative to the true incident light intensity variations—whether caused by data-modulated source flickering or environmental motion. Consequently, practical implementations of OCC and vision-based sensing must explicitly account for this effect and employ optimized exposure settings to jointly support both functionalities. The proposed suboptimal exposure time optimization algorithm achieves an excellent balance between performance and computational efficiency. By leveraging a closed-form analytical solution, it reduces complexity from *O*(*N*), required by numerical search, to *O*(1), while incurring only a modest average normalized deviation of 5.71%

*Sensors* **2025**, *25*, 7061 19 of 20

relative to the global optimum. This minor performance loss is well justified in practical vehicular scenarios, given the priority of real-time responsiveness and low latency. Building on these findings, future research can pursue several promising directions. (1) Adaptive exposure control for OC-ISAC systems that dynamically adjusts exposure time in response to varying data rate demands and vehicle mobility. (2) Robust multi-ROI detection and tracking, enabling reliable maintenance of multiple OCC links through accurate localization and tracking of multiple light sources under heterogeneous ambient lighting conditions. (3) Multi-node vehicular networks based on OC-ISAC, facilitating cooperative sensing and communication among vehicles and infrastructure to enhance situational awareness, network intelligence, and road safety. This work advances the foundational understanding of optical camera-based integrated sensing and communication, positioning cameras not merely as passive sensors but as active, dual-functional nodes in next-generation intelligent transportation systems.

**Author Contributions:** Conceptualization, methodology, and writing—original draft preparation, K.D.; investigation and validation, W.C.; funding acquisition, M.W. All authors have read and agreed to the published version of the manuscript.

**Funding:** This study was funded by the Innovation Team of Higher Education Institutions in Shaanxi Province (Grant No. 2024RS-CXTD-12) and the Application Technology Research and Development Reserve Project of Beilin District (Grant No. GX2445).

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** Data underlying the results presented in this paper are not publicly available at this time but may be obtained from the authors upon reasonable request.

**Conflicts of Interest:** The authors declare no conflicts of interest.

# **References**

- <span id="page-18-0"></span>1. Mohsan, S.A.H. Optical Camera Communications: Practical Constraints, Applications, Potential Challenges, and Future Directions. *J. Opt. Technol.* **2021**, *88*, 729–741. [\[CrossRef\]](http://doi.org/10.1364/JOT.88.000729)
- <span id="page-18-1"></span>2. Teli, S.R.; Matus, V.; Younus, O.; Eöll˝os-Jarošíková, K.; Li, X.; Hassan, N.B.; Lin, B.; Figueiredo, M.; Alves, L.N.; Vegni, A.M.; et al. Optical Camera Communications: Concept, Marketing, Implementation, Challenges and Applications. *Sci. China Inf. Sci.* **2025**, *68*, 201301. [\[CrossRef\]](http://dx.doi.org/10.1007/s11432-025-4504-3)
- <span id="page-18-2"></span>3. Zhang, P.; Liu, Z.; Hu, X.; Sun, Y.; Deng, X.; Zhu, B.; Yang, Y. Constraints and Recent Solutions of Optical Camera Communication for Practical Applications. *Photonics* **2023**, *10*, 608. [\[CrossRef\]](http://dx.doi.org/10.3390/photonics10060608)
- <span id="page-18-3"></span>4. Hasan, M.K.; Ali, M.O.; Rahman, M.H.; Chowdhury, M.Z.; Jang, Y.M. Optical Camera Communication in Vehicular Applications: A Review. *IEEE Trans. Intell. Transp. Syst.* **2022**, *23*, 6260–6281. [\[CrossRef\]](http://dx.doi.org/10.1109/TITS.2021.3086409)
- <span id="page-18-4"></span>5. Tang, P.; Yin, Y.; Tong, Y.; Liu, S.; Li, L.; Jiang, T.; Wang, Q.; Chen, M. Channel Characterization and Modeling for VLC-IoE Applications in 6G: A Survey. *IEEE Internet Things J.* **2024**, *11*, 34872–34895. [\[CrossRef\]](http://dx.doi.org/10.1109/JIOT.2024.3430326)
- <span id="page-18-5"></span>6. Li, X.; Hassan, N.B.; Burton, A.; Ghassemlooy, Z.; Zvanovec, S.; Perez-Jimenez, R. A Simplified Model for the Rolling Shutter Based Camera in Optical Camera Communications. In Proceedings of the 2019 15th International Conference on Telecommunications (ConTEL), Graz, Austria, 3–5 July 2019; IEEE: Piscataway, NJ, USA, 2019; pp. 1–5.
- <span id="page-18-6"></span>7. Rátosi, M.; Simon, G. Robust VLC Beacon Identification for Indoor Camera-Based Localization Systems. *Sensors* **2020**, *20*, 2522. [\[CrossRef\]](http://dx.doi.org/10.3390/s20092522)
- <span id="page-18-7"></span>8. Luo, P.; Zhang, M.; Ghassemlooy, Z.; Le Minh, H.; Tsai, H.M.; Tang, X.; Han, D. Experimental Demonstration of a 1024-QAM Optical Camera Communication System. *IEEE Photonics Technol. Lett.* **2016**, *28*, 139–142. [\[CrossRef\]](http://dx.doi.org/10.1109/LPT.2015.2487544)
- 9. Shi, J.; He, J.; Jiang, Z.W.; Chang, G.K. Modulation Format Shifting Scheme for Optical Camera Communication. *IEEE Photonics Technol. Lett.* **2020**, *32*, 1167–1170. [\[CrossRef\]](http://dx.doi.org/10.1109/LPT.2020.3012834)
- 10. Lain, J.K.; Yang, Z.D.; Xu, T.W. Experimental DCO-OFDM Optical Camera Communication Systems With a Commercial Smartphone Camera. *IEEE Photonics J.* **2019**, *11*, 7906813. [\[CrossRef\]](http://dx.doi.org/10.1109/JPHOT.2019.2948071)
- <span id="page-18-8"></span>11. Wan, X.; Lin, B.; Ghassemlooy, Z.; Huang, T.; Luo, J.; Ding, Y. Non-Line-of-Sight Optical Camera Communications Based on CPWM and a Convolutional Neural Network. *Appl. Opt.* **2023**, *62*, 7367–7372. [\[CrossRef\]](http://dx.doi.org/10.1364/AO.499844)

*Sensors* **2025**, *25*, 7061 20 of 20

<span id="page-19-0"></span>12. Huang, H.; You, X.; Shi, J.; Chen, J.; Yu, C.; Gao, M.; Shen, G. Dimmable Optical Camera Communications With WDM Using RGB and Infrared LEDs. *IEEE Photonics Technol. Lett.* **2025**, *37*, 253–256. [\[CrossRef\]](http://dx.doi.org/10.1109/LPT.2025.3538487)

- <span id="page-19-1"></span>13. Chow, C.W.; Shiu, R.J.; Liu, Y.C.; Liu, Y.; Yeh, C.H. Non-Flickering 100 m RGB Visible Light Communication Transmission Based on a CMOS Image Sensor. *Opt. Express* **2018**, *26*, 7079–7084. [\[CrossRef\]](http://dx.doi.org/10.1364/OE.26.007079) [\[PubMed\]](http://www.ncbi.nlm.nih.gov/pubmed/29609393)
- <span id="page-19-2"></span>14. Younus, O.I.; Hassan, N.B.; Ghassemlooy, Z.; Haigh, P.A.; Zvanovec, S.; Alves, L.N.; Minh, H.L. Data Rate Enhancement in Optical Camera Communications Using an Artificial Neural Network Equaliser. *IEEE Access* **2020**, *8*, 42656–42665. [\[CrossRef\]](http://dx.doi.org/10.1109/ACCESS.2020.2976537)
- 15. Dong, K.; Ke, X.Z.; Wang, M.J. Equalization of Camera-Based Channel to Mitigate Uncertain Sampling for Optical Camera Communications. *Opt. Express* **2022**, *30*, 47776–47791. [\[CrossRef\]](http://dx.doi.org/10.1364/OE.474140)
- <span id="page-19-3"></span>16. Younus, O.I.; Hassan, N.B.; Ghassemlooy, Z.; Zvanovec, S.; Alves, L.N.; Le-Minh, H. The Utilization of Artificial Neural Network Equalizer in Optical Camera Communications. *Sensors* **2021**, *21*, 2826. [\[CrossRef\]](http://dx.doi.org/10.3390/s21082826)
- <span id="page-19-4"></span>17. Hu, X.; Zhang, P.P.; Sun, Y.M.; Deng, X.; Yang, Y.B.; Chen, L.Y. High-Speed Extraction of Regions of Interest in Optical Camera Communication Enabled by Grid Virtual Division. *Sensors* **2022**, *22*, 8375. [\[CrossRef\]](http://dx.doi.org/10.3390/s22218375)
- <span id="page-19-5"></span>18. Nguyen, T.; Islam, A.; Jang, Y.M. Region-of-Interest Signaling Vehicular System Using Optical Camera Communications. *IEEE Photonics J.* **2017**, *9*, 7900720. [\[CrossRef\]](http://dx.doi.org/10.1109/JPHOT.2016.2644960)
- <span id="page-19-6"></span>19. Dong, K.; Kong, M.; Wang, M. Error Performance Analysis for OOK Modulated Optical Camera Communication Systems. *Opt. Commun.* **2025**, *574*, 131121. [\[CrossRef\]](http://dx.doi.org/10.1016/j.optcom.2024.131121)
- <span id="page-19-7"></span>20. Ashok, A.; Jain, S.; Gruteser, M.; Mandayam, N.; Yuan, W.; Dana, K. Capacity of Screen–Camera Communications under Perspective Distortions. *Pervasive Mob. Comput.* **2015**, *16*, 239–250. [\[CrossRef\]](http://dx.doi.org/10.1016/j.pmcj.2014.11.003)
- <span id="page-19-8"></span>21. Dong, K.; Kong, M.; Su, W.; Ma, S.; Wang, M. Generalized Modulation for Distance-Aware Optical Camera Communication beyond Oversampled and Undersampled Schemes. *Opt. Express* **2024**, *32*, 16319–16332. [\[CrossRef\]](http://dx.doi.org/10.1364/OE.519705)
- <span id="page-19-9"></span>22. *802.15.7a-2024*; IEEE Standard for Local and Metropolitan Area Networks—Part 15.7: Short-Range Optical Wireless Communications Amendment 1: Higher Rate, Longer Range Optical Camera Communication (OCC); Amendment to IEEE Std 802.15.7-2018. IEEE: Piscataway, NJ, USA, 2025; pp. 1–52.
- <span id="page-19-10"></span>23. Guo, M.; Zhang, P.; Sun, Y.; Zhang, W.; Zhou, Y.; Yang, Y. Object Recognition in Optical Camera Communication Enabled by Image Restoration. *Opt. Express* **2022**, *30*, 37026–37037. [\[CrossRef\]](http://dx.doi.org/10.1364/OE.467659)
- <span id="page-19-11"></span>24. He, J.; Zhou, B. Vehicle Positioning Scheme Based on Visible Light Communication Using a CMOS Camera. *Opt. Express* **2021**, *29*, 27278–27290. [\[CrossRef\]](http://dx.doi.org/10.1364/OE.433485)
- <span id="page-19-12"></span>25. Ifthekhar, M.S.; Le, N.T.; Hossain, M.A.; Nguyen, T.; Jang, Y.M. Neural Network-Based Indoor Positioning Using Virtual Projective Invariants. *Wirel. Pers. Commun.* **2016**, *86*, 1813–1828. [\[CrossRef\]](http://dx.doi.org/10.1007/s11277-016-3177-0)
- <span id="page-19-13"></span>26. Cheng, X.; Duan, D.; Gao, S.; Yang, L. Integrated Sensing and Communications (ISAC) for Vehicular Communication Networks (VCN). *IEEE Internet Things J.* **2022**, *9*, 23441–23451. [\[CrossRef\]](http://dx.doi.org/10.1109/JIOT.2022.3191386)
- 27. Du, Z.; Liu, F.; Li, Y.X.; Yuan, W.J.; Cui, Y.H.; Zhang, Z.H.; Masouros, C.; Ai, B. Toward ISAC-Empowered Vehicular Networks: Framework, Advances, and Opportunities. *IEEE Wirel. Commun.* **2025**, *32*, 222–229. [\[CrossRef\]](http://dx.doi.org/10.1109/MWC.002.2300496)
- <span id="page-19-14"></span>28. Zhang, Y.W.; Li, S.B.; Li, D.Y.; Zhu, J.Z.; Guan, Q.S. Transformer-Based Predictive Beamforming for Integrated Sensing and Communication in Vehicular Networks. *IEEE Internet Things J.* **2024**, *11*, 20690–20705. [\[CrossRef\]](http://dx.doi.org/10.1109/JIOT.2024.3372060)
- <span id="page-19-15"></span>29. Song, Y.; Mo, R.; Zhang, P.; Wang, C.; Sheng, Z.; Sun, Y.; Yang, Y. VehicleTalk: Lightweight V2V Network Enabled by Optical Wireless Communication and Sensing. In Proceedings of the 2024 IEEE 99th Vehicular Technology Conference (VTC2024-Spring), Singapore, 24–27 June 2024; pp. 1–5.
- 30. Gong, C.; Pan, Y.; Xu, Z. Unified ultraviolet communication and sensing: Modeling and system optimization. *J. Commun.* **2023**, *44*, 1–11.
- 31. Zhang, P.; Wu, J.; Wei, Z.; Sun, Y.; Deng, R.; Yang, Y. Channel Modeling for NLoS Visible Light Networks with Integrated Sensing and Communication. *Opt. Lett.* **2024**, *49*, 2861–2864. [\[CrossRef\]](http://dx.doi.org/10.1364/OL.520129)
- 32. Wen, Y.; Yang, F.; Song, J.; Han, Z. Optical Integrated Sensing and Communication: Architectures, Potentials and Challenges. *IEEE Internet Things Mag.* **2024**, *7*, 68–74. [\[CrossRef\]](http://dx.doi.org/10.1109/IOTM.001.2300196)
- 33. An, N.; Yang, F.; Cheng, L.; Song, J.; Han, Z. Free Space Optical Communications for Intelligent Transportation Systems: Potentials and Challenges. *IEEE Veh. Technol. Mag.* **2023**, *18*, 80–90. [\[CrossRef\]](http://dx.doi.org/10.1109/MVT.2023.3244032)
- <span id="page-19-16"></span>34. Liang, C.; Li, J.; Liu, S.; Yang, F.; Dong, Y.; Song, J.; Zhang, X.P.; Ding, W. Integrated Sensing, Lighting and Communication Based on Visible Light Communication: A Review. *Digit. Signal Process.* **2024**, *145*, 104340. [\[CrossRef\]](http://dx.doi.org/10.1016/j.dsp.2023.104340)

**Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.