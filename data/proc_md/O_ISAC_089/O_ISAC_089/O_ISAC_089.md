

{0}------------------------------------------------

# Free Space Optical Communication for Inter-Satellite Link: Architecture, Potentials and Trends

Guanhua Wang, Fang Yang, Jian Song, and Zhu Han

The authors illustrate the advantages of using the laser for ISLs due to its longer communication distance, higher data speed, and stronger security.

# Abstract

The sixth-generation network is expected to achieve global coverage based on the space-airground integrated network, and the latest satellite network will play an important role in it. The introduction of inter-satellite links (ISLs) can significantly improve the throughput of the satellite network, and has recently received a lot of attention from both academia and industry. In this article, we illustrate the advantages of using the laser for ISLs due to its longer communication distance, higher data speed, and stronger security. Specifically, space-borne laser terminals — with the acquisition, pointing, and tracking mechanism, which realizes long-distance communication — are illustrated. Advanced modulation and multiplexing modes that make high communication rates possible are introduced. The security of ISLs ensured by the characteristics of both laser and the optical channel is also analyzed. Moreover, some open issues, such as advanced optical beam steering, routing and scheduling algorithm, and integrated sensing and communication are discussed to direct future research.

# Introduction

The terrestrial base stations play an important role in the current wireless network, however, limited by the economic benefits and transmission distance, it is difficult to achieve coverage of remote areas, ocean, and sky. Nevertheless, satellite communication can achieve global coverage because of the high altitude. The throughput of traditional satellite systems, such as Iridium and Globalstar, cannot compare with terrestrial communication because of their high cost, limited number, and scarce spectrum. With the development of space technology, satellite communication systems in recent years such as Starlink, Telesat, and OneWeb utilize plenty of low Earth orbit (LEO) satellites with restricted size, weight, and power (SWaP). Small satellites are easy to be substituted and multiple satellites can be launched within one rocket, which makes a large-scale constellation with thousands of satellites possible. Therefore, a constellation with a large number of satellites makes the system more robust and provides higher throughput up to Tb/s. Moreover, the throughput of Telesat with inter-satellite links (ISLs) can approach that of OneWeb with fewer than half as many satellites because the ISLs enable direct information transfer between satellites without ground stations [1], which implies that the ISLs can improve the performance of the system significantly.

Different bands can be selected for ISLs, as shown in Fig. 1. The millimeter-wave (mmWave) is well-researched and has been utilized in 5G. However, its bandwidth is insufficient for future satellite communication. Meanwhile, the beam width is positively correlated with the wavelength, and so the mmWave beam is wide, which limits the communication distance and rate. The Terahertz has huge bandwidth, which makes communication up to Tb/s possible, and in addition, the beam width is appropriate for inter-satellite communication, theoretically allowing data transmission at Gb/s rates over a distance of more than 1,000 km. However, the energy efficiency of current Terahertz devices still needs to be improved for satellites with limited SWaP. The optical band provides plenty of unlicensed spectrum. The intensity modulation direct detection (IM-DD) that is widely applied in the optical band, does not utilize the frequency and phase of the carrier to carry information, and thus the impact of the Doppler shift is small. However, the coherent modulation still requires additional processing to counteract the Doppler shift. Light-emitting diodes (LEDs) have wide applications in visible light communication with high efficiency. Nonetheless, LEDs emit diffuse and incoherent beams, and have long response times, making them inadequate for ISLs. On the contrary, lasers have good monochromaticity, high energy concentration, and strong directivity, while the response time is also short, allowing wide-band modulation. Therefore, existing terminals can transmit data over thousands of kilometers at 10 Gb/s. Solid-state lasers have high output power and high beam quality, but the disadvantages are low energy efficiency and high heat generation. Laser diodes are power efficient and easy to be integrated on a chip, but the output beam quality is not sufficiently good and needs to be collimated through an optical system. In addition, a new type of laser diode called vertical-cavity surface-emitting laser can improve the beam quality. These transmission approaches are compared in Table 1.

