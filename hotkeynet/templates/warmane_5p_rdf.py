# -*- coding: utf-8 -*-

from .warmane_config import Config

Config.WRONG_PASSWORD_POP_UP_X = Config.WRONG_PASSWORD_POP_UP_X_AT_1920_1080
Config.WRONG_PASSWORD_POP_UP_Y = Config.WRONG_PASSWORD_POP_UP_Y_AT_1920_1080
Config.USERNAME_INPUT_BOX_X = Config.USERNAME_INPUT_BOX_X_AT_1920_1080
Config.USERNAME_INPUT_BOX_Y = Config.USERNAME_INPUT_BOX_Y_AT_1920_1080

from . import warmane

warmane.cmd_LaunchAndRenameGameClientWindow = warmane.cmd_LaunchAndRenameWoW1ToWoW5
warmane.cmd_BatchLogin = warmane.cmd_BatchLoginFatmulti1To5

warmane.hk_RoundRobinToggleWindow = warmane.hk_RoundRobinToggleWindow_5W_5P_WoW1ToWoW5
warmane.hk_ToggleToSpecificWindow_list = warmane.hk_ToggleToSpecificWindow_list_WoW1ToWoW5

warmane.hk_SingleLogin_list = warmane.hk_SingleLogin_list_fatmulti1_to_18

script = warmane.create_base_script()
