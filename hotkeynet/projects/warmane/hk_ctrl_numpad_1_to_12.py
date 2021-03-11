# -*- coding: utf-8 -*-

from . import act
from .script import script
from .config_ import Config, different_labels
from ... import keyname
from ...script import (
    Hotkey, SendLabel,
)

def build_hk_ctrl_numpad_1_silence_shot_focus_target():
    return Hotkey(
        name="Ctrl Numpad1",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_1)),
        actions=[
            SendLabel(
                name="all_hunter",
                to=Config.SendLabelTo.all_hunter(),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Hunter.MARKSMAN_SPEC_SILENCING_SHOT,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_1 = build_hk_ctrl_numpad_1_silence_shot_focus_target()


def build_hk_ctrl_numpad_2_counter_spell_focus_target():
    return Hotkey(
        name="Ctrl Numpad2",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_2)),
        actions=[
            SendLabel(
                name="all_mage",
                to=Config.SendLabelTo.all_mage(),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_2 = build_hk_ctrl_numpad_2_counter_spell_focus_target()


def build_hk_ctrl_numpad_3_aggressive_dispel():
    return Hotkey(
        name="Ctrl Numpad3",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_3)),
        actions=[
            SendLabel(
                name="all_shaman",
                to=Config.SendLabelTo.all_shaman(),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.General.STOP_CASTING,
                    act.Shaman.ALL_SPEC_PURGE,
                ]
            ),
            SendLabel(
                name="all_priest",
                to=Config.SendLabelTo.all_priest(),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.General.STOP_CASTING,
                    act.Priest.ALL_SPEC_DISPEL_MAGIC,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_3 = build_hk_ctrl_numpad_3_aggressive_dispel()


def build_hk_ctrl_numpad_4_aoe_fear():
    return Hotkey(
        name="Ctrl Numpad4",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_4)),
        actions=[
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.General.STOP_CASTING,
                    act.Priest.SHADOW_SPEC_PSYCHIC_HORROR,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_4 = build_hk_ctrl_numpad_4_aoe_fear()


def build_hk_ctrl_numpad_5_typhoon():
    return Hotkey(
        name="Ctrl Numpad5",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_5)),
        actions=[
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                    act.General.STOP_CASTING,
                    act.Druid.BALANCE_SPEC_TYPHOON_KEY_G,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_5 = build_hk_ctrl_numpad_5_typhoon()


def build_hk_ctrl_numpad_6_thunder_storm():
    return Hotkey(
        name="Ctrl Numpad6",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_6)),
        actions=[
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.General.STOP_CASTING,
                    act.Shaman.ELEMENTAL_SPEC_THUNDER_STORM,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_6 = build_hk_ctrl_numpad_6_thunder_storm()


def build_hk_ctrl_numpad_7_hymn_of_life():
    return Hotkey(
        name="Ctrl Numpad7",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_7)),
        actions=[
            SendLabel(
                name="all_priest",
                to=Config.SendLabelTo.all_priest(),
                actions=[
                    act.General.STOP_CASTING,
                    act.Priest.ALL_SPEC_DIVINE_HYMN,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_7 = build_hk_ctrl_numpad_7_hymn_of_life()



def build_hk_ctrl_numpad_10_hymn_of_mana():
    return Hotkey(
        name="Ctrl Numpad10",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_0)),
        actions=[
            SendLabel(
                name="all_priest",
                to=Config.SendLabelTo.all_priest(),
                actions=[
                    act.General.STOP_CASTING,
                    act.Priest.ALL_SPEC_HYMN_OF_HOPE,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_10 = build_hk_ctrl_numpad_10_hymn_of_mana()


def build_hk_ctrl_numpad_11_tank_1_taunt():
    return Hotkey(
        name="Ctrl Numpad11",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_11_DIVIDE)),
        actions=[
            SendLabel(
                name="leader_1",
                to=Config.SendLabelTo.leader_1,
                actions=[
                    act.General.STOP_CASTING,
                    act.Paladin.PROTECT_SPEC_HAND_OF_RECKONING,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_11 = build_hk_ctrl_numpad_11_tank_1_taunt()


def build_hk_ctrl_numpad_12_tank_2_taunt():
    return Hotkey(
        name="Ctrl Numpad12",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_12_MULTIPLY)),
        actions=[
            SendLabel(
                name="leader_2",
                to=Config.SendLabelTo.leader_2,
                actions=[
                    act.General.STOP_CASTING,
                    act.DK.ALL_SPEC_DARK_COMMAND,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_12 = build_hk_ctrl_numpad_12_tank_2_taunt()
