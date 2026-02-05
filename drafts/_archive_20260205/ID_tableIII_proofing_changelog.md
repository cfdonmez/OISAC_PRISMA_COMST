# Section I-D Reviewer Proofing Changelog

**Action:** Applied evidence-based calibration to Table III and added reviewer-proofing definitions.

## 1. Text & Legend Updates
- **Gap Synthesis:** Added clarification: "reports *context descriptors*... and evaluates **five gap axes**..." to prevent reviewer confusion about table column count.
- **Legend:** Added *Scoring Criteria* definition: $s_a(p) \in \{0, 1/2, 1\}$ mapped to $\{–, ◐, ●\}$ to define explicit evidence thresholds.

## 2. Table III Calibration Updates (Downgrades)

| Paper | Cell | Old Value | New Value | Reason |
|-------|------|-----------|-----------|--------|
| **[O_ISAC_070]** | FSO Scope | ◐ | **–** | Content check revealed 0 hits for "Free Space" in "Exploring Photonic THz-ISAC". Pure THz. |
| **[O_ISAC_163]** | FSO Scope | ● | **–** | Content check (2 hits) confirmed focus on "Photo-THz" RIS. "Multi-functional" refers to RIS tasks, not cross-modality FSO. |

**Verdict:** Table III is now strictly evidence-backed and uses a defined scoring model to resist reviewer challenges on "subjectivity".
