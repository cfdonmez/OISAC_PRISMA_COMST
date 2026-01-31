# Section I-D Gap Summary Report

**Generated:** 2026-01-19  
**Source:** Analysis of 221 O-ISAC papers + IC_evidence_gold_v3_2.csv + COMST phrasebank

---

## Survey-like Works Identified in O-ISAC Corpus

| Paper ID | Title | Modality | Type | ISAC Depth |
|----------|-------|----------|------|------------|
| **O_ISAC_156** | Physical Layer Security for IoT (incl. JCAS, OWC) | Multi | **COMST Survey** | Partial |
| **O_ISAC_163** | Multi-Functional and Hybrid RIS for ISAC | Multi | **COMST Survey** | Cross-modal |
| **O_ISAC_368** | A Technical Review of ISAC in Optical Transmission System | Multi | **Review** | True O-ISAC |
| **O_ISAC_303** | Integrated sensing, lighting and communication (LiSAC) | VLC | **Review** | True O-ISAC |
| O_ISAC_006 | Recent Advancements and Challenges in ISAC-OF | Fiber | Review | True ISAC |
| O_ISAC_021 | Optical ISAC: Architectures, Potentials and Challenges | FSO | Overview | True ISAC |
| O_ISAC_033 | Simultaneous Sensing and Communication in Optical Fibers | Fiber | Survey | True ISAC |
| O_ISAC_068 | Joint Communication and Sensing Prospects (VLC) | VLC | Overview | True ISAC |
| O_ISAC_327 | Channel Modeling for VLC-IoE in 6G: A Survey | VLC | Survey | Partial |
| O_ISAC_039 | Visible Light Integrated Positioning and Communication | VLC | Overview | True ISAC |
| O_ISAC_161 | ISAC Transceiver Hardware Architectures | Photo-THz | Overview | Cross-modal |
| O_ISAC_142 | Intelligent Surfaces for 6G Wireless Networks | Multi | Overview | Partial |
| O_ISAC_150 | 6G Vision: Requirements, Technologies, Challenges | Multi | Overview | Partial |
| O_ISAC_162 | ISAC Overview: Use Cases, Channel Models, PoC | Multi | Overview | Cross-modal |
| O_ISAC_059 | ISAC for TN and NTN Integration | Multi | Overview | Partial |

**Total Survey-like Works:** 15 papers (2 COMST journals, 4 reviews, 9 overviews)

---

## Counts by Survey Class

- Fiber/DFOS surveys: 2 (O_ISAC_006, O_ISAC_033)
- VLC/LiFi surveys: 3 (O_ISAC_068, O_ISAC_327, O_ISAC_039)
- FSO/OWC surveys: 1 (O_ISAC_021)
- Photo-THz/Hardware surveys: 1 (O_ISAC_161)
- **Unified O-ISAC survey (covering all modalities):** 0 ⚠️

---

## Gap Coverage Analysis (G1–G7)

| Gap ID | Gap Label | Avg Coverage | Best Coverage By |
|--------|-----------|--------------|------------------|
| G1 | Terminology harmonization | 0.3 (Low) | None explicitly |
| G2 | Metric normalization | 0.5 (Low) | O_ISAC_021 (partial) |
| G3 | Cross-modality benchmarking | 0.0 (Absent) | None |
| G4 | Cross-domain transfer | 0.3 (Low) | O_ISAC_161 (hardware focus) |
| G5 | Unified PHY framework/taxonomy | 0.5 (Low) | O_ISAC_006, O_ISAC_021 (partial) |
| G6 | System-level co-design | 0.7 (Moderate) | O_ISAC_068, O_ISAC_161 |
| G7 | Systematic methodology (PRISMA) | 0.0 (Absent) | None |

**Critical Finding:** No existing survey addresses G3 (cross-modality benchmarks) or G7 (PRISMA methodology).

---

## Key Claims for Section I-D (Evidence-Backed)

1. **Claim: RF-ISAC surveys dominate, optical gaps persist**
   - External RF surveys [9], [10] provide extensive waveform/beamforming coverage but ignore optical ISAC.
   - *Phrase template:* "The rapid growth of ISAC has prompted several high-quality surveys... however, these works predominantly focus on RF/mmWave domains."

2. **Claim: Fiber sensing surveys lack communication integration**
   - O_ISAC_006, O_ISAC_033 review DAS/DFOS but do not address joint high-rate data transmission.
   - *Phrase template:* "Distributed fiber sensing reviews provide excellent coverage of... however, they rarely address concurrent communication."

3. **Claim: VLC surveys focus on positioning, not ISAC**
   - O_ISAC_327 (VLC channel modeling), O_ISAC_039 (VLP+VLC) address positioning but not sensing–communication trade-offs.
   - *Phrase template:* "VLC positioning surveys focus on indoor localization... yet, they seldom consider simultaneous high-rate communication."

4. **Claim: FSO channel surveys lack ISAC perspectives**
   - O_ISAC_021 introduces O-ISAC concepts but remains focused on FSO; Photo-THz coverage is nascent.
   - *Phrase template:* "FSO channel modeling surveys characterize atmospheric turbulence... but lack sensing–communication integration."

5. **Claim: No unified O-ISAC taxonomy exists**
   - No survey bridges fiber, FSO, VLC, and Photo-THz under a common framework.
   - *Phrase template:* "To the best of our knowledge, no prior survey provides a unified taxonomy bridging..."

6. **Claim: PRISMA-based systematic reviews are absent**
   - All identified surveys use narrative methodology (systematic_strength = Low).
   - *Phrase template:* "Critically, no existing work applies PRISMA systematic review methodology to the O-ISAC domain."

---

## Recommended I-D Narrative Structure

### Paragraph 1: RF-ISAC Survey Landscape
- Acknowledge extensive RF surveys [9], [10]
- Transition: "Within the optical community, surveys are fragmented across sub-domains."

### Paragraph 2: Fiber/DAS Survey Review
- Cite: [O_ISAC_006], [O_ISAC_033]
- Scope: DAS, φ-OTDR, forward-transmitted light sensing
- Limitation: "do not consider concurrent data transmission"

### Paragraph 3: VLC/LiFi Survey Review
- Cite: [O_ISAC_068], [O_ISAC_327], [O_ISAC_039]
- Scope: VLP algorithms, channel models, positioning
- Limitation: "designed separately... mutual benefits not utilized"

### Paragraph 4: FSO and Photo-THz Survey Review
- Cite: [O_ISAC_021], [O_ISAC_161]
- Scope: Waveform design, hardware architectures
- Limitation: "nascent coverage, single-modality focus"

### Paragraph 5: Gap Synthesis
- State G1–G7 gaps explicitly
- Use "To the best of our knowledge..." and "There is a lack of..."
- Bridge: "These gaps motivate the unified approach of this survey."

### Paragraph 6: Positioning This Survey (Table III)
- Reference existing Table III (lines 136-147 in draft)
- Preview contributions (bridge to Section I-E)
