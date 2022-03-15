{% import "context.j2" as ctx with context -%}

"""Console script for {{cookiecutter.package_name}}."""

{% if ctx.use_click -%}
import os
import sys

import click

from . import __version__


def version_msg():
    """Return the {{cookiecutter.project_slug}} version, location and Python powering it."""
    python_version = sys.version[:3]
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    message = "{{cookiecutter.project_slug}} %(version)s from {} (Python {})"
    return message.format(location, python_version)


@click.command()
@click.version_option(__version__, "-V", "--version", message=version_msg())
def main():
    """Main entrypoint."""
    click.echo("{{ cookiecutter.package_name }}")
    click.echo("=" * len("{{ cookiecutter.package_name }}"))
    click.echo("{{ cookiecutter.project_short_description }}")


if __name__ == "__main__":
    main()  # pragma: no cover

{% elif ctx.use_typer -%}

import os
import sys
from typing import Optional

import typer

from . import __name__, __version__


def version_callback(value: bool) -> None:
    if value:
        python_version = sys.version[:3]
        location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        typer.echo(f"{__name__} {__version__} from {location} (python {python_version})")
        raise typer.Exit()


def cli(
    name: str = typer.Option("World"),
    version: Optional[bool] = typer.Option(None, "--version", callback=version_callback),
) -> None:
    typer.echo(f"Hello {name}")


def main() -> None:
    typer.run(cli)


if __name__ == "__main__":
    main()

{% endif -%}
