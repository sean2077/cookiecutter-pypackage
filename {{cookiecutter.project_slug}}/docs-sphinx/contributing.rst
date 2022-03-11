.. _contributing:

贡献
====


代码格式化
----------

提交代码前请务必执行下述命令以规范代码:

.. code-block:: bash

    make format

参考 :ref:`安装依赖` 安装所需工具:

.. list-table::
    :header-rows: 1

    * - 工具
      - 用途
    * - `autoflake <https://github.com/PyCQA/autoflake>`_
      - 删除 import 中未使用的库和变量
    * - `isort <https://github.com/PyCQA/isort>`_
      - 对 import 进行排序
    * - `black <https://github.com/psf/black>`_
      - 规范代码风格


.. note::

    为防止提交代码前忘记执行 make format , 也为了避免每次提交代码都需要执行 make format 的麻烦，
    可以使用 `pre-commit <https://pre-commit.com/>`_  注册预提交钩子，在提交代码前自动执行格式化命令.

    .. code-block:: bash

        pre-commit install


代码类型检查
-------------

采用 `mypy <http://mypy-lang.org/>`_ 进行代码类型检查, 若使用的IDE为vscode，则可以在settings中搜索 mypy 开启 mypy,
其他集成方式请参考 `Mypy Integrations <https://github.com/python/mypy#integrations>`_.


Commits 规范
--------------

Commits 请遵循 `Conventional Commit <https://www.conventionalcommits.org/en>`_

Vscode IDE 可安装插件 ``Commit Message Editor``.


修改项目文件中的版本号
----------------------

使用 `bump2version <https://github.com/c4urself/bump2version>`_ 统一修改项目文件中的版本号:

.. code-block:: bash

    bump2version {part}

其中 {part} 为 ``major``, ``minor``, ``patch`` 之一.


版本发布规范
-------------

推荐使用工具 `standard-version <https://github.com/conventional-changelog/standard-version>`_ 进行版本发布:

.. code-block:: bash

    standard-version -r v{version}
