# Whole-Manuscript Integration QA

Date: 2026-03-24
Owner: AI + User
Scope: release-gate consistency after abstract + Section IX integration, Section VII/VIII closeout sync, and bundle-hygiene refresh across the canonical manuscript sources.

## Integrated sources

- `drafts/abstract.md` | SHA256 `8134FD488382A97A85675134CDC61224915335648E3C8174AD8D4F4E097194E2`
- `drafts/section_01_introduction.md` | SHA256 `F66C2A415E0AFCF2DAC513E3B7A224DAB26D5C44C8E6F2C7A8BA5C23CE4E0402`
- `drafts/section_02_fundamentals_draft.md` | SHA256 `5A5CE3A1708C38B89A21FD1659A946EB4B38586FD78F56A9C4FFBA5BE14565F9`
- `drafts/section_03_methodology.md` | SHA256 `3BBC8EED7280E9B2C131CB3F025D6E0537E951BD8345A091C6E52E2580CC449A`
- `drafts/section_04_taxonomy.md` | SHA256 `689BD05AC93214F3AA6D0D429EB4735977953033D95339C41DAD64844C9B5926`
- `drafts/section_05_template.md` | SHA256 `AE8D0E434915929B86C35BF53484D3442969F2316C9CC248B01CCA0A53E0045A`
- `drafts/section_06_draft.md` | SHA256 `625225543D97F1CCFDCC4F1BFD0D3BA6818655C53224B3825BCA07AD8334722F`
- `analysis/VII_cr_mrg_v1/section_07_camera_ready.md` | SHA256 `3B75D87F6DC447F463E403F0FD6B320CF7C97BCA0D5DD7707CC02BB403054ED2`
- `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md` | SHA256 `3703DD983E233A493287DBD00AFB53ED7AD259823BE8CDEBCBF349519279622C`
- `drafts/section_09_conclusion.md` | SHA256 `B91B28E70A76D285B91147A87B40569BDD9D2E5E935AF6D0DD8D079DFF2FD729`

## Bundle outputs

- `review_package/01_manuscript_bundle.md` | words `35218` | SHA256 `B09FDEB5D982CDCAE4FD8CDD370E580229B57322421D669FD175BEF618B9417F`
- `review_package/COMST_review_bundle_01_manuscript.md` | words `35218` | SHA256 `B09FDEB5D982CDCAE4FD8CDD370E580229B57322421D669FD175BEF618B9417F`
- `manuscript/current_bundle/OISAC_COMST_current_bundle.md` | words `35218` | SHA256 `F22F36C62A869E6EFDBEE4A63659693DE3A48ADE3F1A0057479664ED25F488D1`

## Findings

- The review-package bundles and the centralized current-bundle copy are synchronized to the latest canonical abstract + Section I-IX sources and now reflect the post-closeout Section VII / Section VIII wording together with the newly drafted front and back matter.
- A canonical abstract source now exists under `drafts/abstract.md`, and that abstract is inserted at the top of both review-package bundles and the centralized current-bundle manuscript.
- A canonical Section IX source now exists under `drafts/section_09_conclusion.md`, and the integrated bundles no longer stop at Section VIII.
- The previous structural gap between Section I-F's organization map and the integrated bundle scope is therefore closed: the manuscript now exposes abstract + Section I-IX in the bundle layer.
- A final editorial readthrough pass removed remaining publication-facing drift in the active bundle path, especially by softening residual audit/artifact wording in Sections III, VII, and VIII and by making the Section VIII-F/VIII-G summary tables more reader-facing.
- Section VII closeout drift was removed: `Fig. VII-1` caption language now matches the deployment-map role of the asset, and `Table VII-2` now includes the missing `indoor_environments` row so the dual-view layer again spans all five macro domains.
- Section VIII closeout drift was removed: the introduction now states the V/VI/VII -> VIII bridge explicitly, `Fig. VIII-1` has a short reading guide in the text, and VIII-G now describes empty discrepancy examples as schema-preserving placeholders rather than populated paper-level evidence.
- Section II now includes explicit `Fig. II-1`, `Fig. II-2`, `Table II-1`, and `Table II-2` insertions in the canonical source, and those references are propagated into both review-package bundles and the centralized `manuscript/current_bundle` copy.
- Section III now uses local methodology labels `Table III-1` and `Fig. III-1` in the canonical source, which removes the direct `Fig. 5` collision that previously overlapped with Section V's planned frontier figure numbering.
- Section III publication-facing prose no longer exposes internal repo paths or file names in the manuscript narrative; methodological traceability is preserved without surfacing repository-specific paths to readers.
- Section III's PRISMA flow is now encoded as a simplified `flowchart TB` mermaid block in the canonical source, improving direct rendering in markdown-oriented editors such as VSCode Mermaid preview.
- Whole-manuscript figure numbering policy is now frozen as a deliberate hybrid scheme: Section I preserves `Fig. 1-3`, while Section II onward uses section-prefixed labels (`Fig. II-1`, `Fig. III-1`, `Fig. V-1`, `Fig. VI-1`, etc.).
- Section V canonical prose was updated accordingly, so the trade-off figures are now referenced as `Fig. V-1` and `Fig. V-2`; the former Section III / Section V figure collision is therefore closed at manuscript level.
- Section V now includes active figure insertions in the canonical source:
  - `fig_v_1.png` = governed operating cloud
  - `fig_v_2.png` = sparse admissible frontier
- Both Section V figures were generated directly from `analysis/V_ev_v2/*.csv` using a local matplotlib pipeline rather than AI image synthesis, preserving metric-scale fidelity.
- Section V legacy denominator drift was reconciled against the canonical 220-study corpus by excluding `O_ISAC_347` from the plotting path and updating the affected prose/table counts from `226/221/54/52` to the canonical `225/220/53/51` equivalents.
- Section IV package is now active in the canonical source rather than remaining planned-only:
  - `Table IV-D` was inserted into Section IV-D
  - `fig_iv_1.png` = canonical taxonomy flow
  - `fig_iv_2.png` = canonical medium-task specialization heatmap
- Section IV figures were generated from a canonical-filtered plotting path (`analysis/IV_ev_v2/generate_section4_figures.py` + `included_studies_canonical.csv`), so the active manuscript assets are safe even though some raw Section IV analysis CSVs still retain the non-canonical `O_ISAC_347` record outside that plotting path.
- The current-bundle README was refreshed so its scope statement now matches the integrated manuscript state (`abstract + Section I-IX`) instead of the older Section I-VIII-only snapshot.
- Figure placement is no longer a release blocker. Remaining figure-side work is limited to optional or low-risk asset-level polish: Section II visual/technical cleanup, `fig_vii_1` indoor-panel label compression, `fig_viii_1` visual polish, and optional future cleanup of raw Section IV analysis sources before direct reuse.

## Verdict

- Status: PASS
- Meaning: the integrated manuscript bundle is now structurally release-consistent for abstract + Section I-IX. Remaining work is limited to optional asset-level figure polish, final editorial refinement if desired, and future-reuse cleanup of non-canonical raw Section IV analysis artefacts.

