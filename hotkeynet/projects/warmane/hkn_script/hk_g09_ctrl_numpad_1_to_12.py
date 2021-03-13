# -*- coding: utf-8 -*-

"""
实现 Ctrl + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
"""

from .. import act
from ._config_and_script import config, script
from .... import keyname
from ....script import (
    Hotkey, SendLabel,
)
from ..constant.talent_category_association import T, TC


def build_hk_ctrl_numpad_1_silence_shot_focus_target():
    return Hotkey(
        name="Ctrl Numpad1",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.NUMPAD_1)),
        actions=[
            SendLabel(
                name=TC.hunter.name,
                to=config.lbs_by_tc(TC.hunter),
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
                name=TC.mage.name,
                to=config.lbs_by_tc(TC.mage),
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
                name=TC.shaman.name,
                to=config.lbs_by_tc(TC.shaman),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.Shaman.ALL_SPEC_PURGE,
                ]
            ),
            SendLabel(
                name=TC.priest.name,
                to=config.lbs_by_tc(TC.priest),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
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
                name=TC.priest_shadow.name,
                to=config.lbs_by_tc(TC.priest_shadow),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
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
                name=TC.druid_balance.name,
                to=config.lbs_by_tc(TC.druid_balance),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
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
                to=config.lbs_by_tc(TC.shaman_elemental),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
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
                name=TC.priest.name,
                to=config.lbs_by_tc(TC.priest),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
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
                name=TC.priest.name,
                to=config.lbs_by_tc(TC.priest),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
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
                name="tank1",
                to=config.lbs_tank1(),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.Paladin.PROTECT_SPEC_KEY_Z_HAND_OF_RECKONING,
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
                name="tank2",
                to=config.lbs_tank2(),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.DK.ALL_SPEC_DARK_COMMAND_KEY_Z,
                ]
            )
        ],
        script=script,
    )


hk_ctrl_numpad_12 = build_hk_ctrl_numpad_12_tank_2_taunt()
