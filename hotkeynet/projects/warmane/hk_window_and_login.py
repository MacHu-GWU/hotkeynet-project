# -*- coding: utf-8 -*-

from . import cmd_window_and_login
from .script import script
from .config import Config
from ... import keyname
from ...script import Hotkey, CallCommand


#---
hk_LaunchAndRenameGameClientWindow = Hotkey(
    name="LaunchAndRenameGameClientWindow",
    key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.L)),
    actions=[
        CallCommand(
            cmd=cmd_window_and_login.cmd_LaunchAndRenameGameClientWindow,
        )
    ],
    script=script,
)


#---
actions = list()
for window in Config.Windows.toggle_round_robin_windows:
    actions.append("<Toggle>")
    actions.append("    {}".format(cmd_window_and_login.cmd_BringToForeground.call(f"WoW{window}")))

hk_RoundRobinToggleWindow = Hotkey(
    name="RoundRobinToggleWindow",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.TAB)),
    actions=actions,
    script=script,
)


#---
for key, window in zip(keyname.F1_to_F22, Config.Windows.toggle_specific_windows):
    hk = Hotkey(
        name=f"ToggleToSpecificWindowWoW{window}",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(key)),
        actions=[
            cmd_window_and_login.cmd_BringToForeground.call(f"WoW{window}")
        ],
        script=script,
    )


#---
hk_CenterOverlapLayout = Hotkey(
    name="CenterOverlapLayout",
    key=keyname.SCROLOCK_ON(keyname.CTRL_SHIFT_ALT(keyname.NUMPAD_11_DIVIDE)),
    actions=[
        CallCommand(cmd=cmd_window_and_login.cmd_CenterOverlapLayout)
    ],
    script=script,
)


#---
hk_BatchLogin = Hotkey(
    name="BatchLogin",
    key=keyname.SCROLOCK_ON(keyname.CTRL_ALT_(keyname.S)),
    actions=[
        CallCommand(
            cmd=cmd_window_and_login.cmd_BatchLogin,
        )
    ],
    script=script,
)


#---
for key, window, account in zip(
        keyname.F1_to_F22,
        Config.Windows.batch_login_windows,
        Config.Windows.batch_login_accounts
):
    window_name = f"WoW{window}"
    username = Config.Credential.account_sequence()[account - 1]["username"]
    password = Config.Credential.account_sequence()[account - 1]["password"]
    hk = Hotkey(
        name=f"SingleLogin{username.title()}",
        key=keyname.SCROLOCK_ON(keyname.CTRL_SHIFT_ALT(key)),
        actions=[
            cmd_window_and_login.cmd_EnterUsernamePasssword.call(window_name, username, password)
        ],
        script=script,
    )