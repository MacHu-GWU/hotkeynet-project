# -*- coding: utf-8 -*-

import typing as T

import attr
from attrs_mate import AttrsClass

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

from . import act
from .icons import Icons

if T.TYPE_CHECKING:
    from .mode.base import Mode


@attr.s
class HknScript(AttrsClass):
    mode: 'Mode' = attr.ib(default=None)
    script: hk.Script = attr.ib(factory=hk.Script)

    def __attrs_post_init__(self):
        # 此时 Script 已经不再 context 中, 我们也不希望没定义一个 Hotkey 就一直用
        # with script 的语法. 所以我们手动将 script 对象设置为 Context 的顶层
        # hk.context.push(self.script)
        self.build_hk_group_07()
        self.build_hk_group_08_alt_numpad_1_to_12()
        self.build_hk_group_09_ctrl_numpad_1_to_12()
        self.build_hk_group_10()
        self.build_hk_group_11_healbot()
        self.build_control_panel()

    # -------------------------------------------------------------------------
    # 实现 Alt + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
    # -------------------------------------------------------------------------
    __anchor_hk_08_alt_numpad_1_to_12 = None

    def build_hk_alt_numpad_1_misdirect_and_tot_focus(self):
        with hk.Hotkey(
            id="Alt Numpad1 - 猎人误导坦克",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_1)),
        ) as self.hk_alt_numpad_1:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.Hunter.ALL_SPEC_MISDIRECTION_FOCUS_MACRO()

    def build_hk_alt_numpad_2_aspect_of_pact_or_hawk(self):
        with hk.Hotkey(
            id="Alt Numpad2 - 猎人在雄鹰和豹群守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_2)),
        ) as self.hk_alt_numpad_2:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.Hunter.ALL_SPEC_ASPECT_OF_PACT_OR_DRAGON_HAWK()

    def build_hk_alt_numpad_3_aspect_of_viper_or_hawk(self):
        with hk.Hotkey(
            id="Alt Numpad3 - 猎人在雄鹰和蝮蛇守护之间切换",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_3)),
        ) as self.hk_alt_numpad_3:
            with hk.SendLabel(
                name=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.Hunter.ALL_SPEC_ASPECT_OF_VIPER_OR_DRAGON_HAWK()

    def build_hk_alt_numpad_4_all_boomy_star_fall(self):
        with hk.Hotkey(
            id="Alt Numpad4 - 鸟德集体放星落",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_4)),
        ) as self.hk_alt_numpad_4:
            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F()

    def build_hk_alt_numpad_5_all_dps_burst(self):
        with hk.Hotkey(
            id="Alt Numpad5 - DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_5)),
        ) as self.hk_alt_numpad_5:
            with hk.SendLabel(
                id=TC.dps.name,
                to=self.mode.lbs_by_tc(TC.dps),
            ):
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

    def build_hk_alt_numpad_6_all_dps_burst_and_hero(self):
        with hk.Hotkey(
            id="Alt Numpad6 - 开嗜血, 同时所有 DPS 开爆发技能",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_6)),
        ) as self.hk_alt_numpad_6:
            with hk.SendLabel(
                id="all_non_shaman_dps",
                to=utils.difference_list(
                    self.mode.lbs_by_tc(TC.dps),
                    self.mode.lbs_by_tc(TC.shaman),
                ),
            ):
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id=TC.shaman_elemental.name,
                to=self.mode.lbs_by_tc(TC.shaman_elemental),
            ):
                act.Shaman.ALL_SPEC_BLOOD_THIRST_HEROISM()
                act.General.DPS_BURST_MACRO_KEY_ALT_D()

            with hk.SendLabel(
                id=TC.shaman_resto.name,
                to=self.mode.lbs_by_tc(TC.shaman_resto),
            ):
                act.Shaman.ALL_SPEC_BLOOD_THIRST_HEROISM()

    def build_hk_alt_numpad_7_8_9_first_raid_damage_reduction(self):
        with hk.Hotkey(
            id="Alt Numpad7",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_7)),
        ) as self.hk_alt_numpad_7:
            with hk.SendLabel(
                id=TC.paladin_protect.name,
                to=self.mode.lbs_by_tc(TC.paladin_protect),
            ):
                # 要点两下, 启动神圣牺牲后自己取消
                act.Paladin.ALL_SPEC_DIVINE_SACRIFICE()
                act.Paladin.ALL_SPEC_DIVINE_SACRIFICE()

        with hk.Hotkey(
            id="Alt Numpad8",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_8)),
        ) as self.hk_alt_numpad_8:
            with hk.SendLabel(
                id=TC.paladin_holy.name,
                to=self.mode.lbs_by_tc(TC.paladin_holy),
            ):
                # 要点两下, 启动神圣牺牲后自己取消
                act.Paladin.ALL_SPEC_DIVINE_SACRIFICE()
                act.Paladin.ALL_SPEC_DIVINE_SACRIFICE()

        with hk.Hotkey(
            id="Alt Numpad9",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_9)),
        ) as self.hk_alt_numpad_9:
            with hk.SendLabel(
                id=TC.paladin_holy.name,
                to=self.mode.lbs_by_tc(TC.paladin_holy),
            ):
                act.Paladin.ALL_SPEC_AURA_MASTERY()

    def build_hk_alt_numpad_10_cleansing_totem(self):
        with hk.Hotkey(
            id="Alt Numpad10 - 萨满放清毒图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_0)),
        ) as self.hk_alt_numpad_10:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_CLEANSING_TOTEM()

    def build_hk_alt_numpad_11_tremor_totem(self):
        with hk.Hotkey(
            id="Alt Numpad11 - 萨满放战栗图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_11_DIVIDE)),
        ) as self.hk_alt_numpad_11:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_TREMOR_TOTEM()

    def build_hk_alt_numpad_12_earth_binding_totem(self):
        with hk.Hotkey(
            id="Alt Numpad12 - 萨满放地缚图腾",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.NUMPAD_12_MULTIPLY)),
        ) as self.hk_alt_numpad_12:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_EARTHBIND_TOTEM()

    def build_hk_group_08_alt_numpad_1_to_12(self):
        self.build_hk_alt_numpad_1_misdirect_and_tot_focus()
        self.build_hk_alt_numpad_2_aspect_of_pact_or_hawk()
        self.build_hk_alt_numpad_3_aspect_of_viper_or_hawk()
        self.build_hk_alt_numpad_4_all_boomy_star_fall()
        self.build_hk_alt_numpad_5_all_dps_burst()
        self.build_hk_alt_numpad_6_all_dps_burst_and_hero()
        self.build_hk_alt_numpad_7_8_9_first_raid_damage_reduction()
        self.build_hk_alt_numpad_10_cleansing_totem()
        self.build_hk_alt_numpad_11_tremor_totem()
        self.build_hk_alt_numpad_12_earth_binding_totem()

    # -------------------------------------------------------------------------
    # 实现 Ctrl + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
    # -------------------------------------------------------------------------
    __anchor_hk_09_ctrl_1_to_12 = None

    def build_hk_ctrl_numpad_1_silence_shot_focus_target(self):
        with hk.Hotkey(
            id="Ctrl Numpad1 - 射击猎人对焦点的目标释放沉默射击",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_1)),
        ) as self.hk_ctrl_numpad_1:
            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.Hunter.MARKSMAN_SPEC_SILENCING_SHOT()

    def build_hk_ctrl_numpad_2_counter_spell_focus_target(self):
        with hk.Hotkey(
            id="Ctrl Numpad2 - 法师对焦点的目标释放法术反制",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_2)),
        ) as self.hk_ctrl_numpad_2:
            with hk.SendLabel(
                id=TC.mage.name,
                to=self.mode.lbs_by_tc(TC.mage),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO()

    def build_hk_ctrl_numpad_3_aggressive_dispel(self):
        with hk.Hotkey(
            id="Ctrl Numpad3 - 进攻驱散",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_3)),
        ) as self.hk_ctrl_numpad_3:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_PURGE()

            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.Target.TARGET_FOCUS_TARGET()
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Priest.ALL_SPEC_DISPEL_MAGIC()

    def build_hk_ctrl_numpad_4_aoe_fear(self):
        with hk.Hotkey(
            id="Ctrl Numpad4",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_4)),
        ) as self.hk_ctrl_numpad_4:
            with hk.SendLabel(
                id=TC.priest_shadow.name,
                to=self.mode.lbs_by_tc(TC.priest_shadow),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Priest.SHADOW_SPEC_PSYCHIC_HORROR()

    def build_hk_ctrl_numpad_5_typhoon(self):
        with hk.Hotkey(
            id="Ctrl Numpad5",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_5)),
        ) as self.hk_ctrl_numpad_5:
            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Druid.BALANCE_SPEC_TYPHOON_KEY_G()

    def build_hk_ctrl_numpad_6_thunder_storm(self):
        with hk.Hotkey(
            id="Ctrl Numpad6",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_6)),
        ) as self.hk_ctrl_numpad_6:
            with hk.SendLabel(
                id="all_elemental_shaman",
                to=self.mode.lbs_by_tc(TC.shaman_elemental),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ELEMENTAL_SPEC_THUNDER_STORM()

    def build_hk_ctrl_numpad_7_hymn_of_life(self):
        with hk.Hotkey(
            id="Ctrl Numpad7",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_7)),
        ) as self.hk_ctrl_numpad_7:
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Priest.ALL_SPEC_DIVINE_HYMN()

    def build_hk_ctrl_numpad_10_hymn_of_mana(self):
        with hk.Hotkey(
            id="Ctrl Numpad10",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_0)),
        ) as self.hk_ctrl_numpad_10:
            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Priest.ALL_SPEC_HYMN_OF_HOPE()

    def build_hk_ctrl_numpad_11_tank_1_taunt(self):
        with hk.Hotkey(
            id="Ctrl Numpad11 - 主坦克嘲讽",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_11_DIVIDE)),
        ) as self.hk_ctrl_numpad_11:
            with hk.SendLabel(
                id="tank1",
                to=self.mode.lbs_tank1,
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Paladin.PROTECT_SPEC_KEY_Z_HAND_OF_RECKONING()

    def build_hk_ctrl_numpad_12_tank_2_taunt(self):
        with hk.Hotkey(
            id="Ctrl Numpad12 - 副坦克嘲讽",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.NUMPAD_12_MULTIPLY)),
        ) as self.hk_ctrl_numpad_12:
            with hk.SendLabel(
                id="tank2",
                to=self.mode.lbs_tank2,
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.DK.ALL_SPEC_DARK_COMMAND_KEY_Z()

    def build_hk_group_09_ctrl_numpad_1_to_12(self):
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

    # -------------------------------------------------------------------------
    # 实现 Shift + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
    # -------------------------------------------------------------------------
    __anchor_hk_10_shift_numpad_1_to_12 = None

    def build_hk_shift_numpad_1(self):
        with hk.Hotkey(
            id="Shift Numpad1",
            key=KN.SCROLOCK_ON(KN.NUMPAD_SHIFT_1_END),
        ) as self.hk_shift_numpad_1:
            with hk.SendLabel(
                name=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_CALL_OF_THE_ELEMENTS()

    def build_hk_shift_numpad_2(self):
        with hk.Hotkey(
            id="Shift Numpad2",
            key=KN.SCROLOCK_ON(KN.NUMPAD_SHIFT_2_DOWN),
        ) as self.hk_shift_numpad_2:
            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                act.Shaman.ALL_SPEC_TOTEMIC_RECALL()

    def build_hk_group_10(self):
        self.build_hk_shift_numpad_1()
        self.build_hk_shift_numpad_2()

    # -------------------------------------------------------------------------
    # 实现由在主控角色界面下, 用鼠标在团队框架上进行单机来实现治疗的快捷键.
    # 需要配合团队框架 Healbot 插件使用.
    # -------------------------------------------------------------------------
    __anchor_hk_11_heal_bot = None

    """
    下面的这批名字为 ``_build_send_label_...`` 的函数是用于生成 ... 的工厂函数. 
    
    我们为 5 大治疗职业: 奶骑, 奶萨, 奶德, 神/戒牧, 准备了工厂函数, 这些工厂函数定义了
    SendLabel.to 的部分, 留给用户自行定义具体的动作
    """

    def _build_send_label_holy_paladin(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.paladin_holy.name,
            to=self.mode.lbs_by_tc(TC.paladin_holy),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_resto_shaman(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.shaman_resto.name,
            to=self.mode.lbs_by_tc(TC.shaman_resto),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_resto_druid(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.druid_resto.name,
            to=self.mode.lbs_by_tc(TC.druid_resto),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_disco_priest(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.priest_disco.name,
            to=self.mode.lbs_by_tc(TC.priest_disco),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_holy_priest(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.priest_holy.name,
            to=self.mode.lbs_by_tc(TC.priest_holy),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_tank(self):
        with hk.SendLabel(
            id=TC.tank.name,
            to=self.mode.lbs_by_tc(TC.tank),
        ) as send_label:
            hk.Key(id=KN.KEY_2)
            return send_label

    def _build_send_label_shaman(self, funcs: T.List[callable]):
        with hk.SendLabel(
            id=TC.shaman.name,
            to=self.mode.lbs_by_tc(TC.shaman),
        ) as send_label:
            for func in funcs:
                func()
            return send_label

    def _build_send_label_dps(self):
        with hk.SendLabel(
            id=TC.dps.name,
            to=self.mode.lbs_by_tc(TC.dps),
        ) as send_label:
            act.Target.TARGET_FOCUS_TARGET()
            hk.Key(key=KN.KEY_2)
            return send_label

    def _build_send_label_non_shaman_dps(self):
        """
        点击 Healbot 的时候, 所有 DPS 继续攻击焦点的目标. 唯独 增强萨满 和 元素萨满 例外.
        虽然它们是 DPS 职业, 但是依然要跟其他治疗一样, 对团队框架目标使用治疗链.
        """
        lbs_dps = self.mode.lbs_by_tc(TC.dps)
        lbs_shaman_non_resto = self.mode.lbs_by_tc(TC.shaman_non_resto)
        to = list(set(lbs_dps).difference(lbs_shaman_non_resto))
        to.sort()
        with hk.SendLabel(
            id="non_shaman_dps",
            to=to,
        ) as send_label:
            act.Target.TARGET_FOCUS_TARGET()
            hk.Key(key=KN.KEY_2)
            return send_label

    def build_hk_healbot_small_heal(self):
        with hk.Hotkey(
            id="Healbot Small Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_small_heal:
            self._build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_RIGHT_CLICK_FLASH_OF_LIGHT,
            ])
            self._build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_RIPTIDE_RIGHT_CLICK,
            ])
            self._build_send_label_resto_druid([
                act.Druid.HEAL_BOT_LEFT_CLICK_REJUVENATION,
            ])
            self._build_send_label_disco_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_POWER_WORD_SHIELD,
            ])
            self._build_send_label_holy_priest([
                act.Priest.HEAL_BOT_DISCO_AND_HOLY_SPEC_FLASH_HEAL,
            ])
            self._build_send_label_tank()
            self._build_send_label_dps()

    def build_hk_healbot_big_heal(self):
        with hk.Hotkey(
            id="Healbot Big Heal",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.MOUSE_RButton)),
        ) as self.hk_healbot_big_heal:
            self._build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_LEFT_CLICK_HOLY_LIGHT,
            ]),
            self._build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_HEALING_WAVE_LEFT_CLICK,
            ]),
            self._build_send_label_resto_druid([
                act.Druid.HEAL_BOT_RIGHT_CLICK_NOURISH,
            ]),
            self._build_send_label_disco_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_POWER_WORD_SHIELD,
            ]),
            self._build_send_label_holy_priest([
                act.Priest.HEAL_BOT_DISCO_AND_HOLY_SPEC_FLASH_HEAL,
            ]),
            self._build_send_label_tank(),
            self._build_send_label_dps(),

    def build_hk_healbot_aoe_heal(self):
        with hk.Hotkey(
            id="Healbot Aoe Heal",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.MOUSE_LButton)),
        ) as self.hk_healbot_aoe_heal:
            self._build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_LEFT_CLICK_HOLY_LIGHT,
            ]),
            self._build_send_label_shaman([
                act.Shaman.HEAL_BOT_CHAIN_HEAL_MIDDLE_CLICK,
            ]),
            self._build_send_label_resto_druid([
                act.Druid.HEAL_BOT_SHIFT_LEFT_WILD_GROWTH,
            ]),
            self._build_send_label_disco_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_POWER_WORD_SHIELD,
            ]),
            self._build_send_label_holy_priest([
                act.Priest.HEAL_BOT_HOLY_SPEC_CIRCLE_OF_HEAL,
            ]),
            self._build_send_label_tank(),
            self._build_send_label_non_shaman_dps(),

    def build_hk_healbot_dispel(self):
        with hk.Hotkey(
            id="Healbot Dispel",
            key=KN.SCROLOCK_ON(KN.MOUSE_MButton),
        ) as self.hk_healbot_dispel:
            self._build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_CLEANSE,
            ]),
            self._build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_CLEANSE_CTRL_LEFT_CLICK,
            ]),
            self._build_send_label_resto_druid([
                act.Druid.HEAL_BOT_CTRL_LEFT_REMOVE_CURSE,
            ]),
            self._build_send_label_disco_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_DISPEL_MAGIC,
            ]),
            self._build_send_label_holy_priest([
                act.Priest.HEAL_BOT_ALL_SPEC_DISPEL_MAGIC,
            ]),
            self._build_send_label_tank(),
            self._build_send_label_non_shaman_dps(),

    def build_hk_group_11_healbot(self):
        self.build_hk_healbot_small_heal()
        self.build_hk_healbot_big_heal()
        self.build_hk_healbot_aoe_heal()
        self.build_hk_healbot_dispel()

    # -------------------------------------------------------------------------
    # 实现使用图形界面上的按钮, 替代一些不常用, 或是紧急情况需要用到的快捷键,
    # 避免了记忆复杂快捷键的麻烦
    # -------------------------------------------------------------------------
    __anchor_control_panel = None

    # def build_control_panel(self):
    #     WIDTH = 36
    #     HEIGHT = 36
    #
    #     with hk.Command(name="AutoExec") as self.cmd_auto_exec:
    #         with hk.CreatePanel(name="MBControlPanel", x=0, y=60, width=120, height=960) as main_panel:
    #             def set_hotkey_or_command(
    #                 button,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 if hotkey is not None:
    #                     hk.SetButtonHotkey(
    #                         button=button.name,
    #                         hotkey=hotkey,
    #                     )
    #                 if command is not None:
    #                     hk.SetButtonCommand(
    #                         button=button.name,
    #                         command=command,
    #                         args=command_args,
    #                     )
    #
    #             def create_button(
    #                 name: str,
    #                 text: str,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreateButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     width=WIDTH,
    #                     height=HEIGHT,
    #                     text=text,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             def create_picture_button(
    #                 name: str,
    #                 file: str,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreatePictureButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     file=file,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             def create_colored_button(
    #                 name: str,
    #                 bkcolor: str,
    #                 textcolor: str = "000000",
    #                 text: T.Optional[str] = None,
    #                 hotkey: T.Optional[hk.Hotkey] = None,
    #                 command: T.Optional[hk.Command] = None,
    #                 command_args: T.Optional[tuple] = None,
    #             ):
    #                 button = hk.CreateColoredButton(
    #                     name=name,
    #                     x=0,
    #                     y=0,
    #                     width=WIDTH,
    #                     height=HEIGHT,
    #                     bkcolor=f"0x{bkcolor}",
    #                     textcolor=f"0x{textcolor}",
    #                     text=text,
    #                 )
    #                 hk.AddButtonToPanel(
    #                     button=button.name,
    #                     panel=main_panel.name,
    #                 )
    #                 set_hotkey_or_command(button, hotkey, command, command_args)
    #
    #             create_picture_button(
    #                 name="ButtonA01",
    #                 file=Icons.wow,
    #                 command=self.cmd_launch_and_rename_all_game_client,
    #             )
    #
    #             create_picture_button(
    #                 name="ButtonA02",
    #                 file=Icons.log_in,
    #                 command=self.cmd_batch_login,
    #             )
    #
    #             create_picture_button(
    #                 name="ButtonA03",
    #                 file=Icons.resize_window,
    #                 command=self.cmd_center_overlap_layout,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Alt + Numpad 1 - 12
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12a",
    #                 bkcolor="E75638",
    #                 text="Alt"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarAlt1To12c",
    #                 bkcolor="E75638",
    #                 text="1-12"
    #             )
    #
    #             create_picture_button(
    #                 name="Alt1",
    #                 file=Icons.ability_hunter_misdirection,
    #                 hotkey=self.hk_alt_numpad_1,
    #             )
    #             create_picture_button(
    #                 name="Alt2",
    #                 file=Icons.ability_mount_whitetiger,
    #                 hotkey=self.hk_alt_numpad_2,
    #             )
    #             create_picture_button(
    #                 name="Alt3",
    #                 file=Icons.ability_hunter_aspectoftheviper,
    #                 hotkey=self.hk_alt_numpad_3,
    #             )
    #             create_picture_button(
    #                 name="Alt4",
    #                 file=Icons.ability_druid_starfall,
    #                 hotkey=self.hk_alt_numpad_4,
    #             )
    #             create_picture_button(
    #                 name="Alt5",
    #                 file=Icons.spell_nature_wispheal,
    #                 hotkey=self.hk_alt_numpad_5,
    #             )
    #             create_picture_button(
    #                 name="Alt6",
    #                 file=Icons.spell_nature_bloodlust,
    #                 hotkey=self.hk_alt_numpad_6,
    #             )
    #             create_picture_button(
    #                 name="Alt7",
    #                 file=Icons.spell_holy_powerwordbarrier,
    #                 hotkey=self.hk_alt_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="Alt8",
    #                 file=Icons.spell_holy_powerwordbarrier,
    #                 hotkey=self.hk_alt_numpad_8,
    #             )
    #             create_picture_button(
    #                 name="Alt9",
    #                 file=Icons.spell_holy_auramastery,
    #                 hotkey=self.hk_alt_numpad_9,
    #             )
    #             create_picture_button(
    #                 name="Alt10",
    #                 file=Icons.spell_nature_diseasecleansingtotem,
    #                 hotkey=self.hk_alt_numpad_10,
    #             )
    #             create_picture_button(
    #                 name="Alt11",
    #                 file=Icons.spell_nature_tremortotem,
    #                 hotkey=self.hk_alt_numpad_11,
    #             )
    #             create_picture_button(
    #                 name="Alt12",
    #                 file=Icons.spell_nature_strengthofearthtotem02,
    #                 hotkey=self.hk_alt_numpad_12,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Ctrl + Numpad 1 - 12
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12a",
    #                 bkcolor="E75638",
    #                 text="Ctrl"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarCtrl1To12c",
    #                 bkcolor="E75638",
    #                 text="1-12"
    #             )
    #
    #             create_picture_button(
    #                 name="CtrlNumpad1",
    #                 file=Icons.ability_theblackarrow,
    #                 hotkey=self.hk_ctrl_numpad_1,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad2",
    #                 file=Icons.spell_frost_iceshock,
    #                 hotkey=self.hk_ctrl_numpad_2,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad3",
    #                 file=Icons.spell_holy_dispelmagic,
    #                 hotkey=self.hk_ctrl_numpad_3,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad4",
    #                 file=Icons.spell_shadow_psychicscream,
    #                 hotkey=self.hk_ctrl_numpad_4,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad5",
    #                 file=Icons.ability_druid_typhoon,
    #                 hotkey=self.hk_ctrl_numpad_5,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad6",
    #                 file=Icons.spell_shaman_thunderstorm,
    #                 hotkey=self.hk_ctrl_numpad_6,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad7",
    #                 file=Icons.spell_holy_divinehymn,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad8",
    #                 file=Icons.spell_nature_tranquility,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad9",
    #                 file=Icons.spell_nature_tranquility,
    #                 hotkey=self.hk_ctrl_numpad_7,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad10",
    #                 file=Icons.spell_holy_symbolofhope,
    #                 hotkey=self.hk_ctrl_numpad_10,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad11",
    #                 file=Icons.spell_holy_unyieldingfaith,
    #                 hotkey=self.hk_ctrl_numpad_11,
    #             )
    #             create_picture_button(
    #                 name="CtrlNumpad12",
    #                 file=Icons.spell_nature_shamanrage,
    #                 hotkey=self.hk_ctrl_numpad_12,
    #             )
    #
    #             # -------------------------------------------------------------
    #             # Shift + Numpad 1 - 9
    #             # -------------------------------------------------------------
    #             create_colored_button(
    #                 name="ButtonBarShift1To9a",
    #                 bkcolor="E75638",
    #                 text="Shift"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarShift1To9b",
    #                 bkcolor="E75638",
    #                 text="+Num"
    #             )
    #             create_colored_button(
    #                 name="ButtonBarShift1To9c",
    #                 bkcolor="E75638",
    #                 text="1-9"
    #             )
    #
    #             hk.SetPanelLayout(
    #                 panel=main_panel.name,
    #                 row_length=3,
    #                 margin=1,
    #                 button_width=36,
    #                 button_height=36,
    #             )
    #
    #             hk.TargetWin(window=main_panel.name)
    #             hk.AlwaysOnTop()

    def build_control_panel(self):
        WIDTH = 24
        HEIGHT = 24

        with hk.Command(name="AutoExec") as self.cmd_auto_exec:
            with hk.CreatePanel(name="MBControlPanel", x=0, y=60, width=120, height=960) as main_panel:
                # Define three temp utility function
                def set_hotkey_or_command(
                    button,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    if hotkey is not None:
                        hk.SetButtonHotkey(
                            button=button.name,
                            hotkey=hotkey,
                        )
                    if command is not None:
                        hk.SetButtonCommand(
                            button=button.name,
                            command=command,
                            args=command_args,
                        )

                def create_button(
                    name: str,
                    text: str,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreateButton(
                        name=name,
                        x=0,
                        y=0,
                        width=WIDTH,
                        height=HEIGHT,
                        text=text,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                def create_picture_button(
                    name: str,
                    file: str,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreatePictureButton(
                        name=name,
                        x=0,
                        y=0,
                        file=file,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                def create_colored_button(
                    name: str,
                    bkcolor: str,
                    textcolor: str = "000000",
                    text: T.Optional[str] = None,
                    hotkey: T.Optional[hk.Hotkey] = None,
                    command: T.Optional[hk.Command] = None,
                    command_args: T.Optional[tuple] = None,
                ):
                    button = hk.CreateColoredButton(
                        name=name,
                        x=0,
                        y=0,
                        width=WIDTH,
                        height=HEIGHT,
                        bkcolor=f"0x{bkcolor}",
                        textcolor=f"0x{textcolor}",
                        text=text,
                    )
                    hk.AddButtonToPanel(
                        button=button.name,
                        panel=main_panel.name,
                    )
                    set_hotkey_or_command(button, hotkey, command, command_args)

                create_picture_button(
                    name="ButtonLaunchAndRenameAllGameClient",
                    file=Icons.wow,
                    command=self.cmd_launch_and_rename_all_game_client,
                )

                create_picture_button(
                    name="ButtonBatchLogin",
                    file=Icons.log_in,
                    command=self.cmd_batch_login_and_enter_game,
                )

                create_picture_button(
                    name="ButtonResizeWindow",
                    file=Icons.resize_window,
                    command=self.cmd_center_overlap_layout,
                )

                create_picture_button(
                    name="ButtonLogOut",
                    file=Icons.log_out,
                    hotkey=self.hk_batch_logout,
                )

                create_picture_button(
                    name="ButtonVolumeDown",
                    file=Icons.vol_down,
                    hotkey=self.hk_volumn_down,
                )

                counter = 0
                index_mapper = dict()
                for window, account in self.mode.login_window_and_account_pairs:
                    index_mapper[window.index] = (window, account)
                for i in range(1, 1 + 25):
                    if i in index_mapper:
                        window, account = index_mapper[i]
                        create_button(
                            name=f"ButtonLogin{str(i).zfill(2)}",
                            text=window.label,
                            command=self.cmd_enter_username_and_password,
                            command_args=(
                                window.title,
                                account.username,
                                account.password,
                            )
                        )
                    else:
                        create_button(
                            name=f"ButtonLogin{str(i).zfill(2)}",
                            text="NA",
                        )

                create_picture_button(
                    name="RDFConfirmRoleAndEnterDungeon",
                    file=Icons.spell_holy_summonchampion,
                    hotkey=self.hk_rdf_confirm_role_and_enter_dungeon,
                )

                # -------------------------------------------------------------
                # Login
                # -------------------------------------------------------------
                # for self.mode.

                # -------------------------------------------------------------
                # Alt + Numpad 1 - 12
                # -------------------------------------------------------------
                for id, text in enumerate([
                    "Alt",
                    "+",
                    "Num",
                    "Pad",
                    "1-12",
                ], start=1):
                    create_colored_button(
                        name=f"ButtonBarAlt1To12B{id}",
                        bkcolor="E75638",
                        text=text
                    )

                create_picture_button(
                    name="Alt1",
                    file=Icons.ability_hunter_misdirection,
                    hotkey=self.hk_alt_numpad_1,
                )
                create_picture_button(
                    name="Alt2",
                    file=Icons.ability_mount_whitetiger,
                    hotkey=self.hk_alt_numpad_2,
                )
                create_picture_button(
                    name="Alt3",
                    file=Icons.ability_hunter_aspectoftheviper,
                    hotkey=self.hk_alt_numpad_3,
                )
                create_button(
                    name=f"Alt3B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt3B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt4",
                    file=Icons.ability_druid_starfall,
                    hotkey=self.hk_alt_numpad_4,
                )
                create_picture_button(
                    name="Alt5",
                    file=Icons.spell_nature_wispheal,
                    hotkey=self.hk_alt_numpad_5,
                )
                create_picture_button(
                    name="Alt6",
                    file=Icons.spell_nature_bloodlust,
                    hotkey=self.hk_alt_numpad_6,
                )
                create_button(
                    name=f"Alt6B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt6B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt7",
                    file=Icons.spell_holy_powerwordbarrier,
                    hotkey=self.hk_alt_numpad_7,
                )
                create_picture_button(
                    name="Alt8",
                    file=Icons.spell_holy_powerwordbarrier,
                    hotkey=self.hk_alt_numpad_8,
                )
                create_picture_button(
                    name="Alt9",
                    file=Icons.spell_holy_auramastery,
                    hotkey=self.hk_alt_numpad_9,
                )
                create_button(
                    name=f"Alt9B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt9B2",
                    text="NA",
                )

                create_picture_button(
                    name="Alt10",
                    file=Icons.spell_nature_diseasecleansingtotem,
                    hotkey=self.hk_alt_numpad_10,
                )
                create_picture_button(
                    name="Alt11",
                    file=Icons.spell_nature_tremortotem,
                    hotkey=self.hk_alt_numpad_11,
                )
                create_picture_button(
                    name="Alt12",
                    file=Icons.spell_nature_strengthofearthtotem02,
                    hotkey=self.hk_alt_numpad_12,
                )
                create_button(
                    name=f"Alt12B1",
                    text="NA",
                )
                create_button(
                    name=f"Alt12B2",
                    text="NA",
                )

                # -------------------------------------------------------------
                # Ctrl + Numpad 1 - 12
                # -------------------------------------------------------------
                for id, text in enumerate([
                    "Ctrl",
                    "+",
                    "Num",
                    "Pad",
                    "1-12",
                ], start=1):
                    create_colored_button(
                        name=f"ButtonBarCtrl1To12B{id}",
                        bkcolor="E75638",
                        text=text
                    )

                create_picture_button(
                    name="CtrlNumpad1",
                    file=Icons.ability_theblackarrow,
                    hotkey=self.hk_ctrl_numpad_1,
                )
                create_picture_button(
                    name="CtrlNumpad2",
                    file=Icons.spell_frost_iceshock,
                    hotkey=self.hk_ctrl_numpad_2,
                )
                create_picture_button(
                    name="CtrlNumpad3",
                    file=Icons.spell_holy_dispelmagic,
                    hotkey=self.hk_ctrl_numpad_3,
                )
                create_button(
                    name=f"Ctrl3B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl3B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad4",
                    file=Icons.spell_shadow_psychicscream,
                    hotkey=self.hk_ctrl_numpad_4,
                )
                create_picture_button(
                    name="CtrlNumpad5",
                    file=Icons.ability_druid_typhoon,
                    hotkey=self.hk_ctrl_numpad_5,
                )
                create_picture_button(
                    name="CtrlNumpad6",
                    file=Icons.spell_shaman_thunderstorm,
                    hotkey=self.hk_ctrl_numpad_6,
                )
                create_button(
                    name=f"Ctrl6B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl6B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad7",
                    file=Icons.spell_holy_divinehymn,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_picture_button(
                    name="CtrlNumpad8",
                    file=Icons.spell_nature_tranquility,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_picture_button(
                    name="CtrlNumpad9",
                    file=Icons.spell_nature_tranquility,
                    hotkey=self.hk_ctrl_numpad_7,
                )
                create_button(
                    name=f"Ctrl9B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl9B2",
                    text="NA",
                )

                create_picture_button(
                    name="CtrlNumpad10",
                    file=Icons.spell_holy_symbolofhope,
                    hotkey=self.hk_ctrl_numpad_10,
                )
                create_picture_button(
                    name="CtrlNumpad11",
                    file=Icons.spell_holy_unyieldingfaith,
                    hotkey=self.hk_ctrl_numpad_11,
                )
                create_picture_button(
                    name="CtrlNumpad12",
                    file=Icons.spell_nature_shamanrage,
                    hotkey=self.hk_ctrl_numpad_12,
                )
                create_button(
                    name=f"Ctrl12B1",
                    text="NA",
                )
                create_button(
                    name=f"Ctrl12B2",
                    text="NA",
                )

                # # -------------------------------------------------------------
                # # Shift + Numpad 1 - 9
                # # -------------------------------------------------------------
                # create_colored_button(
                #     name="ButtonBarShift1To9a",
                #     bkcolor="E75638",
                #     text="Shift"
                # )
                # create_colored_button(
                #     name="ButtonBarShift1To9b",
                #     bkcolor="E75638",
                #     text="+Num"
                # )
                # create_colored_button(
                #     name="ButtonBarShift1To9c",
                #     bkcolor="E75638",
                #     text="1-9"
                # )

                hk.SetPanelLayout(
                    panel=main_panel.name,
                    row_length=5,
                    margin=1,
                    button_width=24,
                    button_height=24,
                )

                hk.TargetWin(window=main_panel.name)
                hk.AlwaysOnTop()
