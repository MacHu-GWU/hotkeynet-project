# -*- coding: utf-8 -*-

"""
Healbot 主要是鼠标动作, 用于使用团队框架进行治疗.
"""

from . import act
from .script import script
from .config import Config, union_list, difference_list
from ... import keyname
from ...script import (
    Hotkey,
    Key, Mouse, SendLabel,
)

def build_hk_healbot_small_heal():
    return Hotkey(
        name="Healbot Small Heal",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.MOUSE_LButton)),
        actions=[
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_holy_pala,
                actions=[
                    act.Paladin.HEAL_BOT_RIGHT_CLICK_FLASH_OF_LIGHT,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Shaman.HEAL_BOT_RIPTIDE,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                    act.Druid.HEAL_BOT_LEFT_CLICK_REJUVENATION,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                    act.Priest.HEAL_BOT_POWER_WORD_SHIELD,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[
                    act.Priest.HEAL_BOT_POWER_WORD_SHIELD,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_tank(),
                actions=[
                    Key(name=keyname.KEY_2)
                ]
            ),
            SendLabel(
                name="",
                to=difference_list(
                    Config.SendLabelTo.all(),
                    Config.SendLabelTo.all_holy_pala,
                    Config.SendLabelTo.all_resto_shaman,
                    Config.SendLabelTo.all_resto_druid,
                    Config.SendLabelTo.all_disco_priest,
                    Config.SendLabelTo.all_holy_priest,
                    Config.SendLabelTo.all_tank(),
                ),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key(name=keyname.KEY_2),
                ]
            )
        ],
        script=script,
    )

hk_healbot_small_heal = build_hk_healbot_small_heal()


def build_hk_healbot_big_heal():
    return Hotkey(
        name="Healbot Big Heal",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.MOUSE_RButton)),
        actions=[
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_holy_pala,
                actions=[
                    act.Paladin.HEAL_BOT_LEFT_CLICK_HOLY_LIGHT,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Shaman.HEAL_BOT_HEALING_WAVE,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                    act.Druid.HEAL_BOT_RIGHT_CLICK_NOURISH,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                    act.Priest.HEAL_BOT_POWER_WORD_SHIELD,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[
                    act.Priest.HEAL_BOT_POWER_WORD_SHIELD,
                ]
            ),
            SendLabel(
                name="",
                to=Config.SendLabelTo.all_tank(),
                actions=[
                    Key(name=keyname.KEY_2)
                ]
            ),
            SendLabel(
                name="",
                to=difference_list(
                    Config.SendLabelTo.all(),
                    Config.SendLabelTo.all_holy_pala,
                    Config.SendLabelTo.all_resto_shaman,
                    Config.SendLabelTo.all_resto_druid,
                    Config.SendLabelTo.all_disco_priest,
                    Config.SendLabelTo.all_holy_priest,
                    Config.SendLabelTo.all_tank(),
                ),
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key(name=keyname.KEY_2),
                ]
            )
        ],
        script=script,
    )

hk_healbot_big_heal = build_hk_healbot_big_heal()
