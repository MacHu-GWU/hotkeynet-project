# -*- coding: utf-8 -*-

from ..character import (
    login_char_fact,
    raid_active_char_fact,
)
from ..game_client import game_client_fact
from .base import Mode


class ModeFactory:
    def use_solo_raid_10p_batlefury_luxiaofeng_core_team(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            active_chars=raid_active_char_fact.x10p_batlefury_luxiaofeng_core_team,
        )


raid_mode_fact = ModeFactory()
