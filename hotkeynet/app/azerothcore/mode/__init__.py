# -*- coding: utf-8 -*-

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet.game.wow.wlk import Talent as TL, TalentCategory as TC

from .. import act
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

    def solo_raid_10p_naxx_abomination_4th_boss(self) -> Mode:
        """
        先所有人手动将焦点设置为奶德.
        然后再按 + 号使用第二套焦点模式对焦点进行修改
        """
        mode = Mode(
            game_client=GameClient().use_1920_1080_resolution(),
            # game_client=GameClient().use_1600_900_resolution(),
            # game_client=GameClient().use_1176_664_resolution(),
            login_chars=login_char_fact.r_abcde_fghij,
            active_chars=raid_active_char_fact.x10p_r_abcde_fghij_core_team,
        )

        with hk.Hotkey(
            id="SetFocusMode2",
            key=KN.SCROLOCK_ON(KN.KEY_12_PLUS),
        ) as mode.hkn_script.hk_12_focus_mode_2:
            for char in mode.active_chars:
                if char.is_leader_1:  # 1 号司机本人清除焦点
                    leader_1_label = char.window.label
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[char.window.label, ],
                    ):
                        act.General.CLEAR_FOCUS_NUMPAD_7()

            # 奶德将焦点设置为 1 号司机
            first_resto_druid_label = mode.lbs_by_tc(TC.druid_resto)[0]
            with hk.SendLabel(
                to=[first_resto_druid_label, ],
            ):
                act.target_leader_key_mapper[leader_1_label]()
                act.General.SET_FOCUS_KEY_NUMPAD_6()
             
        return mode


mode_fact = ModeFactory()
