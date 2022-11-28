# -*- coding: utf-8 -*-

"""
实现由在主控角色界面下, 用鼠标在团队框架上进行单机来实现治疗的快捷键.
需要配合团队框架 Healbot 插件使用.
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


class HotkeyGroup11Healbot:
    def _build_send_label_non_shaman_dps(self: "HknScript"):
        """
        点击 Healbot 的时候, 所有 DPS 继续攻击焦点的目标. 唯独 增强萨满 和 元素萨满 例外.
        虽然它们是 DPS 职业, 但是依然要跟其他治疗一样, 对团队框架目标使用治疗链.
        """
        lbs_dps = self.mode.lbs_by_tc(TC.dps)
        lbs_shaman_non_resto = self.mode.lbs_by_tc(TC.shaman_non_resto)
        to = utils.difference_list(lbs_dps, lbs_shaman_non_resto)
        with hk.SendLabel(
            id="non_shaman_dps",
            to=to,
        ) as send_label:
            act.target.TARGET_FOCUS_TARGET()
            hk.Key(key=KN.KEY_2)
            return send_label

    def build_hk_healbot_small_heal(self: "HknScript"):
        with hk.Hotkey(
            id="Healbot Small Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_small_heal:
            self.mode.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.paladin_holy.HB_Flash_of_Light,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.shaman_restoration.HB_Riptide,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.druid_restoration.HB_Rejuvenation,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    act.priest_discipline.HB_Power_Word_Shield,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.priest_holy.HB_Flash_Heal,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    act.key.Key_2,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.dps,
                funcs=[
                    act.target.TARGET_FOCUS_TARGET,
                    act.key.Key_2,
                ],
            )

    def build_hk_healbot_big_heal(self: "HknScript"):
        with hk.Hotkey(
            id="Healbot Big Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_RButton)),
        ) as self.hk_healbot_big_heal:
            self.mode.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.paladin_holy.HB_Holy_Light,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.shaman_restoration.HB_Healing_Wave,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.druid_restoration.HB_Nourish,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    act.priest_discipline.HB_Power_Word_Shield,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.priest_holy.HB_Flash_Heal,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    act.key.Key_2,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.dps,
                funcs=[
                    act.target.TARGET_FOCUS_TARGET,
                    act.key.Key_2,
                ],
            )

    def build_hk_healbot_aoe_heal(self: "HknScript"):
        with hk.Hotkey(
            id="Healbot Aoe Heal",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_aoe_heal:
            self.mode.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.paladin_holy.HB_Holy_Light,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.shaman_restoration.HB_Chain_Heal_for_mbox,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.druid_restoration.HB_Wild_Growth,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    act.priest_discipline.HB_Power_Word_Shield,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.priest_holy.HB_Circle_of_Healing,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    act.key.Key_2,
                ],
            )
            self._build_send_label_non_shaman_dps(),

    def build_hk_healbot_dispel(self: "HknScript"):
        with hk.Hotkey(
            id="Healbot Dispel",
            key=KN.SCROLOCK_ON(KN.MOUSE_MButton),
        ) as self.hk_healbot_dispel:
            self.mode.build_send_label_by_tc(
                tc=TC.paladin_holy,
                funcs=[
                    act.paladin_holy.HB_Cleanse,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.shaman_resto,
                funcs=[
                    act.shaman_restoration.HB_Cleanse_Spirit,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.druid_resto,
                funcs=[
                    act.druid_restoration.HB_Remove_Curse,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.priest_disco,
                funcs=[
                    act.priest_discipline.Dispel_Magic,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.priest_holy,
                funcs=[
                    act.priest_holy.Dispel_Magic,
                ],
            )
            self.mode.build_send_label_by_tc(
                tc=TC.tank,
                funcs=[
                    act.key.Key_2,
                ],
            )
            self._build_send_label_non_shaman_dps(),

    def build_hk_group_11_healbot_mixin(self: "HknScript"):
        self.build_hk_healbot_small_heal()
        self.build_hk_healbot_big_heal()
        self.build_hk_healbot_aoe_heal()
        self.build_hk_healbot_dispel()
