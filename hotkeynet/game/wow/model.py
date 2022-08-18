# -*- coding: utf-8 -*-

import typing as T
import enum

import attr
from attrs_mate import AttrsClass


class Talent(enum.IntEnum):
    pass


class TalentCategory(enum.IntEnum):
    pass


@attr.s
class Window(AttrsClass):
    """
    代表着一个 魔兽世界 客户端窗口.
    """
    title: str = attr.ib()
    label: str = attr.ib()

    @classmethod
    def make(cls, index: int) -> 'Window':
        return cls(
            title=f"WoW{str(index).zfill(2)}",
            label=f"w{str(index).zfill(2)}",
        )


def _get_win(index_or_window: T.Union[int, Window]) -> 'Window':
    if isinstance(index_or_window, Window):
        return index_or_window
    else:
        return Window.make(index=index_or_window)


@attr.s
class Account(AttrsClass):
    """
    代表着一个 魔兽世界账号.
    """
    username: str = attr.ib()
    password: str = attr.ib()


@attr.s
class Character(AttrsClass):
    """
    代表着一个正在进行的游戏角色. 有着具体的天赋. 比如一个圣骑士角色有两套天赋.
    在天赋 1 下就算是一个 Character, 在天赋 2 下算是另一个 Character.

    :param account: 与该游戏角色所绑定的账号密码信息
    :param name: 游戏角色名
    :param talent: 角色天赋
    :param window_index: 游戏窗口的序号

    **设计思路**

    一次游戏中我们会需要知道哪些角色是坦克, 哪些角色是治疗. 或者说那个角色是扮演主坦,
    哪个角色是副坦. 我们有两种方法可以定义这件事. 一种是在顶层的 Setup 中设计一个属性:
    tank1, 其值是一个 Character 对象. 还有一种方式是在 Character 对象中设计一个属性,
    is_tank1, 其值是一个 boolean 对象.

    个人认为第二种方式更好. 因为玩魔兽玩的就是角色, 从角色的视角出发更符合人类直觉. 而且
    扁平化的枚举所有用到的人物, 以及它们扮演的不同角色, 这样的代码更容易读和编辑.
    """
    account: Account = attr.ib(default=None)
    name: str = attr.ib(default=None)
    window: Window = attr.ib(default=None)
    leader1_window: Window = attr.ib(default=_get_win(1))
    leader2_window: Window = attr.ib(default=_get_win(10))
    active: bool = attr.ib(default=True)

    def set_window(self, index: T.Union[int, Window]) -> 'Character':
        self.window = _get_win(index)
        return self

    def set_leader1_window(self, index: T.Union[int, Window]) -> 'Character':
        self.leader1_window = _get_win(index)
        return self

    def set_leader2_window(self, index: T.Union[int, Window]) -> 'Character':
        self.leader2_window = _get_win(index)
        return self

    def set_active(self) -> 'Character':
        self.active = True
        return self

    def set_inactive(self) -> 'Character':
        self.active = False
        return self
