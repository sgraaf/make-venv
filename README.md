<!-- start docs-include-index -->

# make-venv

[![PyPI](https://img.shields.io/pypi/v/make-venv)](https://img.shields.io/pypi/v/make-venv)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/make-venv)](https://pypi.org/project/make-venv/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sgraaf/make-venv/main.svg)](https://results.pre-commit.ci/latest/github/sgraaf/make-venv/main)
[![Test](https://github.com/sgraaf/make-venv/actions/workflows/test.yml/badge.svg)](https://github.com/sgraaf/make-venv/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/make-venv/badge/?version=latest)](https://make-venv.readthedocs.io/en/latest/?badge=latest)
[![PyPI - License](https://img.shields.io/pypi/l/make-venv)](https://img.shields.io/pypi/l/make-venv)

A command-line utility for making a Python virtual environment.

<!-- end docs-include-index -->

## Installation

<!-- start docs-include-installation -->

make-venv is available on [PyPI](https://pypi.org/project/make-venv/). Install with [pipx](https://pypa.github.io/pipx/) or your package manager of choice:

```sh
pipx install make-venv
```

<!-- end docs-include-installation -->

## Documentation

Check out the [make-venv documentation](https://make-venv.readthedocs.io/en/stable/) for the [User's Guide](https://make-venv.readthedocs.io/en/stable/usage.html) and [CLI Reference](https://make-venv.readthedocs.io/en/stable/cli.html).

## Usage

<!-- start docs-include-usage -->

Running `make-venv --help` or `python -m make_venv --help` shows a list of all of the available options and commands:

<!-- [[[cog
import cog
from make_venv import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["--help"], terminal_width=88)
help = result.output.replace("Usage: cli", "Usage: make-venv")
cog.outl(f"\n```sh\ncookiecutter-python-cli-app-demo-with-rich --help\n{help.rstrip()}\n```\n")
]]] -->

```sh
cookiecutter-python-cli-app-demo-with-rich --help
Usage: make-venv [OPTIONS] COMMAND [ARGS]...

  A command-line utility for making a Python virtual environment.

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  repeat  Repeat the input.
```

<!-- [[[end]]] -->

<!-- end docs-include-usage -->
