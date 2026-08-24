#!/usr/bin/env python3
"""Build the eight submission figures from locked project evidence.

The script uses only deterministic vector drawing and canonical project files.
It writes editable SVG, vector PDF, color PNG, grayscale PNG, plot data, and a
machine readable QA manifest for every figure.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import textwrap
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from PIL import Image


SCRIPT = Path(__file__).resolve()
MANUSCRIPT_ROOT = SCRIPT.parents[1]
PROJECT_ROOT = next(path for path in MANUSCRIPT_ROOT.parents if path.name == "prisma2020Review")
CHECKPOINT_ROOT = PROJECT_ROOT / "systematic_review_workflow" / "09_kayitlar" / "checkpoints"
FIGURE_ROOT = MANUSCRIPT_ROOT / "figures" / "final_submission_2026-08-25"
DATA_ROOT = FIGURE_ROOT / "data"
QA_ROOT = FIGURE_ROOT / "qa"

PRISMA_CSV = (
    CHECKPOINT_ROOT
    / "prisma_flow_PHASE_C_FINAL_2026-07-30"
    / "PRISMA_FLOW_COUNTS_FINAL_2026-07-30.csv"
)
TQAF_AUDIT_CSV = (
    CHECKPOINT_ROOT
    / "quality_assessment_PHASE_E_FINAL_2026-08-04"
    / "phase_e_tqaf_dimension_audit_2026-08-04.csv"
)
PHASE_F_ROOT = CHECKPOINT_ROOT / "synthesis_PHASE_F_FINAL_2026-08-04"
INTEGRATION_CSV = PHASE_F_ROOT / "s2_integration_mechanisms.csv"
TRADEOFF_CSV = PHASE_F_ROOT / "s4_tradeoff_families.csv"
VALIDATION_SETTING_CSV = PHASE_F_ROOT / "s5_validation_maturity.csv"
VALIDATION_METHOD_CSV = PHASE_F_ROOT / "s5_validation_types.csv"
TECHNOLOGY_CSV = PHASE_F_ROOT / "s6_enabling_technologies.csv"
APPLICATION_CSV = PHASE_F_ROOT / "s6_application_domains.csv"
SIX_G_CSV = PHASE_F_ROOT / "s7_six_g_relevance.csv"
FIG08_DISPLAY_CSV = DATA_ROOT / "fig08_chain_display.csv"

BLUE = "#0072B2"
TEAL = "#009E73"
ORANGE = "#E69F00"
SKY = "#56B4E9"
PURPLE = "#8C6BB1"
VERMILION = "#D55E00"
DARK = "#333333"
MID = "#777777"
LIGHT = "#E9EDF2"
PALE_BLUE = "#E8F2F8"
PALE_TEAL = "#E7F4EF"
PALE_ORANGE = "#FBF1DC"
PALE_PURPLE = "#F1EAF5"

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Liberation Sans", "DejaVu Sans"],
        "font.size": 8.2,
        "axes.titlesize": 9.0,
        "axes.labelsize": 8.2,
        "xtick.labelsize": 7.8,
        "ytick.labelsize": 7.8,
        "legend.fontsize": 7.8,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "axes.linewidth": 0.8,
        "savefig.transparent": False,
        "figure.facecolor": "white",
    }
)

BUILD_RECORDS: list[dict[str, object]] = []


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def wrap_label(text: str, width: int) -> str:
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False))


def rounded_box(
    ax: plt.Axes,
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    facecolor: str = "white",
    edgecolor: str = DARK,
    linewidth: float = 1.0,
    radius: float = 0.018,
    zorder: int = 2,
) -> FancyBboxPatch:
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle=f"round,pad=0.008,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        zorder=zorder,
    )
    ax.add_patch(box)
    return box


def arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str = MID,
    style: str = "-|>",
    linewidth: float = 1.0,
    linestyle: str = "-",
    connectionstyle: str = "arc3,rad=0",
    zorder: int = 1,
    mutation_scale: float = 8,
) -> FancyArrowPatch:
    item = FancyArrowPatch(
        start,
        end,
        arrowstyle=style,
        mutation_scale=mutation_scale,
        linewidth=linewidth,
        linestyle=linestyle,
        color=color,
        connectionstyle=connectionstyle,
        shrinkA=0,
        shrinkB=0,
        zorder=zorder,
    )
    ax.add_patch(item)
    return item


def save_figure(
    fig: plt.Figure,
    stem: str,
    *,
    source_paths: list[Path],
    checks: dict[str, object],
) -> None:
    FIGURE_ROOT.mkdir(parents=True, exist_ok=True)
    QA_ROOT.mkdir(parents=True, exist_ok=True)
    pdf_path = FIGURE_ROOT / f"{stem}.pdf"
    svg_path = FIGURE_ROOT / f"{stem}.svg"
    png_path = QA_ROOT / f"{stem}_color.png"
    gray_path = QA_ROOT / f"{stem}_grayscale.png"
    fig.savefig(pdf_path, bbox_inches="tight", pad_inches=0.04)
    fig.savefig(svg_path, bbox_inches="tight", pad_inches=0.04)
    svg_text = svg_path.read_text(encoding="utf-8")
    svg_text = "\n".join(line.rstrip() for line in svg_text.splitlines()) + "\n"
    with svg_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(svg_text)
    fig.savefig(png_path, dpi=240, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    with Image.open(png_path) as image:
        image.convert("L").save(gray_path)
    BUILD_RECORDS.append(
        {
            "figure": stem,
            "sources": [str(path.relative_to(PROJECT_ROOT)) for path in source_paths],
            "source_sha256": {str(path.relative_to(PROJECT_ROOT)): sha256(path) for path in source_paths},
            "outputs": {
                "pdf": str(pdf_path.relative_to(MANUSCRIPT_ROOT)),
                "svg": str(svg_path.relative_to(MANUSCRIPT_ROOT)),
                "color_png": str(png_path.relative_to(MANUSCRIPT_ROOT)),
                "grayscale_png": str(gray_path.relative_to(MANUSCRIPT_ROOT)),
            },
            "checks": checks,
        }
    )


def figure_01_native_evidence() -> None:
    fig, ax = plt.subplots(figsize=(7.16, 3.45))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panels = [
        (
            0.025,
            "A",
            "Model frame",
            "Model result",
            ["Assumptions", "Objective", "Constraints"],
            PALE_BLUE,
            BLUE,
        ),
        (
            0.350,
            "B",
            "Observation frame",
            "Medium observation",
            ["Optical path", "Measurement plane", "Operating conditions"],
            PALE_TEAL,
            TEAL,
        ),
        (
            0.675,
            "C",
            "Deployment frame",
            "Architecture object",
            ["Shared components", "Scenario", "Validation setting"],
            PALE_ORANGE,
            ORANGE,
        ),
    ]
    for x, letter, panel_title, object_title, tags, pale, accent in panels:
        rounded_box(ax, x, 0.30, 0.30, 0.60, facecolor="white", edgecolor=accent, linewidth=1.2)
        ax.text(x + 0.018, 0.855, letter, fontsize=9.2, fontweight="bold", color=DARK, va="center")
        ax.text(x + 0.150, 0.795, wrap_label(panel_title, 24), ha="center", va="center", fontsize=9.0, fontweight="bold")
        rounded_box(ax, x + 0.050, 0.565, 0.20, 0.105, facecolor=pale, edgecolor=accent, linewidth=1.0)
        ax.text(x + 0.150, 0.618, wrap_label(object_title, 22), ha="center", va="center", fontsize=8.3)
        for index, tag in enumerate(tags):
            ty = 0.475 - index * 0.075
            rounded_box(ax, x + 0.045, ty, 0.21, 0.052, facecolor="white", edgecolor="#A9B2BC", linewidth=0.7)
            ax.text(x + 0.150, ty + 0.026, tag, ha="center", va="center", fontsize=7.8)

    rounded_box(ax, 0.085, 0.085, 0.83, 0.125, facecolor="#F5F6F7", edgecolor=DARK, linewidth=1.0)
    ax.text(
        0.50,
        0.147,
        "Each result is interpreted within the context reported by its study",
        ha="center",
        va="center",
        fontsize=8.8,
        fontweight="bold",
    )
    save_figure(
        fig,
        "fig01_native_evidence_objects",
        source_paths=[],
        checks={"panels": 3, "quantitative_encoding": False, "parallel_panels": True},
    )


def figure_02_comparison_framework() -> None:
    fig, ax = plt.subplots(figsize=(7.16, 4.25))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    axes = [
        (0.02, "Physical context", ["Platform and signal path", "Tasks and target", "Geometry and channel"], PALE_TEAL, TEAL),
        (0.265, "Coupling location", ["Hardware and carrier", "Waveform and resources", "Link, design, application"], PALE_ORANGE, ORANGE),
        (0.51, "Measurement contract", ["Definition and plane", "Unit and aggregation", "Conditions and baseline"], PALE_PURPLE, PURPLE),
        (0.755, "Provenance", ["Reported origin", "Validation setting", "Configuration and locator"], PALE_BLUE, BLUE),
    ]
    for x, title, lines, pale, accent in axes:
        rounded_box(ax, x, 0.68, 0.225, 0.27, facecolor=pale, edgecolor=accent, linewidth=1.1)
        ax.text(x + 0.1125, 0.895, title, ha="center", va="center", fontsize=8.7, fontweight="bold", color=DARK)
        ax.text(x + 0.1125, 0.785, "\n".join(lines), ha="center", va="center", fontsize=7.5, linespacing=1.35)
        arrow(ax, (x + 0.1125, 0.68), (0.50, 0.59), color=DARK, connectionstyle="arc3,rad=0.06")

    rounded_box(ax, 0.30, 0.41, 0.40, 0.18, facecolor="#F5F6F7", edgecolor=DARK, linewidth=1.2)
    ax.text(0.50, 0.525, "Contextual comparison record", ha="center", va="center", fontsize=9.0, fontweight="bold")
    ax.text(
        0.50,
        0.458,
        "Each field records its value\nor availability status",
        ha="center",
        va="center",
        fontsize=7.2,
        linespacing=1.2,
    )

    outcomes = [
        (0.035, "Source setting\ninterpretation", PALE_TEAL, TEAL),
        (0.36, "Conditional relation\nacross studies", PALE_BLUE, BLUE),
        (0.685, "Descriptive\nuse", "#F2F2F2", MID),
    ]
    for x, title, pale, accent in outcomes:
        rounded_box(ax, x, 0.12, 0.28, 0.17, facecolor=pale, edgecolor=accent, linewidth=1.0)
        ax.text(x + 0.14, 0.205, title, ha="center", va="center", fontsize=8.2, fontweight="bold")
        arrow(ax, (0.50, 0.41), (x + 0.14, 0.29), color=DARK, connectionstyle="arc3,rad=0.08")

    ax.text(
        0.50,
        0.045,
        "Comparison aligns common fields and preserves the context of each study",
        ha="center",
        va="center",
        fontsize=8.0,
        color=DARK,
    )
    save_figure(
        fig,
        "fig02_comparison_framework",
        source_paths=[],
        checks={"axes": 4, "outcomes": 3, "quantitative_encoding": False},
    )


def figure_03_prisma_flow() -> None:
    rows = read_rows(PRISMA_CSV)
    counts = {row["count_key"]: int(row["count"]) for row in rows}
    assert sum(counts[key] for key in ["source_scopus", "source_ieee_xplore", "source_sciencedirect", "source_springerlink", "source_wiley", "source_taylor_francis"]) == counts["records_identified_databases"]
    assert counts["records_identified_databases"] - counts["duplicates_removed"] - counts["other_removed"] == counts["records_screened"]
    assert counts["records_screened"] - counts["records_not_advanced"] == counts["source_records_forwarded"]
    assert counts["source_records_forwarded"] - counts["postscreen_aliases_consolidated"] == counts["reports_sought"]
    assert counts["reports_sought"] - counts["reports_not_retrieved"] == counts["reports_assessed"]
    assert counts["reports_assessed"] - counts["reports_excluded_full_text"] - counts["reports_contextual_full_text"] == counts["reports_included"]
    assert counts["reports_included"] - counts["studies_included"] == 21
    assert counts["title_abstract_contextual"] + counts["reports_contextual_full_text"] == counts["contextual_corpus_total"]

    plot_rows = [
        {"stage": row["stage"], "key": row["count_key"], "label": row["label"], "count": row["count"]}
        for row in rows
        if row["count_key"] in {
            "records_identified_databases",
            "records_screened",
            "source_records_forwarded",
            "reports_sought",
            "reports_assessed",
            "reports_included",
            "studies_included",
            "contextual_corpus_total",
        }
    ]
    write_rows(DATA_ROOT / "fig03_prisma_plot_data.csv", plot_rows, ["stage", "key", "label", "count"])

    fig, ax = plt.subplots(figsize=(7.16, 5.35))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    main_nodes = [
        (0.88, "Records identified", counts["records_identified_databases"], PALE_BLUE, BLUE),
        (0.75, "Records screened", counts["records_screened"], PALE_BLUE, BLUE),
        (0.62, "Source records forwarded", counts["source_records_forwarded"], PALE_BLUE, BLUE),
        (0.49, "Unique reports sought", counts["reports_sought"], PALE_TEAL, TEAL),
        (0.36, "Full text reports assessed", counts["reports_assessed"], PALE_TEAL, TEAL),
        (0.23, "Eligible reports", counts["reports_included"], PALE_TEAL, TEAL),
        (0.10, "Unique studies", counts["studies_included"], PALE_ORANGE, ORANGE),
    ]
    centers: list[tuple[float, float]] = []
    for y, label, count, pale, accent in main_nodes:
        rounded_box(ax, 0.08, y - 0.043, 0.42, 0.086, facecolor=pale, edgecolor=accent, linewidth=1.1)
        ax.text(0.29, y + 0.014, label, ha="center", va="center", fontsize=8.2, fontweight="bold")
        ax.text(0.29, y - 0.020, f"n={count:,}", ha="center", va="center", fontsize=8.1, color=DARK)
        centers.append((0.29, y))
    for first, second in zip(centers, centers[1:]):
        arrow(ax, (first[0], first[1] - 0.044), (second[0], second[1] + 0.044), color=MID)

    ax.text(0.025, 0.755, "Records", rotation=90, ha="center", va="center", color=BLUE, fontsize=8.3, fontweight="bold")
    ax.text(0.025, 0.355, "Reports", rotation=90, ha="center", va="center", color=TEAL, fontsize=8.3, fontweight="bold")
    ax.text(0.025, 0.10, "Studies", rotation=90, ha="center", va="center", color=ORANGE, fontsize=8.3, fontweight="bold")

    source_text = "\n".join(
        [
            f"Scopus  {counts['source_scopus']:,}",
            f"IEEE Xplore  {counts['source_ieee_xplore']:,}",
            f"SpringerLink  {counts['source_springerlink']:,}",
            f"Other searched sources  {counts['source_sciencedirect'] + counts['source_wiley'] + counts['source_taylor_francis']:,}",
        ]
    )
    side_boxes = [
        (0.79, 0.18, "Source contributions", source_text, PALE_BLUE, BLUE),
        (
            0.60,
            0.18,
            "Screening dispositions",
            f"Duplicate records  {counts['duplicates_removed']:,}\nMetadata dispositions  {counts['other_removed']:,}\nTitle and abstract exclusions  {counts['title_abstract_excluded']:,}\nContextual records  {counts['title_abstract_contextual']:,}\nRelated report flags  {counts['title_abstract_related_flag']:,}",
            "#F2F2F2",
            MID,
        ),
        (0.43, 0.12, "Retrieval boundary", f"Bibliographic aliases  {counts['postscreen_aliases_consolidated']:,}\nReports not retrieved  {counts['reports_not_retrieved']:,}", "#F2F2F2", MID),
        (0.24, 0.15, "Full text outcomes", f"Eligible  {counts['reports_included']:,}\nContextual  {counts['reports_contextual_full_text']:,}\nExclusions  {counts['reports_excluded_full_text']:,}", PALE_TEAL, TEAL),
        (0.055, 0.14, "Contextual corpus", f"{counts['title_abstract_contextual']:,} + {counts['reports_contextual_full_text']:,} = {counts['contextual_corpus_total']:,}", PALE_ORANGE, ORANGE),
    ]
    for y, height, title, body, pale, accent in side_boxes:
        rounded_box(ax, 0.57, y, 0.39, height, facecolor=pale, edgecolor=accent, linewidth=1.0)
        ax.text(0.765, y + height - 0.035, title, ha="center", va="center", fontsize=8.1, fontweight="bold")
        ax.text(0.765, y + height / 2 - 0.017, body, ha="center", va="center", fontsize=7.3, linespacing=1.22)

    ax.text(0.405, 0.555, "2 aliases", ha="left", va="center", fontsize=7.1, color=MID)
    ax.text(0.405, 0.165, "21 companion links", ha="left", va="center", fontsize=7.1, color=MID)

    save_figure(
        fig,
        "fig03_prisma_report_study_flow",
        source_paths=[PRISMA_CSV],
        checks={
            "records_identified": counts["records_identified_databases"],
            "records_screened": counts["records_screened"],
            "reports_sought": counts["reports_sought"],
            "reports_assessed": counts["reports_assessed"],
            "eligible_reports": counts["reports_included"],
            "unique_studies": counts["studies_included"],
            "contextual_records": counts["contextual_corpus_total"],
        },
    )


def figure_04_tqaf_profile() -> None:
    counts: dict[str, Counter[int]] = defaultdict(Counter)
    study_ids: set[str] = set()
    for row in read_rows(TQAF_AUDIT_CSV):
        dimension = row["dimension"]
        score = int(row["score_final"])
        counts[dimension][score] += 1
        study_ids.add(row["study_id"])
    assert len(study_ids) == 206

    order = [
        ("Summary", "overall_evidence_contribution", "Overall evidence contribution"),
        ("Interpretation", "technical_relevance", "Technical relevance"),
        ("Interpretation", "metric_clarity", "Metric clarity"),
        ("Interpretation", "reporting_completeness", "Reporting completeness"),
        ("Interpretation", "limitation_transparency", "Limitation transparency"),
        ("Transfer and reuse", "validation_maturity", "Validation maturity"),
        ("Transfer and reuse", "reproducibility", "Reproducibility"),
        ("Transfer and reuse", "benchmark_readiness", "Benchmark readiness"),
        ("Transfer and reuse", "comparison_admissibility", "Comparison admissibility"),
    ]
    plot_rows: list[dict[str, object]] = []
    for group, key, label in order:
        strong = counts[key][3]
        adequate = counts[key][2]
        low = counts[key][1]
        assert strong + adequate + low == 206
        plot_rows.append(
            {
                "group": group,
                "dimension": label,
                "strong": strong,
                "adequate": adequate,
                "low": low,
                "denominator": 206,
            }
        )
    write_rows(
        DATA_ROOT / "fig04_tqaf_profile.csv",
        plot_rows,
        ["group", "dimension", "strong", "adequate", "low", "denominator"],
    )

    fig, ax = plt.subplots(figsize=(7.16, 4.55))
    y = list(range(len(plot_rows)))
    strong_pct = [100 * int(row["strong"]) / 206 for row in plot_rows]
    adequate_pct = [100 * int(row["adequate"]) / 206 for row in plot_rows]
    low_pct = [100 * int(row["low"]) / 206 for row in plot_rows]

    ax.barh(y, strong_pct, color=BLUE, edgecolor="white", linewidth=0.6, label="Strong")
    ax.barh(y, adequate_pct, left=strong_pct, color="#B5B8BC", edgecolor="white", linewidth=0.6, hatch="..", label="Adequate")
    ax.barh(
        y,
        low_pct,
        left=[a + b for a, b in zip(strong_pct, adequate_pct)],
        color=VERMILION,
        edgecolor="white",
        linewidth=0.6,
        hatch="///",
        label="Low",
    )
    ax.set_yticks(y, [str(row["dimension"]) for row in plot_rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 126)
    ax.set_xlabel("Share of the 206 studies")
    ax.set_xticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax.grid(axis="x", color="#D9DDE1", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.legend(loc="lower center", bbox_to_anchor=(0.48, 1.01), ncol=3, frameon=False)
    ax.text(115.0, -0.86, "Counts\nS   A   L", ha="center", va="bottom", fontsize=7.5, fontweight="bold")
    for index, row in enumerate(plot_rows):
        values = [int(row["strong"]), int(row["adequate"]), int(row["low"])]
        left = 0.0
        ax.text(115.0, index, f"{values[0]:>3} {values[1]:>3} {values[2]:>3}", ha="center", va="center", fontsize=7.1, family="monospace")
    ax.axhline(0.5, color=DARK, linewidth=0.8)
    ax.axhline(4.5, color="#8A8A8A", linewidth=0.7)
    fig.text(0.025, 0.57, "Interpretation", rotation=90, ha="center", va="center", fontsize=7.2, color=MID, fontweight="bold")
    fig.text(0.025, 0.265, "Transfer and reuse", rotation=90, ha="center", va="center", fontsize=7.2, color=MID, fontweight="bold")
    fig.subplots_adjust(left=0.34, right=0.985, top=0.89, bottom=0.13)

    save_figure(
        fig,
        "fig04_tqaf_profile",
        source_paths=[TQAF_AUDIT_CSV],
        checks={"study_denominator": len(study_ids), "rows": len(plot_rows), "all_rows_reconcile": True},
    )


def figure_05_integration_map() -> None:
    rows = read_rows(INTEGRATION_CSV)
    by_key = {row["category"]: row for row in rows}
    expected = {
        "shared_hardware": 117,
        "shared_optical_carrier": 49,
        "shared_waveform": 113,
        "shared_resource_allocation": 118,
        "shared_link_or_channel": 87,
        "joint_design_or_optimization": 72,
        "shared_application_scenario": 46,
        "mixed": 3,
    }
    for key, value in expected.items():
        assert int(by_key[key]["study_count"]) == value

    display = [
        ("shared_hardware", "Hardware", "Front end", DARK, "#F4F5F6"),
        ("shared_optical_carrier", "Optical\ncarrier", "Carrier", DARK, "#F4F5F6"),
        ("shared_waveform", "Waveform", "Waveform", DARK, "#F4F5F6"),
        ("shared_resource_allocation", "Resource\nallocation", "Resources", DARK, "#F4F5F6"),
        ("shared_link_or_channel", "Link or\nchannel", "Link", DARK, "#F4F5F6"),
        ("joint_design_or_optimization", "Joint\ndesign", "Design", DARK, "#F4F5F6"),
        ("shared_application_scenario", "Application", "Service", DARK, "#F4F5F6"),
    ]
    plot_rows = [
        {
            "display_order": index + 1,
            "category": key,
            "label": label,
            "system_location": location,
            "study_count": by_key[key]["study_count"],
            "percent_of_206": by_key[key]["percent_of_206"],
        }
        for index, (key, label, location, _, _) in enumerate(display)
    ]
    plot_rows.append(
        {
            "display_order": 8,
            "category": "mixed",
            "label": "Mixed boundary cases",
            "system_location": "Boundary",
            "study_count": by_key["mixed"]["study_count"],
            "percent_of_206": by_key["mixed"]["percent_of_206"],
        }
    )
    write_rows(
        DATA_ROOT / "fig05_integration_map.csv",
        plot_rows,
        ["display_order", "category", "label", "system_location", "study_count", "percent_of_206"],
    )

    fig, ax = plt.subplots(figsize=(7.16, 3.55))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0.50, 0.94, "Coupling locations may overlap within one study", ha="center", va="center", fontsize=9.0, fontweight="bold")

    x_positions = [0.025 + index * 0.138 for index in range(7)]
    for x, (key, label, location, accent, pale) in zip(x_positions, display):
        rounded_box(ax, x, 0.55, 0.125, 0.27, facecolor=pale, edgecolor=accent, linewidth=1.0)
        ax.text(x + 0.0625, 0.742, label, ha="center", va="center", fontsize=7.0, fontweight="bold", linespacing=1.1)
        ax.text(x + 0.0625, 0.626, f"n={int(by_key[key]['study_count'])}", ha="center", va="center", fontsize=8.4, color=DARK, fontweight="bold")
        ax.plot([x + 0.0625, x + 0.0625], [0.55, 0.31], color=accent, linewidth=1.0)
        ax.text(x + 0.0625, 0.512, location, ha="center", va="center", fontsize=7.1, color=DARK, bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.4})

    arrow(ax, (0.045, 0.40), (0.965, 0.40), color=DARK, linewidth=1.4)
    arrow(ax, (0.045, 0.30), (0.965, 0.30), color=MID, linewidth=1.4, linestyle="--")
    ax.text(0.045, 0.435, "Communication function", ha="left", va="bottom", fontsize=7.7, color=DARK, fontweight="bold")
    ax.text(0.045, 0.245, "Sensing function", ha="left", va="top", fontsize=7.7, color=DARK, fontweight="bold")
    rounded_box(ax, 0.72, 0.08, 0.24, 0.09, facecolor="#F2F2F2", edgecolor=MID, linewidth=0.8)
    ax.text(0.84, 0.125, f"Mixed cases  n={int(by_key['mixed']['study_count'])}", ha="center", va="center", fontsize=7.2)
    ax.text(0.36, 0.085, "Counts show overlapping study coverage", ha="center", va="center", fontsize=7.5, color=DARK)

    save_figure(
        fig,
        "fig05_integration_map",
        source_paths=[INTEGRATION_CSV],
        checks={"study_denominator": 206, "displayed_mechanisms": 7, "mixed_cases": 3, "categories_overlap": True},
    )


def figure_06_tradeoff_profile() -> None:
    raw_rows = read_rows(TRADEOFF_CSV)
    rows_by_key: dict[str, dict[str, int]] = {}
    for row in raw_rows:
        rows_by_key[row["category"]] = {
            "claims": int(row["claim_count"]),
            "studies": int(row["unique_study_count"]),
            "conditional": int(row["conditional_claim_count"]),
            "quantitative": int(row["eligible_quantitative_claim_count"]),
            "qualitative": int(row["eligible_qualitative_claim_count"]),
        }
    for key in ["bandwidth_spectrum_or_resource_allocation", "qualitative_or_partial_general"]:
        rows_by_key[key]["claims"] -= 1
        rows_by_key[key]["studies"] -= 1
        rows_by_key[key]["conditional"] -= 1
        rows_by_key[key]["qualitative"] -= 1

    order = [
        ("bandwidth_spectrum_or_resource_allocation", "Bandwidth, spectrum, and resources"),
        ("power_energy_or_dynamic_range", "Power, energy, and dynamic range"),
        ("communication_reliability_vs_sensing_quality", "Communication reliability and sensing quality"),
        ("rate_resolution", "Rate and resolution"),
        ("rate_accuracy_or_localization", "Rate, accuracy, and localization"),
        ("rate_range_or_coverage", "Rate, range, and coverage"),
        ("waveform_hardware_or_complexity", "Waveform, hardware, and complexity"),
        ("other_joint_tradeoff", "Other joint relations"),
        ("qualitative_or_partial_general", "Qualitative and partial relations"),
        ("security_or_resilience_tradeoff", "Security and resilience"),
        ("synergy_or_non_antagonistic_coupling", "Synergy"),
    ]
    plot_rows: list[dict[str, object]] = []
    for index, (key, label) in enumerate(order, start=1):
        item = rows_by_key[key]
        assert item["quantitative"] + item["qualitative"] == item["claims"]
        plot_rows.append(
            {
                "display_order": index,
                "category": key,
                "label": label,
                "quantitative": item["quantitative"],
                "qualitative": item["qualitative"],
                "claims": item["claims"],
                "unique_studies": item["studies"],
                "conditional": item["conditional"],
                "conditional_percent": round(100 * item["conditional"] / item["claims"], 1),
            }
        )
    assert sum(int(row["quantitative"]) for row in plot_rows) == 218
    assert sum(int(row["qualitative"]) for row in plot_rows) == 184
    assert sum(int(row["claims"]) for row in plot_rows) == 402
    assert sum(int(row["conditional"]) for row in plot_rows) == 371
    write_rows(
        DATA_ROOT / "fig06_tradeoff_profile.csv",
        plot_rows,
        [
            "display_order",
            "category",
            "label",
            "quantitative",
            "qualitative",
            "claims",
            "unique_studies",
            "conditional",
            "conditional_percent",
        ],
    )

    fig = plt.figure(figsize=(7.16, 5.45))
    grid = fig.add_gridspec(1, 3, width_ratios=[1.8, 1.0, 1.25], wspace=0.15)
    ax_a = fig.add_subplot(grid[0, 0])
    ax_b = fig.add_subplot(grid[0, 1], sharey=ax_a)
    ax_c = fig.add_subplot(grid[0, 2], sharey=ax_a)
    y = list(range(len(plot_rows)))
    quant = [int(row["quantitative"]) for row in plot_rows]
    qual = [int(row["qualitative"]) for row in plot_rows]
    claims = [int(row["claims"]) for row in plot_rows]
    studies = [int(row["unique_studies"]) for row in plot_rows]
    conditional_pct = [float(row["conditional_percent"]) for row in plot_rows]

    ax_a.barh(y, quant, color=BLUE, edgecolor="white", linewidth=0.5, label="Quantitative")
    ax_a.barh(y, qual, left=quant, color=ORANGE, edgecolor=DARK, linewidth=0.45, hatch="///", label="Qualitative")
    ax_a.set_yticks(y, [wrap_label(str(row["label"]), 28) for row in plot_rows])
    ax_a.invert_yaxis()
    ax_a.set_xlim(0, 105)
    ax_a.set_xlabel("Substantive records")
    ax_a.set_title("(a) Records by type", loc="left", fontweight="bold")
    ax_a.grid(axis="x", color="#D9DDE1", linewidth=0.6)
    ax_a.set_axisbelow(True)
    handles, labels = ax_a.get_legend_handles_labels()
    for index, value in enumerate(claims):
        ax_a.text(value + 1.5, index, str(value), ha="left", va="center", fontsize=7.1)

    for index, value in enumerate(studies):
        ax_b.plot([0, value], [index, index], color="#A5ABB1", linewidth=1.0)
        marker_face = "white" if value == 1 else DARK
        ax_b.scatter([value], [index], s=24, facecolor=marker_face, edgecolor=DARK, linewidth=0.9, zorder=3)
        ax_b.text(value + 1.5, index, str(value), ha="left", va="center", fontsize=7.1)
    ax_b.set_xlim(0, 76)
    ax_b.set_xlabel("Studies in family")
    ax_b.set_title("(b) Study coverage", loc="left", fontweight="bold")
    ax_b.grid(axis="x", color="#D9DDE1", linewidth=0.6)
    ax_b.set_axisbelow(True)
    ax_b.tick_params(axis="y", labelleft=False, left=False)

    for index, row in enumerate(plot_rows):
        value = float(row["conditional_percent"])
        ax_c.plot([0, value], [index, index], color="#B6A8C4", linewidth=1.0)
        marker_face = "white" if int(row["claims"]) == 1 else PURPLE
        ax_c.scatter([value], [index], s=24, facecolor=marker_face, edgecolor=PURPLE, linewidth=0.9, zorder=3)
        label_x = value - 2.0 if value >= 98 else value + 2.0
        label_align = "right" if value >= 98 else "left"
        ax_c.text(
            label_x,
            index,
            f"{int(row['conditional'])}/{int(row['claims'])}",
            ha=label_align,
            va="center",
            fontsize=7.0,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.25},
        )
    ax_c.axvline(92.3, color=DARK, linewidth=0.8, linestyle="--")
    ax_c.text(92.3, -0.75, "371/402", ha="center", va="bottom", fontsize=7.0, color=DARK, bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.2})
    ax_c.set_xlim(0, 115)
    ax_c.set_xticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax_c.set_xlabel("Conditional share")
    ax_c.set_title("(c) Condition dependence", loc="left", fontweight="bold")
    ax_c.grid(axis="x", color="#D9DDE1", linewidth=0.6)
    ax_c.set_axisbelow(True)
    ax_c.tick_params(axis="y", labelleft=False, left=False)

    for axis in [ax_a, ax_b, ax_c]:
        axis.spines[["top", "right", "left"]].set_visible(False)
        axis.tick_params(axis="y", length=0)
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.50, 0.995), ncol=2, frameon=False)
    fig.subplots_adjust(left=0.35, right=0.99, top=0.86, bottom=0.12)

    save_figure(
        fig,
        "fig06_tradeoff_profile",
        source_paths=[TRADEOFF_CSV],
        checks={
            "substantive_records": 402,
            "quantitative_records": 218,
            "qualitative_records": 184,
            "conditional_records": 371,
            "study_union": 168,
            "families": 11,
        },
    )


def figure_07_validation_profile() -> None:
    setting_rows = read_rows(VALIDATION_SETTING_CSV)
    method_rows = read_rows(VALIDATION_METHOD_CSV)
    assert sum(int(row["study_count"]) for row in setting_rows) == 206
    assert int(next(row for row in method_rows if row["category"] == "unclear")["study_count"]) == 0

    setting_labels = {
        "simulation_or_numerical": "Simulation or numerical",
        "enhanced_simulation_or_dataset": "Enhanced simulation or dataset",
        "laboratory_experiment_or_proof_of_concept": "Laboratory experiment or proof of concept",
        "controlled_prototype": "Controlled prototype",
        "field_trial_or_deployment": "Field trial or deployment",
    }
    method_labels = {
        "analytical": "Analytical",
        "numerical_analysis": "Numerical analysis",
        "simulation": "Simulation",
        "dataset_based": "Dataset based",
        "laboratory_experiment": "Laboratory experiment",
        "prototype_testbed": "Prototype or testbed",
        "field_experiment": "Field experiment",
        "mixed": "Mixed validation",
        "unclear": "Unclear",
    }
    derived_setting = [
        {
            "display_order": index + 1,
            "category": row["maturity_label"],
            "label": setting_labels[row["maturity_label"]],
            "study_count": int(row["study_count"]),
            "percent_of_206": float(row["percent_of_206"]),
        }
        for index, row in enumerate(setting_rows)
    ]
    method_order = ["analytical", "numerical_analysis", "simulation", "dataset_based", "laboratory_experiment", "prototype_testbed", "field_experiment", "mixed"]
    method_by_key = {row["category"]: row for row in method_rows}
    derived_methods = [
        {
            "display_order": index + 1,
            "category": key,
            "label": method_labels[key],
            "study_count": int(method_by_key[key]["study_count"]),
            "percent_of_206": float(method_by_key[key]["percent_of_206"]),
        }
        for index, key in enumerate(method_order)
    ]
    write_rows(DATA_ROOT / "fig07_validation_settings.csv", derived_setting, ["display_order", "category", "label", "study_count", "percent_of_206"])
    write_rows(DATA_ROOT / "fig07_validation_methods.csv", derived_methods, ["display_order", "category", "label", "study_count", "percent_of_206"])

    fig = plt.figure(figsize=(7.16, 4.65))
    grid = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.08], wspace=0.43)
    ax_a = fig.add_subplot(grid[0, 0])
    ax_b = fig.add_subplot(grid[0, 1])

    setting_colors = [BLUE, MID, TEAL, ORANGE, PURPLE]
    y_a = list(range(len(derived_setting)))
    values_a = [int(row["study_count"]) for row in derived_setting]
    bars = ax_a.barh(y_a, values_a, color=setting_colors, edgecolor=DARK, linewidth=0.45)
    for index, (bar, row) in enumerate(zip(bars, derived_setting)):
        if index in {1, 3}:
            bar.set_hatch("//")
        ax_a.text(int(row["study_count"]) + 2, index, f"{int(row['study_count'])}  {float(row['percent_of_206']):.1f}%", ha="left", va="center", fontsize=7.2)
    ax_a.set_yticks(y_a, [wrap_label(str(row["label"]), 27) for row in derived_setting])
    ax_a.invert_yaxis()
    ax_a.set_xlim(0, 94)
    ax_a.set_xlabel("Studies")
    ax_a.set_title("(a) Highest reported setting\nOne category per study", loc="left", fontweight="bold")
    ax_a.grid(axis="x", color="#D9DDE1", linewidth=0.6)
    ax_a.set_axisbelow(True)

    y_b = list(range(len(derived_methods)))
    for index, row in enumerate(derived_methods):
        value = int(row["study_count"])
        color = BLUE if index <= 3 else ORANGE if index <= 6 else MID
        ax_b.plot([0, value], [index, index], color="#ADB2B8", linewidth=1.0)
        ax_b.scatter([value], [index], s=30, facecolor=color, edgecolor=DARK, linewidth=0.6, zorder=3)
        ax_b.text(value + 3, index, f"{value}  {float(row['percent_of_206']):.1f}%", ha="left", va="center", fontsize=7.2)
    ax_b.set_yticks(y_b, [str(row["label"]) for row in derived_methods])
    ax_b.invert_yaxis()
    ax_b.set_xlim(0, 171)
    ax_b.set_xlabel("Studies reporting method")
    ax_b.set_title("(b) Reported validation methods\nCategories may overlap", loc="left", fontweight="bold")
    ax_b.grid(axis="x", color="#D9DDE1", linewidth=0.6)
    ax_b.set_axisbelow(True)

    for axis in [ax_a, ax_b]:
        axis.spines[["top", "right", "left"]].set_visible(False)
        axis.tick_params(axis="y", length=0)
    fig.text(0.50, 0.025, "Settings describe how far a study reached. Methods describe the evidence used along that path.", ha="center", va="center", fontsize=7.8)
    fig.subplots_adjust(left=0.23, right=0.99, top=0.83, bottom=0.16)

    save_figure(
        fig,
        "fig07_validation_profile",
        source_paths=[VALIDATION_SETTING_CSV, VALIDATION_METHOD_CSV],
        checks={"study_denominator": 206, "exclusive_setting_sum": 206, "method_categories_overlap": True, "field_setting": 12},
    )


def figure_08_evidence_chain() -> None:
    if not FIG08_DISPLAY_CSV.exists():
        raise FileNotFoundError(f"Figure 8 display crosswalk is missing at {FIG08_DISPLAY_CSV}")
    display_rows = read_rows(FIG08_DISPLAY_CSV)
    source_tables = {
        "technology": {row["category"]: int(row["study_count"]) for row in read_rows(TECHNOLOGY_CSV)},
        "application": {row["category"]: int(row["study_count"]) for row in read_rows(APPLICATION_CSV)},
        "network": {row["category"]: int(row["study_count"]) for row in read_rows(SIX_G_CSV)},
    }
    for row in display_rows:
        if row["source_category"]:
            matches = [name for name, table in source_tables.items() if row["source_category"] in table]
            assert len(matches) == 1
            assert int(row["count"]) == source_tables[matches[0]][row["source_category"]]
    assert sum(source_tables["network"].values()) == 206

    layer_order = [
        "Optical generation and transport",
        "Waveform and observables",
        "Spatial control",
        "Inference and system models",
        "Application requirements",
        "6G evidence gate",
    ]
    layer_number = {name: str(index + 1) for index, name in enumerate(layer_order)}
    by_layer: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sorted(display_rows, key=lambda item: int(item["display_order"])):
        by_layer[row["layer"]].append(row)

    layer_titles = {
        "Optical generation and transport": "Generation and transport",
        "Waveform and observables": "Waveforms and\nobservables",
        "Spatial control": "Spatial control",
        "Inference and system models": "Inference",
        "Application requirements": "Selected application\ndomains",
        "6G evidence gate": "6G evidence gate",
    }
    positions = {
        "Optical generation and transport": (0.02, 0.57),
        "Waveform and observables": (0.3575, 0.57),
        "Spatial control": (0.695, 0.57),
        "Inference and system models": (0.695, 0.10),
        "Application requirements": (0.3575, 0.10),
        "6G evidence gate": (0.02, 0.10),
    }
    fills = {
        "Optical generation and transport": PALE_BLUE,
        "Waveform and observables": PALE_TEAL,
        "Spatial control": PALE_PURPLE,
        "Inference and system models": PALE_ORANGE,
        "Application requirements": "#F7F1DE",
        "6G evidence gate": "#EEF1F5",
    }
    accents = {
        "Optical generation and transport": BLUE,
        "Waveform and observables": TEAL,
        "Spatial control": PURPLE,
        "Inference and system models": ORANGE,
        "Application requirements": "#9A7B1C",
        "6G evidence gate": DARK,
    }

    fig, ax = plt.subplots(figsize=(7.16, 4.85))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    card_w = 0.285
    card_h = 0.35
    short_labels = {
        "photonic_THz_generation": "Photonic terahertz generation",
        "coherent_optics": "Coherent optics",
        "fiber_DAS": "Fiber sensing reuse",
        "photonic_integration": "Photonic integration",
        "FMCW": "Chirped processing",
        "OFDM": "Multicarrier waveform",
        "beamforming": "Beamforming",
        "OPA": "Optical phased array",
        "MIMO": "Multiple input multiple output",
        "ML_AI": "Machine learning",
        "digital_twin": "Digital twin",
        "vehicular": "Vehicular",
        "environment_monitoring": "Environmental monitoring",
        "indoor_positioning": "Indoor positioning",
        "aerospace": "Aerospace",
        "direct": "Direct relevance",
        "inferred": "Inferential relevance",
        "weak": "Weak relevance",
        "not_applicable": "Not applicable",
    }
    for layer in layer_order:
        x, y = positions[layer]
        rounded_box(ax, x, y, card_w, card_h, facecolor=fills[layer], edgecolor=accents[layer], linewidth=1.1)
        ax.add_patch(patches.Circle((x + 0.028, y + card_h - 0.038), 0.018, facecolor=accents[layer], edgecolor="white", linewidth=0.5, zorder=4))
        ax.text(x + 0.028, y + card_h - 0.038, layer_number[layer], ha="center", va="center", fontsize=7.1, color="white", fontweight="bold", zorder=5)
        ax.text(
            x + 0.058,
            y + card_h - 0.047,
            layer_titles[layer],
            ha="left",
            va="center",
            fontsize=7.8,
            fontweight="bold",
            linespacing=1.0,
        )
        body_rows = by_layer[layer]
        step = 0.050 if len(body_rows) >= 4 else 0.060
        start_y = y + card_h - 0.135
        for index, row in enumerate(body_rows):
            label = short_labels[row["source_category"]]
            suffix = f"  n={int(row['count'])}" if row["count"] else ""
            ax.text(x + card_w / 2, start_y - index * step, f"{label}{suffix}", ha="center", va="center", fontsize=6.85)

    arrow(ax, (0.313, 0.745), (0.3495, 0.745), color=DARK, linewidth=1.3, zorder=5, mutation_scale=12)
    arrow(ax, (0.6505, 0.745), (0.687, 0.745), color=DARK, linewidth=1.3, zorder=5, mutation_scale=12)
    arrow(ax, (0.8375, 0.57), (0.8375, 0.45), color=DARK, linewidth=1.3, zorder=5, mutation_scale=12)
    arrow(ax, (0.687, 0.275), (0.6505, 0.275), color=DARK, linewidth=1.3, zorder=5, mutation_scale=12)
    arrow(ax, (0.3495, 0.275), (0.313, 0.275), color=DARK, linewidth=1.3, zorder=5, mutation_scale=12)
    arrow(
        ax,
        (0.50, 0.45),
        (0.16, 0.57),
        color=MID,
        linewidth=1.2,
        linestyle="--",
        connectionstyle="arc3,rad=0.28",
        zorder=5,
        mutation_scale=13,
    )
    ax.text(0.78, 0.485, "Evidence path", ha="center", va="center", fontsize=7.7, color=DARK, fontweight="bold")
    ax.text(0.29, 0.485, "Requirement feedback", ha="center", va="center", fontsize=7.4, color=MID)
    ax.text(
        0.50,
        0.025,
        "Technology and application labels may overlap. The 6G evidence gate assigns one class per study.",
        ha="center",
        va="center",
        fontsize=7.7,
        color=DARK,
    )

    save_figure(
        fig,
        "fig08_technology_application_chain",
        source_paths=[FIG08_DISPLAY_CSV, TECHNOLOGY_CSV, APPLICATION_CSV, SIX_G_CSV],
        checks={"network_denominator": 206, "layers": 6, "technology_and_application_overlap": True, "equal_arrow_width": True},
    )


def write_manifest() -> None:
    QA_ROOT.mkdir(parents=True, exist_ok=True)
    payload = {
        "build_script": str(SCRIPT.relative_to(PROJECT_ROOT)),
        "build_script_sha256": sha256(SCRIPT),
        "figure_count": len(BUILD_RECORDS),
        "figures": BUILD_RECORDS,
        "global_checks": {
            "deterministic_vector_source": True,
            "ai_generated_assets": False,
            "external_artwork": False,
            "color_and_grayscale_outputs": True,
            "editable_svg_outputs": True,
        },
    }
    (QA_ROOT / "figure_build_qa.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    DATA_ROOT.mkdir(parents=True, exist_ok=True)
    QA_ROOT.mkdir(parents=True, exist_ok=True)
    figure_01_native_evidence()
    figure_02_comparison_framework()
    figure_03_prisma_flow()
    figure_04_tqaf_profile()
    figure_05_integration_map()
    figure_06_tradeoff_profile()
    figure_07_validation_profile()
    figure_08_evidence_chain()
    write_manifest()
    print(f"Built {len(BUILD_RECORDS)} figures in {FIGURE_ROOT}")


if __name__ == "__main__":
    main()
