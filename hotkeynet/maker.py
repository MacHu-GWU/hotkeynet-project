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
    """
    Example::

        >>> from hotkeynet import keyname as KN
        >>> from hotkeynet.maker import ClickMaker
        >>> left_click = ClickMaker(KN.MOUSE_LButton)
        >>> left_click()
        ClickMouse(id='Block0001', blocks=[], button='LButton', stroke='', target='', mode='', restore='')
    """

    def __init__(self, button: str):
        self.button = button

    def __call__(self) -> ClickMouse:
        return ClickMouse(button=self.button)


class ModifiedClickMaker:
    """
    Example::

        >>> from hotkeynet import keyname as KN
        >>> from hotkeynet.maker import ModifiedClickMaker
        >>> ctrl_left_click = ModifiedClickMaker(KN.MOUSE_LButton, KN.CTRL)
        >>> ctrl_left_click()
        [
            KeyDown(id='Block0001', blocks=[], key='Ctrl'),
            ClickMouse(id='Block0002', blocks=[], button='LButton', stroke='Down', target='', mode='', restore=''),
            ClickMouse(id='Block0003', blocks=[], button='LButton', stroke='Up', target='', mode='', restore=''),
            KeyUp(id='Block0004', blocks=[], key='Ctrl')
        ]
    """
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
