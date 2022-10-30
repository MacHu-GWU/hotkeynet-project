# -*- coding: utf-8 -*-

"""
该模块是用来简化定义你的按键绑定的脚本的. 这里的问题源头是所有对你的按键定义都应该是引用.
例如你定义按下 1 的时候 Hotkeynet 帮你按 圣光术, 按下 2 的时候 Hotkeynet 帮你按 圣光闪现.
这里你引用 圣光术 的时候不应该引用同一个对象, 而是调用一个方法创建一个新的对象. 这样才能避免
多次引用导致的一次修改, 意外改变了其他地方的引用的行为.
"""

import typing as T
from .script import Key, ClickMouse, ModifiedClickMouse


class ClickName:
    """
    Templaterize the ClickMouse object.
    """

    def left(self) -> ClickMouse:
        return ClickMouse().set_left_click()

    def right(self) -> ClickMouse:
        return ClickMouse().set_right_click()

    def middle(self) -> ClickMouse:
        return ClickMouse().set_middle_click()

    def shift_left_click(self):
        return ModifiedClickMouse.shift_left_click()

    def shift_right_click(self):
        return ModifiedClickMouse.shift_right_click()

    def shift_middle_click(self):
        return ModifiedClickMouse.shift_middle_click()

    def alt_left_click(self):
        return ModifiedClickMouse.alt_left_click()

    def alt_right_click(self):
        return ModifiedClickMouse.alt_right_click()

    def alt_middle_click(self):
        return ModifiedClickMouse.alt_middle_click()

    def ctrl_left_click(self):
        return ModifiedClickMouse.ctrl_left_click()

    def ctrl_right_click(self):
        return ModifiedClickMouse.ctrl_right_click()

    def ctrl_middle_click(self):
        return ModifiedClickMouse.ctrl_middle_click()


click_name = ClickName()


class BaseKeyMaker:
    def __call__(self) -> T.Union[Key, ClickMouse]:
        raise NotImplementedError


class KeyMaker(BaseKeyMaker):
    def __init__(self, key: str):
        self.key = key

    def __call__(self) -> Key:
        return Key(key=self.key)


class ClickMaker(BaseKeyMaker):
    def __init__(self, click: T.Callable):
        self.click = click

    def __call__(self) -> ClickMouse:
        return self.click()


class ActFactoryMeta(type):
    """
    meta class of ActFactory
    """

    def __new__(cls, name, bases, attrs):
        for k, v in list(attrs.items()):
            if not k.startswith("_"):
                if isinstance(v, str):
                    attrs[k] = KeyMaker(v)
                elif callable(v):
                    attrs[k] = ClickMaker(v)
                else:
                    raise TypeError

        klass = super(ActFactoryMeta, cls).__new__(cls, name, bases, attrs)
        return klass


class ActFactory(metaclass=ActFactoryMeta):
    pass
