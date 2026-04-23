from __future__ import annotations

"""Lesson 4: test the trained model with a webcam.

Students usually change CAMERA_INDEX, CONFIDENCE, and IMAGE_SIZE in easy_config.py.
"""

import sys
from pathlib import Path

sys.dont_write_bytecode = True

import cv2

import easy_config as config
from common import DEFAULT_RUNS_DIR, PROJECT_ROOT, find_best_trained_weights


def resolve_path(value: str | None) -> Path | None:
    if value in (None, ""):
        return None
    path = Path(value)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def resolve_device() -> str | int | None:
    value = config.DEVICE
    if value in (None, ""):
        return None
    return value


def resolve_model_path() -> Path:
    configured = resolve_path(config.MODEL_PATH)
    if configured and configured.exists():
        return configured

    best = find_best_trained_weights(DEFAULT_RUNS_DIR)
    if best and best.exists():
        return best

    raise FileNotFoundError("Model not found. Set MODEL_PATH in easy_config.py or train a model first.")


def main() -> None:
    from ultralytics import YOLO

    model_path = resolve_model_path()
    model = YOLO(str(model_path))

    cap = cv2.VideoCapture(config.CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)

    if not cap.isOpened():
        raise RuntimeError("Cannot open camera.")

    device = resolve_device()

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Camera read failed.")
                break

            kwargs = {
                "source": frame,
                "imgsz": config.IMAGE_SIZE,
                "conf": config.CONFIDENCE,
                "verbose": False,
            }
            if device is not None:
                kwargs["device"] = device

            results = model.predict(**kwargs)
            annotated = results[0].plot()
            cv2.imshow("Easy YOLO Webcam", annotated)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
