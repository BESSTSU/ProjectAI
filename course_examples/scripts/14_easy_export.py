from __future__ import annotations

"""Lesson 4: export a trained model for deployment."""

import sys
from pathlib import Path

sys.dont_write_bytecode = True

import easy_config as config
from common import DEFAULT_RUNS_DIR, PROJECT_ROOT, find_best_trained_weights


def resolve_path(value: str | None) -> Path | None:
    if value in (None, ""):
        return None
    path = Path(value)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


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
    exported = model.export(
        format=config.EXPORT_FORMAT,
        imgsz=config.IMAGE_SIZE,
        half=config.EXPORT_HALF,
    )

    print("Export complete.")
    print("Model:", model_path)
    print("Exported artifact:", exported)


if __name__ == "__main__":
    main()
