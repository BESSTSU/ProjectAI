from __future__ import annotations

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

