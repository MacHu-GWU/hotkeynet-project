# -*- coding: utf-8 -*-

"""
实现与游戏客户端以及登录有关的快捷键.
"""

import typing

from . import cmd_g01_window_and_login
from ._config_and_script import config, script
from ..constant.windows import window_index
from ..constant.credentials import credential_index
from .. import act
from .... import keyname
from ....script import Hotkey, CallCommand, SendLabel, Key, Mouse, SendFocusWindow


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
    # 10 + 8 + 6 = 24
    ctrl_f1_to_10 = [
        keyname.CTRL_(key)
        for key in keyname.F1_to_F12[:10]
    ]
    shift_f5_to_f12 = [
        keyname.SHIFT_(key)
        for key in keyname.F1_to_F12[4:]
    ]
    shift_insert_to_pgdn = [
        keyname.SHIFT_(key)
        for key in keyname.INSERT_TO_PGDN
    ]
    TOGGLE_SPECIFIC_WINDOW_1_TO_25 = ctrl_f1_to_10 + shift_f5_to_f12 + shift_insert_to_pgdn

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
    # 10 + 8 + 6 = 24
    ctrl_alt_f1_to_10 = [
        keyname.CTRL_ALT_(key)
        for key in keyname.F1_to_F12[:10]
    ]
    shift_alt_f5_to_f12 = [
        keyname.ALT_SHIFT_(key)
        for key in keyname.F1_to_F12[4:]
    ]
    shift_alt_insert_to_pgdn = [
        keyname.ALT_SHIFT_(key)
        for key in keyname.INSERT_TO_PGDN
    ]
    LOGIN_SPECIFIC_ACCOUNT_1_TO_25 = ctrl_alt_f1_to_10 + shift_alt_f5_to_f12 + shift_alt_insert_to_pgdn

    hk_dict_view = dict()
    used_window_index = list()
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
        hk_dict_view[char.window_index] = hk

    for ind in range(1, config.game_client_config.n_windows+1):
        if ind not in hk_dict_view:
            key = LOGIN_SPECIFIC_ACCOUNT_1_TO_25[ind-1]

            hk = Hotkey(
                name=f"SingleLogin{char.credential.username.title()}",
                key=keyname.SCROLOCK_ON(key),
                actions=[
                    cmd_g01_window_and_login.cmd_enter_username_and_password.call(
                        window_index[ind].title,
                        credential_index[ind].username,
                        credential_index[ind].password,
                    )
                ],
                script=script,
            )
            hk_dict_view[ind] = hk

    hk_list_view = list()
    for ind in range(1, config.game_client_config.n_windows+1):
        hk_list_view.append(hk_dict_view[ind])

    return hk_list_view

hk_list_login_specific_account = build_hk_login_specific_account()


def build_hk_batch_logout():
    return Hotkey(
        name="BatchLogout",
        key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.O)),
        actions=[
            SendLabel(
                name="",
                to=config.lbs_all(),
                actions=[
                    "<Wait 100>",
                    act.General.TOGGLE_MAIN_GAME_MENU,
                    "<Wait 50>",
                    act.General.TOGGLE_MAIN_GAME_MENU,
                    "<Wait 50>",
                    f"<MoveMouse {config.game_client_config.return_to_game_button_x} {config.game_client_config.return_to_game_button_y}>",
                    "<ClickMouse LButton Both Window NoMove>"
                    "<Wait 50>",
                    act.General.TOGGLE_MAIN_GAME_MENU,
                    "<Wait 50>",
                    f"<MoveMouse {config.game_client_config.log_out_button_x} {config.game_client_config.log_out_button_y}>",
                    "<Wait 50>",
                    "<ClickMouse LButton Both Window NoMove>"
                ]
            )
        ],
        script=script,
    )

hk_batch_logout = build_hk_batch_logout()


def build_hk_logout_on_current_window():
    return Hotkey(
        name="LogoutOnCurrentWindow",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.O)),
        actions=[
            SendFocusWindow(
                name="",
                actions=[
                    "<Wait 500>",
                    act.General.TOGGLE_MAIN_GAME_MENU,
                    "<Wait 50>",
                    act.General.TOGGLE_MAIN_GAME_MENU,
                    "<Wait 50>",
                    f"<MoveMouse {config.game_client_config.return_to_game_button_x} {config.game_client_config.return_to_game_button_y}>",
                    "<ClickMouse LButton Both Window NoMove>"
                    "<Wait 50>",
                    act.General.TOGGLE_MAIN_GAME_MENU,
                    "<Wait 50>",
                    f"<MoveMouse {config.game_client_config.log_out_button_x} {config.game_client_config.log_out_button_y}>",
                    "<Wait 50>",
                    "<ClickMouse LButton Both Window NoMove>"
                ]
            )
        ],
        script=script,
    )

hk_logout_on_current_window = build_hk_logout_on_current_window()
