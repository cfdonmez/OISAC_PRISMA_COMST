# O-ISAC Extraction Tracker

Bu dosya, manuel extraction sürecinde işlenen makalelerin takibini sağlar.

**Son Güncelleme:** 2025-12-28

---

## 📊 Extraction Özet Tablosu

| # | Record ID | Başlık (Kısa) | Medium Class | Eligibility Concern | Completeness | Spot Check | Notes |
|---|-----------|---------------|--------------|---------------------|--------------|------------|-------|
| 1 | O_ISAC_001 | CE-OFDM VLC Sensing | `wireless_vlc` | `none` | medium | ✅ Doğrulandı | Sensing metrikleri teorik (NR) |
| 2 | O_ISAC_002 | Photonic THz ISAC | `hybrid` | `hybrid_thz` | high | - | 120 Gbps / 2.5 mm |
| 3 | O_ISAC_003 | V2V VLC Channel | `wireless_vlc` | `simulation_only` | medium | - | Kanal modelleme, Comm NR |
| 4 | O_ISAC_004 | FMF Sensing + Comm | `cabled_fibre` | `fiber_not_wireless` | high | - | 128 Gbps, Fiber-ISAC ✓ |
| 5 | O_ISAC_005 | UAV FSO Backscatter | `hybrid` | `environmental_sensing` | high | - | Atmosfer algılama, Q-Learning |
| 6 | O_ISAC_006 | Fiber-ISAC Survey | `cabled_fibre` | `review_paper` | high | - | Taksonomi referansı |
| 7 | O_ISAC_007 | Fiber Displacement Probe | `cabled_fibre` | ⛔ `sensing_only_no_comm` | high | ⚠️ | **EXCLUDE** - İletişim yok! |
| 8 | O_ISAC_008 | OPA Lidar QPSK-FMCW | `wireless_lidar_like` | `none` | high | - | 4 Gbps + 15m sensing, OPA ✓ |
| 9 | O_ISAC_009 | VLPC-DCO-OFDM | `wireless_vlc` | `none` | high | - | IEEE JSAC, Gbps + cm-level VLP |
| 10 | O_ISAC_010 | PoF + DMT MCF | `cabled_fibre` | ⛔ `pof_not_sensing` | high | ⚠️ | **EXCLUDE** - Güç+İletişim, Algılama yok! |
| 11 | O_ISAC_011 | RO-ISAC 3D Positioning | `wireless_vlc` | `none` | high | - | Retroreflective CCR, 1 cm resolution ✓ |
| 12 | O_ISAC_012 | PC-FMCW LiDAR | `wireless_fso` | `none` | high | - | 1 Gbps + 1.5 cm resolution, squaring decouples ✓ |
| 13 | O_ISAC_013 | OFDR Vibration Sensor | `cabled_fibre` | ⛔ `sensing_only_isac_mentioned` | high | ⚠️ | **EXCLUDE** - ISAC-OF'dan bahsediyor ama sadece sensing yapıyor! |
| 14 | O_ISAC_014 | PoF Power Grid | `cabled_fibre` | ⛔ `pof_not_sensing` | high | ⚠️ | **EXCLUDE** - PoF + Comm, algılama yok! |
| 15 | O_ISAC_015 | MAP-IVLCS | `wireless_vlc` | `none` | high | - | Movable AP, 353% gain, Pareto curve ✓ |
| 16 | O_ISAC_016 | Photonic Sub-THz D-band | `hybrid_photonic_thz` | `none` | high | - | 251 Gbps + 2.5 cm, CRQ=100 Gbps/cm ✓ |
| 17 | O_ISAC_017 | DNN-DBP Fiber-ISAC | `cabled_fibre` | `none` | high | - | 1200 km, ML-enabled, anomaly detection ✓ |
| 18 | O_ISAC_018 | RoF-ISAC LFM | `hybrid_fiber_wireless` | `none` | high | - | φ-OTDR + 28 GHz Ka-band, 28 pε/√Hz ✓ |
| 19 | O_ISAC_019 | Full-Duplex mmW Photonics | `hybrid_fiber_wireless` | `none` | high | - | Carrier reuse PM/IM, 1.5 cm res ✓ |
| 20 | O_ISAC_020 | Submarine Cable ISAC | `cabled_fibre` | `none` | high | - | φ-OTDR, Earthquake Mw 1.1-6.3, 10-mo field test ✓ |
| 21 | O_ISAC_021 | O-ISAC Tutorial | `wireless_fso` | 📚 `review_paper` | high | - | **REVIEW** - Waveform taxonomy, RF vs O-ISAC, future trends |
| 22 | O_ISAC_022 | m-CAP VLC-ISAC | `wireless_vlc` | `none` | high | - | 32 Mbps + 7.17 cm positioning, 9-AP indoor ✓ |
| 23 | O_ISAC_023 | DCO-OFDM FSO-ISAC | `wireless_fso` | `none` | high | - | 905nm LiDAR, 3.38 bps/Hz + 2.85 cm, BCD optimization ✓ |
| 24 | O_ISAC_024 | DSCM Fiber-ISAC | `cabled_fibre` | `none` | high | - | 2×120 Gbps + 1m resolution, LFM pre-comp, 2.4dB SNR↑ ✓ |
| 25 | O_ISAC_025 | OTN for RF-ISAC | `hybrid_fiber_wireless` | ⚠️ `borderline` | medium | yes | **BORDERLINE** - Optical transport for RF sensing, not O-ISAC |
| 26 | O_ISAC_026 | W-band Photonic ISAC | `hybrid_fiber_wireless` | `none` | high | - | 96.5 GHz, FDM (SCM+LFM), 8 Gbps + 2.75 cm, 10km fiber ✓ |
| 27 | O_ISAC_027 | 2µm Salinity Sensor | `cabled_fibre` | ⛔ `exclude_sensing_only` | high | - | **EXCLUDE** - Pure sensing (salinity), no comm data provided |
| 28 | O_ISAC_028 | S-CADD Receiver | `cabled_fibre` | ⛔ `exclude_pure_comm` | high | - | **EXCLUDE** - Pure communication (DCI), "ISAC" only in affiliation |
| 29 | O_ISAC_029 | D-Band Photonic ISAC | `hybrid_fiber_wireless` | `none` | high | - | 134 GHz, TDM (LFM+16QAM), 116 Gbps + 6mm res, 20km fiber ✓ |
| 30 | O_ISAC_030 | ReflexGest VLC-HGR | `free_space_optics` | `none` | high | - | **VLC-ISAC** - Desk lamp HGR + VLC. Multi-carrier (40-70kHz). >90% Acc. (Visual file mismatch ignored) |
| 31 | O_ISAC_031 | Full-Duplex Photonic SIC | `hybrid_fiber_wireless` | `none` | high | - | 100 GHz, LFM-BPSK, 43.7 dB SIC Depth, Sim Only (OptiSystem) ✓ |
| 32 | O_ISAC_032 | FOVSU Temp Compensation | `cabled_fibre` | ⛔ `exclude_sensing_only` | high | - | **EXCLUDE** - Pure sensing (Vibration), no comm data provided |
| 33 | O_ISAC_033 | 1000km DAS + 10Tb/s | `cabled_fibre` | `none` | high | - | **Review/Exp** - 2 Scenarios: Fwd Phase (380km) + FD-CP-DAS (1007km, 10Tb/s). Benchmark paper. ✓ |
| 34 | O_ISAC_034 | FSO PSS-PPM ISAC | `free_space_optics` | `none` | high | - | **FSO-ISAC** - PSS-PPM modulation for simultaneous ranging/comm. Low rate (~3 Mbps), high acc (~1cm). Multi-user sim. ✓ |
| 35 | O_ISAC_035 | OCDM-FMCW FSO ISAC | `free_space_optics` | `none` | high | - | **FSO-ISAC** - OCDM-based waveform. Dedicated subcarrier for FMCW ranging. ~3.2 Gbps + cm-level accuracy. Exp validated. ✓ |
| 36 | O_ISAC_036 | III-V-on-SOI FiWi ISAC | `hybrid_fiber_wireless` | `none` | high | - | **FiWi-ISAC** - Integrated III-V-on-SOI transmitter. FSO (1m) + mmWave. 24 Gbps + 0.03m res. Exp (20m target). ✓ |
| 37 | O_ISAC_037 | LP Mode Demux Hybrid | `cabled_fibre` | ⛔ `exclude_pure_comm` | high | - | **EXCLUDE** - Pure component design (mode demultiplexer) for MDM comms. No sensing/ISAC. |
| 38 | O_ISAC_038 | NOMA DAS-Comm | `cabled_fibre` | `none` | high | - | **NOMA-ISAC** - LFM Sensing tone superimposed on 60 GBaud 16-QAM (NOMA). 10 km Fiber DAS. Negligible penalty. ✓ |
| 39 | O_ISAC_039 | VIPAC MTL-FL Frame | `visible_light` | `none` | high | - | **VLC-ISAC** - Multi-Task Learning (MTL) + Federated Learning (FL) for joint Channel Est & VLP. ~6-10 cm accuracy. Sim. ✓ |
| 40 | O_ISAC_040 | UAV ADT-CCR RO-ISAC | `free_space_optics` | `none` | high | - | **UAV-ISAC** - UAVs with Angle Diversity Transmitters (ADT) + Target CCR (Retroreflective). 3D Positioning + Comms. Sim. ✓ |
| 41 | O_ISAC_041 | Co-Route Fiber ML-ISAC | `cabled_fibre` | `none` | high | - | **Fiber-Sensing** - ML (FEA-TFW + RF/SVM) on OTDR/phi-OTDR data. Co-cable (99.7%) & Vibration (98%) ID. Field Trial. ✓ |
| 42 | O_ISAC_042 | Coherent LFM-DAS ISAC | `cabled_fibre` | `none` | high | - | **Fiber-ISAC** - LFM sensing probes in Comm Frame Header. 60 GBaud 16-QAM + 0.5m resolution DAS. Shared Tx. Exp. ✓ |
| 43 | O_ISAC_043 | W-band FiWi TFDM | `hybrid_fiber_wireless` | `none` | high | - | **FiWi-ISAC** - Photonic W-band generation. Flexible TFDM (LFM+SCM) for adaptive Rate/Resolution. 10km Fiber + 1m Wireless. Exp. ✓ |
| 44 | O_ISAC_044 | W-band FiWi TFDM (Ext) | `hybrid_fiber_wireless` | `none` | high | - | **FiWi-ISAC** - Extended Journal version of O31/O43? 10 Cases of TFDM. Detailed Phase Noise & Delay analysis. 1.59cm Res. Exp. ✓ |
| 45 | O_ISAC_045 | Si3N4 Micro-Ring IOSAC | `cabled_fibre` | `none` | high | - | **Chip-level ISAC** - Si3N4 Micro-Ring Resonator for simultaneous Salinity Sensing (294 nm/RIU) + 1.25 Gbps OOK Comm. 20 km Fiber. Exp. ✓ |
| 46 | O_ISAC_046 | MCF Ultra-Low Freq DAS | `cabled_fibre` | `space_division_multiplexing` | high | - | **MCF-ISAC** - 7-Core Fiber. Ultra-low freq DAS (0.1 Hz) + 241 Tb/s Comm (96x7 WDM). Co-wavelength SCM+Pulse integration. Exp. ✓ |
| 47 | O_ISAC_047 | W-band OTFS ZP-DFT | `hybrid_fiber_wireless` | `advanced_dsp` | high | - | **FiWi-ISAC** - W-band (100 GHz). OTFS Modulation + ZP-2D-DFT. Improves Sensing Resolution (11cm -> 1.58cm) vs OFDM. 50km Fiber. Exp. ✓ |
| 48 | O_ISAC_048 | FSO DCO-OFDM Power Alloc | `free_space_optics` | `resource_allocation_isac` | high | - | **FSO-ISAC Optimization** - DCO-OFDM Power Allocation. Trade-off between Spectral Efficiency and Sensing Precision (Fisher Info). Sensing prefers high-freq subcarriers. Sim. ✓ |
| 49 | O_ISAC_049 | IVLCS TDMA Optimization | `visible_light` | `resource_allocation_isac` | high | - | **VLC-ISAC Optimization** - Indoor Visible Light. TDMA Resource Allocation (Slot Selection + Power). Minimize Total Power under ENR/CSR constraints. Sim. ✓ |
| 50 | O_ISAC_050 | VLC SPAO Multipath | `visible_light` | `advanced_dsp` | high | - | **VLC-ISAC Positioning** - Indoor VLC SPAO (Simultaneous Position & Orientation). OFDM + MM Algorithm. Harnesses NLOS multipath for estimation. Sim. ✓ |
| 51 | O_ISAC_051 | Remote Phase-Shift LiDAR PLRC | `free_space_optics` | `waveform_optimization` | high | - | **FSO-ISAC LiDAR** - PLRC (Phase-Shift Laser Ranging w/ Comm). RF Subcarrier with DSSS Phase Coding. Solves Phase Ambiguity with Code Correlation. Exp. ✓ |
| 52 | O_ISAC_052 | ADO-OFDM Resource Allocation | `free_space_optics` | `resource_allocation_isac` | high | - | **FSO-ISAC Optimization** - ADO-OFDM (DCO/ACO Hybrid). Adaptive Resource Allocation (Power split between DCO/ACO + Subcarriers). Balances SE vs Fisher Info. Sim. ✓ |
| 53 | O_ISAC_053 | VLC-VLS Closed Loop Control | `visible_light` | `protocol_design` | high | - | **VLC-ISAC Control** - Closed-Loop Controller for Servomotor. VLC for Commands (FM), VLS for Angle Feedback (Reflected Intensity from Triangular Foil). TDM Integration. Exp. ✓ |
| 54 | O_ISAC_054 | LED Pinhole Two-Phase O-ISAC | `visible_light` | `beamforming_optimization` | high | - | **O-ISAC Framework** - Two-Phase (Discovery/Tracking). Phase 1: Source Layout Optimization for max coverage. Phase 2: **Optical Beamforming** (Collimating Lenses) for LED steering. Pinhole Camera Sensing. Sim. ✓ |
| 55 | O_ISAC_055 | LFM-CPM FSO-ISAC Waveform | `free_space_optics` | `waveform_optimization` | high | - | **FSO-ISAC Waveform** - LFM-CPM (Linear Freq Mod + Continuous Phase Mod). Compatible with IM/DD (via Hilbert). Optimization of h and mu for trade-off between BER and CRB. Sim. ✓ |
| 56 | O_ISAC_056 | FSO-ISAC Capacity-Distortion Limits | `free_space_optics` | `information_theory` | high | - | **Fundamental Limits** - Capacity-Distortion (C-D) Region analysis. Optimal Input Distribution (Step vs Exp). Comparison of MAP, MLE, and BCRB estimators for Ranging. Sim/Analytic. ✓ |
| 57 | O_ISAC_057 | 60 GHz Photonic mmWave ISAC | `microwave_photonics` | `hardware_design` | medium | - | **MWP-ISAC** - Photonic generation of 60 GHz LFM-OOK signal using OFC and Heterodyning. **RF Channel**. 1 Gbps Comm / 1.8 cm Ranging. Exp. (Note: Channel is RF). ✓ |
| 58 | O_ISAC_058 | W-Band Photonic Multi-Target ISAC | `microwave_photonics` | `hardware_design` | medium | - | **MWP-ISAC** - 97.5 GHz W-band ISAC (Fiber-Wireless). Solves **False Target** generation in multi-target scenarios using Balanced PD & HPF. 15-60 Gbps Comm / ~2-3 cm Ranging. Exp. (RF Channel). ✓ |
| 59 | O_ISAC_059 | TN-NTN ISAC Architecture & Management | `hybrid_medium` | `network_architecture` | low | O_ISAC_059_review.json | **Network Concept** - Vision for ISAC in Terrestrial/Non-Terrestrial Networks (TN-NTN). Proposes using **O-RAN (RIC)** and **3GPP (NWDAF)** for managing sensing data. Mentions FSO/Optical as enabler. Concept. ✓ |
| 60 | O_ISAC_060 | QPSK-DSSS Unified Waveform for FSO-ISAC | `free_space_optics` | `waveform_design` | medium | - | **Unified Waveform** - QPSK-DSSS (QPSK Data + PN Spreading). **Robustness under Turbulence**. DSSS provides coding gain for Comm and autocorrelation peak for Ranging (100.011m accuracy). Sim. ✓ |
| 61 | O_ISAC_061 | OPA-Based OW-ISAC Beamforming Optimization | `free_space_optics` | `beamforming` | high | - | **OPA-ISAC** - Beamforming optimization for Optical Phased Array (32-element). Novel **Contrast Metric** for sensing (Imaging) + Light-Field SINR for Comm. Solves **Grating Lobe** issue. ITS Sim (~2-7 cm RMSE). Sim/Analytic. ✓ |
| 62 | O_ISAC_062 | 6-DoF VLC SLAP (SCA Algorithm) | `visible_light` | `localization` | high | - | **6-DoF SLAP** - Simultaneous Location And Pose estimation using VLC-OFDM. **SCA Algorithm** for joint optimization of location, pose, and scattering channel. Robust to **NLOS/Diffuse Scattering**. Derived CRLB. ~2-3 cm accuracy. Sim/Analytic. ✓ |
| 63 | O_ISAC_063 | Full-Field Frequency Response Characterization for Coherent TOSA | `fiber_optic` | `hardware_fidelity` | high | - | **TOSA Calibration** - Experimental method to characterize **Coherent TOSA** (AFR, PFR, IQ Skew) using a single **low-bandwidth PD** (2 GHz). Enables high-fidelity 64 GBaud 16-QAM. Critical for experimental ISAC hardware accuracy. Exp. ✓ |
| 64 | O_ISAC_064 | Integrated Sensing and Communications for Metropolitan Environments | `fiber_optic` | `network_sensing` | low | O_ISAC_064_review.json | **Metropolitan ISAC** - Review of field trials in **Hong Kong**. Uses deployed telecom fibers for **Distributed Vibration Sensing (DAS)** to monitor traffic/railways. Integration via LFM probes/carriers. Concept/Review. ✓ |
| 65 | O_ISAC_065 | THz-Over-Fiber System With OCDM for ISAC | `terahertz` | `waveform_design` | high | - | **OCDM-ISAC** - **Orthogonal Chirp Division Multiplexing** (Fresnel Transform) for **THz-over-Fiber**. Outperforms OFDM in robustness against **Frequency Selective Fading**. 32 Gbps Comm / 1.875 cm Ranging. 140 GHz / 10km Fiber / 3m Wireless. Exp. ✓ |
| 66 | O_ISAC_066 | Pre-Distortion for Soliton Collision in DP-NFDM | `fiber_optic` | `comm_focused` | medium | - | **Soliton Pre-Distortion** - Comm-focused study on **Nonlinear Frequency Division Multiplexing (NFDM)**. Derives formula for **Soliton Collision** distortion in **Dual-Polarization** and proposes **Pre-Distortion** to cancel it. Extends reach to 1650 km. Sim. ✓ |

---

## 📈 İstatistikler

| Metrik | Değer |
|--------|-------|
| Toplam çıkarılan | 6 |
| Wireless (VLC/FSO) | 2 |
| Fiber | 2 |
| Hybrid | 2 |
| Review Paper | 1 |
| Spot-check yapılan | 1 |

---

## 🏷️ Eligibility Concern Kategorileri

| Kod | Açıklama |
|-----|----------|
| `none` | Kapsam içinde, sorun yok |
| `hybrid_thz` | Optik üretim ama THz iletim |
| `simulation_only` | Sadece simülasyon, deneysel veri yok |
| `fiber_not_wireless` | Fiber tabanlı, wireless değil |
| `environmental_sensing` | Hedef nesne yerine atmosfer algılama |
| `review_paper` | Derleme makale, orijinal veri yok |

---

## 📝 Notlar

- Tüm JSON dosyaları `data/test_output/` klasöründe
- Her JSON dosyasında `_extraction_flags` alanı mevcut
- PDF vs Markdown doğrulaması O_ISAC_001 için yapıldı (100% başarılı)
