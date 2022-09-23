# -*- coding: utf-8 -*-

from ..character import (
    login_char_fact,
    raid_active_char_fact,
    dungeon_active_char_fact,
)
from ..game_client import GameClient
from ..hkn import HknScript
from ..paths import path_azerothcore_hkn
from .base import Mode


class ModeFactory:
    def solo_raid_10p_core_team(self) -> Mode:
        return Mode(
            game_client=GameClient().use_1920_1080_resolution(),
            # game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            login_chars=login_char_fact.r_abcde_fghij,
            active_chars=raid_active_char_fact.x10p_r_abcde_fghij_core_team,
        )


mode_fact = ModeFactory()
