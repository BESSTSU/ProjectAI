from __future__ import annotations

import argparse
import csv
from pathlib import Path

from common import DEFAULT_RUNS_DIR


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare YOLO training runs from results.csv files.")
    parser.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR, help="Directory with train runs.")
    return parser.parse_args()


def read_best_map(csv_path: Path) -> tuple[float, int]:
    best_map = -1.0
    best_epoch = -1
    with csv_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            current = float(row["metrics/mAP50-95(B)"])
            epoch = int(row["epoch"])
            if current > best_map:
                best_map = current
                best_epoch = epoch
    return best_map, best_epoch


def read_model_name(args_yaml: Path) -> str:
    for line in args_yaml.read_text(encoding="utf-8").splitlines():
        if line.startswith("model:"):
            return line.split(":", 1)[1].strip()
    return "unknown"


def main() -> None:
    args = parse_args()
    rows: list[tuple[str, str, float, int]] = []

    for run_dir in sorted(args.runs_dir.glob("train*")):
        csv_path = run_dir / "results.csv"
        args_path = run_dir / "args.yaml"
        if csv_path.exists() and args_path.exists():
            best_map, best_epoch = read_best_map(csv_path)
            model_name = read_model_name(args_path)
            rows.append((run_dir.name, model_name, best_map, best_epoch))

    rows.sort(key=lambda row: row[2], reverse=True)
    if not rows:
        print("No training results found.")
        return

    print(f"{'Run':<10} {'Model':<15} {'Best mAP50-95':<15} {'Epoch':<5}")
    print("-" * 52)
    for run_name, model_name, best_map, best_epoch in rows[:10]:
        print(f"{run_name:<10} {model_name:<15} {best_map:<15.5f} {best_epoch:<5}")


if __name__ == "__main__":
    main()

