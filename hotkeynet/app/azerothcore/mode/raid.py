# -*- coding: utf-8 -*-

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet.game.wow.wlk import (
    Talent as TL,
    TalentCategory as TC,
)

from .. import act
from ..hkn import HknScript
from ..character import (
    login_char_fact,
    raid_active_char_fact,
)
from ..game_client import game_client_fact
from .base import Mode


class ModeFactory:
    @property
    def x10p_core_team(self) -> Mode:
        return Mode(
            game_client=game_client_fact.resolution_1920_1080,
            # game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.r_abcde_fghij,
            active_chars=raid_active_char_fact.x10p_r_abcde_fghij_core_team,
        )

    @property
    def x10p_naxx_abomination_4th_boss(self) -> Mode:
        """
        先所有人手动将焦点设置为奶德.
        然后再按 + 号使用第二套焦点模式对焦点进行修改
        """
        mode = Mode(
            game_client=game_client_fact.resolution_1920_1080,
            # game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.r_abcde_fghij,
            active_chars=raid_active_char_fact.x10p_r_abcde_fghij_core_team,
        )

        mode.hkn_script.script.blocks.remove(mode.hkn_script.hk_12_focus_mode_2)

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

    @property
    def x25p_core_team(self) -> Mode:
        return Mode(
            # game_client=game_client_fact.resolution_1920_1080,
            game_client=game_client_fact.resolution_1600_900,
            # game_client=game_client_fact.resolution_1176_664,
            login_chars=login_char_fact.r_a_to_y,
            active_chars=raid_active_char_fact.x25p_r_a_to_y_core_team,
            target_tank1=act.Target.TARGET_W01_RA,
            target_tank2=act.Target.TARGET_W10_RJ,
        )


raid_mode_fact = ModeFactory()