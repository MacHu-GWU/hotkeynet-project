# -*- coding: utf-8 -*-

"""
实现 Ctrl + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
"""

import typing as T

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet.game.wow.wlk import (
    Character,
    Window,
    Talent as TL,
    TalentCategory as TC,
    char_oset_helper,
)
from hotkeynet.app.wow.wlk.servers.acore import act

if T.TYPE_CHECKING:
    from .script import HknScript


class HotkeyGroup09CtrlNumpad1To12:
    def build_hk_ctrl_numpad_1_silence_shot_focus_target(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad1 - 射击猎人对焦点的目标释放沉默射击",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_1)),
        ) as self.hk_ctrl_numpad_1:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.target.TARGET_FOCUS_TARGET()
                act.hunter_marksmanship.Silencing_Shot()

    def build_hk_ctrl_numpad_2_counter_spell_focus_target(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad2 - 法师对焦点的目标释放法术反制",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_2)),
        ) as self.hk_ctrl_numpad_2:
            with hk.SendLabel(
                id=TC.mage.name,
                to=self.mode.lbs_by_tc(TC.mage),
            ):
                act.target.TARGET_FOCUS_TARGET()
                act.mage.Counterspell()

    def build_hk_ctrl_numpad_3_aggressive_dispel(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad3 - 进攻驱散",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_3)),
        ) as self.hk_ctrl_numpad_3:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.target.TARGET_FOCUS_TARGET()
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.shaman.Purge()

            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.target.TARGET_FOCUS_TARGET()
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.priest.Dispel_Magic()

    def build_hk_ctrl_numpad_4_aoe_fear(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad4",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_4)),
        ) as self.hk_ctrl_numpad_4:
            with hk.SendLabel(
                id=TC.priest_shadow.name,
                to=self.mode.lbs_by_tc(TC.priest_shadow),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.priest_shadow.Psychic_Horror()

    def build_hk_ctrl_numpad_5_typhoon(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad5",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_5)),
        ) as self.hk_ctrl_numpad_5:
            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.druid_balance.Typhoon()

    def build_hk_ctrl_numpad_6_thunder_storm(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad6",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_6)),
        ) as self.hk_ctrl_numpad_6:
            with hk.SendLabel(
                id="all_elemental_shaman",
                to=self.mode.lbs_by_tc(TC.shaman_elemental),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.shaman_elemental_combat.Thunderstorm()

    def build_hk_ctrl_numpad_7_hymn_of_life(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad7",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_7)),
        ) as self.hk_ctrl_numpad_7:
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.priest.Divine_Hymn()

    def build_hk_ctrl_numpad_10_hymn_of_mana(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad10",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_0)),
        ) as self.hk_ctrl_numpad_10:
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.priest.Hymn_of_Hope()

    def build_hk_ctrl_numpad_11_tank_1_taunt(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad11 - 主坦克嘲讽",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_11_DIVIDE)),
        ) as self.hk_ctrl_numpad_11:
            with hk.SendLabel(
                id="tank1",
                to=self.mode.lbs_tank1,
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.paladin_protection.Hand_of_Reckoning()

    def build_hk_ctrl_numpad_12_tank_2_taunt(self: "HknScript"):
        with hk.Hotkey(
            id="Ctrl Numpad12 - 副坦克嘲讽",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_12_MULTIPLY)),
        ) as self.hk_ctrl_numpad_12:
            with hk.SendLabel(
                id="tank2",
                to=self.mode.lbs_tank2,
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.dk.Dark_Command()

    def build_hk_group_09_ctrl_numpad_1_to_12_mixin(self: "HknScript"):
        self.build_hk_ctrl_numpad_1_silence_shot_focus_target()
        self.build_hk_ctrl_numpad_2_counter_spell_focus_target()
        self.build_hk_ctrl_numpad_3_aggressive_dispel()
        self.build_hk_ctrl_numpad_4_aoe_fear()
        self.build_hk_ctrl_numpad_5_typhoon()
        self.build_hk_ctrl_numpad_6_thunder_storm()
        self.build_hk_ctrl_numpad_7_hymn_of_life()
        self.build_hk_ctrl_numpad_10_hymn_of_mana()
        self.build_hk_ctrl_numpad_11_tank_1_taunt()
        self.build_hk_ctrl_numpad_12_tank_2_taunt()
