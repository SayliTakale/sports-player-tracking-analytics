import pandas as pd
import glob
import math


def compute_distance(df):
    dist = 0.0
    for i in range(1, len(df)):
        x1, y1 = df.loc[i - 1, ["x", "y"]]
        x2, y2 = df.loc[i, ["x", "y"]]
        dist += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def team_wise_statistics(data_path="data/outputs/player_*.csv", fps=30):
    player_files = glob.glob(data_path)

    players = []

    # Compute per-player stats
    for file in player_files:
        player_id = int(file.split("_")[-1].replace(".csv", ""))
        df = pd.read_csv(file)

        avg_x = df["x"].mean()
        distance = compute_distance(df)
        time_sec = len(df) / fps
        speed = distance / time_sec if time_sec > 0 else 0

        players.append({
            "player_id": player_id,
            "avg_x": avg_x,
            "distance": distance,
            "speed": speed
        })

    if len(players) < 2:
        print("Not enough players for team stats")
        return

    # Sort players by average X position
    players.sort(key=lambda x: x["avg_x"])

    mid = len(players) // 2
    team_a = players[:mid]
    team_b = players[mid:]

    def summarize(team):
        return {
            "Players": len(team),
            "Total Distance (px)": round(sum(p["distance"] for p in team), 2),
            "Average Speed (px/sec)": round(
                sum(p["speed"] for p in team) / len(team), 2
            )
        }

    team_stats = {
        "Team A": summarize(team_a),
        "Team B": summarize(team_b)
    }

    return team_stats


if __name__ == "__main__":
    stats = team_wise_statistics()
    if stats:
        for team, values in stats.items():
            print(f"\n{team}")
            for k, v in values.items():
                print(f"  {k}: {v}")
