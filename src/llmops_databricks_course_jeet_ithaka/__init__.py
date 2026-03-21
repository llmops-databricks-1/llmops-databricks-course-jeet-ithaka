"""Top-level package for the LLMOps Databricks course utilities."""

from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_VERSION_FILE = _PROJECT_ROOT / "version.txt"

try:
    __version__ = _VERSION_FILE.read_text().strip()
except FileNotFoundError:  # pragma: no cover - course repo should always have version.txt
    __version__ = "0.0.0"

__all__ = ["__version__"]