*Guanhua Wang, Fang Yang (corresponding author), and Jian Song are with Tsinghua University, P. R. China;*  Digital Object Identifier: 10.1109/MCOM.002.2300024 *Zhu Han is with the University of Houston, USA, and also with Kyung Hee University, South Korea.*

{1}------------------------------------------------

![](_page_1_Picture_0.jpeg)

FIGURE 1. The architecture of satellite network with different types of ISLs.

| Emission source type   | mmWave             | Terahertz      | LED              | Solid-state Laser | Laser Diode |
|------------------------|--------------------|----------------|------------------|-------------------|-------------|
| Spectrum               | 30 GHz-300 GHz     | 300 GHz-30 THz | 200 THz-1200 THz |                   |             |
| Wavelength             | 1 mm-10 mm         | 10 mm-1 mm     | 250 nm-1550 nm   |                   |             |
| Bandwidth              | ~ GHz              | ~ THz          | ~ 100 THz        | ~ 100 THz         | ~ 100 THz   |
| Beam Width             | wide               | narrow         | wide             | very narrow       | ordinary    |
| Efficency              | high               | low            | high             | medium            | high        |
| Device Size            | medium             | medium         | small            | small             | small       |
| Modulation Rate        | < Gb/s             | Gb/s           | ~ Gb/s           | ~ 10 Gb/s         | ~ 10 Gb/s   |
| Communication Distance | 100 km@368<br>Mb/s | 1200 km@1 Gb/s | \                | 4000 km@10 Gb/s   |             |
| Doppler shift          | not resistant      | not resistant  | resistant        | resistant         | resistant   |

**TABLE 1.** Comparison among different signal sources.

At present, laser ISLs have attracted attention and started to be applied in many systems. Starlink is testing the laser ISLs to bypass the ground stations according to its official website. Meanwhile, each satellite has four laser ISLs to connect the neighboring satellites in the same orbit plane (OP) and adjacent OPs [2]. Moreover, the European Data Relay System (EDRS) adopts geostationary orbit (GEO) satellites as relays to forward data from LEO satellites through laser LEO-GEO ISLs [3]. Furthermore, the under-construction Secure and Laser Communication Technology program and the High Throughput Optical Network [4], which utilize laser ISLs, aim to verify quantum communication and achieve "All-Optical Networks" over Tb/s. However, some aspects remain to be investigated. The high speed of satellites requires accurate pointing and swift tracking of space-borne transceiver terminals. Meanwhile, the range of laser ISLs is up to thousands of kilometers, and thus laser modulation and multiplexing schemes are vital. Furthermore, ensuring the security of ISLs by the characteristics of the laser and the space channels is also worth discussing.

The contributions of this article are summarized as follows. First, a typical architecture for satellites with ISLs is summarized, and the roles and interrelations of each level are analyzed. Then, the merits of laser ISLs are analyzed in three aspects compared with other bands: extending the communication distance, enhancing the communication rate, and ensuring the communication security. Finally, the future trends and some open issues are discussed, with respect to the latest device technology, machine learning in the scheduling algorithm, and multi-function integration, while some preliminary ideas on these issues are presented.

#### SATELLITE NETWORK SYSTEM ARCHITECTURE

The structure of the satellite network is shown in Fig. 1. The model is divided into three layers from top to bottom according to altitude: the GEO/medium Earth orbit (MEO) layer, the LEO layer where the satellites communicate with each other by ISLs, and the Earth layer.

The satellites in the LEO layer are connected by ISLs in a mesh and realize the network access by receiving and transmitting the signal sent from the Earth layer. The LEO satellites serve as a relay for transmitting communication information, whose propagation paths are shorter than satellites in higher OPs because of their low altitudes. Moreover, electromagnetic waves travel faster in space than in fibers, which indicates that although the signal transmitted over ISLs travels longer distances, its delay is still comparable to that of the terrestrial network, and it is significant for the delay-sensitive businesses. Due to the demand for communication rate and the limited SWaP of LEO satellites, laser ISLs are expected to be applied.

