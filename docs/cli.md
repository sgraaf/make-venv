# CLI Reference

This page lists the `--help` for `make-venv` and all its commands.

## make-venv

Running `make-venv --help` or `python -m make_venv --help` shows a list of all of the available options and commands:

<!-- [[[cog
import cog
from make_venv import cli
from click.testing import CliRunner
result = CliRunner().invoke(cli.cli, ["--help"], terminal_width=88)
help = result.output.replace("Usage: cli", "Usage: make-venv")
cog.outl(f"\n```sh\nmake-venv --help\n{help.rstrip()}\n```\n")
for command in cli.cli.commands.keys():
    result = CliRunner().invoke(cli.cli, [command, "--help"], terminal_width=88)
    help = result.output.replace("Usage: cli ", "Usage: make-venv ")
    cog.outl(f"## make-venv {command}\n\n```sh\nmake-venv {command} --help\n{help.rstrip()}\n```\n")
]]] -->

```sh
make-venv --help
Usage: make-venv [OPTIONS] COMMAND [ARGS]...

  A command-line utility for making a Python virtual environment.

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  repeat  Repeat the input.
```

## make-venv repeat

```sh
make-venv repeat --help
Usage: make-venv repeat [OPTIONS] INPUT

  Repeat the input.

Options:
  -r, --reverse  Reverse the input.
  -h, --help     Show this message and exit.
```

<!-- [[[end]]] -->
