# 📋 O-ISAC Data Extraction Protocol

> **Version:** 1.0  
> **Last Updated:** 2025-12-28  
> **Aligned With:** PRISMA 2020, prisma_protocol.md (Section 4, 8, 9)

---

## 1. Purpose & Scope

This document codifies **HOW** we extract structured data from O-ISAC papers. It bridges:
- `prisma_protocol.md` → WHAT to extract (eligibility, data items)
- `oisac_extraction_schema_v2.yaml` → WHERE to store (field definitions)
- This protocol → HOW to extract (decision rules, reasoning process)

---

## 2. Eligibility Criteria (Quick Reference)

> Full details: `protocol/prisma_protocol.md` Section 4

### ✅ INCLUDE if:

| Criterion | Description |
|-----------|-------------|
| **Dual Function** | Paper demonstrates BOTH sensing AND communication on optical carrier |
| **Shared Resource** | Functions share hardware, spectrum, waveform, or power budget |
| **Technical Detail** | Sufficient physical-layer models for taxonomy classification |
| **Peer-Reviewed** | Journal article or full-length conference paper |

### ⛔ EXCLUDE if (Exclusion Codes):

| Code | Reason |
|------|--------|
| `EXC-WRONG-DOMAIN` | RF/mmWave ISAC without optical carrier |
| `EXC-PURE-SENSING` | Optical sensing only (e.g., classical φ-OTDR, LiDAR) without communication |
| `EXC-PURE-COMM` | Optical communication only without sensing function |
| `EXC-NO-PHY` | Conceptual/vision paper lacking physical-layer models |
| `EXC-TYPE` | Non-eligible type (thesis, white paper, magazine article) |

### ⚠️ BORDERLINE Cases:

| Scenario | Decision |
|----------|----------|
| Sensing on existing telecom fiber (φ-OTDR + WDM) | ✅ INCLUDE if coexistence designed |
| Power-over-Fiber + Communication | ⛔ EXCLUDE (PoF ≠ sensing) |
| Channel estimation for beamforming | ⛔ EXCLUDE (not explicit sensing) |
| "Future work" mentions ISAC | ⛔ EXCLUDE (no concrete implementation) |

---

## 3. Two-Level Extraction Structure

### 3.1 Study-Level (One per paper)

| Block | Fields |
|-------|--------|
| `bibliographic` | record_id, title, authors, year, venue, doi |
| `classification` | oisac_medium_class, carrier_band, operational_environment |
| `application` | application_domain, scenario_description |
| `evidence` | evidence_type, validation_baselines_present |
| `enabling_tech` | ris_present, opa_present, machine_learning_used |
| `key_contribution` | key_contribution, gap_addressed, performance_enablers |

### 3.2 Scenario-Level (One per experiment/configuration)

Each distinct operating point gets its own scenario record:
- Different distances → separate scenarios
- Different modulation orders → separate scenarios
- Different turbulence conditions → separate scenarios

| Block | Fields |
|-------|--------|
| `identification` | experiment_id, scenario_label |
| `transmitter` | tx_source_type, wavelength_nm, optical_bandwidth_ghz |
| `receiver` | rx_detection_type, rx_detector |
| `integration` | hardware_sharing_mode, duplexing_mode |
| `waveform` | comm_waveform_family, sensing_waveform_family, isac_waveform_relationship |
| `channel_*` | fibre or wireless channel parameters |
| `comm_metrics` | data_rate_gbps, ber, snr_db |
| `sensing_metrics` | sensing_task_type, range_resolution_m, localization_error_m |
| `tradeoff` | coupling_mode, tradeoff_type, tradeoff_representation |

---

## 4. Reasoning Trace (Chain-of-Thought)

Every extraction MUST include a `reasoning_trace` block with 4 steps:

```json
"reasoning_trace": {
    "step_0_visual_inspection": "...",
    "step_1_concept_analysis": "...",
    "step_2_benchmark_verification": "...",
    "step_3_strategic_critique": "..."
}
```

### Step-by-Step Guide:

| Step | Question to Answer | Source |
|------|-------------------|--------|
| **step_0** | What do the figures show? | `visual_analysis.txt`, paper figures |
| **step_1** | What is the O-ISAC mechanism? TDM/FDM/Joint/WDM? | Abstract, Introduction, Methods |
| **step_2** | Are the claimed metrics physically plausible? | Results, compare to prior art |
| **step_3** | What gap does this address? What's missing? | Abstract, Conclusion |

### Example:

```json
"step_0_visual_inspection": "Fig.1: System diagram shows PM→MZM→BPD chain. Fig.3: BER curves show 10^-3 at 15 dB SNR.",
"step_1_concept_analysis": "Hybrid fiber-wireless. Sensing via φ-OTDR on WDM channel, communication on separate λ. Integration: WDM-isolated.",
"step_2_benchmark_verification": "120 Gbps at 1550nm over 10km is consistent with C-band coherent systems. FMCW 2.5mm resolution matches 60 GHz BW.",
"step_3_strategic_critique": "Contribution: First photonic THz ISAC. Gap: No outdoor atmospheric testing."
```

