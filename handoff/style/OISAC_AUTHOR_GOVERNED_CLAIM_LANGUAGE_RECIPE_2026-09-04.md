# O-ISAC Author-Governed Claim-Language Recipe

**Status:** Required authoring policy for the next manuscript version  
**Adopted for planning:** 2026-09-04  
**Authority:** Author-governed editorial and scientific policy  

This recipe is not a descriptive finding extracted from the 76-paper COMST
corpus. It governs how the O-ISAC authors convert the locked evidence base into
reader-facing claims. Corpus-derived house-style guidance remains useful for
structure and reader load, while this policy controls scientific emphasis,
missingness translation, and claim strength.

## 1. Two layers must remain separate

The evidence-management layer preserves source-level values, provenance,
conditions, reviewer decisions, internal status labels, and exclusions. The
reader-facing layer presents the strongest scientifically supported pattern and
the boundary needed to interpret it.

Internal bookkeeping must not become the manuscript's narrative. At the same
time, editorial polish must never invent a missing condition, suppress material
counterevidence, or enlarge the permitted inference.

## 2. Evidence-forward paragraph contract

Build each synthesis paragraph in this order:

> scientific construct or mechanism -> strongest supported evidence -> claim
> boundary, stated once and only when it affects interpretation -> engineering
> meaning or research action

Lead with what the evidence enables the reader to understand. Do not lead with
a catalogue of absent fields, status labels, or rejected comparisons.

## 3. Mandatory claim rules

1. **Scope every claim.** State whether the unit is a report, study, metric
   record, within-study relation, or a bounded corpus-level pattern. Never
   substitute one denominator for another.
2. **Translate internal status into scientific meaning.** Raw extraction or
   adjudication codes stay in governed evidence artifacts. Reader-facing prose
   states their consequence, such as whether the evidence permits a numerical
   comparison, a within-study relation, a mechanism-level interpretation, or
   only architectural context.
3. **Do not turn absent reporting into a result.** An unquantified penalty is
   neither zero nor evidence of no penalty. A missing condition cannot be
   borrowed from a neighbouring experiment, figure, or simulation.
4. **Keep material limits claim-adjacent.** If a missing operating point,
   baseline, measurement plane, timing trace, or condition set changes the
   claim, state the scientific boundary beside that claim. Do not defer it only
   to the limitations section.
5. **Keep material counterevidence in the same synthesis unit.** A design
   benefit and the conditions under which it reverses, disappears, or incurs a
   cost must be interpreted together.
6. **Do not force the desired relation.** When direct numerical comparison is
   unsupported, move to the strongest truthful synthesis level that the source
   supports.
7. **Match verbs to evidence strength.** Prefer `is associated with`, `links`,
   `indicates`, or `supports` unless the study design justifies causal or
   universal language. Do not use `proves`, `guarantees`, or `causes` for
   source-native observational, simulated, or model-based relations.
8. **Do not equate validation setting with joint validation.** A field or
   deployment label does not establish that communication and sensing outcomes
   were obtained in the same run, configuration, or operating condition.
9. **Convert recurring reporting limitations into a research requirement.** A
   literature-level gap must identify what future studies should measure,
   control, report, and release. It must not remain a generic complaint.
10. **Preserve scientific integrity.** Source-level omissions that do not alter
    the permitted claim may remain outside the main narrative. Their relevance
    must be decided against the prespecified J and claim-permission rules before
    prose selection and retained in the audit trail. Missingness or
    counterevidence that changes the permitted claim may not be hidden.
11. **Allow a non-narrative terminal route.** A record that supports none of the
    permitted synthesis levels must remain audit-only, unresolved, or outside
    reader-facing synthesis according to the governed decision. It must not be
    softened into a positive pattern merely to keep it in the narrative.

## 4. Support-to-synthesis decision ladder

Use the highest level that passes its evidence conditions:

1. **Aligned quantitative comparison:** metric meaning, unit, plane, baseline,
   condition set, and independence are sufficiently aligned.
