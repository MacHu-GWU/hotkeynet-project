# -*- coding: utf-8 -*-

"""
实现与游戏客户端以及登录有关的快捷键.
"""

import typing

from . import cmd_g01_window_and_login
from ._config_and_script import config, script
from ..constant.windows import window_index
from .... import keyname
from ....script import Hotkey, CallCommand


# ---
def build_hk_launch_and_rename_game_client():
    return Hotkey(
        name="LaunchAndRenameGameClientWindow",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.L)),
        actions=[
            CallCommand(
                cmd=cmd_g01_window_and_login.cmd_launch_and_rename_all_game_client
            )
        ],
        script=script,
    )


hk_launch_and_rename_game_client = build_hk_launch_and_rename_game_client()


def build_hk_round_robin_toggle_window():
    actions = list()
    for index in config.toggle_window_config.round_robin_window_index:
        actions.append("<Toggle>")
        window_title = window_index[index].title
        actions.append("    {}".format(cmd_g01_window_and_login.cmd_bring_window_to_foreground.call(window_title)))

    return Hotkey(
        name="RoundRobinToggleWindow",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.TAB)),
        actions=actions,
        script=script,
    )


hk_round_robin_toggle_window = build_hk_round_robin_toggle_window()


def build_hk_toggle_specific_window() -> typing.List[Hotkey]:
    # 12 + 8 + 6 = 26
    ctrl_f1_to_12 = [
        keyname.CTRL_(key)
        for key in keyname.F1_to_F12
    ]
    shift_f5_to_f12 = [
        keyname.SHIFT_(key)
        for key in keyname.F1_to_F12[5:]
    ]
    ctrl_insert_to_pgdn = [
        keyname.CTRL_(key)
        for key in keyname.INSERT_TO_PGDN
    ]
    TOGGLE_SPECIFIC_WINDOW_1_TO_25 = ctrl_f1_to_12 + shift_f5_to_f12 + ctrl_insert_to_pgdn

    hk_list = list()
    for key, index in zip(TOGGLE_SPECIFIC_WINDOW_1_TO_25, config.toggle_window_config.key1_to_25_window_index):
        window_title = window_index[index].title
        hk = Hotkey(
            name=f"ToggleToSpecificWindow {key}",
            key=keyname.SCROLOCK_ON(key),
            actions=[
                cmd_g01_window_and_login.cmd_bring_window_to_foreground.call(window_title)
            ],
            script=script,
        )
        hk_list.append(hk)

    return hk_list


hk_list_toggle_specific_window = build_hk_toggle_specific_window()


# ---

def build_hk_center_overlap_layout():
    return Hotkey(
        name="CenterOverlapLayout",
        key=keyname.SCROLOCK_ON(keyname.CTRL_SHIFT_ALT(keyname.NUMPAD_11_DIVIDE)),
        actions=[
            CallCommand(cmd=cmd_g01_window_and_login.cmd_center_overlap_layout)
        ],
        script=script,
    )


hk_center_overlap_layout = build_hk_center_overlap_layout()


def build_hk_batch_login():
    return Hotkey(
        name="BatchLogin",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.S)),
        actions=[
            CallCommand(
                cmd=cmd_g01_window_and_login.cmd_batch_login,
            )
        ],
        script=script,
    )


hk_batch_login = build_hk_batch_login()


def build_hk_login_specific_account() -> typing.List[Hotkey]:
    # 12 + 8 + 6 = 26
    ctrl_alt_f1_to_12 = [
        keyname.CTRL_ALT_(key)
        for key in keyname.F1_to_F12
    ]
    shift_alt_f5_to_f12 = [
        keyname.ALT_SHIFT_(key)
        for key in keyname.F1_to_F12[5:]
    ]
    ctrl_alt_insert_to_pgdn = [
        keyname.CTRL_ALT_(key)
        for key in keyname.INSERT_TO_PGDN
    ]
    LOGIN_SPECIFIC_ACCOUNT_1_TO_25 = ctrl_alt_f1_to_12 + shift_alt_f5_to_f12 + ctrl_alt_insert_to_pgdn

    hk_list = list()
    for char in config.active_character_config.active_characters:
        key = LOGIN_SPECIFIC_ACCOUNT_1_TO_25[char.window_index-1]
        hk = Hotkey(
            name=f"SingleLogin{char.credential.username.title()}",
            key=keyname.SCROLOCK_ON(key),
            actions=[
                cmd_g01_window_and_login.cmd_enter_username_and_password.call(
                    char.window_title,
                    char.credential.username, char.credential.password
                )
            ],
            script=script,
        )
        hk_list.append(hk)
    return hk_list

hk_list_login_specific_account = build_hk_login_specific_account()
