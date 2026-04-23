from __future__ import annotations

import argparse
import time
from pathlib import Path

import cv2

from common import find_best_trained_weights


def default_model_path() -> Path | None:
    return find_best_trained_weights()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run real-time YOLO inference from Raspberry Pi webcam.")
    parser.add_argument("--model", type=Path, default=default_model_path(), help="Path to weights.")
    parser.add_argument("--camera", type=int, default=0, help="Camera index.")
    parser.add_argument("--width", type=int, default=640, help="Capture width.")
    parser.add_argument("--height", type=int, default=480, help="Capture height.")
    parser.add_argument("--imgsz", type=int, default=640, help="YOLO input image size.")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold.")
    return parser.parse_args()


def main() -> None:
    from ultralytics import YOLO

    args = parse_args()
    if not args.model or not args.model.exists():
        raise FileNotFoundError("Model not found. Train first or pass --model explicitly.")

    model = YOLO(str(args.model))
    cap = cv2.VideoCapture(args.camera)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

    if not cap.isOpened():
        raise RuntimeError("Cannot open camera.")

    prev_time = time.time()
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Camera read failed.")
                break

            results = model.predict(frame, imgsz=args.imgsz, conf=args.conf, verbose=False)
            annotated = results[0].plot()

            now = time.time()
            fps = 1.0 / max(now - prev_time, 1e-6)
            prev_time = now

            cv2.putText(
                annotated,
                f"FPS: {fps:.1f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )
            cv2.putText(
                annotated,
                "Press q to quit",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2,
            )

            cv2.imshow("Raspberry Pi YOLO", annotated)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
