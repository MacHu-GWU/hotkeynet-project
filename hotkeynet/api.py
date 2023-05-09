# -*- coding: utf-8 -*-

"""
Stable API.
"""

from . import keyname as KN
from . import canned as CAN
from .maker import (
    KeyMaker,
    ClickMaker,
    ModifiedClickMaker,
)

from .script import (
    context,
    Block,
    Script,
    SendModeEnum,
    Label,
    Command,
    CommandArgEnum,
    CallCommand,
    SendPC,
    Run,
    Hotkey,
    MovementHotkey,
    Key,
    KeyUp,
    KeyDown,
    SendLabel,
    MouseButtonEnum,
    MouseStrokeEnum,
    MouseTargetEnum,
    MouseModeEnum,
    ClickMouse,
    MoveMouse,
    RenameWin,
    TargetWin,
    Wait,
    WaitForWin,
    WaitForWinEnabled,
    SetForegroundWin,
    SetActiveWin,
    Toggle,
    ToggleHotkeys,
    ToggleWin,
    SendWin,
    SendWinM,
    SendWinMF,
    SendWinS,
    SendWinSF,
    SendFocusWin,
    SetWinPos,
    SetWinSize,
    SetWinRect,
    Text,
    CreatePanel,
    CreateButton,
    CreatePictureButton,
    CreateColoredButton,
    AddButtonToPanel,
    SetButtonHotkey,
    SetButtonCommand,
    AlwaysOnTop,
    SetPanelLayout,
)
