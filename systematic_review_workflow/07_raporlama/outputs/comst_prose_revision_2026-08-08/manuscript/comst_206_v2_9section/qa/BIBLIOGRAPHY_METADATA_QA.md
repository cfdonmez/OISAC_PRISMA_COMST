# Cited-Primary Bibliography Metadata QA

**Audit date:** 2026-08-09  
**Candidate bibliography:** `references_206_candidate.bib`  
**Citation scope:** manuscript sections `00_ABSTRACT.tex` through
`13_CONCLUSION.tex`

## Scope and authority

The audit extracted every `OISAC_SCR...` key actually cited in Sections
00--13 and restricted enrichment to those cited-primary entries. The resulting
set contains **76 unique citation keys**, all of which have one and only one
entry in the candidate bibliography. All 76 entries already contained a DOI;
no DOI was inferred, searched by title alone, or newly invented.

Metadata was retrieved from the Crossref REST endpoint
`https://api.crossref.org/works/{doi}` on 2026-08-09. Crossref describes this
endpoint as returning bibliographic metadata deposited by its publishing
members and trusted sources:
<https://www.crossref.org/documentation/retrieve-metadata/rest-api/>.
The local row-level identity authority was
`qa/study_category_citation_map_206.csv`.

An entry was eligible for enrichment only when all of the following held:

1. the DOI returned by Crossref matched the candidate DOI;
2. the candidate title matched the Crossref title, using the Crossref subtitle
   as part of the identity string when present; and
3. the candidate key had exactly one bibliography entry and one row-level
   study-map record.

All **76/76** cited entries passed these identity gates. For
`OISAC_SCR00833`, Crossref stores `CORE-lens` as the title and the remainder as
a subtitle; the combined title--subtitle identity matches the unchanged
candidate title.

## Enrichment rules

Only fields supplied by the DOI record were used. Author names were expanded
to Crossref-deposited given and family names where available. Journal or
proceedings title, volume, issue/number, page range or article identifier, and
year were synchronized with the DOI record. Print year was preferred when
Crossref supplied it; otherwise online, issued, and published year were used
in that order. Page ranges were represented with BibTeX double hyphens. When
Crossref supplied an article number instead of a page range, that identifier
was placed in `pages` for compatibility with the candidate BibTeX workflow.

The existing candidate `title` and `doi` values were deliberately preserved.
No absent issue number, author given name, volume, or pagination field was
guessed from naming conventions or secondary search results.

## Numerical results

| QA item | Result |
|---|---:|
| Unique cited-primary keys | 76 |
| Cited entries with DOI | 76 |
| Unique cited DOIs | 76 |
| DOI + title identities verified | 76 |
| Entries matching retrieved metadata after enrichment | 76 |
| Journal articles | 56 |
| Proceedings articles | 20 |
| Entries with author field | 76 |
| Entries with journal/booktitle | 76 |
| Entries with volume | 56 |
| Entries with issue/number | 48 |
| Entries with pages/article identifier | 76 |
| Entries with verified year | 76 |
| Entries with full deposited given names for every author | 73 |
| Strictly complete cited entries across all requested, type-applicable fields | 67 |
| Authoritatively partial cited entries | 9 |

On structured publication fields alone, a type-appropriate definition---journal
records require volume, issue/number, and pages/article identifier, whereas
proceedings records require booktitle and pages---finds **68 entries fully
populated** and **8 authoritatively partial**. When full deposited given names
are also required, **67 entries are strictly complete** and **9 are partial**.
All 76 remain core-complete for author identity, title, venue, year, DOI, and
page/article identity.

## Remaining authoritative gaps

Crossref did not supply an issue/number for the following eight journal
records, so no `number` field was added:

- `OISAC_SCR00012`
- `OISAC_SCR00056`
- `OISAC_SCR00277`
- `OISAC_SCR00294`
- `OISAC_SCR00376`
- `OISAC_SCR00906`
- `OISAC_SCR00941`
- `OISAC_SCR01025`

Three entries contain at least one given name supplied only as initials in the
Crossref deposit:

- `OISAC_SCR00012`: `H.Y. Fu`;
- `OISAC_SCR00277`: `R. Arunachalam` and `M. Vinoth Kumar` (the third author,
  `Rupali Singh`, is deposited in full); and
- `OISAC_SCR00959`: `J. C. Wang`, `T. Y. Liu`, and `J. H. Zhou`.

Those deposited forms were retained rather than expanded speculatively. The
nine strictly partial entries are the union of these three author cases and
the eight missing-issue cases above; `OISAC_SCR00012` and `OISAC_SCR00277`
occur in both groups.

## Integrity checks

- Every cited key resolves to exactly one candidate BibTeX entry.
- All 76 cited DOI values are unique.
- Candidate DOI and title identity matches the row-level study map for
  **76/76** entries.
- Post-update comparison against the retrieved Crossref fields found
  **0 metadata mismatches**.
- No unresolved HTML entities remain in cited author or venue fields.
- Non-cited bibliography entries were outside the enrichment scope.
- No manuscript section or claim text was changed.
- No backup bibliography, graphic, or compiled manuscript was produced.

The remaining gaps are therefore limitations of the authoritative deposits,
not silently completed metadata.