The GEO/MEO layer realizes the collection of state information of the LEO satellites, generates instructions, and sends them back to the LEO layer, while messages with high delay tolerance can also be delivered by this layer as well. High altitude allows for wider coverage of satellites. For instance, only three GEO satellites are needed to cover all the LEO satellites in Starlink. A GEO/MEO satellite can send commands to a large number of LEO satellites at the same time, and the delay requirement of the controlling information is not high because the link status of the whole constellation is updated every dozens of seconds.

The satellites in the LEO layer are connected by ISLs in a mesh and realize the network access by receiving and transmitting the signal sent from the Earth layer.

The LEO satellites serve as a relay for transmitting communication information, whose propagation paths are shorter than satellites in higher OPs because of their low altitudes.

{2}------------------------------------------------

![](_page_2_Figure_0.jpeg)

FIGURE 2. The three advantages of laser ISLs: extending the communication distance, enhancing the communication rate, and ensuring the communication security.

![](_page_2_Figure_2.jpeg)

FIGURE 3. Schematic diagram of space-borne laser terminal

Therefore, the GEO/MEO satellites are appropriate to collect the status of LEO satellites and send control commands for routing and resource scheduling. Meanwhile, GEO/MEO satellites are suitable as a relay for delivering information without high requirements for the delay as shown in Fig. 1, which are also adopted in the EDRS.

The Earth layer provides services for users while interacting with the GEO/MEO layer. The ground user sends the data to the LEO satellite corresponding to its coverage area and then transmits the data to the target user via the LEO layer. A large-scale LEO constellation covers the Earth, making it easier to communicate in remote areas, oceans, air, and even polar regions. In addi-

tion, when the computing resources are limited, the ground computing centers can receive the status of LEO satellites from the GEO/MEO layer to calculate routing and resource allocation and then send them back to the GEO/MEO satellites. Meanwhile, the satellites in GEO/MEO layer are controlled by the ground stations.

#### EXTENDING THE COMMUNICATION DISTANCE

Based on the aforementioned characteristics of laser signal sources, the merits of laser ISL can be summarized in three points: extending the communication distance, enhancing the communication rate, and ensuring the communication security. As shown in Fig. 2, the following will elaborate on these advantages respectively.

Because of its high energy concentration and small beam divergence, the laser can meet the link budget of long-distance propagation with lower power than other bands, however, this puts higher requirements on the acquisition, pointing and tracking (APT) system of the laser terminals.

#### ACQUISITION, POINTING, AND TRACKING

The primary function of the APT mechanism is to establish a precise beam alignment between the transmitter and receiver ends to maintain link connectivity during communication. Due to the large relative motion range between satellites and their mechanical vibration, the system requires a coarse pointing assembly (CPA) with a broad detection range, typically realized through a highspeed gimbal or telescope, as well as a fine pointing assembly (FPA), which utilizes a fast steering mirror (FSM) driven by piezoelectric or electromagnetic actuators, for high precision and fast response to maintain link stability. Additionally, an inertial measurement unit (IMU), generally a gyroscope, is utilized to measure satellite vibration, while a quadrant detector or focal plane array is employed to detect light intensity distribution and assess the incident beam.

Initially, the two satellites orient themselves by the ephemeris and use beacon light with a broad beam to scan the designated area, utilizing the CPA to align the angle of view. Upon beam 

{3}------------------------------------------------

detection, the terminals determine the transmitting direction of the receiving beam via sensors and send a confi rmation signal in reverse to realize coarse pointing. Once bi-directional confi rmation is completed, the terminal performs real-time fine-tuning with the FPA based on the feedback information from the sensors and IMU and switches to a narrow beam for high-rate communication. Due to the high relative velocity between LEO satellites, a point-ahead assembly (PAA), which functions similarly to the FPA, is also used to eliminate the impact of relative motion according to the position information inferred from sensors.

## spAce-borne lAser trAnsceIver termInAl

