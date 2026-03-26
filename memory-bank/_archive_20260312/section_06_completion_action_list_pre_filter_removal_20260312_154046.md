# Section VI Completion Action List (2026-03-12)

Owner: AI + User
Scope: Bring `drafts/section_06_draft.md` from recovered working draft state to publication-ready Section VI without breaking consistency with Sections I, II, IV, V, VII, and VIII.

## Backup Rule

- Before every edit pass on an existing Section VI document, create a timestamped archive copy under `drafts/_archive_20260205/`.
- Backup created for this pass:
  - `drafts/_archive_20260205/section_06_draft_pre_actionlist_step1_20260312_114658.md`

## Why Section VI Needs Controlled Repair

- Section I promises an enabler-centric section grounded in ORIS, OPA, photonics-assisted generation, and ML integration.
- The recovered Section VI draft evolved into a broader "enabling technologies + system-level co-design" chapter.
- That evolution is useful, but it can create contradictions if prevalence claims, metric language, taxonomy labels, or maturity framing drift away from Sections I, II, IV, V, VII, and VIII.

## Non-Negotiable Guardrails

- Keep Section II governance intact:
  - no OSNR/SNR plane mixing
  - no resolution/accuracy aliasing
  - no `delta_z` to `delta_r_min` substitution
- Keep Section IV taxonomy labels normalized and reusable.
- Keep Section V discipline on governed evidence, bounded interpretation, and explicit limitations.
- Keep Section I promises defensible:
  - Section VI must remain enabler-centric even if it includes system-level co-design layers.
- Treat ORIS as the canonical umbrella term unless a paper-specific alias is required locally.

## Completion Sequence

### Step 1. Freeze the target publication structure and scope boundary
Goal
- Decide what Section VI is in the final manuscript and what it is not.

Actions
- Freeze the final narrative mission of Section VI.
- Freeze the final subsection architecture.
- Freeze what stays in the core manuscript versus what must move out to support material / workflow notes.
- Freeze the cross-section consistency contract with Sections I, II, IV, V, VII, and VIII.

Output
- This action list file, including the target publication structure below.

Done criteria
- We can edit the draft without re-deciding scope on every pass.

### Step 2. Separate core manuscript prose from internal scaffolding
Goal
- Remove working-draft internals from the core paper path.

Actions
- Move or strip `Artifact Map`, `Evidence Table`, raw locator tables, and workflow-style audit prose from the core Section VI draft.
- Keep only publication-facing prose, equations, final tables, and figure comments/placeholders in `drafts/section_06_draft.md`.
- Preserve removed material in a support note or archival workflow file, not by deleting it without trace.

Done criteria
- `drafts/section_06_draft.md` opens like a paper section, not like a lab notebook.

### Step 3. Repair structural order and section flow
Goal
- Fix heading order, broken transitions, and misplaced equations.

Actions
- Restore a clean top-level sequence:
  - section opener
  - notation block
  - VI-A .. VI-F in order
- Fix VI-E / VI-F heading collision and equation-placement corruption.
- Ensure every subsection has:
  - short motivation
  - analytical or synthesis core
  - bounded takeaway / open-issue closeout

Done criteria
- The section reads in a single uninterrupted narrative order.

### Step 4. Freeze the final table program
Goal
- Decide which tables stay in the paper and which are support artifacts only.

Actions
- Normalize numbering and caption style.
- Remove placeholder rows and unresolved table cells.
- Keep only tables that support the paper's argument.

Recommended keep-set
- `Table VI-1`: Unified notation block
- One enabler/comparison table for VI-A
- `Table VI-2`: Reproducibility / benchmark contract table
- At most one additional compact synthesis table if it materially helps VI-E or VI-F

Done criteria
- No table is optional, placeholder-like, or duplicative.

### Step 5. Freeze the final figure program
Goal
- Prepare Section VI figures in the same disciplined way planned for Section V.

Actions
- Insert comment-style figure specifications into the draft before real assets are produced.
- Freeze figure intent, inputs, caption logic, and placement.

Recommended figure set
- `Fig. VI-1`: Enabler landscape map
  - medium vs enabler families
  - governed prevalence, not raw count inflation
- `Fig. VI-2`: System-level coupling diagram
  - enabler -> impairment -> optimization/control -> deployment/benchmark chain

Done criteria
- Figure purpose is fixed and can be turned into assets later without rewriting the prose.

