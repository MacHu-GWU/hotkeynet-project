# -*- coding: utf-8 -*-

"""
实现与人物移动有关的快捷键.
"""

import typing
from ._config_and_script import config, script
from .. import act
from ..constant.talent_category_association import (
    TalentCategory, )
from ..constant.windows import window_index
from .... import keyname
from ....script import MovementHotkey, SendLabel, Key


def go_up(lbs: list):
    lbs = [window_index[ind].label for ind in lbs]
    return SendLabel(name="up", to=lbs, actions=[act.Movement.MOVE_FORWARD, ])


def go_down(lbs: list):
    lbs = [window_index[ind].label for ind in lbs]
    return SendLabel(name="down", to=lbs, actions=[act.Movement.MOVE_BACKWARD, ])


def go_left(lbs: list):
    lbs = [window_index[ind].label for ind in lbs]
    return SendLabel(name="left", to=lbs, actions=[act.Movement.MOVE_LEFT, ])


def go_right(lbs: list):
    lbs = [window_index[ind].label for ind in lbs]
    return SendLabel(name="right", to=lbs, actions=[act.Movement.MOVE_RIGHT, ])


def go_left_up(lbs: list):
    lbs = [window_index[ind].label for ind in lbs]
    return SendLabel(name="left_up", to=lbs, actions=[act.Movement.MOVE_LEFT_TOP, ])


def go_left_down(lbs: list):
    lbs = [window_index[ind].label for ind in lbs]
    return SendLabel(name="left_down", to=lbs, actions=[act.Movement.MOVE_LEFT_BOTTOM, ])


def go_right_up(lbs: list):
    lbs = [window_index[ind].label for ind in lbs]
    return SendLabel(name="right_up", to=lbs, actions=[act.Movement.MOVE_RIGHT_TOP, ])


def go_right_down(lbs: list):
    lbs = [window_index[ind].label for ind in lbs]
    return SendLabel(name="right_down", to=lbs, actions=[act.Movement.MOVE_RIGHT_BOTTOM, ])


def build_hk_all_move_up_down_turn_left_right():
    """
    按下键盘上的上下左右方向键, 分别使得所有窗口 前进, 后退, 左转, 右转.
    """
    return MovementHotkey(
        name="All Move Up Down, Turn Left Right",
        key=keyname.SCROLOCK_ON(f"{keyname.UP}, {keyname.DOWN}, {keyname.LEFT}, {keyname.RIGHT}"),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.General.TRIGGER,
                ]
            )
        ],
        script=script,
    )


hk_all_move_up_down_turn_left_right = build_hk_all_move_up_down_turn_left_right()


def build_hk_non_tank_move_up_down_turn_left_right():
    """
    按下 Ctrl + 上下左右方向键, 非坦克职业按下同样的键. 用于实现非坦克职业进行走位躲避技能.
    """
    return MovementHotkey(
        name="Non Tank Move Up Down, Turn Left Right",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(f"{keyname.UP}, {keyname.DOWN}, {keyname.LEFT}, {keyname.RIGHT}")),
        actions=[
            SendLabel(
                name=TalentCategory.non_tank.name,
                to=config.lbs_by_tc(TalentCategory.non_tank),
                actions=[
                    Key.trigger()
                ]
            )
        ],
        script=script,
    )


hk_non_tank_move_up_down_turn_left_right = build_hk_non_tank_move_up_down_turn_left_right()


def build_hk_non_tank_move_left_right():
    """
    按下 Ctrl + A / D, 非坦克职业进行 Q / E 平移, 走位躲避技能.
    """
    hk_non_tank_move_left = MovementHotkey(
        name="Non Tank Move Left",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.A)),
        actions=[
            SendLabel(
                name=TalentCategory.non_tank.name,
                to=config.lbs_by_tc(TalentCategory.non_tank),
                actions=[
                    act.Movement.MOVE_LEFT,
                ]
            )
        ],
        script=script,
    )

    hk_non_tank_move_right = MovementHotkey(
        name="Non Tank Move Right",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.D)),
        actions=[
            SendLabel(
                name=TalentCategory.non_tank.name,
                to=config.lbs_by_tc(TalentCategory.non_tank),
                actions=[
                    act.Movement.MOVE_RIGHT,
                ]
            )
        ],
        script=script,
    )

    return hk_non_tank_move_left, hk_non_tank_move_right


hk_non_tank_move_left, hk_non_tank_move_right = build_hk_non_tank_move_left_right()


def build_hk_all_jump():
    return MovementHotkey(
        name="All Jump",
        key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.SPACE)),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.Movement.JUMP,
                ]
            )
        ],
        script=script,
    )


hk_all_jump = build_hk_all_jump()