The block diagram of a typical space-borne laser terminal is shown in Fig. 3. A terminal can be divided into an optical module and an electronic module. The optical module mainly realizes transmitter-receiver isolation and APT mechanism. Different wavelengths are used to receive and transmit signals, and are isolated by a dichroic mirror. The received signal is divided into two branches by the beam splitter after the FPA. One is the communication branch, which is converted into an electrical signal by the PD and processed by the communication module, while the other enters a quadrant sensor to calculate the pointing error. Likewise, the transmitted signal is divided into two branches after PAA, one for transmitting and the other for measuring deviation. The electronic system is comprised of control, compute, and communication modules. The compute module collects the information of each sensor and IMU for calculation and transmits the results to other modules. The communication module processes the electrical signal and determines the switch between the beacon light and communication light based on the compute module, and the control module drives the FSM and controls the gimbal by a motor. A terminal called CONDOR designed in [5] adopts similar architecture, communicating at a rate of 5 Gb/s with more than 7,000 km distance, in which a steering range of –175 ∼ +175 deg in azimuth and –25 ∼ +5 deg in elevation is achieved. Without calibration, the terminal requires 30 seconds to establish an ISL, which can be reduced to 2 seconds if the position information of the two satellites is known. The CLICK terminal [6] designed for the smaller CubeSats has given up the gimbal architecture and adopts the aircraft attitude pointing to achieve CPA, and so its size is even smaller. It can be used to connect back and forth satellites in the same OP due to the low relative velocity.

# enhAncIngthe communIcAtIon rAte

Optical ISLs can communicate at a rate of Gb/s over thousands of kilometers, which not only benefi ts from the large bandwidth of the optical band but also profits from the advanced modulation and multiplexing methods.

## modulAtIon schemes

Due to the high frequency of the optical band, it is diffi cult to obtain the local oscillator for coherent detection which has better performance. Adopting the signal intensity to carry information is widely used in optical communication sys-

![](_page_3_Figure_7.jpeg)

FIGURE 4. Maximum bit rate under diff erent communication distances with various modulation schemes based on the link parameters given in [5].

tems. On-off keying (OOK) modulation decides whether to send a pulse within a symbol based on the information bit. The capacity of the direct detection photon channel is investigated in [7], and it is pointed out that there is a positive correlation between the channel capacity and the symbol peak-to-average power ratio (PAPR). Therefore, pulse position modulation (PPM) with higher PAPR is more effi cient than OOK. Meanwhile, PPM also has some derivative types such as differential PPM (DPPM) to further improve its efficiency. Besides, the sub-carrier intensity modulation (SIM) utilizes the phase information by modulating the signal on the intermediate frequency signal and then using the intermediate frequency signal to modulate the intensity of the light source.

The IM-DD is widely used in space-borne laser communication due to its ease of implementation [5, 6]. Figure 4 shows the relationship between the maximum transmission rate and the communication distance for the aforementioned OOK, PPM, and SIM BPSK modulation under the link conditions calculated by the data given in [5], in which the path propagation attenuation, transceiver gain, and energy loss caused by APT error are considered. The scheme with a low communication rate has advantages in computational complexity and other aspects, such as OOK has simpler modulation and demodulation and occupies less bandwidth than PPM at the same rate.

In recent years, with the development of optical phase-locked loops and other devices, optical coherent modulation has been fully studied and demonstrated. Moreover, the CCSDS 141.10-O-1 specifi cation suggests a combination of phase and intensity modulation. Optical communication based on coherent modulation has a lower receiving sensitivity requirement, can better suppress background light noise, and has higher spectrum effi ciency, which is adopted by the EDRS. Moreover, re-using the coherent transceiver from fi ber optics to realize the coherent modulation in free space was adopted in TeraByte InfraRed Delivery program. Furthermore, taking advantage of the fact that the polarization direction of electromagnetic waves has two degrees of freedom, the information can be carried by the modulation of the polarization direction, which is called polarization shift keying.

{4}------------------------------------------------

![](_page_4_Figure_0.jpeg)

