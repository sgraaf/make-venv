from pathlib import Path

import pytest
from click.testing import CliRunner

from make_venv.cli import DEFAULT_DEST, SYSTEM, cli


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_version(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert result.output.startswith("cli, version ")


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
