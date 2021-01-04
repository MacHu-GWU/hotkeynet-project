# -*- coding: utf-8 -*-

from .config import Config
from ... import keyname
from ...script import (
    Script, Command, Hotkey, SendLabel,
    CallCommand,
)

hk_numpad8_SyncLeftClick = Hotkey(
    name="SyncLeftClick",
    key=keyname.SCROLOCK_ON(keyname.NUMPAD_8),
    actions=[
        SendLabel(
            to=[]
        )
    ]
)