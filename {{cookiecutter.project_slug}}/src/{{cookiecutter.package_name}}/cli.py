{% import "context.j2" as ctx with context -%}

"""Console script for {{ctx.package_name}}."""

{% if ctx.use_click -%}
import os
import sys

import click

from . import __version__


def version_msg():
    """Return the {{ctx.project_slug}} version, location and Python powering it."""
    python_version = sys.version[:3]
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    message = "{{ctx.project_slug}} %(version)s from {} (Python {})"
    return message.format(location, python_version)


@click.command()
@click.version_option(__version__, "-V", "--version", message=version_msg())
def main():
    """Main entrypoint."""
    click.echo("{{ ctx.package_name }}")
    click.echo("=" * len("{{ ctx.package_name }}"))
    click.echo("{{ ctx.project_short_description }}")


if __name__ == "__main__":
    main()

{% elif ctx.use_typer -%}

import os
import sys
from typing import Optional

import typer

from . import __version__

app = typer.Typer()


def version_callback(value: bool) -> None:
    if value:
        prog_name = "{{ctx.project_slug}}"
        location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        python_version = sys.version[:3]
        typer.echo(f"{prog_name} {__version__} from {location} (python {python_version})")
        raise typer.Exit()


@app.callback(no_args_is_help=True)
def {{ ctx.package_name }}(
    version: Optional[bool] = typer.Option(
        None, "--version", help="Show version information and exit.", callback=version_callback, is_eager=True
    ),
) -> None:
    pass


@app.command()
def hello(name: str = "World") -> None:
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False) -> None:
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
{% endif -%}
