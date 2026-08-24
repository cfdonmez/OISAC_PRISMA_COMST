from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"
QA = ROOT / "qa"

EXPECTED_SECTIONS = [
    "00_ABSTRACT.tex",
    "01_INTRODUCTION.tex",
    "02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex",
    "03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex",
    "04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex",
    "05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex",
    "06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex",
    "07_ENABLING_TECHNOLOGIES_APPLICATIONS_AND_6G.tex",
    "08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex",
    "09_CONCLUSION.tex",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def active_tex(text: str) -> str:
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith("%"):
            continue
        line = re.sub(r"(?<!\\)%.*$", "", line)
        out.append(line)
    return "\n".join(out)


def bib_keys(path: Path) -> list[str]:
    return re.findall(r"(?im)^\s*@\w+\s*\{\s*([^,\s]+)\s*,", read(path))


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def check(checks: list[dict], check_id: str, condition: bool, observed, expected, note=""):
    checks.append(
        {
            "id": check_id,
            "status": "PASS" if condition else "FAIL",
            "observed": observed,
            "expected": expected,
            "note": note,
        }
    )


def unique(rows: list[dict[str, str]], field: str) -> int:
    return len({row[field].strip() for row in rows if row.get(field, "").strip()})


def main() -> None:
    checks: list[dict] = []
    section_paths = [SECTIONS / name for name in EXPECTED_SECTIONS]
    check(checks, "section_files", all(p.exists() for p in section_paths),
          [p.name for p in section_paths if p.exists()], EXPECTED_SECTIONS)

    texts = {p.name: read(p) for p in section_paths}
    active = {name: active_tex(text) for name, text in texts.items()}
    main_section_count = sum(len(re.findall(r"(?m)^\\section\{", text)) for text in active.values())
    check(checks, "main_section_count", main_section_count == 9, main_section_count, 9)

    abstract_match = re.search(
        r"(?s)\\begin\{abstract\}(.*?)\\end\{abstract\}", texts["00_ABSTRACT.tex"]
    )
    abstract = abstract_match.group(1) if abstract_match else ""
    abstract_plain = abstract.replace(r"\&", "and")
    abstract_plain = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?", " ", abstract_plain)
    abstract_plain = re.sub(r"[{}]", " ", abstract_plain)
    abstract_words = re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", abstract_plain)
    check(
        checks,
        "abstract_word_limit",
        150 <= len(abstract_words) <= 250,
        len(abstract_words),
        "150-250",
        "IEEE permits a range; the audit must not force the abstract to the maximum.",
    )
    all_active_text = "\n".join(active.values())
    check(
        checks,
        "tqaf_canonical_name",
        bool(re.search(r"Technical\s+Quality\s+Assessment\s+Framework", all_active_text))
        and not re.search(r"Technical\s+Quality\s+Appraisal\s+Framework", all_active_text),
        "Assessment"
        if re.search(r"Technical\s+Quality\s+Assessment\s+Framework", all_active_text)
        else "other",
        "Technical Quality Assessment Framework",
    )

    study_bib = bib_keys(ROOT / "references_206_candidate.bib")
    context_bib = bib_keys(ROOT / "references_context_candidate.bib")
    all_bib = set(study_bib) | set(context_bib)
    dup_bib = sorted(k for k, n in Counter(study_bib + context_bib).items() if n > 1)
    check(checks, "study_bibliography", len(study_bib) == 206 and len(set(study_bib)) == 206,
          {"entries": len(study_bib), "unique": len(set(study_bib))}, 206)
    check(checks, "duplicate_bib_keys", not dup_bib, dup_bib, [])

    section_citations: list[str] = []
    labels: list[str] = []
    refs: list[str] = []
    brace_failures: list[str] = []
    environment_failures: list[str] = []
    for name, text in active.items():
        for group in re.findall(r"\\cite\w*\{([^}]*)\}", text):
            section_citations.extend(k.strip() for k in group.split(",") if k.strip())
        labels.extend(re.findall(r"\\label\{([^}]*)\}", text))
        refs.extend(re.findall(r"\\(?:ref|eqref|autoref)\{([^}]*)\}", text))
        if text.count("{") != text.count("}"):
            brace_failures.append(name)
        begins = Counter(re.findall(r"\\begin\{([^}]*)\}", text))
        ends = Counter(re.findall(r"\\end\{([^}]*)\}", text))
        if begins != ends:
            environment_failures.append(name)

    missing_citations = sorted(set(section_citations) - all_bib)
    duplicate_labels = sorted(k for k, n in Counter(labels).items() if n > 1)
    missing_refs = sorted(set(refs) - set(labels))
    check(checks, "section_citations_resolve", not missing_citations, missing_citations, [])
    check(checks, "duplicate_labels", not duplicate_labels, duplicate_labels, [])
    check(checks, "cross_references_resolve", not missing_refs, missing_refs, [])
    check(checks, "brace_balance", not brace_failures, brace_failures, [])
    check(checks, "environment_balance", not environment_failures, environment_failures, [])

    st01 = csv_rows(ROOT / "supplements/st01/ST01_INCLUDED_STUDIES_206.csv")
    lineage = csv_rows(ROOT / "supplements/st01/ST01_ELIGIBLE_REPORT_LINEAGE_227.csv")
    st01_tex = active_tex(read(ROOT / "supplements/st01/ST01_INCLUDED_STUDIES_206.tex"))
    st01_cites = []
    for group in re.findall(r"\\cite\w*\{([^}]*)\}", st01_tex):
        st01_cites.extend(k.strip() for k in group.split(",") if k.strip())
    explicit = active_tex(read(ROOT / "supplements/st01/INCLUDED_STUDIES_206_EXPLICIT_BIBLIOGRAPHY.tex"))
    explicit_keys = []
    for group in re.findall(r"\\nocite\{([^}]*)\}", explicit):
        explicit_keys.extend(k.strip() for k in group.split(",") if k.strip())
    st01_keys = {r["citation_key"].strip() for r in st01}
    check(
        checks,
        "item17_st01",
        len(st01) == unique(st01, "study_id") == unique(st01, "citation_key") == 206
        and set(st01_cites) == st01_keys == set(study_bib),
        {"rows": len(st01), "studies": unique(st01, "study_id"),
         "keys": unique(st01, "citation_key"), "row_citations": len(set(st01_cites))},
        {"rows": 206, "studies": 206, "keys": 206, "row_citations": 206},
    )
    check(
        checks,
        "explicit_bibliography_inclusion",
        len(explicit_keys) == len(set(explicit_keys)) == 206
        and set(explicit_keys) == set(study_bib) and "*" not in explicit_keys,
        {"keys": len(explicit_keys), "unique": len(set(explicit_keys)), "wildcard": "*" in explicit_keys},
        {"keys": 206, "unique": 206, "wildcard": False},
    )
    check(
        checks,
        "eligible_report_lineage",
        len(lineage) == unique(lineage, "report_id") == 227
        and unique(lineage, "study_id") == 206,
        {"rows": len(lineage), "reports": unique(lineage, "report_id"),
         "studies": unique(lineage, "study_id")},
        {"rows": 227, "reports": 227, "studies": 206},
    )

    csv_contracts = [
        ("excluded_reports", "supplements/evidence/ST-16B_EXCLUDED_REPORTS_39.csv", 39, "screening_record_id"),
        ("primary_evidence", "supplements/evidence/ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv", 3020, "evidence_id"),
        ("primary_metrics", "supplements/evidence/ST-19_PRIMARY_METRIC_RESULTS_4779.csv", 4779, "metric_record_id"),
        ("governed_tradeoffs", "supplements/evidence/ST-19_GOVERNED_TRADEOFFS_404.csv", 404, "tradeoff_id"),
        ("substantive_tradeoffs", "supplements/evidence/ST-19_SUBSTANTIVE_TRADEOFFS_402.csv", 402, "tradeoff_id"),
        ("study_tqaf", "supplements/evidence/ST-18_STUDY_LEVEL_TQAF_206.csv", 206, "study_id"),
        ("evidence_bodies", "supplements/evidence/ST-22_EVIDENCE_BODY_CERTAINTY_115.csv", 115, "evidence_body_id"),
        ("evidence_memberships", "supplements/evidence/ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv", 4931, ""),
        ("contextual_syntheses", "supplements/related_synthesis/ST-RS1_CONTEXTUAL_SYNTHESES_38.csv", 38, "citation_key"),
        ("s7_join", "supplements/s7/S7_CANONICAL_JOIN_206.csv", 206, "study_id"),
        ("s7_field_subset", "supplements/s7/S7_PAIRED_FUNCTION_VALIDATION_12.csv", 12, "study_id"),
    ]
    for check_id, rel, expected, key in csv_contracts:
        rows = csv_rows(ROOT / rel)
        condition = len(rows) == expected and (not key or unique(rows, key) == expected)
        check(checks, check_id, condition,
              {"rows": len(rows), "unique": unique(rows, key) if key else "not_applicable"},
              {"rows": expected, "unique": expected if key else "not_applicable"})

    substantive = csv_rows(ROOT / "supplements/evidence/ST-19_SUBSTANTIVE_TRADEOFFS_402.csv")
    governed = csv_rows(ROOT / "supplements/evidence/ST-19_GOVERNED_TRADEOFFS_404.csv")
    check(
        checks,
        "tradeoff_lineage",
        unique(governed, "study_cluster_id") == 169
        and unique(substantive, "study_cluster_id") == 168
        and sum(r["reported_status"].strip().lower() == "absent" for r in governed) == 2
        and not any(r["reported_status"].strip().lower() == "absent" for r in substantive),
        {"governed_studies": unique(governed, "study_cluster_id"),
         "substantive_studies": unique(substantive, "study_cluster_id"),
         "governed_absent": sum(r["reported_status"].strip().lower() == "absent" for r in governed),
         "substantive_absent": sum(r["reported_status"].strip().lower() == "absent" for r in substantive)},
        {"governed_studies": 169, "substantive_studies": 168,
         "governed_absent": 2, "substantive_absent": 0},
    )

    s7 = csv_rows(ROOT / "supplements/s7/S7_PAIRED_FUNCTION_VALIDATION_12.csv")
    paired = sum(r["paired_function_evidence_subset"].strip().lower() in {"1", "true", "yes"} for r in s7)
    check(checks, "s7_paired_subset", paired == 6, paired, 6)

    body_manifest = read(ROOT / "MANUSCRIPT_BODY_INPUTS.tex")
    st01_driver = read(ROOT / "supplements/st01/ST01_SUPPLEMENT_DRIVER.tex")
    check(
        checks,
        "standalone_item17_integration",
        "ST01_INCLUDED_STUDIES_206.tex" in st01_driver
        and "ST01_REFERENCES_206" in st01_driver
        and "INCLUDED_STUDIES_206_EXPLICIT_BIBLIOGRAPHY.tex" not in body_manifest,
        {
            "study_table": "present" if "ST01_INCLUDED_STUDIES_206.tex" in st01_driver else "absent",
            "bibliography": "present" if "ST01_REFERENCES_206" in st01_driver else "absent",
            "forced_main_bibliography": "absent" if "INCLUDED_STUDIES_206_EXPLICIT_BIBLIOGRAPHY.tex" not in body_manifest else "present",
        },
        {"study_table": "present", "bibliography": "present", "forced_main_bibliography": "absent"},
    )

    active_docs = "\n".join(
        read(ROOT / name)
        for name in [
            "README.md",
            "00_SCOPE_AND_SOURCE_MANIFEST.md",
            "03_SUPPLEMENTARY_EVIDENCE_CONTRACT.md",
            "MANUSCRIPT_STRUCTURE.json",
        ]
    ) + "\n" + "\n".join(active.values())
    stale_patterns = {
        "item17_open": r"(?i)item\s*17[^\n]*(?:open|76\s*(?:/|of)\s*206)",
        "st01_pending": r"(?i)journal label and packaging as ST-01[^\n]*future/pending",
        "metric_pending": r"(?i)4,779-row primary publication projection[^\n]*future/pending",
        "tradeoff_pending": r"(?i)402-row substantive publication view[^\n]*future/pending",
        "tqaf_pending": r"(?i)journal packaging[^\n]*future/pending",
        "unregistered": r"(?i)not externally registered",
        "tqaf_wrong_name": r"Technical Quality Appraisal Framework",
    }
    stale_hits = {name: bool(re.search(pattern, active_docs)) for name, pattern in stale_patterns.items()}
    check(checks, "active_state_not_stale", not any(stale_hits.values()), stale_hits,
          {name: False for name in stale_patterns})

    prohibited = []
    for name, text in active.items():
        for pattern in [r"(?i)\bfirst (?:O-ISAC )?(?:survey|review)\b",
                        r"(?i)\bonly (?:O-ISAC )?(?:survey|review)\b",
                        r"(?i)\bmost comprehensive\b"]:
            if re.search(pattern, text):
                prohibited.append({"file": name, "pattern": pattern})
    check(checks, "novelty_overclaim", not prohibited, prohibited, [])

    actual_tables = sum(len(re.findall(r"\\begin\{table\*?\}", t)) for t in active.values())
    actual_figures = sum(len(re.findall(r"\\begin\{figure\*?\}", t)) for t in active.values())
    check(checks, "live_visual_truth", actual_tables == 9 and actual_figures == 0,
          {"table_environments": actual_tables, "logical_tables": len({x for x in labels if x.startswith('tab:')}), "figures": actual_figures},
          {"table_environments": 9, "logical_tables": 8, "figures": 0},
          "Tables I-VIII are live; Table VII uses two table environments, and Figures 1-8 remain specifications only.")

    required_qa = [
        "FINAL_PRISMA_ITEM17_QA.json",
        "FINAL_PRISMA_ITEM17_WORKBOOK_QA.json",
        "JOURNAL_EVIDENCE_SUPPLEMENT_QA_2026-08-13.json",
        "JOURNAL_EVIDENCE_WORKBOOK_QA_2026-08-13.json",
        "REPORTING_SUPPLEMENT_QA_2026-08-13.json",
        "FINAL_ST_RS1_CONTEXTUAL_SYNTHESIS_QA_2026-08-13.json",
        "FINAL_ST_RS1_WORKBOOK_QA_2026-08-13.json",
        "FINAL_SUPPLEMENT_S7_PAIRED_FUNCTION_QA_2026-08-13.json",
        "FINAL_SUPPLEMENT_S7_WORKBOOK_QA_2026-08-13.json",
        "MANUSCRIPT_CLAIM_REAUDIT_2026-08-13.json",
        "FRONT_MATTER_RELEASE_REAUDIT_2026-08-13.json",
    ]
    check(checks, "required_component_qa", all((QA / f).exists() for f in required_qa),
          [f for f in required_qa if (QA / f).exists()], required_qa)

    hard_failures = [c for c in checks if c["status"] == "FAIL"]
    status = "PASS_NONVISUAL_CLOSEOUT_FIGURES_ONLY" if not hard_failures else "FAIL"
    output = {
        "audit_id": "OISAC_COMST_V2_POSTFIX_INTEGRATED_QA_2026-08-13",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "interpretation": (
            "PASS means the compiled local manuscript, direct-citation bibliography, eight live "
            "tables, standalone 206-study supplement, and other materialized supplements satisfy "
            "the tested nonvisual gates. Figures 1-8 and their post-insertion page-budget check "
            "remain; portal attestations and a public persistent release are external actions."
        ),
        "counts": {
            "main_sections": main_section_count,
            "abstract_words": len(abstract_words),
            "study_bib_entries": len(study_bib),
            "context_bib_entries": len(context_bib),
            "unique_section_citation_keys": len(set(section_citations)),
            "live_tables": actual_tables,
            "live_figures": actual_figures,
        },
        "checks": checks,
        "hard_failures": hard_failures,
        "remaining_nonlocal_gates": [
            "Production, insertion, and rendered inspection of Figures 1-8.",
            "Post-figure verification against the 30-page COMST submission limit.",
            "Author portal attestations and final upload actions.",
            "Optional public repository release, persistent URL, and archive DOI.",
        ],
        "key_hashes": {
            "abstract": sha256(SECTIONS / "00_ABSTRACT.tex"),
            "st01_csv": sha256(ROOT / "supplements/st01/ST01_INCLUDED_STUDIES_206.csv"),
            "lineage_227_csv": sha256(ROOT / "supplements/st01/ST01_ELIGIBLE_REPORT_LINEAGE_227.csv"),
            "evidence_workbook": sha256(ROOT / "supplements/evidence/OISAC_JOURNAL_EVIDENCE_SUPPLEMENTS_2026-08-13.xlsx"),
        },
    }
    json_path = QA / "POSTFIX_INTEGRATED_QA_2026-08-13.json"
    json_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Post-fix Integrated QA — 2026-08-13",
        "",
        f"Status: `{status}`",
        "",
        output["interpretation"],
        "",
        "## Tested gates",
        "",
        "| Gate | Status | Observed | Expected |",
        "| --- | --- | --- | --- |",
    ]
    for item in checks:
        observed = json.dumps(item["observed"], ensure_ascii=False)
        expected = json.dumps(item["expected"], ensure_ascii=False)
        lines.append(f"| {item['id']} | {item['status']} | `{observed}` | `{expected}` |")
    lines.extend(["", "## Remaining gates", ""])
    lines.extend(f"- {item}" for item in output["remaining_nonlocal_gates"])
    lines.extend([
        "",
        "The pre-fix PRISMA and architecture reports remain historical snapshots. Their",
        "old 76/206 citation-coverage and pending-supplement observations must not be",
        "used as the current candidate state. `MANUSCRIPT_STRUCTURE.json` and the root",
        "README now point to this post-fix gate and the post-fix PRISMA matrix.",
        "",
    ])
    (QA / "POSTFIX_INTEGRATED_QA_2026-08-13.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"status": status, "failures": len(hard_failures), "checks": len(checks)}, indent=2))


if __name__ == "__main__":
    main()