### Step 6. Apply prevalence and metric-governance hardening
Goal
- Prevent Section VI from overstating maturity or violating earlier metric rules.

Actions
- Freeze strict-vs-raw prevalence policy.
- Filter invalid OPA/RIS metric rows or label them as unvalidated.
- Add an explicit limitation paragraph where needed.
- Ensure claims are evidence-anchored rather than metric-trace inflated.

Done criteria
- Section VI cannot be read as making stronger adoption claims than Section I supports.

### Step 7. Resolve weak-evidence families
Goal
- Bring PIC / programmable photonics / ML / photonic-generation claims to a defensible level.

Actions
- Strengthen anchors where possible.
- Otherwise downgrade to qualitative-only framing.
- Avoid weak family claims becoming headline findings.

Done criteria
- No weakly anchored family is presented as a mature, uniformly evidenced trend.

### Step 8. Align Section VI with Section IV, V, VII, and VIII
Goal
- Make Section VI the bridge section it is supposed to be.

Actions
- Check label and medium consistency against Section IV.
- Check governed-language consistency against Section V.
- Check application handoff to Section VII.
- Check maturity/limitation framing so Section VIII stays grounded.

Done criteria
- Section VI strengthens, rather than destabilizes, the whole-manuscript storyline.

### Step 9. Editorial compression and publication polish
Goal
- Convert the repaired draft into COMST-style survey prose.

Actions
- Remove lab language, internal notes, and over-explaining.
- Keep equations only where they help the synthesis.
- Tighten subsection openers and closers.

Done criteria
- The section reads like a survey manuscript, not a drafting dossier.

### Step 10. Final release gate for Section VI
Goal
- Declare Section VI ready for full-manuscript integration.

Checklist
- Core narrative only
- Clean heading order
- Final table set fixed
- Figure comments inserted
- No unresolved placeholder rows
- No unresolved critical TODOs in core prose
- Cross-section consistency verified

## Step 1 Output: Frozen Target Publication Structure

### Final mission statement

Section VI will explain how O-ISAC becomes practically realizable by linking enabling technologies to system-level control, robustness, optimization, runtime overhead, and benchmarking discipline.

This means Section VI is not a mere hardware catalog.
It is the bridge from:
- Section IV taxonomy
- Section V trade-off evidence
to:
- Section VII deployment/application plausibility
- Section VIII challenge and roadmap synthesis

### Frozen core structure

1. Short Section VI opener
- One paragraph on why enablers matter as coupled levers, not isolated gadgets.

2. `Table VI-1` notation block
- Kept if concise and publication-facing.

3. `VI-A. Programmable Optical Enablers`
- OPA
- ORIS
- PIC / photonic-integration context only if sufficiently anchored
- Core message: controllability and integration leverage

4. `VI-B. Channel Impairments and Robustness`
- Core message: enabler value is conditional on medium-specific impairments

5. `VI-C. Joint Co-Design and Resource Optimization`
- Core message: waveform / beam / power / ORIS control are coupled

6. `VI-D. Experimental Validation, Benchmarking, and Reporting Contract`
- Core message: comparability is the main maturity bottleneck
- This is a hinge subsection and should be preserved

7. `VI-E. Networked and Multi-User O-ISAC`
- Core message: scaling introduces overhead, interference, coordination, and fusion burdens

8. `VI-F. AI/ML and Security-Aware Adaptation`
- Core message: adaptation and trust matter, but maturity is uneven and must be written cautiously

9. Short section synthesis / transition
- One closeout paragraph that hands off naturally to Section VII.

### What must stay out of the core manuscript

- Full artifact maps
- Full evidence tables / claim locator tables
- Workflow notes
- Placeholder-only table rows
- Large TODO lists
- Internal labels like "MODE C" unless converted into publication prose
- Optional-table language

### Cross-section consistency contract

- With Section I:
  - keep the section enabler-centric and do not oversell maturity
- With Section II:
  - preserve metric-plane and metric-type governance
- With Section IV:
  - preserve taxonomy labels and medium naming
- With Section V:
  - preserve governed-evidence caution and bounded interpretation
- With Section VII:
  - keep a clear bridge from enabler capability to deployment plausibility
- With Section VIII:
  - keep maturity gaps explicit so roadmap claims do not overreach

## Immediate next edit pass after Step 1

- Execute Step 2:
  - strip non-manuscript scaffolding from `drafts/section_06_draft.md`
  - preserve removed material in a support note if needed
  - then repair the top-level reading order before touching detailed claims
