"""Tiny standard-library wheel builder for this isolated qualification target."""
from __future__ import annotations

from base64 import urlsafe_b64encode
from hashlib import sha256
from pathlib import Path
import csv
from io import StringIO
from zipfile import ZIP_DEFLATED, ZipFile


NAME = "forge_mission_qualification_parser"
VERSION = "0.1.0"
DIST = f"{NAME}-{VERSION}.dist-info"
WHEEL = f"{NAME}-{VERSION}-py3-none-any.whl"


def get_requires_for_build_wheel(config_settings=None):
    return []


def _metadata():
    return {
        f"{DIST}/METADATA": (f"Metadata-Version: 2.1\nName: forge-mission-qualification-parser\n"
                              f"Version: {VERSION}\nRequires-Python: >=3.11\n").encode(),
        f"{DIST}/WHEEL": b"Wheel-Version: 1.0\nGenerator: qualification-build\nRoot-Is-Purelib: true\nTag: py3-none-any\n",
        f"{DIST}/entry_points.txt": b"[console_scripts]\nmission-parser = mission_parser.cli:main\n",
    }


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    folder = Path(metadata_directory) / DIST
    folder.mkdir(parents=True, exist_ok=True)
    for name, value in _metadata().items():
        (Path(metadata_directory) / name).write_bytes(value)
    return DIST


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    source = Path(__file__).resolve().parent
    files = {path.relative_to(source).as_posix(): path.read_bytes()
             for path in (source / "mission_parser").glob("*.py")}
    files.update(_metadata())
    record = StringIO()
    writer = csv.writer(record, lineterminator="\n")
    for name, value in sorted(files.items()):
        digest = urlsafe_b64encode(sha256(value).digest()).rstrip(b"=").decode()
        writer.writerow((name, f"sha256={digest}", len(value)))
    writer.writerow((f"{DIST}/RECORD", "", ""))
    destination = Path(wheel_directory) / WHEEL
    with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
        for name, value in files.items():
            archive.writestr(name, value)
        archive.writestr(f"{DIST}/RECORD", record.getvalue())
    return WHEEL
