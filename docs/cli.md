# CLI Reference

This page lists the `--help` for `make-venv`.

## make-venv

Running `make-venv --help` or `python -m make_venv --help` shows a list of all of the available options:

<!-- [[[cog
import cog
from make_venv import cli
from click.testing import CliRunner
result = CliRunner().invoke(cli.cli, ["--help"], terminal_width=88)
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
  -h, --help                    Show this message and exit.
```

<!-- [[[end]]] -->
