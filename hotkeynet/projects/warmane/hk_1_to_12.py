# -*- coding: utf-8 -*-

"""

实现在多开模式下按键 1-12 的功能.

之所以为每一个快捷键创建一个工厂函数是为了能将注释放在函数的 docstr 里, 以便自动生成文档.

该如何给 1-12 (10 是 0, 11 是 minus, 12 是 plus) 按键分配技能.


首先有一个原则, 当你发 Hotkey 然后向窗口广播的时候, 我们希望由 Hotkey 发送的按键越少越好. 因为如果按键过多, 会导致更高的延时.

Hotkeynet 可以发送非常特殊的 Numpad Up, Down, Left, Right, 以及 End, Home, PgUp, PgDn, Clear, 这些对应着 Shift + Numpad1-9.
这些按键是无法作为快捷键在游戏中进行设置的, 但却能作为 Hotkeynet 的触发器. 换言之, 我们可以用 Shift + Numpad1-9 设置特殊的功能.

小键盘



"""

from . import act
from .config import Config, different_labels
from .script import script
from ... import keyname
from ...script import (
    Hotkey,
    Key, SendLabel,
)


def build_hk_1():
    """
    **功能**

    坦克职业照常按下 1, DPS 职业跟随焦点用一键循环输出宏打怪. 部分治疗职业给焦点坦克刷血,
    部分治疗职业刷团血.
    """
    return Hotkey(
        name="Key1",
        key=keyname.SCROLOCK_ON(keyname.KEY_1),
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
                    act.Paladin.HOLY_SPEC_ONE_MINUTE_HEAL_ROTATION_MACRO_KEY_1,
                ]
            ),
            # death knight
            SendLabel(
                name="all_unholy_tank_dk",
                to=Config.SendLabelTo.all_unholy_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_tank_dk",
                to=Config.SendLabelTo.all_blood_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_unholy_dps_dk",
                to=Config.SendLabelTo.all_unholy_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_dps_dk",
                to=Config.SendLabelTo.all_blood_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_dps_dk",
                to=Config.SendLabelTo.all_frost_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # hunter
            SendLabel(
                name="all_marksman_hunter",
                to=Config.SendLabelTo.all_marksman_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_survival_hunter",
                to=Config.SendLabelTo.all_survival_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_beast_hunter",
                to=Config.SendLabelTo.all_beast_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # shaman
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_enhancement_shaman",
                to=Config.SendLabelTo.all_enhancement_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_shaman",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Target.TARGET_FOCUS,
                    Key.trigger(),
                ]
            ),

            # druid
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_druid",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                    act.Target.TARGET_FOCUS,
                    act.Druid.RESTO_SPEC_HOT_HEAL_MACRO,
                ]
            ),

            # mage
            SendLabel(
                name="all_arcane_mage",
                to=Config.SendLabelTo.all_arcane_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_fire_mage",
                to=Config.SendLabelTo.all_fire_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_mage",
                to=Config.SendLabelTo.all_frost_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # warlock
            SendLabel(
                name="all_demonic_warlock",
                to=Config.SendLabelTo.all_demonic_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_affiliate_warlock",
                to=Config.SendLabelTo.all_affiliate_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_destruction_warlock",
                to=Config.SendLabelTo.all_destruction_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # priest
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_disco_priest",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                    act.Target.TARGET_FOCUS,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_holy_priest",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[
                    act.Target.TARGET_FOCUS,
                    Key.trigger(),
                ]
            ),
        ],
        script=script,
    )


hk_1 = build_hk_1()


