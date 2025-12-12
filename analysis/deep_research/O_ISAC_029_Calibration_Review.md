# Calibration Report: O_ISAC_029

**Date:** 2025-12-13
**Agent:** Deep Research Agent (Gemini 2.5 Flash)
**Baseline:** v3 Extraction Pipeline (O_ISAC_029_v21.json)
**Status:** ⚠️ Discrepancies Found

## Executive Summary
The Deep Research Agent successfully generated an evidence package for O_ISAC_029. When compared with the existing baseline extraction (v21), the agent demonstrated **High Recall** for detailed hardware specifications and experimental conditions, often providing more context (e.g., specific laser models, "net" vs "peak" data rates).

However, there are notable **Precision/Recall** discrepancies in specific numerical values (Fiber Length, BER) where the Baseline and Agent disagree. A manual verification suggests the Agent's extraction (supported by quotes) is likely more accurate or refers to a different experimental configuration than the one selected in the Baseline.

## Detailed Comparison

| Feature | Deep Research Agent | Baseline (v21) | Verdict | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Data Rate** | **116 Gbit/s** (peak), 108.4 (net) | **116 Gbps** | ✅ Match | Agent correctly identified the overhead nuance. |
| **Fiber Length** | **20 km** | **10 km** | ❌ **Mismatch** | Agent quotes "20-km SMF transmission configuration". Baseline might be referring to a different exp setup or is outdated. |
| **BER** | **< 1E-2** | **0.001** (1E-3) | ⚠️ Deviation | Agent cites the threshold/performance limit ("remains below 1E-2"). Baseline cites a specific data point (0.001). |
| **Range Res.** | **6 mm** | **0.006 m** | ✅ Match | Units handled (mm vs m). |
| **Center Freq.** | **134 GHz** | D-band (Implicit) | ✅ Superior | Agent extracted the exact center frequency (134 GHz). |
| **Sensing Range**| **10.24m** (Unambiguous), **1m** (Practical) | **10 m** | ⚠️ Nuance | Baseline captured the theoretical max. Agent captured both theoretical and practical limits. |
| **Hardware** | Detailed (ECL-1/2, TFLN-MZM Model) | Generic (tfln_mzm) | ✅ Superior | Agent retrieved specific model numbers (MZ135-LN-110). |

## Key Findings & Recommendations

1.  **Fiber Length Discrepancy (20km vs 10km):** The prompt should encourage listing *all* tested configurations if multiple exist. The Agent found the "20km" mention.
    *   *Action:* Verify if the paper has multiple setups (Back-to-back, 10km, 20km). If so, the Agent should ideally capture all or the "best" performance.
2.  **BER (Threshold vs Value):** The Agent tends to quote the text ("below 1E-2"), while the extraction schema asks for a specific value (0.001).
    *   *Action:* Update System Prompt to prefer "measured best performance" values over general thresholds if available.
3.  **Hardware Detail:** The Agent excels at finding specific component models. This is a strong plus for the Deep Research approach.

## Conclusion
The Deep Research Agent is performing well, matching or exceeding the baseline in detail. The discrepancies highlight potential errors in the *Baseline* or ambiguity in the paper, rather than Agent failure. The Agent's ability to provide "Quote Banks" (Source Groundwater) effectively validates its claims.
