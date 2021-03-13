# -*- coding: utf-8 -*-

"""
实现功能性的按键.
"""

from ._config_and_script import config, script
from .. import act
from .... import keyname
from ....script import (
    Hotkey,
    Mouse, SendLabel,
)


def build_hk_confirm():
    return Hotkey(
        name="Confirm",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.Y)),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.General.CONFIRM_MACRO_KEY_NUMPAD_5
                ]
            )
        ],
        script=script,
    )


hk_confirm = build_hk_confirm()


def build_hk_leave_party():
    return Hotkey(
        name="LeaveParty",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.L)),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.General.LEAVE_PARTY_MACRO_KEY_ALT_END
                ]
            )
        ],
        script=script,
    )


hk_leave_party = build_hk_leave_party()


def build_hk_all_pass_item():
    return Hotkey(
        name="All Pass Item",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.Q)),
        actions=[
            SendLabel(
                name="pass_item_button",
                to=config.lbs_all(),
                actions=[
                    Mouse(
                        button=keyname.MOUSE_LButton,
                        mode=f"{config.game_client_config.pass_item_button_x} {config.game_client_config.pass_item_button_1_y}",
                    ),
                    Mouse(
                        button=keyname.MOUSE_LButton,
                        mode=f"{config.game_client_config.pass_item_button_x} {config.game_client_config.pass_item_button_2_y}",
                    ),
                    Mouse(
                        button=keyname.MOUSE_LButton,
                        mode=f"{config.game_client_config.pass_item_button_x} {config.game_client_config.pass_item_button_3_y}",
                    ),
                    Mouse(
                        button=keyname.MOUSE_LButton,
                        mode=f"{config.game_client_config.pass_item_button_x} {config.game_client_config.pass_item_button_4_y}",
                    ),
                ]
            ),
        ],
        script=script,
    )


hk_all_pass_item = build_hk_all_pass_item()


def build_hk_volumn_down():
    return Hotkey(
        name="Volume Down",
        key=keyname.SCROLOCK_ON(keyname.CTRL_SHIFT_ALT(keyname.M)),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    act.System.MASTER_VOLUME_DOWN,
                ]
            )
        ],
        script=script,
    )


hk_volumn_down = build_hk_volumn_down()
