# -*- coding: utf-8 -*-

from ..character import (
    trade_active_char_fact,
)
from ..game_client import GameClient
from .base import Mode


class ModeFactory:
    def use_22p_monthly_login_1(self) -> Mode:
        return Mode(
            # game_client=GameClient().use_1920_1080_resolution(),
            game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            active_chars=trade_active_char_fact.x22p_monthly_login_team_1,
        )

    def use_22p_monthly_login_2(self) -> Mode:
        return Mode(
            # game_client=GameClient().use_1920_1080_resolution(),
            game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            active_chars=trade_active_char_fact.x22p_monthly_login_team_2,
        )


trade_mode_fact = ModeFactory()
