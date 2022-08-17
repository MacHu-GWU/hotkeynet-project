# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass


@attr.s
class Character(AttrsClass):
    """
    :param credential:
    :param window_index: 你将在哪个窗口玩这个人物
    :param leader1_window_index: 多开时模式 1 下的焦点角色所在的窗口序号
    :param leader2_window_index: 多开时模式 2 下的焦点角色所在的窗口序号
    """
    credential = attr.ib(default=None)  # type: Credential
    name = attr.ib(default=None)  # type: str
    talent = attr.ib(default=None)  # type: Talent
    window_index = attr.ib(default=None)  # type: int
    leader1_window_index = attr.ib(default=None)  # type: int
    leader2_window_index = attr.ib(default=None)  # type: int
    is_tank1 = attr.ib(default=False)  # type: bool
    is_tank2 = attr.ib(default=False)  # type: bool
    is_dr_pala1 = attr.ib(default=False)  # type: bool
    is_dr_pala2 = attr.ib(default=False)  # type: bool
