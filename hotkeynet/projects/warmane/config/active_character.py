# -*- coding: utf-8 -*-

import typing

import attr

from .base import BaseConfig
from ..constant.characters import Character
from ..constant.talent_category_association import (
    Talent, TalentCategory, get_talent_by_category,
)
from ..constant.windows import window_index

@attr.s
class ActiveCharacterConfig(BaseConfig):
    """
    定义了所有启用的角色列表.
    """
    active_characters = attr.ib(default=lambda: [])  # type: typing.List[Character]

    _characters_name_mapper = None

    def get_character_by_name(self, name: str) -> Character:
        if self._characters_name_mapper is None:
            self._characters_name_mapper = {
                char.name: char
                for char in self.active_characters
            }
        return self._characters_name_mapper[name]

    def set_leader1_window_index(self, ind: int):
        """
        将所有角色的 leader1 的 window index 设为某个值. 当然 window index 本身就是
        这个值的角色除外, 因为他本身就是 leader.
        """
        for ac in self.active_characters:
            if ac.window_index != ind:
                ac.leader1_window_index = ind
            else:
                ac.leader1_window_index = None

    def set_leader2_window_index(self, ind: int):
        for ac in self.active_characters:
            if ac.window_index != ind:
                ac.leader2_window_index = ind
            else:
                ac.leader2_window_index = None

    def validate_active_characters(self):
        """
        """
        assert len(set([ac.window_index for ac in self.active_characters])) == len(self.active_characters)

    def validate(self):
        self.validate_active_characters()

    def iter_by_window_index(self) -> typing.List[Character]:
        return list(sorted(self.active_characters, key=lambda ac: ac.window_index))

    def iter_by_talent_category(self, tc: TalentCategory) -> typing.List[Character]:
        talent_list = get_talent_by_category(tc)
        return [
            ac
            for ac in self.active_characters
            if ac.talent in talent_list
        ]

    def iter_by_talent(self, t: Talent) -> typing.List[Character]:
        return [
            ac
            for ac in self.active_characters
            if ac.talent is t
        ]

    def window_label_list_by_talent_category(self, tc: TalentCategory) -> typing.List[str]:
        """
        返回所属的 active character 列表中所有符合 TalentCategory 的 Character,
        例如 TalentCategory.dps 这种, 其所对应的 window label. 以供 HotkeyNet 脚本
        中的 SendLabel.to 这样属性使用.
        """
        return [
            window_index[ac.window_index].label
            for ac in self.iter_by_talent_category(tc=tc)
        ]

    def window_label_list_by_talent(self, t: Talent) -> typing.List[str]:
        """
        返回所属的 active character 列表中所有符合 Talent 的 Character,
        例如 Talent.druid_pve_balance 这种, 其所对应的 window label. 以供 HotkeyNet 脚本
        中的 SendLabel.to 这样属性使用.
        """
        return [
            window_index[ac.window_index].label
            for ac in self.iter_by_talent(t=t)
        ]

    def window_label_list_all(self):
        return [
            window_index[ac.window_index].label
            for ac in self.active_characters
        ]
