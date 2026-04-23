from __future__ import annotations

import argparse
from pathlib import Path

from common import find_best_trained_weights


def default_model_path() -> Path | None:
    return find_best_trained_weights()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a YOLO model for deployment.")
    parser.add_argument("--model", type=Path, default=default_model_path(), help="Path to trained weights.")
    parser.add_argument("--format", default="openvino", help="Export format: openvino, torchscript, onnx")
    parser.add_argument("--imgsz", type=int, default=640, help="Input image size.")
    parser.add_argument("--half", action="store_true", help="Use FP16 when supported.")
    return parser.parse_args()


def main() -> None:
    from ultralytics import YOLO

    args = parse_args()
    if not args.model or not args.model.exists():
        raise FileNotFoundError("Model not found. Train first or pass --model explicitly.")

    model = YOLO(str(args.model))
    export_path = model.export(format=args.format, imgsz=args.imgsz, half=args.half)

    print("Export complete.")
    print("Model:", args.model)
    print("Exported artifact:", export_path)


if __name__ == "__main__":
    main()
