# -*- coding: utf-8 -*-

"""
Ctrl 1 ~ 6 主要是宠物的动作条设置
"""

from . import act
from .script import script
from .config_ import Config
from ... import keyname
from ...script import (
    Hotkey,
    Key, Mouse, SendLabel,
)

def build_hk_ctrl_1_6():
    return [
        Hotkey(
            name="Ctrl {}".format(i),
            key=keyname.SCROLOCK_ON(keyname.CTRL_(getattr(keyname, "KEY_{}".format(i)))),
            actions=[
                SendLabel(
                    name="all",
                    to=Config.SendLabelTo.all(),
                    actions=[
                        act.Target.TARGET_FOCUS_TARGET,
                        Key.trigger(),
                    ]
                )
            ],
            script=script,
        ) for i in range(1, 6+1)
    ]

(
    hk_ctrl_1,
    hk_ctrl_2,
    hk_ctrl_3,
    hk_ctrl_4,
    hk_ctrl_5,
    hk_ctrl_6,
) = build_hk_ctrl_1_6()
