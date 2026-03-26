from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.path import Path as MplPath


ROOT = Path(__file__).resolve().parents[2]
SUMMARY_PATH = ROOT / "analysis" / "IV_evidence_v2" / "section4E_summary_table.csv"
CANONICAL_PATH = ROOT / "screening" / "included_studies_canonical.csv"
DRAFTS_DIR = ROOT / "drafts"
BUNDLE_FIG_DIR = ROOT / "manuscript" / "current_bundle" / "figures"

FIG_IV_1_NAME = "fig_iv_1.png"
FIG_IV_2_NAME = "fig_iv_2.png"

MEDIUM_ORDER = ["Hybrid", "Fiber", "VLC/LiFi", "FSO", "THz", "Other"]
MECHANISM_ORDER = ["Shared front-end", "Separate front-ends"]
DETECTION_ORDER = ["Coherent", "Direct", "Residual"]
TASK_ORDER = ["Ranging", "2D localization", "Localization", "Vibration", "Other"]

MEDIUM_COLORS = {
    "Hybrid": "#4C78A8",
    "Fiber": "#54A24B",
    "VLC/LiFi": "#F58518",
    "FSO": "#E45756",
    "THz": "#B279A2",
    "Other": "#9D9D9D",
}

DETECTION_COLORS = {
    "Coherent": "#4C78A8",
    "Direct": "#54A24B",
    "Residual": "#9D9D9D",
}

NODE_FACE = "#F7F7F7"
NODE_EDGE = "#4A4A4A"


def load_canonical_ids() -> set[str]:
    with CANONICAL_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        key = "track_id" if "track_id" in reader.fieldnames else reader.fieldnames[0]
        return {row[key] for row in reader}


def display_medium(value: str) -> str:
    mapping = {
        "hybrid": "Hybrid",
        "cabled_fibre": "Fiber",
        "wireless_vlc": "VLC/LiFi",
        "wireless_fso": "FSO",
        "terahertz": "THz",
    }
    return mapping.get(value, "Other")


def display_mechanism(value: str) -> str:
    return {
        "shared_frontend": "Shared front-end",
        "separate_frontends": "Separate front-ends",
    }.get(value, "Separate front-ends")


def display_detection(value: str) -> str:
    normalized = (value or "").strip().lower()
    if normalized == "coherent":
        return "Coherent"
    if normalized in {"direct", "direct_detection", "direct detection"}:
        return "Direct"
    return "Residual"


def primary_task(value: str) -> str:
    raw = (value or "").strip()
    token = raw.split("|_")[0] if "|_" in raw else raw
    mapping = {
        "ranging": "Ranging",
        "localization_2d": "2D localization",
        "localization": "Localization",
        "vibration": "Vibration",
    }
    return mapping.get(token, "Other")


def load_rows() -> list[dict[str, str]]:
    canonical_ids = load_canonical_ids()
    with SUMMARY_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = [row for row in reader if row["paper_id"] in canonical_ids]
    unique_ids = {row["paper_id"] for row in rows}
    if len(unique_ids) != 220:
        raise RuntimeError(f"Expected 220 canonical studies, found {len(unique_ids)}")
    return rows


def layout_positions(
    counts: Counter[str],
    order: list[str],
    scale: float,
    bottom: float = 0.08,
    top: float = 0.92,
    gap: float = 0.025,
) -> dict[str, tuple[float, float]]:
    available = top - bottom
    total_node_height = sum(counts[label] * scale for label in order)
    total_gap = gap * max(0, len(order) - 1)
    extra = max(0.0, available - total_node_height - total_gap)
    current = top - extra / 2
    positions: dict[str, tuple[float, float]] = {}
    for label in order:
        height = counts[label] * scale
        y_top = current
        y_bottom = y_top - height
        positions[label] = (y_bottom, y_top)
        current = y_bottom - gap
    return positions


def ribbon(
    ax,
    x0: float,
    x1: float,
    y0_bottom: float,
    y0_top: float,
    y1_bottom: float,
    y1_top: float,
    color: str,
    alpha: float,
) -> None:
    ctrl = (x1 - x0) * 0.45
    vertices = [
        (x0, y0_top),
        (x0 + ctrl, y0_top),
        (x1 - ctrl, y1_top),
        (x1, y1_top),
        (x1, y1_bottom),
        (x1 - ctrl, y1_bottom),
        (x0 + ctrl, y0_bottom),
        (x0, y0_bottom),
        (x0, y0_top),
    ]
    codes = [
        MplPath.MOVETO,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.LINETO,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.CLOSEPOLY,
    ]
    patch = PathPatch(MplPath(vertices, codes), facecolor=color, edgecolor="none", alpha=alpha)
    ax.add_patch(patch)


