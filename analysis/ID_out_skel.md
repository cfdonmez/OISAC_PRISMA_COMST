# Section I-D Outline Skeleton (Draft-Ready)

> **COMST Rhetorical Moves:** categorize → delimit scope → compare coverage → expose gaps → state contributions
> 
> **Source Assets:** `phrasebank.json`, `COMST_master_recipe.md`, `introduction_templates.md`

---

## Paragraph 1: RF-ISAC Survey Landscape (Context Setting)

**Purpose:** Acknowledge extensive RF-ISAC survey literature; frame optical as the underexplored frontier.

**Sentence starters (COMST phrasebank):**
- "The rapid growth of ISAC has prompted several high-quality surveys in recent years..."
- "However, these works predominantly focus on the RF and mmWave domains."
- "For instance, comprehensive RF-ISAC tutorials [9], [10] provide extensive coverage of waveform design, beamforming, and signal processing for radar-communications, but they offer little to no discussion on optical-layer integration."

**Citations:** External RF-ISAC surveys (numbered refs [9], [10], [11] etc. outside O_ISAC corpus)

**Word budget:** ~80 words

---

## Paragraph 2: Fiber/DAS Survey Review

**Purpose:** Review distributed fiber sensing surveys; note lack of ISAC integration.

**Key surveys to cite:**
- [O_ISAC_006] — "Recent Advancements and Challenges in ISAC-OF" (Fiber review)
- [O_ISAC_033] — "Simultaneous Sensing and Communication in Optical Fibers" (DAS + coherent)

**Sentence starters:**
- "Distributed fiber sensing reviews provide excellent coverage of Rayleigh, Brillouin, and Raman-based techniques [12]..."
- "However, they do not consider concurrent data transmission on the same fiber."
- "Recent work [O_ISAC_006] surveys ISAC-OF advancements but remains focused on cabled modalities."

**Key limitation to state:** "lack sensing–communication trade-off analysis"

**Word budget:** ~100 words

---

## Paragraph 3: VLC/LiFi Survey Review

**Purpose:** Review VLC positioning surveys; note lack of high-rate data integration.

**Key surveys to cite:**
- [O_ISAC_068] — "Joint Communication and Sensing Prospects: Potential Through Visible Light"
- [O_ISAC_327] — "Channel Characterization and Modeling for VLC-IoE in 6G: A Survey"
- [O_ISAC_039] — "Visible Light Integrated Positioning and Communication: MTL Framework"

**Sentence starters:**
- "VLC positioning surveys [11] focus on indoor localization algorithms and receiver design..."
- "Yet, they seldom consider simultaneous high-rate data communication."
- "As articulated in [O_ISAC_039]: 'VLC and VLP systems are usually designed separately... mutual benefits have not been utilized effectively.'"

**Key limitation to state:** "designed separately, mutual benefits not exploited"

**Word budget:** ~100 words

---

## Paragraph 4: FSO and Photo-THz Survey Review

**Purpose:** Review FSO channel and photonic-THz surveys; note nascent ISAC coverage.

**Key surveys to cite:**
- [O_ISAC_021] — "Optical ISAC: Architectures, Potentials and Challenges" (FSO overview)
- [O_ISAC_161] — "ISAC Transceiver Hardware Architectures, Technologies, and Trends" (Hardware)

**Sentence starters:**
- "FSO channel modeling surveys [13] characterize atmospheric turbulence and pointing errors for communication links..."
- "...but lack sensing–communication integration perspectives."
- "Photonic-THz surveys are emerging [O_ISAC_161] but remain focused on single-link demonstrations and hardware constraints."

**Key limitation to state:** "nascent coverage, no cross-modality comparison"

**Word budget:** ~100 words

---

## Paragraph 5: Gap Synthesis (Critical Gaps Identified)

**Purpose:** Synthesize what no existing survey provides, aligned with I-C fragmentation claims.

**Gap bullets (from gap matrix, aligned with I-C):**
- **G1 (Terminology):** No survey provides a unified glossary bridging fiber/FSO/VLC/Photo-THz naming
- **G3 (Benchmarking):** No cross-modality benchmark suite enabling fair comparison
- **G5 (Unified Framework):** No unified PHY taxonomy covering all O-ISAC modalities + joint S&C
- **G7 (Methodology):** No PRISMA-based systematic review in O-ISAC domain

**Sentence starters (COMST phrasebank):**
- "To the best of our knowledge, no prior survey provides a unified taxonomy..."
- "There is a lack of a unified physical-layer framework that bridges fiber sensing, optical wireless, and the broader ISAC community."
- "Critically, no existing work applies the PRISMA 2020 systematic review methodology to the O-ISAC domain, limiting reproducibility and evidence-based synthesis."

**Word budget:** ~120 words

---

## Paragraph 6: Positioning This Survey (Table III Reference)

**Purpose:** Present Table III comparison; preview contributions and bridge to Section I-E.

**Must include:**
- Reference to Table III (already in draft at lines 136-147)
- Explicit statement of how this survey addresses G1–G7 gaps
- Bridge sentence to Section I-E (Contributions)

**Sentence starters:**
- "Table III provides a systematic comparison between this survey and existing related works, explicitly highlighting the unique scope and contributions of our PRISMA-based approach."
- "Our survey addresses these gaps through five primary contributions, detailed in Section I-E."
- "In contrast to prior reviews, this work provides..."

**Word budget:** ~80 words

---

## Total Paragraph Budget: ~580 words (within ~600 word target for I-D)

---

## COMST Table III Enhancement Notes

The existing Table III (lines 136-147) should be verified to include:
- All identified O-ISAC surveys: [O_ISAC_006], [O_ISAC_021], [O_ISAC_068], [O_ISAC_327], [O_ISAC_161]
- Gap coverage columns aligned with G1–G7
- Clear "This Survey" row showing full coverage

---

## Phrase Templates for I-D (from COMST Phrasebank)

### Gap Identification
- "While there have been several surveys and reviews on [X], there is a lack of..."
- "To the best of our knowledge, no prior survey..."
- "Although extensive research has been conducted on [X], there is still a lack of..."
- "Unlike other reviews, this survey..."

### Comparison/Contrast
- "In contrast to [Ref], our work..."
- "While [Ref] focuses on [X], we address [Y]."
- "Existing surveys tend to be confined to specific sub-domains..."

### Transition to Contributions
- "To address these gaps, this survey provides..."
- "The main contributions are summarized as follows:"
- "Table III summarizes the comparison between this survey and related works."
