# -*- coding: utf-8 -*-

"""
此模块下的的定义了各种 Config Data Class 对象, 用于保存
"""

import attr

from .active_character import ActiveCharacterConfig
from .base import BaseConfig
from .game_client import GameClientConfig
from .toggle_window import ToggleWindowConfig
from ..constant.talent_category_association import TalentCategory, get_talent_by_category
from ..constant.windows import window_index
from ....script import Script


def _default_post_hook(config: 'Config', script: Script):
    pass


@attr.s
class Config(BaseConfig):
    game_client_config = attr.ib(default=None)  # type: GameClientConfig
    toggle_window_config = attr.ib(default=None)  # type: ToggleWindowConfig
    active_character_config = attr.ib(default=None)  # type: ActiveCharacterConfig
    post_hook = attr.ib(default=_default_post_hook)

    def lbs_all(self):
        lbs = [
            window_index[char.window_index].label
            for char in self.active_character_config.active_characters
        ]
        lbs.sort()
        return lbs

    def lbs_by_tc(self, tc: TalentCategory):
        talent_set = get_talent_by_category(category=tc)
        lbs = [
            window_index[char.window_index].label
            for char in self.active_character_config.active_characters
            if char.talent in talent_set
        ]
        lbs.sort()
        return lbs

    def lbs_tank1(self):
        lbs = [
            window_index[char.window_index].label
            for char in self.active_character_config.active_characters
            if char.is_tank1
        ]
        lbs.sort()
        return lbs

    def lbs_tank2(self):
        lbs = [
            window_index[char.window_index].label
            for char in self.active_character_config.active_characters
            if char.is_tank2
        ]
        lbs.sort()
        return lbs

    def lbs_dr_pala1(self):
        lbs = [
            window_index[char.window_index].label
            for char in self.active_character_config.active_characters
            if char.is_dr_pala1
        ]
        lbs.sort()
        return lbs

    def lbs_dr_pala2(self):
        lbs = [
            window_index[char.window_index].label
            for char in self.active_character_config.active_characters
            if char.is_dr_pala2
        ]
        lbs.sort()
        return lbs
