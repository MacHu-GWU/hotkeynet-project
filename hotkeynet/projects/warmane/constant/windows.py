# -*- coding: utf-8 -*-

"""
枚举所有的窗口, 并在之后的代码中对其进行引用.

由于 Warmane 只允许最多 25 开, 所以逻辑上最多打开 25 个游戏客户端.
"""

import typing

import attr


@attr.s
class Window:
    title = attr.ib()
    label = attr.ib()


window_list = [
    Window(title="WoW{}".format(ind + 1), label="w{}".format( str(ind + 1).zfill(2)))
    for ind in range(25)
]  # type: typing.List[Window]

window_index = {
    ind + 1: window
    for ind, window in enumerate(window_list)
}  # type: typing.Dict[int, Window]
