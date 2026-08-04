#!/usr/bin/env python3
"""Derive Phase-F/S1-S7 publication summaries from the locked Phase-D workbook.

The script is intentionally standard-library only. It reads XLSX XML directly,
verifies the locked source SHA-256, applies explicit deterministic normalization
rules, excludes quarantined claims from claim-based synthesis, and writes a
fully auditable CSV/JSON/Markdown package without modifying canonical inputs.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


def required_input_path(env_name: str) -> Path:
    """Resolve a host-supplied input without embedding a local workstation path."""
    raw = os.environ.get(env_name, "").strip()
    if not raw:
        raise RuntimeError(f"Set {env_name} to the required source artifact path.")
    return Path(raw).expanduser().resolve()


SOURCE = required_input_path("OISAC_PHASE_D_WORKBOOK")
EXPECTED_SOURCE_SHA256 = "c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348"
CROSSWALK = required_input_path("OISAC_PHASE_E_CROSSWALK")
EXPECTED_CROSSWALK_SHA256 = "41d6f8f574bdd0d6eba04806b2930ade8fa1d3d56e28b083de3d56bb13e7d122"
OUTPUT_DIR = Path(__file__).resolve().parent
DENOMINATOR = 206

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

MODALITY_CODES = (
    "photonic_THz",
    "fiber",
    "VLC_LiFi",
    "FSO",
    "hybrid_optical",
    "other_optical",
)
INTEGRATION_CODES = (
    "shared_waveform",
    "shared_hardware",
    "shared_optical_carrier",
    "shared_link_or_channel",
    "shared_resource_allocation",
    "joint_design_or_optimization",
    "shared_application_scenario",
    "mixed",
    "other",
    "unclear",
)
VALIDATION_CODES = (
    "analytical",
    "numerical_analysis",
    "simulation",
    "dataset_based",
    "laboratory_experiment",
    "prototype_testbed",
    "field_experiment",
    "mixed",
    "unclear",
)
APPLICATION_CODES = (
    "6G_access",
    "indoor_positioning",
    "vehicular",
    "industrial",
    "security",
    "environment_monitoring",
    "underwater",
    "aerospace",
    "datacenter",
    "optical_access_network",
    "healthcare",
    "smart_infrastructure",
    "other",
)
TECHNOLOGY_CODES = (
    "OFDM",
    "beamforming",
    "MIMO",
    "coherent_optics",
    "photonic_integration",
    "photonic_THz_generation",
    "ML_AI",
    "RIS_ORIS",
    "OPA",
    "digital_twin",
    "fiber_DAS",
    "FMCW",
    "other",
)
SIX_G_CODES = ("direct", "inferred", "weak", "not_applicable")

EXPECTED_EXCLUSIVE_DISTRIBUTIONS = {
    "modality": {
        "photonic_THz": 69,
        "fiber": 56,
        "VLC_LiFi": 38,
        "FSO": 31,
        "hybrid_optical": 9,
        "other_optical": 3,
    },
    "validation_maturity_max": {"2": 32, "3": 18, "4": 78, "5": 66, "6": 12},
    "dataset_availability": {
        "unavailable_or_NR": 145,
        "on_request": 41,
        "open": 13,
        "NA": 7,
    },
    "code_model_availability": {
        "unavailable_or_NR": 197,
        "on_request": 7,
        "partial_components": 1,
        "NA": 1,
    },
    "six_g": {"direct": 138, "inferred": 64, "weak": 1, "not_applicable": 3},
}
EXPECTED_FALLBACK_OTHER_COUNTS = {
    "integration_mechanism": 0,
    "enabling_technology": 19,
    "application_domain": 15,
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def low(value: object) -> str:
    text = clean(value).lower()
    text = text.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text)


def tokens(value: object) -> list[str]:
    return [part.strip() for part in re.split(r"[|;]", clean(value)) if part.strip()]


def contains_any(text: str, needles: tuple[str, ...] | list[str]) -> bool:
    return any(needle in text for needle in needles)


def pct(count: int, denominator: int = DENOMINATOR) -> float:
    return round(100.0 * count / denominator, 1) if denominator else 0.0


def column_index(cell_reference: str) -> int:
    match = re.match(r"([A-Z]+)", cell_reference)
    if not match:
        raise ValueError(f"Invalid XLSX cell reference: {cell_reference}")
    number = 0
    for char in match.group(1):
        number = number * 26 + ord(char) - 64
    return number - 1


class XlsxReader:
    def __init__(self, path: Path):
        self.archive = zipfile.ZipFile(path)
        self.shared_strings = self._read_shared_strings()
        self.sheet_paths = self._read_sheet_paths()

    def close(self) -> None:
        self.archive.close()

    def _read_shared_strings(self) -> list[str]:
        if "xl/sharedStrings.xml" not in self.archive.namelist():
            return []
        root = ET.fromstring(self.archive.read("xl/sharedStrings.xml"))
        return [
            "".join(node.text or "" for node in item.iterfind(".//m:t", NS))
            for item in root.findall("m:si", NS)
        ]

    def _read_sheet_paths(self) -> dict[str, str]:
        workbook = ET.fromstring(self.archive.read("xl/workbook.xml"))
        relations = ET.fromstring(self.archive.read("xl/_rels/workbook.xml.rels"))
        relation_map = {
            relation.attrib["Id"]: relation.attrib["Target"] for relation in relations
        }
        result: dict[str, str] = {}
        for sheet in workbook.find("m:sheets", NS):
            target = relation_map[sheet.attrib[f"{{{NS['r']}}}id"]].lstrip("/")
            if not target.startswith("xl/"):
                target = posixpath.normpath(posixpath.join("xl", target))
            result[sheet.attrib["name"]] = target
        return result

    def _cell_value(self, cell: ET.Element) -> str:
        kind = cell.attrib.get("t")
        if kind == "inlineStr":
            return "".join(node.text or "" for node in cell.iterfind(".//m:t", NS))
        value = cell.find("m:v", NS)
        if value is None:
            return ""
        raw = value.text or ""
        if kind == "s":
            return self.shared_strings[int(raw)]
        if kind == "b":
            return "TRUE" if raw == "1" else "FALSE"
        return raw

    def rows(self, sheet_name: str) -> list[dict[str, str]]:
        root = ET.fromstring(self.archive.read(self.sheet_paths[sheet_name]))
        matrix: list[list[str]] = []
        for row in root.iterfind(".//m:sheetData/m:row", NS):
            cells = {
                column_index(cell.attrib["r"]): self._cell_value(cell)
                for cell in row.findall("m:c", NS)
            }
            if not cells:
                continue
            matrix.append([cells.get(i, "") for i in range(max(cells) + 1)])
        if not matrix:
            return []
        headers = matrix[0]
        return [
            dict(zip(headers, row + [""] * (len(headers) - len(row))))
            for row in matrix[1:]
        ]


def normalize_modality(raw: str) -> tuple[list[str], str, list[str]]:
    value = clean(raw)
    lowered = low(value).replace("-", "_").replace(" ", "_")
    exact = {code.lower(): code for code in MODALITY_CODES}
    if lowered in exact:
        return [exact[lowered]], "controlled_exact", []
    if not value or lowered in {"nr", "na", "unc", "unclear", "not_reported"}:
        return ["unclear"], "missing_or_unclear", []

    # The ordering is deliberate: explicit hybrid and visible-light phrases must
    # win before the generic fibre/free-space terms embedded in them.
    if contains_any(
        lowered,
        (
            "hybrid",
            "fiber_wireless",
            "fibre_wireless",
            "d_band_wireless",
            "radio_over_fiber",
            "radio_over_fibre",
            "wireless_isac",
        ),
    ):
        code = "hybrid_optical"
    elif contains_any(
        lowered,
        ("visible", "vlc", "li_fi", "lifi", "screen_camera", "camera_communication", "retroreflect", "led", "ultraviolet", "_uv_"),
    ):
        code = "VLC_LiFi"
    elif contains_any(lowered, ("terahertz", "_thz", "thz_")):
        code = "photonic_THz"
    elif contains_any(
        lowered,
        ("free_space", "_fso", "fso_", "optical_wireless", "near_infrared", "laser_wireless"),
    ):
        code = "FSO"
    elif contains_any(lowered, ("microwave_photonic", "mmwave", "millimeter_wave", "millimetre_wave", "w_band", "d_band")):
        code = "hybrid_optical"
    elif contains_any(
        lowered,
        (
            "fiber",
            "fibre",
            "ofdr",
            "otdr",
            "distributed_acoustic",
            "coherent_optical",
            "coherent_dscm",
            "submarine",
            "dwddm",
            "dwdm",
            "passive_optical_network",
            "pon_",
            "_pon",
            "optical_fronthaul",
            "optical_transport",
        ),
    ):
        code = "fiber"
    else:
        code = "other_optical"
    return [code], "keyword_normalized", [] if code != "other_optical" else [value]


def normalize_integration(raw: str) -> tuple[list[str], str, list[str]]:
    value = clean(raw)
    if not value or low(value) in {"nr", "na", "unc", "unclear", "not_reported"}:
        return ["unclear"], "missing_or_unclear", []
    direct_codes = set(INTEGRATION_CODES) - {"other", "unclear"}
    found: set[str] = set()
    unresolved: list[str] = []
    for token in tokens(value):
        token_low = low(token).replace("-", "_").replace(" ", "_")
        if token_low in direct_codes:
            found.add(token_low)
            continue
        mapped_before = len(found)
        if contains_any(
            token_low,
            (
                "shared_waveform",
                "joint_waveform",
                "integrated_waveform",
                "unified_waveform",
                "waveform_reuse",
                "shared_signal",
                "shared_frame",
                "shared_pilot",
                "dual_function_waveform",
                "common_waveform",
                "signal_reuse",
                "communication_signal_reuse",
                "forward_communication_signal",
                "carrier_phase_reuse",
                "training_sequence_reuse",
                "received_signal_reuse",
                "reflected_downlink",
                "shared_intensity",
                "shared_transmission",
                "shared_pulses",
                "shared_illumination",
                "single_pam4_waveform",
                "single_ook_transmission",
                "single_cycle_waveform",
            ),
        ):
            found.add("shared_waveform")
        if "shared" in token_low and contains_any(
            token_low, ("waveform", "signal", "pulse", "frame", "pilot", "transmission")
        ):
            found.add("shared_waveform")
        if contains_any(
            token_low,
            (
                "shared_hardware",
                "shared_transceiver",
                "shared_receiver",
                "shared_transmitter",
                "shared_laser",
                "shared_optical_source",
                "shared_source",
                "shared_front_end",
                "shared_frontend",
                "common_hardware",
                "hardware_reuse",
                "single_coherent_receiver",
                "co_located_led_pd",
                "collocated_led_pd",
                "dual_function",
                "monolithic_integration",
                "shared_monolithic_chip",
                "shared_material_platform",
                "shared_camera",
                "shared_photonic_frontend",
                "shared_photonic_transmitter",
                "shared_photonic_microwave_generator",
                "shared_ro_isac_transceiver",
            ),
        ):
            found.add("shared_hardware")
        if "shared" in token_low and contains_any(
            token_low,
            ("hardware", "transceiver", "receiver", "transmitter", "laser", "source", "front_end", "frontend", "camera", "chip", "platform"),
        ):
            found.add("shared_hardware")
        if contains_any(
            token_low,
            (
                "shared_optical_carrier",
                "shared_carrier",
                "same_carrier",
                "carrier_reuse",
                "shared_wavelength",
                "shared_d_band_carrier",
                "shared_j_band_waveform",
                "shared_35_ghz_waveform",
                "lfm_optical_carrier",
            ),
        ):
            found.add("shared_optical_carrier")
        if contains_any(
            token_low,
            (
                "shared_link",
                "shared_channel",
                "shared_fiber",
                "shared_fibre",
                "shared_infrastructure",
                "shared_optical_path",
                "shared_reflected_optical_path",
                "shared_rof_link",
                "shared_wireless_transmission",
                "fiber_as_sensor",
                "fibre_as_sensor",
                "fiber_reuse",
                "fibre_reuse",
                "cable_reuse",
                "co_optical_path",
                "co_propag",
                "counter_propagation",
                "common_link",
                "same_channel",
                "shared_90km",
            ),
        ):
            found.add("shared_link_or_channel")
        if "shared" in token_low and contains_any(
            token_low, ("link", "channel", "path", "fiber", "fibre", "cable")
        ):
            found.add("shared_link_or_channel")
        if contains_any(
            token_low,
            (
                "resource",
                "allocation",
                "multiplex",
                "shared_spectrum",
                "overlapped_radar_communication_spectrum",
                "bandwidth_sharing",
                "power_split",
                "power_domain_superposition",
                "superposition",
                "time_division",
                "frequency_division",
                "space_division",
                "orthogonal_channel_partition",
                "wavelength_division",
                "wdm",
                "fdm",
                "ofdma",
                "tdd",
                "subcarrier",
                "pilot_tone",
                "embedded_pilot",
                "beam_split",
                "time_switched",
                "time_delay_spatial_separation",
                "polarization_interleav",
            ),
        ):
            found.add("shared_resource_allocation")
        if contains_any(
            token_low,
            (
                "joint_design",
                "joint_optimization",
                "joint_optimisation",
                "joint_parameter",
                "joint_input",
                "joint_qos",
                "joint_multibeam",
                "joint_transmit_receive",
                "joint_sop",
                "joint_map",
                "co_design",
                "joint_waveform",
                "joint_processing",
                "joint_algorithm",
                "fusion_processing",
                "coherent_fusion",
                "multi_task_learning",
                "parallel_demodulation_and_positioning",
                "capacity_distortion_optimization",
                "latency_optimization",
                "data_rate_optimization",
                "weighted_sum_rate",
            ),
        ):
            found.add("joint_design_or_optimization")
        if contains_any(
            token_low,
            (
                "application_scenario",
                "shared_scenario",
                "coexistence",
                "sensing_assisted",
                "communication_assisted",
                "same_application",
                "simultaneous_communication_and_sensing",
                "communication_and_sensing",
                "communication_sensing",
                "sensing_feedback",
                "sensing_app",
                "task_offloading",
                "risk_status",
                "association",
            ),
        ):
            found.add("shared_application_scenario")
        if token_low == "mixed" or token_low.startswith("mixed_"):
            found.add("mixed")
        if len(found) == mapped_before:
            unresolved.append(token)
    # ``other`` is a study-level fallback, never a co-label. Keep any unmatched
    # fine-grained tokens in the audit when a recognized mechanism exists.
    if found - {"other"}:
        found.discard("other")
    if not found:
        found.add("other")
    mode = "controlled_exact" if not unresolved and all(low(t).replace("-", "_").replace(" ", "_") in direct_codes for t in tokens(value)) else "keyword_normalized"
    return [code for code in INTEGRATION_CODES if code in found], mode, unresolved


def normalize_validation(raw: str) -> tuple[list[str], str, list[str]]:
    value = clean(raw)
    if not value or low(value) in {"nr", "na", "unc", "unclear", "not_reported"}:
        return ["unclear"], "missing_or_unclear", []
    found: set[str] = set()
    unresolved: list[str] = []
    controlled = set(VALIDATION_CODES) - {"unclear"}
    for token in tokens(value):
        t = low(token).replace("-", "_").replace(" ", "_")
        if t in controlled:
            found.add(t)
            continue
        before = len(found)
        if contains_any(t, ("field_trial", "field_experiment", "field_deploy", "real_world", "outdoor_field", "field_observation", "operator_live_network")):
            found.add("field_experiment")
        if contains_any(t, ("prototype", "testbed", "proof_of_concept", "proof-of-concept", "poc")):
            found.add("prototype_testbed")
        if contains_any(t, ("laboratory", "hardware_experiment", "controlled_hardware", "device_characterization", "device_characterisation", "biological_sample", "optical_bench", "experimental")):
            found.add("laboratory_experiment")
        if contains_any(t, ("dataset", "machine_learning", "supervised", "retrospective", "observational", "classification", "weather_data", "live_network_sensing_data")):
            found.add("dataset_based")
        if contains_any(t, ("simulation", "monte_carlo", "emulation", "vpi", "parameter_sweep", "digital_twin", "algorithmic_emulation")):
            found.add("simulation")
        if contains_any(t, ("numerical_analysis", "numerical_illustration", "optimization", "optimisation", "reported_calculation", "computational_analysis")):
            found.add("numerical_analysis")
        # Numerical simulation is a simulation, not a second analytical type.
        if "numerical_simulation" in t:
            found.add("simulation")
            found.discard("numerical_analysis")
        if contains_any(t, ("analytical", "theoretical", "derivation", "closed_form", "signal_and_channel_model")):
            found.add("analytical")
        if t == "mixed" or t.startswith("mixed_"):
            found.add("mixed")
        if len(found) == before:
            unresolved.append(token)
    if not found:
        found.add("unclear")
    mode = "controlled_exact" if not unresolved and all(low(t).replace("-", "_").replace(" ", "_") in controlled for t in tokens(value)) else "keyword_normalized"
    return [code for code in VALIDATION_CODES if code in found], mode, unresolved


def normalize_applications(raw: str) -> tuple[list[str], str, list[str]]:
    value = clean(raw)
    if not value:
        return ["other"], "missing_fallback", []
    direct = {code.lower(): code for code in APPLICATION_CODES}
    found: set[str] = set()
    unresolved: list[str] = []
    for token in tokens(value):
        t = low(token).replace("-", "_").replace(" ", "_")
        if t in direct:
            found.add(direct[t])
            continue
        before = len(found)
        if contains_any(t, ("6g", "six_g", "beyond_5g", "radio_access", "mobile_fronthaul", "ran_", "future_access")):
            found.add("6G_access")
        if contains_any(t, ("indoor_position", "localization", "localisation", "positioning", "indoor_navigation")):
            found.add("indoor_positioning")
        if contains_any(t, ("vehicul", "automotive", "autonomous_driving", "autonomous_train", "high_speed_rail", "train_to_train", "transportation", "railway", "traffic")):
            found.add("vehicular")
        if contains_any(t, ("industrial", "manufactur", "industry_4", "industrial_iot", "factory")):
            found.add("industrial")
        if contains_any(t, ("security", "intrusion", "eavesdrop", "surveillance", "secure", "fault_local", "survivability")):
            found.add("security")
        if contains_any(t, ("environment", "weather", "vibration", "seismic", "structural_health", "pollution", "monitoring")):
            found.add("environment_monitoring")
        if contains_any(t, ("underwater", "undersea", "aquatic", "subsea")):
            found.add("underwater")
        if contains_any(t, ("aerospace", "satellite", "spaceborne", "uav", "drone", "aviation")):
            found.add("aerospace")
        if contains_any(t, ("datacenter", "data_center", "data_centre")):
            found.add("datacenter")
        if contains_any(t, ("optical_access", "access_network", "fiber_wireless_access", "fibre_wireless_access", "fiber_network", "fibre_network", "telecom_fiber", "telecom_fibre", "pon", "fronthaul", "transport_network")):
            found.add("optical_access_network")
        if contains_any(t, ("health", "medical", "biological", "biosens", "patient")):
            found.add("healthcare")
        if contains_any(t, ("smart_infrastructure", "smart_city", "smart_build", "smart_lighting", "human_computer_interaction", "infrastructure", "internet_of_everything", "ioe")):
            found.add("smart_infrastructure")
        if len(found) == before:
            unresolved.append(token)
    # ``other`` is assigned only when this study has no recognized broad
    # application category. Unmatched co-occurring tokens remain audit-only.
    if found - {"other"}:
        found.discard("other")
    if not found:
        found.add("other")
    mode = "controlled_exact" if not unresolved and all(low(t).replace("-", "_").replace(" ", "_") in direct for t in tokens(value)) else "keyword_normalized"
    return [code for code in APPLICATION_CODES if code in found], mode, unresolved


def normalize_technologies(raw: str) -> tuple[list[str], str, list[str]]:
    value = clean(raw)
    if not value:
        return ["other"], "missing_fallback", []
    direct = {code.lower(): code for code in TECHNOLOGY_CODES}
    found: set[str] = set()
    unresolved: list[str] = []
    for token in tokens(value):
        t = low(token).replace("-", "_").replace(" ", "_")
        if t in direct:
            found.add(direct[t])
            continue
        before = len(found)
        if "ofdm" in t or contains_any(t, ("ufmc", "ocdm", "multicarrier", "multi_carrier")):
            found.add("OFDM")
        if contains_any(t, ("beamform", "beam_steer", "beamsteer", "movable_access_point", "motorized_track_lighting")):
            found.add("beamforming")
        if contains_any(t, ("mimo", "simo", "multiple_input_multiple_output", "single_input_multiple_output")):
            found.add("MIMO")
        if contains_any(t, ("coherent", "homodyne", "heterodyne")):
            found.add("coherent_optics")
        if contains_any(t, ("photonic_integration", "integrated_photonic", "silicon_photonic", "photonic_chip", "photonic_integrated", "monolithic_integration", "iii_nitride", "ingan", "gan_on_silicon", "mqw", "comb_waveguide")):
            found.add("photonic_integration")
        if contains_any(t, ("photonic_thz", "thz_generation", "utc_pd", "photomix", "photonic_mmwave", "photonic_millimeter", "w_band_photonic", "microwave_phot", "radio_over_fiber", "radio_over_fibre", "photonic_dechirp", "optical_dechirp", "optoelectronic_oscillator", "chaotic_oeo", "frequency_multiplier", "frequency_multipli", "frequency_sextupl", "mmwave", "thz")) or t in {"rof", "a_rof", "arof"}:
            found.add("photonic_THz_generation")
        if contains_any(t, ("ml_ai", "machine_learning", "deep_learning", "neural", "transformer", "lstm", "classifier", "artificial_intelligence", "cnn", "dnn", "variational_autoencoder", "conditional_gan", "generative_adversarial", "svm", "random_forest", "decision_tree", "q_learning", "whale_optimization", "domain_adaptation", "linear_regression")):
            found.add("ML_AI")
        if contains_any(t, ("ris", "oris", "oirs", "reconfigurable_intelligent", "intelligent_reflecting", "intelligent_surface")):
            found.add("RIS_ORIS")
        if contains_any(t, ("optical_phased_array", "opa", "phased_array")):
            found.add("OPA")
        if "digital_twin" in t:
            found.add("digital_twin")
        if contains_any(t, ("fiber_das", "fibre_das", "distributed_acoustic", "distributed_fiber_sensing", "distributed_fibre_sensing", "ofdr", "otdr", "cc_otdr")):
            found.add("fiber_DAS")
        if contains_any(t, ("fmcw", "frequency_modulated_continuous_wave", "lfm", "chirp", "frequency_sweep", "itof")):
            found.add("FMCW")
        if len(found) == before:
            unresolved.append(token)
    # ``other`` is assigned only when this study has no recognized broad
    # technology category. Unmatched co-occurring tokens remain audit-only.
    if found - {"other"}:
        found.discard("other")
    if not found:
        found.add("other")
    mode = "controlled_exact" if not unresolved and all(low(t).replace("-", "_").replace(" ", "_") in direct for t in tokens(value)) else "keyword_normalized"
    return [code for code in TECHNOLOGY_CODES if code in found], mode, unresolved


def normalize_six_g(raw: str) -> tuple[list[str], str, list[str]]:
    value = clean(raw)
    t = low(value).replace("-", "_").replace(" ", "_")
    if t in SIX_G_CODES:
        return [t], "controlled_exact", []
    if t in {"na", "n/a", "not_applicable"}:
        return ["not_applicable"], "controlled_exact", []
    if contains_any(t, ("explicit", "direct")) and "not_explicit" not in t:
        return ["direct"], "keyword_normalized", []
    if contains_any(t, ("inferred", "implicit", "enabling", "conceptual", "b5g", "beyond_5g", "next_generation", "candidate", "future_")):
        return ["inferred"], "keyword_normalized", []
    if contains_any(t, ("weak", "indirect", "contextual", "adjacent", "not_explicit")):
        return ["weak"], "keyword_normalized", []
    if not t or t in {"nr", "unc", "unclear"}:
        return ["weak"], "missing_to_weak", [value] if value else []
    return ["weak"], "fallback_to_weak", [value]


def normalize_data_status(raw: str) -> str:
    t = low(raw).replace("-", "_").replace(" ", "_")
    if contains_any(t, ("public_repository", "supplementary", "available_in_article")) or t == "open":
        return "publicly_available"
    if "request" in t:
        return "available_on_request"
    if contains_any(t, ("not_applicable", "no_data_generated", "na")) and t not in {"nr"}:
        return "not_applicable"
    if contains_any(t, ("third_party", "external_open")):
        return "third_party_or_partial"
    if not t or t in {"nr", "unc", "unclear"}:
        return "not_reported"
    return "not_public_or_unlinked"


def normalize_code_status(raw: str) -> str:
    t = low(raw).replace("-", "_").replace(" ", "_")
    if contains_any(t, ("public_repository", "supplementary", "available_in_article")) or t == "open":
        return "publicly_available"
    if "request" in t:
        return "available_on_request"
    if contains_any(t, ("partial_external", "external_component")):
        return "partial_external_components_only"
    if t in {"na", "not_applicable"}:
        return "not_applicable"
    return "not_reported" if not t or t in {"nr", "unc", "unclear"} else "not_public_or_unlinked"


def maturity_category(study: dict[str, str], validation: set[str], data_status: str, code_status: str) -> str:
    raw = low(study.get("validation_type_codes", ""))
    repeatability = low(study.get("repeatable_parameters_status", ""))
    protocol_ready = contains_any(repeatability, ("substantial", "high"))
    if data_status == "publicly_available" and code_status == "publicly_available" and protocol_ready:
        return "7_benchmark_ready_open_data_code_protocol"
    if "field_experiment" in validation:
        return "6_field_trial_or_deployment"
    if "laboratory_experiment" in validation and "prototype_testbed" in validation:
        return "5_controlled_lab_prototype"
    if "laboratory_experiment" in validation or "prototype_testbed" in validation:
        return "4_proof_of_concept_experiment"
    sensitivity_terms = ("sensitivity", "ablation", "parameter_sweep", "monte_carlo", "robust", "comparative", "baseline")
    if "simulation" in validation and contains_any(raw, sensitivity_terms):
        return "3_simulation_with_sensitivity_or_ablation"
    if "simulation" in validation or "dataset_based" in validation:
        return "2_simulation_or_dataset_only"
    return "1_analytical_or_numerical_only"


def is_conditional_claim(ledger_row: dict[str, str]) -> bool:
    return (
        clean(ledger_row.get("claim_status"))
        in {
            "supported_but_cross_study_comparison_gated",
            "supported_with_source_specific_guardrail",
        }
        or clean(ledger_row.get("comparison_admissibility"))
        in {"conditionally_comparable", "conditionally_admissible", "caution"}
        or clean(ledger_row.get("cross_study_quantitative_comparison_allowed"))
        == "yes_with_conditions"
    )


def tradeoff_family(row: dict[str, str]) -> str:
    text = low(
        " | ".join(
            clean(row.get(field))
            for field in (
                "reported_status",
                "evidence_type",
                "communication_axis_or_variable",
                "sensing_axis_or_variable",
                "optimization_objective",
                "constraints",
            )
        )
    ).replace("-", "_")
    rate = contains_any(text, ("rate", "throughput", "bitrate", "capacity", "spectral_efficiency", "sum_rate"))
    if rate and contains_any(text, ("range_resolution", "spatial_resolution", "resolution", "resolvability")):
        return "rate_resolution"
    if rate and contains_any(text, ("accuracy", "error", "precision", "localization", "localisation", "positioning")):
        return "rate_accuracy_or_localization"
    if rate and contains_any(text, ("range", "distance", "coverage", "reach")):
        return "rate_range_or_coverage"
    if contains_any(text, ("bandwidth", "spectrum", "spectral", "subcarrier", "resource_allocation", "resource allocation", "overhead", "pilot", "time_division", "frequency_division", "sampling_rate")):
        return "bandwidth_spectrum_or_resource_allocation"
    if contains_any(text, ("power", "energy", "rop", "vpp", "bias_current", "cpsr", "cspr", "optical_intensity")):
        return "power_energy_or_dynamic_range"
    if contains_any(text, ("ber", "evm", "snr", "osnr", "reliability", "error_rate", "communication_penalty", "crosstalk")):
        return "communication_reliability_vs_sensing_quality"
    if contains_any(text, ("security", "secrecy", "eavesdrop", "intrusion")):
        return "security_or_resilience_tradeoff"
    if contains_any(text, ("waveform", "modulation", "qam", "chirp", "cyclic_prefix", "complexity", "hardware", "laser", "linewidth", "receiver", "aperture", "directivity", "orientation", "pointing")):
        return "waveform_hardware_or_complexity"
    if contains_any(text, ("joint_benefit", "synerg", "no_antagonistic", "resource_reuse", "matched_joint")):
        return "synergy_or_non_antagonistic_coupling"
    if contains_any(text, ("qualitative", "partial", "absent", "future_only", "not_reported")):
        return "qualitative_or_partial_general"
    return "other_joint_tradeoff"


def aggregate_study_labels(study_labels: dict[str, list[str]], ordered_codes: tuple[str, ...]) -> list[dict[str, object]]:
    studies_by_label: dict[str, set[str]] = {code: set() for code in ordered_codes}
    for study_id, labels in study_labels.items():
        for label in set(labels):
            studies_by_label.setdefault(label, set()).add(study_id)
    rows = []
    for code in ordered_codes:
        count = len(studies_by_label.get(code, set()))
        rows.append({"category": code, "study_count": count, "percent_of_206": pct(count)})
    return rows


def aggregate_claim_categories(rows: list[dict[str, str]], category_field: str) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[clean(row.get(category_field)) or "not_reported"].append(row)
    result = []
    for category, members in grouped.items():
        studies = {clean(row.get("study_cluster_id")) for row in members if clean(row.get("study_cluster_id"))}
        result.append(
            {
                "category": category,
                "claim_count": len(members),
                "unique_study_count": len(studies),
                "percent_of_206_studies": pct(len(studies)),
                "conditional_claim_count": sum(int(row["_conditional"]) for row in members),
                "eligible_quantitative_claim_count": sum(clean(row.get("_survey_use_class")) == "eligible_quantitative" for row in members),
                "eligible_qualitative_claim_count": sum(clean(row.get("_survey_use_class")) == "eligible_qualitative" for row in members),
                "context_only_claim_count": sum(clean(row.get("_survey_use_class")) == "context_only" for row in members),
            }
        )
    return sorted(result, key=lambda item: (-int(item["unique_study_count"]), -int(item["claim_count"]), str(item["category"])))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        fieldnames = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=False)
        handle.write("\n")


def markdown_table(rows: list[dict[str, object]], columns: list[tuple[str, str]], limit: int | None = None) -> str:
    shown = rows if limit is None else rows[:limit]
    header = "| " + " | ".join(label for _, label in columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    lines = [header, separator]
    for row in shown:
        lines.append("| " + " | ".join(str(row.get(key, "")).replace("|", "\\|") for key, _ in columns) + " |")
    return "\n".join(lines)


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    actual_sha = sha256_file(SOURCE)
    if actual_sha != EXPECTED_SOURCE_SHA256:
        raise RuntimeError(f"Source SHA mismatch: expected {EXPECTED_SOURCE_SHA256}, got {actual_sha}")
    crosswalk_sha = sha256_file(CROSSWALK)
    if crosswalk_sha != EXPECTED_CROSSWALK_SHA256:
        raise RuntimeError(
            f"Phase-E crosswalk SHA mismatch: expected {EXPECTED_CROSSWALK_SHA256}, got {crosswalk_sha}"
        )
    with CROSSWALK.open("r", encoding="utf-8") as handle:
        crosswalk_payload = json.load(handle)
    crosswalk_studies = crosswalk_payload.get("per_study_crosswalk", [])
    crosswalk_by_study = {
        clean(row.get("study_cluster_id")): row for row in crosswalk_studies
    }
    duplicate_crosswalk_ids = len(crosswalk_by_study) != len(crosswalk_studies)

    reader = XlsxReader(SOURCE)
    try:
        master = reader.rows("01_STUDY_MASTER")
        evidence = reader.rows("03_EVIDENCE_ITEMS")
        metrics = reader.rows("04_METRIC_RESULTS")
        tradeoffs = reader.rows("05_TRADEOFF_EVIDENCE")
        ledger = reader.rows("22_SURVEY_CLAIM_LEDGER")
        conflicts = reader.rows("23_CONFLICT_REGISTER")
        study_use = reader.rows("24_STUDY_SURVEY_USE")
    finally:
        reader.close()

    study_ids = [clean(row.get("study_cluster_id")) for row in master]
    if len(master) != DENOMINATOR or len(set(study_ids)) != DENOMINATOR or "" in study_ids:
        raise RuntimeError("Study master does not reconcile to 206 unique nonblank study clusters")

    # Phase-E per_study_crosswalk is the sole authority for mutually exclusive
    # modality/maturity/data/code/6G classifications. Phase-F normalizes only
    # the preserved multi-label dimensions below.
    normalizers = {
        "integration_mechanism_codes": normalize_integration,
        "validation_type_codes": normalize_validation,
        "application_domain_codes": normalize_applications,
        "enabling_technology_codes": normalize_technologies,
    }
    normalized: dict[str, dict[str, list[str]]] = {field: {} for field in normalizers}
    audit_frequency: dict[str, Counter[str]] = {
        field: Counter(clean(row.get(field)) for row in master) for field in normalizers
    }
    audit_resolution: dict[tuple[str, str], tuple[list[str], str, list[str]]] = {}
    for row in master:
        study_id = clean(row["study_cluster_id"])
        for field, normalizer in normalizers.items():
            raw = clean(row.get(field))
            labels, mode, unresolved = normalizer(raw)
            normalized[field][study_id] = labels
            audit_resolution[(field, raw)] = (labels, mode, unresolved)

    if set(crosswalk_by_study) != set(study_ids):
        missing_in_crosswalk = sorted(set(study_ids) - set(crosswalk_by_study))
        extra_in_crosswalk = sorted(set(crosswalk_by_study) - set(study_ids))
        raise RuntimeError(
            "Phase-E per-study crosswalk does not match the Phase-D study universe: "
            f"missing={missing_in_crosswalk}, extra={extra_in_crosswalk}"
        )

    modality_by_study = {
        study_id: [clean(crosswalk_by_study[study_id].get("modality"))]
        for study_id in study_ids
    }
    maturity_by_study = {
        study_id: [clean(crosswalk_by_study[study_id].get("validation_maturity_max"))]
        for study_id in study_ids
    }
    data_by_study = {
        study_id: [clean(crosswalk_by_study[study_id].get("dataset_availability"))]
        for study_id in study_ids
    }
    code_by_study = {
        study_id: [clean(crosswalk_by_study[study_id].get("code_model_availability"))]
        for study_id in study_ids
    }
    six_g_by_study = {
        study_id: [clean(crosswalk_by_study[study_id].get("six_g"))]
        for study_id in study_ids
    }

    modality_rows = aggregate_study_labels(modality_by_study, MODALITY_CODES)
    integration_rows = aggregate_study_labels(normalized["integration_mechanism_codes"], INTEGRATION_CODES)
    validation_rows = aggregate_study_labels(normalized["validation_type_codes"], VALIDATION_CODES)
    application_rows = aggregate_study_labels(normalized["application_domain_codes"], APPLICATION_CODES)
    technology_rows = aggregate_study_labels(normalized["enabling_technology_codes"], TECHNOLOGY_CODES)
    six_g_rows = aggregate_study_labels(six_g_by_study, SIX_G_CODES)

    fallback_axes = {
        "integration_mechanism": normalized["integration_mechanism_codes"],
        "enabling_technology": normalized["enabling_technology_codes"],
        "application_domain": normalized["application_domain_codes"],
    }
    multi_label_axis_coverage = {
        axis: sum(bool(labels) for labels in by_study.values())
        for axis, by_study in fallback_axes.items()
    }
    fallback_other_counts = {
        axis: sum(set(labels) == {"other"} for labels in by_study.values())
        for axis, by_study in fallback_axes.items()
    }
    fallback_other_colabel_violations = {
        axis: sorted(
            study_id
            for study_id, labels in by_study.items()
            if "other" in labels and set(labels) != {"other"}
        )
        for axis, by_study in fallback_axes.items()
    }

    maturity_order = ("2", "3", "4", "5", "6")
    data_order = ("unavailable_or_NR", "on_request", "open", "NA")
    code_order = ("unavailable_or_NR", "on_request", "partial_components", "NA")
    maturity_rows = aggregate_study_labels(maturity_by_study, maturity_order)
    maturity_labels = {
        "2": "simulation_or_numerical",
        "3": "enhanced_simulation_or_dataset",
        "4": "laboratory_experiment_or_proof_of_concept",
        "5": "controlled_prototype",
        "6": "field_trial_or_deployment",
    }
    for row in maturity_rows:
        row["maturity_label"] = maturity_labels[str(row["category"])]
    data_rows = aggregate_study_labels(data_by_study, data_order)
    code_rows = aggregate_study_labels(code_by_study, code_order)

    ledger_by_record: dict[str, dict[str, str]] = {}
    duplicate_ledger_record_ids: list[str] = []
    for row in ledger:
        record_id = clean(row.get("record_id"))
        if record_id in ledger_by_record:
            duplicate_ledger_record_ids.append(record_id)
        ledger_by_record[record_id] = row

    primary_use_classes = {"eligible_quantitative", "eligible_qualitative"}

    def attach_ledger(source_rows: list[dict[str, str]], id_field: str) -> tuple[list[dict[str, str]], list[str]]:
        eligible: list[dict[str, str]] = []
        missing: list[str] = []
        for source_row in source_rows:
            record_id = clean(source_row.get(id_field))
            ledger_row = ledger_by_record.get(record_id)
            if ledger_row is None:
                missing.append(record_id)
                continue
            # Primary synthesis excludes both quarantine and context-only rows.
            # The latter remain visible in the inclusive governed-universe count.
            if clean(ledger_row.get("survey_use_class")) not in primary_use_classes:
                continue
            row = dict(source_row)
            row["_conditional"] = "1" if is_conditional_claim(ledger_row) else "0"
            row["_survey_use_class"] = clean(ledger_row.get("survey_use_class"))
            row["_claim_status"] = clean(ledger_row.get("claim_status"))
            eligible.append(row)
        return eligible, missing

    eligible_evidence, missing_evidence_ledger = attach_ledger(evidence, "evidence_id")
    eligible_metrics, missing_metric_ledger = attach_ledger(metrics, "metric_record_id")
    eligible_tradeoffs, missing_tradeoff_ledger = attach_ledger(tradeoffs, "tradeoff_id")

    metric_domain_rows = aggregate_claim_categories(eligible_metrics, "metric_domain")
    metric_family_rows = aggregate_claim_categories(eligible_metrics, "metric_family_code")

    for row in eligible_tradeoffs:
        row["_tradeoff_family"] = tradeoff_family(row)
    tradeoff_family_rows = aggregate_claim_categories(eligible_tradeoffs, "_tradeoff_family")

    use_classes = Counter(clean(row.get("survey_use_class")) for row in ledger)
    record_type_use_class = Counter(
        (clean(row.get("record_type")), clean(row.get("survey_use_class")))
        for row in ledger
    )
    actual_record_type_use_class_crosstab: dict[str, dict[str, int]] = defaultdict(dict)
    for (record_type, use_class), count in sorted(record_type_use_class.items()):
        actual_record_type_use_class_crosstab[record_type][use_class] = count
    actual_record_type_use_class_crosstab = dict(actual_record_type_use_class_crosstab)
    expected_record_type_use_class_crosstab = {
        "evidence": {"eligible_qualitative": 3020, "quarantined_conflict": 21},
        "metric": {
            "eligible_quantitative": 4779,
            "context_only": 31,
            "quarantined_conflict": 51,
        },
        "tradeoff": {"eligible_qualitative": 186, "eligible_quantitative": 218},
    }
    use_class_studies: dict[str, set[str]] = defaultdict(set)
    conditional_by_use = Counter()
    for row in ledger:
        use_class = clean(row.get("survey_use_class"))
        use_class_studies[use_class].add(clean(row.get("study_cluster_id")))
        if use_class != "quarantined_conflict" and is_conditional_claim(row):
            conditional_by_use[use_class] += 1
    claim_use_rows = []
    for use_class in ("eligible_quantitative", "eligible_qualitative", "context_only", "quarantined_conflict"):
        claim_use_rows.append(
            {
                "survey_use_class": use_class,
                "claim_count": use_classes[use_class],
                "unique_study_count": len({x for x in use_class_studies[use_class] if x}),
                "conditional_claim_subset": conditional_by_use[use_class],
                "included_in_inclusive_governed_universe": "no" if use_class == "quarantined_conflict" else "yes",
                "included_in_primary_synthesis": "yes" if use_class in primary_use_classes else "no",
            }
        )
    inclusive_nonquarantine_claims = len(ledger) - use_classes["quarantined_conflict"]
    primary_synthesis_claims = sum(use_classes[use_class] for use_class in primary_use_classes)
    conditional_inclusive_nonquarantine = sum(conditional_by_use.values())
    conditional_primary_synthesis = sum(
        conditional_by_use[use_class] for use_class in primary_use_classes
    )

    study_status = Counter(clean(row.get("survey_use_status")) for row in study_use)
    adjudication_tier = Counter(clean(row.get("adjudication_tier")) for row in study_use)
    independent_human = Counter(clean(row.get("independent_human_status")) for row in study_use)
    restriction_rows = [
        {
            "restriction_dimension": "study_survey_use_status",
            "category": category,
            "count": count,
            "denominator": len(study_use),
            "percent": pct(count, len(study_use)),
        }
        for category, count in sorted(study_status.items())
    ]
    restriction_rows += [
        {
            "restriction_dimension": "adjudication_tier",
            "category": category,
            "count": count,
            "denominator": len(study_use),
            "percent": pct(count, len(study_use)),
        }
        for category, count in sorted(adjudication_tier.items())
    ]
    restriction_rows += [
        {
            "restriction_dimension": "independent_human_status",
            "category": category,
            "count": count,
            "denominator": len(study_use),
            "percent": pct(count, len(study_use)),
        }
        for category, count in sorted(independent_human.items())
    ]
    restriction_rows += [
        {
            "restriction_dimension": "claim_restriction",
            "category": "quarantined_conflict_excluded",
            "count": use_classes["quarantined_conflict"],
            "denominator": len(ledger),
            "percent": pct(use_classes["quarantined_conflict"], len(ledger)),
        },
        {
            "restriction_dimension": "claim_restriction",
            "category": "context_only_excluded_from_primary_synthesis",
            "count": use_classes["context_only"],
            "denominator": inclusive_nonquarantine_claims,
            "percent": pct(use_classes["context_only"], inclusive_nonquarantine_claims),
        },
        {
            "restriction_dimension": "claim_restriction",
            "category": "conditional_inclusive_nonquarantined_subset",
            "count": conditional_inclusive_nonquarantine,
            "denominator": inclusive_nonquarantine_claims,
            "percent": pct(conditional_inclusive_nonquarantine, inclusive_nonquarantine_claims),
        },
        {
            "restriction_dimension": "claim_restriction",
            "category": "conditional_primary_synthesis_subset",
            "count": conditional_primary_synthesis,
            "denominator": primary_synthesis_claims,
            "percent": pct(conditional_primary_synthesis, primary_synthesis_claims),
        },
    ]

    audit_rows: list[dict[str, object]] = []
    for field in normalizers:
        for raw, frequency in sorted(audit_frequency[field].items(), key=lambda item: (-item[1], item[0])):
            labels, mode, unresolved = audit_resolution[(field, raw)]
            raw_tokens = {low(part).replace("-", "_").replace(" ", "_") for part in tokens(raw)}
            explicit_other = "other" in raw_tokens or any(part.startswith("other_") for part in raw_tokens)
            broad_fallback_only = set(labels) <= {"other", "other_optical", "unclear"}
            if explicit_other and "other" not in labels:
                audit_bucket = "other_explicit_token_audit_only"
            elif broad_fallback_only:
                audit_bucket = "fallback_other_or_unclear"
            elif unresolved:
                audit_bucket = "mapped_with_fine_grained_long_tail_preserved"
            else:
                audit_bucket = "controlled_or_fully_mapped"
            audit_rows.append(
                {
                    "field": field,
                    "raw_value": raw,
                    "raw_study_frequency": frequency,
                    "normalized_values": "|".join(labels),
                    "mapping_mode": mode,
                    "audit_bucket": audit_bucket,
                    "unresolved_fragments": "|".join(unresolved),
                    "blocking_for_current_synthesis": "no",
                }
            )

    # Audit the five exclusive dimensions exactly as supplied by Phase E. No
    # Phase-F classifier is called for these fields.
    exclusive_audit_fields = (
        ("primary_optical_modality_code", "modality_raw", "modality"),
        ("validation_maturity_max", "validation_raw", "validation_maturity_max"),
        ("dataset_availability_status", "dataset_availability_raw", "dataset_availability"),
        ("code_model_availability_status", "code_model_availability_raw", "code_model_availability"),
        ("six_g_relevance_code", "six_g_raw", "six_g"),
    )
    for field, raw_field, canonical_field in exclusive_audit_fields:
        grouped = Counter(
            (
                clean(row.get(raw_field)),
                clean(row.get(canonical_field)),
            )
            for row in crosswalk_studies
        )
        for (raw, canonical), frequency in sorted(
            grouped.items(), key=lambda item: (-item[1], item[0])
        ):
            audit_rows.append(
                {
                    "field": field,
                    "raw_value": raw,
                    "raw_study_frequency": frequency,
                    "normalized_values": canonical,
                    "mapping_mode": "phase_e_per_study_crosswalk_authoritative",
                    "audit_bucket": "phase_e_frozen_crosswalk",
                    "unresolved_fragments": "",
                    "blocking_for_current_synthesis": "no",
                }
            )

    # One compact S1-S7 index supports direct manuscript routing; detailed tables
    # remain in dedicated CSV files.
    top_modality = max(modality_rows, key=lambda row: int(row["study_count"]))
    top_integration = max(integration_rows, key=lambda row: int(row["study_count"]))
    top_metric_domain = max(metric_domain_rows, key=lambda row: int(row["unique_study_count"]))
    top_tradeoff = max(tradeoff_family_rows, key=lambda row: int(row["unique_study_count"]))
    top_maturity = max(maturity_rows, key=lambda row: int(row["study_count"]))
    top_tech = max(technology_rows, key=lambda row: int(row["study_count"]))
    top_app = max(application_rows, key=lambda row: int(row["study_count"]))
    six_g_direct = next(row for row in six_g_rows if row["category"] == "direct")
    synthesis_matrix = [
        {"section": "S1", "topic": "Optical modality taxonomy", "headline": f"{top_modality['category']}: {top_modality['study_count']}/206 ({top_modality['percent_of_206']}%)", "source_table": "s1_modality.csv", "denominator_note": "Mutually exclusive; sums to 206."},
        {"section": "S2", "topic": "Integration mechanisms", "headline": f"Most frequent: {top_integration['category']} in {top_integration['study_count']}/206 studies", "source_table": "s2_integration_mechanisms.csv", "denominator_note": "Multi-label; category counts may sum above 206."},
        {"section": "S3", "topic": "Metric reporting", "headline": f"Broadest study coverage: {top_metric_domain['category']} ({top_metric_domain['unique_study_count']} studies; {top_metric_domain['claim_count']} primary metric claims)", "source_table": "s3_metric_domains.csv; s3_metric_families.csv", "denominator_note": "Quarantined and context-only claims excluded; conditions shown separately."},
        {"section": "S4", "topic": "Tradeoff evidence", "headline": f"Most frequent derived family: {top_tradeoff['category']} ({top_tradeoff['unique_study_count']} studies; {top_tradeoff['claim_count']} primary claims)", "source_table": "s4_tradeoff_families.csv", "denominator_note": "Only primary eligible use classes included; one derived family per tradeoff claim."},
        {"section": "S5", "topic": "Validation maturity and openness", "headline": f"Largest maturity tier: {top_maturity['category']} ({top_maturity['study_count']}/206)", "source_table": "s5_validation_types.csv; s5_validation_maturity.csv; s5_open_data.csv; s5_open_code.csv", "denominator_note": "Maturity is mutually exclusive; validation type is multi-label."},
        {"section": "S6", "topic": "Enabling technology and applications", "headline": f"Top technology: {top_tech['category']} ({top_tech['study_count']}); top application: {top_app['category']} ({top_app['study_count']})", "source_table": "s6_enabling_technologies.csv; s6_application_domains.csv", "denominator_note": "Both are multi-label; totals may exceed 206."},
        {"section": "S7", "topic": "6G relevance and gaps", "headline": f"Direct 6G relevance: {six_g_direct['study_count']}/206 ({six_g_direct['percent_of_206']}%)", "source_table": "s7_six_g_relevance.csv; restriction_counts.csv", "denominator_note": "6G relevance is mutually exclusive and sums to 206."},
    ]

    output_tables: dict[str, list[dict[str, object]]] = {
        "s1_modality.csv": modality_rows,
        "s2_integration_mechanisms.csv": integration_rows,
        "s3_metric_domains.csv": metric_domain_rows,
        "s3_metric_families.csv": metric_family_rows,
        "s4_tradeoff_families.csv": tradeoff_family_rows,
        "s5_validation_types.csv": validation_rows,
        "s5_validation_maturity.csv": maturity_rows,
        "s5_open_data.csv": data_rows,
        "s5_open_code.csv": code_rows,
        "s6_enabling_technologies.csv": technology_rows,
        "s6_application_domains.csv": application_rows,
        "s7_six_g_relevance.csv": six_g_rows,
        "claim_use_counts.csv": claim_use_rows,
        "restriction_counts.csv": restriction_rows,
        "normalization_audit.csv": audit_rows,
        "phase_f_synthesis_matrix.csv": synthesis_matrix,
    }
    for filename, rows in output_tables.items():
        write_csv(OUTPUT_DIR / filename, rows)

    def distribution_from_rows(rows: list[dict[str, object]]) -> dict[str, int]:
        return {str(row["category"]): int(row["study_count"]) for row in rows}

    actual_exclusive_distributions = {
        "modality": distribution_from_rows(modality_rows),
        "validation_maturity_max": distribution_from_rows(maturity_rows),
        "dataset_availability": distribution_from_rows(data_rows),
        "code_model_availability": distribution_from_rows(code_rows),
        "six_g": distribution_from_rows(six_g_rows),
    }
    declared = crosswalk_payload.get("canonical_distributions_by_study", {})
    phase_e_declared_distributions = {
        "modality": {str(key): int(value) for key, value in declared.get("modality", {}).items()},
        "validation_maturity_max": {str(key): int(value) for key, value in declared.get("validation_maturity_max", {}).items()},
        "dataset_availability": {str(key): int(value) for key, value in declared.get("dataset_availability", {}).items()},
        "code_model_availability": {str(key): int(value) for key, value in declared.get("code_model_availability", {}).items()},
        "six_g": {str(key): int(value) for key, value in declared.get("six_g_relevance", {}).items()},
    }
    phase_e_exclusive_match = (
        actual_exclusive_distributions == EXPECTED_EXCLUSIVE_DISTRIBUTIONS
        and phase_e_declared_distributions == EXPECTED_EXCLUSIVE_DISTRIBUTIONS
    )

    checks = {
        "source_sha_matches_locked_value": actual_sha == EXPECTED_SOURCE_SHA256,
        "phase_e_crosswalk_sha_matches_locked_value": crosswalk_sha == EXPECTED_CROSSWALK_SHA256,
        "phase_e_crosswalk_rows_206": len(crosswalk_studies) == DENOMINATOR,
        "phase_e_crosswalk_ids_unique": not duplicate_crosswalk_ids,
        "phase_e_crosswalk_study_universe_matches_phase_d": set(crosswalk_by_study) == set(study_ids),
        "phase_e_crosswalk_internal_qa_pass": crosswalk_payload.get("qa", {}).get("pass") is True,
        "phase_e_declared_exclusive_distributions_match_expected": phase_e_declared_distributions == EXPECTED_EXCLUSIVE_DISTRIBUTIONS,
        "phase_f_exclusive_tables_match_expected_phase_e": actual_exclusive_distributions == EXPECTED_EXCLUSIVE_DISTRIBUTIONS,
        "exclusive_dimensions_match_phase_e_BLOCKING": phase_e_exclusive_match,
        "study_master_rows_206": len(master) == DENOMINATOR,
        "unique_study_clusters_206": len(set(study_ids)) == DENOMINATOR,
        "modality_mutually_exclusive_sum_206": sum(int(row["study_count"]) for row in modality_rows) == DENOMINATOR,
        "six_g_mutually_exclusive_sum_206": sum(int(row["study_count"]) for row in six_g_rows) == DENOMINATOR,
        "validation_maturity_mutually_exclusive_sum_206": sum(int(row["study_count"]) for row in maturity_rows) == DENOMINATOR,
        "open_data_mutually_exclusive_sum_206": sum(int(row["study_count"]) for row in data_rows) == DENOMINATOR,
        "open_code_mutually_exclusive_sum_206": sum(int(row["study_count"]) for row in code_rows) == DENOMINATOR,
        "s2_s6_multilabel_axes_cover_all_206_BLOCKING": all(
            len(fallback_axes[axis]) == DENOMINATOR
            and multi_label_axis_coverage[axis] == DENOMINATOR
            for axis in fallback_axes
        ),
        "other_is_fallback_only_no_colabels_BLOCKING": all(
            not violations for violations in fallback_other_colabel_violations.values()
        ),
        "fallback_other_counts_exact_BLOCKING": fallback_other_counts == EXPECTED_FALLBACK_OTHER_COUNTS,
        "study_status_sum_206": sum(study_status.values()) == DENOMINATOR,
        "ledger_rows_8306": len(ledger) == 8306,
        "claim_use_classes_sum_to_ledger": sum(use_classes.values()) == len(ledger),
        "record_type_use_class_crosstab_exact_BLOCKING": actual_record_type_use_class_crosstab == expected_record_type_use_class_crosstab,
        "quarantined_claims_72": use_classes["quarantined_conflict"] == 72,
        "inclusive_governed_nonquarantined_universe_8234": inclusive_nonquarantine_claims == 8234,
        "context_only_claims_31": use_classes["context_only"] == 31,
        "primary_synthesis_claims_8203_BLOCKING": primary_synthesis_claims == 8203,
        "primary_evidence_claims_3020": len(eligible_evidence) == 3020,
        "primary_metric_claims_4779_BLOCKING": len(eligible_metrics) == 4779,
        "primary_tradeoff_claims_404": len(eligible_tradeoffs) == 404,
        "primary_components_sum_to_8203": len(eligible_evidence) + len(eligible_metrics) + len(eligible_tradeoffs) == primary_synthesis_claims == 8203,
        "context_only_excluded_from_primary_metric_domains_BLOCKING": sum(int(row["context_only_claim_count"]) for row in metric_domain_rows) == 0,
        "context_only_excluded_from_primary_metric_families_BLOCKING": sum(int(row["context_only_claim_count"]) for row in metric_family_rows) == 0,
        "evidence_ledger_join_complete": not missing_evidence_ledger,
        "metric_ledger_join_complete": not missing_metric_ledger,
        "tradeoff_ledger_join_complete": not missing_tradeoff_ledger,
        "ledger_record_ids_unique": not duplicate_ledger_record_ids,
        "primary_metric_domain_claims_reconcile_4779": sum(int(row["claim_count"]) for row in metric_domain_rows) == len(eligible_metrics) == 4779,
        "primary_metric_family_claims_reconcile_4779": sum(int(row["claim_count"]) for row in metric_family_rows) == len(eligible_metrics) == 4779,
        "primary_tradeoff_family_claims_reconcile_404": sum(int(row["claim_count"]) for row in tradeoff_family_rows) == len(eligible_tradeoffs) == 404,
        "study_use_rows_206": len(study_use) == DENOMINATOR,
        "survey_ready_statuses_only": set(study_status) <= {"survey_ready", "survey_ready_with_claim_restrictions"},
        "independent_human_review_not_misrepresented": independent_human == Counter({"not_documented": DENOMINATOR}),
    }
    qa_status = "PASS" if all(checks.values()) else "FAIL"

    summary = {
        "package": "OISAC Phase-F S1-S7 publication-ready descriptive synthesis",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "workbook": str(SOURCE),
            "sha256": actual_sha,
            "expected_locked_sha256": EXPECTED_SOURCE_SHA256,
            "phase_e_crosswalk": str(CROSSWALK),
            "phase_e_crosswalk_sha256": crosswalk_sha,
            "expected_phase_e_crosswalk_sha256": EXPECTED_CROSSWALK_SHA256,
        },
        "scope_and_denominators": {
            "unique_study_clusters": len(set(study_ids)),
            "study_weighting_rule": "Each study_cluster_id contributes at most once to each category.",
            "mutually_exclusive_tables": ["s1_modality.csv", "s5_validation_maturity.csv", "s5_open_data.csv", "s5_open_code.csv", "s7_six_g_relevance.csv", "study survey_use_status"],
            "multi_label_tables": ["s2_integration_mechanisms.csv", "s5_validation_types.csv", "s6_enabling_technologies.csv", "s6_application_domains.csv"],
            "multi_label_warning": "Category totals in multi-label tables can exceed 206 and must not be interpreted as additional studies.",
            "multi_label_coverage": multi_label_axis_coverage,
            "fallback_other_semantics": "For integration, enabling technology, and application domain, other is assigned only when the study has no recognized category on that axis; unmatched co-occurring tokens are audit-only.",
            "fallback_other_counts": fallback_other_counts,
            "exclusive_dimension_authority": "Phase-E per_study_crosswalk is the sole authority for modality, validation_maturity_max, dataset_availability, code_model_availability, and six_g; Phase F does not reclassify these dimensions.",
            "exclusive_distributions": actual_exclusive_distributions,
        },
        "claim_governance": {
            "total_claims": len(ledger),
            "inclusive_governed_nonquarantined_universe": inclusive_nonquarantine_claims,
            "inclusive_universe_caution": "The 8,234 non-quarantined records include 31 context-only metrics and must not be reported as the primary evidence count.",
            "context_only_claims_excluded_from_primary_synthesis": use_classes["context_only"],
            "quarantined_claims_excluded_from_all_claim_based_numeric_results": use_classes["quarantined_conflict"],
            "primary_synthesis_claims": primary_synthesis_claims,
            "conditional_primary_synthesis_claims": conditional_primary_synthesis,
            "conditional_inclusive_nonquarantined_claims": conditional_inclusive_nonquarantine,
            "conditional_definition": "A claim is conditional when it is comparison-gated, source-guardrailed, conditionally admissible/comparable, marked caution, or allows cross-study quantitative comparison only with conditions.",
            "primary_evidence_claims": len(eligible_evidence),
            "primary_metric_claims": len(eligible_metrics),
            "primary_tradeoff_claims": len(eligible_tradeoffs),
            "record_type_use_class_crosstab": actual_record_type_use_class_crosstab,
        },
        "study_restrictions": {
            "survey_use_status": dict(sorted(study_status.items())),
            "adjudication_tier": dict(sorted(adjudication_tier.items())),
            "independent_human_status": dict(sorted(independent_human.items())),
            "provenance_caution": "Independent human PDF verification is not documented; these are AI-assisted/user-delegated survey-scope adjudications and must not be described as dual-independent-reviewer findings.",
        },
        "headline_tables": {
            "S1_modality": modality_rows,
            "S2_integration_mechanism": integration_rows,
            "S3_metric_domain": metric_domain_rows,
            "S4_tradeoff_family": tradeoff_family_rows,
            "S5_validation_type": validation_rows,
            "S5_validation_maturity": maturity_rows,
            "S5_open_data": data_rows,
            "S5_open_code": code_rows,
            "S6_enabling_technology": technology_rows,
            "S6_application_domain": application_rows,
            "S7_six_g_relevance": six_g_rows,
        },
        "normalization": {
            "method": "Phase-E per_study_crosswalk is copied without reclassification for the five mutually exclusive dimensions. Preserved Phase-F multi-label fields use deterministic field-specific keyword rules. Every raw-to-normalized mapping is recorded in normalization_audit.csv.",
            "audit_bucket_counts": dict(sorted(Counter(str(row["audit_bucket"]) for row in audit_rows).items())),
            "long_tail_rule": "Other is a fallback-only study label. A source-explicit other token that co-occurs with a recognized category is retained only in the other_explicit_token_audit_only bucket; fine-grained out-of-codebook fragments are likewise audit-only after broad mapping.",
            "phase_e_authoritative_exclusive_fields": ["modality", "validation_maturity_max", "dataset_availability", "code_model_availability", "six_g"],
            "phase_f_interpretive_outputs": ["integration mechanism broad mapping", "validation type multi-label mapping", "application domain mapping", "enabling technology mapping", "tradeoff family"],
        },
        "qa_status": qa_status,
        "qa_checks": checks,
    }
    write_json(OUTPUT_DIR / "phase_f_synthesis_summary.json", summary)

    md = f"""# OISAC Phase-F S1-S7 publication-ready numeric summary

