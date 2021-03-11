# -*- coding: utf-8 -*-

"""
此模块下的的定义了各种 Config Data Class 对象, 用于保存
"""

import attr

from .active_character import ActiveCharacterConfig
from .base import BaseConfig
from .game_client import GameClientConfig
from .toggle_window import ToggleWindowConfig


@attr.s
class Config(BaseConfig):
    game_client_config = attr.ib(default=None)  # type: GameClientConfig
    toggle_window_config = attr.ib(default=None)  # type: ToggleWindowConfig
    active_character_config = attr.ib(default=None)  # type: ActiveCharacterConfig