FIGURE 5. Future trends and open issues for optical ISLs.

#### MULTIPLEXING SCHEMES

Optical communication can also achieve time division multiplexing (TDM), code division multiplexing (CDM), and frequency division multiplexing (FDM). Moreover, similar to polarization modulation, polarization multiplexing can also be achieved by using two orthogonal polarization directions. Since the TDM, CDM, and polarization multiplexing are straightforward, they will not be repeated here.

Limited by the modulation rate and complexity of the emitters, a single optical signal cannot fully utilize the rich spectrum resources of the optical band. The source with different bands should be used as the central frequency for modulation and they can be distinguished by the wavelength at the receiver. This multiplexing method is called wavelength division multiplexing, a type of FDM. Although there are unutilized frequency bands between different wavelengths, which sacrifices part of the spectral efficiency, wavelength division multiplexing can take advantage of the large bandwidth of the laser link. Moreover, with the development of optical devices, dense wavelength division multiplexing reduces the interval between different wavelengths to less than 1 nm, which can further improve the utilization rate of the spectrum.

Mode division multiplexing can be realized according to the characteristic that the different orbital angular momentum (OAM) modes of photons are orthogonal. The OAM of photons, whose macro representation is a vortex beam, has infinite orthogonal states in theory, which can greatly increase the total channel capacity. In recent years, significant progress has been made in the generation and separation of vortex light by Dammann grating. With the combination of wavelength division multiplexing and OAM mode multiplexing, the spectral efficiency of more than 20 bit/s/Hz and the transmission capacity of 100 Tb/s have been achieved [8].

#### Ensuring the Communication Security

#### HIGH DIRECTIVITY AND NARROW BEAM

The optical band has a shorter wavelength, and so the beam width can be narrower than other bands with the same aperture of antennas. At the same time, the Gauss beam can be collimated by the beam expander to obtain a smaller divergence. The beam divergence angle of existing space-borne laser terminals is dozens of microradians. In the CONDOR system, which aims to achieve communication over thousands of kilometers, the beam divergence is 17.44 mrad. It means that more than 80 percent of the energy is concentrated in the circular region with a radius of 90 m centered on the aiming center after the laser beam propagates 5,000 km, which makes it difficult to eavesdrop.

Meanwhile, for the receiver, the received intensity decays exponentially with the square of the ratio between the APT deviation and beam width, which means a small alignment error will cause a great attenuation of the received energy. It implies that when both sides complete the APT mechanism and establish a stable communication link, it requires a large amount of energy to interfere with the communication since the interference signal is difficult to coaxial with the transmitter and the receiver. Therefore, the laser beam has an effective resistance to interference.

#### ANISOTROPY OF THE OPTICAL CHANNEL

The optical channel for ISLs is mainly affected by background light and various cosmic rays. Meanwhile, very low Earth orbit satellites operate in the upper ionosphere, and free particles in the ionosphere will also affect the transmission of electromagnetic waves. Because of the directivity of background noise and the overall motion trend of ionospheric particles, there is anisotropy in the optical ISLs of LEO. If the receivers are in different orientations, the channel state information will also change. Using the difference of channel state information between the legitimate receiver and eavesdropper, the signal quality of the eavesdropper should be reduced without affecting the receiver by reasonable precoding and constellation design, to ensure communication security. For instance, when the channel has anisotropy to the direction of polarization modulation, by modulation and coding based on the channel response, the polarization direction of the signal keeps unchanged in the desired direction while distorted in the undesirable direction, and eavesdropping can be prevented.

{5}------------------------------------------------

## Quantum SecureCommunication

Quantum communication is theoretically secure, which is different from traditional encryption methods that are computationally secure. For photons, the quantum properties are particularly significant in the polarization state. Meanwhile, the laser is generated by stimulated radiation, and its polarization direction is the same as that of the optical pump, and so it is convenient to prepare photons with a specified polarization state. The quantum key distribution method has been well studied. The ultimate limits and the practical rates of quantum key distribution via satellites under actual free-space channel conditions are discussed in [9].

