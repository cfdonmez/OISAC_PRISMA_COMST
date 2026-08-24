from __future__ import annotations

import csv
import hashlib
import json
import shutil
from datetime import datetime
from pathlib import Path


V2 = Path(__file__).resolve().parents[1]
WORKFLOW = V2.parents[4]
STAGING = (
    WORKFLOW
    / "07_raporlama"
    / "outputs"
    / "public_release_v1_0_0_staging_2026-08-07"
    / "OISAC_PRISMA_206_v1.0.0_DRAFT"
)
OUT = V2 / "supplements" / "reporting"
SEARCH_OUT = OUT / "search"
PROTOCOL_OUT = OUT / "protocol"
QA_OUT = V2 / "qa" / "REPORTING_SUPPLEMENT_QA_2026-08-13.json"


SEARCH_FILES = [
    "README.md",
    "final_search_execution_log_2026-06-22.csv",
    "final_search_package_v1_2026-06-22.md",
    "scopus_final_search_summary_2026-06-22.md",
    "scopus_final_search_QA_report_2026-06-22.md",
    "ieee_final_search_summary_2026-06-22.md",
    "ieee_final_search_QA_report_2026-06-22.md",
    "sciencedirect_final_search_summary_2026-06-22.md",
    "sciencedirect_final_search_QA_report_2026-06-22.md",
    "springerlink_final_search_summary_2026-06-22.md",
    "springerlink_final_search_QA_report_2026-06-22.md",
    "wiley_final_search_summary_2026-06-22.md",
    "wiley_final_search_QA_report_2026-06-22.md",
    "taylorfrancis_final_search_summary_2026-06-22.md",
    "taylorfrancis_final_search_QA_report_2026-06-22.md",
    "supplementary_final_search_summary_2026-06-22.md",
]


PROTOCOL_FILES = [
    (STAGING / "protocol" / "protocol_initial_2026-06-17.md", "protocol_initial_2026-06-17.md"),
    (STAGING / "protocol" / "protocol_amendment_actual_workflow_2026-08-04.md", "protocol_amendment_actual_workflow_2026-08-04.md"),
    (STAGING / "protocol" / "protocol_registration_lineage_correction_2026-08-07.md", "protocol_registration_lineage_correction_2026-08-07.md"),
    (WORKFLOW / "01_protokol" / "05_contextual_synthesis_positioning_update_2026-08-13.md", "contextual_synthesis_positioning_update_2026-08-13.md"),
]


