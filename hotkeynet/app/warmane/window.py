# -*- coding: utf-8 -*-

import typing as T
import enum

from hotkeynet.enumerate import EnumGetter
from hotkeynet.game.wow.model import Window


class WindowEnum(enum.Enum):
    """
    枚举出所有的窗口对象, 以供以后引用.
    """
    wow1 = Window(title="WoW1", label="w01")
    wow2 = Window(title="WoW2", label="w02")
    wow3 = Window(title="WoW3", label="w03")
    wow4 = Window(title="WoW4", label="w04")
    wow5 = Window(title="WoW5", label="w05")
    wow6 = Window(title="WoW6", label="w06")
    wow7 = Window(title="WoW7", label="w07")
    wow8 = Window(title="WoW8", label="w08")
    wow9 = Window(title="WoW9", label="w09")
    wow10 = Window(title="WoW10", label="w10")
    wow11 = Window(title="WoW11", label="w11")
    wow12 = Window(title="WoW12", label="w12")
    wow13 = Window(title="WoW13", label="w13")
    wow14 = Window(title="WoW14", label="w14")
    wow15 = Window(title="WoW15", label="w15")
    wow16 = Window(title="WoW16", label="w16")
    wow17 = Window(title="WoW17", label="w17")
    wow18 = Window(title="WoW18", label="w18")
    wow19 = Window(title="WoW19", label="w19")
    wow20 = Window(title="WoW20", label="w20")
    wow21 = Window(title="WoW21", label="w21")
    wow22 = Window(title="WoW22", label="w22")
    wow23 = Window(title="WoW23", label="w23")
    wow24 = Window(title="WoW24", label="w24")
    wow25 = Window(title="WoW25", label="w25")


class WindowGetter(EnumGetter[WindowEnum, Window]):
    enum_class = WindowEnum

    @classmethod
    def get_window(cls, index: int) -> Window:
        return _window_mapper[index]


_window_mapper: T.Dict[int, Window] = {
    ind + 1: window
    for ind, window in enumerate(WindowGetter.iter_values())
}
