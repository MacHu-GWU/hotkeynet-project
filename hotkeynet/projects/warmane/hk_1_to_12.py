# -*- coding: utf-8 -*-

from . import act
from .script import script
from .config import Config
from ... import keyname
from ...script import (
    Script, Command, Hotkey,
    Key, Mouse, SendLabel,
    CallCommand,
)

hk_1 = Hotkey(
    name="Key1",
    key=keyname.SCROLOCK_ON(keyname.KEY_1),
    actions=[
        SendLabel(
            to=Config.SendLabelTo.all_protect_pala,
            actions=[
                Key.trigger(),
            ]
        )
    ],
    script=script,
)