def build_hk_2():
    """
    **功能**

    坦克职业照常按下 1, DPS 职业跟随焦点用一键循环输出宏打怪.
    治疗使用比较省蓝的团队随机治疗宏给团队治疗.
    """
    return Hotkey(
        name="Key2",
        key=keyname.SCROLOCK_ON(keyname.KEY_2),
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
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_tank_dk",
                to=Config.SendLabelTo.all_blood_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_unholy_dps_dk",
                to=Config.SendLabelTo.all_unholy_dps_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_dps_dk",
                to=Config.SendLabelTo.all_blood_dps_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_dps_dk",
                to=Config.SendLabelTo.all_frost_dps_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            # hunter
            SendLabel(
                name="all_marksman_hunter",
                to=Config.SendLabelTo.all_marksman_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_survival_hunter",
                to=Config.SendLabelTo.all_survival_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_beast_hunter",
                to=Config.SendLabelTo.all_beast_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # shaman
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_shaman",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    Key.trigger(),
                ]
            ),
            # druid
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
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
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_fire_mage",
                to=Config.SendLabelTo.all_fire_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_mage",
                to=Config.SendLabelTo.all_frost_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # warlock
            SendLabel(
                name="all_demonic_warlock",
                to=Config.SendLabelTo.all_demonic_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_affiliate_warlock",
                to=Config.SendLabelTo.all_affiliate_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_destruction_warlock",
                to=Config.SendLabelTo.all_destruction_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # priest
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
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


hk_2 = build_hk_2()


def build_hk_3():
    """

    :return:
    """
    return Hotkey(
        name="Key3",
        key=keyname.SCROLOCK_ON(keyname.KEY_3),
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
                    act.Paladin.HOLY_SPEC_PERIODICAL_BEACON_OF_LIGHT_ON_FOCUS_MACRO,
                ]
            ),
            # death knight
            SendLabel(
                name="all_unholy_tank_dk",
                to=Config.SendLabelTo.all_unholy_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_tank_dk",
                to=Config.SendLabelTo.all_blood_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_unholy_dps_dk",
                to=Config.SendLabelTo.all_unholy_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_dps_dk",
                to=Config.SendLabelTo.all_blood_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_dps_dk",
                to=Config.SendLabelTo.all_frost_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # hunter
            SendLabel(
                name="all_marksman_hunter",
                to=Config.SendLabelTo.all_marksman_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_survival_hunter",
                to=Config.SendLabelTo.all_survival_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_beast_hunter",
                to=Config.SendLabelTo.all_beast_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # shaman
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_enhancement_shaman",
                to=Config.SendLabelTo.all_enhancement_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_shaman",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Target.TARGET_FOCUS,
                    act.Shaman.RESTO_SPEC_HEALING_WAVE_KEY_7,
                ]
            ),
            # druid
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_druid",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                    act.Target.TARGET_FOCUS,
                    act.Druid.RESTO_SPEC_NOURISH_KEY_3,
                ]
            ),

            # mage
            SendLabel(
                name="all_arcane_mage",
                to=Config.SendLabelTo.all_arcane_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_fire_mage",
                to=Config.SendLabelTo.all_fire_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_mage",
                to=Config.SendLabelTo.all_frost_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # warlock
            SendLabel(
                name="all_demonic_warlock",
                to=Config.SendLabelTo.all_demonic_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_affiliate_warlock",
                to=Config.SendLabelTo.all_affiliate_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_destruction_warlock",
                to=Config.SendLabelTo.all_destruction_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # priest
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_disco_priest",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                ]
            ),
            SendLabel(
                name="all_holy_priest",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[

                ]
            ),
        ],
        script=script,
    )


hk_3 = build_hk_3()


def build_hk_4():
    return Hotkey(
        name="Key4",
        key=keyname.SCROLOCK_ON(keyname.KEY_4),
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
                    act.Target.TARGET_FOCUS,
                    act.Paladin.HOLY_SPEC_PERIODICAL_JUDGEMENT_OF_LIGHT_ON_FOCUS_TARGET,
                ]
            ),
            # death knight
            SendLabel(
                name="all_unholy_tank_dk",
                to=Config.SendLabelTo.all_unholy_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_tank_dk",
                to=Config.SendLabelTo.all_blood_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_unholy_dps_dk",
                to=Config.SendLabelTo.all_unholy_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_dps_dk",
                to=Config.SendLabelTo.all_blood_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_dps_dk",
                to=Config.SendLabelTo.all_frost_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # hunter
            SendLabel(
                name="all_marksman_hunter",
                to=Config.SendLabelTo.all_marksman_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_survival_hunter",
                to=Config.SendLabelTo.all_survival_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_beast_hunter",
                to=Config.SendLabelTo.all_beast_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # shaman
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_enhancement_shaman",
                to=Config.SendLabelTo.all_enhancement_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_shaman",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # druid
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_druid",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                    Key.trigger(),
                ]
            ),

            # mage
            SendLabel(
                name="all_arcane_mage",
                to=Config.SendLabelTo.all_arcane_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_fire_mage",
                to=Config.SendLabelTo.all_fire_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_mage",
                to=Config.SendLabelTo.all_frost_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # warlock
            SendLabel(
                name="all_demonic_warlock",
                to=Config.SendLabelTo.all_demonic_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_affiliate_warlock",
                to=Config.SendLabelTo.all_affiliate_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_destruction_warlock",
                to=Config.SendLabelTo.all_destruction_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # priest
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_disco_priest",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                ]
            ),
            SendLabel(
                name="all_holy_priest",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[
                ]
            ),
        ],
        script=script,
    )


