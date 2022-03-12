开发
====

请在开发前确保安装了以下工具:

- `poetry <https://python-poetry.org/>`_: 管理依赖和工具配置
- `pipx <https://github.com/pypa/pipx>`_: 管理工具的安装


切换 Python 环境
----------------

本项目为 Poetry 项目，拥有隔离的 Python 环境，可通过如下命令查看相关信息:

.. code-block:: bash

    poetry env info

在不同的 IDE 中注意切换到相应的 Python 环境:

Vscode:
    F1 -> 搜索: "Python: Select Interpreter" -> 选择上述路径下的 Python 解释器.

Pycharm/IDEA:
    参考: https://www.jetbrains.com/help/idea/configuring-local-python-interpreters.html


在终端中进入该项目路径后执行如下命令也可进入相应的虚拟环境中:

.. code-block:: bash

    poetry shell


.. _安装依赖:

安装依赖
--------

安装项目依赖库及测试、文档、开发所需工具:

.. code-block:: bash

    poetry install -E test -E doc -E dev


更新依赖
--------

.. code-block:: bash

    poetry update


安装应用
--------

推荐以 editable 模式安装本应用:

.. code-block:: bash

    pipx install -e .


维护文档
--------

本项目基于 `Sphinx <https://www.sphinx-doc.org/en/master/>`_ 构建文档，
推荐使用 IDE `Vscode <https://www.sphinx-doc.org/en/master/>`_ 编辑文档。

推荐 Vscode 插件:

- `restructuredtext <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_
- `reStructuredText Syntax highlighting <https://marketplace.visualstudio.com/items?itemName=trond-snekvik.simple-rst>`_
- `LiveServer <https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer>`_

提交代码
--------

进行项目开发前请先参阅 :ref:`contributing`.
