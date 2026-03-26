# COMST Master Writing Recipe (76-paper synthesis)

Source: `analysis/synth_rpt.md`, `analysis/wrt_bp_master.json`, `analysis/lay_stats.json`, `analysis/rhet_rpt.json`, and section templates in `memory-bank/`. Built from 76 IEEE COMST survey papers.

## 0) Baseline budgets
- Total words: ~36k; visuals: ~19 figures, ~12 tables.
- Word share by section (avg): Intro ~10%; Related Surveys ~10%; Fundamentals/System ~23%; Technical Solutions/Taxonomy ~17%; Challenges/Future ~11%; Conclusion + refs ~27% (includes lessons + references block).
- Implication: invest most words in Fundamentals + Solutions; keep Intro lean; make Conclusion a synthesis hub, not just a summary.

## 1) Canonical skeleton and objectives
- Introduction (goal: why-now + gap + promise, ~4k words)
  - Hook with trend + hard requirement (6G KPI, reliability, latency, verticals).
  - Gap vs existing surveys; add Table I: survey comparison (columns: Year, Scope, Tech focus, Missing).
  - Contribution bullets (3-5) + visual map (outline/taxonomy sketch).
  - Close with organization map sentence.
- Related Surveys (if separated from Intro, ~4k words)
  - Critique prior surveys by axis (scope, metrics, datasets, verticals).
  - Use comparison table verbs: surveys/summarizes/shows/provides.
  - Declare what you will do differently (taxonomy depth, synthesis, prototyping, PRISMA rigor).
- Fundamentals / System Model (~9k words, largest block)
  - Define architecture, actors, channels, threat model, and KPIs; include notation/abbreviation table.
  - Include at least one architecture/signal-flow figure; keep math minimal but precise.
  - Bridge to applications: map fundamentals to 6G verticals (eMBB/URLLC/mMTC) or domain-specific scenarios.
- Technical Taxonomy / Solutions (~7k words)
  - Build a classification tree (by use-case, layer, enabling tech, or performance objective).
  - For each branch: describe problem framing, representative methods, pros/cons, and **end with a bold Lesson X: ...** synthesis paragraph.
  - Use summary tables per branch (Ref, Scenario, Method, Metric, Key takeaway). Favor qualitative comparison over heavy simulations (only ~1/3 papers run evals).
- Cross-cutting Enablers (sprinkle or dedicate subsections)
  - Security/privacy, standardization status, datasets/benchmarks, hardware/prototypes as credibility bridges.
  - If prototypes exist, slot a short "Prototype/Hardware" subsection before algorithms to ground realism.
- Challenges & Future Directions (~4.5k words)
  - Mirror taxonomy axes: list open issues per branch with trade-offs and risks.
  - Use forward-looking verbs (remain, require, demand, enable) and connect to enabling tech trends (AI, THz, RIS, semantic comms, edge/cloud).
- Conclusion (~10k words including refs)
  - Synthesize 3-5 distilled insights (not repetition) + 3-5 actionable future research items.
  - Remind the reader of the taxonomy and where gaps remain; avoid new citations unless essential.

## 2) Visual and table recipe
- Must-have figures: early outline/structure tree; taxonomy diagram; at least one scenario/architecture schematic per major vertical/use-case; optional timeline/evolution chart.
- Must-have tables: survey comparison table (existing reviews); taxonomy/solution summary tables per branch; abbreviations/notation; challenges vs enablers mapping.
- Caption verbs that match COMST style (from rhetoric_report): "surveys", "summarizes", "shows", "provides".

## 3) Language and rhetorical moves
- Sentence starters (top transition starters): however, therefore, finally, thus, hence, consequently.
- Introductions lean on "Although extensive research..., there is still a lack of ..."; contributions start with "The main contributions are visualized in Fig. X and summarized as follows:".
- Use Lesson blocks to force synthesis: **Lesson X: <one-line takeaway>** after each subsection.
- Keep tone formal/technical; prefer precise verbs (mitigates, enables, characterizes, quantifies) over vague ones.

## 4) Workflow to instantiate for your survey
- Outline selection: start from `synthesis_report.md` standard flow; adjust taxonomy axes to O-ISAC specifics (e.g., sensing modality, comms objective, deployment scenario).
- Phrase selection: pull hooks/gap/contribution lines from `memory-bank/*templates.md`; reuse phrasebank patterns for gap, contrast, and future work.
- Evidence plan: for each taxonomy branch, pre-collect 3-7 anchor papers with key metric/setting; log in a solution summary table template.
- Visual plan: sketch taxonomy figure + 1 scenario schematic per vertical before writing; reserve figure numbers early.
- Compliance check: Intro <=10% words, Fundamentals+Solutions ~40%, Challenges >=10%, visuals >=15, tables >=8.

## 5) Quick checklist (before writing each section)
- Do I state the gap vs existing surveys and show it in Table I?
- Does each major subsection end with a Lesson paragraph?
- Is there a taxonomy figure + matching summary table?
- Are security/privacy/standardization noted somewhere (even briefly)?
- Are figures/tables captioned with active verbs (surveys/summarizes/shows/provides)?
- Did I map scenarios to standard verticals or clear use-cases to signal exhaustiveness?

## 6) Common pitfalls to avoid (from blueprints)
- Pure algorithm dumps without a hardware/prototype bridge.
- Scenario descriptions without concrete architectures (BS/edge/user links) or KPI hooks.
- Future-work lists detached from the taxonomy (must mirror the structure you built).
- Overlong intro without a visual map; under-specified contributions.

Use this recipe with the section templates (`memory-bank/`) and phrasebank (`analysis/pbank.json`) to turn the 76-paper reverse-engineering into a single-pass writing workflow.
