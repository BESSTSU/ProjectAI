from __future__ import annotations

import csv
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None


EXAMPLES_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = EXAMPLES_ROOT.parent
MODEL_DIR = PROJECT_ROOT / "Model"
OUTPUTS_DIR = EXAMPLES_ROOT / "outputs"
DEFAULT_DATA_YAML = MODEL_DIR / "Woodenbox-13" / "data.yaml"
DEFAULT_RUNS_DIR = MODEL_DIR / "runs" / "detect"


def load_env() -> None:
    env_path = EXAMPLES_ROOT / ".env"
    if load_dotenv and env_path.exists():
        load_dotenv(env_path)


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def first_existing_path(*paths: Path) -> Path | None:
    for path in paths:
        if path.exists():
            return path
    return None


def _read_best_map(csv_path: Path) -> float:
    best_map = -1.0
    with csv_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = row.get("metrics/mAP50-95(B)")
            if value is None:
                continue
            best_map = max(best_map, float(value))
    return best_map


def find_best_trained_weights(runs_dir: Path = DEFAULT_RUNS_DIR) -> Path | None:
    best_score = -1.0
    best_weights: Path | None = None
    fallback_weights: list[Path] = []

    for run_dir in sorted(runs_dir.glob("train*")):
        weights_path = run_dir / "weights" / "best.pt"
        if not weights_path.exists():
            continue

        fallback_weights.append(weights_path)

        csv_path = run_dir / "results.csv"
        if not csv_path.exists():
            continue

        score = _read_best_map(csv_path)
        if score > best_score:
            best_score = score
            best_weights = weights_path

    if best_weights:
        return best_weights
    if fallback_weights:
        return max(fallback_weights, key=lambda path: path.stat().st_mtime)
    return None


def find_sample_image() -> Path | None:
    candidates = [
        MODEL_DIR / "Woodenbox-13" / "valid" / "images",
        MODEL_DIR / "Woodenbox-13" / "test" / "images",
        MODEL_DIR / "Woodenbox-13" / "train" / "images",
    ]
    for folder in candidates:
        if folder.exists():
            for ext in ("*.jpg", "*.jpeg", "*.png"):
                found = sorted(folder.glob(ext))
                if found:
                    return found[0]
    return None


def get_env(name: str, default: str | None = None) -> str | None:
    load_env()
    return os.getenv(name, default)
