# -*- coding: utf-8 -*-

"""
实现 Ctrl 1 ~ 6 的功能. 主要是宠物的动作条按键. 1 进攻主人目标, 2 撤回, 3 原地待命.
"""

from ._config_and_script import config, script
from .. import act
from .... import keyname
from ....script import (
    Hotkey, SendLabel,
)


def build_hk_ctrl_1_6():
    return [
        Hotkey(
            name="Ctrl {}".format(i),
            key=keyname.SCROLOCK_ON(keyname.CTRL_(getattr(keyname, "KEY_{}".format(i)))),
            actions=[
                SendLabel(
                    name="all",
                    to=config.lbs_all(),
                    actions=[
                        act.Target.TARGET_FOCUS_TARGET,
                        act.General.TRIGGER,
                    ]
                )
            ],
            script=script,
        ) for i in range(1, 6 + 1)
    ]


(
    hk_ctrl_1,
    hk_ctrl_2,
    hk_ctrl_3,
    hk_ctrl_4,
    hk_ctrl_5,
    hk_ctrl_6,
) = build_hk_ctrl_1_6()
