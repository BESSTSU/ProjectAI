from __future__ import annotations

"""Lesson 3: train a custom YOLO model.

Students usually change BASE_MODEL, EPOCHS, BATCH, and TRAIN_RUN_NAME in easy_config.py.
"""

import sys
from pathlib import Path

sys.dont_write_bytecode = True

import easy_config as config
from common import PROJECT_ROOT, ensure_dir


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


def main() -> None:
    from ultralytics import YOLO
    import torch

    data_yaml = resolve_path(config.DATA_YAML)
    if not data_yaml or not data_yaml.exists():
        raise FileNotFoundError(f"Dataset yaml not found: {config.DATA_YAML}")

    project_dir = resolve_path(config.TRAIN_PROJECT_DIR)
    if not project_dir:
        raise FileNotFoundError("TRAIN_PROJECT_DIR is empty.")

    ensure_dir(project_dir)
    device = resolve_device()
    if device is None:
        device = 0 if torch.cuda.is_available() else "cpu"

    model = YOLO(config.BASE_MODEL)
    model.train(
        data=str(data_yaml),
        epochs=config.EPOCHS,
        imgsz=config.IMAGE_SIZE,
        batch=config.BATCH,
        device=device,
        project=str(project_dir),
        name=config.TRAIN_RUN_NAME,
    )

    print("Training complete.")
    print("Data:", data_yaml)
    print("Base model:", config.BASE_MODEL)
    print("Device:", device)
    print("Run output:", project_dir / config.TRAIN_RUN_NAME)


if __name__ == "__main__":
    main()
