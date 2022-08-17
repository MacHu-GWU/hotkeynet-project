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
    代表着一个任务角色.
    """
    account: Account = attr.ib(default=None)
    credential = attr.ib(default=None)
    name: str = attr.ib(default=None)
    talent: Talent = attr.ib(default=None)
    # window_index = attr.ib(default=None)  # type: int
    # leader1_window_index = attr.ib(default=None)  # type: int
    # leader2_window_index = attr.ib(default=None)  # type: int
    # is_tank1 = attr.ib(default=False)  # type: bool
    # is_tank2 = attr.ib(default=False)  # type: bool
    # is_dr_pala1 = attr.ib(default=False)  # type: bool
    # is_dr_pala2 = attr.ib(default=False)  # type: bool
