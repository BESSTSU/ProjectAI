from __future__ import annotations

import importlib
import platform
import sys

from common import DEFAULT_DATA_YAML, PROJECT_ROOT


def check_module(name: str) -> str:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        return f"OK - {name} {version}"
    except Exception as exc:  # pragma: no cover
        return f"Missing - {name} ({exc})"


def main() -> None:
    print("Project root:", PROJECT_ROOT)
    print("Python:", sys.version.split()[0])
    print("Platform:", platform.platform())
    print("Dataset yaml exists:", DEFAULT_DATA_YAML.exists(), DEFAULT_DATA_YAML)
    print(check_module("cv2"))
    print(check_module("ultralytics"))
    print(check_module("roboflow"))
    print(check_module("yaml"))


if __name__ == "__main__":
    main()

