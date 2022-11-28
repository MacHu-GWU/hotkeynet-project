# -*- coding: utf-8 -*-

"""
实现 Alt + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
"""

import typing as T

import hotkeynet as hk
from hotkeynet import KN
from hotkeynet import utils
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


class HotkeyGroup08AltNumpad1To12:
    def build_hk_alt_numpad_1_misdirect_and_tot_focus(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad1 - 猎人误导坦克",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_1)),
        ) as self.hk_alt_numpad_1_hunter_misdirect:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.hunter.Misdirection_Focus_Macro()

    def build_hk_alt_numpad_2_aspect_of_pact_or_hawk(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad2 - 猎人在雄鹰和豹群守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_2)),
        ) as self.hk_alt_numpad_2_aspect_of_pact_or_hawk:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.hunter.Aspect_of_Pact_or_dragon_hawk()

    def build_hk_alt_numpad_3_aspect_of_viper_or_hawk(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad3 - 猎人在雄鹰和蝮蛇守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_3)),
        ) as self.hk_alt_numpad_3_aspect_of_viper_or_hawk:
            with hk.SendLabel(
                name=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.hunter.Aspect_of_viper_or_dragon_hawk()

    def build_hk_alt_numpad_4_all_boomkin_star_fall(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad4 - 鸟德集体放星落",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_4)),
        ) as self.hk_alt_numpad_4_all_boomkin_star_fall:
            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.druid_balance.Starfall()

    def build_hk_alt_numpad_5_all_dps_burst(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad5 - DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_5)),
        ) as self.hk_alt_numpad_5_all_dps_burst:
            with hk.SendLabel(
                id=TC.dps.name,
                to=self.mode.lbs_by_tc(TC.dps),
            ):
                act.general.DPS_BURST_MACRO_KEY_ALT_D()

    def build_hk_alt_numpad_6_all_dps_burst_and_hero(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad6 - 开嗜血, 同时所有 DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_6)),
        ) as self.hk_alt_numpad_6_all_dps_burst_and_hero:
            with hk.SendLabel(
                id="all_non_shaman_dps",
                to=utils.difference_list(
                    self.mode.lbs_by_tc(TC.dps),
                    self.mode.lbs_by_tc(TC.shaman),
                ),
            ):
                act.general.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id=TC.shaman_elemental.name,
                to=self.mode.lbs_by_tc(TC.shaman_elemental),
            ):
                act.shaman.Bloodlust_or_Heroism()
                act.general.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id=TC.shaman_resto.name,
                to=self.mode.lbs_by_tc(TC.shaman_resto),
            ):
                act.shaman.Bloodlust_or_Heroism()

    def build_hk_alt_numpad_7_8_9_first_raid_damage_reduction(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad7",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_7)),
        ) as self.hk_alt_numpad_7_raid_damage_reduction:
            with hk.SendLabel(
                id=TC.paladin_protect.name,
                to=self.mode.lbs_by_tc(TC.paladin_protect),
            ):
                # 要点两下, 启动神圣牺牲后自己取消
                act.paladin_protection.Divine_Sacrifice()
                act.paladin_protection.Divine_Sacrifice()

        with hk.Hotkey(
            id="Alt Numpad8",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_8)),
        ) as self.hk_alt_numpad_8_raid_damage_reduction:
            with hk.SendLabel(
                id=TC.paladin_holy.name,
                to=self.mode.lbs_by_tc(TC.paladin_holy),
            ):
                # 要点两下, 启动神圣牺牲后自己取消
                act.paladin_protection.Divine_Sacrifice()
                act.paladin_protection.Divine_Sacrifice()

        with hk.Hotkey(
            id="Alt Numpad9",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_9)),
        ) as self.hk_alt_numpad_9_raid_damage_reduction:
            with hk.SendLabel(
                id=TC.paladin_holy.name,
                to=self.mode.lbs_by_tc(TC.paladin_holy),
            ):
                act.paladin_holy.Aura_Mastery()

    def build_hk_alt_numpad_10_cleansing_totem(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad10 - 萨满放清毒图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_0)),
        ) as self.hk_alt_numpad_10_cleansing_totem:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.shaman.Cleansing_Totem()

    def build_hk_alt_numpad_11_tremor_totem(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad11 - 萨满放战栗图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_11_DIVIDE)),
        ) as self.hk_alt_numpad_11_tremor_totem:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.shaman.Tremor_Totem()

    def build_hk_alt_numpad_12_earth_binding_totem(self: "HknScript"):
        with hk.Hotkey(
            id="Alt Numpad12 - 萨满放地缚图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_12_MULTIPLY)),
        ) as self.hk_alt_numpad_12_earth_binding_totem:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.shaman.Earthbind_Totem()

    def build_hk_group_08_alt_numpad_1_to_12_mixin(self):
        self.build_hk_alt_numpad_1_misdirect_and_tot_focus()
        self.build_hk_alt_numpad_2_aspect_of_pact_or_hawk()
        self.build_hk_alt_numpad_3_aspect_of_viper_or_hawk()
        self.build_hk_alt_numpad_4_all_boomkin_star_fall()
        self.build_hk_alt_numpad_5_all_dps_burst()
        self.build_hk_alt_numpad_6_all_dps_burst_and_hero()
        self.build_hk_alt_numpad_7_8_9_first_raid_damage_reduction()
        self.build_hk_alt_numpad_10_cleansing_totem()
        self.build_hk_alt_numpad_11_tremor_totem()
        self.build_hk_alt_numpad_12_earth_binding_totem()
