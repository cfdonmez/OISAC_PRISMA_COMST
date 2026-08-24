"""Build ST-RS1 and Supplement S7 from audited local authorities.

The script does not edit manuscript section TeX files.  It materializes two
bounded publication-facing data carriers plus machine-readable QA records.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve()
V2 = HERE.parents[1]
REPO = HERE.parents[7]

DEDUP = REPO / "systematic_review_workflow/03_secim/deduplication/final_2026-06-22/deduplicated_records_for_title_abstract_screening_APPROVED_2026-06-22.csv"
BIB = V2 / "references_context_candidate.bib"
ST01 = V2 / "supplements/st01/ST01_INCLUDED_STUDIES_206.csv"
TQAF = V2 / "supplements/evidence/ST-18_STUDY_LEVEL_TQAF_206.csv"
TQAF_AUDIT = REPO / "systematic_review_workflow/05_kalite_kanit/phase_e_tqaf_dimension_audit_2026-08-04.csv"

RS_DIR = V2 / "supplements/related_synthesis"
S7_DIR = V2 / "supplements/s7"
QA_DIR = V2 / "qa"

F_ARCH = "architecture_and_system_design"
F_ANALYTIC = "analytical_limits_and_estimation_methods"
F_EVOLUTION = "technological_evolution_standardization_and_deployment"
F_PHYSICAL = "physical_media_and_optical_networks"
F_WAVEFORM = "waveforms_resource_multiplexing_and_photonic_hardware"
F_APPLICATION = "applications_and_challenges_across_platforms"

AMENDMENT = "contextual_synthesis_positioning_update_2026-08-13"
OUTSIDE = "contextual_only_outside_locked_206_study_primary_denominator"

EXPECTED_TABLE_I_KEYS = {
    "Wen2024OISACArchitectures", "Su2025OISACTheoryPractice", "Chu2025ROISACOverview", "Wang2026CrossLayerISACoF",
    "Khorasgani2026GeneralOpticalISACSurvey", "Rode2025PolarizationISAC",
    "Zhang2026ISACEvolution", "Liu2025OpticalNetworkISACProspect", "Cao2026SubmarineFiberISAC", "Zhang2026OpticalTransmissionNetworks", "Ip2026DeployedTelecomCableISAC",
    "Liang2024LiSACReview", "Zhang2023OpticalNetworkISACFrontier", "He2025FiberISACAdvances", "Liu2026OpticalFiberISACReview", "Lu2026ConvergedFiberISACReview", "Wang2026FiberNetworkISAC",
    "Yang2025DSCMISACReview", "He2026PhotonicFiberISAC", "Yu2023PhotonAssistedTHz", "Bai2025MicrowavePhotonicsISAC", "Wang2025MicrowavePhotonicsISAC", "Lyu2026PhotonicTHzWaveforms",
    "Mohsan2026OISACReview",
}

EXPECTED_SHORT_KEYS = {
    "Yang2025ForwardVibrationOverview", "Zhang2025PhotonicTHzOverview", "Huang2026OPALiDAROverview",
    "Liu2025SeamlessFiberFSOOverview", "Wang2025OpticalFiberNetworksOverview", "Wu2024FiberISACOverview",
    "Yan2023OpticalTransmissionReview", "Boffi2025AccessMonitoringOverview", "Salem2024VisibleLightProspects",
    "Rosmaninho2025ModulationStrategies", "Yu2023THzPhotonicsOverview", "Chen2025ROISACProgress",
    "Lu2024IntegratedOpticalCommSensingOverview", "Lu2025IntegratedOpticalCommSensingOverview",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def norm_doi(value: str) -> str:
    return value.strip().lower().removeprefix("https://doi.org/").removeprefix("doi:")


def norm_title(value: str) -> str:
    value = re.sub(r"[{}]", "", value)
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def row_has_leakage(row: dict[str, object]) -> bool:
    text = " | ".join(str(value) for value in row.values())
    return bool(re.search(r"(?:[A-Za-z]:\\|/Users/|/home/|file://|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,})", text, re.I))


def parse_bib(path: Path) -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    current_key: str | None = None
    current: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        start = re.match(r"\s*@\w+\{([^,]+),", raw)
        if start:
            if current_key:
                entries[current_key] = current
            current_key = start.group(1).strip()
            current = {}
            continue
        if current_key:
            field = re.match(r"\s*(\w+)\s*=\s*\{(.*)\},?\s*$", raw)
            if field:
                current[field.group(1).lower()] = field.group(2).strip()
    if current_key:
        entries[current_key] = current
    return entries


# Captured records are keyed to the exact citation keys used by Table I or the
# new short/focused bibliography entries.  Primary-family assignments for the
# 24 full-length records reproduce the audited Table-I reconciliation.
CAPTURED: dict[str, dict[str, str]] = {
    "SCR-00005": {"key": "Mohsan2026OISACReview", "form": "full_length_or_independently_citable", "family": F_APPLICATION, "secondary": "architecture_and_system_design; waveforms_and_resource_design; future_directions", "scope": "O-ISAC; multi_platform; applications; challenges", "medium": "multi_platform_optical"},
    "SCR-00006": {"key": "Khorasgani2026GeneralOpticalISACSurvey", "form": "full_length_or_independently_citable", "family": F_ANALYTIC, "secondary": "architecture_and_system_design; future_directions", "scope": "general_ISAC; optical_ISAC; information_theoretic_limits; estimators", "medium": "FSO_and_general_optical"},
    "SCR-00040": {"key": "Bai2025MicrowavePhotonicsISAC", "form": "full_length_or_independently_citable", "family": F_WAVEFORM, "secondary": "architecture_and_system_design; applications_and_challenges", "scope": "microwave_photonics; resource_multiplexing; integrated_waveforms", "medium": "photonic_assisted_RF_THz"},
    "SCR-00266": {"key": "He2025FiberISACAdvances", "form": "full_length_or_independently_citable", "family": F_PHYSICAL, "secondary": "waveforms_and_resource_design; deployment_and_operations", "scope": "fiber_ISAC; forward_sensing; backscatter_sensing; network_operations", "medium": "optical_fiber_networks"},
    "SCR-00292": {"key": "Liu2026OpticalFiberISACReview", "form": "full_length_or_independently_citable", "family": F_PHYSICAL, "secondary": "architecture_and_system_design; deployment_and_operations", "scope": "fiber_ISAC; distributed_sensing; optical_networks", "medium": "optical_fiber_networks"},
    "SCR-00309": {"key": "Rode2025PolarizationISAC", "form": "full_length_or_independently_citable", "family": F_ANALYTIC, "secondary": "physical_media_and_networks; machine_learning_methods", "scope": "polarization_sensing; machine_learning; fiber", "medium": "optical_fiber"},
    "SCR-00358": {"key": "Cao2026SubmarineFiberISAC", "form": "full_length_or_independently_citable", "family": F_EVOLUTION, "secondary": "physical_media_and_networks; applications_and_challenges", "scope": "submarine_fiber; environmental_monitoring; deployment", "medium": "submarine_optical_fiber"},
    "SCR-00371": {"key": "Wang2026FiberNetworkISAC", "form": "full_length_or_independently_citable", "family": F_PHYSICAL, "secondary": "architecture_and_system_design; applications_and_challenges", "scope": "fiber_ISAC; optical_networks; principles; challenges", "medium": "optical_fiber_networks"},
    "SCR-00395": {"key": "Yang2025DSCMISACReview", "form": "full_length_or_independently_citable", "family": F_WAVEFORM, "secondary": "architecture_and_system_design; physical_media_and_networks", "scope": "digital_subcarrier_multiplexing; vibration_sensing; fiber", "medium": "optical_fiber"},
    "SCR-00565": {"key": "Liang2024LiSACReview", "form": "full_length_or_independently_citable", "family": F_PHYSICAL, "secondary": "applications_and_challenges; waveforms_and_resource_design", "scope": "visible_light; lighting; communication; sensing", "medium": "VLC_LiFi"},
    "SCR-00672": {"key": "Yu2023PhotonAssistedTHz", "form": "full_length_or_independently_citable", "family": F_WAVEFORM, "secondary": "architecture_and_system_design; applications_and_challenges", "scope": "photon_assisted_THz; communication; sensing", "medium": "photonic_THz"},
    "SCR-00911": {"key": "Wen2024OISACArchitectures", "form": "full_length_or_independently_citable", "family": F_ARCH, "secondary": "applications_and_challenges; multi_platform_taxonomy", "scope": "O-ISAC; architectures; potentials; challenges", "medium": "multi_platform_optical"},
    "SCR-00928": {"key": "Zhang2026ISACEvolution", "form": "full_length_or_independently_citable", "family": F_EVOLUTION, "secondary": "standardization_context; future_directions", "scope": "general_ISAC_evolution; optical_positioning_context", "medium": "general_ISAC_with_optical_context"},
    "SCR-00960": {"key": "Wang2026CrossLayerISACoF", "form": "full_length_or_independently_citable", "family": F_ARCH, "secondary": "physical_media_and_networks; deployment_and_operations", "scope": "fiber_ISAC; cross_layer; long_haul; short_reach", "medium": "optical_fiber_networks"},
    "SCR-00962": {"key": "He2026PhotonicFiberISAC", "form": "full_length_or_independently_citable", "family": F_WAVEFORM, "secondary": "architecture_and_system_design; applications_and_challenges", "scope": "fiber_photonics; enabling_technologies; integration", "medium": "optical_fiber"},
    "SCR-00968": {"key": "Wang2025MicrowavePhotonicsISAC", "form": "full_length_or_independently_citable", "family": F_WAVEFORM, "secondary": "applications_and_challenges; 6G_context", "scope": "microwave_photonics; 6G; sensing_and_communication", "medium": "photonic_assisted_RF_THz"},
    "SCR-00971": {"key": "Zhang2026OpticalTransmissionNetworks", "form": "full_length_or_independently_citable", "family": F_EVOLUTION, "secondary": "physical_media_and_networks; architecture_and_system_design", "scope": "optical_transmission_networks; deployment; integration", "medium": "optical_fiber_networks"},
    "SCR-00982": {"key": "Lyu2026PhotonicTHzWaveforms", "form": "full_length_or_independently_citable", "family": F_WAVEFORM, "secondary": "architecture_and_system_design; performance_comparison", "scope": "photonic_THz; integrated_waveforms", "medium": "photonic_THz"},
    "SCR-01177": {"key": "Lu2026ConvergedFiberISACReview", "form": "full_length_or_independently_citable", "family": F_PHYSICAL, "secondary": "architecture_and_system_design; technological_evolution", "scope": "converged_networks; fiber_sensing; communication", "medium": "optical_fiber_networks"},
    "SCR-01179": {"key": "Ip2026DeployedTelecomCableISAC", "form": "full_length_or_independently_citable", "family": F_EVOLUTION, "secondary": "physical_media_and_networks; applications_and_challenges", "scope": "deployed_telecom_cables; terrestrial; submarine", "medium": "terrestrial_and_submarine_fiber"},
    "SCR-00042": {"key": "Yang2025ForwardVibrationOverview", "form": "short_or_focused", "family": F_PHYSICAL, "secondary": "waveforms_and_resource_design; network_operations", "scope": "forward_vibration_sensing; optical_communication_systems", "medium": "optical_fiber"},
    "SCR-00108": {"key": "Zhang2025PhotonicTHzOverview", "form": "short_or_focused", "family": F_WAVEFORM, "secondary": "architecture_and_system_design; algorithms", "scope": "photonic_THz; waveform_design; optical_processing", "medium": "photonic_THz"},
    "SCR-00222": {"key": "Huang2026OPALiDAROverview", "form": "short_or_focused", "family": F_ARCH, "secondary": "applications_and_challenges; physical_media_and_networks", "scope": "OPA; LiDAR; optical_wireless; smart_city", "medium": "FSO_and_OPA_LiDAR"},
    "SCR-00929": {"key": "Liu2025SeamlessFiberFSOOverview", "form": "short_or_focused", "family": F_PHYSICAL, "secondary": "architecture_and_system_design; deployment_and_operations", "scope": "fiber; FSO; seamless_networks", "medium": "hybrid_fiber_FSO"},
    "SCR-00932": {"key": "Wang2025OpticalFiberNetworksOverview", "form": "short_or_focused", "family": F_PHYSICAL, "secondary": "applications_and_challenges; technological_evolution", "scope": "optical_fiber_networks; current_research; challenges", "medium": "optical_fiber_networks"},
    "SCR-00936": {"key": "Wu2024FiberISACOverview", "form": "short_or_focused", "family": F_PHYSICAL, "secondary": "technological_evolution; applications_and_challenges", "scope": "optical_fiber; advancements; challenges", "medium": "optical_fiber"},
    "SCR-00952": {"key": "Yan2023OpticalTransmissionReview", "form": "short_or_focused", "family": F_PHYSICAL, "secondary": "architecture_and_system_design; technological_evolution", "scope": "optical_transmission_systems; technical_review", "medium": "optical_fiber_transmission"},
    "SCR-00967": {"key": "Boffi2025AccessMonitoringOverview", "form": "short_or_focused", "family": F_APPLICATION, "secondary": "physical_media_and_networks; deployment_and_operations", "scope": "access_networks; anthropic_activity_monitoring; safety", "medium": "optical_access_networks"},
    "SCR-00991": {"key": "Salem2024VisibleLightProspects", "form": "short_or_focused", "family": F_APPLICATION, "secondary": "physical_media_and_networks; future_directions", "scope": "visible_light; joint_communication_and_sensing", "medium": "VLC_LiFi"},
    "SCR-00999": {"key": "Rosmaninho2025ModulationStrategies", "form": "short_or_focused", "family": F_WAVEFORM, "secondary": "physical_media_and_networks; 6G_context", "scope": "modulation; optical_wireless; robustness; 6G", "medium": "optical_wireless"},
    "SCR-01003": {"key": "Yu2023THzPhotonicsOverview", "form": "short_or_focused", "family": F_WAVEFORM, "secondary": "applications_and_challenges; architecture_and_system_design", "scope": "terahertz_photonics; radar; ISAC", "medium": "photonic_THz"},
}


# Seven sources from the dated manuscript-stage bounded update.  Metadata is
# restricted to values already present in the source audit and resolved BibTeX.
ADDITIONS: list[dict[str, str]] = [
    {"id": "MSA-SU-2025", "key": "Su2025OISACTheoryPractice", "form": "full_length_or_independently_citable", "family": F_ARCH, "secondary": "translation_to_practice; applications_and_challenges", "scope": "O-ISAC; architecture; theory_to_practice", "medium": "multi_platform_optical", "date": "2025-12-11", "precision": "exact_available_online_date", "date_source": "2026-08-11_bounded_source_audit"},
    {"id": "MSA-ZHANG-2023", "key": "Zhang2023OpticalNetworkISACFrontier", "form": "full_length_or_independently_citable", "family": F_PHYSICAL, "secondary": "technological_evolution; applications_and_challenges", "scope": "optical_networks; research_frontier; integration", "medium": "optical_fiber_networks", "date": "2022-06-23", "precision": "exact_first_online_date", "date_source": "2026-08-11_bounded_source_audit"},
    {"id": "MSA-LIU-2025", "key": "Liu2025OpticalNetworkISACProspect", "form": "full_length_or_independently_citable", "family": F_EVOLUTION, "secondary": "physical_media_and_networks; applications_and_challenges", "scope": "optical_networks; technology; applications; prospects", "medium": "optical_fiber_networks", "date": "2025", "precision": "publication_year_only", "date_source": "resolved_context_bibliography"},
    {"id": "MSA-CHU-2025", "key": "Chu2025ROISACOverview", "form": "full_length_or_independently_citable", "family": F_ARCH, "secondary": "applications_and_challenges; future_directions", "scope": "retroreflective_optical_ISAC; 6G; optical_wireless", "medium": "retroreflective_optical_wireless", "venue": "arXiv", "date": "2025-12-01", "precision": "exact_arxiv_submission_date", "date_source": "2026-08-11_bounded_source_audit"},
    {"id": "MSA-CHEN-2025", "key": "Chen2025ROISACProgress", "form": "short_or_focused", "family": F_ARCH, "secondary": "technological_evolution; applications_and_challenges", "scope": "retroreflective_optical_ISAC; research_progress", "medium": "retroreflective_optical_wireless", "date": "2025", "precision": "publication_year_only", "date_source": "resolved_context_bibliography"},
    {"id": "MSA-LU-2024", "key": "Lu2024IntegratedOpticalCommSensingOverview", "form": "short_or_focused", "family": F_PHYSICAL, "secondary": "architecture_and_system_design; deployment_and_operations", "scope": "distributed_sensing; optical_communication; fiber", "medium": "optical_fiber_networks", "date": "2024", "precision": "publication_year_only", "date_source": "resolved_context_bibliography"},
    {"id": "MSA-LU-2025", "key": "Lu2025IntegratedOpticalCommSensingOverview", "form": "short_or_focused", "family": F_ARCH, "secondary": "physical_media_and_networks; future_directions", "scope": "integrated_optical_communication_and_sensing; overview", "medium": "multi_platform_optical", "date": "2025", "precision": "publication_year_only", "date_source": "resolved_context_bibliography"},
]


FAMILY_EVIDENCE = {
    F_ARCH: ("previously reported architectures, integration mechanisms, and system-design patterns", "narrative or taxonomic comparison of architecture and integration choices"),
    F_ANALYTIC: ("analytical models, limits, estimators, and design approaches summarized by the source", "conceptual and analytical comparison; no pooled estimate inferred"),
    F_EVOLUTION: ("technology lineage, standardization context, or deployment cases summarized by the source", "chronological or deployment-oriented narrative comparison"),
    F_PHYSICAL: ("media-specific systems and optical-network integration approaches summarized by the source", "descriptive comparison by optical medium, network context, and integration mechanism"),
    F_WAVEFORM: ("waveform, multiplexing, photonic-hardware, or THz implementation families summarized by the source", "mechanism-oriented descriptive comparison"),
    F_APPLICATION: ("application scenarios, platform requirements, challenges, and open directions summarized by the source", "requirements-oriented narrative comparison"),
}


def build_st_rs1() -> tuple[Path, dict[str, object]]:
    dedup = {row["screening_record_id"]: row for row in read_csv(DEDUP)}
    bib = parse_bib(BIB)
    rows: list[dict[str, object]] = []

    for sid, coding in CAPTURED.items():
        source = dedup[sid]
        key = coding["key"]
        b = bib.get(key, {})
        resolved_authors = source["authors"]
        if sid in {"SCR-01177", "SCR-01179"}:
            resolved_authors = re.sub(r"[{}]", "", b["author"])
        publication_date = source.get("publication_date", "").strip()
        date_value = publication_date or source["year"]
        date_precision = "reported_date_string" if publication_date and publication_date != source["year"] else "publication_year_only"
        evidence_unit, comparison_logic = FAMILY_EVIDENCE[coding["family"]]
        rows.append({
            "register_id": "",
            "citation_key": key,
            "citation_command": f"\\cite{{{key}}}",
            "source_record_id": sid,
            "screening_record_id": sid,
            "title": source["title"],
            "authors": resolved_authors,
            "year": int(source["year"]),
            "venue": source["source_title"],
            "persistent_identifier_type": "DOI",
            "persistent_identifier": norm_doi(source["doi"]),
            "source_url": f"https://doi.org/{norm_doi(source['doi'])}",
            "source_form": coding["form"],
            "workflow_origin": "captured_in_executed_review_workflow",
            "executed_workflow_status": "retained_contextual_synthesis",
            "synthesis_function_rule_status": "eligible",
            "primary_evidence_denominator_status": OUTSIDE,
            "primary_role": "table_i_navigation_source" if coding["form"].startswith("full") else "st_rs1_companion_source",
            "table_i_assignment_status": "displayed_in_table_i" if coding["form"].startswith("full") else "not_displayed_short_or_focused",
            "primary_reader_task_family": coding["family"],
            "secondary_reader_tasks": coding["secondary"],
            "secondary_scope_tags": coding["scope"],
            "optical_medium_or_network_scope": coding["medium"],
            "native_evidence_unit": evidence_unit,
            "comparison_logic": comparison_logic,
            "lineage_flag": "none_identified_in_bounded_audit",
            "inclusion_rationale": "Central scope concerns integrated optical communication and sensing, and the dominant function synthesizes more than one prior system, solution class, or research line.",
            "neutral_boundary": "Contextual synthesis used for survey positioning; not treated as primary technical evidence, an independent effect, or a quality benchmark." if coding["form"].startswith("full") else "Short or focused contextual synthesis retained for companion visibility; not treated as primary technical evidence or as equivalent in depth to a full-length review.",
            "date_value": date_value,
            "date_precision": date_precision,
            "date_source": "executed_deduplicated_record_export_2026-06-22",
            "metadata_source": "executed_deduplicated_record_export_2026-06-22; resolved_context_bibliography",
            "classification_basis": "2026-08-11_bounded_source_function_audit_plus_executed_export_title_abstract",
            "amendment_id": AMENDMENT,
            "bib_doi_match": norm_doi(b.get("doi", "")) == norm_doi(source["doi"]),
            "bib_title_match": (
                norm_title(b.get("title", "")) == norm_title(source["title"])
                or norm_title(b.get("title", "")) in norm_title(source["title"])
                or norm_title(source["title"]) in norm_title(b.get("title", ""))
            ),
        })

    for addition in ADDITIONS:
        key = addition["key"]
        b = bib[key]
        evidence_unit, comparison_logic = FAMILY_EVIDENCE[addition["family"]]
        lineage = "none_identified_in_bounded_audit"
        if key in {"Zhang2023OpticalNetworkISACFrontier", "Liu2025OpticalNetworkISACProspect"}:
            lineage = "distinct_update_within_optical_network_synthesis_lineage"
        elif key in {"Chen2025ROISACProgress", "Chu2025ROISACOverview"}:
            lineage = "related_research_line_no_formal_version_relationship_asserted"
        elif key in {"Lu2024IntegratedOpticalCommSensingOverview", "Lu2025IntegratedOpticalCommSensingOverview"}:
            lineage = "related_research_line_no_formal_version_relationship_asserted"
        rows.append({
            "register_id": "",
            "citation_key": key,
            "citation_command": f"\\cite{{{key}}}",
            "source_record_id": addition["id"],
            "screening_record_id": "not_in_executed_exports",
            "title": re.sub(r"[{}]", "", b["title"]),
            "authors": re.sub(r"[{}]", "", b["author"]),
            "year": int(b["year"]),
            "venue": addition.get("venue", re.sub(r"[{}]", "", b.get("journal", b.get("booktitle", "not_reported")))),
            "persistent_identifier_type": "DOI",
            "persistent_identifier": norm_doi(b["doi"]),
            "source_url": b.get("url", f"https://doi.org/{norm_doi(b['doi'])}"),
            "source_form": addition["form"],
            "workflow_origin": "manuscript_stage_bounded_addition",
            "executed_workflow_status": "absent_from_executed_exports_contextual_addition_only",
            "synthesis_function_rule_status": "eligible_under_bounded_manuscript_positioning_rule",
            "primary_evidence_denominator_status": OUTSIDE,
            "primary_role": "table_i_navigation_source" if addition["form"].startswith("full") else "st_rs1_companion_source",
            "table_i_assignment_status": "displayed_in_table_i" if addition["form"].startswith("full") else "not_displayed_short_or_focused",
            "primary_reader_task_family": addition["family"],
            "secondary_reader_tasks": addition["secondary"],
            "secondary_scope_tags": addition["scope"],
            "optical_medium_or_network_scope": addition["medium"],
            "native_evidence_unit": evidence_unit,
            "comparison_logic": comparison_logic,
            "lineage_flag": lineage,
            "inclusion_rationale": "Central scope concerns integrated optical communication and sensing, and the dominant function synthesizes more than one prior system, solution class, or research line.",
            "neutral_boundary": "Contextual synthesis added by a bounded manuscript-stage positioning update; not treated as primary technical evidence, an independent effect, or a quality benchmark." if addition["form"].startswith("full") else "Short or focused contextual synthesis added by a bounded manuscript-stage positioning update; not treated as primary technical evidence or as equivalent in depth to a full-length review.",
            "date_value": addition["date"],
            "date_precision": addition["precision"],
            "date_source": addition["date_source"],
            "metadata_source": "resolved_context_bibliography; 2026-08-11_bounded_source_function_audit",
            "classification_basis": "2026-08-11_bounded_source_function_audit",
            "amendment_id": AMENDMENT,
            "bib_doi_match": True,
            "bib_title_match": True,
        })

    family_order = {F_ARCH: 1, F_ANALYTIC: 2, F_EVOLUTION: 3, F_PHYSICAL: 4, F_WAVEFORM: 5, F_APPLICATION: 6}
    rows.sort(key=lambda r: (0 if str(r["source_form"]).startswith("full") else 1, family_order[str(r["primary_reader_task_family"])], int(r["year"]), str(r["citation_key"])))
    for index, row in enumerate(rows, 1):
        row["register_id"] = f"ST-RS1-{index:02d}"

    fields = list(rows[0].keys())
    csv_path = RS_DIR / "ST-RS1_CONTEXTUAL_SYNTHESES_38.csv"
    write_csv(csv_path, rows, fields)

    counts = Counter(str(row["source_form"]) for row in rows)
    origin_counts = Counter(str(row["workflow_origin"]) for row in rows)
    keys = [str(row["citation_key"]) for row in rows]
    table_i = [str(row["citation_key"]) for row in rows if row["table_i_assignment_status"] == "displayed_in_table_i"]
    short_keys = [str(row["citation_key"]) for row in rows if row["source_form"] == "short_or_focused"]
    dois = [norm_doi(str(row["persistent_identifier"])) for row in rows]
    checks = {
        "rows_equal_38": len(rows) == 38,
        "unique_citation_keys_equal_38": len(set(keys)) == 38,
        "full_length_equal_24": counts["full_length_or_independently_citable"] == 24,
        "short_or_focused_equal_14": counts["short_or_focused"] == 14,
        "captured_equal_31": origin_counts["captured_in_executed_review_workflow"] == 31,
        "manuscript_stage_additions_equal_7": origin_counts["manuscript_stage_bounded_addition"] == 7,
        "table_i_assignments_equal_24_unique": len(table_i) == 24 and len(set(table_i)) == 24,
        "table_i_key_set_matches_audited_assignment": set(table_i) == EXPECTED_TABLE_I_KEYS,
        "short_key_set_matches_audited_14_source_companion": set(short_keys) == EXPECTED_SHORT_KEYS,
        "all_outside_primary_denominator": all(row["primary_evidence_denominator_status"] == OUTSIDE for row in rows),
        "all_citation_keys_resolve": all(key in bib for key in keys),
        "all_persistent_identifiers_present": all(str(row["persistent_identifier"]).strip() for row in rows),
        "persistent_identifiers_unique_38": len(set(dois)) == 38,
        "all_date_sources_present": all(str(row["date_source"]).strip() for row in rows),
        "all_primary_roles_present": all(str(row["primary_role"]).strip() for row in rows),
        "all_secondary_scope_present": all(str(row["secondary_scope_tags"]).strip() for row in rows),
        "captured_bib_doi_matches": all(bool(row["bib_doi_match"]) for row in rows if row["workflow_origin"] == "captured_in_executed_review_workflow"),
        "captured_bib_title_matches": all(bool(row["bib_title_match"]) for row in rows if row["workflow_origin"] == "captured_in_executed_review_workflow"),
        "no_local_path_or_email_leakage": not any(row_has_leakage(row) for row in rows),
        "no_prohibited_self_score_or_first_only_claim": not any(re.search(r"\b(first|only|best|rank|score)\b", str(row["neutral_boundary"]), re.I) for row in rows),
    }
    qa = {
        "artifact": str(csv_path.relative_to(V2)),
        "status": "PASS" if all(checks.values()) else "FAIL",
        "scope_statement": "Bounded manuscript-positioning register; no worldwide-exhaustiveness claim.",
        "denominator_statement": "38 contextual syntheses remain outside the locked 206-study primary technical denominator.",
        "counts": {"rows": len(rows), "unique_keys": len(set(keys)), "full_length": counts["full_length_or_independently_citable"], "short_or_focused": counts["short_or_focused"], "captured": origin_counts["captured_in_executed_review_workflow"], "manuscript_stage_additions": origin_counts["manuscript_stage_bounded_addition"]},
        "checks": checks,
        "sha256": sha256(csv_path),
        "authorities": {"deduplicated_export_sha256": sha256(DEDUP), "context_bibliography_sha256": sha256(BIB)},
        "unresolved_fields": [],
    }
    qa_path = QA_DIR / "FINAL_ST_RS1_CONTEXTUAL_SYNTHESIS_QA_2026-08-13.json"
    qa_path.write_text(json.dumps(qa, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return csv_path, qa


def build_s7() -> tuple[Path, Path, dict[str, object]]:
    st01 = read_csv(ST01)
    tqaf_rows = read_csv(TQAF)
    audit_rows = [row for row in read_csv(TQAF_AUDIT) if row["dimension"] == "validation_maturity"]
    tqaf = {row["study_id"]: row for row in tqaf_rows}
    audit = {row["study_id"]: row for row in audit_rows}

    joined: list[dict[str, object]] = []
    carrier: list[dict[str, object]] = []
    for study in st01:
        sid = study["study_id"]
        q = tqaf[sid]
        a = audit[sid]
        inputs = json.loads(a["inputs_json"])
        traces = json.loads(a["record_trace_json"])
        max_tier = int(study["validation_maturity_max"])
        score = int(q["validation_maturity"])
        comm = bool(inputs["field_or_deployment_outcome_by_domain"]["communication"])
        sensing = bool(inputs["field_or_deployment_outcome_by_domain"]["sensing"])
        is_max = max_tier == 6
        is_pair = is_max and score == 3 and comm and sensing
        joined.append({
            "study_id": sid,
            "primary_report_id": study["primary_report_id"],
            "citation_key": study["citation_key"],
            "canonical_modality": study["modality"],
            "maximum_validation_tier": max_tier,
            "tqaf_validation_maturity_score": score,
            "communication_field_or_deployment_outcome": "yes" if comm else "no",
            "sensing_field_or_deployment_outcome": "yes" if sensing else "no",
            "maximum_field_or_deployment_subset": "yes" if is_max else "no",
            "paired_function_evidence_subset": "yes" if is_pair else "no",
        })
        if not is_max:
            continue
        trace_strings = []
        for trace in traces:
            trace_strings.append(f"{trace.get('record_id', 'NR')} :: {trace.get('locator', 'NR')}")
        carrier.append({
            "study_id": sid,
            "primary_report_id": study["primary_report_id"],
            "primary_screening_record_id": study["primary_screening_record_id"],
            "citation_key": study["citation_key"],
            "citation_command": study["citation_command"],
            "author_year": study["author_year"],
            "title": study["title"],
            "year": int(study["year"]),
            "venue": study["venue"],
            "doi": study["doi"],
            "canonical_modality": study["modality"],
            "maximum_validation_tier": max_tier,
            "maximum_validation_tier_definition": "field_trial_or_deployment_was_the_strongest_observed_setting",
            "tqaf_validation_maturity_score": score,
            "tqaf_validation_maturity_category": "score_3_field_or_deployment_evidence_for_both_functions" if score == 3 else "score_2_maximum_field_tier_does_not_by_itself_meet_the_paired_function_rule",
            "communication_field_or_deployment_outcome": "yes" if comm else "no",
            "sensing_field_or_deployment_outcome": "yes" if sensing else "no",
            "paired_function_evidence_subset": "yes" if is_pair else "no",
            "paired_function_interpretation": "field_or_deployment_outcomes_recorded_for_both_communication_and_sensing" if is_pair else "maximum_tier_6_observed_but_review_specific_both_function_gate_not_met",
            "relationship_timing": "NR_not_exposed_in_audited_projection",
            "maximum_tier_source_locator": " || ".join(trace_strings) if trace_strings else "NR_not_exposed_in_audited_projection",
            "communication_function_source_locator": "NR_function_specific_mapping_not_exposed_by_existing_audited_projection",
            "sensing_function_source_locator": "NR_function_specific_mapping_not_exposed_by_existing_audited_projection",
            "source_locator_status": "combined_audited_validation_trace_available; function_specific_locator_mapping_unresolved",
            "bounded_interpretation_note": "Tier 6 identifies the strongest observed setting, not validation of the complete joint system. TQAF score 3 is the narrower review-specific gate requiring field or deployment outcomes for both functions.",
            "tqaf_method_version": a["method_version"],
            "tqaf_source_workbook_sha256": a["source_workbook_sha256"],
        })

    joined.sort(key=lambda row: str(row["study_id"]))
    carrier.sort(key=lambda row: (0 if row["paired_function_evidence_subset"] == "yes" else 1, str(row["study_id"])))
    joined_path = S7_DIR / "S7_CANONICAL_JOIN_206.csv"
    carrier_path = S7_DIR / "S7_PAIRED_FUNCTION_VALIDATION_12.csv"
    write_csv(joined_path, joined, list(joined[0].keys()))
    write_csv(carrier_path, carrier, list(carrier[0].keys()))

    max_ids = {str(row["study_id"]) for row in joined if row["maximum_field_or_deployment_subset"] == "yes"}
    pair_ids = {str(row["study_id"]) for row in joined if row["paired_function_evidence_subset"] == "yes"}
    checks = {
        "joined_rows_equal_206": len(joined) == 206,
        "joined_unique_study_ids_equal_206": len({str(row["study_id"]) for row in joined}) == 206,
        "maximum_field_or_deployment_rows_equal_12": len(max_ids) == 12 and len(carrier) == 12,
        "paired_function_rows_equal_6": len(pair_ids) == 6,
        "paired_ids_strict_subset_of_maximum_ids": pair_ids < max_ids,
        "all_pair_rows_have_score_3_and_both_domains": all(int(row["tqaf_validation_maturity_score"]) == 3 and row["communication_field_or_deployment_outcome"] == "yes" and row["sensing_field_or_deployment_outcome"] == "yes" for row in joined if row["paired_function_evidence_subset"] == "yes"),
        "all_carrier_rows_have_tier_6": all(int(row["maximum_validation_tier"]) == 6 for row in carrier),
        "all_st01_ids_resolve": len(st01) == len(joined),
        "all_tqaf_ids_resolve": set(row["study_id"] for row in st01) == set(tqaf),
        "all_validation_audit_ids_resolve": set(row["study_id"] for row in st01) == set(audit),
        "no_phase_f_s7_conflation": all("6G relevance" not in str(value) for row in carrier for value in row.values()),
        "function_specific_missingness_explicit": all(str(row["communication_function_source_locator"]).startswith("NR_") and str(row["sensing_function_source_locator"]).startswith("NR_") for row in carrier),
        "no_local_path_or_email_leakage": not any(row_has_leakage(row) for row in joined + carrier),
    }
    qa = {
        "artifacts": [str(joined_path.relative_to(V2)), str(carrier_path.relative_to(V2))],
        "status": "PASS_WITH_EXPLICIT_UNRESOLVED_FUNCTION_SPECIFIC_LOCATORS" if all(checks.values()) else "FAIL",
        "counts": {"canonical_join_rows": len(joined), "maximum_tier_6_rows": len(max_ids), "paired_function_score_3_rows": len(pair_ids), "nonpaired_maximum_tier_rows": len(max_ids - pair_ids)},
        "checks": checks,
        "maximum_tier_study_ids": sorted(max_ids),
        "paired_function_study_ids": sorted(pair_ids),
        "sha256": {joined_path.name: sha256(joined_path), carrier_path.name: sha256(carrier_path)},
        "authorities": {"st01_sha256": sha256(ST01), "tqaf_206_sha256": sha256(TQAF), "tqaf_dimension_audit_sha256": sha256(TQAF_AUDIT)},
        "unresolved_fields": [
            "relationship_timing is not exposed in an existing audited projection.",
            "The audited TQAF trace supplies combined record locators but does not map separate locators to communication and sensing; function-specific locator fields remain explicit NR values.",
        ],
        "boundary": "Supplement S7 is the paired-function validation view; it is not Phase-F synthesis domain S7 (6G relevance). Maximum tier 6 is not equivalent to TQAF validation score 3.",
    }
    qa_path = QA_DIR / "FINAL_SUPPLEMENT_S7_PAIRED_FUNCTION_QA_2026-08-13.json"
    qa_path.write_text(json.dumps(qa, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return joined_path, carrier_path, qa


def write_manifests(rs_path: Path, rs_qa: dict[str, object], joined_path: Path, carrier_path: Path, s7_qa: dict[str, object]) -> None:
    rs_readme = f"""# ST-RS1 — Bounded Contextual Synthesis Register