hk_4 = build_hk_4()


def build_hk_5():
    return Hotkey(
        name="Key5",
        key=keyname.SCROLOCK_ON(keyname.KEY_5),
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
                    act.Target.TARGET_SELF,
                    act.Paladin.HOLY_SPEC_HOLY_LIGHT_KEY_5,
                ]
            ),
            # death knight
            SendLabel(
                name="all_unholy_tank_dk",
                to=Config.SendLabelTo.all_unholy_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_tank_dk",
                to=Config.SendLabelTo.all_blood_tank_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_unholy_dps_dk",
                to=Config.SendLabelTo.all_unholy_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_dps_dk",
                to=Config.SendLabelTo.all_blood_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_dps_dk",
                to=Config.SendLabelTo.all_frost_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # hunter
            SendLabel(
                name="all_marksman_hunter",
                to=Config.SendLabelTo.all_marksman_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_survival_hunter",
                to=Config.SendLabelTo.all_survival_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_beast_hunter",
                to=Config.SendLabelTo.all_beast_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # shaman
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.Target.TARGET_SELF,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_enhancement_shaman",
                to=Config.SendLabelTo.all_enhancement_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_shaman",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Target.TARGET_SELF,
                    act.Shaman.ALL_SPEC_CHAIN_HEAL,
                ]
            ),
            # druid
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_druid",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                    act.Target.TARGET_SELF,
                    act.Druid.RESTO_SPEC_WILD_GROWTH_KEY_5,
                ]
            ),
            # mage
            SendLabel(
                name="all_arcane_mage",
                to=Config.SendLabelTo.all_arcane_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_fire_mage",
                to=Config.SendLabelTo.all_fire_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_mage",
                to=Config.SendLabelTo.all_frost_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # warlock
            SendLabel(
                name="all_demonic_warlock",
                to=Config.SendLabelTo.all_demonic_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_affiliate_warlock",
                to=Config.SendLabelTo.all_affiliate_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_destruction_warlock",
                to=Config.SendLabelTo.all_destruction_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # priest
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.Target.TARGET_SELF,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_disco_priest",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                    act.Priest.ALL_SPEC_PRAYER_OF_HEALING,
                ]
            ),
            SendLabel(
                name="all_holy_priest",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[
                    act.Priest.HOLY_SPEC_CIRCLE_OF_HEALING,
                ]
            ),
        ],
        script=script,
    )

hk_5 = build_hk_5()


