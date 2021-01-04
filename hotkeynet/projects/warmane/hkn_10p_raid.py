# -*- coding: utf-8 -*-

from .config import Config

Config.WRONG_PASSWORD_POP_UP_X = Config.WRONG_PASSWORD_POP_UP_X_AT_1920_1080
Config.WRONG_PASSWORD_POP_UP_Y = Config.WRONG_PASSWORD_POP_UP_Y_AT_1920_1080
Config.USERNAME_INPUT_BOX_X = Config.USERNAME_INPUT_BOX_X_AT_1920_1080
Config.USERNAME_INPUT_BOX_Y = Config.USERNAME_INPUT_BOX_Y_AT_1920_1080

from . import hkn_base

hkn_base.cmd_LaunchAndRenameGameClientWindow = hkn_base.cmd_LaunchAndRenameWoW1ToWoW10
hkn_base.cmd_ResizeAndRelocateWindowToCenter = hkn_base.cmd_ResizeAndRelocateWindowToCenter1800x1012
hkn_base.cmd_BatchLogin = hkn_base.cmd_BatchLoginFatmulti1To10

hkn_base.hk_RoundRobinToggleWindow = hkn_base.hk_RoundRobinToggleWindow_10W_10P_WoW1ToWoW10
hkn_base.hk_ToggleToSpecificWindow_list = hkn_base.hk_ToggleToSpecificWindow_list_WoW1ToWoW10

hkn_base.hk_SingleLogin_list = hkn_base.hk_SingleLogin_list_fatmulti1_to_18

script = hkn_base.create_script()
