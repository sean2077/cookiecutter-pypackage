from {{cookiecutter.project_slug}} import __author__, __name__, __version__, __project_hyphen__
from setuptools import find_packages, setup

def read_requirements():
    reqs = []
    with open("requirements.txt", "r") as f:
        for line in f:
            reqs.append(line.strip())
    return reqs


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{{ cookiecutter.project_url }}",
    packages=find_packages(include=[f"{__name__}*"]),
    install_requires=read_requirements(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            f"{__project_hyphen__} = {__name__}.{__name__}:main",
        ],
    },
)
