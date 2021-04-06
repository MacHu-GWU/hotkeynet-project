# -*- coding: utf-8 -*-

"""
实现按键 1-12 的功能.
"""

import typing

from ._config_and_script import config, script, Config
from .. import act
from ..constant.talent_category_association import (
    Talent, TalentCategory, get_talent_by_category,
)
from .... import keyname
from ....script import Hotkey, SendLabel, Key


def build_actions_default(config: Config,
                          is_healer_target_focus: bool,
                          key: Key) -> typing.List[SendLabel]:
    actions = list()

    for talent in get_talent_by_category(category=TalentCategory.tank):
        sl = SendLabel(
            name=talent.name,
            to=config.active_character_config.window_label_list_by_talent(t=talent),
            actions=[
                key,
            ]
        )
        actions.append(sl)

    for talent in get_talent_by_category(category=TalentCategory.dps):
        sl = SendLabel(
            name=talent.name,
            to=config.active_character_config.window_label_list_by_talent(t=talent),
            actions=[
                act.Target.TARGET_FOCUS_TARGET,
                key,
            ]
        )
        actions.append(sl)

    if is_healer_target_focus:
        _actions = [
            act.Target.TARGET_FOCUS,
            key,
        ]
    else:
        _actions = [
            key,
        ]
    for talent in get_talent_by_category(category=TalentCategory.healer):
        sl = SendLabel(
            name=talent.name,
            to=config.active_character_config.window_label_list_by_talent(t=talent),
            actions=_actions
        )
        actions.append(sl)
    return actions


def build_hk_1():
    actions = build_actions_default(
        config=config, is_healer_target_focus=True, key=Key(name=keyname.KEY_1))
    hk = Hotkey(
        name="Key1",
        key=keyname.SCROLOCK_ON(keyname.KEY_1),
        actions=actions,
        script=script,
    )
    hk.get_send_label_by_name(Talent.paladin_pve_holy.name).actions = [
        act.Target.TARGET_RAID,
        act.General.TRIGGER,
    ]
    return hk


hk_1 = build_hk_1()


def build_hk_2():
    actions = build_actions_default(
        config=config, is_healer_target_focus=False, key=Key(name=keyname.KEY_2))
    hk = Hotkey(
        name="Key2",
        key=keyname.SCROLOCK_ON(keyname.KEY_2),
        actions=actions,
        script=script,
    )
    hk.get_send_label_by_name(Talent.paladin_pve_holy.name).actions = [
        act.Target.TARGET_RAID,
        act.General.TRIGGER,
    ]
    return hk


hk_2 = build_hk_2()


def build_hk_3():
    actions = build_actions_default(
        config=config, is_healer_target_focus=True, key=Key(name=keyname.KEY_3))
    hk = Hotkey(
        name="Key3",
        key=keyname.SCROLOCK_ON(keyname.KEY_3),
        actions=actions,
        script=script,
    )
    hk.get_send_label_by_name(Talent.paladin_pve_holy.name).actions = [
        act.General.TRIGGER,
    ]
    return hk


hk_3 = build_hk_3()


def build_hk_4():
    actions = build_actions_default(
        config=config, is_healer_target_focus=False, key=Key(name=keyname.KEY_4))
    hk = Hotkey(
        name="Key4",
        key=keyname.SCROLOCK_ON(keyname.KEY_4),
        actions=actions,
        script=script,
    )
    return hk


hk_4 = build_hk_4()


def build_hk_5():
    actions = build_actions_default(
        config=config, is_healer_target_focus=False, key=Key(name=keyname.KEY_5))
    hk = Hotkey(
        name="Key5",
        key=keyname.SCROLOCK_ON(keyname.KEY_5),
        actions=actions,
        script=script,
    )
    hk.get_send_label_by_name(Talent.paladin_pve_holy.name).actions = [
        act.Target.TARGET_SELF,
        act.Paladin.HOLY_SPEC_KEY_5_HOLY_LIGHT,
    ]
    hk.get_send_label_by_name(Talent.shaman_pve_resto.name).actions = [
        act.Target.TARGET_SELF,
        act.Shaman.ALL_SPEC_CHAIN_HEAL,
    ]
    hk.get_send_label_by_name(Talent.druid_pve_resto.name).actions = [
        act.Target.TARGET_SELF,
        act.Druid.RESTO_SPEC_WILD_GROWTH_KEY_5,
    ]
    hk.get_send_label_by_name(Talent.priest_pve_disco.name).actions = [
        act.Priest.ALL_SPEC_PRAYER_OF_HEALING,
    ]
    hk.get_send_label_by_name(Talent.priest_pve_holy.name).actions = [
        act.Priest.ALL_SPEC_PRAYER_OF_HEALING,
    ]
    return hk


hk_5 = build_hk_5()


