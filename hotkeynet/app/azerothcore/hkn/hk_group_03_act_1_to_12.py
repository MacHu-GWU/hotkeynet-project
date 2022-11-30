# -*- coding: utf-8 -*-

"""
实现按键 1-12 的功能.
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


class HotkeyGroup03Act1To12Mixin:
    def _get_send_label_by_id(
        self: "HknScript",
        id_: str,
        blocks: T.Iterable[hk.SendLabel],
    ) -> T.Optional[hk.SendLabel]:
        for block in blocks:
            if isinstance(block, hk.SendLabel):
                if block.id == id_:
                    return block
        return None

    def build_actions_default(
        self: "HknScript",
        key: str,
        healer_target_nothing: bool = False,
        healer_target_focus: bool = False,
        healer_target_focus_target: bool = False,
        healer_target_self: bool = False,
        healer_target_party: bool = False,
        healer_target_raid: bool = False,
    ) -> T.List[hk.SendLabel]:
        """
        通常情况下, 我们打怪的逻辑是: 坦克拉怪, DPS 输出, 治疗奶. 而我们有那么多键位. 为了
        避免为那么多键位写一大堆重复代码, 我们定义了一个工厂函数, 用于生成默认的设置.
        简单来说默认设置就是:

        1. 坦克对当前选择的怪施放技能
        2. DPS 对焦点的目标释放技能
        3. 治疗 对某个目标释放技能, 这里的 "某个" 取决于哪个模式. 请参考下面的参数定义:

        :param healer_target_nothing: 在施放治疗技能前不选择目标
        :param healer_target_focus: 治疗前 (下同), 先选定焦点, 通常是坦克司机
        :param healer_target_focus_target: 先选择焦点的目标, 通常是坦克选择队友然后治疗该队友
        :param healer_target_self: 先选择自己
        :param healer_target_party: 先用宏随机选定小队成员
        :param healer_target_raid: 先用宏随机选择团队成员

        以上 5 个模式中必须选择其中的一个.

        **注**

        这里我们需要为所有的 Active Characters 的每一个特定的天赋创建一个 SendLabel 对象.
        这和我们之前为一类 TalentCategory 创建一个 SendLabel, 然后在 SendLabel.to
        里面指定多个 label 的模式不同. 虽然后者从代码的角度讲更加紧凑, 但是却丧失了之后为
        每个特定的天赋在特殊场景下指定不同的行为的能力. 所以我们才用的这种不符合直觉的写法.
        """
        if (
            sum(
                [
                    healer_target_nothing,
                    healer_target_focus,
                    healer_target_focus_target,
                    healer_target_self,
                    healer_target_party,
                    healer_target_raid,
                ]
            )
            != 1
        ):
            raise ValueError()

        send_label_list = list()

        # Tank
        for talent in TC.tank.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.mode.lbs_by_tl(talent),
            ) as send_label:
                hk.Key.make(key)
                send_label_list.append(send_label)

        # DPS
        for talent in TC.dps.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.mode.lbs_by_tl(talent),
            ) as send_label:
                act.target.TARGET_FOCUS_TARGET()
                hk.Key.make(key)
                send_label_list.append(send_label)

        # Healer
        for talent in TC.healer.talents:
            with hk.SendLabel(
                id=talent.name,
                to=self.mode.lbs_by_tl(talent),
            ) as send_label:
                if healer_target_nothing:
                    hk.Key.make(key)
                elif healer_target_focus:
                    act.target.TARGET_FOCUS()
                    hk.Key.make(key)
                elif healer_target_focus_target:
                    act.target.TARGET_FOCUS_TARGET()
                    hk.Key.make(key)
                elif healer_target_self:
                    act.target.TARGET_SELF()
                    hk.Key.make(key)
                elif healer_target_party:
                    act.target.TARGET_PARTY()
                    hk.Key.make(key)
                elif healer_target_raid:
                    act.target.TARGET_RAID()
                    hk.Key.make(key)
                else:  # pragma: no cover
                    raise NotImplementedError

                send_label_list.append(send_label)

        return send_label_list

    def _build_send_label_by_talent(
        self: "HknScript",
        talent: T.Union[TL, T.List[TL]],
        target: T.Optional[T.Union[T.Callable, T.List[T.Callable]]],
        key: str,
    ) -> T.List[hk.SendLabel]:
        send_label_list: T.List[hk.SendLabel] = list()
        if isinstance(talent, TL):
            talent_list: T.List[TL] = [
                talent,
            ]
        else:
            talent_list: T.List[TL] = talent

        if target is None:
            target_list: T.List[T.Callable] = []
        elif isinstance(target, list):
            target_list: T.List[T.Callable] = target
        else:
            target_list: T.List[T.Callable] = [
                target,
            ]

        for talent in talent_list:
            with hk.SendLabel(
                id=talent.name,
                to=self.mode.lbs_by_tl(talent),
            ) as send_label:
                for target in target_list:
                    target()
                hk.Key.make(key)
                send_label_list.append(send_label)

        return send_label_list

    def _build_default_tank_action(self: "HknScript", key: str) -> T.List[hk.SendLabel]:
        return self._build_send_label_by_talent(
            talent=list(TC.tank.talents),
            target=list(),
            key=key,
        )

    def _build_default_dps_action(self: "HknScript", key: str) -> T.List[hk.SendLabel]:
        return self._build_send_label_by_talent(
            talent=list(TC.dps.talents),
            target=act.target.TARGET_FOCUS_TARGET,
            key=key,
        )

    def build_hk_1_heal_tank(self: "HknScript"):
        with hk.Hotkey(
            id="Key1",
            key=KN.SCROLOCK_ON(KN.KEY_1),
        ) as self.hk_1:
            self._build_default_tank_action(key=KN.KEY_1)
            self._build_default_dps_action(key=KN.KEY_1)

            # 奶德, 奶萨 用小治疗奶坦克
            label_list_druid_resto = self.mode.lbs_by_tc(TC.druid_resto)
            label_list_shaman_resto = self.mode.lbs_by_tc(TC.shaman_resto)
            label_list = label_list_druid_resto + label_list_shaman_resto
            if len(label_list) == 0:
                pass
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id="SlowTankHealer",
                    to=label_list,
                ):
                    act.target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_1)
            else:
                with hk.SendLabel(
                    id="SlowTankHealer1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.mode.target_leader_1()
                    hk.Key.make(KN.KEY_1)
                with hk.SendLabel(
                    id="SlowTankHealer2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.mode.target_leader_2()
                    hk.Key.make(KN.KEY_1)
                with hk.SendLabel(
                    id="SlowTankHealerOther",
                    to=label_list[2:],
                ):
                    act.target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_1)

            # 戒律牧, 随机给团上盾
            self._build_send_label_by_talent(
                talent=list(TC.priest_disco.talents),
                target=None,
                key=KN.KEY_1,
            )

            # 奶骑, 随机奶团
            self._build_send_label_by_talent(
                talent=list(TC.paladin_holy.talents),
                target=act.target.TARGET_RAID,
                key=KN.KEY_1,
            )

    def build_hk_2_heal_nothing(self: "HknScript"):
        with hk.Hotkey(
            id="Key2",
            key=KN.SCROLOCK_ON(KN.KEY_2),
        ) as self.hk_2:
            self._build_default_tank_action(key=KN.KEY_2)
            self._build_default_dps_action(key=KN.KEY_2)

            # 德鲁伊, 萨满, 戒律牧, 用位于 2 号键位上的一键治疗宏
            self._build_send_label_by_talent(
                talent=list(
                    TC.druid_resto.talents
                    | TC.shaman_resto.talents
                    | TC.priest_disco.talents
                ),
                target=None,
                key=KN.KEY_2,
            )
            # 奶骑, 随机奶团
            self._build_send_label_by_talent(
                talent=list(TC.paladin_holy.talents),
                target=act.target.TARGET_RAID,
                key=KN.KEY_2,
            )

    def build_hk_3_heal_tank(self: "HknScript"):
        with hk.Hotkey(
            id="Key3",
            key=KN.SCROLOCK_ON(KN.KEY_3),
        ) as self.hk_3:
            self._build_default_tank_action(key=KN.KEY_3)
            self._build_default_dps_action(key=KN.KEY_3)

            # 奶骑, 按概率为 Leader 补 圣光道标
            label_list = self.mode.lbs_by_tc(TC.paladin_healer)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个奶骑, 则给焦点加圣光道标
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.paladin_healer.name,
                    to=self.mode.lbs_by_tc(TC.paladin_healer),
                ):
                    act.target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_3)
            # 如果有 2 或 2 个以上的奶骑, 两个奶骑分别给两个 leader 加圣光道标
            # 其他的奶骑给焦点加圣光道标
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="HolyPaladin1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.mode.target_leader_1()
                    hk.Key.make(KN.KEY_3)
                with hk.SendLabel(
                    id="HolyPaladin2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.mode.target_leader_2()
                    hk.Key.make(KN.KEY_3)
                with hk.SendLabel(
                    id="HolyPaladin3andAbove",
                    to=label_list[2:],
                ):
                    act.target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_3)

            # 奶萨, 奶德 用大治疗奶坦克
            label_list_shaman_resto = self.mode.lbs_by_tc(TC.shaman_resto)
            label_list_druid_resto = self.mode.lbs_by_tc(TC.druid_resto)
            label_list = label_list_shaman_resto + label_list_druid_resto
            if len(label_list) == 0:
                pass
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id="BigTankHealer",
                    to=label_list,
                ):
                    act.target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_3)
            else:
                with hk.SendLabel(
                    id="BigTankHealer1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.mode.target_leader_1()
                    hk.Key.make(KN.KEY_3)
                with hk.SendLabel(
                    id="BigTankHealer2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.mode.target_leader_2()
                    hk.Key.make(KN.KEY_3)
                with hk.SendLabel(
                    id="BigTankHealerOther",
                    to=label_list[2:],
                ):
                    act.target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_3)

            # 戒律牧, 随机给团上盾
            self._build_send_label_by_talent(
                talent=list(TC.priest_disco.talents),
                target=None,
                key=KN.KEY_3,
            )

    def build_hk_4_heal_nothing(self: "HknScript"):
        with hk.Hotkey(
            id="Key4",
            key=KN.SCROLOCK_ON(KN.KEY_4),
        ) as self.hk_4:
            self._build_default_tank_action(key=KN.KEY_4)
            self._build_default_dps_action(key=KN.KEY_4)

            # 奶骑给焦点的目标补圣光审判
            label_list = self.mode.lbs_by_tc(TC.paladin_healer)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个奶骑, 则给焦点的目标补圣光审判
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.paladin_healer.name,
                    to=self.mode.lbs_by_tc(TC.paladin_healer),
                ):
                    act.target.TARGET_FOCUS_TARGET()
                    hk.Key.make(KN.KEY_4)
            # 如果有 2 或 2 个以上的奶骑, 两个奶骑分别给两个 leader 的目标补圣光审判
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="HolyPaladin1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.mode.target_leader_1()
                    act.target.ASSIST_TARGET()
                    hk.Key.make(KN.KEY_4)
                with hk.SendLabel(
                    id="HolyPaladin2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.mode.target_leader_2()
                    act.target.ASSIST_TARGET()
                    hk.Key.make(KN.KEY_4)
                with hk.SendLabel(
                    id="HolyPaladin3andAbove",
                    to=label_list[2:],
                ):
                    act.target.TARGET_FOCUS_TARGET()
                    hk.Key.make(KN.KEY_4)

            # 奶萨 用位于 4 号键位上的按概率周期性给坦克上大地之盾的宏
            label_list = self.mode.lbs_by_tc(TC.shaman_resto)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个奶萨, 则给焦点补大地之盾
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.shaman_resto.name,
                    to=self.mode.lbs_by_tc(TC.shaman_resto),
                ):
                    act.target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_4)

            # 如果有 2 或 2 个以上的奶萨, 两个奶萨分别给两个坦克补大地之盾
            # 其他多余的奶萨什么也不做
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="RestoShaman1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.mode.target_leader_1()
                    hk.Key.make(KN.KEY_4)
                with hk.SendLabel(
                    id="RestoShaman2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.mode.target_leader_2()
                    hk.Key.make(KN.KEY_4)

            # 德鲁伊, 用位于 4 号键位上的一键治疗宏
            self._build_send_label_by_talent(
                talent=list(TC.druid_resto.talents),
                target=None,
                key=KN.KEY_4,
            )

            # 戒律牧 用位于 4 号键位上的按概率周期性给坦克上愈合祷言或苦修的宏
            label_list = self.mode.lbs_by_tc(TC.priest_disco)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个戒律牧, 则给焦点补愈合祷言
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.shaman_resto.name,
                    to=self.mode.lbs_by_tc(TC.priest_disco),
                ):
                    act.target.TARGET_FOCUS()
                    hk.Key.make(KN.KEY_4)

            # 如果有 2 或 2 个以上的奶萨, 两个奶萨分别给两个 leader 的补大地之盾
            # 其他多余的奶萨什么也不做
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="DiscoPriest1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.mode.target_leader_1()
                    hk.Key.make(KN.KEY_4)
                with hk.SendLabel(
                    id="DiscoPriest2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.mode.target_leader_2()
                    hk.Key.make(KN.KEY_4)

    def build_hk_5_aoe_heal_self(self: "HknScript"):
        with hk.Hotkey(
            id="Key5",
            key=KN.SCROLOCK_ON(KN.KEY_5),
        ) as self.hk_5:
            send_label_list = self.build_actions_default(
                key=KN.KEY_5,
                healer_target_focus_target=True,  # 选择 焦点的目标
            )

            # 奶骑对自己放圣光术
            send_label = self._get_send_label_by_id(
                id_=TL.paladin_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.target.TARGET_SELF(),
                    act.paladin_holy.Holy_Light(),
                ]

            # 奶萨对自己放治疗链
            send_label = self._get_send_label_by_id(
                id_=TL.shaman_pve_resto.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.target.TARGET_SELF(),
                    act.shaman.Chain_Heal(),
                ]

            # 奶德对自己放野性生长
            send_label = self._get_send_label_by_id(
                id_=TL.druid_pve_resto.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.target.TARGET_SELF(),
                    act.druid_restoration.Wild_Growth(),
                ]

            # 戒律牧放治疗祷言
            send_label = self._get_send_label_by_id(
                id_=TL.priest_pve_disco.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.priest_discipline.Prayer_of_Healing(),
                ]

            # 神圣牧放治疗祷言
            send_label = self._get_send_label_by_id(
                id_=TL.priest_pve_holy.name,
                blocks=send_label_list,
            )
            with send_label():
                send_label.blocks = [
                    act.priest_holy.Prayer_of_Healing(),
                ]

    def build_hk_6_one_time_debuff(self: "HknScript"):
        with hk.Hotkey(
            id="Key6",
            key=KN.SCROLOCK_ON(KN.KEY_6),
        ) as self.hk_6:
            send_label_list = self.build_actions_default(
                key=KN.KEY_6,
                healer_target_focus_target=True,  # 选择 焦点
            )

    def build_hk_7(self: "HknScript"):
        with hk.Hotkey(
            id="Key7",
            key=KN.SCROLOCK_ON(KN.KEY_7),
        ) as self.hk_7:
            send_label_list = self.build_actions_default(
                key=KN.KEY_7,
                healer_target_focus_target=True,  # 选择 焦点
            )

    def build_hk_8_buff_self(self: "HknScript"):
        with hk.Hotkey(
            id="Key8",
            key=KN.SCROLOCK_ON(KN.KEY_8),
        ) as self.hk_8:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                hk.Key(key=KN.KEY_8)

    def build_hk_9_buff_raid(self: "HknScript"):

        with hk.Hotkey(
            id="Key9",
            key=KN.SCROLOCK_ON(KN.KEY_9),
        ) as self.hk_9:
            with hk.SendLabel(
                id="all",
                to=self.mode.lbs_all,
            ):
                hk.Key(key=KN.KEY_9)

    def build_hk_0_short_term_buff(self: "HknScript"):
        """
        补刷持续时间短的 Buff.
        """
        with hk.Hotkey(
            id="Key0",
            key=KN.SCROLOCK_ON(KN.KEY_0),
        ) as self.hk_0_short_term_buff:
            with hk.SendLabel(
                id=TC.dk.name,
                to=self.mode.lbs_by_tc(TC.dk),
            ):
                act.dk.Horn_of_Winter()

            label_list = self.mode.lbs_by_tc(TC.paladin_healer)
            if len(label_list) == 0:
                pass
            # 如果只有 1 个奶骑, 则给焦点加圣光道标
            elif len(label_list) == 1:
                with hk.SendLabel(
                    id=TC.paladin_healer.name,
                    to=self.mode.lbs_by_tc(TC.paladin_healer),
                ):
                    act.target.TARGET_FOCUS()
                    act.paladin_holy.Beacon_of_Light()
            # 如果有 2 或 2 个以上的奶骑, 两个奶骑分别给两个 leader 加圣光道标
            # 其他的奶骑给焦点加圣光道标
            elif len(label_list) == 2:
                with hk.SendLabel(
                    id="HolyPaladin1",
                    to=[
                        label_list[0],
                    ],
                ):
                    self.mode.target_leader_1()
                    act.paladin_holy.Beacon_of_Light()
                with hk.SendLabel(
                    id="HolyPaladin2",
                    to=[
                        label_list[1],
                    ],
                ):
                    self.mode.target_leader_2()
                    act.paladin_holy.Beacon_of_Light()
                with hk.SendLabel(
                    id="HolyPaladin3andAbove",
                    to=label_list[2:],
                ):
                    act.target.TARGET_FOCUS()
                    act.paladin_holy.Beacon_of_Light()

            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(TC.shaman),
            ):
                act.shaman_restoration.Water_Shield()

            with hk.SendLabel(
                id=TC.warlock.name,
                to=self.mode.lbs_by_tc(TC.warlock),
            ):
                act.warlock.Fel_Armor()

            with hk.SendLabel(
                id=TC.priest.name,
                to=self.mode.lbs_by_tc(TC.priest),
            ):
                act.priest.Inner_Fire()

    def build_hk_11_focus_mode_1(self: "HknScript"):
        """
        所有人的焦点设置为它们的 1 号司机 (除了司机本人)
        """
        with hk.Hotkey(
            id="SetFocusMode1",
            key=KN.SCROLOCK_ON(KN.KEY_11_MINUS),
        ) as self.hk_11_focus_mode_1:
            for char in self.mode.active_chars:
                if char.is_leader_1:  # 司机本人清除焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[
                            char.window.label,
                        ],
                    ):
                        act.general.CLEAR_FOCUS_NUMPAD_7()
                else:  # 其他人设置焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[
                            char.window.label,
                        ],
                    ):
                        act.target_leader_key_mapper[char.leader_1_window.label]()
                        act.general.SET_FOCUS_KEY_NUMPAD_6()

    def build_hk_12_focus_mode_2(self: "HknScript"):
        """
        所有人的焦点设置为它们的 2 号司机 (除了司机本人)
        """
        with hk.Hotkey(
            id="SetFocusMode2",
            key=KN.SCROLOCK_ON(KN.KEY_12_PLUS),
        ) as self.hk_12_focus_mode_2:
            for char in self.mode.active_chars:
                if char.is_leader_2:  # 司机本人清除焦点
                    with hk.SendLabel(
                        id=char.account.username,
                        to=[
                            char.window.label,
                        ],
                    ):
                        act.general.CLEAR_FOCUS_NUMPAD_7()
                else:  # 其他人设置焦点
                    with hk.SendLabel(
                        name=char.account.username,
                        to=[
                            char.window.label,
                        ],
                    ):
                        act.target_leader_key_mapper[char.leader_2_window.label]()
                        act.general.SET_FOCUS_KEY_NUMPAD_6()

    # # --- alt 1,2,3,4,5
    def build_hk_alt_5(self: "HknScript"):
        """
        对自己放大型群刷技能.
        """
        with hk.Hotkey(
            id="Alt 5",
            key=KN.SCROLOCK_ON(KN.ALT_(KN.KEY_5)),
        ) as self.hk_alt_5:
            with hk.SendLabel(
                id=TC.priest_holy.name,
                to=self.mode.lbs_by_tc(tc=TC.priest_holy),
            ):
                act.target.TARGET_SELF()
                act.priest_holy.Circle_of_Healing()

            with hk.SendLabel(
                id=TC.shaman.name,
                to=self.mode.lbs_by_tc(tc=TC.shaman),
            ):
                act.target.TARGET_FOCUS_TARGET()
                act.shaman.Chain_Heal()

    def build_hk_group_03_act_1_to_12_mixin(self):
        self.build_hk_1_heal_tank()
        self.build_hk_2_heal_nothing()
        self.build_hk_3_heal_tank()
        self.build_hk_4_heal_nothing()
        self.build_hk_5_aoe_heal_self()
        self.build_hk_6_one_time_debuff()
        self.build_hk_7()
        self.build_hk_8_buff_self()
        self.build_hk_9_buff_raid()
        self.build_hk_0_short_term_buff()
        self.build_hk_11_focus_mode_1()
        self.build_hk_12_focus_mode_2()

        self.build_hk_alt_5()
