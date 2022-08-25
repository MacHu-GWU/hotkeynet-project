# -*- coding: utf-8 -*-

import typing as T
import enum

from hotkeynet.enumerate import EnumHelper
from hotkeynet.game.wow.model import Window


class WindowEnum(enum.Enum):
    """
    枚举出所有的窗口对象, 以供以后引用.
    """
    wow01 = Window(title="WoW01", label="w01")
    wow02 = Window(title="WoW02", label="w02")
    wow03 = Window(title="WoW03", label="w03")
    wow04 = Window(title="WoW04", label="w04")
    wow05 = Window(title="WoW05", label="w05")
    wow06 = Window(title="WoW06", label="w06")
    wow07 = Window(title="WoW07", label="w07")
    wow08 = Window(title="WoW08", label="w08")
    wow09 = Window(title="WoW09", label="w09")
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

    @property
    def val(self) -> 'Window':
        return self.value

    @classmethod
    def get_window(cls, index: int) -> Window:
        return getattr(cls, f"wow{str(index).zfill(2)}").val


class WindowHelper(EnumHelper[WindowEnum, Window]):
    enum_class = WindowEnum
