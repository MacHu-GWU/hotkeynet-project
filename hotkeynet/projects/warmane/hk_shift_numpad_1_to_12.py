# -*- coding: utf-8 -*-

from . import act
from .script import script
from .config import Config, different_labels
from ... import keyname
from ...script import (
    Hotkey, SendLabel,
)

def build_hk_shift_numpad_1():
    return Hotkey(
        name="Shift Numpad1",
        key=keyname.SCROLOCK_ON(keyname.NUMPAD_SHIFT_1_END),
        actions=[
            SendLabel(
                name="all_shaman",
                to=Config.SendLabelTo.all_shaman(),
                actions=[
                    act.General.STOP_CASTING,
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
                name="all_shaman",
                to=Config.SendLabelTo.all_shaman(),
                actions=[
                    act.General.STOP_CASTING,
                    act.Shaman.ALL_SPEC_TOTEMIC_RECALL,
                ]
            )
        ],
        script=script,
    )

hk_shift_numpad_2 = build_hk_shift_numpad_2()
#
# hk_shift_numpad_1 = build_hk_shift_numpad_1()
#
#
# def build_hk_ctrl_numpad_2_counter_spell_focus_target():
#     return Hotkey(
#         name="Ctrl Numpad2",
#         key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_2)),
#         actions=[
#             SendLabel(
#                 name="all_mage",
#                 to=Config.SendLabelTo.all_mage(),
#                 actions=[
#                     act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO,
#                 ]
#             )
#         ],
#         script=script,
#     )
#
#
# hk_ctrl_numpad_2 = build_hk_ctrl_numpad_2_counter_spell_focus_target()