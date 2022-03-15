#!/usr/bin/env python
import os
import shutil
import subprocess
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

CONTEXT = {
    "platform": "{{ cookiecutter.platform }}",
    "open_source_license": "{{ cookiecutter.open_source_license }}",
    "command_line_interface": "{{ cookiecutter.command_line_interface }}",
    "document_tool": "{{ cookiecutter.document_tool }}",
    "_cleanup": True,
}

ACTIONS_MAP = {
    "platform": {
        "GitHub": {
            "keep": [".github"],
        },
        "GitLab": {
            "keep": [".gitlab-ci.yml"],
        },
    },
    "open_source_license": {
        "Not open source": {
            "remove": ["LICENSE"],
        },
    },
    "command_line_interface": {
        "No command-line interface": {
            "remove": [
                os.path.join("{{ cookiecutter.package_name }}", "cli.py"),
            ],
        }
    },
    "document_tool": {
        "Sphinx": {
            "rename": [("docs-sphinx", "docs")],
        },
        "Mkdocs": {
            "rename": [("docs-mkdocs", "docs")],
            "keep": ["mkdocs.yml"],
        },
        "No docs": {
            "remove": ["docs-sphinx", "docs-mkdocs"],
        },
    },
    "_cleanup": {
        True: {
            "remove": ["context.j2"],
        }
    },
}


def remove(path):
    abspath = os.path.join(PROJECT_DIRECTORY, path)
    print(f"remove {abspath}")
    try:
        if os.path.exists(abspath):
            if os.path.isdir(abspath):
                shutil.rmtree(abspath)
            elif os.path.isfile(abspath):
                os.remove(abspath)
    except FileNotFoundError:
        pass


def rename(src, dst):
    abs_src = os.path.join(PROJECT_DIRECTORY, src)
    abs_dst = os.path.join(PROJECT_DIRECTORY, dst)
    print(f"rename {abs_src} -> {abs_dst}")
    try:
        os.rename(abs_src, abs_dst)
    except FileNotFoundError as e:
        print(e)
        pass


def take_actions(key, actions):
    choice = CONTEXT[key]
    print(f"take actions for {key}={choice}")
    for key, actions in actions.items():
        removes = actions.get("remove", ())
        if key == choice:
            for path in removes:
                remove(path)
            for src, dst in actions.get("rename", ()):
                rename(src, dst)
            continue
        keeps = actions.get("keep", [])
        renames = [old for old, new in actions.get("rename", ())]
        for path in keeps + renames:
            if path not in removes:
                remove(path)


def execute(*args, suppress_exception=False, cwd=None):
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out, err = proc.communicate()
        out = out.decode("utf-8")
        err = err.decode("utf-8")
        if err and not suppress_exception:
            raise Exception(err)
        else:
            return out
    finally:
        os.chdir(cur_dir)


def init_git():
    # workaround for issue #1
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute(
            "git",
            "config",
            "--global",
            "init.defaultBranch",
            "{{ cookiecutter.project_default_branch }}",
            cwd=PROJECT_DIRECTORY,
        )
        execute("git", "init", cwd=PROJECT_DIRECTORY)


def install_pre_commit_hooks():
    execute(sys.executable, "-m", "pip", "install", "pre-commit>=2.17.0")
    execute(sys.executable, "-m", "pre_commit", "install")


if __name__ == "__main__":

    print("------ post_gen_project.py ------")

    for key, actions in ACTIONS_MAP.items():
        if key not in CONTEXT:
            print(f"not supported {key=}")
            continue
        take_actions(key, actions)

    try:
        init_git()
    except Exception as e:
        print(e)

    if "{{ cookiecutter.install_precommit_hooks }}" == "y":
        try:
            install_pre_commit_hooks()
        except Exception as e:
            print(str(e))
            print(
                "Failed to install pre-commit hooks. Please run `pre-commit install` by your self. For more on pre-commit, please refer to https://pre-commit.com"
            )
