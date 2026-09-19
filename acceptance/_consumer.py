"""Install the target package into a fresh environment, then call its entrypoint."""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import venv


ROOT = Path(__file__).resolve().parents[1]


def run_installed(record: str) -> subprocess.CompletedProcess[str]:
    with TemporaryDirectory() as directory:
        environment = Path(directory) / "venv"
        venv.EnvBuilder(with_pip=True).create(environment)
        python = environment / "bin" / "python"
        entrypoint = environment / "bin" / "mission-parser"
        subprocess.run([str(python), "-m", "pip", "install", "--no-deps", "--no-build-isolation",
                        str(ROOT)], check=True, capture_output=True, text=True)
        return subprocess.run([str(entrypoint), record], capture_output=True, text=True)