def build_hk_6_one_time_debuff():
    return Hotkey(
        name="Key6",
        key=keyname.SCROLOCK_ON(keyname.KEY_6),
        actions=[
            # paladin
            SendLabel(
                name="all_protect_pala",
                to=Config.SendLabelTo.all_protect_pala,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_holy_pala",
                to=Config.SendLabelTo.all_holy_pala,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Paladin.HOLY_SPEC_FLASH_OF_LIGHT_KEY_6,
                ]
            ),
            # death knight
            SendLabel(
                name="all_unholy_tank_dk",
                to=Config.SendLabelTo.all_unholy_tank_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_tank_dk",
                to=Config.SendLabelTo.all_blood_tank_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_unholy_dps_dk",
                to=Config.SendLabelTo.all_unholy_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_dps_dk",
                to=Config.SendLabelTo.all_blood_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_dps_dk",
                to=Config.SendLabelTo.all_frost_dps_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # hunter
            SendLabel(
                name="all_marksman_hunter",
                to=Config.SendLabelTo.all_marksman_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_survival_hunter",
                to=Config.SendLabelTo.all_survival_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_beast_hunter",
                to=Config.SendLabelTo.all_beast_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            # shaman
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.Target.TARGET_SELF,
                    act.Shaman.ELEMENTAL_SPEC_DPS_ROTATE_MACRO,
                ]
            ),
            SendLabel(
                name="all_enhancement_shaman",
                to=Config.SendLabelTo.all_enhancement_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Shaman.ENHANCEMENT_SPEC_DPS_ROTATE_MACRO,
                ]
            ),
            SendLabel(
                name="all_resto_shaman",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Shaman.RESTO_SPEC_LESS_HEALING_WAVE_KEY_6,
                ]
            ),
            # druid
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_resto_druid",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Druid.RESTO_SPEC_REJUVENATION_KEY_6,
                ]
            ),
            # mage
            SendLabel(
                name="all_arcane_mage",
                to=Config.SendLabelTo.all_arcane_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Mage.ARCANE_SPEC_DPS_ROTATE_MACRO,
                ]
            ),
            SendLabel(
                name="all_fire_mage",
                to=Config.SendLabelTo.all_fire_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Mage.FIRE_SPEC_DPS_ROTATE_MACRO,
                ]
            ),
            SendLabel(
                name="all_frost_mage",
                to=Config.SendLabelTo.all_frost_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Mage.FROST_SPEC_DPS_ROTATE_MACRO,
                ]
            ),
            # warlock
            SendLabel(
                name="all_demonic_warlock",
                to=Config.SendLabelTo.all_demonic_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_affiliate_warlock",
                to=Config.SendLabelTo.all_affiliate_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Warlock.ALL_SPEC_CURSE_OF_ELEMENT,
                ]
            ),
            SendLabel(
                name="all_destruction_warlock",
                to=Config.SendLabelTo.all_destruction_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Warlock.ALL_SPEC_CURSE_OF_ELEMENT,
                ]
            ),
            # priest
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_disco_priest",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                    act.Priest.ALL_SPEC_PRAYER_OF_HEALING,
                ]
            ),
            SendLabel(
                name="all_holy_priest",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[
                    act.Priest.HOLY_SPEC_CIRCLE_OF_HEALING,
                ]
            ),
        ],
        script=script,
    )


hk_6 = build_hk_6_one_time_debuff()


def build_hk_7():
    """
    **功能**:

    让治疗职业使用 能够瞬间救活一个人的治疗法术 治疗焦点坦克的目标.
    而其他 Tank Dps 职业选中焦点坦克的目标即可, 不做任何动作.

    **应用场景**:

    1. 当 Boss 有攻击反伤, 或是攻击的伤害转嫁到团队成员身上的技能时, 焦点选中受伤
        目标按此键能保证被反伤或是转嫁的人不会死亡.
    2. 需要紧急治疗一个人的时候. 但推荐使用 healbot 的鼠标按键.
    """
    return Hotkey(
        name="Key7",
        key=keyname.SCROLOCK_ON(keyname.KEY_7),
        actions=[
            # paladin
            SendLabel(
                name="all_protect_pala",
                to=Config.SendLabelTo.all_protect_pala,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_holy_pala",
                to=Config.SendLabelTo.all_holy_pala,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Paladin.HOLY_SPEC_HOLY_LIGHT_KEY_7,
                ]
            ),
            # death knight
            SendLabel(
                name="all_unholy_tank_dk",
                to=Config.SendLabelTo.all_unholy_tank_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_tank_dk",
                to=Config.SendLabelTo.all_blood_tank_dk,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_unholy_dps_dk",
                to=Config.SendLabelTo.all_unholy_dps_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_blood_dps_dk",
                to=Config.SendLabelTo.all_blood_dps_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            SendLabel(
                name="all_frost_dps_dk",
                to=Config.SendLabelTo.all_frost_dps_dk,
                actions=[
                    Key.trigger(),
                ]
            ),
            # hunter
            SendLabel(
                name="all_marksman_hunter",
                to=Config.SendLabelTo.all_marksman_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_survival_hunter",
                to=Config.SendLabelTo.all_survival_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_beast_hunter",
                to=Config.SendLabelTo.all_beast_hunter,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            # shaman
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_enhancement_shaman",
                to=Config.SendLabelTo.all_enhancement_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Shaman.ENHANCEMENT_SPEC_DPS_ROTATE_MACRO,
                ]
            ),
            SendLabel(
                name="all_resto_shaman",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Shaman.RESTO_SPEC_HEALING_WAVE_KEY_7,
                ]
            ),
            # druid
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_resto_druid",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Druid.RESTO_SPEC_NOURISH_KEY_7,
                ]
            ),
            # mage
            SendLabel(
                name="all_arcane_mage",
                to=Config.SendLabelTo.all_arcane_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_fire_mage",
                to=Config.SendLabelTo.all_fire_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_frost_mage",
                to=Config.SendLabelTo.all_frost_mage,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            # warlock
            SendLabel(
                name="all_demonic_warlock",
                to=Config.SendLabelTo.all_demonic_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_affiliate_warlock",
                to=Config.SendLabelTo.all_affiliate_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_destruction_warlock",
                to=Config.SendLabelTo.all_destruction_warlock,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            # priest
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                ]
            ),
            SendLabel(
                name="all_disco_priest",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Priest.ALL_SPEC_POWER_WORLD_SHIELD,
                ]
            ),
            SendLabel(
                name="all_holy_priest",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Priest.ALL_SPEC_FLASH_HEAL,
                ]
            ),
        ],
        script=script,
    )


