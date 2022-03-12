{% import "context.j2" as ctx with context -%}

# {{ cookiecutter.project_name }}

{% if ctx.is_github -%}
[![tests](<{{ ctx.project_url }}/actions/workflows/Tests/badge.svg?branch={{ ctx.project_default_branch }}&event=push>)](<{{ ctx.project_url }}/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![codecov](<https://codecov.io/gh/{{ ctx.project_path }}/branch/{{ ctx.project_default_branch }}/graphs/badge.svg>)](<https://codecov.io/github/{{ ctx.project_path }}>)
{% elif ctx.is_gitlab -%}
[![pipeline](<{{ ctx.project_url }}/badges/{{ ctx.project_default_branch }}/pipeline.svg>)](<{{ ctx.project_url }}>)
[![coverage](<{{ ctx.project_url }}/badges/{{ ctx.project_default_branch }}/coverage.svg>)](<{{ ctx.project_url }}>)
{% endif -%}
[![version](<https://img.shields.io/static/v1?label=version&message={{ ctx.project_version }}&color=green>)](<{{ ctx.project_url }}>)
{% if ctx.is_open_source -%}
[![pypi](<https://img.shields.io/pypi/v/{{ ctx.project_slug }}.svg>)](<https://pypi.org/project/{{ ctx.project_slug }}/>)
[![python](<https://img.shields.io/pypi/pyversions/{{ ctx.project_slug }}.svg>)](<https://pypi.org/project/{{ ctx.project_slug }}/>)
{% else -%}
[![python](<https://img.shields.io/badge/python-3.8%2B-blue>)](<{{ ctx.project_url }}>)
{% endif -%}
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](<https://img.shields.io/badge/mypy-checked-blue>)](http://mypy-lang.org/)

{{ cookiecutter.project_short_description }}

* Documentation: <{{ ctx.document_url }}>
* {{ ctx.platform }}: <{{ ctx.project_url }}>
{% if ctx.is_open_source -%}
* PyPI: <https://pypi.org/project/{{ ctx.project_slug }}/>
* Free software: {{ ctx.open_source_license }}
{% endif %}
## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zhangxianbing/cookiecutter-pypackage](https://github.com/zhangxianbing/cookiecutter-pypackage) project template.