This directory materializes the bounded 38-source manuscript-positioning register. It contains 24 full-length or independently citable syntheses and 14 short or focused syntheses. Thirty-one sources were captured in the executed workflow; seven were added through the dated manuscript-stage amendment `{AMENDMENT}`.

All 38 rows are contextual only and remain outside the locked 206-study primary technical denominator. The register is not a claim of worldwide exhaustiveness and does not rank or score prior surveys.

Hard-gate QA status: `{rs_qa['status']}`. The CSV is UTF-8 with a BOM for Excel compatibility. Citation keys resolve in `../../references_context_candidate.bib`.
"""
    (RS_DIR / "README.md").write_text(rs_readme, encoding="utf-8")

    s7_readme = f"""# Supplement S7 — Paired-Function Validation View

`S7_CANONICAL_JOIN_206.csv` documents the one-to-one join between the 206-study inventory and the 206 TQAF rows. `S7_PAIRED_FUNCTION_VALIDATION_12.csv` is the publication-facing 12-study maximum-field/deployment subset.

Exactly 12 studies reached maximum validation tier 6. Six of those 12 also received TQAF validation-maturity score 3, the narrower review-specific gate requiring field or deployment outcomes for both communication and sensing. The other six are not failed studies; tier 6 alone does not prove paired-function field validation.

