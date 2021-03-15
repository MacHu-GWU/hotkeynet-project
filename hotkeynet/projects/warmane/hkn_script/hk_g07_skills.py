# -*- coding: utf-8 -*-

"""
实现每个游戏内所绑定的动作条快捷键, 会触发哪些职业的哪些功能.
"""

from ._config_and_script import config, script
from .. import act
from ..constant.talent_category_association import T, TC
from .... import keyname
from ....script import (
    Hotkey,
    Key, SendLabel,
)
from ....utils import union_list, intersection_list, difference_list

_ACTION_BAR_5_________________________________ = ""

hk_alt_f1 = Hotkey(
    name="Alt F1",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.F1)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_f2 = Hotkey(
    name="Alt F2",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.F2)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_f1 = Hotkey(
    name="Shift F1",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.F1)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_f2 = Hotkey(
    name="Shift F2",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.F2)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_c = Hotkey(
    name="Shift C",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.C)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_r = Hotkey(
    name="Shift R",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.R)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_f = Hotkey(
    name="Shift F",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.F)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_g = Hotkey(
    name="Shift G",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.G)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

# hk_shift_tab = Hotkey(
#     name="Shift Tab",
#     key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.TAB)),
#     actions=[
#         SendLabel(
#             name="",
#             to=Config.SendLabelTo.all_shaman(),
#             actions=[
#                 Key.trigger()
#             ]
#         ),
#         "<SendFocusWin>",
#         Key.trigger(),
#     ],
#     script=script,
# )

hk_ctrl_e = Hotkey(
    name="Ctrl E",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.E)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_r = Hotkey(
    name="Ctrl R",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.R)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_f = Hotkey(
    name="Ctrl F",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.F)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

_ACTION_BAR_4_________________________________ = ""

# hk_middle_click = Hotkey(
#     name="MButton",
#     key=keyname.SCROLOCK_ON(keyname.MOUSE_MButton),
#     actions=[
# SendLabel(
#     name="",
#     to=Config.SendLabelTo.all(),
#     actions=[
#         Key.trigger()
#     ]
# )
#     ],
#     script=script,
# )

hk_shift_middle_click = Hotkey(
    name="Shift MButton",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.MOUSE_MButton)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_middle_click = Hotkey(
    name="Alt MButton",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.MOUSE_MButton)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_oem3_wave = Hotkey(
    name="Ctrl Oem3",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.OEM3_WAVE_OR_BACK_QUOTE)),
    actions=[
        SendLabel(
            name="all",
            to=config.lbs_all(),
            actions=[
                act.General.MOUNT_DOWN_MACRO_CTRL_OEM3_WAVE
            ]
        )
    ],
    script=script,
)

hk_shift_oem3_wave = Hotkey(
    name="Shift Oem3",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.OEM3_WAVE_OR_BACK_QUOTE)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_oem3_wave = Hotkey(
    name="Alt Oem3",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.OEM3_WAVE_OR_BACK_QUOTE)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_a = Hotkey(
    name="Alt A",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.A)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_s = Hotkey(
    name="Alt S",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.S)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_d = Hotkey(
    name="Alt D",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.D)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_e = Hotkey(
    name="Alt E",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.E)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_r = Hotkey(
    name="Alt R",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.R)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_f = Hotkey(
    name="Alt F",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.F)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

_ACTION_BAR_3_________________________________ = ""

hk_shift_z = Hotkey(
    name="Shift Z",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.Z)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_t = Hotkey(
    name="Shift T",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.T)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_x = Hotkey(
    name="Shift X",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.X)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_z_land = Hotkey(
    name="Ctrl Z",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.Z)),
    actions=[
        SendLabel(
            name="",
            to=config.lbs_all(),
            actions=[
                act.General.LAND_MOUNT_SPELL_KEY_CTRL_Z
            ]
        )
    ],
    script=script,
)

hk_ctrl_t = Hotkey(
    name="Ctrl T",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.T)),
    actions=[
        SendLabel(
            name="all",
            to=config.lbs_all(),
            actions=[
                act.General.EAT_FOOD_KEY_CTRL_T
            ]
        )
    ],
    script=script,
)

