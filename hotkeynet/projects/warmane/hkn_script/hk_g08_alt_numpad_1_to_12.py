# -*- coding: utf-8 -*-

"""
实现 Alt + 小键盘 1-12 的快捷键功能. 通常是一些不常用, 但是关键时刻必备的技能.
"""

from ._config_and_script import config, script
from .. import act
from ..constant.talent_category_association import TC
from .... import keyname
from ....script import (
    Hotkey, SendLabel,
)
from ....utils import difference_list


def build_hk_alt_numpad_1_misdirect_and_tot_focus():
    return Hotkey(
        name="Alt Numpad1",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_1)),
        actions=[
            SendLabel(
                name=TC.hunter.name,
                to=config.lbs_by_tc(TC.hunter),
                actions=[
                    act.Hunter.ALL_SPEC_MISDIRECTION_FOCUS_MACRO,
                ]
            )
        ],
        script=script,
    )


hk_alt_numpad_1 = build_hk_alt_numpad_1_misdirect_and_tot_focus()


def build_hk_alt_numpad_2_aspect_of_pact_or_hawk():
    return Hotkey(
        name="Alt Numpad2",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_2)),
        actions=[
            SendLabel(
                name=TC.hunter.name,
                to=config.lbs_by_tc(TC.hunter),
                actions=[
                    act.Hunter.ALL_SPEC_ASPECT_OF_PACT_OR_DRAGON_HAWK,
                ]
            )
        ],
        script=script,
    )


hk_alt_numpad_2 = build_hk_alt_numpad_2_aspect_of_pact_or_hawk()


def build_hk_alt_numpad_3_aspect_of_viper_or_hawk():
    return Hotkey(
        name="Alt Numpad3",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_3)),
        actions=[
            SendLabel(
                name=TC.hunter.name,
                to=config.lbs_by_tc(TC.hunter),
                actions=[
                    act.Hunter.ALL_SPEC_ASPECT_OF_VIPER_OR_DRAGON_HAWK,
                ]
            )
        ],
        script=script,
    )


hk_alt_numpad_3 = build_hk_alt_numpad_3_aspect_of_viper_or_hawk()


def build_hk_alt_numpad_4_all_boomy_star_fall():
    return Hotkey(
        name="Alt Numpad4",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_4)),
        actions=[
            SendLabel(
                name=TC.druid_balance.name,
                to=config.lbs_by_tc(TC.druid_balance),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F,
                ]
            )
        ],
        script=script,
    )


hk_alt_numpad_4 = build_hk_alt_numpad_4_all_boomy_star_fall()


def build_hk_alt_numpad_5_all_dps_burst():
    return Hotkey(
        name="Alt Numpad5",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_5)),
        actions=[
            SendLabel(
                name=TC.dps.name,
                to=config.lbs_by_tc(TC.dps),
                actions=[
                    act.General.DPS_BURST_MACRO_KEY_ALT_D,
                ]
            )
        ],
        script=script,
    )


hk_alt_numpad_5 = build_hk_alt_numpad_5_all_dps_burst()


def build_hk_alt_numpad_6_all_dps_burst_and_hero():
    return Hotkey(
        name="Alt Numpad6",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_6)),
        actions=[
            SendLabel(
                name="all_non_shaman_dps",
                to=difference_list(
                    config.lbs_by_tc(TC.dps),
                    config.lbs_by_tc(TC.shaman),
                ),
                actions=[
                    act.General.DPS_BURST_MACRO_KEY_ALT_D,
                ]
            ),
            SendLabel(
                name=TC.shaman_elemental.name,
                to=config.lbs_by_tc(TC.shaman_elemental),
                actions=[
                    act.Shaman.ALL_SPEC_BLOOD_THIRST_HEROISM,
                    act.General.DPS_BURST_MACRO_KEY_ALT_D,
                ]
            ),
            SendLabel(
                name=TC.shaman_resto.name,
                to=config.lbs_by_tc(TC.shaman_resto),
                actions=[
                    act.Shaman.ALL_SPEC_BLOOD_THIRST_HEROISM,
                ]
            ),
        ],
        script=script,
    )


hk_alt_numpad_6 = build_hk_alt_numpad_6_all_dps_burst_and_hero()


def build_hk_alt_numpad_7_8_9_first_raid_damage_reduction():
    hk_alt_numpad_7 = Hotkey(
        name="Alt Numpad7",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_7)),
        actions=[
            SendLabel(
                name=TC.paladin_protect.name,
                to=config.lbs_by_tc(TC.paladin_protect),
                actions=[
                    # 要点两下
                    act.Paladin.ALL_SPEC_DIVINE_SACRIFICE,
                    act.Paladin.ALL_SPEC_DIVINE_SACRIFICE,
                ]
            ),
        ],
        script=script,
    )

    hk_alt_numpad_8 = Hotkey(
        name="Alt Numpad8",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_8)),
        actions=[
            # SendLabel(
            #     name="holy_pala",
            #     to=Config.SendLabelTo.g2_dr_holy_pala,
            #     actions=[
            #         act.Paladin.ALL_SPEC_DIVINE_SACRIFICE,
            #         act.Paladin.ALL_SPEC_DIVINE_SACRIFICE,
            #     ]
            # ),
        ],
        script=script,
    )

    hk_alt_numpad_9 = Hotkey(
        name="Alt Numpad9",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_9)),
        actions=[
            # SendLabel(
            #     name="holy_pala",
            #     to=Config.SendLabelTo.g3_dr_holy_pala,
            #     actions=[
            #         act.Paladin.ALL_SPEC_AURA_MASTERY,
            #         act.Paladin.ALL_SPEC_AURA_MASTERY,
            #     ]
            # ),
        ],
        script=script,
    )

    return hk_alt_numpad_7, hk_alt_numpad_8, hk_alt_numpad_9


(
    hk_alt_numpad_7,
    hk_alt_numpad_8,
    hk_alt_numpad_9,
) = build_hk_alt_numpad_7_8_9_first_raid_damage_reduction()


def build_hk_alt_numpad_10_cleasing_totem():
    return Hotkey(
        name="Alt Numpad10",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_0)),
        actions=[
            SendLabel(
                name=TC.shaman.name,
                to=config.lbs_by_tc(TC.shaman),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.Shaman.ALL_SPEC_CLEANSING_TOTEM,
                ]
            ),
        ],
        script=script,
    )


hk_alt_numpad_10 = build_hk_alt_numpad_10_cleasing_totem()


def build_hk_alt_numpad_11_tremor_totem():
    return Hotkey(
        name="Alt Numpad11",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_11_DIVIDE)),
        actions=[
            SendLabel(
                name=TC.shaman.name,
                to=config.lbs_by_tc(TC.shaman),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.Shaman.ALL_SPEC_TREMOR_TOTEM,
                ]
            ),
        ],
        script=script,
    )


hk_alt_numpad_11 = build_hk_alt_numpad_11_tremor_totem()


def build_hk_alt_numpad_12_earth_binding_totem():
    return Hotkey(
        name="Alt Numpad12",
        key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.NUMPAD_12_MULTIPLY)),
        actions=[
            SendLabel(
                name=TC.shaman.name,
                to=config.lbs_by_tc(TC.shaman),
                actions=[
                    act.General.STOP_CASTING_KEY_OEM1_SEMICOLUMN,
                    act.Shaman.ALL_SPEC_EARTHBIND_TOTEM,
                ]
            ),
        ],
        script=script,
    )


hk_alt_numpad_12 = build_hk_alt_numpad_12_earth_binding_totem()