**QA status:** {qa_status}
**Locked source SHA-256:** `{actual_sha}`
**Authoritative Phase-E crosswalk SHA-256:** `{crosswalk_sha}`
**Denominator:** 206 unique study clusters
**Claim governance:** The inclusive governed universe contains {inclusive_nonquarantine_claims:,} non-quarantined records, but this includes {use_classes['context_only']} context-only metrics. Primary synthesis therefore uses {primary_synthesis_claims:,} claims: {len(eligible_evidence):,} evidence, {len(eligible_metrics):,} metric, and {len(eligible_tradeoffs):,} tradeoff claims. The {use_classes['context_only']} context-only metrics and {use_classes['quarantined_conflict']} quarantined claims are excluded from primary numeric synthesis. Within the primary set, {conditional_primary_synthesis:,} claims meet the explicit conditional/guardrail definition and are shown as a subset, not as unconditional evidence.

## Reading rule

Modality, validation maturity, open-data status, open-code status, and 6G relevance come only from the frozen Phase-E `per_study_crosswalk`; Phase F does not reclassify them. These fields and study status are mutually exclusive and each reconciles to 206. A mismatch with Phase E is a blocking QA failure. Integration mechanisms, validation types, enabling technologies, and application domains are multi-label: their category totals can exceed 206 because one study can contribute to several categories. For integration, enabling technology, and application domain, `other` is used only when a study has no recognized category on that axis; unmatched co-occurring tokens remain audit-only. Each of these axes still covers all 206 studies. Metric-domain/family and tradeoff tables report both claim counts and unique-study counts; summing unique-study counts across categories double-counts multi-topic studies.

