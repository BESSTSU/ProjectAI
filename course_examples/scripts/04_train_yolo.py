from __future__ import annotations

import argparse
from pathlib import Path

from common import DEFAULT_DATA_YAML, MODEL_DIR, ensure_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a custom YOLO model.")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_YAML, help="Path to data.yaml")
    parser.add_argument("--model", default="yolo11s.pt", help="Base model name or weights path.")
    parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs.")
    parser.add_argument("--imgsz", type=int, default=640, help="Input image size.")
    parser.add_argument("--batch", type=int, default=8, help="Batch size.")
    parser.add_argument("--device", default=None, help="CUDA device id or cpu. Auto if omitted.")
    parser.add_argument("--name", default="course_train", help="Run name.")
    parser.add_argument("--project", type=Path, default=MODEL_DIR / "runs" / "course", help="Output project dir.")
    return parser.parse_args()


def main() -> None:
    from ultralytics import YOLO
    import torch

    args = parse_args()
    if not args.data.exists():
        raise FileNotFoundError(f"Dataset yaml not found: {args.data}")

    ensure_dir(args.project)

    if args.device:
        device = args.device
    else:
        device = 0 if torch.cuda.is_available() else "cpu"

    print("Using dataset:", args.data)
    print("Using model:", args.model)
    print("Using device:", device)

    model = YOLO(args.model)
    model.train(
        data=str(args.data),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=device,
        project=str(args.project),
        name=args.name,
    )

    print("Training finished.")
    print("Best weights should be under:", args.project / args.name / "weights" / "best.pt")


if __name__ == "__main__":
    main()