The existing audited TQAF trace provides combined record locators. It does not expose relationship timing or a separate locator-to-function mapping, so those fields remain explicit `NR` values rather than inferred text. Supplement S7 is not the Phase-F S7 6G-relevance domain.

Hard-gate QA status: `{s7_qa['status']}`.
"""
    (S7_DIR / "README.md").write_text(s7_readme, encoding="utf-8")

    all_outputs = [rs_path, joined_path, carrier_path, QA_DIR / "FINAL_ST_RS1_CONTEXTUAL_SYNTHESIS_QA_2026-08-13.json", QA_DIR / "FINAL_SUPPLEMENT_S7_PAIRED_FUNCTION_QA_2026-08-13.json", RS_DIR / "README.md", S7_DIR / "README.md"]
    for optional in [
        RS_DIR / "ST-RS1_CONTEXTUAL_SYNTHESES_38.xlsx",
        S7_DIR / "S7_PAIRED_FUNCTION_VALIDATION_12.xlsx",
        QA_DIR / "FINAL_ST_RS1_WORKBOOK_QA_2026-08-13.json",
        QA_DIR / "FINAL_SUPPLEMENT_S7_WORKBOOK_QA_2026-08-13.json",
    ]:
        if optional.exists():
            all_outputs.append(optional)
    lines = [f"{sha256(path)}  {path.relative_to(V2).as_posix()}" for path in all_outputs]
    (V2 / "supplements/REMAINING_SUPPLEMENTS_SHA256_2026-08-13.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    RS_DIR.mkdir(parents=True, exist_ok=True)
    S7_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)
    rs_path, rs_qa = build_st_rs1()
    joined_path, carrier_path, s7_qa = build_s7()
    write_manifests(rs_path, rs_qa, joined_path, carrier_path, s7_qa)
    print(json.dumps({"st_rs1": rs_qa["status"], "s7": s7_qa["status"], "st_rs1_rows": rs_qa["counts"]["rows"], "s7_rows": s7_qa["counts"]["maximum_tier_6_rows"]}, indent=2))


if __name__ == "__main__":
    main()
