import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Setup
PROJECT_ROOT = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST"
CSV_PATH = os.path.join(PROJECT_ROOT, "data", "ext_v4_uni.csv")
PLOT_DIR = os.path.join(PROJECT_ROOT, "analysis", "plots")
os.makedirs(PLOT_DIR, exist_ok=True)

# Load Data
print(f"Reading from {CSV_PATH}")
df = pd.read_csv(CSV_PATH)
df_clean = df.replace("NR", np.nan)

# Convert columns
numeric_cols = ["Bitrate_Gbps", "Resolution_m", "Distance_m", "Wavelength_nm"]
for col in numeric_cols:
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

# Filter
df_viz = df_clean.dropna(subset=["Bitrate_Gbps", "Distance_m"]).copy()
print(f"Data points for Bitrate vs Distance: {len(df_viz)}")

# Simplify Scenarios
def simplify_scenario(s):
    s = str(s).lower()
    if "fiber" in s or "fibre" in s or "cabled" in s: return "Fiber-ISAC"
    if "fso" in s or "free-space" in s: return "FSO-ISAC"
    if "vlc" in s or "visible" in s: return "VLC-ISAC"
    if "lidar" in s: return "LiDAR-ISAC"
    return "Hybrid"

df_viz['Scenario_Group'] = df_viz['Scenario'].apply(simplify_scenario)

# --- Plot 1: Bitrate vs Distance ---
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_viz, x="Distance_m", y="Bitrate_Gbps", 
    hue="Scenario_Group", style="Scenario_Group", 
    s=100, alpha=0.8, palette="viridis"
)
plt.xscale("log")
plt.yscale("log")
plt.title("O-ISAC Trade-off: Bitrate vs. Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Data Rate (Gbps)")
plt.savefig(os.path.join(PLOT_DIR, "v4_trend_bitrate_vs_distance.png"))
print("Saved v4_trend_bitrate_vs_distance.png")

# --- Plot 2: Resolution vs Bitrate ---
plt.figure(figsize=(10, 6))
df_res = df_clean.dropna(subset=["Bitrate_Gbps", "Resolution_m"]).copy()
print(f"Data points for Resolution vs Bitrate: {len(df_res)}")

sns.scatterplot(
    data=df_res, x="Bitrate_Gbps", y="Resolution_m",
    s=100, color="crimson", alpha=0.7
)
plt.xscale("log")
plt.yscale("log")
plt.gca().invert_yaxis() # Lower resolution is better
plt.title("O-ISAC Capability: Resolution vs. Bitrate")
plt.ylabel("Sensing Resolution (m) [Inverted]")
plt.xlabel("Data Rate (Gbps)")
plt.savefig(os.path.join(PLOT_DIR, "v4_trend_resolution_vs_bitrate.png"))
print("Saved v4_trend_resolution_vs_bitrate.png")
