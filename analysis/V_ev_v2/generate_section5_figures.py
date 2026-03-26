from __future__ import annotations

from pathlib import Path
import shutil

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "analysis" / "V_evidence_v2"
DRAFTS_DIR = BASE_DIR / "drafts"
CURRENT_FIGURES_DIR = BASE_DIR / "manuscript" / "current_bundle" / "figures"
REVIEW_PACKAGE_DIR = BASE_DIR / "review_package"
CANONICAL_INCLUDED_PATH = BASE_DIR / "screening" / "included_studies_canonical.csv"

FIG_V1 = DRAFTS_DIR / "fig_v_1.png"
FIG_V2 = DRAFTS_DIR / "fig_v_2.png"
GBPS = 1e9


MEDIUM_ORDER = [
    "hybrid",
    "cabled_fibre",
    "wireless_fso",
    "wireless_vlc",
    "wireless",
    "wireless_rf",
    "terahertz",
    "other",
]

MEDIUM_COLORS = {
    "hybrid": "#2A9D8F",
    "cabled_fibre": "#6BA368",
    "wireless_fso": "#4C78A8",
    "wireless_vlc": "#7D82B8",
    "wireless": "#8FA7BF",
    "wireless_rf": "#B8B0D9",
    "terahertz": "#C98E3D",
    "other": "#C9CDD2",
}

MEDIUM_LABELS = {
    "hybrid": "Hybrid",
    "cabled_fibre": "Fiber",
    "wireless_fso": "Wireless FSO",
    "wireless_vlc": "Wireless VLC",
    "wireless": "Wireless",
    "wireless_rf": "Wireless RF",
    "terahertz": "THz",
    "other": "Other",
}

COUPLING_MARKERS = {
    "resource_division": "o",
    "joint_waveform": "s",
    "other": "D",
    "missing": "D",
}

COUPLING_LABELS = {
    "resource_division": "Resource division",
    "joint_waveform": "Joint waveform",
    "other": "Other / missing",
    "missing": "Other / missing",
}


def parse_bool(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().map({"true": True, "false": False})


def normalize_coupling(series: pd.Series) -> pd.Series:
    normalized = (
        series.fillna("missing").astype(str).str.strip().str.replace(" ", "_", regex=False)
    )
    normalized.loc[~normalized.isin(COUPLING_MARKERS)] = "other"
    return normalized


def load_points() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "section5C_tradeoff_points.csv")
    canonical_ids = set(
        pd.read_csv(CANONICAL_INCLUDED_PATH)["track_id"].dropna().astype(str).str.strip()
    )
    df = df[df["paper_id"].astype(str).str.strip().isin(canonical_ids)].copy()
    for col in ["governance_blocked", "drmin_eligible", "crq_eligible"]:
        df[col] = parse_bool(df[col])
    df["coupling_mode_norm"] = normalize_coupling(df["coupling_mode"])
    df["rate_gbps"] = df["r_bps"] / GBPS
    return df


def load_pareto() -> pd.DataFrame:
    pareto = pd.read_csv(DATA_DIR / "section5E_pareto_points.csv").copy()
    pareto["coupling_mode_norm"] = normalize_coupling(pareto["coupling_mode"])
    pareto["rate_gbps"] = pareto["r_bps"] / GBPS
    return pareto


def medium_color(medium: str) -> str:
    return MEDIUM_COLORS.get(medium, MEDIUM_COLORS["other"])


def medium_label(medium: str) -> str:
    return MEDIUM_LABELS.get(medium, MEDIUM_LABELS["other"])


def coupling_label(key: str) -> str:
    return COUPLING_LABELS.get(key, COUPLING_LABELS["other"])


def medium_handles(media: list[str]) -> list[Line2D]:
    handles: list[Line2D] = []
    for medium in MEDIUM_ORDER:
        if medium not in media:
            continue
        handles.append(
            Line2D(
                [0],
                [0],
                marker="o",
                linestyle="none",
                markerfacecolor=medium_color(medium),
                markeredgecolor="#32404D",
                markeredgewidth=0.6,
                markersize=8,
                label=medium_label(medium),
            )
        )
    return handles


