import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Display size (what you SEE)
DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 540

# Text appearance (BIG & CLEAR)
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.95      # 🔥 clearly visible
FONT_THICKNESS = 2
BOX_THICKNESS = 2


def track_players(video_path):
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

    # Get original video size
    orig_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    orig_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Scaling factors
    scale_x = DISPLAY_WIDTH / orig_w
    scale_y = DISPLAY_HEIGHT / orig_h

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 🔹 Resize FIRST
        frame = cv2.resize(frame, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

        # Detect on resized frame (fast + consistent)
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

            # Bounding box
            cv2.rectangle(
                frame, (x1, y1), (x2, y2),
                (0, 255, 0), BOX_THICKNESS
            )

            label = f"ID {tid}"
            (tw, th), _ = cv2.getTextSize(
                label, FONT, FONT_SCALE, FONT_THICKNESS
            )

            # Background rectangle
            cv2.rectangle(
                frame,
                (x1, y1 - th - 12),
                (x1 + tw + 10, y1),
                (0, 255, 0),
                -1
            )

            # Text
            cv2.putText(
                frame,
                label,
                (x1 + 5, y1 - 5),
                FONT,
                FONT_SCALE,
                (0, 0, 0),
                FONT_THICKNESS,
                cv2.LINE_AA
            )

        cv2.imshow("Player Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    track_players("data/input_videos/match.mp4")