In recent years, the theory of quantum secure direct communication using the quantum entanglement effect has been proposed. The sender transmits only one of each pair of entangled photons at a time, and the measurement for a single photon will make the quantum state of the entangled photons pair collapse, and so it can always confirm whether there is an eavesdropper after a single transmission, then the communication security can be ensured. Since the space channel is simpler than the ground channel, quantum secure communication is easier to realize in satellite communication [10].

# Future Trends andOpen Issues

The optical ISLs have great potential in terms of communication distance, data rate, and communication security, but also have much room for improvement in many aspects as shown in Fig. 5.

## Advanced Methods forLaserBeam Steering

In the current space-borne terminals, the gimbal for beam steering occupies a large volume and mass. With the development of optical device manufacturing technology, many beam steering schemes are using optical characteristics, including micro-electro-mechanical system (MEMS), optical phased array (OPA), and liquid crystal schemes [11]. The MEMS utilizes a power splitter to divide the beam into several sub-beams and uses micro-motors to drive different optical units, such as mirrors or gratings, to control the direction of the sub-beams, and thus achieving the overall beam steering. OPA uses phase shifters made of electro-optic or thermo-optic materials to form a two-dimensional array. The incident light of OPA also passes through the power splitter and the phase shifting unit, and then through the transmitting unit. The refractive index of the liquid crystal can be changed by applying a periodic stepped voltage to different parts, forming a structure similar to a blazed grating to change the direction of the beam. These technologies can be integrated into silicon chips and are suitable for satellites with limited SWaP, but there are still some deficiencies. The response time of general liquid crystal materials is tens of milliseconds, and the ferroelectric liquid crystal materials with fast response need a higher voltage drive. The beam steering range of OPA or MEMS is also restricted because of the limited scale. Moreover, these schemes are controlled by circuit switches, and so the steering angles are still not accurate enough for tasks with high precision requirements. Larger arrays and hybrid analog-digital drives may be required in the future to improve accuracy.

## HeterogeneousNetwork Convergence

The satellite communication system cannot meet the communication demands alone, and it should exist as a supplement and enhancement of the existing network. Therefore, it is important to realize the space-air-ground integrated network. Long-distance communication with low delay can be realized by ISLs, and so the heterogeneous network comprised of satellite and terrestrial networks can provide different quality of service for various tasks. Moreover, when one part of the heterogeneous network is heavily loaded or unstable, others can provide backups. Algorithms and standards can be designed to implement handover between terrestrial and satellite networks according to quality of service and service types. At the same time, the communication terminal should also be compatible with a variety of networks. For the connection between the satellite network and other networks, since laser propagation in the atmosphere is severely degraded by rain and fog, the microwave is generally used for satellite-ground communication. The traditional method needs to translate the optical signal into an electrical signal and then modulate it into a microwave. The emerging microwave photonics can directly convert optical signal to microwave signal, which makes it suitable for the connection with heterogeneous networks such as unmanned aerial vehicle (UAV) cluster networks. Furthermore, a space-air-ground architecture was proposed [12] to reduce atmospheric turbulence and increase the usability of optical links.

## RoutingandScheduling Algorithm

Due to the fast movement of low-orbit satellites, the topology structure of the inter-satellite network changes rapidly, which poses a challenge to the communication routing and scheduling algorithm. In recent years, the method to find the optimal policy by machine learning has achieved considerable results in many problems, and it has also been applied to various kinds of resource scheduling algorithms. In a satellite network similar to EDRS, the throughput of the system is optimized by reinforcement learning, and feature functions are designed based on the characteristics of the model to fit the state-action value function [13]. Furthermore, due to the uneven geographical and time distribution of communication demand, it is necessary to sacrifice the delay performance and choose a variety of paths to make the satellite load more balanced. Moreover, the distribution of satellite constellations and ground stations can also be optimized to improve the energy efficiency of communications. Additionally, each satellite in the current Starlink maintains four fixed links with its neighbors, while temporary ISL establishment between non-adjacent satellites can achieve fewer hops and reduce the node delay [2]. Meanwhile, ISLs with low utilization may be deactivated to improve power efficiency. However, the switching of temporary links results in a dynamic routing and an additional setup delay. Therefore, the scheduling of dynamic satellite links is also worth researching.

