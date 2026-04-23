from __future__ import annotations

import argparse
from pathlib import Path

from common import OUTPUTS_DIR, ensure_dir, find_best_trained_weights, find_sample_image


def default_model_path() -> Path | None:
    return find_best_trained_weights()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run prediction on one image.")
    parser.add_argument("--model", type=Path, default=default_model_path(), help="Path to YOLO weights.")
    parser.add_argument("--source", type=Path, default=find_sample_image(), help="Path to input image.")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold.")
    return parser.parse_args()


def main() -> None:
    from ultralytics import YOLO

    args = parse_args()
    if not args.model or not args.model.exists():
        raise FileNotFoundError("Model not found. Train first or pass --model explicitly.")
    if not args.source or not args.source.exists():
        raise FileNotFoundError("Input image not found. Pass --source explicitly.")

    output_dir = ensure_dir(OUTPUTS_DIR / "predict")
    model = YOLO(str(args.model))
    results = model.predict(
        source=str(args.source),
        conf=args.conf,
        save=True,
        project=str(output_dir),
        name="image_demo",
    )

    print("Prediction complete.")
    print("Image source:", args.source)
    print("Model:", args.model)
    print("Saved results in:", output_dir / "image_demo")
    print("Detections returned:", len(results))


if __name__ == "__main__":
    main()
