from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(rel_path: str) -> list[dict[str, str]]:
    path = ROOT / rel_path
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def find_row(rows: list[dict[str, str]], key: str, value: str) -> dict[str, str] | None:
    for row in rows:
        if row.get(key) == value:
            return row
    return None


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []

    flow = read_csv("screening/prisma_flow_counts.csv")
    require(len(flow) == 1, "Expected one PRISMA flow row.", failures)
    if flow:
        row = flow[0]
        expected_flow = {
            "databases_results": "980",
            "other_sources_results": "0",
            "duplicates_removed": "280",
            "records_screened": "700",
            "records_excluded_title": "478",
            "fulltext_assessed": "222",
            "fulltext_excluded": "2",
            "studies_included": "220",
        }
        for key, expected in expected_flow.items():
            require(row.get(key) == expected, f"Flow mismatch for {key}: expected {expected}, got {row.get(key)}.", failures)

    excluded = read_csv("screening/excluded_fulltext_log.csv")
    require(len(excluded) == 2, f"Expected 2 full-text exclusions, got {len(excluded)}.", failures)
    excluded_ids = {r["Track_ID"] for r in excluded}
    require({"O_ISAC_087", "O_ISAC_347"} <= excluded_ids, "Excluded full-text log must contain O_ISAC_087 and O_ISAC_347.", failures)

    included = read_csv("screening/included_studies_canonical.csv")
    included_ids = {r["track_id"] for r in included}
    require(len(included) == 220, f"Expected 220 included canonical rows, got {len(included)}.", failures)
    require("O_ISAC_347" not in included_ids, "O_ISAC_347 must not remain in the included canonical corpus.", failures)

    included_ledger = read_csv("screening/canonical_included_corpus_ledger.csv")
    require(len(included_ledger) == 220, f"Expected 220 included ledger rows, got {len(included_ledger)}.", failures)

    included_anomalies = read_csv("screening/canonical_included_corpus_anomalies.csv")
    require(len(included_anomalies) == 0, f"Expected 0 included-corpus anomalies, got {len(included_anomalies)}.", failures)

    assessed = read_csv("screening/fulltext_assessed_reconstruction.csv")
    require(len(assessed) == 222, f"Expected 222 full-text assessed rows, got {len(assessed)}.", failures)
    row_347 = find_row(assessed, "track_id", "O_ISAC_347")
    require(row_347 is not None, "O_ISAC_347 must remain in the assessed reconstruction.", failures)
    if row_347:
        require(row_347.get("present_in_final_corpus") == "no", "O_ISAC_347 must have present_in_final_corpus=no.", failures)
        require(row_347.get("present_in_excluded_fulltext_log") == "yes", "O_ISAC_347 must have present_in_excluded_fulltext_log=yes.", failures)

    assessed_anomalies = read_csv("screening/fulltext_assessed_anomalies.csv")
    require(len(assessed_anomalies) == 2, f"Expected 2 assessed anomalies, got {len(assessed_anomalies)}.", failures)
    require(find_row(assessed_anomalies, "track_id", "O_ISAC_044") is None, "O_ISAC_044 should no longer be in assessed anomalies.", failures)

    screening_log = read_csv("screening/screening_log.csv")
    row_347_log = find_row(screening_log, "record_id", "O_ISAC_347")
    require(row_347_log is not None, "O_ISAC_347 must remain in screening_log.", failures)
    if row_347_log:
        require(row_347_log.get("fulltext_decision") == "Excluded", "O_ISAC_347 screening_log fulltext_decision must be Excluded.", failures)
        require(row_347_log.get("is_final_included") == "no", "O_ISAC_347 screening_log is_final_included must be no.", failures)

    row_044_log = find_row(screening_log, "record_id", "O_ISAC_044")
    require(row_044_log is not None, "O_ISAC_044 must remain in screening_log.", failures)
    if row_044_log:
        require(row_044_log.get("present_in_retrieved_docs") == "yes", "O_ISAC_044 should now have present_in_retrieved_docs=yes.", failures)

    screening_anomalies = read_csv("screening/screening_log_anomalies.csv")
    require(len(screening_anomalies) == 6, f"Expected 6 screening anomalies, got {len(screening_anomalies)}.", failures)
    require(find_row(screening_anomalies, "record_id", "O_ISAC_044") is None, "O_ISAC_044 should no longer be in screening anomalies.", failures)

    extraction = read_csv("data/ext_v4_uni.csv")
    unique_oisac = {r["Paper_ID"] for r in extraction if r.get("Paper_ID", "").startswith("O_ISAC_")}
    require(len(unique_oisac) == 220, f"Expected 220 unique O_ISAC extraction rows, got {len(unique_oisac)}.", failures)
    require("O_ISAC_347" not in unique_oisac, "O_ISAC_347 must not remain in ext_v4_uni.csv.", failures)

    named_pdf = ROOT / "data/ret_docs/O_ISAC_044.pdf"
    require(named_pdf.exists(), "Expected named PDF alias data/ret_docs/O_ISAC_044.pdf.", failures)

    identification_reconstruction = read_csv("search/formal_identification_reconstruction_20251130.csv")
    upstream_reconstruction = read_csv("search/upstream_prisma_reconstruction_20260310.csv")
    inferred_timeline = read_csv("search/inferred_freeze_provenance_timeline_20260310.csv")
    reconstructed_note = ROOT / "search/reconstructed_freeze_bundle_note_20260310.md"
    inferred_note = ROOT / "search/inferred_freeze_provenance_from_memory_bank_20260310.md"
    require(len(identification_reconstruction) == 3, f"Expected 3 source rows in formal identification reconstruction, got {len(identification_reconstruction)}.", failures)
    require(len(upstream_reconstruction) == 7, f"Expected 7 upstream PRISMA reconstruction rows, got {len(upstream_reconstruction)}.", failures)
    require(len(inferred_timeline) == 7, f"Expected 7 inferred provenance rows, got {len(inferred_timeline)}.", failures)
    require(reconstructed_note.exists(), "Expected search/reconstructed_freeze_bundle_note_20260310.md.", failures)
    require(inferred_note.exists(), "Expected search/inferred_freeze_provenance_from_memory_bank_20260310.md.", failures)
    require(find_row(inferred_timeline, "evidence_id", "MB1") is not None, "Expected MB1 in inferred provenance timeline.", failures)
    require(find_row(inferred_timeline, "evidence_id", "RV4") is not None, "Expected RV4 in inferred provenance timeline.", failures)

    conflict_rows = read_csv("screening/external/ieee_511_conflicts_vs_canonical.csv")
    triage_rows = read_csv("screening/external/ieee_511_conflict_triage_20260310.csv")
    decision_rows = read_csv("screening/external/ieee_511_conflict_decisions_20260310.csv")
    require(len(conflict_rows) == 17, f"Expected 17 external conflict rows, got {len(conflict_rows)}.", failures)
    require(len(triage_rows) == 17, f"Expected 17 conflict triage rows, got {len(triage_rows)}.", failures)
    require(len(decision_rows) == 17, f"Expected 17 conflict decision rows, got {len(decision_rows)}.", failures)
    status_counts = Counter(r["reconciliation_status"] for r in conflict_rows)
    require(status_counts == Counter({
        "resolved_retain_canonical": 9,
        "whole_manuscript_rebaseline_candidate_remove": 4,
        "whole_manuscript_rebaseline_candidate_contextualize": 4,
    }), f"Unexpected external conflict status distribution: {dict(status_counts)}.", failures)

    script_summary = {
        "included_rows": len(included),
        "assessed_rows": len(assessed),
        "excluded_rows": len(excluded),
        "identification_reconstruction_rows": len(identification_reconstruction),
        "upstream_reconstruction_rows": len(upstream_reconstruction),
        "inferred_provenance_rows": len(inferred_timeline),
        "included_anomalies": len(included_anomalies),
        "assessed_anomalies": len(assessed_anomalies),
        "screening_anomalies": len(screening_anomalies),
        "external_conflicts": len(conflict_rows),
    }

    if failures:
        print("SECTION III VALIDATION: FAIL")
        for failure in failures:
            print(f"- {failure}")
        print(f"Summary: {script_summary}")
        return 1

    print("SECTION III VALIDATION: PASS")
    print(f"Summary: {script_summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
