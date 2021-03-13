# -*- coding: utf-8 -*-

"""
实现 Shift + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
"""

from ._config_and_script import config, script
from .. import act
from ..constant.talent_category_association import TC
from .... import keyname
from ....script import (
    Hotkey, SendLabel,
)


def build_hk_shift_numpad_1():
    return Hotkey(
        name="Shift Numpad1",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_SHIFT_1_END),
        actions=[
            SendLabel(
                name=TC.shaman.name,
                to=config.lbs_by_tc(TC.shaman),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.Shaman.ALL_SPEC_CALL_OF_THE_ELEMENTS,
                ]
            )
        ],
        script=script,
    )


hk_shift_numpad_1 = build_hk_shift_numpad_1()


def build_hk_shift_numpad_2():
    return Hotkey(
        name="Shift Numpad2",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_SHIFT_2_DOWN),
        actions=[
            SendLabel(
                name=TC.shaman.name,
                to=config.lbs_by_tc(TC.shaman),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.Shaman.ALL_SPEC_TOTEMIC_RECALL,
                ]
            )
        ],
        script=script,
    )


hk_shift_numpad_2 = build_hk_shift_numpad_2()
