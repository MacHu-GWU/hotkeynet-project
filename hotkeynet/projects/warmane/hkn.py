# -*- coding: utf-8 -*-

from . config import Config

from .script import script
from . import cmd_window_and_login

from . import label
from . import hk_window_and_login
from . import hk_1_to_12
from . import hk_numpad_1_to_12
from . import hk_skills
from . import hk_movement
from . import hk_utility
from . import hk_ctrl_1_6
from . import hk_healbot

from . import post_hook
from . import hk_alt_numpad_1_to_12
from . import hk_ctrl_numpad_1_to_12
from . import hk_shift_numpad_1_to_12
from . import hk_control_panel

from . import act

class Mode:
    def batlefury_luxiaofeng_high_gs_team_solo_raid_onyxia(self):
        # print(hk_1_to_12.hk_1.actions)
        send_label = hk_1_to_12.hk_1.get_send_label_by_name("all_holy_pala")

        send_label.actions = [
            act.Target
        ]
        print(send_label)
        print("="* 100)
        print(Config.SendLabelTo.all_resto_druid)
        # print("123123")


mode = Mode()

try:
    getattr(mode, Config.combat_mode)()
except AttributeError:
    pass
