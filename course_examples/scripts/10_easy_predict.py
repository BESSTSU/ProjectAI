from __future__ import annotations

"""Lesson 2: run prediction with a trained model.

Students usually change SOURCE, CONFIDENCE, and IMAGE_SIZE in easy_config.py.
"""

import sys
from pathlib import Path

sys.dont_write_bytecode = True

import easy_config as config
from common import DEFAULT_RUNS_DIR, OUTPUTS_DIR, PROJECT_ROOT, ensure_dir, find_best_trained_weights


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


def resolve_source() -> str | int:
    source = config.SOURCE
    if isinstance(source, int):
        return source

    text = str(source).strip()
    if not text:
        raise FileNotFoundError("SOURCE is empty. Set SOURCE in easy_config.py.")

    path = resolve_path(text)
    if path and path.exists():
        return str(path)
    if text.isdigit():
        return int(text)
    return text


def main() -> None:
    from ultralytics import YOLO

    model_path = resolve_model_path()
    source = resolve_source()
    output_dir = resolve_path(config.PREDICT_OUTPUT_DIR) or (OUTPUTS_DIR / "easy_runner")
    ensure_dir(output_dir)
    save_dir = output_dir / config.PREDICT_OUTPUT_NAME

    kwargs = {
        "source": source,
        "conf": config.CONFIDENCE,
        "imgsz": config.IMAGE_SIZE,
        "save": config.SAVE_OUTPUT,
        "show": config.SHOW_WINDOW,
        "project": str(output_dir),
        "name": config.PREDICT_OUTPUT_NAME,
        "exist_ok": True,
    }
    device = resolve_device()
    if device is not None:
        kwargs["device"] = device

    model = YOLO(str(model_path))
    results = model.predict(**kwargs)

    print("Prediction complete.")
    print("Model:", model_path)
    print("Source:", source)
    print("Saved results in:", save_dir)
    print("Detections returned:", len(results))


if __name__ == "__main__":
    main()
