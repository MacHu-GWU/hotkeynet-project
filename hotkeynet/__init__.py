# -*- coding: utf-8 -*-

"""
Package Description.
"""


from ._version import __version__

__short_description__ = "Package short description."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from . import keyname
    KN = keyname

    from .script import (
        context,
        Command,
        CommandArgEnum,
        Hotkey,
        Key,
        KeyDown,
        KeyUp,
        Label,
        ModifiedMouseClick,
        Mouse,
        MouseButtonEnum,
        MovementHotkey,
        RenameWin,
        Run,
        Script,
        SendLabel,
        SendModeEnum,
        SendPC,
        SetActiveWin,
        SetForegroundWin,
        TargetWin,
        Toggle,
        ToggleHotkeys,
        ToggleWin,
        Wait,
        SendWin,
        SendWinM,
        SendWinMF,
        SendWinS,
        SendWinSF,
        SetWinPos,
        SetWinRect,
        SetWinSize,
        Text,
    )

except ImportError as e:
    pass
except:
    raise