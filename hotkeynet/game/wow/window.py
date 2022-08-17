# -*- coding: utf-8 -*-

"""
枚举所有的窗口, 并在之后的代码中对其进行引用.

由于 Warmane 只允许最多 25 开, 所以逻辑上最多打开 25 个游戏客户端.
"""

import attr
from attrs_mate import AttrsClass


@attr.s
class Window(AttrsClass):
    title: str = attr.ib()
    label: str = attr.ib()
