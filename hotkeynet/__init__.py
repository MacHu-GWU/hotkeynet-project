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
        Command,
        CommandArgEnum,
        Context,
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
    )

except ImportError as e:
    pass
except:
    raise