def build_hk_6_one_time_debuff():
    actions = build_actions_default(
        config=config, is_healer_target_focus=True, key=Key(name=keyname.KEY_6))
    hk = Hotkey(
        name="Key6",
        key=keyname.SCROLOCK_ON(keyname.KEY_6),
        actions=actions,
        script=script,
    )
    return hk


hk_6 = build_hk_6_one_time_debuff()


def build_hk_7():
    actions = build_actions_default(
        config=config, is_healer_target_focus=True, key=Key(name=keyname.KEY_7))
    hk = Hotkey(
        name="Key7",
        key=keyname.SCROLOCK_ON(keyname.KEY_7),
        actions=actions,
        script=script,
    )
    return hk


hk_7 = build_hk_7()


def build_hk_8_buff_self():
    return Hotkey(
        name="Key8",
        key=keyname.SCROLOCK_ON(keyname.KEY_8),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    Key(name=keyname.KEY_8)
                ]
            )
        ],
        script=script,
    )


hk_8_buff_self = build_hk_8_buff_self()


def build_hk_9_buff_raid():
    return Hotkey(
        name="Key9",
        key=keyname.SCROLOCK_ON(keyname.KEY_9),
        actions=[
            SendLabel(
                name="all",
                to=config.lbs_all(),
                actions=[
                    Key(name=keyname.KEY_9)
                ]
            )
        ],
        script=script,
    )


hk_9_buff_raid = build_hk_9_buff_raid()


def build_hk_0_short_term_buff():
    return Hotkey(
        name="Key0",
        key=keyname.SCROLOCK_ON(keyname.KEY_0),
        actions=[
            SendLabel(
                name=TalentCategory.dk.name,
                to=config.lbs_by_tc(TalentCategory.dk),
                actions=[
                    act.DK.ALL_SPEC_HORN_OF_WINTER_KEY_SHIFT_TAB,
                ]
            ),
            SendLabel(
                name=TalentCategory.paladin_healer.name,
                to=config.lbs_by_tc(TalentCategory.paladin_healer),
                actions=[
                    act.Target.TARGET_FOCUS,
                    act.Paladin.HOLY_SPEC_KEY_0_BEACON_OF_LIGHT,
                ]
            ),
            SendLabel(
                name=TalentCategory.shaman.name,
                to=config.lbs_by_tc(TalentCategory.shaman),
                actions=[
                    act.Shaman.ALL_SPEC_KEY_0_WATER_OR_LIGHTNING_SHIELD,
                ]
            ),
            SendLabel(
                name=TalentCategory.warlock.name,
                to=config.lbs_by_tc(TalentCategory.warlock),
                actions=[
                    act.Warlock.ALL_SPEC_FEL_ARMOR,
                ]
            ),
        ],
        script=script,
    )


hk_0_short_term_buff = build_hk_0_short_term_buff()


def build_hk_11_focus_mode_1():
    actions = list()
    for char in config.active_character_config.iter_by_window_index():
        if char.leader1_window_index:
            try:
                sl = SendLabel(
                    name=char.name,
                    to=[char.window_label, ],
                    actions=[
                        act.target_leader_key_mapper[char.leader1_window_label],
                        act.General.SET_FOCUS_KEY_NUMPAD_6,
                    ]
                )
                actions.append(sl)
            except KeyError:
                pass
        else:
            sl = SendLabel(
                name=char.name,
                to=[char.window_label, ],
                actions=[
                    act.General.CLEAR_FOCUS_NUMPAD_7,
                ]
            )
            actions.append(sl)

    return Hotkey(
        name="SetFocusMode1",
        key=keyname.SCROLOCK_ON(keyname.KEY_11_MINUS),
        actions=actions,
        script=script,
    )


hk_11_focus_mode_1 = build_hk_11_focus_mode_1()


def build_hk_12_focus_mode_2():
    actions = list()
    for char in config.active_character_config.iter_by_window_index():
        print(char.name, char.leader2_window_index)
        if char.leader2_window_index:
            try:
                sl = SendLabel(
                    name=char.name,
                    to=[char.window_label, ],
                    actions=[
                        act.target_leader_key_mapper[char.leader2_window_label],
                        act.General.SET_FOCUS_KEY_NUMPAD_6,
                    ]
                )
                actions.append(sl)
            except KeyError:
                pass
        else:
            sl = SendLabel(
                name=char.name,
                to=[char.window_label, ],
                actions=[
                    act.General.CLEAR_FOCUS_NUMPAD_7,
                ]
            )
            actions.append(sl)

    return Hotkey(
        name="SetFocusMode2",
        key=keyname.SCROLOCK_ON(keyname.KEY_12_PLUS),
        actions=actions,
        script=script,
    )


hk_12_focus_mode_2 = build_hk_12_focus_mode_2()
