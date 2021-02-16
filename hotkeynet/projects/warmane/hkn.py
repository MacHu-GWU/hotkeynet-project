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
from ... import keyname
from ...script import Hotkey, SendLabel

class Mode:
    """
    各种特殊战斗模式情况下, 在基础的各职业的经典键位设置下, 对 Hotkeynet 脚本进行额外的修改
    """
    def batlefury_luxiaofeng_high_gs_team_solo_raid_onyxia(self):
        """
        """
        send_label = hk_1_to_12.hk_1.get_send_label_by_name("all_holy_pala")
        send_label.actions = [
            act.Target.TARGET_W1_BATLEFURY,
            act.Paladin.HOLY_SPEC_ONE_MINUTE_HEAL_ROTATION_MACRO_KEY_1,
        ]

        send_label = hk_1_to_12.hk_2.get_send_label_by_name("all_holy_pala")
        send_label.actions = [
            act.Target.TARGET_W1_BATLEFURY,
            act.Paladin.HOLY_SPEC_ONE_MINUTE_HEAL_ROTATION_MACRO_KEY_2,
        ]

        hk_c = Hotkey(
            name="Fear Ward on DK",
            key=keyname.SCROLOCK_ON(keyname.C),
            actions=[
                SendLabel(
                    name="all_shadow_priest",
                    to=Config.SendLabelTo.all_shadow_priest,
                    actions=[
                        act.Target.TARGET_W10_LUXIAOFENG,
                        act.General.STOP_CASTING,
                        act.Priest.ALL_SPEC_FEAR_WARD,
                    ]
                )
            ],
            script=script,
        )

        hk_v = Hotkey(
            name="Raid Defence CD",
            key=keyname.SCROLOCK_ON(keyname.V),
            actions=[
                SendLabel(
                    name="all_protect_pala",
                    to=Config.SendLabelTo.all_protect_pala,
                    actions=[
                        act.Paladin.ALL_SPEC_DIVINE_SACRIFICE,
                    ]
                ),
                SendLabel(
                    name="all_holy_pala",
                    to=Config.SendLabelTo.all_holy_pala,
                    actions=[
                        act.General.STOP_CASTING,
                        act.Paladin.ALL_SPEC_AURA_MASTERY,
                    ]
                ),
            ],
            script=script,
        )

        hk_b = Hotkey(
            name="Protect Pala Personal CD",
            key=keyname.SCROLOCK_ON(keyname.B),
            actions=[
                SendLabel(
                    name="all_protect_pala",
                    to=Config.SendLabelTo.all_protect_pala,
                    actions=[
                        act.Paladin.ALL_SPEC_DIVINE_PROTECTION,
                    ]
                ),
            ],
            script=script,
        )

    #--- ICC
    def batlefury_luxiaofeng_high_gs_team_solo_raid_icc_1_marrowgar(self):




mode = Mode()

try:
    getattr(mode, Config.combat_mode)()
except AttributeError:
    pass
