# -*- coding: utf-8 -*-

"""
实现各个职业的特定应用场景技能的快捷键. 例如鸟德星落, 鸟德吹风, 法师打断, 等等.
"""

import typing as T
import itertools

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


class HotkeyGroup07UtilitySpellMixin:
    def build_hk_domino_action_bar_5(self: "HknScript"):
        # with hk.Hotkey(
        #     id="Alt F1",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.F1)),
        # ) as self.hk_alt_f1:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt F2",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.F2)),
        # ) as self.hk_alt_f2:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift F1",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.F1)),
        # ) as self.hk_shift_f1:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift F1",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.F1)),
        # ) as self.hk_shift_f1:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift F2",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.F2)),
        # ) as self.hk_shift_f2:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift C",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.C)),
        # ) as self.hk_shift_c:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift R",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.R)),
        # ) as self.hk_shift_r:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift F",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.F)),
        # ) as self.hk_shift_f:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift G",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.G)),
        # ) as self.hk_shift_g:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        # with hk.Hotkey(
        #     id="Shift Tab",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.TAB)),
        # ) as self.hk_shift_tab:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_by_tc(TC.shaman),
        #     ):
        #         hk.Key.trigger()

        # with hk.Hotkey(
        #     id="Ctrl E",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.E)),
        # ) as self.hk_ctrl_e:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Ctrl R",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.R)),
        # ) as self.hk_ctrl_r:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Ctrl F",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.F)),
        # ) as self.hk_ctrl_f:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        pass

    def build_hk_domino_action_bar_4(self: "HknScript"):
        # with hk.Hotkey(
        #     id="MButton",
        #     key=KN.SCROLOCK_ON(KN.MOUSE_MButton),
        # ) as self.hk_middle_click:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift MButton",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.MOUSE_MButton)),
        # ) as self.hk_shift_middle_click:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt MButton",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.MOUSE_MButton)),
        # ) as self.hk_alt_middle_click:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        with hk.Hotkey(
            id="Ctrl + `",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.OEM3_WAVE_OR_BACK_QUOTE)),
        ) as self.hk_ctrl_oem3_wave_dismount:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.general.MOUNT_DOWN_MACRO_CTRL_OEM3_WAVE()

        # with hk.Hotkey(
        #     id="Shift + `",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.OEM3_WAVE_OR_BACK_QUOTE)),
        # ) as self.hk_shift_oem3_wave:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + `",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.OEM3_WAVE_OR_BACK_QUOTE)),
        # ) as self.hk_alt_oem3_wave:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + A",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.A)),
        # ) as self.hk_alt_a:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + S",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.S)),
        # ) as self.hk_alt_s:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + D",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.D)),
        # ) as self.hk_alt_d:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + E",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.E)),
        # ) as self.hk_alt_e:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + R",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.R)),
        # ) as self.hk_alt_r:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + F",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.F)),
        # ) as self.hk_alt_f:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        with hk.Hotkey(
            id="Alt Shift F - 鸟德轮流放星落",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_(KN.F)),
        ) as self.hk_alt_shift_f_take_turn_star_fall:
            for label in self.mode.lbs_by_tc(TC.druid_balance):
                with hk.Toggle():
                    with hk.SendLabel(to=[label, ]):
                        act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                        act.druid_balance.Starfall()


    def build_hk_domino_action_bar_3(self: "HknScript"):
        # with hk.Hotkey(
        #     id="Shift + Z",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.Z)),
        # ) as self.hk_shift_z:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift + T",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.T)),
        # ) as self.hk_shift_t:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Shift + X",
        #     key=KN.SCROLOCK_ON(KN.SHIFT_(KN.X)),
        # ) as self.hk_shift_x:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        # 所有人使用陆地坐骑
        with hk.Hotkey(
            id="Ctrl + Z",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.Z)),
        ) as self.hk_ctrl_z_use_land_mount:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.general.LAND_MOUNT_SPELL_KEY_CTRL_Z()

        # 吃食物
        with hk.Hotkey(
            id="Ctrl + T",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.T)),
        ) as self.hk_ctrl_t_eat_and_drink_food:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.general.EAT_FOOD_KEY_CTRL_T()

        # with hk.Hotkey(
        #     id="Ctrl + G",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.G)),
        # ) as self.hk_ctrl_g:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        # with hk.Hotkey(
        #     id="Ctrl + X",
        #     key=KN.SCROLOCK_ON(KN.CTRL_(KN.X)),
        # ) as self.hk_ctrl_x:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + Z",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.Z)),
        # ) as self.hk_alt_z:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()
        #
        # with hk.Hotkey(
        #     id="Alt + T",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.T)),
        # ) as self.hk_alt_t:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        with hk.Hotkey(
            id="Alt + G - 所有鸟德轮流放台风, 推波击退",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.G)),
        ) as self.hk_alt_g_druid_typhoon:
            for label in self.mode.lbs_by_tc(TC.druid_balance):
                with hk.Toggle():
                    with hk.SendLabel(
                        to=[label,],
                    ):
                        act.druid_balance.Typhoon()

        with hk.Hotkey(
            id="Alt + X - 所有 AOE 职业放区域选定 AOE 技能, 例如法师暴风雪, DK死亡凋零",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.X)),
        ) as self.hk_alt_x_aoe_target_location:
            with hk.SendLabel(
                id=TC.dk.name,
                to=self.mode.lbs_by_tc(TC.dk),
            ):
                # act.General.ESC()
                act.dk.Death_and_Decay()

            with hk.SendLabel(
                id=TC.hunter.name,
                to=self.mode.lbs_by_tc(TC.hunter),
            ):
                # act.General.ESC()
                act.hunter.Volley()

            with hk.SendLabel(
                id=TC.druid_balance.name,
                to=self.mode.lbs_by_tc(TC.druid_balance),
            ):
                # act.General.ESC()
                act.druid_balance.Hurricane()

            with hk.SendLabel(
                id=TC.warlock.name,
                to=self.mode.lbs_by_tc(TC.warlock),
            ):
                # act.General.ESC()
                act.warlock.Rain_of_Fire()

            with hk.SendLabel(
                id=TC.mage.name,
                to=self.mode.lbs_by_tc(TC.mage),
            ):
                # act.General.ESC()
                act.mage.Blizzard()

    def build_hk_domino_action_bar_2(self: "HknScript"):
        # with hk.Hotkey(
        #     id="R - 能打断的职业打断",
        #     key=KN.SCROLOCK_ON(KN.ALT_(KN.G)),
        # ) as self.hk_alt_g_druid_typhoon:
        #     with hk.SendLabel(
        #         id=TC.paladin_protect.name,
        #         to=self.mode.lbs_by_tc(TC.paladin_protect),
        #     ):
        #         hk.Key(key=KN.R)
        #
        #
        # _hk_r_actions = [
        #     # paladin
        #     SendLabel(
        #         name=TC.paladin_protect.name,
        #         to=self.mode.lbs_by_tc(TC.paladin_protect),
        #         actions=[
        #             Key(name=KN.R),
        #         ]
        #     ),
        #     SendLabel(
        #         name=TC.paladin_holy.name,
        #         to=self.mode.lbs_by_tc(TC.paladin_holy),
        #         actions=[
        #             act.Paladin.HOLY_SPEC_KEY_R_FOCUS_JUDGEMENT,
        #         ]
        #     ),
        #     # death knight
        #     SendLabel(
        #         name=TC.dk_tank.name,
        #         to=self.mode.lbs_by_tc(TC.dk_tank),
        #         actions=[
        #             act.DK.ALL_SPEC_MIND_FREEZE_KEY_R,
        #         ]
        #     ),
        #     SendLabel(
        #         name=TC.dk_dps.name,
        #         to=self.mode.lbs_by_tc(TC.dk_dps),
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             act.DK.ALL_SPEC_MIND_FREEZE_KEY_R,
        #         ]
        #     ),
        #     # hunter
        #     SendLabel(
        #         name=TC.hunter_marksman.name,
        #         to=self.mode.lbs_by_tc(TC.hunter_marksman),
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             act.Hunter.MARKSMAN_SPEC_DPS_ROTATE_MACRO,
        #         ]
        #     ),
        #     # shaman
        #     SendLabel(
        #         name=TC.shaman.name,
        #         to=self.mode.lbs_by_tc(TC.shaman),
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             act.Shaman.ALL_SPEC_WIND_SHEAR_MACRO,
        #         ]
        #     ),
        #
        #     # mage
        #     SendLabel(
        #         name=TC.mage.name,
        #         to=self.mode.lbs_by_tc(TC.mage),
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO,
        #         ]
        #     ),
        # ]
        #
        # special_labels = union_list(*[
        #     sl.to
        #     for sl in _hk_r_actions
        # ])
        #
        # regular_tank_labels = difference_list(
        #     self.mode.lbs_by_tc(TC.tank),
        #     special_labels,
        # )
        #
        # regular_dps_labels = difference_list(
        #     self.mode.lbs_by_tc(TC.dps),
        #     special_labels,
        # )
        #
        # regular_healer_labels = difference_list(
        #     self.mode.lbs_by_tc(TC.healer),
        #     special_labels,
        # )
        #
        # _hk_r_actions.extend([
        #     SendLabel(
        #         name="other_tank",
        #         to=regular_tank_labels,
        #         actions=[
        #             Key(name=KN.KEY_2),
        #         ]
        #     ),
        #     SendLabel(
        #         name="other_dps",
        #         to=regular_dps_labels,
        #         actions=[
        #             act.Target.TARGET_FOCUS_TARGET,
        #             Key(name=KN.KEY_3),
        #         ]
        #     ),
        #     SendLabel(
        #         name="other_healer",
        #         to=regular_healer_labels,
        #         actions=[
        #             act.Target.TARGET_FOCUS,
        #             Key(name=KN.KEY_3),
        #         ]
        #     ),
        # ])

        """
        创建轮流打断快捷键.

        由于萨满的打断技能为远程, 并且 CD 最短只有 6 秒, 所以我们主要围绕萨满进行.
        核心思想是将 1 个近战和 1 个远程分为一组, 没有近战远程就可以了. 然后以
        萨满 -> 其他 -> 萨满 -> 其他 这样的顺序打断. 例如其他可以是打断技能 CD 较长的法师
        或猎人.
        """
        with hk.Hotkey(
            id="R - 能打断的职业打断",
            key=KN.SCROLOCK_ON(KN.R),
        ) as self.hk_r_interrupt:
            # 近战打断, CD 都是 10 秒
            # warrior_lbs = self.mode.lbs_by_tc(TC.warrior)
            # rogue_lbs = self.mode.lbs_by_tc(TC.rogue)
            dk_lbs = self.mode.lbs_by_tc(TC.dk)

            # 远程打断
            shaman_non_resto_lbs = self.mode.lbs_by_tc(TC.shaman_non_resto)  # 萨满打断技能 CD 很短, 只有 6 秒
            shaman_resto_lbs = self.mode.lbs_by_tc(TC.shaman_resto)  # 萨满打断技能 CD 很短, 只有 6 秒
            shaman_lbs = shaman_non_resto_lbs + shaman_resto_lbs
            mage_lbs = self.mode.lbs_by_tc(TC.mage)  # 法师反制 CD 24 秒
            marksman_hunter_lbs = self.mode.lbs_by_tc(TC.hunter_marksman)  # 猎人 沉默射击 CD 24 秒
            # shadow_priest_lbs = self.mode.lbs_by_tc(TC.priest_shadow) # 不是每一个牧师都会点出沉默

            n_melee = len(dk_lbs)
            n_shaman = len(shaman_lbs)
            n_range = len(mage_lbs) + len(marksman_hunter_lbs)

            melee_pairs = [
                (label, act.dk.Mind_Freeze) for label in dk_lbs
            ]
            shaman_pairs = [
                (label, act.shaman.Wind_Shear) for label in shaman_lbs
            ]
            range_pairs = (
                [(label, act.mage.Counterspell) for label in mage_lbs]
                + [(label, act.hunter_marksmanship.Silencing_Shot) for label in marksman_hunter_lbs]
            )

            loop_melee = itertools.cycle(melee_pairs)
            loop_range = itertools.cycle(range_pairs)

            # 没有萨满的情况:
            if len(shaman_lbs) == 0:
                pass
            # 有一个 萨满的情况
            elif len(shaman_lbs) == 1:
                shaman_label, shaman_key = shaman_lbs[0], act.shaman.Wind_Shear
                # 如果没有其他远程打断角色, 那么每次都是这个萨满来打断
                if n_range == 0:
                    with hk.SendLabel(to=[shaman_label, ]):
                        shaman_key()
                # 如果有少于 2 个其他远程打断角色, 那么打断循环就是:
                # 角色 1 -> 萨满 -> 角色 2 -> 萨满 -> 角色 1 -> 萨满 -> ...
                elif len(range_pairs) <= 2:
                    for label, key in range_pairs:
                        with hk.Toggle():
                            with hk.SendLabel(to=[label, ]):
                                key()
                        with hk.Toggle():
                            with hk.SendLabel(to=[shaman_label, ]):
                                shaman_key()
                # 如果有多于 2 个 (3 个或 3 个以上) 其他远程打断角色, 那么打断循环就是:
                # 角色 1 和 萨满 -> 角色 2 和 萨满 -> 角色 3 和 萨满 -> 角色 1 和 萨满 -> ...
                else:
                    for label, key in range_pairs:
                        with hk.Toggle():
                            with hk.SendLabel(to=[label, ]):
                                key()
                            with hk.SendLabel(to=[shaman_label, ]):
                                shaman_key()
            # 有两个 萨满的情况, 两个萨满配合其他人轮流来
            elif len(shaman_lbs) >= 2:
                # 如果有其他远程打断角色, 那么这两个萨满还是轮流来
                # 但是穿插其他远程打断角色 以及 近战打断角色
                for label, key in shaman_pairs:
                    with hk.Toggle():
                        with hk.SendLabel(to=[label, ]):
                            key()
                        if n_melee:
                            label_melee, key_melee = next(loop_melee)
                            with hk.SendLabel(to=[label_melee, ]):
                                key_melee()
                        if n_range:
                            label_range, key_range = next(loop_range)
                            with hk.SendLabel(to=[label_range, ]):
                                key_range()
                # 重复两次是因为我们有可能 近战 / 远程 打断的数量多于萨满
                for label, key in shaman_pairs:
                    with hk.Toggle():
                        with hk.SendLabel(to=[label, ]):
                            key()
                        if n_melee:
                            label_melee, key_melee = next(loop_melee)
                            with hk.SendLabel(to=[label_melee, ]):
                                key_melee()
                        if n_range:
                            label_range, key_range = next(loop_range)
                            with hk.SendLabel(to=[label_range, ]):
                                key_range()

        # 创建团队随机驱散快捷键
        # paladin put cleansing skill on Action Bar Key T
        # shaman put curse toxin skill on Action Bar Key on T
        # druid put remove curse skill on Action Bar Key on T
        # mage put remove curse skill on Action Bar Key on T
        # priest put dispel magic skill on Action Bar Key on T
        with hk.Hotkey(
            id="T - 所有驱散职业随机选择团队成员驱散",
            key=KN.SCROLOCK_ON(KN.T),
        ) as self.hk_t_dispel_raid:
            with hk.SendLabel(
                id=TC.dispeler.name,
                to=self.mode.lbs_by_tc(TC.dispeler),
            ):
                act.target.TARGET_RAID()
                hk.Key.trigger()

        # with hk.Hotkey(
        #     id="Z",
        #     key=KN.SCROLOCK_ON(KN.Z),
        # ) as self.hk_z:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        # with hk.Hotkey(
        #     id="G",
        #     key=KN.SCROLOCK_ON(KN.G),
        # ) as self.hk_g:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

        with hk.Hotkey(
            id="Alt Shift G - 鸟德轮流放台风",
            key=KN.SCROLOCK_ON(KN.ALT_SHIFT_(KN.G)),
        ) as self.hk_alt_shift_g_take_turn_typhoon:
            for label in self.mode.lbs_by_tc(TC.druid_balance):
                with hk.Toggle():
                    with hk.SendLabel(to=[label, ]):
                        act.general.STOP_CASTING_KEY_OEM1_SEMICOLUMN()
                        act.druid_balance.Typhoon()

        # with hk.Hotkey(
        #     id="X",
        #     key=KN.SCROLOCK_ON(KN.X),
        # ) as self.hk_x:
        #     with hk.SendLabel(
        #         to=self.mode.lbs_all,
        #     ):
        #         hk.Key.trigger()

    def build_hk_group_07_mixin(self):
        self.build_hk_domino_action_bar_5()
        self.build_hk_domino_action_bar_4()
        self.build_hk_domino_action_bar_3()
        self.build_hk_domino_action_bar_2()
