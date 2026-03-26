Scenario 3
Scenario title: Two-Phase Indoor LED O-ISAC With Distributed O-APs
Scenario vector `s3`: indoor room geometry `W x L x H`, ceiling O-AP circular placement, multi-device PD-array receivers, and two-phase directionless-to-directional operation [O_ISAC_108].
Sensing task + sensing metric: device position estimation from reflected optical observations; sensing metric is coordinate `MSE_P`, with reported sensing MSE below `10^-4` at the evaluated operating point [O_ISAC_108].
Communication task + comm metric: OFDM-based optical service with MRC reception; communication metric is BER, including reported gains of `2.70 dB` (directionless) and `63.35 dB` (directional) against the separate baseline [O_ISAC_108].
Dominant component label + evidence justification: Conventional; implementation evidence shows LED O-APs, pinhole cameras, PD arrays, and collimating lenses, without explicit OPA or ORIS hardware [O_ISAC_108].
Representative works: [O_ISAC_108].

Scenario 4
Scenario title: Indoor Multi-User VLC-CDMA Using Optical Complementary Codes
Scenario vector `s4`: indoor `5 m x 5 m x 3 m` room, ceiling LED array with four wavelengths, desktop receivers at `0.85 m`, and LOS plus reflected optical paths [O_ISAC_388].
Sensing task + sensing metric: none explicitly reported for sensing-plane performance; the reported evaluation focus is indoor communication behavior in multi-user access [O_ISAC_388].
Communication task + comm metric: OCC-based VLC-CDMA multi-user transmission; communication metric is BER versus SNR, user count, and data rate, with degradation as user count increases [O_ISAC_388].
Dominant component label + evidence justification: Conventional; the architecture uses LED arrays, optical filters, PD receivers, and OCC/OOC code structures, without explicit OPA or ORIS mention [O_ISAC_388].
Representative works: [O_ISAC_388].

Key takeaways for this vertical
- Indoor deployment evidence spans localization-oriented LED O-ISAC operation and indoor multi-user VLC-CDMA access under room-constrained channel assumptions [O_ISAC_108] [O_ISAC_388].
- Sensing-plane evidence is explicit in Scenario 3 via coordinate MSE, while Scenario 4 does not report a sensing-plane metric [O_ISAC_108] [O_ISAC_388].
- Communication-plane evidence in both scenarios is BER-based; outcomes vary with directional operation, user count, SNR, and multipath conditions [O_ISAC_108] [O_ISAC_388].
- Dominant implementations in both scenarios remain Conventional LED/PD/filter/camera stacks rather than explicitly OPA- or ORIS-driven architectures [O_ISAC_108] [O_ISAC_388].
