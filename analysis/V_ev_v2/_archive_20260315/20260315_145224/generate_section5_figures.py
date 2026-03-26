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

FIG_V1 = DRAFTS_DIR / "fig_v_1.png"
FIG_V2 = DRAFTS_DIR / "fig_v_2.png"


MEDIUM_COLORS = {
    "hybrid": "#1f77b4",
    "cabled_fibre": "#d95f02",
    "wireless_fso": "#2ca02c",
    "wireless_vlc": "#9467bd",
    "wireless": "#8c564b",
    "wireless_rf": "#e377c2",
    "terahertz": "#17becf",
    "other": "#7f7f7f",
}

COUPLING_MARKERS = {
    "resource_division": "o",
    "joint_waveform": "s",
    "other": "^",
    "missing": "X",
}


def load_points() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "section5C_tradeoff_points.csv")
    for col in ["governance_blocked", "drmin_eligible", "crq_eligible"]:
        df[col] = df[col].astype(str).str.lower().map({"true": True, "false": False})
    df["coupling_mode_norm"] = (
        df["coupling_mode"]
        .fillna("missing")
        .astype(str)
        .str.strip()
        .str.replace(" ", "_", regex=False)
    )
    df.loc[~df["coupling_mode_norm"].isin(COUPLING_MARKERS), "coupling_mode_norm"] = "other"
    return df


def medium_color(medium: str) -> str:
    return MEDIUM_COLORS.get(medium, MEDIUM_COLORS["other"])


def medium_handles(media: list[str]) -> list[Line2D]:
    return [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=medium_color(m), markeredgecolor="black",
               markersize=8, label=m)
        for m in media
    ]


def add_coupling_legend(ax) -> None:
    handles = [
        Line2D([0], [0], marker=marker, color="black", linestyle="none", markersize=8, label=label)
        for label, marker in [
            ("resource_division", COUPLING_MARKERS["resource_division"]),
            ("joint_waveform", COUPLING_MARKERS["joint_waveform"]),
            ("other/missing", COUPLING_MARKERS["missing"]),
        ]
    ]
    ax.legend(
        handles=handles,
        title="Coupling",
        loc="upper right",
        frameon=False,
        fontsize=9,
        title_fontsize=10,
    )


def plot_panel(ax, background: pd.DataFrame, foreground: pd.DataFrame, x_col: str, x_label: str, title: str) -> None:
    bg = background[(background["r_bps"] > 0) & (background[x_col] > 0)].copy()
    fg = foreground[(foreground["r_bps"] > 0) & (foreground[x_col] > 0)].copy()

    ax.scatter(
        bg[x_col],
        bg["r_bps"],
        s=26,
        c="#d8d8d8",
        alpha=0.35,
        linewidths=0,
        zorder=1,
        label="Raw context",
    )

    for coupling, marker in COUPLING_MARKERS.items():
        subset = fg[fg["coupling_mode_norm"] == coupling]
        if subset.empty:
            continue
        ax.scatter(
            subset[x_col],
            subset["r_bps"],
            s=72,
            c=subset["medium"].map(medium_color),
            marker=marker,
            edgecolors="black",
            linewidths=0.7,
            alpha=0.95,
            zorder=3,
        )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid(True, which="major", color="#d9d9d9", linewidth=0.8, alpha=0.8)
    ax.grid(True, which="minor", color="#eeeeee", linewidth=0.4, alpha=0.7)
    ax.set_xlabel(x_label, fontsize=11)
    ax.set_ylabel("Rate, R (bps)", fontsize=11)
    ax.set_title(title, fontsize=12, fontweight="bold", pad=10)

    text = f"Raw context: n={len(bg)}\nGoverned usable: n={len(fg)}"
    ax.text(
        0.03,
        0.04,
        text,
        transform=ax.transAxes,
        fontsize=9,
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "white", "edgecolor": "#bdbdbd"},
    )


def make_fig_v1(df: pd.DataFrame) -> None:
    usable = df[df["governance_blocked"] == False].copy()
    res_bg = df[df["r_bps"].notna() & df["drmin_m"].notna()]
    res_fg = usable[usable["r_bps"].notna() & usable["drmin_m"].notna() & (usable["drmin_eligible"] == True)]
    acc_bg = df[df["r_bps"].notna() & df["sigma_r_m"].notna()]
    acc_fg = usable[usable["r_bps"].notna() & usable["sigma_r_m"].notna()]

    plt.rcParams.update({
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
    })

    fig, axes = plt.subplots(1, 2, figsize=(14, 6.6))
    plot_panel(
        axes[0],
        res_bg,
        res_fg,
        "drmin_m",
        r"Resolution, $\Delta r_{\min}$ (m)",
        "(a) Governed rate-resolution cloud",
    )
    plot_panel(
        axes[1],
        acc_bg,
        acc_fg,
        "sigma_r_m",
        r"Accuracy, $\sigma_r$ (m)",
        "(b) Governed rate-accuracy cloud",
    )

    media = ["hybrid", "cabled_fibre", "wireless_fso", "wireless_vlc", "wireless", "wireless_rf", "terahertz", "other"]
    handles = medium_handles([m for m in media if m in set(df["medium"].dropna())])
    fig.legend(
        handles=handles,
        title="Medium",
        loc="upper center",
        bbox_to_anchor=(0.5, 0.965),
        ncol=4,
        frameon=False,
        fontsize=9,
        title_fontsize=10,
    )
    add_coupling_legend(axes[1])

    fig.suptitle(
        "Fig. V-1. Governed operating cloud after metric-role and measurement-plane filtering",
        fontsize=14,
        fontweight="bold",
        y=0.995,
    )
    fig.subplots_adjust(top=0.84, bottom=0.16, wspace=0.12)
    fig.text(
        0.5,
        0.03,
        "Gray points show raw context; colored points show governance-usable evidence only. "
        "Resolution and accuracy are separated by design to avoid metric-role collapse.",
        ha="center",
        fontsize=10,
    )
    fig.savefig(FIG_V1, dpi=300, bbox_inches="tight")
    plt.close(fig)


