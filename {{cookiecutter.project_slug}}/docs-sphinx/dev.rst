开发
====

本项目采用 `poetry <https://python-poetry.org/>`_ 管理依赖和配置，
请在开发前确保安装了最新的 poetry 工具.


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


临时安装应用
------------

poetry install 默认以 editable 模式安装本应用.

.. code-block:: bash

    poetry install

.. note::
    通过此方式安装的应用只能在对应的 poetry 虚拟环境（poetry shell）中运行，
    要全局安装此应用，请参考 :ref:`installation`


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