## S1 — Optical modality

{markdown_table(modality_rows, [('category', 'Modality'), ('study_count', 'Studies'), ('percent_of_206', '% of 206')])}

## S2 — Integration mechanisms

{markdown_table(integration_rows, [('category', 'Mechanism'), ('study_count', 'Studies'), ('percent_of_206', '% of 206')])}

## S3 — Metric domains

{markdown_table(metric_domain_rows, [('category', 'Metric domain'), ('unique_study_count', 'Studies'), ('claim_count', 'Primary metric claims'), ('conditional_claim_count', 'Conditional subset')])}

The complete 2,000+ family vocabulary is retained in `s3_metric_families.csv`; no semantic collapse of source-specific metric families was imposed. Both S3 tables exclude the 31 context-only metric rows as well as quarantined rows.

## S4 — Derived tradeoff families

{markdown_table(tradeoff_family_rows, [('category', 'Tradeoff family'), ('unique_study_count', 'Studies'), ('claim_count', 'Primary claims'), ('conditional_claim_count', 'Conditional subset')])}

## S5 — Validation maturity

{markdown_table(maturity_rows, [('category', 'Maturity tier'), ('maturity_label', 'Phase-E label'), ('study_count', 'Studies'), ('percent_of_206', '% of 206')])}

### Open data

