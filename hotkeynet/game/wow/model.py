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

    :param title: Windows 里的窗口上面的 Title
    :param label: HotkeyNet 脚本里定义的 Label
    """
    title: str = attr.ib()
    label: str = attr.ib()

    @classmethod
    def make(cls, index: int) -> 'Window':
        return cls(
            title=f"WoW{str(index).zfill(2)}",
            label=f"w{str(index).zfill(2)}",
        )

    @property
    def index(self) -> int:
        return int(self.label[1:])


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
    :param window: 游戏窗口
    :param active: 设置这个人物是否是属于 HotkeyNet 的快捷键所操作的人物.
        例如你在一场游戏中定义了 5 个人物, 但是只启用了 1, 2, 3 号 3 个人物. 4, 5 号
        设置为 active = False. 在此情况下多开脚本的行为是这样的:

        1. 启动游戏时启动所有窗口
        2. 批量输入账号密码登录时, 只登录 3 个人物
        3. 按 1234 操作的时候只操作 3 个人物
        4. 使用单个窗口登录时, 可以选择全部的 5 个人物进行登录
        5. 可以用切换单个窗口快捷键切换到 5 个人物之一的窗口
        6. 用 Round robin 切换窗口时, 只在 3 个人物之间切换

        这样适合于专注于玩几个人物, 但保留快速登录其他人物的能力. 比如登录小号聊天, 倒东西等.
    :param is_leader_1: 该角色是否为 1 号司机
    :param is_leader_2: 该角色是否为 2 号司机
    :param leader_1_window: 该角色的 1 号司机的游戏窗口
    :param leader_2_window: 该角色的 2 号司机的游戏窗口

    这里没有包含任何与职业, 天赋有关的设定. 因为该模块是所有 WoW 版本通用的. 跟职业, 天赋
    有关的设定在具体版本的子模块中被定义.

    **设计思路**

    一次游戏中我们会需要知道哪些角色是坦克, 哪些角色是治疗. 或者说那个角色是扮演主坦,
    哪个角色是副坦. 我们有两种方法可以定义这件事. 一种是在顶层的 Setup 中设计一个属性:
    tank1, 其值是一个 Character 对象. 还有一种方式是在 Character 对象中设计一个属性,
    is_tank1, 其值是一个 boolean 对象.

    个人认为第二种方式更好. 因为玩魔兽玩的就是角色, 从角色的视角出发更符合人类直觉. 而且
    扁平化的枚举所有用到的人物, 以及它们扮演的不同角色, 这样的代码更容易读和编辑.

    **注意事项**

    leader_1_window 和 leader_2_window 是要跟 HotkeyNet 脚本, 以及宏命令配合使用的.
    通常 leader 就是其他队员的焦点目标, 游戏中肯定是要有一个宏命令来先选中这个焦点目标,
    然后才能将其设置为焦点的. 由于宏命令和动作条, 我们不可能创建无数个宏命令. 所以我们会在
    act 中定义我们设定好的, 有限的几个宏命令. 你设定的 leader 的窗口必须要属于那几个宏命令
    之一才能工作.
    """
    account: Account = attr.ib(default=None)
    name: str = attr.ib(default=None)
    window: Window = attr.ib(default=None)
    active: bool = attr.ib(default=True)

    is_leader_1: bool = attr.ib(default=False)
    is_leader_2: bool = attr.ib(default=False)
    leader_1_window: Window = attr.ib(default=None)
    leader_2_window: Window = attr.ib(default=None)

    def set_window(self, window: Window) -> 'Character':
        self.window = window
        return self

    def set_active(self) -> 'Character':
        self.active = True
        return self

    def set_inactive(self) -> 'Character':
        self.active = False
        return self

    def set_is_leader_1(self) -> 'Character':
        self.is_leader_1 = True
        return self

    def set_not_leader_1(self) -> 'Character':
        self.is_leader_1 = False
        return self

    def set_is_leader_2(self) -> 'Character':
        self.is_leader_2 = True
        return self

    def set_not_leader_2(self) -> 'Character':
        self.is_leader_1 = False
        return self

    def set_leader_1_window(self, window: Window) -> 'Character':
        self.leader_1_window = window
        return self

    def set_leader_2_window(self, window: Window) -> 'Character':
        self.leader_2_window = window
        return self

