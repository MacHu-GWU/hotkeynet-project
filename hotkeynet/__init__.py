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
        AddButtonToPanel,
        AlwaysOnTop,
        Command,
        CommandArgEnum,
        CreateButton,
        CreatePanel,
        CreatePictureButton,
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
        render,
        Run,
        Script,
        SendFocusWin,
        SendLabel,
        SendModeEnum,
        SendPC,
        SendWin,
        SendWinM,
        SendWinMF,
        SendWinS,
        SendWinSF,
        SetActiveWin,
        SetButtonCommand,
        SetButtonHotkey,
        SetForegroundWin,
        SetWinPos,
        SetWinRect,
        SetWinSize,
        TargetWin,
        Text,
        Toggle,
        ToggleHotkeys,
        ToggleWin,
        Wait,
        WaitForWin,
        WaitForWinEnabled,
    )

except ImportError as e:
    pass
except:
    raise