{markdown_table(data_rows, [('category', 'Data status'), ('study_count', 'Studies'), ('percent_of_206', '% of 206')])}

### Open code/model

{markdown_table(code_rows, [('category', 'Code/model status'), ('study_count', 'Studies'), ('percent_of_206', '% of 206')])}

## S6 — Enabling technologies

{markdown_table(technology_rows, [('category', 'Technology'), ('study_count', 'Studies'), ('percent_of_206', '% of 206')])}

## S6 — Application domains

{markdown_table(application_rows, [('category', 'Application'), ('study_count', 'Studies'), ('percent_of_206', '% of 206')])}

## S7 — 6G relevance

{markdown_table(six_g_rows, [('category', '6G relevance'), ('study_count', 'Studies'), ('percent_of_206', '% of 206')])}

## Restrictions and provenance boundary

Study use status is {study_status.get('survey_ready', 0)} `survey_ready` and {study_status.get('survey_ready_with_claim_restrictions', 0)} `survey_ready_with_claim_restrictions`, reconciling to 206. Independent human verification status is `not_documented` for all 206 studies. These outputs therefore must be described as AI-assisted/user-delegated survey-scope adjudication, not as dual-independent-reviewer verification.

The five exclusive S1/S5/S7 dimensions are copied per study from Phase E and are marked `phase_e_frozen_crosswalk` in `normalization_audit.csv`. Phase-F normalization of the preserved multi-label fields is deterministic and fully exposed there. Source-explicit `other` tokens that accompany a recognized category are marked `other_explicit_token_audit_only` and do not inflate the `other` study count; true fallback studies remain `fallback_other_or_unclear`. Fine-grained long-tail fragments remain visible after broad mapping. None of these audit buckets silently admits a quarantined claim. The locked Phase-D workbook and Phase-E crosswalk were read only and were not changed.
"""
    (OUTPUT_DIR / "PHASE_F_S1_S7_PUBLICATION_SUMMARY.md").write_text(md, encoding="utf-8", newline="\n")

    # Manifest covers all deliverables except QA_REPORT itself to avoid a circular hash.
    manifest_files = sorted(
        path for path in OUTPUT_DIR.iterdir()
        if path.is_file() and path.name not in {"QA_REPORT.json"}
    )
    qa_payload = {
        "status": qa_status,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_workbook": str(SOURCE),
        "source_sha256": actual_sha,
        "expected_source_sha256": EXPECTED_SOURCE_SHA256,
        "phase_e_crosswalk": str(CROSSWALK),
        "phase_e_crosswalk_sha256": crosswalk_sha,
        "expected_phase_e_crosswalk_sha256": EXPECTED_CROSSWALK_SHA256,
        "exclusive_dimension_authority": "PHASE_E per_study_crosswalk only",
        "expected_exclusive_distributions": EXPECTED_EXCLUSIVE_DISTRIBUTIONS,
        "phase_e_declared_exclusive_distributions": phase_e_declared_distributions,
        "phase_f_output_exclusive_distributions": actual_exclusive_distributions,
        "expected_record_type_use_class_crosstab": expected_record_type_use_class_crosstab,
        "actual_record_type_use_class_crosstab": actual_record_type_use_class_crosstab,
        "expected_fallback_other_counts": EXPECTED_FALLBACK_OTHER_COUNTS,
        "actual_fallback_other_counts": fallback_other_counts,
        "multi_label_axis_coverage": multi_label_axis_coverage,
        "fallback_other_colabel_violations": fallback_other_colabel_violations,
        "counts": {
            "studies": len(master),
            "evidence_rows": len(evidence),
            "metric_rows": len(metrics),
            "tradeoff_rows": len(tradeoffs),
            "ledger_rows": len(ledger),
            "conflict_register_rows": len(conflicts),
            "primary_evidence_claims": len(eligible_evidence),
            "primary_metric_claims": len(eligible_metrics),
            "primary_tradeoff_claims": len(eligible_tradeoffs),
            "primary_synthesis_claims": primary_synthesis_claims,
            "inclusive_governed_nonquarantined_claims": inclusive_nonquarantine_claims,
            "context_only_claims_excluded_from_primary": use_classes["context_only"],
            "quarantined_claims": use_classes["quarantined_conflict"],
            "conditional_primary_synthesis_claims": conditional_primary_synthesis,
            "conditional_inclusive_nonquarantined_claims": conditional_inclusive_nonquarantine,
        },
        "checks": checks,
        "join_diagnostics": {
            "missing_evidence_ledger_ids": missing_evidence_ledger,
            "missing_metric_ledger_ids": missing_metric_ledger,
            "missing_tradeoff_ledger_ids": missing_tradeoff_ledger,
            "duplicate_ledger_record_ids": duplicate_ledger_record_ids,
            "duplicate_phase_e_crosswalk_ids": duplicate_crosswalk_ids,
        },
        "output_manifest_sha256": {path.name: sha256_file(path) for path in manifest_files},
    }
    write_json(OUTPUT_DIR / "QA_REPORT.json", qa_payload)

    print(json.dumps({"status": qa_status, "output_dir": str(OUTPUT_DIR), "counts": qa_payload["counts"]}, indent=2))
    return 0 if qa_status == "PASS" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - command-line failure reporting
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
