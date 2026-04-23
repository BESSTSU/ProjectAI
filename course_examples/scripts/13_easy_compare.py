from __future__ import annotations

"""Lesson 4: compare training runs and pick the best model."""

import sys
import csv

sys.dont_write_bytecode = True

from common import DEFAULT_RUNS_DIR


def main() -> None:
    rows: list[tuple[str, float]] = []

    for run_dir in sorted(DEFAULT_RUNS_DIR.glob("train*")):
        csv_path = run_dir / "results.csv"
        if not csv_path.exists():
            continue

        best_map = -1.0
        with csv_path.open("r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                best_map = max(best_map, float(row["metrics/mAP50-95(B)"]))
        rows.append((run_dir.name, best_map))

    rows.sort(key=lambda item: item[1], reverse=True)
    if not rows:
        print("No training results found.")
        return

    print("Top training runs:")
    for run_name, best_map in rows[:10]:
        print(f"- {run_name}: {best_map:.5f}")


if __name__ == "__main__":
    main()
