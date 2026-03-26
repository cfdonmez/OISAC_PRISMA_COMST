# Stylekit and Template Asset Paths (v1)

## Explicit internal style assets discovered

| asset path | governs | evidence | how to apply |
|---|---|---|---|
| `writing_recipes/COMST_master_recipe.md` | COMST rhetorical skeleton, word budgets, visuals/tables, Lesson endings. | `writing_recipes/COMST_master_recipe.md:10-37`, `writing_recipes/COMST_master_recipe.md:38-47`, `writing_recipes/COMST_master_recipe.md:54-63` | Use as high-level section pacing + synthesis style contract before section drafting. |
| `docs/surv_write_guide.md` | COMST + PRISMA integration, per-section writing obligations, visual-density expectations. | `docs/surv_write_guide.md:9-12`, `docs/surv_write_guide.md:29-37`, `docs/surv_write_guide.md:49-55`, `docs/surv_write_guide.md:68-75` | Use for section-level objective checks (intro gap framing, methodology rigor, challenge framing). |
| `memory-bank/master_writing_guide.md` | Detailed template system: headings, figure/table quotas, citation rhetoric, acronym handling, lesson pattern. | `memory-bank/master_writing_guide.md:302-337`, `memory-bank/master_writing_guide.md:365-379`, `memory-bank/master_writing_guide.md:393-395` | Use as operational writing checklist; treat org-map snippet in this file as legacy (see contradictions). |
| `memory-bank/introduction_templates.md` | Intro micro-template, table/figure caption behavior, lesson sentence requirement. | `memory-bank/introduction_templates.md:19-29`, `memory-bank/introduction_templates.md:55-60` | Apply for section-I structure and active-verb caption style. |
| `memory-bank/body_section_templates.md` | Body-section synthesis patterns (challenge-based and architecture-based exposition). | `memory-bank/body_section_templates.md:14`, `memory-bank/body_section_templates.md:21`, `memory-bank/body_section_templates.md:30` | Use for non-list tutorial survey rhetoric in technical body sections. |
| `writing_recipes/manifest.json` | Style asset index and usage workflow order. | `writing_recipes/manifest.json:89-117` | Use to resolve which template/recipe files are the intended writing stack. |
| `drafts/section6_20260217_143141/section_06_camera_ready.md` | Strong implicit in-manuscript anchor for current style: section-prefixed table numbering, notation table, "Key takeaways and open problems" endings. | `drafts/section6_20260217_143141/section_06_camera_ready.md:7-27`, `drafts/section6_20260217_143141/section_06_camera_ready.md:58`, `drafts/section6_20260217_143141/section_06_camera_ready.md:109-120` | Use as camera-ready style anchor for mature sections while template docs are being reconciled. |

## Style contradictions that affect usage

- Legacy organization text in style templates conflicts with current manuscript constitution:
  - `memory-bank/master_writing_guide.md:138-140`
  - `memory-bank/introduction_templates.md:38-40`
  - Current constitution: `drafts/section_01_introduction.md:163-179`

Practical rule: keep rhetorical/visual conventions from the stylekit, but take section numbering/order from `drafts/section_01_introduction.md` Section F.
