# Whole-Manuscript Integration QA

Date: 2026-03-15
Owner: AI + User
Scope: release-gate integration of the current canonical Section I-VIII sources into review-package manuscript bundles.

## Integrated sources

- `drafts/section_01_introduction.md` | SHA256 `F66C2A415E0AFCF2DAC513E3B7A224DAB26D5C44C8E6F2C7A8BA5C23CE4E0402`
- `drafts/section_02_fundamentals_draft.md` | SHA256 `5A5CE3A1708C38B89A21FD1659A946EB4B38586FD78F56A9C4FFBA5BE14565F9`
- `drafts/section_03_methodology.md` | SHA256 `EC8878954CB43F7A7AACAEDB2D9E899389174D67C246A1B6FCA1E739884F9F00`
- `drafts/section_04_taxonomy.md` | SHA256 `0F0FEBBB3CB62F021A5F252A3B885ED6882A6D7D0AB8B76216852B03B8BE0FEF`
- `drafts/section_05_template.md` | SHA256 `18CF374BA01FC8B1B4E1BE832AA4721653F28DE035776FFCA994770C2F708DFA`
- `drafts/section_06_draft.md` | SHA256 `625225543D97F1CCFDCC4F1BFD0D3BA6818655C53224B3825BCA07AD8334722F`
- `analysis/VII_camera_ready_merge_v1/section_07_camera_ready.md` | SHA256 `D8E2AA704D171D856D18C8D7B5FCEB0CEB8299C05CF8149EC968FC5A50F1810C`
- `analysis/VIII_camera_ready_merge_v1/section_08_camera_ready.md` | SHA256 `C2E9EE36E85BBC9ED17078E7D17CB30BDA533297013884E00D4CDB5F6123FF37`

## Bundle outputs

- `review_package/01_manuscript_bundle.md` | words `33651` | SHA256 `AE5E0DD817456DA6FF224518BD6D828D4CBAA7EDE264325F2852EF4E4C5E0D67`
- `review_package/COMST_review_bundle_01_manuscript.md` | words `33651` | SHA256 `AE5E0DD817456DA6FF224518BD6D828D4CBAA7EDE264325F2852EF4E4C5E0D67`

## Findings

- The review-package manuscript bundles were stale and incomplete before this pass; they now integrate the current canonical Section I-VIII sources in UTF-8.
- Section VII and Section VIII are now present in the manuscript bundle, matching the latest camera-ready sources used elsewhere in the repo.
- Section II now includes explicit `Fig. II-1`, `Fig. II-2`, `Table II-1`, and `Table II-2` insertions in the canonical source, and those references are propagated into both review-package bundles and the centralized `manuscript/current_bundle` copy.
- Section III now uses local methodology labels `Table III-1` and `Fig. III-1` in the canonical source, which removes the direct `Fig. 5` collision that previously overlapped with Section V's planned frontier figure numbering.
- Section III publication-facing prose no longer exposes internal repo paths or file names in the manuscript narrative; methodological traceability is preserved without surfacing repository-specific paths to readers.
- Section III's PRISMA flow is now encoded as a simplified `flowchart TB` mermaid block in the canonical source, improving direct rendering in markdown-oriented editors such as VSCode Mermaid preview.
- Whole-manuscript figure numbering policy is now frozen as a deliberate hybrid scheme: Section I preserves `Fig. 1-3`, while Section II onward uses section-prefixed labels (`Fig. II-1`, `Fig. III-1`, `Fig. V-1`, `Fig. VI-1`, etc.).
- Section V canonical prose was updated accordingly, so the trade-off figures are now referenced as `Fig. V-1` and `Fig. V-2`; the former Section III / Section V figure collision is therefore closed at manuscript level.
- The repo does not currently expose a canonical standalone Section IX source file under drafts/analysis/review_package; the integrated bundle therefore stops at Section VIII.
- Section V still contains legacy paper-level denominator language using ``221 papers`` in analysis-derived prose, while the manuscript-wide canonical included corpus is ``220``. Because the current integration pass did not rerun the Section V analysis pack, this remains a flagged consistency item rather than an auto-corrected value.
- Figure assets are still pending outside this integration pass, especially Section V ``Fig. V-1 / Fig. V-2`` and user-owned placement of Section VI figures. Section II figures are now inserted, but `Fig. II-2` still has a review-tracked technical cleanup note before final release polish.

## Verdict

- Status: CONDITIONAL PASS
- Meaning: the integrated review bundle is now up to date for Section I-VIII, but final release still requires resolution of the Section IX source gap (if a conclusion section is expected), Section V legacy denominator reconciliation, and the remaining figure package/polish items.

