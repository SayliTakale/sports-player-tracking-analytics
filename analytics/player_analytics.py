import cv2
import csv
import math
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 540


def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def player_analytics(video_path):
    model = YOLO("yolov8n.pt")

    tracker = DeepSort(
        max_age=30,
        n_init=3,
        max_iou_distance=0.7
    )

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("ERROR: Video not opened")
        return

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    frame_id = 0
    player_positions = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_id += 1
        results = model(frame, classes=[0], conf=0.4)
        detections = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                conf = float(box.conf[0])
                detections.append(
                    ([int(x1), int(y1), int(x2), int(y2)], conf, 0)
                )

        tracks = tracker.update_tracks(detections, frame=frame)

        for track in tracks:
            if not track.is_confirmed():
                continue

            tid = track.track_id
            x1, y1, x2, y2 = map(int, track.to_ltrb())
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            player_positions.setdefault(tid, []).append((frame_id, cx, cy))

            cv2.rectangle(frame, (x1, y1), (x2, y2),
                          (0, 255, 0), 2)
            cv2.putText(frame, f"ID {tid}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

        display_frame = cv2.resize(frame, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
        cv2.imshow("Player Analytics", display_frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    # 📊 Save CSV + compute stats
    for tid, points in player_positions.items():
        dist = 0
        for i in range(1, len(points)):
            _, x1, y1 = points[i - 1]
            _, x2, y2 = points[i]
            dist += euclidean((x1, y1), (x2, y2))

        time_sec = len(points) / fps
        speed = dist / time_sec if time_sec > 0 else 0

        print(f"Player {tid}: Distance={dist:.2f}px Speed={speed:.2f}px/s")

        with open(f"data/outputs/player_{tid}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["frame", "x", "y"])
            writer.writerows(points)


if __name__ == "__main__":
    player_analytics("data/input_videos/match.mp4")
