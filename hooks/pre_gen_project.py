import os
import re
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

CONTEXT = {
    "package_name": "{{ cookiecutter.package_name}}",
}


if __name__ == "__main__":

    print("------ pre_gen_project.py ------")

    if not re.match(MODULE_REGEX, CONTEXT["package_name"]):
        print(
            f"ERROR: The pkg name ({CONTEXT['package_name']}) is not a valid Python module name. Please do not use a - and use _ instead."
        )
        sys.exit(1)
