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
print(Config.SendLabelTo.all_unholy_tank_dk)
hk_1 = Hotkey(
    name="Key1",
    key=keyname.SCROLOCK_ON(keyname.KEY_1),
    actions=[
        SendLabel(
            to=Config.SendLabelTo.all_protect_pala,
            actions=[
                Key.trigger(),
            ]
        ),
        SendLabel(
            to=Config.SendLabelTo.all_holy_pala,
            actions=[
                act.Paladin.HOLY_SPEC_ONE_MINUTE_HEAL_ROTATION_KEY_1,
            ]
        ),
        SendLabel(
            to=Config.SendLabelTo.all_unholy_tank_dk,
            actions=[
                Key.trigger(),
            ]
        ),
        SendLabel(
            to=Config.SendLabelTo.all_marksman_hunter,
            actions=[
                act.Hunter.ALL_SPEC_FREEZING_ARROW,
            ]
        ),
    ],
    script=script,
)