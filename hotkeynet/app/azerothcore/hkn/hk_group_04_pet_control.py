# -*- coding: utf-8 -*-

"""
实现 Ctrl 1 ~ 6 的功能. 主要是宠物的动作条按键. 1 进攻主人目标, 2 撤回, 3 原地待命.
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


class HotkeyGroup04PetControlMixin:
    def build_hk_ctrl_1_to_6(self: "HknScript"):
        for i in range(1, 1 + 6):
            key = KN.CTRL_(getattr(KN, "KEY_{}".format(i)))
            with hk.Hotkey(
                id=key,
                key=KN.SCROLOCK_ON(key),
            ):
                with hk.SendLabel(
                    name="all",
                    to=self.mode.lbs_all,
                ):
                    act.target.TARGET_FOCUS_TARGET()
                    act.general.TRIGGER()

    def build_hk_group_04_pet_control_mixin(self: "HknScript"):
        self.build_hk_ctrl_1_to_6()
