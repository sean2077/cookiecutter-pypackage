{% import "context.j2" as ctx with context -%}

.. _installation:

安装
====

.. note::

    本项目为 Python 应用（区别于 Python 库），为避免依赖冲突问题，
    也可以使用 `pipx <https://github.com/pypa/pipx>`_ 替换下述命令中的 ``pip``,
    以在隔离环境中安装本应用。

{% if ctx.is_open_source -%}

从 PyPi 安装
------------

.. code-block:: bash

    pip install {{ ctx.project_slug }}

{% endif -%}

从源代码安装
------------

.. code-block:: bash

    pip install git+{{ ctx.project_url }}.git

或

.. code-block:: bash

    git clone {{ ctx.project_url }}.git
    cd {{ ctx.project_slug }}
    pip install .