def make_fig_v2(df: pd.DataFrame) -> None:
    valid = df[(df["crq_eligible"] == True) & df["r_bps"].notna() & df["drmin_m"].notna()].copy()
    pareto = pd.read_csv(DATA_DIR / "section5E_pareto_points.csv")
    pareto["coupling_mode_norm"] = (
        pareto["coupling_mode"].fillna("missing").astype(str).str.strip().str.replace(" ", "_", regex=False)
    )
    pareto.loc[~pareto["coupling_mode_norm"].isin(COUPLING_MARKERS), "coupling_mode_norm"] = "other"

    fig, ax = plt.subplots(figsize=(8.6, 6.4))

    for coupling, marker in COUPLING_MARKERS.items():
        subset = valid[valid["coupling_mode_norm"] == coupling]
        if subset.empty:
            continue
        ax.scatter(
            subset["drmin_m"],
            subset["r_bps"],
            s=46,
            c=subset["medium"].map(medium_color),
            alpha=0.28,
            marker=marker,
            linewidths=0,
            zorder=1,
        )

    # Pareto points overlay: same coordinates are intentionally preserved.
    for _, row in pareto.iterrows():
        ax.scatter(
            row["drmin_m"],
            row["r_bps"],
            s=220,
            facecolors="none",
            edgecolors=medium_color(row["medium"]),
            marker=COUPLING_MARKERS.get(row["coupling_mode_norm"], "o"),
            linewidths=2.3,
            zorder=4,
        )

    ax.annotate(
        "Hybrid Pareto\nresource_division",
        xy=(pareto.iloc[0]["drmin_m"], pareto.iloc[0]["r_bps"]),
        xytext=(0.006, 7.0e10),
        textcoords="data",
        fontsize=9.5,
        arrowprops={"arrowstyle": "-", "lw": 1.0, "color": medium_color("hybrid")},
        color=medium_color("hybrid"),
    )
    ax.annotate(
        "Wireless FSO Pareto\njoint_waveform",
        xy=(pareto.iloc[1]["drmin_m"], pareto.iloc[1]["r_bps"]),
        xytext=(0.0022, 1.45e11),
        textcoords="data",
        fontsize=9.5,
        arrowprops={"arrowstyle": "-", "lw": 1.0, "color": medium_color("wireless_fso")},
        color=medium_color("wireless_fso"),
    )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid(True, which="major", color="#d9d9d9", linewidth=0.8, alpha=0.8)
    ax.grid(True, which="minor", color="#eeeeee", linewidth=0.4, alpha=0.7)
    ax.set_xlabel(r"Resolution, $\Delta r_{\min}$ (m)", fontsize=11)
    ax.set_ylabel("Rate, R (bps)", fontsize=11)
    ax.set_title("Sparse admissible frontier from the CRQ-valid subset", fontsize=12, fontweight="bold", pad=10)

    legend_handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=medium_color("hybrid"), markeredgecolor="black",
               markersize=8, label="hybrid"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=medium_color("wireless_fso"), markeredgecolor="black",
               markersize=8, label="wireless_fso"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor="#bdbdbd", markeredgecolor="none",
               markersize=8, label="other valid points"),
        Line2D([0], [0], marker="o", color="black", linestyle="none", markersize=8, label="resource_division Pareto"),
        Line2D([0], [0], marker="s", color="black", linestyle="none", markersize=8, label="joint_waveform Pareto"),
    ]
    ax.legend(handles=legend_handles, title="Legend", loc="upper right", frameon=False, fontsize=9, title_fontsize=10)

    ax.text(
        0.03,
        0.05,
        "CRQ-valid points: n=20\nPareto points: n=2\nBoth Pareto points share the same operating coordinate.",
        transform=ax.transAxes,
        fontsize=9,
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "white", "edgecolor": "#bdbdbd"},
    )

    fig.suptitle(
        "Fig. V-2. Sparse admissible frontier after CRQ-eligibility compression",
        fontsize=14,
        fontweight="bold",
        y=0.98,
    )
    fig.subplots_adjust(top=0.90, bottom=0.16)
    fig.text(
        0.5,
        0.03,
        "Faint markers denote the 20 CRQ-valid points; outlined markers denote the 2 nondominated points. "
        "The frontier is illustrative and should not be read as a stable modality ranking.",
        ha="center",
        fontsize=10,
    )
    fig.savefig(FIG_V2, dpi=300, bbox_inches="tight")
    plt.close(fig)


def copy_to_current_bundle() -> None:
    CURRENT_FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(FIG_V1, CURRENT_FIGURES_DIR / FIG_V1.name)
    shutil.copy2(FIG_V2, CURRENT_FIGURES_DIR / FIG_V2.name)


def main() -> None:
    df = load_points()
    make_fig_v1(df)
    make_fig_v2(df)
    copy_to_current_bundle()
    print(f"Wrote {FIG_V1}")
    print(f"Wrote {FIG_V2}")


if __name__ == "__main__":
    main()
