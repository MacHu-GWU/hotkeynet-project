# -*- coding: utf-8 -*-

"""
:mod:`~hotkeynet.keyname` 模块以字符串的形式枚举了所有的按键和鼠标, 最终在写脚本的时候
要用 :mod:`~hotkeynet.script` 模块中的类和 ``keyname`` 模块一起构成按键定义. 例如:

.. code-block:: python

    Key(key=KN.KEY_1)

可是这些按键定义是可变的, 有可能被修改. 如果一个按键定义类在多个地方被引用了, 那么一旦被修改将引发
不可知的错误. 所以我们希望在每次引用已经封装好的按键定义时都自动创建一个新的对象, 以避免这种问题.
这就要用到工厂函数. 本模块提供了很多工厂类, 它们都是可调用的, 每次调用都会创建一个新的对象.
"""

import typing as T
from .script import (
    Key,
    KeyDown,
    KeyUp,
    MouseStrokeEnum,
    ClickMouse,
)


class KeyMaker:
    """
    Example::

        >>> from hotkeynet import keyname as KN
        >>> from hotkeynet.maker import KeyMaker
        >>> key_1 = KeyMaker(KN.KEY_1)
        >>> key_1()
        Key(id='Block0001', blocks=[], key='1')
    """

    def __init__(self, key: str):
        self.key = key

    def __call__(self) -> Key:
        return Key(key=self.key)


class ClickMaker:
    """ """

    def __init__(self, button: str):
        self.button = button

    def __call__(self) -> ClickMouse:
        return ClickMouse(button=self.button)


class ModifiedClickMaker:
    def __init__(self, button: str, *keys: str):
        self.button = button
        self.keys = keys

    def __call__(self) -> T.List[T.Union[KeyDown, KeyUp, ClickMouse]]:
        actions = list()
        for key in self.keys:
            actions.append(KeyDown(key=key))
        actions.append(
            ClickMouse(button=self.button, stroke=MouseStrokeEnum.Down.value)
        )
        actions.append(ClickMouse(button=self.button, stroke=MouseStrokeEnum.Up.value))
        for key in self.keys:
            actions.append(KeyUp(key=key))
        return actions


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


class ErrorMaker(BaseKeyMaker):
    def __init__(
        self,
        klass,
        attribute,
        value: T.Any,
    ):
        self.klass = klass
        self.attribute = attribute
        self.value = value

    def __call__(self):
        raise ValueError(
            f"the definition of {self.klass}.{self.attribute} is wrong! "
            f"the value is {self.value!r}"
        )


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
                    attrs[k] = ErrorMaker(
                        klass=name,
                        attribute=k,
                        value=v,
                    )

        klass = super(ActFactoryMeta, cls).__new__(cls, name, bases, attrs)
        return klass


class ActFactory(metaclass=ActFactoryMeta):
    """
    Act 枚举类的基类. 能自动将属性转化成工厂函数.
    """

    pass
