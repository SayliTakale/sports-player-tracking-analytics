import pandas as pd
import math


def compute_player_stats(csv_path, fps=30):
    df = pd.read_csv(csv_path)

    # Frames tracked
    frames_tracked = len(df)

    # Time on screen
    time_seconds = frames_tracked / fps

    # Distance covered (pixels)
    distance = 0.0
    for i in range(1, len(df)):
        x1, y1 = df.loc[i - 1, ["x", "y"]]
        x2, y2 = df.loc[i, ["x", "y"]]
        distance += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Average speed
    avg_speed = distance / time_seconds if time_seconds > 0 else 0

    return {
        "Frames Tracked": frames_tracked,
        "Time on Screen (sec)": round(time_seconds, 2),
        "Distance Covered (pixels)": round(distance, 2),
        "Average Speed (px/sec)": round(avg_speed, 2),
    }
