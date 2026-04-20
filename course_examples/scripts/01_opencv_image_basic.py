from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import numpy as np

from common import OUTPUTS_DIR, ensure_dir, find_sample_image


def build_demo_image() -> np.ndarray:
    image = np.zeros((480, 640, 3), dtype=np.uint8)
    image[:] = (30, 30, 30)
    cv2.rectangle(image, (60, 80), (280, 300), (0, 255, 0), 3)
    cv2.circle(image, (420, 220), 90, (255, 120, 0), -1)
    cv2.putText(
        image,
        "OpenCV Demo",
        (160, 420),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (255, 255, 255),
        3,
    )
    return image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple OpenCV image processing example.")
    parser.add_argument("--input", type=Path, default=None, help="Path to input image.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = ensure_dir(OUTPUTS_DIR / "opencv_basic")

    image_path = args.input if args.input else find_sample_image()
    if image_path and image_path.exists():
        image = cv2.imread(str(image_path))
        source_name = image_path.stem
    else:
        image = build_demo_image()
        source_name = "synthetic_demo"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    original_path = output_dir / f"{source_name}_original.jpg"
    gray_path = output_dir / f"{source_name}_gray.jpg"
    edges_path = output_dir / f"{source_name}_edges.jpg"

    cv2.imwrite(str(original_path), image)
    cv2.imwrite(str(gray_path), gray)
    cv2.imwrite(str(edges_path), edges)

    print("Saved:")
    print(" -", original_path)
    print(" -", gray_path)
    print(" -", edges_path)


if __name__ == "__main__":
    main()

