# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import attr
from ordered_set import OrderedSet

from .. import model
from ..model import Account, Window
from .talent import Talent as TL, TalentCategory as TC


# @attr.s
@dataclasses.dataclass
class Character(model.Character):
    """
    :param talent: 角色天赋
    :param is_tank_1: 自己是否是 1 号坦克
    :param is_tank_2: 自己是否是 2 号坦克
    :param tank_1_window: 从自己的视角看 1 号坦克的窗口是哪个
    :param tank_2_window: 从自己的视角看 2 号坦克的窗口是哪个
    :param is_dr_pala_1: 自己是否是 1 号减伤圣骑士
    :param is_dr_pala_2: 自己是否是 2 号减伤圣骑士
    """
    talent: TL = dataclasses.field(default=None)
    is_tank_1: bool = dataclasses.field(default=False)
    is_tank_2: bool = dataclasses.field(default=False)
    tank_1_window: model.Window = dataclasses.field(default=None)
    tank_2_window: model.Window = dataclasses.field(default=None)
    is_dr_pala_1: bool = dataclasses.field(default=False)
    is_dr_pala_2: bool = dataclasses.field(default=False)

    def __hash__(self):
        return hash(self.id)

    def set_tank_1(self) -> 'Character':
        self.is_tank_1 = True
        return self

    def set_not_tank_1(self) -> 'Character':
        self.is_tank_1 = False
        return self

    def set_tank_2(self) -> 'Character':
        self.is_tank_2 = True
        return self

    def set_not_tank_2(self) -> 'Character':
        self.is_tank_2 = False
        return self

    def set_tank_1_window(self, window: model.Window) -> 'Character':
        self.tank_1_window: Window = window
        return self

    def set_tank_2_window(self, window: model.Window) -> 'Character':
        self.tank_2_window: Window = window
        return self

    def set_dr_pala_1(self) -> 'Character':
        self.is_dr_pala_1 = True
        return self

    def set_dr_pala_2(self) -> 'Character':
        self.is_dr_pala_2 = True
        return self

    def set_leader_1_tank_1(self) -> 'Character':
        self.set_is_leader_1()
        self.set_tank_1()
        return self

    def set_leader_2_tank_2(self) -> 'Character':
        self.set_is_leader_2()
        self.set_tank_2()
        return self

    def set_leader_12_and_tank_12(self) -> 'Character':
        self.set_is_leader_1()
        self.set_tank_1()
        self.set_is_leader_2()
        self.set_tank_2()
        return self