2. **Within-study relation:** a shared or varied factor connects communication
   and sensing outcomes inside one traceable study context.
3. **Mechanism or directional synthesis:** heterogeneous native values support
   a recurring coupling mechanism or direction, but not a common numerical
   scale.
4. **Architecture or feasibility mapping:** the source establishes a physical
   path, integration choice, or feasible function without supporting a joint
   performance relation.
5. **Actionable literature gap:** the missing link is itself recurrent and
   scientifically consequential, and it leads to a specific experiment,
   benchmark, reporting field, or reusable artifact.
6. **Audit-only or no reader-facing claim:** no scientifically supported
   synthesis route remains, or a material conflict is unresolved. Preserve the
   trace and disposition; if the conflict materially affects a corpus-level
   conclusion, report that effect beside the conclusion.

Failure at one level triggers a routing decision, not automatic rescue. Use the
strongest lower level that remains supported, or the audit-only terminal route
when no reader-facing inference is justified.

## 5. J-consistent claim construction

For the scientific object

\[
J_r=\langle P_r,G_r,X_r,C_r,S_r,M_r,E_r\rangle,
\]

the preferred claim skeleton is:

> Within [P] and through [G], the [variation in / presence of / constraint
> imposed by] [X] links [C] and [S] under [M], where that link is explicitly
> traceable in the source. The available [E] supports a [within-study / bounded
> cross-study / mechanism-level / descriptive] inference.

Use the skeleton as a logic check, not as repetitive prose. A valid paragraph
may distribute these elements across several sentences.

If the full relation is not established, use positive routing language:

> Across the source-native operating contexts, [X] recurrently links [relevant
> outcomes or mechanisms]. The evidence therefore supports [strongest supported
> synthesis level], while a shared [scientific element] is required for
> [stronger inference].

## 6. Reader-facing translation examples

Avoid a bookkeeping-led sentence:

> Several records had incomplete or unclear fields and were excluded from the
> comparison.

Prefer a science-led sentence:

> Across source-native settings, power allocation and receiver dynamic range
> repeatedly linked communication fidelity to sensing sensitivity. Because the
> studies did not establish aligned operating points, the evidence supports the
> recurring mechanism rather than a pooled numerical ranking.

Avoid an unsupported success claim:

> The architecture produces no communication penalty while improving sensing.

Prefer the permitted claim:

> The architecture demonstrated the sensing function alongside communication;
> the available trace does not quantify the magnitude or absence of a
> communication penalty at the same operating point.

Avoid a generic future-work complaint:

> More complete reporting is needed.

Prefer an actionable requirement:

> Future evaluations should report paired communication and sensing outcomes
> under a shared condition set, identify the baseline and measurement plane,
> and retain a configuration-level validation trace that permits reconstruction.

## 7. Placement rule

| Manuscript location | Reader-facing role |
|---|---|
| Introduction | State the unresolved decision problem, not a list of missing fields. |
| Foundations/comparison framework | Define the evidence and claim-permission rules once. |
| Technical synthesis | Lead with mechanisms and supported relations; state material boundaries beside the claim. |
| Validation/benchmark section | Aggregate recurrent transfer and reconstruction limits. |
| Discussion/roadmap | Convert literature-level gaps into controlled actions, success measures, and artifacts. |
| Supplement/governed evidence | Preserve row-level status, provenance, adjudication, and full audit detail. |

## 8. Release checklist

- Does the paragraph begin with scientific meaning rather than record status?
- Is the analysis unit and denominator correct?
- Is the chosen synthesis level the strongest one actually supported?
- Are material conditions and counterevidence visible where they affect the
  claim?
- Has any absent value been converted into a zero, a negative result, or a
  favourable assumption?
- Does every literature-level gap lead to a specific research or reporting
  action?
- Can each quantitative statement be traced to its governed evidence source?

The governing principle is concise: **internal codes remain in the audit
layer; reader-facing prose carries scientific meaning, the honest inference
boundary, and the strongest supported action.**
