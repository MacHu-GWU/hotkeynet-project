# -*- coding: utf-8 -*-

"""
实现与人物移动有关的快捷键.
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


class HotkeyGroup02MovementMixin:
    def _convert_int_lbs_to_str_lbs(self: "HknScript", lbs: T.List[int]) -> T.List[str]:
        return [f"w{str(ind).zfill(2)}" for ind in lbs]

    def _go_up(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="up",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.movement.MOVE_FORWARD()
            return send_label

    def _go_down(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="down",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.movement.MOVE_BACKWARD()
            return send_label

    def _go_left(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="left",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.movement.MOVE_LEFT()
            return send_label

    def _go_right(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="right",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.movement.MOVE_RIGHT()
            return send_label

    def _go_left_up(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="left_up",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.movement.MOVE_LEFT_TOP()
            return send_label

    def _go_left_down(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="left_down",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.movement.MOVE_LEFT_BOTTOM()
            return send_label

    def _go_right_up(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="right_up",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.movement.MOVE_RIGHT_TOP()
            return send_label

    def _go_right_down(self, lbs: T.List[int]):
        with hk.SendLabel(
            id="right_down",
            to=self._convert_int_lbs_to_str_lbs(lbs),
        ) as send_label:
            act.movement.MOVE_RIGHT_BOTTOM()
            return send_label

    def build_hk_all_move_up_down_turn_left_right(self: "HknScript"):
        """
        按下键盘上的上下左右方向键, 分别使得所有窗口 前进, 后退, 左转, 右转.
        """
        with hk.MovementHotkey(
            id="All Move Up Down, Turn Left Right",
            key=KN.SCROLOCK_ON(f"{KN.UP}, {KN.DOWN}, {KN.LEFT}, {KN.RIGHT}"),
        ) as self.hk_all_move_up_down_turn_left_right:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.general.TRIGGER()

    def build_hk_non_tank_move_up_down_turn_left_right(self: "HknScript"):
        """
        按下 Ctrl + 上下左右方向键, 非坦克职业按下同样的键. 用于实现非坦克职业进行走位躲避技能.
        """
        with hk.MovementHotkey(
            id="Non Tank Move Up Down, Turn Left Right",
            key=KN.SCROLOCK_ON(KN.CTRL_(f"{KN.UP}, {KN.DOWN}, {KN.LEFT}, {KN.RIGHT}")),
        ) as self.hk_non_tank_move_up_down_turn_left_right:
            with hk.SendLabel(
                to=self.mode.lbs_by_tc(TC.non_tank),
            ):
                act.general.TRIGGER()

    def build_hk_non_tank_move_left_right(self: "HknScript"):
        """
        按下 Ctrl + A / D, 非坦克职业进行 Q / E 平移, 走位躲避技能.
        """
        with hk.MovementHotkey(
            id="Non Tank Move Left",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.A)),
        ) as self.hk_non_tank_move_left:
            with hk.SendLabel(
                to=self.mode.lbs_by_tc(TC.non_tank),
            ):
                act.movement.MOVE_LEFT()

        with hk.MovementHotkey(
            id="Non Tank Move Right",
            key=KN.SCROLOCK_ON(KN.CTRL_(KN.D)),
        ) as self.hk_non_tank_move_right:
            with hk.SendLabel(
                to=self.mode.lbs_by_tc(TC.non_tank),
            ):
                act.movement.MOVE_RIGHT()

    def build_hk_all_jump(self: "HknScript"):
        with hk.MovementHotkey(
            id="All Jump",
            key=KN.SCROLOCK_ON(KN.SHIFT_(KN.SPACE)),
        ) as self.hk_all_jump:
            with hk.SendLabel(
                to=self.mode.lbs_all,
            ):
                act.movement.JUMP()

    def build_hk_spread_matrix(self: "HknScript"):
        """
        **矩阵分散站位***

        角色分队

        G1: 防骑, 奶德, 法师, 猎人, 术士
        G2: DK坦, 奶骑, 萨满, 暗牧, 鸟德: 奶骑组群刷不厉害, 所以需要萨满, 暗牧辅助

        以下矩阵分散站位适用于所有人在Boss的一侧进行分散的情形. 典型的Boss战有:

        Naxx 蜘蛛1, 2; ICC 亡语女士
        ICC 亡语女士, 萨鲁法尔, 血腥女王

        先按下 "[" 键进行矩阵分散, 然后按下 "]" 将 法师和暗牧移动到边缘.

                   防骑   DK坦

              术士     猎人     元素萨

        法师    奶德     鸟德    奶骑     暗牧
        """
        with hk.MovementHotkey(
            id="Spread Matrix 1",
            key=KN.SCROLOCK_ON(KN.OEM4_SQUARE_BRACKET_LEFT),
        ) as self.hk_spread_matrix_1:
            send_label_list: T.List[hk.SendLabel] = [
                self._go_left([6, 15, 14]),
                self._go_right([3, 11, 18]),
                self._go_left_down([4, 8, 16, 13]),
                self._go_right_down([5, 9, 12, 17]),
                self._go_down(
                    [
                        2,
                    ]
                ),
            ]
            for send_label in send_label_list:
                self.mode.remove_inactive_labels(send_label.to)

        with hk.MovementHotkey(
            id="Spread Matrix 2",
            key=KN.SCROLOCK_ON(KN.OEM6_SQUARE_BRACKET_RIGHT),
        ) as self.hk_spread_matrix_2:
            send_label_list: T.List[hk.SendLabel] = [
                self._go_left([4, 11, 12]),
                self._go_right([5, 15, 16]),
            ]
            for send_label in send_label_list:
                self.mode.remove_inactive_labels(send_label.to)

    def build_hk_spread_circle(self: "HknScript"):
        """
        **环形分散站位**

        以下环形分散站位适用于所有人相互距离8码, 而又需要小范围的移动而躲避技能的情况. 典型的Boss战有:

        - Naxx 克尔苏加德
        - ICC 烂肠, 腐面, 血亲王议会

        按下该快捷键后, 大家会分别向, 上下左右, 斜线方向移动, 并且面朝一致的方向, 也就是可以
        保持圆形队形不变向前后移动. 此适用于无法预先安排好阵型, 而需要在战斗中走到指定位置的情形.
        按下快捷键分散后, 大家离中心的距离其实是不一样的, 有的远有的近. 此时再按下跟随焦点键,
        所有人即可向中心靠拢, 然后再按后退键即可实现一个环形站位, 且环形大小可以通过前进后退进行调整.

                    鸟德/奶德2
            猎人                暗牧
                      DK坦
        奶德          boss          奶骑
                      防骑
            法师                元素萨
                    术士/奶德3
        """
        with hk.MovementHotkey(
            id="Spread Circle",
            key=KN.SCROLOCK_ON(KN.OEM5_PIPE_OR_BACK_SLASH),
        ) as self.hk_spread_circle1:
            send_label_list: T.List[hk.SendLabel] = [
                self._go_up([3, 14, 15]),
                self._go_down([6, 11, 18]),
                self._go_left([8, 12, 16]),
                self._go_right([9, 13, 17]),
                self._go_left_up([7, 19]),
                self._go_left_down([4, 20]),
                self._go_right_up([5, 21]),
                self._go_right_down([2, 22]),
            ]
            for send_label in send_label_list:
                self.mode.remove_tank_labels(send_label.to)
                self.mode.remove_inactive_labels(send_label.to)

    def build_hk_group_02_movement_mixin(self: "HknScript"):
        self.build_hk_all_move_up_down_turn_left_right()
        self.build_hk_non_tank_move_up_down_turn_left_right()
        self.build_hk_non_tank_move_left_right()
        self.build_hk_all_jump()
        self.build_hk_spread_matrix()
        self.build_hk_spread_circle()
