"""Console script for {{cookiecutter.package_name}}."""

{% if cookiecutter.command_line_interface|lower == 'click' -%}
import os
import sys

import click

from {{cookiecutter.package_name}} import __version__


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
{%- endif %}