Quantum communication is theoretically secure, which is different from traditional encryption methods that are computationally secure. For photons, the quantum properties are particularly significant in the polarization state.

{6}------------------------------------------------

Meanwhile, ISLs with low utilization may be deactivated to improve power efficiency. However, the switching of temporary links results in a dynamic routing and an additional setup delay. Therefore, the scheduling of dynamic satellite links is also worth researching.

## LocalizationandNavigation

Because of the large coverage of satellite communication, it is reasonable to combine satellite communication with navigation, measurement, and control services. Moreover, a large number of LEO satellites help reduce the variance of the estimation results. In [14], a navigation method using the Doppler measurements of LEO satellites is proposed, which is different from the traditional way of employing GEO satellites for positioning, making LEO satellites able to communicate and navigate simultaneously. However, for laser transmission, the detection of Doppler shift is complicated, the localization can be achieved by using the timeof-flight of optical signals from different satellites. Furthermore, the localization and navigation have requirements for the precision of location information of the satellites. The approximate location of satellites can be calculated by the orbit parameters, and the precise relative position between satellites can be obtained through the APT mechanism when the ISL is established, and the relative position information between satellites can be used to reduce the error of the satellite position.

## IntegratedSensingandCommunication

Based on the similarity between communication and sensing in device architecture and signal processing, integrated sensing and communication (ISAC) has attracted widespread attention. Because the spaceborne laser terminals can realize accurate beam steering and acquisition, they are suitable for the ISAC. With a space-borne laser terminal, the outgoing beam is adjusted according to the satellite's motion and the beam stability, and the terrain height is measured according to the return wave [15]. In addition, satellite laser remote sensing can also achieve the perception of air pollution, cloud thickness, and other information, which is also helpful to sense the link status to improve the quality of communication. Furthermore, the trade-off between communication rate and sensing accuracy can be achieved by flexible waveform design. The pulse-modulated waveform is suitable for sensing, while for communication, the PAPR of the signal is constrained to reduce the distortion of the received signal, a reasonable design of the modulated waveform should be considered. Besides, the evaluation indicators of ISAC should be adjusted according to the specific task to meet the various demands for communication and sensing.

# Conclusion

An overview of the system architecture of satellite networks has been presented in this article, and different bands for ISL from various perspectives are analyzed. The benefits of laser ISL have been highlighted in extending the communication distance, enhancing the communication rate, and ensuring the communication security. Moreover, some future trends and open issues for laser ISLs have also been explored, such as developing more compact and efficient beam steering devices, designing effective routing and scheduling algorithms for dynamic satellite networks, integrating multiple functions in laser terminals, and achieving seamless convergence with heterogeneous networks. By addressing these challenges and opportunities, laser ISLs can provide the great potential to significantly improve the performance of satellite communication in the near future.

## Acknowledgment

This work was supported by the National Key Research and Development Program of China under Grant 2022YFE0101700.

#### References