hk_7 = build_hk_7()


def build_hk_8_self_buff():
    """
    所有人刷自己的个人Buff
    """
    return Hotkey(
        name="Key8",
        key=keyname.SCROLOCK_ON(keyname.KEY_8),
        actions=[
            SendLabel(
                name="all",
                to=Config.SendLabelTo.all(),
                actions=[
                    act.General.BUFF_SELF_MACRO,
                ]
            )
        ],
        script=script,
    )

hk_8 = build_hk_8_self_buff()


def build_hk_9_raid_buff():
    """
    所有人刷团队 Buff
    """
    return Hotkey(
        name="Key9",
        key=keyname.SCROLOCK_ON(keyname.KEY_9),
        actions=[
            SendLabel(
                name="all",
                to=Config.SendLabelTo.all(),
                actions=[
                    act.General.BUFF_RAID_MACRO,
                ]
            )
        ],
        script=script,
    )

hk_9 = build_hk_9_raid_buff()


def build_hk_10():
    return Hotkey(
        name="Key0",
        key=keyname.SCROLOCK_ON(keyname.KEY_0),
        actions=[
            # paladin
            SendLabel(
                name="all_protect_pala",
                to=Config.SendLabelTo.all_protect_pala,
                actions=[
                    act.Paladin.ALL_SPEC_SACRED_SHIELD
                ]
            ),
            SendLabel(
                name="all_holy_pala",
                to=Config.SendLabelTo.all_holy_pala,
                actions=[
                    act.Target.TARGET_FOCUS,
                    act.Paladin.HOLY_SPEC_BEACON_OF_LIGHT,
                ]
            ),
            # death knight
            SendLabel(
                name="all_unholy_tank_dk",
                to=Config.SendLabelTo.all_unholy_tank_dk,
                actions=[
                    act.DK.ALL_SPEC_HORN_OF_WINTER,
                ]
            ),
            SendLabel(
                name="all_blood_tank_dk",
                to=Config.SendLabelTo.all_blood_tank_dk,
                actions=[
                    act.DK.ALL_SPEC_HORN_OF_WINTER,
                ]
            ),
            # hunter
            SendLabel(
                name="all_marksman_hunter",
                to=Config.SendLabelTo.all_marksman_hunter,
                actions=[
                ]
            ),
            SendLabel(
                name="all_survival_hunter",
                to=Config.SendLabelTo.all_survival_hunter,
                actions=[
                ]
            ),
            SendLabel(
                name="all_beast_hunter",
                to=Config.SendLabelTo.all_beast_hunter,
                actions=[
                ]
            ),
            # shaman
            SendLabel(
                name="all_elemental_shaman",
                to=Config.SendLabelTo.all_elemental_shaman,
                actions=[
                    act.Shaman.ALL_SPEC_WATER_SHELD,
                ]
            ),
            SendLabel(
                name="all_enhancement_shaman",
                to=Config.SendLabelTo.all_enhancement_shaman,
                actions=[
                    act.Shaman.ALL_SPEC_LIGHTNING_SHIELD,
                ]
            ),
            SendLabel(
                name="all_resto_shaman",
                to=Config.SendLabelTo.all_resto_shaman,
                actions=[
                    act.Shaman.ALL_SPEC_WATER_SHELD,
                ]
            ),
            # druid
            SendLabel(
                name="all_boomkin_druid",
                to=Config.SendLabelTo.all_boomkin_druid,
                actions=[
                ]
            ),
            SendLabel(
                name="all_resto_druid",
                to=Config.SendLabelTo.all_resto_druid,
                actions=[
                ]
            ),
            # mage
            SendLabel(
                name="all_arcane_mage",
                to=Config.SendLabelTo.all_arcane_mage,
                actions=[
                ]
            ),
            SendLabel(
                name="all_fire_mage",
                to=Config.SendLabelTo.all_fire_mage,
                actions=[
                ]
            ),
            SendLabel(
                name="all_frost_mage",
                to=Config.SendLabelTo.all_frost_mage,
                actions=[
                ]
            ),
            # warlock
            SendLabel(
                name="all_demonic_warlock",
                to=Config.SendLabelTo.all_demonic_warlock,
                actions=[
                    act.Warlock.ALL_SPEC_FEL_ARMOR,
                ]
            ),
            SendLabel(
                name="all_affiliate_warlock",
                to=Config.SendLabelTo.all_affiliate_warlock,
                actions=[
                    act.Warlock.ALL_SPEC_FEL_ARMOR,
                ]
            ),
            SendLabel(
                name="all_destruction_warlock",
                to=Config.SendLabelTo.all_destruction_warlock,
                actions=[
                    act.Warlock.ALL_SPEC_FEL_ARMOR,
                ]
            ),
            # priest
            SendLabel(
                name="all_shadow_priest",
                to=Config.SendLabelTo.all_shadow_priest,
                actions=[
                    act.Priest.ALL_SPEC_INNER_FIRE,
                ]
            ),
            SendLabel(
                name="all_disco_priest",
                to=Config.SendLabelTo.all_disco_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Priest.ALL_SPEC_INNER_FIRE,
                ]
            ),
            SendLabel(
                name="all_holy_priest",
                to=Config.SendLabelTo.all_holy_priest,
                actions=[
                    act.Target.TARGET_FOCUS_TARGET,
                    act.Priest.ALL_SPEC_INNER_FIRE,
                ]
            ),
        ],
        script=script,
    )

