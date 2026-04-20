from __future__ import annotations

import argparse
from pathlib import Path

from common import MODEL_DIR, get_env


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download YOLO dataset from Roboflow.")
    parser.add_argument("--workspace", default="woodenboxdetector", help="Roboflow workspace name.")
    parser.add_argument("--project", default="woodenbox", help="Roboflow project name.")
    parser.add_argument("--version", type=int, default=13, help="Dataset version.")
    parser.add_argument("--format", default="yolov11", help="Download format.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=MODEL_DIR,
        help="Folder where the dataset will be downloaded.",
    )
    return parser.parse_args()


def main() -> None:
    from roboflow import Roboflow

    args = parse_args()
    api_key = get_env("ROBOFLOW_API_KEY")
    if not api_key:
        raise RuntimeError("ROBOFLOW_API_KEY not found. Create course_examples/.env first.")

    rf = Roboflow(api_key=api_key)
    project = rf.workspace(args.workspace).project(args.project)
    version = project.version(args.version)
    dataset = version.download(args.format, location=str(args.output_dir))

    print("Dataset downloaded to:", dataset.location)
    print("Expected data.yaml:", Path(dataset.location) / "data.yaml")


if __name__ == "__main__":
    main()

