# -*- coding: utf-8 -*-

"""

如果你不知道该设置什么键, 则注释掉所有的actions即可. 或是用 ``<SendFocusWin>`` 发送到当前
焦点窗口

"""
from . import act
from .config import Config, different_labels
from .script import script
from ... import keyname
from ...script import (
    Hotkey,
    Key, Mouse, SendLabel,
)

hk_confirm = Hotkey(
    name="Confirm",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.Y)),
    actions=[
        SendLabel(
            name="all",
            to=Config.SendLabelTo.all(),
            actions=[
                act.General.CONFIRM
            ]
        )
    ],
    script=script,
)


hk_leave_party = Hotkey(
    name="LeaveParty",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.L)),
    actions=[
        SendLabel(
            name="all",
            to=Config.SendLabelTo.all(),
            actions=[
                act.General.LEAVE_PARTY
            ]
        )
    ],
    script=script,
)


def build_hk_all_pass_item():
    return Hotkey(
        name="All Pass Item",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.Q)),
        actions=[
            SendLabel(
                name="all",
                to=Config.SendLabelTo.all(),
                actions=[
                    Mouse(
                        button=keyname.MOUSE_LButton,
                        mode=f"{Config.Coordinate.pass_item_button_x} {Config.Coordinate.pass_item_button_1_y}",
                    ),
                ]
            ),
            SendLabel(
                name="all",
                to=Config.SendLabelTo.all(),
                actions=[
                    Mouse(
                        button=keyname.MOUSE_LButton,
                        mode=f"{Config.Coordinate.pass_item_button_x} {Config.Coordinate.pass_item_button_2_y}",
                    ),
                ]
            ),
            SendLabel(
                name="all",
                to=Config.SendLabelTo.all(),
                actions=[
                    Mouse(
                        button=keyname.MOUSE_LButton,
                        mode=f"{Config.Coordinate.pass_item_button_x} {Config.Coordinate.pass_item_button_3_y}",
                    ),
                ]
            ),
            SendLabel(
                name="all",
                to=Config.SendLabelTo.all(),
                actions=[
                    Mouse(
                        button=keyname.MOUSE_LButton,
                        mode=f"{Config.Coordinate.pass_item_button_x} {Config.Coordinate.pass_item_button_4_y}",
                    ),
                ]
            ),
        ],
        script=script,
    )

hk_all_pass_item = build_hk_all_pass_item()
