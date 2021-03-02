# -*- coding: utf-8 -*-

"""

如果你不知道该设置什么键, 则注释掉所有的actions即可. 或是用 ``<SendFocusWin>`` 发送到当前
焦点窗口

"""

from . import act
from .config import Config, different_labels
from .script import script
from ... import keyname
from ...script import (
    Hotkey,
    Key, SendLabel,
)

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
            to=Config.SendLabelTo.all(),
            actions=[
                act.General.MOUNT_DOWN
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
        SendLabel(
            name="",
            to=Config.SendLabelTo.all(),
            actions=[
                Key.trigger()
            ]
        )
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
            to=Config.SendLabelTo.all(),
            actions=[
                Key.trigger()
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
            name="",
            to=Config.SendLabelTo.all(),
            actions=[
                Key.trigger()
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
    name="Ctrl T",
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
            to=Config.SendLabelTo.all_boomkin_druid,
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
            name="all_dk",
            to=Config.SendLabelTo.all_dps_dk(),
            actions=[
                act.DK.ALL_SPEC_DEATH_AND_DECAY_ALT_X,
            ]
        ),
        SendLabel(
            name="all_hunter",
            to=Config.SendLabelTo.all_hunter(),
            actions=[
                act.Hunter.ALL_SPEC_VOLLEY_ALT_X,
            ]
        ),
        SendLabel(
            name="all_druid",
            to=Config.SendLabelTo.all_boomkin_druid,
            actions=[
                act.Druid.ALL_SPEC_HURRICANE,
            ]
        ),
        SendLabel(
            name="all_warlock",
            to=Config.SendLabelTo.all_warlock(),
            actions=[
                act.Warlock.ALL_SPEC_RAIN_OF_FIRE,
            ]
        ),
        SendLabel(
            name="all_mage",
            to=Config.SendLabelTo.all_mage(),
            actions=[
                act.Mage.ALL_SPEC_BLIZZARD,
            ]
        ),
    ],
    script=script,
)

_ACTION_BAR_2_________________________________ = ""

