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
    """
    account: Account = attr.ib(default=None)
    name: str = attr.ib(default=None)
    talent: Talent = attr.ib(default=None)
    window: Window = attr.ib(default=None)

    leader1_window: Window = attr.ib(default=None)
    leader2_window: Window = attr.ib(default=None)
    is_tank1: bool = attr.ib(default=False)
    is_tank2: bool = attr.ib(default=False)
    is_dr_pala1: bool = attr.ib(default=False)
    is_dr_pala2: bool = attr.ib(default=False)