hk_10 = build_hk_10()


def build_hk_11():
    return Hotkey(
        name="SetFocusMode1",
        key=keyname.SCROLOCK_ON(keyname.KEY_11_MINUS),
        actions=[
            SendLabel(
                name="non_leader_1",
                to=Config.SendLabelTo.non_leader_1(),
                actions=[
                    act.Target.TARGET_LEADER_1,
                    act.Target.SET_TARGET_AS_FOCUS,
                ]
            ),
            SendLabel(
                name="leader_1",
                to=Config.SendLabelTo.leader_1,
                actions=[
                    act.General.CLEAR_FOCUS,
                ]
            )
        ],
        script=script,
    )

hk_11 = build_hk_11()


def build_hk_12():
    return Hotkey(
        name="SetFocusMode2",
        key=keyname.SCROLOCK_ON(keyname.KEY_12_PLUS),
        actions=[
            SendLabel(
                name="non_leader_2",
                to=Config.SendLabelTo.non_leader_2(),
                actions=[
                    act.Target.TARGET_LEADER_2,
                    act.Target.SET_TARGET_AS_FOCUS,
                ]
            ),
            SendLabel(
                name="leader_2",
                to=Config.SendLabelTo.leader_2,
                actions=[
                    act.General.CLEAR_FOCUS,
                ]
            )
        ],
        script=script,
    )

hk_12 = build_hk_12()