DEVIATIONS = [
    {
        "deviation_id": "DEV-01",
        "planned_or_legacy_state": "Prospective registration language appeared in frozen legacy materials.",
        "executed_state": "The OSF record was registered retrospectively on 12 February 2026 after searching and screening had been completed.",
        "reason": "The registration was created during synthesis and manuscript drafting.",
        "review_stage_identified": "Registration-lineage audit, 7 August 2026",
        "effect_on_results": "No change to locked scientific results; registration interpretation corrected.",
    },
    {
        "deviation_id": "DEV-02",
        "planned_or_legacy_state": "The frozen OSF state recorded a 30 November 2025 search and 221 included studies.",
        "executed_state": "The rebaselined review searched through 22 June 2026 and mapped 227 eligible reports to 206 studies.",
        "reason": "The source set, time window, report-to-study mapping, and denominators were rebaselined.",
        "review_stage_identified": "June to August 2026 rebaseline",
        "effect_on_results": "The 221 and 206 values are different states and must not be shown as attrition.",
    },
    {
        "deviation_id": "DEV-03",
        "planned_or_legacy_state": "Independent duplicate human review and third-reviewer arbitration were planned.",
        "executed_state": "The workflow was investigator supervised and claim governed; routine independent duplicate human review and third-reviewer arbitration were not performed.",
        "reason": "The executed workflow used recorded claim governance, deterministic QA, and investigator-authorized adjudication.",
        "review_stage_identified": "Actual-workflow audit, 4 August 2026",
        "effect_on_results": "Reviewer independence is reported as a review-process limitation; no interrater statistic is claimed.",
    },
    {
        "deviation_id": "DEV-04",
        "planned_or_legacy_state": "Two-assessor quality assessment and conventional bias language appeared in legacy plans.",
        "executed_state": "A deterministic review-specific eight-dimension TQAF was used; no conventional study-level risk-of-bias instrument was applied.",
        "reason": "The heterogeneous engineering evidence required technical evidence and reporting appraisal rather than a clinical RoB instrument.",
        "review_stage_identified": "Phase E appraisal implementation",
        "effect_on_results": "TQAF is reported separately and is not labelled RoB or GRADE.",
    },
    {
        "deviation_id": "DEV-05",
        "planned_or_legacy_state": "Qualitative publication-bias assessment and sensitivity checks were planned.",
        "executed_state": "No formal missing-results or publication-bias assessment and no formal sensitivity analysis were performed.",
        "reason": "The review had no common effect measure, pooled model, or harmonized prespecified outcome set.",
        "review_stage_identified": "Methods and synthesis closeout",
        "effect_on_results": "Selective reporting cannot be excluded; QA and invariance checks are not called sensitivity analysis.",
    },
    {
        "deviation_id": "DEV-06",
        "planned_or_legacy_state": "Cross-study rate-range-resolution scatter or frontier analysis was planned.",
        "executed_state": "The review synthesized condition-aware tradeoff records by family and did not estimate a universal frontier.",
        "reason": "Tasks, units, measurement planes, operating conditions, and validation settings were not commensurate.",
        "review_stage_identified": "Phase F synthesis",
        "effect_on_results": "Tradeoff conclusions remain conditional and no cross-platform ranking is reported.",
    },
    {
        "deviation_id": "DEV-07",
        "planned_or_legacy_state": "The planned search freeze was 30 June 2026.",
        "executed_state": "The executed cutoff was 22 June 2026.",
        "reason": "The user advanced the final search freeze on 22 June 2026.",
        "review_stage_identified": "Final search execution",
        "effect_on_results": "Eligibility and source reporting use 22 June 2026 consistently.",
    },
    {
        "deviation_id": "DEV-08",
        "planned_or_legacy_state": "The executed workflow contained 67 contextual records.",
        "executed_state": "A bounded manuscript-stage positioning audit added seven contextual syntheses outside the executed exports.",
        "reason": "The prior-survey comparison required fair coverage of relevant syntheses found during manuscript audit.",
        "review_stage_identified": "Manuscript positioning audit, 13 August 2026",
        "effect_on_results": "No primary denominator or technical result changed; the additions are contextual only.",
    },
]


BOUNDARY_TEXT = """# Review conduct and reporting boundaries

This publication supplement records the executed process rather than the
stronger procedures described in legacy plans.

- The review was investigator supervised and claim governed. Routine independent
  duplicate human screening, extraction, appraisal, and third-reviewer
  arbitration were not performed.
- Authors of included or unretrieved reports were not contacted.
- The review neither digitized graphs nor generated new performance values.
  Missing values were not inferred and conflicting values were not averaged.
- No common effect measure or pooled statistical model was used. The synthesis
  was structured, taxonomy based, metric governed, and narrative.
- Heterogeneity was described across modality, architecture, metric meaning,
  measurement plane, scenario, operating condition, and validation setting.
  No meta-regression or statistical heterogeneity estimate was performed.
- No conventional study-level risk-of-bias instrument was applied. The
  deterministic eight-dimension TQAF is a nonvalidated, review-specific
  technical evidence and reporting appraisal; it is not RoB or GRADE.
- No formal missing-results or publication-bias assessment and no formal
  sensitivity analysis were performed. Selective reporting cannot be excluded.
- The retrospective OSF record is a predecessor state. Its 221-study value is
  not an attrition parent of the final 206-study universe.
- Raw database exports and publisher PDFs are not redistributed because their
  redistribution rights were not established.
"""