def coupling_handles(keys: list[str]) -> list[Line2D]:
    ordered = ["resource_division", "joint_waveform", "other", "missing"]
    seen: list[str] = []
    handles: list[Line2D] = []
    for key in ordered:
        if key not in keys:
            continue
        label = coupling_label(key)
        if label in seen:
            continue
        seen.append(label)
        handles.append(
            Line2D(
                [0],
                [0],
                marker=COUPLING_MARKERS[key],
                linestyle="none",
                markerfacecolor="white",
                markeredgecolor="#32404D",
                markeredgewidth=0.9,
                markersize=8,
                label=label,
            )
        )
    return handles


def style_axes(ax) -> None:
    ax.set_facecolor("#FBFCFD")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid(True, which="major", color="#D7DDE3", linewidth=0.85)
    ax.grid(True, which="minor", color="#EDF1F4", linewidth=0.45)
    for spine in ax.spines.values():
        spine.set_color("#7B8794")
        spine.set_linewidth(0.9)
    ax.tick_params(colors="#27313B", labelsize=10)


def add_chip(fig, x: float, label: str) -> None:
    fig.text(
        x,
        0.955,
        label,
        ha="center",
        va="center",
        fontsize=10,
        color="#23313F",
        bbox={
            "boxstyle": "round,pad=0.35,rounding_size=0.2",
            "facecolor": "#F3F6F8",
            "edgecolor": "#CAD4DC",
        },
    )


def add_count_box(ax, raw_n: int, governed_n: int) -> None:
    ax.text(
        0.04,
        0.92,
        f"Raw {raw_n}  ->  Governed {governed_n}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        color="#20303C",
        bbox={
            "boxstyle": "round,pad=0.35,rounding_size=0.2",
            "facecolor": "white",
            "edgecolor": "#BFC8D0",
        },
    )


def scatter_governed(ax, df: pd.DataFrame, x_col: str) -> None:
    for coupling_key in ["resource_division", "joint_waveform", "other", "missing"]:
        subset = df[df["coupling_mode_norm"] == coupling_key]
        if subset.empty:
            continue
        ax.scatter(
            subset[x_col],
            subset["rate_gbps"],
            s=70,
            marker=COUPLING_MARKERS[coupling_key],
            c=subset["medium"].map(medium_color),
            edgecolors="#32404D",
            linewidths=0.65,
            alpha=0.95,
            zorder=3,
        )


def plot_role_panel(
    ax,
    background: pd.DataFrame,
    foreground: pd.DataFrame,
    x_col: str,
    x_label: str,
    title: str,
) -> None:
    bg = background[(background["rate_gbps"] > 0) & (background[x_col] > 0)].copy()
    fg = foreground[(foreground["rate_gbps"] > 0) & (foreground[x_col] > 0)].copy()

    style_axes(ax)

    ax.scatter(
        bg[x_col],
        bg["rate_gbps"],
        s=48,
        c="#D3D8DE",
        alpha=0.33,
        linewidths=0,
        zorder=1,
    )
    scatter_governed(ax, fg, x_col)

    ax.set_xlabel(x_label, fontsize=12, color="#22313D")
    ax.set_ylabel(r"Communication rate $R$ (Gbps)", fontsize=12, color="#22313D")
    ax.set_title(title, fontsize=13, color="#1F2F3A", pad=12)
    add_count_box(ax, len(bg), len(fg))


