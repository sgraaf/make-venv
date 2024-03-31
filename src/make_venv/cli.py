"""Main CLI for make-venv."""

from __future__ import annotations

import platform
import subprocess
import sys
from pathlib import Path

import click

from . import __version__
from .utils import collect_outdated_packages

DEFAULT_DEST = Path(".venv")
DEFAULT_PYTHON = Path(sys.executable)
DEFAULT_SEED = True
DEFAULT_PROMPT = "<name-of-parent-directory-of-virtual-environment>"
DEFAULT_REQUIREMENT = None
DEFAULT_INSTALL_IPYTHON_KERNEL = False
DEFAULT_KERNEL_NAME = (
    "Python <version> (<name-of-parent-directory-of-virtual-environment>)"
)
DEFAULT_UPGRADE = False

SYSTEM = platform.system()


@click.command(
    context_settings={"help_option_names": ["-h", "--help"], "show_default": True},
)
@click.option(
    "-d",
    "--dest",
    "venv_dir",
    type=click.Path(file_okay=False, writable=True, path_type=Path),
    default=DEFAULT_DEST,
    help="Directory to create the virtual environment at.",
)
@click.option(
    "-p",
    "--python",
    "python_executable",
    type=click.Path(dir_okay=False, executable=True, path_type=Path),
    default=DEFAULT_PYTHON,
    metavar="PYTHON",
    help="The Python interpreter to use for the virtual environment.",
)
@click.option(
    " /-S",
    "--seed/--no-seed",
    default=DEFAULT_SEED,
    is_flag=True,
    help="Install seed packages (`pip`, `setuptools`, and `wheel`) into the virtual environment.",
)
@click.option(
    "--prompt",
    type=click.STRING,
    default=DEFAULT_PROMPT,
    metavar="PROMPT",
    help="Provide an alternative prompt prefix for the virtual environment.",
)
@click.option(
    "-r",
    "--requirement",
    "requirements_file",
    type=click.Path(dir_okay=False, readable=True, path_type=Path),
    default=DEFAULT_REQUIREMENT,
    help="Install packages from the given requirements file.",
)
@click.option(
    "-u",
    "-U",
    "--upgrade",
    default=DEFAULT_UPGRADE,
    is_flag=True,
    help="Upgrade all outdated packages to the newest available version.",
)
@click.option(
    "-k",
    "--install-ipython-kernel",
    default=DEFAULT_INSTALL_IPYTHON_KERNEL,
    is_flag=True,
    help="Install the iPython kernel into the virtual environment.",
)
@click.option(
    "-n",
    "--kernel-name",
    type=click.STRING,
    default=DEFAULT_KERNEL_NAME,
    metavar="NAME",
    help="The display name of the iPython kernel, if applicable.",
)
@click.version_option(__version__, "-v", "--version")
def cli(
    venv_dir: Path = DEFAULT_DEST,
    python_executable: Path = DEFAULT_PYTHON,
    seed: bool = DEFAULT_SEED,
    prompt: str | None = None,
    requirements_file: Path | None = DEFAULT_REQUIREMENT,
    upgrade: bool = DEFAULT_UPGRADE,
    install_ipython_kernel: bool = DEFAULT_INSTALL_IPYTHON_KERNEL,
    kernel_name: str | None = None,
) -> None:
    """A command-line utility for making a Python virtual environment."""
    # determine the name of the parent directory of the to-be-created venv
    parent_dir = venv_dir.resolve().parent.name

    # create venv
    click.echo(f"Creating virtual environment at {venv_dir}...")
    create_venv_command: list[str | Path] = [python_executable, "-m", "venv"]
    if prompt is not None:
        if prompt == DEFAULT_PROMPT:
            prompt = parent_dir
        create_venv_command += ["--prompt", prompt]
    create_venv_command.append(venv_dir)
    subprocess.run(create_venv_command, check=False)

    # get the venv's executable (interpreter)
    if SYSTEM == "Windows":
        venv_executable = venv_dir / "Scripts" / "python.exe"
    else:
        venv_executable = venv_dir / "bin" / "python"

    # install seed packages into the virtual environment, if applicable
    if seed:
        click.echo("Installing seed packages into the virtual environment...")
        subprocess.run(
            [
                venv_executable,
                "-m",
                "pip",
                "--disable-pip-version-check",
                "install",
                "pip",
                "setuptools",
                "wheel",
            ],
            stdout=subprocess.DEVNULL,
            check=False,
        )

    # install packages from the given requirements file, if applicable
    if requirements_file is not None:
        click.echo("Installing packages from the given requirements file...")
        subprocess.run(
            [
                venv_executable,
                "-m",
                "pip",
                "--disable-pip-version-check",
                "install",
                "--requirement",
                requirements_file,
            ],
            stdout=subprocess.DEVNULL,
            check=False,
        )

    # install the iPython kernel into the virtual environment, if applicable
    if install_ipython_kernel:
        click.echo("Installing the iPython kernel into the virtual environment...")

        # determine the display name of the iPython kernel
        if kernel_name is None or kernel_name == DEFAULT_KERNEL_NAME:
            python_with_version = (
                subprocess.check_output([python_executable, "-V"]).decode().strip()
            )
            kernel_name = f"{python_with_version} ({parent_dir})"

        subprocess.run(
            [
                venv_executable,
                "-m",
                "pip",
                "--disable-pip-version-check",
                "install",
                "ipykernel",
            ],
            stdout=subprocess.DEVNULL,
            check=False,
        )
        subprocess.run(
            [
                venv_executable,
                "-m",
                "ipykernel",
                "install",
                "--user",
                "--name",
                f"{parent_dir}_{venv_dir.name.removeprefix('.')}",
                "--display-name",
                kernel_name,
            ],
            stdout=subprocess.DEVNULL,
            check=False,
        )

    # upgrade all outdated packages to the newest available version, if applicable
    if upgrade:
        click.echo("Upgrading all outdated packages to the newest available version...")
        for outdated_package in collect_outdated_packages(venv_executable):
            subprocess.run(
                [
                    venv_executable,
                    "-m",
                    "pip",
                    "--disable-pip-version-check",
                    "install",
                    "--upgrade",
                    outdated_package,
                ],
                stdout=subprocess.DEVNULL,
                check=False,
            )

    click.echo()
    click.echo("All done!")
    click.echo()
    click.echo("Now run:")
    if SYSTEM == "Windows":
        click.echo(venv_dir / "Scripts" / "activate")
    else:
        click.echo(f"source {venv_dir / 'bin' / 'activate'}")
