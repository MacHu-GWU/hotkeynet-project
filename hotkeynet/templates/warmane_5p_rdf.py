# -*- coding: utf-8 -*-

from .warmane_config import Config

Config.WRONG_PASSWORD_POP_UP_X = Config.WRONG_PASSWORD_POP_UP_X_AT_1920_1080
Config.WRONG_PASSWORD_POP_UP_Y = Config.WRONG_PASSWORD_POP_UP_Y_AT_1920_1080
Config.USERNAME_INPUT_BOX_X = Config.USERNAME_INPUT_BOX_X_AT_1920_1080
Config.USERNAME_INPUT_BOX_Y = Config.USERNAME_INPUT_BOX_Y_AT_1920_1080

from . import warmane

warmane.cmd_LaunchAndRenameGameClientWindow = warmane.cmd_LaunchAndRenameWoW1ToWoW5

script = warmane.create_base_script()