def make_fig_v1(df: pd.DataFrame) -> None:
    usable = df[df["governance_blocked"] == False].copy()
    res_bg = df[df["r_bps"].notna() & df["drmin_m"].notna()].copy()
    res_fg = usable[
        usable["r_bps"].notna()
        & usable["drmin_m"].notna()
        & (usable["drmin_eligible"] == True)
    ].copy()
    acc_bg = df[df["r_bps"].notna() & df["sigma_r_m"].notna()].copy()
    acc_fg = usable[usable["r_bps"].notna() & usable["sigma_r_m"].notna()].copy()

    plt.rcParams.update(
        {
            "font.size": 10,
            "axes.titlesize": 13,
            "axes.labelsize": 12,
        }
    )

    fig, axes = plt.subplots(1, 2, figsize=(14.8, 6.6))

    plot_role_panel(
        axes[0],
        res_bg,
        res_fg,
        "drmin_m",
        r"Bandwidth-limited resolution $\Delta r_{\min}$ (m)",
        "Rate vs physical resolution",
    )
    plot_role_panel(
        axes[1],
        acc_bg,
        acc_fg,
        "sigma_r_m",
        r"Estimator-level accuracy $\sigma_r$ (m)",
        "Rate vs estimator-level accuracy",
    )

    axes[0].set_xlim(0.002, 30)
    axes[0].set_ylim(0.02, 700)
    axes[1].set_xlim(0.001, 2000)
    axes[1].set_ylim(0.02, 700)

    add_chip(fig, 0.22, "Role-separated synthesis")
    add_chip(fig, 0.50, "Governance filtered")
    add_chip(fig, 0.78, "Support-conditioned reading")

    represented_media = [m for m in MEDIUM_ORDER if m in set(df["medium"].dropna())]
    medium_legend = fig.legend(
        handles=medium_handles(represented_media),
        title="Medium class",
        loc="center left",
        bbox_to_anchor=(0.84, 0.58),
        frameon=False,
        fontsize=10,
        title_fontsize=11,
    )
    fig.add_artist(medium_legend)

    represented_couplings = list(df["coupling_mode_norm"].dropna().unique())
    fig.legend(
        handles=coupling_handles(represented_couplings),
        title="Coupling mode",
        loc="center left",
        bbox_to_anchor=(0.84, 0.28),
        frameon=False,
        fontsize=10,
        title_fontsize=11,
    )

    fig.text(
        0.5,
        0.065,
        "Gray points provide raw role-conditioned context; colored points mark governance-usable evidence only. "
        "Resolution and accuracy remain separated by design so the figure does not collapse different sensing roles into one axis.",
        ha="center",
        fontsize=10.2,
        color="#32404D",
    )

    fig.subplots_adjust(left=0.08, right=0.82, top=0.86, bottom=0.18, wspace=0.18)
    fig.savefig(FIG_V1, dpi=300, bbox_inches="tight")
    plt.close(fig)


