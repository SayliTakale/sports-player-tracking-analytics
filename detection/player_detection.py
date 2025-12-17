import cv2
from ultralytics import YOLO

DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 540


def detect_players(video_path):
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("ERROR: Video not opened")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, classes=[0], conf=0.4)

        for r in results:
            for box in r.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2),
                              (0, 255, 0), 2)

        # 🔽 Resize only for display
        display_frame = cv2.resize(frame, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
        cv2.imshow("Player Detection", display_frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_players("data/input_videos/match.mp4")
