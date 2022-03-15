{% import "context.j2" as ctx with context -%}

#!/usr/bin/env python
"""Tests for `{{ ctx.package_name }}` package."""

import pytest
{% if ctx.use_click -%}
from click.testing import CliRunner
{% elif ctx.use_typer -%}
from typer.testing import CliRunner
{%- endif %}

{% if ctx.is_cli -%}
from {{ ctx.package_name }} import cli
{%- endif %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get("https://github.com/audreyr/cookiecutter-pypackage")


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert "GitHub" in BeautifulSoup(response.content).title.string
    del response
{%- if ctx.is_cli %}

{% if ctx.use_click -%}
app = cli.main
{% elif ctx.use_typer -%}
app = cli.app
{%- endif %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "{{ ctx.package_name }}" in result.output
    help_result = runner.invoke(app, ["--help"])
    assert help_result.exit_code == 0
    assert "--help                          Show this message and exit." in help_result.output
{%- endif %}