def make_fig_v2(df: pd.DataFrame) -> None:
    usable = df[df["governance_blocked"] == False].copy()
    valid = usable[
        (usable["crq_eligible"] == True)
        & usable["r_bps"].notna()
        & usable["drmin_m"].notna()
        & (usable["drmin_eligible"] == True)
    ].copy()
    pareto = load_pareto()

    plt.rcParams.update(
        {
            "font.size": 10,
            "axes.titlesize": 13,
            "axes.labelsize": 12,
        }
    )

    fig, ax = plt.subplots(figsize=(10.6, 6.6))
    style_axes(ax)

    for coupling_key in ["resource_division", "joint_waveform", "other", "missing"]:
        subset = valid[valid["coupling_mode_norm"] == coupling_key]
        if subset.empty:
            continue
        ax.scatter(
            subset["drmin_m"],
            subset["rate_gbps"],
            s=70,
            marker=COUPLING_MARKERS[coupling_key],
            c=subset["medium"].map(medium_color),
            alpha=0.28,
            linewidths=0,
            zorder=1,
        )

    pareto_draw_order = ["resource_division", "joint_waveform", "other", "missing"]
    for coupling_key in pareto_draw_order:
        subset = pareto[pareto["coupling_mode_norm"] == coupling_key]
        if subset.empty:
            continue
        row = subset.iloc[0]
        ax.scatter(
            row["drmin_m"],
            row["rate_gbps"],
            s=300 if coupling_key == "resource_division" else 235,
            marker=COUPLING_MARKERS.get(row["coupling_mode_norm"], "o"),
            facecolors="white",
            edgecolors=medium_color(row["medium"]),
            linewidths=2.4,
            zorder=5 if coupling_key == "resource_division" else 6,
        )

    shared_xy = (pareto.iloc[0]["drmin_m"], pareto.iloc[0]["rate_gbps"])
    ax.annotate(
        "Hybrid\nresource division",
        xy=shared_xy,
        xytext=(0.0050, 58),
        textcoords="data",
        fontsize=10,
        color=medium_color("hybrid"),
        arrowprops={"arrowstyle": "-", "lw": 1.0, "color": medium_color("hybrid")},
        ha="left",
    )
    ax.annotate(
        "Wireless FSO\njoint waveform",
        xy=shared_xy,
        xytext=(0.0125, 155),
        textcoords="data",
        fontsize=10,
        color=medium_color("wireless_fso"),
        arrowprops={"arrowstyle": "-", "lw": 1.0, "color": medium_color("wireless_fso")},
        ha="left",
    )

    ax.set_xlabel(r"Bandwidth-limited resolution $\Delta r_{\min}$ (m)", fontsize=12, color="#22313D")
    ax.set_ylabel(r"Communication rate $R$ (Gbps)", fontsize=12, color="#22313D")
    ax.set_title("CRQ-valid subset and illustrative Pareto points", fontsize=13, color="#1F2F3A", pad=12)
    ax.set_xlim(0.002, 30)
    ax.set_ylim(0.8, 500)

    ax.text(
        0.04,
        0.93,
        "CRQ-valid 20  |  Pareto 2\nBoth Pareto points share the same operating coordinate.",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        color="#20303C",
        bbox={
            "boxstyle": "round,pad=0.35,rounding_size=0.2",
            "facecolor": "white",
            "edgecolor": "#BFC8D0",
        },
    )

    represented_media = [m for m in MEDIUM_ORDER if m in set(valid["medium"].dropna())]
    medium_legend = fig.legend(
        handles=medium_handles(represented_media),
        title="Medium class",
        loc="center left",
        bbox_to_anchor=(0.84, 0.62),
        frameon=False,
        fontsize=10,
        title_fontsize=11,
    )
    fig.add_artist(medium_legend)

    represented_couplings = list(valid["coupling_mode_norm"].dropna().unique()) + list(
        pareto["coupling_mode_norm"].dropna().unique()
    )
    fig.legend(
        handles=coupling_handles(represented_couplings),
        title="Coupling mode",
        loc="center left",
        bbox_to_anchor=(0.84, 0.34),
        frameon=False,
        fontsize=10,
        title_fontsize=11,
    )

    fig.text(
        0.5,
        0.065,
        "Faint markers denote the CRQ-valid governed subset, whereas the outlined markers highlight the two nondominated points. "
        "The frontier is illustrative evidence, not a modality ranking.",
        ha="center",
        fontsize=10.2,
        color="#32404D",
    )

    fig.subplots_adjust(left=0.10, right=0.80, top=0.88, bottom=0.18)
    fig.savefig(FIG_V2, dpi=300, bbox_inches="tight")
    plt.close(fig)


def copy_to_targets() -> None:
    CURRENT_FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    REVIEW_PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(FIG_V1, CURRENT_FIGURES_DIR / FIG_V1.name)
    shutil.copy2(FIG_V2, CURRENT_FIGURES_DIR / FIG_V2.name)
    shutil.copy2(FIG_V1, REVIEW_PACKAGE_DIR / FIG_V1.name)
    shutil.copy2(FIG_V2, REVIEW_PACKAGE_DIR / FIG_V2.name)


def main() -> None:
    df = load_points()
    make_fig_v1(df)
    make_fig_v2(df)
    copy_to_targets()
    print(f"Wrote {FIG_V1}")
    print(f"Wrote {FIG_V2}")


if __name__ == "__main__":
    main()
