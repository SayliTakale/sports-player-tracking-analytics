import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import glob

from analytics.player_stats import compute_player_stats
from analytics.team_stats import team_wise_statistics


# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Sports Player Analytics",
    layout="wide"
)

st.title("🏟️ Sports Player Analytics Dashboard")

# ===============================
# LOAD PLAYER FILES
# ===============================
player_files = glob.glob("data/outputs/player_*.csv")

if not player_files:
    st.warning("No player data found. Please run analytics first.")
    st.stop()

player_ids = sorted([
    f.split("_")[-1].replace(".csv", "") for f in player_files
])

# ===============================
# PLAYER SELECTOR
# ===============================
player_id = st.selectbox("Select Player ID", player_ids)

csv_path = f"data/outputs/player_{player_id}.csv"
df = pd.read_csv(csv_path)

# ===============================
# PLAYER STATISTICS PANEL
# ===============================
stats = compute_player_stats(csv_path, fps=30)

st.subheader("📊 Player Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Frames Tracked", stats["Frames Tracked"])
c2.metric("Time on Screen (sec)", stats["Time on Screen (sec)"])
c3.metric("Distance Covered (px)", stats["Distance Covered (pixels)"])
c4.metric("Avg Speed (px/sec)", stats["Average Speed (px/sec)"])

st.divider()

# ===============================
# DATA + HEATMAP
# ===============================
left, right = st.columns(2)

with left:
    st.subheader("📄 Player Position Data")
    st.dataframe(df.head(25), use_container_width=True)

with right:
    st.subheader("🔥 Movement Heatmap")
    fig, ax = plt.subplots()
    ax.hist2d(df["x"], df["y"], bins=50, cmap="hot")
    ax.invert_yaxis()
    ax.set_xlabel("X Position (pixels)")
    ax.set_ylabel("Y Position (pixels)")
    st.pyplot(fig)

# ===============================
# TEAM-WISE STATISTICS
# ===============================
st.divider()
st.subheader("👥 Team-wise Statistics")

team_stats = team_wise_statistics()

if team_stats:
    colA, colB = st.columns(2)

    with colA:
        st.markdown("### 🟢 Team A")
        for key, value in team_stats["Team A"].items():
            st.metric(key, value)

    with colB:
        st.markdown("### 🔵 Team B")
        for key, value in team_stats["Team B"].items():
            st.metric(key, value)
else:
    st.info("Not enough players detected to compute team statistics.")