def build_hk_spread_matrix():
    """
         **矩阵分散站位***

         角色分队

         G1: 防骑, 奶德, 法师, 猎人, 术士
         G2: DK坦, 奶骑, 萨满, 暗牧, 鸟德: 奶骑组群刷不厉害, 所以需要萨满, 暗牧辅助
         以下矩阵分散站位适用于所有人在Boss的一侧进行分散的情形. 典型的Boss战有:

         Naxx 蜘蛛1, 2; ICC 亡语女士
         ICC 亡语女士, 萨鲁法尔, 血腥女王

         先按下 [ 键进行矩阵分散, 然后按下 ] 将 法师和暗牧移动到边缘.

                     防骑   DK坦

                术士     猎人     元素萨

         法师    奶德     鸟德    奶骑     暗牧

    """
    hk_spread_matrix_1 = MovementHotkey(
        name="Spread Matrix 1",
        key=keyname.SCROLOCK_ON(keyname.OEM4_SQUARE_BRACKET_LEFT),
        actions=[
            SendLabel(
                name="all",
                to=["w6", "w15", "w14"],
                actions=[
                    act.Movement.MOVE_LEFT,
                ]
            ),
            SendLabel(
                name="all",
                to=["w3", "w11", "w18"],
                actions=[
                    act.Movement.MOVE_RIGHT,
                ]
            ),
            SendLabel(
                name="all",
                to=["w4", "w8", "w16", "w13"],
                actions=[
                    act.Movement.MOVE_LEFT_BOTTOM,
                ]
            ),
            SendLabel(
                name="all",
                to=["w5", "w9", "w12", "17"],
                actions=[
                    act.Movement.MOVE_RIGHT_BOTTOM,
                ]
            ),
            SendLabel(
                name="all",
                to=["w2", ],
                actions=[
                    act.Movement.MOVE_BACKWARD,
                ]
            ),
        ],
        script=script,
    )

    hk_spread_matrix_2 = MovementHotkey(
        name="Spread Matrix 2",
        key=keyname.SCROLOCK_ON(keyname.OEM6_SQUARE_BRACKET_RIGHT),
        actions=[
            SendLabel(
                name="all",
                to=["w4", "w11", "w12"],
                actions=[
                    act.Movement.MOVE_LEFT,
                ]
            ),
            SendLabel(
                name="all",
                to=["w5", "w15", "16"],
                actions=[
                    act.Movement.MOVE_RIGHT,
                ]
            ),
        ],
        script=script,
    )

    return hk_spread_matrix_1, hk_spread_matrix_2


hk_spread_matrix_1, hk_spread_matrix_2 = build_hk_spread_matrix()


def build_hk_spread_circle_1():
    """
    **环形分散站位**

    以下环形分散站位适用于所有人相互距离8码, 而又需要小范围的移动而躲避技能的情况. 典型的Boss战有:

    - Naxx 克尔苏加德
    - ICC 烂肠, 腐面, 血亲王议会

    按下该快捷键后, 大家会分别向, 上下左右, 斜线方向移动, 并且面朝一致的方向, 也就是可以保持圆形队形不变向前后移动. 此适用于无法预先安排好阵型, 而需要在战斗中走到指定位置的情形. 按下快捷键分散后, 大家离中心的距离其实是不一样的, 有的远有的近. 此时再按下跟随焦点键, 所有人即可向中心靠拢, 然后再按后退键即可实现一个环形站位, 且环形大小可以通过前进后退进行调整.

                鸟德/奶德2
        猎人                暗牧
                  DK坦
    奶德          boss          奶骑
                  防骑
        法师                元素萨
                术士/奶德3
    """
    actions = [
        go_up([3, 14, 15]),
        go_down([6, 11, 18, ]),
        go_left([8, 12, 16, ]),
        go_right([9, 13, 17, ]),
        go_left_up([7, 19]),
        go_left_down([4, 20, ]),
        go_right_up([5, 21, ]),
        go_right_down([2, 22]),
    ] # type: typing.List[SendLabel]

    tank_char_window_label_list = config.lbs_by_tc(tc=TalentCategory.tank)

    for send_label in actions:
        for label in tank_char_window_label_list:
            if label in send_label.to:
                send_label.to.remove(label)

    return MovementHotkey(
        name="Spread Circle",
        key=keyname.SCROLOCK_ON(keyname.OEM5_PIPE_OR_BACK_SLASH),
        actions=actions,
        script=script,
    )


hk_spread_circle1 = build_hk_spread_circle_1()


def build_hk_spread_circle_2():
    """
    **环形分散站位**

    以下环形分散站位适用于所有人相互距离8码, 而又需要小范围的移动而躲避技能的情况. 典型的Boss战有:

    - Naxx 克尔苏加德
    - ICC 烂肠, 腐面, 血亲王议会

    按下该快捷键后, 大家会分别向, 上下左右, 斜线方向移动, 并且面朝一致的方向, 也就是可以保持圆形队形不变向前后移动. 此适用于无法预先安排好阵型, 而需要在战斗中走到指定位置的情形. 按下快捷键分散后, 大家离中心的距离其实是不一样的, 有的远有的近. 此时再按下跟随焦点键, 所有人即可向中心靠拢, 然后再按后退键即可实现一个环形站位, 且环形大小可以通过前进后退进行调整.

                鸟德/奶德2
        猎人                暗牧
                  DK坦
    奶德          boss          奶骑
                  防骑
        法师                元素萨
                术士/奶德3
    """
    return MovementHotkey(
        name="Spread Circle",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.OEM5_PIPE_OR_BACK_SLASH)),
        actions=[
            go_left([11, 12, 13, 14]),
            go_up([15, 16, 17, 18, 19, 20, 21, 22]),
        ],
        script=script,
    )


hk_spread_circle2 = build_hk_spread_circle_2()
