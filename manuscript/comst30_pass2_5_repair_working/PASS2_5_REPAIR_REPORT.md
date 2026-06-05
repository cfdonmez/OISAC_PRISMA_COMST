# PASS-2.5 Hard Repair Report

## Scope

- Working directory: `manuscript/comst30_pass2_5_repair_working/`
- Source copied from: `manuscript/comst30_pass2_working/`
- Protected directories not edited:
  - `manuscript_submission/`
  - `manuscript/finalShortened/`
  - `manuscript/finalManuscript/`
  - `manuscript/comst30_working/`
  - `manuscript/comst30_pass2_working/`

## Baseline Before Repair

Build command:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex
```

| Metric | Baseline |
|---|---:|
| Page count | 27 |
| References start page | 22 |
| Compiled bibitems | 132 |
| Figures | 7 |
| Tables | 12 |
| Numbered equation environments | 3 |
| Overfull hbox | 0 |
| Underfull hbox | 99 |
| Underfull vbox | 8 |
| Undefined citations | 0 |
| Undefined references | 0 |
| Active `\nocite{*}` | 0 |
| Main-build biography blocks | 0 |
| Explicit Zenodo DOI present | No |

## Repairs Applied

### Duplicate / Corrupted Introduction Blocks Removed

Removed the entire duplicate Introduction subsection:

- `\subsection{Optical Advantage and Fragmentation Detail}`
- its nested "Advantage" paragraphs;
- repeated "Unified O-ISAC Taxonomy" prose;
- repeated "The Fragmentation Challenge" prose;
- repeated "Related Surveys and Gap Analysis" prose.

This removed corrupted citation remnants such as `over 38 km .`, `bps/m .`, `JRC ,`, blank equation text after "physical resolution is", and `OSNR ,`.

### Missing Equation Placeholders

| Placeholder pattern | Action |
|---|---|
| `physical resolution is` followed by blank equation and `where v=c` | Removed with the duplicate Introduction block. The valid range-resolution equation remains in Section II. |
| `each study p is mapped to` followed by missing taxonomy vector | Removed with the duplicate taxonomy detail. The valid taxonomy vector remains at the start of Section IV. |
| `Measurement-plane governance follows:` followed by no equation | Removed with the duplicate taxonomy detail. No extra measurement-plane equation was needed. |

No duplicate equations were restored because the required equations already exist in the main technical sections.

### Taxonomy Duplicate Cleaned

The corrupted `Additional Axis-Level Taxonomy Detail` subsection was compressed into clean taxonomy clarification. It now preserves the core counts without missing equations or orphan punctuation:

- hybrid 116/220;
- fiber 45/220;
- VLC/LiFi 25/220;
- FSO 19/220;
- terahertz 1/220;
- shared front-end 194/220;
- direct 118/220 and coherent 97/220;
- ranging 162/220.

Additional short taxonomy clarification was added only after the page-count safeguard showed the draft had fallen below 26 pages.

### Manuscript-Internal Process Language Removed

Replaced the compiled paragraph that referred to Pass 2 and `\nocite{*}` with final-manuscript wording:

- The main bibliography is representative and load-bearing.
- The full 220-study corpus is preserved through ledger, extraction sheet, supplementary evidence records, and Zenodo package.
- No compiled prose mentions Pass 1, Pass 2, or `\nocite{*}`.

Source comments mentioning "Pass-2 main text" were also neutralized to "main text".

### Data Availability Added

Added a compact unnumbered `Data Availability` section before the references:

- Zenodo DOI: `10.5281/zenodo.19643231`
- Repository record name: `OISAC_PRISMA_COMST`
- States that the full corpus remains traceable through the supplementary ledger while the main manuscript cites representative/load-bearing records.

### Page Count Safeguard

After corrupted duplicate removal, the draft fell to 24 pages. To keep the repaired manuscript in the requested 26--29 page band without restoring corrupted blocks:

- Added controlled Section V core clarification on governed attrition and benchmark implications.
- Added controlled Section V reading rules explaining corpus membership, scenario points, rate--Delta r_min, rate--sigma_r/RMSE, full-triplet interpretation, and CRQ caution.
- Added short taxonomy clarification after Section V expansion still left the manuscript below 26 pages.

No large tables, duplicate figures, or original 44-page blocks were restored.

## Final Build

Final clean build command:

```text
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex
```

| Metric | Final |
|---|---:|
| Page count | 26 |
| References start page | 21 |
| Compiled bibitems | 132 |
| Figures | 7 |
| Tables | 12 |
| Numbered equation environments | 3 |
| Overfull hbox | 0 |
| Underfull hbox | 100 |
| Underfull vbox | 5 |
| Undefined citations | 0 |
| Undefined references | 0 |
| Active `\nocite{*}` | 0 |
| Main-build biography blocks | 0 |
| Data Availability includes DOI `10.5281/zenodo.19643231` | Yes |

## Artifact Scan Results

No matches remained for the requested hard-repair artifact patterns:

- duplicate/corrupted Introduction headings;
- missing-equation placeholders;
- `Pass 2`, `Pass-2`, `Pass 1`, `Pass-1`;
- `\nocite{*}`;
- "printing all 220 references" / "best use of a COMST page budget";
- orphan punctuation patterns such as ` ,`, ` .`, ` ;`, ` :`, `\cite{}`, and `[]`.

## Remaining Risks

- Underfull hbox warnings remain high because the source still contains compact IEEE two-column tables inherited from Pass 2. They are layout warnings, not build failures; overfull hboxes remain zero.
- References start on page 21 rather than page 22 because the hard repair removed corrupted duplicate material. The page count remains inside the requested 26--29 range and the representative bibliography count remains 132.
- The manuscript is now a clean repair base, but it has not received the final Pass-3 layout/style polish pass.

## Final Recommendation

Ready for Pass-3 final polish.