- [1] I. del Portillo, B. G. Cameron, and E. F. Crawley, "A Technical Comparison of Three Low Earth Orbit Satellite Constellation Systems to Provide Global Broadband," *Acta Astronautica*, vol. 159, June 2019, pp. 123–35.
- [2] A. U. Chaudhry and H. Yanikomeroglu, "Laser Inter-Satellite Links in a Starlink Constellation: A Classification and Analysis," *IEEE Vehic. Tech. Mag*., vol. 16, no. 2, June 2021, pp. 48–56.
- [3] H. Hauschildt *et al.*, "European Data Relay System Goes Global," *Proc. 2017 IEEE Int'l. Conf. Space Optical Systems and Applications*, Nov. 2017, pp. 15–18.
- [4] C. A. Vasko *et al.*, "Optical High-Speed Data Network in Space — An Update on HydRON's System Concept," *Proc. 2022 IEEE Int'l. Conf. Space Optical Systems and Applications*, Mar. 2022, pp. 7–13.
- [5] S. Müncheberg *et al*., "Development Status and Breadboard Results of a Laser Communication Terminal for Large LEO Constellations," *Proc. Int'l. Conf. Space Optics*, vol. 11180, 2019, pp. 1180–92.
- [6] K. Cahoy *et al*., "The CubeSat Laser Infrared Crosslink Mission (CLICK)," *Proc. Int'l. Conf. Space Optics*, vol. 11180, 2019, pp. 358–69.
- [7] A. Wyner, "Capacity and Error Exponent for the Direct Detection Photon Channel — Part I," *IEEE Trans. Inf. Theory*, vol. 34, no. 6, Nov. 1988, pp. 1449–61.
- [8] H. Huang *et al*., "100 Tbit/s Freespace Data Link Enabled by Three-Dimensional Multiplexing of Orbital Angular Momentum, Polarization, and Wavelength," *Opt. Lett*., vol. 39, no. 2, Jan. 2014, pp. 197–200.
- [9] S. Pirandola, "Satellite Quantum Communications: Fundamental Bounds and Practical Security," *Phys. Rev. Research*, vol. 3, May 2021, p. 023130.
- [10] G. Vallone *et al.*, "Experimental Satellite Quantum Communications," *Phys. Rev. Lett*., vol. 115, no. 4, July 2015, p. 040502.
- [11] Y. Wang *et al*., "2D Broadband Beamsteering With Large-Scale MEMS Optical Phased Array," *Optica*, vol. 6, no. 5, May 2019, pp. 557–62.
- [12] S. R *et al.*, "HAPS-Based Relaying for Integrated Space–Air– Ground Networks With Hybrid FSO/RF Communication: A Performance Analysis," *IEEE Trans. Aerosp. Electron. Syst*., vol. 57, no. 3, June 2021, pp. 1581–99.
- [13] D. Zhou *et al*., "Machine Learning-Based Resource Allocation in Satellite Networks Supporting Internet of Remote Things," *IEEE Trans. Wireless Commun*., vol. 20, no. 10, Oct. 2021, pp. 6606–21.
- [14] B. Mclemore and M. Psiaki, "Navigation Using Doppler Shift From LEO Constellations and INS Data," *IEEE Trans. Aerosp. Electron. Syst*., vol. 58, no. 5, Oct. 2022, pp. 4295–4314.
- [15] J. Xie *et al*., "Design and Data Processing of China's First Spaceborne Laser Altimeter System for Earth Observation: GaoFen-7," *IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens.*, vol. 13, Mar. 2020, pp. 1034–44.

#### Biographies

Guanhua Wang is a Ph.D. student with the Department of Electronic Engineering, Tsinghua University, Beijing, China.

Fang Yang [M'11, SM'13] received his B.S.E. and Ph.D. degrees in electronic engineering from Tsinghua University, Beijing China, in 2005 and 2009, respectively. Currently, he is an Associate Professor with Department of Electronic Engineering, Tsinghua University.

Jian Song [M'06, SM'10, F'16] received the B.Eng. and Ph.D. degrees in electrical engineering from Tsinghua University, Beijing, China, in 1990 and 1995, respectively. Currently, he is the Director of Tsinghua DTV Technology R&D Center. He has published more than 300 peer-reviewed journal and conference papers. He holds two U.S. and more than 80 Chinese patents. He is a Fellow of IET.

Zhu Han [S'01, M'04, SM'09, F'14] received his B.S. degree in electronic engineering from Tsinghua University, Beijing, China, in 1997 and his M.S. and Ph.D. degrees in electrical and computer engineering from the University of Maryland, College Park, in 1999 and 2003, respectively. He is a Professor in the Electrical and Computer Engineering Department and in the Computer Science Department at the University of Houston, Texas.