# Section VI Validation and Reconstructability QA

Date: 2026-08-24

Status: `PASS_AWAITING_AUTHOR_REREAD`

## Scope

This report governs the revised Section VI source, its compact Table VI, the
planned Figure 7 carrier, the Section V handoff, and the transition to Section
VII. It records technical verification only. The section has not received
author approval.

## Survey narrative

Section VI now follows four reader questions.

1. Validation Settings and Methods separates the strongest reported setting
   from the overlapping methods used to build the evidence.
2. Field Evidence Across Communication and Sensing distinguishes field or
   deployment outcomes in both functional domains from concurrent joint
   operation.
3. Artifact Access and Reconstructability separates reported access routes
   from the additional information needed to recreate a physical experiment.
4. Benchmark Readiness interprets the appraisal distribution and states the
   descriptive scope of the survey.

Figure 7 remains the planned carrier for validation distributions. Table VI is
a compact single-column map of observed artifact access. Supplement S7 carries
the 12-study field or deployment subset, and S-Appraisal carries the study
level TQAF scores. The prose interprets scientific meaning and does not turn
these carriers into a method audit.

## Count reconciliation

- Exclusive maximum setting distribution is 32, 18, 78, 66, and 12, totaling
  206 studies. A total of 156 studies reached at least a laboratory experiment
  or proof of concept.
- Overlapping validation methods are 131 analytical, 14 numerical analysis,
  104 simulation, 13 dataset evaluation, 148 laboratory experiment, 83
  prototype or testbed, 12 field experiment, 33 mixed, and 0 unclear.
- Reported data access is 145 unavailable or not reported, 41 available on
  request, 13 open, and 7 not applicable.
- Reported code or model access is 197 unavailable or not reported, 7
  available on request, 1 partial components, and 1 not applicable.
- TQAF reproducibility is 4 low, 199 adequate, and 3 strong. Benchmark
  readiness is 48 low, 158 adequate, and 0 strong.
- Supplement S7 contains 12 studies. Six report field or deployment outcomes
  in both functional domains and six do not meet that narrower rule.
  Relationship timing and separate function locators remain unresolved for
  all 12 records.

## Evidence boundary

The six S7 cases establish study-level field or deployment outcomes in both
functional domains. They do not establish the same run, concurrent operation,
one shared configuration, or one shared condition set. Section VI now states
that a concurrency claim requires both outcomes to be traceable to the same
configuration, time interval, and conditions.

The reconstruction framework is identified as a framework developed in this
review. Table VI reports observed access states only. The surrounding prose
explains the configuration, calibration, processing, metric, data, and version
information needed for reconstruction.

## Language and carrier QA

- COMST style audit words: 1,300.
- Mean sentence length: 16.049 words.
- Mean paragraph length: 59.091 words.
- Sentences over 35 words: 1.2 percent.
- TeXcount sum: 1,323 words, including 1,288 text words, 22 heading words, and
  13 caption words.
- Reader prose, caption, and table note contain zero author-inserted colons or
  semicolons, zero uses of `neither`, and no avoidable alphabetic hyphenation.
  The remaining hyphenated forms are formal labels such as O-ISAC and named
  supplements.
- Table VI is readable as one compact survey map and does not duplicate the
  reconstruction framework, Figure 7, or Figure 4.

## Citation and build QA

- Main citation coverage is 206 of 206 included studies with zero missing.
- Included-study citation uses are 415 across 197 citation commands. No
  included-study citation cluster exceeds seven sources.
- The final IEEEtran build is 23 pages and 203,337 bytes.
- PDF SHA-256 is
  `4467D5816FA20A1A0D0E64B11A9EC0997EC786D168F04AE83582056DB4D3CBC8`.
- Section VI source SHA-256 is
  `441D1767C96A8FAFA41C015C5E1C60880A4AE861897DC46AAA50AF764CB7B11C`.
- Fatal, undefined citation, undefined reference, duplicate destination,
  overfull box, and oversized float findings are zero.
- Rendered pages 11 through 14 show no clipping, overlap, overflow, or broken
  reading order. Table VI appears intact on page 13, and the Section VII
  transition begins cleanly on page 14.

## Next author action

Reread the revised Section VI from its opening. Keep the section at
`awaiting author approval` until that reading is complete. Sections VII through
IX and the Abstract remain later steps in the author reading sequence.
