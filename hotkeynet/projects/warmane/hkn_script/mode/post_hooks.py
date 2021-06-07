# -*- coding: utf-8 -*-

import typing
from ...config import Config
from ...constant.characters import CharacterFactory
from .....script import Script, Action, SendLabel, SendFocusWindow
from ...constant.talent_category_association import TC
from ...constant.windows import window_index
from ... import act


send_focus_window_trigger = SendFocusWindow(
    name="",
    actions=[
        act.General.TRIGGER,
    ]
)

def _has_send_focus_window(actions: typing.List[Action]) -> bool:
    """
    Identify whether there is a ``SendFocusWindow`` in actions.
    :param actions:
    :return:
    """
    for act in actions:
        if isinstance(act, SendFocusWindow):
            return True
    return False


def _add_send_focus_window_if_not_available(actions: typing.List[Action]) -> bool:
    if _has_send_focus_window(actions):
        return False
    else:
        actions.append(send_focus_window_trigger)
        return True


def litgoatdk_abcde_team_death_grip(config: 'Config', script: Script):

    from .. import hk_g07_skills

    # if config.active_character_config.is_char_exists(CharacterFactory.make_char_fatmulti1_litgoatdka_pve_blood_dk()):
    hk_g07_skills.hk_g.actions.append(
        SendLabel(
            name=TC.dk.name,
            to=config.lbs_by_tc(TC.dk),
            actions=[
                act.DK.ALL_SPEC_DEATH_GRIP_KEY_G,
            ]
        )
    )

    from ..hk_g08_alt_numpad_1_to_12 import hk_alt_numpad_1, hk_alt_numpad_2, hk_alt_numpad_3

    if config.active_character_config.is_char_exists(CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk()):
        hk_alt_numpad_1.actions.append(
            SendLabel(
                name="dk2",
                to=[CharacterFactory.make_char_fatmulti2_litgoatdkb_pvp_frost_dk().window_label, ],
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.DK.ALL_SPEC_DEATH_GRIP_KEY_G,
                ]
            )
        )

    if config.active_character_config.is_char_exists(CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk()):
        hk_alt_numpad_2.actions.append(
            SendLabel(
                name="dk3",
                to=[CharacterFactory.make_char_fatmulti3_litgoatdkc_pvp_frost_dk().window_label, ],
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.DK.ALL_SPEC_DEATH_GRIP_KEY_G,
                ]
            )
        )

    if config.active_character_config.is_char_exists(CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk()):
        hk_alt_numpad_3.actions.append(
            SendLabel(
                name="dk4",
                to=[CharacterFactory.make_char_fatmulti4_litgoatdkd_pvp_frost_dk().window_label, ],
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.DK.ALL_SPEC_DEATH_GRIP_KEY_G,
                ]
            )
        )

def boomkin_round_robin_starfall(config: 'Config', script: Script):
    from ..hk_g08_alt_numpad_1_to_12 import hk_alt_numpad_1, hk_alt_numpad_2, hk_alt_numpad_3
    from ..hk_g09_ctrl_numpad_1_to_12 import hk_ctrl_numpad_1, hk_ctrl_numpad_2, hk_ctrl_numpad_3

    hk_alt_numpad_1.actions.append(
        SendLabel(
            name="balance druid 1",
            to=[window_index[11].label, ],
            actions=[
                act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F
            ]
        )
    )

    hk_alt_numpad_2.actions.append(
        SendLabel(
            name="balance druid 2",
            to=[window_index[12].label, ],
            actions=[
                act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F
            ]
        )
    )

    hk_alt_numpad_3.actions.append(
        SendLabel(
            name="balance druid 3",
            to=[window_index[13].label, ],
            actions=[
                act.Druid.BALANCE_SPEC_STAR_FALL_ALT_F
            ]
        )
    )

    hk_ctrl_numpad_1.actions.append(
        SendLabel(
            name="balance druid 1",
            to=[window_index[11].label, ],
            actions=[
                act.Druid.BALANCE_SPEC_TYPHOON_KEY_G
            ]
        )
    )

    hk_ctrl_numpad_2.actions.append(
        SendLabel(
            name="balance druid 1",
            to=[window_index[12].label, ],
            actions=[
                act.Druid.BALANCE_SPEC_TYPHOON_KEY_G
            ]
        )
    )

    hk_ctrl_numpad_3.actions.append(
        SendLabel(
            name="balance druid 1",
            to=[window_index[13].label, ],
            actions=[
                act.Druid.BALANCE_SPEC_TYPHOON_KEY_G
            ]
        )
    )


def druid_all_stealth(config: 'Config', script: Script):
    from .. import hk_g07_skills

    hk_g07_skills.hk_alt_f1.actions = [
        SendLabel(
            name=TC.druid.name,
            to=config.lbs_by_tc(tc=TC.druid),
            actions=[
                act.Druid.ALL_SPEC_CAT_STEALTH_MACRO,
            ]
        )
    ]


def lgms_ijkl_shadow_priest_group(config: 'Config', script: Script):
    from .. import hk_g07_skills

    hk_g07_skills.hk_g.actions.append(
        SendLabel(
            name=TC.priest.name,
            to=config.lbs_by_tc(tc=TC.priest),
            actions=[
                act.Priest.ALL_SPEC_HOLY_NOVA,
            ]
        )
    )


def resto_shaman_earth_shield(config: 'Config', script: Script):
    from ..hk_g07_skills import hk_z

    hk_z.actions.append(
        SendLabel(
            name=TC.shaman_resto.name,
            to=config.lbs_by_tc(tc=TC.shaman_resto)[:1],
            actions=[
                act.Target.TARGET_FOCUS,
                act.Shaman.RESTO_SPEC_EARTH_SHIELD,
            ]
        )
    )

    _add_send_focus_window_if_not_available(hk_z.actions)