def draw_nodes(ax, positions: dict[str, tuple[float, float]], x_center: float, width: float, colors: dict[str, str] | None = None) -> None:
    for label, (y_bottom, y_top) in positions.items():
        face = (colors or {}).get(label, NODE_FACE)
        rect = Rectangle(
            (x_center - width / 2, y_bottom),
            width,
            y_top - y_bottom,
            facecolor=face,
            edgecolor=NODE_EDGE,
            linewidth=1.1,
        )
        ax.add_patch(rect)


def annotate_nodes(ax, positions: dict[str, tuple[float, float]], counts: Counter[str], x_center: float, fontsize: int = 10) -> None:
    for label, (y_bottom, y_top) in positions.items():
        ax.text(
            x_center,
            (y_bottom + y_top) / 2,
            f"{label}\n{counts[label]}",
            ha="center",
            va="center",
            fontsize=fontsize,
            color="#1F1F1F",
            fontweight="semibold",
        )


def build_flow_figure(rows: list[dict[str, str]]) -> plt.Figure:
    medium_counts = Counter(display_medium(row["medium"]) for row in rows)
    mechanism_counts = Counter(display_mechanism(row["mechanism"]) for row in rows)
    detection_counts = Counter(display_detection(row["detection"]) for row in rows)

    left_mid = Counter(
        (display_medium(row["medium"]), display_mechanism(row["mechanism"])) for row in rows
    )
    mid_right = Counter(
        (display_mechanism(row["mechanism"]), display_detection(row["detection"])) for row in rows
    )
    triple_counts = Counter(
        (
            display_medium(row["medium"]),
            display_mechanism(row["mechanism"]),
            display_detection(row["detection"]),
        )
        for row in rows
    )

    total = len(rows)
    bottom, top, gap = 0.08, 0.90, 0.024
    max_gap = max(
        gap * max(0, len(MEDIUM_ORDER) - 1),
        gap * max(0, len(MECHANISM_ORDER) - 1),
        gap * max(0, len(DETECTION_ORDER) - 1),
    )
    scale = (top - bottom - max_gap) / total

    left_pos = layout_positions(medium_counts, MEDIUM_ORDER, scale, bottom=bottom, top=top, gap=gap)
    mid_pos = layout_positions(mechanism_counts, MECHANISM_ORDER, scale, bottom=bottom, top=top, gap=gap)
    right_pos = layout_positions(detection_counts, DETECTION_ORDER, scale, bottom=bottom, top=top, gap=gap)

    fig, ax = plt.subplots(figsize=(13.5, 8.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.965, "Fig. IV-1. Unified O-ISAC taxonomy flow", ha="center", va="center", fontsize=18, fontweight="bold")
    ax.text(0.5, 0.935, "Canonical N = 220 studies; long-tail media grouped as Other for readability", ha="center", va="center", fontsize=10, color="#555555")

    x_left, x_mid, x_right = 0.16, 0.50, 0.84
    node_width = 0.14

    ax.text(x_left, 0.905, "Medium", ha="center", va="bottom", fontsize=12, fontweight="bold")
    ax.text(x_mid, 0.905, "Integration", ha="center", va="bottom", fontsize=12, fontweight="bold")
    ax.text(x_right, 0.905, "Detection", ha="center", va="bottom", fontsize=12, fontweight="bold")

    src_cursor = {label: left_pos[label][1] for label in MEDIUM_ORDER}
    dst_cursor = {label: mid_pos[label][1] for label in MECHANISM_ORDER}
    for medium in MEDIUM_ORDER:
        for mechanism in MECHANISM_ORDER:
            count = left_mid[(medium, mechanism)]
            if not count:
                continue
            height = count * scale
            y0_top = src_cursor[medium]
            y0_bottom = y0_top - height
            src_cursor[medium] = y0_bottom

            y1_top = dst_cursor[mechanism]
            y1_bottom = y1_top - height
            dst_cursor[mechanism] = y1_bottom

            ribbon(
                ax,
                x_left + node_width / 2,
                x_mid - node_width / 2,
                y0_bottom,
                y0_top,
                y1_bottom,
                y1_top,
                MEDIUM_COLORS[medium],
                0.38,
            )

    src_cursor = {label: mid_pos[label][1] for label in MECHANISM_ORDER}
    dst_cursor = {label: right_pos[label][1] for label in DETECTION_ORDER}
    for mechanism in MECHANISM_ORDER:
        for detection in DETECTION_ORDER:
            count = mid_right[(mechanism, detection)]
            if not count:
                continue
            height = count * scale
            y0_top = src_cursor[mechanism]
            y0_bottom = y0_top - height
            src_cursor[mechanism] = y0_bottom

            y1_top = dst_cursor[detection]
            y1_bottom = y1_top - height
            dst_cursor[detection] = y1_bottom

            ribbon(
                ax,
                x_mid + node_width / 2,
                x_right - node_width / 2,
                y0_bottom,
                y0_top,
                y1_bottom,
                y1_top,
                DETECTION_COLORS[detection],
                0.30,
            )

    draw_nodes(ax, left_pos, x_left, node_width, colors={k: NODE_FACE for k in MEDIUM_ORDER})
    draw_nodes(ax, mid_pos, x_mid, node_width)
    draw_nodes(ax, right_pos, x_right, node_width)
    annotate_nodes(ax, left_pos, medium_counts, x_left)
    annotate_nodes(ax, mid_pos, mechanism_counts, x_mid)
    annotate_nodes(ax, right_pos, detection_counts, x_right)

    dominant_lines = [
        f"Hybrid -> Shared front-end -> Coherent: {triple_counts[('Hybrid', 'Shared front-end', 'Coherent')]}",
        f"Hybrid -> Shared front-end -> Direct: {triple_counts[('Hybrid', 'Shared front-end', 'Direct')]}",
        f"Fiber -> Shared front-end -> Coherent: {triple_counts[('Fiber', 'Shared front-end', 'Coherent')]}",
        f"VLC/LiFi -> Shared front-end -> Direct: {triple_counts[('VLC/LiFi', 'Shared front-end', 'Direct')]}",
        f"VLC/LiFi -> Separate front-ends -> Direct: {triple_counts[('VLC/LiFi', 'Separate front-ends', 'Direct')]}",
        f"FSO -> Shared front-end -> Coherent: {triple_counts[('FSO', 'Shared front-end', 'Coherent')]}",
        f"FSO -> Shared front-end -> Direct: {triple_counts[('FSO', 'Shared front-end', 'Direct')]}",
    ]
    ax.text(
        0.5,
        0.02,
        "Dominant branches: " + " | ".join(dominant_lines),
        ha="center",
        va="bottom",
        fontsize=8.7,
        color="#333333",
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "#F7F7F7", "edgecolor": "#D0D0D0"},
    )

    return fig


