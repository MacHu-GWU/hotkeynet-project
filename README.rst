
.. image:: https://readthedocs.org/projects/hotkeynet/badge/?version=latest
    :target: https://hotkeynet.readthedocs.io/index.html
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/hotkeynet-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/hotkeynet-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/hotkeynet-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/hotkeynet-project

.. image:: https://img.shields.io/pypi/v/hotkeynet.svg
    :target: https://pypi.python.org/pypi/hotkeynet

.. image:: https://img.shields.io/pypi/l/hotkeynet.svg
    :target: https://pypi.python.org/pypi/hotkeynet

.. image:: https://img.shields.io/pypi/pyversions/hotkeynet.svg
    :target: https://pypi.python.org/pypi/hotkeynet

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/hotkeynet-project

------

.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://hotkeynet.readthedocs.io/index.html

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://hotkeynet.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
    :target: https://hotkeynet.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/hotkeynet-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/hotkeynet-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/hotkeynet-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/hotkeynet#files


Welcome to ``hotkeynet`` Documentation
==============================================================================


Overview
------------------------------------------------------------------------------
HotkeyNet 是一个诞生于 2000 年左右, 并在 2009 年停止维护的键盘鼠标自动化软件, 只支持 Windows, 得益于 Windows 强大的兼容性, 它所依赖的底层 Windows API 都没有改动, 所以一直能稳定运行. 万一它真的不能用了, 我会考虑直接用 Windows API 自己实现一个基于 Python 的键盘鼠标自动化软件. 本项目是对 HotkeyNet 脚本用 Python 的二次封装. 使得你可以用更现代的 Python 编程语言来写 HotKeyNet 脚本, 大大提高了项目的可维护性和开发效率.

HotkeyNet 脚本是一个类 XML 语法的 DSL (特定领域编程语言). 基于纯文本, 没有编辑器. 这使得代码复用和动态更改变得极其困难. 虽然它有 ``Template`` 语法允许你对文本进行替换, 但由于对 面向对象, If, Else 逻辑的缺失, 使得编程过程极为痛苦, 修改起来也非常麻烦. 不可能做到模块化. 早期我凭借着编程功底, 用 ``Template`` 做出来了一个相对可维护的脚本, 但是整个脚本还是极为臃肿. 由于 HotkeyNet 的设计原因, 它解析长脚本的速度极慢, 这使得原生脚本根本不可能适用于复杂多变的项目需求.

这个项目的是用面向对象的语法, 对所有的 Block (代码块) 进行面向对象封装, 然后利用 Python 的类型推断, 自动补全功能, 大大提升了编程效率和编程体验. 避免了记忆原生语法中的那些命令, 而让 IDE 进行自动补全. 而且还能利用各种数据结构批量生成各种代码, 删除无用注释, 大大增加了代码可读性, 复用性和灵活性.

在本项目的加持下, 编写 HotkeyNet 的流程就变成了:

- 在 Python 中写 HotkeyNet 脚本
- 运行 Python 生成最终脚本
- 打开 HotkeyNet 软件并使用该脚本

由于 HotkeyNet 官方网站已经不在了, 本项目在 https://hotkeynet.readthedocs.io/index.html 维护了一个文档的镜像, 以供查阅.

.. _install:

Install
------------------------------------------------------------------------------

``hotkeynet`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install hotkeynet

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade hotkeynet