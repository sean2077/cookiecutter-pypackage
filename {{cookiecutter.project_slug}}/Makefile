VERSION := $(shell grep -oPm1 '(?<=version = ")[^"]+' pyproject.toml)
GIT_SHORT_HASH=$(shell git rev-parse --short HEAD)
BUILD_DATE=$(shell date '+%Y年%m月%d日 %H:%M:%S')
SRC=src/{{ cookiecutter.package_name }}

.PHONY: build image

default: info

info:
	@echo "version: ${VERSION}"
	@echo "build date: ${BUILD_DATE}"
	@echo "git hash: ${GIT_SHORT_HASH}"

format:
	find $(SRC) -name '*.py' -type f -exec autoflake -i --remove-all-unused-imports --ignore-init-module-imports {} +
	find $(SRC) -name '*.py' -type f -exec isort {} +
	find $(SRC) -name '*.py' -type f -exec black {} +

lint:
	mypy $(SRC) tests

pre-commit:
	pre-commit run -a -v

test:
	PYTHONPATH=src:$(PYTHONPATH) pytest --cov=$(SRC) --durations=0 -vv -s tests

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python3 -c "$$BROWSER_PYSCRIPT"

coverage:
	PYTHONPATH=src:$(PYTHONPATH) pytest --cov=. --cov-report=term --cov-report=html
	$(BROWSER) coverage/index.html


clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr docs/_build/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

update:
	poetry update -vv

install:
	pipx install .

{% if cookiecutter.document_tool == 'Mkdocs' -%}
doc:
	PYTHONPATH=src:$(PYTHONPATH) mkdocs serve
{% endif -%}

release-patch:
	bump2version patch --allow-dirty

release-minor:
	bump2version minor --allow-dirty

release-major:
	bump2version major --allow-dirty
