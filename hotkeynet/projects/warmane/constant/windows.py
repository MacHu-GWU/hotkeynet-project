# -*- coding: utf-8 -*-

"""
枚举所有的窗口, 并在之后的代码中对其进行引用.
"""

import typing

import attr


@attr.s
class Window:
    title = attr.ib()
    label = attr.ib()


window_list = [
    Window(title="WoW{}".format(ind + 1), label="w{}".format(ind + 1))
    for ind in range(25)
]  # type: typing.List[Window]

window_index = {
    ind + 1: window
    for ind, window in enumerate(window_list)
}  # type: typing.Dict[int, Window]
