"""Utility functions for make-venv."""

from __future__ import annotations

import json
import subprocess
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def collect_outdated_packages(
    python_executable: Path | str = sys.executable,
) -> list[str]:
    """Collect list of outdated package names."""
    return [
        package["name"]
        for package in json.loads(
            subprocess.check_output(
                [  # noqa: S603
                    python_executable,
                    "-m",
                    "pip",
                    "--disable-pip-version-check",
                    "list",
                    "--outdated",
                    "--format=json",
                ],
            )
            .decode()
            .strip()
        )
    ]
