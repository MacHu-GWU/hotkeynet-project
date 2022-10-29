# -*- coding: utf-8 -*-

from ..character import (
    login_char_fact,
    dungeon_active_char_fact,
)
from ..game_client import game_client_fact
from .base import Mode


class ModeFactory:
    def use_5p_team_solo_dungeon_festival_team_1_dk(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.group_22p_litgugu_abcd,
            active_chars=dungeon_active_char_fact.x5p_festival_team_1_dk,
        )

    def use_5p_team_solo_dungeon_festival_team_2_ss(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.group_22p_litgugu_abcd,
            active_chars=dungeon_active_char_fact.x5p_festival_team_2_ss,
        )

    def use_5p_team_solo_dungeon_festival_team_3_mix(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.group_22p_litgugu_abcd,
            active_chars=dungeon_active_char_fact.x5p_festival_team_3_mix,
        )

    def use_5p_team_solo_festival_team_4_ms_sm(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.group_22p_litgugu_abcd,
            active_chars=dungeon_active_char_fact.x5p_festival_team_4_ms_sm,
        )

    def use_5p_team_solo_festival_team_5_ms_sm(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.group_22p_litgugu_abcd,
            active_chars=dungeon_active_char_fact.x5p_festival_team_5_ms_sm,
        )

    def use_5p_team_solo_festival_team_6_litgugu_efgh(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.group_22p_litgugu_efgh,
            active_chars=dungeon_active_char_fact.x5p_festival_team_6_litgugu_efgh,
        )

    def use_5p_lgqs_abcde_leveling(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            active_chars=dungeon_active_char_fact.x5p_lgqs_abcde,
        )


dungeon_mode_fact = ModeFactory()
