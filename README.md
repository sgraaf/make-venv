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

Running `make-venv --help` or `python -m make_venv --help` shows a list of all of the available options:

<!-- [[[cog
import cog
from make_venv import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["--help"], terminal_width=88)
help = result.output.replace("Usage: cli", "Usage: make-venv")
cog.outl(f"\n```sh\nmake-venv --help\n{help.rstrip()}\n```\n")
]]] -->

```sh
make-venv --help
Usage: make-venv [OPTIONS]

  A command-line utility for making a Python virtual environment.

Options:
  -d, --dest DIRECTORY          Directory to create the virtual environment at.
                                [default: .venv]
  -p, --python PYTHON           The Python interpreter to use for the virtual
                                environment.  [default:
                                C:\Users\sgraaf\Documents\Git\make-
                                venv\.nox\cog\Scripts\python.EXE]
  --seed / -S, --no-seed        Install seed packages (`pip`, `setuptools`, and `wheel`)
                                into the virtual environment.  [default: seed]
  --prompt PROMPT               Provide an alternative prompt prefix for the virtual
                                environment.  [default: <name-of-parent-directory-of-
                                virtual-environment>]
  -r, --requirement FILE        Install packages from the given requirements file.
  -u, -U, --upgrade             Upgrade all outdated packages to the newest available
                                version.
  -k, --install-ipython-kernel  Install the iPython kernel into the virtual environment.
  -n, --kernel-name NAME        The display name of the iPython kernel, if applicable.
                                [default: Python <version> (<name-of-parent-directory-
                                of-virtual-environment>)]
  -v, --version                 Show the version and exit.
  -h, --help                    Show this message and exit.
```

<!-- [[[end]]] -->

<!-- end docs-include-usage -->
