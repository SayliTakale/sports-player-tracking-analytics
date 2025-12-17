# 🏟️ Sports Player Tracking & Analytics

An end-to-end **video-based sports analytics system** that detects, tracks, and analyzes players from match footage using **Computer Vision and Deep Learning** techniques.

This project demonstrates how raw sports videos can be transformed into **structured analytics**, including player statistics, movement heatmaps, trajectories, and team-wise insights.

---

## 🚀 Features

- 🎯 **Player Detection** using YOLOv8
- 🔄 **Player Tracking with Unique IDs** using DeepSORT
- 📊 **Player Statistics**
  - Distance covered
  - Average speed
  - Time on screen
  - Frames tracked
- 🔥 **Movement Heatmaps**
- 🧭 **Trajectory Visualization**
- 👥 **Team-wise Statistics** (automatic spatial grouping)
- 📈 **Interactive Dashboard** built with Streamlit
- 🧩 Clean, modular, and beginner-friendly code structure

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **OpenCV** – video processing
- **YOLOv8 (Ultralytics)** – player detection
- **DeepSORT** – multi-object tracking
- **Pandas** – analytics
- **Matplotlib** – visualization
- **Streamlit** – dashboard UI

---

## 📂 Project Structure

sports_player_tracking/
│
├── data/
│ ├── input_videos/ # Input match videos (ignored in GitHub)
│ └── outputs/ # Generated CSV analytics (ignored in GitHub)
│
├── detection/
│ └── player_detection.py # Player detection
│
├── tracking/
│ └── player_tracking.py # Player tracking with IDs
│
├── analytics/
│ ├── player_analytics.py # Distance, speed, CSV generation
│ ├── player_stats.py # Player statistics computation
│ ├── team_stats.py # Team-wise statistics
│ ├── heatmap.py # Heatmap visualization
│ └── trajectory.py # Trajectory visualization
│
├── dashboard/
│ └── app.py # Streamlit analytics dashboard
│
├── requirements.txt
├── .gitignore
└── README.md



---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/sports-player-tracking-analytics.git
cd sports-player-tracking-analytics
