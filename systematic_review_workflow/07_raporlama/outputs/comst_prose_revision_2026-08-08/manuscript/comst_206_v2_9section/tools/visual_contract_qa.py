#!/usr/bin/env python3
"""Reproducible gate for the v2 nine-section visual/table contract.

The central placement contract and the future-production comment blocks in the
section TeX files are the authorities checked here.  This script does not build
visual assets and does not alter TeX.  It writes a machine-readable JSON report
and a compact Markdown report, then exits nonzero whenever any gate fails.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence


CONTRACT_REL = Path("02_VISUAL_AND_TABLE_PLACEMENT_CONTRACT.md")
DEFAULT_JSON_REL = Path("qa/FINAL_VISUAL_CONTRACT_QA.json")
DEFAULT_MD_REL = Path("qa/FINAL_VISUAL_CONTRACT_QA.md")


@dataclass(frozen=True)
class GateSpec:
    key: str
    description: str
    patterns: tuple[str, ...]
    mode: str = "all"


@dataclass(frozen=True)
class CarrierSpec:
    order: int
    visible: str
    carrier_id: str
    kind: str
    section: str
    source_rel: Path
    label: str
    expected_contract_status: str
    marker_pattern: str | None = None
    blueprint_id: str | None = None
    critical_gates: tuple[GateSpec, ...] = field(default_factory=tuple)


def gate(key: str, description: str, *patterns: str, mode: str = "all") -> GateSpec:
    return GateSpec(key, description, tuple(patterns), mode)


def rnum(value: str) -> str:
    """Regex for a display integer, accepting an optional thousands comma."""
    return re.escape(value).replace(r"\,", ",?")


SECTION_1 = Path("sections/01_INTRODUCTION.tex")
SECTION_2 = Path("sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex")
SECTION_3 = Path("sections/03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex")
SECTION_4 = Path("sections/04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex")
SECTION_5 = Path("sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex")
SECTION_6 = Path("sections/06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex")
SECTION_7 = Path("sections/07_ENABLING_TECHNOLOGIES_APPLICATIONS_AND_6G.tex")
SECTION_8 = Path("sections/08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex")


CARRIERS: tuple[CarrierSpec, ...] = (
    CarrierSpec(
        1,
        "Table I",
        "table_i_prior_surveys",
        "table",
        "I",
        SECTION_1,
        "tab:prior_surveys",
        "Implemented in TeX; layout pending",
    ),
    CarrierSpec(
        2,
        "Fig. 1",
        "figure_1_native_evidence",
        "figure",
        "II",
        SECTION_2,
        "fig:native_evidence_objects",
        "Blueprint only",
        r"^%\s+FUTURE FIGURE 1\b",
        "FIG-OISAC-RS1",
        (
            gate("denominator", "Conceptual carrier has no prevalence denominator.", r"no prevalence denominator"),
            gate("layout", "Three evidence objects are equal, parallel, and unconnected.", r"three equal, parallel, and unconnected"),
            gate("objects", "All three native evidence-object types are named.", r"model-defined result", r"medium-native observation", r"architecture or deployment object"),
            gate("nonduplication", "The block forbids repetition of Table I families/sources and arrows.", r"do not repeat the six reader-task families or individual sources", r"do not connect the panels with arrows"),
        ),
    ),
    CarrierSpec(
        3,
        "Fig. 2",
        "figure_2_comparison_framework",
        "figure",
        "II",
        SECTION_2,
        "fig:comparison_framework",
        "Blueprint only",
        r"^%\s+FUTURE FIGURE 2\b",
        "FIG-OISAC-01",
        (
            gate("denominator", "The framework is explicitly conceptual and denominator-free.", r"conceptual model, no denominator"),
            gate("axes", "Four equal axes feed one candidate comparison record.", r"four equal axes feeding\s+one candidate comparison record", r"physical context", r"coupling location", r"measurement contract", r"provenance"),
            gate("outcomes", "The gate has exactly the three permitted uses.", r"three equal outcomes", r"within-study\s+interpretation", r"conditional cross-study relation", r"descriptive only"),
            gate("missingness", "Missing fields remain unknown and are not inferred.", r"missing field\s*=\s*unknown; never infer"),
            gate("no_unconditional", "No unconditional cross-platform outcome exists.", r"no unconditional cross-platform comparison category exists"),
            gate("nonduplication", "Figure 2 owns the decision path and Table II owns fields.", r"figure 2 shows the decision path; table ii defines the fields"),
        ),
    ),
    CarrierSpec(
        4,
        "Table II",
        "table_ii_comparison_record",
        "table",
        "II",
        SECTION_2,
        "tab:comparison_record",
        "Blueprint only",
        r"^%\s+FUTURE TABLE II\b",
        "T-02",
        (
            gate("unit", "The row unit is a record field, not a study.", r"row unit is one record field, not one study"),
            gate("field_contract", "The table retains approximately 17 rows in five groups.", r"approximately 17 ordered field rows in five groups"),
            gate("states", "Controlled requirement and missingness states are explicit.", r"required, conditionally required, not applicable", r"missing tokens are nr, na, or unclear, never a\s+blank"),
            gate("provenance", "All four value-provenance states are preserved.", r"reported, source calculated, source digitized,\s+and source derived"),
            gate("failure_and_use", "Columns state the failure consequence and required use.", r"why comparison fails if absent or misaligned", r"required for"),
            gate("outcomes", "Uses match Figure 2 and remain conditional/descriptive.", r"within-study interpretation", r"conditional cross-study\s+relation", r"descriptive only", r"no unconditional comparison category"),
        ),
    ),
    CarrierSpec(
        5,
        "Fig. 3",
        "figure_3_prisma_flow",
        "figure",
        "III",
        SECTION_3,
        "fig:prisma_report_study_flow",
        "Locked source visual pending placement",
        r"^%\s+FUTURE FIGURE 3\b",
        "FIG-OISAC-02",
        (
            gate("denominators", "Records, reports, and unique-study denominators remain distinct.", r"native denominators are records, reports, and unique studies"),
            gate("main_path", "The locked PRISMA main path is complete.", r"1,?733 records identified\s*->\s*1,?259 screened\s*->\s*330 unique reports sought\s*->\s*272 full-text reports assessed\s*->\s*227 eligible reports\s*->\s*206 unique studies"),
            gate("side_branches", "All required exclusion/context/retrieval branches are retained.", r"472 duplicates and 2 other", r"864 title and abstract exclusions, 61 contextual records, and 2 duplicate", r"58 reports not retrieved", r"39 full-text exclusions and 6 full-text contextual assignments"),
            gate("context_reconciliation", "The 67-record contextual corpus is reconciled as 61+6.", r"67-record contextual corpus equals 61 plus 6"),
            gate("report_study_delta", "The 227-to-206 difference is consolidation, not exclusion.", r"report-to-study difference of 21 is companion or related-report\s+consolidation, not exclusion"),
            gate("predecessor", "The 221-study predecessor stays outside attrition.", r"221-study osf snapshot outside the flow", r"never\s+draw an attrition arrow from 221 to 206"),
            gate("alias_boundary", "The 332 historical queue is not confused with 330 reports.", r"do not merge the 332 historical source queue with the 330 unique reports"),
        ),
    ),
    CarrierSpec(
        6,
        "Table III",
        "table_iii_evidence_reconciliation",
        "table",
        "III",
        SECTION_3,
        "tab:evidence_reconciliation",
        "Blueprint only",
        r"^%\s+FUTURE TABLE III\b",
        "T-03",
        (
            gate("panels", "Disposition and record-type/audit partitions remain in two panels.", r"this two-panel evidence-reconciliation design", r"panel a row unit", r"panel b row unit"),
            gate("governed_total", "The 8,306 governed universe reconciliation is exact.", r"3,?206\s*\+\s*4,?997\s*\+\s*31\s*\+\s*72\s*=\s*8,?306"),
            gate("primary_total", "The 8,203 primary record types are explicit.", r"3,?020 evidence records", r"4,?779 metric records", r"404 tradeoff-ledger records", r"8,?203 primary total"),
            gate("substantive_tradeoffs", "Governed and substantive tradeoff counts remain distinct.", r"402 tradeoff records from 168 studies are substantive", r"keep 404 governed tradeoff-ledger rows distinct from 402 substantive rows"),
            gate("audit_events", "The external 93-event register stays distinct from 72 quarantined claims.", r"93 conflict-register audit events", r"93 audit events are outside both record-type totals", r"keep 93 audit events distinct from 72 quarantined claims"),
            gate("percentage_denominator", "Every percentage must carry its denominator.", r"every percentage must print its denominator"),
        ),
    ),
    CarrierSpec(
        7,
        "Fig. 4",
        "figure_4_tqaf_profile",
        "figure",
        "III",
        SECTION_3,
        "fig:tqaf_profile",
        "Blueprint only",
        r"^%\s+FUTURE FIGURE 4\b",
        "FIG-OISAC-03",
        (
            gate("structure", "Eight TQAF dimensions and a separate overall row are required.", r"eight tqaf\s+dimensions", r"separate overall evidence-contribution bar", r"it is not a ninth dimension"),
            gate("counts", "All eight dimension triplets and the overall triplet are locked.", r"123/68/15", r"168/7/31", r"196/10/0", r"153/44/9", r"6/168/32", r"3/199/4", r"0/158/48", r"4/10/192", r"125/75/6"),
            gate("denominator", "Every bar uses the 206-study denominator.", r"use the 206-study denominator for every bar"),
            gate("interpretation_boundary", "TQAF is not relabeled as risk of bias or GRADE.", r"do not call these scores risk of bias or grade certainty"),
            gate("nonduplication", "Validation tiers and evidence-body certainty remain outside Figure 4.", r"do not mix maximum validation tiers or evidence-body certainty"),
        ),
    ),
    CarrierSpec(
        8,
        "Table IV",
        "table_iv_modality_map",
        "table",
        "IV",
        SECTION_4,
        "tab:modality_map",
        "Blueprint only",
        r"^%\s+FUTURE TABLE IV\b",
        "T-04",
        (
            gate("denominator", "The denominator is 206 unique studies.", r"denominator 206 unique studies"),
            gate("rows", "All six mutually exclusive platform rows and counts are fixed.", r"exactly one canonical family, ordered 69 photonics assisted thz,\s+56 fiber, 38 vlc/lifi, 31 fso, 9 hybrid optical, and 3 other optical"),
            gate("columns", "Physical path, observables, roles, constraints, boundary, and citations are required.", r"target-facing path or perturbation location", r"recurring sensing\s+observables or tasks", r"communication role", r"active\s+physical and implementation constraints", r"numerical transfer boundary", r"representative citations"),
            gate("counting_rule", "Family counts are exclusive while coupling descriptions are multilabel.", r"counts are mutually exclusive; coupling\s+locations are descriptive and multilabel"),
            gate("sum", "The six canonical counts reconcile to 206.", r"69", r"56", r"38", r"31", r"9", r"3"),
        ),
    ),
    CarrierSpec(
        9,
        "Fig. 5",
        "figure_5_integration_map",
        "figure",
        "IV",
        SECTION_4,
        "fig:integration_map",
        "Blueprint only",
        r"^%\s+FUTURE FIGURE 5\b",
        "FIG-OISAC-04",
        (
            gate("denominator", "The 206-study mechanism census is explicitly multilabel.", r"denominator 206, multilabel"),
            gate("chain", "A generic source-to-service chain carries parallel lanes.", r"generic left-to-right system chain with parallel communication and\s+sensing lanes", r"source/front end\s*->.*service/application"),
            gate("bands", "All seven equal coupling bands and counts are retained.", r"seven equal coupling bands", r"shared hardware 117", r"optical carrier 49", r"waveform 113", r"resource allocation 118", r"link or channel 87", r"joint design or optimization 72", r"application scenario 46"),
            gate("mixed_boundary", "Three mixed boundary cases remain an audit callout.", r"three mixed boundary cases as a separate\s+audit callout"),
            gate("encoding", "Counts use fixed badges and cannot be summed or read as maturity.", r"badge size\s+remains constant", r"counts must not be summed", r"node order shows location, not frequency or maturity"),
        ),
    ),
    CarrierSpec(
        10,
        "Table V",
        "table_v_metric_admissibility",
        "table",
        "V",
        SECTION_5,
        "tab:metric_admissibility",
        "Blueprint only",
        r"^%\s+FUTURE TABLE V\b",
        "T-05",
        (
            gate("lineage", "Raw-to-primary metric lineage is exact.", r"4,?861 raw metric\s+rows minus 31 context-only and 51 quarantined-conflict rows\s*=\s*4,?779 primary"),
            gate("denominators", "Record and study denominators remain distinct and multilabel.", r"record n/4,?779", r"study n/206", r"study coverage uses 206 and is multilabel"),
            gate("domain_reconciliation", "Leading domains plus residual reconcile to 4,779.", r"sensing 1,?816, communication 1,?328, joint 870, and implementation 476 total\s+4,?490", r"4,?490\s*\+\s*289\s*=\s*4,?779"),
            gate("study_coverage", "Study coverage counts are nonadditive.", r"study counts 203, 194,\s+158, and 64 must not be summed"),
            gate("panels", "Metric census, semantic classes, and admissibility remain three panels.", r"panel a:", r"panel b:", r"panel c:"),
            gate("admissibility", "Only conditional yes/no outcomes are allowed.", r"118\W*yes with conditions\W* and 4,?661\W+no\W* records; no unconditional yes"),
        ),
    ),
    CarrierSpec(
        11,
        "Fig. 6",
        "figure_6_tradeoff_profile",
        "figure",
        "V",
        SECTION_5,
        "fig:tradeoff_profile",
        "Blueprint only",
        r"^%\s+FUTURE FIGURE 6\b",
        "FIG-OISAC-05",
        (
            gate("lineage", "Governed and substantive tradeoff lineages are both explicit.", r"404 governed rows/169 studies/373 conditional rows", r"402 substantive records,\s+168 studies, and 371 conditional substantive records"),
            gate("panels", "The profile has three aligned, semantically distinct panels.", r"three aligned panels", r"panel a uses stacked horizontal bars", r"panel b uses lollipops", r"panel c\s+plots conditional share"),
            gate("record_types", "Quantitative and qualitative substantive records sum to 402.", r"218 quantitative and 184 qualitative"),
            gate("study_overlap", "The 168-study union is overlapping and nonadditive.", r"overall union is 168 and family counts must not be summed"),
            gate("conditionality", "The substantive conditional denominator is 371/402.", r"371 of 402 records are conditional", r"92\.3%\s+overall"),
            gate("bandwidth_correction", "Bandwidth/resource family values use the sentinel-corrected counts.", r"50\s*\+\s*44\s*=\s*94", r"70 studies", r"89 conditional"),
            gate("qualitative_correction", "Qualitative/partial family values use the sentinel-corrected counts.", r"2\s*\+\s*8\s*=\s*10", r"8 studies", r"7 conditional"),
            gate("interpretation_boundary", "Frequency is not effect strength or a universal Pareto frontier.", r"frequency is not effect strength", r"do not define a common design space or universal pareto frontier"),
        ),
    ),
    CarrierSpec(
        12,
        "Fig. 7",
        "figure_7_validation_profile",
        "figure",
        "VI",
        SECTION_6,
        "fig:validation_profile",
        "Blueprint only",
        r"^%\s+PLANNED FIGURE 7\b",
        "FIG-OISAC-06",
        (
            gate("denominator", "Panel A is exclusive, Panel B multilabel, denominator 206.", r"denominator 206\. panel a is exclusive and panel b is multilabel"),
            gate("panels", "Exactly two aligned panels are allowed.", r"exactly two aligned panels"),
            gate("maximum_tiers", "Maximum validation tiers and the at-least-lab total are exact.", r"32 basic simulation/numerical", r"18 enhanced simulation/dataset-supported", r"78 laboratory/poc", r"66 controlled prototype", r"12 field/deployment", r"156 studies reached at least laboratory/poc"),
            gate("methods", "All multilabel validation-method counts are retained.", r"analytical 131", r"numerical analysis 14", r"simulation 104", r"dataset based 13", r"laboratory experiment 148", r"prototype/testbed 83", r"field experiment 12", r"mixed\s+validation 33", r"unclear 0"),
            gate("denominator_callout", "The 148-method and 78-maximum-tier denominators are distinguished.", r"148 laboratory methods is not the same\s+denominator as 78 maximum-laboratory studies"),
            gate("no_third_panel", "Paired-function evidence remains outside a third panel.", r"keep paired-function evidence in prose and supplement s7, not a third panel"),
            gate("nonduplication", "Artifacts and TQAF remain in Table VI and Figure 4.", r"keep artifact availability in table vi and tqaf validation in figure 4"),
        ),
    ),
    CarrierSpec(
        13,
        "Table VI",
        "table_vi_artifact_reconstruction",
        "table",
        "VI",
        SECTION_6,
        "tab:artifact_reconstruction",
        "Blueprint only",
        r"^%\s+PLANNED TABLE VI\b",
        "T-06",
        (
            gate("denominators", "Availability uses n=206; reconstruction has no prevalence denominator.", r"panel a denominator 206", r"panel b is a controlled contract with no prevalence denominator"),
            gate("data_status", "All source-reported data statuses are exact.", r"data rows are unavailable\s+or not reported 145, on request 41, open 13, na 7"),
            gate("code_status", "All source-reported code/model statuses are exact.", r"code/model rows are\s+unavailable or not reported 197, on request 7, partial 1, na 1"),
            gate("reconstruction_contract", "Panel B contains nine controlled reconstruction requirements.", r"nine rows: system\s+configuration", r"hardware and photonic components", r"geometry, channel, and\s+environment", r"calibration", r"waveform and resource parameters", r"processing and\s+algorithms", r"metric definitions and reference planes", r"raw or intermediate\s+data", r"version, license, and preservation information"),
            gate("access_boundary", "Reported access is not treated as receipt or executability.", r"on request does\s+not mean received", r"open does not mean complete or executable"),
            gate("audit_boundary", "The table does not imply universal retesting or common execution.", r"links were\s+not universally retested and artifacts were not executed under a common\s+protocol"),
            gate("nonduplication", "TQAF reproducibility is not redrawn or rescored.", r"do not redraw\s+the tqaf reproducibility profile or assign retrospective pass/fail scores"),
        ),
    ),
    CarrierSpec(
        14,
        "Fig. 8",
        "figure_8_technology_application_chain",
        "figure",
        "VII",
        SECTION_7,
        "fig:technology_application_chain",
        "Blueprint only",
        r"^%\s+PLANNED FIGURE 8\b",
        "FIG-OISAC-07",
        (
            gate("denominator", "Technology/application counts are multilabel and the 6G gate is exclusive over 206.", r"technology and\s+application counts are multilabel; the 6g relevance gate is exclusive over\s+206 studies"),
            gate("layers", "The cross-layer map contains exactly six named layers.", r"six left-to-right layers", r"1\. generation and transport", r"2\. waveform and physical observables", r"3\. spatial control and multiplicity", r"4\. inference and system model", r"5\. application requirement bundles", r"6\. 6g evidence gate"),
            gate("generation_counts", "Generation/transport counts are retained.", r"photonic thz 68", r"coherent optics 64", r"photonic\s+integration 20", r"fiber das/infrastructure reuse 22", r"other 19"),
            gate("waveform_counts", "FMCW/chirped and OFDM/multicarrier counts are retained.", r"fmcw/chirped 66", r"ofdm/multicarrier 56"),
            gate("spatial_counts", "Spatial-control counts are retained.", r"beamforming 13", r"opa 11", r"mimo 7", r"ris/oris 2"),
            gate("inference_counts", "Inference-layer ML/AI and digital-twin counts are retained.", r"ml/ai 20 and digital twin 2"),
            gate("six_g_gate", "The exclusive S7 relevance partition is 138/64/1/3.", r"direct 138, inferential 64, weak 1, not applicable 3", r"138/64/1/3"),
            gate("encoding", "Counts do not become Sankey widths, co-occurrence, or causal arrows.", r"arrow width never encodes counts", r"do not draw a sankey", r"arrows do not\s+encode co-occurrence or causal influence"),
            gate("readiness_boundary", "6G framing is not compliance or readiness.", r"6g framing is not conformance,\s+interoperability, or deployment readiness"),
        ),
    ),
    CarrierSpec(
        15,
        "Table VII",
        "table_vii_application_requirements",
        "table",
        "VII",
        SECTION_7,
        "tab:application_requirements",
        "Blueprint only",
        r"^%\s+PLANNED TABLE VII\b",
        "T-07",
        (
            gate("denominator", "Application counts use n=206 and are multilabel.", r"denominator 206,\s+multilabel"),
            gate("rows", "All 13 Phase-F application rows and counts are fixed.", r"13 phase f application domains", r"6g/access 100", r"environmental monitoring 55", r"vehicular 41", r"smart\s+infrastructure 41", r"industrial 34", r"optical access network 32", r"security/surveillance 26", r"indoor positioning 25", r"aerospace 20", r"healthcare 8", r"datacenter 4", r"underwater 2", r"other 15"),
            gate("columns", "The ten-column operating-requirement contract is complete.", r"requirement cluster", r"application domain", r"n/206 and percent", r"target/event and sensing role", r"communication/service role", r"geometry/environment", r"dominant operating requirements", r"safety, privacy, or\s+deployment constraint", r"representative evidence", r"interpretation boundary"),
            gate("nonadditivity", "All 13 domains are included and not summed.", r"include all 13 domains and their audited counts; do not sum them"),
            gate("six_g_boundary", "6G/access is distinct from exclusive S7 relevance.", r"keep 6g/access distinct from s7 relevance"),
            gate("threshold_boundary", "No uniform performance/safety thresholds are invented.", r"do not invent uniform latency, reliability, privacy, or safety thresholds"),
        ),
    ),
    CarrierSpec(
        16,
        "Table VIII",
        "table_viii_research_roadmap",
        "table",
        "VIII",
        SECTION_8,
        "tab:research_roadmap",
        "Blueprint only",
        r"^%\s+PLANNED TABLE VIII\b",
        "T-08",
        (
            gate("denominators", "Numeric traces retain local denominators; recommendations have no prevalence total.", r"each numeric trace retains\s+its local denominator; the five recommendations have no prevalence total"),
            gate("columns", "The roadmap has the required nine columns.", r"priority\s*\|\s*observed evidence gap\s*\|\s*evidence trace\s*\|\s*required action or\s+protocol change\s*\|\s*modality-specific stress test\s*\|\s*required baselines and\s+varied controls\s*\|\s*success criterion\s*\|\s*required artifact or output\s*\|\s*dependency or risk"),
            gate("rows", "Exactly five dependency-ordered priorities are specified.", r"exactly five rows in dependency order", r"make the measurement contract routine", r"build modality-aware benchmarks", r"test joint operation under realistic\s+disturbance", r"release the artifacts that define the experiment", r"evaluate\s+intelligence, scale, and security as system properties"),
            gate("action_contract", "Every row links trace, action, stress, baselines, success, artifact, and dependency.", r"every row must point\s+backward to an observed result", r"communication-only and sensing-only baselines", r"externally testable success criterion", r"required artifact", r"prerequisite or failure risk"),
            gate("recommendation_boundary", "Recommendations are not written as already tested results.", r"must\s+not be written as interventions already tested by this review"),
            gate("nonduplication", "The roadmap avoids generic lists, unsupported dates, and ranks.", r"do not add generic topic lists", r"do not assign deadlines, maturity scores, or priority ranks"),
        ),
    ),
)


EXPECTED_VISIBLE_ORDER = [carrier.visible for carrier in CARRIERS]
EXPECTED_LABELS = [carrier.label for carrier in CARRIERS]
PENDING_CARRIERS = [carrier for carrier in CARRIERS if carrier.order != 1]
SECTION_SCAN_ORDER = [SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5, SECTION_6, SECTION_7, SECTION_8]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.casefold()).strip()


def strip_tex_comments(text: str) -> str:
    kept: list[str] = []
    for line in text.splitlines():
        escaped = False
        cut = len(line)
        for index, char in enumerate(line):
            if char == "%" and not escaped:
                cut = index
                break
            escaped = char == "\\" and not escaped
            if char != "\\":
                escaped = False
        kept.append(line[:cut])
    return "\n".join(kept)


def line_number(text: str, pattern: str) -> int | None:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    return None if match is None else text.count("\n", 0, match.start()) + 1


def parse_contract_rows(text: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 7:
            continue
        rows.append(
            {
                "order": int(cells[0]),
                "visible": cells[1],
                "placement": cells[2],
                "reader_question": cells[3],
                "core_content": cells[4],
                "nonduplication": cells[5],
                "status": cells[6],
                "line": number,
            }
        )
    return rows


def extract_comment_block(text: str, marker_pattern: str) -> tuple[str, int] | None:
    lines = text.splitlines()
    starts = [i for i, line in enumerate(lines) if re.search(marker_pattern, line, re.IGNORECASE)]
    if len(starts) != 1:
        return None
    start = starts[0]
    block: list[str] = []
    for line in lines[start:]:
        if line.lstrip().startswith("%") or not line.strip():
            block.append(line)
            continue
        break
    return "\n".join(block), start + 1


def comment_payload(block: str) -> str:
    payload: list[str] = []
    for line in block.splitlines():
        if line.lstrip().startswith("%"):
            payload.append(re.sub(r"^\s*%\s?", "", line))
        else:
            payload.append("")
    return "\n".join(payload)


def extract_comment_field(payload: str, heading_pattern: str, stop_patterns: Sequence[str]) -> str:
    lines = payload.splitlines()
    for index, line in enumerate(lines):
        match = re.match(heading_pattern, line, flags=re.IGNORECASE)
        if not match:
            continue
        chunks = [match.group(1).strip()] if match.lastindex else []
        for following in lines[index + 1 :]:
            if any(re.match(pattern, following, flags=re.IGNORECASE) for pattern in stop_patterns):
                break
            if re.fullmatch(r"=+", following.strip()):
                break
            if not following.strip():
                if any(chunks):
                    break
                continue
            chunks.append(following.strip())
        return " ".join(chunk for chunk in chunks if chunk).strip(" `\"")
    return ""


def words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-/][A-Za-z0-9]+)*", text))


def regex_gate(text: str, specification: GateSpec) -> tuple[bool, list[str]]:
    matches = [bool(re.search(pattern, text, flags=re.IGNORECASE)) for pattern in specification.patterns]
    passed = all(matches) if specification.mode == "all" else any(matches)
    missing = [pattern for pattern, matched in zip(specification.patterns, matches) if not matched]
    return passed, missing


def add_check(
    checks: list[dict[str, object]],
    *,
    check_id: str,
    passed: bool,
    category: str,
    message: str,
    file: str | None = None,
    line: int | None = None,
    carrier_id: str | None = None,
    evidence: object | None = None,
) -> None:
    item: dict[str, object] = {
        "id": check_id,
        "status": "PASS" if passed else "FAIL",
        "category": category,
        "message": message,
    }
    if file is not None:
        item["file"] = file
    if line is not None:
        item["line"] = line
    if carrier_id is not None:
        item["carrier_id"] = carrier_id
    if evidence is not None:
        item["evidence"] = evidence
    checks.append(item)


def marker_to_visible(line: str) -> str | None:
    figure = re.search(r"(?:FUTURE|PLANNED) FIGURE\s+(\d+)", line, flags=re.IGNORECASE)
    if figure:
        return f"Fig. {figure.group(1)}"
    table = re.search(r"(?:FUTURE|PLANNED) TABLE\s+([IVX]+)", line, flags=re.IGNORECASE)
    if table:
        return f"Table {table.group(1).upper()}"
    return None


def check_live_table_i(root: Path, spec: CarrierSpec, text: str, checks: list[dict[str, object]]) -> dict[str, object]:
    rel = spec.source_rel.as_posix()
    code = strip_tex_comments(text)
    table_match = re.search(r"\\begin\{table\*?\}.*?\\end\{table\*?\}", code, flags=re.DOTALL)
    table_text = table_match.group(0) if table_match else ""
    start_line = None if table_match is None else code.count("\n", 0, table_match.start()) + 1

    local_start = len(checks)
    add_check(checks, check_id="table_i.environment", passed=table_match is not None, category="activation", message="Table I is materialized as one active TeX table.", file=rel, line=start_line, carrier_id=spec.carrier_id)
    caption_ok = bool(re.search(r"\\caption\s*\{.+?\}", table_text, flags=re.DOTALL))
    add_check(checks, check_id="table_i.caption", passed=caption_ok, category="metadata", message="Table I has an active nonempty caption.", file=rel, line=line_number(code, r"\\caption\s*\{"), carrier_id=spec.carrier_id)
    label_count = len(re.findall(rf"\\label\{{{re.escape(spec.label)}\}}", table_text))
    add_check(checks, check_id="table_i.label", passed=label_count == 1, category="metadata", message="Table I has exactly one active stable label.", file=rel, line=line_number(code, rf"\\label\{{{re.escape(spec.label)}\}}"), carrier_id=spec.carrier_id, evidence={"count": label_count})
    ref_count = len(re.findall(rf"Table~\\ref\{{{re.escape(spec.label)}\}}", code))
    add_check(checks, check_id="table_i.lead_in", passed=ref_count == 1, category="metadata", message="Table I has exactly one active prose lead-in reference.", file=rel, line=line_number(code, rf"Table~\\ref\{{{re.escape(spec.label)}\}}"), carrier_id=spec.carrier_id, evidence={"count": ref_count})

    cite_groups = re.findall(r"\\cite\{([^}]+)\}", table_text)
    cite_sizes = [len([key for key in group.split(",") if key.strip()]) for group in cite_groups]
    cite_keys = [key.strip() for group in cite_groups for key in group.split(",") if key.strip()]
    add_check(checks, check_id="table_i.family_rows", passed=cite_sizes == [4, 2, 5, 6, 6, 1], category="critical_contract", message="The six reader-task families retain source-group sizes 4/2/5/6/6/1.", file=rel, line=start_line, carrier_id=spec.carrier_id, evidence={"citation_group_sizes": cite_sizes})
    add_check(checks, check_id="table_i.displayed_sources", passed=len(cite_keys) == 24 and len(set(cite_keys)) == 24, category="data_authority", message="Table I displays 24 unique synthesis sources exactly once.", file=rel, line=start_line, carrier_id=spec.carrier_id, evidence={"source_keys": len(cite_keys), "unique_source_keys": len(set(cite_keys))})
    note_norm = normalize(table_text)
    note_patterns = [r"24 displayed syntheses once", r"14 short or focused", r"38 total", r"outside the primary\s+evidence base of 206 studies", r"seven sources added during manuscript preparation"]
    add_check(checks, check_id="table_i.note_denominators", passed=all(re.search(pattern, note_norm) for pattern in note_patterns), category="critical_contract", message="Table I note preserves 24 displayed + 14 focused = 38 contextual sources, the 206-study boundary, and seven preparation additions.", file=rel, line=line_number(code, r"\\parbox"), carrier_id=spec.carrier_id)
    add_check(checks, check_id="table_i.no_ranking", passed=bool(re.search(r"do not rank review quality", note_norm)), category="nonduplication", message="Table I explicitly avoids review-quality ranking.", file=rel, line=line_number(code, r"Families aid navigation"), carrier_id=spec.carrier_id)

    local = checks[local_start:]
    status = "PASS" if all(item["status"] == "PASS" for item in local) else "FAIL"
    return {
        "order": spec.order,
        "visible_item": spec.visible,
        "carrier_id": spec.carrier_id,
        "kind": spec.kind,
        "section": spec.section,
        "file": rel,
        "expected_state": "live",
        "contract_status": spec.expected_contract_status,
        "label": spec.label,
        "blueprint_id": None,
        "data_authority": "Six active Table I family rows containing 24 unique cited syntheses; note reconciles the 38-source contextual register.",
        "status": status,
        "check_ids": [item["id"] for item in local],
    }


def run_qa(root: Path) -> dict[str, object]:
    checks: list[dict[str, object]] = []
    carriers_out: list[dict[str, object]] = []
    sources: dict[Path, str] = {}

    required_paths = [CONTRACT_REL, *SECTION_SCAN_ORDER]
    for rel in required_paths:
        path = root / rel
        exists = path.is_file()
        add_check(checks, check_id=f"source_exists.{rel.as_posix()}", passed=exists, category="source", message=f"Required authority file exists: {rel.as_posix()}.", file=rel.as_posix())
        if exists:
            sources[rel] = read_text(path)

    if any(rel not in sources for rel in required_paths):
        return assemble_report(root, checks, carriers_out, sources)

    contract = sources[CONTRACT_REL]
    rows = parse_contract_rows(contract)
    row_by_order = {int(row["order"]): row for row in rows}

    add_check(checks, check_id="contract.row_count", passed=len(rows) == 16, category="architecture", message="The central reading-order map contains exactly 16 carriers.", file=CONTRACT_REL.as_posix(), line=line_number(contract, r"## Reading-order map"), evidence={"count": len(rows)})
    visible_order = [str(row["visible"]) for row in rows]
    add_check(checks, check_id="contract.visible_order", passed=visible_order == EXPECTED_VISIBLE_ORDER, category="architecture", message="Visible numbering follows Table I, Figures 1-8, and Tables II-VIII in reading order.", file=CONTRACT_REL.as_posix(), line=line_number(contract, r"## Reading-order map"), evidence={"observed": visible_order, "expected": EXPECTED_VISIBLE_ORDER})
    figure_count = sum(str(row["visible"]).startswith("Fig.") for row in rows)
    table_count = sum(str(row["visible"]).startswith("Table") for row in rows)
    add_check(checks, check_id="contract.carrier_counts", passed=(figure_count, table_count) == (8, 8), category="architecture", message="The architecture contains exactly eight figures and eight tables.", file=CONTRACT_REL.as_posix(), evidence={"figures": figure_count, "tables": table_count})

    status_observed = [str(row["status"]) for row in rows]
    expected_statuses = [carrier.expected_contract_status for carrier in CARRIERS]
    add_check(checks, check_id="contract.statuses", passed=status_observed == expected_statuses, category="activation", message="Table I is live/layout-pending and the other 15 carriers remain pending under their declared statuses.", file=CONTRACT_REL.as_posix(), evidence={"observed": status_observed})

    registry_match = re.search(r"## Stable label registry\s+(.*?)(?=\n## )", contract, flags=re.DOTALL | re.IGNORECASE)
    registry_labels = re.findall(r"`([^`]+)`", registry_match.group(1)) if registry_match else []
    add_check(checks, check_id="contract.label_registry", passed=registry_labels == EXPECTED_LABELS and len(set(registry_labels)) == 16, category="metadata", message="The stable-label registry contains the 16 labels once and in visible reading order.", file=CONTRACT_REL.as_posix(), line=line_number(contract, r"## Stable label registry"), evidence={"observed": registry_labels, "expected": EXPECTED_LABELS})

    questions_ok = len(rows) == 16 and all(len(str(row["reader_question"])) >= 20 and str(row["reader_question"]).rstrip().endswith("?") for row in rows)
    add_check(checks, check_id="contract.reader_questions", passed=questions_ok, category="reader_task", message="Every carrier has a substantive reader question in the central contract.", file=CONTRACT_REL.as_posix(), line=line_number(contract, r"## Reading-order map"))
    nondup_ok = len(rows) == 16 and all(len(str(row["nonduplication"])) >= 30 for row in rows)
    add_check(checks, check_id="contract.nonduplication_boundaries", passed=nondup_ok, category="nonduplication", message="Every carrier has a nonempty nonduplication boundary.", file=CONTRACT_REL.as_posix(), line=line_number(contract, r"## Reading-order map"))
    core_ok = len(rows) == 16 and all(len(str(row["core_content"])) >= 30 for row in rows)
    add_check(checks, check_id="contract.core_messages", passed=core_ok, category="reader_task", message="Every carrier has a substantive core-content/message contract.", file=CONTRACT_REL.as_posix(), line=line_number(contract, r"## Reading-order map"))

    placement_ok = len(rows) == 16 and all(re.match(rf"^{re.escape(spec.section)}(?:,|\b)", str(row_by_order.get(spec.order, {}).get("placement", ""))) for spec in CARRIERS)
    add_check(checks, check_id="contract.section_placement", passed=placement_ok, category="placement", message="All 16 central-map placements use the expected nine-section section number.", file=CONTRACT_REL.as_posix())

    all_section_text = "\n".join(sources[rel] for rel in SECTION_SCAN_ORDER)
    active_code = "\n".join(strip_tex_comments(sources[rel]) for rel in SECTION_SCAN_ORDER)
    active_tables = len(re.findall(r"\\begin\{table\*?\}", active_code))
    active_figures = len(re.findall(r"\\begin\{figure\*?\}", active_code))
    add_check(checks, check_id="activation.environments", passed=(active_tables, active_figures) == (1, 0), category="activation", message="Only Table I is materialized; no planned figure/table environment is active.", evidence={"active_tables": active_tables, "active_figures": active_figures})

    pending_active_labels = {carrier.label: len(re.findall(rf"\\label\{{{re.escape(carrier.label)}\}}", active_code)) for carrier in PENDING_CARRIERS}
    pending_active_refs = {carrier.label: len(re.findall(rf"\\ref\{{{re.escape(carrier.label)}\}}", active_code)) for carrier in PENDING_CARRIERS}
    add_check(checks, check_id="activation.pending_labels", passed=all(count == 0 for count in pending_active_labels.values()), category="activation", message="All 15 pending stable labels remain comment-only.", evidence=pending_active_labels)
    add_check(checks, check_id="activation.pending_references", passed=all(count == 0 for count in pending_active_refs.values()), category="activation", message="All 15 pending lead-in references remain comment-only.", evidence=pending_active_refs)

    marker_lines: list[str] = []
    observed_markers = ["Table I"]
    for rel in SECTION_SCAN_ORDER:
        for line in sources[rel].splitlines():
            if re.match(r"^%\s+(?:FUTURE|PLANNED) (?:FIGURE|TABLE)\b", line, flags=re.IGNORECASE):
                marker_lines.append(line)
                visible = marker_to_visible(line)
                if visible:
                    observed_markers.append(visible)
    add_check(checks, check_id="comments.planned_block_count", passed=len(marker_lines) == 15, category="architecture", message="Exactly 15 future/planned production blocks exist.", evidence={"count": len(marker_lines)})
    add_check(checks, check_id="comments.visible_order", passed=observed_markers == EXPECTED_VISIBLE_ORDER, category="architecture", message="Section-comment block order matches the central visible numbering.", evidence={"observed": observed_markers, "expected": EXPECTED_VISIBLE_ORDER})

    carriers_out.append(check_live_table_i(root, CARRIERS[0], sources[SECTION_1], checks))

    seen_blueprints: list[str] = []
    seen_pending_labels: list[str] = []
    for spec in PENDING_CARRIERS:
        rel = spec.source_rel.as_posix()
        source_text = sources[spec.source_rel]
        extracted = extract_comment_block(source_text, spec.marker_pattern or "")
        local_start = len(checks)
        if extracted is None:
            add_check(checks, check_id=f"{spec.carrier_id}.block", passed=False, category="metadata", message=f"Expected unique production block for {spec.visible} was not found.", file=rel, carrier_id=spec.carrier_id)
            carriers_out.append({"order": spec.order, "visible_item": spec.visible, "carrier_id": spec.carrier_id, "kind": spec.kind, "section": spec.section, "file": rel, "expected_state": "pending", "contract_status": spec.expected_contract_status, "label": spec.label, "blueprint_id": spec.blueprint_id, "data_authority": "", "status": "FAIL", "check_ids": [checks[-1]["id"]]})
            continue

        block, block_line = extracted
        payload = comment_payload(block)
        block_norm = normalize(payload)
        seen_blueprints.append(spec.blueprint_id or "")
        seen_pending_labels.append(spec.label)

        add_check(checks, check_id=f"{spec.carrier_id}.block", passed=True, category="metadata", message=f"Unique production block found for {spec.visible}.", file=rel, line=block_line, carrier_id=spec.carrier_id)
        label_count = len(re.findall(rf"^Stable label:\s*{re.escape(spec.label)}\s*$", payload, flags=re.IGNORECASE | re.MULTILINE))
        add_check(checks, check_id=f"{spec.carrier_id}.stable_label", passed=label_count == 1, category="metadata", message=f"Stable label is exactly {spec.label}.", file=rel, line=line_number(block, r"Stable label:"), carrier_id=spec.carrier_id, evidence={"count": label_count})
        blueprint_count = len(re.findall(rf"^Blueprint ID:\s*{re.escape(spec.blueprint_id or '')}\b", payload, flags=re.IGNORECASE | re.MULTILINE))
        add_check(checks, check_id=f"{spec.carrier_id}.blueprint_id", passed=blueprint_count == 1, category="metadata", message=f"Blueprint ID is exactly {spec.blueprint_id}.", file=rel, line=line_number(block, r"Blueprint ID:"), carrier_id=spec.carrier_id, evidence={"count": blueprint_count})

        authority_lines = len(re.findall(r"^Data authority:", payload, flags=re.IGNORECASE | re.MULTILINE))
        authority = extract_comment_field(payload, r"^Data authority:\s*(.*)$", (r"^(?:Reader question|Purpose|Layout|Panel|Row unit|Required|Future|Main|Working title|Placement|Intended placement):",))
        add_check(checks, check_id=f"{spec.carrier_id}.data_authority", passed=authority_lines == 1 and words(authority) >= 3, category="data_authority", message="A nonempty, unique data-authority declaration is present.", file=rel, line=line_number(block, r"Data authority:"), carrier_id=spec.carrier_id, evidence={"declaration": authority})

        lead_count = len(re.findall(r"^Future lead-in(?:\s*\([^)]*\))?:", payload, flags=re.IGNORECASE | re.MULTILINE))
        lead = extract_comment_field(payload, r"^Future lead-in(?:\s*\([^)]*\))?:\s*(.*)$", (r"^(?:Exact\s+)?Future caption:", r"^(?:Visual|Table|Production)?\s*constraints?:", r"^Constraints:"))
        lead_has_ref = bool(re.search(rf"(?:Figure|Table)~\\ref\{{{re.escape(spec.label)}\}}", lead, flags=re.IGNORECASE))
        add_check(checks, check_id=f"{spec.carrier_id}.lead_in", passed=lead_count == 1 and words(lead) >= 8 and lead_has_ref, category="metadata", message="Future lead-in is nonempty, unique, and references the stable label.", file=rel, line=line_number(block, r"Future lead-in"), carrier_id=spec.carrier_id, evidence={"word_count": words(lead), "text": lead})

        caption_count = len(re.findall(r"^(?:Exact\s+)?Future caption:", payload, flags=re.IGNORECASE | re.MULTILINE))
        caption = extract_comment_field(payload, r"^(?:Exact\s+)?Future caption:\s*(.*)$", (r"^(?:Visual|Table|Production)?\s*constraints?:", r"^Constraints:"))
        add_check(checks, check_id=f"{spec.carrier_id}.caption", passed=caption_count == 1 and words(caption) >= 12, category="metadata", message="Future caption is nonempty and unique.", file=rel, line=line_number(block, r"(?:Exact\s+)?Future caption:"), carrier_id=spec.carrier_id, evidence={"word_count": words(caption), "text": caption})

        for requirement in spec.critical_gates:
            passed, missing = regex_gate(block_norm, requirement)
            add_check(checks, check_id=f"{spec.carrier_id}.critical.{requirement.key}", passed=passed, category="critical_contract", message=requirement.description, file=rel, line=block_line, carrier_id=spec.carrier_id, evidence=None if passed else {"missing_regex": missing})

        local = checks[local_start:]
        carriers_out.append(
            {
                "order": spec.order,
                "visible_item": spec.visible,
                "carrier_id": spec.carrier_id,
                "kind": spec.kind,
                "section": spec.section,
                "file": rel,
                "block_line": block_line,
                "expected_state": "pending",
                "contract_status": spec.expected_contract_status,
                "label": spec.label,
                "blueprint_id": spec.blueprint_id,
                "data_authority": authority,
                "future_lead_in": lead,
                "future_caption": caption,
                "status": "PASS" if all(item["status"] == "PASS" for item in local) else "FAIL",
                "check_ids": [item["id"] for item in local],
            }
        )

    add_check(checks, check_id="comments.unique_blueprints", passed=len(seen_blueprints) == 15 and len(set(seen_blueprints)) == 15 and "" not in seen_blueprints, category="metadata", message="The 15 pending carriers have unique nonempty blueprint IDs.", evidence={"blueprint_ids": seen_blueprints})
    add_check(checks, check_id="comments.unique_pending_labels", passed=seen_pending_labels == EXPECTED_LABELS[1:] and len(set(seen_pending_labels)) == 15, category="metadata", message="The 15 pending blocks expose unique stable labels in reading order.", evidence={"labels": seen_pending_labels})

    # Cross-carrier production gates are central authority, not asset QA claims.
    central_norm = normalize(contract)
    production_gates = (
        gate("recompute", "Counts must be recomputed from named locked sources.", r"recompute every displayed count from the named locked source"),
        gate("tradeoff_lineage", "Both governed and substantive tradeoff lineages are preserved.", r"preserve the 404/169 governed and 402/168 substantive tradeoff lineages"),
        gate("normalization", "Canonical modality/mechanism normalization is locked.", r"hash-locked modality crosswalk", r"phase-f mechanism\s+normalization"),
        gate("vector_accessibility", "Vector, grayscale, text-size, and alt-text requirements are explicit.", r"editable and vector based", r"no copied source artwork, ai\s+illustration", r"at least 8-point text", r"grayscale-safe distinctions", r"complete alt text"),
        gate("activation", "References/captions activate only after source, semantic, and render QA.", r"activate figure references and captions in the manuscript only after", r"source, semantic, and rendered-layout qa"),
    )
    for specification in production_gates:
        passed, missing = regex_gate(central_norm, specification)
        add_check(checks, check_id=f"production_gate.{specification.key}", passed=passed, category="production_gate", message=specification.description, file=CONTRACT_REL.as_posix(), line=line_number(contract, r"## Production gates"), evidence=None if passed else {"missing_regex": missing})

    return assemble_report(root, checks, carriers_out, sources)


def assemble_report(root: Path, checks: list[dict[str, object]], carriers: list[dict[str, object]], sources: dict[Path, str]) -> dict[str, object]:
    failed = [item for item in checks if item["status"] == "FAIL"]
    passed = len(checks) - len(failed)
    carrier_failures = sum(carrier.get("status") == "FAIL" for carrier in carriers)
    return {
        "qa_name": "final_visual_contract_qa",
        "status": "PASS" if not failed else "FAIL",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": str(root.resolve()),
        "authority": {
            "central_contract": CONTRACT_REL.as_posix(),
            "section_comment_blocks": [rel.as_posix() for rel in SECTION_SCAN_ORDER],
            "scope": "Contract/comment QA only; no visual assets generated and no TeX activated.",
        },
        "summary": {
            "expected_carriers": 16,
            "expected_figures": 8,
            "expected_tables": 8,
            "expected_live": 1,
            "expected_pending": 15,
            "carriers_reported": len(carriers),
            "carrier_failures": carrier_failures,
            "checks_total": len(checks),
            "checks_passed": passed,
            "checks_failed": len(failed),
        },
        "source_files_read": [rel.as_posix() for rel in sources],
        "carriers": sorted(carriers, key=lambda item: int(item["order"])),
        "checks": checks,
        "failures": failed,
    }


def md_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(report: dict[str, object], invocation: str) -> str:
    status = str(report["status"])
    summary = report["summary"]
    assert isinstance(summary, dict)
    carriers = report["carriers"]
    checks = report["checks"]
    failures = report["failures"]
    assert isinstance(carriers, list) and isinstance(checks, list) and isinstance(failures, list)

    lines = [
        "# Final Visual Contract QA",
        "",
        f"**Status:** {status}",
        "",
        "This is a contract-level gate only. It creates no figure/table asset and activates no TeX carrier.",
        "The central placement contract and the section comment blocks are the governing authorities.",
        "",
        "## Gate summary",
        "",
        f"- Carriers: **{summary['carriers_reported']}/16** (expected 8 figures + 8 tables).",
        f"- Activation state: **1 live** carrier (Table I) + **15 pending** production blocks.",
        f"- Checks: **{summary['checks_passed']} passed**, **{summary['checks_failed']} failed**, **{summary['checks_total']} total**.",
        f"- Carrier failures: **{summary['carrier_failures']}**.",
        "",
        "## Carrier matrix",
        "",
        "| Order | Visible item | Section | State | Stable label | Blueprint ID | QA |",
        "|---:|---|---:|---|---|---|---|",
    ]
    for carrier in carriers:
        assert isinstance(carrier, dict)
        lines.append(
            "| {order} | {visible} | {section} | {state} | `{label}` | {blueprint} | **{status}** |".format(
                order=carrier.get("order", ""),
                visible=md_escape(carrier.get("visible_item", "")),
                section=carrier.get("section", ""),
                state=carrier.get("expected_state", ""),
                label=carrier.get("label", ""),
                blueprint=f"`{carrier['blueprint_id']}`" if carrier.get("blueprint_id") else "live",
                status=carrier.get("status", "FAIL"),
            )
        )

    lines.extend(["", "## Failed gates", ""])
    if not failures:
        lines.append("None. All architecture, metadata, activation, panel, denominator, and nonduplication gates passed.")
    else:
        lines.append("| Check | Carrier | Location | Failure |")
        lines.append("|---|---|---|---|")
        for failure in failures:
            assert isinstance(failure, dict)
            location = str(failure.get("file", ""))
            if failure.get("line"):
                location += f":{failure['line']}"
            lines.append(
                f"| `{md_escape(failure.get('id', ''))}` | {md_escape(failure.get('carrier_id', 'global'))} | `{md_escape(location)}` | {md_escape(failure.get('message', ''))} |"
            )

    categories: dict[str, dict[str, int]] = {}
    for item in checks:
        assert isinstance(item, dict)
        category = str(item.get("category", "other"))
        bucket = categories.setdefault(category, {"PASS": 0, "FAIL": 0})
        bucket[str(item["status"])] += 1
    lines.extend(["", "## Checks by category", "", "| Category | Passed | Failed |", "|---|---:|---:|"])
    for category in sorted(categories):
        lines.append(f"| {category} | {categories[category]['PASS']} | {categories[category]['FAIL']} |")

    lines.extend(
        [
            "",
            "## Re-run",
            "",
            "```powershell",
            invocation,
            "```",
            "",
            "The command exits with code 0 only on PASS and code 1 on any failed gate.",
            "",
        ]
    )
    return "\n".join(lines)


def resolve_output(root: Path, value: str | None, default_rel: Path) -> Path:
    if value is None:
        return root / default_rel
    path = Path(value)
    return path if path.is_absolute() else root / path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="v2 manuscript root (default: parent of tools/)")
    parser.add_argument("--json-out", help="JSON report path, absolute or relative to --root")
    parser.add_argument("--md-out", help="Markdown report path, absolute or relative to --root")
    parser.add_argument("--no-write", action="store_true", help="Run checks and print status without writing reports")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    report = run_qa(root)
    json_out = resolve_output(root, args.json_out, DEFAULT_JSON_REL)
    md_out = resolve_output(root, args.md_out, DEFAULT_MD_REL)

    if not args.no_write:
        json_out.parent.mkdir(parents=True, exist_ok=True)
        md_out.parent.mkdir(parents=True, exist_ok=True)
        json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        invocation = "python tools/visual_contract_qa.py"
        md_out.write_text(render_markdown(report, invocation), encoding="utf-8")

    summary = report["summary"]
    assert isinstance(summary, dict)
    print(f"{report['status']}: {summary['checks_passed']}/{summary['checks_total']} checks passed; {summary['checks_failed']} failed")
    if report["status"] == "FAIL":
        failures = report["failures"]
        assert isinstance(failures, list)
        for failure in failures:
            assert isinstance(failure, dict)
            location = str(failure.get("file", ""))
            if failure.get("line"):
                location += f":{failure['line']}"
            print(f"- {failure['id']} [{location}]: {failure['message']}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
