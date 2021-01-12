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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_tab = Hotkey(
    name="Shift Tab",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.TAB)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_e = Hotkey(
    name="Ctrl E",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.E)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

_ACTION_BAR_4_________________________________ = ""

hk_middle_click = Hotkey(
    name="MButton",
    key=keyname.SCROLOCK_ON(keyname.MOUSE_MButton),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_middle_click = Hotkey(
    name="Shift MButton",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.MOUSE_MButton)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_oem3_wave = Hotkey(
    name="Ctrl Oem3",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.OEM3_WAVE)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_shift_oem3_wave = Hotkey(
    name="Shift Oem3",
    key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.OEM3_WAVE)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_oem3_wave = Hotkey(
    name="Alt Oem3",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.OEM3_WAVE)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_z = Hotkey(
    name="Ctrl Z",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.Z)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_t = Hotkey(
    name="Ctrl T",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.T)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_ctrl_g = Hotkey(
    name="Ctrl G",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.G)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_alt_x = Hotkey(
    name="Alt X",
    key=keyname.SCROLOCK_ON(keyname.ALT_(keyname.X)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

_ACTION_BAR_2_________________________________ = ""

hk_r = Hotkey(
    name="R",
    key=keyname.SCROLOCK_ON(keyname.R),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_z = Hotkey(
    name="Z",
    key=keyname.SCROLOCK_ON(keyname.Z),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_t = Hotkey(
    name="T",
    key=keyname.SCROLOCK_ON(keyname.T),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)

hk_g = Hotkey(
    name="G",
    key=keyname.SCROLOCK_ON(keyname.G),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
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
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)


hk_ctrl_insert = Hotkey(
    name="Ctrl Insert",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.INSERT)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)


hk_ctrl_home = Hotkey(
    name="Ctrl Home",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.HOME)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)


hk_ctrl_page_up = Hotkey(
    name="Ctrl PageUp",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.PAGE_UP)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)


hk_ctrl_delete = Hotkey(
    name="Ctrl Delete",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.DELETE)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)


hk_ctrl_end = Hotkey(
    name="Ctrl End",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.END)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)


hk_ctrl_page_down = Hotkey(
    name="Ctrl PageDown",
    key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.PAGE_DOWN)),
    actions=[
        # SendLabel(
        #     name="",
        #     to=Config.SendLabelTo.all,
        #     actions=[
        #         Key.trigger()
        #     ]
        # )
    ],
    script=script,
)