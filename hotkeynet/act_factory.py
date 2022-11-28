# -*- coding: utf-8 -*-

"""
在 ``hotkeytnet`` 这个库中, 我们编程的对象主要是定义:

- "触发器", 也就是 ``hotkeynet.script.Hotkey`` 对象.
- 以及按下触发器后的 "动作", 也就是 ``hotkeynet.script.Key`` 对象.

这个 ``hotkeynet.script.Key`` 对应着键盘鼠标的虚拟按键码, 定义了按下什么键.

我们希望程序代码更具有人类可读性, 而不是定义 "触发器 Scroll + 1" 对应的 "动作是 1".
这里的 1 对于多开游戏的人来说是知道对应着动作条按键 1. 而对程序开发者而言, 看到了 1 并不能
说明任何问题.

为了解决这一问题, 我们发明了 ``act`` 模块. 用人类可读的变量名的方式, 用游戏内的功能, 例如
移动, 施放某个技能等名字, 枚举了所有游戏动作以及背后的实际键盘按键的关系. 这一关系也可以作为
我们设置游戏动作条的参考.

由于我们每次引用变量时, 我们希望引用的是 ``hotkeynet.script.Key`` 实例对象. 而一个实例对象
是 mutable 的, 可以被修改. 如果一个动作在多个地方被引用了, 那么一个地方的修改就可能悄悄的
改变在另一个地方的行为. 所以我们对这种枚举类的引用做了一些改变. 使得我们在定义枚举类的时候,
使用的是简单的 Key Name 字符串, 也是不可变的对象. 而在引用枚举类的时候, 用的则是 变量名 加 括号,
``变量名()`` 的语法实际上是一个工厂函数, 每次都是创建新的实例, 避免了以上的问题, 同时又让
定义枚举类的语法变得非常简洁.
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
