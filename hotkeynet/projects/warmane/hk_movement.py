# -*- coding: utf-8 -*-

"""
"""

from . import act
from .config import Config, different_labels
from .script import script
from ... import keyname
from ...script import (
    MovementHotkey,
    Key, SendLabel,
)

hk_all_move_up_down_turn_left_right = MovementHotkey(
    name="all_move_up_down_turn_left_right",
    key=keyname.SCROLOCK_ON(f"{keyname.UP}, {keyname.DOWN}, {keyname.LEFT}, {keyname.RIGHT}"),
    actions=[
        SendLabel(
            name="all",
            to=Config.SendLabelTo.all,
            actions=[
                Key.trigger()
            ]
        )
    ],
    script=script,
)

hk_non_tank_move_up_down_turn_left_right = MovementHotkey(
    name="non_tank_move_up_down_turn_left_right",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(f"{keyname.UP}, {keyname.DOWN}, {keyname.LEFT}, {keyname.RIGHT}")),
    actions=[
        SendLabel(
            name="non_tank",
            to=Config.SendLabelTo.non_tank(),
            actions=[
                Key.trigger()
            ]
        )
    ],
    script=script,
)

hk_non_tank_move_left = MovementHotkey(
    name="non_tank_move_left",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.A)),
    actions=[
        SendLabel(
            name="non_tank",
            to=Config.SendLabelTo.non_tank(),
            actions=[
                act.Movement.MOVE_LEFT,
            ]
        )
    ],
    script=script,
)

hk_non_tank_move_right = MovementHotkey(
    name="non_tank_move_right",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.D)),
    actions=[
        SendLabel(
            name="non_tank",
            to=Config.SendLabelTo.non_tank(),
            actions=[
                act.Movement.MOVE_RIGHT,
            ]
        )
    ],
    script=script,
)

hk_all_jump = MovementHotkey(
    name="all",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.SPACE)),
    actions=[
        SendLabel(
            name="all",
            to=Config.SendLabelTo.all,
            actions=[
                act.Movement.JUMP,
            ]
        )
    ],
    script=script,
)
