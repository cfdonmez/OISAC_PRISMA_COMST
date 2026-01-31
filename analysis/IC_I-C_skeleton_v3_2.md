# Section I-C: The Fragmentation Challenge (Writing Skeleton)

*Generated from gold evidence set v3.2*

## C1: Terminology Inconsistency

The O-ISAC field suffers from inconsistent terminology, with terms such as "optical ISAC," "photonic ISAC," "O-ISAC," and "ISAC-OF" used interchangeably across different modality communities.

**Supporting evidence:**
- [O_ISAC_161] ISAC Transceiver Hardware Architectures, Technologies, and T... — "Quebec-Nature et Technologies (FRQNT). (Invited Ar..."
- [O_ISAC_015] Movable Access Point-Aided Integrated Visible Light Communic... — "system model and algorithm is compared with a fixe..."
- [O_ISAC_001] Modulation Strategies for Robust Optical Wireless Communicat... — "(ISAC)* ## I. INTRODUCTION The next generation of ..."
- [O_ISAC_030] ReflexGest: Recognizing Hand Gestures Under VLC-Capable Lamp... — "in this section. We first clarify the limit of thr..."
- [O_ISAC_034] Pulse Sequence Sensing and Pulse Position Modulation for Opt... — "accurate sensing ability of the environment, which..."

## C2: Non-Standardized Metrics

Sensing performance is reported using diverse metrics (RMSE, CRB, FIM, range resolution) with inconsistent definitions, making cross-study comparison challenging.

**Supporting evidence:**
- [O_ISAC_013] Single-Ended > 100-km Distributed Vibration Sensor Based on ... — uses Δr
- [O_ISAC_023] Free-Space Optical Integrated Sensing and Communication Base... — uses RMSE
- [O_ISAC_050] Visible Light Communication-Enabled Simultaneous Position an... — uses Cramér-Rao
- [O_ISAC_005] Integrated Sensing and Communication for UAV Trajectory Opti... — uses SNR
- [O_ISAC_008] Wide-steering Integrated Sensing and Communication OPA-based... — uses SNR

## C3: Sub-Domain Fragmentation

Research in fiber, FSO, VLC, and Photo-THz sensing has evolved largely in isolation, with limited cross-citation and no unified evaluation framework.

**Supporting evidence:**
- [O_ISAC_036] Heterogeneous Integrated III-V-on-SOI Transmitter for 6G FiW... — "# Heterogeneous Integrated III-V-on-SOI Transmitte..."
- [O_ISAC_080] Integrated Communication and In-band Spectrum Polarization-B... — "on, attaining vibration localization error equival..."
- [O_ISAC_082] Signal-Signal Beating Interference: From Destructive to Cons... — "ope detection, the baseband echo signal is process..."
- [O_ISAC_013] Single-Ended > 100-km Distributed Vibration Sensor Based on ... — "* located can be expressed as $$I_{\text{test}}(t)..."
- [O_ISAC_032] Temperature Compensation Method for Polarization-Multiplexed... — "separate the strain and temperature, giving the me..."

## C4: Weak Cross-Domain Technology Transfer

Despite shared physical-layer challenges, technology transfer between O-ISAC sub-domains remains limited due to incompatible hardware paradigms and evaluation methodologies.

**Supporting evidence:**
- [O_ISAC_068] Joint Communication and Sensing Prospects: Potential Through... — Discusses 'interoperability' in VLC
- [O_ISAC_161] ISAC Transceiver Hardware Architectures, Technologies, and T... — Discusses 'interoperability' in Photo-THz
- [O_ISAC_002] Photonic Terahertz Integrated Sensing and Communication (ISA... — Discusses 'lack of' in Photo-THz
- [O_ISAC_009] Integrated Positioning and Communication Relying on Wireless... — Discusses 'fragmented' in VLC, mentions Photo-THz
- [O_ISAC_067] Measurement-based Validation of Ray-tracing Model at sub-THz... — Discusses 'lack of' in Photo-THz

## C5: Missing Unifying Framework

No comprehensive taxonomy, benchmark suite, or unified PHY-layer framework exists to enable systematic comparison across O-ISAC modalities.

**Supporting evidence:**
- [O_ISAC_039] Visible Light Integrated Positioning and Communication: A Mu... — "proposed MTL-based network is evaluated, which is ..."
- [O_ISAC_082] Signal-Signal Beating Interference: From Destructive to Cons... — ""Integrated sensing and communication channel mode..."
- [O_ISAC_161] ISAC Transceiver Hardware Architectures, Technologies, and T... — "scalable, commercially viable solutions requires o..."
- [O_ISAC_327] Channel Characterization and Modeling for VLC-IoE Applicatio... — "to support the evaluation of VLC-IoE systems in 6G..."
- [O_ISAC_001] Modulation Strategies for Robust Optical Wireless Communicat... — "trategies for Robust Optical Wireless Communicatio..."

---

## Minimal Normalization Proposal

To enable cross-modality comparison, we propose:
1. **Ranging accuracy**: Report both RMSE (absolute) and CRB/FIM (theoretical bound) at specified SNR.
2. **Resolution**: Standardize Δr definition as 3-dB bandwidth-based for all modalities.
3. **SNR**: Distinguish electrical vs. optical SNR; report both when applicable.
4. **Benchmark scenarios**: Define indoor/outdoor, static/mobile reference scenarios.
5. **Unified taxonomy**: Adopt consistent O-ISAC terminology across modalities.
