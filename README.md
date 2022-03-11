# Cookiecutter PyPackage

集成多个现代工具的 Python 项目的 [cookiecutter](https://github.com/cookiecutter/cookiecutter) 模板.

## 使用

安装 [cookiecutter](https://github.com/cookiecutter/cookiecutter) (1.7+):

```bash
pip install -U cookiecutter
```

构建 Python 项目:

```bash
cookiecutter https://github.com/waynerv/cookiecutter-pypackage.git --directory zh
```

## 亮点

本模板集成的工具及功能说明如下（部分类别工具只可选其一）:

### 项目工具

* [Poetry](https://python-poetry.org/): 管理依赖、构建和发布.
* [bump2version](https://github.com/c4urself/bump2version): 一行命令修改项目中所有指定位置的版本号.
* [Pre-commit](https://pre-commit.com/): 提交代码前自动执行代码检查、代码格式化等操作.
* [pipx](https://github.com/pypa/pipx): 在隔离环境中安装和运行 Python 应用程序.

### 测试工具

用途：构建单元测试、覆盖率测试等

* [Pytest](https://pytest.org): 构建 Python 项目的单元测试.
* [Pytest-cov](https://github.com/pytest-dev/pytest-cov): Pytest 的覆盖率测试插件

### 代码规范工具

* [Isort](https://github.com/PyCQA/isort): import 排序工具
* [Black](https://github.com/psf/black): 规范代码风格工具
* [Mypy](http://mypy-lang.org/): 静态类型检查工具

### 第三方CLI框架（可选）

用途：构建 Python 命令行应用程序。

下述工具选其一:

| 工具                                                 | 优点                                                         | 缺点 | 适用的场景 |
| ---------------------------------------------------- | ------------------------------------------------------------ | ---- | ---------- |
| [Click](https://click.palletsprojects.com/en/8.0.x/) | 基于 Python 装饰器构建CLI，比较简洁直观；丰富的插件；有生成Sphinx文档的插件 |      |            |
| [Typer](https://typer.tiangolo.com/)                 | 基于 Python 类型提示构建CLI, 非常简洁直观；基于 Click，继承了 Click 的诸多优点和插件；支持赋予自动补全的能力 |      | 更推荐     |

### 文档工具（可选）

下述文档工具选其一：

| 工具                                  | 优点                                                 | 缺点                                                         | 适用的场景 |
| ------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------ | ---------- |
| [Sphinx](https://www.sphinx-doc.org/) | 支持各种复杂的引用；丰富的插件；支持打印命令输出结果 | 基于reStructuredText, 需要较高的学习成本（但有）；本地编辑调试比较麻烦 |            |
| [Mkdocs](https://www.mkdocs.org)      | 基于markdown文档；丰富美观的主题；本地调试比较方便   | 对 Python 项目的自动文档生成支持得                           |            |

### 集成（CI/CD）工具

用途：自动化构建、测试和部署过程。

| 工具                                                 | 优点                   | 缺点 | 适用的场景        |
| ---------------------------------------------------- | ---------------------- | ---- | ----------------- |
| [Github Actions](https://docs.github.com/cn/actions) | Github平台原生集成工具 |      | 项目托管于 Github |
| [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/)       | Gitlab平台原生集成工具 |      | 项目托管于 Gitlab |

其他集成工具如[Travis CI](https://www.travis-ci.com/)、[Tox](https://tox.readthedocs.io)等都不具有特别明显的优势，不建议使用。
