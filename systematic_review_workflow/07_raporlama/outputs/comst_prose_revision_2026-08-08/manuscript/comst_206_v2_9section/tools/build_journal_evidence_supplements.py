#!/usr/bin/env python3
"""Build journal-facing, sanitized evidence supplements from public projections.

This builder does not alter the locked Phase C--F authorities. It filters the
already sanitized public projections into publication-facing views and fails
closed when a denominator, identifier, join, or leakage gate is violated.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


BUILD_DATE = date(2026, 8, 13).isoformat()
V2_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = next(p for p in V2_ROOT.parents if p.name == "systematic_review_workflow")
PUBLIC_ROOT = (
    WORKFLOW
    / "07_raporlama"
    / "outputs"
    / "public_release_v1_0_0_staging_2026-08-07"
    / "OISAC_PRISMA_206_v1.0.0_DRAFT"
)
OUT = V2_ROOT / "supplements" / "evidence"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise RuntimeError(f"Missing header: {path}")
        return list(reader.fieldnames), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_unique(rows: list[dict[str, str]], field: str, expected: int) -> None:
    values = [row[field].strip() for row in rows]
    if len(rows) != expected or len(set(values)) != expected or "" in values:
        raise RuntimeError(
            f"Uniqueness gate failed for {field}: rows={len(rows)}, "
            f"unique={len(set(values))}, blanks={values.count('')}, expected={expected}"
        )


def find_leakage(paths: list[Path]) -> list[str]:
    patterns = [
        re.compile(r"[A-Za-z]:\\Users\\", re.I),
        re.compile(r"/Users/", re.I),
        re.compile(r"(?i)(?:password|credential|api[_ -]?key)\s*[:=]"),
    ]
    findings: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for pattern in patterns:
            if pattern.search(text):
                findings.append(f"{path.name}: {pattern.pattern}")
    return findings


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    source = {
        "studies": PUBLIC_ROOT / "data" / "included_studies_206_public.csv",
        "claims": PUBLIC_ROOT / "data" / "claim_governance_8306_public.csv",
        "evidence": PUBLIC_ROOT / "data" / "evidence_index_3041_public.csv",
        "metrics": PUBLIC_ROOT / "data" / "metric_results_4861_public.csv",
        "tradeoffs": PUBLIC_ROOT / "data" / "tradeoff_evidence_404_public.csv",
        "tqaf": PUBLIC_ROOT / "data" / "study_level_tqaf_206_public.csv",
        "bodies": PUBLIC_ROOT / "data" / "evidence_body_certainty_115_public.csv",
        "membership": PUBLIC_ROOT / "data" / "evidence_body_membership_4931_public.csv",
        "exclusions": PUBLIC_ROOT / "prisma" / "full_text_exclusions_39_public.csv",
    }
    for name, path in source.items():
        if not path.is_file():
            raise FileNotFoundError(f"Missing source {name}: {path}")

    study_fields, studies = read_csv(source["studies"])
    claim_fields, claims = read_csv(source["claims"])
    evidence_fields, evidence = read_csv(source["evidence"])
    metric_fields, metrics = read_csv(source["metrics"])
    trade_fields, tradeoffs = read_csv(source["tradeoffs"])
    tqaf_fields, tqaf = read_csv(source["tqaf"])
    body_fields, bodies = read_csv(source["bodies"])
    membership_fields, membership = read_csv(source["membership"])
    exclusion_fields, exclusions = read_csv(source["exclusions"])

    assert_unique(studies, "study_cluster_id", 206)
    study_ids = {row["study_cluster_id"] for row in studies}

    claim_by_record: dict[str, dict[str, str]] = {}
    for row in claims:
        key = row["record_id"]
        if key in claim_by_record:
            raise RuntimeError(f"Duplicate governed record ID: {key}")
        claim_by_record[key] = row
    if len(claim_by_record) != 8306:
        raise RuntimeError(f"Claim ledger expected 8306 unique rows, got {len(claim_by_record)}")

    governance_fields = [
        "claim_status",
        "survey_use_class",
        "comparison_admissibility",
        "cross_study_quantitative_comparison_allowed",
        "conflict_id",
        "reason_code",
        "independent_human_status",
        "source_workbook_sha256",
    ]
    evidence_primary: list[dict[str, str]] = []
    for row in evidence:
        governed = claim_by_record.get(row["evidence_id"])
        if governed is None or governed["record_type"] != "evidence":
            raise RuntimeError(f"Evidence row lacks governed match: {row['evidence_id']}")
        if governed["survey_use_class"] != "eligible_qualitative":
            continue
        joined = dict(row)
        for field in governance_fields:
            joined[field] = governed[field]
        evidence_primary.append(joined)

    metrics_primary = [
        row for row in metrics if row["final_survey_use_class"] == "eligible_quantitative"
    ]
    tradeoffs_substantive = [
        row for row in tradeoffs if row["reported_status"].strip().lower() != "absent"
    ]

    exclusion_citation_rows = []
    for row in exclusions:
        cited = dict(row)
        cited["citation_token"] = (
            f"https://doi.org/{row['doi']}" if row["doi"].strip() else row["citation"]
        )
        exclusion_citation_rows.append(cited)
    exclusion_citation_fields = exclusion_fields + ["citation_token"]

    outputs: list[tuple[str, list[str], list[dict[str, str]], str]] = [
        (
            "ST-16B_EXCLUDED_REPORTS_39.csv",
            exclusion_citation_fields,
            exclusion_citation_rows,
            "PRISMA Item 16b: 39 assessed full-text reports individually identified by DOI URL or full citation, with one primary reason.",
        ),
        (
            "ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv",
            evidence_fields + governance_fields,
            evidence_primary,
            "PRISMA Item 19 support: 3,020 primary qualitative evidence records.",
        ),
        (
            "ST-19_PRIMARY_METRIC_RESULTS_4779.csv",
            metric_fields,
            metrics_primary,
            "PRISMA Item 19 support: 4,779 primary quantitative metric records.",
        ),
        (
            "ST-19_GOVERNED_TRADEOFFS_404.csv",
            trade_fields,
            tradeoffs,
            "Governed tradeoff ledger: 404 rows, including two explicit absence audit sentinels.",
        ),
        (
            "ST-19_SUBSTANTIVE_TRADEOFFS_402.csv",
            trade_fields,
            tradeoffs_substantive,
            "Scientific tradeoff view: 402 source-supported rows after excluding two absence sentinels.",
        ),
        (
            "ST-18_STUDY_LEVEL_TQAF_206.csv",
            tqaf_fields,
            tqaf,
            "Review-specific eight-dimension TQAF projection; not a conventional risk-of-bias tool.",
        ),
        (
            "ST-22_EVIDENCE_BODY_CERTAINTY_115.csv",
            body_fields,
            bodies,
            "Review-defined certainty summaries for 115 evidence bodies.",
        ),
        (
            "ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv",
            membership_fields,
            membership,
            "Membership links connecting studies to the 115 review-defined evidence bodies.",
        ),
    ]

    generated: list[Path] = []
    descriptions: dict[str, str] = {}
    for filename, fields, rows, description in outputs:
        target = OUT / filename
        write_csv(target, fields, rows)
        generated.append(target)
        descriptions[filename] = description

    # Hard denominator and identity gates.
    assert_unique(exclusion_citation_rows, "screening_record_id", 39)
    if any(not row["citation_token"].strip() for row in exclusion_citation_rows):
        raise RuntimeError("Item 16b citation token is blank")
    assert_unique(evidence_primary, "evidence_id", 3020)
    assert_unique(metrics_primary, "metric_record_id", 4779)
    assert_unique(tradeoffs, "tradeoff_id", 404)
    assert_unique(tradeoffs_substantive, "tradeoff_id", 402)
    assert_unique(tqaf, "study_id", 206)
    assert_unique(bodies, "evidence_body_id", 115)
    if len(membership) != 4931:
        raise RuntimeError(f"Membership rows expected 4931, got {len(membership)}")

    row_study_ids = {
        row["study_cluster_id"]
        for rows in (evidence_primary, metrics_primary, tradeoffs, tradeoffs_substantive)
        for row in rows
    }
    if not row_study_ids <= study_ids:
        raise RuntimeError(f"Unknown study IDs in evidence carriers: {sorted(row_study_ids - study_ids)}")
    if {row["study_id"] for row in tqaf} != study_ids:
        raise RuntimeError("TQAF 206-study identifier set does not equal included-study set")
    body_ids = {row["evidence_body_id"] for row in bodies}
    if not {row["evidence_body_id"] for row in membership} <= body_ids:
        raise RuntimeError("Unknown evidence-body ID in membership carrier")
    if not {row["study_cluster_id"] for row in membership} <= study_ids:
        raise RuntimeError("Unknown study ID in evidence-body membership carrier")

    use_counts = Counter(row["final_survey_use_class"] for row in tradeoffs_substantive)
    admissibility_counts = Counter(
        row["final_comparison_admissibility"] for row in tradeoffs_substantive
    )
    if use_counts != Counter({"eligible_quantitative": 218, "eligible_qualitative": 184}):
        raise RuntimeError(f"Substantive tradeoff use-class mismatch: {dict(use_counts)}")
    if admissibility_counts != Counter(
        {"conditionally_comparable": 371, "descriptive_only": 31}
    ):
        raise RuntimeError(
            f"Substantive tradeoff admissibility mismatch: {dict(admissibility_counts)}"
        )
    if len({row["study_cluster_id"] for row in tradeoffs}) != 169:
        raise RuntimeError("Governed tradeoff study denominator is not 169")
    if len({row["study_cluster_id"] for row in tradeoffs_substantive}) != 168:
        raise RuntimeError("Substantive tradeoff study denominator is not 168")

    leakage = find_leakage(generated)
    if leakage:
        raise RuntimeError(f"Leakage gate failed: {leakage}")

    manifest = {
        "build_date": BUILD_DATE,
        "status": "PASS_MATERIALIZED_JOURNAL_EVIDENCE_CARRIERS",
        "scope": "sanitized evidence supplements; no publisher full text",
        "source_root": str(PUBLIC_ROOT.relative_to(WORKFLOW.parent)),
        "sources": {
            name: {
                "relative_path": str(path.relative_to(WORKFLOW.parent)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for name, path in source.items()
        },
        "outputs": [
            {
                "file": path.name,
                "rows": sum(1 for _ in path.open("r", encoding="utf-8-sig")) - 1,
                "sha256": sha256(path),
                "description": descriptions[path.name],
            }
            for path in generated
        ],
        "hard_gates": {
            "excluded_reports": 39,
            "primary_evidence_records": 3020,
            "primary_metric_records": 4779,
            "governed_tradeoffs": 404,
            "governed_tradeoff_studies": 169,
            "substantive_tradeoffs": 402,
            "substantive_tradeoff_studies": 168,
            "substantive_quantitative": 218,
            "substantive_qualitative": 184,
            "substantive_conditional": 371,
            "substantive_descriptive": 31,
            "tqaf_studies": 206,
            "evidence_bodies": 115,
            "body_memberships": 4931,
            "leakage_findings": 0,
        },
        "interpretation_limits": [
            "TQAF is review-specific and is not conventional risk of bias or GRADE.",
            "Metric rows are not independent effects and are not a meta-analytic sample.",
            "The 404-row governed tradeoff view includes two absence audit sentinels.",
            "The 402-row substantive tradeoff view excludes those sentinels.",
            "Draft manuscript packaging is not a public repository release.",
        ],
    }
    manifest_path = OUT / "SUPPLEMENT_MANIFEST_2026-08-13.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    readme_lines = [
        "# O-ISAC Journal Evidence Supplements",
        "",
        f"Generated: {BUILD_DATE}  ",
        "Status: materialized and denominator-QA-passed manuscript carriers; not a public repository release.",
        "",
        "These files preserve the study-level and claim-level evidence required for transparent reporting without turning the survey prose into a catalogue. They were deterministically filtered from the already sanitized public staging projections. No publisher PDF, restricted database export, local path, credential, or long source-derived passage is included.",
        "",
        "## Files",
        "",
    ]
    for path in generated:
        rows = sum(1 for _ in path.open("r", encoding="utf-8-sig")) - 1
        readme_lines.append(f"- `{path.name}` ({rows:,} rows): {descriptions[path.name]}")
    readme_lines += [
        "",
        "## Boundaries",
        "",
        "- The evidence and metric tables preserve source-reported values and existing governed classifications; they do not add graph digitization, imputed values, pooled effects, or a universal platform ranking.",
        "- The 404-row tradeoff file is the complete governed audit view. The 402-row file is the scientific view after removal of two rows whose `reported_status` is `absent`.",
        "- The TQAF table reports a deterministic, nonvalidated, review-specific technical appraisal. It must not be labelled risk of bias or GRADE.",
        "- Evidence bodies are review-defined synthesis units, not additional studies.",
        "- Study citations and 227-report lineage are materialized separately under ST-01.",
        "- A manuscript may cite these files as supplementary material after final package naming and journal upload, but it must not call them publicly available until a repository release exists.",
        "",
        "See `SUPPLEMENT_MANIFEST_2026-08-13.json` and `SHA256SUMS.txt` for row-count, provenance, and integrity gates.",
    ]
    readme_path = OUT / "README.md"
    readme_path.write_text("\n".join(readme_lines) + "\n", encoding="utf-8")

    checksum_targets = generated + [manifest_path, readme_path]
    checksum_path = OUT / "SHA256SUMS.txt"
    checksum_path.write_text(
        "".join(f"{sha256(path)}  {path.name}\n" for path in checksum_targets),
        encoding="ascii",
    )

    qa = {
        "status": "PASS",
        "output_directory": str(OUT),
        "output_csv_count": len(generated),
        "manifest": manifest_path.name,
        "checksum_manifest": checksum_path.name,
        "all_hard_gates_passed": True,
    }
    (V2_ROOT / "qa" / "JOURNAL_EVIDENCE_SUPPLEMENT_QA_2026-08-13.json").write_text(
        json.dumps(qa, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(qa, indent=2))


if __name__ == "__main__":
    main()