hk_r = Hotkey(
    name="R Interrupt Spell",
    key=keyname.SCROLOCK_ON(keyname.R),
    actions=[
        # paladin
        SendLabel(
            name="all_protect_pala",
            to=Config.SendLabelTo.all_protect_pala,
            actions=[
                Key.trigger(),
            ]
        ),
        SendLabel(
            name="all_holy_pala",
            to=Config.SendLabelTo.all_holy_pala,
            actions=[
                act.Target.TARGET_RAID,
                act.Paladin.HOLY_SPEC_ONE_MINUTE_HEAL_ROTATION_MACRO_KEY_2,
            ]
        ),
        # death knight
        SendLabel(
            name="all_unholy_tank_dk",
            to=Config.SendLabelTo.all_unholy_tank_dk,
            actions=[
                act.DK.ALL_SPEC_MIND_FREEZE,
            ]
        ),
        SendLabel(
            name="all_blood_tank_dk",
            to=Config.SendLabelTo.all_blood_tank_dk,
            actions=[
                act.DK.ALL_SPEC_MIND_FREEZE,
            ]
        ),
        # hunter
        SendLabel(
            name="all_marksman_hunter",
            to=Config.SendLabelTo.all_marksman_hunter,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Hunter.MARKSMAN_SPEC_DPS_ROTATE_MACRO,
            ]
        ),
        SendLabel(
            name="all_survival_hunter",
            to=Config.SendLabelTo.all_survival_hunter,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Hunter.SURVIVAL_SPEC_DPS_ROTATE_MACRO,
            ]
        ),
        SendLabel(
            name="all_beast_hunter",
            to=Config.SendLabelTo.all_beast_hunter,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Hunter.BEAST_SPEC_DPS_ROTATE_MACRO,
            ]
        ),
        # shaman
        SendLabel(
            name="all_elemental_shaman",
            to=Config.SendLabelTo.all_elemental_shaman,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Shaman.ALL_SPEC_WIND_SHEAR_MACRO,
            ]
        ),
        SendLabel(
            name="all_enhancement_shaman",
            to=Config.SendLabelTo.all_enhancement_shaman,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Shaman.ALL_SPEC_WIND_SHEAR_MACRO,
            ]
        ),
        SendLabel(
            name="all_resto_shaman",
            to=Config.SendLabelTo.all_resto_shaman,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Shaman.ALL_SPEC_WIND_SHEAR_MACRO,
            ]
        ),
        # druid
        SendLabel(
            name="all_boomkin_druid",
            to=Config.SendLabelTo.all_boomkin_druid,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Druid.BALANCE_SPEC_DPS_ROTATE_MACRO,
            ]
        ),
        SendLabel(
            name="all_resto_druid",
            to=Config.SendLabelTo.all_resto_druid,
            actions=[
                act.Druid.RESTO_SPEC_HEAL_RAID_MACRO_KEY_2,
            ]
        ),

        # mage
        SendLabel(
            name="all_arcane_mage",
            to=Config.SendLabelTo.all_arcane_mage,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO,
            ]
        ),
        SendLabel(
            name="all_fire_mage",
            to=Config.SendLabelTo.all_fire_mage,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO,
            ]
        ),
        SendLabel(
            name="all_frost_mage",
            to=Config.SendLabelTo.all_frost_mage,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Mage.ALL_SPEC_COUNTER_SPELL_MACRO,
            ]
        ),
        # warlock
        SendLabel(
            name="all_demonic_warlock",
            to=Config.SendLabelTo.all_demonic_warlock,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Warlock.DEMON_SPEC_DPS_ROTATE,
            ]
        ),
        SendLabel(
            name="all_affiliate_warlock",
            to=Config.SendLabelTo.all_affiliate_warlock,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Warlock.AFFLICTION_SPEC_DPS_ROTATE,
            ]
        ),
        SendLabel(
            name="all_destruction_warlock",
            to=Config.SendLabelTo.all_destruction_warlock,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Warlock.DESTRUCTION_SPEC_DPS_ROTATE,
            ]
        ),
        # priest
        SendLabel(
            name="all_shadow_priest",
            to=Config.SendLabelTo.all_shadow_priest,
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                act.Priest.SHADOW_SPEC_DPS_ROTATE_SPEC,
            ]
        ),
        SendLabel(
            name="all_disco_priest",
            to=Config.SendLabelTo.all_disco_priest,
            actions=[
                act.Priest.DISC_SPEC_HEAL_RAID_MACRO_KEY_2,
            ]
        ),
        SendLabel(
            name="all_holy_priest",
            to=Config.SendLabelTo.all_holy_priest,
            actions=[
                act.Priest.HOLY_SPEC_HEAL_RAID_MACRO_KEY_2,
            ]
        ),
    ],
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
            name="",
            to=Config.SendLabelTo.all_dispeler(),
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

hk_shift_insert = Hotkey(
    name="Shift Insert",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.INSERT)),
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


hk_shift_home = Hotkey(
    name="Shift Home",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.HOME)),
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


hk_shift_page_up = Hotkey(
    name="Shift PageUp",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.PAGE_UP)),
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


hk_shift_delete = Hotkey(
    name="Shift Delete",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.DELETE)),
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


hk_shift_end = Hotkey(
    name="Shift End",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.END)),
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


hk_shift_page_down = Hotkey(
    name="Shift PageDown",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.PAGE_DOWN)),
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


hk_alt_insert = Hotkey(
    name="Alt Insert",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.INSERT)),
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


hk_alt_home = Hotkey(
    name="Alt Home",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.HOME)),
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


hk_alt_page_up = Hotkey(
    name="Alt PageUp",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.PAGE_UP)),
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


hk_alt_delete = Hotkey(
    name="Alt Delete",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.DELETE)),
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


hk_alt_end = Hotkey(
    name="Alt End",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.END)),
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


hk_alt_page_down = Hotkey(
    name="Alt PageDown",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.PAGE_DOWN)),
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

_ACTION_BAR_UNDEFINED = ""


hk_alt_shift_f_all_boomkin_star_fall = Hotkey(
    name="Alt Shift F",
    key=keyname.SCROLOCK_ON(keyname.ALT_SHIFT_(keyname.F)),
    actions=[
        SendLabel(
            name="",
            to=Config.SendLabelTo.all_boomkin_druid,
            actions=[
                act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F
            ]
        )
    ],
    script=script,
)
