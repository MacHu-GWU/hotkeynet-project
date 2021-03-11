# -*- coding: utf-8 -*-

import attr
import typing
from .base import BaseConfig

@attr.s
class ToggleWindowConfig(BaseConfig):
    """
    Number of windows.

    定义了 **默认切换窗口快捷键** 与 WoW1, 2, .... 25 这些窗口的对应关系.

    :param key1_to_25_window_index: 定义了 **默认切换窗口快捷键 1 - 25** (通常是
        Ctrl F1 - F12, Ctrl Insert - PgDn, Win F1 ~ F7 一共 25 个键.
        例如: [1, 2, 3, 6, 7, 8] 表示 Ctrl F1 ~ F3 切换到 WoW1 ~ WoW3,
        而 Ctrl F4 ~ F6 则切换到 WoW6 ~ WoW8
    :param round_robin_window_index: 定义了 首位循环切换窗口快捷键所循环的窗口序列.
        例如: [5, 6, 7, 8] 则表示只在 WoW5, WoW6, WoW7, WoW8 之间循环
    """
    key1_to_25_window_index = attr.ib(default=None) # type: typing.List[int]
    round_robin_window_index = attr.ib(default=None) # type: typing.List[int]

    def validate(self):
        pass