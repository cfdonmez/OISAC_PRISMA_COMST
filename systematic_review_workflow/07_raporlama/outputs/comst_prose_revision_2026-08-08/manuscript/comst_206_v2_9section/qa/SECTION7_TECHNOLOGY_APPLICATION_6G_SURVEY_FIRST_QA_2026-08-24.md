# Section VII Technology, Application, and 6G Evidence QA

Date: 2026-08-24

Status: `PASS_AWAITING_AUTHOR_REREAD`

## Scope

This report governs the revised Section VII source, its compact Table VII, the
planned Figure 8 carrier, the Section VI handoff, and the transition to Section
VIII. It records technical verification only. The section has not received
author approval.

## Survey narrative

Section VII now follows four reader questions.

1. Technologies That Create and Shape Observables explains how waveform,
   optical, carrier generation, and spatial control mechanisms form the
   communication and sensing observables.
2. Integration Beyond the Waveform shows how devices, infrastructure reuse,
   inference, and digital models extend joint design beyond signal selection.
3. Applications as Operating Requirements translates application labels into
   sensing targets, service settings, and evaluation conditions.
4. From 6G Relevance to Network Evidence distinguishes corpus relevance from
   conformance, interoperability, deployment readiness, and market maturity.

The section begins from the validation boundary established in Section VI and
ends by giving Section VIII a clear gap chain. The prose interprets mechanisms
and evidence. Table VII carries the compact application map. Planned Figure 8
will carry technology coverage and the exclusive 6G evidence gate.

## Count reconciliation

Technology labels are multilabel. The corrected counts are 56 OFDM or related
multicarrier, 13 beamforming, 7 multiple input multiple output, 64 coherent
optical techniques, 20 photonic integration, 68 photonic terahertz or microwave
photonic generation, 20 machine learning or artificial intelligence, 1
reconfigurable optical intelligent surface, 8 optical phased array, 2 digital
twin, 22 fiber distributed acoustic sensing, 66 frequency modulated continuous
wave or related chirped processing, and 19 other.

Application labels are also multilabel. Table VII reports 100 6G and access,
41 vehicular, 32 optical access, 13 indoor positioning, 4 data center, 55
environmental monitoring, 41 smart infrastructure, 34 industrial, 26 security
and surveillance, 6 healthcare, 20 aerospace, 2 underwater, and 17 other.

The exclusive 6G crosswalk totals 206 studies. It contains 138 direct, 64
inferential, 1 weak, and 3 not applicable assignments. The application label
named 6G and access remains distinct from this exclusive relevance code.

## Normalization correction

The Phase F normalization source and checkpoint were corrected before the
section was finalized. Token boundaries now prevent `Risley_prism` from being
read as RIS and prevent propagation or backpropagation terms from being read as
OPA. Healthcare excludes link health and structural health records. Indoor
positioning requires explicit indoor context. These corrections changed RIS or
ORIS from 2 to 1, OPA from 11 to 8, healthcare from 8 to 6, indoor positioning
from 25 to 13, and the fallback application category from 15 to 17.

Both regenerated Phase F artifact audits pass 29 of 29 checks. The study
universe remains 206, the exclusive 6G distribution remains 138, 64, 1, and 3,
and the primary claim totals are unchanged.

## Evidence boundary

The section preserves the distinction between an optical stage that generates
or stabilizes a carrier and the wireless or free space domain through which the
radiated carrier propagates. Beamforming, optical phased arrays, multiple input
multiple output processing, and intelligent surfaces are treated as different
spatial functions rather than interchangeable labels.

The machine learning synthesis asks readers to interpret each task with its
reference data, training distribution, evaluation shift, uncertainty, and
inference cost. Application counts describe coverage in the reviewed corpus.
They do not establish prevalence, platform rank, market maturity, conformance,
or deployment readiness. The two underwater records support framing or
laboratory emulation and are not presented as pooled underwater field evidence.

## Language and carrier QA

- COMST style audit words: 1,424.
- Mean sentence length: 14.680 words.
- Mean paragraph length: 71.200 words.
- Sentences over 35 words: 0.0 percent.
- TeXcount sum: 1,460 words, including 1,423 text words, 28 heading words, and
  9 caption words.
- Reader prose, caption, and table note contain zero author inserted colons or
  semicolons, zero uses of `neither`, and no avoidable alphabetic hyphenation.
- Table VII contains four columns and thirteen application rows arranged as
  three stacked panels. Each panel repeats the column headings and contains no
  more than five rows. Domain names provide bold row anchors, counts use the
  compact `n (percent)` form, and the study references form a centered visual
  axis.
- The table retains one caption, one label, open sides, `footnotesize` text,
  and booktabs rules. It uses no vertical rules, shading, decorative color, or
  row numbering. This follows the local design already used in Table II and the
  IEEE guidance for table placement, width, type size, and row spacing.
- Role and condition cells summarize recurring patterns. For each domain, the
  table includes a selected study set and lists its references in the Studies
  column.
- The float barrier is placed at the end of Section VII. This preserves prose
  continuity while keeping Table VII before Section VIII.

## Citation and build QA

- Main citation coverage is 206 of 206 included studies with zero missing.
- Included study citation uses are 415 across 200 citation commands. No
  included study citation cluster exceeds seven sources.
- The final IEEEtran build is 23 pages and 203,204 bytes.
- PDF SHA-256 is
  `8045AA1F597390721C2A39653F7861EB3EA35605F168A8B8281C9368E9061959`.
- Section VII source SHA-256 is
  `99FE3C62E4139083352D57E477AFF00848C8DDBE149E47D3CD116E05D8775714`.
- Fatal, undefined citation, undefined reference, duplicate destination,
  overfull box, and oversized float findings are zero.
- Rendered pages 13 through 17 show no clipping, overlap, overflow, or broken
  reading order. Section VII begins on page 14, Table VII appears intact on
  page 16, and Section VIII begins below it on the same page. Table VIII remains
  at the top of page 17 and therefore stays ahead of the limitations and
  conclusion text.

## Next author action

Reread the revised Section VII from its opening. Keep the section at
`awaiting author approval` until that reading is complete. Section VIII and the
remaining closing material stay later steps in the author reading sequence.