hk_ctrl_g = Hotkey(
    name="Ctrl G",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.G)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_x = Hotkey(
    name="Ctrl X",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.X)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_z = Hotkey(
    name="Alt Z",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.Z)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_t = Hotkey(
    name="Alt T",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.T)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_g = Hotkey(
    name="Alt G",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.G)),
    actions=[
        SendLabel(
            name="",
            to=config.lbs_by_tc(TC.druid_balance),
            actions=[
                act.Druid.BALANCE_SPEC_TYPHOON_KEY_G,
            ]
        )
    ],
    script=script,
)

hk_alt_x_aoe = Hotkey(
    name="Alt X",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.X)),
    actions=[
        SendLabel(
            name=TC.dk.name,
            to=config.lbs_by_tc(TC.dk),
            actions=[
                # act.General.ESC,
                act.DK.ALL_SPEC_DEATH_AND_DECAY_KEY_ALT_X,
            ]
        ),
        SendLabel(
            name=TC.hunter.name,
            to=config.lbs_by_tc(TC.hunter),
            actions=[
                # act.General.ESC,
                act.Hunter.ALL_SPEC_VOLLEY_ALT_X,
            ]
        ),
        SendLabel(
            name=TC.druid_balance.name,
            to=config.lbs_by_tc(TC.druid_balance),
            actions=[
                # act.General.ESC,
                act.Druid.ALL_SPEC_HURRICANE,
            ]
        ),
        SendLabel(
            name=TC.warlock.name,
            to=config.lbs_by_tc(TC.warlock),
            actions=[
                # act.General.ESC,
                act.Warlock.ALL_SPEC_RAIN_OF_FIRE,
            ]
        ),
        SendLabel(
            name=TC.mage.name,
            to=config.lbs_by_tc(TC.mage),
            actions=[
                # act.General.ESC,
                act.Mage.ALL_SPEC_BLIZZARD,
            ]
        ),
    ],
    script=script,
)

_ACTION_BAR_2_________________________________ = ""

_hk_r_actions = [
    # paladin
    SendLabel(
        name=TC.paladin_protect.name,
        to=config.lbs_by_tc(TC.paladin_protect),
        actions=[
            Key(name=keyname.R),
        ]
    ),
    SendLabel(
        name=TC.paladin_holy.name,
        to=config.lbs_by_tc(TC.paladin_holy),
        actions=[
            act.Paladin.HOLY_SPEC_KEY_R_FOCUS_JUDGEMENT,
        ]
    ),
    # death knight
    SendLabel(
        name=TC.dk_tank.name,
        to=config.lbs_by_tc(TC.dk_tank),
        actions=[
            act.DK.ALL_SPEC_MIND_FREEZE_KEY_R,
        ]
    ),
    SendLabel(
        name=TC.dk_dps.name,
        to=config.lbs_by_tc(TC.dk_dps),
        actions=[
            act.Target.TARGET_FOCUS_TARGET,
            act.DK.ALL_SPEC_MIND_FREEZE_KEY_R,
        ]
    ),
    # hunter
    SendLabel(
        name=TC.hunter_marksman.name,
        to=config.lbs_by_tc(TC.hunter_marksman),
        actions=[
            act.Target.TARGET_FOCUS_TARGET,
            act.Hunter.MARKSMAN_SPEC_DPS_ROTATE_MACRO,
        ]
    ),
    # shaman
    SendLabel(
        name=TC.shaman.name,
        to=config.lbs_by_tc(TC.shaman),
        actions=[
            act.Target.TARGET_FOCUS_TARGET,
            act.Shaman.ALL_SPEC_WIND_SHEAR_MACRO,
        ]
    ),

    # mage
    SendLabel(
        name=TC.mage.name,
        to=config.lbs_by_tc(TC.mage),
        actions=[
            act.Target.TARGET_FOCUS_TARGET,
            act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO,
        ]
    ),
]

special_labels = union_list(*[
    sl.to
    for sl in _hk_r_actions
])

regular_tank_labels = difference_list(
    config.lbs_by_tc(TC.tank),
    special_labels,
)

