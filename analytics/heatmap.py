import pandas as pd
import matplotlib.pyplot as plt


def generate_heatmap(csv_path):
    df = pd.read_csv(csv_path)

    x = df["x"]
    y = df["y"]

    plt.figure(figsize=(8, 6))
    plt.hist2d(x, y, bins=50, cmap="hot")
    plt.colorbar(label="Movement Frequency")
    plt.title("Player Movement Heatmap")
    plt.xlabel("X Position (pixels)")
    plt.ylabel("Y Position (pixels)")
    plt.gca().invert_yaxis()  # Match video coordinate system
    plt.show()


if __name__ == "__main__":
    generate_heatmap("data/outputs/player_1.csv")