def build_heatmap_figure(rows: list[dict[str, str]]) -> plt.Figure:
    matrix_counts: defaultdict[tuple[str, str], int] = defaultdict(int)
    row_totals = Counter()
    for row in rows:
        medium = display_medium(row["medium"])
        task = primary_task(row["sensing_task"])
        matrix_counts[(medium, task)] += 1
        row_totals[medium] += 1

    matrix = [
        [matrix_counts[(medium, task)] for task in TASK_ORDER]
        for medium in MEDIUM_ORDER
    ]

    fig, ax = plt.subplots(figsize=(11.5, 6.7))
    image = ax.imshow(matrix, cmap="Blues", aspect="auto")

    ax.set_xticks(range(len(TASK_ORDER)))
    ax.set_xticklabels(TASK_ORDER, rotation=20, ha="right", fontsize=10)
    ax.set_yticks(range(len(MEDIUM_ORDER)))
    ax.set_yticklabels([f"{medium} ({row_totals[medium]})" for medium in MEDIUM_ORDER], fontsize=10)

    for row_index, medium in enumerate(MEDIUM_ORDER):
        for col_index, task in enumerate(TASK_ORDER):
            value = matrix_counts[(medium, task)]
            text_color = "white" if value >= 40 else "#1F1F1F"
            ax.text(col_index, row_index, str(value), ha="center", va="center", fontsize=10, color=text_color, fontweight="semibold")

    ax.set_title("Fig. IV-2. Medium-task specialization heatmap", fontsize=16, fontweight="bold", pad=18)
    ax.set_xlabel("Primary sensing task", fontsize=11, fontweight="bold")
    ax.set_ylabel("Medium class", fontsize=11, fontweight="bold")

    cbar = fig.colorbar(image, ax=ax, fraction=0.035, pad=0.03)
    cbar.set_label("Number of studies", fontsize=10)

    ax.text(
        -0.45,
        len(MEDIUM_ORDER) + 0.3,
        "Primary task = first normalized token; long-tail media aggregated as Other.",
        fontsize=9,
        color="#555555",
    )

    fig.tight_layout()
    return fig


def save_figure(fig: plt.Figure, name: str) -> None:
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    BUNDLE_FIG_DIR.mkdir(parents=True, exist_ok=True)
    for target in (DRAFTS_DIR / name, BUNDLE_FIG_DIR / name):
        fig.savefig(target, dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    rows = load_rows()
    save_figure(build_flow_figure(rows), FIG_IV_1_NAME)
    save_figure(build_heatmap_figure(rows), FIG_IV_2_NAME)
    print(f"Generated {FIG_IV_1_NAME} and {FIG_IV_2_NAME} from canonical N={len(rows)} rows.")


if __name__ == "__main__":
    main()