regular_dps_labels = difference_list(
    config.lbs_by_tc(TC.dps),
    special_labels,
)

regular_healer_labels = difference_list(
    config.lbs_by_tc(TC.healer),
    special_labels,
)

_hk_r_actions.extend([
    SendLabel(
        name="other_tank",
        to=regular_tank_labels,
        actions=[
            Key(name=keyname.KEY_2),
        ]
    ),
    SendLabel(
        name="other_dps",
        to=regular_dps_labels,
        actions=[
            act.Target.TARGET_FOCUS_TARGET,
            Key(name=keyname.KEY_3),
        ]
    ),
    SendLabel(
        name="other_healer",
        to=regular_healer_labels,
        actions=[
            act.Target.TARGET_FOCUS,
            Key(name=keyname.KEY_3),
        ]
    ),
])


hk_r = Hotkey(
    name="R Interrupt Spell",
    key=keyname.SCROLOCK_ON(keyname.R),
    actions=_hk_r_actions,
    script=script,
)


hk_z = Hotkey(
    name="Z",
    key=keyname.SCROLOCK_ON(keyname.Z),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

# pala put cleansing on T
# shaman put curse toxin on T
# druid put remove curse on T
# mage put remove curse on T
# priest put dispel magic on T
hk_t = Hotkey(
    name="T Random Dispel Raid",
    key=keyname.SCROLOCK_ON(keyname.T),
    actions=[
        SendLabel(
            name=TC.dispeler.name,
            to=config.lbs_by_tc(TC.dispeler),
            actions=[
                act.Target.TARGET_RAID,
                Key.trigger()
            ]
        )
    ],
    script=script,
)

hk_g = Hotkey(
    name="G",
    key=keyname.SCROLOCK_ON(keyname.G),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_x = Hotkey(
    name="X",
    key=keyname.SCROLOCK_ON(keyname.X),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all(),
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

_ACTION_BAR_7_8_9_10_____________________________ = ""

# hk_shift_insert = Hotkey(
#     name="Shift Insert",
#     key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.INSERT)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_shift_home = Hotkey(
#     name="Shift Home",
#     key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.HOME)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_shift_page_up = Hotkey(
#     name="Shift PageUp",
#     key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.PAGE_UP)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_shift_delete = Hotkey(
#     name="Shift Delete",
#     key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.DELETE)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_shift_end = Hotkey(
#     name="Shift End",
#     key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.END)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_shift_page_down = Hotkey(
#     name="Shift PageDown",
#     key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.PAGE_DOWN)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_alt_insert = Hotkey(
#     name="Alt Insert",
#     key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.INSERT)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_alt_home = Hotkey(
#     name="Alt Home",
#     key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.HOME)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_alt_page_up = Hotkey(
#     name="Alt PageUp",
#     key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.PAGE_UP)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_alt_delete = Hotkey(
#     name="Alt Delete",
#     key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.DELETE)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_alt_end = Hotkey(
#     name="Alt End",
#     key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.END)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )
#
# hk_alt_page_down = Hotkey(
#     name="Alt PageDown",
#     key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.PAGE_DOWN)),
#     actions=[
#         # SendLabel(
#         #     name="",
#         #     to=Config.SendLabelTo.all(),
#         #     actions=[
#         #         Key.trigger()
#         #     ]
#         # )
#     ],
#     script=script,
# )

_ACTION_BAR_UNDEFINED = ""


hk_alt_shift_f_all_boomkin_star_fall = Hotkey(
    name="Alt Shift F",
    key=keyname.SCROLOCK_ON(keyname.ALT_SHIFT_(keyname.F)),
    actions=[
        SendLabel(
            name=TC.druid_balance.name,
            to=config.lbs_by_tc(TC.druid_balance),
            actions=[
                act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F
            ]
        ),
        SendLabel(
            name=TC.dk.name,
            to=config.lbs_by_tc(TC.dk),
            actions=[
                act.DK.UNHOLY_SPEC_CORPSE_EXPLOSION_ALF_F,
            ]
        ),
    ],
    script=script,
)