class CharacterOrderedSetHelper:
    """
    对 Character OrderedSet 有序集合的各种操作相关的函数.
    """

    def _find_key_char_window(
        self,
        chars: OrderedSet[Character],
        attr: str,
    ) -> T.Optional[Window]:
        """
        从一堆 Character 当中找到那个扮演某个特定队伍角色的人所在的窗口.

        例如找到谁是一堆角色中的 1 号司机

        如果一个队伍里有多个人被设为 1 号司机, 那么就设为自然顺序遇到的第一个 1 号司机.
        其他人则会被取消设为一号司机 (还没有实现).
        """
        window: T.Optional[Window] = None
        for char in chars:
            if getattr(char, attr):
                return char.window
        return window

    def _find_leader_1(self, chars: OrderedSet[Character]) -> T.Optional[Window]:
        return self._find_key_char_window(chars, attr="is_leader_1")

    def _find_leader_2(self, chars: OrderedSet[Character]) -> T.Optional[Window]:
        return self._find_key_char_window(chars, attr="is_leader_2")

    def _find_tank_1(self, chars: OrderedSet[Character]) -> T.Optional[Window]:
        return self._find_key_char_window(chars, attr="is_tank_1")

    def _find_tank_2(self, chars: OrderedSet[Character]) -> T.Optional[Window]:
        return self._find_key_char_window(chars, attr="is_tank_2")

    def _set_key_char_window(
        self,
        chars: OrderedSet[Character],
        attr: str,
        window: Window,
    ):
        """
        例如将指定的窗口设为所有人的 1 号司机.

        这里要注意的是 1 号司机本人不会将自己设为一号司机. 因为司机通常会要绑定焦点. 司机
        本人不需要吧自己设为焦点.
        """
        for char in chars:
            if char.window.label != window.label:
                setattr(char, attr, window)

    def _set_leader_1_window(
        self,
        chars: OrderedSet[Character],
        window: Window,
    ):
        self._set_key_char_window(chars, "leader_1_window", window)

    def _set_leader_2_window(
        self,
        chars: OrderedSet[Character],
        window: Window,
    ):
        self._set_key_char_window(chars, "leader_2_window", window)

    def _set_tank_1_window(
        self,
        chars: OrderedSet[Character],
        window: Window,
    ):
        self._set_key_char_window(chars, "tank_1_window", window)

    def _set_tank_2_window(
        self,
        chars: OrderedSet[Character],
        window: Window,
    ):
        self._set_key_char_window(chars, "tank_2_window", window)

    def set_team_leader_and_tank(self, chars: OrderedSet[Character]):  # pragma: no cover
        """
        在定义队伍时, 我们希望能简化操作. 只要在一堆角色中指定谁是 1 号司机, 谁是 2 号司机,
        那么其他人就自动将他们的 Character.leader_1_window, Character.leader_2_window
        设置好.
        """
        # find leader char window
        leader_1_window: T.Optional[Window] = self._find_leader_1(chars)
        leader_2_window: T.Optional[Window] = self._find_leader_2(chars)
        tank_1_window: T.Optional[Window] = self._find_tank_1(chars)
        tank_2_window: T.Optional[Window] = self._find_tank_2(chars)

        if leader_1_window is not None:
            self._set_leader_1_window(chars, leader_1_window)
        else:
            raise ValueError("At least one char has to be the leader 1")

        if leader_2_window is not None:
            self._set_leader_2_window(chars, leader_2_window)
        else:
            raise ValueError("At least one char has to be the leader 2")

        if tank_1_window is not None:
            self._set_tank_1_window(chars, tank_1_window)

        if tank_2_window is not None:
            self._set_tank_2_window(chars, tank_2_window)

        return chars

    def set_active(self, chars: OrderedSet[Character]):  # pragma: no cover
        for char in chars:
            char.active = True
        return chars

    def set_inactive(self, chars: OrderedSet[Character]):  # pragma: no cover
        for char in chars:
            char.active = False
        return chars

    def sort_chars_by_window_label(
        self,
        chars: OrderedSet[Character],
    ) -> OrderedSet[Character]:
        """
        将许多角色按照所在的窗口编号排序.
        """
        return OrderedSet(sorted(chars, key=lambda char: char.window.label))

    def sort_chars_by_window_title(
        self,
        chars: OrderedSet[Character],
    ) -> OrderedSet[Character]:
        """
        将许多角色按照所在的窗口名称排序.
        """
        return OrderedSet(sorted(chars, key=lambda char: char.window.title))

    def filter_by_talent(
        self,
        chars: OrderedSet[Character],
        tl: TL,
    ) -> OrderedSet[Character]:
        """
        筛选出属于某个天赋的所有角色.

        例如你可以选出所有 PvE DK 血坦克 ``Talent.dk_pve_blood_tank`` 的角色.
        """
        return OrderedSet([
            char
            for char in chars
            if char.talent is tl
        ])

    def filter_by_talent_category(
        self,
        chars: OrderedSet[Character],
        tc: TC,
    ) -> OrderedSet[Character]:
        """
        筛选出天赋属于某个天赋类别的所有角色.

        例如你可以选出所有 PvE Tank 类别的角色. 实际上是先根据类别找出所有对应的天赋的集合,
        然后一一判断这个角色的天赋在不在集合中.
        """
        talent_set = tc.talents
        return OrderedSet([
            char
            for char in chars
            if char.talent in talent_set
        ])


char_oset_helper = CharacterOrderedSetHelper()
