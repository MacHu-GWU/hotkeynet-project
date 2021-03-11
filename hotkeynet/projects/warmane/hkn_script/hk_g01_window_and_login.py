# -*- coding: utf-8 -*-

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
    hk_list = list()
    # 12 + 6 + 7 = 25
    print()
    f1_to_12 = [
        keyname.CTRL_(key)
        for key in keyname.F1_to_F12
    ]
    f13_to_18 = [
        keyname.CTRL_(key)
        for key in keyname.INSERT_TO_PGDN
    ]
    f19_to_25 = [
        keyname.LWIN_(key)
        for key in keyname.F1_to_F12[:7]
    ]
    TOGGLE_SPECIFIC_WINDOW_1_TO_25 = f1_to_12 + f13_to_18 + f19_to_25

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
# hk_CenterOverlapLayout = Hotkey(
#     name="CenterOverlapLayout",
#     key=keyname.SCROLOCK_ON(keyname.CTRL_SHIFT_ALT(keyname.NUMPAD_11_DIVIDE)),
#     actions=[
#         CallCommand(cmd=cmd_window_and_login.cmd_CenterOverlapLayout)
#     ],
#     script=script,
# )
#
#
# #---
# hk_BatchLogin = Hotkey(
#     name="BatchLogin",
#     key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.S)),
#     actions=[
#         CallCommand(
#             cmd=cmd_window_and_login.cmd_BatchLogin,
#         )
#     ],
#     script=script,
# )
#
#
# #---
# for key, window, account in zip(
#         keyname.F1_to_F22,
#         Config.Windows.batch_login_windows,
#         Config.Windows.batch_login_accounts
# ):
#     window_name = f"WoW{window}"
#     username = Config.Credential.account_sequence()[account - 1]["username"]
#     password = Config.Credential.account_sequence()[account - 1]["password"]
#     hk = Hotkey(
#         name=f"SingleLogin{username.title()}",
#         key=keyname.SCROLOCK_ON(keyname.CTRL_SHIFT_ALT(key)),
#         actions=[
#             cmd_window_and_login.cmd_EnterUsernamePasssword.call(window_name, username, password)
#         ],
#         script=script,
#     )
