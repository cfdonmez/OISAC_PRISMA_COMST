# VIII Overview QA

## Gate Checklist
- placeholders (TODO/TBD/FIXME/ELLIPSIZATION): PASS (count=0)
- G0 intent check (`Open Challenges and Research Roadmap`): PASS
- G2 preflight readiness PASS: PASS
- G3 evidence-pack lock (`analysis/VIII_ev_v1`): PASS
- domain labels exact (5 required labels): PASS
- bridge policy acknowledged as INDIRECT by design: PASS
- ORIS canon (OIRS=0, standalone IRS=0): PASS
- bracket-safe math (no [ ] in math): PASS
- length in range (200-280 words): PASS (words=207)
- cite-keys restricted to VIII preflight shortlist: PASS

- Overall verdict: **PASS**

## Cite-Key Existence (references.bib)
- O_ISAC_035: present
- O_ISAC_115: present
- O_ISAC_163: present
- O_ISAC_202: present
- O_ISAC_220: present
- Missing keys: none

## Processed Markdown Validation Log
- Validation target per key: Abstract/Intro + one relevant section + Conclusion/Limitations opened.
- O_ISAC_035 -> data/proc_markdowns/O_ISAC_035/O_ISAC_035.md -> HeadingPath: OCDM-Based FMCW Waveform Design for FSO Integrated Sensing and Communications > I. INTRODUCTION -> intro_line=9, relevant_line=52, conclusion_or_limitations_line=291
- O_ISAC_115 -> data/proc_markdowns/O_ISAC_115/O_ISAC_115/O_ISAC_115.md -> HeadingPath: Integrated Sensing and Communication in 6G: the Deterministic Channel Models for THz Imaging -> intro_line=13, relevant_line=9, conclusion_or_limitations_line=243
- O_ISAC_163 -> data/proc_markdowns/O_ISAC_163/O_ISAC_163.md -> HeadingPath: II. BACKGROUND AND STUDY > E. Contributions of This Survey -> intro_line=23, relevant_line=90, conclusion_or_limitations_line=640
- O_ISAC_202 -> data/proc_markdowns/O_ISAC_202/O_ISAC_202.md -> HeadingPath: Integrated optical covert sensing and communication > 1. Introduction -> intro_line=13, relevant_line=23, conclusion_or_limitations_line=130
- O_ISAC_220 -> data/proc_markdowns/O_ISAC_220/O_ISAC_220.md -> HeadingPath: Advanced SMART network: empowering subsea monitoring with dense photonic integrated sensing and communication > 1. INTRODUCTION -> intro_line=13, relevant_line=19, conclusion_or_limitations_line=182

## Path Resolution Method
- Primary: `analysis/man_v1/file_index.csv`
- Fallback: `analysis/II_md_inv.csv`
- Hits via primary: 0/5
- Hits via fallback: 5/5

## SHA256
- `VIII_OVERVIEW.md`: `028476aceda01757be4568ff32c1c2b3a3b9eede62b1a54e33b0de395351269b`
- `VIII_OVERVIEW_supp.md`: `8323fd447eb14bd3d93bc4304ca72f31f7904f0e34df92e3366aacbc88b14d4f`
