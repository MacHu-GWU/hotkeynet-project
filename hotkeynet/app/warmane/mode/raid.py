# -*- coding: utf-8 -*-

from ..character import (
    login_char_fact,
    raid_active_char_fact,
)
from ..game_client import GameClient
from .base import Mode


class ModeFactory:
    def use_solo_raid_10p_batlefury_luxiaofeng_core_team(self) -> Mode:
        return Mode(
            # game_client=GameClient().use_1920_1080_resolution(),
            game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            active_chars=raid_active_char_fact.x10p_batlefury_luxiaofeng_core_team,
        )


raid_mode_fact = ModeFactory()
