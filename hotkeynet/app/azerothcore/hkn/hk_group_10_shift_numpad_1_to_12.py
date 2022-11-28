# -*- coding: utf-8 -*-

"""
实现 Shift + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
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


class HotkeyGroup10ShiftNumpad1To12:
    def build_hk_shift_numpad_1(self: "HknScript"):
        with hk.Hotkey(
            id="Shift Numpad1",
            key=KN.SCROLOCK_ON(KN.NUMPAD_SHIFT_1_END),
        ) as self.hk_shift_numpad_1:
            with hk.SendLabel(
                name=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.shaman.Call_of_the_Ancestors()

    def build_hk_shift_numpad_2(self: "HknScript"):
        with hk.Hotkey(
            id="Shift Numpad2",
            key=KN.SCROLOCK_ON(KN.NUMPAD_SHIFT_2_DOWN),
        ) as self.hk_shift_numpad_2:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.shaman.Totemic_Recall()

    def build_hk_group_10_mixin(self):
        self.build_hk_shift_numpad_1()
        self.build_hk_shift_numpad_2()
