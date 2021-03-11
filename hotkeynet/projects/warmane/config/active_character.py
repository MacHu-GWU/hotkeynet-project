# -*- coding: utf-8 -*-

import attr
import typing
from .base import BaseConfig
from ..constant.characters import Character


@attr.s
class ActiveCharacterConfig(BaseConfig):
    """
    定义了所有启用的角色列表.
    """
    active_characters = attr.ib(default=lambda: []) # type: typing.List[Character]

    def iter_by_window_index(self):
        return sorted(self.active_characters, key=lambda ac: ac.window_index)

    def set_leader1_window_index(self, ind: int):
        """
        将所有角色的 leader1 的 window index 设为某个值. 当然 window index 本身就是
        这个值的角色除外, 因为他本身就是 leader.
        """
        for ac in self.active_characters:
            if ac.window_index != ind:
                ac.leader1_window_index = ind

    def set_leader2_window_index(self, ind: int):
        for ac in self.active_characters:
            if ac.window_index != ind:
                ac.leader2_window_index = ind


    def validate_active_characters(self):
        """
        """
        assert len(set([ac.window_index for ac in self.active_characters])) == len(self.active_characters)

    def validate(self):
        self.validate_active_characters()
