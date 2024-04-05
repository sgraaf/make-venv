from importlib import import_module
from importlib.metadata import version
from pathlib import Path

import pytest
from click.testing import CliRunner

from make_venv.cli import DEFAULT_DEST, SYSTEM, cli

from .utils import run_command_in_shell


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_main_module() -> None:
    """Exercise (most of) the code in the `__main__` module."""
    import_module("make_venv.__main__")


def test_run_as_module() -> None:
    """Is the script runnable as a Python module?"""
    result = run_command_in_shell("python -m make_venv --help")
    assert result.exit_code == 0


def test_run_as_executable() -> None:
    """Is the script installed (as a `console_script`) and runnable as an executable?"""
    result = run_command_in_shell("make-venv --help")
    assert result.exit_code == 0


def test_version_runner(runner: CliRunner) -> None:
    """Does `--version` display the correct version?"""
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"cli, version {version('make-venv')}\n"


def test_default(runner: CliRunner) -> None:
    with runner.isolated_filesystem():
        result = runner.invoke(cli)
        assert result.exit_code == 0
        if SYSTEM == "Windows":
            assert result.output.strip().endswith(
                f"Now run:\n{DEFAULT_DEST / 'Scripts' / 'activate'}"
            )
        else:
            assert result.output.strip().endswith(
                f"Now run:\nsource {DEFAULT_DEST / 'bin' / 'activate'}"
            )
        assert DEFAULT_DEST.is_dir()


@pytest.mark.parametrize("dest", [Path(".env"), Path("subdir") / ".venv"])
def test_dest(runner: CliRunner, dest: Path) -> None:
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--dest", str(dest)])
        assert result.exit_code == 0
        if SYSTEM == "Windows":
            assert result.output.strip().endswith(
                f"Now run:\n{dest / 'Scripts' / 'activate'}"
            )
        else:
            assert result.output.strip().endswith(
                f"Now run:\nsource {dest / 'bin' / 'activate'}"
            )
        assert dest.is_dir()
