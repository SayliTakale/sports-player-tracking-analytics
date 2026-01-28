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





---

## ▶️ How to Run the Project (Windows)

---

1️⃣ Create and Activate Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Input Video
Place a sports video file in:
data/input_videos/match.mp4
Note: Input videos are intentionally ignored in GitHub and must be added locally.

4️⃣ Run Player Detection 
Detect players with bounding boxes only:
python detection/player_detection.py
Press ESC to close the video window.

5️⃣ Run Player Tracking 
Track players with persistent IDs:
python tracking/player_tracking.py
Press ESC to stop the video.

6️⃣ Generate Player Analytics
Generate CSV files required for analytics and dashboard:
python analytics/player_analytics.py
CSV files will be saved in:
data/outputs/

7️⃣ Launch Analytics Dashboard
Run the Streamlit dashboard using the virtual environment:
python -m streamlit run dashboard/app.py
The dashboard will open automatically in your browser.

---

## 📝 License

This project is released under a **Dual Licensing model**.

```
### Academic / Research Use
- Students, educators, and researchers may **view, download, and run**
  this project for learning or research purposes.
- **Prior written permission from the author is required** before using
  the project for academic submissions, research work, or publications.

### Commercial / Organizational Use
- Any use by companies, startups, organizations, or for-profit entities
  **requires a paid commercial license**.
- Commercial use without permission is strictly prohibited and may result
  in legal action.

For full legal terms, see the [`LICENSE`](./LICENSE) file.

For permission or commercial licensing inquiries, contact:
**Sayli Takale**
saylitakale2308@gmail.com
```
