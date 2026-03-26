# Section I-D Table III Cell Calibration Report

**Generated:** 2026-01-21 00:16
**Action:** Reviewer-level calibration of Metrics/Benchmark/Transfer cells.

## 1. Calibration Target: O_ISAC_021 (FSO Tutorial)

**Current Cells:** Metrics ◐ | Benchmark – | Transfer –

### Evidence Reviewed
- **Table 1 (line 59-72):** Comparison of WiFi/mmWave/O-ISAC with metrics: distance (<1km), data rate (Gbps), resolution (cm), angle resolution (1 mrad).
- **Fig. 4 (line 146-149):** DCO-OFDM numerical results with BER vs. SNR and RMSE for distance.
- **CRB discussion (line 163):** Cramér-Rao Bound for power allocation optimization.
- **Missing:** No cross-modality benchmarks; no explicit transfer evaluation.

### Verdict
| Axis | Score | Justification |
|------|-------|---------------|
| Metrics | ◐ ✔ | Reports BER/RMSE/SNR but no standardized taxonomy (resolution vs. accuracy). |
| Benchmark | – ✔ | FSO-only evaluations; no cross-modal tables. |
| Transfer | – ✔ | Hybrid RF+Optical as future trend, not explicit portability study. |

**Conclusion:** Scores are correctly calibrated.

---

## 2. Calibration Target: O_ISAC_303 (VLC Review)

**Current Cells:** Metrics ◐ | Benchmark – | Transfer –

### Evidence Reviewed
- **Table 3 (line 294-321):** 20+ systems with BER, throughput, SNR, localization precision, orienting error.
- **Table 4 (line 330-343):** Hybrid LiSAC performance (data rate, positioning accuracy).
- **CRLB discussion (line 267):** For positioning error variance.
- **Missing:** No cross-modality benchmarks (all VLC/LiFi); no transfer discussion to fiber/FSO.

### Verdict
| Axis | Score | Justification |
|------|-------|---------------|
| Metrics | ◐ ✔ | Substantial Table 3, but VLC-specific; no unified cross-modal taxonomy. |
| Benchmark | – ✔ | VLC-only system comparisons. |
| Transfer | – ✔ | No DSP/waveform portability to other modalities. |

**Conclusion:** Scores are correctly calibrated.

---

## 3. Overall Assessment

> **"Neither generous nor harsh"**: Both papers provide within-modality performance data (justifying ◐ for Metrics) but lack cross-modality normalization, unified benchmarks, and transfer analysis (justifying – for Benchmark and Transfer).

No cell changes recommended.