README = """# O-ISAC review reporting supplement

Status: materialized journal-candidate supplement; not a public repository
release and not DOI-bearing.

This folder packages the review-authored search records, protocol and dated
amendments, a sanitized 446-row data dictionary, an explicit deviation table,
and conduct boundaries needed to interpret the nine-section survey. Scientific
counts remain governed by locked Phase C through F artifacts.

## Contents

- `search/`: six-source strategies, execution log, source summaries, and QA.
  Exact query-to-export mapping for two low-yield Taylor & Francis exports
  could not be reconstructed; the files preserve that limitation and no query
  was invented.
- `protocol/`: initial protocol plus dated executed-workflow, registration
  lineage, and contextual-positioning amendments.
- `S_PROTOCOL_DEVIATIONS_2026-08-13.csv`: change, rationale, review stage, and
  effect for eight material departures or lineage corrections.
- `S_DATA_DICTIONARY_446.csv`: sanitized field dictionary from the draft
  release staging package.
- `S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md`: concise executed-method and
  nonperformance statement.
- `MANIFEST.json` and `SHA256SUMS.txt`: file inventory and integrity hashes.

This carrier does not make the package public. Persistent repository, DOI,
rights, and license decisions remain separate author and release gates.
"""


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    SEARCH_OUT.mkdir(parents=True, exist_ok=True)
    PROTOCOL_OUT.mkdir(parents=True, exist_ok=True)

    copied: list[Path] = []
    for name in SEARCH_FILES:
        src = STAGING / "search" / name
        if not src.exists():
            raise FileNotFoundError(src)
        dst = SEARCH_OUT / name
        shutil.copyfile(src, dst)
        copied.append(dst)

    for src, name in PROTOCOL_FILES:
        if not src.exists():
            raise FileNotFoundError(src)
        dst = PROTOCOL_OUT / name
        shutil.copyfile(src, dst)
        copied.append(dst)

    dictionary_src = STAGING / "data" / "data_dictionary_446_public.csv"
    dictionary_dst = OUT / "S_DATA_DICTIONARY_446.csv"
    shutil.copyfile(dictionary_src, dictionary_dst)
    copied.append(dictionary_dst)

    deviations = OUT / "S_PROTOCOL_DEVIATIONS_2026-08-13.csv"
    with deviations.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(DEVIATIONS[0]))
        writer.writeheader()
        writer.writerows(DEVIATIONS)
    copied.append(deviations)

    boundary = OUT / "S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md"
    boundary.write_text(BOUNDARY_TEXT, encoding="utf-8")
    copied.append(boundary)

    readme = OUT / "README.md"
    readme.write_text(README, encoding="utf-8")
    copied.append(readme)

    with dictionary_dst.open("r", encoding="utf-8-sig", newline="") as f:
        dictionary_rows = sum(1 for _ in csv.DictReader(f))
    with deviations.open("r", encoding="utf-8-sig", newline="") as f:
        deviation_rows = sum(1 for _ in csv.DictReader(f))

    text_blob = "\n".join(
        p.read_text(encoding="utf-8-sig", errors="replace")
        for p in copied
        if p.suffix.lower() in {".md", ".csv"}
    )
    prohibited = ["C:\\Users\\", "file://", "chrome-extension://"]
    leaks = {needle: text_blob.count(needle) for needle in prohibited}

    hashes = []
    for p in sorted(copied, key=lambda x: x.relative_to(OUT).as_posix()):
        hashes.append(
            {
                "path": p.relative_to(OUT).as_posix(),
                "bytes": p.stat().st_size,
                "sha256": sha256(p),
            }
        )

    manifest = {
        "package": "OISAC_REVIEW_REPORTING_SUPPLEMENT_2026-08-13",
        "created": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "MATERIALIZED_NOT_PUBLICLY_RELEASED",
        "source_boundary": "Review-authored and sanitized files only; no raw database exports or publisher PDFs.",
        "files": hashes,
    }
    manifest_path = OUT / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    copied.append(manifest_path)

    sums = OUT / "SHA256SUMS.txt"
    sums.write_text(
        "".join(f"{sha256(p)}  {p.relative_to(OUT).as_posix()}\n" for p in sorted(copied, key=lambda x: x.relative_to(OUT).as_posix())),
        encoding="utf-8",
    )

    checks = {
        "qa_id": "REPORTING_SUPPLEMENT_QA_2026-08-13",
        "status": "PASS" if dictionary_rows == 446 and deviation_rows == 8 and not any(leaks.values()) else "FAIL",
        "search_files": len(SEARCH_FILES),
        "protocol_files": len(PROTOCOL_FILES),
        "data_dictionary_rows": dictionary_rows,
        "deviation_rows": deviation_rows,
        "unreconstructed_query_mappings": 2,
        "unreconstructed_query_source": "Taylor & Francis Online",
        "query_invention": False,
        "leak_counts": leaks,
        "public_release": False,
    }
    QA_OUT.write_text(json.dumps(checks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if checks["status"] != "PASS":
        raise SystemExit(json.dumps(checks, ensure_ascii=False))


if __name__ == "__main__":
    main()
