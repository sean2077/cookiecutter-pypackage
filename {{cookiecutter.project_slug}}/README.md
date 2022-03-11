{% set project_slug = cookiecutter.project_slug -%}
{% set project_version = cookiecutter.project_version -%}
{% set project_default_branch = cookiecutter.project_default_branch -%}
{% set platform = cookiecutter.platform -%}
{% set platform_username = cookiecutter.platform_username -%}
{% set platform_url = cookiecutter.platform_url -%}
{% set open_source_license = cookiecutter.open_source_license -%}

{% set is_github = platform == 'GitHub' -%}
{% set is_gitlab = platform == 'GitLab' -%}
{% set project_path = platform_username ~ '/' ~ project_slug -%}
{% set project_url = platform_url ~ '/' ~ project_path -%}
{% set is_open_source = open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

{% if is_github -%}
[![tests](<{{ project_url }}/actions/workflows/Tests/badge.svg?branch={{ project_default_branch }}&event=push>)](<{{ project_url }}/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![codecov](<https://codecov.io/gh/{{ project_path }}/branch/{{ project_default_branch }}/graphs/badge.svg>)](<https://codecov.io/github/{{ project_path }}>)
{% elif is_gitlab -%}
[![pipeline](<{{ project_url }}/badges/{{ project_default_branch }}/pipeline.svg>)](<{{ project_url }}>)
[![coverage](<{{ project_url }}/badges/{{ project_default_branch }}/coverage.svg>)](<{{ project_url }}>)
{% endif -%}
[![version](<https://img.shields.io/static/v1?label=version&message={{ project_version }}&color=green>)](<{{ project_url }}>)
{% if is_open_source -%}
[![pypi](<https://img.shields.io/pypi/v/{{ project_slug }}.svg>)](<https://pypi.org/project/{{ project_slug }}/>)
[![python](<https://img.shields.io/pypi/pyversions/{{ project_slug }}.svg>)](<https://pypi.org/project/{{ project_slug }}/>)
{% else -%}
[![python](<https://img.shields.io/badge/python-3.8%2B-blue>)](<{{ project_url }}>)
{% endif -%}
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](<https://img.shields.io/badge/mypy-checked-blue>)](http://mypy-lang.org/)

{{ cookiecutter.project_short_description }}

{% if is_github -%}
* Documentation: <https://{{ platform_username }}.github.io/{{ project_slug }}>
{% elif is_gitlab -%}
{% set lst = platform_username.split('/') -%}
* Documentation: <https://{{ lst[0] }}.pages.{{ platform_url[8:] }}/{{ lst[1:]|join('/') }}/{{ project_slug }}>
{% endif -%}
* {{ platform }}: <{{ project_url }}>
{% if is_open_source -%}
* PyPI: <https://pypi.org/project/{{ project_slug }}/>
* Free software: {{ open_source_license }}
{% endif %}
## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zhangxianbing/cookiecutter-pypackage](https://github.com/zhangxianbing/cookiecutter-pypackage) project template.
