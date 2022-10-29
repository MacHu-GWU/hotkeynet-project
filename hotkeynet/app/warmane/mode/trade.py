# -*- coding: utf-8 -*-

from ..character import (
    login_char_fact,
    trade_active_char_fact,
)
from ..game_client import game_client_fact
from .base import Mode


class ModeFactory:
    def use_22p_monthly_login_1(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            active_chars=trade_active_char_fact.x22p_monthly_login_team_1,
        )

    def use_22p_monthly_login_2(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            active_chars=trade_active_char_fact.x22p_monthly_login_team_2,
        )

    def use_5p_daily_alchemy_transmute(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.group_core_6p_alchemy_transmute,
            active_chars=trade_active_char_fact.x5p_alchemy_transmute,
        )


trade_mode_fact = ModeFactory()
