# -*- coding: utf-8 -*-

"""
实现由在主控角色界面下, 用鼠标在团队框架上进行单机来实现治疗的快捷键.
需要配合团队框架 Healbot 使用.
"""

from ._config_and_script import config, script
from .. import act
from ....utils import difference_list
from ..constant.talent_category_association import TC
from .... import keyname
from ....script import (
    Hotkey,
    Key, SendLabel,
)


def _build_send_label_holy_paladin(actions):
    return SendLabel(
        name=TC.paladin_holy.name, to=config.lbs_by_tc(TC.paladin_holy),
        actions=actions,
    )


def _build_send_label_resto_shaman(actions):
    return SendLabel(
        name=TC.shaman_resto.name, to=config.lbs_by_tc(TC.shaman_resto),
        actions=actions,
    )

def _build_send_label_dps_shaman(actions):
    return SendLabel(
        name=TC.shaman_non_resto.name, to=config.lbs_by_tc(TC.shaman_non_resto),
        actions=actions,
    )


def _build_send_label_resto_druid(actions):
    return SendLabel(
        name=TC.druid_resto.name, to=config.lbs_by_tc(TC.druid_resto),
        actions=actions,
    )


def _build_send_label_disco_priest(actions):
    return SendLabel(
        name=TC.priest_disco.name, to=config.lbs_by_tc(TC.priest_disco),
        actions=actions,
    )


def _build_send_label_holy_priest(actions):
    return SendLabel(
        name=TC.priest_holy.name, to=config.lbs_by_tc(TC.priest_holy),
        actions=actions,
    )


def _build_send_label_tank():
    return SendLabel(
        name=TC.tank.name, to=config.lbs_by_tc(TC.tank),
        actions=[
            Key(name=keyname.KEY_2)
        ]
    )


def _build_send_label_dps():
    return SendLabel(
        name=TC.dps.name,
        to=difference_list(config.lbs_by_tc(TC.dps), config.lbs_by_tc(TC.shaman_non_resto)),
        actions=[
            act.Target.TARGET_FOCUS_TARGET,
            Key(name=keyname.KEY_2)
        ]
    )


def build_hk_healbot_small_heal():
    return Hotkey(
        name="Healbot Small Heal",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.MOUSE_LButton)),
        actions=[
            _build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_RIGHT_CLICK_FLASH_OF_LIGHT,
            ]),
            _build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_RIPTIDE_RIGHT_CLICK,
            ]),
            _build_send_label_resto_druid([
                act.Druid.HEAL_BOT_LEFT_CLICK_REJUVENATION,
            ]),
            _build_send_label_disco_priest([
                act.Priest.HEAL_BOT_POWER_WORD_SHIELD,
            ]),
            _build_send_label_holy_priest([
                act.Priest.HEAL_BOT_HOLY_SPEC_FLASH_HEAL,
            ]),
            _build_send_label_tank(),
            _build_send_label_dps(),
        ],
        script=script,
    )


hk_healbot_small_heal = build_hk_healbot_small_heal()


def build_hk_healbot_big_heal():
    return Hotkey(
        name="Healbot Big Heal",
        key=keyname.SCROLOCK_ON(keyname.CTRL_(keyname.MOUSE_RButton)),
        actions=[
            _build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_LEFT_CLICK_HOLY_LIGHT,
            ]),
            _build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_HEALING_WAVE_LEFT_CLICK,
            ]),
            _build_send_label_resto_druid([
                act.Druid.HEAL_BOT_RIGHT_CLICK_NOURISH,
            ]),
            _build_send_label_disco_priest([
                act.Priest.HEAL_BOT_POWER_WORD_SHIELD,
            ]),
            _build_send_label_holy_priest([
                act.Priest.HEAL_BOT_HOLY_SPEC_FLASH_HEAL,
            ]),
            _build_send_label_tank(),
            _build_send_label_dps(),
        ],
        script=script,
    )


hk_healbot_big_heal = build_hk_healbot_big_heal()


def build_hk_healbot_aoe_heal():
    return Hotkey(
        name="Healbot Aoe Heal",
        key=keyname.SCROLOCK_ON(keyname.SHIFT_(keyname.MOUSE_LButton)),
        actions=[
            _build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_LEFT_CLICK_HOLY_LIGHT,
            ]),
            _build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_CHAIN_HEAL_MIDDLE_CLICK,
            ]),
            _build_send_label_dps_shaman([
                act.Shaman.HEAL_BOT_CHAIN_HEAL_MIDDLE_CLICK,
            ]),
            _build_send_label_resto_druid([
                act.Druid.HEAL_BOT_WILD_GROWTH,
            ]),
            _build_send_label_disco_priest([
                act.Priest.HEAL_BOT_POWER_WORD_SHIELD,
            ]),
            _build_send_label_holy_priest([
                act.Priest.HEAL_BOT_CIRCLE_OF_HEALING,
            ]),
            # _build_send_label_tank(),
            # _build_send_label_dps(),
        ],
        script=script,
    )


hk_healbot_aoe_heal = build_hk_healbot_aoe_heal()


def build_hk_healbot_dispel():
    return Hotkey(
        name="Healbot Dispel",
        key=keyname.SCROLOCK_ON(keyname.MOUSE_MButton),
        actions=[
            _build_send_label_holy_paladin([
                act.Paladin.HEAL_BOT_CLEANSE,
            ]),
            _build_send_label_resto_shaman([
                act.Shaman.HEAL_BOT_CLEANSE_CTRL_LEFT_CLICK,
            ]),
            _build_send_label_resto_druid([
                act.Druid.HEAL_BOT_REMOVE_CURSE,
            ]),
            _build_send_label_disco_priest([
                act.Priest.HEAL_BOT_DISPEL_MAGIC,
            ]),
            _build_send_label_holy_priest([
                act.Priest.HEAL_BOT_DISPEL_MAGIC,
            ]),
        ],
        script=script,
    )


hk_healbot_dispel = build_hk_healbot_dispel()