---

## 5. Extraction Flags (`_extraction_flags`)

Every JSON MUST start with this block:

```json
"_extraction_flags": {
    "eligibility_concern": "none | borderline_topic | review_paper | exclude_*",
    "data_completeness": "high | medium | low",
    "needs_spot_check": true | false,
    "notes": "Free-text explanation"
}
```

### Eligibility Concern Values:

| Value | Meaning |
|-------|---------|
| `none` | Valid O-ISAC paper, no issues |
| `borderline_topic` | Reviewed, included with reservations |
| `review_paper` | Survey/tutorial - extract differently |
| `exclude_pure_sensing` | Sensing only, no communication |
| `exclude_pure_comm` | Communication only, no sensing |
| `exclude_pof_no_sensing` | Power-over-Fiber without sensing |

---

## 6. Missing Data Handling (NR vs NA)

| Code | Meaning | When to Use |
|------|---------|-------------|
| `"NR"` | Not Reported | Paper could have reported but didn't |
| `null` | Not Applicable | Field doesn't apply to this paper type |
| `"EST-FIG"` | Estimated from Figure | Value digitized from plot |

### Rules:

1. **Never guess** - If not stated, use "NR"
2. **Fibre fields NA for FSO papers** - e.g., `fibre_length_km: null`
3. **If extractable from figure** - Use value + flag in notes: `"notes": "EST-FIG from Fig.3"`
4. **Prefer NR over wrong values** - Better to have gaps than errors

---

## 7. Enum Value Reference

### 7.1 O-ISAC Medium Class (`oisac_medium_class`)

| Value | Description |
|-------|-------------|
| `cabled_fibre` | φ-OTDR, DAS, Brillouin, WDM+sensing on fiber |
| `wireless_fso` | Free-space optical, laser links |
| `wireless_vlc` | Visible light communication (LED-based) |
| `wireless_lidar_like` | OPA-based, automotive LiDAR ISAC |
| `wireless_retroreflective` | CCR-based bidirectional links |
| `hybrid_fiber_wireless` | RoF, photonic-assisted mmW/THz |

### 7.2 ISAC Waveform Relationship (`isac_waveform_relationship`)

| Value | Description |
|-------|-------------|
| `single_dual_function` | Same waveform serves both S&C |
| `comm_embedded_in_sensing` | Comm data on sensing waveform (e.g., QPSK on FMCW) |
| `sensing_embedded_in_comm` | Sensing on comm signal (e.g., OFDM radar) |
| `multiplexed_separate` | Separate waveforms, TDM/FDM/WDM multiplexed |
| `not_specified` | Paper doesn't clarify |

### 7.3 Key Contribution Enablers (`performance_enablers`)

Common values (see schema for full list):
- `photonic_dechirping` - PDC for THz reception
- `joint_waveform_design` - Unified S&C waveform
- `coherent_homodyne` / `coherent_heterodyne` - Detection schemes
- `phi_otdr` / `das` - Fiber sensing methods
- `frequency_comb` - OFC-based systems
- `wavelength_reuse` - Same λ for S&C

---

## 8. Review Paper Handling

For survey/tutorial papers (like O_ISAC_006, O_ISAC_021):

1. Set `"eligibility_concern": "review_paper"`
2. Extract `bibliographic` and `classification` normally
3. Extract ONE representative scenario if numerical results present
4. In `key_contribution`, summarize the review's scope
5. Note coverage areas in `notes`

---

## 9. Quality Checklist

Before finalizing each extraction:

- [ ] `_extraction_flags` present and accurate?
- [ ] `reasoning_trace` has all 4 steps?
- [ ] `key_contribution` block complete?
- [ ] At least one `scenario_level` entry?
- [ ] All numeric values have units in field names?
- [ ] Enums match schema exactly?
- [ ] No placeholder values like "XXX" or "TODO"?

---

## 10. File Naming & Location

| Output | Location |
|--------|----------|
| Extraction JSON | `data/test_output/O_ISAC_XXX_simulation.json` |
| Tracking Table | `data/extraction_tracker.md` |
| Schema | `analysis/oisac_extraction_schema_v2.yaml` |

---

## 11. Related Documentation

| Document | Purpose |
|----------|---------|
| [prisma_protocol.md](../protocol/prisma_protocol.md) | Full PRISMA protocol |
| [schema_v2.yaml](../analysis/oisac_extraction_schema_v2.yaml) | Field definitions |
| [V4_PIPELINE_EXPLAINED.md](V4_PIPELINE_EXPLAINED.md) | Automated pipeline |
| [PHASE3_COT_ENGINE.md](PHASE3_COT_ENGINE.md) | CoT reasoning details |
| [extraction_tracker.md](../data/extraction_tracker.md) | Progress tracking |

---

**Maintained by:** O-ISAC Survey Team  
**Version Control:** Git tracked in project repository
